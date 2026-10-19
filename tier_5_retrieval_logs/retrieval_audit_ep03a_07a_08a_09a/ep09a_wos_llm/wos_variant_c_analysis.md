# EP-09a — WoS Variant C Analysis (2026-05-20)

## Query

```
TS=("Kumada-Tamao-Corriu" OR "Kumada cross-coupling") AND TS=("comparison with" OR "vs" OR "versus" OR "compared to") AND TS=("Ni(acac)2" OR "iron catalyst" OR "Fe catalyst" OR "stoichiometric") AND DT=(Article)
```

- Database: WoS Core Collection
- Filter: Document Type = Article
- Date executed: 2026-05-20
- Executor: User (Hokkaido U subscription)
- **Hit count: 1**

This variant targets explicit comparison language combined with Kumada terminology and named predecessor catalyst keywords (`Ni(acac)2` / `iron catalyst` / `Fe catalyst` / `stoichiometric`).

## Candidate and 0B §5 classification

### Candidate 1: Zhou-Saper-Krogman-Foxman-Thomas 2014 (*Dalton Trans.*)

| Field | Value |
|---|---|
| Title | Effect of ligand modification on the reactivity of phosphinoamide-bridged heterobimetallic Zr/Co complexes |
| Authors | Wen Zhou, Noam I. Saper, Jeremy P. Krogman, Bruce M. Foxman, Christine M. Thomas |
| Journal / Year / DOI | *Dalton Trans.* 2014, 43, 1984–1989 / [10.1039/c3dt52133h](https://doi.org/10.1039/c3dt52133h) |
| Catalyst | **Co/Zr heterobimetallic complexes** — `ICo((iPr2PNXyl)3)Zr` (Xyl variant, this work) vs `ICo((iPr2PNMes)3)ZrCl` (Mes variant, previously reported by same group) |
| Substrate | Alkyl halides + n-octylMgBr (Kumada coupling reaction) |
| Comparison axis | **Within-Co/Zr-family**: Xyl vs Mes phosphinoamide N-aryl substituent variants |
| Keyword match origin | "Kumada cross-coupling" ✓ + "Comparison of 4 with the previously reported mesityl-substituted complex" ✓ + "stoichiometric and catalytic reactions" ✓ |
| Head-to-head benchmark vs named EP-09a predecessors (Corriu Ni(acac)₂ / Tamura-Kochi Fe / Corey-Whitesides) | NO |
| Comparison vs dppe-Ni | NO |
| **0B §5 classification** | **Not applicable** — Co/Zr heterobimetallic catalyst design paper; the comparison is internal to the Co/Zr ligand-variant family (Xyl vs Mes), NOT against named Ni-Kumada predecessors. Catalyst metal is Co (not Ni); "stoichiometric" refers to internal stoichiometric reactivity studies of the new complex, not Corey-Whitesides stoichiometric Cu reagents |

## Summary — Variant C

| Classification | Count |
|---|---|
| Complete filler | **0** |
| Partial filler | **0** |
| Minimal filler | **0** |
| Not applicable | **1** |
| **Total** | **1** |

## Interpretation

Variant C combined explicit comparison language (`comparison with` / `vs` / `versus` / `compared to`) with Kumada terminology and named predecessor terms. Only **1 paper** matched, and it is a **within-Co/Zr-family ligand-variant comparison study**, not a Ni-Kumada vs named predecessor benchmark.

The keyword match arose from:
- Kumada cross-coupling being one of the test reactions
- Internal "comparison of 4 with the previously reported mesityl-substituted complex"
- Stoichiometric reactivity studies

None of these align with the EP-09a target. The Variant C result therefore provides further independent support for the EP-09a negative claim at the comparison-language retrieval dimension.

## Diagnostic note — within-family comparisons dominate

The 1-hit result is informative as it shows that when "comparison" language IS used with Kumada cross-coupling in WoS-indexed papers, the comparison is typically:

- **Within the new catalyst's own ligand-variant family** (Zhou 2014: Co/Zr Xyl vs Mes)
- **Within the new catalyst's own substrate scope** (e.g., scope-extension within one paper)

NOT:
- Across the new catalyst vs named predecessor catalysts at matched substrate / matched conditions

This is consistent with the publication-incentive interpretation in Discussion 1: papers establish novelty by showing internal optimisation (within-paper variant comparisons), not by benchmarking against external named predecessors at matched conditions.

## EP-09a WoS Module — running cumulative (A + B + C)

| Variant | Hits | Complete | Partial | Minimal | Not applicable |
|---|---|---|---|---|---|
| A (strict named-benchmark) | 9 | 0 | 0 | 2 | 7 |
| B (head-to-head Ni-Grignard vocabulary) | 1 | 0 | 0 | 0 | 1 |
| C (comparison language + predecessor terms) | 1 | 0 | 0 | 0 | 1 |
| **Cumulative (A + B + C)** | **11** | **0** | **0** | **2** | **9** |

## Next steps

- Variant D (Fe-Kumada vs Ni-Kumada same-substrate matched conditions): pending execution

## File locations

- Raw export: `validation/ep09a_wos_llm/wos_variant_c.txt`
- Hit count summary: `validation/ep09a_wos_llm/hit_counts.md`
- Sibling Variant A / B analyses: `validation/ep09a_wos_llm/wos_variant_{a,b}_analysis.md`
