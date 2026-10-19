# Sonnet vs GPT-5.5 — Murai 1993 v18.2 Cross-Model 比較・検証レポート

**作成日:** 2026-04-27
**作成モデル:** Opus 4.7（横断比較・検証実施）
**対象論文:** Murai, S.; Kakiuchi, F.; Sekine, S.; Tanaka, Y.; Kamatani, A.; Sonoda, M.; Chatani, N. (1993) Nature 366, 529-531 — devset Murai
**プロンプト:** v18.2 (S0–S2) + v3 (S3–S4)
**比較対象モデル:** Claude Sonnet 4.6 / OpenAI GPT-5.5 thinking
**関連:** `papers/dev/kumada/cross_model_v182_comparison.md`（Kumada 版 cross-model 比較）, `improvements/v18.3_plan.md`, `improvements/cross_model_kumada_vs_murai_meta.md`

---

## 1. 動機

Kumada での cross-model 比較で得られた知見（GPT-5.5 web search が WoS 構造化検索より UQS Stage 4 に適合、Sonnet の 67% hallucination 率）が **paper-specific な structural property に依存するか、モデル能力の一般的差異か** を判別するため、dev/murai を 2 例目として cross-model 検証する。

dev/murai は以下の特性で適切：
- v17 までの完備した baseline、v18+ ゼロのクリーン・キャンバス（Sonnet/GPT-5.5 とも v18.2 を fresh で実行）
- Kumada と異なる論文タイプ（Murai 1993 Nature, Ru 触媒 C-H 活性化、有機合成）
- 異なる方法論プロファイル

---

## 2. 比較設計

### 2.1 入力統一

- 同一 PDF (`Murai_1993.pdf`)
- 同一 v18.2 プロンプト群
- 同一 Stage 順序 (S0 → Turn 1-3 → Turn 4 → S2 → S3v3 → S4v3)

### 2.2 評価軸

Kumada 比較と同一の評価軸（量的比較、C12-C16 発火、質的差異、VQ 判定、充填論文の DOI 検証、充填妥当性）。

---

## 3. 充填論文 DOI 検証結果

### 3.1 Sonnet 予想（7 報、Crossref API で全件検証済）

| # | Sonnet 引用 | Crossref 検証 | DOI |
|---|---|---|---|
| 1 | Kakiuchi-Sekine-Tanaka-Kamatani-Sonoda-Chatani-Murai (1995) BCSJ 68(1), 62-83 [REDACTED: substantial verbatim quotation; see Tier 9] | ✅ 完全一致 | 10.1246/bcsj.68.62 |
| 2 | Murai-Kakiuchi-Sekine-Tanaka-Kamatani-Sonoda-Chatani (1994) Pure Appl. Chem. 66(7), 1527-1534 "Catalytic C-H/olefin coupling" | ✅ 完全一致 | 10.1351/pac199466071527 |
| 3 | Kakiuchi-Murai (2002) Acc. Chem. Res. 35(10), 826-834 "Catalytic C−H/Olefin Coupling" | ✅ 完全一致 | 10.1021/ar960318p |
| 4 | **Chatani-Fukuyama-Kakiuchi-Murai (1998) JACS 120, 11522 "Rh触媒C-H/CO挿入"** | ⚠️ **部分 hallucination** | 実際は Fukuyama-Chatani-**Tatsumi**-Kakiuchi-Murai (1998) JACS 120, 11522-11523、**Ru₃(CO)₁₂ 触媒**（Sonnet が Rh と誤記）、Tatsumi 著者欠落 |
| 5 | Balcells-Clot-Eisenstein (2010) Chem. Rev. 110(2), 749-823 [REDACTED: substantial verbatim quotation; see Tier 9] | ✅ 完全一致 | 10.1021/cr900315k |
| 6 | Guari-Sabo-Etienne-Chaudret (1999) Eur. J. Inorg. Chem. 1999(7), 1047-1055 [REDACTED: substantial verbatim quotation; see Tier 9] | ✅ 完全一致 | 10.1002/(SICI)1099-0682(199907)1999:7<1047::AID-EJIC1047>3.0.CO;2-B |
| 7 | Ackermann-Althammer-Born (2006) Angew. Chem. Int. Ed. 45(16), 2619-2622 [REDACTED: substantial verbatim quotation; see Tier 9] | ✅ 完全一致 | 10.1002/anie.200504450 |

**Sonnet hallucination 率: 0/7 (0%) 全 hallucination + 1/7 (14%) 部分 hallucination**

### 3.2 GPT-5.5 引用（8 報、Crossref API で全件検証済）

| # | GPT-5.5 引用 | Crossref 検証 | DOI |
|---|---|---|---|
| 1 | Kakiuchi BCSJ 1995（共有）| ✅ 完全一致 | 10.1246/bcsj.68.62 |
| 2 | Sonoda-Kakiuchi-Chatani-Murai (1997) BCSJ 70(12), 3117-3128 [REDACTED: substantial verbatim quotation; see Tier 9] | ✅ 完全一致 | 10.1246/bcsj.70.3117 |
| 3 | Matsubara-Koga-Musaev-Morokuma (1998) JACS 120(48), 12692-12693 [REDACTED: substantial verbatim quotation; see Tier 9] | ✅ 完全一致 | 10.1021/ja9816943 |
| 4 | Guari-Castellanos-Sabo-Etienne-Chaudret (2004) J. Mol. Catal. A 212(1-2), 77-82 "RuH2(H2)2(PCy3)2: a room temperature catalyst for the Murai reaction" | ✅ 完全一致 | 10.1016/j.molcata.2003.10.034 |
| 5 | Yi-Lee (2009) Organometallics 28(15), 4266-4268 [REDACTED: substantial verbatim quotation; see Tier 9] | ✅ 完全一致 | 10.1021/om900416k |
| 6 | Kakiuchi-Kochi-Mizushima-Murai (2010) JACS 132(50), 17741-17750 [REDACTED: substantial verbatim quotation; see Tier 9] | ✅ 完全一致 | 10.1021/ja104918f |
| 7 | Rouquet-Chatani (2013) Chem. Sci. 4, 2201 [REDACTED: substantial verbatim quotation; see Tier 9] | ✅ 完全一致 | 10.1039/c3sc50310k |
| 8 | Lei-Feng-Du-Xu (2000) Sci. China B 43(4), 412-420 [REDACTED: substantial verbatim quotation; see Tier 9] | ✅ 完全一致 | 10.1007/bf02969447 |

**GPT-5.5 hallucination 率: 0/8 (0%)**

---

## 4. Murai での核心発見

### 4.1 Sonnet hallucination が **大幅に減少**（Kumada との対比）

| 観点 | Kumada (1972) | **Murai (1993)** |
|---|---|---|
| Sonnet 全 hallucination | 2/3 (67%) | **0/7 (0%)** |
| Sonnet 部分 hallucination | 0% | **1/7 (14%)** |
| GPT-5.5 hallucination | 0/9 (0%) | 0/8 (0%) |

Sonnet の hallucination 率は **論文ごとに大きく変動**：Kumada（古い、過密な著者ネットワーク）では深刻、Murai（より新しい、整然とした著者構造）では minimal。

### 4.2 部分 hallucination の詳細（Chatani-Fukuyama 1998）

Sonnet 予想：「Chatani, N.; Fukuyama, T.; Kakiuchi, F.; Murai, S. *J. Am. Chem. Soc.* 1998, 120, 11522-11523 — Rh触媒によるC–H/CO挿入で中間体に関する機構的知見」

実際の論文：
- 著者: **Fukuyama**, T.; **Chatani**, N.; **Tatsumi**, J.; Kakiuchi, F.; Murai, S.
- タイトル: [REDACTED: substantial verbatim quotation; see Tier 9]
- DOI: 10.1021/ja982794b

差異：
1. 著者順序の swap: 実際は Fukuyama 筆頭、Sonnet は Chatani を筆頭と記載
2. 著者欠落: Tatsumi（第 3 著者）を Sonnet が省略
3. **化学が誤り: Rh 触媒ではなく Ru₃(CO)₁₂ 触媒**（金属が異なる）

タイトル・DOI レベルで paper exists だが、Sonnet が記述した化学内容が事実と異なる。これは「書誌レベルの捏造」ではなく「化学的内容の誤記」というより微妙な hallucination パターン。

### 4.3 両モデル共通同定の意義（Kakiuchi 1995 BCSJ）

Sonnet と GPT-5.5 が **独立に Kakiuchi BCSJ 1995 を最重要充填候補として同定**。これは：
- 両モデルが Communication→Full Paper 自動充填パターンを正しく認識
- Stage 4 §D の「自己充填」「分割提示充填」分類が両モデルで等価に機能
- 両モデル独立同定により、このパターンの robustness が **n=2 → n=2** で確認

### 4.4 EP-10a usage の二極化（両論文で一貫）

| 出力 | EP-10a 使用回数 |
|---|---|
| Sonnet Kumada s4v3 | **0 回** |
| Sonnet Murai s4v3 | **0 回** |
| GPT-5.5 Kumada v182 | 15 回 |
| GPT-5.5 Murai v182 | 14 回 |

両論文で完全に一貫したモデル間差。**Sonnet は EP-10a（v18.2 で「暫定」と marked）を保守的に未使用、GPT-5.5 は両論文で活用**。

GPT-5.5 が Murai でも EP-10a を独立に使用したことで、**EP-10a 7 つ目の独立観察**（MEMORY.md 既存 5 源 + Kumada GPT-5.5 + Murai GPT-5.5）。Codebook v0.4 への正式昇格条件が更に強化。

---

## 5. 補完的カバレッジプロファイル

両モデルの推奨選定リスト（5+7 報）の比較：

| 論文タイプ | Sonnet 寄り | GPT-5.5 寄り |
|---|---|---|
| Review / Perspective | Pure Appl. Chem. 1994, Acc. Chem. Res. 2002, Chem. Rev. 2010, Angew. Chem. 2006 | （少ない）|
| Primary research (機構)| Balcells 2010 (DFT review) | Matsubara 1998 (DFT primary), Lei 2000 (ab initio), JACS 2010 (kinetics) |
| Primary research (scope)| （少ない）| Sonoda 1997, Yi-Lee 2009, Rouquet 2013 |
| 異種金属拡張 | Ackermann 2006 (Pd) | Rouquet 2013 (bidentate DG) |

→ **Sonnet はレビュー/総説寄り、GPT-5.5 は primary research 寄り**。両者は構造的に補完的。

具体的な **覆い分け**:
- **Sonnet が GPT-5.5 を補完**: Pure Appl. Chem. 1994（Murai 自身の早期 retrospective、近代的 review 論文では言及されない）、Balcells Chem. Rev. 2010（DFT 包括 review、計算化学の包括的視点）、Ackermann 2006（異種金属 Pd への拡張視点）
- **GPT-5.5 が Sonnet を補完**: Matsubara 1998 / Lei 2000（DFT primary、レビューでない原著論文）、Yi-Lee 2009（cationic Ru-H 室温触媒）、JACS 2010（structural elucidation + kinetics）、Rouquet 2013（bidentate directing group による scope 拡張）

---

## 6. v18.2 改訂 (C12-C16) 発火状況（Murai での観察）

| 改訂 | Sonnet | GPT-5.5 | 備考 |
|---|---|---|---|
| **C12** 報告対称性 | △ 部分 | ✅ 明確 | Kumada と同型 |
| **C13** 最悪シナリオ | ✅ 実装 | △ 暗黙的 | Kumada と同型 |
| **C14** 診断問い | △ 弱い | ✅ 強い | Kumada と同型 |
| **C15** 参照クラス | ✅ 実装 | △ 間接的 | Kumada と同型 |
| **C16** epistemic marker | ❌ 該当外 | ❌ 該当外 | Murai は実験論文（Kumada と同様 C16 不発火が正解）|

Kumada と Murai で C12-C16 の発火パターンが **同型** に再現。これは v18.2 改訂の **モデル間 portability の安定性** を示す。

---

## 7. 量的比較サマリー

| 項目 | Sonnet | GPT-5.5 | 観察 |
|---|---|---|---|
| **A 項目** | 11 | 10 | 同等 |
| **B 項目** | 14 | 18 | GPT-5.5 が +4（細粒度傾向は Kumada と同様）|
| **C 項目** | 4 | 6 | GPT-5.5 が +2 |
| **U 項目** | 1 | 6 | **GPT-5.5 が +5（Kumada と同パターン）** |
| **SRG 数** | 6 | 8 | GPT-5.5 が +2 |
| **D-4 候補数** | 6 | 8 | GPT-5.5 が C9 拡張上限活用 |
| **EP 第二群** | 3 | 4（+EP-10a） | **GPT-5.5 が EP-10a を Murai でも導入** |
| **推奨選定論文** | 5 | 7 | GPT-5.5 が広い coverage |
| **VQ 判定** | VQ-2 | VQ-2 (qualified) | 同等（Kumada では差異あったが Murai では一致）|

**注目ポイント**：U 項目数の差（1 vs 6）は Kumada（1 vs 7）と同型。**Sonnet の SRG 集約 vs GPT-5.5 の U 分散** という粒度差は **両論文で一貫したモデル特性** であることが確認された。

VQ 判定の Era-norm tolerance 適用度の差（Kumada では Sonnet VQ-2 qualified vs GPT-5.5 VQ-2 未達）は Murai では一致（両者 VQ-2 (qualified)）。**1993 年は両モデルとも era-norm tolerance を必要としない modern era とみなした** ため判定差が消えた可能性。

---

## 8. user の Web of Science 仮説の Murai での再検証

GPT-5.5 が見つけた充填論文のうち、**WoS keyword 検索で見つけにくい性質** を持つもの：

| 論文 | WoS 検索の困難性 |
|---|---|
| **Sonoda 1997 BCSJ "Effect of Various Substituents"** | タイトルに "Murai" や "Ru" を含まず、「substituent effects」は無数の論文に共通するキーワード |
| **Matsubara 1998 JACS "DFT study on activation of ortho-CH"** | "ortho-CH" や "DFT" は一般的キーワード、Murai 1993 の文脈との繋がりは semantic 理解必須 |
| **Yi-Lee 2009 Organometallics "Cationic Ru hydride complex"** | 異なる触媒系（cationic Ru-H vs Ru(H)(H)L）、Murai 1993 との繋がりは「同種反応の異触媒系」という意味論的概念必須 |
| **Rouquet 2013 Chem. Sci. "bidentate-chelation assistance"** | 異なる directing group（amide vs ketone）、scope 拡張の意味論的繋がり必須 |

→ ユーザーの WoS 仮説は Murai でも支持される。**LLM semantic search が WoS keyword search より UQS Stage 4 に適合** という結論は **Kumada → Murai で再現**（n=2）。

---

## 9. UQS としての価値判断

### 9.1 cross-model 移植性

両論文で v18.2 改訂 (C12-C16) の発火パターンが **同型** に再現。Sonnet と GPT-5.5 は **異なる得意領域を持ちながら、UQS プロンプトの構造的従順度は同等**。

### 9.2 GPT-5.5 の補完的価値

- **Stage 4 充填論文同定**: Murai での 0% hallucination + WoS 検索困難な論文の同定により、Kumada での観察が再現
- **EP-10a robustness**: Murai での独立使用により 7 源確認、Codebook v0.4 昇格条件が確実
- **Primary research coverage**: Sonnet がカバーしないモダンな実験/計算論文（Sonoda 1997, Matsubara 1998, Yi-Lee 2009, JACS 2010, Rouquet 2013）

### 9.3 Sonnet の paper-dependent な信頼性

- Murai では hallucination 率 0%（Kumada の 67% から大幅減少）
- 部分 hallucination（Chatani 1998 chemistry 誤記）は依然として存在
- **論文年代・著者ネットワーク密度に依存** という条件付きの評価が必要

### 9.4 推奨される運用方針（Murai 観察反映）

| ワークフロー段階 | 推奨ツール | 理由 |
|---|---|---|
| **Stage 0-3 解析** | Sonnet（公式 baseline）| プロンプト遵守度・フォーマット標準 |
| **Stage 4 充填論文 first pass** | Sonnet | 内部知識による初期候補生成 |
| **Stage 4 充填論文 verification + extension** | GPT-5.5 + web search | 意味論的検索で modern + niche 論文を補完、両論文で 0% hallucination |
| **Stage 4 著者・書誌の確証（古い/iconic 論文の場合）** | Crossref API + WebFetch | Sonnet hallucination 検出 |
| **Stage 4 著者・書誌の確証（新しい/整然論文の場合）** | optional | Sonnet が信頼できる場合は省略可 |

→ verification step を **conditional に発動** することで効率化（v18.3_plan.md C17 に反映）

---

## 10. Kumada との比較メタ観察（要約）

詳細は `improvements/cross_model_kumada_vs_murai_meta.md` を参照。主要ポイント：

1. **Sonnet hallucination 率は paper-dependent**: Kumada 67% → Murai 0%（劇的差）
2. **GPT-5.5 hallucination 率は paper-independent**: Kumada 0%, Murai 0%（一貫）
3. **両モデル独立同定の robustness**: 「Communication→Full Paper 自動充填」パターンが両論文（Kumada 1976 Tamao BCSJ, Murai 1995 Kakiuchi BCSJ）で両モデル独立確認
4. **EP-10a の cross-paper robustness**: GPT-5.5 が Kumada + Murai 両方で独立使用（7 源到達）
5. **C12-C16 発火パターンの同型再現**: モデル間差は両論文で一貫、UQS プロンプトの portability 確認

---

## 11. 参照

| ファイル | 内容 |
|---|---|
| `papers/dev/murai/murai_v182_sonnet_*.md` | Sonnet v18.2 出力（8 ファイル）|
| `papers/dev/murai/gpt55thinking/GPT55_murai_v182.md` | GPT-5.5 v18.2 出力（単一 export）|
| `papers/dev/kumada/cross_model_v182_comparison.md` | Kumada 版 cross-model 比較（並行レポート）|
| `improvements/cross_model_kumada_vs_murai_meta.md` | Kumada vs Murai メタ観察 |
| `improvements/v18.3_plan.md` | v18.3 計画書（本検証反映後の更新版）|
| `improvements/regression_log.md` Entry 055 | Sonnet 自動比較 v17 vs v182 Murai |

---

*本レポートは UQS の cross-model verification methodology の 2 例目の実証事例である。Kumada での観察（Sonnet 67% hallucination, GPT-5.5 0% hallucination）が paper-dependent であることを Murai で確認。これにより v18.3 C17（Bibliographic verification step）を conditional triggering に修正する根拠が得られた。*

---

> **Tier 8 redaction notice**: This file is a redacted copy of the corresponding Tier 3 / Tier 9 output. Verbatim source-paper quotations have been replaced by `[REDACTED: see source paper §<loc>; full text retained in Tier 9 reviewer-only deposit]` markers, preserving location references and our own analytical content. Bibliographic fields (title, authors, journal, year, DOI), analytical labels (`evidence_chain:` with B-/U-/A-/C- internal IDs), short technical terms, and our own analytical text are not redacted. The redaction was applied by `scripts/redact_for_tier8.py` and, for this version, by `scripts/build_paperA_R1_public.py` with `scripts/redact_source_ngram_runs.py` (scripts of the project repository; they are not deposited).
