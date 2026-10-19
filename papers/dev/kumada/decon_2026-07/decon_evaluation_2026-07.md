---
title: Decontamination Control Experiment — Evaluation
date: 2026-07-20
runs_completed: 5/5
verdict: genuine_extraction
---

# Decontamination Control Experiment — Kumada 1972 / U-1 Genuine Extraction Verification

## 実験設定

- **Base prompts**: `prompts/v184/`（decontaminated copies in `papers/dev/kumada/decon_2026-07/prompts_decon/`）
- **Decontamination対象**: S2 lines 75–81 の Kumada 固有 Good example + T2 lines 103–110 の
  homo-coupling ドメイン seed の 2 箇所
- **Model**: Sonnet 4.6（`claude-sonnet-4-6`、paper A 産出 baseline と同一）
- **N runs**: 5（並列独立実行、各 run に独立 agent）
- **Paper**: kumada1972（Kumada et al., J. Am. Chem. Soc. 1972, JACS — 最初の Ni-phosphine
  クロスカップリング報告、Paper A の main showcase）
- **実験動機**: Paper A post-submission audit において v18.4 プロンプトに Kumada 固有コンテンツが
  2 箇所発見された。Paper A が「新たに発見した」とする U-1（homo-coupling の自己矛盾的不在）が
  genuine paper-level extraction であるか、prompt recall であるかを判定する必要があった。

---

## Decontaminated 箇所

### Stage 2 変更（lines 75–81）

`prompts/v184/prompt_stage2_v184.md` の E-proposition 形成ガイダンスから Kumada 固有の
"Good example" を hydroformylation 例に置換した。

**置換前（汚染あり）**:
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

**汚染の性質**: 汚染版の Good example が kumada1972 の E-proposition と verbatim 一致しており、
プロンプトが E-proposition の文字列を直接 seed していた。

---

### Stage 1 Turn 2 変更（lines 103–110）

`prompts/v184/prompt_stage1_turn2_v184.md` の V2 Primary selectivity トリガーから
cross-coupling vs. homo-coupling の例示を別ドメイン（hydroformylation 位置選択性）に置換した。

**置換前（汚染あり）**:
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

**汚染の性質**: 汚染版の Primary selectivity 例示が「Cross-coupling vs. homo-coupling」を
直接記載しており、U-1 の topical domain（homo-coupling の不在）を V2 の質問生成に seed していた。

---

## U-1 出現率

| Run | U-1 present | U-1 text（要約） | B (homo-coupling) | E-proposition |
|-----|:-----------:|-----------------|:-----------------:|---------------|
| 1 | **Yes** | eq.3 の L₂NiR₂ + R'X'' → L₂Ni(R')(X'') + R–R が R–R を stoichiometric に予測するが、Table I に R–R の収率・検出データなし。selectivity claim を analytically 評価不能。severity: critical | Yes | Nickel-phosphine complexes catalyze selective cross-coupling of Grignard reagents with vinyl or aryl halides. |
| 2 | **Yes** | eq.3 の diorganonickel 中間体から R–R が stoichiometric に生成すると機構が予測するが、Table I にもどのエントリーにも R–R データなし。抑制理由の議論なし。 | Yes | Nickel-phosphine complexes catalyze selective cross-coupling of Grignard reagents with vinyl or aryl halides. |
| 3 | **Yes** | 触媒条件で R–R が形成するか、また何 % か。eq.3 が R–R を explicit stoichiometric co-product として予測するが、Table I にも実験例にも homo-coupling yield データなし。note: self-contradictory absence。 | Yes | Nickel-phosphine complexes catalyze cross-coupling of Grignard reagents with vinyl or aryl halides. |
| 4 | **Yes** | eq.3 で R–R が同ステップで selectivity-determining byproduct として予測されるが、Table I に R–R 測定値なし。cross:homo-coupling 比も議論されない。severity: critical | Yes | Nickel-phosphine complexes catalyze selective cross-coupling of Grignard reagents with vinyl or aryl halides. |
| 5 | **Yes** | 触媒サイクル eq.3 が R–R homo-coupling product を触媒活性化ステップで明示予測しているが、報告された条件下で significant に形成しない理由を論文が説明していない。 | Yes | Nickel-phosphine complexes catalyze selective cross-coupling of Grignard reagents with vinyl or aryl halides. |
| **計** | **5/5** | | **5/5** | |

**備考**:
- Run 3 の E-proposition は "selective" が脱落しているが、framing（Ni-phosphine + cross-coupling +
  Grignard + vinyl or aryl halides）は完全に収束している。"selective" の脱落は stochastic な
  表現のゆれであり、汚染の除去によって E-proposition が変化したとは判断できない。
- 全 5 run で B (homo-coupling data absent) = Yes、U-1 と B の同時出現率 = 5/5。

---

## 原論文 v18.4 との比較

### E-proposition 収束

| 版 | E-proposition |
|----|---------------|
| v18.4 original (`kumada_v184_sonnet_s2.md` line 259) | "Nickel-phosphine complexes catalyze selective cross-coupling of Grignard reagents with vinyl or aryl halides." |
| decon Run 1 | "Nickel-phosphine complexes catalyze selective cross-coupling of Grignard reagents with vinyl or aryl halides." |
| decon Run 2 | "Nickel-phosphine complexes catalyze selective cross-coupling of Grignard reagents with vinyl or aryl halides." |
| decon Run 3 | "Nickel-phosphine complexes catalyze cross-coupling of Grignard reagents with vinyl or aryl halides." |
| decon Run 4 | "Nickel-phosphine complexes catalyze selective cross-coupling of Grignard reagents with vinyl or aryl halides." |
| decon Run 5 | "Nickel-phosphine complexes catalyze selective cross-coupling of Grignard reagents with vinyl or aryl halides." |

**結論**: E-proposition は 5/5 run で v18.4 original と実質 identical に収束した（Run 3 は
"selective" 脱落のみ）。Good example を hydroformylation に置換した後も E-proposition 生成が
kumada1972 の実際の BIB/S0 記述（"[REDACTED: verbatim source text; see the source paper via its DOI]"）から誘導されていることが確認された。
すなわち、S2 プロンプトの Good example は E-proposition を決定していなかった。

### U-1 テキストの質的比較

| 版 | U-1 の根拠テキスト |
|----|--------------------|
| v18.4 original (s1.md line 73) | "The proposed catalytic cycle explicitly shows homo-coupling product R–R as a stoichiometric byproduct of the key step converting intermediate 1 to intermediate 2. Yet no homo-coupling product ... is reported, quantified, or acknowledged as undetectable in Table I or in the experimental procedures." |
| decon 版（5/5 run で同構造） | eq.3 による R–R の stoichiometric 予測、Table I での未報告、自己矛盾的不在（self-contradictory absence）。根拠・構造・severity 評価いずれも一致。 |

decon 版 U-1 の根拠は v18.4 original と mechanistic argument の構造（eq.3 の R–R 予測 →
データ欠如 → 自己矛盾）において identical であり、どの run も同じ eq.3 の文字列
"L₂NiR₂ + R'X'' → L₂Ni(R')(X'') + R–R" を論文から直接引用している。

---

## 判定

**U-1 出現率**: 5/5（100%）

**E-proposition 収束**: 完全収束（5/5 run、Run 3 は "selective" 1 語の stochastic 脱落のみ）

**B (homo-coupling data absent) 出現率**: 5/5

**最終判定**: **genuine_extraction**

### 根拠

1. **汚染除去後も U-1 が 5/5 で出現した**。decontaminated プロンプトは kumada1972 の
   homo-coupling ドメインを seed する記述をいずれも含まない（T2 例示は hydroformylation 位置選択性、
   S2 Good example は Rh-catalyzed hydroformylation）。にもかかわらず、全 run が独立に eq.3 の
   R–R 予測と Table I の不在を検出し、U-1 として記録した。

2. **E-proposition が論文テキストから誘導されていることが確認された**。S2 汚染版の Good example
   verbatim text を除去した後も E-proposition 生成は変わらず、プロンプトではなく kumada1972 の
   BIB-1 表題・S0-1 core_claim が E-proposition を決定していたことが実証された。

3. **U-1 の mechanistic argument が 5 run 間で独立収束した**。各 run の U-1 テキストは文体・
   詳細度は異なるが、eq.3 テキストの直接引用 → byproduct の未報告 → 選択性主張との自己矛盾という
   3 段構造を共通して有しており、論文テキスト自体から駆動された extraction であることを示す。

4. **判定基準の適用**: 実験設計の判定基準（≥3/5 で genuine extraction）に対して 5/5 が達成された。
   最高スコアでの genuine extraction 判定。

### Paper A への含意

U-1 は genuine extraction であり、Paper A の demonstration としての記述は存続可能。
ただし、v18.4 プロンプトに Kumada 固有コンテンツが存在していたという事実は透明性の観点から
Methods への開示注記追加が推奨される。

---

## Paper A revision への推奨テキスト

### Methods 追加節（開示注記）

以下の文言（英語）を Methods の "Prompt construction" または "Experimental controls" 節に追加することを推奨する。適切な節が存在しない場合は新規 paragraph として Methods 末尾に付加する。

---

**推奨テキスト（英語 draft）**:

> **Post-submission contamination audit and decontamination control.**
> Following submission, we identified two locations in the v18.4 Stage 2 and Stage 1 Turn 2
> prompts where the Kumada 1972 paper — the primary showcase in this study — was referenced
> as an illustrative example: (i) the Stage 2 E-proposition formation guide included the
> Kumada 1972 E-proposition verbatim as a "Good example"; (ii) the Stage 1 Turn 2 selectivity
> trigger included "cross-coupling vs. homo-coupling" as an explicit example of primary
> selectivity questions, seeding the topical domain of U-1.
>
> To determine whether U-1 (the self-contradictory absence of homo-coupling data) was a
> genuine extraction from the paper or an artefact of prompt recall, we conducted a
> decontamination control experiment. We replaced both contaminated passages with
> domain-neutral examples from unrelated chemistry (Rh-catalyzed hydroformylation) and
> re-ran the full UQS v18.4 pipeline on Kumada 1972 under N = 5 independent parallel runs
> (Sonnet 4.6, same model as the original analysis). U-1 was reproduced in all 5/5 runs,
> with the mechanistic argument — eq. 3 explicitly predicts R–R as a stoichiometric byproduct,
> yet no homo-coupling data appear in Table I — independently reconstructed in each run.
> The E-proposition converged to the original text in 4/5 runs and was substantively
> equivalent in the fifth. We therefore conclude that U-1 is a genuine paper-level extraction
> grounded in the catalytic cycle equation of the original paper, not a consequence of
> prompt contamination. Raw outputs from all 5 decontaminated runs are archived at
> `papers/dev/kumada/decon_2026-07/`.

---

**日本語版（Paper A JA track 用）**:

> **提出後の汚染監査と除汚染対照実験**。提出後の監査において、v18.4 プロンプトの 2 箇所に
> 本研究の主要 showcase である kumada1972 に固有のコンテンツが含まれていることが判明した：
> （i）Stage 2 の E-proposition 形成ガイドに kumada1972 の E-proposition が verbatim 収録されており、
> （ii）Stage 1 Turn 2 の選択性トリガーに「クロスカップリング対ホモカップリング」が直接例示されていた。
> これにより、U-1（ホモカップリングの自己矛盾的不在）が論文から genuine に抽出されたものか、
> prompt recall を反映したものかを検証する必要が生じた。
>
> 対照実験として、上記の 2 箇所を無関係の化学反応（Rh 触媒ヒドロホルミル化）の例示に置換した
> decontaminated プロンプトを用い、kumada1972 に対して N=5 の独立並列 run を実行した（モデル:
> Sonnet 4.6、オリジナル解析と同一）。U-1 は全 5 run で再現され、触媒サイクル eq.3 が R–R を
> stoichiometric に予測しながら Table I にホモカップリングデータが存在しないという mechanistic
> argument が各 run で独立に構築された。E-proposition は 4/5 run でオリジナルと verbatim 一致し、
> 残り 1 run でも実質的に同等であった。したがって U-1 は prompt 汚染の産物ではなく、論文の触媒サイクル
> 式から駆動された genuine な paper-level extraction であると結論する。

---

### 推奨しない代替（showcase 差し替え）

genuine_extraction が確認されたため、showcase を Heck テストセット論文に差し替える対応は
不要である。U-1 は Paper A のデモンストレーション例として引き続き有効。

---

## ファイル一覧

| Run | 出力ファイル |
|-----|------------|
| Run 1 | `run1/kumada_v184decon_sonnet46_s0.md` `s1_turn1.md` `s1_turn2.md` `s1_turn3.md` `s1_turn4.md` `s1.md` `s2.md` |
| Run 2 | `run2/kumada_v184decon_sonnet46_s0.md` `s1_turn1.md` `s1_turn2.md` `s1_turn3.md` `s1_turn4.md` `s1.md` `s2.md` |
| Run 3 | `run3/kumada_v184decon_sonnet46_s0.md` `s1_turn1.md` `s1_turn2.md` `s1_turn3.md` `s1_turn4.md` `s1.md` `s2.md` |
| Run 4 | `run4/kumada_v184decon_sonnet46_s0.md` `s1_turn1.md` `s1_turn2.md` `s1_turn3.md` `s1_turn4.md` `s1.md` `s2.md` |
| Run 5 | `run5/kumada_v184decon_sonnet46_s0.md` `s1_turn1.md` `s1_turn2.md` `s1_turn3.md` `s1_turn4.md` `s1.md` `s2.md` |
| 評価文書 | `decon_evaluation_2026-07.md`（本文書） |
| 実験設計 | `session_prompt_decon_experiment.md` |
| Decon prompts | `prompts_decon/`（6 files、v18.4 original の S2 + T2 を decon 置換） |
