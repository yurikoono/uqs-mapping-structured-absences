---
title: changelog v182
created: 2026-05-28
status: active
audience: portfolio
open_questions: false
backfilled: true
---

# Changelog: v18.1 → v18.2

**作成日:** 2026-04-26
**作成モデル:** Opus
**性格:** NobleGas References 16 報の v18.1 解析結果に基づく物理化学分野
拡張版。構造的再設計なし。5 件の追記（C12〜C16）のみ。v18.1 基本設計を
完全保持。

---

## 📌 Status (2026-04-26 確定)

v18.2 は **2026-04-26 に確定版として `docs/version_history.md` に登録された**。
確定判断の根拠となった退行確認は未公表の他論文草稿への適用である。（R1 版 2026-10-16: 未公表の他論文草稿に関する記述のため本 deposit から除いた。）

v18.2 は v18.1 確定（2026-04-25）後に NobleGas References cross-paper
analysis の結果を踏まえて策定された minor revision である。
Stage 3 / Stage 4 は v3 のまま変更なし（v18 の C2〜C8 がそのまま継承）。
Stage 0、Stage 1 Turn 2/Turn 3 も v18.1 から内容変更なし（C1 がそのまま継承）。

変更対象ファイル：
- `prompts/v182/prompt_stage1_turn1_v182.md`（C12）
- `prompts/v182/prompt_stage1_turn4_v182.md`（C14 親ルール）
- `prompts/v182/prompt_stage2_v182.md`（C13, C14 follow-up, C15, C16）

### 退行確認結果（2026-04-26 完了）

（R1 版 2026-10-16: 未公表の他論文草稿に関する記述のため本 deposit から除いた。）

---

## 動機：NobleGas References cross-paper analysis の結果

NobleGas References 16 報を v18.1 で解析（regression_log Entry 037〜054）
した結果、物理化学分野固有の構造的パターンが多数検出された。詳細は：

- `papers/NobleGas/analysis_summary_v181_sonnet.md`（n=16 横断分析）
- `improvements/open_issues.md` OI-034〜050（17 件、新規構造的問題）

PRI-12 cluster A の適用率は 16/16 (100%)、特に A5 (Multi-layer
approximation stacking) が 14/16 (87.5%) で出現。物理化学分野での
PRI-12 使用が体系的であることを確認。

新規パターンとして以下が複数論文で独立観察された：

1. **複数測定値報告対称性の体系的不在**（OI-042, 046, 049）— 3 報以上
2. **計算手法の方法論的失敗が診断問いにならない**（OI-039）— 3 報以上
3. **BSSE/不確かさ補正後の最悪シナリオ消失**（OI-035, 036, 044）— 3 報以上
4. **参照クラス定義の単一参照点循環性**（OI-041, 050）— 3 報以上
5. **計算 epistemic marker の事実記述語への後退**（OI-037）— 3 報以上

---

## 変更一覧

### C12: 複数測定値報告対称性チェック追加 — 必須

**対象ファイル:** prompts/v182/prompt_stage1_turn1_v182.md
**コメントタグ:** `<!-- v18.2 C12: multi-measurement reporting symmetry check -->`

**変更内容:**
Turn 1 V1 エージェントの mandatory check リストに追加。論文が複数の
測定値（モード、化学種、サブ系、条件等）を報告する際の対称性を 3 観点で
評価：
- (1) Mode/species reporting symmetry: 一つのモードを根拠として使うなら、
  他のモードも同等に報告されているか
- (2) Sub-system reporting symmetry: 複数サブ系の予測/測定で報告詳細度が
  対称か
- (3) Failure-case reporting symmetry: 成功事例と並んで失敗事例も同等の
  明示性で報告されているか

非対称が発見された場合、severity medium 以上の question candidate として
記録する。

**根拠:**
- arcoco2004（ν(CO) vs ν(CoCO) 選択的前景化）
- ngninn2004（He>Ne 異常の選択的提示）
- zhou1999（バンド強度報告の体系的不在）

**対応 OI:** OI-042, OI-046, OI-049

**期待される効果:** Stage 1 V1 段階で「選択的前景化」パターンが U項目
候補として早期捕捉され、D-4 への昇格可能性が向上。

---

### C13: 補正後最悪シナリオ明示ルール — 必須

**対象ファイル:** prompts/v182/prompt_stage2_v182.md
**コメントタグ:** `<!-- v18.2 C13: worst-case scenario explicit description -->`

**変更内容:**
Stage 2 D-4 候補展開時の追加チェック項目として追加。論文の中核的定量
主張において以下のいずれかが成立する場合、補正後の定性的結論反転
（消滅・順序逆転・分類変更）の最悪シナリオを D-4 候補本文に陽的に
記述する：
- (i) BSSE / ZPE / 相対論補正の typical magnitude が判定マージンと同等
- (ii) 論文が補正前の値で結論を導き、感度分析を実施していない
- (iii) 弱結合系（BE ≤ 10 kcal/mol）で二値判定を行っている

最悪シナリオの記述例も含む（Ne–NiCO の dissociation limit 到達、
Pt-Ng 質量非依存性の anharmonic 順序反転等）。

**根拠:**
- ngnico2004（Ne–NiCO BSSE 補正後消滅シナリオ）
- ngpt2005（PtAr/PtKr/PtXe 質量非依存性振動数）
- arptco2018（計算倍音多成分 vs 実験単一バンド整合性）

**対応 OI:** OI-035, OI-036, OI-044

**期待される効果:** 「反直観的数値」「catastrophic artifact」「量的予測
失敗」パターンが D-4 テキストに陽的に記述され、VQ 判定の透明性が向上。
U項目（self-contradictory absence）と D-4 の連動強化。

---

### C14: 方法論失敗の診断問い D-4 昇格 — 必須

**対象ファイル:**
- prompts/v182/prompt_stage1_turn4_v182.md（A 項目記述ルール、親）
- prompts/v182/prompt_stage2_v182.md（D-4 昇格 follow-up）

**コメントタグ:** `<!-- v18.2 C14: methodological-failure diagnostic ... -->`

**変更内容:**

**Turn 4 側（A 項目分類ルール）:**
A 項目が「論文自身が認めた方法論的失敗」を記録している場合、追加 A 項目
（または密接に link された U 項目）として診断的問いを記録する：「なぜ
この手法はここで失敗するか、その失敗は手法の domain of validity に何を
含意するか」。"diagnostic_question_for: A-N" と注記する。

診断問いは以下を含む：
1. 失敗観察と区別される（独立項目）
2. 原因 attribution を問う（multireference、basis incompleteness 等）
3. Stage 2 D-4 への独立昇格をフラグ化

**Stage 2 側（D-4 昇格義務化）:**
"diagnostic_question_for" 注記付きの A 項目は **必ず独立 D-4 候補として
展開** する。D-4 本文には：
- 失敗した方法の名称
- 失敗のモード（root-tracking、収束、定量誤差）
- 失敗の attribution 候補
- 論文の domain-of-validity 主張への含意

を含める。grounded_in には親 A 項目を必ず含める。

**根拠:**
- koukounas2008（NiF MRCI 失敗 vs CASPT2 成功の比較診断なし）
- gerry2004a（Sternheimer 3 倍誤差の代替機構探索なし）
- ngnico2004（根追跡失敗の手法学的原因分析なし）

**対応 OI:** OI-039

**期待される効果:** 方法論論文（method paper）における失敗の診断問いが
構造的に独立 D-4 候補として現れる。Method paper の核心的主張（domain of
validity）に直結する問いの捕捉率向上。

---

### C15: 参照クラス定義の C→D-4 昇格ルール — 必須

**対象ファイル:** prompts/v182/prompt_stage2_v182.md
**コメントタグ:** `<!-- v18.2 C15: reference-class-definition C→D-4 promotion -->`

**変更内容:**
Stage 2 D-4 候補選択時の追加チェック項目として追加。論文の中心的定量
比較主張が「参照クラス」（典型的 vdW 複合体、弱共有結合類縁体、ベンチ
マーク群等）に依存する場合、以下のいずれかに該当するなら独立 D-4 候補
として記録：
- (i) 参照クラスを構成する文献群のうち、定量比較が単一文献または 2 件
  以下に依存
- (ii) 参照クラスの「代表性」が論文内で議論されていない
- (iii) 参照クラス定義が論文自身の指標を用いて操作的に行われ、参照
  クラス選定と検証指標の循環が生じている

D-4 本文には参照クラス名称・依存文献の特定・代表性問題の記述を含める。
grounded_in に C 項目（引用文献）と関連 D-1 主張項目を含める。

**根拠:**
- gerry2000b（Ar-NaCl 一報のみで「典型的 vdW 複合体」参照クラス定義）
- zhou2001（M⁺-CO GIBMS/PES 実験データ引用のみ、数値比較なし）
- frenking2021（DCD モデル定義の外部基準参照なし）

**対応 OI:** OI-041, OI-050

**期待される効果:** C 項目（引用のみ、数値比較なし）から D-4（独立問い）
への昇格判断が標準化され、「典型」「一般的」主張の根拠薄弱性が体系的に
捕捉される。

---

### C16: 計算 Epistemic Marker 保持ルール — 必須

**対象ファイル:** prompts/v182/prompt_stage2_v182.md
**コメントタグ:** `<!-- v18.2 C16: epistemic marker preservation -->`

**変更内容:**
`confirmed_english_propositional` の制約に追加。論文の主要証拠が計算的・
理論的（DFT, CCSD(T), MP2, CASSCF, MD, AFIR, DFT-IR 等）に由来する場合、
主張動詞は計算手法由来の epistemic marker を保持：
- Good: "DFT calculations predict that ..."
- Good: "CCSD(T) computations indicate that ..."
- Good: "Theory suggests that ..."
- Bad: "X binds Y" / "X forms Y complex" / "X is converted to Y"

論文が計算予測と実験観察の両方を主張する場合は両方を並列保持する。
実験論文はそのまま事実的記述語を使用してよい。

**根拠:**
- ngnico2008（"CCSD(T) predictions" → "Ar-NiCO exists" への縮減）
- ngpt2005（計算予測の事実化傾向）
- arptco2018（「解決宣言」による計算修飾語消失）

**対応 OI:** OI-037

**期待される効果:** 計算化学論文の認識論的降格パターンが言語的に補正
される。Abstract/Title との標識不整合が削減。読者の認識論的解釈の精度
向上。

---

## 変更マッピング（ファイル別）

| ファイル | v18.1 → v18.2 変更 | 備考 |
|---------|--------------------|------|
| prompt_stage0_v182.md | （内容変更なし、版番号のみ）| - |
| prompt_stage1_turn1_v182.md | **C12**（複数測定値報告対称性チェック）| - |
| prompt_stage1_turn2_v182.md | （内容変更なし、版番号のみ）| C1 が v18 から継承 |
| prompt_stage1_turn3_v182.md | （内容変更なし、版番号のみ）| C1 が v18 から継承 |
| **prompt_stage1_turn4_v182.md** | **C14**（方法論失敗の診断問い親ルール）| C11（v18.1）も継承 |
| **prompt_stage2_v182.md** | **C13, C14 follow-up, C15, C16** | C9, C10, C11（v18.1）も継承 |
| prompt_stage2_v182_en.md | （内容変更なし、版番号のみ）| 英語単独版は別途同期検討 |
| prompt_stage3_v3.md | （v18/v18.1 から変更なし）| stage2f3/ で独立版管理、v18/v18.1/v18.2 共有 |
| prompt_stage4_v3.md | （v18/v18.1 から変更なし）| stage2f3/ で独立版管理、v18/v18.1/v18.2 共有 |

---

## v18.1 からの不変部分

以下の v18.1 設計要素は全て v18.2 で完全保持：
- C1〜C8（v18 改訂、Turn 1-3 視点抽象化、PRI-12 二階層、RI-06 注記、
  遡及的検証構造、分割提示構造、EP-08a インセンティブ未充填、
  Success-driven question erasure、自己参照的検証チェック）
- C9〜C11（v18.1 改訂、D-4 候補上限拡張、予測テーブル grounding、
  多重 critical/high U項目独立記録保護）
- v17 から継承された全運用ルール

Stage 3 / Stage 4 の構造（§1〜§6 / §A〜§E）も完全保持。v18.2 の追加は
すべて Stage 1 Turn 1 / Stage 1 Turn 4 / Stage 2 D-4 セクション内の
項目追加のみ。

---

## 退行確認プロトコル（v18.2 開発後に実施）

v18.2 が物理化学分野での改善を提供しつつ、v18/v18.1 の改善を保持する
ことを確認する：

### 1. 未公表草稿への適用（一次目標）

（R1 版 2026-10-16: 未公表の他論文草稿に関する記述のため本 deposit から除いた。）

### 2. devset 退行確認（二次目標）

Kumada または Murai を v18.2 で再実行：
- C12〜C16 の追加が有機合成論文での D-4 構造を歪めていないか
- v17 D4-3（Table I 二層性）等の Kumada 特有パターンが
  影響を受けていないか

### 3. NobleGas References 副次確認（三次目標）

NobleGas References から 1-2 報（gerry2006a または frenking2021）を
v18.2 で再実行し、v18.1 出力との差を確認：
- C12〜C16 が想定通りに発火するか
- 偽陽性（過剰適用）が生じていないか

退行確認結果は `improvements/_prompts/regression_log.md` Entry 055 以降として
記録予定。

---

## 次のアクション（v18.2 確定後）

1. ✅ NobleGas References 16 報の v18.1 解析完了（2026-04-25/26）
2. ✅ Cross-paper aggregation 完了（analysis_summary_v181_sonnet.md）
3. ✅ v18.2 プロンプト実装完了（prompts/v182/）
4. ✅ v18.2 changelog 完了（本ファイル）
5.–7. ✅ 未公表草稿への適用と v18.2 確定判断 （R1 版 2026-10-16: 未公表の他論文草稿に関する記述のため本 deposit から除いた。）
8. ✅ docs/version_history.md に v18.2 確定を反映

### v19 候補課題（保留）

- 未公表草稿への適用から導かれた v19 候補 （R1 版 2026-10-16: 未公表の他論文草稿に関する記述のため本 deposit から除いた。）
- v18.1 から継続: D-4 候補上限の更なる調整、SRG 再編による細粒度候補吸収
  パターン（Entry 036 メタ観察）への対応

### Phase 2 評価パイロット

v18.2 を Phase 2 Tier 1 advisor 評価パイロットの基準版として確定。詳細は
`future_work/pilot_evaluation_issues.md` 参照。

