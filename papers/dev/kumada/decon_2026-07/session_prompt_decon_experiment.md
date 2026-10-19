---
title: Decontamination Control Experiment — Paper A Revision
created: 2026-07-19
purpose: Determine whether U-1 (homo-coupling absence) in Kumada 1972 analysis is genuine extraction or prompt recall
output_dir: papers/dev/kumada/decon_2026-07/
---

# Decontamination Control Experiment — Paper A / Kumada 1972 (v18.4)

## 背景と目的

Paper A（Digital Discovery 投稿済み）は kumada1972 を主要 showcase として使用している。
Post-submission audit により、v18.4 プロンプトに以下の **2 箇所の Kumada 固有コンテンツ**が確認された：

1. `prompts/v184/prompt_stage2_v184.md` lines 80–81 に、kumada1972 の E-proposition が
   "Good example" として **verbatim 収録**されている
2. `prompts/v184/prompt_stage1_turn2_v184.md` lines 105–107 に V2 primary selectivity の
   例として「Cross-coupling vs. homo-coupling」が記載されており、論文の showcase finding である
   **U-1（homo-coupling の自己矛盾的不在）のトピックドメインを直接 seed している**

これにより、Paper A が「新たに発見した」とする U-1 が、genuine extraction ではなく
prompt recall を反映している可能性が生じた。

**この実験**は、汚染箇所を generic な例に置換した decontaminated prompt で kumada1972 を
再実行（N=5、Sonnet 4.6 固定）し、U-1 と E-proposition が再現するかを確認する。

**二値判定**：
- U-1 が ≥3/5 run で出現 → genuine extraction、Paper A demonstration は開示注記で存続可
- U-1 が ≤2/5 run で出現 → prompt recall が支配的、showcase を Heck test-set 論文に差替え

---

## HARD CONSTRAINTS（開始前に確認、違反時は即停止）

1. **Model = Sonnet 4.6 ONLY** — `/model sonnet` でモデルを確認。Sonnet 4.6 以外の場合は停止
2. **`prompts/v184/` originals を書き換えない** — 変更版は `papers/dev/kumada/decon_2026-07/prompts_decon/` に保存
3. **`papers/_database/uqs_analysis_registry.csv` に触れない** — production run ではない
4. **`papers/dev/kumada/repro_2026-07/` のファイルを読まない** — 独立 run として実施
5. **全出力は `papers/dev/kumada/decon_2026-07/` 内にのみ保存**
6. **この実験の出力を Paper A2/B/C の empirical base に使わない** — Paper A revision 専用

---

## Step 1: モデル確認 + 汚染箇所の確認読み取り

```
/model sonnet
```

以下の 2 ファイルの該当箇所を Read して汚染内容を確認する：

- `prompts/v184/prompt_stage2_v184.md` lines 65–90
- `prompts/v184/prompt_stage1_turn2_v184.md` lines 95–120

---

## Step 2: Decontaminated プロンプトの作成

### 作業場所

```
papers/dev/kumada/decon_2026-07/prompts_decon/
```

v18.4 の Stage 0 / S1 Turn 1 / S1 Turn 3 / S1 Turn 4 / S2 の各ファイルを
`prompts/v184/` からこのフォルダに **コピー（名前は同じ、フォルダが decon 版を示す）**。

```bash
cp prompts/v184/prompt_stage0_v184.md papers/dev/kumada/decon_2026-07/prompts_decon/
cp prompts/v184/prompt_stage1_turn1_v184.md papers/dev/kumada/decon_2026-07/prompts_decon/
cp prompts/v184/prompt_stage1_turn2_v184.md papers/dev/kumada/decon_2026-07/prompts_decon/
cp prompts/v184/prompt_stage1_turn3_v184.md papers/dev/kumada/decon_2026-07/prompts_decon/
cp prompts/v184/prompt_stage1_turn4_v184.md papers/dev/kumada/decon_2026-07/prompts_decon/
cp prompts/v184/prompt_stage2_v184.md papers/dev/kumada/decon_2026-07/prompts_decon/
```

### 2a. Stage 2 プロンプトの修正

`papers/dev/kumada/decon_2026-07/prompts_decon/prompt_stage2_v184.md` の
**lines 75–81 のみ**を以下に置換する（他の箇所は変更しない）：

**置換前（lines 75–81）**:
```
  - **Bad examples** — do not produce any of these:
    - "...high-yield cross-coupling..." → "high-yield" is a feature, not scope
    - "...aryl and vinyl halides" → use "or" if the paper prints "or"
    - "...suppressing homocoupling products" → result phrase, not scope
    - "...to yield coupled products" → result clause, not scope
  - **Good example:** "Nickel-phosphine complexes catalyze selective
    cross-coupling of Grignard reagents with vinyl or aryl halides."
```

**置換後（decon 版）**:
```
  - **Bad examples** — do not produce any of these:
    - "...high-yield hydroformylation..." → "high-yield" is a feature, not scope
    - "...linear and branched aldehydes" → use "or" if the paper prints "or"
    - "...suppressing branching products" → result phrase, not scope
    - "...to yield linear products" → result clause, not scope
  - **Good example:** "Rhodium-phosphine complexes catalyze selective
    hydroformylation of terminal alkenes to linear aldehydes under syngas."
```

### 2b. Stage 1 Turn 2 プロンプトの修正

`papers/dev/kumada/decon_2026-07/prompts_decon/prompt_stage1_turn2_v184.md` の
**lines 103–110 のみ**を以下に置換する（他の箇所は変更しない）：

**置換前（lines 103–110）**:
```
  **Primary selectivity** (the paper's central claim) must be addressed
  first. Examples:
  - Cross-coupling vs. homo-coupling: is the preference for cross-coupled
    product governed by relative rates of competing reductive eliminations
    (kinetic control) or by thermodynamic product stability?
  - Regioselectivity: is the observed regiochemistry determined by the
    relative rates of oxidative addition at different positions, or by
    equilibration of intermediates?
```

**置換後（decon 版）**:
```
  **Primary selectivity** (the paper's central claim) must be addressed
  first. Examples:
  - Linear vs. branched product formation: is the regioselectivity governed
    by steric effects at the metal center (kinetic control) or by
    equilibration of insertion intermediates (thermodynamic control)?
  - Endo vs. exo selectivity: is the observed diastereoselectivity determined
    by the relative rates of competing transition states, or by post-reaction
    equilibration of intermediates?
```

### 確認

置換後、変更箇所のみ diff 確認：

```bash
diff prompts/v184/prompt_stage2_v184.md \
     papers/dev/kumada/decon_2026-07/prompts_decon/prompt_stage2_v184.md

diff prompts/v184/prompt_stage1_turn2_v184.md \
     papers/dev/kumada/decon_2026-07/prompts_decon/prompt_stage1_turn2_v184.md
```

**変更が 2 箇所のみ**（S2 の 7 行、T2 の 8 行）であることを確認してから次のステップへ。

---

## Step 3: Workflow でN=5 並列実行

### 出力ファイル命名規則

```
papers/dev/kumada/decon_2026-07/run{N}/kumada_v184decon_sonnet46_s{stage}.md
```

- `run1/` 〜 `run5/` の 5 フォルダ
- 各フォルダ内に s0, s1_turn1, s1_turn2, s1_turn3, s1_turn4, s1（Turn 4 統合版）, s2

### 実行プロセス（各 run）

以下の順序で decon プロンプトを使用して実行（通常の UQS 分析と同じ）:

1. **S0**: `prompts_decon/prompt_stage0_v184.md` + kumada1972 PDF
   - 論文 PDF: `papers/dev/kumada/Kumada_1972.pdf`（先頭大文字に注意）
   - 出力: `run{N}/kumada_v184decon_sonnet46_s0.md`

2. **S1 Turn 1–4** → 統合 S1:
   - 各 turn に対応する decon プロンプトを使用
   - 出力: `run{N}/kumada_v184decon_sonnet46_s1.md`（Turn 4 統合版）

3. **S2**: `prompts_decon/prompt_stage2_v184.md`
   - 出力: `run{N}/kumada_v184decon_sonnet46_s2.md`

### Workflow スクリプト

以下のようなスクリプト構造で N=5 を並列実行（各エージェントが 1 run を担当）:

```javascript
export const meta = {
  name: 'kumada-decon-n5',
  description: 'Decontamination control: N=5 parallel runs of kumada1972 with decon prompts',
  phases: [
    { title: 'ModelGate', detail: 'Verify Sonnet 4.6' },
    { title: 'Runs', detail: 'N=5 full pipeline S0→S2' },
  ],
}

// Step 0: Model verification
phase('ModelGate')
const gate = await agent(
  'Check the current model. Run the bash command: echo $CLAUDE_MODEL or look for model identity. ' +
  'The model MUST be claude-sonnet-4-6. Return JSON: { model: "<model_id>", ok: true/false }',
  { schema: { type: 'object', properties: { model: { type: 'string' }, ok: { type: 'boolean' } }, required: ['model', 'ok'] } }
)
if (!gate || !gate.ok) {
  log(`HARD STOP: model is ${gate?.model ?? 'unknown'}, required claude-sonnet-4-6`)
  return { error: 'model_mismatch', model: gate?.model }
}
log(`Model OK: ${gate.model}`)

// Step 1: Parallel N=5 runs
phase('Runs')
const runs = await parallel([1,2,3,4,5].map(n => () =>
  agent(
    `Run a complete UQS v18.4 pipeline (DECONTAMINATED version) on kumada1972.
    
CONSTRAINTS:
- Model must be Sonnet 4.6
- Use ONLY prompts from: papers/dev/kumada/decon_2026-07/prompts_decon/
- Do NOT use prompts from prompts/v184/ directly
- Save ALL outputs to: papers/dev/kumada/decon_2026-07/run${n}/
- File naming: kumada_v184decon_sonnet46_s{stage}.md

PIPELINE (execute in order, each step uses the context of all prior steps):
1. Read papers/dev/kumada/decon_2026-07/prompts_decon/prompt_stage0_v184.md
2. Read papers/dev/kumada/Kumada_1972.pdf (all pages if ≤20, split if more)
3. Execute Stage 0 → save run${n}/kumada_v184decon_sonnet46_s0.md
4. Read prompts_decon/prompt_stage1_turn1_v184.md → execute Turn 1 → save s1_turn1.md
5. Read prompts_decon/prompt_stage1_turn2_v184.md → execute Turn 2 → save s1_turn2.md
6. Read prompts_decon/prompt_stage1_turn3_v184.md → execute Turn 3 → save s1_turn3.md
7. Read prompts_decon/prompt_stage1_turn4_v184.md → execute Turn 4 → save s1_turn4.md
   (also produce the integrated Stage 1 output as s1.md)
8. Read prompts_decon/prompt_stage2_v184.md → execute Stage 2 → save s2.md

At the end, return a summary JSON:
{
  "run": ${n},
  "u1_present": true/false,  // U-1 (homo-coupling absence) appears in S1 output
  "u1_text": "...",          // the exact U-1 item text if present, else null
  "e_proposition": "...",    // the E-proposition text from S2
  "b_homo_present": true/false,  // B item about homo-coupling data absent
  "files_saved": ["list of saved files"]
}`,
    {
      label: `run${n}`,
      phase: 'Runs',
      schema: {
        type: 'object',
        properties: {
          run: { type: 'number' },
          u1_present: { type: 'boolean' },
          u1_text: { type: ['string', 'null'] },
          e_proposition: { type: 'string' },
          b_homo_present: { type: 'boolean' },
          files_saved: { type: 'array', items: { type: 'string' } }
        },
        required: ['run', 'u1_present', 'u1_text', 'e_proposition', 'b_homo_present', 'files_saved']
      }
    }
  )
))

return { gate, runs: runs.filter(Boolean) }
```

---

## Step 4: 評価とドキュメント作成

### U-1 出現率の集計

5 run のうち何回 U-1 が出現したかをカウント:

| 評価基準 | 判定 |
|---|---|
| 5/5 run で U-1 出現 | Genuine extraction。Paper A 継続（開示注記追加） |
| 4/5 run で U-1 出現 | Genuine extraction（1 run の偶発的欠落）。継続 |
| 3/5 run で U-1 出現 | Borderline。E-proposition の内容で最終判断 |
| 2/5 以下で U-1 出現 | Prompt recall が支配的。Showcase 差し替え必要 |

### E-proposition の比較

5 run の E-proposition テキストを並べ、原論文 v18.4 の E-proposition
（`papers/dev/kumada/kumada_v184_sonnet_s2.md` または `kumada_v19_sonnet46_s2.md`）と比較:

- **収束している**: decon 版でも同一フレーミング → genuine extraction の支持
- **発散している**: decon 版で異なるフレーミング → prompt が E-proposition を決定していた

### 評価ドキュメントの保存先

```
papers/dev/kumada/decon_2026-07/decon_evaluation_2026-07.md
```

---

## Step 5: 評価ドキュメントのテンプレート

```markdown
---
title: Decontamination Control Experiment — Evaluation
date: YYYY-MM-DD
runs_completed: N/5
verdict: genuine_extraction | prompt_recall | borderline
---

## 実験設定

- Base prompts: prompts/v184/ (decon modifications applied to S2 lines 75-81 and T2 lines 103-110)
- Model: Sonnet 4.6
- N runs: 5
- Paper: kumada1972 (Kumada 1972, JACS)

## Decontaminated 箇所

### Stage 2 変更（lines 75-81）
[置換前/後を記録]

### Stage 1 Turn 2 変更（lines 103-110）
[置換前/後を記録]

## U-1 出現率

| Run | U-1 present | U-1 text (要約) | B (homo-coupling) | E-proposition |
|-----|------------|-----------------|-------------------|---------------|
| 1   | Yes/No     | ...             | Yes/No            | ...           |
| 2   | ...        |                 |                   |               |
| 3   | ...        |                 |                   |               |
| 4   | ...        |                 |                   |               |
| 5   | ...        |                 |                   |               |
| **計** | **N/5** |               |                   |               |

## 原論文 v18.4 との比較

[v18.4 U-1 テキストと decon 版を並べて比較]

## 判定

**U-1 出現率**: N/5

**E-proposition 収束**: 収束/発散/部分一致

**最終判定**: [genuine_extraction | prompt_recall | borderline]

**Paper A への含意**:
- [ ] U-1 は genuine extraction → Paper A demonstration は存続、開示注記を追加
- [ ] U-1 は prompt recall → Showcase を Heck test-set 論文に差し替え
- [ ] Borderline → E-proposition 内容で最終判断 or N 追加

## Paper A revision への推奨テキスト

[Methods への追加節案または Showcase 差し替え提案]
```

---

## 注意事項

- 論文 PDF は `papers/dev/kumada/Kumada_1972.pdf`（先頭大文字）
- v18.4 の Stage 1 Turn 4 は複数バリアント（pilot_v4-v7 等）があるが、
  本実験では `prompt_stage1_turn4_v184.md`（バリアントなし）を使用
- Session 1 run あたりの context が重くなる場合は N=2-3 から始め、残りは別 session で実施可
- 実験失敗・中断した場合は `/record` を skip し失敗報告のみ

---

## 完了条件

1. N=5 run が完了、各 run に s0/s1/s2 の出力ファイルが保存されている
2. `decon_evaluation_2026-07.md` に上記テンプレートを埋めた評価ドキュメントが保存されている
3. 最終判定（genuine_extraction / prompt_recall / borderline）が明示されている
