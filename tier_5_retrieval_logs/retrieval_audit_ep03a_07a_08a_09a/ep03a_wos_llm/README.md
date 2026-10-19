# EP-03a: LLM-named filling papers vs Web of Science structured queries (pilot)

**What this is.** The n = 1 pilot of SI-9 (run 2026-04-20; content checks 2026-04-20/21; not re-run for R1, see `../tier1_audit_summary_20260520.md`). The EP-03a filling papers named by two Stage 4 v2 runs on Kumada 1972 (v17 prompts; Claude Opus 4.7 and GPT-5.4 Thinking, 2026-04-19; project paths `papers/dev/kumada/kumada_v17_opus47_s4v2.md` and `papers/dev/kumada/gpt54thinking/kumada_v17_gpt54thinking_s4.md`, in this package under `tier_3_stage_outputs/dev_set/kumada/` *(reviewer version only; redacted Markdown copies under `tier_8_redacted_public_raw_outputs/`)*) are compared with the records returned by structured Web of Science Core Collection queries built from the EP-03a definition.

## EP-03a Definition (from SI-3)

EP-03a requires the direct spectroscopic/structural observation of Ni–phosphine intermediates relevant to the Kumada 1972 catalytic cycle (L₂Ni(Ar)(X) or equivalent active species), in the NiCl₂(dpe) system or a closely related Ni–diphosphine system. Filling is satisfied by isolation and characterization (X-ray, NMR, EPR, IR, etc.) of the proposed intermediate in an experimentally matched or adjacent system.

## What was done

| Step | Result | Record |
|---|---|---|
| LLM candidates: union of the EP-03a filling papers named by the two runs | six papers; one (Morrell & Kochi 1975) named by both models | `llm_candidates_ep03a.md` |
| Query v1 (Ni + diphosphine family + intermediate + characterisation) | 49 records | `wos_query.txt`, `wos_raw_49hits.txt`; table `wos_49hits_triage_table.md` made by `parse_wos.py` (its relevance column was left blank: the candidate-recovery check below replaced the planned manual triage) |
| Four reformulated queries A–D (ligand clause relaxed; cross-coupling context required in B and D) | 171, 25, 74 and 21 records; 262 unique DOIs over the five queries | `wos_query_alternatives.md`, `wos_variant_{a,b,c,d}.txt`; a WoS autocorrect that changed the query (`alkylnickel` → `allylnickel`) is recorded in `query_anomalies_log.md` |
| Recovery of each candidate in each query (DOI, or first author + year) | none of the six recovered by any query | `analyze_variants.py` → `variant_analysis_report.md` |
| Direct look-up of each candidate (DOI, then author + year + journal) | all six are indexed in WoS | `candidate_direct_queries.md`, `candidate_check_*.txt` |
| Content check of each candidate against the paper | see the log; for Yamamoto 1978 the citation is real but its content does not match the description | `verification_log.md` |
| Diagnosis | four failure modes: (i) no abstract in the WoS record, (ii) ligand class outside the query's keyword family, (iii) compound trade names not matched, (iv) a real citation whose content differs from the LLM's description | `diagnostic_report.md` |

## Files in this folder

- `README.md`
- `analyze_variants.py`
- `candidate_check_1_parshall1974.txt`
- `candidate_check_1b_parshall1974_tier2.txt`
- `candidate_check_2_morrell_kochi1975.txt`
- `candidate_check_3_yamamoto1978.txt`
- `candidate_check_3b_yamamoto_kohara_alt.txt`
- `candidate_check_4_vicic2004.txt`
- `candidate_check_4b_vicic2004_tier2.txt`
- `candidate_check_5_vicic2006.txt`
- `candidate_check_6_dawson2020.txt`
- `candidate_direct_queries.md`
- `diagnostic_report.md`
- `llm_candidates_ep03a.md`
- `parse_wos.py`
- `query_anomalies_log.md`
- `variant_analysis_report.md`
- `verification_log.md`
- `wos_49hits_triage_table.md`
- `wos_query.txt`
- `wos_query_alternatives.md`
- `wos_raw_49hits.txt`
- `wos_variant_a.txt`
- `wos_variant_b.txt`
- `wos_variant_c.txt`
- `wos_variant_d.txt`

The WoS exports carry bibliographic fields only (abstracts, Keywords Plus and funding fields removed). Not deposited: `archive_pre_autocorrect_fix/` (exports made before the autocorrect was noticed, listed in `diagnostic_report.md` §6). Files named in the planning version of this README that were never produced: `comparison_report.md` (the comparison is in `variant_analysis_report.md` and `diagnostic_report.md`). The pre-pilot plan for a further Phase 2 benchmark is a project memo and is not deposited.

## Limitations

- One EP; no generalisation to other EPs is claimed (EP-07a, 08a and 09a are audited in the sibling folders).
- The five queries do not exhaust the possible formulations; the diagnosis explains the zero recovery for these five.
- WoS records of older papers often lack indexed abstracts, which lowers keyword recall for exactly the period of the Kumada lineage.
