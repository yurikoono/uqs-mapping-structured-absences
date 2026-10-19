```
prompt_version: stage3-v2-20260416
model_info: claude-sonnet-4-6

# 科学的知見の再認定判定票

## Eno, Lu & Morken 2016（Journal of the American Chemical Society, communication）

### §1 Claim Architecture

**コア主張の要約：**
本論文は三つの柱から成る。**Novelty柱**：対称プロキラル環状硫酸エステルを電解剤とするNi触媒不斉Kumadaクロスカップリングの初例。従来法が「sp²炭素に隣接した活性化された求電子剤」を必要とするのに対し、本反応は「非活性化アルキル求電子剤」で機能し、三級炭素立体中心を高鏡像体比（最高96:4 er）で構築する。**Utility柱**：広い基質スコープ（17例）、グラムスケール合成、クロマン前駆体合成という合成的有用性の実証。**機構的主張柱**：ラジカル時計実験（陰性結果）と同位体標識立体特異性実験（90%ジアステレオ特異性）を根拠に、SN2様立体反転的酸化的付加が機構を支配するという提案と触媒サイクル（Scheme 4）の提示。

**Layered structureの判定：**
三層構造が成立しており、各層は独立している。

1. **合成的主張層**（T1）：環状硫酸エステルから三級炭素立体中心を構築するNi触媒不斉カップリングの実証。er数値・収率・基質スコープが証拠。機構的主張層への単一の反証（例：RE立体化学仮定の崩壊）ではこの層は崩れない。
2. **スコープ主張層**（T1）：17例にわたる広い適用性。SFCによるer定量が根拠。SRG-5の問題（分析法非開示）が潜在的に信頼性を弱める。
3. **機構的主張層**（T1）：SN2様酸化的付加とScheme 4の触媒サイクル提案。ラジカル時計・立体特異性実験・Grignard試薬によるer変化が根拠。この層への反証はスコープ主張層・合成的主張層に波及しない。

層間の依存関係：機構的主張層が正しいとして初めて合成的主張の**設計原理**（なぜ高erが得られるか）が正当化されるが、合成的事実そのものの有効性は機構に依存しない。合成的主張層と機構的主張層の結合は「説明の結合」であり「証拠の結合」ではない。

---

### §2 SRG / CLA → RI / ER / EP Crosswalk

**SRG-1 [Radical clock — evidentiary sufficiency of negative result]**

* **Primary RI**: RI-04 (Unreplicated discriminator)
* **Secondary RI**: RI-03 (Unobserved explanatory)
* **ER**: 陰性結果実験（ラジカル時計）から非ラジカル機構を推論するためには、(1) ≥95%のマスバランス閉鎖（生成物25が「存在しない」ことと「検出限界以下」を区別）、(2) 速度論的ウィンドウ解析（シクロプロピルカルビニルラジカルの開環速度定数と本Ni触媒サイクルの速度の比較による探針適格性の実証）が必要である。
* **EP**: EP-04a (Discrimination / replication pack)
* **Case-specific実装**: (1) 化合物23の反応をGC-MSおよびNMRで全生成物定量し≥95%のマスバランスを確立する；(2) シクロプロピルカルビニルラジカル開環速度定数（k_ring ≈ 10⁸ s⁻¹）とNi触媒サイクルの推定速度（k_Ni；競合Stobbe法または時間分解実験）を比較し、プローブが速度論的に適格（k_ring/k_Ni ≥ 10²）であることを実証する；(3) 25の真正標準品を合成し既知濃度でスパイクしてSFC/GC-MSでの検出限界を定量する。
* **注記**: B-1（3/3, temperature_gap=none）、U-1（3/3）。TEMPERATURE_SUMMARYではhigh_convergence_low_gap。収率56%の質量収支欠損（44%）は、論文が提案する非ラジカルNiサイクルが予測する「カップリング生成物のみ」という帰結と矛盾する自己矛盾的不在（U-1）を形成している。RI-04の「否定的証拠の不完全性」パターンの代表事例（§6参照）。

---

**SRG-2 [Stereospecificity experiment — measurement and interpretive validity]**

* **Primary RI**: RI-06 (Imported model)
* **Secondary RI**: RI-04 (Unreplicated discriminator)
* **ER**: 立体特異性実験から酸化的付加の立体化学を推論するためには、「C–C結合形成的還元的脱離は炭素上の配置保持で進行する」という仮定（"Assuming…"）の独立検証が必要である。加えて参照化合物（26-d₁）の光学純度と立体化学決定に用いた分析法の明示が要求される。
* **EP**: EP-06a (Analogy-validation pack); EP-04a (Discrimination / replication pack)
* **Case-specific実装**: (1) 化学量論的RE実験：既知立体化学のpyboxNi(Ar)(アルキル)錯体を合成し、熱的REの立体化学的結果を同位体標識アルキル基を用いて独立に決定する；(2) 参照化合物(4S,5S)-26-d₁および27の光学純度を旋光度＋SFCで報告する；(3) 90% dsの決定に使用した分析法（SFCカラム・条件・検出法・ピーク同定）を特定する。
* **注記**: B-2（3/3, temperature_gap=low）、U-3（3/3）。TEMPERATURE_SUMMARYではhigh_convergence_low_gap。"Assuming…"という仮定標識は文の前半に集約され、Abstract（"Mechanistic experiments point to a stereoinvertive SN2-like oxidative addition"）では仮定依存性が消える標識不整合パターンが確認された（§6参照）。

---

**SRG-3 [Catalytic cycle — Ni species and elementary step characterization]**

* **Primary RI**: RI-03 (Unobserved explanatory)
* **Secondary RI**: RI-06 (Imported model)（サイクルレベル輸入）
* **ER**: 提案された触媒サイクル（Scheme 4）の検証には、(1) pyboxNi(Ar)錯体CのNMR/EPR/UV-Vis同定；(2) Ni酸化状態の決定（Ni(0)/Ni(II) vs. Ni(I)/Ni(III) マニフォールド）；(3) ArMgBr濃度に対する速度次数の決定；(4) 遷移金属化（ArMgBr → C）と酸化的付加（C + 環状硫酸エステル → D）の各素反応の化学量論的実証が必要である。
* **EP**: EP-03a (Direct-observation / state-assignment pack); EP-06a (Analogy-validation pack)
* **Case-specific実装**: (1) Ni(acac)₂/(R,R)-L5とArMgBrを−25 °CでTHF中で混合し、低温¹H NMR・UV-Vis・EPR（Ni(I)検出）でNi種を同定する；(2) PhMgBrに対する初速度の[PhMgBr]依存性（1次/2次/飽和）を測定しpyboxNi(Ar)の触媒スペシーとしての妥当性を評価する；(3) Ni(acac)₂/(R,R)-L5と化学量論量のPhMgBrの混合物に環状硫酸エステルを加え、生成物（カップリング体＋硫酸Mg塩E相当）を単離・同定して素反応を確認する。
* **注記**: B-3（2/3, temperature_gap=low）、U-4（2/3）、B-18（2/3）、B-19（2/3）。TEMPERATURE_SUMMARYではhigh_convergence_low_gap。Scheme 4はNi酸化状態を特定しないまま図示しており、Ni(0)/Ni(II)とNi(I)/Ni(III)の両マニフォールドと文面上一致する中立的図示が不確実性を隠蔽している（§6参照）。

---

**SRG-4 [Scope failure — unquantified and undiagnosed substrate limitations]**

* **Primary RI**: RI-07 (Unsupported boundary)
* **Secondary RI**: RI-05 (Qualitative overread)
* **ER**: 失敗基質の境界主張には、(1) 代表的な失敗例の収率・er・転化率の定量データ；(2) 「不活性」の操作的定義（0%転化か痕跡量生成か選択性不足か）；(3) 少なくとも定性的な失敗モードの診断（立体的障害、電子的不活性化、配位毒作用）が必要である。
* **EP**: EP-07a (Boundary-test pack); EP-05a (Quantitative-ranking substantiation pack)
* **Case-specific実装**: (1) ortho-ArMgBr（2例）とアルキルMgBr（1例）について転化率（GC/NMR）・収率・er（SFC）を報告する；(2) Scheme 2インセットの「非反応性基質」（三級アルコール誘導体、四級炭素）について反応時間14hでの転化率を測定し回収SM量を記録する；(3) グリセロール基質21の75:25 erについて、OBn基を除去した化合物との比較実験を行い配位毒作用と立体的障害の寄与を分離する。
* **注記**: B-4（2/3, gap=none）、B-5（metric_incompleteness）、B-14（2/3）、A-1（deferred, V2 convergence 1/3）。失敗モードの未診断はA-1で明示される「今後の触媒開発」の方向性を決定するために不可欠であり、SRG-4とA-1の結合はStage 2 D-4のピボット構造（A-1 ↔ B-4/B-5）を形成している。

---

**SRG-5 [Enantioselectivity measurement — analytical traceability]**

* **Primary RI**: RI-01 (Reporting integrity)
* **Secondary RI**: RI-08 (Unquantified reliability)
* **ER**: 17例にわたるer値（論文の主要定量的主張）の信頼性確立には、(1) 全生成物に対するSFCカラム同定・移動相・流速・UV検出波長の記載；(2) 全17エントリーの個別実験値と標準偏差（または範囲）；(3) 弱いUV吸収体（脂肪族一級アルコール）に対する検出器適格性の確認が必要である。
* **EP**: EP-01a (Reporting-coherence pack); EP-08a (Replication / uncertainty pack)
* **Case-specific実装**: (1) 補足情報に全17生成物のSFC分析条件（カラムメーカー・品番・移動相組成・流速・カラム温度・UV波長・保持時間）を表形式で提供する；(2) 2回実験のer値と収率を個別に記載し平均値±半値域を報告する；(3) UV吸収が弱い生成物（products 2, 3, 4, 7等；脂肪族一級アルコール）について代替検出法（ELSD、RIまたはUV活性誘導体化）の検討と記録を行う。
* **注記**: B-6（RI-01の主因）、B-7（2/3, temperature_gap=low）。TEMPERATURE_SUMMARYではhigh_convergence_low_gap。このSRGは論文全体の定量的基盤に関わり、VQ-2達成の最優先ターゲットである。

---

**SRG-6 [MgBr2 side reaction — characterization and catalytic-condition relevance]**

* **Primary RI**: RI-02 (Object identification)
* **Secondary RI**: RI-03 (Unobserved explanatory)
* **ER**: 副反応生成物（3-ブロモプロパノール誘導体）の構造同定と触媒条件下での競合度の定量化が必要である。熟成仮説（MgBr₂沈殿が副反応を抑制）は実験的に未確認のまま。
* **EP**: EP-02a (Identity / purity substantiation pack); EP-03a (Direct-observation / state-assignment pack)
* **Case-specific実装**: (1) MgBr₂とTHF中の環状硫酸エステル1を0 °Cで反応させ、生成物を¹H NMR・¹³C NMR・MSで完全同定する；(2) 同副反応のkobs（GC追跡）をNi触媒クロスカップリング速度と比較して触媒条件下での競合度を定量化する；(3) 市販MgBr₂を意図的に添加した新鮮PhMgBrと通常熟成PhMgBrのカップリング結果を比較し熟成仮説を検証する。
* **注記**: B-11（全エージェントが関連する問いを提起）。VQに対する直接的な致命性は低いが、B-1（44%の質量収支欠損）との連関でMgBr₂副反応が未管理変数として機能している可能性がある。

---

**SRG外：CLA**

**CLA-1: Stereoselection step assignment — kinetic vs. thermodynamic enantiocontrol (U-2)**

* **Primary RI**: RI-03 (Unobserved explanatory)
* **ER**: 「立体化学決定段階は環状硫酸エステルのキラルNi錯体による開環」（Scheme 4本文）という主張の検証には、Eyring解析（複数温度でのer測定によるΔΔH‡とΔΔS‡の決定）、または競合速度論実験（異なるArMgBrとの競合）によるCurtin–Hammett状況の排除が必要である。
* **EP**: EP-03a (Direct-observation / state-assignment pack)
* **Case-specific実装**: −40〜+20 °C（5点以上）でのer測定からEyring線形性（1/T vs. ln(k_major/k_minor)）を確認し、ΔΔH‡とΔΔS‡を求めてエンタルピー支配（基質配座制御を示唆）かエントロピー支配（溶媒和・錯体柔軟性制御を示唆）かを判定する。
* **注記**: U-2（V2単独、高）はいずれのSRGにも属さないが、D-1 NC-3（機構的主張）に直結する。自己矛盾的不在のCLA：Scheme 4モデルは立体化学決定段階の同定を前提として成立しているが、その同定を支持する実験データが存在しない。D-4候補4でgrounded_in B-18, U-2として言及されており、B-18はSRG-3のmemberだがU-2はいずれのSRGにも属さないためCLAとして記録する。

---

**CLA-2: Reactive conformation — conformational energy validation (B-13, C-5)**

* **Primary RI**: RI-06 (Imported model)
* **Secondary RI**: RI-05 (Qualitative overread)
* **ER**: 「C5置換基が軸位に配した反応性配座」（Scheme 4, 配座A）の妥当性には、(1) 対象環状硫酸エステル基質のDFT配座解析による軸/赤道位エネルギー差の定量；(2) Ref 21（Lowe et al., 1988年）のデータが本置換基群に転用可能であることの実証が必要である。
* **EP**: EP-06a (Analogy-validation pack); EP-05a (Quantitative-ranking substantiation pack)
* **Case-specific実装**: (1) 化合物1（R=Me）、3用基質（R=Et）、4用基質（R=iPr）のM06-2X/6-311G**による配座最適化と軸/赤道位ΔG計算（THFのPCM溶媒和補正込み）；(2) 計算されたΔG(ax/eq)とRef 21の結晶構造データとの比較；(3) er（products 2 vs. 3 vs. 4）とΔG(ax/eq)の相関係数算出。
* **注記**: B-13（2/3, temperature_gap=none）、C-5（引用ギャップ）。B-13はsame_root_groupsのformal memberではないが（METAにてB-3 ↔ B-13のリンクとして記載）、Scheme 4立体化学モデルの基質側の基盤を構成するため独立CLAとして記録する。RI-05が解消されない場合VQ-3はqualified（注1）。

---

### §3 現在のVQ判定

**現在判定: VQ-1 (Observation)**

**VQ-1 [Observation] は通る。**
主要カップリング生成物（2–18）はすべて¹H NMR・¹³C NMR・HRMSで同定されており、RI-02の要件を満たす。SRG-6の副生成物（3-ブロモプロパノール誘導体）に関するRI-02は非致命的——主要合成成果ではなく、機構的予備実験の副産物同定欠如にとどまる。VQ-1継承前提はVQ-2以上の判定において成立している。

**VQ-2 [Method] は未達。**
RI-01（SRG-5）：SFCカラム・移動相・検出条件が一切記載されておらず、17例すべてのer値が独立再現不能。これは本論文の主要定量的主張の核心的方法論欠如であり致命的。RI-07（SRG-4）：失敗基質の境界主張が定量データなしに記述されており、スコープ主張の範囲が検証不能。致命的。VQ-2未達。

ただし**合成的有用性主張（化合物2–18の実証）単独では**：RI-01がera-norm toleratedの境界上にあり（2016 JACS Communicationの誌面制約による）、RI-07は将来のFull Paper展開で自動解消される可能性がある。この層のみ評価すれば **VQ-2 qualified** に到達する。**機構的主張（SN2様酸化的付加・Scheme 4触媒サイクル）は VQ-1止まり**：RI-03（中間体未観測）・RI-04（ラジカル時計の不十分な証拠）・RI-06（RE仮定輸入、サイクルレベル輸入）がすべて致命的に残存。

**VQ-3 [Mechanism] は未達（VQ-2継承により）。**
VQ-2が未達のため継承原則によりVQ-3も未達。独自要件として、RI-03（SRG-3: pyboxNi(Ar)およびScheme 4全中間体が未観測；CLA-1: 立体化学決定段階の同定なし）・RI-04（SRG-1: ラジカル時計の単一陰性実験・マスバランス未閉鎖）・RI-06（SRG-2: RE立体化学仮定輸入；SRG-3: サイクルレベルの他系輸入；CLA-2: Ref 21の配座データ輸入）がすべて致命的に残存。RI-05（CLA-2: 置換基サイズ類似性から配座を定性的に推論）が解消されない限りVQ-3はqualifiedにしかならない（注1）。

**VQ-4 [Benchmark] は未達（VQ-3継承により）。**
VQ-3が未達のため継承原則によりVQ-4も未達。独自要件として、RI-08（SRG-5: er値の個別値・標準偏差未報告）およびRI-09（C-1, C-2: 先行研究との定量的直接比較不在）が致命的に残存。

---

### §4 Era-Norm Annotation

**communication-era tolerated（2016 JACS Communication）:**

- **B-6**（SRG-5, RI-01）：SFC分析条件の非記載 — 2016年の合成系コミュニケーションでは、SFC/HPLCの詳細条件はSI記載が慣習であり（本論文ではSI参照も明示されていないが）、誌面4頁での省略は当時許容範囲内であった。現代基準では不足（両タグ）。
- **B-7**（SRG-5, RI-08）：2実験の平均のみ・個別値なし — 合成スコープ論文での2回平均報告は2016年時点では標準的であり、統計的不確実性の明示要求は当時の一般的慣行ではなかった。現代基準では不足（両タグ）。
- **B-3**（SRG-3, RI-03）：触媒サイクルの機構提案のみ・中間体観測なし — 合成コミュニケーションにおける「作業仮説としての機構提案」は2016年時点では許容されており、機構立証は通常Full Paperに委ねられた。
- **B-4, B-5**（SRG-4, RI-07）：失敗基質の定性的記述のみ — 4頁コミュニケーションで失敗例の完全データを提供する慣行は2016年時点では確立されていなかった。
- **B-17**（SRG外）：配位子選択性の構造的根拠なし — 合成コミュニケーションでは「最も有効だった」と報告するのみで構造的理由を論じないことは2016年当時一般的であった。

**modern-era deficient（現代の再認定では許容できない欠落）:**

- **B-6, B-7**（SRG-5, RI-01 + RI-08）：現代の不斉触媒化学ではキラルSFC/HPLCの完全な分析条件（カラム型番・移動相・流速・検出波長・保持時間）のSI記載が標準的に求められる；17例の主要定量的主張がer値である本論文では、2026年時点の再投稿審査において必須情報として要求される。（両タグ記載）
- **B-1**（SRG-1, RI-04）：現代の機構化学的基準では、陰性のラジカル時計実験を「非ラジカル機構の証拠」として使用する場合、マスバランス閉鎖（≥95%）と速度論的ウィンドウ評価の明示が要求される；44%の質量収支欠損を持つ実験は現代基準では機構的証拠として受け入れられない。
- **B-2**（SRG-2, RI-06）："Assuming…"という仮定標識を付けながら機構的結論を導出し、Abstractで仮定依存性を消去する構造は、現代のpeer reviewでは独立した立体化学的検証（化学量論的RE実験）なしには機構的主張として受け入れられない。
- **B-4, B-5**（SRG-4, RI-07）：現代の不斉触媒スコープ論文では失敗例についても代表的なデータ（転化率・収率・er）の報告が求められ、定性的な「不活性」「ほぼラセミ」という記述のみでは境界主張を支持しないと判断される。

（B-6・B-7は両タグに記載：2016年当時はcommunication formatで許容されたが、現代基準では不足。）

---

### §5 最短補強ルート

**目的関数設定：**
第一目的関数：VQ-2 (Method) 達成。
第二目的関数：VQ-3 (Mechanism) 達成（VQ-2達成を前提）。

**VQ-2 への最短ルート：**

1. **EP-01a** (Reporting-coherence pack) — 全17生成物のSFC分析条件（カラム・移動相・検出波長・保持時間）をSIに追記する。RI-01 を解消。情報利得最大（全er値の一次的信頼性を回復）、実験コストゼロ（既存データの報告補完）。
2. **EP-08a** (Replication / uncertainty pack) — 2実験の個別er値と収率を報告し、平均値±半値域で記載する。RI-08 を部分的に前進。EP-01aと同時実施可能。
3. **EP-07a** (Boundary-test pack) — 失敗基質（ortho-ArMgBr 2例、アルキルMgBr 1例、Scheme 2インセット2例）のデータ（転化率・収率・er）を新たに測定・報告する。RI-07 を解消。中程度の実験コスト（5–7反応の追加実施）。

認定ゲート順注記：VQ-2の最終認定は継承原則に従いVQ-1通過後に、RI-01解消（EP-01a）とRI-07解消（EP-07a）の両方が必要。EP-01a/EP-08aは実験コストゼロで先行実施し、EP-07aは新規実験として後続させる。

**VQ-3 への最短ルート（VQ-2達成後）：**

1. **EP-03a** (Direct-observation / state-assignment pack) — Ni(acac)₂/(R,R)-L5 + ArMgBrから化学量論的Ni錯体を調製し、¹H NMR・EPR・UV-VisでNi酸化状態と配位構造を同定する。RI-03 (SRG-3) を前進し、同時にRI-06（サイクルレベル輸入）も前進（Ni酸化状態実証により提案触媒サイクルの妥当性評価が可能になる）。SRG-3の4メンバー全てに前進効果があり情報利得最大。
2. **EP-04a** (Discrimination / replication pack) — 化合物23のラジカル時計実験を再実施し、全生成物のマスバランス閉鎖（≥95%）と速度論的ウィンドウ評価を実施する。RI-04 を解消。中程度のコスト（再現性実験＋速度論測定）。
3. **EP-06a** (Analogy-validation pack) — (a) 化学量論的RE立体化学実験（pyboxNi(Ar)(アルキル)錯体の合成とRE立体化学測定）でRI-06 (SRG-2) を解消；(b) DFT配座解析（CLA-2）でRI-06 (CLA-2) を部分的に前進。(a)と(b)は並行実施可能。
4. **EP-03a（for CLA-1）** — Eyring解析（複数温度でのer測定）で立体化学決定段階を同定する。RI-03 (CLA-1) を解消。比較的低コスト（既存反応系での温度変数追加）。

認定ゲート順注記：VQ-3の最終認定は継承原則に従いVQ-2通過後に、RI-03・RI-04・RI-06すべての解消が必要。RI-05（CLA-2の定性的過解釈）が残存する場合VQ-3はqualified。実験投入順はEP-03a（情報利得最大）→ EP-04a（RI-04単独対処）→ EP-06a（RI-06残余、計算と実験の並行）→ Eyring解析（CLA-1）。

---

### §6 制度設計への寄与

**1. 否定的証拠の不完全性（RI-04 case-specific実装の確認）**

SRG-1（B-1/U-1）は、陰性のラジカル時計実験を肯定的機構証拠として使用する際に質量収支閉鎖と速度論的ウィンドウ評価が欠けているパターンの事例として記録する。本論文の特徴として、(a) 44%という大きな質量収支欠損が明示された数値として報告されている点と、(b) "only detected"という記述が検出限界への言及なしに使用されている点がある。これはRI-04の「代替経路排除なく高位解釈」と適合する。Codebook v0.2の「否定的証拠の不完全性」注記の代表事例として追加可能。

**2. 標識不整合（Labeling mismatch）の検出**

SRG-2（B-2/U-3）において典型的な標識不整合パターンを確認した。[REDACTED: substantial verbatim quotation; see Tier 9]（仮定を適切に標識）の直後、[REDACTED: substantial verbatim quotation; see Tier 9]と叙述し、さらにAbstractでは"Mechanistic experiments point to a stereoinvertive S_N2-like oxidative addition"と仮定依存性が完全に消去されている。仮定標識の位置が本文中の一文前半に集約され、Abstract・結論部での消失という構造。RI-06と連動する「仮定→推論→主張への昇格の連鎖」パターンとして記録する。

**3. RI-06「サイクルレベル輸入」の事例確認と新たな観察**

SRG-3はRI-06「スコープ注記: サイクルレベル輸入」の事例である。Scheme 4の触媒サイクル全体が他系のNiクロスカップリング研究（refs 11a, 11b）から構成されており、環状硫酸エステルという新規基質クラスでの適用可能性が実証されていない。新たな観察：本論文はNi酸化状態（Ni(0)/Ni(II) vs. Ni(I)/Ni(III)）を特定しないまま図示することで、2016年当時活発に論争中だった酸化状態問題（GAP-4参照：Diao/Stahl、Engle/Sanford等によるNi(I)/Ni(III)研究）を暗黙に回避している。「酸化状態不特定の中立的図示」が機構的曖昧性を保存するパターンとして記録する。

**4. PRI-11（Mechanism-kinetics decoupling）の第三事例の可能性**

SRG-3のB-18/B-19は、提案触媒サイクル（Scheme 4）から速度式を代数的に導出せずに、「ArMgBrの性質によってerが変化する」という選択性パターンのみからpyboxNi(Ar)が反応種であると結論する構造を示している。これはPRI-11の定義（「提案触媒サイクルまたは反応機構から速度式を代数的に導出せずに、観測速度次数との一致のみで機構を支持している」）に類似する構造を持つ（速度次数ではなく選択性パターンからの推論だが、速度論的支持なしに機構種を同定する点は同型）。Breitenfeld 2014、Pengfei 2024に続く第三事例として記録し、PRI-11昇格の判断材料として提供する。定義の精緻化提案：「速度次数との一致のみ」を「速度論的データなしに」と広げることで、選択性パターンからの種の同定も包摂できる。

**5. VQ-2層別非対称性の確認**

合成的主張層（VQ-2 qualified）と機構的主張層（VQ-1止まり）の層別非対称性は、合成コミュニケーションが機構実験を追加することでVQ水準を実質的に下げる可能性（機構主張追加→未解消RI増加）というUQSの評価構造とジャーナルのインセンティブ構造の乖離点を示す。機構的インパクトを強調する論文が定量的にはVQ評価で不利になるという逆説は、VQ-2 Method要件の運用上の重要な境界条件として記録する価値がある。

本ケースは既存の制度設計の複数要素を追加確認しつつ、標識不整合パターンの具体的事例とPRI-11定義精緻化に向けた新規材料を提供した。
```

---

> **Tier 8 redaction notice**: This file is a redacted copy of the corresponding Tier 3 / Tier 9 output. Verbatim source-paper quotations have been replaced by `[REDACTED: see source paper §<loc>; full text retained in Tier 9 reviewer-only deposit]` markers, preserving location references and our own analytical content. Bibliographic fields (title, authors, journal, year, DOI), analytical labels (`evidence_chain:` with B-/U-/A-/C- internal IDs), short technical terms, and our own analytical text are not redacted. The redaction was applied by `scripts/redact_for_tier8.py` and, for this version, by `scripts/build_paperA_R1_public.py` with `scripts/redact_source_ngram_runs.py` (scripts of the project repository; they are not deposited).
