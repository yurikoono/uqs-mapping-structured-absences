# Stage 4: EP充填論文の同定と選定マップ生成
<!-- prompt_version: stage4-v6-20260504 -->
<!-- v6 patch (= v19 cycle): Letter→Full auto-resolution (C23) / filling timescale categorization (C24) / constraint-disclosure-impossible (C26) -->
<!-- Source basis: papers/structural_chem_pilot/{watsoncrick1953,hodgkin1969}/STATUS.md (n=2 Dev pair) -->
<!-- Backward compatible: existing 三群分類 / Step 1-2 logic preserved; v6 adds annotations and pattern extensions -->
**Language: 日本語（RI/EP/VQコード・技術用語・論文引用は英語）**

出力の冒頭にプロンプトバージョンを記載すること：
```
prompt_version: stage4-v6-20260504
```

---

## 入力

以下を本プロンプトの前に貼り付けること：
1. **Stage 0出力**（BIB-1〜BIB-8b, S0-1〜S0-7）
2. **Stage 1 Turn 4出力**（A, B, C, U, META, TEMPERATURE_SUMMARY, GAP）
3. **Stage 2出力**（D-1〜E, confirmed_english）
4. **Stage 3出力**（§1〜§6）

主要参照セクション：
- **§2 SRG / CLA → RI / ER / EP Crosswalk**（EP一覧とcase-specific実装）
- **§5 最短補強ルート**（EP投入順序とVQ目的関数）
- **§3 現在のVQ判定**（各VQ水準の通過/未達）
- **§4 Era-Norm Annotation**（当時の許容と現代の不足）

---

## 目的

Stage 3の§5（最短補強ルート）が提示した各EPについて、それを科学史上
実際に充填した（または部分的に充填した）論文を同定し、推奨選定リスト
として構造化する。これにより、UQSが抽出した「語られていない問い」が
後続の科学的発展によってどのように解消されたかを実証的に検証できる。

---

## 出力規律

以下の§A〜§Eの構成に従い、構造化された選定マップのみを出力すること。
説明的散文、フォローアップ質問、次ステップの提案、指定フィールド外の
テキストを付加しない。

**基本姿勢：** 充填論文の同定にはモデルのドメイン知識（学術論文・
研究者・研究グループの知識）を最大限に活用する。知識が不確実な場合は
その旨を明記し（confidence levelで表示）、ハルシネーションを避ける。

---

## 参照体系

Stage 3で使用した以下の体系をそのまま参照する：
- **EPコード体系**: EP-01a〜EP-10a（Stage 3 §2で割り当て済み）
- **RIコード体系**: RI-01〜RI-09, PRI-10（Root-Issue Codebook v0.2）
- **VQ判定基準マトリクス**: VQ-1〜VQ-4（継承原則を含む）

---

## 選定マップの生成手順

### Step 1: §A EP充填難易度の三群分類

**入力：** Stage 3 §2（各EPのcase-specific実装）+ §5（EP投入順序）

Stage 3 §5に列挙された全EPを、充填論文の検出しやすさに基づいて
以下の3群に分類する。

**分類基準：**

| 群 | ラベル | 判定基準 |
|:---|:-------|:---------|
| **第一群** | 文献で明確に追跡可能 | EPが要求する実験が独立した論文の主題として存在する可能性が高い。具体的な実験手法・基質系・測定法が明確であり、文献検索で直接ヒットしうる |
| **第二群** | 間接的に追跡可能 | EPが要求する情報がレビュー論文・教科書・方法論論文の一部として含まれるが、独立論文の主題ではない。または、類似系での実証はあるが対象系そのものでの実証が限定的 |
| **第三群** | 充填が見つからない可能性あり | EPが論文固有の報告形式問題（RI-01）や反復測定慣行（RI-08）に起因し、独立論文として充填される性質ではない。または、分野が体系的に回避してきた問いである可能性 |

**分類手順：**
1. 各EPのcase-specific実装（§2）を参照し、要求される実験の独立論文
   としての存在可能性を評価する
2. EPに割り当てられたRIコードを考慮する：
   - RI-03, RI-06, RI-07 → 第一群候補（機構・境界・類似性の実験的検証は
     独立研究として発表されやすい）
   - RI-05, RI-09 → 第二群候補（定量的裏付けやベンチマーク比較は
     レビュー・総説に含まれやすい）
   - RI-01, RI-08 → 第三群候補（報告形式・反復測定は通常Full Paperへの
     展開時に自動解消されるか、分野慣行として未解消のまま残る）
3. ただし上記はデフォルト傾向であり、case-specific実装の具体性に
   基づいて個別に判断すること（例：RI-01でもFull Paper展開が独立論文
   として存在すれば第一群）

<!-- v18 C6: EP-08a incentive-structural unfilling pattern -->
**第三群の典型パターン①「インセンティブ構造的未充填」（v18追加）：**
統計的信頼性・再現性に関するEP（EP-08a型）は、計算化学・物理化学
分野では「追試」「統計的評価」として独立論文化されにくく、技術的に
可能でも出版インセンティブの不整合により第三群に分類されることが
多い。次に該当する場合は第三群とし、その旨を「インセンティブ構造的
未充填」として明記すること：
- EP-08a（Replication / uncertainty pack）が方法論論文に紐付き、
  対象系での反復測定や統計的有意性評価が独立論文化されていない
- EP-09a（Internal benchmark pack）のうち、原論文の主張を直接
  検証する文脈での追試が見当たらないが、類似系のベンチマークは
  豊富に存在するケース

<!-- v18 C7: Success-driven question erasure pattern -->
**第三群の典型パターン②「Success-driven question erasure」（v18追加）：**
成功した代替アプローチの存在により、元の問いの検証需要自体が社会的に
消滅するパターン。特に合成化学・応用化学分野で観察される。次に該当
する場合は第三群とし、その旨を「成功による問いの抹消」として明記
すること：
- 別アプローチで主目的（全合成、所望の生成物の取得、目標の達成）が
  実現したことにより、原論文の検証対象（生合成仮説、特定経路、
  特定機構）の直接検証需要が消滅
- 充填論文の「不在」そのものが成功の副作用として記録されるべき
  （技術的不能ではなく、社会的・科学コミュニティ的な検証需要の消滅）

例：E,E異性体の全合成成功により、Z,Z前駆体からの生合成カスケード
仮説の直接検証が長期未充填となるケース。

<!-- v6/v19 C26: Constraint-disclosure-impossible filling sub-pattern -->
**第三群の典型パターン③「Constraint-disclosure-impossible」（v6/v19 追加）：**
model-building / structure-proposal paper（新規実験データなし）で reporting
completeness 関連 EP（EP-01a 系）が指摘されている場合、retrospective
disclosure が以下のいずれかにより**物理的に不可能**なケースは
「constraint-disclosure-impossible」と明記し第三群に分類すること：
- 拘束データ source の lab notebooks / 一次資料が散逸 / archival のみ
  アクセス可能（1953 年代の研究 lab data 等）
- 拘束パラメータが論文当時の閉域 communication（book chapter, conference,
  letter to colleagues 等）にのみ存在し、formal publication が無い
- 著者 / 共同研究者 / co-author が物理的に retrospective interview 不可能
  （deceased, archived only）

該当する場合、Stage 4 出力に以下を annotation すること：
```yaml
incentive_structure_type: "constraint-disclosure-impossible"
archival_alternative: "<archival source if any, e.g., CSHL 1953 archives, 著者の retrospective narrative book chapter>"
filling_substitute: "<historical / archival / mini-review が部分代替 — full filling は構造的に不可能>"
```

C6（インセンティブ構造的未充填、計算化学・物理化学 EP-08a/EP-09a 系）は
「インセンティブ不整合」(出版動機を変えれば fill 可能)、本 C26 sub-pattern は
「物理的 retrospective 不可能」(原理的に fill 不可能) と区別する。

例：Watson-Crick 1953 における EP-01a 充填は CSHL 1953 archives + Klug 1968
retrospective narrative の partial 代替で観測される — full filling は
拘束データ一次資料の散逸により構造的に不可能。

<!-- v6/v19 C23: Letter→Full Paper auto-resolution / within-issue companion pattern -->
**第二群の典型パターン①「Letter→Full Paper auto-resolution / within-issue
companion」（v6/v19 追加）：**
論文形式が Letter / Communication / 短報であり、reporting completeness
関連の EP（EP-01a 系）が指摘されている場合、以下を確認：
- 同一著者グループの Full Paper / Article 形式の続報が 1〜3 年以内に
  存在するか（Blundell 1971/1972, Watson-Crick 1953b 等）
- 同号（within-issue companion）に同一 phenomenon を独立 evidence で扱う
  論文が存在するか（Wilkins 1953 + Franklin & Gosling 1953 同号 等）

該当する場合、当該 filling 候補に以下の annotation を付加：
```yaml
auto_resolution_type: "Letter→Full Paper" | "within-issue companion" | "conference→journal"
expected_resolution_window: "1-3 yr"
auto_resolution_status: "occurred" | "promised" | "not_observed"
filling_timescale_category: "format-driven"
```

`auto_resolution_status: occurred` の場合（Blundell 1971/1972 のような実例）
は Stage 3 §5（最短補強ルート）の対応 EP に「format-driven auto-resolved」を
明記すること。`promised`（論文中で "details to be reported" 等の言及あり、
Full Paper 未確認）と `not_observed`（Full Paper 続報が文献上見当たらない）
は別扱い。

本パターンは Letter / Communication / 短報のみで発火する設計であり、
Full Article / regular paper では skip して "C23 trigger: not applicable
(non-Letter format)" と明記する。

**出力形式：**
```
**第一群（文献で明確に追跡可能）：** EP-XXa, EP-YYa, ...
  — [各EPについて第一群と判定した根拠を1文ずつ]

**第二群（間接的に追跡可能）：** EP-XXa, EP-YYa, ...
  — [各EPについて第二群と判定した根拠を1文ずつ。Letter→Full Paper
    auto-resolution（C23）に該当する場合はその旨を明記]

**第三群（充填が見つからない可能性あり）：** EP-XXa, EP-YYa, ...
  — [各EPについて第三群と判定した根拠を1文ずつ。インセンティブ構造的
    未充填、成功による問いの抹消、または constraint-disclosure-impossible
    （C26）に該当する場合はその旨を明記]
```

---

### Step 2: §B 各EPの充填論文候補の同定

**入力：** §Aの三群分類 + Stage 3 §2（case-specific実装）+ §5 +
モデルのドメイン知識

**検索方法論：**
充填論文の同定は、被引用件数や原論文との表面的類似性ではなく、
**EPのcase-specific実装から検索語を逆算する**アプローチで行う。

手順：
1. 各EPのcase-specific実装（§2）から、実行されるべき実験の
   具体的内容（基質・分析法・測定対象）を抽出する
2. その実験内容を検索語に変換する（例：EP-03aの「NiCl₂(dpe)系の
   中間体の分光学的同定」→ "nickel diphosphine intermediate
   characterization spectroscopic"）
3. モデルのドメイン知識を検索語に適合する論文の同定に活用する
4. 高被引用論文は充填論文の候補ではなく、原論文の手法を「使った」
   応用論文である可能性が高いことに注意する。充填論文は、原論文の
   EPに対応する実験を実施した論文であり、原論文を引用すらして
   いない場合がある

第一群・第二群の各EPについて、以下のテンプレートで充填論文候補を
同定する。第三群についても、部分的な充填や関連する発展があれば記録する。

**同定の基本原則：**
- **充填開始点（Filling Onset）**: そのEPに対応する実験・データを
  最初に提供した論文。部分的な充填でもよい。
- **充填確立点（Filling Establishment）**: 充填が決定的になった論文。
  EPが要求する実験的証拠を本質的に提供している。
- 両者が同一論文の場合は1エントリにまとめる。
- **原著者グループの自己充填**: 原論文の著者グループ自身が後続論文
  （Full Paper、続報）でEPを充填するパターンは特に注視する。
  通信→Full Paper遷移での自動解消パターンを含む。

**各EP候補のテンプレート（v18.3 改訂）：**
```
**EP-XXa [共通ラベル]（第N群）**

* **充填するRI**: RI-XX [Label]
* **充填開始点**: [著者名 et al., 雑誌名 年, 巻号ページ] — [1文で充填内容を記述]
* **充填確立点**: [著者名 et al., 雑誌名 年, 巻号ページ] — [1文で充填内容を記述]
  （充填開始点と同一の場合: 「同上」）
* **充填の性質**: [以下から選択]
  - Complete: EPの要件を実質的に完全に満たす
  - Partial: EPの要件の一部を満たすが、残存する未充填要素がある
  - Indirect: 対象系そのものではなく類似系での充填
  - Attempted: EPの方向に進んだが、充填論文自体のデータ信頼性
    （VQ水準）が不十分であり、充填として機能しない
  - Paradigm-shift: 原論文の枠組みそのものを置換する新パラダイムに
    よって、EPの前提が変化した（EPが解消されたのではなく、
    問いの枠組みが変わった)
<!-- v18.3 C17: split confidence into bibliographic + filling adequacy -->
* **Bibliographic confidence**: [High / Medium / Low]
  - High: 著者名・年・雑誌・巻号ページが完全に特定でき、DOI が同定可能
  - Medium: タイトルと著者の組合せに confidence あるが正確な巻号は推測
  - Low: 「〜前後」「〜系列」「あるいは関連レビュー」等の hedged prediction
* **Filling adequacy confidence**: [High / Medium / Low]
  - 書誌の存在を仮定した上で、EP の case-specific 実装を満たすかへの confidence
  - High: 論文の内容が EP の要件を直接満たすことが文書から明らか
  - Medium: 論文の内容と EP との対応に推論を含む
  - Low: 関連論文だが EP 充填との具体的対応が不明確
<!-- v18.3 C17: conditional verification recommendation -->
* **Verification recommendation**: [必須 / 推奨 / 省略可]
  - 判定ルール（v18.3 で導入、conditional triggering）：
    [必須] 以下のいずれかに該当する場合：
      (a) 論文年代が古い（1980 年以前）
      (b) 著者ネットワークが密（同一研究グループから 10+ の関連論文がある場合）
      (c) 反応名が author name に由来する命名規則を持つ
          （Wittig / Diels–Alder / Sandmeyer / Claisen 等の named reaction）
      (d) Sonnet が Confidence: Medium-Low の予想を含む論文を 2 件以上リスト
    [推奨] 単一要因を含む場合（1990 年代の論文 + 著者ネットワーク 5-10 報、
           Communication-Full Paper 自動充填の核心論文 等）
    [省略可] 上記いずれにも該当せず、全候補が High Bibliographic confidence
  - [必須] のエントリは post-hoc verification step（§B 末尾の Step 4）まで
    final selection として扱わない
* **DOI / URL（任意）**: [可能であれば DOI を記載。Verification recommendation
                         が [必須] の場合は推奨記載]
<!-- v6/v19 C24: filling timescale categorization -->
* **Filling timescale category（v6/v19 追加）**: [以下から選択]
  - **format-driven (1-3 yr)**: Letter→Full Paper 自動解消、within-issue
    companion paper、conference→journal 遷移等。論文形式の変化が driving force。
  - **field-methodology (2-5 yr)**: 分野全体の方法論的応答（新 protocol の
    field-wide adoption、新解析手法の流行、新測定技術の普及等）が driving force。
  - **technical-barrier (10-20+ yr)**: 分解能・instrumentation・理論的計算能力
    barrier の解消が driving force。Hodgkin 1969 → Baker 1988（19 年）型。
  - **incentive-aligned (variable)**: 上記 3 category に該当しないが標準的な
    時間スケールで充填されたケース（5-10 yr 程度の競争的応答等）。
  - **non-applicable**: 第三群の constraint-disclosure-impossible 等で
    timescale を意味のある形で割り当てられないケース。
* **注記**: [追加情報。例：同一論文が複数EPを充填する場合の相互参照、
  充填までの年数、充填の文脈（なぜこの研究が行われたか）、Layer asymmetry
  との関係（Stage 2 v19 C22 出力を参照、Layer 1 充填と Layer 2 充填が
  異なる timescale category に属する場合はその不一致を記述）等]
```

**同定のガイドライン：**
1. 原論文の発表年（BIB-4）以降の文献を対象とする
2. 同一EP内に複数の充填候補がある場合、最も決定的な1-2報に絞る
3. 同一論文が複数のEPを充填する場合（バンドル充填）は、各EPの
   エントリで相互参照する
4. 充填論文が見つからない場合は「**未同定**」と記載し、その理由を
   1-2文で記述する
5. **レビュー論文はEPを充填しない。** レビュー論文は既存データを
   体系化するが、新しい実験的証拠を提供しない。レビューは充填論文
   ではなく、充填論文を特定するための二次情報源として使用する。
   ただし、レビューに含まれるメタ分析や独自の定量的再評価が
   EPの要件に直接対応する場合は例外として記載し、その旨を注記する
6. **充填論文は自らを「充填」と宣言しない。** EPを充填する論文は、
   原論文の不在を埋めることを目的として書かれているわけではない。
   異なる文脈・異なる目的で書かれた論文の実験内容が、EPの要件を
   構造的に満たしているかどうかを判定する操作（証拠的相補性の
   検出）が必要である。表面的な主題の類似性ではなく、EPの
   case-specific実装との対応関係で充填を判定すること

<!-- v18.3 C17: Bibliographic verification sub-step within §B -->
**§B 末尾チェック：Bibliographic verification（v18.3 追加、conditional triggering）**

§B で同定した全充填論文候補について、以下のチェックリストを実施する：

1. **トリガー条件の評価（論文単位）**：
   - (a) 論文年代が古いか（1980 年以前）
   - (b) 著者ネットワークが密か（同一研究グループから 10+ の関連論文がある）
   - (c) 反応名が author name に由来する命名規則を持つか
        （Wittig / Diels–Alder / Sandmeyer / Claisen / Michael / Friedel–Crafts 等）
   - (d) Bibliographic confidence Medium-Low の候補が 2 件以上含まれるか

2. **Verification recommendation の付与**：
   - 上記 (a)(b)(c)(d) のいずれかに該当 → 全候補に [必須]
   - 単一要因のみ該当（例：1990 年代の論文 + 著者ネットワーク 5-10 報）→ [推奨]
   - いずれにも該当せず、全候補が High Bibliographic confidence → [省略可]

3. **必須 verification の場合の出力要件**：
   - 各候補に DOI または書誌情報（Crossref で検索可能な形式）を付記
   - 「**Bibliographic verification status**: [pending / verified / hallucination_warning]」
     フィールドを追加（実行時は通常 pending、post-hoc 検証で更新）
   - §C 推奨選定リストでは、verification status: pending のエントリは
     「⚠️ verification 待機中」として明示

4. **Hallucination 警告例（既知パターン）**：
   - **著者組合せ捏造**: 同一研究グループの異なる論文の著者を混合する
     （個々の著者名は実在するが、その組合せの論文は存在しない）
   - **架空の coauthor**: 該当 corpus に含まれない著者を追加する
   - **chemistry 内容の誤記**: 書誌は概ね正しいが、触媒金属・配位子・
     反応型などの化学的内容を誤って記述する

5. **post-hoc verification の推奨手順**：
   - Crossref API（https://api.crossref.org/works/{DOI}）で書誌情報を確認
   - 著者リストの完全一致を検証（順序・スペル）
   - タイトルから論文の内容を推定し、EP との対応関係を再評価
   - hallucination が検出された場合、論文を選定リストから除外し再検索

**根拠**: cross-model 検証により、parametric retrieval の hallucination 率が
paper-dependent であることが確認されている。conditional triggering によって
検証コストをリスクに比例して配分する。

---

### Step 3: §C 推奨選定リスト

**入力：** §Bの充填論文候補

§Bで同定した充填論文候補から、EP充填検証に最適な5-7報の推奨
選定リストを作成する。

**選定基準（優先順、v18.3 改訂）：**
1. **EP充填のカバレッジ**: より多くのEPを充填する論文を優先
2. **充填の決定性**: Completeな充填 > Partial > Indirect
3. **VQ階層の階段状カバレッジ**: VQ-2要件、VQ-3要件、VQ-4要件の
   各層から少なくとも1報ずつ含む
4. **年代の多様性**: 充填の時間的展開を検証するため、可能な限り
   異なる年代の論文を選ぶ
5. **Filling adequacy confidence**: High > Medium。Lowの論文は原則として
   選定リストに含めない（§Bの候補欄には記載可）
6. **Bibliographic confidence**（v18.3 追加）: Verification recommendation
   が [必須] のエントリは、Bibliographic verification 完了まで「⚠️ verification
   待機」として明示する。verified 後に正式な選定リストへ昇格

**出力形式（v18.3 改訂）：**
```
| 順序 | 論文 | 充填するEP | VQ水準 | 年代 | Bib.Conf | Fill.Conf | Verification |
|------|------|-----------|--------|------|----------|-----------|--------------|
| 1 | [著者 et al., 雑誌 年, 巻号ページ] | EP-XXa, EP-YYa | VQ-N | YYYY | High/Med | High/Med | 必須/推奨/省略可 |
| ... | ... | ... | ... | ... | ... | ... | ... |
```

選定理由を表の後に1-2段落で記述する。バンドル充填（1論文が複数EP
をカバー）がある場合はその効率性を明記する。

Verification recommendation [必須] のエントリは、§B の Bibliographic
verification sub-step に従い post-hoc 検証を経るまで「⚠️ pending
verification」として表記する。verified 後に通常表記に切り替える。

---

### Step 4: §D VQ階層と充填時間順序の対応分析

**入力：** §Cの推奨選定リスト + Stage 3 §3（VQ判定）

推奨選定リストの論文を発表年順に並べ、VQ階層との対応を分析する。

**分析の枠組み：**

1. **時間順マッピング**: 各充填論文の発表年とそれが充填するVQ水準を
   対応づけ、「VQ-N要件がY年に充填された」という時間軸を構築する
2. **階層-時間仮説の検証**: 以下の仮説を検証する：
   > 「VQ階層が上がるほど、充填に要する時間が長くなる傾向がある。
   > これはVQ階層が科学の発展の難易度構造を反映しているためである。」
   - 支持する証拠があれば記述する
   - 反例があればそれも記述する
3. **充填パターンの分類**: 以下のパターンのうち該当するものを記録する：
   - **自己充填**: 原著者グループによる後続論文での解消
   - **技術駆動充填**: 新しい分析技術・計算手法の登場による解消
   - **分野横断充填**: 異なる研究分野からのアプローチによる解消
   - **パラダイム転換充填**: EPの前提となる枠組みが変わることで
     問い自体が再定義された（充填というよりsuccession）
   - **長期遅延充填**: 原論文から20年以上を経た充填
   <!-- v18 C7-related: precedent filling pattern -->
   - **先行充填（v18追加）**：原論文より時間的に先行する論文によって
     EPの内容が既に充填されていたパターン（例：Doering–Roth 1962 が
     W-H 1965 のEP-06aを3年先行充填）。原論文は「既に充填されていた
     問いへの理論的枠組み」として機能する
   - **分割提示充填（v18追加）**：原論文が「Paper I（理論）」として
     自己位置付けし、続報「Paper II（数値実証）」が同一著者グループ
     から発表されることで充填されるパターン
   - **未充填**: 現在まで充填されていない（§Eで扱う）
4. **著者回顧との照合（該当する場合）**: 原著者自身が後年の
   回顧（レビュー、retrospective、ノーベル講演等）で言及した
   「特徴」や「成果」のリストと、Stage 3のEPリストを照合する。
   著者が回顧で認識したEPと認識しなかったEPの差は、「分野の
   内部者には不可視の構造的不在」の直接的な証拠として記録できる

**出力形式：**
```
**充填の時間軸：**
- VQ-N 要件: EP-XXa → [年] [著者] [充填パターン]
- VQ-N 要件: EP-YYa → [年] [著者] [充填パターン]
...

**階層-時間対応の評価：**
[仮説の支持/不支持に関する2-3文の分析]

**特筆すべきパターン：**
[長期遅延充填、バンドル充填、自己充填等の特筆事項]
```

---

### Step 5: §E 未充填EPの発見的意義

**入力：** §B（未同定EP）+ §D（未充填パターン）

§Bで充填論文が未同定、または§Dで未充填と判定されたEPについて、
その科学史的意義を記述する。

**分析の観点：**
1. **未充填の理由**: なぜ充填されなかったのかを推定する
   - 技術的困難（実験的に不可能または極めて困難）
   - 分野慣行（その種の実験は慣例的に行われない）
   - 報告形式問題（通信→Full Paper遷移で部分解消されたが完全ではない）
   - 関心の欠如（科学コミュニティがその問いに関心を持たなかった）
   - **インセンティブ構造の不整合**（充填に必要な実験は技術的に可能
     だが、その実験を独立論文として出版するインセンティブが存在しない。
     例：既存系の追試、反復測定、基質マッチドベンチマーク比較は、
     新規性を要求する出版慣行のもとで論文化されにくい）
   <!-- v18 C7: success-driven erasure as unfilling reason -->
   - **成功による問いの抹消（Success-driven question erasure、v18追加）**：
     代替アプローチの成功によって、原論文の検証対象（仮説、経路、
     機構）への直接検証需要が社会的に消滅したパターン。技術的には
     可能だが、検証する動機が失われている
   <!-- v18: long-term unfilling via success obviation -->
   - **理論的成功による検証需要消失（v18追加）**：理論的・方法論的
     成功が後続世代への影響力を獲得した結果、原論文時点の経験的検証
     （実験データ、統計的評価）の需要が消滅したパターン。1960年代の
     基礎理論論文（Fukui 1952、W-H 1965等）で50〜74年の超長期未充填
     として観察される
2. **UQSの発見としての価値**: 「分野がN年にわたって体系的に避けてきた
   問い」として記録できるかを判定する。記録できる場合、その発見的
   意義を1-2文で記述する
3. **将来の充填可能性**: 現代の技術・方法論で充填可能かを評価する
4. **VQ階層逆転の診断**: 未充填EPが低VQ要件（RI-01, RI-08, RI-09）に
   集中し、充填済みEPが高VQ要件（RI-03, RI-06, RI-07）に集中する
   パターンが見られる場合、これは「科学的論理に基づくEP充填順序
   （低VQ→高VQ）」と「出版インセンティブに基づく実際の充填順序
   （高VQ→低VQ）」の逆転として記録する。この逆転パターンは、
   分野のインセンティブ構造がUQSの構造的不在の一部を維持している
   ことの証拠となる

**出力形式：**
```
**未充填EP一覧：**

EP-XXa [共通ラベル]:
* **未充填の理由**: [上記カテゴリから選択 + 1-2文の説明]
* **発見的意義**: [あり/なし。ありの場合は1-2文]
* **将来の充填可能性**: [高/中/低 + 1文の根拠]
```

未充填EPがない場合は「全EPについて充填論文が同定された」と記載する。

---

## 出力形式

```
prompt_version: stage4-v6-20260504
model_info: <model name and version>

# EP充填選定マップ

## [論文著者名] [年]（[BIB-3] [BIB-7]）

### §A EP充填難易度の三群分類
[三群分類の出力]

### §B 各EPの充填論文候補
[各EPのテンプレート]

### §C 推奨選定リスト
[5-7報の選定表と選定理由]

### §D VQ階層と充填時間順序の対応分析
[時間軸、階層-時間対応、特筆パターン]

### §E 未充填EPの発見的意義
[未充填EP一覧または「全EPについて充填論文が同定された」]
```
