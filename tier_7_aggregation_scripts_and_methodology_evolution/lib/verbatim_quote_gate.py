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

# H29-d (2026-07-24): structural labels the analyst authors, which happen to sit in
# quotation marks and were therefore verified as if the paper contained them.
# Measured on a 300-quote sample of `quoted` FAILs: 63% were SRG concept labels, e.g.
#     - Group SRG-5 "XPS deconvolution reporting": B-2, V3-Q10
#     - SRG-2: concept="Substrate scope boundaries incompletely defined" -- members: ...
#     - shared_root: "Performance superiority claims not numerically closed ..."
# A same-root-group name is analyst-authored by definition and can never be a paper
# quote, so excluding it is lossless. The test is the ENCLOSING LINE, not the span:
# a genuine paper quote can appear on a pipe row (`[U] U-4 | P4:Lcol:30-42* | "..."`)
# and must survive, so position-in-row heuristics are deliberately not used here.
#
# `timing_pressure` was in this list until 2026-07-27 and was REMOVED: unlike an SRG
# label, a timing_pressure line is analyst narrative that quotes the paper to justify
# the reading (e.g. `timing_pressure: … The explicit statement "Further studies are
# required …" further anchors this reading`, kumada v20 run2 s2). Excluding the whole
# line dropped a genuine verbatim quote from the audit (bounded loss, Fable review
# 2026-07-27 §問1c). The quote harvester only lifts quotation-mark-delimited spans, so
# the surrounding narrative is never harvested anyway — keeping the line lets its real
# quote be verified while the narrative stays untouched.
_LABEL_CONTEXT = re.compile(
    r'\bSRG[-\s]?\d|\bsame_root_group\b|\bconcept\s*=|\bshared[_\s]root\b|'
    r'\bGroup\s+\d+\s*["“]', re.I)


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

    def _line_of(pos: int) -> str:
        start = text.rfind("\n", 0, pos) + 1
        end = text.find("\n", pos)
        return text[start:end if end != -1 else len(text)]

    def add(raw, kind, require_english, context=""):
        raw = raw.strip().strip('"“”').strip()
        if len(raw) < 15:
            return
        if _FIELD_TOKENS.search(raw):
            return
        if "|" in raw:               # pipe-delimited table row / schema line
            return
        # H29-d: an analyst-authored group/root label, not a claim about the paper
        if context and _LABEL_CONTEXT.search(context):
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
        add(m.group(1), "quoted", require_english=True, context=_line_of(m.start()))
    return quotes


# ---------------------------------------------------------------- splice tolerance
# (2026-07-29, H31/B-3 follow-up — v24 candidate 1 diagnosis)
#
# A quote that IS verbatim in the printed paper can still fail the substring and
# fuzzy tests, because `pdftotext` linearizes a two-column article by dropping
# footnote blocks, reference lists, table bodies and running headers INTO the
# middle of the running sentence. Measured on the kumada v23 interleaved set, all
# three "non_verbatim" verdicts were of this kind, e.g.
#     quote : "[REDACTED: verbatim source text; see the source paper via its DOI]
#[REDACTED: verbatim source text; see the source paper via its DOI]"
#     doc   : "…to undergo coupling while ‹2777 chars of footnotes 1-3, eq 1 and
#              Table I with its footnotes› [REDACTED: verbatim source text; see the source paper via its DOI]
#[REDACTED: verbatim source text; see the source paper via its DOI]"
# The model read the PDF multimodally and saw one continuous sentence; the
# reference is what is broken. Same for OCR damage inside a word ("di-n-butyl-
# benzenes" → "di ii butylbenzenes").
#
# So we re-test a failing quote as an ORDERED SEQUENCE OF SEGMENTS: greedily match
# the longest run of quote tokens that occurs after the previous match, and accept
# only when the quote is nearly fully covered by a few long segments whose gaps
# look like reference/footnote material (many year and journal-abbreviation tokens)
# or are short enough to be intra-word OCR damage.
#
# LIMIT (deliberate, do not paper over): this cannot distinguish a footnote splice
# from a model that concatenated two genuinely distant body sentences separated by
# a footnote block. That failure class is guarded elsewhere — structurally by
# multi_quote/trailing_annotation, and at the prompt layer by H31/B-2 and H32 — and
# splice hits are reported under their OWN verdict (PASS_SPLICED / "spliced"), never
# folded into PASS, so they stay visible for human reading rather than disappearing.
_YEAR_TOK = re.compile(r"^(18|19|20)\d\d$")
_JOURNAL_TOK = frozenset("""
amer chem soc ibid commun common organometal inorg phys lett rev ber bull tetrahedron
synth angew acta nouv dokl izv zh chim ann engl int naturforsch prepr rec trav univ sci
fac quart press academic ed eds vol chap chapter london york
""".split())

_SPLICE_MIN_SEG = 5        # tokens; shorter runs are coincidence, not a span
_SPLICE_MIN_ANCHOR = 8     # tokens; the first segment must be a real anchor
_SPLICE_MAX_SEG = 4        # more pieces than this is not a splice, it is a collage
_SPLICE_MIN_COVER = 0.85   # fraction of quote tokens inside substantive segments
_SPLICE_TINY_GAP = 40      # chars; below this a gap is intra-word OCR damage


def _segment_quote(nq: str, doc: str):
    """Greedy longest-run segmentation of `nq` against `doc`, left to right."""
    toks, i, cursor, segs = nq.split(), 0, 0, []
    while i < len(toks):
        lo, hi, best_n, best_pos = 1, len(toks) - i, 0, -1
        while lo <= hi:                     # binary search on run length
            mid = (lo + hi) // 2
            pos = doc.find(" ".join(toks[i:i + mid]), cursor)
            if pos != -1:
                best_n, best_pos, lo = mid, pos, mid + 1
            else:
                hi = mid - 1
        if best_n == 0:                     # token absent downstream (OCR damage)
            i += 1
            continue
        span = " ".join(toks[i:i + best_n])
        segs.append((best_pos, best_n, best_pos + len(span)))
        cursor = best_pos + len(span)
        i += best_n
    return segs, len(toks)


def _gap_is_interruption(gap: str) -> bool:
    if len(gap) <= _SPLICE_TINY_GAP:
        return True                          # intra-word OCR damage
    t = gap.split()
    years = sum(1 for x in t if _YEAR_TOK.match(x))
    journal = sum(1 for x in t if x in _JOURNAL_TOK)
    return years >= 2 and journal >= 2       # reference / footnote block


def splice_match(nq: str, doc: str) -> bool:
    """True when `nq` is verbatim in `doc` apart from reference-extraction breaks."""
    segs, ntok = _segment_quote(nq, doc)
    subst = [s for s in segs if s[1] >= _SPLICE_MIN_SEG]
    if not (2 <= len(subst) <= _SPLICE_MAX_SEG):
        return False
    if subst[0][1] < _SPLICE_MIN_ANCHOR:
        return False
    if sum(s[1] for s in subst) / ntok < _SPLICE_MIN_COVER:
        return False
    return all(_gap_is_interruption(doc[a[2]:b[0]])
               for a, b in zip(subst, subst[1:]))


# ---------------------------------------------------------------- matching
_RANK = {"PASS": 4, "PASS_FUZZY": 3, "PASS_SPLICED": 2, "WARN": 1, "FAIL": 0}


def score_quote(nq: str, refs: dict[str, str], allow_splice: bool = True):
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
        if status not in ("PASS_FUZZY",) and allow_splice and splice_match(nq, doc):
            status = "PASS_SPLICED"
        if _RANK[status] > _RANK[best[0]] or (_RANK[status] == _RANK[best[0]] and pr > best[2]):
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

    order = _RANK
    results.sort(key=lambda r: (order[r["status"]], r["partial"]))

    counts = {k: 0 for k in order}
    for r in results:
        counts[r["status"]] += 1

    print(f"\n=== verbatim-quote gate: {pdir} ===")
    print(f"reference: {os.path.basename(pdfs[0])}"
          + (f" + {os.path.basename(sis[0])}" if sis else "")
          + f" | {len(results)} unique quotes across {len(out_files)} files")
    print(f"summary: FAIL={counts['FAIL']}  WARN={counts['WARN']}  "
          f"PASS_SPLICED={counts['PASS_SPLICED']}  "
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
