# GPT-5.4 Thinking — Kumada 1972 Comparison Run

> **Note (2026-10-19).** This README is the plan written before the run. The run used the v17 prompts (Stage 3 and Stage 4 v2), and this folder holds `kumada_v17_gpt54thinking_s0`–`s4` (merged Stage 1 file) and six Stage 4 retrieval-depth runs (`s4v2_retrieval_depth_run1`–`3` with Stage 4 v2, `s4v6_retrieval_depth_run1`–`3` with Stage 4 v6), with the two prompt files `PASTE_PROMPT_v2.md` and `PASTE_PROMPT_v6.md`. Three of them (`s4v2` run 2, `s4v6` runs 1 and 3) record GPT-5.5 Thinking in `model_info`; the folder name keeps the planned model.

**Purpose**: Cross-vendor model comparison for SI-6 (Discussion 3 post-training-profile hypothesis).

**Input paper**: Tamao, Sumitani, Kumada, *J. Am. Chem. Soc.* **1972**, *94*, 4374–4376 (same file as the existing Claude-family comparison at `papers/dev/kumada/Kumada_1972.pdf`).

**Model**: GPT-5.4 Thinking.

**Prompt version**: TBD. Two sensible choices:
- **v15** (strict parity with existing `devset_kumada_v15_{haiku,sonnet,opus}.md`).
- **v17** (current production version; allows Discussion 3 to reference the same prompt as the rest of the paper). If v17 is chosen, the Claude-family baseline should be re-run with v17 as well for apples-to-apples comparison.

**Expected output files** (per CLAUDE.md naming convention):

```
kumada_v{N}_gpt54thinking_s0.md
kumada_v{N}_gpt54thinking_s1_turn1.md
kumada_v{N}_gpt54thinking_s1_turn2.md
kumada_v{N}_gpt54thinking_s1_turn3.md
kumada_v{N}_gpt54thinking_s1.md          # Turn 4 synthesis
kumada_v{N}_gpt54thinking_s2.md
```

Where `{N}` = `15` or `17` per the choice above.

**Execution note**: Run all stages sequentially in a single session so Stage 2 has full Turn 1–3 context, per CLAUDE.md §"実行ステップ".

**Comparison dimensions** (per SI-6.2): output volume, question-generation breadth (V1/V2/V3 new vs duplicate), A/B/C/U classification density, D-4 candidate count and unique-insight set, E-section transformations with T2/T3 discipline, `scope_type` accuracy, output-discipline compliance (no prohibited explanatory prose).

**Relevance to Discussion 3**: GPT-5.4 Thinking is a reasoning-oriented model from OpenAI; the comparison tests whether the capability profile observed in Claude Sonnet/Opus (structural compliance with multi-stage prompts, T1/T2/T3 anchoring discipline, D-4 generation with complete metadata) transfers across vendors and post-training regimes, or is Claude-specific.

**Destination**: Results feed SI-6 and the comparison file `analysis/analysis_model_comparison_v{N}.md` (add a GPT-5.4 Thinking section parallel to the existing Haiku/Sonnet/Opus sections).
