```
prompt_version: stage3-v2-20260416
model_info: claude-sonnet-4-6

# 科学的知見の再認定判定票

## Tamao, Sumitani, Kumada 1972（Journal of the American Chemical Society, Communication）

### §1 Claim Architecture

**コア主張:**
本論文の中心的主張は「ニッケル-ジホスフィン錯体を触媒とするGrignard試薬とビニル・アリールハライドの選択的クロスカップリング」という実用的合成手法の確立である。

**Novelty柱**: (NC-1) 触媒量のNiCl₂(dpe)がβ-H含有アルキルGrignard試薬を含む多様なGrignard試薬と、特にsp²塩化物を含むビニル・アリールハライドとの選択的クロスカップリングを76–98%収率で実現する; (NC-2) bidentate diphosphine配位子クラスが単座ホスフィンを大幅に超える触媒活性を示し、その活性序列がcis-ジオルガノニッケル中間体の幾何要件という機構仮説を示唆する。

**Utility柱**: 従来の合成経路では「容易に到達できない」m-di-n-butylbenzeneやα-vinylnaphthaleneを一段階で合成できる実用的調製法（NC-5）。

**Layered structure: あり — 主張は4つの独立層から構成される:**

- **層1 (選択性・収率)**: β-H許容 + 高収率。Table Iの11エントリの収率データと2つの詳細例によって実証。
- **層2 (sp²選択性・塩化物反応性)**: sp²ハライドのみ使用可能 + 塩化物の高反応性。境界主張と肯定的特徴として記述。
- **層3 (配位子設計原理・機構仮説)**: bidentate diphosphineの役割とcis-geometry仮説。単一基質での活性序列の定性的データに基づく。
- **層4 (合成有用性)**: 到達困難な化合物の一段階合成。2つの詳細例によって例示。

**層間の依存関係**: 層3（cis-geometry仮説）の反証は層1、2、4を崩さない。Corriu/Masse (D4-8)によるNi(acac)₂での同様の選択性が確認されても、層1・2・4の実用性は保持される。ただし、層3の独自性（bidentate ligandが「必要条件」か「有効な選択肢」かという区別）は根本的に揺らぐ。層1が崩れた場合（選択性が実際にはホモカップリング混合物だった場合）のみ、論文全体の核心的価値が崩壊する。

---

### §2 SRG / CLA → RI / ER / EP Crosswalk

**SRG-1 [Mechanistic cycle without experimental evidence in dpe-Ni system]**

* **Primary RI**: RI-06 (Imported model) — 触媒サイクル全体（eqs 2–4）をdipy-Ni系（refs 11–12）とRMgX/NiX transmetalationの先行系から対象系（NiCl₂(dpe)）へ、同型性実証なしにサイクルレベルで輸入（Codebook v0.2 RI-06スコープ注記: サイクルレベル輸入に該当）
* **Secondary RI**: RI-03 (Unobserved explanatory) — 説明の中核を担う中間体1, 2, 3が直接観測も速度論的拘束もされていない
* **ER**: NiCl₂(dpe)系での触媒サイクルを機構的主張として記述するには、対象系での少なくとも1つの素反応ステップの化学量論的実証、または中間体の分光学的同定が必要。dipy配位子（N配位子）とdpe（P配位子）は電子的・立体的に根本的に異なるため、輸入モデルの同型性は仮定できない。
* **EP**: EP-06a (Analogy-validation pack); EP-03a (Direct-observation / state-assignment pack)
* **Case-specific実装**: (i) NiCl₂(dpe)と化学量論量のn-BuMgBrを低温（−78°C）でEt₂O中で反応させ、低温 ³¹P{¹H} NMRおよび ¹H NMRでジオルガノニッケル中間体1の形成を観測する; (ii) 独立合成した[Ni(n-Bu)₂(dpe)]をPhClと反応させ、eq (3)が予測するn-Bu–n-Bu（R–R相当）の生成を確認する化学量論的実験を実施する; (iii) ラジカルクロック基質（例: (5-hexenyl)MgBr）またはEPR測定でNi(I)/Ni(III)経路とNi(0)/Ni(II)経路を識別する。
* **注記**: B-2 (V1=high, V2=critical; convergence=2/3; gap=low)、B-14 (V1=medium, V2=high; convergence=2/3; gap=low)、U-1 (severity=high, 自己矛盾的不在: eq (3)がR-R生成を予測するが未報告)、U-2 (severity=medium, 黒色混合物の均一/不均一性問題)、U-4 (severity=medium, 配位子活性序列からの因果的帰属)。TEMPERATURE_SUMMARYでhigh_convergence_low_gap複数該当。§6に「RI-06 + RI-03の不可分共起パターン」として記録。

---

**SRG-2 [Selectivity claim without byproduct data]**

* **Primary RI**: RI-05 (Qualitative overread) — "selective" という数値なき定性的記述から、ホモカップリング完全抑制という構造的・合成的優位性を導出; eq (3)が予測するR-R生成物の報告が自己矛盾的に不在
* **Secondary RI**: RI-01 (Reporting integrity) — 収率データがクロスカップリング選択性の指標として使用されているが、質量収支にホモカップリング・β-脱離生成物が含まれない
* **ER**: 「選択的クロスカップリング」という方法論的主張の成立には、クロスカップリング生成物とホモカップリング生成物（R–R）、β-脱離生成物の相対量を定量した反応混合物の質量収支データが必要。
* **EP**: EP-05a (Quantitative-ranking substantiation pack); EP-01a (Reporting-coherence pack)
* **Case-specific実装**: 代表的基質（n-BuMgBr + PhCl, EtMgBr + PhCl）で反応混合物をGC-MSで分析し、n-Bu–n-Bu、1-ブテン（β-脱離）、PhCl（未反応）とクロスカップリング生成物（Ph-n-Bu、Ph-Et）の相対量を定量する。Table Iの収率76%（n-BuMgBr + PhCl）の残24%の質量収支を完全に記述する実験を実施する。
* **注記**: B-1 (V1=high, V2=high, V3=high; convergence=3/3; gap=none; 全エージェントhigh評価での最高優先候補)。U-1はeq (3)の機構的予測と不在のR-Rデータの自己矛盾的不在として独立に記録されている。C-1はTamura-Kochi鉄触媒との定量的比較の不在（Dropped Quantitative Benchmark）として補強。

---

**SRG-3 [Analytical quality of Table I yield data]**

* **Primary RI**: RI-01 (Reporting integrity) — 測定フレーム（glpc条件未記載: カラム仕様・検出器・内部標準）・報告単位の不統一（Example 1はハライド基準94%、Example 2はGrignard基準80%、Table I適用基準不明）による横比較不能
* **Secondary RI**: RI-08 (Unquantified reliability) — 反復測定なし、不確かさ記述なし; B-12の2例での収率計算基準の不一致はRI-08の内部矛盾型サブタイプ（Codebook v0.2注記に該当）
* **ER**: 同一表内の収率データを比較するには、統一されたglpc条件（カラム仕様、検出器、内部標準の同一性・濃度）、統一された収率計算基準（ハライド基準またはGrignard基準）、および全エントリの反応時間の報告が必要。
* **EP**: EP-01a (Reporting-coherence pack)
* **Case-specific実装**: Table Iの全11エントリについて、同一glpc条件（同一内部標準（例: n-デカン）、同一カラム・検出器）での収率を有機ハライド基準の質量収支として再測定・再報告する。各エントリの反応時間と温度を記録する。
* **注記**: B-4 (V1=medium, V3=medium; convergence=2/3; gap=none)、B-8 (V1=medium, V3=medium; convergence=2/3; gap=none)、B-9 (A-2リンク; mixed item)、B-12 (内部矛盾型RI-08の典型事例)、B-13 (and/or構文によるRI-02との連動)。§4のEra-Norm AnnotationでB-4, B-8, B-13がcommunication-era toleratedと分類される（通信形式に起因する自動解消候補）。

---

**SRG-4 [Scope restriction basis]**

* **Primary RI**: RI-07 (Unsupported boundary) — 失敗例なしに「sp²ハライドのみ使用可能」（"Only Csp² halides...can be used"）と限界を主張; 拡張適用: 制限を「最も注目すべき特徴の一つ」として肯定的に再フレームする形態（通常の否定的境界主張の逆向き）
* **Secondary RI**: RI-05 (Qualitative overread) — 同一基質での比較データなしに「塩化物の高反応性」という定性的順位から塩化物の合成的優位性という構造的含意を導出
* **ER**: 「sp²ハライドのみ使用可能」という境界主張には、sp³ハライドを試みた失敗例（条件を変えて不活性を確認）またはsp²選択性の速度論的・機構的根拠が必要。「塩化物の高反応性」という主張には、同一Grignard試薬に対するPhCl, PhBr, PhIの収率または初期速度の直接比較データが必要。
* **EP**: EP-07a (Boundary-test pack); EP-05a (Quantitative-ranking substantiation pack)
* **Case-specific実装**: (i) n-BuMgBrと代表的sp³ハライド（n-BuCl, n-BuBr, cyclohexyl chloride）を[NiCl₂(dpe)]存在下で試み、反応の有無をGCで確認する; (ii) PhCl, PhBr, PhIをそれぞれEtMgBrと同一条件（0°C, Et₂O, 1 mol%触媒）で反応させ、収率と初期速度を比較して塩化物の「高反応性」を定量化する。
* **注記**: B-5 (V1=medium, V2=medium; intentional_narrowing + methodological_limitation混合)、B-6 (sp³試験の不在)、A-2 (convergence=1/3; 将来の拡張課題として送り出し)。D-2のformat_exploitationで指摘された「A-2 ↔ B-5ピボット」構造 —— sp²制限の実験的根拠を問わずに「特徴」として確定させるメカニズム。

---

**SRG-5 [Solvent and condition effects without quantitative basis]**

* **Primary RI**: RI-01 (Reporting integrity) — "definitely superior"という確定的表現で溶媒効果を主張するが、THF使用時の収率データが一切存在しない
* **Secondary RI**: RI-05 (Qualitative overread) — 比較データなしに「ジエチルエーテルの確実な優位性」から溶媒選択の構造的含意を導出
* **ER**: 「ジエチルエーテルがTHFより確実に優れている」という主張には、同一基質・同一触媒量・同一反応時間でのエーテルとTHFの収率比較データが必要。
* **EP**: EP-01a (Reporting-coherence pack); EP-05a (Quantitative-ranking substantiation pack)
* **Case-specific実装**: n-BuMgBr + PhClを[NiCl₂(dpe)]触媒下、Et₂OとTHFの両溶媒で同一条件（0°C, 2 mol%触媒, 20h）で反応させ、GCで収率を比較する。Tamura-Kochi鉄触媒（ref 6）との比較もTHF中で実施する。
* **注記**: B-7 (V1=medium, V2=medium)、B-9 (SRG-3と共有)。VQ-2の必須要件（RI-01/RI-07）には間接的影響のみ。SRG-3（RI-01）のFull Paper展開での自動解消によって副次的に解消される可能性が高い。

---

**SRG-6 [Cis/trans selectivity observation]**

* **Primary RI**: RI-04 (Unreplicated discriminator) — cis/trans比（80:20, 43:57）という単一測定値に分析精度や代替経路排除（速度論/熱力学の区別、反応時間依存性の確認）なく「機構的含意がある」という高位解釈
* **Secondary RI**: RI-08 (Unquantified reliability) — 分析法（GLC面積比？NMR積分？）の不記述、反復測定なし、"43:57"という精度の根拠なし
* **ER**: cis/trans比データから「機構的含意がある」という解釈には、分析法の明示（定量GLC条件）、複数試行での反復測定（標準偏差の記録）、および速度論的vs熱力学的制御の区別実験（時間系列または温度系列）が必要。
* **EP**: EP-04a (Discrimination / replication pack); EP-08a (Replication / uncertainty pack)
* **Case-specific実装**: cis-1,2-dichloroethylene + PhMgBrの反応を（a）複数の反応時間点（2h, 5h, 20h）で停止し、（b）複数の温度（0°C, rt, reflux）で実施して、定量GLC（内部標準として既知モル比のcis/trans-stilbene混合物による検量線作成）でcis/trans比を測定する。3回以上の独立実験で再現性を確認する。cis-stilbeneおよびtrans-stilbeneを熱力学的条件下（高温・長時間）にかけて平衡比を確認する。
* **注記**: A-1 (V1=medium, V2=high; convergence=2/3; gap=low)、B-11 (V3=medium)、U-3 (severity=medium; kinetic/thermodynamic indeterminacy)。cis/trans比の観察はVQ-1の範囲に留まる（観察は成立するが機構的解釈のための証拠基盤は未整備）。

---

**SRG外：CLA**

**CLA-1: 配位子活性序列からcis-geometry仮説 + Corriu/Masse問題（D4-8対応）**

grounded_in: B-3（配位子活性序列の定性的データのみ）、C-3（Corriu/Masse, Note Added in Proofで記録・比較なし）。B-3はSRG-1のメンバーに含まれず（SRG-1: B-2, B-14, U-1, U-2, U-4）、C-3もいかなるSRGにも属さない。D-1のNC-4（bidentate diphosphineの役割と触媒設計原理）に直接関わる。

* **Primary RI**: RI-05 (Qualitative overread) — 単一基質（n-BuMgBr + PhCl, footnote 21）での定性的活性序列から「cis configurationが触媒の第一要件」という構造的・因果的結論を導出; bite angle, 電子的性質, 立体的要因が共変している序列から単一因子への帰属
* **Secondary RI**: RI-09 (External superiority) — Corriu/MasseのNi(acac)₂（キレートジホスフィンを持たない）との直接比較なしに、bidentate diphosphineを触媒設計の要件として提示; 競合する独立報告の存在が記録されながら比較実験が欠落
* **ER**: 「cis geometry of diorganonickel intermediateが第一要件」という主張には、bite angleを独立変数として体系的に変化させた配位子系での定量的活性比較と、既知cis-ジオルガノニッケル錯体の独立合成・検証が必要。diphosphineの独自性（vs. Ni(acac)₂等の非キレート型）には直接比較実験が必要。
* **EP**: EP-05a (Quantitative-ranking substantiation pack); EP-09a (Internal benchmark pack)
* **Case-specific実装**: (i) bite angleを系統的に変化させた一連のdiphosphine-Ni触媒（dmpe, dpe, dpp等）で、3種の基質組み合わせ（alkyl-Grignard × aryl halide; aryl-Grignard × vinyl halide等）の収率を定量的に比較しbite angle vs. yield相関を構築する; (ii) NiCl₂(dpe)とNi(acac)₂を同一基質・条件（n-BuMgBr + PhCl, Et₂O, 0°C→rt, 20h, 1 mol%触媒）で反応させ、選択性と収率を直接比較する（Corriu/Masse条件の再現）; (iii) cis-[Ni(n-Bu)₂(dpe)]を独立合成し、PhClとの反応でcis-reductive eliminationを実証する。
* **注記**: B-3 (V1=medium, V2=medium/high; convergence=2/3)、C-3 (convergence=1/3; single reference)。Note Added in Proofが記録したがNi(acac)₂との比較が欠落したCorriu/Masse問題は、NC-4（配位子設計原理）の独自性評価において最重要の未解決問い。

---

### §3 現在のVQ判定

**現在判定: VQ-1 (Observation)**

**VQ-1 [Observation] は通る**（RI-02が非致命的な形で残存）。
2つの詳細例（m-di-n-butylbenzene, α-vinylnaphthalene）の生成物は物性値（bp, n²⁰D）で文献値と照合されており、生成物同一性は確立されている。触媒[NiCl₂(dpe)]は文献既知化合物（ref 14）。B-13の"and/or"構文により一部Table Iエントリでは単一分析法のみによる同定の可能性が残るが（RI-02 non-fatal）、2つの代表例での実証がVQ-1通過の根拠となる。

**VQ-2 [Method] は未達**（VQ-1のRI-02 non-fatalを継承前提として）。
未解消RI: RI-01（SRG-3: glpc条件不記載、収率基準不統一）、RI-07（SRG-4: sp²制限の失敗例不在）。RI-01はTable I全体の比較可能性を損なう構造的問題であり、現代基準では致命的（era-norm依存: 1972年通信形式では許容されたが現代では不足、§4参照）。RI-07についてはsp²制限を失敗例なしに「最も注目すべき特徴の一つ」として提示している点が問題。

**VQ-3 [Mechanism] は未達**。
未解消RI: RI-03（SRG-1: 中間体1, 2, 3の直接観測・速度論的拘束なし）、RI-06（SRG-1: サイクルレベルモデル輸入—dipy-Ni/RMgX transmetalation系からの輸入）、RI-04（SRG-6: cis/trans比の単一測定）。さらにRI-05（SRG-2: 選択性の定性的主張）が重大に残存するため、VQ-3到達時にも「限定的（Qualified）」となる。

**VQ-4 [Benchmark] は未達**（VQ-3未達のため継承原則により未達）。

**層別VQ非対称性:**
ただし**合成実用性層（層1 + 層2の実用的側面）**単独では：VQ-2 (Method) に到達している可能性がある。2つの詳細例は統一された条件で実施され、物性値で確認された生成物を提供する。RI-01の通信形式への帰属（era-norm tolerated）を考慮すると、「この方法は機能する」という層1の実用的主張はVQ-2水準の証拠を持つ。これに対して機構層（層3）はVQ-2にも到達していない（RI-07未解消 + RI-06が支配的問題）。この非対称性は、Kumada反応が合成化学として高い実用的価値を持ちながら、機構的理解が長期にわたって未解決だったという科学史的事実と整合する。

---

### §4 Era-Norm Annotation

**communication-era tolerated:**

- B-4（glpc条件の詳細不記載）: 1972年JACS Communicationsではglpc条件の完全記述（カラム仕様、内部標準の同一性）は標準的要件ではなく、glpc収率の記載のみで許容された。
- B-8（反応時間の不記載）: 2–4ページの通信形式では全エントリの反応時間記載は慣例的に要求されなかった; 代表的2例の記述で十分と見なされた。
- B-13（生成物の個別分光データ不記載）: 1972年JACS Communicationsでは通信形式において全エントリの個別elemental analysisやNMRデータの完全記述は要求されず、Table Iの物性値と文献値比較が主要同定手段として許容された。
- B-9（条件非最適化免責）: 探索的通信論文において「条件は最適でない」と明記する慣行は当時のgenre conventionの範囲内であり、再現性への配慮として肯定的にも受け取られた。

**modern-era deficient:**

- B-1（選択性の定量的根拠なし）: 現代では「選択的」という方法論的主張にはホモカップリング生成物・β-脱離生成物を含む反応混合物の質量収支（GC-MS）が標準的に要求される; eq (3)が予測するR-Rの不報告は現代基準では自己矛盾（U-1）を構成する。
- B-2（触媒サイクルの実験的根拠なし）: 現代の機構化学では提案触媒サイクルの中間体に関して低温NMR観測、速度論測定、ラジカルクロック等による少なくとも部分的証拠が要求される; 「working hypothesis」の標識は末尾1文のみで本文は事実的記述語（標識不整合パターン）。
- B-10（触媒の均一/不均一性未確認）: 現代では均一系分子触媒の主張にはHg(0)ポイズニング試験等による均一/不均一性の区別が標準的に要求される; 黒色混合物の観察を分析せずに通過させることは許容されない。
- C-3（Corriu/Masseとの比較不在）: 現代では同時期の独立競合報告（特にNi(acac)₂が類似の選択性を達成するという報告）に対する実験的対比なしに配位子設計原理を主張することは許容されない。

**両タグに記載（当時は許容されたが現代では不足）:**

- B-4: 1972年通信形式では許容されたが、現代のreproducibility standardsではRI-01として致命的不足（VQ-2到達を妨げる）; Full Paper展開（Tamao et al., 1976–1977）で部分的に解消。
- B-13: 当時は許容されたが、現代では"and/or"構文による生成物同一性の不完全確認（RI-02, non-fatalとして残存）は問題となる; Full Paper展開での自動解消候補。

---

### §5 最短補強ルート

**VQ-2 への最短ルート：**
1. EP-01a (Reporting-coherence pack) — Table Iの全11エントリについて、同一glpc条件（同一内部標準・カラム・検出器）での収率を有機ハライド基準で再測定・再報告し、各エントリの反応時間を記録する。RI-01 (SRG-3) を前進。
2. EP-07a (Boundary-test pack) — 代表的Grignard試薬（n-BuMgBr）とsp³ハライド（n-BuCl, cyclohexyl chloride）を用いてsp²選択性の実験的根拠を確立する; PhCl/PhBr/PhIを同一基質・条件で比較し「塩化物の高反応性」を定量化する。RI-07 (SRG-4) を前進。

（補助）EP-02a (Identity/purity substantiation pack) — Table IのすべてのエントリについてGC-MSまたは¹H NMRデータを個別に記録し、RI-02 (VQ-1 non-fatal残存) を解消する。

認定ゲート順注記: 実験投入順は情報利得順（EP-01a → EP-07a → EP-02a）だが、最終認定はVQ-1 → VQ-2 → VQ-3 → VQ-4のゲート順で確定する。

---

**VQ-3 への最短ルート（VQ-2到達後）：**
1. EP-03a (Direct-observation / state-assignment pack) — NiCl₂(dpe)と化学量論量のn-BuMgBrを低温でEt₂O中で反応させ、低温 ³¹P{¹H} NMRでジオルガノニッケル中間体1の形成を観測する; 独立合成した[Ni(n-Bu)₂(dpe)]の特性評価と化学反応性の確認。RI-03 (SRG-1) を前進。

2. EP-06a (Analogy-validation pack) — NiCl₂(dpe)系での化学量論的素反応（eq 2, eq 3それぞれに対応する個別反応）を実施し、dipy-Ni系から輸入した触媒サイクルの対象系での同型性を実証する。RI-06 (SRG-1) を前進。

3. EP-05a (Quantitative-ranking substantiation pack) — 代表的基質（n-BuMgBr + PhCl）で反応混合物の質量収支（クロスカップリング vs. ホモカップリング vs. β-脱離）をGC-MSで定量し「選択的」という主張に数値的根拠を付与する。RI-05 (SRG-2) を前進 → VQ-3 (qualified)からVQ-3 (unqualified)へ。

4. EP-04a (Discrimination / replication pack) — cis/trans-stilbene比の時間・温度系列実験（速度論/熱力学制御の区別）と定量GLC反復測定（n≥3）を実施する。RI-04 (SRG-6) を前進。

認定ゲート順注記: 実験投入順は情報利得順（EP-03a, EP-06a同時投入 → EP-05a → EP-04a）だが、VQ-3認定にはRI-03とRI-06の両解消が必要。RI-05が重大に残存する間はVQ-3は「限定的（Qualified）」。

---

**VQ-4 への補足（参考）：**

EP-08a (Replication / uncertainty pack) — 代表的3–5エントリの収率を独立実験で3回以上測定し、標準偏差を報告。RI-08 (SRG-6, SRG-3) を前進。
EP-09a (Internal benchmark pack) — NiCl₂(dpe)とNi(acac)₂（Corriu/Masse系）を同一基質・条件で直接比較する。RI-09 (CLA-1) を前進。

---

### §6 制度設計への寄与

**1. RI-06 サイクルレベル輸入の代表事例（Codebook v0.2確認）**
SRG-1は、Codebook v0.2のRI-06スコープ注記（「触媒サイクル全体を別系から構成する大規模モデル輸入」）の明確な代表事例を提供する。dipy-Ni系からdpe-Ni系へのeqs 2–4全体の輸入は、個別素反応の類推（例: 「transmetalationが起こる」）を超えて、触媒サイクルの構造全体を移転している。このサイクルレベル輸入は、輸入元の配位子電子的性質が対象系と根本的に異なる（N配位子 vs. P配位子）ため、同型性の前提が特に疑わしい事例である。RI-06の代表事例として正式に記録する。

**2. RI-07拡張適用: 制限の肯定的再フレームという新しい形態**
SRG-4（B-5）のsp²制限は、Codebook v0.2のRI-07拡張適用注記（「〜が最も深刻な限界」という否定的境界主張にRI-07を適用する）とは逆向きで、「[REDACTED: verbatim source text; see the source paper via its DOI]」という形で制限を「最も注目すべき特徴」として肯定的に再フレームしている。データなしに「この制限がなぜ存在するか（試験したか否か）」を問わずに特徴として確定させるこの構造は、A-2 ↔ B-5ピボット構造（D-2のformat_exploitationで指摘済み）によって可能になっている。RI-07の拡張適用の新しい代表形態として記録する。

**3. 標識不整合（Labeling mismatch）パターンの確認**
eqs 2–4の触媒サイクルは「working hypothesis」と最終文でのみ標識されているが、本文全体では「reacts with」「forms」「is subsequently converted to」「releases」「regenerated」という事実的記述語で叙述されている（B-2の注記で指摘済み）。仮説標識が末尾1文に集約され、本文全体が事実的記述語を使用するこのパターンは、D-2のformat_exploitationで指摘された内容と整合し、RI-06のサイクルレベル輸入と連動して読者が仮説と確立された事実を区別することを困難にする構造として記録する。

**4. 層別VQ非対称性の初確認**
本論文の多層構造（合成実用性層 + 機構層）において、合成実用性層（層1）単独ではVQ-2に到達しうる一方で機構層はVQ-2にも到達しないという非対称性が確認された。論文全体の判定はVQ-1にとどまるが、どの主張層がどのVQ水準にあるかを識別する層別分析がUQSの分析精度を高める事例として記録する。

**5. 通信→Full Paper遷移の自動解消パターンの確認（§4補完）**
SRG-3（RI-01）のB-4（glpc条件）、B-8（反応時間）、B-13（個別分光データ）は通信形式の紙幅制約に直接起因し、Full Paper展開で自動解消される性質の欠落である（著者グループが1976–1977年にFull Paperシリーズを発表）。§4のEra-Norm AnnotationでB-4, B-8, B-13がcommunication-era toleratedと分類されたことと整合し、VQ-2到達に必須のRI-01がera-norm依存として解消される典型的通信→Full Paper遷移パターンの事例として記録する。

**6. RI共起パターン: RI-06 + RI-03の不可分共起**
SRG-1においてRI-06（サイクルレベル輸入）とRI-03（中間体の直接観測なし）が共起している。重要な点として、RI-06を解消しても（dipy-Ni系とdpe-Ni系の同型性を実証しても）、それだけではNiCl₂(dpe)中間体の実在証明にはならない—— EP-06a（化学量論的検証）と EP-03a（直接観測）の両方の解消が必要であり、どちらか一方では不十分である。この RI-06+RI-03 の不可分共起パターンは、「触媒サイクルを他系から輸入して提案する論文」類型において繰り返し現れる構造的問題として記録する。

**既存RI・PRI昇格への影響：**
本ケースでは新規PRI候補は検出されなかった。D4-2（機構サイクルの実験的根拠不在）はRI-06（サイクルレベル輸入）とRI-03（中間体未観測）の共起で十分カバーされる。PRI-11（Mechanism-kinetics decoupling）の適用を検討したが、本論文は速度データを一切報告していないため（速度式の導出と比較の問題よりも機構提案自体の根拠不足が主問題）、RI-06/RI-03共起の方が適切な記述と判断した。PRI-11の昇格判断には本ケースは参考にならない（速度データのある論文での独立確認が必要）。
```
