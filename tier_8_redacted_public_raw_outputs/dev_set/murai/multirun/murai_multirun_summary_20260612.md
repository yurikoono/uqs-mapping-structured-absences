> # ⚠️ SUPERSEDED — QUANTITATIVE CLAIMS WITHDRAWN (2026-08-29)
>
> **Every quantitative statement in this file is withdrawn and must not be cited.** A
> pre-submission audit found the underlying candidate ledger keyed at author–year
> granularity: one run can list the same paper as several rows, and verification verdicts
> attach to author–year bins rather than to paper identities, so no paper-level statistic
> (recurrence, robust-core membership, verified-candidate rate, per-arm failure rate,
> Jaccard) is reliably reconstructible from it. This includes the "15 / 18", "101 / 125",
> "24 fabricated", the per-arm percentages, and the replication verdicts in the findings
> table below.
>
> The withdrawal is *not* repaired by recounting, because the derived statistics share the
> key defect. See **`RECOUNT_NOTE_20260829.md`** in this directory, which supersedes this
> file. The published paper's multi-run observations rest on the Kumada 1972 pilot alone.
>
> The per-run output files in this directory remain valid as stored records; only the
> aggregate statistics computed from them are withdrawn.

# Murai 1993 cross-vendor multi-run Stage 4 study — summary (n = 2 extension)

**Date**: 2026-06-12. **Purpose**: extend the single-paper (Kumada 1972) multi-run robustness study to a second dev-set paper (Murai 1993), addressing the "multi-run robustness is single-paper" limitation (Discussion §4.6; Fable5 review Concern 5).

## Design (Claude-family arm)

- **Source paper**: Murai *et al.*, *Nature* 1993, **366**, 529–531 (Ru₃(CO)₁₂-catalysed ortho-selective C–H alkylation of aromatic ketones with olefins).
- **Inputs**: v17 baseline Stage 0–3 outputs (`murai_v17_sonnet_s0–s3.md`) + source PDF, identical across runs.
- **Matrix**: 3 Claude-family vendors × 2 Stage 4 prompts (v2, v6) × 3 fresh independent runs = **18 runs**. Each run executed by a subagent running as the named vendor model, instructed to retrieve only genuinely-recalled real filling papers and to keep low-confidence candidates (no fabrication to fill gaps).
- **Verification**: every unique candidate (45) web-verified (real / fabricated). 125 candidate-instances total; 101 verified-real, 24 fabricated.
- **Run files**: `papers/dev/murai/multirun/murai_v17_{sonnet,opus48,haiku}_s4{v2,v6}_retrieval_depth_run{1,2,3}.md`.

### Honest caveats (read before comparing to the Kumada n = 24 study)

1. **Claude-family only.** The GPT-5.4 web-augmented arm of the Kumada study was **not** reproduced (no OpenAI access in this environment); the web-augmentation finding is therefore *not* re-tested here. Only the parametric-retrieval (Claude Read-tool) arm is replicated.
2. **Model snapshots differ.** This run used the current **Opus 4.8** (the Kumada study used Opus 4.7), current Sonnet, and Haiku 4.5. Absolute rates are not directly comparable across snapshots; the *qualitative pattern* is the object of comparison.
3. **Paper-dependence.** Murai 1993 is post-1980 and not author-network-dense (risk factors F1/F2 not satisfied), so lower absolute fabrication than the Kumada Haiku arm is expected and observed — consistent with the paper-dependent-hallucination thesis itself.

## Findings — the four Kumada regularities replicate on Murai

| Finding (Kumada n = 24) | Murai n = 18 (Claude-family) | Replicates? |
|---|---|---|
| **Robust-core convergence** — one canonical Communication→Full-Paper candidate dominates (Tamao 1976 BCSJ, 23/24 = 96%) | **Kakiuchi/Murai 1995 BCSJ (68, 62–83)** — the Full-Paper follow-up to the Murai 1993 *Nature* Communication — retrieved in **15/18 runs (83%)**; next: Kakiuchi 2002 *Acc. Chem. Res.* 8/18, Chatani 1998 6/18 | **Yes** |
| **Run-to-run stochasticity** — within-prompt Jaccard 0.30–0.65 | within-cell pairwise Jaccard (real candidates) **0.08–0.55** (mean 0.08–0.55 across cells; lowest Opus v2, highest Sonnet v6) — substantial, universal across vendors | **Yes** (range slightly wider/lower) |
| **Model-size hallucination gradient** — Haiku 5–10/run > Sonnet 1–3 > Opus 0–1 | **Haiku 32% (mean 2/run, 0–5) > Sonnet 14% (1.3/run, 0–3) ≈ Opus 4.8 13% (0.7/run, 0–2)** | **Yes** (gradient direction identical; absolute magnitudes lower, as expected for a non-network-dense post-1980 paper) |
| **Tier paper-conditioned stability** — Self-Tier 95–100% consistent across runs | 10/13 (77%) multi-run real candidates have a dominant (≥60%) Self-Tier | **Partly** (majority-stable but weaker than Kumada's near-unanimity) |

## Interpretation

The core structural claims that motivate UQS 2.0's multi-run aggregation and risk-conditional verification mechanisms — robust-core convergence, irreducible run-to-run stochasticity, and the model-size hallucination gradient — **hold on a second source paper**, no longer resting on Kumada 1972 alone. The model-size gradient is directional-identical on Murai even though Murai's lower risk-factor profile yields lower absolute fabrication, which is itself consistent with the paper-dependent-hallucination thesis. The Tier-stability replication is weaker (77% vs 95–100%), a point worth flagging.

What is **not** established here: the web-augmentation effect (GPT arm not run), and any cross-snapshot quantitative equivalence (Opus 4.8 ≠ 4.7). A full 4-vendor Murai replication including GPT-5.x with web search remains for external execution.

Per-run candidate lists and the verification verdicts are deposited alongside this summary.
