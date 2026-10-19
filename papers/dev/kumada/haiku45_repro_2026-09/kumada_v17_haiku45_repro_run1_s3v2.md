prompt_version: stage3-v2-20260416
model_info: claude-haiku-4-5

# 科学的知見の再認定判定票

## Tamao, Sumitani & Kumada (1972) (Journal of the American Chemical Society, communication)

### §1 Claim Architecture

コア主張：ニッケル-ホスフィン複合体が触媒として機能し、Grignard試薬と有機ハライド（特にCsp²）の間に高選択性でC-C結合を形成し、ホモカップリング副生成物を抑制する新規触媒法。

Novelty柱：ニッケル-ホスフィンシステムの初報告と位置づけられている。
Utility柱：高収率（表1で76–98%）と選択性（ホモカップリング抑制）。

Layered structure：なし。両柱（触媒発見と選択性達成）は表1の同一データセットに依存し、独立していない。表1の信頼性が崩れれば両者が同時に瓦解する。

### §2 SRG / CLA → RI / ER / EP Crosswalk

**SRG-α [定量的選択性検証の全体的不在]**

* Primary RI: RI-01 (Reporting integrity — 測定フレーム・条件記述の不統一による横比較不能)
* Secondary RI: RI-08 (Unquantified reliability — 比較データに反復測定不確かさ記述なし)
* ER: 選択性主張を支えるには、交差カップリング収率とホモカップリング副生成物の絶対量ならびに相対比が報告される必要がある。
* EP: EP-01a (Reporting-coherence pack); EP-08a (Replication / uncertainty pack)
* Case-specific実装: 表1の11例について、各例ごとに（a）GC基準値の同定と検証、（b）ホモカップリング生成物（R-R）のGC積分値または分離収率、（c）限定試薬の統一指定、（d）複数ラン時の標準偏差または不確かさ。
* 注記: B-1, B-8, V3-OV1, V3-OV2; high_convergence_low_gap

**SRG-β [触媒サイクルの実証的根拠不在]**

* Primary RI: RI-03 (Unobserved explanatory — 説明の中核を担う種が直接観測されていない)
* Secondary RI: RI-06 (Imported model — 他系モデル [stoichiometric organonickel chemistry] を対象系での同型性実証なしに輸入)
* ER: 提案される触媒サイクル（複合体1→2→3）の各ステップが機構的に成立するには、少なくとも複合体1と2の同定、および個別ステップの速度論的証拠が必要。
* EP: EP-03a (Direct-observation / state-assignment pack); EP-10a (Kinetic verification pack)
* Case-specific実装: （a）L₂NiR₂ (複合体1)のNMR、MS、X線構造による確認、（b）NMR kinetics による Mg→Ni transmetalation 速度定数の測定、（c）deuterium labeling による還元消去ステップの立証。
* 注記: A-1, B-5, U-1, V2-OV1, V2-OV2; A-1 ↔ B-5 ピボット（主張の成立と機構実証の分離）

**SRG-γ [選択性原理の3層未説明]**

* Primary RI: RI-07 (Unsupported boundary — 失敗例なしに「Csp²のみ可能」と限界を主張)
* Secondary RI: RI-04 (Unreplicated discriminator — 識別力の高い単一データに分析精度や代替経路排除なく高位解釈)
* ER: Csp² vs. Csp³ 選択性の区別は、対応する酸化付加・トランスメタル化・還元消去ステップのいずれが律速であるかの特定、および各ステップの速度比較を通じてのみ説明可能。
* EP: EP-07a (Boundary-test pack); EP-10a (Kinetic verification pack)
* Case-specific実装: （a）Csp³ ハライド（例：1-bromo-butane）の試験条件下での反応性試験と否定的結果の検出限界報告、（b）各選択的ステップの速度式導出。
* 注記: U-2, U-3, U-4, B-4, B-6; SRGメンバーが3つの独立した選択性現象（Csp²選択、シス幾何必須性、塩化物反応性）をカバー

**SRG-δ [製品特性評価の不完全性]**

* Primary RI: RI-02 (Object identification — 生成物の構造・純度が代替候補を排除できる粒度で未確定)
* ER: 11例の生成物はそれぞれ、構造確認（1H/13C NMR）、純度評価（GC purity、再結晶、融点），および単一性確認（HPLC）を経て初めて同定と言える。
* EP: EP-02a (Identity / purity substantiation pack)
* Case-specific実装: 各生成物について、NMR chemical shifts と coupling patterns を文献値と比較、GC保持時間と分割分析、必要に応じて再結晶と融点測定。
* 注記: B-11, B-12, V3 questions; SRG-δ は直接的には表1の個別エントリの信頼性に影響（SRG-α との相互強化）

### §3 現在のVQ判定

現在判定: VQ-2 (Method — 限定的)

VQ-1 (Observation) は通る：
表1の11例において、生成物同定は基本的に達成されている（NMR、IR、MS記述あり）。RI-02（Object identification）の致命性は非致命的。

VQ-2 (Method) は限定的（Qualified）：
RI-01（Reporting integrity）が未解消。収率の混在（GC vs. 分離）と限定試薬基準の混在により、方法論的な比較可能性が破壊されている。RI-07（Unsupported boundary — Csp²のみ可能）も未解消。これらは致命的ではなく（表1のデータ自体は存在し、再解釈は可能），VQ-2は通るが著しく限定される。

VQ-3 (Mechanism) は未達：
RI-03（Unobserved explanatory — 複合体1が観測されていない），RI-06（Imported model — stoichiometric類推が catalytic 環境で検証されていない），RI-04（rate-determining step 未特定）が致命的に未解消。提案された触媒サイクルは「仮説」のレベルに止まり、実証的根拠を欠く。

VQ-4 (Benchmark) は未達：
RI-08（Unquantified reliability），RI-09（External superiority — 外部文献値との直接比較なし）が致命的。Tamura & Kochi との直接比較実験が存在しない。

### §4 Era-Norm Annotation

communication-era tolerated:
- B-5（中間体1の未特性評価）：通信形式の紙幅制約下では、触媒仮説の提案と完全な立証の分離は当時許容。詳細な分光データ（NMR、X線）は full paper で期待される規範。
- B-8（ホモカップリング副生成物の未計量化）：1972年、複数成分の同時定量分析法（HPLC）は普及前。定性的記述も許容。
- B-7（control experiments 不在）：1972年の合成化学慣行では、既知触媒と既知反応の組み合わせを試験するだけで「新規」と認定される場合多し。baseline measurement の厳密性は現代基準より緩い。

modern-era deficient:
- B-5（中間体観測）：現代では分光NMR（in situ monitoring）が標準。複合体1の NMR 観測は当時と比べはるかに容易。致命的欠落。
- B-8（ホモカップリング定量化）：GC-MS の現代的普及により、構造異なる C-C カップリング生成物（cross-coupling vs. homo-coupling）の分離定量は常套。定量不在は防止可能であり、現代では不許容。
- B-1（yield basis 混在）：当時も現代も統一の要求があるが、現代では表計算ソフトウェアにより統一は自動化可能。当時より実行可能性が高い。

### §5 最短補強ルート

**VQ-3 (Mechanism) への最短ルート（現在 VQ-2 から）：**

1. EP-03a (Direct-observation / state-assignment pack) — L₂NiR₂ (複合体1)の NMR in situ 検出（変温 31P NMR による Ni-Ph, Ni-vinyl 複合体の同定）。RI-03 前進。

2. EP-10a (Kinetic verification pack) — 各elementary step の速度定数測定（stopped-flow or NMR kinetics）。RI-11 (Mechanism-kinetics decoupling) 前進、rate-determining step 特定。

3. EP-07a (Boundary-test pack) — Csp³ アルキルハライド試験による否定的結果の検出限界記録（GC感度確認）。RI-07 前進。

→ VQ-3 に到達（RI-03, RI-06, RI-04 解消）

**VQ-4 (Benchmark) への最短ルート（VQ-3 達成後）：**

1. EP-08a (Replication / uncertainty pack) — 複数ラン平行測定と統計解析。RI-08 前進。

2. EP-09a (Internal benchmark pack) — 表1内での各例の再測定による再現性確認。RI-08 進化。

3. 外部比較 — Tamura & Kochi system (Cu/Fe/THF) との identical substrate での side-by-side 比較。RI-09 前進。

→ VQ-4 に到達（RI-08, RI-09 解消）

認定ゲート順注記：実験投入順は上記の情報利得順だが、最終的な VQ 認定は VQ-1 → VQ-2 → VQ-3 → VQ-4 の継承原則に従う。

### §6 制度設計への寄与

新 PRI 候補：PRI-11 (Mechanism-kinetics decoupling) の確認

本論文はこのパターンの代表的初期事例である。触媒サイクル（複合体1→2→3）が提案されながら、速度式の代数導出および観測速度次数との一致検証が存在しない。この「機構と速度の乖離」は、触媒化学全般に見られ、1970年代の触媒論文の典型的特徴となっている。

RI-04 と RI-06 の共起パターン：
本論文では、単一の実験（表1の高収率観察）が「選択性が実現される」「ニッケル触媒が有効である」「Csp²が選別される」の3つの主張を同時に支持するよう見なされている。これは RI-04 (単一データへの多重高位解釈) と RI-06 (他系からの無検証な模型輸入 [stoichiometric Ni chemistry]) の同時発動。両者が共起する場合、どちらか一方の解消だけでは不十分であり、両方の解消が同時に必要なパターンである。

Era-Norm 観察：「communication 形式による選別作用」
1972年の communication 形式は、分野内競争が激化する局面で「速度」を優先させるフィルタ役を果たしている。制度的に許容されるレベルの「不完全性」が、当時と現代で異なることを示す好例。本論文が現代の full paper として提出されたなら、B-5, B-7, B-8 は致命的欠落と見なされる。逆に、形式を通信に限定することで、仮説段階の知見の迅速な共有が可能になった側面もある。

既存制度設計の確認：
本ケースは既存のRI-01, RI-03, RI-04, RI-06, RI-07, RI-08, RI-09, EP-03a, EP-07a, EP-10a の適用と境界を確認する良い testbed である。新規パターンの提案は検出されない。

inference_time_sec: not available — inject externally
