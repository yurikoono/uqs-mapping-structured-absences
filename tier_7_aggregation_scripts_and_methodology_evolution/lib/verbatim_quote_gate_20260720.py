#!/usr/bin/env python3
"""verbatim_quote_gate.py — pre-Stage-2/3 quote-provenance gate (prototype).

Purpose
-------
UQS outputs anchor almost every finding to a `key_quote` / quoted string that is
supposed to be lifted verbatim from the paper. Nothing currently checks that the
quote *actually exists* in the paper. This gate is a pure script (NOT a model):
it harvests quotes from S0/S1/S2 outputs, normalizes them and the paper's
extracted text, and reports whether each quote is grounded.

It catches the *fabricated-token* failure class (a quote the paper never
contains). It does NOT catch the *present-data-asserted-absent* class
(a real quote whose surrounding note falsely claims "not quantified") — that
needs the separate "covered null-slot" mechanism. Run both.

Design follows the Fable-5 × orchestrator review of dev/terao2002
(improvements/_methodology/fable5_terao2002_comprehensive_review_20260719.md).

Usage
-----
    python3 scripts/verbatim_quote_gate.py papers/dev/terao2002
    python3 scripts/verbatim_quote_gate.py papers/dev/terao2002 --json report.json
    python3 scripts/verbatim_quote_gate.py papers/dev/terao2002 --stages s0,s2

Exit code is nonzero if any harvested quote is FAIL (unmatched) — so it can gate
a pipeline step. WARNs do not fail the gate by default (use --strict).
"""
from __future__ import annotations

import argparse
import glob
import json
import os
import re
import subprocess
import sys
import unicodedata

try:
    from rapidfuzz import fuzz
except ImportError:
    sys.exit("rapidfuzz required: pip install rapidfuzz")

# ---------------------------------------------------------------- normalization
_SUB = str.maketrans("₀₁₂₃₄₅₆₇₈₉", "0123456789")
_SUP = str.maketrans("⁰¹²³⁴⁵⁶⁷⁸⁹", "0123456789")
_GREEK = {"η": "eta", "π": "pi", "β": "beta", "α": "alpha", "σ": "sigma",
          "µ": "u", "μ": "u", "·": " ", "→": " ", "×": " "}
# chemical abbreviation canonicalization: both the paper's spelling and the
# model's internal shorthand collapse to one token, so "1,3-BD" (which never
# appears in the paper text) still matches "1,3-butadiene".
_CHEM = [
    (re.compile(r"1\s*,\s*3\s*-\s*(bd|butadiene|diene)"), " 13diene "),
    (re.compile(r"\bbutadiene\b"), " 13diene "),
    (re.compile(r"\bn\s*-\s*oct(yl)?\b"), " noct "),
    (re.compile(r"\bn\s*-\s*decyl\b"), " ndecyl "),
    (re.compile(r"\bni\s*\(\s*cod\s*\)\s*2\b"), " nicod2 "),
]


def normalize(s: str) -> str:
    s = unicodedata.normalize("NFKC", s)
    s = s.translate(_SUB).translate(_SUP)
    for k, v in _GREEK.items():
        s = s.replace(k, v)
    s = s.lower()
    # unify all dash variants to plain hyphen BEFORE chem canonicalization
    s = re.sub(r"[‐‑‒–—−]", "-", s)
    for rx, repl in _CHEM:
        s = rx.sub(repl, s)
    # drop everything but alphanumerics + space (kills markdown, punctuation)
    s = re.sub(r"[^a-z0-9 ]", " ", s)
    s = re.sub(r"\s+", " ", s).strip()
    return s


# ---------------------------------------------------------------- pdf reference
def extract_pdf_text(pdf_path: str) -> str:
    try:
        out = subprocess.run(["pdftotext", "-q", pdf_path, "-"],
                             capture_output=True, text=True, check=True)
        return out.stdout
    except Exception as e:  # pragma: no cover
        print(f"  ! pdftotext failed on {pdf_path}: {e}", file=sys.stderr)
        return ""


# ---------------------------------------------------------------- quote harvest
# quoted strings: single-line only (no newline inside), so the greedy match can't
# span unrelated quote characters across the document.
_QUOTE_RE = re.compile(r'["“”]([^"“”\n]{15,400})["“”]')
_KEYQUOTE_RE = re.compile(r'^\s*key_quote:\s*(.+?)\s*$', re.MULTILINE)
# UQS structured-field tokens: if a captured span contains these it is analytical
# scaffolding (S0-S2 schema fields / S1 Turn-4 table rows), not a paper quote.
_FIELD_TOKENS = re.compile(
    r'temperature_note|grounded_in|same_root_group|scope_type|derived_from|'
    r'confirmed_english|convergence|anchoring_note|questions_that_cannot|'
    r'deferral_type|reason_inferred|mixed_detail|linked_to|item_id|'
    r'cross_field_temperature|evidence_type|novelty_claim|success_criteri|'
    r'prior_work|core_claim|next_question_stated|severity|loc:')
# field-value phrases the model emits (not quotes lifted from a paper)
_FIELD_VALUES = {"not stated in paper", "not applicable", "n a", "none retrospective",
                 "not available", "none", "yes", "no"}


def _ascii_letter_ratio(s: str) -> float:
    letters = [c for c in s if c.isalpha()]
    if not letters:
        return 0.0
    return sum(c.isascii() for c in letters) / len(letters)


def harvest_quotes(md_path: str):
    """Return list of (raw_quote, field_kind) from one output file.

    Keeps: every key_quote field, plus single-line double-quoted strings that are
    English-dominant (a paper quote) and free of UQS field scaffolding. Japanese
    analytical prose in D-4/E bodies is intentionally excluded — the gate checks
    quotes claimed to be lifted from an English paper, not the model's commentary.
    """
    with open(md_path, encoding="utf-8") as fh:
        text = fh.read()
    # The E-section confirmed_english block holds UQS-GENERATED English
    # (propositional + question), not quotes lifted from the paper — exclude it
    # so the gate does not flag synthesized text as an unmatched "quote".
    text = re.sub(r"```confirmed_english.*?```", " ", text, flags=re.DOTALL)
    text = re.sub(r"^\s*confirmed_english_\w+:.*$", " ", text, flags=re.MULTILINE)
    quotes = []
    seen = set()

    def add(raw, kind, require_english):
        raw = raw.strip().strip('"“”').strip()
        if len(raw) < 15:
            return
        if _FIELD_TOKENS.search(raw):
            return
        if "|" in raw:               # pipe-delimited table row / schema line
            return
        if require_english and _ascii_letter_ratio(raw) < 0.6:
            return
        key = normalize(raw)
        if not key or len(key) < 12 or key in seen:
            return
        if key in _FIELD_VALUES:
            return
        seen.add(key)
        quotes.append((raw, kind))

    for m in _KEYQUOTE_RE.finditer(text):
        add(m.group(1), "key_quote", require_english=False)
    for m in _QUOTE_RE.finditer(text):
        add(m.group(1), "quoted", require_english=True)
    return quotes


# ---------------------------------------------------------------- matching
def score_quote(nq: str, refs: dict[str, str]):
    """Return (status, best_src, partial, token_set) for a normalized quote."""
    best = ("FAIL", None, 0.0, 0.0)
    for src, doc in refs.items():
        if not doc:
            continue
        if nq and nq in doc:
            return ("PASS", src, 100.0, 100.0)
        pr = fuzz.partial_ratio(nq, doc)
        # locate the best-aligned window, then judge weighted-token overlap on it
        al = fuzz.partial_ratio_alignment(nq, doc)
        window = doc[al.dest_start:al.dest_end] if al else ""
        ts = fuzz.token_set_ratio(nq, window) if window else 0.0
        if pr >= 92 and ts >= 80:
            status = "PASS_FUZZY"
        elif pr >= 78 or ts >= 62:
            status = "WARN"
        else:
            status = "FAIL"
        rank = {"PASS": 3, "PASS_FUZZY": 2, "WARN": 1, "FAIL": 0}
        if rank[status] > rank[best[0]] or (rank[status] == rank[best[0]] and pr > best[2]):
            best = (status, src, pr, ts)
    return best


# ---------------------------------------------------------------- driver
def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("paper_dir")
    ap.add_argument("--stages", default="s0,s1,s2",
                    help="comma list of stage suffixes to scan (default s0,s1,s2)")
    ap.add_argument("--version", default=None,
                    help="only harvest output files whose name contains this token "
                         "(e.g. v19), so a folder with mixed prompt versions is filtered")
    ap.add_argument("--json", default=None)
    ap.add_argument("--strict", action="store_true",
                    help="exit nonzero on WARN as well as FAIL")
    args = ap.parse_args()

    pdir = args.paper_dir.rstrip("/")
    pdfs = sorted(p for p in glob.glob(f"{pdir}/*.pdf") if "_si" not in os.path.basename(p).lower())
    sis = sorted(glob.glob(f"{pdir}/*_si.pdf"))
    if not pdfs:
        # repro / subfolders often reuse the parent folder's PDF
        parent = os.path.dirname(pdir)
        pdfs = sorted(p for p in glob.glob(f"{parent}/*.pdf")
                      if "_si" not in os.path.basename(p).lower())
        sis = sorted(glob.glob(f"{parent}/*_si.pdf"))
    if not pdfs:
        sys.exit(f"no main PDF in {pdir}")

    refs = {"main": normalize(extract_pdf_text(pdfs[0]))}
    if sis:
        refs["si"] = normalize(extract_pdf_text(sis[0]))

    stages = [s.strip() for s in args.stages.split(",") if s.strip()]
    out_files = []
    for st in stages:
        out_files += sorted(glob.glob(f"{pdir}/*_{st}.md"))
    if args.version:
        out_files = [f for f in out_files if f"_{args.version}_" in os.path.basename(f)]
    # de-dup while preserving order
    out_files = list(dict.fromkeys(out_files))
    if not out_files:
        sys.exit(f"no stage outputs matching {stages} in {pdir}")

    results = []
    for f in out_files:
        for raw, kind in harvest_quotes(f):
            nq = normalize(raw)
            status, src, pr, ts = score_quote(nq, refs)
            prov = []
            if re.search(r"1\s*,\s*3\s*-\s*bd", raw.lower()):
                prov.append("uses '1,3-BD' (abbrev absent from paper text)")
            results.append({
                "file": os.path.basename(f), "kind": kind, "status": status,
                "src": src, "partial": round(pr, 1), "token_set": round(ts, 1),
                "provenance_flag": prov, "quote": raw[:160],
            })

    order = {"FAIL": 0, "WARN": 1, "PASS_FUZZY": 2, "PASS": 3}
    results.sort(key=lambda r: (order[r["status"]], r["partial"]))

    counts = {k: 0 for k in order}
    for r in results:
        counts[r["status"]] += 1

    print(f"\n=== verbatim-quote gate: {pdir} ===")
    print(f"reference: {os.path.basename(pdfs[0])}"
          + (f" + {os.path.basename(sis[0])}" if sis else "")
          + f" | {len(results)} unique quotes across {len(out_files)} files")
    print(f"summary: FAIL={counts['FAIL']}  WARN={counts['WARN']}  "
          f"PASS_FUZZY={counts['PASS_FUZZY']}  PASS={counts['PASS']}\n")
    for r in results:
        flag = ("  ⚑ " + "; ".join(r["provenance_flag"])) if r["provenance_flag"] else ""
        print(f"[{r['status']:<10}] pr={r['partial']:>5} ts={r['token_set']:>5} "
              f"src={str(r['src']):<4} {r['file']}:{r['kind']}{flag}")
        print(f"             “{r['quote']}”")

    if args.json:
        with open(args.json, "w", encoding="utf-8") as fh:
            json.dump({"paper_dir": pdir, "counts": counts, "results": results},
                      fh, ensure_ascii=False, indent=2)
        print(f"\nwrote {args.json}")

    fail = counts["FAIL"] + (counts["WARN"] if args.strict else 0)
    sys.exit(1 if fail else 0)


if __name__ == "__main__":
    main()
