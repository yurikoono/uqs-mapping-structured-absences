---
title: changelog v181
created: 2026-05-28
status: active
audience: portfolio
open_questions: false
backfilled: true
---

# Changelog: v18 → v18.1

**作成日:** 2026-04-25
**作成モデル:** Opus
**性格:** v18 退行確認で検出された OI-024〜029（D-4 候補上限制約による
トレードオフ的退行）への対応。構造的再設計なし。3 件の追記（C9, C10, C11）
のみ。v18 基本設計を完全保持。

---

## 📌 Status (2026-04-25 確定)

v18.1 は **2026-04-25 に確定版として `docs/version_history.md` に登録された**。
退行確認は Entry 031〜035（5論文 v18 vs v18.1）で完了し、メタ観察を Entry 036
として記録。全 5 論文で v181 > v18 の総合判定。OI-024〜029 のうち 3 件解消
（OI-027/028/029）+ 1 件部分対応（OI-026）。新規退行 4 件（OI-030〜033）は
構造的観察として regression_log Entry 036 に記録、v19 候補として継続保留。

v18.1 は v18 確定（2026-04-25）後に同日策定された minor revision である。
Stage 3 / Stage 4 は v3 のまま変更なし（v18 の C2〜C8 がそのまま継承される）。
Stage 0、Stage 1 Turn 1〜3 も v18 から内容変更なし（C1 がそのまま継承される）。

変更対象ファイル：
- `prompts/v181/prompt_stage2_v181.md`（C9, C10）
- `prompts/v181/prompt_stage1_turn4_v181.md`（C11）
- `prompts/v181/prompt_stage2_v181.md`（C11 のフォローアップ）

### 退行確認結果（2026-04-25 完了、5論文）

`improvements/_prompts/regression_log.md` Entry 031〜036 に記録：

| Entry | 論文 | 段階 | 総合判定 | D-4 候補数 |
|-------|------|------|---------|-----------|
| 031 | Kumada (devset) | 1 | v181 > v18 | 6 → 7 |
| 032 | gerrat1968 | 4a | v181 > v18 | 5 → 10（C9 拡張上限）|
| 033 | binkley1979 | 4b | v181 > v18 | 5 → 9（C9 拡張上限）|
| 034 | nakanishi2025 | 2 | v181 > v18 | 8 → 10 |
| 035 | woodward1965 | 3 | v181 > v18 | 6 → 8 |
| 036 | （メタ観察）| — | — | SRG 再編による細粒度候補吸収パターンを記録 |

**結果:** D-4 候補総数 30 → 44（+47%）。OI-027/028/029 完全解消（3 件）+
OI-026 部分対応（1 件）+ OI-024/025（Kumada）継続未解消（2 件）+ 新規退行
OI-030〜033（4 件 medium）。構造的退行ゼロ。

---

## 動機：v18 退行確認で検出された共通パターン

v18 の 5 論文退行確認（regression_log Entry 026〜030）で 6 件の OI（OI-024〜029）
が新規記録された。すべて構造的退行ではなく、以下の共通原因を持つ
「トレードオフ的退行」：

> **D-4 候補上限 8 + 優先度フォールバック規則の副作用** により、
> v18 の核心改善（より重要な候補の昇格）と引き換えに、v17 で独立化
> されていた中位の問いが top-8 に収まらず消失する

| OI | 論文 | severity | 消失したパターン |
|----|------|---------|------------------|
| OI-024 | Kumada | medium | Table I 収率の「方法証明 vs 計画用途」二層性 |
| OI-025 | Kumada | low | 目的論的接続（「何のための手段か」） |
| OI-026 | binkley1979 | medium | HF/MP2 平衡幾何差異と電子相関効果の分離 |
| OI-027 | woodward1965 | medium | 奇電子系・荷電系の独立 MO 解析 |
| OI-028 | nakanishi2025 | medium | 数値指標の閾値信頼性・分子間比較可能性 U項目 |
| OI-029 | gerrat1968 | medium | PHF と状態和法の計算量対比 |

---

## 変更一覧

### C9: D-4 候補数上限の条件付き拡張（Stage 2 v18.1）— 必須

**対象ファイル:** prompts/v181/prompt_stage2_v181.md
**コメントタグ:** `<!-- v18.1 C9: D-4 candidate ceiling conditional expansion -->`

**変更内容:**
v18 までは D-4 候補上限が固定 8 だった。v18.1 では以下の二段階上限を導入：

- **デフォルト上限: 8**（v17/v18 と同じ）
- **拡張上限: 10**（以下のいずれかを満たす場合のみ）：
  - (a) high_convergence_high_gap 項目が 3 件以上
  - (b) critical または high severity の U項目が 2 件以上
  - (c) D-4 候補のうち 6 件以上が独立した SRG/CLA に紐付いている

拡張上限を適用した場合は冒頭に明示的に記載する。拡張上限でも収まらない
場合（>10）は questions_that_cannot_be_asked に格下げするか note 欄での
1文言及に圧縮する。

**根拠:** 
- OI-024（Kumada Table I 二層性）、OI-026（binkley1979 幾何効果分離）、
  OI-029（gerrat1968 計算量対比）はいずれも v17 で独立 D-4 候補だったが、
  v18 で top-8 に収まらず消失した。これらの論文では high_convergence_high_gap
  または high U項目が複数存在し、(a)(b) の条件を満たすため、拡張上限の
  恩恵を受ける。
- OI-025（Kumada 目的論的接続、low severity）も拡張上限で救済される可能性が
  あるが、優先度規則上は依然として下位候補となるため、必ずしも復活しない。

**設計意図:**
- デフォルト上限 8 を維持することで v18 の D-4 構造（最も重要な候補の昇格）
  を保持する
- 拡張条件は「高情報量論文の救済」を目的とし、低情報量論文での候補数
  インフレーションを防ぐ
- 上限 10 は経験的設定であり、将来観察に応じて調整可能

---

### C10: 予測テーブル独立 grounding チェック + 新手法動機付け回避コストチェック（Stage 2 v18.1）— 必須

**対象ファイル:** prompts/v181/prompt_stage2_v181.md
**コメントタグ:** `<!-- v18.1 C10: prediction table grounding check -->`

**変更内容:**
D-4 出発点となる視点リストに 2 項目を追加：

**(C10-a) 予測テーブル独立 grounding チェック:**
論文が複数のサブ系（カチオン/ラジカル/アニオン、複数の置換基、複数の溶媒、
複数の温度条件、複数の幾何構造、複数の電子状態等）の予測を表形式または
リスト形式で提示する場合、以下を確認：
- 各サブ系の予測が論文内で独立に検証されているか
- 予測が単一の原理（電子計数類推、対称性類推、代表系からの外挿）から
  演繹されているのみで、各サブ系固有の根拠が示されていないか

独立検証または固有根拠が欠如している場合、「Table I / 予測テーブルに
対する独立 grounding の不在」を D-4 候補として独立記録する。

**根拠:** OI-027（woodward1965 奇電子系・荷電系の独立 MO 解析不在）。
v17 D-4-6 が「シクロプロピルカチオン・ラジカル・アニオンのMO分解析が
独立に行われていない」を独立 D-4 候補化していたが、v18 では消失した。
n=27 解析サマリーで観察された「電子計数類推による系列予測パターン」
を捕捉する。

**(C10-b) 新手法動機付け回避コストチェック:**
新手法・新指標・新アルゴリズムを提案する論文が、その動機として先行手法
の問題点（計算コスト、スケーリング、精度、実装複雑性等）の回避を明示
している場合、回避された手法のコストと新手法のコストの定量的対比が
論文内に存在するかを確認する。定量的対比なしに「優位性」を主張する
場合、「先行手法回避の動機が定量化されていない」を D-4 候補として
独立記録する。

**根拠:** OI-029（gerrat1968 PHF vs 状態和法の計算量対比未記録）。
v17 D4-4 が独立記録していた「状態和法のN乗スケーリング vs PHF線形
スケーリングの対比未定量化」が v18 で消失した。新手法提案論文の
構造的盲点として一般化。

---

### C11: 多重 critical/high U項目の独立記録保護（Turn 4 + Stage 2 v18.1）— 必須

**対象ファイル:**
- prompts/v181/prompt_stage1_turn4_v181.md（Turn 4 U項目分類ガイダンス）
- prompts/v181/prompt_stage2_v181.md（D-4 探索時の保護フォローアップ）

**コメントタグ:** `<!-- v18.1 C11: multi-critical U-item ... -->`

**変更内容:**

**Turn 4 側（U項目分類ルール）:**
複数の self-contradictory absence または prerequisite-absence パターンが
同一論文に存在する場合、すべての critical または high severity の U項目を
独立して記録する。最も severity の高い U項目が存在しても、他の
high-severity U項目を B 項目に格下げしない。

特に以下の 2 種類の U項目は B 項目への吸収から保護される：

**(C11-a) Threshold reliability（閾値信頼性）:**
数値記述子の二値分類閾値（"X > c → category A"）に対し、論文自身の
データ（境界事例・外れ値・ edge data points）が閾値の判別力を内部矛盾
させている場合。self-contradictory absence の一形態。

**(C11-b) Inter-system / inter-molecular comparability（分子間比較可能性）:**
スカラー量を異なる系（電子数・軌道数・正規化・次元数が異なる）の間で
絶対値として比較するが、その比較の数学的前提（comparability prerequisite）
が論文内で確立されていない場合。prerequisite-absence の一形態。

両者とも明示的な note を付記して U項目として記録する。

**Stage 2 側（D-4 への昇格時の保護）:**
Turn 4 で記録された複数の critical/high U項目が D-4 探索時に B 項目に
吸収されないよう、明示的なフォローアップガイダンスを追加。特に
threshold reliability / comparability prerequisite の 2 種類は独立
D-4 候補として展開することを義務化。

**根拠:** OI-028（nakanishi2025 U-4/U-5 消失）。v17 では U-4（λ_R/λ_F = 1.0
閾値の数値的信頼性）と U-5（λ値の分子間比較可能性）が独立 high U項目として
記録されていたが、v18 で U-1（critical: 生成物分布の検証不在）が確立した
ことで両者が B-5/B-9 に部分吸収された。「より重要な U項目の記録が周辺
U項目の独立記録を阻害する」交互作用パターンへの対応。

---

## 変更マッピング（ファイル別）

| ファイル | v18 → v18.1 変更 | 備考 |
|---------|------------------|------|
| prompt_stage0_v181.md | （内容変更なし、版番号のみ）| - |
| prompt_stage1_turn1_v181.md | （内容変更なし、版番号のみ）| C1 が v18 から継承 |
| prompt_stage1_turn2_v181.md | （内容変更なし、版番号のみ）| C1 が v18 から継承 |
| prompt_stage1_turn3_v181.md | （内容変更なし、版番号のみ）| C1 が v18 から継承 |
| **prompt_stage1_turn4_v181.md** | **C11（U項目分類ルール）** | - |
| **prompt_stage2_v181.md** | **C9, C10, C11（フォローアップ）** | - |
| prompt_stage2_v181_en.md | （内容変更なし、版番号のみ）| 英語単独版は別途同期検討 |
| prompt_stage3_v3.md | （v18 から変更なし）| stage2f3/ で独立版管理、v18 と共有 |
| prompt_stage4_v3.md | （v18 から変更なし）| stage2f3/ で独立版管理、v18 と共有 |

---

## v18 からの不変部分

以下の v18 設計要素は全て v18.1 で完全保持：
- C1〜C8 全て（Turn 1-3 視点抽象化、PRI-12 二階層、RI-06 注記、遡及的検証構造、
  分割提示構造、EP-08a インセンティブ未充填、Success-driven question erasure、
  自己参照的検証チェック）
- v17 から継承された C1〜C8（v17 の旧 C1〜C8、これは v18 と同一）
- rhetorical_function 制約、ピボット構造、SRG、scope anchor rule、
  self-contradictory absence rule、exhaustive extraction rule、
  suppressed classification checklist、anchoring discipline 全て

Stage 3 / Stage 4 の構造（§1〜§6 / §A〜§E）も完全保持。v18.1 の追加は
すべて Stage 1 Turn 4 と Stage 2 D-4 セクション内の項目追加のみ。

---

## 退行確認プロトコル（v18.1 開発後に実施）

v18.1 が v18 の改善を保持しつつ OI-024〜029 を救済することを確認する：

1. **devset 退行確認（Kumada）**:
   - v17 D4-3（Table I 二層性）が D-4 候補として復活するかを確認
   - v17 D4-7（目的論的接続）も拡張上限の恩恵を受けるか観察
   - v18 で正しく昇格した候補（Ni 酸化状態問題、scope_type 修正等）が
     維持されているか確認
2. **C10 動作確認**:
   - woodward1965 で奇電子系・荷電系 grounding 候補が復活するか
   - gerrat1968 で計算量対比候補が復活するか
3. **C11 動作確認**:
   - nakanishi2025 で U-4 (threshold reliability) と U-5 (comparability
     prerequisite) が独立 U項目として記録されるか
   - これらが D-4 候補として独立展開されるか
4. **拡張上限の発動確認**:
   - 拡張上限が適用された論文で冒頭に明示的記載があるか
   - 拡張上限の発動条件 (a)(b)(c) が正しく評価されているか
5. **副作用チェック**:
   - 低情報量論文（拡張上限条件を満たさない）で候補数が不必要に増えて
     いないか
   - C10 のチェックが過剰適用（予測テーブルではない単純な比較表に対しても
     起動）していないか

退行確認の結果は `improvements/_prompts/regression_log.md` に新規エントリ
（Entry 031 以降）として記録する。

---

## 次のアクション（v18.1 確定後）

1. ✅ ~~退行確認プロトコル実行~~ — 2026-04-25 完了（Entry 031〜036）
2. ✅ ~~v18.1 を `docs/version_history.md` に登録~~ — 2026-04-25 完了
3. ✅ ~~open_issues.md ステータス更新~~ — 2026-04-25 完了
   - OI-027: resolved（C10 で解消）
   - OI-028: resolved（C11 で完全解消）
   - OI-029: resolved（C10b で解消）
   - OI-026: partial（v181 D4-3 で部分対応）
   - OI-024, OI-025: open（Kumada 特有のパターン、v19 候補）
4. **v19 候補課題（保留）:**
   - regression_log Entry 036 で記録した 3 件の v19 candidate：
     - (a) v18→v18.1 候補保持チェック（v18 で独立 D-4 候補だった項目が SRG 統合
       候補の note 内に明示記述されているかを確認）
     - (b) U-as-D-4-anchor 保護（単独 U項目の B 項目への格下げ防止）
     - (c) D-4 候補の granularity diff 検出（B-anchor が T2 grounding に後退する
       パターンの自動検出）
   - OI-024（Table I 二層性）、OI-025（目的論的接続）への対応：D-4 出発点視点
     リストに「方法の存在証明 vs 計画用途」「目的論的接続の不在」を明示化する
     候補
   - OI-030〜033（v18→v18.1 で発生した SRG 再編による細粒度候補吸収）への
     構造的対応
5. **Phase 2 評価パイロット:**
   - v18.1 を Phase 2 Tier 1 advisor 評価パイロットの基準版として確定
   - 詳細は `future_work/pilot_evaluation_issues.md` 参照
