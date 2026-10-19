---
title: R3-3 残り — Stage 4 再集計のための filling level と逆転判定の定義案
created: 2026-09-28
status: active
audience: paperA
open_questions: true
---

# Stage 4 再集計のための定義案（数える前に固定する）

対象: 投稿版の per-run Stage 4 記録 24 本（`papers/dev/{kumada,murai}/*_v184_sonnet_s4v2*.md`、2 論文 × JA/EN × 6 run）。
再集計する主張:
- (a) 「VQ 階層逆転は 24/24 run で再現」（Results Part 4、SI-3、SI-11）
- (b) 「EP-08a/EP-09a は 12 run すべてで specified filling level において undocumented」（Results Part 3）

## 数える前に分かった 3 つのこと

1. **「24/24」はモデル自身の判定を数えた可能性が高い。** Stage 4 v2 prompt の Step 5 の 4 番目（"VQ-hierarchy inversion diagnosis"）は、逆転の型（未充填が RI-01/08/09 に、充填が RI-03/06/07 に集まる）と、その解釈（出版インセンティブ）を prompt の側で示したうえで、当てはまれば記録するよう指示している。モデルが書いた判定文を数えれば、prompt が誘導した結果を数えることになる。→ **判定文（§D・§E の診断）は使わず、EP ごとのラベルから私たちの側で判定する。**
2. **同じ run の中で情報源が食い違う。** 例: `kumada_v184_sonnet_s4v2_en_run2.md` は EP-08a を §B で "Partial" としつつ、§E の未充填一覧にも載せている。ラベルが「Complete (for …) + Indirect (for …)」のように混ざる場合もある。→ どの欄を正とするかを先に決める。
3. **本文の VQ の向きが一貫していない。** Methods 1.2 は VQ-4（replication / benchmark）を最上位と定義している。一方 Discussion 1 は同じ EP-08a/09a（RI-08/RI-09）を "low-VQ benchmarking EPs"、機構系を "high-VQ" と呼んでいる。Stage 4 prompt と Phase 1.5 報告書も Discussion 1 と同じ向き。→ 再集計では **Methods 1.2 の VQ 目標**（下の表）で群を分け、改稿で Discussion 1 の呼び方を直す（別項目として点検表に追加）。

## 定義案

### D1. ラベルの出所

- **§B の各 EP の "Nature of filling" を唯一の出所にする。** §C（推奨一覧）、§D（階層と時間の対応）、§E（未充填の診断）は使わない。
- §B に EP の項目が無ければ、その EP は未充填とする。
- 混合ラベルは**最も弱い成分**を採る（例: "Complete (for X) + Indirect (for Y)" → Indirect）。EP が求める対象系そのものについて最も控えめな読みにするため。
- 食い違い（§B では充填、§E では未充填）は CSV に `conflict=1` として記録し、件数を報告する。

### D2. 充填とみなす水準（3 水準、数える前に主水準を指定）

| 水準 | 充填とみなすラベル | 位置づけ |
|---|---|---|
| **L-std（主）** | Complete、Partial | 本文の主張を支配する locked WoS audit の閾値（Partial 以上）と揃う |
| L-strict（感度） | Complete のみ | |
| L-lenient（感度） | Complete、Partial、Indirect | |

- **Attempted と Paradigm-shift は、どの水準でも充填に数えない。** prompt 自身が、Attempted を "does not function as a filling"、Paradigm-shift を "the EP is not resolved" と定義しているため。
- **Confidence は水準に使わない。** ただし L-std について、Confidence = Low の充填を除いた場合の値を併記する。
- Top-3 の再集計では主規則を置かなかった（結果を見た後だったため）。**今回はまだ数えていないので、主水準を先に 1 つ指定できる。** L-std を提案する。

### D3. EP の群（Methods 1.2 と Fig. 3 の VQ 目標）

| 群 | EP |
|---|---|
| VQ-1/2 目標 | EP-01a、EP-02a、EP-07a |
| VQ-3 目標（機構） | EP-03a、EP-04a、EP-05a、EP-06a、EP-10a |
| VQ-4 目標（replication / benchmark） | EP-08a、EP-09a |

- EP の ID と群は両論文で共通のライブラリを使う（Murai で出てこない EP は分母から除く）。**要確認**: Murai の Stage 3 が各 EP に付けた VQ 目標がこの表と一致するか、数える前に確かめる。

### D4. 逆転の判定（run ごと、数える前に固定）

- **逆転あり** ⇔ (i) VQ-4 目標の 2 EP がどちらも未充填 かつ (ii) VQ-3 目標の EP が 1 つ以上充填
- 併記する強い版: (ii′) VQ-3 目標の EP の過半数（出てきた EP のうち半数超）が充填
- run ごとに群別の充填率（VQ-1/2、VQ-3、VQ-4）も CSV に出し、二値の判定だけでなく勾配を見られるようにする

### D5. 主張 (b) の判定

- EP-08a、EP-09a のそれぞれについて、L-std で未充填だった run の数を論文 × 言語ごとに数える（分母は各 6、合計 12 run/論文）

### D6. 範囲の明記

- これは **Stage 4 の LLM-parametric 層**の再集計で、本文の主張を支配する locked WoS audit ではない。改稿文でもそう書く（「24/24」は探索層の run 間再現性であって、充填の事実を示すものではない）。
- 充填の**時期**（「4–12 年で充填」「30–54 年後も未充填」）は今回の対象外。Onset 年の分布として別に集計できる。

## 決めてほしいこと

1. D2 の主水準を L-std（Complete + Partial）にしてよいか
2. D1 の混合ラベルを「最も弱い成分」で読むことでよいか
3. D4 の逆転の判定を (i) + (ii) とし、(ii′) を併記する形でよいか
4. Discussion 1 の "low-VQ benchmarking EPs" を Methods 1.2 の向き（VQ-4 = 最上位）に直すことを、点検表に追加してよいか
