# RECOUNT NOTE — Murai multi-run study summary values superseded (2026-08-29)

**Status of this note**: appended to the deposit as a dated correction record. The raw per-run
files and the two TSVs are unchanged; this note supersedes the *headline values* of
`murai_multirun_summary_20260612.md` for manuscript reporting.

## Finding

Pre-submission audit (Sol recheck 2026-08-29, independently reproduced the same day) found that
`murai_multirun_candidates.tsv` is keyed at **author–year granularity**:

1. One `(vendor, prompt, run)` cell can list the same paper as several rows under different
   Evidence Packs (the flagship candidate Kakiuchi 1995 BCSJ contributes 18 rows).
2. `murai_multirun_verifications.tsv` carries only `first_author` + `year` as identity fields,
   so a verdict attaches to an author–year *bin*, and distinct shells sharing that bin
   (BCSJ 1995, 68, 62 / Chem. Lett. 1995 / speculative JACS and Nature shells) inherit the
   same verdict.

## Recount at paper-identity level (deterministic, from the candidates TSV alone)

| Quantity | Summary memo | Strict-identity recount |
|---|---:|---:|
| Kakiuchi 1995 BCSJ (68, 62) recurrence | 15 / 18 runs | **9–10 / 18 runs** (9 by page-range-strict matching, 10 by journal+volume matching; the 1-run difference is one ambiguous shell) |
| Kakiuchi 1995 author–year bin presence | — | 11 / 18 runs |
| Kakiuchi 1995 candidate rows | — | 22 (18 BCSJ-shell, 2 Chem. Lett., 1 Nature, 1 JACS) |

Consequently the summary's derived statistics — `101 / 125 verified real`,
per-arm failure rates `32 / 14 / 13 %`, and `Jaccard 0.08–0.55` over verified candidates —
are author–year-bin statistics, not paper-identity statistics, and are **not valid at the
paper level**. They were withdrawn from manuscript reporting on 2026-08-29 rather than locally recomputed, because a valid recomputation
requires re-keying and re-verifying per identity.

## Repair path (registered, not executed)

1. Re-key the candidate ledger with a stable identity: DOI where available, otherwise a
   normalized full citation shell; keep mutually incompatible shells as separate unresolved
   candidates.
2. Re-verify each identity (not each author–year bin).
3. Deduplicate identities within each `(vendor, prompt, run)` cell.
4. Regenerate recurrence / verified-rate / per-arm failure / Jaccard from one deterministic
   script and propagate to any future manuscript use.

The Kumada 1972 retrieval-depth runs are unaffected: their per-run matrices (§13.3 and §15.3 of
`01_response/r33b_candidates/records/kumada_retrieval_depth_verification_extract.md`) record candidate
identities with explicit conflation adjudication.

Audit trail: an independent re-check of 2026-08-29 and the authors' own recount of the same day (working
records, not deposited).
