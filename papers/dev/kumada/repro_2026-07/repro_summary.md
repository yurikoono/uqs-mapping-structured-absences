# UQS reproducibility — summary (model-pinned)

## v184  (n=5 valid runs)

| metric | mean ± SD (CV) |
|---|---|
| nA | 2.20 ± 0.45 (CV 0.20) |
| nB | 8.20 ± 1.30 (CV 0.16) |
| nC | 4.20 ± 0.84 (CV 0.20) |
| nU | 2.20 ± 1.10 (CV 0.50) |
| nUcrit | 0.40 ± 0.89 (CV 2.24) |
| nUhigh | 0.60 ± 0.89 (CV 1.49) |
| nD4 | 8.60 ± 0.55 (CV 0.06) |
| canonical strict (final taxonomy + D-4) | 6.60 / 7 (miss 5.71%) |
| canonical loose (anywhere in final artifacts) | 7.00 / 7 (miss 0.00%) |
| scope_type | mode=tool_question, distinct=2 (flips=1) |

_per-run canonical strict/loose:_ 1:7/7 (of 7), 2:7/7 (of 7), 3:6/7 (of 7), 4:6/7 (of 7), 5:7/7 (of 7)

## v19  (n=5 valid runs)

| metric | mean ± SD (CV) |
|---|---|
| nA | 2.60 ± 0.55 (CV 0.21) |
| nB | 7.40 ± 1.67 (CV 0.23) |
| nC | 3.60 ± 0.55 (CV 0.15) |
| nU | 2.20 ± 1.64 (CV 0.75) |
| nUcrit | 0.20 ± 0.45 (CV 2.24) |
| nUhigh | 1.20 ± 1.10 (CV 0.91) |
| nD4 | 7.75 ± 0.50 (CV 0.06) |
| canonical strict (final taxonomy + D-4) | 6.20 / 7 (miss 11.43%) |
| canonical loose (anywhere in final artifacts) | 6.80 / 7 (miss 2.86%) |
| scope_type | mode=tool_question, distinct=1 (flips=0) |

_per-run canonical strict/loose:_ 1:5/6 (of 7), 2:6/7 (of 7), 3:7/7 (of 7), 4:7/7 (of 7), 5:6/7 (of 7)

## Canonical instrument disagreement

_strict=0/loose=1 = surfaced during turns, did not reach the final taxonomy under the axis vocabulary (spot-check whether the taxonomy covers it in other words). loose=0 = genuinely absent from the run's final artifacts._

- strict=0/loose=1 cells: v184/run3:black_precipitate, v184/run4:exotherm_radical, v19/run1:exotherm_radical, v19/run2:exotherm_radical, v19/run5:exotherm_radical
- loose=0 (true absence) cells: v19/run1:ether_thf

## v184 vs v19 — is the difference real or lottery?

_A gap is flagged **REAL** only if |mean gap| > pooled within-version SD (i.e. exceeds run-to-run noise). Otherwise it is within lottery range._

| metric | v184 | v19 | gap | pooled SD | verdict |
|---|---|---|---|---|---|
| nA | 2.20 | 2.60 | 0.40 | 0.50 | within noise |
| nB | 8.20 | 7.40 | 0.80 | 1.50 | within noise |
| nC | 4.20 | 3.60 | 0.60 | 0.71 | within noise |
| nU | 2.20 | 2.20 | 0.00 | 1.40 | within noise |
| nUcrit | 0.40 | 0.20 | 0.20 | 0.71 | within noise |
| nUhigh | 0.60 | 1.20 | 0.60 | 1.00 | within noise |
| nD4 | 8.60 | 7.75 | 0.85 | 0.52 | REAL |

> Interpretation: **REAL** rows are prompt-attributable differences (model is fixed). **within noise** rows mean the apparent difference is a sampling artifact — do NOT register it as a regression.

---

_Canonical coverage is a keyword proxy on two scopes; spot-check the disagreement list before citing any per-finding claim. Rigorous metrics: the count table and scope_type._

**Paper A hook:** report absolute-count claims as `mean ± SD (CV=…)`; use the STRICT miss rate as "probability a single run's final taxonomy omits a canonical finding" and the LOOSE miss rate as "probability it is absent from the run entirely". Relative claims (X > Y) are unaffected; absolute claims carry this error.
