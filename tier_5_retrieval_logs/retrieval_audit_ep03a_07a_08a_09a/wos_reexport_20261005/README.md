# WoS re-export, 2026-10-05 — comparison with the 2026-05-20 searches

Executor: author (Hokkaido University subscription), WoS Core Collection, Advanced Search (Query Builder → Query Preview),
query strings verbatim from the per-variant analysis files (`ep{07,08,09}a_wos_llm/wos_variant_*_analysis.md` and `hit_counts.md`), no date limit, all runs on 2026-10-05.
Export format: plain text, tagged fields AU/AF/TI/SO/PY/VL/IS/BP/EP/DI/UT etc. (no AB, CR, ID or FU fields — the
files carry bibliographic facts only; this is sufficient to identify every record and needs no redaction).

## Hit counts

| EP | Variant | 2026-05-20 | 2026-10-05 | Records vs May analysis file |
|---|---|---|---|---|
| EP-07a | A | 9 | 9 | 9/9 identical (`ep07a_wos_variant_a.txt`) |
| EP-07a | B | 0 | 0 | — |
| EP-08a | A | 3 | **2** | 2 of the 3 May records returned; Zhou–Xu–Zhang–Kong 2020 (10.1039/d0qo00901f) not returned (`ep08a_wos_variant_a.txt`) |
| EP-08a | B | 1 | 1 | identical (`ep08a_wos_variant_b.txt`) |
| EP-08a | C | 7 | 7 | 7/7 identical (`ep08a_wos_variant_c.txt`) |
| EP-08a | D / D′ / D″ | 0 / 0 / 0 | 0 / 0 / 0 | — |
| EP-09a | A | 9 | 9 | 9/9 identical (`ep09a_wos_variant_a.txt`) |
| EP-09a | B | 1 | 1 | identical (`ep09a_wos_variant_b.txt`) |
| EP-09a | C | 1 | 1 | identical (`ep09a_wos_variant_c.txt`) |
| EP-09a | D | 0 | 0 | — |

Matching was by DOI or WoS UT against `ep{07,08,09}a_wos_llm/wos_variant_*_analysis.md`
(and, for EP-08a A, the genuine May export `ep08a_wos_llm/wos_variant_a.txt`). No new record appeared.

## The one difference

EP-08a Variant A returned 2 records instead of 3. The missing record, Zhou et al. 2020 (*Org. Chem. Front.*), was
classified **Not applicable** in May (a Highlight on Ni electroreductive coupling; its "reproducibility" keyword
refers to Zn reductant). Why WoS no longer returns it under `DT=(Article)` was not established (a change in the
record's document type or topic indexing is possible but unverified). Because it was not a filler, the EP-08a
result (0 Complete / 0 Partial / 0 Minimal) and every claim that rests on it are unchanged.

## Consequence

The six raw exports lost before deposit are replaced by these re-exports. The 2026-05-20 hit counts and
per-candidate classifications stand; SI-9.8.6 records the one count difference.
