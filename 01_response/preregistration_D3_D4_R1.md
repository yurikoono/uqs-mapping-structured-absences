---
title: Paper A R1 — D3 held-out 評価と D4 単一 prompt baseline の事前登録
created: 2026-09-29
status: active
audience: paperA
open_questions: false
---

# 事前登録: D3（held-out）/ D4（単一 prompt baseline）

**凍結**: 本 file を commit した時点で凍結する。以後の変更は末尾の「変更記録」に日付と理由を添えて追記するだけとし、
本文は書き換えない。どの run もこの commit より後に実行する。設計の経緯は `D3_D4_design_proposal_20260929.md`。

**決定（2026-09-29、小野）**: 設計案の推奨どおり。D3 = 案 D3-A、D4 = B0 と B1 の 2 arm、
D3・D4 の出力を D1(b) の blind 評価材料に含める、成功の定義は下記の案のとおり。

## 0. 共通の凍結構成

- model: `claude-sonnet-4-6`（CLI `claude -p --model claude-sonnet-4-6`）。
  各 run の model は CLI の JSON 出力（`modelUsage`）で確認し、4.6 以外を含む run は破棄して再実行する。
  破棄した run も件数を報告する。
- UQS arm: S0–S2 = `prompts/v184/`（S0、S1 turn1–4、S2 EN = `prompt_stage2_v184_en.md`）、
  Stage 3 = `prompts/stage2f3/prompt_stage3_v2_en.md`（hash は SI-7 に一致する `b1358ff4…`）。
  pilot 変種（`*textbook*`）は使わない。
- 各 run は独立した fresh process とし、S0→S2 は単一 context で実行する（Paper A の手順）。
- production registry に記録するが、`notes` に `paperA_R1_prereg` を付けて corpus の解析と区別する。

## 1. D4 — 単一 prompt baseline

### 1.1 対象と反復

- 論文: Kumada 1972（`papers/dev/kumada/Kumada_1972.pdf` の 3 報のうち真ん中の報）。
- arm: B0、B1 をそれぞれ N = 5。UQS 側は既存の `papers/dev/kumada/repro_2026-07/` の
  v18.4 N = 5（run1–5）を使い、再実行しない。
  この 5 run の Stage 2 は `prompt_stage2_v184.md`（D-4 と E を日本語で書く版）で実行されている（`repro_driver.sh`）。
  canon の regex は日本語の語も含むので loose 計器はそのまま適用できる。特定性の採点は D-4 を英訳せずに日本語のまま行う。
- 出力先: `papers/dev/kumada/baseline_R1_2026-09/kumada_bl{0,1}_sonnet46_run{k}.md`。

### 1.2 prompt（逐語。対象論文の特定文は UQS の再現実験と同じ文を使う）

共通の前置き（B0・B1 とも）:

```
TARGET PAPER: papers/dev/kumada/Kumada_1972.pdf is a JACS page carrying THREE communications.
The target is the MIDDLE one: Tamao, Sumitani & Kumada, "Selective Carbon-Carbon Bond Formation
by Cross-Coupling of Grignard Reagents with Organic Halides. Catalysis by Nickel-Phosphine
Complexes." Read the PDF and analyse only that communication.
```

**B0（素朴）**:

```
List the questions this paper leaves unanswered and the claims it does not fully support.
For each item, give (1) the question or unsupported claim, (2) what evidence would be needed to
resolve it, and (3) a verbatim quotation from the paper that anchors the item, on its own line as
key_quote: "<exact text from the paper>".
Return only the list, in Markdown.
```

**B1（定義つき）**: B0 の本文の後に次を加える。

```
Classify each item into exactly one category:
A (deferred): the paper sends the issue to future work, or raises a question and closes without
  resolving it; the gap would disappear if a follow-up paper resolved it.
B (trace of rejection): approaches, conditions, substrates or interpretations the authors
  explicitly negated, limited or set aside in this work; descriptive of this experiment's boundary.
C (uncontinued citation): a prior work cited but never substantively engaged.
U (unclassified): analytically important but fitting none of A/B/C.
Then list same-root groups: items from your list that derive from the same underlying absent data
or methodological gap (factual grouping only).
```

定義文は v18.4 turn4 の A/B/C/U・same-root group の定義を 1〜2 文に要約したもの。

### 1.3 エンドポイント

1. **benchmark 7 軸の被覆（主）**: `papers/dev/kumada/repro_2026-07/canon.json` の regex を、各 run の出力全文に適用する
   （= loose 計器）。UQS 側は s1+s2 の全文に適用する（Paper A Methods 6 の loose と同じ）。
   run ごとの被覆数（0–7）を arm ごとに平均・範囲で報告する。strict 計器は UQS の taxonomy 形式を前提にしているため
   baseline に適用できず、比較には使わない。
   - **keyword proxy の確認**: miss となった (run, 軸) を全件、人が読む。言い換えで同じ所見を述べていれば
     「proxy miss」として別掲し、主の値は regex のまま変えない。
2. **原典への anchor**: `scripts/verbatim_quote_gate.py` の PASS / WARN / FAIL の件数と率。FAIL と、弱い partial match
   （Methods 6 と同じ扱い）は人が照合して、「原典に実在（図表など text layer 外）」と「原典を正確に伝えていない」に分ける。
3. **要求の特定性（副）**: 各項目が、それを閉じる証拠を具体的に指定しているか（2 値。
   「具体的」= 測定・実験・データの種類が特定されている。例:「収率の再現性データ」は具体的、「さらなる研究」は具体的でない）。
   UQS 側の採点単位は S2 の D-4 候補とする。採点者は 2 名（小野と、AI panel 1 名）で、Cohen の κ を報告する。
4. **記述量**: 項目数。

**計器の偏りの開示**: canon の 7 軸は UQS の Kumada 解析から作ったものなので、エンドポイント 1 は UQS に有利に働きうる。
これを本文と応答書で明記する。補いとして、canon 外の所見のうち baseline だけにあるもの（UQS の N = 5 のどの run の全文にも
現れないもの）を人が列挙して報告する。

**解釈の規則**: 検定はしない（N = 5）。範囲が重ならない差だけを「差がある」と書き、それ以外は記述にとどめる。
baseline が UQS と同等以上だった場合も、そのまま報告する。

## 2. D3 — held-out 評価

### 2.1 母集団と適格条件

母集団: Heck 反応の研究論文（題名か要旨に "Heck" を含む）。`corpus/corpus_paper_list.csv` と、追加の検索
（Crossref の `query.bibliographic=Heck`、`from-online-pub-date:2026-02-01`）の結果を合わせる。

適格条件（すべてを満たすもの）:

1. Crossref の `published-online`（無ければ `published-print`）が **2026-02-01 以降**
   （Sonnet 4.6 の training-data cutoff = 2026-01 より後）。
2. refinement set 10 報、dev 2 報、および registry に既に解析がある論文と重複しない。
3. 研究論文である（review、correction、erratum、expression of concern、editorial を除く）。
4. 題名か要旨で Heck 型のカップリング（Mizoroki–Heck、aza-Heck、Heck–Matsuda、oxidative Heck を含む）が主題であり、
   単に言及しているだけではない。判定は題名と要旨のみで行い、本文は見ない。
5. 本文 PDF を入手できる。SI があれば SI も入手する。SI が無いことは除外理由にしない。

### 2.2 選び方

適格な論文を DOI の辞書順に並べて 1 から番号を振り、`random.Random(20260929).sample(range(1, n+1), 4)` で 4 報を選ぶ。
選んだ論文の PDF が入手できない場合は、同じ乱数列の次の番号で補う（補った事実を報告する）。
適格な論文が 4 報に満たない場合は全件を使い、報数を報告する（検索の窓は広げない）。
category の偏りは選び直さずに報告する。

### 2.3 実行

各論文 N = 1。S0→S1 turn1–4→S2 EN を単一 context で実行し、続けて Stage 3 v2 EN を実行する。Stage 4 は行わない
（2026 年の論文には充填側の記録期間がないため）。出力先: `papers/paperA_heldout_R1/{paper_id}/`、命名 infix は `_v184_sonnet46_`。

### 2.4 エンドポイント

1. **構造の完全性**: S1 の A/B/C/U 分類と same_root_groups、S2 の D-4 と E 節、S3 の SRG と EP 辞書がすべて存在すること
   （見出しと必須 field の機械 check。check script は run の前に書いて commit する）。
2. **原典への anchor**: quote gate の件数と率。FAIL と弱い partial match は D4 と同じ手順で人が照合する。
3. **件数**: A/B/C/U、SRG、D-4、EP の件数。Kumada の v18.4 N = 5（平均 ± SD）と並べて記述するだけにする。
4. **EP の形式的妥当性**: 各 EP が、要求する証拠の class と、本文への anchor（key_quote か節の参照）を持つこと。

**成功の定義**: 選ばれた全論文で 1 と 4 を満たし、かつ 2 で「原典を正確に伝えていない」と判定された引用が 0 件であること。
満たさなかった場合も結果をそのまま報告し、Results Part 4 の文言を結果に合わせて書く。

## 3. D1(b) への受け渡し

D4 の B0・B1 各 1 run（run1）、UQS の repro run1、D3 の出力から、評価用の項目一覧を作る。
項目は出所を伏せ、形式を揃え（番号・分類記号・内部 ID を除き、「問い + 必要な証拠」の 2 文に揃える）、
並びを乱数で混ぜる。この手順の詳細は D1 の評価設計で別に事前登録する。

## 変更記録

- **2026-09-29（実行後）**: D4 endpoint 2 はどちらの引用種別（`key_quote` か、その他の引用符付き文字列か）を数えるかを
  指定していなかった。両方を報告し、`key_quote` 同士を同種比較の行とする。
- **2026-09-29（実行後）**: endpoint 1 の regex には既知の誤検出がある（`Ni\(0\)` と `radical`。2026-07-27 に内部で記録済み）。
  事前登録した値はそのまま報告し、事前登録外の補助として、全 arm に同じ条件で絞った pattern をかけた結果と、
  （承認されれば）軸ごとの定義文に基づく人手判定を加える。いずれも事前登録外と明記する。
- **2026-09-29（D3 実行中）**: §2.4 の「check script は run の前に書いて commit する」を守れず、run の開始後に書いた
  （`d3_heldout/check_heldout.py`）。書いた時点で出力を見ていたのは wang2026 の S0 のみ。基準は出力ではなく各 prompt の
  出力形式（S1 turn4 の item 形式と META、S2 EN の D-1〜E 見出し、S3 v2 EN の §1〜§6 と SRG/CLA template）から取った。
  EP の anchor は「block 内に item_id（A-/B-/C-/U-n、V*-Q*）または頁・表・図・Scheme・SI の参照がある」と操作化した。
- **2026-09-29（Fable 5.1 査読 F1・F3 を受けて追記）**: 次の 3 点は、データを見た後に決めた、または事前登録の順序を守れなかった点である。
  1. **D3 endpoint 4 の判定を、全 run の完了後に緩めた。** 最初に commit した check script（40c1747、09:48）は、
     Step 2c template の 4 欄（Primary RI、ER、`**EP**:`、case-specific implementation）がすべての block にあることを要求していた。
     これを 4 報の生出力に適用すると PASS は 1/4（shekarizadeh2026 のみ）である。全 run の完了後（f0a60eb、09:54）、判定を
     「EP の class と、item ID または頁・表の参照があること」に置き換えて 4/4 とし、この変更をここに書かなかった。
     item ID による anchor はほぼ常に満たされるため、置き換えた判定は事前登録の文言（「key_quote か節の参照」）より緩い。
     → 事前登録の文言に戻して再判定する（下記「D3 endpoint 4 の再判定」）。template の 4 欄の結果（1/4）も併記する。
  2. **D4 の人手判定の狭義・広義 2 段は、arm ごとの絞り込み pattern の結果（d38ad6b、08:53）を見た後に設計した**（rubric の commit は 057a296、09:23）。
     広義は 2026-07-19 の元の定義の文言そのもので、狭義は 2026-07-27 の再解釈を操作化したもの。どちらもデータを見た後の選択である。
  3. **D3 の driver（`run_heldout.py`）の commit は run の開始（09:22）より後**（057a296、09:23）だった。driver の prompt 本文は run の出力の
     `_*_cli.json` に残る呼び出しと同一。

## 追加 arm B2（出力量を揃えた baseline）— 2026-09-29、実行前に登録

**理由**: Fable 5.1 査読 F6。UQS の loose scope（s1+s2）は約 4.8〜5.9 万字、B0/B1 は約 1 万字である。「run のどこかに現れる」という基準は
出力量が多いほど有利なので、多段構成の効果と出力量の効果を分けられない。B2 はこの交絡を切り分けるための対照とする。

**prompt**: B1 の本文（共通の前置き + B0 + B1 追加文、`prompt_bl1.txt` と同一）の後に、次の文を加える。UQS の観点
（脚注・実験の項・表を見よ、など）は加えず、分量と網羅性だけを指示する。

```
Be exhaustive. Produce a long and thorough list: aim for at least 40 items and at least 45,000 characters in total.
Do not stop early; keep going until you have covered everything you can find.
```

**実行**: Kumada 1972、N = 5、Sonnet 4.6、各 run は独立の fresh process。出力は `papers/dev/kumada/baseline_R1_2026-09/kumada_bl2_sonnet46_run{k}.md`。
出力が 45,000 字に届かなくても再実行はせず、実測の字数を報告する。

**エンドポイント**: §1.3 と同じ。加えて出力の字数を報告する。benchmark 7 軸は、`adjudication_rubric_20260929.md` の同じ基準
（狭義・広義、loose scope）で判定する。判定者は B2 の 5 run と、既存 15 run の再判定分をまとめて、新しい独立の判定者 2 名とする。
今回は各判定者に別々の作業 directory を指定し、全 snippet を読むよう求める（F4 への対応）。

**解釈**: B2 が UQS との差を縮めれば、差の一部は出力量によるものとする。縮めなければ、差は出力量だけでは説明できないとする。
どちらの結果でも、そのまま報告する。

