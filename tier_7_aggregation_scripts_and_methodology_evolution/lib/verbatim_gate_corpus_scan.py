#!/usr/bin/env python3
"""verbatim_gate_corpus_scan.py — run verbatim_quote_gate over many folders.

Aggregates the per-quote verdicts into a corpus-level confabulation-rate report:
per-paper counts + a global roll-up + the full list of FAIL/WARN quotes (the
candidate confabulations) for §H registration.

Usage:
    python3 scripts/verbatim_gate_corpus_scan.py --version v19 --dirs-file scratchpad/v19_dirs.txt
    python3 scripts/verbatim_gate_corpus_scan.py --version v19 papers/dev/kumada papers/dev/murai
"""
from __future__ import annotations
import argparse
import importlib.util
import json
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
spec = importlib.util.spec_from_file_location("vqg", os.path.join(HERE, "verbatim_quote_gate.py"))
vqg = importlib.util.module_from_spec(spec)
spec.loader.exec_module(vqg)  # type: ignore


# Supplementary PDFs travel under many names. The original "_si" test missed
# ja017559z_s1.pdf and 41467_2021_22715_MOESM1_ESM.pdf, which then sorted ahead of
# the article and became the reference document -- so every quote from those
# directories FAILed against an SI. Both the pattern and the "first PDF only"
# habit are fixed here; see the S2-1b audit report.
SI_NAME = re.compile(r"(_si\b|_si\d|_si_|_s\d+$|moesm|_esm\b|supp)", re.I)


def scan_dir(pdir: str, version: str | None, stages: list[str]):
    import glob

    def split_pdfs(d):
        allp = sorted(glob.glob(f"{d}/*.pdf"))
        main = [p for p in allp if not SI_NAME.search(os.path.splitext(os.path.basename(p))[0])]
        si = [p for p in allp if SI_NAME.search(os.path.splitext(os.path.basename(p))[0])]
        return main, si

    pdfs, sis = split_pdfs(pdir)
    if not pdfs:
        pdfs, sis = split_pdfs(os.path.dirname(pdir))
    if not pdfs:
        return None
    # every article PDF, not just pdfs[0]: errata and multi-part articles are
    # part of the paper's text and a quote may legitimately come from any of them
    main_ref = vqg.normalize(" ".join(vqg.extract_pdf_text(p) for p in pdfs))
    ref_chars = len(main_ref)
    refs = {"main": main_ref}
    if sis:
        refs["si"] = vqg.normalize(" ".join(vqg.extract_pdf_text(p) for p in sis))
    # a machine-readable paper yields thousands of chars; <2000 means the PDF is
    # scanned/image-only and the gate CANNOT verify quotes against it.
    ref_ok = ref_chars >= 2000

    out_files = []
    for st in stages:
        out_files += sorted(glob.glob(f"{pdir}/*_{st}.md"))
    if version:
        out_files = [f for f in out_files if f"_{version}_" in os.path.basename(f)]
    out_files = list(dict.fromkeys(out_files))
    if not out_files:
        return None

    results = []
    for f in out_files:
        for raw, kind in vqg.harvest_quotes(f):
            nq = vqg.normalize(raw)
            status, src, pr, ts = vqg.score_quote(nq, refs)
            import re
            prov = bool(re.search(r"1\s*,\s*3\s*-\s*bd", raw.lower()))
            results.append({"file": os.path.basename(f), "kind": kind,
                            "status": status, "src": src, "partial": round(pr, 1),
                            "token_set": round(ts, 1), "prov_1_3_bd": prov,
                            "quote": raw[:240]})
    counts = {k: 0 for k in ("FAIL", "WARN", "PASS_FUZZY", "PASS")}
    for r in results:
        counts[r["status"]] = counts.get(r["status"], 0) + 1   # the gate added PASS_SPLICED later
    return {"dir": pdir, "pdf": os.path.basename(pdfs[0]),
            "ref_chars": ref_chars, "ref_ok": ref_ok,
            "n_files": len(out_files), "counts": counts, "results": results}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("dirs", nargs="*")
    ap.add_argument("--dirs-file", default=None)
    ap.add_argument("--version", default=None)
    ap.add_argument("--stages", default="s0,s1,s2")
    ap.add_argument("--json", default=None)
    args = ap.parse_args()

    dirs = list(args.dirs)
    if args.dirs_file:
        with open(args.dirs_file) as fh:
            dirs += [ln.strip() for ln in fh if ln.strip()]
    dirs = list(dict.fromkeys(dirs))
    stages = [s.strip() for s in args.stages.split(",") if s.strip()]

    scanned, ref_failed = [], []
    for d in dirs:
        res = scan_dir(d, args.version, stages)
        if res is None:
            print(f"  (skip, no PDF/outputs) {d}", file=sys.stderr)
            continue
        (scanned if res["ref_ok"] else ref_failed).append(res)

    def counts_for(papers, kind=None):
        """Aggregate status counts; kind=None → all quotes, else only that kind."""
        c = {k: 0 for k in ("FAIL", "WARN", "PASS_FUZZY", "PASS")}
        for p in papers:
            for r in p["results"]:
                if kind is None or r["kind"] == kind:
                    c[r["status"]] = c.get(r["status"], 0) + 1
        return c

    print("\n================ v19 CORPUS verbatim-quote gate ================")
    if ref_failed:
        print("EXCLUDED — reference PDF not machine-readable (needs OCR; gate cannot verify):")
        for p in ref_failed:
            print(f"   {p['dir'].replace('papers/','')}  ({p['ref_chars']} chars extracted)")
        print()

    hdr = (f"{'paper':<40} {'kq:FAIL':>7} {'kq:WARN':>7} {'kq:PASS*':>8} "
           f"{'all:FAIL':>8} {'all:tot':>7}")
    print(hdr); print("-" * len(hdr))
    for p in sorted(scanned, key=lambda x: -counts_for([x], "key_quote")["FAIL"]):
        kc = counts_for([p], "key_quote"); ac = counts_for([p])
        kqn = sum(kc.values()) or 1
        name = p["dir"].replace("papers/", "")
        print(f"{name:<40} {kc['FAIL']:>7} {kc['WARN']:>7} "
              f"{100*(kc['PASS']+kc['PASS_FUZZY'])/kqn:7.0f}% "
              f"{ac['FAIL']:>8} {sum(ac.values()):>7}")

    kq = counts_for(scanned, "key_quote"); al = counts_for(scanned)
    kqn = sum(kq.values()) or 1; aln = sum(al.values()) or 1
    print("-" * len(hdr))
    print(f"\n=== PRIMARY metric — key_quote fields (canonical 'lifted from paper' anchors) ===")
    print(f"  key_quotes: {kqn}  |  FAIL {kq['FAIL']}  WARN {kq['WARN']}  "
          f"PASS_FUZZY {kq['PASS_FUZZY']}  PASS {kq['PASS']}")
    print(f"  CONFABULATION rate (FAIL/key_quotes)        : {100*kq['FAIL']/kqn:5.1f}%")
    print(f"  suspect rate       ((FAIL+WARN)/key_quotes) : {100*(kq['FAIL']+kq['WARN'])/kqn:5.1f}%")
    print(f"  grounded rate      ((PASS+FUZZY)/key_quotes): {100*(kq['PASS']+kq['PASS_FUZZY'])/kqn:5.1f}%")
    print(f"\n  (secondary, all English quoted strings n={aln}: FAIL {100*al['FAIL']/aln:.1f}% "
          f"— noisier, includes D-1 novelty & S0-6 next_question quotes)")

    print("\n---- key_quote FAILs (primary confabulation candidates for §H) ----")
    for p in scanned:
        for r in p["results"]:
            if r["status"] == "FAIL" and r["kind"] == "key_quote":
                flag = " ⚑1,3-BD" if r["prov_1_3_bd"] else ""
                print(f"[{p['dir'].replace('papers/','')}] {r['file']} pr={r['partial']}{flag}\n"
                      f"    “{r['quote']}”")

    if args.json:
        with open(args.json, "w", encoding="utf-8") as fh:
            json.dump({"scanned": scanned, "ref_failed": ref_failed,
                       "key_quote_counts": kq, "all_counts": al},
                      fh, ensure_ascii=False, indent=2)
        print(f"\nwrote {args.json}")


if __name__ == "__main__":
    main()
