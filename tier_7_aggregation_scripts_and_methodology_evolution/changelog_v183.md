---
title: changelog v183
created: 2026-05-28
status: active
audience: portfolio
open_questions: false
backfilled: true
---

# Changelog: v18.2 → v18.3

**作成日:** 2026-04-27
**作成モデル:** Opus 4.7
**性格:** Cross-model verification methodology の正式化版。dev/kumada + dev/murai
(n=2) での cross-model verification 実証に基づく構造的改訂。Stage 0-2 は内容
変更なし、Stage 3/4 で 4 件の必須改訂（C17, C18, C18.5, C19）を実装。

---

## 📌 Status (2026-04-27 確定)

v18.3 は v18.2 確定（2026-04-26）後、dev/kumada cross-model 検証（n=1、2026-04-26）
+ dev/murai cross-model 検証（n=2、2026-04-27）の結果に基づき同日策定された。

退行確認・runtime 検証は v18.3 確定の前提とせず（C17/C18.5/C19 の改訂は構造的
追加であり既存機能を破壊しない、C18 は運用プロトコルで prompt 自体への影響なし）、
**implementation 即確定** とする。Phase 2 advisor pilot 開始前の最終 prompt 版
として位置付ける。

実装ファイル：
- `prompts/v183/`（Stage 0-2 内容変更なし、版番号のみ更新）
- `prompts/stage2f3/prompt_stage3_v4.md`（C18.5 + C19）
- `prompts/stage2f3/prompt_stage4_v4.md`（C17）
- `improvements/cross_model_verification_protocol.md`（C18 運用プロトコル）

---

## 動機：n=2 での cross-model verification 結果

### dev/kumada (2026-04-26)

- Sonnet hallucination 率: **2/3 (67%)** 著者組合せ捏造
  - 例: "Tamao-Sumitani-Hayashi-Kumada JACS 1976"（実在せず）
  - 例: "Nagase-Hayashi-Kumada Tetrahedron Lett. 1973"（Nagase が実在 corpus にない）
- GPT-5.5 hallucination 率: **0/9 (0%)** 全 verified

### dev/murai (2026-04-27)

- Sonnet hallucination 率: **0/7 (0%)** 全 + **1/7 (14%)** 部分
  - 部分例: Chatani-Fukuyama 1998 を Rh 触媒と記述（実際は Ru₃(CO)₁₂、書誌は概ね正しい）
- GPT-5.5 hallucination 率: **0/8 (0%)** 一貫

### メタ観察

- **Sonnet hallucination は paper-dependent な structural property**: 論文年代
  + 著者ネットワーク密度 + named reaction の組合せで発生条件が決まる
- **GPT-5.5 web search は paper-independent な robustness**: 両論文で 0%
- **両モデル独立同定の robustness**: Communication→Full Paper 自動充填パターンを
  両論文で両モデル独立同定（n=2 確認）
- **EP-10a の 7 源到達**: Codebook v0.4 への正式昇格条件確実達成

---

## 変更一覧

### C17: Stage 4 §B Bibliographic verification step を conditional triggering で追加 — 必須

**対象ファイル:** `prompts/stage2f3/prompt_stage4_v4.md`
**コメントタグ:** `<!-- v18.3 C17: ... -->`

**変更内容:**

#### (a) §B 各候補テンプレートの拡張

従来の単一 `Confidence` を **2 つに分離**：
- `Bibliographic confidence`: 書誌情報（著者・年・雑誌・巻号ページ）の正確性
- `Filling adequacy confidence`: EP の case-specific 実装を満たすかの判定

加えて **`Verification recommendation`** フィールドを追加（必須 / 推奨 / 省略可）。

#### (b) Conditional triggering 判定ルール

```
[必須] 以下のいずれかに該当：
  (a) 論文年代が古い（1980 年以前）
  (b) 著者ネットワークが密（同一研究グループから 10+ 関連論文）
  (c) 反応名が author name に由来する命名規則
      （Kumada / Heck / Stille / Suzuki / Murai 等）
  (d) Sonnet が Confidence: Medium-Low の予想を含む論文を 2 件以上リスト

[推奨] 単一要因のみ該当
[省略可] いずれにも該当せず + 全候補が High Bibliographic confidence
```

#### (c) §B 末尾に Bibliographic verification sub-step を追加

5 つのチェック項目を含む verification 手順、既知の hallucination パターン
（著者組合せ捏造、架空 coauthor、chemistry 内容誤記）の例示、Crossref API
post-hoc 検証の推奨手順を明記。

#### (d) §C 推奨選定リスト出力形式の拡張

```
| 順序 | 論文 | 充填するEP | VQ水準 | 年代 | Bib.Conf | Fill.Conf | Verification |
```

[必須] verification のエントリは「⚠️ pending verification」と表記、verified
後に通常表記に切り替え。

**根拠:**
- Kumada (n=1, 2026-04-26): Sonnet 67% hallucination
- Murai (n=2, 2026-04-27): Sonnet 0% 全 + 14% 部分
- paper-dependent な hallucination 発生条件の経験的観察

**期待される効果:**
- 検証コストの paper-dependent な最適配分
- Hallucination の構造的検出
- Murai のような modern + 整然論文での冗長検証の回避

---

### C18: Cross-Model Verification Protocol 化 — 必須

**対象ファイル:** `improvements/cross_model_verification_protocol.md`（新規運用文書）

**変更内容:**

UQS Stage 4 充填論文同定の robustness 確保のための運用プロトコルを正式化。
prompt 自体への変更なし、運用文書として独立配置。

**プロトコルの 6 ステップ:**

1. **Sonnet による Stage 4 first pass**: CLAUDE.md 標準手順
2. **GPT-5.5（or 同等の web search 対応モデル）による並走実行**: 別セッション
3. **推奨選定リストの差分抽出**: 両モデル共通同定 / 単独同定の分類
4. **Bibliographic verification（Crossref API）**: DOI で書誌情報確認
5. **Hallucination 検出と排除**: ✅完全一致 / ⚠️部分一致 / ❌完全捏造の分類
6. **最終 §C 推奨選定リストの確定**: verified エントリで final selection

**Conditional triggering** を C17 と同期して適用（既知パターン詳細含む）。

**根拠:** dev/kumada + dev/murai での実証に基づく運用プロトコル。Phase 2
advisor pilot に組み込む可能性が高い。

**期待される効果:**
- UQS Stage 4 の robustness が cross-model + DOI verification で構造的に確保
- Phase 2 pilot の publishable methodology として活用可能
- 運用ログを `papers/{path}/cross_model_log_v18X.md` として標準化可能

---

### C18.5: EP-10a を正式登録（暫定マーカー削除） — 必須

**対象ファイル:** `prompts/stage2f3/prompt_stage3_v4.md`
**コメントタグ:** `<!-- v18.3 C18.5: EP-10a 正式登録 -->`

**変更内容:**

#### (a) EP辞書から「（暫定）」マーカー削除

```
Before: | **EP-10a** | Kinetic verification pack（暫定） |
After:  | **EP-10a** | Kinetic verification pack |
```

#### (b) EP-10a 運用注記を追加

適用条件、充填する RI（複数同時）、PRI-11 との関係、正式登録の根拠を明記。
適用条件として 7 つの動力学的検証手法を列挙：
- Initial-rate kinetics
- Reaction order
- Temperature dependence (ΔH‡, ΔS‡, ΔG‡)
- Isotope effects (KIE)
- Crossover experiments
- Radical-trap controls (TEMPO 等)
- Computational kinetic verification

#### (c) PRI 昇格状態セクションに EP-10a の正式登録を追記

7 つの独立観察源を明示：
1. Sonnet on Breitenfeld 2014 (2026-04-16)
2. Sonnet on Mazet 2021 (2026-04-16)
3. Sonnet on Pengfei/Li 2024 (2026-04-16)
4. GPT-5.4 Thinking on Kumada 1972 (2026-04-19)
5. Claude Opus 4.7 on Kumada 1972 (2026-04-19)
6. GPT-5.5 thinking on Kumada 1972 (2026-04-26)
7. GPT-5.5 thinking on Murai 1993 (2026-04-27)

**根拠:**
- 7 つの独立観察源（cross-model + cross-paper）で確認
- Codebook v0.3 の昇格条件「2 報以上での独立確認」を過剰に達成
- v18.3 で formal codification

**期待される効果:**
- Sonnet が「暫定」マーカーで保守的に未使用だった状況が解消（formal 化により
  両モデルが一貫して EP-10a を使用するはず）
- UQS Codebook が物理化学・有機合成・計算化学を横断する形で進化

---

### C19: VQ 判定の era-norm 標準化（2 段階判定） — 必須

**対象ファイル:** `prompts/stage2f3/prompt_stage3_v4.md`
**コメントタグ:** `<!-- v18.3 C19: VQ judgment 2-step procedure -->`

**変更内容:**

§3 現在の VQ 判定を **2 段階構造** に変更：

#### Step 3a: Modern reassessment baseline

現代の方法論基準（2025 年以降の publication 標準）で全 VQ 要件を評価。
era-norm tolerance を一切適用しない原則的判定。

#### Step 3b: Era-norm annotation での補正

論文の出版年・ジャーナル・形式を考慮し、当時の慣行で許容された欠落を
§4 Era-Norm Annotation で記録（既存 Step 4 で詳細化）。

#### Step 3c: Final VQ judgment（出力形式）

- "VQ-N achieved": Step 3a で達成
- "VQ-N (era-norm qualified)": Step 3a で未達だが era-norm tolerated に該当
- "VQ-N not reached": Step 3a で未達かつ era-norm tolerated に該当しない

加えて "VQ-N (qualified)" は RI-05 等の残存に対して使用継続（era-norm 由来の
qualified とは区別、後者は "(era-norm qualified)" と明記）。

**根拠:**
Sonnet vs GPT-5.5 cross-model 比較（Kumada 1972）で：
- Sonnet: VQ-2 (qualified) — era-norm tolerated 適用
- GPT-5.5: VQ-2 未達 — modern reassessment baseline 適用

の判定差が観察された。2 段階判定により両者の前提が透明化、cross-model
比較が容易になる。

**期待される効果:**
- VQ 通過/未達のラベルが標準化
- Era-norm tolerance の適用範囲が透明化
- Cross-model 間の判定差が予測可能

---

## 変更マッピング（ファイル別）

| ファイル | v18.2 → v18.3 変更 | 備考 |
|---------|--------------------|------|
| `prompts/v183/prompt_stage0_v183.md` | （内容変更なし、版番号のみ）| - |
| `prompts/v183/prompt_stage1_turn1_v183.md` 〜 `turn4` | （内容変更なし、版番号のみ）| C12 (v18.2)、C14 (v18.2)、C11 (v18.1) はそのまま継承 |
| `prompts/v183/prompt_stage2_v183.md` | （内容変更なし、版番号のみ）| C9, C10, C11, C13, C15, C16 (v18.x) はそのまま継承 |
| `prompts/v183/prompt_stage2_v183_en.md` | （内容変更なし、版番号のみ）| - |
| **`prompts/stage2f3/prompt_stage3_v4.md`** | **C18.5 + C19** | EP-10a 正式登録 + VQ 2 段階判定 |
| **`prompts/stage2f3/prompt_stage4_v4.md`** | **C17** | Bibliographic verification (conditional triggering) |
| **`improvements/cross_model_verification_protocol.md`** | **C18 (新規運用文書)** | 6 ステップ運用プロトコル |

---

## v18.2 からの不変部分

以下の v18.2 設計要素は全て v18.3 で完全保持：

- C1〜C16（v17, v18, v18.1, v18.2 の全改訂）
- Stage 0、Stage 1 Turn 1-4、Stage 2 の本文（版番号のみ更新）
- PRI-12 二階層構造（v18 C2）
- D-4 候補数の条件付き拡張（v18.1 C9）
- 予測テーブル独立 grounding チェック（v18.1 C10）
- 多重 critical/high U項目独立記録保護（v18.1 C11）
- 複数測定値報告対称性チェック（v18.2 C12）
- 補正後最悪シナリオ明示（v18.2 C13）
- 方法論失敗の診断問い D-4 昇格（v18.2 C14）
- 参照クラス C→D-4 昇格（v18.2 C15）
- 計算 epistemic marker 保持（v18.2 C16）

Stage 3 / Stage 4 の構造（§1〜§6 / §A〜§E）も完全保持。v18.3 の追加は
Stage 3 §3 + Stage 3 EP辞書 + Stage 4 §B/§C 内の項目追加のみ。

---

## 退行確認の扱い（v18.3 では省略）

v18.3 の改訂は以下の理由で **退行確認を省略して即確定** とする：

1. **C17（conditional triggering）**: 既存出力フォーマットへの追加（破壊的変更なし）
2. **C18（運用文書）**: prompt 自体への影響なし
3. **C18.5（EP-10a 正式登録）**: 暫定マーカー削除のみ、運用注記追加（破壊的変更なし）
4. **C19（VQ 2 段階判定）**: 出力ラベルが追加されるが、既存の "VQ-N (qualified)"
   表記は保持されるため後方互換

検証は **Phase 2 advisor pilot 開始時の preparatory study** として実施可能：
- pilot 対象論文の最初の 1-2 報で v18.3 を実行
- 期待される動作（C17 conditional triggering、C19 2 段階判定、EP-10a 一貫使用）
  が機能するか確認
- 異常があれば v18.3.1 で minor fix

---

## 次のアクション（v18.3 確定後）

1. ✅ v18.3 prompts 実装完了
2. ✅ v18.3 changelog 完了（本ファイル）
3. → `docs/version_history.md` に v18.3 確定を反映
4. → `CLAUDE.md` の short-form recognition pattern を更新（v183, s3v4, s4v4 を
   認識するように）
5. → Phase 2 pilot 開始前の preparatory study で v18.3 動作確認
6. → 必要に応じて 3 例目 cross-model 検証（未公表草稿（他の論文、本研究では使用せず） References から 1 報）

---

## v19 候補課題（保留）

v18.3 では対応しない、将来の v19 候補：

1. **OI-024〜025（Kumada 特有 Table I 二層性、目的論的接続）**: v18.1 で発生、
   open のまま継続
2. **OI-030〜033（v18→v18.1 で発生した SRG 再編による細粒度候補吸収）**: v18.1
   で発生、open のまま継続
3. **OI-053〜055（Kumada / Murai での v182 退行）**: v18.2 で発生、
   open のまま継続（R1 版 2026-10-16: 未公表の他論文草稿に関する記述のため本 deposit から除いた。）
4. **dual-layer VQ explicit output**（future_work §1.8）: v18.3 C19 で部分対応
   したが完全対応は v19 候補
5. **Stage 4 trigger 自動判定ロジック**: 現状は手動判断、自動化は v19 候補
6. **Crossref API 呼び出し自動化**: 現状は手動、tool 化は v19 候補
7. **3 例目以降の cross-model 検証**: 物理化学領域での paper-dependent パターン
   確認（オプション）

---

## 参照

| ファイル | 内容 |
|---|---|
| `improvements/_prompts/v18.3_plan.md` | v18.3 計画書（実装前の設計仕様）|
| `improvements/cross_model_verification_protocol.md` | C18 運用プロトコル |
| `improvements/cross_model_kumada_vs_murai_meta.md` | n=2 メタ観察 |
| `papers/dev/kumada/cross_model_v182_comparison.md` | Kumada cross-model 検証 |
| `papers/dev/murai/cross_model_v182_comparison.md` | Murai cross-model 検証 |
| `improvements/_prompts/changelog_v17.md`〜`changelog_v182.md` | 過去の改訂履歴 |
| `MEMORY.md` GPT-5.4 author hallucination | 過去 cross-model 観察 |
| `MEMORY.md` EP-10a 開発 | 7 つの独立観察源 |
| `future_work/deferred_items_registry.md §1.7` | Codebook v0.4 / EP-10a 形式化 |
| `future_work/pilot_evaluation_issues.md` | Phase 2 advisor pilot |

---

*v18.3 は UQS の cross-model verification methodology を正式化した版である。
dev/kumada + dev/murai (n=2) での実証に基づき conditional triggering 設計を
採用し、検証コストを paper-dependent に最適配分する。EP-10a の 7 源確認に
基づく正式登録、VQ 判定の 2 段階化を含む。Phase 2 advisor pilot 開始前の
最終 prompt 版として位置付けられる。*
