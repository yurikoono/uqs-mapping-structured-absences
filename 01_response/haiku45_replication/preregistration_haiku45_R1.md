---
title: Paper A R1 — Haiku 4.5 replication of the SI-6 arm before the model's deprecation floor (pre-registration)
created: 2026-09-29
status: active
audience: paperA
open_questions: false
---

# Pre-registration: Haiku 4.5 replication of the SI-6 arm

**Frozen at commit, before any run.**

**Why.** SI-6 (the four-model comparison) contains a single Haiku 4.5 run (2026-04-19). The deprecation floor of Haiku 4.5
is 2026-10-15 (Anthropic model-deprecations page, checked 2026-09-29; commit 859fc60), and no successor is named.
Referee 2 point 3 asks about reproducibility across models. After that date, the Haiku arm can no longer be re-run.

**Position in the paper: insurance, not a dependency.** Paper A's position is that the deposited record can be audited
without re-running anything. These runs are extra evidence that the SI-6 Haiku result is not a single draw. No claim in
the paper will be made to depend on them, and their result will be reported whichever way it comes out.

**Configuration** (read from SI-6 and from the archived output headers, not from memory):
- Paper: Kumada 1972. The input is `papers/dev/kumada/Kumada_1972.pdf`. The target is the middle communication; use the
  same instruction as the reproducibility study.
- S0–S2: `prompts/v17/` (`prompt_stage0_v17.md`, turn1–turn4 `_v17.md`, `prompt_stage2_v17.md`). The archived Haiku S2 header
  reads `stage2-v17-20260415`, which is the JA/EN-mixed file, not `_en`.
- Stage 3: `prompts/stage2f3/prompt_stage3_v2.md`. The archived header reads `stage3-v2-20260416`, the JA file; its SHA-256
  matches SI-7.
- Stage 4: **not run**. It needs literature retrieval, and the insurance purpose concerns the S0–S3 structural outputs
  that SI-6 compares.
- Model: `claude-haiku-4-5`, verified from the CLI `modelUsage` field. The archived runs record `claude-haiku-4-5-20251001`;
  the CLI alias is assumed to resolve to the same snapshot, and this is recorded as an assumption.
- Session: single context, S0 → S1 turn1–4 → S2 → S3, one fresh process per replicate, **N = 3**.
- Output names: `papers/dev/kumada/haiku45_repro_2026-09/kumada_v17_haiku45_repro_run{k}_{s0,s1_turn1,s1_turn2,s1_turn3,s1,s2,s3v2}.md`.

**Prompt identity.** The v17 prompt files have filesystem mtimes of 2026-04-15 13:46–13:54, before the 2026-04-19 runs,
and their `prompt_version` tags match the archived output headers. Git history starts at the 2026-06-10 snapshot, so git
alone cannot prove identity. The v17 hashes are not in SI-7; adding them is a separate fix.

**Endpoints** (descriptive only; there is no success criterion). For each run, and for the archived run alongside:
1. structural completeness: A/B/C/U taxonomy, same_root_groups, D-4 with `grounded_in` and `key_quote`, E section,
   `scope_type`, and the Stage 3 §1–§6 sections;
2. counts of SRGs (S3), D-4 candidates, U items, and U items flagged self-contradictory; the scope_type label;
3. **overlap at the level of which absences surfaced**, not labels: for each of the six SRG roots of Kumada 1972 reported
   in SI-6 / Results Part 1, whether the run's S1 META or S3 contains a group with that root, adjudicated against the SRG
   descriptions in the archived Sonnet S3;
4. quote gate on S0–S2, with FAILs and WARNs below 85 classified as in SI-11.20.

**Reporting.** Results go into SI-6 as an addendum. Stability of which absences surface is reported separately from
stability of labels and counts.
