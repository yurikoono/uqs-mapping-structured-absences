---
title: cross model verification protocol
created: 2026-05-28
status: active
audience: portfolio
open_questions: false
backfilled: true
---

# UQS Cross-Model Verification Protocol（v18.3 で正式化）

**作成日:** 2026-04-27
**位置付け:** UQS Stage 4 充填論文同定の robustness 確保のための運用プロトコル
**根拠:**
- `papers/dev/kumada/cross_model_v182_comparison.md`（n=1）
- `papers/dev/murai/cross_model_v182_comparison.md`（n=2）
- `improvements/cross_model_kumada_vs_murai_meta.md`（メタ観察）

---

## 1. プロトコルの目的

UQS Stage 4 における充填論文同定の **robustness** を、複数モデルの並走と
書誌検証の組合せで確保する。具体的には：

1. **Hallucination の検出と排除**: 単一モデル（特に Sonnet）が paper-dependent に
   発生させる著者組合せ捏造を、cross-model + Crossref API で構造的に検出
2. **Coverage の補完**: Sonnet（review/perspective 寄り）と GPT-5.5（primary
   research 寄り）の補完的カバレッジを活用
3. **Methodological transparency**: cross-model 検証ログを残すことで Phase 2
   advisor pilot の publishability を強化

---

## 2. 適用判断（conditional triggering）

UQS Stage 4 の Bibliographic verification step（v18.3 prompt_stage4_v4.md §B
末尾）の判定ルールに準じ、以下の場合に cross-model verification を **推奨**：

| 状況 | Cross-model verification |
|---|---|
| 論文年代が古い（1980 年以前）| **強く推奨** |
| 著者ネットワークが密（同一研究グループから 10+ 論文）| **強く推奨** |
| 反応名が author name に由来する命名規則を持つ | **強く推奨** |
| Stage 4 で Sonnet Confidence: Medium-Low が 2 件以上 | **推奨** |
| 1990 年代以降の論文 + 著者ネットワーク 5-10 報 | **推奨（オプション）** |
| 全候補が High Bibliographic confidence + 整然とした著者構造 | **省略可** |

---

## 3. プロトコル手順

### Step 1: Sonnet による Stage 4 first pass

CLAUDE.md 標準手順に従い、Claude Code セッションで Sonnet による Stage 4 を
実行：

```
{paper_path} のs4v4を実行
```

出力: `{paper_id}_v18X_sonnet_s4v4.md`（または対応する版番号）

### Step 2: GPT-5.5 (or 同等の web search 対応モデル) による並走実行

別のセッション（ChatGPT, Perplexity, Gemini Deep Research 等）で同じ Stage 4
プロンプトを実行：

- 入力: 論文 PDF + 同じ Stage 4 プロンプト + 同じ Stage 0-3 出力
  （Sonnet のものを参照可）
- 出力: `{paper_id}_v18X_gpt55_s4v4.md`（または該当モデル名）
- 推奨配置: `papers/{path}/gpt55thinking/` 等のサブディレクトリ

### Step 3: 推奨選定リストの差分抽出

両モデルの §C 推奨選定リストを以下の観点で比較：

| 観点 | 動作 |
|---|---|
| **両モデル共通同定** | 論文を「robust 候補」としてマーク。Communication→Full Paper 自動充填等の核心パターンが両モデルで独立同定された場合は特に高信頼度 |
| **Sonnet のみ同定** | 「Sonnet 単独候補」として記録。多くは review / perspective 寄り。hallucination リスクが高い場合は Step 4 で verification |
| **GPT-5.5 のみ同定** | 「GPT-5.5 単独候補」として記録。多くは primary research / modern literature 寄り。Sonnet が cutoff 後文献を見落とした可能性が高い |

### Step 4: Bibliographic verification（Crossref API）

両モデルの推奨選定リストの全エントリ（または [必須] / [推奨] verification の
ものに限定）について、Crossref API で書誌情報を検証：

```bash
# 例: DOI で検索
curl https://api.crossref.org/works/{DOI}

# 例: 書誌情報で検索
curl "https://api.crossref.org/works?query.bibliographic={query}&rows=5"
```

検証項目：

- **論文の実在性**: DOI が有効か、または書誌検索で hit するか
- **著者リストの正確性**: 順序・スペル・著者数が予想と一致するか
- **タイトルの正確性**: 予想されたタイトルと実際のタイトルが一致するか
- **巻号ページの正確性**: 雑誌・巻・号・ページが一致するか
- **出版年の正確性**: 出版年が予想と一致するか

### Step 5: Hallucination 検出と排除

検証結果に基づき以下を実施：

| 検証結果 | 対応 |
|---|---|
| ✅ 完全一致 | エントリを「verified」として final selection に昇格 |
| ⚠️ 部分一致（著者順序の swap、抜け）| エントリを保持しつつ「partial match」として注記、内容確認を要する |
| ⚠️ chemistry 内容の誤記（Murai Chatani 1998 型）| 書誌は正しいが Sonnet/GPT が記述した内容が論文と異なる場合、内容を訂正してエントリを保持 |
| ❌ 完全な捏造（実在しない著者組合せ等）| エントリを排除、再検索（GPT-5.5 web search 等で代替候補を探す）|

### Step 6: 最終 §C 推奨選定リストの確定

verified エントリ + 内容訂正済みエントリで final §C 推奨選定リストを生成。
各エントリに：

- DOI（verification 済み）
- Verification source（Crossref / 別モデル等）
- Final confidence rating
- Cross-model 同定状況（両モデル共通 / 単独）

を付与。

---

## 4. 既知の Hallucination パターン（v18.3 時点）

### 4.1 Sonnet 系列

| パターン | 例 | 検出方法 |
|---|---|---|
| **著者組合せ捏造** | "Tamao-Sumitani-Hayashi-Kumada JACS 1976"（実在せず）| Crossref で検索 hit せず |
| **架空の coauthor 追加** | "Nagase-Hayashi-Kumada Tetrahedron Lett. 1973"（Nagase が実在 corpus にない）| Crossref で検索 hit せず |
| **Chemistry 内容の誤記** | "Chatani 1998 = Rh 触媒" 実際は Ru₃(CO)₁₂ | タイトル確認 |
| **Hedged prediction の評価困難** | "1974 前後 Tetrahedron Lett."（具体性不足）| 検証不可、Confidence: Low として扱う |

### 4.2 GPT-5.4 系列（v17 時代の記録、MEMORY.md 参照）

| パターン | 観察ケース |
|---|---|
| Middle-author 名の捏造 | refs 26/31 middle-author sub |
| Full author-list 置換 | ref 30 |
| 全著者 hallucination（severe）| Yamamoto 1978 triple-mismatch |

### 4.3 GPT-5.5（最新観察、両論文で 0% hallucination）

- 現時点で著者組合せ捏造・chemistry 誤記の発生例なし
- Web search による外部 anchor 機能が paper-specific な脆弱性を排除
- 検証時には DOI が直接付与されるため Crossref 確認が容易

---

## 5. プロトコル運用例（実例ベース）

### 例 1: dev/kumada（古い + 著者ネットワーク密 + named reaction）

トリガー: (a) + (b) + (c) すべて該当 → cross-model verification **必須**

実施結果:
- Sonnet: 7 報予想（5 推奨選定 + 2 body 引用）→ 3 件 verified、2 件
  全 hallucination、2 件 hedged prediction で検証不可
- GPT-5.5: 9 報引用 → 9 件すべて verified
- 両モデル共通同定: 1 報（Tamao 1976 BCSJ Full Paper）— Sonnet 表現は
  hallucination だが概念は正解
- Final selection: GPT-5.5 引用 7 報を中心に、Sonnet の Hayashi-Tajika-
  Tamao-Kumada 1976（verified）を補完追加

### 例 2: dev/murai（新しい + 整然とした著者構造）

トリガー: (c) のみ該当（Murai reaction = named reaction）→ verification **推奨**

実施結果:
- Sonnet: 7 報予想 → 6 件 verified、1 件 部分 hallucination（Chatani 1998
  chemistry 誤記、書誌は正しい）
- GPT-5.5: 8 報引用 → 8 件すべて verified
- 両モデル共通同定: 1 報（Kakiuchi 1995 BCSJ Full Paper、両モデル正確同定）
- Final selection: 両モデル全候補 verified を統合、Chatani 1998 の chemistry
  内容を Sonnet 記述から修正

### 例 3: 仮想例（modern + 整然とした論文）

トリガー: いずれも該当せず → verification **省略可**

想定される運用:
- Sonnet 単独実行で Final selection を確定
- 例外的に重要な論文（Phase 2 pilot 対象等）の場合は recommended として
  実施

---

## 6. プロトコルの limitations

### 6.1 確定的に言えること

- Sonnet の paper-dependent hallucination は 2 例（Kumada, Murai）で確認
- GPT-5.5 の paper-independent な robustness は 2 例で確認（n=2、追加検証推奨）
- Crossref API による書誌検証は automation 可能

### 6.2 まだ検証が不十分なこと

- **Sonnet hallucination の閾値の定量モデル**: paper_age と著者ネットワーク
  密度のどの組合せで hallucination が発生するか未定量
- **GPT-5.5 web search の限界**: 実在しないが web search で hit する論文
  （mis-attribution された web ページ等）への robustness は未検証
- **異分野での再現性**: 物理化学（未公表草稿（他の論文、本研究では使用せず）, NobleGas References）での
  cross-model 適用は user の判断による
- **WoS vs LLM semantic search の体系的比較**: 仮説支持の根拠は得られているが
  定量比較は未実施

### 6.3 v18.3 以降の改善候補

- Stage 4 prompt に **trigger 自動判定ロジック** を組み込み（現状は手動判断）
- Crossref API 呼び出しを Stage 4 出力後の **post-hoc verification step** として
  自動化
- Cross-model verification ログを `papers/{path}/cross_model_log_v18X.md` として
  標準化
- 他モデル（Perplexity Pro, Gemini 3 Deep Research, GPT-5.5 deep research 等）
  での同等 robustness 確認

---

## 7. Phase 2 pilot での扱い

Phase 2 advisor pilot で以下を検討：

1. **Tier 1 advisor への説明**: 本プロトコルを methodological supplement として
   提示、UQS の robustness 主張の根拠資料として活用
2. **Pilot kit に組み込み**: 上記 Step 1-6 を pilot tooling として automation
3. **Pilot 中の data collection**: pilot 参加者の論文で cross-model verification
   を実施し、hallucination 率の paper-dependence パターンを蓄積
4. **Pilot 後の publication**: Phase 2 results paper で cross-model verification
   methodology を独立した contribution として記述

---

## 8. 参照

| ファイル | 内容 |
|---|---|
| `papers/dev/kumada/cross_model_v182_comparison.md` | Kumada cross-model 検証（n=1）|
| `papers/dev/murai/cross_model_v182_comparison.md` | Murai cross-model 検証（n=2）|
| `improvements/cross_model_kumada_vs_murai_meta.md` | 横断メタ観察（paper-dependent パターンの理論化）|
| `improvements/_prompts/v18.3_plan.md` | v18.3 計画書（C17/C18/C18.5/C19 の設計）|
| `improvements/_prompts/changelog_v183.md` | v18.3 確定 changelog（C18 として本プロトコル参照）|
| `prompts/stage2f3/prompt_stage4_v4.md` | Stage 4 v4 プロンプト（C17 conditional triggering）|
| `MEMORY.md` GPT-5.4 author hallucination | 過去の cross-model 観察 |
| `MEMORY.md` EP-10a 開発 | 7 つの独立観察源 |
| `future_work/pilot_evaluation_issues.md` | Phase 2 advisor pilot |

---

## 9. Stage 3 PRI candidate surface cross-model verification（enzyme_pilot pilot 拡張、2026-05-27）

### 9.1 プロトコル拡張の背景

セクション 1-8 で記述した cross-model verification は **Stage 4 充填論文同定の bibliographic robustness** に焦点を当てたものである。2026-05-27 の enzyme_pilot/privett2012 パイロットは、cross-model verification の **第 2 の適用軸**を明らかにした：Stage 3 §6 における **PRI (Persistent Root Issue) 候補の surface robustness** の検証。

### 9.2 enzyme_pilot/privett2012 n=2 cross-paper × n=2 cross-model 検証の結果

**対象論文**: Privett et al. PNAS 109(10):3790-3795 (2012); Röthlisberger et al. Nature 453:190-195 (2008)  
**検証設計**: Röthlisberger 2008 で発散した 2 つの PRI-13 候補が Privett 2012 (n=2 cross-paper) でも両モデルに surface するか

| 4-cell matrix | Röthlisberger 2008 | Privett 2012 |
|---|---|---|
| **Sonnet 4.6** | ✅ PRI-13a 起源 (Convenience-driven endpoint bias) | ❌ Absent (D-2 timing_pressure に間接言及のみ) |
| **Opus 4.7** | ❓ PRI-13b (Design-evolution axis decoupling, n=1 未確認) | ✅ PRI-13a 直接 surface (CLA-1, §6 に登録) |

**判定**: PRI-13a formal promotion **DEFERRED** (2/4 cells 確認、対角パターン)

### 9.3 cross-model surface divergence の構造的解釈

PRI-13a の surface 有無は **モデルの analytical lens** の差異を反映する:

- **Sonnet = technical/mechanistic lens**: D-4 候補が技術的計測欠如として記述される。A-3 deferral は「比較回避メカニズム」として読まれ、反復停止規則の不在は D-4 CLA として昇格しない。
- **Opus = institutional/structural lens**: 論文の narrative structure・前進的棚上げ・出版十分性判断の pattern として読まれる。同じ raw material から「反復停止規則 articulate の不在 = convenience-driven endpoint bias」という構造的 pattern が浮上する。

この lens divergence は Paper A §C13 (cross-model output divergence as evidence for multi-run aggregation protocol の必要性) の empirical case として位置付けられる。

### 9.4 Stage 3 PRI surface cross-model verification のトリガー条件（暫定 v0.1）

| 状況 | 推奨 |
|---|---|
| PRI formal promotion 検討 (n=2 independence test) | **必須** — 両モデルの Stage 3 §6 と D-4 crosswalk を比較 |
| PRI provisional status (n=1) のまま 2 報目解析 | **推奨** |
| PRI surface pattern が論文ジャンルまたはモデル種に依存するか調べたい | **推奨** |
| Stage 2F cross-paper aggregate 解析の前 | **推奨（Stage 2F 前処理として）** |

### 9.5 Stage 3 surface 比較の手順（v0.1）

1. 両モデルの Stage 2 D-4 candidate list を読み、PRI 候補 raw material (timing pressure / stopping rule / deferral items) の対応表を作成
2. 両モデルの Stage 3 §2 SRG/CLA crosswalk を読み、PRI 候補が CLA として独立 surface しているか確認
3. 両モデルの Stage 3 §6 を読み、PRI 候補が正式 PRI 項目として登録されているか確認
4. Decision Table (4 cells: paper × model) を作成し、各 cell の surface strength を (a) explicit label presence / (b) structural homology / (c) anchor items / (d) surface strength の 4 軸で評価
5. 4-cell matrix の充填率で promotion 判定: 全 4 cells ✅ → formal promotion; 2/4 or 3/4 → DEFERRED; 1/4 → n=1 provisional に据え置き

### 9.6 関連ファイル

| ファイル | 内容 |
|---|---|
| `improvements/cross_model_privett2012_comparison_20260527.md` | n=2 cross-paper × n=2 cross-model 比較の詳細 (PRI-13a/b + PRI-14) |
| `improvements/cross_model_privett2012_opus47_pri13_observation_20260527.md` | Opus 4.7 on Privett 2012 の観察（Pending #1 closed 2026-05-27） |
| `papers/enzyme_pilot/privett2012/STATUS.md` | Privett 2012 パイプライン status + cross-model verdict |
| `prompts/stage2f3/prompt_stage3_v4.md` §PRI昇格状態 | PRI-13a observational record 追記提案（user 確認後反映予定） |

---

*本プロトコルは UQS の cross-model verification methodology を v18.3 で正式化
したものである。dev/kumada + dev/murai (n=2) での実証に基づく conditional
triggering 設計を採用し、検証コストを paper-dependent に最適配分する。Phase 2
pilot で publishable な methodology contribution として位置付ける。  
**2026-05-27 拡張 (§9)**: enzyme_pilot/privett2012 パイロットで Stage 3 PRI candidate surface robustness の cross-model verification という第 2 軸が確立された。*
