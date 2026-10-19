---
title: Paper A R1 — B2 → Stage 3 results
created: 2026-09-29
status: active
audience: paperA
open_questions: true
---

> **Note (2026-10-19).** This record gives the state of 2026-09-29. The author check of 2026-10-05 is in `01_response/verification/human_verification_D3D4_20260929.md` (the author's marks and notes) and is reported in SI-6.10 and SI-11.20; statements below that no human has verified the ratings or the adjudication describe the state before it.

# B2 → Stage 3 results (prereg `preregistration_B2_stage3.md`, commit 052a74c)

**Runs.** Ten Stage 3 v2 EN runs on Sonnet 4.6, one per input record, 2026-09-29 14:05–14:34. All ten passed the model check,
and none had to be re-run. Arm U used the UQS v18.4 repro S0+S1+S2 as input; arm B used the B2 single-prompt output.
The inputs had neutral IDs, and the key was not shown to the Stage 3 process.

**Rating.** Endpoints 2 and 3 were rated by two LLM raters. They worked in separate directories, read in opposite
orders, and were not shown the key. The rubric is `b2_stage3_rating/rubric_e2_e3.md`, frozen before rating (commit 5237dac).
Blinding was partial: the input records differ in format, so a rater can tell the arms apart. No human has verified the
ratings yet.

| endpoint | arm U (pipeline S1/S2 input) | arm B (B2 input) | pre-registered rule |
|---|---|---|---|
| 5. execution | 5/5 complete (§1–§6) | 5/5 complete | reported only |
| 1. SRG/CLA blocks anchored (quotation or location) | 25/26; per run 0.86–1.00 | 61/73; per run 0.73–1.00 | ranges overlap → no difference |
| 2. quotations misreporting the source (FAIL + WARN < 85, 74 rows) | 0 of 43 rows (both raters) | 0 of 31 rows (both raters) | no difference |
| 3. unsupported fills (content presented as if in the input, not supported, not flagged) | total 5 / 2 (rater A / B); per run 0–3 | total 18 / 17; per run 0–9 | B higher in total, but per-run ranges overlap and U also has fills |
| 4. Table 1 EP classes surfaced (of 10) | 8, 8, 8, 8, 8 | 9, 9, 10, 9, 10 | B higher (ranges do not overlap) |

The endpoint 2 class agreement between the raters is 62/74, and the A/B/C/S class splits differ mainly between B and C.
The endpoint 3 raters agree on the per-run pattern.

**Reading, by the pre-registered table.** The outcome is **mixed**, so it is reported per endpoint with no summary verdict.

- **Stage 3 runs on a single-prompt record** and, when told to, says explicitly that D-4 and TEMPERATURE_SUMMARY are absent.
  Execution therefore shows nothing either way.
- **Anchoring and quotation fidelity** do not separate the arms.
- **EP coverage is higher from the B2 input.** It surfaced 9–10 of the ten Table 1 EP classes, against 8 from the pipeline
  input. The Table 1 dictionary was assembled from several models' Stage 3 runs (EP-02a and EP-10a were added by
  cross-model convergence), so a longer, more exhaustive input record plausibly surfaces more of it.
- **Unsupported fills are more frequent from the B2 input** (17–18 against 2–5 in total), though the per-run ranges overlap.
  - *Kinds of fill.* Mostly internal-consistency errors: item classes that contradict the record's own tags, SRG
    cross-references to groups that do not contain the item, miscounted Table I entries, and a few invented details
    (for example, a metal attributed to a footnote).
  - *Where they concentrate.* In two B runs: 8–9 fills and 4–6 fills.
  - *Size.* No fill amounts to a fabricated finding.

**Consequence for the manuscript.**
- The sentence "whether it is needed for the downstream analyses has not been tested" is replaced by this result.
- On this check, the pipeline's Stage 1/2 structure is **not required** for Stage 3 to produce an anchored EP record of
  comparable quality. The single-prompt record even surfaced more EP classes.
- What the structured input bought was **fewer internal-consistency errors** in the Stage 3 record (descriptive, N = 5).
- This supports reducing the claim for the staged design to the auditability and internal consistency of its record,
  as the pre-registered table anticipated for this pattern.

**Caveats.**
- Same-model raters and partial blinding.
- N = 5 per arm.
- The Stage 3 prompt was written for the pipeline's format, and the adapter sentence was needed.
- The Table 1 dictionary is itself a pipeline product.
- In arm U, one record (repro run 5) carries the cross-paper quotation found earlier. The Stage 3 output did not repeat it.
