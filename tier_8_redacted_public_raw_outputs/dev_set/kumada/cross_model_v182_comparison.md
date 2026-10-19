# Sonnet vs GPT-5.5 — Kumada 1972 v18.2 Cross-Model 比較・検証レポート

**作成日:** 2026-04-27
**作成モデル:** Opus 4.7（横断比較・検証実施）
**対象論文:** Tamao, Sumitani, Kumada (1972) JACS 94(12), 4374-4376 — devset Kumada
**プロンプト:** v18.2 (S0–S2) + v3 (S3–S4)
**比較対象モデル:** Claude Sonnet 4.6 / OpenAI GPT-5.5 thinking
**関連:** regression_log.md Entry 052 (Sonnet 自動比較), changelog_v182.md, MEMORY.md (GPT-5.4 author hallucination 記録)

---

## 1. 動機と位置付け

UQS は v17 確定（提出版）以降、Sonnet を公式 baseline として運用してきた（CLAUDE.md「分析は常に Sonnet で実行」）。2026-04-27 にユーザーが GPT-5.5（OpenAI 最上位 thinking モデル）リリース後に独立に同じ v18.2 プロンプトで Kumada 1972 を解析したことで、cross-model 比較の機会が得られた。

本検証は **3 つの方法論的問い** に答える：

1. **モデル portability**: 同じ v18.2 プロンプトが異なるベンダー・異なるティアのモデルで等価な解析品質を出力するか
2. **Web search の補完価値**: GPT-5.5 の web search 機能が Stage 4 充填論文同定で価値を生むか
3. **Web of Science vs LLM semantic search**: ユーザーの過去観察「WoS 構造化検索では真に適切な充填論文が見つからない」を empirical に検証

これらは UQS Stage 4 の core capability（充填論文同定）の方法論的位置付けに直結する問いである。

---

## 2. 比較設計

### 2.1 モデル仕様

| 項目 | Sonnet 4.6 | GPT-5.5 thinking |
|---|---|---|
| ベンダー | Anthropic | OpenAI |
| ティア | 中位（Opus 4.7 が上位）| 最上位 |
| Web search | なし（内部知識のみ）| あり（ChatGPT 経由） |
| 出力形式 | 9 ファイル分割（CLAUDE.md 規格）| 単一 export ファイル |
| 解析日 | 2026-04-26 | 2026-04-26 |

**重要な前提**: 出力形式の差はユーザーが Web Interface で実行後にファイル分割を省略した手作業の問題であり、**モデル能力の評価には含めない**。

### 2.2 入力統一

- 同一 PDF (`Kumada_1972.pdf`)
- 同一 v18.2 プロンプト群 (`prompts/v182/` および `prompts/stage2f3/prompt_stage{3,4}_v3.md`)
- 同一 Stage 順序 (S0 → Turn 1 → Turn 2 → Turn 3 → Turn 4 → S2 → S3v3 → S4v3)

### 2.3 評価軸

1. **量的比較**: A/B/C/U 項目数、SRG 数、D-4 候補数、EP 三群分類、推奨選定リスト
2. **v18.2 改訂発火状況**: C12-C16 の発火確認
3. **質的差異**: 観察精度、推論深度、外部知識活用、フォーマット遵守
4. **VQ 判定**: era-norm tolerated vs modern reassessment
5. **充填論文の実在性検証**: Crossref API による DOI 確認
6. **充填論文の充填妥当性**: タイトル・著者・出版年から Kumada 1972 EP 充填の意味論的妥当性評価

---

## 3. 量的比較サマリー

| 項目 | Sonnet | GPT-5.5 | 観察 |
|---|---|---|---|
| **A 項目** | 4 | 2-3 | Sonnet は deferred を厳密に |
| **B 項目** | 10 | 14 | GPT-5.5 が細粒度（+40%）|
| **C 項目** | 3 | 3 | 同等 |
| **U 項目** | 1 | 7 | GPT-5.5 が分散的（+600%）、複数 critical 含む |
| **CLA 項目** | 2 | 2 | 同等 |
| **SRG 数** | 5 | 7 | GPT-5.5 が +2 |
| **D-4 候補数** | 6 | 5-6 | 同等範囲（C9 拡張上限内）|
| **EP 第二群** | 3 | 4（+EP-10a）| GPT-5.5 が新規カテゴリ導入 |
| **推奨選定論文** | 5 | 7 | GPT-5.5 が modern reach |
| **VQ 判定** | VQ-2 (qualified) | VQ-1 qualified, VQ-2 未達 | **判定哲学が異なる** |

---

## 4. v18.2 改訂 (C12-C16) 発火状況

| 改訂 | Sonnet | GPT-5.5 | 備考 |
|---|---|---|---|
| **C12** 報告対称性 | △ 部分 | ✅ 明確（V1-Q13/14）| GPT-5.5 が改訂指示に明示的従順 |
| **C13** 最悪シナリオ | ✅ 実装 | △ 暗黙的 | Sonnet が explicit marker 使用 |
| **C14** 診断問い | △ 弱い | ✅ 強い（CLA, U-4 prerequisite-absence）| GPT-5.5 が構造化 |
| **C15** 参照クラス | ✅ 実装 | △ 間接的 | Sonnet が D-4-5 で循環性明示 |
| **C16** epistemic marker | ❌→該当外 | ❌→該当外 | **Kumada は実験論文なので C16 は本来不発火が正解**（C16 は計算論文向け）|

**評価**: 5 件中 4 件で実質互角（C12/C13/C14/C15 で 2 勝 2 敗）。**得意領域が補完的に分布**。

---

## 5. 充填論文の実在性 + 充填妥当性検証（核心結果）

### 5.1 GPT-5.5 引用論文（9 報すべて検証成功、hallucination 0%）

| # | GPT-5.5 引用 | DOI 確認 | 充填妥当性 |
|---|---|---|---|
| 1 | Tamao-Kiso-Sumitani-Kumada (1972) JACS 94(26), 9268 "Alkyl group isomerization..." | ✅ 10.1021/ja00781a070 | ★★★ EP-07a (secondary alkyl scope) + 暗黙の β-H 消去機構充填（OI-001 直接対応） |
| 2 | Tamao-Zembayashi-Kiso-Kumada (1973) J. Organomet. Chem. 55(2), C91 "Stereochemistry..." | ✅ 10.1016/s0022-328x(00)82058-6 | ★★★ EP-04a 直接充填（cis/trans dichloroethylene 立体化学を主題化）|
| 3 | Kiso-Tamao-Kumada (1973) J. Organomet. Chem. 50(1), C12 "Effects of halides..." | ✅ 10.1016/s0022-328x(00)95063-0 | ★★ EP-07a + EP-04a partial |
| 4 | Tamao + 8 others (1976) BCSJ 49(7), 1958 "General Scope and Limitations" | ✅ 10.1246/bcsj.49.1958 | ★★★ **正統な Full Paper**（"I." = 第一報）、EP-01a/02a/05a/07a を bundle 充填 |
| 5 | Tamao-Kodama-Nakajima-Kumada-Minato-Suzuki (1982) Tetrahedron 38(22), 3347 "...Coupling—II" | ✅ 10.1016/0040-4020(82)80117-8 | ★★ EP-07a/02a 拡張 |
| 6 | Bumagin-Beletskaya (1990) Russ. Chem. Rev. 59(12), 1174 "Key steps..." | ✅ 10.1070/RC1990v059n12ABEH003585 | ★ レビューだが EP-06a 間接 |
| 7 | Breitenfeld-Wodrich-Hu (2014) Organometallics 33(20), 5708 "Bimetallic Oxidative Addition..." | ✅ 10.1021/om500506y | ★★★ Modern Ni-Kumada mechanism、EP-03a/EP-10a 充填（MEMORY.md EP-10a 開発の根拠論文）|
| 8 (§B) | Kumada-Tamao-Sumitani (2003) Org. Synth. "1,2-Dibutylbenzene" | ✅ 10.1002/0471264180.os058.22 | ★★ EP-08a procedure 寄り |
| 9 (§B) | Tamao (2002) J. Organomet. Chem. 653(1-2), 23 "Discovery..." | ✅ 10.1016/S0022-328X(02)01159-2 | ★ 著者回顧、EP-09a 間接 |

**Hallucination 率: 0/9 (0%)**。全引用が DOI で verifiable な実在論文。GPT-5.4 で記録された author hallucination パターン（MEMORY.md）は GPT-5.5 + web search で完全に解消。

### 5.2 Sonnet 予想論文の検証（67% hallucination）

| Sonnet 予想 | 検証結果 | 備考 |
|---|---|---|
| Tamao-Sumitani-**Hayashi**-Kumada (1976) JACS（Kumada Full Paper）| ❌ **存在しない** | 著者組合せ捏造：実在する 2 論文（Tamao-Sumitani-**Kiso**-Kumada BCSJ + Hayashi-**Tajika**-Tamao-Kumada JACS）を混合 |
| Hayashi-Tajika-Tamao-Kumada (1976) JACS 98(12), 3718 | ✅ 実在（DOI: 10.1021/ja00428a061）| Sonnet が正しく同定した唯一の確証付き論文 |
| **Nagase**-Hayashi-Kumada (1973-74) Tetrahedron Lett. | ❌ **存在しない** | Nagase は該当 corpus に含まれず |
| Hayashi-Kumada (1974 前後) Tetrahedron Lett. | △ 検証不可 | "1974 前後" の hedged prediction で個別検証不能 |
| Kumada (1980) Pure Appl. Chem. レビュー | △ 検証不可 | "または関連レビュー" の generic prediction |
| Corriu et al. (1974-1977) J. Organomet. Chem. | △ 検証不可 | 年範囲・タイトル指定なし |

**確証可能な予想 3 件中 2 件が著者組合せ捏造（67%）**。Sonnet も Confidence: Medium-Low と self-aware で報告していたが、結果として **書誌レベルでの信頼性が limited**。

### 5.3 user の Web of Science 仮説の検証

ユーザーの過去観察（本セッション中に共有）：
> 「以前に Web of Science の検索オプションを構成して検索してもらいましたが、真に適切な充填論文はその方法では見つかりませんでした。」

GPT-5.5 が見つけた「正解」論文の特性を分析：

| 論文 | WoS keyword 検索で見つかりにくい理由 |
|---|---|
| **BCSJ 1976 General Scope and Limitations** | タイトルに "Kumada" や "cross-coupling" のキーワードがない。"General Scope" は無数の論文タイトルに現れる |
| **JACS 1972 Alkyl group isomerization** | タイトルが「アルキル基異性化」を主題化、Kumada 1972 の deferred 問題（OI-001 β-H 消去）を充填する **意味論的繋がり** の理解が必要 |
| **Organometallics 2014 Bimetallic Oxidative Addition** | 現代用語（"Bimetallic OA", "Nickamine"）で記述されており、Kumada 1972 のキーワード共起では出てこない |

**仮説支持の理由**: 検索パラダイムの差。

| 検索方式 | 動作原理 | UQS Stage 4 適合性 |
|---|---|---|
| WoS 構造化検索 | キーワード共起 + ブール演算 | **構造的に不適**（意味論的繋がりを判別不能）|
| LLM web search | 意味論的クエリ + 関連性スコア | **構造的に適合**（「EP の case-specific 実装を満たす論文」という抽象クエリの解釈可能）|

UQS Stage 4 §B の指示「論文の表面的主題ではなく、EP の case-specific 実装との対応関係で充填を判定（証拠的相補性の検出）」は本質的に semantic search タスク。よって **WoS は構造的に不適、LLM web search は構造的に適合** という結論が得られる。

---

## 6. 質的差異の詳細

### 6.1 観察精度（同等）

両モデルとも論文テキストの引用・数値（"10⁻²–10⁻³"、"cis:trans = 80:20"、"76–98%"）を正確に記録。BIB 情報も同等の精度。観察精度に差はない。

### 6.2 推論深度（補完的）

- **Sonnet**: SRG レベルでの集約（10 B 項目を 5 SRG にまとめる）、構造化された読み
- **GPT-5.5**: U 項目レベルでの分散（U-1〜U-7 を個別記録）、exhaustive な列挙

両者は **同じ問題を異なる粒度で記録**。どちらが優れているかは UQS の意図に依存。Sonnet は priority structure の明示に向き、GPT-5.5 は隠れた問いの発見に向く。

### 6.3 EP-10a 創発的導入（GPT-5.5 のみ）

GPT-5.5 が v18.2 プロンプトに **明記されていない EP-10a「Kinetic verification pack」を Stage 4 で導入**。これは MEMORY.md の「EP-10a 開発（Kumada 1972 EP dictionary 追加、2026-04-19）」の 5 つの独立な源（Sonnet on Breitenfeld 2014、Mazet 2021、Pengfei 2024、GPT-5.4 thinking on Kumada、Opus 4.7 on Kumada）に **GPT-5.5 が独立に追加された 6 つ目の源** となる。

→ **EP-10a の robustness を強く示唆**。Codebook v0.4 への正式昇格条件が更に強化された。

### 6.4 VQ 判定の哲学的差異

| モデル | 判定 | 適用基準 |
|---|---|---|
| Sonnet | VQ-2 (qualified) | 1972 era-norm tolerated（Stage 3 §4 Era-Norm Annotation の "communication-era tolerated" 適用）|
| GPT-5.5 | VQ-2 未達（VQ-1 qualified）| modern reassessment baseline |

両者は **どちらが正しいか** ではなく **「現代側からのアップグレード設計図」を作るときの基準点をどこに置くか** という方法論的差異。CLAUDE.md および Stage 3 v3 プロンプトは両解釈を許容するが、「VQ 通過/未達」のラベルで使う場合の標準を統一する必要がある（v18.3 / v19 候補）。

---

## 7. UQS としての価値判断

### 7.1 cross-model 移植性

異なるベンダー・異なるティアのモデル（Sonnet 4.6 中位 vs GPT-5.5 thinking 最上位）が同じ v18.2 プロンプトで **互角の解析品質** を出力した事実は：

- **UQS プロンプトが高い model-portability を持つ** ことを示す（プロンプト工学の成果）
- 得意領域（粒度 vs 集約、era-norm vs modern reassessment）は **モデル固有の bias** に起因
- CLAUDE.md の baseline = Sonnet 選択は **コスト/性能のバランス点として正当化**

### 7.2 GPT-5.5 の補完的価値

| 用途 | GPT-5.5 の優位 |
|---|---|
| **Stage 4 充填論文同定** | ★★★ web search による真の充填論文発見、9/9 zero hallucination |
| **U 項目の robustness 確認** | ★★ 細粒度 U 項目の発見が Sonnet の SRG 集約を補強 |
| **EP-10a 等の新規 EP/PRI 候補発見** | ★★★ MEMORY.md 記録の EP-10a robustness を裏付け |
| **書誌情報の正確性** | ★★★ DOI まで verifiable |
| **Modern literature reach** | ★★ 2014/2021 文献までカバー |

### 7.3 Sonnet の限界（structural）

- 内部知識依存による cutoff 後文献の見落とし
- 著者組合せ hallucination（67% 確証可能予想で発生）
- "1974 前後" のような hedged prediction が多くなる
- **Stage 4 充填論文同定は内部知識のみでは limited**

### 7.4 推奨される運用方針

| ワークフロー段階 | 推奨ツール | 理由 |
|---|---|---|
| **Stage 0-3 解析（公式 baseline）** | Sonnet | プロンプト遵守度・フォーマット標準・CLAUDE.md 方針 |
| **Stage 4 充填論文 first pass** | Sonnet | 内部知識による初期候補生成（網羅的）|
| **Stage 4 充填論文 verification + extension** | GPT-5.5 + web search | 意味論的検索で modern + niche 論文を補完 |
| **Stage 4 著者・書誌の確証** | Crossref API + WebFetch | 自動化された hallucination 検出 |

**core insight**: Sonnet と GPT-5.5 は **置換関係ではなく補完関係**。両者を並走させる cross-model verification protocol が UQS Stage 4 の robustness を一段引き上げる。

---

## 8. v18.3 / v19 への含意

本検証から派生する v18.3 / v19 候補（詳細は `improvements/v18.3_plan.md`）：

1. **Stage 4 §B に「Bibliographic verification step」を明示追加**: 充填論文候補に DOI/URL 提示を要求し、Crossref で post-hoc 検証可能にする
2. **充填論文の Confidence rating 分離**: 「論文の存在 confidence」と「EP 充填妥当性 confidence」を分離評価
3. **Cross-model verification protocol 化**: Sonnet 候補を GPT-5.5 等で web search 確証する標準手順
4. **VQ 判定の era-norm 標準化**: Sonnet（era-norm tolerated）と GPT-5.5（modern reassessment）の判定差を解消するメタルール

---

## 9. 結論

### 主要発見

1. **GPT-5.5 (web search): 9/9 引用論文すべて実在し書誌正確**、hallucination 0%
2. **Sonnet (内部知識): 確証可能な予想 3 件中 2 件で著者組合せ hallucination**（GPT-5.4 系と同型のパターンが Sonnet にも存在）
3. **user の WoS 仮説 empirical 支持**: GPT-5.5 が見つけた「正解」充填論文は WoS keyword search で構造的に見つかりにくい性質を持つ
4. **UQS Stage 4 の方法論的含意**: 充填論文同定は keyword search より semantic search に適合、cross-model verification が robustness 確保に valuable
5. **EP-10a robustness 確認**: GPT-5.5 が独立に EP-10a を導出（MEMORY.md 記録の 5 つの独立源に 6 つ目が追加）→ Codebook v0.4 への正式昇格条件強化

### UQS workflow への含意

- Sonnet を公式 baseline として維持（CLAUDE.md 方針正当）
- GPT-5.5 を **Stage 4 充填論文同定の補完ツール** として活用
- Crossref API による書誌確認を **post-hoc verification step** として workflow に組み込む（v18.3 候補）
- WoS は **二次情報源** として位置付け、UQS Stage 4 の core 検索手段としては LLM semantic search を採用

### 次の cross-model verification 対象

**dev/murai を次の cross-model verification 対象** とすることが推奨される（dev/murai は v17 までの完備、v18+ ゼロのクリーン・キャンバス、Kumada と異なる Ru-catalyzed C-H activation の有機合成論文）。

---

## 10. 参照

| ファイル | 内容 |
|---|---|
| `papers/dev/kumada/kumada_v182_sonnet_*.md` | Sonnet v18.2 出力（9 ファイル）|
| `papers/dev/kumada/gpt55thinking/GPT55_Kumada_v182.md` | GPT-5.5 v18.2 出力（単一エクスポート）|
| `papers/dev/kumada/gpt54thinking/` | GPT-5.4 v17 出力（参考、author hallucination 観察元）|
| `improvements/regression_log.md` Entry 052 | Sonnet 自動比較 v18.1 vs v18.2 Kumada |
| `improvements/changelog_v182.md` | v18.2 改訂仕様（C12-C16）|
| `improvements/v18.3_plan.md` | v18.3 への含意（Bibliographic verification 追加）|
| `MEMORY.md` GPT-5.4 author hallucination | 過去の cross-model 観察 |

---

*本レポートは UQS の cross-model verification methodology の最初の実証事例である。Sonnet（公式 baseline）と GPT-5.5（補完ツール）の補完的役割を確立し、Stage 4 充填論文同定における web search の構造的適合性を empirical に確認した。本知見は v18.3 / v19 設計および Phase 2 評価パイロットの方法論的根拠として活用される。*
