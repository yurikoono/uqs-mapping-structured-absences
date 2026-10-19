# EP-08a — WoS Variant B Analysis (2026-05-20)

## Query

```
TS=("Kumada coupling" OR "NiCl2(dpe)" OR "NiCl2(dppe)" OR "Ni-phosphine Grignard") AND TS=("triplicate" OR "n=3" OR "n ≥ 3" OR "standard deviation" OR "95% CI" OR "confidence interval") AND DT=(Article)
```

- Database: WoS Core Collection
- Filter: Document Type = Article
- Date executed: 2026-05-20
- Executor: User (Hokkaido U subscription)
- **Hit count: 1**

## Candidate and 0B classification

### Candidate 1: Cornacchio-Price-Jennings-McDonald-Staroverov-Jones 2009 (*J. Org. Chem.*)

| Field | Value |
|---|---|
| Title | Meta-Substituted Thienyl Benzenes: A Comparative Synthetic, Structural and Computational Study |
| Authors | Angelica L. P. Cornacchio, Jacquelyn T. Price, Michael C. Jennings, Robert McDonald, Viktor N. Staroverov, Nathan D. Jones |
| Journal / Year / DOI | *J. Org. Chem.* 2009, 74, 530–544 / [10.1021/jo801771d](https://doi.org/10.1021/jo801771d) |
| Reaction class | Kumada coupling — but with **PdCl₂(dppf)** catalyst, **not Ni-catalyzed** |
| Substrate class | Thienyl Grignards + 1,3- or 1,3,5-bromo / iodobenzenes (different substrate class from Kumada 1972 Table I) |
| Catalyst identity | **PdCl₂(dppf)** (palladium, not Ni); dppf ≠ dppe |
| Replicate / SD / time-course reporting | Not explicit in abstract; research focus is on synthesis of thienyl benzenes + their UV-Vis / cyclic voltammetry / DFT characterisation |
| "Replicate / SD / CI" keyword match origin | Likely from KeyWords Plus or author-keyword field (not visible in TS abstract); abstract does not contain these terms in textual form |
| **0B §4 classification** | **Not applicable** — catalyst class mismatch (Pd ≠ Ni); substrate class differs from Kumada 1972 Table I; research focus is on product properties, not on systematic replicate measurement of dppe-Ni Kumada Table I yields |

## Summary — Variant B

| Classification | Count |
|---|---|
| Complete filler | **0** |
| Partial filler | **0** |
| Minimal filler | **0** |
| Not applicable | **1** |

## Interpretation — preliminary

Variant B applied a **Kumada-specific catalyst syntax filter** (`NiCl2(dpe)` / `NiCl2(dppe)` / `Ni-phosphine Grignard`) AND **specific replicate methodology keywords** (`triplicate` / `n=3` / `SD` / `CI`). This combination returned only **1 paper**, and that paper:

- Has "Kumada coupling" as a keyword match (textually present in abstract)
- But uses **Pd-catalysed** Kumada coupling (PdCl₂(dppf)) — outside dppe-Ni system scope per 0B §4 cross-cutting rule "System identity — filling must be in the dppe-Ni Kumada system OR explicitly mapped back"
- Does not provide per-substrate n ≥ 3 replicate measurement with SDs as required for EP-08a Complete / Partial filling

The fact that this single hit also fails 0B is **consistent with the EP-08a negative claim**. The Kumada-specific catalyst keyword filter combined with replicate methodology terms returns no actual filler.

## Diagnostic note — Pd-Kumada vs Ni-Kumada in WoS retrieval

The Pd-Kumada paper appeared in this Ni-specific-catalyst query because "Kumada coupling" appears verbatim in the abstract regardless of metal. This is **NOT a failure mode (i)–(v) per SI-9 diagnostic**, but rather a feature of keyword retrieval: the catalyst-class restriction is at the level of the second OR-block (`NiCl2(dpe)` / `NiCl2(dppe)` / `Ni-phosphine Grignard`), but author-keyword inclusion of "Kumada coupling" can override this in WoS Topic-search semantics if the paper claims "Kumada-coupling-like" methodology in either the abstract or the keywords field.

This is a useful retrieval-diagnostic observation but does not affect the negative claim conclusion.

## Combined Variant A + B running total (EP-08a)

| Variant | Hits | Complete | Partial | Minimal | Not applicable |
|---|---|---|---|---|---|
| A (strict Ni + replicate) | 3 | 0 | 0 | 0 | 3 |
| B (Kumada-specific + replicate methodology) | 1 | 0 | 0 | 0 | 1 |
| **Total** | **4** | **0** | **0** | **0** | **4** |

## Next steps for this Module

- Variant C (cis/trans-stilbene time-course) — pending execution
- Variant D (Kumada-named control) — pending execution
- Scopus variants A-D — pending execution
- Crossref API verification of all candidates' DOIs — Claude TODO after full variant set

## File locations

- Raw export: `validation/ep08a_wos_llm/wos_variant_b.txt`
- Hit count summary: `validation/ep08a_wos_llm/hit_counts.md`
- Sibling Variant A analysis: `validation/ep08a_wos_llm/wos_variant_a_analysis.md`
