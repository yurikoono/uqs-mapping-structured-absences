# Matcher of SI-6.10 (datum-selection agreement)

- `classification_concordance.py` — the matcher used for SI-6.10 (project path `scripts/classification_concordance.py`; comments in Japanese). It reduces each Stage 1 Turn 4 output to the set of quoted source passages (datums), matches datums across runs by fuzzy agreement of the quoted text and reports agreement within and across two arms. `--selftest` runs its built-in checks.
- `si6_10_datum_jaccard.py` — runs the matcher on the deposited runs (`papers/dev/kumada/haiku45_2026-09/` and `papers/dev/kumada/repro_2026-07/`) and prints the SI-6.10 table (mean ± sample SD of the per-pair Jaccard index).

Run from the root of the deposit (needs `rapidfuzz`):

    python3 tier_7_aggregation_scripts_and_methodology_evolution/classification_concordance/si6_10_datum_jaccard.py

**Public cut.** The datums this script compares are quoted passages of the analysed paper, which are redacted in this
cut, so here it prints different numbers. The SI-6.10 values below (and the matcher's `--selftest`) reproduce only from
the reviewer version of the deposit.

Output at deposit time (2026-10-16, reviewer version):

```
| Comparison | Pairs | Mean pairwise datum Jaccard |
|---|---|---|
| Within Claude Haiku 4.5 | 10 | 0.258 ± 0.090 |
| Within Claude Sonnet 4.6 | 10 | 0.297 ± 0.054 |
| Across the two models | 25 | 0.188 ± 0.090 |
```
