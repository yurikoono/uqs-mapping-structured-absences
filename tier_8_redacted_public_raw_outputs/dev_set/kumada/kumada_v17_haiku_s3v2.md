prompt_version: stage3-v2-20260416
model_info: Claude Haiku 4.5 (claude-haiku-4-5-20251001)

# 科学的知見の再認定判定票

## Tamao, Sumitani, Kumada 1972（JACS Communication）

---

### §1 Claim Architecture

**コア主張：** ニッケル-ホスフィン錯体触媒を用いたGrignard試薬と有機ハロゲン化物のクロスカップリングが，ホモカップリングおよび不釣り合い化を回避しながら高い収率で進行する（Utility柱）。この反応は従来法では合成困難なアルキルベンゼン誘導体を1段階で与える新規合成法である（Novelty柱）。

**Layered structure:** YES。Novelty（新規触媒法）とUtility（合成的実用性）が独立層を形成。Novelty層のみが成立しても，Utilityは触媒の安定性・再現性で損傷可。逆に，Utilityが実証されてもメカニズムの不確実性はNoveltySub-claimsの強度を低下させる。この非対称性が特徴。

---

### §2 SRG / CLA → RI / ER / EP Crosswalk

**SRG-1 [機構サイクルの検証不在]** (U1, U2, U3由来)

* **Primary RI**: RI-03 (Unobserved explanatory)
* **Secondary RI**: RI-06 (Imported model), RI-11 (Mechanism-kinetics decoupling — 暫定)
* **ER**: 提案した触媒サイクル（式2–4）の各素反応ステップが，少なくとも速度論的制約（速度定数，活性化パラメータ）またはスペクトロスコピック検証（中間体確認）を受けて，反駁可能性のレベルで証拠付けされていなければならない。
* **EP**: EP-03a (Direct-observation / state-assignment pack); EP-10a (Kinetic verification pack)
* **Case-specific実装**: (a) ³¹P NMRによるニッケル錯体1, 2の温度可変追跡; (b) stopped-flow kinetics により酸化的付加（Hal-Ni)、RMgX付加、還元的脱離の各ステップの速度定数を個別に測定; (c) クロス結合／ホモ結合の速度比（k_cross/k_homo）の算出。
* **注記**: U1(diastereomeric TS), U2(intermediate detection), U3(anomalous selectivity). high_convergence_low_gap: V1-Q8(critical,critical), V1-Q9(high,high), low_convergence_high_gap: none. Convergence=1/3(U項目はTurn 4分類)。

**SRG-2 [選択性の定量的根拠不在]** (U4, U3, B17, B6由来)

* **Primary RI**: RI-04 (Unreplicated discriminator)
* **Secondary RI**: RI-05 (Qualitative overread)
* **ER**: クロス結合生成物（R-R'）とホモ結合生成物（R-R）の比率（少なくとも1つの基質について），および立体化学制御の機構（cis:trans比が速度論的か熱力学的制御か）が，定量的比較可能な形式で報告されていなければならない。
* **EP**: EP-07a (Boundary-test pack); EP-05a (Quantitative-ranking substantiation pack)
* **Case-specific実装**: (a) Table Iの各エントリについてGC-MS分析により粗反応混合物中のR-R', R-R, 異性体の定量; (b) 選択的例（cis:trans = 80:20）と非選択的例（43:57）について，温度・反応時間・溶媒を変化させた追跡実験で速度論的vs熱力学的平衡の特性化。
* **注記**: U4(selectivity quantification), U3(anomaly), B6(anomalous enrichment), B17(selectivity comparison absent). high_convergence_high_gap: B3に隣接。temperature_gap=medium (V2-Q3: critical, V3-OV4: high)。Convergence=2/3 (V2+V3)。

**SRG-3 [収率測定基準の混在と不確定性]** (B3, B4, B12, V3-Q1-3由来)

* **Primary RI**: RI-08 (Unquantified reliability)
* **Secondary RI**: RI-01 (Reporting integrity)
* **ER**: glpc収率と分離収率，および内部標準の種類・応答係数補正，が統一的に報告されており，異なる測定基準間の変換係数が明記されていなければならない。また，精密な定量的比較を前提とする主張（「高い収率」「選択的」）には，複数回測定と不確かさ記述が必須。
* **EP**: EP-01a (Reporting-coherence pack); EP-08a (Replication / uncertainty pack)
* **Case-specific実装**: (a) Table I再計測をglpc内部標準固定，検出方法(FID対MS)統一で実施; (b) 分離収率については再現性試験（n=3）と平均±SDを報告; (c) glpc収率については応答係数の直線性確認と外挿範囲の記載。
* **注記**: B3(yield basis mixing — critical,V3), B4(exothermic note), B12(and/or ambiguity). high_convergence_high_gap: B3 (V1=medium, V3=critical, gap=medium)。

**SRG-4 [リガンド効果と立体化学要件の推定]** (B1, V2-Q5, RI-05由来)

* **Primary RI**: RI-05 (Qualitative overread)
* **Secondary RI**: RI-06 (Imported model)
* **ER**: bidentate diphosphineの「cis配置が必須」という推定は，単なる活性相関（活性順位: dpp > dpe > dmpe）ではなく，各リガンドの立体パラメータ（Cone angle等）と複合体幾何学の直接的な相関を示す計算または結晶構造データに支持されていなければならない。
* **EP**: EP-05a (Quantitative-ranking substantiation pack); EP-06a (Analogy-validation pack)
* **Case-specific実装**: (a) 各リガンド複合体[NiCl₂(L₂)]の単結晶構造解析による幾何学確定; (b) 同一基質での複合体1, 2の²³¹P NMRスペクトル逆参照による立体配置確認; (c) 計算化学（DFT）による各複合体のフロンティア軌道と酸化的付加TS予測との相関。
* **注記**: B1(ligand ranking without mechanism). high_convergence_low_gap: none（単一agent）。 convergence=1/3 (V2-Q5のみ)。

**SRG-5 [スコープ陳述と実証スコープの乖離]** (B5, V1-Q1, V1-Q4, V1-Q6, V1-Q7由来)

* **Primary RI**: RI-07 (Unsupported boundary)
* **ER**: 「多様なGrignard」「様々な条件」という陳述は，二次アルキルGrignard，異なるリガンド（dpp等），異なる溶媒（THF等）の数値スコープデータで具体化されていなければならない。陳述スコープが実証スコープを超える場合，その超過部分は明示的に「将来の課題」と標識されるべき。
* **EP**: EP-07a (Boundary-test pack)
* **Case-specific実装**: (a) [NiCl₂(dpp)]/[NiCl₂(dmpe)]での各基質の相対収率を報告; (b) THFでの代表例の再試; (c) i-PrMgBr, c-HexMgBrでの改変スコープ実験。
* **注記**: B5(no secondary alkyl data), V1-Q1(other ligands not fully characterized), V1-Q4, V1-Q6/Q7(stoichiometry, solvent). high_convergence_low_gap: 複数のlow-severity項目。

**CLA (SRG外):** なし。SRG-1–5で網羅される。

---

### §3 現在のVQ判定

**現在判定: VQ-2 (Method)** [限定的]

**VQ-1 (Observation):** 通る。Table Iの10例について生成物の基本的な同定（bp, 屈折率, NMR; ただしand/orで不完全）と大まかな収率が報告されている。RI-02（Object identification）は「代替候補を排除できる粒度」に達していないが（立体異性体の詳細な構造確認なし），VQ-1の基本要件（「何が生成されたか」の粗い同定）は満たされている。非致命的。

**VQ-2 (Method):** 通る（ただし限定的）。RI-01（Reporting integrity）について，収率基準が混在しているが（glpc対分離），それぞれのカテゴリ内では一貫している。また，実験手順（Examples 1-2）は再現に必要な基本データを含んでいる。しかし，**RI-07（Unsupported boundary）が残存：スコープ陳述（「多様」「可能」）の実証範囲が限定的である。** RI-02の継承に関し，非致命的欠落。判定根拠：基本的な実験プロトコル（試薬比，反応時間，温度範囲）は記載されており，再現可能性は低リスク。スコープの陳述超過は慎重さの不足，方法の無効ではない。

**VQ-3 (Mechanism):** 未達。理由：
- RI-03（Unobserved explanatory）: 触媒サイクルの素反応ステップ（中間体1, 2）が直接観測も速度論的拘束も受けていない（致命的）。
- RI-06（Imported model）: 式1, 3の「確立された事実」は参考文献11–13に帰属されているが，その参考文献自体は速度論的データを含まない（致命的）。
- RI-11（Mechanism-kinetics decoupling）: 提案サイクル（式2–4）から速度式が代数的に導出されておらず，観測速度次数との一致確認も行われていない（致命的）。

VQ-3への昇格には，EP-03a (Direct-observation pack) と EP-10a (Kinetic verification pack) の投入が最小限必須。

**VQ-4 (Benchmark):** 未達。VQ-3が未達のため，自動的にVQ-4も未達。仮にVQ-3に到達した場合でも，RI-08（Unquantified reliability）と RI-09（External superiority）を解消する必要がある（内部反復測定の追加，Tamura-Kochi系との同一基質での直接比較）。

---

### §4 Era-Norm Annotation

**communication-era tolerated:**
- B3, B4, B12 (Reporting ambiguity, yield basis): 1972年JACS Communication形式では2.5ページ制約が標準。詳細な分析条件記載は通常，ESIやFull Paperに後送される慣例。
- B7, B1, B5 (Solvent/ligand/scope claims without data): Communication形式では初期発見の速報が優先され，完全なスコープ報告は次報に期待される文化的規範。
- A1, A2 (Conditions not optimized, further studies needed): 注記的な免責事項は通信論文の定型フレーズであり，当時は方法論的誠実さの表現と見なされた。

**modern-era deficient:**
- U1, U2, U3 (Unobserved intermediates, mechanism without evidence): 現代の触媒化学では，提案サイクルに対する最小限の速度論的検証（初速度測定，stopped-flow，温度依存）が基本的要件。NMRによる中間体追跡も標準技術として確立。
- SRG-2 (Selectivity unquantified): 「選択的カップリング」という中心的主張が定量的根拠（クロス:ホモ比）なしに陳述されることは，現代基準では受け入れがたい（定量基準：>95%を「高選択性」と見なす慣例）。
- SRG-1 + SRG-4 (Mechanism+ligand effect): 1972年当時，計算化学（DFT）は存在せず，立体パラメータ（Cone angle）の確立も1970年代後半。RI-06の「Imported model」適用は，当時の知識体系では適切だったが，現代ではDFT検証が必須。Era-dependent on both theoretical access and field expectations.

---

### §5 最短補強ルート

**目的関数: VQ-3への昇格**

1. **EP-03a (Direct-observation / state-assignment pack)** — 常温²³¹P NMRによる [NiCl₂(dpe)] + PhMgBr + PhCl 混合系の追跡で，中間体L₂NiPh₂ (1) およびL₂Ni(Ph)(Cl) (2) の信号を時間分解観測。RI-03の直接検証により，機構仮説の検証可能性を確立。

2. **EP-10a (Kinetic verification pack)** — 代表例（PhMgBr + PhCl）について初速度法（PhCl濃度変化，PhMgBr濃度変化，[NiCl₂(dpe)]変化）を実施し，観測速度次数を決定。RI-11 (Mechanism-kinetics decoupling) の直接解消。

3. **EP-07a (Boundary-test pack)** — [NiCl₂(dpp)]での同一基質スコープ（最小3例）を補充。RI-07 (Unsupported boundary) の部分的解消。

4. **EP-05a (Quantitative-ranking substantiation pack)** — 粗混合物GC-MS分析により，全Table Iエントリについてクロス:ホモ比を定量化。RI-04, RI-05の同時解消。

**認定ゲート順注記:** 実験投入は上記優先度順だが，VQ-3認定は VQ-1 → VQ-2 → VQ-3 の順序で段階的に通過する必要がある。VQ-1継承要件（RI-02の非致命性確認）を再確認してからVQ-2に進み，VQ-2合格後にRI-03, RI-06, RI-11の三点セットが同時に解消することを確認してVQ-3進行。

---

### §6 制度設計への寄与

**既存RI code の新しい代表事例:**
- RI-03 (Unobserved explanatory): 触媒機構の「中間体が予測されるが直接検証されない」ケースの典型事例。触媒化学全般で高頻出パターン。
- RI-06 (Imported model): 参考文献から「確立された事実」として他系のモデル（σ-allylic metalキャラクタリゼーション）を輸入するが，同型性検証なしというパターン。構造類似性による推論の一般的陥穽を示す。
- RI-11 (Mechanism-kinetics decoupling): 暫定PRIとして昇格の可能性を高める事例。提案サイクルが観測速度と「一致する」ように見えるが，実は複数の異なるサイクルが同じ速度式を与える可能性の未排除。

**新規PRI候補:**
不検出（「触媒が分解しない」と陰性証拠から推定）と肯定的機構証拠の混同。本論文では「ホモ結合が検出されず，したがって選択性は高い」と読めるが，検出下限が報告されていない。**PRI-12案: "Negative-evidence thresholding"** — 「検出限界値未記載で陰性結果を肯定的機構証拠として使用」。2報以上の独立確認で昇格検討。

**VQ判定基準への知見:**
Communication形式での「メカニズムは後回し」という戦略的選択の正当性。VQ-2には到達できるが，VQ-3昇格に必要なRI要件（RI-03, RI-06の致命性）は形式に依存しない本質的欠落。Era-normはVQ-2までの許容範囲を規定するが，VQ-3の致命性は時代不問。

**EP辞書への追加:**
EP-10a (Kinetic verification pack) の Ni系触媒への case-specific実装例を追加。「³¹P NMR stopped-flow追跡 + 初速度測定による速度式導出」は，Pd系のEP-10a実装と異なるニッケル固有のセットアップ（例：σ複合体の化学シフト範囲，T1緩和時間特性）を提供する。

---

inference_time_sec: not available — inject externally
