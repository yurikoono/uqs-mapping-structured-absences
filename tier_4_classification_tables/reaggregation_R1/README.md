---
title: R3-3 再集計 — Top-3 reinforcement EP SET の inclusion frequency
created: 2026-09-28
status: active
audience: paperA
open_questions: true
---

# R3-3 再集計: Top-3 EP SET の inclusion frequency

## 何をしたか

投稿版の per-run Stage 3 記録 24 本（`submissions/paperA_2026-06-30_Digital_Discovery_v1/papers/dev/{kumada,murai}/*_v184_sonnet_s3v2*.md`、Kumada / Murai × JA / EN × 6 run）から、Top-3 EP を**抽出規則を先に決めて**機械的に数え直した。スクリプトは `reaggregate_top3.py`、出力は次の 3 つ。
- `multirun_top3_per_run.csv`: 72 行（24 run × 3 規則）
- `inclusion_frequency_per_cell.csv`
- `extraction_trace.md`: run ごとの §5 のルート見出しと EP の並び。手作業での監査用

## 抽出規則

Stage 3 v2 prompt は「Top-3」という出力欄を定めていない。§5（Shortest-reinforcement route）に「目的関数ごとの EP 投資順」を書かせているだけで（prompt Step 5a–5b）、明示の Top-3 表があるのは Kumada JA run 1 だけだった。そこで次の 3 規則で数えた。

| 規則 | 定義 | 性格 |
|---|---|---|
| FIRSTOBJ | §5 の最初のルートブロック（prompt の第一目的関数 = 現在の 1 段上の VQ）の先頭 3 EP | prompt の手順に最も忠実。ただし論文や run によって目標の VQ が変わる（Kumada は主に VQ-3、Murai は run により VQ-2） |
| VQ3 | 「VQ-3 へのルート」ブロックの先頭 3 EP | 目標を固定するので論文間で比べられる |
| FIRST3 | §5 に登場する最初の 3 EP | 感度分析。報告書の run 別の並びに最も近い |

## 結果（EP-03a / EP-04a / EP-06a の inclusion frequency、各セル n = 6）

| セル | 規則 | EP-03a | EP-04a | EP-06a | 3 つそろった run |
|---|---|---|---|---|---|
| Kumada JA | FIRSTOBJ | 5/6 (83%) | 5/6 (83%) | 5/6 (83%) | 5/6 |
| | VQ3 | 6/6 (100%) | 6/6 (100%) | 6/6 (100%) | 6/6 |
| | FIRST3 | 5/6 (83%) | 5/6 (83%) | 6/6 (100%) | 5/6 |
| Kumada EN | FIRSTOBJ | **4/6 (67%)** | 5/6 (83%) | 5/6 (83%) | 4/6 |
| | VQ3 | 5/6 (83%) | 6/6 (100%) | 6/6 (100%) | 5/6 |
| | FIRST3 | 5/6 (83%) | 5/6 (83%) | 5/6 (83%) | 5/6 |
| Murai JA | FIRSTOBJ | **3/6 (50%)** | **2/6 (33%)** | **3/6 (50%)** | 2/6 |
| | VQ3 | 6/6 (100%) | **3/6 (50%)** | 6/6 (100%) | 3/6 |
| | FIRST3 | **4/6 (67%)** | **2/6 (33%)** | **3/6 (50%)** | 2/6 |
| Murai EN | FIRSTOBJ | 5/6 (83%) | 5/6 (83%) | 5/6 (83%) | 5/6 |
| | VQ3 | 6/6 (100%) | 6/6 (100%) | 6/6 (100%) | 6/6 |
| | FIRST3 | 5/6 (83%) | 5/6 (83%) | 5/6 (83%) | 5/6 |

太字は 75% 未満。

## 読み取れること

1. **Kumada**: VQ3 と FIRST3 の規則では、2 つのセル（JA・EN）× 3 EP の値がすべて 83% 以上。FIRSTOBJ では EN の EP-03a が 67% で閾値を下回る（run 4 の最初のルートが VQ-2 行きのため）。
2. **Murai**: **JA のセルは、どの規則でも閾値を満たさない**（EP-04a は 33–50%）。EN のセルはどの規則でも 83% 以上。
3. したがって投稿版 SI の「Kumada と Murai の両方で ≥75%」（SI-11 l.229 ほか）は、どの規則でも成り立たない。本文 Principle 4 の「Top-3 SET が ≥75% で再現」は、Kumada に限れば 2 規則で成り立つが、1 規則では成り立たない。

## Phase 1.5 報告書（2026-05-10）との食い違い

報告書の集計表は、次の 2 点で一次記録と合わない。
- **報告書の中での算術の誤り**: Kumada EN の run 別の表では EP-06a を含む run が 5 本（run 4 は「07a, 03a, 04a」）なのに、集計欄は 6/6（100%）となっている。
- **run 別の並びがファイルと一致しない**: 例えば Murai EN run 5 は、報告書では「03a, 01a, 07a」、ファイルでは §5 のどこを取っても「03a, 04a, 06a」が先頭。Murai EN run 6 は、報告書では「03a, 01a, 07a」、ファイルでは「01a, 09a, 07a」が先頭（VQ-2 行きのルート）。報告書の並びが、どのファイルのどの箇所から取られたのかは特定できなかった（subagent の検証でも 7 run が再現不能）。

報告書の Murai の値（JA は EP-04a 67% / EP-06a 67%、EN は 67% / 50%）も、どの規則の再集計値とも一致しない。**この報告書の数値はどれも、一次記録から再導出できない**ものとして扱う。

## 改稿への提案（2026-09-28 user 承認、本文・SI-3・SI-11 に適用済）

1. **Principle 4（Methods 1.4）と SI-3 / SI-11**: Top-3 の主張を「Kumada 1972 の 2 セル（JA・EN）」に限定する。3 規則の感度分析表（上の表）を SI に載せ、CSV 3 本を寄託する。**事後に都合のよい規則を選んだと読まれないよう、主規則を 1 つに絞らず 3 規則すべてを報告する**。
2. **Murai**: JA のセルが閾値に届かないことを明記する。「単一 run の順位は揺れるが、SET は安定する」という主張は Murai JA では成り立たない、と書く。
3. **応答書（R3-3）**: 指摘を認める。抽出規則が未定義だったこと、集計表が一次記録から再現できなかったことを述べ、再集計の方法と結果を示す。

## まだ再集計していないもの（R3-3 の残り）

- 本文 l.277 の「VQ 階層逆転は 24/24 run で再現」と l.202 の「EP-08a/09a が 12 run すべてで undocumented」。Stage 4 の per-run 記録 24 本から数え直す必要がある。「specified filling level」の定義を先に決める
- L3 の「23/24 multi-run universal-core convergence」: Paper A の記録に出所が見つからない。**削除する**（2026-09-30 更新: 別研究の値を出所として示す記述は取り下げた）
- SI-11.4 の「40–70% (n = 12)」「60–85%」、SI-11.13 の「~75%」: 出所が見つからない


## 追記

- Murai JA の EP-04a（33%）は、SI-11.1 の失敗基準（inclusion frequency < 50%）に該当する。SI-3 に明記した。

---

# R3-3 残り: Stage 4 の再集計（2026-09-28）

定義は `definitions_fixed_before_counting.md`（user 承認済、**数える前に固定**）。スクリプトは `reaggregate_stage4.py`。
出力は `stage4_labels_per_ep.csv`（240 行 = 24 run × 10 EP、生のラベル文字列つき）と `stage4_inversion_per_run.csv`（96 行 = 24 run × 4 水準）。

## 抽出の確認

- ラベルの内訳: Partial 98、Indirect 46、Complete 23、未同定（unidentified / N/A 等）14、Attempted・Paradigm-shift 6、§B に項目なし 53。§B に無いのはほぼ EP-02a と EP-10a（各 22 件）で、その run の Stage 3 がこれらの EP を立てていない。§B で名前に触れているのに拾えなかったのは 1 件だけ
- 補足ブロック（例: 「**EP-03a 補充（KIE測定）**」）が本来のラベルを上書きしないよう修正した
- §B では充填、§E では未充填と、同じ run の中で食い違う EP は 12 件（CSV の `conflict=1`）
- Kumada の EP-08a / 09a は、生のラベルを 24 行すべて目視で確認した。モデル自身が §B で「Partial」と書いていて（多くは但し書き付き）、抽出の誤りではない

## 結果（24 run、各セル n = 6）

| 水準 | 逆転 | 逆転（強い版） | 逆転（VQ-3 = 03/04/06 のみ） | EP-08a 未充填 | EP-09a 未充填 | モデルの文章が「逆転」に触れる |
|---|---|---|---|---|---|---|
| **L-std（主）** | **12/24** | 7/24 | 12/24 | **14/24** | **18/24** | 24/24 |
| L-strict | 4/24 | 0/24 | 3/24 | 23/24 | 23/24 | 24/24 |
| L-lenient | 2/24 | 2/24 | 2/24 | 9/24 | 2/24 | 24/24 |
| L-std（Low 除外） | 16/24 | 7/24 | 16/24 | 20/24 | 18/24 | 24/24 |

主水準（L-std）のセル別の値:

| セル | 逆転 | 逆転（強い版） | EP-08a 未充填 | EP-09a 未充填 |
|---|---|---|---|---|
| Kumada JA | 1/6 | 1/6 | 1/6 | 3/6 |
| Kumada EN | 3/6 | 2/6 | 4/6 | 4/6 |
| Murai JA | 4/6 | 2/6 | 5/6 | 6/6 |
| Murai EN | 4/6 | 2/6 | 4/6 | 5/6 |

## 読み取れること

1. **「逆転は 24/24 run で再現」は、EP ごとのラベルからは再現しない。** 主水準で 12/24、最も緩い水準では 2/24、最も厳しい水準（Complete のみを充填とする）でも 4/24。24/24 に一致するのは「モデルの文章が逆転に触れている」run の数だけで、これは prompt（Stage 4 v2 Step 5 の 4 番目）が逆転の判定を書かせているためと考えられる。
2. **厳しい水準では VQ-4 の EP がほぼ未充填になる（EP-08a・09a とも 23/24）が、同時に VQ-3 の EP も Complete にはほとんど届かない。** そのため逆転の判定は 4/24 にとどまる。「VQ-3 は埋まり、VQ-4 は埋まらない」という非対称は、水準の取り方によって現れたり消えたりする。
3. **「EP-08a/09a は 12 run すべてで undocumented」も再現しない。** Kumada の 12 run のうち、主水準で未充填なのは EP-08a が 5/12、EP-09a が 7/12。
4. これらはすべて **Stage 4 の探索層（LLM-parametric）** の値。本文の非検出の主張を支配するのは locked WoS audit だが、その raw export には重複の問題がある（R3-1）。

## 改稿への提案（2026-09-28 user 承認、本文・SI-3・SI-11 に適用済）

1. 本文（Results Part 2・Part 4）、SI-3、SI-11 の「24/24」と「all 12 runs」を削除し、上の再集計（4 水準の表）に置き換える。「モデルの文章が逆転に触れた 24/24」は、prompt が判定を求めているため証拠にならないと明記する
2. VQ 階層逆転の主張の根拠を、Stage 4 の run 間再現性から外す。根拠として残るのは Kumada の locked WoS audit（R3-1 の再 export 後）と Fig. 2 の充填マップで、主張は「n = 1 の反応系での観察」に戻す
3. 応答書: Referee 3 の「robustness の数値に裏付けがない」を全面的に認め、再集計の方法と結果を示す

---

# R3-3 残り 2: 「11 報すべてで recur」と「4–12 年 / 30–54 年」（2026-09-28）

スクリプト `reaggregate_11papers.py`（`reaggregate_stage4.py` と同じ定義を使う）。出力は `corpus11_labels_per_ep.csv`（110 行）と `corpus11_inversion_per_paper.csv`。

## 対象の 11 報

Phase 2 報告書（2026-05-10）の定義による。開発セット 2 報（Kumada 1972、Murai 1993。EN run 1）と EP-filling-context 9 報（kumada1976b、monnereau2009、breitenfeld2014、cherney2015、molander2016、molken2016、mazet2021、pengfei2024、tamao2002。各 1 run）。
- **この 11 報には review が 2 本（Cherney 2015、Tamao 2002）含まれる。** 本文 Methods 3 は「v18.4 EN corpus（11 報）= 開発セット + case-study set から review（Cherney 2015）を除いたもの」としていて、構成が合わない（別途直す必要がある）
- 開発セット以外は 1 run だけなので、run 間のばらつきは評価できない

## 結果 1: 逆転は 11 報すべてでは起きていない

| 水準 | 逆転 | 強い版 |
|---|---|---|
| **Complete + Partial（主）** | **6/11** | 5/11 |
| Complete のみ | 0/11 | 0/11 |
| Complete + Partial + Indirect | 1/11 | 1/11 |

- 主水準で逆転が成り立つのは Kumada 1972、Murai 1993、kumada1976b、breitenfeld2014、mazet2021、pengfei2024 の 6 報
- 成り立たない 5 報のうち 4 報（cherney2015、molander2016、molken2016、tamao2002）は、VQ-4 の EP が Partial 以上とラベルされている。monnereau2009 は VQ-3 の EP が 1 つも Partial 以上にならない

## 結果 2: 年数

**VQ-3 の充填までの年数**（主水準で充填とラベルされ、Filling Onset に年がある EP、開始年 − 出版年）
- 開始年が出版年以降の 13 件: 0–11 年（中央値 2 年）。Kumada 1972 は 4、4、8 年、Murai 1993 は 1、2、6、11 年
- 残る 7 件は、**開始年が解析した論文より前**（例: molken2016 の EP-06a に、run 自身が「molken2016 に先立つ」と書いて Jarvo 2012 を挙げている）。論文より前の文献は後からの充填ではないため、上の 13 件からは除いた。**この除外は数字を見た後で決めた**
- Onset に挙がる文献は LLM の parametric recall で、`tentative_citation` と注記されたものも多い。書誌は検証していないので、年数は「Stage 4 の run がそう主張している」値であって、文献記録の値ではない

**「30–54 年後も VQ-4 が手薄」**
- 出版から 30 年以上たっている論文は 11 報中 3 報しかない（Kumada 1972 = 54 年、kumada1976b = 50 年、Murai 1993 = 33 年）。残る 8 報は 2–24 年で、30–54 年という記述はそもそも当てはまらない
- この 3 報では、主水準で VQ-4 の EP はどちらも未充填（ラベルは Indirect、none、Attempted など）。Indirect まで含めると、3 報とも VQ-4 のどちらかが「充填」になる

## 読み取れること

1. 「VQ 階層逆転が 11 報すべてで繰り返し現れる」は成り立たない。主水準で 6/11、最も厳しい水準では 0/11。
2. 「4–12 年」は Kumada と Murai の値（1–11 年）にほぼ対応するが、11 報全体の性質ではない。
3. 「30–54 年」が当てはまるのは 3 報だけで、その 3 報でも閾値を Indirect まで下げると成り立たない。

## 改稿への提案（2026-09-28 user 承認、本文・SI-3 に適用済）

1. Results Part 2 の「recurs across all 11 papers of the v18.4 EN corpus (Fig. 3)」を削除し、「主水準で 11 報中 6 報（各 1 run、review 2 本を含む）」と書く。Fig. 3 は Kumada 1972 のみの図なので、この文の出典にしない
2. Discussion 1 の「Within the 11-paper v18.4 EN corpus, mechanistic EPs fill within 4–12 years while … 30–54 years later」を、Kumada 1972 と Murai 1993 に限った記述に直す（VQ-3 の充填は 1–11 年と run が主張しており書誌は未検証、VQ-4 は 33–54 年後も Partial 以上に達しない）
3. Methods 3 の「v18.4 EN corpus」の構成を実際の 11 報に合わせる（review 2 本を含むことを明記）
