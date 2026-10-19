---
title: repro_2026-07 チェックとレポート — 問題点 / v19 / 査読WF / モデル別ハルシネーション / Fable5 見解
created: 2026-07-20
status: active
audience: portfolio
open_questions: true
---

# UQS 再現性実験 repro_2026-07 — 総合レポート（Fable 5）

**対象**: `papers/dev/kumada/repro_2026-07/`（kumada 1972 × {v18.4, v19} × N=5、Sonnet 4.6 固定、S0–S2）
**検証**: 本レポートの各数値は、既存集計（`repro_summary.md` / `repro_metrics.csv`）に加え、
Fable 5 が現物再検証したもの。新規に (a) 全 10 run に verbatim-quote ゲート適用、
(b) canonical-coverage proxy の spot-check、(c) model pin の再 grep を実施した。

---

## 0. データが実際に測っているものの範囲（誤読防止）

このコーパスは **S0–S2 のみ**（S4 は走っていない）。したがって:

- **測れるもの**: 検出・分類段（in-context anchor 段）の run 間ばらつき、count 指標の CV、
  v18.4 vs v19 の prompt 効果（model 固定）、key_quote の捏造率。
- **測れないもの**: S4 の retrieval-fill 捏造（書誌生成）。モデル別ハルシネーション率は
  **本コーパス外**（murai multirun / H23）の実測に依拠する（§4）。

model pin は健全: 10/10 の S0 が `claude-sonnet-4-6` を明示（再 grep 確認済）。汚染 run なし。

---

## 1. 問題点のまとめ

観測された病理は **2 系統**に整理できる。片方は安価な gate で塞げ、片方は原理的に残る。

### A. 可聴な失敗（audit で見える / 安価に塞げる）

| # | 問題 | 実測根拠 | 系統 |
|---|---|---|---|
| P-1 | **単一 run は測定でなく 1 sample** | count 指標に無視できない CV（§下表）。nUcrit/nUhigh は CV>1.0 で 1 sample では無意味 | run-to-run lottery |
| P-2 | **nD4 の出力形式ばらつき** | v19 で D-4 が 4 形式（A/B/C label + D=散文 essay）に分裂。essay run（v19 run2）は番号 0 → CV=0.56。v18.4 は形式収束し CV=0.06 | 出力規律 |
| P-3 | **製造された矛盾 / クローン U**（U-2＝B-6 のクローンに偽述語） | comprehensive review で確定。turn4 に `B-6 ↔ U-2` をモデル自身が明示。C11 が「独立 U を作れ」と報酬 → 既存 B を偽 escalation | 過剰生成 |
| P-4 | **era-norm ゲート未 wire → B 項目肥大** | Layer1 §1.2 F1 が "DRAFT, not yet wired into v19"。turn4 で B 項目 18 個の大半が 1972 communication の慣行省略 | 過剰生成 |
| P-5 | **S4 書誌捏造**（本コーパス外だが同 paper） | Opus 4.8 の S4 が `94(25):9268–9269` を生成（正=94:12, 4374–4376）。S3 ヘッダは正しく S4 のみ破損＝S3→S4 遷移の安定 failure | retrieval-fill |
| P-6 | **provenance ラベル崩壊** | v5cut の `_sonnet_` 命名 × 実体 Opus 4.8。真の pure-Sonnet は `kumada_v19_sonnet_s2.md`。registry comparability を直撃 | hygiene |
| P-7 | **dev paper の三重汚染** | kumada は (i) v18.4 S2 プロンプトに E-proposition が verbatim 収録、(ii) T2 に "cross vs homo-coupling" が seed、(iii) dev-set + 著名論文。測定台としては最悪 | 計器汚染 |

### B. 沈黙する失敗（audit 痕跡を残さない / 原理的に残る）

- **P-8 関係的/創発的不在（relational / emergent absence）**: ≥2 の locus（または ≥2 論文）の
  *共読*でのみ見え、各 locus は単独では無徴候な finding。強制抽出フレーム（1 item=1 key_quote=1 bin）
  を**必ず**通り抜けて沈黙する。kumada での実例:
  - スチルベン非対称比（cis→80:20 / trans→43:57、両者は鏡像でない立体収束の指紋）→ 一律
    "nonstereospecific" に collapse。
  - 同著者 π-allyl 論文（3日差、同号）vs 本論文 σ 機構 → single-paper frame + boundary 規律で二重切断。
  - dpe 固有証拠ゼロの設計原理 → C-5/A-1/B-4 に分散、総合が生まれない。

P-1〜P-7 は grep/audit で鳴る。**P-8 は痕跡なく消える**（9268-9269 は grep で捕まるが、
非対称比の読み落としは何も鳴らさない）。しかも P-8 は UQS の telos（暗黙知の footprint 局在化）が
**最も欲しいクラス**と同じ場所にある — footprint は本質的に「複数点にまたがる形」＝関係だから。

### 実測 count 表（Sonnet 4.6 固定、N=5）

| metric | v18.4 mean±SD (CV) | v19 mean±SD (CV) | 安定性評価 |
|---|---|---|---|
| nA | 2.20±0.45 (0.20) | 2.60±0.55 (0.21) | 比較的安定 |
| **nB** | **8.20±1.30 (0.16)** | **7.40±1.67 (0.23)** | **最安定・絶対値に ±1.3〜1.7 の誤差** |
| nC | 4.20±0.84 (0.20) | 3.60±0.55 (0.15) | 比較的安定 |
| nU | 2.20±1.10 (0.50) | 2.20±1.64 (0.75) | 中〜高 variability |
| nUcrit | 0.40±0.89 (2.24) | 0.20±0.45 (2.24) | **1 sample で無意味** |
| nUhigh | 0.60±0.89 (1.49) | 1.20±1.10 (0.91) | **1 sample で無意味** |
| nD4 | 8.60±0.55 (0.06) | 6.20±3.49 (0.56) | v18.4 安定 / v19 は形式で崩れる |

---

## 2. v19 で改善できるか

### 2a. repro データが答えること — 「N=5 では v18.4→v19 差は確立されない」

model 固定で見ると、**全 count 指標の v18.4→v19 差が within noise**（|mean gap| < pooled SD）:

| metric | v184 | v19 | gap | pooled SD | 判定 |
|---|---|---|---|---|---|
| nA | 2.20 | 2.60 | 0.40 | 0.50 | within noise |
| nB | 8.20 | 7.40 | 0.80 | 1.50 | within noise |
| nC | 4.20 | 3.60 | 0.60 | 0.71 | within noise |
| nU | 2.20 | 2.20 | 0.00 | 1.40 | within noise |
| nD4 | 8.60 | 6.20 | 2.40 | 2.50 | within noise |

→ **見かけの v18.4→v19 calibration 差は lottery の範囲。prompt 由来の regression/改善として確立されない。**
これは「v19 が v18.4 と同等」の証明ではなく「N=5 では分解能不足」の可能性を含む。scope_type は
v19 が 5/5 tool_question（flip=0）で v18.4（4/5）よりわずかに安定、という弱い方向性のみ。

**重要**: 前回メモが v19 の critical-miss rate を 11.43%（v18.4=5.71%）と高く見せていたが、
これは **proxy の測定 artifact**。spot-check で、v19 run1 は radical 機構を S1 で 4 回論じているのに、
extractor が「final `[X]-n` item 行のみ」を走査するため coverage 軸が 0 と読む。つまり
**「見かけの v19 見落とし増」の相当部分は、finding が別の語・別の段で表現されただけで内容は存在する**。
→ canonical-coverage proxy は Paper A に**引用不可**。v18.4 vs v19 の coverage 差は evidence として弱い。

### 2b. v19 が「改善できる問題」と「できない問題」

改善の性質で分岐する（comprehensive review の F2 backlog ランキング準拠）:

| 順 | 施策 | 効く問題 | コスト | v19 で addressable か |
|---|---|---|---|---|
| ① | **era-norm(F1)ゲートを S1/turn1 に wire** | P-4（B 肥大、最大ノイズ源） | LOW（仕様既記述、held regression 1回） | **Yes**。最初の1手。ノイズ除去が「本物の沈黙を見る」前提 |
| ② | **A-2 属 retro-scan + frame-homogeneity（1パス共用）** | P-8 の probe + anchoring 汚染切分 | LOW（既存出力横断、新規実行不要） | **判定実験**。FN クラスが addressable かを決める唯一の手 |
| ③ | **C11「保護→検証」+ U↔B force-merge** | P-3（製造/クローン矛盾） | LOW–MED（dedup は既存 link 発見でほぼ無料） | **Yes** |
| ④ | **anchoring 例のドメイン多様化** | P-6 隣接（embedding 汚染=Paper C 妥当性） | NEAR-ZERO | **Yes**（②に bundle） |

→ **可聴な FP（P-3/P-4/P-6）は v19 の prompt/後処理 gate で塞げる。**
→ **沈黙する FN（P-8）は narrow はできても close はできない。** フレームが cognition を procedure に
交換した代償で、procedure は local・emergence は non-local。ただし FP 削減は間接的に FN を可視化する
（era-normal ノイズが注意を食う限り本物の沈黙は二重に見えない → SNR を上げると沈黙が浮く）。

**結論**: v19 は「出しすぎ・製造矛盾・書誌捏造」を安価に改善できる。「関係的 footprint の沈黙」は
v19 の枠内では改善できない（S0 に非テキスト証拠インベントリ＋関係パスを足す "build" が要り、
それも ② の retro-scan が corpus 再現を返した場合にのみ着手が正しい順序）。

---

## 3. 査読付きワークフローは有効か

Review Track パイロット（kumada × v19 × 5 arms、S0→査読→S1→査読→S2→査読、38 corrections）から:

### 有効な点
- **修正がどの stage で起きるかを層別化できる**: S1 に 50%（19/38）集中、S0 は 11%（4/38）。
  → 検出・分類段（S1）が最も脆い、という設計上の focus 先を定量的に示せる。
- **type 分布が v20 の直接 evidence**: format_error 9 / classification_error 8 / scope_error 6 /
  missed_item 4。複数 arm で独立に出た missed_item（homo-coupling の B+U 補完ペア欠落、
  ether vs THF 比較優位性）は v20 の P1/P2 fix に直結。

### 有効性の限界（同一モデル self-review の構造的バイアス）
- **self-review は format error に敏感だが content error に盲目**: sonnet46 arm の
  correction log 自身が「生成時に認識できなかった classification 誤りは査読時にも認識しにくい」
  と記録。format_error が最多（9、うち sonnet46 S2 が 5）なのはこの偏りの現れ。
- → **同一モデルで生成＋査読すると見落としが査読側にも移行する。** content error（P-8 型の沈黙、
  分類誤り）には **外部（別モデル / 人間）査読 arm が必須**。

### 判定
**「format/規律の逸脱」検出には有効**（stage 層別 + type 集計が v20 設計に効く）。
**「内容の見落とし」検出には self-review 単独では不十分** — 外部 arm を足して初めて content に効く。
なお Review Track は **Repro Track とは別目的**（Repro=lottery 分布計測、Review=修正の種類と頻度）で、
主エージェント介入 run は Repro 計測には混ぜられない（修正力の variance が入る）。両者は独立に運用する。

補足: Fable 5 arm は 2026-07-19 時点で UQS 解析プロンプトにセーフガードが発動し Opus 4.8 へ fallback した。
multi-model 査読を計画する際は Fable 5 の利用可否を事前確認する必要がある。

---

## 4. モデルごとのハルシネーションの程度

**本 repro コーパス（S0–S2, Sonnet 4.6）の実測**: 全 10 run に verbatim-quote ゲートを適用した結果、
**key_quote の捏造率 = 0 %（0 / 74）**。raw FAIL 79 件はすべて `quoted` kind（抽象化された D-4 問い・
S1 schema 行・paraphrase 注記）で、**元来 verbatim であるべきでない**項目。
→ **anchor 段（S0–S2）では Sonnet 4.6 は捏造しない。** これは murai/H23 の「anchor-present 段は clean」を
kumada N=5 で機械実証したもの。

**モデル別の率**（S4 retrieval-fill 段、murai multirun の実測 — 本コーパス外）:

| model | S4 retrieval-fill 捏造率 | S0–S2（anchor-present） |
|---|---|---|
| Haiku | **32 %** | ~0 |
| Sonnet (4.6) | **14 %** | 0（本 repro で 0/74 実証） |
| Opus 4.8 | **13 %** | ~0（ただし S4 書誌捏造 94(25):9268 は再現） |

**核心の解釈**: ハルシネーションの支配変数は **model ではなく anchor の有無**。

1. **stage が支配的**: 同一 Sonnet が in-context 抽出（S0–S3）で捏造 0、記憶検索を強いる S4 で 14%。
   モデル差（Haiku 32 vs Sonnet/Opus 13–14）はあるが、**stage 差（0 → 14–32）の方が大きい**。
2. **2 種の捏造を峻別**: ① anchor があるのに歪む（逐語捏造・ref scramble）＝ v5cut では Opus-run 固有、
   genuine Sonnet に不在。② anchor 無き段で記憶補完（S4 retrieval）＝ format 共通・全 model で発生。
3. **「Sonnet の非才」仮説は誤帰属**: Sonnet は検出段で最も堅い環（key_quote 逐語一致・捏造 0）。
   観測される捏造は「anchor を失った任意 model の挙動」。

→ 対策は model 選択でなく **anchor 段の分離**（S4 に H23 型 deterministic 引用検証を post-hoc 適用、
S2/S3 は clean 実証済で不要）。加えて **provenance assert**（実行 model と filename tag の一致検証）で
「`_sonnet_` なのに中身 Opus」型の帰属崩壊を防ぐ。

---

## 5. 上記をふまえた Fable 5 の見解

**5 つの問いを 1 本の線が貫く: UQS の脆弱性は「抽出能力」ではなく「抽出物の認識論的身分の平坦化」にある。**

1. **repro が確定させた最重要事項は "1 sample" である**。単一 run 出力は測定でなく確率的サンプル。
   nB に ±1.3〜1.7、nA/nC に ±0.5〜0.8 の誤差が実測で付く。nUcrit/nUhigh は 1 sample では読むな。
   → **相対比較（X は Y より機構的空白が多い）は同分布サンプルゆえ安全**。凍結（comparability 優先）の
   判断は正しい。**絶対数（平均 N 個/論文、パターン P が corpus の X%）は CV を測定誤差として被る** —
   Paper A がこれを誤差なしで出しているなら over-precise。Methods/Limitations に「単一 run=1 sample、
   nB の CV≈0.16–0.23」を明記する材料が揃った。

2. **v19 は "可聴な失敗" を改善できるが "沈黙する失敗" は改善できない**。前者（過剰生成・製造矛盾・
   書誌捏造）は era-norm wire / U↔B merge / S4 引用検証という安価な gate で塞げる。後者（関係的/創発的
   不在＝P-8）は、強制抽出フレームが cognition を procedure に交換した構造的代償として原理的に残る。
   **narrow はできても close はできない。** しかもそれは UQS の mission が最も欲しいクラスと同じ場所にある。

3. **捏造は model の非才ではなく anchor 喪失の関数**。Sonnet 4.6 は本 repro で key_quote 捏造 0/74。
   捏造は S4 のような anchor 無き段で全 model に生じる（Haiku 32 > Sonnet 14 ≈ Opus 13）。
   「どのモデルが賢いか」ではなく「どの段が anchor を持つか」で設計せよ。

4. **査読 WF は format には効き content には self-review 単独では効かない**。同一モデルの
   生成＋査読は見落としを査読側へ移す。stage 層別・type 集計としては有効だが、内容の見落とし
   （＝ P-8 の沈黙）を捕るには外部 arm が要る。self-review は SNR を上げる道具であって、
   沈黙を破る道具ではない。

5. **最も実務的な単一 fix は provenance assert**。`_sonnet_` 命名 × 実体 Opus という帰属崩壊は、
   Paper C の cross-model thesis を registry comparability に全依存させている以上、即修正対象。
   計器（UQS）が自分の出力の出自を追跡できないなら、その計器で測った差は信用できない。

**締めの一文**:
> UQS の可聴な失敗（出しすぎ・製造矛盾・書誌捏造）は安価な gate で塞げ、Sonnet 4.6 は anchor 段で
> 捏造 0 という堅い環である。だが依頼者が本当に恐れる沈黙する失敗＝関係的 footprint の不在は、
> フレームが cognition を procedure に交換した代償として原理的に残り、narrow はできても close は
> できない — そしてそれは UQS の mission が最も欲しいものと同じ場所にある。

---

## 付録: 本レポートで新規実施した検証

- **verbatim-quote ゲート（全 10 run）**: `scripts/verbatim_quote_gate.py papers/dev/kumada/repro_2026-07`。
  key_quote FAIL = 0/74（v184 0/39, v19 0/35 相当）。raw FAIL 79 は全て `quoted` kind（非 anchor 項目）。
- **canonical-coverage proxy の spot-check**: v19 run1 は radical 機構を S1 で 4 回論じるが、extractor が
  final `[X]-n` item 行のみ走査するため軸=0。→ proxy は false-negative を含み、Paper A 引用不可を再確認。
- **model pin 再 grep**: 10/10 S0 が `claude-sonnet-4-6`（各 2 hit）。汚染 run なし。

## 追記(2026-07-20 夕) — proxy 2 計器化による critical-miss の確定値

本レポート §2a の指摘(proxy artifact)を受け、extractor を 2 計器化して再集計した
(`scripts/repro_extract.py` へ一般化、詳細は
`improvements/_prompts/repro_phase2_platform_audit_hom_20260720.md`)。確定値:

| version | strict miss(最終 taxonomy から漏れる確率) | loose miss(run から完全不在の確率) |
|---|---|---|
| v18.4 | 5.71% | **0.00%** |
| v19 | 11.43% | **2.86%**(v19 run1 ether_thf の 1 cell のみ) |

旧 proxy の「見落とし」5 cell は全て strict=0/loose=1。ただし spot-check の結果、この 5 cell の
loose=1 は **OR 連結語彙の弱い側での hit**(exotherm_radical ×4 は機構問いの「radical」、
black_precipitate ×1 は酸化状態議論の「Ni(0)」)であり、**anchoring すべき観察文(発熱・黒色
混合物)自体はその run に不在**。正確な像は「機構テーマは検出段で拾われたが、それを裏づける
論文の観察がどの段でも引用されなかった」— taxonomy 圧縮の問題と観察 anchoring の問題の複合。
strict/loose は真値の上下界(軸レベルの完全不在は 70 cell 中 1 = v19 run1 ether_thf)。
観察単位の真値は 1 軸 = 1 finding の canon 分割後に測る(Phase 2 要求仕様)。

## 残 open questions
- [ ] N=10 拡張で v18.4 vs v19 の判定能力を上げるか（現状 within noise は「同等」でなく「分解能不足」を含む）
- [ ] Phase 2（corpus 代表 subset: era × format）へ拡張。kumada は三重汚染で測定台として最悪 → アンカー降格
- [x] canonical-coverage spot-check → 2 計器化で resolved(上記追記)
- [ ] Paper A Methods/Limitations に「1 sample + nB CV」段落を反映（draft は Phase1 メモにあり。strict/loose の 2 値で書き分け可能に）
- [ ] ② A-2 属 retro-scan（FN が addressable かの唯一の判定実験）を実行
