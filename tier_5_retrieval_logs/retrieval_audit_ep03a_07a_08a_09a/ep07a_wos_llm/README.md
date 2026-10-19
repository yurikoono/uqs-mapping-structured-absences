# EP-07a: Structured Retrieval Audit (Tier 1 #1 Module 4, abbreviated)

**Purpose.** Abbreviated structured bibliographic positive control for the EP-07a scope-extension audit (Csp³ halides + Cl/Br/I direct comparison for the dppe-Ni Kumada system). Companion to EP-03a (mechanistic positive control). Tests whether structured retrieval recovers the publication-incentive-aligned scope-extension filling literature that the LLM identified (Tamao 1976 BCSJ Full Paper I + 1976-1985 follow-ups).

**Scope.** WoS Core Collection + Scopus + Google Scholar + Crossref. Positive-control test: filling expected dense, so this audit calibrates retrieval coverage rather than testing a negative claim.

## EP-07a Definition (from SI-3.7 + 0B §3)

> EP-07a Boundary-test pack — VQ-2 (for scope boundary). Case-specific implementation: (i) test n-BuCl, sec-BuCl, PhCH₂Cl (Csp³ halides) under the same conditions (NiCl₂(dpe) / Et₂O) with PhMgBr and present inactive / poorly selective results as a "failed scope" row of Table I; (ii) test PhBr and PhI with the reference substrate (n-BuMgBr) under the same conditions as PhCl for direct yield comparison.

**0B classification criteria** (locked 2026-05-20, see `improvements/paperA_ep_audit_criteria_20260520.md` §3):

- **Complete**: ≥ 3 Csp³ halides AT same conditions + PhCl/PhBr/PhI comparison AT matched dppe-Ni
- **Partial**: either Csp³ scope OR Cl/Br/I comparison, not both; OR cross-substrate without strict condition matching
- **Minimal**: scope under modified catalyst/ligand; OR single Csp³; OR qualitative Cl/Br/I
- **Non-filler**: no scope-extension paper addresses Csp³ halides or Cl/Br/I comparison in Kumada

## Status (as deposited, R1 2026-10-16)

This README was written when the audit was planned (2026-05-20). What was actually done:

| Step | Done? | Record |
|---|---|---|
| WoS Core Collection, variants A–B | Yes, 2026-05-20 (hits: A 9, B 0); re-run with the same query strings on 2026-10-05 (hits: A 9, B 0) | `hit_counts.md`; `../wos_reexport_20261005/README.md` |
| Per-record classification against the locked criteria | Yes | `wos_variant_a_analysis.md` (Variant B returned no records) |
| Scopus | Not run | — |
| Google Scholar / open web | Not run | — |
| Crossref check of each candidate | No separate log; the DOIs are those of the WoS records | — |
| Audit report | No separate report; the findings are in `hit_counts.md`, the variant analyses and `../tier1_audit_summary_20260520.md` | — |

## Pre-known anchors (from `stage4_literature_update_20260419.md`)

| Paper | LLM identification | Expected 0B level (pre-audit hypothesis) |
|---|---|---|
| Tamao et al. *Bull. Chem. Soc. Jpn.* 49, 1958 (1976) | EP-07a (Opus 4.7 + GPT-5.4 cross-model) | Partial / Complete |
| Tamao et al. *Tetrahedron* 1982 | EP-07a (GPT-5.4) | Partial |
| Terao-Watanabe-Ikumi-Kuniyasu-Kambe *J. Am. Chem. Soc.* 2002 | EP-07a sp³ boundary (Opus 4.7) | Partial (sp³ extension) |
| Anderson-Jones-Vicic *J. Am. Chem. Soc.* 2004 / 2006 | EP-03a, EP-07a partial (Opus 4.7) | Partial |
| Breitenfeld 2014 | EP-07a paradigm-shift (sp³ extension) | Partial (paradigm-shift) |
| Pengfei (Li) 2024 | EP-07a paradigm-shift (sp³ extension, Pd-Ni transition) | Partial-or-Minimal (system distance) |

## Queries to execute

See `paperA_tier1_retrieval_audit_execution_20260520.md` §Module 4 for the 2-variant WoS Core Collection query and Scopus translation:

- A: Csp³ halide scope in Kumada / Ni cross-coupling
- B: Cl/Br/I substrate comparison (PhCl + PhBr + PhI in same paper)

## Why abbreviated

EP-07a is positive control rather than central negative claim. Its primary function in Tier 1 #1 is **calibration**: if the LLM-parametric retrieval has correctly identified the dense Tamao-1976 / 1976-1985 follow-up filling literature, structured DB retrieval should recover overlapping candidates. Significant under-recovery would indicate a failure mode worth documenting. Significant over-recovery (DB returns relevant papers LLM missed) would indicate Tamao-era literature is broader than the LLM accessed.

Per the master execution plan, EP-07a is the **lowest-priority module in Tier 1 #1** and can be skipped if time pressure forces core-only execution (EP-03a extension + EP-08a + EP-09a).

## Files in this folder

- `README.md`
- `hit_counts.md`
- `wos_variant_a_analysis.md`

Raw WoS exports: `../wos_reexport_20261005/ep07a_wos_variant_a.txt` (re-export of 2026-10-05; the May export of Variant A was not kept, see `../WOS_EXPORT_STATUS.md`). Variant B returned no records. The exports carry bibliographic fields only (abstracts, Keywords Plus and funding fields removed).
Files listed in the planning version of this README (`*_queries.txt`, `wos_raw_export.txt`, `scopus_raw_export.csv`, `gs_candidates.md`, `crossref_verifications.md`, `*_candidates.md`, `*_audit_report.md`) were never produced. The query strings as run are given in each `wos_variant_*_analysis.md`.

## Related documents

- `../tier1_audit_summary_20260520.md` — summary of the EP-03a / 07a / 08a / 09a audit
- `../WOS_EXPORT_STATUS.md` and `../wos_reexport_20261005/` — the 2026-10-05 re-exports
- `../ep03a_wos_llm/` — the EP-03a audit
- The planning memos named above (execution plan, criteria memo, query sheet of 2026-05-20) are project working files and are not deposited; the criteria are reproduced in this README.
