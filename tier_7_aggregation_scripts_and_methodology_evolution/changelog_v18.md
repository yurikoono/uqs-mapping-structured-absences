---
title: changelog v18
created: 2026-05-28
status: active
audience: portfolio
open_questions: false
backfilled: true
---

# Changelog: v17 → v18

**作成日:** 2026-04-25
**作成モデル:** Opus
**性格:** 物理化学・基礎理論分野への拡張対応。構造的再設計なし。
全変更が追記・例外追加・カタログ拡張。v17の基本設計を完全保持。

---

## 📌 Status (2026-04-25 確定)

v18 は **2026-04-25 に確定版として `docs/version_history.md` に登録された**。
Nakanishi 2025 引用文献群27報（NRO/NPO・AFIR・反応性指数・IBO・歴史的基礎
理論・量子化学基礎・有機合成）の v17 適用結果を踏まえた物理化学・基礎理論
分野拡張版。動機・所見の詳細は以下を参照：

- `improvements/_meetings/session_handover_v17_to_v18_physchem.md`（n=27の所見と
  v18設計指針）
- `papers/nakanishi/analysis_summary_v17_sonnet.md`（27報の横断分析
  サマリー）

### 退行確認結果（2026-04-25 完了、5論文）

`improvements/_prompts/regression_log.md` Entry 026〜030 に記録：

| Entry | 論文 | 段階 | 総合判定 |
|-------|------|------|---------|
| 026 | Kumada (devset) | 1 | v18 > v17 |
| 027 | binkley1979 | 4b | v17 ≈ v18 |
| 028 | woodward1965 | 3 | v18 > v17 |
| 029 | nakanishi2025 | 2 | v18 > v17 |
| 030 | gerrat1968 | 4a | v18 > v17 |

**結果:** 5論文中4論文で v18 > v17、1論文で実質同等。構造的退行ゼロ。
Stage 4 v3 動作確認では C6・C7・先行充填・分割提示充填・理論的成功による
検証需要消失の各パターンが該当論文で機能。

### 新規 Open Issues（OI-024〜029、6件、すべて medium 以下）

すべて D-4 候補数制限（上限8）と優先度フォールバック規則のトレードオフ
による消失。構造的退行ではなく、次版（v19）での D-4 候補数制限調整または
優先度規則 sub-rule 追加の検討対象。詳細は `improvements/open_issues.md`。

---

## 変更一覧

### C1: S1 Turn 1-3 視点例示の抽象化・汎用化 — 必須

**対象ファイル:** prompt_stage1_turn1_v18.md, prompt_stage1_turn2_v18.md,
prompt_stage1_turn3_v18.md
**コメントタグ:** `<!-- v18 C1: ... -->`

**変更内容:**
有機合成・触媒機構・基質スコープに偏っていた視点例示を、計算化学・
理論化学・物理化学・歴史的理論論文を含む形に抽象化した。具体的には：

- **Turn 1 "Focus on:" リスト**: 情報非対称性の例として synthetic /
  computational / physical chemistry の3カテゴリを並列に提示。各カテゴリで
  典型的なパターンを列挙（GC vs isolated yields、MAE without RMSD、
  signal-to-noise asymmetry等）。"Domain coverage note" を追加し、論文の
  実際の方法論に合わせた質問生成を促す。
- **Turn 1 Dropped Quantitative Benchmark check**: 数値軸の例を 4 つの
  サブフィールド（合成、計算、物理化学、理論基礎）に展開。各サブフィールドの
  典型的な数値量（rate constants / MAE・RMSD / transition frequencies /
  asymptotic limits）を併記。
- **Turn 2 Field differentiation rule**: 例を3つのpaper typeに展開
  （Synthesis paper、Computational methodology paper、Theoretical paper）。
  V1の field とそれに対する V2 の選択可・不可の例を各 type で示す。
- **Turn 2 Absence-based field triggers**: 既存の触媒サイクル・選択性
  triggers に加え、(i) 新理論枠組み・計算手法・記述子に対する独立検証
  欠如時の trigger、(ii) 形式論証から導出された選択則・対称性予測に
  対する falsifiability trigger を追加。
- **Turn 2 DFT reporting checklist**: 6項目を10項目に拡張。追加項目は
  spin contamination ⟨S²⟩、active-space justification（CASSCF/CASPT2/
  MRCI/NEVPT2）、basis-set convergence、numerical convergence
  （forces/Hessian）。"Pd complexes" 限定の文言を一般化。
- **Turn 3 Determination guidance表**: 6行を10行に拡張。追加行は
  multireference electronic structure、construct validity / measurement
  theory（記述子・スコア関数論文向け）、philosophy of science /
  falsifiability analysis（選択則・対称性論文向け）、statistical
  learning / overfitting diagnostics。

**根拠:** Nakanishi 2025引用文献群27報の分析で、有機金属固有の例示が
物理化学・量子化学・歴史的基礎理論論文への適用時にミスマッチを生じる
ことが繰り返し観察された（papers/nakanishi/analysis_summary_v17_sonnet.md
§5.2参照）。

---

### C2: PRI-12 を二階層構造で正式登録 — 必須

**対象ファイル:** prompt_stage3_v3.md（独立版管理、stage2f3/）
**コメントタグ:** `<!-- v18 C2: PRI-12 two-cluster registration -->`

**変更内容:**
v17 PRI 暫定リスト（PRI-10、PRI-11）に **PRI-12: Structural validation
deficiency** を正式昇格として追加。Codebook 表に1行を追加し、本文中に
詳細な二階層定義を登録：

**クラスター A: Self-referential validation（自己参照的検証）**
- サブタイプ A1〜A8（Descriptor-Causality overclaim、Circular validation
  design、Construct-validity circularity、Epistemological closure claim、
  Multi-layer approximation stacking、Parameter portability overclaim、
  Stochastic completeness overclaim、Boundary-adjacent application
  without diagnostic）
- 適用対象：現代の計算化学・物理化学方法論論文

**クラスター B: Deductive-retrospective circularity（演繹的遡及構造）**
- サブタイプ B1〜B6（Composite model import、Retrospective Confirmation
  Bias、Axiomatic framework overclaim、Retroductive-foundation mismatch、
  Definitional closure protection、Algorithm convergence opacity）
- 適用対象：歴史的基礎理論論文、形式的理論提案論文

**適用要件：** クラスター明示、サブタイプID付記、既存RIとの関係を1文、
複合該当時は両記載、新サブタイプ提案は§6で扱う。

**根拠:** Nakanishi 2025引用文献群27報のうち23報（85%）で独立浮上。
昇格基準（独立2報での同型確認）を大幅に超過。

---

### C3: RI-06 判定基準への方法論論文向け注記 — 必須

**対象ファイル:** prompt_stage3_v3.md
**コメントタグ:** `<!-- v18 C3: methodology paper exemption note for RI-06 -->`

**変更内容:**
Codebook 運用注記に「RI-06 判定注記：方法論論文の分野標準慣行」を追加。
RI-06 を適用する条件を以下の両方を満たす場合に限定：
- (a) 参照先の評価指標が対象論文の研究対象と異なる系・条件・モデルに由来
- (b) その移転の妥当性が論文内で議論されていない

単純に「分野標準的な指標を引用した」だけでは RI-06 は適用しない。

**根拠:** maedapccp2013、knizia2013/2015、tsuneda2014で RI-06 が頻出
したが、いずれも「方法論論文として先行手法の評価指標を引用しているだけ」
のケースが含まれており、判定の安定性を損なっていた。

---

### C4: 遡及的検証構造検出フラグ追加 — 必須

**対象ファイル:** prompt_stage3_v3.md
**コメントタグ:** `<!-- v18 C4: Deductive-retrospective structure check -->`

**変更内容:**
Step 2 の §2 SRG/CLA Crosswalk に「Deductive-retrospective structure
チェック（方法論・理論提案論文で実施）」を追加。以下のいずれかが成立
する場合、PRI-12 クラスターB を §2 に記録し、VQ-2 達成を慎重に評価
する（RI-07 または RI-01 の Fatal 判定を検討）：
- (a) 中心主張が演繹的導出で、検証事例が著者選定に限られる
- (b) 反証条件が操作的に未定義で、再分類により反証回避できる構造
- (c) 理論提案先行・実験検証を後続論文に委譲
- (d) 既存事例との一致を「確認」として遡及的に引用

歴史的基礎理論論文（一般に1970年以前）では本パターンが構造的に現れ
やすいため、§4の Era-Norm Annotation で「当時の理論論文の慣行」と
して併記すること。

**根拠:** woodward1965×3、fukui1952、fukui1970、wh1969、mcweeny1960
の 6 報すべてで遡及的検証構造が VQ-1 止まり判定の主因となった。
v17 では明示的な検出フラグがなく、判定の再現性が確保されていなかった。

---

### C5: 分割提示構造（Paper I/II）の判定基準追加 — 必須

**対象ファイル:** prompt_stage3_v3.md
**コメントタグ:** `<!-- v18 C5: split-presentation structure note for RI-09 -->`

**変更内容:**
Codebook 運用注記の RI-09 セクションに「分割提示構造（Paper I/II）」
判定基準を追加：
- (a) Paper II が既刊で参照可能な場合 → 結合してVQ判定
- (b) Paper II が予告のみ・未刊の場合 → Paper I 単独で VQ-2 (Method)
  上限とし、RI-09 を「数値ベンチマーク委譲（split-presentation）」
  として記録

§6 で「VQ非対称性パターン」として記述する。

**根拠:** gerrat1968 と binkley1979 で分割提示構造が独立検出された。
理論的定式化（高VQ要件）を先行提示し、数値実証（低VQ基盤要件）を
後続論文に先送りする VQ階層逆転の変形であり、明示的な判定基準が
必要。

---

### C6: EP-08a「インセンティブ構造的未充填」を第三群典型例として明示 — 推奨

**対象ファイル:** prompt_stage4_v3.md（独立版管理、stage2f3/）
**コメントタグ:** `<!-- v18 C6: EP-08a incentive-structural unfilling pattern -->`

**変更内容:**
Step 1 §A 三群分類に「第三群の典型パターン①『インセンティブ構造的
未充填』」を追加。EP-08a（Replication / uncertainty pack）が方法論論文に
紐付き、対象系での反復測定や統計的有意性評価が独立論文化されていない
場合、または EP-09a で原論文の主張を直接検証する追試が見当たらない
場合、第三群と分類しその旨を明記。

**根拠:** AFIR系3/4、反応性指数系2/2、NRO系1/4で確認された分野横断
未充填パターン。「追試・統計的評価」は計算化学・物理化学分野で独立
論文として評価されにくいため、技術的可能性に関わらず第三群となる
ケースを明示する必要がある。

---

### C7: Success-driven question erasure パターンの明示 — 推奨

**対象ファイル:** prompt_stage4_v3.md
**コメントタグ:** `<!-- v18 C7: Success-driven question erasure pattern -->`

**変更内容:**
Step 1 §A 三群分類に「第三群の典型パターン②『Success-driven question
erasure』」を追加。代替アプローチの成功によって元の問いの検証需要
自体が社会的に消滅するパターン（例：E,E異性体の全合成成功により
Z,Z前駆体からの生合成カスケード仮説の直接検証が長期未充填）を第三群
として記録する。

§E 未充填理由カテゴリにも「成功による問いの抹消」「理論的成功による
検証需要消失」を追加。後者は1960年代基礎理論論文の50〜74年超長期未充填
として観察される。

§D 充填パターン分類にも「先行充填」と「分割提示充填」を追加（v18新規
パターン2件、Doering-Roth 1962、gerrat/binkleyから）。

**根拠:** nicolaoujacs（エンジアンドリック酸全合成）で初検出。
fukui1952 / woodward1965×3 の超長期未充填パターン（50〜74年）の
構造的説明として機能する。

---

### C8: 自己参照的検証デザイン検出フラグ追加 — 推奨

**対象ファイル:** prompt_stage3_v3.md
**コメントタグ:** `<!-- v18 C8: Self-referential validation check -->`

**変更内容:**
Step 2 の §2 SRG/CLA Crosswalk に「Self-referential validation チェック
（全論文で実施）」を追加。以下のいずれかが成立する場合、PRI-12
クラスターA の該当サブタイプ（A1〜A8）を §2 に記録：
- (a) 検証指標と被検証対象が同一の数学的構成物に依存
- (b) 検証成功基準が提案理論の前提と論理的に循環
- (c) 提案された記述子・指標・スコア関数の妥当性が、その記述子自身を
  用いた評価で確立
- (d) 多層近似が累積するが各層の独立検証なし

**根拠:** 第1バッチ12報のうち8報、第3バッチでさらに数報で繰り返し
浮上した自己参照的検証デザインを、VQ判定時に体系的に検出可能にする。
PRI-12 カタログ（C2）と連動して機能する。

---

## 変更マッピング（ファイル別）

| ファイル | 適用された変更 | 備考 |
|---------|-------------|------|
| prompt_stage0_v18.md | （v17から内容変更なし、版番号のみ更新）| - |
| prompt_stage1_turn1_v18.md | C1 | Focus list、Dropped Quantitative Benchmark |
| prompt_stage1_turn2_v18.md | C1 | Field differentiation、Absence-based triggers、DFT checklist |
| prompt_stage1_turn3_v18.md | C1 | Determination guidance表 |
| prompt_stage1_turn4_v18.md | （v17から内容変更なし、版番号のみ更新）| - |
| prompt_stage2_v18.md | （v17から内容変更なし、版番号のみ更新）| PRIカタログはStage 3 |
| prompt_stage2_v18_en.md | （v17から内容変更なし、版番号のみ更新）| - |
| prompt_stage3_v3.md | C2, C3, C4, C5, C8 | stage2f3/ 独立版管理 |
| prompt_stage4_v3.md | C6, C7（+ §D §E 関連追記）| stage2f3/ 独立版管理 |

---

## v17からの不変部分

以下のv17基本設計要素は全てv18で保持：
- rhetorical_function 制約
- ピボット構造探索
- SRG（Same Root Groups）
- scope anchor rule
- self-contradictory absence rule
- exhaustive extraction rule
- suppressed classification checklist
- DFT reporting checklist の元6項目（v18は4項目追加）
- B-item consolidation rule
- cross_field_temperature / TEMPERATURE_SUMMARY
- フォールバック規則
- Anchoring discipline（T1/T2/T3）
- Multi-paper PDF boundary rule
- v17 で追加された C1〜C8 の全運用ルール
  （scope failure verification、ESI delegation、Dropped Quantitative
   Benchmark、sequential protocol confounding等）

Stage 3 / Stage 4 の構造（§1〜§6 / §A〜§E）も完全保持。v18 の追加は
全て既存セクション内の項目追加・サブパターン追加であり、新セクション
の追加なし。

---

## 退行確認プロトコル（v18開発後に実施）

`improvements/_meetings/session_handover_v17_to_v18_physchem.md` 末尾の
「退行確認プロトコル」に従う。4段階：

1. **devset 再実行**（Kumada または Murai を v18 で再実行）
   - D-4 主候補の保持、VQ判定の不変を確認
2. **物理化学論文（現代系）への適用**（nakanishi2025 または ebisawa2022pccp）
   - PRI-12 クラスターA 検出率の維持・向上を確認
3. **歴史的基礎理論論文への適用**（woodward1965_13 または fukui1952）
   - PRI-12 クラスターB（演繹的遡及構造）検出が機能するか
   - C4 が VQ-1 止まり判定を適切に生成するか
4. **分割提示構造論文への適用**（gerrat1968 または binkley1979）
   - C5 が Paper I/II 関係を明示的に記録するか

退行確認の結果は `improvements/_prompts/regression_log.md` に新規エントリ
（Entry 25 以降）として記録する。

---

## 次のアクション（v18 確定後）

1. ✅ ~~退行確認プロトコル実行~~ — 2026-04-25 完了（5論文、Entry 026〜030）
2. ✅ ~~v18 を `docs/version_history.md` に登録~~ — 2026-04-25 完了
3. **v19 候補課題（保留）:**
   - OI-024〜029 の共通原因（D-4 候補上限8 + 優先度フォールバック規則の
     トレードオフ）への対応：候補数制限調整または優先度規則の sub-rule 追加
   - `future_work/deferred_items_registry.md §1.8` の dual-layer VQ explicit
     output（era-norm / modern-era 両方の明示出力）— v18 では未実装、独立
     改訂課題として継続保留
4. **PRI-12 観察追加:**
   - 新サブタイプの候補が検出された場合、Stage 3 v3 §6 で「PRI-12
     cluster_other / subtype: [新規記述]」として記録し、本ファイルに追記
   - クラスターA・B両方に該当する複合パターン事例の追加観察
5. **Phase 2 評価パイロット:**
   - v18 を Phase 2 Tier 1 advisor 評価パイロットの基準版として使用
   - 詳細は `future_work/pilot_evaluation_issues.md` 参照
