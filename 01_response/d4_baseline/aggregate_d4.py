#!/usr/bin/env python3
"""D4 aggregation per prereg §1.3 (commit 88e7cc3). Run from repo root.
Endpoint 1: canon loose (case-insensitive regex over the full output; UQS = s1+s2 as in repro_extract).
Endpoint 2: verbatim quote gate against Kumada_1972.pdf.  Endpoint 4: item count.
Endpoint 3 (specificity) is scored separately by two raters."""
import csv, glob, importlib.util, json, os, re, statistics as st
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
HERE = _out("manuscript_A/DigitalDiscovery_R1/01_response/d4_baseline", "01_response/d4_baseline")
BL = _src("papers/dev/kumada/baseline_R1_2026-09"); RP = _src("papers/dev/kumada/repro_2026-07")
spec = importlib.util.spec_from_file_location("vqg", _src("scripts/verbatim_quote_gate.py", _LIB + "verbatim_quote_gate.py"))
vqg = importlib.util.module_from_spec(spec); spec.loader.exec_module(vqg)
canon = {k: re.compile(v, re.I) for k, v in json.load(open(f"{RP}/canon.json")).items()}
_PDF = _src("papers/dev/kumada/Kumada_1972.pdf")   # source PDF: not deposited; place it here (DOI 10.1021/ja00767a075)
if not _os.path.isfile(_PDF):
    raise SystemExit(f"the quote gate needs the source PDF of Kumada 1972 at {_PDF} (not deposited; obtain it via its DOI)")
refs = {"main": vqg.normalize(vqg.extract_pdf_text(_PDF))}
uqs_counts = {r["run"]: r for r in csv.DictReader(open(f"{RP}/repro_metrics.csv")) if r["ver"] == "v184"}

cells = []
for k in range(1, 6):
    cells.append(("uqs_v184", k, [f"{RP}/kumada_v184_sonnet46_repro_run{k}_s1.md", f"{RP}/kumada_v184_sonnet46_repro_run{k}_s2.md"]))
for arm in ("bl0", "bl1", "bl2"):
    for k in range(1, 6):
        cells.append((arm, k, [f"{BL}/kumada_{arm}_sonnet46_run{k}.md"]))

rows, quotes = [], []
for arm, k, files in cells:
    if not all(os.path.exists(f) for f in files):
        continue
    text = "\n".join(open(f, encoding="utf-8").read() for f in files)
    hits = {a: int(bool(p.search(text))) for a, p in canon.items()}
    qs = []
    for f in files:
        for raw, kind in vqg.harvest_quotes(f):
            status, src, pr, ts = vqg.score_quote(vqg.normalize(raw), refs)
            qs.append((kind, status))
            quotes.append({"arm": arm, "run": k, "status": status, "partial": round(pr, 1), "token_set": round(ts, 1), "kind": kind, "quote": raw[:200]})
    if arm.startswith("bl"):
        n_items = len(re.findall(r"^#{2,4}\s*\d+[.)]", text, re.M)) or len(re.findall(r"^\s*key_quote:", text, re.M))
    else:
        u = uqs_counts[str(k)]; n_items = sum(int(u[c]) for c in ("nA", "nB", "nC", "nU"))  # A+B+C+U from repro_metrics.csv
    rows.append({"arm": arm, "run": k, "canon_loose": sum(hits.values()), **{f"loose_{a}": v for a, v in hits.items()},
                 "n_quotes": len(qs), **{f"{kd}_{s}": sum(1 for q in qs if q == (kd, s)) for kd in ("key_quote", "quoted") for s in ("PASS", "PASS_FUZZY", "PASS_SPLICED", "WARN", "FAIL")},
                 "n_items": n_items})

with open(f"{HERE}/d4_metrics.csv", "w", newline="") as f:
    w = csv.DictWriter(f, fieldnames=list(rows[0])); w.writeheader(); w.writerows(rows)
with open(f"{HERE}/d4_quotes.csv", "w", newline="") as f:
    w = csv.DictWriter(f, fieldnames=list(quotes[0])); w.writeheader(); w.writerows(sorted(quotes, key=lambda q: (q["arm"], q["run"], q["partial"])))
for arm in ("uqs_v184", "bl0", "bl1", "bl2"):
    R = [r for r in rows if r["arm"] == arm]
    if not R: continue
    c = [r["canon_loose"] for r in R]
    def g(kd):
        n = sum(r[f"{kd}_{x}"] for r in R for x in ("PASS", "PASS_FUZZY", "PASS_SPLICED", "WARN", "FAIL"))
        ok = sum(r[f"{kd}_{x}"] for r in R for x in ("PASS", "PASS_FUZZY", "PASS_SPLICED"))
        return f"{kd} {ok}/{n} pass (WARN {sum(r[kd+'_WARN'] for r in R)}, FAIL {sum(r[kd+'_FAIL'] for r in R)})"
    miss = [(r["run"], a[6:]) for r in R for a in r if a.startswith("loose_") and r[a] == 0]
    print(f"{arm}: N={len(R)} canon_loose mean={st.mean(c):.2f} range={min(c)}-{max(c)} | {g('key_quote')} | {g('quoted')} | items {[r['n_items'] for r in R]} | misses {miss}")
