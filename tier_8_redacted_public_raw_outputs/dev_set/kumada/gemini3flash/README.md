# Gemini Trial Run (Auto-Selected) — INTERNAL METHODOLOGY RECORD ONLY

## Status

**This data is retained as an internal working record and is NOT part of the published SI-6 four-model comparison.**

See `manuscript/si/output/SI-6.md` SI-6.1 scope note and `manuscript/si/output/si_issues_log.md` Issue #1 for the decision rationale.

## What happened (2026-04-18)

A trial run on Kumada 1972 was initiated via Antigravity with the intent of targeting **Gemini 3 Flash**. The platform auto-selected **Gemini 1.5 Pro** instead (model auto-selection based on input complexity). The resulting output files in this folder are therefore Gemini 1.5 Pro output, not Gemini 3 Flash output.

## Why this run is excluded from SI-6

1. **Not model-pinned**: the executed model differs from the user-intended model. This breaks the experimental-control invariant that SI-6 requires for apples-to-apples comparison.
2. **Cross-generation**: Gemini 1.5 Pro (2024-era) is one generation behind the other SI-6 comparators (Claude Sonnet 4.6 / Opus 4 / GPT-5.4 Thinking, all 2025–26 frontier reasoning models). Comparing across generations confounds "model-family differences" with "generation-and-scale differences."
3. **Analytically unnecessary**: the SI-6.5 post-training-profile argument rests on (i) the within-Claude-family capability threshold (Haiku ≪ Sonnet ≈ Opus) and (ii) the cross-vendor convergence between Sonnet and GPT-5.4 Thinking. A divergent fifth model from a third vendor does not strengthen the argument and would invite legitimate methodological pushback.
4. **Publication fairness**: using a 2024-era model's partial output as a negative example against 2025–26 reasoning models is not a fair benchmark of the Gemini family. A publicly released comparison based on this trial would misrepresent Google's current capability.

## What this data IS useful for

- **Multimodal PDF reading diagnostic**: the diagnostic questions (Scheme 1 intermediate geometry; Table I footnote-f attribution; eq 3 R–R mass-balance observation) confirmed that the platform's multimodal PDF pipeline is functioning — this is an operational finding that is useful for future UQS runs on other Gemini models or via other platforms.
- **VQ-2 judgment as operational calibration point**: the divergence (Gemini 1.5 Pro → VQ-2; Claude Sonnet + GPT-5.4 Thinking → VQ-1) shows that the VQ-2 gate's severity calibration is model-sensitive. This is a methodology finding that feeds into improvements/open_issues.md rather than SI-6.
- **Planning reference for future Gemini runs**: if Gemini 3 Flash (or a later variant) becomes model-pinnable via Antigravity or the Gemini API, this trial serves as the "before" observation against which the pinned run can be compared to isolate model-version effects.

## Files in this folder

The five output files are in the sub-folder `GPT1.5/` (a folder name given at the time of the run; the files are Gemini 1.5 Pro outputs, as their `model_info` lines state).

| File | Content |
|---|---|
| `kumada_v17_gemini3_s0.md` | Stage 0 output (auto-selected Gemini 1.5 Pro; `model_info:` field self-reports accurately) |
| `kumada_v17_gemini3_s1.md` | Stage 1 output with Turns 1–4 merged into one file (deviates from v13+ convention) |
| `kumada_v17_gemini3_s2.md` | Stage 2 output |
| `kumada_v17_gemini3_s3.md` | Stage 3 output (judges VQ-2 — more lenient than Sonnet/GPT-5.4's VQ-1) |
| `kumada_v17_gemini3_s4.md` | Stage 4 output |

The `gemini3` in the filenames reflects the user-intended target; the actual executing model was Gemini 1.5 Pro per the internal `model_info:` field of each file. If a model-pinned Gemini 3 Flash run is later performed, files should be named `kumada_v17_gemini3flash_s{N}.md` and kept in a separate sibling folder.

## Do not cite this data in the manuscript

The published SI-6 documents a four-model comparison (Claude Haiku + Claude Sonnet + Claude Opus + GPT-5.4 Thinking). The Gemini run in this folder is NOT referenced in SI-6.md, SI-6.7 (section deleted), or the reconciliation table. Citing this trial in public-facing material would be methodologically inconsistent with the scope decision documented above.
