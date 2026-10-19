#!/usr/bin/env python3
"""Aggregate the hand adjudication (rubric adjudication_rubric_20260929.md). Run from repo root."""
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
key = json.load(open(f"{D}/adjudication_key.json"))
r1 = {x["cell"]: x for x in json.load(open(f"{D}/adjudication_rater1.json"))}
r2 = {x["cell"]: x for x in json.load(open(f"{D}/adjudication_rater2.json"))}
orch = {x["cell"]: x for x in json.load(open(f"{D}/adjudication_nocandidate_orchestrator.json"))}
rows, agree, n = [], collections.Counter(), collections.Counter()
for c, k in key.items():
    if c in orch:
        v = orch[c]; src = "orchestrator_fullread"
    else:
        a, b = r1[c], r2[c]
        for lv in ("narrow", "broad"):
            n[lv] += 1; agree[lv] += a[lv] == b[lv]
        v = a if (a["narrow"], a["broad"]) == (b["narrow"], b["broad"]) else None; src = "raters_agree" if v else "DISAGREE"
    rows.append({**k, "cell": c, "narrow": v["narrow"] if v else "", "broad": v["broad"] if v else "", "source": src})
with open(_out("manuscript_A/DigitalDiscovery_R1/01_response/d4_baseline", "01_response/d4_baseline") + "/adjudication_final.csv", "w", newline="") as f:
    w = csv.DictWriter(f, fieldnames=list(rows[0])); w.writeheader(); w.writerows(rows)
print("agreement:", {lv: f"{agree[lv]}/{n[lv]}" for lv in n}, "| disagreements:", sum(r["source"] == "DISAGREE" for r in rows))
axes = ["homocoupling", "black_precipitate", "exotherm_radical", "stereo_nonspec", "ligand_ranking", "glpc_standard", "ether_thf"]
for lv in ("narrow", "broad"):
    print(f"\n== {lv} (present per 5 runs; loose unless noted)")
    for arm, scope in (("uqs_v184", "strict"), ("uqs_v184", "loose"), ("bl0", "loose"), ("bl1", "loose")):
        R = [r for r in rows if r["arm"] == arm and r["scope"] == scope]
        per = {a: sum(int(r[lv]) for r in R if r["axis"] == a) for a in axes}
        runs = [sum(int(r[lv]) for r in R if r["run"] == k) for k in range(1, 6)]
        miss = 35 - sum(per.values())
        print(f"{arm:9s} {scope:6s} per-run {runs} mean {sum(runs)/5:.1f} | miss {miss}/35 = {100*miss/35:.1f}% | {per}")
