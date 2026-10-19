# How the analyses were run, and how to re-run or audit them

*Deposit for "Mapping structured absences in scientific papers: an auditable LLM-assisted workflow demonstrated on
cross-coupling chemistry" (Digital Discovery, DD-ART-06-2026-000428). First written for the first-round revision
(R1, 2026-09-28); updated for the final R1 version, 2026-10-16.*

UQS is not a packaged program. It is a fixed sequence of prompts (Tier 1) applied by a large language model to one
paper at a time, in an interactive agent environment. This file records how that was done for the analyses in the
paper, where the execution departed from the stage prompts, what was not recorded, and how a third party can
either re-run the analyses or audit the deposited outputs without re-running them.

## 1. Environment

| Item | Value | Source |
|---|---|---|
| Execution environment | Claude Code (Anthropic's command-line agent), in interactive sessions and in sub-agents launched from a session | project records |
| Models | Claude Sonnet 4.6 (`claude-sonnet-4-6`) for Stages 0–4; Claude Opus 4.7 (`claude-opus-4-7`) for Stage 2F; other models only in the comparisons of SI-6 and the cross-checks listed in `zenodo_manifest.md` §1 | `model_info` line of each output |
| Model identity check | every deposited output records the model identifier reported by the environment; the check over the cited analyses is in `papers/_audits/paperA_quote_gate_R1_2026-09/model_identity_audit.log` | — |
| PDF input | the source PDF was read directly by the model (native multimodal input: text, figures, schemes and tables); no separate text extraction was used as input | Methods 6 |
| Sampling parameters | not set by the authors; Claude Code does not expose temperature or top-p, so the environment defaults applied. The values were not recorded | — |
| Claude Code version | not recorded | — |
| Execution dates | aggregate ranges per phase in `zenodo_manifest.md` §3; per-file dates in the file names or headers | — |

## 2. Procedure for one paper

The stages are applied in this order, each with its prompt file from Tier 1. Each stage's output is saved as a
Markdown file before the next stage starts.

| Step | Prompt file (Tier 1) | Output file |
|---|---|---|
| Stage 0 | `v184_production/prompt_stage0_v184.md` | `{paper}_v184_sonnet_s0.md` |
| Stage 1, Turn 1 | `v184_production/prompt_stage1_turn1_v184.md` | `{paper}_v184_sonnet_s1_turn1.md` |
| Stage 1, Turn 2 | `v184_production/prompt_stage1_turn2_v184.md` | `…_s1_turn2.md` |
| Stage 1, Turn 3 | `v184_production/prompt_stage1_turn3_v184.md` | `…_s1_turn3.md` |
| Stage 1, Turn 4 | `v184_production/prompt_stage1_turn4_v184.md` | `…_s1.md` |
| Stage 2 | `v184_production/prompt_stage2_v184_en.md` (Japanese-language cells, four context analyses and R1 control runs on Kumada 1972: `v184_production/prompt_stage2_v184.md`, as recorded by `prompt_version: stage2-v184-20260502` in their outputs; SI-7 row 23) | `…_s2_en.md` (English track; `…_s2.md`) |
| Stage 3 | `prompt_stage3_v2_en.md` (four context analyses: `prompt_stage3_v4.md`) | `…_s3v2_en.md` (`…_s3v4.md`) |
| Stage 4 | `prompt_stage4_v2_en.md` (four context analyses: `prompt_stage4_v6.md`) | `…_s4v2_en.md` (`…_s4v6.md`) |
| Stage 2F | `prompt_stage2f_v6.md`, `_v7.md`, `_v71.md` (Opus 4.7), over the group of papers | `kumada1972_{g1,g2,g3,all}_v184_opus47_s2f{,v7,v71}.md` |

The project's rule is to run Stages 0–2 (and Stage 3 when requested) of one paper in a single conversation, so that
Stage 2 sees the PDF and every earlier stage; the prompt files are written on that assumption.

The Japanese-language cells of the development-set multi-run (Kumada JA, Murai JA) used the Japanese versions of the Stage 2–4 prompts (`v184_production/prompt_stage2_v184.md`, `prompt_stage3_v2.md`, `prompt_stage4_v2.md`); their outputs have no `_en` suffix.

Multi-run outputs carry a run suffix (`_run2` … `_run6`); run 1 has no suffix. The ten refinement-set papers were
analysed with the v17 prompts (`tier_1_prompt_versions/v17_baseline/`) and Stage 3 / Stage 4 v1 and v2, and are named
`{paper}_v17_sonnet_…`.

## 3. How the batches were executed, and departures from the stage prompts

The run records (`improvements/` memos of 2026-05-10, kept in the project repository) describe the following.
Where they are silent, this is stated.

- **Development set, N = 6 multi-run (Phase 1.5, 2026-05-10).** Executed by sub-agents in six sequential batches
  (60 agents). The Stage 4 agents were given, in addition to the stage prompt, an explicit reminder to preserve
  non-anglicised given names (the "Pattern E" failure of SI-11.2). The exact wording of that instruction was not
  archived.
- **Nine EP-context papers (Phase 2, 2026-05-10).** Executed by sub-agents in eight sequential rounds, one round per
  stage and one agent per paper (72 agents). The records do not state how each agent was given the outputs of the
  earlier stages; within-conversation continuity across stages is therefore not claimed for these nine papers. Three
  Stage 2 runs (kumada1976b, breitenfeld2014, tamao2002) timed out and were re-run with an added length-budget hint;
  the hint's wording was not archived.
- **Stage 2F (Phase 2c).** Executed by twelve Opus 4.7 sub-agents in two rounds (sub-groups, then integration), each
  given a length budget in addition to the stage prompt.
- **Control experiments of the revision** (`papers/`): executed from written run instructions that are deposited
  with them (for example `papers/ablation_provenance/_run_kit/RUN_INSTRUCTIONS.md` and `KICKOFF_PROMPT.txt`), one
  fresh session per run.

## 4. Re-running an analysis

1. Obtain the source PDF from the DOI in `tier_2_input_metadata/paperA_21_paper_corpus_manifest.csv` (source PDFs
   are not deposited, for copyright reasons).
2. In a conversation with the model, provide the PDF and send the prompt files of §2 in order, saving each reply.
   Any interface that accepts a PDF and keeps the conversation history will do; the analyses in the paper used Claude
   Code.
3. Compare the new outputs with the deposited ones at the level the paper claims — SET membership and categorical
   structure, not identical wording (Methods 6; SI-11.1 re-execution checklist).

Model snapshots may be withdrawn by the provider; re-execution under another model version will give different
point outputs. Section 5 does not depend on re-execution.

## 5. Auditing without re-running

From the archive root:

```bash
shasum -a 256 -c CHECKSUMS.sha256                      # integrity of every file (also listed in MANIFEST.csv)
cd tier_4_classification_tables/reaggregation_R1
python3 reaggregate_top3.py                            # Top-3 EP SET re-count (SI-3)
python3 reaggregate_stage4.py                          # Stage 4 VQ-hierarchy-inversion re-count (SI-3)
python3 reaggregate_11papers.py                        # 11-paper re-count (SI-3)
```

The three scripts read the deposited per-run outputs under `tier_3_stage_outputs/` *(reviewer version only; redacted Markdown copies under `tier_8_redacted_public_raw_outputs/`)* and rewrite the CSV files next
to them; the rewritten files should be byte-identical to the deposited ones. They need Python 3 only.

The input-ablation control (SI-11.19) is re-scored with the two scripts in `papers/ablation_provenance/_scoring/`
(Python 3 and `pdftotext` from Poppler; the source PDFs must be obtained from their DOIs):

```bash
python3 anchor_matcher.py    <paper.pdf> [<si.pdf>] ../_run_kit/stub_<paper>.txt ../<paper>/arm<P|W>/run*/*.md
python3 specifics_matcher.py <paper.pdf> [<si.pdf>] ../_run_kit/stub_<paper>.txt ../<paper>/arm<P|W>/run*/*.md
```

Pass the PDF paths as separate arguments (in shells that do not split variables, such as zsh, a single quoted
string holding two paths is read as one missing file and every quote then scores as not found).

The quote-provenance gate and the model-identity check of Methods 6 are documented, with their outputs and the
manual adjudication, in `papers/_audits/paperA_quote_gate_R1_2026-09/README.md`.

## 6. Not provided

- An end-to-end program that runs the pipeline unattended. The analyses were run interactively as described above.
- The orchestration instructions given to sub-agents (§3), beyond what the run records describe.
- Sampling parameters and the Claude Code version (§1).
