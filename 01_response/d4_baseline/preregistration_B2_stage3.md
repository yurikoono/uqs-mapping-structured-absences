---
title: Paper A R1 — does Stage 3 need the pipeline's Stage 1/2 structure? (B2 → Stage 3) — pre-registration
created: 2026-09-29
status: active
audience: paperA
open_questions: false
---

# Pre-registration: B2 → Stage 3

**Status: approved by the author on 2026-09-29 and frozen at this commit. Nothing had been run when it was frozen.**

## Question

Methods 6 now states that the pipeline's D-4 candidates, evidence chains and EP dictionary are "a difference of design, not
a demonstrated advantage, and whether it is needed for the downstream analyses has not been tested". This check tests
exactly that. Does the Stage 3 analysis (the EP derivation of Results Part 1) produce an equally anchored and faithful
EP record when it is fed a length-matched single-prompt output (B2) instead of the pipeline's Stage 1/2 record?

**Not an endpoint: whether Stage 3 "runs".** Stage 3 v2 was written to read the pipeline's own Stage 1/2 format. A crash
or a refusal on B2 input would show only that the prompt expects its own input format. Execution failure is therefore
recorded and reported, but it counts as evidence for neither reading. The informative outcomes are about the content of the
output.

## Design

- **Arms.** Arm U takes as input the UQS repro runs 1–5: Kumada 1972 v18.4 S0 + S1 + S2, `papers/dev/kumada/repro_2026-07/`.
  Arm B takes the B2 runs 1–5, full recovered text, from `papers/dev/kumada/baseline_R1_2026-09/`. N = 5 per arm, one Stage 3
  run per input run.
- **Stage 3 prompt.** `prompts/stage2f3/prompt_stage3_v2_en.md`, unchanged (SHA-256 `b1358ff4…`, as in SI-7).
- **Execution.** Both arms run identically: a fresh `claude -p` process with Sonnet 4.6, reading the PDF and the input files.
  This departs from the paper's usual single-context S0→S3 session, and it does so equally for both arms.
- **Adapter text.** The same for both arms, verbatim:
  > "The file(s) below are the Stage 1/2 record of this paper. Apply the Stage 3 prompt to them and to the PDF. Where the prompt refers to a field the record does not contain, say so explicitly rather than supplying it."
- **Blinding.** The Stage 3 process is not told which arm it is in. The file names are neutral (`record_run{k}.md`).

## Endpoints

Each endpoint is scored per SRG/CLA block of each Stage 3 output.

1. **Evidence Pack anchoring** (the D3 E4 wording): the block names an EP class, and quotes the paper or gives a location in it.
   Item IDs do not count.
2. **Anchor fidelity.** Run the quote gate on the Stage 3 output. FAILs and WARNs below 85 are classified as in SI-11.20.
   Count the quotations that do not faithfully report the source.
3. **Support by the input record.** For each block, check whether the member items it cites exist in the input record.
   **The central count is blocks, or statements inside blocks, that fill a slot the input does not contain** — for example
   a D-4-dependent field written for a B2 input that has no D-4 — without saying that it is missing (a fabricated bridge).
4. **Which EPs surface.** Take the set of EP classes that surface and compare it with the ten-EP dictionary of Table 1, as
   overlap counts. Labels are compared as classes, not wording.
5. **Execution status**: completed, partial, or failed. This is reported, not scored.

Scoring is done on the rubric above. The raters are two LLM raters blind to arm, with separate directories, plus author
verification of every block counted under endpoint 3 and every misquotation under endpoint 2.

## Readings (fixed before the run)

| outcome | reading |
|---|---|
| Arm B matches arm U on endpoints 1–4, with overlapping ranges | Stage 3 does not need the pipeline's Stage 1/2 structure. The manuscript says so, and the claim for the staged design reduces to auditability of the record. |
| Arm B is lower on 1, 2 or 4 with non-overlapping ranges, **or** arm B shows fabricated bridges (3) that arm U does not | The Stage 1/2 structure is a precondition for an anchored EP record. This is reported as evidence for the design, with N = 5 and the same-model-rater caveat. |
| Arm B fails to execute | Reported. No reading: this shows only prompt–input coupling. |
| Mixed | Reported per endpoint, with no summary verdict. |

## Cost

Ten Stage 3 runs, roughly 1–2 hours of wall time, then rating with the same procedure as the D4 re-adjudication.

## Implementation details (fixed at freeze)

- **Staging.** Each input record is copied into `papers/dev/kumada/b2_stage3_R1_2026-09/in_{id}/record.md`, where
  `{id}` is a random 6-digit ID (`random.Random(20260929)`). The key (id → arm, run) is kept in `_key.json`, and the
  Stage 3 process is never shown it.
- **Arm U record.** The repro run's `s0`, `s1` and `s2` files, concatenated in that order, each preceded by a
  `--- file: s0 ---`-style separator.
- **Arm B record.** The B2 run file, with its HTML header comment (which names the arm) removed.
- **Target paper instruction.** The same middle-communication boundary sentence as in the reproducibility study.
- **Output.** `…/in_{id}/s3.md`, written by the Stage 3 process with the Write tool. The CLI JSON is kept, and the full text is
  recovered from the session transcript if the result field is truncated.
- **Model check.** `modelUsage` must be `claude-sonnet-4-6`; a run that fails the check is discarded and re-run once.
