# EP-08a: Structured Retrieval Audit (Tier 1 #1 Module 2)

**Purpose.** Structured bibliographic stress test of the EP-08a non-detection claim (replicate-measurement / uncertainty reporting for the dppe-Ni Kumada system over the 54-year retrieval window). Companion to the existing EP-03a pilot (`../ep03a_wos_llm/`).

**Scope.** WoS Core Collection + Scopus + Google Scholar + Crossref multi-database audit. Negative-claim test: the manuscript asserts EP-08a as cross-model-convergent unfilled (Sonnet + GPT-5.4); this audit tests whether structured bibliographic search also returns no Complete or Partial filler under the §0B §4 criteria.

## EP-08a Definition (from SI-3.7 + 0B §4)

> EP-08a Replication / uncertainty pack — VQ-4. Case-specific implementation: (i) for all 11 Table I entries, n ≥ 3 replicates with standard deviations on yield; (ii) for cis/trans-dichloroethylene substrates, n ≥ 3 replicates with glpc and ¹H NMR cross-method determination; (iii) time-course (1 h, 5 h, 20 h) to distinguish kinetic vs thermodynamic product.

**0B classification criteria** (locked 2026-05-20, see `improvements/paperA_ep_audit_criteria_20260520.md` §4):

- **Complete**: all 11 Table I entries with n ≥ 3 replicates + SD/CI, cross-method, time-course
- **Partial**: replicates+SD for subset, OR cross-method without replicates, OR time-course alone
- **Minimal**: anecdotal "replicated" without n/SD, OR summary statistic only
- **Non-filler**: no replicate measurement with reported uncertainty for dppe-Ni Kumada at substrate-matched conditions

## Status (as deposited, R1 2026-10-16)

This README was written when the audit was planned (2026-05-20). What was actually done:

| Step | Done? | Record |
|---|---|---|
| WoS Core Collection, variants A–D, with two reformulations of D (D′, D″) | Yes, 2026-05-20 (hits: A 3, B 1, C 7, D/D′/D″ 0); re-run with the same query strings on 2026-10-05 (hits: A 2, B 1, C 7, D/D′/D″ 0) | `hit_counts.md`; `../wos_reexport_20261005/README.md` |
| Per-record classification against the locked criteria | Yes | `wos_variant_{a,b,c,d}_analysis.md` |
| Scopus | Not run | — |
| Google Scholar / open web | Preliminary search only | `gs_candidates_preliminary.md` (open-web search of 2026-05-20) |
| Crossref check of each candidate | No separate log; the DOIs are those of the WoS records | — |
| Audit report | No separate report; the findings are in `hit_counts.md`, the variant analyses and `../tier1_audit_summary_20260520.md` | — |

## Queries to execute

See `paperA_tier1_retrieval_audit_execution_20260520.md` §Module 2 for the 4-variant WoS Core Collection query and Scopus translation. Variants A-D progressively probe:

- A: strict (Kumada + cross-coupling + replicate/SD/uncertainty)
- B: relaxed (Kumada + triplicate/n=3/95% CI)
- C: cis/trans time-course (kinetic vs thermodynamic)
- D: control (Kumada-Tamao OR Kumada-Corriu + variability terms)

## Preliminary findings (2026-05-20 Google open-web)

WebSearch query: `"Kumada coupling" replicate measurement "standard deviation" Ni Grignard reproducibility`

| # | Paper / DOI | First-pass classification | Why | Verification needed |
|---|---|---|---|---|
| 1 | [Nickel-Catalyzed Kumada Cross-Coupling Reactions of Tertiary Alkylmagnesium Halides and Aryl Bromides/Triflates](https://pmc.ncbi.nlm.nih.gov/articles/PMC8036247/) (PMC8036247) | **Boundary: Minimal candidate** | Reproducibility issue traced to NiCl₂ hydration state. NOT the original 11 Table I substrates; addresses different substrate class (tertiary alkyl-Mg + aryl bromides/triflates). | WebFetch full content; check if SDs reported on any matched substrate |
| 2 | Large-scale (50 kg batch) Kumada coupling process-chemistry paper (Academia preprint) | **Partial candidate (process-chemistry boundary case)** | Process-chemistry scale-up demonstrates reproducibility at industrial scale; matches 0B §4 boundary "process / flow chemistry replication → Partial" if conditions are documented | Identify exact paper (likely PRD article); check substrates + condition matching |

**Initial open-web signal**: NO peer-reviewed paper surfaces with **systematic replicate measurements + reported SDs on the original 1972 Kumada Table I substrates**. Two boundary candidates exist (reproducibility-context Kambe-style paper + process-chemistry scale-up). This is preliminary evidence the negative claim survives open-web check; structured WoS / Scopus execution will refine.

## Failure-mode considerations (carrying over from SI-9 EP-03a pilot)

Per the EP-03a pilot diagnostic, structured WoS retrieval may suffer:

- (i) Pre-1991 abstract-coverage gap (less relevant here since EP-08a target era is 1972-2026)
- (ii)-(iii) Keyword-retrieval mismatch (Kumada papers may not use "standard deviation" verbatim; may use "n = 3", "in triplicate", "average of N runs")
- (iv) DOI-resolves-but-content-mismatch (LLM-claimed replicate papers may be fabrications — Crossref + content read required)
- (v) Full-citation fabrication (cross-model parallel check needed)

The §B variant of the query is specifically designed to catch keyword variants ("triplicate", "n=3", "95% CI") to mitigate failure mode (ii).

## Files in this folder

- `README.md`
- `gs_candidates_preliminary.md`
- `hit_counts.md`
- `wos_variant_a.txt`
- `wos_variant_a_analysis.md`
- `wos_variant_b_analysis.md`
- `wos_variant_c_analysis.md`
- `wos_variant_d_analysis.md`

Raw WoS exports: `wos_variant_a.txt` (export of 2026-05-20) and `../wos_reexport_20261005/ep08a_wos_variant_{a,b,c}.txt` (2026-10-05). Variants D, D′ and D″ returned no records. The exports carry bibliographic fields only (abstracts, Keywords Plus and funding fields removed).
Files listed in the planning version of this README (`*_queries.txt`, `wos_raw_export.txt`, `scopus_raw_export.csv`, `gs_candidates.md`, `crossref_verifications.md`, `*_candidates.md`, `*_audit_report.md`) were never produced. The query strings as run are given in each `wos_variant_*_analysis.md`.

## Related documents

- `../tier1_audit_summary_20260520.md` — summary of the EP-03a / 07a / 08a / 09a audit
- `../WOS_EXPORT_STATUS.md` and `../wos_reexport_20261005/` — the 2026-10-05 re-exports
- `../ep03a_wos_llm/` — the EP-03a audit
- The planning memos named above (execution plan, criteria memo, query sheet of 2026-05-20) are project working files and are not deposited; the criteria are reproduced in this README.
