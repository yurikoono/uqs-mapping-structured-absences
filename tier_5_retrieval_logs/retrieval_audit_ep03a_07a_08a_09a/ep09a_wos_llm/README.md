# EP-09a: Structured Retrieval Audit (Tier 1 #1 Module 3)

**Purpose.** Structured bibliographic stress test of the EP-09a non-detection claim (substrate-matched, condition-matched head-to-head benchmark against named predecessor catalysts — Corriu/Masse Ni(acac)₂, Tamura-Kochi Fe, Corey/Whitesides stoichiometric — for the dppe-Ni Kumada system over the 54-year retrieval window).

**Scope.** WoS Core Collection + Scopus + Google Scholar + Crossref multi-database audit. Negative-claim test: the manuscript asserts EP-09a as cross-model-convergent unfilled at the "same-axis head-to-head" level (Sonnet + GPT-5.4; only Tamao 1976 BCSJ partial at catalyst-class-level); this audit tests whether structured bibliographic search returns any Complete or Partial filler under 0B §5 criteria.

## EP-09a Definition (from SI-3.7 + 0B §5)

> EP-09a Internal benchmark pack — VQ-4. Case-specific implementation: parallel reactions with Tamura-Kochi (Fe) and Corriu/Masse (Ni(acac)₂) and Corey/Whitesides stoichiometric reagents on the same substrate, yielding direct numerical yield, selectivity, and operability comparisons.

**0B classification criteria** (locked 2026-05-20, see `improvements/paperA_ep_audit_criteria_20260520.md` §5):

- **Complete**: parallel reaction with ≥ 2 of 3 named benchmarks at substrate-matched + condition-matched setup + numerical yield + selectivity + operability comparison
- **Partial**: 1 benchmark with same substrate + matched conditions, OR all 3 with different substrates / conditions, OR 2 benchmarks with same substrate but non-strict conditions
- **Minimal**: mention of "predecessor catalysts" without numerical comparison, OR benchmark to non-named systems
- **Non-filler**: no same-axis head-to-head benchmark with named predecessor catalysts in retrieval

## Status (as deposited, R1 2026-10-16)

This README was written when the audit was planned (2026-05-20). What was actually done:

| Step | Done? | Record |
|---|---|---|
| WoS Core Collection, variants A–D | Yes, 2026-05-20 (hits: A 9, B 1, C 1, D 0); re-run with the same query strings on 2026-10-05 (hits: A 9, B 1, C 1, D 0) | `hit_counts.md`; `../wos_reexport_20261005/README.md` |
| Per-record classification against the locked criteria | Yes | `wos_variant_{a,b,c,d}_analysis.md` |
| Scopus | Not run | — |
| Google Scholar / open web | Preliminary search only | `gs_candidates_preliminary.md` (open-web search of 2026-05-20) |
| Crossref check of each candidate | No separate log; the DOIs are those of the WoS records | — |
| Audit report | No separate report; the findings are in `hit_counts.md`, the variant analyses and `../tier1_audit_summary_20260520.md` | — |

## Queries to execute

See `paperA_tier1_retrieval_audit_execution_20260520.md` §Module 3 for the 4-variant WoS Core Collection query and Scopus translation. Variants A-D progressively probe:

- A: strict named-benchmark (NiCl₂(dpe) OR Kumada + Ni(acac)₂ / Corriu / Masse / Tamura-Kochi / Corey-Whitesides)
- B: head-to-head Ni comparison (head-to-head / side-by-side / parallel reaction / benchmark)
- C: predecessor catalyst comparison (Kumada-Tamao-Corriu + comparison-language + Ni(acac)₂ / Fe / stoichiometric)
- D: Fe-Kumada vs Ni-Kumada same-substrate (matched conditions)

## Preliminary findings (2026-05-20 Google open-web)

WebSearch query: `"NiCl2(dpe)" OR "NiCl2(dppe)" "Ni(acac)2" head-to-head benchmark comparison Grignard coupling`

| # | Paper / DOI | First-pass classification | Why | Verification needed |
|---|---|---|---|---|
| 1 | [Nickel-Catalyzed Cross-Coupling Reaction of Grignard Reagents with Alkyl Halides and Tosylates: Remarkable Effect of 1,3-Butadienes](https://pubmed.ncbi.nlm.nih.gov/11960446/) (Kambe 2002) | **Boundary: Minimal-or-Partial** | Reports qualitative catalyst comparison: "Nickel complexes bearing no phosphine ligands (NiCl₂, Ni(acac)₂, Ni(COD)₂) afford coupling products in good yields, whereas NiCl₂(PPh₃)₂ and NiCl₂(dppp) were less effective in alkyl coupling reactions." Substrate distance from Kumada 1972 11-Table-I is significant (alkyl halide + butadiene additive system), conditions not strictly matched. | WebFetch full content; check if substrate-matched numerical comparison exists; classify Partial vs Minimal |
| 2 | [NiCl₂(dppe)-Catalyzed Cross-Coupling of Aryl Mesylates, Arenesulfonates, and Halides with Arylboronic Acids](https://pubs.acs.org/doi/abs/10.1021/jo049940i) | **Out of scope (different reaction class)** | Suzuki-class reaction (Ni + arylboronic acid), not Grignard cross-coupling. Different EP target. | None — exclude |
| 3 | [Well-defined nickel and palladium precatalysts for cross-coupling](https://pmc.ncbi.nlm.nih.gov/articles/PMC5637737/) | **Boundary: Minimal candidate** | Review of Ni vs Pd precatalysts. May contain benchmark tables; depends on content. | WebFetch full content; check for matched-condition benchmark data on Kumada substrates |
| 4 | [Synthesis of Ni(dppe)₂ and Nickel (I) Catalysts and their... (PDF)](https://www.mobt3ath.com/uplode/book/book-14282.pdf) | **Boundary: needs reading** | Likely thesis / book chapter. May contain benchmarking. | WebFetch / direct read; classify |

**Initial open-web signal**: Several catalyst-class-level comparisons exist (Kambe 2002 = Minimal-to-Partial qualitative; NiCl₂(dppe) review-context comparisons). **No same-axis head-to-head benchmark with named predecessors (Corriu/Masse Ni(acac)₂ vs dppe-Ni at matched Kumada substrate)** has surfaced in open-web. This is preliminary support for the manuscript's "absent at named-predecessor head-to-head level" claim, while flagging Kambe 2002 + Ni-Pd review as content-check candidates.

## Failure-mode considerations (carrying over from SI-9 EP-03a pilot)

Per the EP-03a pilot diagnostic, structured WoS retrieval may suffer:

- (i) Pre-1991 abstract-coverage gap (most relevant here for Corriu/Masse 1972 and Tamura-Kochi 1971 papers themselves; less relevant for post-1990 benchmark candidates)
- (ii)-(iii) Keyword-retrieval mismatch ("Corriu", "Masse", "Tamura-Kochi" may not appear as searched authors; benchmark may be reported with paraphrased phrasing)
- (iv) DOI-resolves-but-content-mismatch (LLM may attribute benchmark to wrong paper)
- (v) Full-citation fabrication (cross-model parallel check needed)

The §B variant of the query (head-to-head / side-by-side / parallel reaction) is designed to catch papers reporting benchmark without naming the named predecessors verbatim.

## Files in this folder

- `README.md`
- `gs_candidates_preliminary.md`
- `hit_counts.md`
- `wos_variant_a_analysis.md`
- `wos_variant_b_analysis.md`
- `wos_variant_c_analysis.md`
- `wos_variant_d_analysis.md`

Raw WoS exports: `../wos_reexport_20261005/ep09a_wos_variant_{a,b,c}.txt` (re-exports of 2026-10-05; the May exports were not kept, see `../WOS_EXPORT_STATUS.md`). Variant D returned no records. The exports carry bibliographic fields only (abstracts, Keywords Plus and funding fields removed).
Files listed in the planning version of this README (`*_queries.txt`, `wos_raw_export.txt`, `scopus_raw_export.csv`, `gs_candidates.md`, `crossref_verifications.md`, `*_candidates.md`, `*_audit_report.md`) were never produced. The query strings as run are given in each `wos_variant_*_analysis.md`.

## Related documents

- `../tier1_audit_summary_20260520.md` — summary of the EP-03a / 07a / 08a / 09a audit
- `../WOS_EXPORT_STATUS.md` and `../wos_reexport_20261005/` — the 2026-10-05 re-exports
- `../ep03a_wos_llm/` — the EP-03a audit
- The planning memos named above (execution plan, criteria memo, query sheet of 2026-05-20) are project working files and are not deposited; the criteria are reproduced in this README.
