```
prompt_version: stage4-v1-20260416
model_info: claude-sonnet-4-6

# EP充填選定マップ

## Race et al. 2016（Chemical Science, full_paper）

### §A EP充填難易度の三群分類

**第一群（文献で明確に追跡可能）：** EP-07a（SRG-2）, EP-03a（SRG-5）, EP-07a（SRG-6）

  — **EP-07a（SRG-2）**: Pd-free / 遷移金属フリー条件でのiminyl radical生成実験は、独立した方法論的関心をもつ論文の主題として存在しやすく（Leonori photoredoxグループ等）、文献検索でヒット可能性が高い。
  — **EP-03a（SRG-5）**: p-cymene系での明示的なアリールC–H活性化確認実験は、aza-Heck Full Paperへの展開時に著者グループ自身が実施する可能性が高く、自己充填パターンで追跡可能。
  — **EP-07a（SRG-6）**: matched-pair実験（同一O-acyl基・配位子違いのみ）は合成手法論文の比較実験として独立発表されやすいが、実際には未実施の可能性が高く、「不在の証拠」として追跡価値がある。

**第二群（間接的に追跡可能）：** EP-03a（SRG-4）, EP-04a（SRG-3）, EP-09a（CLA-2）

  — **EP-03a（SRG-4）**: Pd(0)/配位子系のSET熱力学（酸化電位・CV）は、触媒化学のレビューや計算化学論文の一部として含まれやすいが、この特定の反応系を主題にした独立論文は限定的。
  — **EP-04a（SRG-3）**: Newcombのラジカル時計速度定数は参照文献（refs 19a/19b）として存在するが、本系への定量的抽出・適用は独立論文の主題になりにくく、レビューや補足情報の中で言及される形が主。
  — **EP-09a（CLA-2）**: iminyl radicalの各手法比較ベンチマークはレビュー論文・総説に含まれやすく、独立した一次論文としての充填は間接的。

**第三群（充填が見つからない可能性あり）：** EP-08a（SRG-1）

  — **EP-08a（SRG-1）**: B-1の反復測定欠如・不確かさ記述欠如はRI-08（報告形式慣行）に起因し、communication→Full Paper遷移で部分的に解消されるが、合成化学分野では反復測定を独立論文として発表する慣行がなく、完全充填は構造的に困難。

---

### §B 各EPの充填論文候補

**EP-07a [Boundary-test pack]（SRG-2）（第一群）**

* **充填するRI**: RI-07 [Unsupported boundary]
* **充填開始点**: Bower group Full Paper, Chemical Science または JACS, 推定2017–2020 — 「電子豊富Pd触媒を用いたiminyl radical生成のaza-Heck通信論文のFull Paper展開」として、Pd-free/Cu系等での同一基質試験を含む可能性がある。
* **充填確立点**: 同上（Full Paperが実施されていれば同一論文）
* **充填の性質**: Partial — Full Paper展開では配位子スクリーニングの拡張は期待できるが、「Pd以外の金属でもiminyl radicalが生成するか」の境界テストが明示的主題になるかは不確実。
* **Confidence**: Medium — Bower研究グループの後続論文は高い確信で存在するが、EP-07a（SRG-2）の要件（Pd-free条件）との対応は推論を含む。
* **注記**: 文献検索推奨クエリ：「Bower AND iminyl radical AND palladium」（Web of Science）。Leonori (Oxford) グループのPhotoredox-iminyl radical系論文もPd-free充填として機能しうる（ただし異なる化学系）。

---

**EP-03a [Direct-observation / state-assignment pack]（SRG-5）（第一群）**

* **充填するRI**: RI-03 [Unobserved explanatory]
* **充填開始点**: Bower group Full Paper（上記と同一の可能性あり）— p-cymene部位へのアリールC–H活性化が「証拠」か「副産物」かを明示した実験を含む可能性。
* **充填確立点**: 同上
* **充填の性質**: Partial — p-cymene試験そのものは確認されても、imino-Pd(II)中間体の直接観測（EPの完全要件）はFull Paperでも省略される可能性が高い。
* **Confidence**: Low — Full Paperでp-cymeneデータが明示的に報告されるかは不確実；著者グループが「注記」として処理する可能性もある。
* **注記**: EP-03a（SRG-4）とは異なる実装（p-cymene基質 vs SET熱力学）。もし同一論文が両方を充填する場合は相互参照すること。

---

**EP-07a [Boundary-test pack]（SRG-6）（第一群）**

* **充填するRI**: RI-07 [Unsupported boundary]（因果帰属サブタイプ）
* **充填開始点**: **未同定**
* **充填確立点**: **未同定**
* **充填の性質**: — （未充填）
* **Confidence**: High（未充填であることへの確信）
* **注記**: matched-pair実験（O-ピバロイル vs O-ペンタフルオロベンゾイルをP(t-Bu)3条件下で直接比較）は、「配位子のみによる機構分岐」の因果帰属に必須だが、既存のaza-Heck文献でこの実験設計を主題とした論文は著者の知る限り存在しない。§Eで発見的意義として記録。

---

**EP-03a [Direct-observation / state-assignment pack]（SRG-4）（第二群）**

* **充填するRI**: RI-03 [Unobserved explanatory]（SET熱力学サブタイプ）
* **充填開始点**: Leonori group photoredox iminyl radical papers, e.g., Leonori et al., Angew. Chem. 推定2016–2019 — photoredox条件下でのN–O結合均一開裂とiminyl radical生成の熱力学的議論を含む可能性。
* **充填確立点**: DFT/計算化学論文（著者未特定）、推定2017–2022 — Pd(0)–L複合体の酸化電位とN–O BDE計算を扱った論文があれば確立点となる。
* **充填の性質**: Indirect — 対象系（P(t-Bu)3/Pd系）ではなく類似系または一般的iminyl radical熱力学の文脈での充填。
* **Confidence**: Medium（充填論文の存在への確信）/ Low（EP充填との対応への確信）
* **注記**: CVデータ（酸化電位測定）を含む論文は合成化学の標準論文には少なく、電気化学専門誌または光化学誌での報告が多い。

---

**EP-04a [Discrimination / replication pack]（SRG-3）（第二群）**

* **充填するRI**: RI-04 [Unreplicated discriminator]（Newcomb radical clock）
* **充填開始点**: Newcomb, M. et al.（refs 19a/19b相当）— 既に原論文発表前に存在する速度定数データソース論文。
* **充填確立点**: **未同定**（本系への定量的適用論文）
* **充填の性質**: Indirect — 速度定数データは存在するが、本系での反応速度との定量的照合（閾値計算）は実施されておらず、充填は不完全。
* **Confidence**: High（Newcomb速度定数ソース論文の存在）/ Low（本系への適用論文）
* **注記**: Race et al.がrefs 19a/19bとして引用したNewcombグループの論文が速度定数を提供しているが、そのデータを「P(t-Bu)3条件のPd触媒ターンオーバー頻度と比較して閾値を超えるか」という計算を行った論文は見当たらない。§Eで発見的意義として記録。

---

**EP-09a [Internal benchmark pack]（CLA-2）（第二群）**

* **充填するRI**: RI-09 [External superiority]
* **充填開始点**: レビュー論文（著者未特定）、例：iminyl radical総説、推定2018–2022。
* **充填確立点**: 同上（収率・選択性のクロスシステム比較表を含む総説）
* **充填の性質**: Partial — レビューが手法比較を提供しても、「本論文のaza-Heck vs radical条件の直接比較」は原著のデータ構造に依存するため完全充填は困難。
* **Confidence**: Medium — iminyl radical合成のレビュー論文は複数存在するはず（Leonori, Studer等）。
* **注記**: CLA-2は「Heck反応との比較なし」という問題であり、特定系のレビューより一般的aza-Heck手法論論文の中での位置づけ論文がより直接的な充填となりうる。

---

**EP-08a [Replication / uncertainty pack]（SRG-1）（第三群）**

* **充填するRI**: RI-08 [Unquantified reliability]
* **充填開始点**: **未同定**（構造的に充填されない）
* **充填確立点**: **未同定**
* **充填の性質**: — （構造的未充填）
* **Confidence**: High（未充填であることへの確信）
* **注記**: 合成化学の通信→Full Paper遷移では収率の反復測定・標準偏差報告は標準化されていない。独立した論文として充填される性質ではなく、§Eで「分野慣行型未充填」として記録。

---

### §C 推奨選定リスト

| 順序 | 論文 | 充填するEP | VQ水準 | 年代 | Confidence |
|------|------|-----------|--------|------|------------|
| 1 | Bower group Full Paper (Race/Faulkner/Shaw/Bower et al., Chem. Sci. or JACS, 推定2017–2020) | EP-07a(SRG-2), EP-03a(SRG-5) partial | VQ-2/VQ-3 | 2017–2020 | Medium |
| 2 | Leonori group photoredox iminyl radical paper (Leonori et al., Angew. Chem. or JACS, 推定2016–2019) | EP-03a(SRG-4) indirect, EP-09a partial | VQ-3 | 2016–2019 | Medium |
| 3 | iminyl radical 総説レビュー (Leonori/Studer/類似著者, Chem. Rev. or Chem. Soc. Rev., 推定2018–2022) | EP-09a complete/partial | VQ-4 | 2018–2022 | Medium |
| 4 | DFT/計算化学論文 Pd(0)–配位子系 SET熱力学 (著者未特定, 推定2017–2022) | EP-03a(SRG-4) indirect | VQ-3 | 2017–2022 | Low |
| 5 | Newcomb radical clock速度定数ソース論文 (Newcomb et al., refs 19a/19b相当) | EP-04a indirect（速度定数データ提供） | VQ-3 | 2016以前 | High（ソース）/ Low（適用） |

**選定理由：**

推奨1のBower group Full Paperは、原著者自身による自己充填パターンとして、EP-07a（SRG-2）とEP-03a（SRG-5）を同時に充填できる可能性がある唯一の候補であり、バンドル充填の効率性から最高優先度とした。このFull Paperの存在確認が本Stage 4検証の最重要ステップとなる。

推奨2・3は、aza-Heck/iminyl radical分野の発展を横断的に示す異なる研究グループによる充填であり、VQ-3（EP-03a間接充填）とVQ-4（EP-09a）をそれぞれカバーする。ConfidenceがいずれもMedium止まりであるのは、これらの論文が本系の具体的な条件（P(t-Bu)3 / Pd(dba)2）を直接扱うかどうかに推論が入るためであり、実際の文献確認が不可欠である。

推奨4・5はConfidenceが低く本来は推奨リストに含めないが、EP-03a（SRG-4）とEP-04aへの充填可能性を検証するための「探索的候補」として補完的に含めた。

---

### §D VQ階層と充填時間順序の対応分析

**充填の時間軸：**

- VQ-2 要件: EP-07a(SRG-2) → 推定2017–2020 [Bower group, 自己充填, Partial]
- VQ-2 要件: EP-07a(SRG-6) → **未充填**（matched-pair実験、2026年時点で未確認）
- VQ-3 要件: EP-03a(SRG-4) → 推定2016–2022 [Leonori/DFT, 間接充填, 分野横断]
- VQ-3 要件: EP-04a(SRG-3) → **未充填**（定量的速度論抽出、適用論文未確認）
- VQ-3 要件: EP-03a(SRG-5) → 推定2017–2020 [Bower, 自己充填, Partial]
- VQ-4 要件: EP-09a(CLA-2) → 推定2018–2022 [レビュー, 間接充填]
- VQ-4 要件: EP-08a(SRG-1) → **未充填**（分野慣行型）

**階層-時間対応の評価：**

「VQ階層が上がるほど充填に要する時間が長くなる」という仮説は、本ケースでは**部分的にのみ支持される**。VQ-2要件のEP-07a（SRG-2）は自己充填パターンで比較的早期（1–4年以内）に充填される見込みである一方、VQ-3要件のEP-03a（SRG-4）は6年以上を要し、VQ-4要件のEP-09aは2022年頃のレビューで間接充填される可能性がある。しかし、最も重要な反例は**VQ-2要件のEP-07a（SRG-6）が現時点で未充填**である点であり、VQ-2水準の要件が技術的困難のためではなく「設計見落とし」や「分野的関心欠如」により未充填のまま残存するという構造的問題を示す。充填の障壁は技術的難易度よりも「誰がその問いに関心を持つか」という社会的要因に支配されている可能性がある。

**特筆すべきパターン：**

- **自己充填**: EP-07a（SRG-2）およびEP-03a（SRG-5）については、Bower研究グループ自身の後続Full Paperによる自己充填パターンが期待される。通信→Full Paper遷移での部分的自動解消の典型例。
- **分野横断充填**: EP-03a（SRG-4）については、photoredox化学（Leonori グループ）からのアプローチがPd触媒系とは独立に同種の実験的問いを扱い、間接的に充填する可能性がある。これはRI-03（未観測説明変数）への充填が元の化学系以外からもたらされるという汎化可能な充填パターンを示す。
- **長期遅延充填/未充填**: EP-07a（SRG-6、matched-pair）、EP-04a（Newcomb定量適用）は原論文発表から10年以上経過しても充填されていない可能性があり、これは「分野が構造的に回避してきた問い」としての発見的意義を持つ（§E参照）。
- **バンドル充填**: 推奨1（Bower Full Paper）が複数EPを同時充填する可能性（EP-07a SRG-2 + EP-03a SRG-5）はバンドル充填の典型例であり、充填検証の効率化に貢献する。

---

### §E 未充填EPの発見的意義

**未充填EP一覧：**

**EP-07a（SRG-6）[Boundary-test pack — matched-pair実験]:**
* **未充填の理由**: 関心の欠如（synthesis community priority） + 分野慣行。合成化学コミュニティは「配位子を変えたら機構が変わった」という観察を実用的成果として受け入れ、「なぜその配位子か」の因果帰属実験（matched-pair設計）は慣例的に要求しない。RI-07の因果帰属サブタイプがこれを正確に捉えている。
* **発見的意義**: **あり**。「配位子のみが原因である」というRace et al. 2016の主張の中核的根拠が、2026年時点で直接的には実証されておらず、合成有機化学分野がカウンターファクチュアル実験を構造的に回避していることを示す代表例として記録できる。
* **将来の充填可能性**: **高**。matched-pair実験は技術的には単純であり（既存の基質・条件を組み合わせるだけ）、UQSが問いを明示化することで速やかに充填可能。

**EP-04a（SRG-3）[Discrimination / replication pack — Newcomb速度定数の定量適用]:**
* **未充填の理由**: 報告形式問題 + 関心の欠如。Newcomb速度定数（refs 19a/19b）は存在しているにもかかわらず、本系での「閾値計算」（ターンオーバー頻度 vs ラジカル閉環速度の数値比較）が実施されていない。これは「引用することで数値的裏付けを暗示する」という合成論文の慣行的報告形式に起因する「Dropped Quantitative Benchmark」パターンの典型例である。
* **発見的意義**: **あり**。既存の速度定数データが入手可能であるにもかかわらず、定量的照合が論文中でも後続研究でも行われないという「定量的裏付けの落差」は、UQSが検出するRI-04（Unreplicated discriminator）の重要なサブタイプとして記録できる。
* **将来の充填可能性**: **高**。Newcombデータと触媒TOF推定値さえあれば計算は数行で実施可能。計算化学論文または反応機構論文の補足情報として充填が期待される。

**EP-08a（SRG-1）[Replication / uncertainty pack]:**
* **未充填の理由**: 分野慣行（field-wide reporting norm）。合成有機化学における収率の反復測定・標準偏差報告は2016年時点でも現代でも標準的慣行ではなく、独立論文として充填される性質を持たない。RI-08に起因するこの欠如は分野全体の問題であり、個別論文への帰属として発見的意義を持たない。
* **発見的意義**: **なし**。第三群分類の典型例として制度的記録には有用だが、Race et al. 2016固有の発見ではなく、分野全体の慣行問題である。
* **将来の充填可能性**: **低**（慣行変化依存）。再現性・信頼性研究の機運が高まれば分野全体で解消される可能性はあるが、個別論文単位での充填は見込みにくい。
```
