#!/usr/bin/env python3
"""Mechanical endpoints 1, 2 (gate counts), 4, 5 for B2 -> Stage 3 (prereg preregistration_B2_stage3.md). Run from repo root.
Scoring is arm-blind; the key is joined only at the end."""
import json, re, glob, importlib.util, os, csv
# Paths (2026-10-17). In the project repository this script is run from the repository root, as before, and every path
# below is the repository path. Inside the Zenodo deposit of Paper A it can be run from any directory: an input that is not
# found relative to the working directory is read from the deposit (`_src`), the implementations come from
# tier_7_aggregation_scripts_and_methodology_evolution/lib/, and outputs go to rerun_output/ at the deposit root (`_out`),
# so the deposited results are not overwritten and can be compared with the re-run.
import os as _os
_DEP = _os.path.abspath(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), "..", ".."))
_LIB = "tier_7_aggregation_scripts_and_methodology_evolution/lib/"
def _src(repo, dep=None):
    return repo if _os.path.exists(repo) else _os.path.join(_DEP, repo if dep is None else dep)
def _out(repo, dep):
    if _os.path.isdir(repo):
        return repo
    d = _os.path.join(_DEP, "rerun_output", dep); _os.makedirs(d, exist_ok=True); return d
O = _src("papers/dev/kumada/b2_stage3_R1_2026-09"); D = _out("manuscript_A/DigitalDiscovery_R1/01_response/d4_baseline", "01_response/d4_baseline")
_CH = _src("manuscript_A/DigitalDiscovery_R1/01_response/d3_heldout/check_heldout.py", "01_response/d3_heldout/check_heldout.py")
src = open(_CH).read(); ns = {"__file__": _CH}; exec(src.split("res = {}")[0], ns)
spec = importlib.util.spec_from_file_location("vqg", _src("scripts/verbatim_quote_gate.py", _LIB + "verbatim_quote_gate.py")); vqg = importlib.util.module_from_spec(spec); spec.loader.exec_module(vqg)
_PDF = _src("papers/dev/kumada/Kumada_1972.pdf")   # source PDF: not deposited; place it here (DOI 10.1021/ja00767a075)
if not _os.path.isfile(_PDF):
    raise SystemExit(f"the quote gate needs the source PDF of Kumada 1972 at {_PDF} (not deposited; obtain it via its DOI)")
refs = {"main": vqg.normalize(vqg.extract_pdf_text(_PDF))}
TABLE1 = {f"EP-{i:02d}a" for i in range(1, 11)}
rows, quotes = [], []
for d in sorted(glob.glob(f"{O}/in_*")):
    i = d.split("_")[-1]; f = f"{d}/s3.md"
    if not os.path.exists(f): rows.append({"id": i, "status": "no_output"}); continue
    t = open(f).read()
    a = re.search(r"^#{2,3}\s*§\s*2\b.*$", t, re.M); b = re.search(r"^#{2,3}\s*§\s*3\b.*$", t, re.M)
    s2 = t[a.end():b.start()] if a and b else t
    # SRG/CLA headings: bold, at line start; CLA may be unnumbered ("**CLA: ...**"); section headers like "**Outside the SRGs: CLAs**" excluded
    hs = [m.start() for m in re.finditer(r"^\*\*(?:SRG-?\d+|CLA(?:-?\d+)?\s*[:：\[「(（])", s2, re.M)]
    blocks = [s2[x:y] for x, y in zip(hs, hs[1:] + [len(s2)])]
    anchored = sum(1 for b in blocks if re.search(r"EP-\d+[a-z]", b) and (ns["QUOTE"].search(b) or ns["LOCREF"].search(b)))
    eps = set(re.findall(r"EP-\d+[a-z]", t))
    secs = [h for h in ("§1", "§2", "§3", "§4", "§5", "§6") if h in t]
    st = [0, 0, 0, 0, 0]
    for raw, kind in vqg.harvest_quotes(f):
        s, src_, pr, ts = vqg.score_quote(vqg.normalize(raw), refs)
        k = ["PASS", "PASS_FUZZY", "PASS_SPLICED", "WARN", "FAIL"].index(s); st[k] += 1
        quotes.append({"id": i, "kind": kind, "status": s, "partial": round(pr, 1), "quote": raw[:200]})
    rows.append({"id": i, "status": "completed" if len(secs) == 6 else "partial", "sections": len(secs), "blocks": len(blocks),
                 "blocks_anchored": anchored, "ep_labels": len(eps), "ep_in_table1": len(eps & TABLE1), "eps": " ".join(sorted(eps)),
                 "gate_pass": st[0] + st[1] + st[2], "gate_warn": st[3], "gate_fail": st[4], "chars": len(t)})
key = json.load(open(f"{O}/_key.json"))
for r in rows: r.update(key[r["id"]])
with open(f"{D}/b2_stage3_mechanical.csv", "w", newline="") as fh:
    w = csv.DictWriter(fh, fieldnames=list(rows[0])); w.writeheader(); w.writerows(rows)
with open(f"{D}/b2_stage3_quotes.csv", "w", newline="") as fh:
    qq = [{**q, **key[q["id"]]} for q in quotes]; w = csv.DictWriter(fh, fieldnames=list(qq[0])); w.writeheader(); w.writerows(qq)
for r in sorted(rows, key=lambda r: (r["arm"], r["run"])):
    print(r["arm"], r["run"], r["id"], r["status"], f"blocks {r['blocks_anchored']}/{r['blocks']} anchored", f"EP {r['ep_in_table1']}/10 of Table1 ({r['ep_labels']} labels)", f"gate P/W/F {r['gate_pass']}/{r['gate_warn']}/{r['gate_fail']}", r["chars"])
