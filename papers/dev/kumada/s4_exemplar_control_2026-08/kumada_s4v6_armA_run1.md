```
prompt_version: stage4-v6-20260504
model_info: claude-sonnet-4-6

# EP充填選定マップ

## Tamao, Sumitani, Kumada 1972（Journal of the American Chemical Society, Communication）

---

### §A EP充填難易度の三群分類

**C23 trigger**: 本論文はJACS Communication（1972年）— Letter/Communication形式に該当。
reporting completeness 関連EP（EP-01a, EP-02a）について Letter→Full Paper auto-resolution
パターン（C23）を確認する。Kumada研究グループは1976年（約4年後）にBull. Chem. Soc. Jpn.
にFull Paper（Part I）を発表しており、auto_resolution_status: "occurred"が適用される。

---

**第一群（文献で明確に追跡可能）：** EP-03a, EP-04a, EP-06a, EP-07a

- **EP-03a**（Direct-observation / state-assignment pack, RI-03）: NiCl₂(dpe)系での中間体
  分光学的同定は、触媒機構の核心的問いとして1970年代後半〜1980年代にかけて独立研究の
  主題として発表されやすい。NiおよびPd触媒クロスカップリングの機構研究は活発な
  独立論文形成領域であった。
- **EP-04a**（Discrimination / replication pack, RI-04）: cis/trans-stilbene比の
  速度論vs熱力学的制御の判別という立体化学的問いは、クロスカップリングの
  立体選択性を主題とする独立論文（Full Paper以降の立体化学研究）として発表される
  可能性が高い。
- **EP-06a**（Analogy-validation pack, RI-06）: dipy-Ni系からdpe-Ni系への触媒サイクル
  輸入の実験的検証（個別素反応の化学量論的実証）は、酸化的付加・脱メタル化・
  還元的脱離の各素反応を個別に検証する独立論文として発表されやすい（RI-06デフォルト
  第一群）。
- **EP-07a**（Boundary-test pack, RI-07）: sp³ハライドとsp²ハライドの反応性境界、
  および塩化物/臭化物/ヨウ化物の反応性比較は、方法論論文の基板スコープ節または
  専用の境界検証論文として発表されやすい（RI-07デフォルト第一群）。

---

**第二群（間接的に追跡可能）：** EP-01a, EP-02a, EP-05a, EP-09a

- **EP-01a**（Reporting-coherence pack, RI-01 in SRG-3）: **Letter→Full Paper
  auto-resolution（C23）**。Tamao et al. 1976（Bull. Chem. Soc. Jpn., Full Paper）が
  glpc条件・反応時間・収率基準の統一的記述を提供している。独立論文として存在するが、
  主題はscope確立であり、reporting coherence の修正は副次的。
  ```yaml
  auto_resolution_type: "Letter→Full Paper"
  expected_resolution_window: "1-5 yr"
  auto_resolution_status: "occurred"
  filling_timescale_category: "format-driven"
  ```
- **EP-02a**（Identity/purity substantiation pack, RI-02）: **Letter→Full Paper
  auto-resolution（C23）**。同上Full Paperが各エントリの詳細分光データを提供。
  ```yaml
  auto_resolution_type: "Letter→Full Paper"
  expected_resolution_window: "1-5 yr"
  auto_resolution_status: "occurred"
  filling_timescale_category: "format-driven"
  ```
- **EP-05a**（Quantitative-ranking substantiation pack, RI-05 in SRG-2）: ホモカップリング
  生成物を含む質量収支の定量データはFull Paper展開や機構研究論文の一部として含まれる
  可能性が高いが、「ホモカップリング定量」を主題とする独立論文は同定困難（RI-05
  デフォルト第二群）。
- **EP-09a**（Internal benchmark pack, RI-09 in CLA-1）: NiCl₂(dpe)とNi(acac)₂の
  同一条件での直接比較は、比較型方法論研究の中に含まれる可能性があるが、
  この特定の比較を主題とする独立論文は同定困難（RI-09デフォルト第二群）。

---

**第三群（充填が見つからない可能性あり）：** EP-08a

- **EP-08a**（Replication / uncertainty pack, RI-08）: 代表的エントリの収率を独立実験
  で3回以上測定して標準偏差を報告する研究は、**インセンティブ構造的未充填**に該当する。
  Kumada反応系の収率の統計的再現性評価そのものを主題とする論文は、新規性要求の高い
  出版慣行のもとで独立論文化されにくい。技術的には可能だが出版動機が存在しない典型例。

---

### §B 各EPの充填論文候補

**Bibliographic verification トリガー評価（§B 末尾チェック、論文セット全体）：**

本論文（Tamao-Sumitani-Kumada 1972）は以下の全条件を満たすため、§B で列挙する
全充填候補について Verification recommendation: **[必須]** が一括適用される：
- (a) 多くの候補論文の発表年が1980年以前
- (b) 同一研究グループ（Kumada lab）から10報以上の関連論文が存在する
- (c) "Kumada coupling" として著者名に由来する命名規則を持つ named reaction

---

**EP-01a [Reporting-coherence pack]（第二群, Letter→Full Paper auto-resolution）**

* **充填するRI**: RI-01 (Reporting integrity) — SRG-3（Table I収率データの分析的信頼性）
* **充填開始点**: Tamao, K.; Sumitani, K.; Kiso, Y.; Zembayashi, M.; Fujioka, A.;
  Kodama, S.; Nakajima, I.; Minato, A.; Kumada, M. "Nickel-Phosphine Complex-Catalyzed
  Grignard Coupling. I. Cross-Coupling of Alkyl, Aryl, and Alkenyl Grignard Reagents
  with Aryl and Alkenyl Halides: General Scope and Limitations." *Bull. Chem. Soc. Jpn.*
  **1976**, *49*, 1958–1969. —
  通信論文で欠落していたglpc条件・反応時間・各エントリの個別収率根拠を統一的な
  Full Paper形式で報告し、11エントリを超えた大規模スコープ研究として完全記述。
* **充填確立点**: 同上
* **充填の性質**: Complete（RI-01のFull Paper自動解消）
* **Bibliographic confidence**: High（Kumada反応Full Paperシリーズとして広く引用される
  確立した論文；著者リストの正確な確認は必要）
* **Filling adequacy confidence**: High（Full Paper形式でglpc条件・反応時間・収率基準が
  統一記述されることが期待される）
* **Verification recommendation**: [必須] — (a)(b)(c) 全条件該当
* **Bibliographic verification status**: pending
* **Filling timescale category**: format-driven (1-5 yr)
* **注記**: 本論文はSRG-3の主要構成員（B-4, B-8, B-9, B-12, B-13）を集合的に充填する
  バンドル充填候補。Stage 3 §4のEra-Norm Annotationで「communication-era tolerated」
  に分類されたB-4, B-8, B-13がFull Paperへの遷移で自動解消（§6 通信→Full Paper
  遷移パターンと整合）。

---

**EP-02a [Identity/purity substantiation pack]（第二群, Letter→Full Paper auto-resolution）**

* **充填するRI**: RI-02 (Product identity / purity) — Table I生成物の"and/or"同定
* **充填開始点**: Tamao, K.; Sumitani, K.; Kiso, Y.; Zembayashi, M.; Fujioka, A.;
  Kodama, S.; Nakajima, I.; Minato, A.; Kumada, M. *Bull. Chem. Soc. Jpn.* **1976**,
  *49*, 1958–1969. —
  Full Paper形式で各生成物のGC・NMR等の個別分光データを報告（EP-01aとバンドル充填）。
* **充填確立点**: 同上（EP-01aとの共通充填点）
* **充填の性質**: Complete（RI-02のFull Paper自動解消候補）
* **Bibliographic confidence**: High（EP-01aと同一論文）
* **Filling adequacy confidence**: Medium（Full Paperが各エントリの個別NMR/IR/MS
  データを記載するかどうかは実際の論文内容の確認が必要）
* **Verification recommendation**: [必須]
* **Bibliographic verification status**: pending
* **Filling timescale category**: format-driven (1-5 yr)
* **注記**: EP-01aとバンドル充填。Stage 3 §3でRI-02が「non-fatal」として分類され
  VQ-1通過の根拠となったが、Full PaperでのComplete充填によりVQ-1水準は補強される。

---

**EP-03a [Direct-observation / state-assignment pack]（第一群）**

* **充填するRI**: RI-03 (Unobserved explanatory) — SRG-1（中間体1,2,3の直接観測なし）
* **充填開始点（候補A — 酸化的付加ステップ）**:
  Tsou, T. T.; Kochi, J. K. "Mechanism of Oxidative Addition. Reaction of Nickel(0)
  Complexes with Aromatic Halides." *J. Am. Chem. Soc.* **1979**, *101*, 6319–6332. —
  Ni(0)錯体とArXの酸化的付加機構を速度論的・分光学的に解析し、eq (2)に対応する
  Ni(0) + ArX → Ni(Ar)(X) ステップに実験的根拠を提供（部分充填）。
* **充填開始点（候補B — ジオルガノニッケル中間体の直接観測）**:
  Yamamoto, T.; Yamamoto, A. "Diorganonickel Complexes. Synthesis and Reactivity."
  *J. Organomet. Chem.* (1970年代複数報) — NiR₂型錯体の合成・特性評価・反応性を
  記述する。ただし dpe-Ni 系での eq (3) に直接対応する [Ni(dpe)(R)₂] の系統的研究か
  どうかは確認が必要。
* **充填確立点**: 未同定 — NiCl₂(dpe)系に特化してeqs (2)-(4)の全ステップを
  化学量論的に検証した単独論文は現時点では同定できず。SRG-1全体の充填確立点は
  複数論文に分散していると推定される。
* **充填の性質**: Partial（酸化的付加ステップの部分充填; 候補A。全サイクルの充填は
  複数論文に分散）
* **Bibliographic confidence**: Medium（候補A: Tsou-Kochi 1979はKochi研究室の
  Ni機構研究として知られるが正確な巻号・ページは確認要；候補B: タイトルおよび
  巻号は推測域）
* **Filling adequacy confidence**: Medium（候補Aが酸化的付加のみの部分充填に
  対応するかどうかは内容確認が必要）
* **Verification recommendation**: [必須]
* **Bibliographic verification status**: pending
* **Filling timescale category**: field-methodology (2-10 yr)
* **注記**: Stage 3 §6で「RI-06 + RI-03の不可分共起パターン」として記録。EP-03aの
  充填は EP-06a（類似性実証）と不可分であり、どちらか一方の充填だけでは
  触媒サイクルの実験的根拠としては不十分。EP-06aとの共同充填論文も存在しうる。
  Kochi研究室はNi・Pd触媒クロスカップリング機構の多数の論文を発表しており、
  候補論文が複数存在する可能性が高い。

---

**EP-04a [Discrimination / replication pack]（第一群）**

* **充填するRI**: RI-04 (Unreplicated discriminator) — SRG-6（cis/trans比の速度論vs
  熱力学的制御）
* **充填開始点（候補）**:
  Tamao, K.; Sumitani, K.; Kiso, Y.; Zembayashi, M.; Fujioka, A.; Kodama, S.;
  Nakajima, I.; Minato, A.; Kumada, M. *Bull. Chem. Soc. Jpn.* **1976**, *49*, 1958–1969.
  — Full Paper中でcis/trans体の反応を詳細に記述し、温度・時間条件での補足情報を
  含む可能性がある（部分充填候補）。
* **充填確立点（候補）**:
  Tamao, K.; Hayashi, T.; Ito, Y.; Kumada, M.（1970年代後半-1980年代初頭の立体化学
  研究論文。具体的なタイトル・巻号は同定困難）— Kumadaグループはビニルハライドの
  立体選択性を系統的に研究し、速度論的制御に関する知見を蓄積した。
* **充填の性質**: Partial（Full Paper部分充填候補。速度論/熱力学区別の
  完全な時間・温度系列実験を主題とする独立論文は現時点では同定困難）
* **Bibliographic confidence**: Medium（候補1 = High; 候補2 = Low、存在は推定だが
  タイトル・巻号は不明）
* **Filling adequacy confidence**: Medium（Full PaperがSRG-6の速度論/熱力学区別に
  必要な時間・温度系列データを含むかどうかは確認要）
* **Verification recommendation**: [必須]
* **Bibliographic verification status**: pending
* **Filling timescale category**: format-driven / field-methodology (1-10 yr)
* **注記**: A-1（deferred; 立体化学機構の将来課題として外部化）とB-11（分析条件不在）
  の複合問題。cis-stilbene富化という「異常な」観察（A-1）の機構的解明は、
  Kumada以降のクロスカップリング立体化学研究全体のテーマとなったが、
  この特定のNi-dpe系での時間・温度系列実験は未充填の可能性がある。

---

**EP-05a [Quantitative-ranking substantiation pack]（第二群）**

* **充填するRI**: RI-05 (Qualitative overread) — SRG-2（「選択的」の質量収支的根拠）
  および SRG-4（「塩化物の高反応性」の定量的根拠）
* **充填開始点（SRG-2, 選択性定量）**:
  Tamao, K.; Sumitani, K.; Kiso, Y.; Zembayashi, M.; Fujioka, A.; Kodama, S.;
  Nakajima, I.; Minato, A.; Kumada, M. *Bull. Chem. Soc. Jpn.* **1976**, *49*, 1958–1969.
  — Full Paperにてホモカップリング副生物の記述が含まれる可能性（SRG-2の部分充填候補）。
* **充填開始点（SRG-4, ハライド比較）**:
  同上Full Paper — PhCl vs PhBr vs PhIの収率/速度比較が含まれる可能性。
* **充填確立点**: 未同定 — GC-MSによる完全質量収支（クロス vs ホモ vs β-脱離）を
  明示的に主題とした論文の同定が現時点では困難。
* **充填の性質**: Partial（Full Paperが収率データの改善を提供するが、
  ホモカップリングの明示的定量は別論文の可能性）
* **Bibliographic confidence**: Medium（Full Paperの存在はHigh; ホモカップリング
  定量データの収録は確認要）
* **Filling adequacy confidence**: Low-Medium（EP-05aが要求する反応混合物質量収支の
  完全定量がFull Paperに含まれるかどうかは不明）
* **Verification recommendation**: [必須]
* **Bibliographic verification status**: pending
* **Filling timescale category**: format-driven / incentive-aligned (1-10 yr)
* **注記**: SRG-2（選択性主張の定量的根拠）はB-1（convergence=3/3, temperature_gap=none）
  として最高優先度のB項目であったが、充填の明確な同定が困難な第二群に分類される点は
  注目すべき逆転パターン（§Eで議論）。

---

**EP-06a [Analogy-validation pack]（第一群）**

* **充填するRI**: RI-06 (Imported model) — SRG-1（dipy-Ni系からdpe-Ni系への
  サイクルレベル輸入の同型性実証）
* **充填開始点（候補A — 酸化的付加の化学量論的実証）**:
  Tsou, T. T.; Kochi, J. K. *J. Am. Chem. Soc.* **1979**, *101*, 6319–6332. —
  Ni(0)錯体のArXへの酸化的付加を速度論的に解析（EP-03aとの共同候補；eq (2)対応）。
* **充填開始点（候補B — 還元的脱離ステップ）**:
  Stille, J. K.; Lau, K. S. Y. "Mechanisms of Oxidative Addition of Organic Halides
  to Group 8 d8 Metal Complexes." *Acc. Chem. Res.* **1977**, *10*, 434–442. —
  レビューだが、Ni-phosphine系の個別素反応の知見を収集・整理する内容であり、
  SRG-1の対象系での類似性検証の文脈的位置付けを提供（充填論文ではなく
  充填文脈整理として機能）。なお、レビューは充填論文として機能しない原則に従い
  本候補はガイドライン上は参考に留める。
* **充填確立点（候補C — 還元的脱離の直接実証）**:
  Gillie, A.; Stille, J. K. "Mechanisms of 1,1-Reductive Elimination from Palladium."
  *J. Am. Chem. Soc.* **1980**, *102*, 4933–4941. — これはPd系の論文であり、
  Ni-dpe系の直接充填ではないが、還元的脱離機構の一般化に貢献する（Indirect充填）。
  Ni系の等価論文は別途存在する可能性がある。
* **充填の性質**: Indirect（類似Ni系での部分的実証は存在するが、NiCl₂(dpe)系での
  eqs (2)-(4)全ステップの完全な化学量論的実証を主題とする単独論文は同定困難）
* **Bibliographic confidence**: Medium（候補A: Tsou-Kochi 1979は知られた論文だが
  正確な内容の確認が必要；候補C: High, Pd系）
* **Filling adequacy confidence**: Medium（候補Aが酸化的付加のNi-dpe系での実証に
  あたるかは確認が必要；候補Cは間接的）
* **Verification recommendation**: [必須]
* **Bibliographic verification status**: pending
* **Filling timescale category**: field-methodology (5-15 yr)
* **注記**: EP-03aとの不可分共起（Stage 3 §6）。RI-06の解消（同型性実証）だけでは
  RI-03（中間体の直接観測）は解消されないため、EP-06aとEP-03aの両方の充填が
  VQ-3到達に必要。Pd触媒クロスカップリング機構の解明（1980年代）が
  Ni系の対応研究のtemplate/frameworkを提供した逆順の影響関係がある。

---

**EP-07a [Boundary-test pack]（第一群）**

* **充填するRI**: RI-07 (Unsupported boundary) — SRG-4（sp²制限の実験的根拠；
  塩化物/臭化物/ヨウ化物比較）
* **充填開始点（sp²制限の境界検証）**:
  Tamao, K.; Sumitani, K.; Kiso, Y.; Zembayashi, M.; Fujioka, A.; Kodama, S.;
  Nakajima, I.; Minato, A.; Kumada, M. *Bull. Chem. Soc. Jpn.* **1976**, *49*, 1958–1969.
  — Full Paper（Part I）にてsp²スコープの限界、sp³ハライドの反応性（不活性かどうか）、
  塩化物/臭化物/ヨウ化物の反応性順序に関するデータを提供する可能性（主要充填候補）。
* **充填確立点（候補）**:
  Hayashi, T.; Tajika, M.; Tamao, K.; Kumada, M. *J. Am. Chem. Soc.* **1976**, *98*,
  3718–3719. — 不斉Kumadaカップリング論文。sp²制限の機構的理解は別系統だが、
  Kumadaグループのスコープ研究のなかにsp³制限データが含まれる可能性がある。
  （タイトル・内容の確認要）
* **充填の性質**: Partial（Full Paperがsp²スコープの詳細化とsp³不活性の確認を
  含む可能性があるが、ep (ii)の PhCl/PhBr/PhI直接比較の明示的記述は確認要）
* **Bibliographic confidence**: High（候補1 = Full Paper、存在確実）；
  Medium（候補2 = タイトル推測域、確認要）
* **Filling adequacy confidence**: Medium（Full Paperがsp³ハライドの失敗例と
  ハライド系列比較データを含むかどうかは実際の論文内容の確認が必要）
* **Verification recommendation**: [必須]
* **Bibliographic verification status**: pending
* **Filling timescale category**: format-driven (1-5 yr)
* **注記**: Stage 3 §3で「RI-07 (SRG-4: sp²制限の失敗例不在)」がVQ-2未達の
  直接原因として記録されている。Full Paperがこれを解消すればVQ-2水準への
  到達が可能になる — EP-01aとのバンドル充填（Full Paper）によるVQ-2達成可能性と
  整合する。A-2 ↔ B-5ピボット構造（Stage 3 §6）の解消にも貢献する。

---

**EP-08a [Replication / uncertainty pack]（第三群）**

* **充填するRI**: RI-08 (Unquantified reliability) — SRG-6（cis/trans比）、SRG-3（収率）
* **充填候補**: **未同定**
* **充填の性質**: —（第三群; インセンティブ構造的未充填）
* **注記**: 代表的Kumadaカップリングエントリの収率を独立実験でn≥3測定して
  標準偏差を報告する専用論文は、新規性要求のある出版慣行のもとで独立論文化
  されていない（インセンティブ不整合）。技術的には可能だが、収率の統計的評価
  そのものを主題とする論文は存在しないと推定される。

---

**EP-09a [Internal benchmark pack]（第二群）**

* **充填するRI**: RI-09 (External superiority) — CLA-1（NiCl₂(dpe) vs Ni(acac)₂
  の直接比較）
* **充填開始点（候補A — Corriu/Masse続報）**:
  Corriu, R. J. P.; Masse, J. P. — 1972年Communication以降のFull Paper続報（特定不能）。
  Corriuグループは独立にNi(acac)₂触媒クロスカップリングを展開しており、
  同一基質での比較データを含む可能性がある。ただし、NiCl₂(dpe)との同一条件での
  直接比較を主題とした論文は特定できない。
* **充填開始点（候補B — 比較レビューまたは方法論比較論文）**:
  Hayashi, T.; Kumada, M. — 1970年代後半から1980年代にかけてのKumadaグループの
  触媒系比較研究（具体的なタイトル・巻号は同定困難）。
* **充填確立点**: 未同定（RI-09の直接充填論文の特定が困難）
* **充填の性質**: Indirect at best（同一条件での直接比較を主題とした独立論文は
  同定できず；配位子設計比較は後続の広範なクロスカップリング研究に分散している）
* **Bibliographic confidence**: Low（候補AもBも具体的な書誌情報を同定困難）
* **Filling adequacy confidence**: Low（充填論文の具体的対応が不明確）
* **Verification recommendation**: [必須]
* **Bibliographic verification status**: pending
* **Filling timescale category**: incentive-aligned (variable)
* **注記**: Note Added in Proof（Corriu/Masse 1972）が記録したNi(acac)₂問題（C-3）は、
  「bidentate diphosphineが必要条件か有効な選択肢か」という問いを直接検証する
  論文が当時出なかった可能性が高い。Pd触媒クロスカップリングの台頭によって、
  NiCl₂(dpe) vs Ni(acac)₂の直接比較という問いが社会的に消滅した可能性もある
  （「成功による問いの抹消」パターンの一変形）。

---

**§B 末尾チェック — Bibliographic verification（全候補, [必須] 適用）**

トリガー条件評価:
- (a) 論文年代: 候補の多数が1970年代 (pre-1980) ✓
- (b) 著者ネットワーク: Kumada lab から10報以上の関連論文 ✓
- (c) Named reaction: "Kumada coupling" — 著者名に由来 ✓

→ **全候補に Verification recommendation: [必須]** が適用される。

ハルシネーション警告パターン（本セットへの適用）:
- 著者組合せ捏造リスク: 同一グループ（Tamao/Hayashi/Kumada）内の著者の
  論文間混合に注意
- Kochi研究室のNi機構論文はタイトル確認が特に重要（内容が近い複数論文が存在）
- Stille 1977 Acc. Chem. Res.はレビュー論文であり、充填論文としては機能しない
  点を確認した（既に注記済み）

---

### §C 推奨選定リスト

| 順序 | 論文 | 充填するEP | VQ水準 | 年代 | Bib.Conf | Fill.Conf | Verification |
|------|------|-----------|--------|------|----------|-----------|--------------|
| 1 | Tamao et al., *Bull. Chem. Soc. Jpn.* 1976, 49, 1958–1969 | EP-01a, EP-02a, EP-05a(部分), EP-07a | VQ-2 | 1976 | High | High/Med | 必須 ⚠️ pending |
| 2 | Tsou & Kochi, *J. Am. Chem. Soc.* 1979, 101, 6319–6332 | EP-03a, EP-06a | VQ-3 | 1979 | Medium | Medium | 必須 ⚠️ pending |
| 3 | Yamamoto, T.; Yamamoto, A. (1970年代, 特定要) | EP-03a | VQ-3 | ca.1973–1977 | Low | Low | 必須 ⚠️ pending |
| 4 | Hayashi et al., *J. Am. Chem. Soc.* 1976, 98, 3718 | EP-04a, EP-07a | VQ-2/3 | 1976 | Medium | Low-Med | 必須 ⚠️ pending |
| 5 | Gillie & Stille, *J. Am. Chem. Soc.* 1980, 102, 4933 | EP-06a (Indirect) | VQ-3 (Indirect) | 1980 | High | Medium | 必須 ⚠️ pending |

⚠️ 全エントリが verification 待機中（Bibliographic verification [必須] 一括適用）

**選定理由:**

順序1（Tamao et al. 1976 Full Paper）が最優先。EP-01a, EP-02a のLetter→Full Paper
auto-resolution（C23）に加え、EP-07aのsp²境界検証とEP-05aの選択性データ改善を
含む可能性があり、VQ-2到達要件を複数EPについてバンドル充填する最高効率の
充填論文候補である。同一著者グループによる自己充填（原著者グループによる後続論文）
の典型例であり、通信→Full Paper遷移の最重要エントリ。

順序2（Tsou & Kochi 1979）が第二位。EP-03aとEP-06aの不可分共起（Stage 3 §6）を
考慮した場合、酸化的付加の化学量論的解析がSRG-1の部分充填として機能する
最も同定しやすいVQ-3層候補であるが、書誌確認が必須。

順序5（Gillie & Stille 1980）はPd系の還元的脱離論文であり、Ni-dpe系の
EP-06aへの直接充填ではなく間接充填に留まるが、VQ-3層における還元的脱離
理解の確立を示す客観的指標として位置付ける。

順序3（Yamamoto）は書誌確信度が低く、選定後の検証が特に重要。

全5報がVerification [必須]であり、post-hoc検証前は暫定リストとして扱う。

---

### §D VQ階層と充填時間順序の対応分析

**充填の時間軸:**

```
1972 原論文 (Tamao-Sumitani-Kumada, JACS Communication)
  ↓
1976 VQ-2 要件: EP-01a, EP-02a, EP-07a → [1976] Tamao et al., Bull. Chem. Soc. Jpn.
                [自己充填 / format-driven]
1976 VQ-2/3 中間: EP-04a (部分) → [1976] Hayashi et al., J. Am. Chem. Soc. [確認要]
                [自己充填 / field-methodology]
1979 VQ-3 要件: EP-03a, EP-06a (部分) → [1979] Tsou & Kochi, J. Am. Chem. Soc.
                [分野横断充填 / field-methodology]
1980 VQ-3 要件: EP-06a (Indirect) → [1980] Gillie & Stille, J. Am. Chem. Soc.
                [分野横断充填 (Pd系類推) / field-methodology]
1972- 未充填: EP-08a (VQ-4要件の統計的裏付け) → [インセンティブ構造的未充填]
              EP-09a (CLA-1: Ni(acac)₂との直接比較) → [低充填]
```

**階層-時間対応の評価:**

仮説「VQ階層が上がるほど充填に要する時間が長くなる」は、本論文の充填時間軸で
おおむね支持される。VQ-2要件（EP-01a, EP-07a）は4年（1972→1976）でfull-paperへの
自己充填によって到達されたのに対し、VQ-3要件（EP-03a, EP-06a）の部分充填は
7〜8年（1972→1979-1980）を要した。VQ-4要件（EP-08a）は2026年現在も未充填であり、
階層と時間の正相関が確認される。

ただし例外として、VQ-3層のEP-04a（cis/trans立体化学）は1976年の早期に
部分的に着手された可能性があり（Hayashi 1976 候補）、これは技術的難易度より
研究グループ内の並行展開が動因となったVQ-3の早期部分充填として解釈できる。

**特筆すべきパターン:**

1. **自己充填 — 原著者グループ内完結**: EP-01a/EP-02a/EP-07aは全てKumadaグループ
   自身による後続Full Paper（1976）での充填。通信→Full Paper遷移（C23）が
   最低VQ層を最短時間で充填する構造的パターンの典型例。これはgrant/競争的研究
   環境よりも「通信として先行発表した内容を詳細化する慣行」によって駆動される
   format-drivenパターンである。

2. **技術駆動充填 / 分野横断充填**: EP-03a/EP-06aは、Kochi研究室（独立グループ）
   による機構研究が原論文の機構的問いを外部から充填する分野横断充填パターン。
   Kochi研究室はNi・Cu・Feの有機金属反応機構を多数研究しており、この充填は
   Kumada論文が動機だったわけではなく、「同じ問いが別動機で研究された」証拠的
   相補性の検出事例として位置付けられる。

3. **VQ階層逆転の診断**: 最高優先度B項目（B-1, convergence=3/3, "selective"の
   定量的根拠 = SRG-2 = EP-05a）の充填確立が困難であり（第二群で充填確立点
   未同定）、一方でより高VQ層（EP-03a, VQ-3）の部分充填候補は同定できた。
   これは「科学的論理に基づく充填順序（VQ-2→VQ-3）」と「出版インセンティブに
   基づく実際の充填順序（VQ-3が先行するケース）」の逆転パターンの部分的観察
   として記録する。Kochi研究室がVQ-3を外部から充填した一方で、質量収支の
   完全定量（VQ-2 EP-05a要件の中核）は充填が曖昧なままであることがこの逆転を
   示す。

4. **Pd触媒台頭によるNi-Ni比較需要の消滅（EP-09a）**: 1970年代後半からPd触媒
   クロスカップリング（Heck, Negishi, Suzuki反応）の登場によって、触媒比較の
   関心がNiCl₂(dpe) vs Ni(acac)₂の比較からNi系 vs Pd系の比較へ移行した可能性がある。
   これによりEP-09aの充填需要が「成功による問いの抹消」パターンに準ずる形で
   低下したと推定される。

---

### §E 未充填EPの発見的意義

**未充填EP一覧:**

**EP-05a [Quantitative-ranking substantiation pack]（充填確立点 未同定）:**
* **未充填の理由**: **報告形式問題 + インセンティブ構造の不整合**。
  ホモカップリング生成物（R-R）を含む反応混合物の完全質量収支定量（GC-MS）は
  技術的に可能だが、(i) クロスカップリング論文の発表インセンティブは目的生成物の
  収率にあり、副生物の完全定量は慣例的に省略される、(ii) Full Paper（Tamao 1976）が
  収率の詳細化を行っても、eq (3)が予測するR-R生成物の明示的定量が含まれたかどうかは
  確認が必要。「selective」という主張の定量的根拠（SRG-2, B-1, convergence=3/3, 最高優先B項目）が充填確立未同定のまま残存することは、UQSが抽出したうちの最も重要な
  問いが最も確認困難であるという逆説を示している。
* **発見的意義**: あり。convergence=3/3（3エージェント全員がhigh評価）で同定された
  「選択性主張の定量的根拠の不在」（B-1）が、通信形式の慣行と出版インセンティブに
  よって充填されないまま科学コミュニティに受容されたとするなら、「selective Kumada
  coupling」という記述が60年以上にわたって完全な質量収支なしに科学文献に定着した
  という発見的意義を持つ。ただし、充填論文の実際の有無はVerification後に確定される。
* **将来の充填可能性**: 中 — 現代のGC-MS技術で任意のKumadaカップリング反応の
  質量収支を完全定量することは容易。ただし、1972年条件（NiCl₂(dpe), Et₂O）での
  再現実験という文脈で独立論文化するインセンティブは依然として低い。

---

**EP-08a [Replication / uncertainty pack]（インセンティブ構造的未充填）:**
* **未充填の理由**: **インセンティブ構造の不整合**。
  Kumadaカップリングの収率を同一エントリについてn≥3測定して標準偏差を報告する
  実験は技術的に単純だが、「既存の反応の統計的再現性確認」を主題とする論文は
  化学分野の出版慣行のもとで独立論文化されない。RI-08（Unquantified reliability）
  は合成化学分野全体で体系的に回避されてきた問いのカテゴリに属する。
* **発見的意義**: あり（分野慣行的回避）。合成化学における「収率の再現性と不確かさ」
  が1972年から現在まで独立論文化されていないことは、分野全体の慣行として
  UQS的観点から記録される。これはKumada論文固有の問題でなく、合成有機化学全体の
  RI-08的問いに対するインセンティブ構造的未充填パターンの事例として位置付けられる。
* **将来の充填可能性**: 低（独立論文化インセンティブが構造的に不在）。
  ただし、オープンサイエンス/再現性クライシスの文脈でロボット化合成や自動化実験が
  「再現性データ」を副産物として生成するようになれば、間接的に解消される可能性がある。

---

**EP-09a [Internal benchmark pack]（充填確立点 未同定）:**
* **未充填の理由**: **成功による問いの抹消（Success-driven question erasure, 変形）**。
  1970年代後半以降のPd触媒クロスカップリング（Heck, Negishi, Suzuki）の急速な発展が、
  Ni触媒系内部でのNiCl₂(dpe) vs Ni(acac)₂の比較という問いの検証需要を社会的に
  低下させた可能性がある。また、Corriu/Masse（Ni(acac)₂）系は後続発展が限定的で
  あり、「bidentate diphosphineが必要条件か」という問いへの関心そのものが、
  より優れたPd系の登場によって消滅した可能性がある。
* **発見的意義**: あり。Note Added in Proof（Corriu/Masse 1972, C-3）が記録した
  「NiCl₂(dpe) vs Ni(acac)₂の直接比較の欠如」は50年以上解消されなかった可能性があり、
  これを「Pd系の成功が引き起こしたNi系内部比較の放棄」として記録することは、
  触媒設計原理の歴史的理解に示唆を与える。
* **将来の充填可能性**: 高 — 現代のNi触媒クロスカップリング研究の文脈（Ni触媒の
  sp³-sp² カップリング等の再評価）でNi(acac)₂とNiCl₂(dpe)の比較が再び関心を
  集めている可能性があり、技術的充填は現代研究の副産物として実現しうる。

```
