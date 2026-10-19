```
prompt_version: stage4-v1-20260416
model_info: claude-sonnet-4-6

# EP充填選定マップ

## Tamao, Sumitani, Kumada 1972（J. Am. Chem. Soc. communication）

### §A EP充填難易度の三群分類

**第一群（文献で明確に追跡可能）：** EP-01a, EP-07a, EP-04a, EP-06a

— EP-01a (Reporting-coherence pack): 通信→Full Paper遷移が本系で明確に発生しており（Tamao et al., Bull. Chem. Soc. Jpn. 1976）、glpc条件・反応時間・収率基準の統一記載が独立論文の主題として存在する。
— EP-07a (Boundary-test pack): sp³ハライドの失敗例と塩化物/臭化物/ヨウ化物の直接比較は1976年Full Paperのスコープ拡張部分で正面から扱われており、文献検索で直接ヒットする。
— EP-04a (Discrimination / replication pack): 副生物定量とcis/trans比の繰り返し測定は、1976年Full Paperおよびその後の立体化学論文の主要テーマとして独立的に記載されている。
— EP-06a (Analogy-validation pack): NiCl₂(dpe)系での化学量論的ステップ検証およびNi(acac)₂との直接比較は、機構研究と配位子効果研究として独立論文の主題となっており（Kochi, Corriu各グループ）、文献で追跡可能。

**第二群（間接的に追跡可能）：** EP-03a, EP-05a, EP-09a

— EP-03a (Direct-observation / state-assignment pack): ジオルガノニッケル(II)中間体の直接分光観測は、NiCl₂(dpe)系に特化した独立論文は限定的だが、有機ニッケル化学全般を扱う配位化学論文（Yamamoto Aグループ等）の一部として間接的に充填されている。
— EP-05a (Quantitative-ranking substantiation pack): 全6配位子の定量的活性データはFull PaperおよびKumadaレビュー（1980）に含まれるが、配位子活性の定量化そのものを独立主題とした論文は見つかりにくい。
— EP-09a (Internal benchmark pack): Tamura-Kochi・Corriu/Masseとの定量比較はレビュー論文・Plenary Lectureの文脈で提供されており、同一基質での並行比較実験として独立発表された可能性は低い。

**第三群（充填が見つからない可能性あり）：** EP-08a

— EP-08a (Replication / uncertainty pack): 1972年Kumadaデータのn≥3反復と標準偏差付き収率の報告は、有機金属合成の分野慣行として体系的に行われておらず、この特定の系に対して統計的不確かさを明示した独立論文は存在しない可能性が高い。

---

### §B 各EPの充填論文候補

**EP-01a Reporting-coherence pack（第一群）**

* **充填するRI**: RI-01 Reporting integrity
* **充填開始点**: Tamao, Sumitani, Kiso, Zembayashi, Fujioka, Kodama, Nakajima, Minato, Kumada, Bull. Chem. Soc. Jpn. 1976, 49, 1958–1969 — glpc条件・反応時間・使用溶媒・Grignard試薬の詳細を含む完全実験手順を記載した標準的Full Paper。
* **充填確立点**: 同上
* **充填の性質**: Complete — RI-01が要求するglpc条件統一・収率算出基準の統一・反応時間の全エントリ記載が実質的に達成されている。
* **Confidence**: High
* **注記**: 1972年通信から4年後の自己充填（原著者グループ）。通信→Full Paper遷移での自動解消パターンの典型例。同論文がEP-07a・EP-04aも部分充填する（バンドル充填）。

---

**EP-07a Boundary-test pack（第一群）**

* **充填するRI**: RI-07 Unsupported boundary; RI-09 External superiority（B-6のCl/Br/I比較分）
* **充填開始点**: Tamao et al., Bull. Chem. Soc. Jpn. 1976, 49, 1958–1969 — sp²ハライドのみが反応することをスコープ実験で実証し、sp³ハライドが β-水素脱離により選択性不良となる代表例を含む。
* **充填確立点**: 同上（RI-07分）。Cl/Br/I比較については同Full Paperが基礎データを提供し、その後のレビューで確立。
* **充填の性質**: Partial — sp²/sp³の境界は実験的に確認されたが、β-脱離が不活性の主要因であるという機構的帰属（RI-07の「なぜ」の部分）は後続の機構研究で充填される。
* **Confidence**: High
* **注記**: sp³ハライドの「失敗例」が最終的にRI-07を充填するというパターンは、Full Paper展開での自動解消の典型。CLA-1（D4-7）の"useful"主張の定量的根拠は同論文のスコープ記述によって部分的に充填される。

---

**EP-04a Discrimination / replication pack（第一群）**

* **充填するRI**: RI-04 Unreplicated discriminator
* **充填開始点（SRG-2分: byproduct定量）**: Tamao et al., Bull. Chem. Soc. Jpn. 1976, 49, 1958–1969 — 複数エントリで収率・選択性データを拡充し、ホモカップリング副生物の記述を含む。
* **充填開始点（SRG-6分: cis/trans比）**: Tamao, K.; Sumitani, K.; Zembayashi, M.; Kumada, M. Bull. Chem. Soc. Jpn. 1976 または後続の立体化学論文 — ビニル基質のcis/trans比をNMRで独立定量した可能性。
* **充填確立点**: Tamao et al., Bull. Chem. Soc. Jpn. 1976（SRG-2分）。SRG-6分の繰り返し測定については確立点未同定。
* **充填の性質**: Partial — クロス/ホモ比は1976年Full Paperで改善されたが、cis/trans比の反復統計（n≥3, 標準偏差）は確認されていない。
* **Confidence**: High（1976 Full Paper分）; Low（cis/trans比の繰り返し測定分）
* **注記**: cis/trans比の不確かさ評価（U-3: 速度論的vs熱力学的）は1976年以降の立体化学専門論文で部分的に扱われる可能性があるが、同定には文献確認が必要。

---

**EP-06a Analogy-validation pack（第一群）**

* **充填するRI**: RI-06 Imported model; RI-05（CLA-2 secondary）
* **充填開始点（化学量論的ステップ検証）**: Tamao, K.; Kodama, S.; Nakajima, I.; Kumada, M. et al., Tetrahedron 1982 年頃の機構研究論文（推定） — NiCl₂(dpe)+RMgBrの化学量論的反応が独立に研究されたと推定。ただし正確な論文同定には文献確認が必要。
* **充填確立点（酸化的付加機構）**: Tsou, T. T.; Kochi, J. K. J. Am. Chem. Soc. 1979, 101, 6319 付近 — Ni(0)–ホスフィン錯体への有機ハライドの酸化的付加機構（二電子 vs ラジカル経路）を検討し、Ni(0)/Ni(II)二電子経路を支持する証拠を提示。
* **充填開始点（Ni(acac)₂比較: CLA-2）**: Corriu, R. J. P.; Moreau, J. J. E. J. Organomet. Chem. 1975–1978年頃 — Ni(acac)₂触媒によるGrignard反応のスコープと選択性をKumada系と間接的に比較した論文群。
* **充填の性質**: Partial — Ni(0)/Ni(II)二電子機構の支持は得られたが、NiCl₂(dpe)系でのdpe特有中間体（1, 2, 3）の直接単離・分光観測は後続の研究でも完全充填には至っていない可能性がある。
* **Confidence**: Medium（Tsou-Kochi系）; Medium（Corriu比較系）
* **注記**: EP-06aはSRG-1（RI-06）とCLA-2（RI-05）の双方に寄与する二重充填候補。Kochi研究グループは1970年代後半から有機ニッケル機構を精力的に研究しており、Ni触媒クロスカップリング機構への寄与は実質的に確実だが、特定論文の詳細には文献確認を推奨。

---

**EP-03a Direct-observation / state-assignment pack（第二群）**

* **充填するRI**: RI-03 Unobserved explanatory
* **充填開始点（ジオルガノNi中間体の合成・特性評価）**: Yamamoto, T.; Yamamoto, A.; Ikeda, S. J. Am. Chem. Soc. 1971, 93, 3350 — ホスフィン配位子を持つジアルキルニッケル錯体の合成と熱的不安定性の研究（Kumada 1972より先行するが、1972年通信の中間体類似体として機能）。
* **充填開始点（均一系/不均一系の判別）**: 2000年代以降の研究グループ（Rothenberg, Bedford等）による "nanoparticle vs. molecular catalyst" 論争論文群 — 水銀毒実験・ろ過実験等の標準的検証手法が確立した時期。
* **充填確立点（NiCl₂(dpe)系に特化した中間体観測）**: 未同定 — NiCl₂(dpe)に固有の中間体を直接観測した独立論文は、文献確認なしには特定できない。
* **充填の性質**: Indirect（Yamamoto系: 類似系での充填）; Partial（均一系/不均一系判別: 現代の方法論が適用可能だが1972年系への遡及的検証は限定的）
* **Confidence**: High（Yamamoto 1971系）; Low（NiCl₂(dpe)特有の直接観測）
* **注記**: Yamamoto, A.（東工大）グループは1970年代に有機ニッケルホスフィン錯体の化学量論的化学を体系化しており、diorganonickel phosphine complexesの合成・キャラクタリゼーションはU-2（黒色混合物問題）の背景知識として機能する。しかし1972年論文の具体的系（dpe配位子）への特化した直接観測研究の同定には文献確認が必要。

---

**EP-05a Quantitative-ranking substantiation pack（第二群）**

* **充填するRI**: RI-05 Qualitative overread
* **充填開始点**: Tamao et al., Bull. Chem. Soc. Jpn. 1976, 49, 1958–1969 — 6種の配位子についての活性データを拡充し、dpp > dpe > dmpe ≈ PPh₃₂ >> PEt₃₂ ≈ PPh₂Me₂の序列を定量的（収率ベース）に確認。
* **充填確立点**: Kumada, M. Pure Appl. Chem. 1980, 52, 669–679 — Kumada自身のPlenary Lectureレビューで、配位子bite angle効果と活性序列の相関についての系統的な議論が提供される。
* **充填の性質**: Partial — 収率ベースの活性序列は充填されたが、bite angle・電子効果・立体効果の独立変数としての定量的切り分け（U-4: 幾何効果vs電子効果の区別）は完全充填には至っていない。
* **Confidence**: High（Kumada 1980レビュー）; Medium（1976 Full Paperの定量的配位子データ）
* **注記**: CLA-2（D4-8: bidentate phosphineの必要性）に対する充填はKumadaレビューとCorriuの後続研究の双方によって提供される。NiCl₂(dpe)のbite angleが選択性に必須かどうかの最終的答え（Ni(acac)₂でも機能する）は、1990年代以降の不斉Kumadaカップリング研究（BINAP配位子の重要性）が事実上確立した。

---

**EP-09a Internal benchmark pack（第二群）**

* **充填するRI**: RI-09 External superiority
* **充填開始点（Tamura-Kochi Fe触媒との比較）**: Kumada, M. Pure Appl. Chem. 1980, 52, 669–679 — Kumadaレビュー内でFe触媒（Tamura-Kochi）との適用範囲の比較が叙述的に提供される（定量的並行実験ではない）。
* **充填確立点（Corriu/Masse Ni(acac)₂との比較）**: Corriu, R. J. P.; Moreau, J. J. E. 1970年代後半の論文群 — Ni(acac)₂とbidentate phosphine系のスコープ・選択性を独立のGrignardカップリング研究として継続的に記録しており、間接的な比較情報を提供する。
* **充填の性質**: Indirect — 同一基質での並行実験による定量比較（論文内での直接数値比較）は確認されていない。分野の発展の中での暗黙の比較として充填。
* **Confidence**: Medium（Kumadaレビュー）; Medium（Corriu論文群）
* **注記**: CLA-1（D4-7: Corey/Whitesides試薬との定量比較）の充填は、合成有機化学における「Grignard cross-coupling vs stoichiometric organometallic」の実用比較として現れるが、特定の並行実験論文は同定できていない。Confidence: Low。

---

**EP-08a Replication / uncertainty pack（第三群）**

* **充填するRI**: RI-08 Unquantified reliability
* **充填開始点**: **未同定**
* **充填確立点**: **未同定**
* **充填の性質**: — （未充填）
* **Confidence**: Low（充填論文の不存在に対する確信）
* **注記**: n≥3反復・標準偏差付き収率の報告は、1970年代〜2010年代の有機金属合成において分野慣行として体系的に実施されてこなかった。2010年代以降のフロー化学・高スループットスクリーニング文脈でのケモインフォマティクス論文が部分的に近い内容を扱うが、1972年Kumadaデータへの遡及的検証は存在しない。§Eで詳細を扱う。

---

### §C 推奨選定リスト

| 順序 | 論文 | 充填するEP | VQ水準 | 年代 | Confidence |
|------|------|-----------|--------|------|------------|
| 1 | Tamao, Sumitani, Kiso, Zembayashi, Fujioka, Kodama, Nakajima, Minato, Kumada, Bull. Chem. Soc. Jpn. 1976, 49, 1958 | EP-01a, EP-07a, EP-04a（部分）, EP-05a（部分） | VQ-2, VQ-3 | 1976 | High |
| 2 | Tsou, T. T.; Kochi, J. K. J. Am. Chem. Soc. 1979, 101, 6319付近（Ni(0)ホスフィン酸化的付加機構） | EP-06a（RI-06 Ni(0)/Ni(II)二電子経路支持） | VQ-3 | ~1979 | Medium |
| 3 | Kumada, M. Pure Appl. Chem. 1980, 52, 669–679 | EP-05a, EP-09a | VQ-3, VQ-4 | 1980 | High |
| 4 | Yamamoto, T.; Yamamoto, A.; Ikeda, S. J. Am. Chem. Soc. 1971, 93, 3350（または同グループ1972–1978年の後続論文） | EP-03a（RI-03 ジオルガノNi中間体の類似体合成・観測） | VQ-3 | 1971–1978 | High（Yamamoto 1971）; Medium（後続） |
| 5 | Corriu, R. J. P.; Moreau, J. J. E. J. Organomet. Chem. 1975–1978年頃（Ni(acac)₂系のGrignardカップリング研究） | EP-06a（CLA-2: Ni(acac)₂vs NiCl₂(dpe)比較）, EP-09a（部分） | VQ-3, VQ-4 | ~1975–1978 | Medium |

**選定理由：**

論文1（Tamao et al. 1976）は、VQ-2到達に必要なRI-01とRI-07を一報でバンドル充填するため最優先とした。EP-01a（Reporting coherence: glpc条件・反応時間・収率基準）とEP-07a（Boundary-test: sp³失敗例・Cl/Br/I比較）の両方をComplete〜Partialで充填し、VQ-2への最短ルートを具体的に示す。この1報だけでVQ-2要件の中核が満たされることは、「自己充填パターン」と「通信→Full Paper遷移での自動解消」の両方を実証する。

論文2（Tsou-Kochi ~1979）と論文4（Yamamoto 1971–）は、VQ-3のRI-06（機構類推）とRI-03（中間体観測）をそれぞれ異なる切り口から充填する。論文2がNi(0)/Ni(II)二電子経路の機構的支持を与え（EP-06a）、論文4がジオルガノNi中間体の間接的実在証拠を与える（EP-03a）。両論文の組み合わせでSRG-1の主要RI（RI-06, RI-03）が充填される。

論文3（Kumada 1980レビュー）と論文5（Corriu比較論文）はVQ-3/4要件（EP-05a, EP-09a）をそれぞれ異なる立場（原著者グループvs独立グループ）から部分充填する。この組み合わせにより、bidentate phosphineの役割（CLA-2）とTamura-Kochi/Corriu/Masse系との比較（EP-09a）が間接的に検証される。VQ-4は完全充填に至らないが、充填の「時間限界」を示す事例として重要。

---

### §D VQ階層と充填時間順序の対応分析

**充填の時間軸：**

- **VQ-2 要件: EP-01a**（RI-01: Reporting integrity） → 1976年 Tamao et al. 【自己充填】
- **VQ-2 要件: EP-07a**（RI-07: Unsupported boundary） → 1976年 Tamao et al. 【自己充填】
- **VQ-3 要件: EP-04a**（RI-04: Unreplicated discriminator、byproduct分） → 1976年 Tamao et al. 【自己充填、Partial】
- **VQ-3 要件: EP-06a**（RI-06: Imported model、機構分） → ~1979年 Tsou-Kochi 【技術駆動充填 + 分野横断充填】
- **VQ-3 要件: EP-03a**（RI-03: Unobserved explanatory） → 1971–1978年 Yamamoto A. 【Indirect、技術駆動充填】
- **VQ-3 要件: EP-05a**（RI-05: Qualitative overread） → 1976–1980年 Tamao/Kumada 【自己充填、Partial】
- **VQ-3 要件: EP-06a**（CLA-2: Ni(acac)₂比較分） → ~1975–1978年 Corriu et al. 【分野横断充填、Indirect】
- **VQ-4 要件: EP-09a**（RI-09: External superiority） → 1980年– Kumadaレビュー 【自己充填、Indirect】
- **VQ-4 要件: EP-08a**（RI-08: Unquantified reliability） → **未充填**（分野慣行の問題）

**階層-時間対応の評価：**
VQ-2要件（EP-01a, EP-07a）が1972年から4年後（1976年）に充填されたのに対し、VQ-3要件のうち機構関連（EP-06a: RI-06, EP-03a: RI-03）は1976–1979年頃に部分充填が始まり、完全充填には10年以上を要した（またはされていない）。この時間的勾配は「VQ階層が上がるほど充填に要する時間が長くなる」という階層-時間仮説を支持する。VQ-4要件（EP-08a: RI-08）は現在まで未充填であり、この仮説をさらに強く支持する。ただし、EP-07aとEP-01aが同一論文で同時充填されている点は、一部のVQ-2要件が「バンドル充填」によって時間を圧縮されることを示す。

**特筆すべきパターン：**

- **自己充填（Tamao/Kumada グループ）**: VQ-2全要件（EP-01a, EP-07a）とVQ-3の一部（EP-04a, EP-05a）は原著者グループ自身が1976年のFull Paperで充填した。これは1972年通信の「未完成報告」が意図的な「予告」として機能していたことを示唆し、通信形式が連続した研究プログラムの一部として機能した証拠である。
- **技術駆動充填（EP-06a, EP-03a）**: RI-06（輸入モデル検証）とRI-03（中間体観測）への充填は、1970年代後半の有機金属化学のインフラ整備（低温NMR, ESI-MS前駆体としての高磁場NMR, 単結晶X線解析の普及）によって可能になった。これは機構的要件の充填が技術進化に依存するパターンを示す。
- **分野横断充填（CLA-2: Corriu論文群）**: Ni(acac)₂系の研究はフランスのCorriuグループによって独立に進められ、「chelating phosphineが必須か」というCLA-2の問いに対する間接的な答えを提供した。これは競合グループの存在がUQS項目の充填を加速するパターンの事例。
- **未充填（EP-08a）**: EP-08a（RI-08: 反復測定・統計的不確かさ）は「長期遅延充填」を超えて実質的未充填。これは§Eで詳細を扱う。

---

### §E 未充填EPの発見的意義

**未充填EP一覧：**

**EP-08a Replication / uncertainty pack:**
* **未充填の理由**: 分野慣行 — 有機金属合成化学において1970年代から2010年代にわたり、n≥3反復測定と標準偏差付き収率の体系的報告は慣例的に行われてこなかった。この慣行の不在は「分野が選択的に回避してきた実践」であり、特定の論文の問題ではなくフィールド全体の報告規範の問題である。1972年Kumadaデータに対して遡及的に統計的検証を行った研究は存在せず、また行う動機も分野内に現れていない。
* **発見的意義**: あり — 「有機金属クロスカップリング合成化学は、収率データの統計的信頼性評価を50年以上にわたって体系的に実施してこなかった」という発見的命題を提示できる。これはUQSが抽出した「分野が長期間回避してきた問い」の典型例として記録価値があり、現代のReproducibilityクライシス議論と直結する。RI-08の未充填率（充填0報）が示す時間スケールは、RI-04/RI-06（充填4〜7年）やRI-01/RI-07（充填4年）と対照的であり、VQ-4要件の一部が「原理的に充填可能だが分野慣行として実施されていない」という特殊なカテゴリに属することを示す。
* **将来の充填可能性**: 高 — 現代の高スループット実験化学（HTE）とデータ駆動合成化学（OrdExp, Bayesian optimization）のコンテキストで、クロスカップリング反応の反復測定と不確かさ評価は技術的に実現可能である。実際、Doyle/Denmark/Glorius等のグループが推進するデータ駆動合成最適化では収率の反復測定が標準化されている（2018年以降の機械学習支援合成論文）。ただしKumada 1972年の特定基質系への遡及的適用は、現代の研究グループにとって動機付けが弱い。
```
