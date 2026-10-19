#!/usr/bin/env python3
"""R3-3 (b): Stage 4 filling-paper candidates — retained / retracted / unclassifiable.

Builds `candidates.csv` and `tally_counts.json` from primary records only:
  * the Stage 4 output files (what each run proposed, with file + line), and
  * the verification records that exist for some of those runs (what was checked, and the verdict).

Nothing is copied from SI or manuscript text. Where a verdict is transcribed from a prose record
(a memo or log without a machine-readable table), the transcription carries the record path and
line number, and the script ASSERTS that the cited line contains a fixed token, so a moved or
edited record makes the build fail instead of silently mis-attributing a verdict.

Two parts
---------
Part A  = the 37 Stage 4 analyses that the revised Methods 6 calls "the 37 Stage 4 analyses reported
          here" (33 under Stage 4 v2, 4 under Stage 4 v6). The list is reconstructed in PART_A below
          (24 Kumada/Murai multi-run files + 9 case-study files + 4 context analyses).
          Candidate unit = one "Filling Onset" / "Filling Establishment" slot (JA: 充填開始点 / 充填確立点)
          in §B that names a publication.
Part B  = every candidate that appears in a verification record (supporting studies cited in
          SI-6 / SI-9 / SI-11.2 / Methods 6). Candidate unit = the unit the record itself uses
          (listed below per record set).

Aggregation rule (applied identically to every row; stated in tally.md)
---------------------------------------------------------------------
bib_check     : resolved | corrected | not_resolved | mismatch | insufficient | not_checked
content_check : fills | does_not_fill | not_checked
status (strict, = Methods 2 "retained only after the chain"):
    retracted      if bib_check in {not_resolved, mismatch} or content_check == does_not_fill
    retained       if bib_check in {resolved, corrected} and content_check == fills
    unclassifiable otherwise
status_bib_only (lenient, bibliographic layer only):
    retracted      if bib_check in {not_resolved, mismatch} or content_check == does_not_fill
    retained       if bib_check in {resolved, corrected}
    unclassifiable otherwise

Run:  python3 build_tally.py      (from anywhere; paths are resolved from this file)
"""
from __future__ import annotations

import csv
import hashlib
import json
import re
import sys
from collections import Counter, defaultdict, OrderedDict
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[3]                      # r33b_candidates -> 01_response -> DigitalDiscovery_R1 -> manuscript_A -> repo
DEP = ROOT / "zenodo_deposit_paperA_reviewer_R1_20260928"
OUT_CSV = HERE / "candidates.csv"
OUT_JSON = HERE / "tally_counts.json"

# ----------------------------------------------------------------------------------------------
# helpers
# ----------------------------------------------------------------------------------------------

_cache: dict[Path, list[str]] = {}


def lines(rel: str) -> list[str]:
    p = ROOT / rel
    if p not in _cache:
        _cache[p] = p.read_text(encoding="utf-8").split("\n")
    return _cache[p]


def sha(rel: str) -> str:
    return hashlib.sha256((ROOT / rel).read_bytes()).hexdigest()


_manifest = None


def deposit_path(rel: str) -> str:
    """Path of the same file inside the R1 reviewer deposit (matched by SHA-256), or ''."""
    global _manifest
    if _manifest is None:
        _manifest = {}
        with open(DEP / "MANIFEST.csv", encoding="utf-8") as fh:
            for r in csv.DictReader(fh):
                _manifest.setdefault(r["sha256"], []).append(r["path"])
    hits = _manifest.get(sha(rel), [])
    hits = [h for h in hits if not h.startswith("per_reference_catalogue")] or hits
    return hits[0] if hits else ""


def header(rel: str) -> tuple[str, str]:
    """(prompt_version, model_info) verbatim from the file header."""
    pv = mi = ""
    for l in lines(rel)[:12]:
        m = re.match(r"\s*prompt_version:\s*(.+)", l)
        if m:
            pv = m.group(1).strip()
        m = re.match(r"\s*model_info:\s*(.+)", l)
        if m:
            mi = m.group(1).strip()
    return pv, mi


def assert_record(rel: str, line_no: int, token: str) -> None:
    L = lines(rel)
    if line_no < 1 or line_no > len(L) or token not in L[line_no - 1]:
        sys.exit(f"RECORD CHECK FAILED: {rel}:{line_no} does not contain {token!r}\n"
                 f"   line is: {L[line_no-1][:200] if 0 < line_no <= len(L) else '<out of range>'}")


def section(rel: str, start_pat: str, end_pat: str) -> tuple[int, int]:
    L = lines(rel)
    s = next((i for i, l in enumerate(L) if re.match(start_pat, l)), None)
    if s is None:
        return 0, len(L)
    e = next((i for i in range(s + 1, len(L)) if re.match(end_pat, L[i])), len(L))
    return s, e


def find_line(rel: str, pattern: str, prefer: tuple[str, str] | None = (r"^#{2,4}\s*§B", r"^#{2,4}\s*§D")) -> int:
    """First line matching `pattern`, preferring the §B–§C region. 0 if not found."""
    L = lines(rel)
    rx = re.compile(pattern)
    if prefer:
        s, e = section(rel, *prefer)
        for i in range(s, e):
            if rx.search(L[i]):
                return i + 1
    for i, l in enumerate(L):
        if rx.search(l):
            return i + 1
    return 0


YEAR = re.compile(r"(?<!\d)(19[4-9]\d|20[0-2]\d)(?!\d)")
DOI = re.compile(r"10\.\d{4,9}/[^\s\)\]，、;|`（）]+")
ITALIC = re.compile(r"(?<!\*)\*(?!\*)([^*\n]{2,90}?)(?<!\*)\*(?!\*)")
JOURNALS = [
    "J. Am. Chem. Soc.", "Journal of the American Chemical Society", "JACS",
    "Bull. Chem. Soc. Jpn.", "Bulletin of the Chemical Society of Japan", "BCSJ",
    "J. Organomet. Chem.", "Journal of Organometallic Chemistry", "Tetrahedron Lett.", "Tetrahedron",
    "Chem. Lett.", "Org. Synth.", "Organic Syntheses", "Pure Appl. Chem.", "Angew. Chem.", "Organometallics",
    "Chem. Rev.", "Acc. Chem. Res.", "Chem. Sci.", "Nature", "Science", "J. Org. Chem.", "Chem. Commun.",
    "J. Chem. Soc., Chem. Commun.", "Chem. Eur. J.", "Inorg. Chem.", "ACS Catal.", "Org. Lett.",
    "Dalton Trans.", "Adv. Synth. Catal.", "Synthesis", "Russ. Chem. Rev.", "Eur. J. Inorg. Chem.",
]


def parse_citation(text: str) -> dict:
    """Best-effort first author / year / journal / DOI of the first citation in a slot."""
    t = re.sub(r"^\s*[\*\-]*\s*(\([a-z]\)\s*)?", "", text)
    cit = re.split(r"\s+—\s+|\s+–\s+(?=[^\d])| — ", t)[0]
    m = re.match(r"\s*\**\s*([A-Z][A-Za-zÀ-ÿ'’\-]+)", cit)
    fa = m.group(1) if m else ""
    if fa in {"The", "A", "An", "No", "None", "Same", "See", "Unidentified", "Not", "Partial", "Indirect", "Complete", "Direct"}:
        fa = ""
    ym = YEAR.search(cit) or YEAR.search(t)
    year = ym.group(1) if ym else ""
    jm = ITALIC.search(cit)
    journal = jm.group(1).strip() if jm else ""
    if not journal:
        for j in sorted(JOURNALS, key=len, reverse=True):
            if j in cit:
                journal = j
                break
    dm = DOI.search(text)
    doi = dm.group(0).rstrip(".,") if dm else ""
    if fa and year and journal:
        spec = "specific"
    elif year or journal:
        spec = "partial"
    else:
        spec = "generic"
    return dict(first_author=fa, year=year, journal=journal, doi=doi, specificity=spec)


NONE_RX = re.compile(r"^\s*\**\s*(unidentified|not identified|none identified|no paper|no specific|no independent|"
                     r"none\b|n/a|未同定|該当なし|なし|—\s*未同定|—|-)\b", re.I)
SAME_RX = re.compile(r"^\s*\**\s*(同上|同一|same as above|same paper|same\b|as above|上記と同一|上述と同一)", re.I)
LABEL_RX = re.compile(r"^\s*(?:[\*\-]\s*)?\*\*\s*(Filling Onset|Filling Establishment|充填開始点|充填確立点)([^*]*)\*\*\s*[:：]?\s*(.*)$")
FIELD_RX = re.compile(r"^\s*[\*\-]\s*\*\*")
EP_RX = re.compile(r"(?:^\s*\*\*|^#{2,5}\s*)(EP-\d+[a-z]?)")


def parse_slots(rel: str) -> tuple[list[dict], Counter]:
    """§B onset/establishment slots of one Stage 4 output."""
    L = lines(rel)
    s, e = section(rel, r"^#{2,4}\s*§\s*B", r"^#{2,4}\s*§\s*C")
    ep = ""
    out, skipped = [], Counter()
    i = s
    while i < e:
        l = L[i]
        m_ep = EP_RX.search(l)
        if m_ep and not LABEL_RX.match(l):
            ep = m_ep.group(1)
        m = LABEL_RX.match(l)
        if m:
            role = "onset" if m.group(1) in ("Filling Onset", "充填開始点") else "establishment"
            qual = m.group(2).strip()
            text = m.group(3).strip()
            line_no = i + 1
            if not text:            # label on its own line; take continuation lines
                j, buf = i + 1, []
                while j < e and j < i + 8:
                    lj = L[j]
                    if LABEL_RX.match(lj) or EP_RX.search(lj) or (FIELD_RX.match(lj) and not lj.startswith("  ")):
                        break
                    if lj.strip():
                        buf.append(lj.strip())
                    j += 1
                text = " ".join(buf)
                if not text:
                    skipped["label_heading_only"] += 1
                    i += 1
                    continue
            if SAME_RX.match(text):
                skipped["same_as_above"] += 1
            elif NONE_RX.match(text):
                skipped["not_identified"] += 1
            else:
                c = parse_citation(text)
                out.append(dict(ep=ep, slot=f"{role}{(' ' + qual) if qual else ''}", line=line_no,
                                text=text, **c))
        i += 1
    # v6: a separate "* **DOI**: ..." line inside the EP block -> attach to the last candidate of that EP
    for i in range(s, e):
        if re.match(r"^\s*[\*\-]\s*\*\*DOI\*\*", L[i]):
            dm = DOI.search(L[i])
            prev = [c for c in out if c["line"] < i + 1]
            if dm and prev and not prev[-1]["doi"]:
                prev[-1]["doi"] = dm.group(0).rstrip(".,") + f" (EP-block DOI line {i+1})"
    return out, skipped


def status_of(bib: str, content: str) -> tuple[str, str, str]:
    """(status, retraction_reason, status_bib_only) under the stated rule."""
    reason = ""
    if bib == "not_resolved":
        reason = "DOI does not resolve"
    elif bib == "mismatch":
        reason = "metadata mismatch"
    elif content == "does_not_fill":
        reason = "content does not fill"
    if reason:
        return "retracted", reason, "retracted"
    if bib in ("resolved", "corrected"):
        return ("retained" if content == "fills" else "unclassifiable"), "", "retained"
    return "unclassifiable", "", "unclassifiable"


ROWS: list[dict] = []
CHECKS: list[str] = []          # re-derivation checks vs. what records/summary state


def add(**kw):
    st, rr, sb = status_of(kw["bib_check"], kw["content_check"])
    if kw.get("evidence_line") == "NOT FOUND":
        st, rr, sb = "unclassifiable", "", "unclassifiable"
        kw["unclassifiable_reason"] = ("candidate named in the verification record/ledger but not found in the deposited "
                                       "analysis file (record-file mismatch); the verdict cannot be tied to a proposal")
    kw.setdefault("status", st)
    kw.setdefault("retraction_reason", rr)
    kw.setdefault("status_bib_only", sb)
    if kw["status"] == "unclassifiable" and not kw.get("unclassifiable_reason"):
        if kw["bib_check"] == "not_checked":
            kw["unclassifiable_reason"] = "no verification record for this candidate"
        elif kw["bib_check"] == "insufficient":
            kw["unclassifiable_reason"] = "citation too incomplete to resolve (record says unverifiable)"
        elif kw["content_check"] == "not_checked":
            kw["unclassifiable_reason"] = "bibliographic check only; no content check recorded"
    ROWS.append(kw)


def model_short(mi: str) -> str:
    s = mi.lower()
    for k, v in [("opus 4.8", "Opus 4.8 (as self-reported)"), ("sonnet-4-6", "Sonnet 4.6"), ("sonnet 4.6", "Sonnet 4.6"),
                 ("sonnet (current snapshot)", "Sonnet (unversioned self-report)"), ("opus-4-7", "Opus 4.7"),
                 ("opus 4.7", "Opus 4.7"),
                 ("haiku", "Haiku 4.5"), ("gpt-5.4", "GPT-5.4 Thinking"), ("gpt-5.5", "GPT-5.5 Thinking")]:
        if k in s:
            return v
    return mi or "unknown"


# ----------------------------------------------------------------------------------------------
# PART A — the 37 analyses
# ----------------------------------------------------------------------------------------------
K, M = "papers/dev/kumada", "papers/dev/murai"
PART_A = []
for paper, d, stem in [("Kumada 1972", K, "kumada"), ("Murai 1993", M, "murai")]:
    for lang, suf in [("JA", ""), ("EN", "_en")]:
        for r in range(1, 7):
            f = f"{d}/{stem}_v184_sonnet_s4v2{suf}{'' if r == 1 else f'_run{r}'}.md"
            PART_A.append((f"A:{stem}-{lang}-run{r}", paper, f))
CASES = [("Breitenfeld 2014", "papers/ep/kumada1972/breitenfeld2014/breitenfeld2014_v184_sonnet_s4v2_en.md"),
         ("Cherney 2015", "papers/ep/kumada1972/cherney2015/cherney2015_v184_sonnet_s4v2_en.md"),
         ("Kumada 1976 BCSJ (Tamao)", "papers/ep/kumada1972/kumada1976b/kumada1976b_v184_sonnet_s4v2_en.md"),
         ("Mazet 2021", "papers/ep/kumada1972/mazet2021/mazet2021_v184_sonnet_s4v2_en.md"),
         ("Molander 2016", "papers/ep/kumada1972/molander2016/molander2016_v184_sonnet_s4v2_en.md"),
         ("Monnereau 2009", "papers/ep/kumada1972/monnereau2009/monnereau2009_v184_sonnet_s4v2_en.md"),
         ("Morken 2016", "papers/ep/kumada1972/molken2016/molken2016_v184_sonnet_s4v2_en.md"),
         ("Li (Pengfei) 2024", "papers/ep/kumada1972/pengfei2024/pengfei2024_v184_sonnet_s4v2_en.md"),
         ("Tamao 2002 mini-review", "papers/ep/discussion/tamao2002/tamao2002_v184_sonnet_s4v2_en.md")]
for p, f in CASES:
    PART_A.append((f"A:case-{Path(f).parent.name}", p, f))
CONTEXT = [("Uchino 1970", "papers/dev/uchino/uchino1970_v184_sonnet_s4v6.md"),
           ("Terao-Kambe 2002", "papers/dev/terao2002/terao2002_v184_sonnet_s4v6.md"),
           ("Jones-Vicic 2005", "papers/dev/jones2005/jones2005_v184_sonnet_s4v6.md"),
           ("Martin-Buchwald 2007", "papers/dev/martin2007/martin2007_v184_sonnet_s4v6.md")]
for p, f in CONTEXT:
    PART_A.append((f"A:context-{Path(f).stem.split('_')[0]}", p, f))
assert len(PART_A) == 37, len(PART_A)

PART_A_SKIPS: dict[str, Counter] = {}
for aid, paper, f in PART_A:
    pv, mi = header(f)
    dp = deposit_path(f)
    slots, skipped = parse_slots(f)
    PART_A_SKIPS[aid] = skipped
    for c in slots:
        add(part="A", record_set="A_primary_37", analysis_id=aid, paper_analysed=paper, ep=c["ep"],
            slot=c["slot"], stage4_version=pv, model=model_short(mi), model_info_verbatim=mi,
            cand_first_author=c["first_author"], cand_year=c["year"], cand_journal=c["journal"],
            cand_doi_proposed=c["doi"], cand_specificity=c["specificity"], cand_text=c["text"][:220],
            bib_check="not_checked", content_check="not_checked",
            unclassifiable_reason="no candidate-level verification record exists for this analysis",
            evidence_file=f, evidence_line=c["line"], in_deposit=dp,
            verification_record="", verification_record_line="", notes="")

# ----------------------------------------------------------------------------------------------
# PART B — verification records
# ----------------------------------------------------------------------------------------------


def hand(record_set, analysis_id, paper, afile, find, fa, year, journal, ep, bib, content,
         rec, rec_line, rec_token, notes="", doi="", unit="candidate named in the record"):
    pv, mi = header(afile)
    ln = find_line(afile, find) if find else 0
    txt = lines(afile)[ln - 1].strip()[:220] if ln else ""
    if not doi and ln:
        dm = DOI.search(lines(afile)[ln - 1])
        doi = dm.group(0) if dm else ""
    assert_record(rec, rec_line, rec_token)
    add(part="B", record_set=record_set, analysis_id=analysis_id, paper_analysed=paper, ep=ep, slot=unit,
        stage4_version=pv or ("v18.2 S0-S2 + Stage 4 v3 (per record; file has no header)" if "gpt55" in record_set else ""),
        model=model_short(mi) if mi else ("GPT-5.5 Thinking (per record; file has no header)" if "gpt55" in record_set else "unknown"),
        model_info_verbatim=mi, cand_first_author=fa,
        cand_year=year, cand_journal=journal, cand_doi_proposed=doi,
        cand_specificity="specific" if (fa and year and journal) else "partial", cand_text=txt,
        bib_check=bib, content_check=content, evidence_file=afile, evidence_line=ln or "NOT FOUND",
        in_deposit=deposit_path(afile), verification_record=rec, verification_record_line=rec_line, notes=notes)
    if not ln:
        CHECKS.append(f"{record_set}/{analysis_id}: candidate {fa} {year} named in record not found in {afile}")


# B1 — Kumada 1972, v18.2 S0–S2 + Stage 4 v3, Sonnet 4.6 vs GPT-5.5 Thinking (record: cross_model_v182_comparison.md §5)
R = "papers/dev/kumada/cross_model_v182_comparison.md"
SK = "papers/dev/kumada/kumada_v182_sonnet_s4v3.md"
for find, fa, yr, jr, bib, ln, tok, note in [
    (r"Tamao, Sumitani, Hayashi, Kumada", "Tamao", "1976", "J. Am. Chem. Soc.", "not_resolved", 110, "存在しない",
     "author-combination fabrication (record §5.2)"),
    (r"Hayashi, Tajika, Tamao, Kumada", "Hayashi", "1976", "J. Am. Chem. Soc.", "resolved", 111, "ja00428a061",
     "real (record §5.2); record makes no content judgement"),
    (r"Nagase, Hayashi, Kumada", "Nagase", "1973", "Tetrahedron Lett.", "not_resolved", 112, "存在しない",
     "author-combination fabrication; year given as '1973または1974'"),
    (r"Hayashi, Kumada, \*Tetrahedron Lett\.\* 1974", "Hayashi", "1974", "Tetrahedron Lett.", "insufficient", 113, "検証不可", "hedged ('1974前後')"),
    (r"Kumada, \*Pure Appl\. Chem\.\* 1980", "Kumada", "1980", "Pure Appl. Chem.", "insufficient", 114, "検証不可", "generic ('または関連レビュー')"),
    (r"Corriu et al\. \*J\. Organomet\. Chem\.\* 1974", "Corriu", "1974", "J. Organomet. Chem.", "insufficient", 115, "検証不可", "year range, no title"),
]:
    hand("B1_kumada_v182_sonnet", "B1:kumada-v182-sonnet-s4v3", "Kumada 1972", SK, find, fa, yr, jr, "", bib,
         "not_checked", R, ln, tok, note)
G5K = "papers/dev/kumada/gpt55thinking/GPT55_Kumada_v182.md"
for find, fa, yr, jr, ln, tok in [
    (r"Tamao, Kiso, Sumitani, Kumada, JACS 1972", "Tamao", "1972", "J. Am. Chem. Soc.", 94, "ja00781a070"),
    (r"Tamao, Zembayashi, Kiso, Kumada, J\. Organomet", "Tamao", "1973", "J. Organomet. Chem.", 95, "82058-6"),
    (r"Kiso, Tamao, Kumada, J\. Organomet", "Kiso", "1973", "J. Organomet. Chem.", 96, "95063-0"),
    (r"Tamao, Sumitani, Kiso, Kumada, Bull\. Chem", "Tamao", "1976", "Bull. Chem. Soc. Jpn.", 97, "bcsj.49.1958"),
    (r"Tamao et al\., Tetrahedron 1982", "Tamao", "1982", "Tetrahedron", 98, "80117-8"),
    (r"Bumagin and Beletskaya", "Bumagin", "1990", "Russ. Chem. Rev.", 99, "ABEH003585"),
    (r"Breitenfeld et al\., Organometallics 2014", "Breitenfeld", "2014", "Organometallics", 100, "om500506y"),
    (r"Tamao et al\., Organic Syntheses 2003", "Kumada", "2003", "Org. Synth.", 101, "os058.22"),
    (r"Tamao.{0,40}2002|Discovery of the cross-coupling", "Tamao", "2002", "J. Organomet. Chem.", 102, "01159-2"),
]:
    hand("B1_kumada_v182_gpt55", "B1:kumada-v182-gpt55", "Kumada 1972", G5K, find, fa, yr, jr, "", "resolved",
         "fills", R, ln, tok, "content judged from title/metadata (star rating in record §5.1), not from full text")

# B2 — Murai 1993, same design (record: papers/dev/murai/cross_model_v182_comparison.md §3)
R = "papers/dev/murai/cross_model_v182_comparison.md"
SM = "papers/dev/murai/murai_v182_sonnet_s4v3.md"
for find, fa, yr, jr, bib, content, ln, tok, note in [
    (r"Kakiuchi, F\.; Sekine.{0,160}1995", "Kakiuchi", "1995", "Bull. Chem. Soc. Jpn.", "resolved", "not_checked", 43, "bcsj.68.62", ""),
    (r"Murai, S\.; Kakiuchi.{0,90}Pure Appl", "Murai", "1994", "Pure Appl. Chem.", "resolved", "not_checked", 44, "pac199466071527", ""),
    (r"Kakiuchi, F\.; Murai, S\. \*Acc\. Chem\. Res\.\*", "Kakiuchi", "2002", "Acc. Chem. Res.", "resolved", "not_checked", 45, "ar960318p", ""),
    (r"Chatani, N\.; Fukuyama", "Chatani", "1998", "J. Am. Chem. Soc.", "corrected", "does_not_fill", 46, "部分 hallucination",
     "paper exists (author order/omission corrected) but the model's content description is wrong (Rh vs actual Ru3(CO)12); "
     "content check fails the 'paper says what the model claims' test; the record calls it a partial hallucination and does not state a retention decision"),
    (r"Balcells, D\.", "Balcells", "2010", "Chem. Rev.", "resolved", "not_checked", 47, "cr900315k", ""),
    (r"Guari, Y\.; Sabo-Etienne", "Guari", "1999", "Eur. J. Inorg. Chem.", "resolved", "not_checked", 48, "1047", ""),
    (r"Ackermann, L\.; Althammer", "Ackermann", "2006", "Angew. Chem. Int. Ed.", "resolved", "not_checked", 49, "anie.200504450", ""),
]:
    hand("B2_murai_v182_sonnet", "B2:murai-v182-sonnet-s4v3", "Murai 1993", SM, find, fa, yr, jr, "", bib, content,
         R, ln, tok, note)
G5M = "papers/dev/murai/gpt55thinking/GPT55_murai_v182.md"
for find, fa, yr, jr, ln, tok in [
    (r"Kakiuchi et al\., Bulletin of the Chemical Society of Japan 1995", "Kakiuchi", "1995", "Bull. Chem. Soc. Jpn.", 57, "bcsj.68.62"),
    (r"Sonoda et al\., Bulletin", "Sonoda", "1997", "Bull. Chem. Soc. Jpn.", 58, "bcsj.70.3117"),
    (r"Matsubara, Koga, Musaev", "Matsubara", "1998", "J. Am. Chem. Soc.", 59, "ja9816943"),
    (r"Guari et al\., Journal of Molecular Catalysis", "Guari", "2004", "J. Mol. Catal. A", 60, "molcata.2003.10.034"),
    (r"Yi.{0,12}Lee", "Yi", "2009", "Organometallics", 61, "om900416k"),
    (r"Kakiuchi, Kochi, Mizushima", "Kakiuchi", "2010", "J. Am. Chem. Soc.", 62, "ja104918f"),
    (r"Rouquet", "Rouquet", "2013", "Chem. Sci.", 63, "c3sc50310k"),
    (r"Lei et al\., Science in China", "Lei", "2000", "Sci. China B", 64, "bf02969447"),
]:
    hand("B2_murai_v182_gpt55", "B2:murai-v182-gpt55", "Murai 1993", G5M, find, fa, yr, jr, "", "resolved",
         "not_checked", R, ln, tok, "bibliographic check only (record §3.2 has no content column)")

# B3 — EP-03a candidates from Opus 4.7 (v17 S0–S3, Stage 4 v2) and GPT-5.4 Thinking (v17, Stage 4 v2)
#      records: tier_5 .../ep03a_wos_llm/verification_log.md (+ llm_candidates_ep03a.md, candidate_check_*.txt)
R = "zenodo_deposit_paperA_reviewer_R1_20260928/tier_5_retrieval_logs/retrieval_audit_ep03a_07a_08a_09a/ep03a_wos_llm/verification_log.md"
OP = "papers/dev/kumada/kumada_v17_opus47_s4v2.md"
G54 = "papers/dev/kumada/gpt54thinking/kumada_v17_gpt54thinking_s4.md"
hand("B3_ep03a_audit", "B3:kumada-v17-opus47-s4v2", "Kumada 1972", OP, r"Parshall, J\. Am\. Chem\. Soc\. 96, 2360",
     "Parshall", "1974", "J. Am. Chem. Soc.", "EP-03a", "resolved", "fills", R, 12, "Fully accurate",
     "content verified from PDF; verdict 'Partial' (PEt3 analogue). The DOI later written into llm_candidates_ep03a.md "
     "(10.1021/ja00815a017) is an analyst transcription error: WoS export candidate_check_1 resolves it to a different paper; "
     "the correct record (ja00815a009) is in candidate_check_1b. The model itself gave no DOI.")
hand("B3_ep03a_audit", "B3:kumada-v17-opus47-s4v2", "Kumada 1972", OP, r"Yamamoto, Kohara, Yamamoto, Bull\. Chem\. Soc\. Jpn\. 51, 2091",
     "Yamamoto", "1978", "Bull. Chem. Soc. Jpn.", "EP-03a", "mismatch", "does_not_fill", R, 49, "Triple mismatch",
     "author (Hayashi, not Kohara) + journal/year/volume (the 1978 tuple is a polycondensation paper) + content; library hard copy")
hand("B3_ep03a_audit", "B3:kumada-v17-opus47-s4v2", "Kumada 1972", OP, r"Anderson, Jones, Vicic, J\. Am\. Chem\. Soc\. 126, 8100",
     "Anderson", "2004", "J. Am. Chem. Soc.", "EP-03a", "resolved", "fills", R, 23, "Fully accurate",
     "content verified from PDF (paradigm-shift filler). The DOI written into llm_candidates_ep03a.md (10.1021/ja0488380) is an "
     "analyst transcription error (candidate_check_4 resolves it to Hong/Grubbs); correct DOI ja0483903 in candidate_check_4b.")
hand("B3_ep03a_audit", "B3:kumada-v17-opus47-s4v2", "Kumada 1972", OP, r"Jones, Martin, McMurdo, Vicic",
     "Jones", "2006", "J. Am. Chem. Soc.", "EP-03a", "corrected", "not_checked", R, 39, "Jones-Martin-McFarland",
     "listed under 'Pending verification'; model wrote 'McMurdo' for McFarland (candidate_direct_queries.md)")
hand("B3_ep03a_audit", "B3:kumada-v17-opus47-s4v2", "Kumada 1972", OP, r"^\| 2 \| Morrell, Kochi",
     "Morrell", "1975", "J. Am. Chem. Soc.", "EP-03a", "resolved", "not_checked", R, 38, "PDF available, not yet read",
     "listed under 'Pending verification'. Note: Opus gives a title for this paper (line 55) that is not the real title")
hand("B3_ep03a_audit", "B3:kumada-v17-gpt54-s4", "Kumada 1972", G54, r"充填開始点\*\*: Morrell and Kochi",
     "Morrell", "1975", "J. Am. Chem. Soc.", "EP-03a", "resolved", "not_checked", R, 38, "PDF available, not yet read",
     "listed under 'Pending verification'")
hand("B3_ep03a_audit", "B3:kumada-v17-gpt54-s4", "Kumada 1972", G54, r"充填確立点\*\*: Dawson et al",
     "Dawson", "2020", "Chem. Eur. J.", "EP-03a", "resolved", "not_checked", R, 40, "Dawson 2020",
     "listed under 'Pending verification'. The page '8002' in llm_candidates_ep03a.md / stage4_literature_update is an analyst "
     "addition; the WoS export candidate_check_6 gives p. 3044. The model gave no page.")

# B4 — GPT-5.4 candidates that the 2026-04-19 literature-update memo records as DOI-verified (2026-04-22)
R = "manuscript_A/DigitalDiscovery_R1/01_response/r33b_candidates/records/stage4_literature_update_20260419.md"   # copy of improvements/stage4_literature_update_20260419.md
hand("B4_lit_update_gpt54", "B3:kumada-v17-gpt54-s4", "Kumada 1972", G54, r"充填開始点\*\*: Tamao et al\., \*J\. Organomet\. Chem\.\* 1973",
     "Tamao", "1973", "J. Organomet. Chem.", "EP-04a", "corrected", "fills", R, 64, "author corrected 2026-04-22",
     "record says GPT-5.4's output named the third author 'Sumitani'; the deposited GPT-5.4 Stage 4 output names only "
     "'Tamao et al.' (with a correct ScienceDirect link), so the corrected error is not visible in this file")
hand("B4_lit_update_gpt54", "B3:kumada-v17-gpt54-s4", "Kumada 1972", G54, r"充填確立点\*\*: Chen et al\., \*J\. Am\. Chem\. Soc\.\* 2019",
     "Chen", "2019", "J. Am. Chem. Soc.", "EP-10a", "corrected", "fills", R, 116, "errors corrected 2026-04-22",
     "record says the original attribution had a fabricated author list and '141, 18'; the deposited GPT-5.4 Stage 4 output "
     "gives only 'Chen et al., J. Am. Chem. Soc. 2019' with a correct DOI link, so the corrected error is not visible in this file")

# B5 — Kumada 1972 retrieval-depth runs (v17 S0–S3; Stage 4 v2/v6), retrieval-depth verification record
R = "manuscript_A/DigitalDiscovery_R1/01_response/r33b_candidates/records/kumada_retrieval_depth_verification_extract.md"   # line-preserving extract (records/make_extracts.py)
SON = {"v2P2": f"{K}/kumada_v17_sonnet_s4v2_retrieval_depth.md", "v2R2": f"{K}/kumada_v17_sonnet_s4v2_retrieval_depth_run2.md",
       "v2R3": f"{K}/kumada_v17_sonnet_s4v2_retrieval_depth_run3.md", "v6P1": f"{K}/kumada_v17_sonnet_s4v6_retrieval_depth.md",
       "v6R2": f"{K}/kumada_v17_sonnet_s4v6_retrieval_depth_run2.md", "v6R3": f"{K}/kumada_v17_sonnet_s4v6_retrieval_depth_run3.md"}
SON_ORDER = ["v2P2", "v2R2", "v2R3", "v6P1", "v6R2", "v6R3"]
# candidate id -> (find regex, first author, year, journal, bib, content, verdict line, token, matrix line, note)
SON_C = OrderedDict([
    ("C1", (r"Bull\.? ?Chem\.? ?Soc\.? ?J(pn|apan)", "Tamao", "1976", "Bull. Chem. Soc. Jpn.", "resolved", "not_checked", 614, "bcsj.49.1958", 629, "")),
    ("C2", (r"Tsou", "Tsou", "1979", "J. Am. Chem. Soc.", "resolved", "not_checked", 615, "ja00519a015", 630, "")),
    ("C6", (r"Corriu", "Corriu", "1972", "J. Chem. Soc., Chem. Commun.", "resolved", "not_checked", 616, "c3972000144a", 631, "")),
    ("C8", (r"Tajika|3718", "Hayashi", "1976", "J. Am. Chem. Soc.", "resolved", "not_checked", 617, "ja00428a061", 632,
            "an earlier section of the same record (§11.6, l.520–522) reports this tuple as unconfirmed; §13.2 confirms it")),
    ("C20", (r"Uchino", "Uchino", "1970", "J. Organomet. Chem.", "not_checked", "not_checked", 622, "未確認", 633, "")),
    ("C12", (r"Komiya", "Komiya", "1983", "Organometallics", "resolved", "does_not_fill", 618, "ligand 誤同定", 634,
             "ligand is dmpe, not dppe as the model claimed (record §10.2 #2)")),
    ("C13", (r"9268", "Tamao", "1972", "J. Am. Chem. Soc.", "resolved", "does_not_fill", 619, "主題違い", 635,
             "paper is on alkyl-group isomerization, not the cis/trans question the model claimed")),
    ("C14", (r"Smith[^\n]{0,30}Kochi", "Smith", "1976", "J. Org. Chem.", "resolved", "does_not_fill", 620, "Fe catalysis", 636,
             "iron, not nickel catalysis")),
    ("C15", (r"Knochel|Devasagayaraj", "Devasagayaraj", "1995", "Angew. Chem. Int. Ed.", "resolved", "fills", 621, "Knochel", 637,
             "record §10.2 #5 validates it as the EP-07a paradigm-shift filler")),
    ("G1", (r"Corriu[^\n]{0,80}(続報|Full Paper|continuation|J\. Organomet|197[3-6])", "Corriu", "1973-75", "J. Organomet. Chem.",
            "not_resolved", "not_checked", 623, "不在", 638,
            "'Corriu group continuation': record §10.2 #6 found no such paper; the model had itself marked the citation uncertain")),
])
assert_record(R, 627, "| Candidate | v2 P2")
for cid, (find, fa, yr, jr, bib, content, vl, vtok, ml, note) in SON_C.items():
    assert_record(R, vl, vtok)
    cells = [c.strip() for c in lines(R)[ml - 1].split("|")[2:8]]
    for run, cell in zip(SON_ORDER, cells):
        if not cell.startswith("✓"):
            continue
        hand("B5_kumada_retrieval_depth_sonnet", f"B5:kumada-v17-sonnet-{run}", "Kumada 1972", SON[run], find, fa, yr, jr, "",
             bib, content, R, ml, cell, note, unit="candidate identity per run (record §13.3 matrix)")
# Pilot 1 inline starter and Pilot 2 / baseline author-list checks
hand("B5_kumada_retrieval_depth_sonnet", "B5:kumada-v17-sonnet-v6P1", "Kumada 1972", SON["v6P1"], r"1971[^\n]{0,30}44|44[^\n]{0,10}1505|bcsj\.44",
     "Yamamoto", "1971", "Bull. Chem. Soc. Jpn.", "EP-03a", "not_resolved", "not_checked", R, 274, "citation f",
     "predicted DOI 10.1246/bcsj.44.1505 does not exist; related work is JACS 93, 3350", unit="inline-mentioned starter (record §10.2 #7)")
BASE = f"{K}/kumada_v17_sonnet_s4v2.md"
assert_record(R, 448, "Kiso が欠落")
for find, fa, yr, jr, bib, ln, tok, note in [
    (r"Bull\.? ?Chem\.? ?Soc\.? ?J(pn|apan)", "Tamao", "1976", "Bull. Chem. Soc. Jpn.", "corrected", 448, "Kiso", "author list omits Kiso"),
    (r"Tsou", "Tsou", "1979", "J. Am. Chem. Soc.", "resolved", 615, "ja00519a015", "C2 verdict (§13.2)"),
    (r"Tajika|3718", "Hayashi", "1976", "J. Am. Chem. Soc.", "resolved", 617, "ja00428a061",
     "§11.6 (l.520) first reported the predicted DOI as resolving to an unrelated paper; §13.2 later confirms the paper"),
    (r"Corriu", "Corriu", "1975", "J. Organomet. Chem.", "not_checked", 413, "Corriu-Moreau", "Corriu-Moreau 1975: named in record, not checked"),
    (r"Yamamoto[^\n]{0,40}Ishii|Ishii", "Yamamoto", "1979", "J. Am. Chem. Soc.", "not_checked", 421, "Yamamoto-Ishii-Tanaka", "named in record, not checked"),
    (r"Pure Appl", "Kumada", "1980", "Pure Appl. Chem.", "not_checked", 422, "Pure Appl. Chem. 1980", "review; record marks it '(review, excluded)'"),
]:
    hand("B5_kumada_retrieval_depth_sonnet", "B5:kumada-v17-sonnet-s4v2-baseline", "Kumada 1972", BASE, find, fa, yr, jr, "",
         bib, "not_checked", R, ln, tok, note, unit="candidate named in record §11.3")
assert_record(R, 447, "Okumura")
hand("B5_kumada_retrieval_depth_sonnet", "B5:kumada-v17-sonnet-v2P2", "Kumada 1972", SON["v2P2"], r"Okumura|Hayashi, T\.; Zembayashi",
     "Tamao", "1976", "Bull. Chem. Soc. Jpn.", "", "corrected", "not_checked", R, 447, "Okumura",
     "author-list errors (Hayashi for Kiso, Okumura for Minato) recorded for this run's Tamao 1976 citation; "
     "this row annotates the same C1 occurrence already counted above and is NOT counted again",
     unit="annotation (not counted)")
ROWS[-1]["status"] = "annotation"; ROWS[-1]["status_bib_only"] = "annotation"

# GPT-5.4 Thinking, 6 runs (record §15.3 matrix, §15.4 / §13.2 / §10.2 / §15.6 verdicts)
GPT = {"v2R1": f"{K}/gpt54thinking/kumada_v17_gpt54thinking_s4v2_retrieval_depth_run1.md",
       "v2R2": f"{K}/gpt54thinking/kumada_v17_gpt54thinking_s4v2_retrieval_depth_run2.md",
       "v2R3": f"{K}/gpt54thinking/kumada_v17_gpt54thinking_s4v2_retrieval_depth_run3.md",
       "v6R1": f"{K}/gpt54thinking/kumada_v17_gpt54thinking_s4v6_retrieval_depth_run1.md",
       "v6R2": f"{K}/gpt54thinking/kumada_v17_gpt54thinking_s4v6_retrieval_depth_run2.md",
       "v6R3": f"{K}/gpt54thinking/kumada_v17_gpt54thinking_s4v6_retrieval_depth_run3.md"}
GPT_ORDER = ["v2R1", "v2R2", "v2R3", "v6R1", "v6R2", "v6R3"]
assert_record(R, 920, "未検証の新規候補")
GPT_C = OrderedDict([
    ("C1", (r"Bull\.? ?Chem\.? ?Soc\.? ?J(pn|apan)|bcsj\.49", "Tamao", "1976", "Bull. Chem. Soc. Jpn.", "resolved", "not_checked", 614, "bcsj.49.1958", 895, "")),
    ("C6", (r"Corriu", "Corriu", "1972", "J. Chem. Soc., Chem. Commun.", "resolved", "not_checked", 616, "c3972000144a", 896, "")),
    ("NEW1", (r"82058|C91|Stereochemistry of the nickel", "Tamao", "1973", "J. Organomet. Chem.", "resolved", "not_checked", 916, "verified clean", 897, "")),
    ("NEW3", (r"Mor{1,2}ell", "Morrell", "1975", "J. Am. Chem. Soc.", "resolved", "not_checked", 917, "verified clean", 898, "")),
    ("NEW2", (r"95063|C12|nature of halides|halide", "Kiso", "1973", "J. Organomet. Chem.", "not_checked", "not_checked", 920, "NEW2", 899, "")),
    ("C13", (r"9268|ja00781a070|isomerization", "Tamao", "1972", "J. Am. Chem. Soc.", "resolved", "fills", 960, "correctly identified", 900,
             "bibliographic verdict from record §10.2 #3; record §15.6 says GPT-5.4 described the topic correctly")),
    ("NEW4", (r"Org(anic)?\.? ?Synth", "Kumada", "1978", "Org. Synth.", "not_checked", "not_checked", 920, "NEW4", 901, "")),
    ("C2", (r"Tsou", "Tsou", "1979", "J. Am. Chem. Soc.", "resolved", "not_checked", 918, "both verified", 902, "")),
    ("NEW5", (r"Tetrahedron[^\n]{0,20}1982|1982[^\n]{0,40}Tetrahedron|3347", "Tamao", "1982", "Tetrahedron", "not_checked", "not_checked", 920, "NEW5", 903, "")),
    ("NEW7", (r"Matsubara", "Matsubara", "2017", "Organometallics", "not_checked", "not_checked", 920, "NEW7", 904, "")),
    ("NEW6", (r"Smith[^\n]{0,40}Kochi|Kochi[^\n]{0,40}1980", "Smith", "1980", "J. Organomet. Chem.", "not_checked", "not_checked", 920, "NEW6", 905, "")),
    ("NEW8", (r"Zembayashi[^\n]{0,160}1975|1975[^\n]{0,40}Tetrahedron Lett", "Zembayashi", "1975", "Tetrahedron Lett.", "not_checked", "not_checked", 920, "NEW8", 906, "")),
])
for cid, (find, fa, yr, jr, bib, content, vl, vtok, ml, note) in GPT_C.items():
    assert_record(R, vl, vtok)
    cells = [c.strip() for c in lines(R)[ml - 1].split("|")[2:8]]
    for run, cell in zip(GPT_ORDER, cells):
        if not cell.startswith("✓"):
            continue
        hand("B5_kumada_retrieval_depth_gpt54", f"B5:kumada-v17-gpt54-{run}", "Kumada 1972", GPT[run], find, fa, yr, jr, "",
             bib, content, R, ml, cell, note or ("record lists it as not yet verified (§15.4)" if bib == "not_checked" else ""),
             unit="candidate identity per run (record §15.3 matrix)")

# Haiku 4.5, v2 run 1 (record §16.2.2)
HK = f"{K}/kumada_v17_haiku_s4v2_retrieval_depth_run1.md"
for find, fa, yr, jr, bib, ln, tok, note in [
    (r"Yamamoto, K\., Hayashi, T\., & Kumada", "Yamamoto", "1973", "J. Organomet. Chem.", "not_checked", 1123, "likely fabricated", "record: 'unconfirmed, likely fabricated' - no resolution check recorded"),
    (r"Yamamoto, K\., Matsumura", "Yamamoto", "1975", "J. Organomet. Chem.", "not_checked", 1124, "likely fabricated", "record: 'likely fabricated' - no resolution check recorded"),
    (r"Kumada, M\., Tamao, K\., & Sumitani, K\. \(1974\)", "Kumada", "1974", "J. Organomet. Chem.", "not_checked", 1125, "likely fabricated", "record: 'likely fabricated' - no resolution check recorded"),
    (r"Tamao, K\., Yamamoto, H\., & Kumada", "Tamao", "1977", "Chem. Lett.", "not_checked", 1126, "likely fabricated", "record: 'likely fabricated' - no resolution check recorded"),
    (r"4173-4181", "Tamao", "1976", "J. Am. Chem. Soc.", "mismatch", 1127, "重大誤り", "journal, volume and pages wrong (real paper is BCSJ 49, 1958)"),
    (r"Kumada, M\., & Tamao, K\. \(1982\)", "Kumada", "1982", "Adv. Organomet. Chem.", "not_checked", 1128, "likely fabricated", "record: 'likely fabricated review' - no resolution check recorded"),
]:
    hand("B5_kumada_retrieval_depth_haiku", "B5:kumada-v17-haiku-v2R1", "Kumada 1972", HK, find, fa, yr, jr, "", bib,
         "not_checked", R, ln, tok, note, unit="candidate named in record §16.2.2")

# B6 — Murai 1993 multi-run (v17 S0–S3; Stage 4 v2/v6; 3 Claude models x 3 runs) — TSVs cover all candidates
MR = "papers/dev/murai/multirun"
cand = list(csv.DictReader(open(ROOT / MR / "murai_multirun_candidates.tsv", encoding="utf-8"), delimiter="\t"))
ver = {}
for i, r in enumerate(csv.DictReader(open(ROOT / MR / "murai_multirun_verifications.tsv", encoding="utf-8"), delimiter="\t")):
    ver[(r["first_author"], r["year"])] = (r, i + 2)


def shell(paper: str, year: str) -> str:
    """Normalised bibliographic shell: journal letters before the year + first two numbers after it."""
    k = paper.find(year)
    pre = re.sub(r"[^A-Za-z]", "", paper[max(0, k - 40):k])[-14:]
    nums = re.findall(r"\d+", paper[k + 4:])[:2]
    return f"{pre}|{'|'.join(nums)}"


bins = defaultdict(set)
for r in cand:
    bins[(r["first_author"], r["year"])].add(shell(r["paper"], r["year"]))
n_real = n_fake = 0
for r in cand:
    f = f"{MR}/murai_v17_{r['vendor']}_s4{r['prompt']}_retrieval_depth_run{r['run']}.md"
    key = (r["first_author"], r["year"])
    v, vline = ver.get(key, (None, ""))
    note = ""
    if v is None:
        bib = "not_checked"; note = "no verdict row for this author-year"
    else:
        real = v["real"] == "True"
        n_real += real; n_fake += (not real)
        if len(bins[key]) > 1:
            nums = re.findall(r"\d+", r["paper"][r["paper"].find(r["year"]) + 4:])[:2]
            if real and nums and all(n in v["note"] for n in nums):
                bib = "resolved"; note = f"author-year bin has {len(bins[key])} distinct shells; verdict note names this shell"
            else:
                bib = "insufficient"
                note = (f"verdict is keyed to author-year bin {key} that holds {len(bins[key])} distinct citation shells; "
                        f"cannot be attributed to this shell (see RECOUNT_NOTE_20260829.md)")
        else:
            bib = "resolved" if real else "not_resolved"
            if real and re.search(r"different|closely|though|but with", v["note"], re.I):
                bib = "corrected"; note = "record: real paper exists but with different metadata"
    pv, mi = header(f)
    ln = find_line(f, re.escape(r["first_author"]) + r"[^\n]{0,400}" + r["year"], prefer=None)
    if not ln:   # fallback: first page number of the shell on a line that also carries the year or the author
        nums = re.findall(r"\d+", r["paper"][r["paper"].find(r["year"]) + 4:])[:2]
        for n in reversed(nums):
            ln = find_line(f, rf"(?<!\d){n}(?!\d)[^\n]*" + "|".join([r["year"], re.escape(r["first_author"])]), prefer=None) \
                if False else find_line(f, rf"(?=[^\n]*(?<!\d){n}(?!\d))(?=[^\n]*({r['year']}|{re.escape(r['first_author'])}))", prefer=None)
            if ln:
                break
    add(part="B", record_set="B6_murai_multirun", analysis_id=f"B6:murai-v17-{r['vendor']}-{r['prompt']}-run{r['run']}",
        paper_analysed="Murai 1993", ep=r["ep_filled"], slot="candidate row in murai_multirun_candidates.tsv",
        stage4_version=pv or f"stage4-{r['prompt']}", model=model_short(mi), model_info_verbatim=mi,
        cand_first_author=r["first_author"], cand_year=r["year"], cand_journal="", cand_doi_proposed="",
        cand_specificity="specific", cand_text=r["paper"][:220], bib_check=bib, content_check="not_checked",
        evidence_file=f, evidence_line=ln or "NOT FOUND", in_deposit=deposit_path(f),
        verification_record=f"{MR}/murai_multirun_verifications.tsv", verification_record_line=vline, notes=note,
        unclassifiable_reason=("verdict is keyed to an author-year bin holding several citation shells; it cannot be "
                               "attributed to this shell" if "cannot be attributed" in note else ""))
n_tsv_real = sum(1 for r in cand if ver.get((r["first_author"], r["year"]), ({"real": ""},))[0]["real"] == "True")
CHECKS.append(f"B6 Murai multi-run: {len(cand)} candidate rows; verdict 'real' attaches to {n_tsv_real} and 'fabricated' to "
              f"{len(cand) - n_tsv_real} rows by author-year join (the summary memo reports 101 real / 24 fabricated); "
              f"{sum(1 for k, s in bins.items() if len(s) > 1)} author-year bins contain >1 citation shell")

# B7 — Stage 4 exemplar-control (post-submission; Sonnet 4.6; Stage 4 v6 and v6-decon; 10 runs) — §C lists, Crossref
EX = "papers/dev/kumada/s4_exemplar_control_2026-08"
adj = json.load(open(ROOT / EX / "crossref_adjudication.json", encoding="utf-8"))
adj_line = {}
raw_json = (ROOT / EX / "crossref_adjudication.json").read_text(encoding="utf-8")
for a in adj:
    pos = raw_json.find(json.dumps(a["key"], ensure_ascii=False))
    adj_line[a["key"]] = raw_json[:pos].count("\n") + 1 if pos >= 0 else ""
MAP = {"RESOLVED": ("resolved", ""), "BIB_ERROR": ("mismatch", ""), "FABRICATED": ("not_resolved", ""),
       "UNVERIFIABLE": ("insufficient", ""), "INCOMPLETE": ("insufficient", "")}
arm_counts = Counter()
for f in sorted((ROOT / EX).glob("kumada_s4v6_arm*_run*.md")):
    rel = str(f.relative_to(ROOT))
    arm = re.search(r"arm([AB])", f.name).group(1)
    s, e = section(rel, r"^#+\s*§C", r"^#+\s*§D")
    L = lines(rel)
    for i in range(s, e):
        l = L[i]
        if not re.match(r"^\|\s*\d+\s*\|", l):
            continue
        cell = l.split("|")[2].strip()
        c = parse_citation(cell.replace("⚠️", "").strip())
        fa, yr = c["first_author"], c["year"] or "?"
        same = [a for a in adj if a["key"].split("|")[0] == fa and a["key"].split("|")[1] == yr]
        if not same:   # citations the adjudication keyed without a year (e.g. '1970年代', '1975頃')
            same = [a for a in adj if a["key"].split("|")[0] == fa and a["key"].split("|")[1] == "?"]
        if len(same) > 1:
            pg = [a for a in same if a["key"].split("|")[3] and a["key"].split("|")[3] in cell]
            same = pg if pg else [a for a in same if not a["key"].split("|")[3]] or same
        a = same[0] if len(same) == 1 else None
        if a is None:
            CHECKS.append(f"B7: {rel}:{i+1} could not be matched to an adjudication key: {cell[:70]}")
            bib, akey = "not_checked", ""
        else:
            bib, akey = MAP[a["status"]][0], a["key"]
            arm_counts[(akey, arm)] += 1
        note = (a.get("adjudication", "") if a else "")
        if a and "上記と同一" in a["raw"]:
            note = "duplicate of an earlier row in the same §C list ('上記と同一'); adjudicated UNVERIFIABLE"
        pv, mi = header(rel)
        runtag = re.search(r"run\d+", f.name).group(0)
        add(part="B", record_set="B7_exemplar_control", analysis_id=f"B7:kumada-s4v6-arm{arm}-{runtag}",
            paper_analysed="Kumada 1972", ep="", slot="§C recommended-list row", stage4_version=(pv or "stage4-v6") + ("" if arm == "A" else " [arm B: decontaminated copy; header tag unchanged]"),
            model=model_short(mi) if mi else "Sonnet 4.6 (per Methods 6)", model_info_verbatim=mi,
            cand_first_author=fa, cand_year=c["year"], cand_journal=c["journal"], cand_doi_proposed=c["doi"],
            cand_specificity=c["specificity"], cand_text=cell[:220], bib_check=bib, content_check="not_checked",
            evidence_file=rel, evidence_line=i + 1, in_deposit=deposit_path(rel),
            verification_record=f"{EX}/crossref_adjudication.json", verification_record_line=adj_line.get(akey, ""),
            notes=f"adjudication key {akey}; status {a['status'] if a else ''}; {note}".strip("; "))
for a in adj:
    if (arm_counts[(a["key"], "A")], arm_counts[(a["key"], "B")]) != (a["A"], a["B"]):
        CHECKS.append(f"B7 count mismatch for {a['key']}: re-derived A={arm_counts[(a['key'],'A')]} B={arm_counts[(a['key'],'B')]} "
                      f"vs json A={a['A']} B={a['B']}")

nf = Counter(r["analysis_id"] for r in ROWS if r.get("evidence_line") == "NOT FOUND")
for a, n in sorted(nf.items()):
    tot = sum(1 for r in ROWS if r["analysis_id"] == a)
    CHECKS.append(f"{a}: {n} of {tot} candidates named in the record/ledger are not found in the deposited analysis file")

# ----------------------------------------------------------------------------------------------
# hint column: same (first author, year) tuple resolved in some Part B record
# ----------------------------------------------------------------------------------------------
resolved_tuples = defaultdict(set)
for r in ROWS:
    if r["part"] == "B" and r["bib_check"] in ("resolved", "corrected") and r["status"] != "annotation":
        resolved_tuples[(r["cand_first_author"], r["cand_year"])].add(r["record_set"])
for r in ROWS:
    r["hint_same_author_year_resolved_in"] = ";".join(sorted(resolved_tuples.get((r["cand_first_author"], r["cand_year"]), set()))) \
        if r["part"] == "A" else ""

# ----------------------------------------------------------------------------------------------
# write CSV + counts
# ----------------------------------------------------------------------------------------------
COLS = ["row_id", "part", "record_set", "analysis_id", "paper_analysed", "ep", "slot", "stage4_version", "model",
        "model_info_verbatim", "cand_first_author", "cand_year", "cand_journal", "cand_doi_proposed", "cand_specificity",
        "status", "retraction_reason", "status_bib_only", "unclassifiable_reason", "bib_check", "content_check",
        "evidence_file", "evidence_line", "in_deposit", "verification_record", "verification_record_line",
        "hint_same_author_year_resolved_in", "notes", "cand_text"]
for i, r in enumerate(ROWS, 1):
    r["row_id"] = i
    for c in COLS:
        r.setdefault(c, "")
with open(OUT_CSV, "w", encoding="utf-8", newline="") as fh:
    w = csv.DictWriter(fh, fieldnames=COLS, extrasaction="ignore")
    w.writeheader()
    w.writerows(ROWS)

counted = [r for r in ROWS if r["status"] != "annotation"]


def tally(rows, key="status"):
    c = Counter(r[key] for r in rows)
    return {k: c.get(k, 0) for k in ("retained", "retracted", "unclassifiable")} | {"total": len(rows)}


per_analysis = OrderedDict()
for r in counted:
    per_analysis.setdefault(r["analysis_id"], []).append(r)
out = {
    "part_A": {"analyses": len(PART_A), "strict": tally([r for r in counted if r["part"] == "A"]),
               "slots_skipped": dict(sum(PART_A_SKIPS.values(), Counter())),
               "analyses_with_zero_parsed_candidates": [a for a, _, _ in PART_A if a not in per_analysis]},
    "part_B": {"strict": tally([r for r in counted if r["part"] == "B"]),
               "bib_only": tally([r for r in counted if r["part"] == "B"], "status_bib_only")},
    "part_B_by_record_set": {rs: {"strict": tally(v), "bib_only": tally(v, "status_bib_only"),
                                  "analyses": len({r["analysis_id"] for r in v})}
                             for rs, v in sorted(defaultdict(list, {k: [r for r in counted if r["record_set"] == k]
                                                                  for k in {r["record_set"] for r in counted if r["part"] == "B"}}).items())},
    "retraction_reasons": dict(Counter(r["retraction_reason"] for r in counted if r["status"] == "retracted")),
    "retained_with_correction": sum(1 for r in counted if r["status"] == "retained" and r["bib_check"] == "corrected"),
    "unclassifiable_reasons": dict(Counter(r["unclassifiable_reason"] for r in counted if r["status"] == "unclassifiable")),
    "per_analysis": {a: {"paper": v[0]["paper_analysed"], "stage4_version": v[0]["stage4_version"], "model": v[0]["model"],
                         **tally(v), "bib_only_retained": sum(1 for r in v if r["status_bib_only"] == "retained")}
                     for a, v in per_analysis.items()},
    "part_B_context_all_slots_in_analysis": {a: len(parse_slots(v[0]["evidence_file"])[0])
                                              for a, v in per_analysis.items()
                                              if v[0]["part"] == "B" and v[0]["record_set"] not in ("B6_murai_multirun", "B7_exemplar_control")},
    "part_A_hint_rows": sum(1 for r in counted if r["part"] == "A" and r["hint_same_author_year_resolved_in"]),
    "checks": CHECKS,
}
OUT_JSON.write_text(json.dumps(out, ensure_ascii=False, indent=1), encoding="utf-8")
print(json.dumps({k: out[k] for k in ("part_A", "part_B", "retraction_reasons", "retained_with_correction")}, ensure_ascii=False, indent=1))
print("by record set:")
for rs, v in out["part_B_by_record_set"].items():
    print(f"  {rs:38s} analyses={v['analyses']:3d} strict={v['strict']} bib_only={v['bib_only']}")
print("checks:")
for c in CHECKS:
    print("  -", c)
