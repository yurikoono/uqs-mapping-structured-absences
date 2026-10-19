---
title: session handover v15 to v16
created: 2026-05-28
status: active
audience: meeting
open_questions: false
backfilled: true
---

# セッション引き継ぎ文書：v15 → v16 プロンプト改善と解析再開
<!-- 作成日: 2026-04-14 -->
<!-- 前セッション完了物: app1, app2, comp1, comp2 (4報) -->

---

## このセッションで行うこと（2ステップ）

**Step A**: v15プロンプトをv16に改訂する
**Step B**: v16を用いてhom1から残り6報の解析を実行する

解析はhom1 → hom2 → het1 → het2 → scr1 → scr2 の順に進める。
各論文について Stage 0 → Turn 1 → Turn 2 → Turn 3 → Turn 4 → Stage 2 の
全パイプラインを完走する（CLAUDE.mdの手順に従う）。

---

## Part A: v16プロンプト改訂

### 改訂元ファイル

```
<project-root>/prompts/v15/
  prompt_stage0_v15.md
  prompt_stage1_turn1_v15.md
  prompt_stage1_turn2_v15.md
  prompt_stage1_turn3_v15.md
  prompt_stage1_turn4_v15.md
  prompt_stage2_v15.md
```

### 改訂先ファイル

上記を `prompts/v16/` にコピーし、以下の改訂を施す。
**ファイル内の `v15` という文字列はすべて `v16` に更新すること。**
（prompt_version: stage1-v15-20260331 → stage1-v16-YYYYMMDD 等）

---

### 改訂内容一覧

改訂の根拠詳細は以下で参照できる：
`improvements/improvement_proposals_batch1.md`

以下は「何を・どこに・どう書き換えるか」の実装仕様。

---

#### [A-1] prompt_stage1_turn1_v15.md → v16
**追記場所**: プロンプト冒頭のコンテキスト参照指示の直後

**追記内容**:
```
**Erratum / correction handling:** If S0-7 reports an erratum, correction,
or note added in proof that corrects specific content (e.g., "errors in
Scheme 2"), treat the corrected version as the authoritative source for
that content. Do not generate questions based on the uncorrected version
of the affected passage. Where the erratum does not specify what was
corrected, flag the affected content with [erratum — corrected version
unclear] and avoid strong interpretive claims about that passage.
```

---

#### [A-2] prompt_stage1_turn2_v15.md → v16

**追記1 — "Field differentiation rule (mandatory)" の末尾に追加**:
```
**V2 pre-emption declaration:** At the end of the `field:` line in your
output, append `[preempts_turn3_default: yes]` if the field you have
selected is the same field that Turn 3's guidance table would recommend
for V3 (e.g., you select computational chemistry when DFT is present in
the paper). This flag tells V3 to choose an alternative field.
```

**追記2 — 選択性トリガー（"Secondary selectivity" ブロック）の末尾に追加**:
```
**Independence from field choice:** The selectivity trigger applies
regardless of which field V2 adopts. Even when V2 selects a computational
methodology field, V2 must still check: "Does the paper report selectivity
data (yield ratios, er, dr, regio- or chemoselectivity)?" If yes, generate
at least one question asking whether the observed selectivity is kinetically
or thermodynamically controlled — as a separate, explicitly labeled
question independent of the DFT methodology questions.
```

**追記3 — DFTトリガー（"absence-based field triggers" のDFT項）に追加**:
```
**DFT reporting checklist (mandatory when V2 adopts computational
chemistry):** For each item below that is absent from the paper's DFT
methodology description, generate one question:
1. Energy type: Is ΔE (electronic energy), ΔH (enthalpy), or ΔG (Gibbs
   free energy) reported? Were thermochemical corrections (ZPE, thermal,
   entropy) applied?
2. Dispersion correction: Was D3BJ or equivalent applied? (Especially
   relevant for Pd complexes, π-systems, or bulky ligands.)
3. Solvation model: Was implicit solvation (PCM / SMD / COSMO) applied?
   Relevant if any intermediate is ionic/charged or if the experimental
   solvent is polar (DMF, MeCN, MeOH, etc.).
4. Conformational sampling: How were the lowest-energy TS structures
   identified? (Grid search, CREST, systematic dihedral scan, assertion?)
5. Reference state: In energy profiles, is the zero-energy reference
   clearly defined, and is it the genuine resting state or an artificial
   intermediate?
6. Temperature consistency: Are thermochemical corrections computed at
   the actual reaction temperature, or at default 298.15 K?
Generate a question for each absent item that is relevant to the paper's
mechanistic or selectivity conclusions. Do not generate questions for
items that are irrelevant to the paper's claims.
```

---

#### [A-3] prompt_stage1_turn3_v15.md → v16

**書き換え — 判定表の直後（"These triggers are illustrative" の前）に挿入**:
```
**Pre-emption check (mandatory first step):** Before selecting a field,
read V2's output header. If V2 declared `[preempts_turn3_default: yes]`,
the field this table recommends is unavailable to V3. In that case:
1. State which field V2 took and why it is pre-empted.
2. Select the next most important methodological perspective not covered
   by V1 or V2. Guidance by paper type:
   - DFT paper already taken by V2 → prioritize:
     * NMR spectroscopy / quantitative analytical chemistry (if ³¹P/¹H
       NMR monitoring or NMR-derived equilibrium constants are primary
       evidence)
     * Chemical kinetics / physical chemistry (if rate constants or
       activation parameters are primary evidence)
     * Analytical chemistry / chromatography (if HPLC/GC-MS product
       quantification is primary evidence)
   - State the alternative choice and the pre-emption reason explicitly
     in the `field_rationale` field.
```

---

#### [A-4] prompt_stage1_turn4_v15.md → v16

**書き換え1 — C項目定義ブロックの冒頭に追加**:
```
**Antagonist reference exclusion (check before classifying C items):**
A reference that was the direct experimental target of the paper — i.e.,
the paper designed specific experiments to refute or confirm it — is
FULLY ENGAGED and must NOT be classified as C, even if no side-by-side
comparison table exists. Indicator phrases in the paper: "to rule out,"
"against the mechanism proposed by [ref]," "in contrast to [ref],"
"to test the hypothesis of [ref]," "refuting [ref]."
If you initially flag such a reference as a C candidate, reclassify it
immediately and note "fully engaged antagonist — excluded from C" in
your working notes.
```

**書き換え2 — B項目の "Classifications:" 行を更新**:
```
[現行]
"Classifications: methodological_limitation / intentional_narrowing / mixed"

[改訂後]
"Classifications: methodological_limitation / intentional_narrowing /
reporting_omission / mixed

reporting_omission: A standard methodological datum that the field
conventionally requires in reporting (e.g., thermochemical correction
type for DFT results, NMR acquisition parameters for quantitative NMR,
HPLC calibration details for selectivity claims) that is entirely absent
from the paper — with no acknowledgment of the omission and no limiting
statement. Unlike methodological_limitation (which involves an explicitly
acknowledged constraint), reporting_omission involves no textual
acknowledgment at all. The rhetorical_function field should read 'not
stated in paper.'
Use this classification when: (a) the paper presents a quantitative
claim, (b) a standard datum required to evaluate that claim is absent,
and (c) no U classification is needed because the item fits B's
structural role (it describes a boundary of what the paper did)."
```

**書き換え3 — "Step 1: Compute cross_field_temperature" の規則説明に追加**:
```
**Counting overlaps toward convergence:**
Overlap entries (V2-OVn, V3-OVn) count as agent flags for convergence
purposes:
- V1 raises Q as a new question → convergence contribution: 1
- V2 records Q as V2-OVn (overlap re-evaluation) → contribution: 2
  (convergence = 2/3 between V1 and V2)
- V3 also records Q as V3-OVn → contribution: 3 (convergence = 3/3)
The temperature_gap is computed from all three severity values (V1, V2,
V3) regardless of whether they appear as new questions or overlap
re-evaluations. The severity_V2 value comes from the V2-OVn entry;
the severity_V3 value comes from the V3-OVn entry.
```

**書き換え4 — TEMPERATURE_SUMMARY フォーマットの note として追加**:
```
Note on expected frequency: In practice, high_convergence_high_gap is
frequently empty because agents in adjacent fields rarely disagree on
severity by more than one step (distance > 1). An empty
high_convergence_high_gap list is the normal case, not an exception.
The fallback rule is the standard D-4 selection path when this list
is empty — apply it without qualification.
```

---

#### [A-5] prompt_stage2_v15.md → v16

**書き換え1 — "Scope of the propositional form (E)" ブロックの末尾に追加**:
```
**Mechanism papers:** For papers whose S0-1 core_claim describes a
mechanistic finding (a pathway re-assignment, rate-determining step
identification, or mechanistic distinction) rather than a new synthetic
transformation, the confirmed_english_propositional describes the
transformation studied — not the mechanistic finding itself. The
proposition must still end after naming the substrate scope (no mechanism
clause). Example:
  Correct:   "Palladium complexes catalyze copper-free Heck–Cassar–
              Sonogashira cross-coupling of terminal alkynes with aryl
              halides or triflates."
  Incorrect: "...via direct alkyne coordination rather than Pd(II)–Pd(II)
              transmetalation." [mechanism clause — prohibited]
The mechanistic finding belongs in confirmed_english_question only.
```

**書き換え2 — D-4 セクションの "テキスト根拠の要件" ブロック内 key_quote 説明を修正**:
```
[現行]
key_quote: [根拠となる論文テキストの一文]

[改訂後]
key_quote: [根拠となる論文メインテキストの一文。Supporting Information
            (ESI/SI) の記述は使用不可。メインテキストに直接の根拠が存在
            しない場合は、最も近い文脈を提供するメインテキストの一文を
            使用し、T2またはT3とラベルを付ける]
```

**書き換え3 — D-4 "出発点となる視点" リストに追加（末尾の熱力学項の直後）**:
```
- 否定的証拠の分析的根拠：論文が「検出されず」「観測されず」という
  結果を肯定的な機構的証拠として用いている場合、その検出下限・検出
  条件が主テキストに記載されているかを必ず確認すること。
  「検出されない = 存在しない」と「検出されない = 検出感度以下」を
  区別するために必要な実験的根拠が欠けている場合は、D-4候補として
  記録すること。（B-itemフラグ "negative result as evidence" が付いた
  B項目は特に注意して確認すること。）
```

**書き換え4 — D-4 "priority_structure" 指示を拡張**:
```
[現行末尾]
"どのA・B項目がその構造の根拠になるかを明示してください。"

[改訂後]
"どのA・B項目がその構造の根拠になるかを明示してください。
特に以下の「ピボット構造」を探索すること：
- 論文の中心的主張を成立させるために、ある実験的説明が「今後の課題」
  として外に置かれている場合（A項目がB項目の説明を引き受けることを
  回避している場合）、そのAとBのペアをピボット項目として明示する。
- 複数のB項目の定量的根拠が共通して省略されており（same_root_group）、
  その省略なしには主張の定量的信頼性が成立しない場合、そのSRGを
  構造の中核として明示する。
ピボット項目のitem_idを「A-n ↔ B-m（ピボット）」の形式で明示すること。"
```

---

## Part B: 解析実行計画

### 完了済み（v15で分析済み）

| 論文ID | タイトル略称 | Stage完了 |
|---|---|---|
| app1 | Pd-catalyzed enantioselective Heck alkenylation (Sigman) | S0〜S2 ✓ |
| app2 | Asymmetric aza-Heck cyclization → quaternary hydantoins | S0〜S2 ✓ |
| comp1 | Narasaka–Heck: iminyl radical / aza-Heck dichotomy (Bower) | S0〜S2 ✓ |
| comp2 | Copper-free HCS mechanism (Palladino/Cabri) | S0〜S2 ✓ |

### 未解析（v16で実行予定）

| 論文ID | PDFファイル名 | 実行順 |
|---|---|---|
| hom1 | hom1_d0sc02246b.pdf | 1番目 |
| hom2 | hom2_reductive-heck.pdf | 2番目 |
| het1 | het1_pd-mof-operando.pdf | 3番目 |
| het2 | het2_deconvoluting.pdf | 4番目 |
| scr1 | scr1_heck-gvl.pdf | 5番目 |
| scr2 | scr2_d5mr00032g.pdf | 6番目 |

### 各論文の出力ファイル命名規則

```
{論文ID}_v16_sonnet_s0.md          ← Stage 0
{論文ID}_v16_sonnet_s1_turn1.md    ← Turn 1 (V1)
{論文ID}_v16_sonnet_s1_turn2.md    ← Turn 2 (V2)
{論文ID}_v16_sonnet_s1_turn3.md    ← Turn 3 (V3)
{論文ID}_v16_sonnet_s1.md          ← Turn 4 (統合)
{論文ID}_v16_sonnet_s2.md          ← Stage 2
```

保存先: `papers/test/{論文ID}/`

---

## Part C: セッション開始手順

1. `/model sonnet` でモデルを確認する（claude-sonnet-4-6 であることを確認）

2. `prompts/v15/` の全ファイルを `prompts/v16/` にコピーする
   ```bash
   cp -r prompts/v15 prompts/v16
   ```

3. `prompts/v16/` の各ファイルに対して、上記 [A-1]〜[A-5] の改訂を施す
   - 改訂は1ファイルずつ順番に行い、各改訂後にファイルを保存・確認する
   - すべての `v15` 文字列を `v16` に更新する（prompt_version行など）
   - 改訂日付を `20260414`（または実行日）に更新する

4. v16プロンプトの改訂が完了したら、hom1から解析を開始する
   - PDFは `/opt/homebrew/bin/pdftotext` で抽出する
   - セッション内でコンテキストを保持したまま S0 → Turn 1 → ... → S2 まで
     一気通貫で実行する（途中でセッションを分割しない）

---

## 参照文書

- **改善提案の詳細**: `improvements/improvement_proposals_batch1.md`
  - 14件の改善提案と4件の観察メモ
  - 各提案に「問題 → 影響ファイル → 提案テキスト」が記載されている
  - Part Aの改訂内容はこれを簡潔に実装したもの

- **UQSプロトコル**: `CLAUDE.md`（実行手順の詳細）

- **完了済み解析の参照**:
  - comp2の Turn 2 は「V2がDFT計算化学を先取りしたため V3 が NMR/分析化学
    を選択した」ケース（IP-T2-01/T3-01 の典型例）
  - comp2の Turn 4 は「拮抗参照文献（Košmrlj 2018）をC項目候補から除外した」
    ケース（IP-T4-01 の典型例）

---

## 注意事項

- v16による解析はhom1から開始し、v15で完了した4報は再分析しない
  （比較一貫性のため v15 分析はそのまま保存する）
- 上記 Part A の改訂テキストは仕様であり、プロンプトへの統合時には
  周囲のテキストとの文体・書式を合わせて調整してよい
- v16改訂後に `improvements/improvement_proposals_batch1.md` の
  "v16実装推奨" 欄に「実装済み ✓」と追記しておく
```
