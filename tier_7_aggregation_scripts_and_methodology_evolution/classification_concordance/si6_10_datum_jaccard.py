#!/usr/bin/env python3
"""Recompute the SI-6.10 table (datum-selection agreement, within one model vs across models) from the deposited runs.

Run from the root of the deposit:
    python3 tier_7_aggregation_scripts_and_methodology_evolution/classification_concordance/si6_10_datum_jaccard.py
Needs Python 3.9+ and rapidfuzz (`pip install rapidfuzz`). Calls classification_concordance.py (the matcher: datums matched by
fuzzy agreement of the quoted text, threshold 88; signatures shorter than 30 characters excluded) on the five Claude Haiku 4.5
and five Claude Sonnet 4.6 Stage 1 Turn 4 outputs, then prints the mean and sample SD of the per-pair Jaccard index,
matched / (matched + only_a + only_b). (The matcher's own printed summary is a pooled Jaccard, which differs.)
haiku45_2026-09/_deviation_prompt_lookahead/ holds superseded runs and is not used.
"""
import json, os, statistics, subprocess, sys, tempfile

HERE = os.path.dirname(os.path.abspath(__file__))
ARM_A = "papers/dev/kumada/haiku45_2026-09/kumada_v184_haiku45_run*_s1.md"
ARM_B = "papers/dev/kumada/repro_2026-07/kumada_v184_sonnet46_repro_run*_s1.md"
with tempfile.TemporaryDirectory() as td:
    out = os.path.join(td, "pairs.json")
    subprocess.run([sys.executable, os.path.join(HERE, "classification_concordance.py"), ARM_A, ARM_B,
                    "--label-a", "haiku45", "--label-b", "sonnet46", "--json", out], check=True, stdout=subprocess.DEVNULL)
    pairs = json.load(open(out))
print("| Comparison | Pairs | Mean pairwise datum Jaccard |")
print("|---|---|---|")
for name, key in (("Within Claude Haiku 4.5", "within_a"), ("Within Claude Sonnet 4.6", "within_b"), ("Across the two models", "cross")):
    j = [r["matched"] / (r["matched"] + r["only_a"] + r["only_b"]) for r in pairs[key]]
    print(f"| {name} | {len(j)} | {statistics.mean(j):.3f} ± {statistics.stdev(j):.3f} |")
