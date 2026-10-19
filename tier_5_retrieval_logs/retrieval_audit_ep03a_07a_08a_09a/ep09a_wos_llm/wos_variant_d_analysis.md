# EP-09a — WoS Variant D Analysis (2026-05-20)

## Query

```
TS=("iron-catalyzed" OR "Fe-catalyzed") AND TS=("nickel-catalyzed" OR "Ni-catalyzed") AND TS=(Grignard OR Kumada) AND TS=("same substrate" OR "matched conditions" OR "benchmark") AND DT=(Article)
```

- Database: WoS Core Collection
- Filter: Document Type = Article
- Date executed: 2026-05-20
- Executor: User (Hokkaido U subscription)
- **Hit count: 0** ("Your search found no results")

This variant targets the Tamura-Kochi Fe-Kumada vs dppe-Ni-Kumada cross-metal benchmark scenario, combined with explicit matched-substrate / matched-conditions / benchmark vocabulary.

## Interpretation

The 0-hit result indicates that **no paper in WoS Core Collection** combines:

- Iron-catalysed OR Fe-catalysed (Tamura-Kochi Fe-Kumada family)
- AND Nickel-catalysed OR Ni-catalysed (Ni-Kumada family)
- AND Grignard OR Kumada
- AND explicit matched-conditions / benchmark language

This is the most direct EP-09a target query — explicit cross-metal head-to-head comparison vocabulary with the two metal families that the Tamura-Kochi (Fe) and Corriu (Ni) named predecessor systems represent. The 0-hit finding is consistent with the EP-09a negative claim at this most chemistry-specific retrieval dimension.

## Summary — Variant D

| Classification | Count |
|---|---|
| Complete filler | **0** |
| Partial filler | **0** |
| Minimal filler | **0** |
| Not applicable | **0** |
| **Total hits** | **0** |

## EP-09a WoS Module — final cumulative summary (4 variants complete)

| Variant | Query target | Hits | Complete | Partial | Minimal | Not applicable |
|---|---|---|---|---|---|---|
| A (strict named-benchmark) | Kumada syntax + Corriu/Masse/Tamura-Kochi/Corey-Whitesides | 9 | 0 | 0 | 2 | 7 |
| B (head-to-head Ni-Grignard vocabulary) | nickel + cross-coupling + benchmark-language + Grignard | 1 | 0 | 0 | 0 | 1 |
| C (comparison language + predecessor terms) | Kumada-Tamao-Corriu + comparison-language + Ni(acac)₂/Fe/stoichiometric | 1 | 0 | 0 | 0 | 1 |
| D (Fe-Kumada vs Ni-Kumada matched) | Fe-cat + Ni-cat + Grignard/Kumada + matched-conditions | 0 | — | — | — | — |
| **EP-09a WoS Module Total** | — | **11** | **0** | **0** | **2** | **9** |

## EP-09a negative claim — final WoS Module diagnostic

Across four orthogonal WoS Variants (strict named-benchmark / head-to-head Ni-Grignard vocabulary / comparison language + predecessor terms / Fe-Kumada vs Ni-Kumada matched-conditions), **structured Web of Science Core Collection retrieval returned 11 candidate papers, none of which provide substrate-matched + condition-matched numerical benchmark of dppe-Ni Kumada against named predecessor catalysts** (Corriu/Masse Ni(acac)₂; Tamura-Kochi Fe; Corey-Whitesides stoichiometric) per 0B §5 Complete or Partial filler criteria.

The 2 Minimal filler candidates (Quesnelle-Snieckus 2018; Berding 2009) sit at the weakest inclusion criteria — qualitative cross-reaction-class comparison and verbal superiority claim respectively, neither providing matched-condition numerical data.

This independently triangulates:
- Cross-model LLM-parametric retrieval (Sonnet + GPT-5.4 cross-vendor convergence on EP-09a unfilled status)
- Open-web preliminary check (Kambe 2002 / Hazari 2017 / NiCl₂(dppe) Suzuki paper, all Minimal or Not applicable)
- WoS structured retrieval (this analysis, 4 variants)

The EP-09a negative claim is **strongly supported** at the WoS-bibliographic-retrieval dimension.

## Cross-cutting diagnostic — three convergent patterns across EP-09a Variants A-D

1. **Catalyst-design papers dominate keyword matches** (Variant A: NHC-Ni, pincer-Ni, dinuclear-Ni; Variant C: Co/Zr heterobimetallic) — predecessor terms appear as historical context, not as benchmark targets
2. **Within-family comparisons dominate when comparison language IS used** (Variant C: Zhou 2014 Co/Zr Xyl vs Mes ligand variants; not against external named predecessors)
3. **Explicit benchmark vocabulary co-occurs with cross-coupling-Grignard effectively never** (Variant B: 1 off-target hit; Variant D: 0 hits)

These three patterns together describe a **structural pattern**: modern chemistry publishing on Ni-Kumada systems organises its comparisons internally (new catalyst's variants, scope-extension within paper), not externally (against named predecessor catalysts at matched conditions). This is the empirical signature of the publication-incentive interpretation developed in Discussion 1.

## File locations

- Hit count summary: `validation/ep09a_wos_llm/hit_counts.md` — to be updated to record Variant D = 0 hits
- All 4 variant raw exports: `validation/ep09a_wos_llm/wos_variant_{a,b,c}.txt` + Variant D = 0 hits (no export)
- Per-variant analyses: `validation/ep09a_wos_llm/wos_variant_{a,b,c,d}_analysis.md`
- Sibling EP-08a Module: `validation/ep08a_wos_llm/` (6 formulations complete; 11 hits, 0 applicable)
