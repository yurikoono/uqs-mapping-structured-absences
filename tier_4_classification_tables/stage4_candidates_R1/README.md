# Stage 4 candidates and their status (R1; SI-9.10)

This folder and `01_response/r33b_candidates/` hold the same files (final R1 version, 2026-10-16); SI-9.10 cites both paths.

- `candidates.csv` — every candidate proposed by Stage 4: (A) the 37 analyses reported in the paper, none checked individually;
  (B) the verification-study runs, with the verdicts recorded for them. Columns give the rule applied (strict / lenient), the
  checks made, and the record and line each verdict rests on (`verification_record`, `verification_record_line`).
- `tally.md`, `tally_counts.json` — the aggregation rule, the counts, and how the records were read.
- `build_tally.py` — regenerates `candidates.csv` from the run files and verification records. It runs against the project
  repository layout (`papers/...`); README §0 item 11 maps those paths to this package.
- `records/` — the two prose records cited in `verification_record` that are not elsewhere in the package: B4
  (`stage4_literature_update_20260419.md`, a copy) and B5 (`kumada_retrieval_depth_verification_extract.md`, a line-preserving
  extract of the verification sections of the project record `pilot_retrieval_depth_20260508.md`, built by `make_extracts.py`;
  the record itself, from an exploratory pilot of 2026-05-08, is not deposited).

**`evidence_line` = `NOT FOUND`** (11 rows, record set B6_murai_multirun). These candidates are named in a verification record (the Murai multi-run ledger) but do not occur in the deposited run file the ledger assigns them to, so no line can be given; `NOT FOUND` is set by `build_tally.py` by design. `tally.md` §5, item 9 ("B6 Murai ledger vs files") lists them. They are counted as unclassifiable.

**Public cut.** Tier 3 paths are in the reviewer version only. In this cut the `in_deposit` column of `candidates.csv` points to the redacted Markdown copies under `tier_8_redacted_public_raw_outputs/` (same sub-path); a Tier 3 path without such a copy is marked *(reviewer version only)*.
