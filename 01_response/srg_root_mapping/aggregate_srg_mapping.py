#!/usr/bin/env python3
"""Aggregate SRG root mapping (rubric_srg_root_mapping.md). Run from repo root."""
import json
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
D = _src("manuscript_A/DigitalDiscovery_R1/01_response/srg_root_mapping", "01_response/srg_root_mapping")
key = json.load(open(f"{D}/srg_blocks_key.json"))
A = {x["block"]: x for x in json.load(open(f"{D}/rater_A.json"))}; B = {x["block"]: x for x in json.load(open(f"{D}/rater_B.json"))}
dis = [b for b in key if sorted(A[b]["roots"]) != sorted(B[b]["roots"])]
print("blocks", len(key), "| identical root sets", len(key) - len(dis), "| disagreements", [(b, key[b]["output"], A[b]["roots"], B[b]["roots"]) for b in dis])
outs = list(dict.fromkeys(v["output"] for v in key.values()))
R = ["R1", "R2", "R3", "R4", "R5", "R6"]
for label, pick in (("agreed only (intersection)", lambda b: set(A[b]["roots"]) & set(B[b]["roots"])), ("either rater (union)", lambda b: set(A[b]["roots"]) | set(B[b]["roots"]))):
    print(f"\n== {label}")
    print(f"{'output':24s} " + " ".join(R) + "  n_blocks")
    for o in outs:
        bl = [b for b in key if key[b]["output"] == o]
        cov = set().union(*[pick(b) for b in bl])
        print(f"{o:24s} " + "  ".join("o" if r in cov else "." for r in R) + f"   {len([b for b in bl if not A[b].get('header')])}")
