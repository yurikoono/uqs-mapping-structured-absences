#!/usr/bin/env python3
"""Aggregate the v2 re-adjudication (20 runs incl. B2; two raters with separate directories). Run from repo root."""
import json, collections, csv
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
D = _src("manuscript_A/DigitalDiscovery_R1/01_response/d4_baseline", "01_response/d4_baseline")
key = json.load(open(f"{D}/adjudication_v2_key.json"))
a = {x["cell"]: x for x in json.load(open(f"{D}/adjudication_v2_raterA.json"))}
b = {x["cell"]: x for x in json.load(open(f"{D}/adjudication_v2_raterB.json"))}
rows, agree = [], collections.Counter()
for c, k in key.items():
    for lv in ("narrow", "broad"): agree[lv] += a[c][lv] == b[c][lv]
    same = (a[c]["narrow"], a[c]["broad"]) == (b[c]["narrow"], b[c]["broad"])
    rows.append({**k, "cell": c, "narrow": a[c]["narrow"] if same else "", "broad": a[c]["broad"] if same else "", "source": "agree" if same else "DISAGREE"})
with open(_out("manuscript_A/DigitalDiscovery_R1/01_response/d4_baseline", "01_response/d4_baseline") + "/adjudication_v2_final.csv", "w", newline="") as f:
    w = csv.DictWriter(f, fieldnames=list(rows[0])); w.writeheader(); w.writerows(rows)
print("agreement", dict(agree), "of", len(key), "| identical evidence", sum(1 for c in a if a[c]["evidence"] and a[c]["evidence"] == b[c]["evidence"]))
axes = ["homocoupling", "black_precipitate", "exotherm_radical", "stereo_nonspec", "ligand_ranking", "glpc_standard", "ether_thf"]
for lv in ("narrow", "broad"):
    print(f"\n== {lv}")
    for arm, scope in (("uqs_v184", "strict"), ("uqs_v184", "loose"), ("bl0", "loose"), ("bl1", "loose"), ("bl2", "loose")):
        R = [r for r in rows if r["arm"] == arm and r["scope"] == scope]
        runs = [sum(int(r[lv]) for r in R if r["run"] == k) for k in range(1, 6)]
        per = {x: sum(int(r[lv]) for r in R if r["axis"] == x) for x in axes}
        miss = 35 - sum(runs)
        print(f"{arm:9s} {scope:6s} per-run {runs} mean {sum(runs)/5:.1f} | miss {miss}/35 = {100*miss/35:.1f}% | {per}")
