<!-- model_info: claude-haiku-4-5-20251001 -->
prompt_version: stage3-v4-20260427

# 科学的知見の再認定判定票

## Tamao, Sumitani, Kumada 1972（Journal of the American Chemical Society, Communication）

### §1 Claim Architecture

**コア主張：**
遷移金属触媒（特にニッケル-ジホスフィン錯体）を用いた Grignard 試薬と有機ハロゲン化物の選択的クロスカップリング反応を報告する。提案システムは、(1) 従来困難であったホモカップリング・不均化を抑制し、(2) β 水素含有 Grignard 試薬を許容し、(3) sp² 炭素ハロゲン化物（特に塩化物）で高収率（76–98%）を達成する。

**新規性柱：** ニッケル-ジホスフィン触媒による高選択的クロスカップリング
**有用性柱：** 合成実務上、従来困難だった不飽和化合物を 1 段で製造可能

**Layered structure の有無と構造：**
YES — 本論文の成否は 2 つの独立層に依存し、層間に相互依存がある。

- **層 1（触媒層）**: ニッケル-ジホスフィン錯体が機能する触媒である
- **層 2（選択性層）**: クロスカップリング生成物が優先的に生成され、ホモカップリング・不均化が定量的に抑制されている

両層が同時に成立してはじめて「新しい有用な合成法」という主張が立つ。もし層 2 が成立しない（実は副生成物が相当量生成されている）なら、層 1 の触媒活性だけでは応用価値が失われる。論文の success criteria はこの層間の相互依存を前提としており、結果的に **単一の反証が全体主張を覆す脆弱な構造** を持つ。

---

### §2 SRG / CLA → RI / ER / EP Crosswalk

#### Stage 1 Turn 4 同根グループ（SRG）の取得と RI マッピング

**SRG-1: Product selectivity と byproduct suppression の定量的不在**
（B6, U1, V1-Q7, V1-Q8, V2-Q8, V3-Q2, V3-Q6）

* **Primary RI**: RI-04 [Unreplicated discriminator]
  — Table I が最終分離収率のみ報告し、粗反応液の成分分析（glpc での相対ピーク面積、¹H NMR による R–R / R–R' / R'–X の定量）が欠落。クロスカップリング生成物が本当に選択的であるのか、副生成物が 1% 以下（検出限界以下）にあるのか、5% あるのかが判別不能。「高選択性」という順位主張は単一の分離収率によるのみであり、再現性データなし。

* **Secondary RI**: RI-05 [Qualitative overread]
  — 「高選択性」という主張が定性的順位付け（収率のみ）から導出されており、競争反応の相対速度や活性化エネルギー差が示されていない。

* **ER**: 粗反応液の glpc 分析で内部標準（既知量の内部参照物質）を用い、各化学種（R–R', R–R, R'–X, その他）のピーク面積を測定し、% yield in crude mixture と % selectivity を報告。あるいは ¹H NMR による定量アロマティック統合で同等の目的を達成。

* **EP**: EP-05a [Quantitative-ranking substantiation pack]

* **Case-specific 実装**: 
  glpc メソッド：FID 検出、OV-101 カラム 25 m、内部標準（例：n-tetradecane 既知 mg）、各化学種の response factor（キャリブレーション標準による）を記録。分析対象：Example 1 の粗抽出物（蒸留前）の glpc を記録。ピーク（m-di-n-butylbenzene [主]、n-butylbenzene [未反応]、n-BuBr [未反応]、di-n-butyl [ホモ]、その他）の相対面積から % selectivity を算出。

* **注記**: TEMPERATURE_SUMMARY に high_convergence_low_gap として標識（B6: convergence 3/3, temperature_gap=none）。多機関合意（V1, V2, V3 全員が high severity フラグ）により根的深さが確認。

---

**SRG-2: Catalyst intermediates と cycle kinetics の未特性化**
（B8, U4, V1-Q10, V2-Q2, V2-Q3, V2-Q4, V2-Q11）

* **Primary RI**: RI-03 [Unobserved explanatory]
  — 提案される中間体（L₂NiR₂ as 1, L₂Ni(R')(X'') as 2, L₂Ni(R'')(R''') as 3）は論文中に構造式で示されるが、NMR（¹H, ¹³C, ³¹P）または ESI-MS による直接観測が実施されていない。特に、diphosphine の coordination geometry（cis か trans か）は「cis 必須」と主張されるが、対応する ³¹P NMR 化学シフト、coupling constant、あるいは XRD 構造が報告されていない。

* **Secondary RI**: RI-06 [Imported model]
  — 触媒サイクル全体が「一般的な σ-organonickel chemistry」の類推により構成されており、本反応系での in-situ 検証がない。先行文献（Chalk & Harrod 1965, Sommer et al. 1969）の hydrosilylation メカニズムが、異なる反応（cross-coupling）に適用されている。

* **ER**: (a) 反応混合物の ¹H NMR, ¹³C NMR, ³¹P NMR を in-situ で測定し、中間体 1, 2 の formation/decay を観察。特に ³¹P NMR で diphosphine の coordination shift と coupling pattern から geometry 判定。(b) ESI-MS で [L₂Ni(R)]⁺ 等の m/z 確認。(c) または NiCl₂(dpe) に Grignard を加えた際の色変化・NMR 変化をトラップ実験で記録。

* **EP**: EP-03a [Direct-observation / state-assignment pack]; EP-10a [Kinetic verification pack]

* **Case-specific 実装**: C₆D₆ 中で NiCl₂(dpe) に PhMgBr を加え、¹H NMR で reaction mixture をリアルタイム測定。³¹P NMR で ligand resonance shift を記録（free dpe との比較）。Ni complex の生成率を ¹H NMR 積分で定量し、time-course curve を取得。

* **注記**: V2-Q2, V2-Q3 で high severity に標識。TEMPERATURE_SUMMARY の high_convergence_low_gap ポジション（linked_items: B8 ↔ U4）で確認。

---

**SRG-3: Mechanistic basis for catalyst/ligand effects と selectivity の未提供**
（B2, U2, U3, U5, V1-Q2, V1-Q3, V1-Q4, V2-Q5, V2-Q6, V2-Q7）

* **Primary RI**: RI-05 [Qualitative overread]
  — ligand activity order（dpp > dpe > dmpe « PPh₃, ~100倍の幅）が報告されるが、定性的記述のみ。ΔG‡, ΔH‡, ΔS‡（Eyring parameters）が各配位子について測定されていない。活性の差が transition-state stabilization に由来するのか ground-state stabilization か、あるいは pre-exponential factor A の差か Ea の差かが不明。また「cis configuration が必須」という主張は配位子 geometry から推定されるのみで、実構造に基づかない。

* **Secondary RI**: RI-01 [Reporting integrity]
  — mechanistic 説明（Equations 2–4）が条件記述なく事実的述調で提示される。例：「[REDACTED: verbatim source text; see the source paper via its DOI]」は仮説的トーン（「forms と推定される」）ではなく断定的（「forms」）。

* **ER**: 各配位子（dpp, dpe, dmpe, PPh₃）について温度可変速度論を実施し、Arrhenius plot から Ea および log A を算出。Eyring plot から ΔG‡, ΔH‡, ΔS‡ を決定。activity 差の物理化学的基盤を明示。

* **EP**: EP-10a [Kinetic verification pack]

* **Case-specific 実装**: 各配体での m-dichlorobenzene + n-BuMgBr coupling を 3–4 温度で実施（例：25°C, 35°C, 45°C, 55°C）。初期速度 v₀ を ¹H NMR で定量（aromatic H の積分変化）。Arrhenius plot: ln(k) vs 1/T で Ea 算出。Eyring plot: ln(k/T) vs 1/T で ΔG‡, ΔH‡, ΔS‡ 算出。³¹P NMR で coordination shift が温度依存するか測定（dynamic NMR による exchange kinetics の可能性確認）。

* **注記**: V1-Q2 high, V2-Q2 high, B2 high_convergence_low_gap (convergence 2/3, temperature_gap=none)。cis/trans selectivity との複合根（U2）も同グループに集約される。

---

**SRG-4: Quantitative yield accounting と analytical validation の不完全性**
（B7, B12, V1-Q9, V3-Q1, V3-Q3, V3-Q4, V3-Q5, V3-Q9, V3-Q10）

* **Primary RI**: RI-08 [Unquantified reliability]
  — Table I の全 11 エントリが単一実験のみ報告（n=1）。Example 1（m-di-n-butylbenzene）の分離収率 94% は、出発 dichlorobenzene ベースであり、残り 6% の物質収支が説明されない。「9.63 g, 94%」は計算値であるが、粗生成物の初期質量が記載されていない。複数回の実験による error bars や SD が報告されていない。

* **Secondary RI**: RI-02 [Object identification]
  — 分離生成物の純度が「pure m-di-n-butylbenzene」と断定されるが、純度測定方法が明記されていない。蒸留によるのみでは co-distilling impurities の除外不完全。¹H NMR integral による purity assay, glpc area% 等の検出方法が欠落。また、全 Table I の生成物のうち、多くは bp と n_D のみで特性化されており、¹H NMR, ¹³C NMR, MS が多くの生成物について報告されていない。

* **ER**: Replication: Example 1, 2 を各 n≥3 で繰り返し、mean yield ± SD を報告。Mass balance: crude extraction 後の総質量を記録。蒸留後の residue（bp range 外の溜分）を回収・秤量し、「出発物質（g）→ 蒸留溜分（g）+ residue（g）」の全体収支を示す。Purity: 蒸留後の主溜分を glpc で分析（FID, internal standard）。peak area% で purity を定量。あるいは ¹H NMR aromatic-region integration で purity 算出（standard との比較）。Product characterization: 全 Table I 化合物について ¹H NMR, ¹³C NMR, MS(m/z 主ピークと fragmentation pattern) を記録。

* **EP**: EP-08a [Replication / uncertainty pack]; EP-02a [Identity / purity substantiation pack]; EP-01a [Reporting-coherence pack]

* **Case-specific 実装**: Example 1 (m-di-n-butylbenzene): 粗抽出物：蒸留前に全質量測定（例：x g）。蒸留溜分（84°C, 5 mm）：y g（例：9.63 g）。Residue（蒸留後釜残）：z g。物質収支：x = y + z。Purity: 溜分 y を glpc（内部標準 1 mg 既知量）で分析、peak 面積から% purity。Replicate: 同一条件で n=3 実行、mean 94% ± SD を報告。

* **注記**: B7, B12 が high_convergence_high_gap に分類（温度ギャップ中程度）。V3-Q1, Q3 で high severity。

---

**SRG-5: Scope limitations が mechanistic / kinetic 正当化なく提示**
（B1, B13, V1-Q1, V1-Q11, V1-Q12, V2-Q9）

* **Primary RI**: RI-07 [Unsupported boundary]
  — 論文は「[REDACTED: verbatim source text; see the source paper via its DOI]」と述べるが、なぜ Csp³ ハロゲン化物が失敗するか、あるいは試されたのか未報告。Csp² restriction が thermodynamic か kinetic かが不明。また、Grignard 試薬スコープは「primary/secondary alkyl, aryl」に限定されており、allyl, propargyl, conjugated-diene Grignard が試されたか明記されない。

* **Secondary RI**: RI-05 [Qualitative overread]
  — substrate-specific remarks（「high yields are obtained even from...β-hydrogen atoms」）が定性的記述のみで、systematic variation（electronic effects など）がない。

* **ER**: Csp³ 探索：primary alkyl halide（例：n-octyl bromide）および secondary alkyl halide（例：cyclohexyl bromide）を added test として実施し、反応性（収率 or 転化率）を測定。Grignard 多様性：allylMgBr, propargylMgBr を試行。Electronic variation：p-MeO-PhCl, p-CF₃-PhCl を aromatic halide として試し、electronics との相関を検証。

* **EP**: EP-07a [Boundary-test pack]

* **Case-specific 実装**: Example 1 の条件を保持し、n-octyl Br を有機ハロゲン化物として試行（Table I の variant）。転化率と selectivity を glpc で測定。α-naphthylMgBr の代わりに allylMgBr（条件 B）を試行。

* **注記**: V1-Q1, V1-Q11, V1-Q12 で medium severity。SRG-5 は SRG-1–4 ほど高温度ではないが、scope 定義の清晰性に関する structural gap。

---

#### SRG 外：CLA（Claim-level Adjunct）

**CLA-1: Byproduct suppression claim vs 検出不実施**
（D4-C1; grounded in U1, B6）

* **Primary RI**: RI-04 [Unreplicated discriminator]
* **Secondary RI**: RI-05 [Qualitative overread]
* **ER**: 粗反応液成分分析により、R–R', R–R, R'–X, disproportionation products の % 定量
* **EP**: EP-05a [Quantitative-ranking substantiation pack]

論文が「[REDACTED: verbatim source text; see the source paper via its DOI]」と自ら motivation を述べているにもかかわらず、その主張の reverse（本触媒でホモカップリングが抑制される根拠）を提供していない。これは自己矛盾的不在（U1）であり、CLAとして独立記録。

---

**CLA-2: Stereochemistry anomaly 未解明**
（D4-C2; grounded in U2）

* **Primary RI**: RI-03 [Unobserved explanatory]
* **Secondary RI**: RI-05 [Qualitative overread]
* **ER**: Reaction progress 解析（¹H NMR time-course）：cis と trans starting material 各々について、反応時間関数としての cis/trans ratio in product を測定。In-situ NMR による π-alkenyl intermediate geometry assignment（¹³C NMR alkenyl-carbon signals, coupling pattern）。
* **EP**: EP-10a [Kinetic verification pack]; EP-03a [Direct-observation / state-assignment pack]

論文が「anomalously enriched with the cis isomer」と異常性を明記しながら、その機構的説明を放棄している点がCLA化。提案される触媒サイクル（Eq. 2–4）では π-alkenyl intermediate が定義された幾何を持つはずなのに、観測結果が予測と矛盾する。

---

**CLA-3: β-Hydride suppression メカニズム不在**
（D4-C3; grounded in U3）

* **Primary RI**: RI-03 [Unobserved explanatory]
* **Secondary RI**: RI-05 [Qualitative overread]
* **ER**: Deuteration experiment: d₃-n-BuMgBr（CD₃CH₂CH₂MgBr）を用いて、coupling 後に product mixture を ¹H NMR/GC-MS で分析。Kinetic competition: β-hydride elimination kinetics vs reductive coupling kinetics の相対値を検出。
* **EP**: EP-10a [Kinetic verification pack]

提案メカニズムでは Ni–R 結合が formed され、β-hydride 脱離は standard pathway のはずだが、論文は「高収率」という現象的観察のみから β-hydride 許容性を主張している。

---

**CLA-4: Resting state と rate-limiting step 未確定**
（D4-C4; grounded in U4）

* **Primary RI**: RI-03 [Unobserved explanatory]
* **ER**: Initial-rate kinetics による reaction order 決定：[Ni], [Grignard], [RX] 各々の order を測定。Intermediate abundance 推定：¹H NMR で時間経過に伴う intermediate signals の accumulation を追跡。
* **EP**: EP-10a [Kinetic verification pack]

---

**CLA-5: Ligand activity 定量的解釈の欠落**
（D4-C5; grounded in B2）

* **Primary RI**: RI-05 [Qualitative overread]
* **Secondary RI**: RI-01 [Reporting integrity]
* **ER**: 各配位子の Arrhenius/Eyring parameters 測定、ΔG‡ 差から ground-state vs transition-state effect 分別
* **EP**: EP-10a [Kinetic verification pack]; EP-03a [Direct-observation pack]

論文が「[REDACTED: verbatim source text; see the source paper via its DOI]」と **構造的根拠を述べながら**、その構造を確認していない点。

---

**CLA-6: Experimental 検証の体系的不足**
（D4-C6; grounded in B7, B12）

* **Primary RI**: RI-08 [Unquantified reliability]
* **Secondary RI**: RI-02 [Object identification]
* **ER**: SRG-4 と同一（replication, mass balance, purity）
* **EP**: EP-08a, EP-02a, EP-01a

---

**CLA-7: Tamura–Kochi との定量比較欠落**
（D4-C7; grounded in C1）

* **Primary RI**: RI-09 [External superiority]
* **ER**: 同一基質で両触媒系を並行実施。PhMgBr + PhCl を [NiCl₂(dpe)] vs Fe(acac)₃ (Tamura-Kochi) で反応させ、yield, selectivity, reaction time, TON/TOF を直接比較。
* **EP**: EP-09a [Internal benchmark pack]

---

### §3 現在のVQ判定

#### Step 3a: Modern reassessment baseline での判定

**VQ-1 (Observation) — 必須 RI-02 の通過判定:**

RI-02 [Object identification] status: 生成物特性化は bp, n_D による文献値との一致に限定。¹H/¹³C NMR, MS が多くの化合物で未報告。蒸留後の純度測定方法が未記載。

**判定: RI-02 未解消 → VQ-1 NOT REACHED**

理由：多くの有機化合物の構造確認は ¹H NMR の aromatic region integration や MS fragmentation に依存する。bp と n_D は既知化合物の確認には有用だが、新規または複雑な生成物の構造唯一性を保証しない。

---

**VQ-2 (Method) — 必須 RI-01, RI-07 の通過判定:**

VQ-1 継承：未達のため、VQ-2 も原理的に未達
RI-01 [Reporting integrity] status: Yield 報告に SD, error bars なし。GLC 方法論（内部標準, response factors）未詳細。
RI-07 [Unsupported boundary] status: Csp² halide restriction の mechanistic explanation なし。

**判定: RI-01, RI-07 未解消 → VQ-2 NOT REACHED (modern baseline)**

**ただし，VQ-2 (era-norm qualified):** JACS Communication 形式（通常 2–3 ページ）では、detailed GLC method documentation や replication data table は ESI に委譲されるのが慣行。1972 年当時、ESI システムが存在しなかった場合、communication 形式での analytical detail 削減は journal constraint として許容されていた。

---

**VQ-3 (Mechanism) — 必須 RI-03, RI-04, RI-06 の通過判定:**

VQ-2 継承：未達のため、VQ-3 も原理的に未達

RI-03 [Unobserved explanatory] status: 提案中間体（1, 2, 3）の直接観測（NMR, MS）なし。β-hydride suppression メカニズム未説明。cis 幾何の structural 根拠なし。

RI-04 [Unreplicated discriminator] status: 配位子活性順序は単一実験ベース。Reaction-progress 分析なし。

RI-06 [Imported model] status: Catalytic cycle が既存 Ni(II) literature from hydrosilylation analogy に基づく。本反応系での in-situ kinetic/spectroscopic 検証なし。

**判定: RI-03, RI-04, RI-06 未解消 → VQ-3 NOT REACHED**

---

**VQ-4 (Benchmark) — 必須 RI-08, RI-09 の通過判定:**

RI-08 [Unquantified reliability] status: Replication data なし。Mass balance 不完全（6% 未説明）。

RI-09 [External superiority] status: Tamura-Kochi との定量比較なし。

**判定: RI-08, RI-09 未解消 → VQ-4 NOT REACHED**

---

#### Step 3b & 3c: Final VQ Judgment

| VQ Level | Modern Baseline | Era-Norm Adjusted | Rationale |
|:---------|:----------------|:-----------------|-----------|
| VQ-1 | NOT REACHED | (unchanged) | RI-02 (product identification by bp/nD insufficient) |
| VQ-2 | NOT REACHED | **(era-norm qualified)** | RI-01, RI-07 — communication format tolerated analytical abbreviation |
| VQ-3 | NOT REACHED | (unchanged) | RI-03, RI-04, RI-06 remain unresolved regardless of publication format |
| VQ-4 | NOT REACHED | (unchanged) | RI-08, RI-09 unresolved |

**最終判定：VQ-2 (era-norm qualified) — 1972 年 JACS Communication 規約下では許容、2025 年基準では VQ-2 未達**

---

### §4 Era-Norm Annotation

#### communication-era tolerated:

**B6 [Product selectivity data omission]:**
Communication 形式（2 ページ）では crude-reaction-mixture product-distribution analysis を supplement に委譲するのが慣行。1972 年当時、supporting information システムが不確定だったため、data condensation は容認された。[Communication brevity convention]

**B12 [GLC method details]:**
内部標準の identity, response-factor calibration, detection limit は当時の journal culture で peer reviewer との personal communication に依存することが多かった。[Analytical detail verbosity expectation shift]

**B8 [Intermediate NMR characterization]:**
提案メカニズムの mechanistic detail は communication でしばしば "working hypothesis" 扱いで、full paper での実験検証を予期するのが normal。本論文末尾の disclaimer「[REDACTED: verbatim source text; see the source paper via its DOI]」がこれを反映。[Genre convention: proof-of-concept first, mechanism second]

#### modern-era deficient:

**B2 [Ligand activity order without kinetics]:**
Eyring equation（1935 年発表）は 1972 年に既知技術。~100 倍の activity span は Ea 差（通常 5–10 kcal/mol 相当）として解釈可能。activation energy 測定の欠落は技術的制約ではなく deprioritization。[Kinetic methodology available but not deployed]

**B3 [Cis/trans stereoselectivity anomaly]:**
Reaction-progress analysis by GC-FID or ¹H NMR time-course は 1972 年に standard protocol。stereochemical control（kinetic vs thermodynamic）の区別は 40 年以上前から可能。[Probe accessible in 1972 but unrealized]

**B4 [Solvent effect mechanism]:**
Solvation equilibria と reaction-coordinate coupling は 1972 年物理化学の canonical テーマ。定量的説明の欠落は deliberate。[Mechanistic model available]

**B7 [Mass balance / purity documentation]:**
既に 1972 年でも isolation yield の 100% 達成困難時は "unaccounted material" の記載が standard practice だった。「9.63 g, 94%」と crude→distilled mass の関係が不透明なのは、era-standard に対しても deficient。[Standard rigor absent even by era norm]

---

### §5 最短補強ルート

**現在の VQ 水準：** VQ-2 (era-norm qualified)
**第一目的関数：** VQ-3 到達（Mechanism 認定）

#### VQ-3 への最短ルート：

**1. EP-10a (Kinetic verification pack)** — 優先度最高
   - Case-specific: m-Dichlorobenzene + n-BuMgBr coupling を 4 温度（25, 35, 45, 55°C）で実施。Initial-rate v₀ を ¹H NMR で測定。[Grignard], [RX], [Ni(dpe)]² の各 order を決定。Arrhenius plot (ln k vs 1/T) → Ea; Eyring plot → ΔG‡, ΔH‡, ΔS‡。配位子比較：dpe (Ea ≈ X kcal/mol) vs dpp (Ea ≈ X–10 kcal/mol) で activation energy gap を定量化。
   - RI 前進：RI-03, RI-04, RI-06
   - 情報利得：Single EP で 3 つの致命的 RI を同時に進捗

**2. EP-03a (Direct-observation / state-assignment pack)** — 並行実施推奨
   - Case-specific: NiCl₂(dpe) の NMR（¹H, ¹³C, ³¹P NMR を C₆D₆ 中で記録）。NiCl₂(dpe) + 1 equiv. n-BuMgBr → 色変化観察。生成物混合物の ¹H NMR, ³¹P NMR を room temp. で記録。³¹P NMR coupling constant (²J_PP) から diphosphine geometry（cis vs trans）の determination。
   - RI 前進：RI-03, RI-06
   - 付随的効果：CLA-2 (cis/trans selectivity anomaly) の partial insight

**3. EP-08a (Replication / uncertainty pack)** 
   - Case-specific: Example 1, 2 を各 n=3 で実施。mean yield ± SD を記載。各実験について glpc chromatogram を記録。
   - RI 前進：RI-08, RI-04

**4. EP-02a (Identity / purity substantiation pack)** 
   - Case-specific: 全 Table I 化合物について ¹H NMR, ¹³C NMR, GC-MS を記録。蒸留後の main fraction について glpc purity, elemental analysis を実施。
   - RI 前進：RI-02

**5. EP-07a (Boundary-test pack)** 
   - Case-specific: n-octyl Br, cyclohexyl Br での coupling を試行。p-MeO-PhCl, p-CF₃-PhCl を aromatic halide として試行。
   - RI 前進：RI-07

**6. EP-09a (Internal benchmark pack)** 
   - Case-specific: PhMgBr + PhCl を [NiCl₂(dpe)] と Fe(acac)₃ で parallel reaction。TON, TOF を計算。
   - RI 前進：RI-09

認定ゲート順注記：実験投入順は情報利得・実行可能性に基づく（kinetics → spectroscopy → analytics）。最終的な VQ 認定は継承原則（VQ-1 → VQ-2 → VQ-3 → VQ-4）に従い、下位水準が達成されてはじめて上位認定が成立する。

---

### §6 制度設計への寄与

**RI-05 (Qualitative overread) — 「配位子スクリーン without kinetics」の canonical example として確立。**

本論文の ligand activity order（dpp > dpe > dmpe « PPh₃, ~100倍）は modern catalysis literature で最も頻繁に参照される early example。この成功（high-impact communication, Kumada group status）が後続 50 年の synthetic-method literature に **quantitative ranking without kinetic foundation** を implicitly authorize した可能性がある。

Codebook recommendation: RI-05b subtype「Ranking-to-structure overclaim」を正式化。定義：「多段階（>5 倍）の quantitative 順位付けが報告されるが、activation energy, rate constant, または pre-exponential factor の discriminatory data が欠落し、属性（geometry, coordination, steric）への帰属が推測に基づく」。

---

**PRI-11 (Mechanism-kinetics decoupling) の formal codebook entry を推奨。**

定義：「Catalytic cycle or elementary step sequence が proposed and named (intermediates 1, 2, 3 等)、段階的 description が given、しかし rate law、rate-limiting step identification、temperature dependence が測定されていない結果、proposed cycle が rate-determining step を含むのか、どの中間体が accumulate するのか、on-cycle / off-cycle の区別が原理的に indeterminate のままである。」

本論文は PRI-11 の perfect textbook case：3-step cycle が述べられ、equation 2–4 で visualize されるが、rate law がないため「Ni–R formation が rate-determining か、reductive elimination が rate-determining か」が solved されていない。

---

**PRI-12 (Structural validation deficiency) — Cluster A (Self-referential validation), Subtype A6 (Parameter portability overclaim).**

「cis configuration is the first requisite」という claim は、diphosphine ligands の intrinsic property（bidentate chelation は typically cis）から inferred。しかし active Ni-intermediate の actual geometry が cis であるか、それとも dynamic equilibrium を持つか、または transition state が cis であるかが structured 證拠なく asserted。

Codebook update: A6 subtype「Parameter portability overclaim」に Kumada 1972 "cis requirement" を representative example として登録。

---

**新規パターン：標識不整合（Labeling mismatch）。**

論文の mechanism section：「[REDACTED: verbatim source text; see the source paper via its DOI]」は indicative mood（事実述調）で mechanistic pathway を describe。その後、finale：「[REDACTED: verbatim source text; see the source paper via its DOI]」として limitation を back-disclaim。

Rhetorical flow: (proposes detailed mechanism in indicative) → (end-acknowledges it is speculative)

Recommendation：This pattern を「prospective-claim-with-retrospective-caveat」として note。Modern style では caveat を up-front に place する（「我々は以下の speculative cycle を propose する」）が、1972 communication では forward narrative → end caveat が normal だった。

---

**本ケースから既存制度設計への確認：**

本論文は既存の RI-codebook と VQ-matrix の **robustness** を confirm した。特に RI-04, RI-06, PRI-11 の定義が 1972 context でも predictive。

制度設計への minimal changes：
1. RI-05b subtype 正式化（Ranking-to-structure overclaim）
2. PRI-11 formal codebook entry
3. Era-norm annotation に「method availability」check を mandatory addition

---

inference_time_sec: not available — inject externally
