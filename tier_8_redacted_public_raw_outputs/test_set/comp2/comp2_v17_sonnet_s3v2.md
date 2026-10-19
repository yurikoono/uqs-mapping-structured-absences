```
prompt_version: stage3-v2-20260416
model_info: claude-sonnet-4-6

# 科学的知見の再認定判定票

## Palladino et al. 2023（ACS Catalysis, Full Paper）

### §1 Claim Architecture

**コア主張：**
本論文のコア主張は「銅フリーHCS反応は、Pd(II)酸化的付加錯体へのアルキンの直接配位機構（Heck型カルボパラジウム化）を経由し、対イオンに依存して中性経路（ハライド）または陽イオン経路（トリフラート）の2経路が並存する」である。Novelty柱は三点：(i) 触媒条件を模倣した化学量論的実験によるPd(II)–Pd(II)トランスメタル化機構の実験的否定、(ii) 二級アミン塩基（TMG, PYR）が前駆体還元とカルボパラジウム化障壁低下の両方に寄与するという実験・DFT的実証、(iii) アリールトリフラートのHCSにおける初のDFT計算。Utility柱は、HCSプロトコル設計（塩基・配位子・対イオン選択の合理化）への機構的指針提供である。

**Layered structure：**
主張は独立した4層として読める。
- (a) **実験的観察層**：B複合体からのアルキン直接配位がM経由経路より速い（V_max比較）—— BとMの競争反応（Table 3, Figure 5）に基づき独立して成立
- (b) **前駆体還元層**：二級アミン（TMG, PYR）がTEAより効率的に前駆体を還元し、Rタイプ中間体を形成する —— Table 1/4の観察に基づき独立して成立
- (c) **DFT計算層**：TS0 = 20.2 kcal/mol（中性）, TS1^PPh3 = 32.0 kcal/mol（無触媒）, TS0^OTf = 24.0 kcal/mol（陽イオン）の障壁比較が機構選択を定量化 —— 計算のみに基づき、実験層から独立して問い直せる
- (d) **二経路選択層**：ハライドでは中性経路、トリフラートでは陽イオン経路 —— (c)に強く依存し、実験的証拠（Table 3, Table 4）と組み合わせて成立

層間依存関係：DFT計算層(c)の方法論的信頼性が失われると、二経路選択の定量的根拠（TS0 vs. TS0^OTf の障壁差）が失われる。ただし実験層(a)と前駆体還元層(b)はDFTに対して独立して成立し、「直接配位がPd(II)–Pd(II)経路より速い」という方向的結論は実験証拠のみで維持できる。一方、「中性 vs. 陽イオン経路の切り替えが対イオンによって決まる」という定量的機構命題は(c)(d)層の信頼性に直接依存する。

---

### §2 SRG / CLA → RI / ER / EP Crosswalk

**SRG-1 [DFT methodology reporting completeness]**

* **Primary RI**: RI-08 (Unquantified reliability)
* **Secondary RI**: RI-01 (Reporting integrity); RI-09 (External superiority) — C-1 adjunct
* **ER**: DFT障壁値（TS0 = 20.2 kcal/mol等）が機構的証拠として機能するためには、(1) 分散補正（D3BJ等）の有無と採用の根拠、(2) 溶媒和モデル（PCM/SMD/COSMO-RS）の名称と参照値照合、(3) 熱力学補正プロトコル（RRHO vs. 準RRHO; PPh₃低振動数モードへの対応）、(4) Pd/Iへの相対論的取扱い（ECP明示）、(5) Mårtensson（ref 13b）の計算障壁との同一座標上での数値比較（C-1）を満たす必要がある。
* **EP**: EP-08a (Replication / uncertainty pack); EP-09a (Internal benchmark pack)
* **Case-specific実装**: PBE/def2-TZVP計算へのD3BJ分散補正追加単点計算; SMD(DMF)溶媒和の明示的記述; PPh₃トルシオンに対する準RRHOエントロピー補正の適用; Pd・Iへのdef2-TZVP-ECPの明示確認; Mårtensson 2008（Organometallics 27, 2490–2498; ref 13b）の脱プロトン化機構DFT障壁をFigure 10aと同一エネルギー座標で対比する補充表の追加
* **注記**: B-1（convergence=3/3, high_convergence_low_gap; primary）, B-11, B-12, B-13, B-17（convergence=2/3, V1=high, V2=high, temperature_gap=none）, C-1（RI-09 adjunct; Mårtensson比較の欠如）。SRG-1は論文最大のSRG（5項目+1 adjunct）であり、DFT計算層の信頼性基盤全体に関わる。

---

**SRG-2 [Quantitative NMR measurement protocol]**

* **Primary RI**: RI-08 (Unquantified reliability)
* **Secondary RI**: RI-01 (Reporting integrity)
* **ER**: Table 4の平衡定数kとFigure 5のV_maxを機構的証拠として使用するためには、すべての検出³¹P種（B°, Ra, OPPh₃, 遊離PPh₃）の²¹P T₁測定値と繰り返し遅延パラメータ、V_maxの基礎となる速度論モデル（速度式・適合法・サンプリング間隔）、Table 4全エントリの複数回測定と誤差バーが必要である。
* **EP**: EP-08a (Replication / uncertainty pack); EP-01a (Reporting-coherence pack)
* **Case-specific実装**: DMF-d₆中のB°_NO₂, Ra, OPPh₃に対する³¹P T₁の反転回復法測定と報告; Figure 5の速度論トレースへの一次速度式またはMichaelis-Menten型適合と残差プロット; Table 4の全11エントリに対するn≥3複数回測定と95%信頼区間; OPPh₃スパイク標準による積分校正の実施
* **注記**: B-3（primary, V3=high, convergence=1/3）, B-4（V1=medium, V3=high, convergence=2/3, temperature_gap=low）, B-5, B-10。SRG-2の欠如により、k差（Table 4エントリ1–9; PYRとTMG間で約4–5倍）の統計的有意性が評価不能。

---

**SRG-3 [Single-timepoint experimental design]**

* **Primary RI**: RI-03 (Unobserved explanatory)
* **Secondary RI**: RI-08 (Unquantified reliability)
* **ER**: Table 1（前駆体還元, 10分固定）とTable 4（base/B°比率, 時間不変性未確認）の単一時点測定が「真の平衡」または「変換完了」を示すためには、複数時点での測定による時間不変性の確認が必要である。特にTable 1のTEA不活性（entries 5–6）については、TEAが「熱力学的に不能」か「動力学的に遅い」かを区別するためにTime courseが不可欠である。
* **EP**: EP-03a (Direct-observation / state-assignment pack)
* **Case-specific実装**: Table 1全エントリに対する0–120分の³¹P NMR経時測定（5–10分間隔; TEAエントリは24時間まで延長）; Table 4の各base/B°比率についての2時点以上での時間不変性確認（NMR収集後30分 vs. 120分での比率比較）
* **注記**: B-8（V1=medium, V3=medium, convergence=2/3, temperature_gap=none; primary）, B-5（SRG-2とも共有; 真の平衡確認の欠如）。SRG-3はTable 1でのTEA不活性結論（「TEAは前駆体還元ができない」）の動力学的対熱力学的解釈、ならびにTEAベースHCSプロトコルへの示唆に直接影響する。

---

**SRG-4 [Experimental verification of elementary steps]**

* **Primary RI**: RI-03 (Unobserved explanatory)
* **Secondary RI**: RI-04 (Unreplicated discriminator)
* **ER**: 提案触媒サイクルの素反応（中間体NからcisC経由の塩基媒介脱プロトン化TS3 = 12.6 kcal/mol; 複合体MからのRE生成kRE）を機構的証拠として使用するためには、これらの素反応を直接検証する実験（重水素化アルキンによるkH/kD測定; Mの速度論的特性化）が必要である。
* **EP**: EP-03a (Direct-observation / state-assignment pack); EP-04a (Discrimination / replication pack)
* **Case-specific実装**: PhC≡CDを基質としたTable 3相当の競争反応（またはFigure 5と同一の速度論トレース）によるkH/kD測定（基底値は計算値TS3 = 12.6 kcal/molから~3–7程度を予測）; Figure 5と同一の化学量論的NMRプラットフォームを用いたM単独の経時測定（M → 4a のkRE）とM + PhC≡CH 競争反応（kcoord）の測定
* **注記**: A-2（deferred, T1, linked to U-1）, U-1（severity: high; 提案サイクルのTS3 = 12.6 kcal/molに対する実験的証拠なし; 通常のHCS条件で実行可能な実験が未実施であることが自己矛盾的不在）, U-2（severity: high; Mの速度論的競合性が未定量にもかかわらず4a生成がMのマーカーとして使用; REは「本研究の対象外」と明記しながら4a診断に利用——自己矛盾的不在）。SRG-4の未解消は触媒サイクルが実験的に閉じていないことを意味する。

---

**SRG-5 [Product quantification methodology]**

* **Primary RI**: RI-01 (Reporting integrity)
* **Secondary RI**: RI-08 (Unquantified reliability)
* **ER**: 3a/4a比が機構的診断（複合体Mの関与の有無）として機能するためには、HPLC検出波長での3a（アリールアルキン）と4a（1,3-エニン二量体）の相対応答係数（モル吸光係数比）の較正、Table 3競争反応の質量収支、主テキストへの溶媒スクリーン8エントリ（entries 8–15）の定量サマリーが必要である。
* **EP**: EP-01a (Reporting-coherence pack); EP-08a (Replication / uncertainty pack)
* **Case-specific実装**: 既知濃度の3aと4aを用いたHPLC応答係数較正曲線（240 nm付近のUV吸収波長）の作成と報告; Table 3全エントリの質量収支（%炭素回収率）の報告; Table 3 entries 8–15の主テキストへの定量的収率サマリーテーブルの追加（溶媒別の3b収率%）
* **注記**: B-6（mass balance欠如; primary）, B-7（V3=medium; HPLC較正欠如）, B-16（V1=medium, V3=medium, convergence=2/3, temperature_gap=none）。SRG-5の欠如により、論文の主要診断メトリック（3a/4a比）の定量的精度が評価不能。

---

**SRG外：CLA**

**CLA-1: 否定的証拠の検出下限**

* **Primary RI**: RI-07 (Unsupported boundary)
* **Secondary RI**: RI-04 (Unreplicated discriminator)
* **ER**: 「複合体Mは標準的HCS反応に関与しない」という境界主張は、PPh₃添加条件下での³¹P NMRによる「Mの非検出」に基づくが、この主張が成立するためには³¹P NMRの検出下限（触媒前駆体量に対する%）と触媒サイクルへの有意な関与を排除するために必要な感度の明示が必要である。
* **EP**: EP-07a (Boundary-test pack)
* **Case-specific実装**: PPh₃添加触媒条件下（DMF-d₇, 25°C）での既知量Mスパイク実験による³¹P NMR検出限界の定量的確立（例：触媒量の何%未満まで検出可能か）; 触媒ターンオーバーに対するM関与の許容上限の計算（例：M経由経路が10%に達するために必要なM濃度と検出限界の比較）
* **注記**: B-19（単独アイテム）。自己矛盾的不在のパターン：論文は4aの生成をMの関与の証拠として使用しているが（Scheme 2 Route B）、「Mが検出されない＝Mが関与しない」という論理の境界条件（何%未満の形成であれば「関与しない」と言えるか）を定量化していない。これはRI-07の否定的境界主張適用例（Codebook v0.2a拡張）。

---

**CLA-2: モデル基質の電子的代表性**

* **Primary RI**: RI-07 (Unsupported boundary)
* **Secondary RI**: RI-05 (Qualitative overread)
* **ER**: 「機構は芳香族置換基に関わらず同一」という主張は、電子的に極端なp-ニトロフェニルハライドを唯一の詳細機構研究モデルとして構築されており、電子的に中性または供与性のアリールハライド（例：PhI, p-MeO-PhI）でのV_max, R複合体分布, 3a/4a比の少なくとも1組の定量的比較が必要である。
* **EP**: EP-07a (Boundary-test pack); EP-05a (Quantitative-ranking substantiation pack)
* **Case-specific実装**: B^I_CH₃（p-methyl; Table 3 entries 3–4でB-CH化合物が一部使用済み）に対するFigure 5相当の速度論トレース測定と V_max(B^I_CH₃) vs. V_max(M)比較; B^I_Ph（unsubstituted）複合体でのTable 4相当のbase/B°比率とkの測定および電子的置換基効果（Hammett σ）との定量的相関
* **注記**: B-15（V1=medium）。Table 3 entries 3–4でB^I_CHが定性的にテストされているが、速度論データと平衡定数データはB^I_NO₂とB^I_CH₃の比較として提供されていない（「similar outcome」という定性的記述のみ）。

---

**CLA-3: 二経路選択の制御原理**

* **Primary RI**: RI-05 (Qualitative overread)
* **Secondary RI**: RI-08 (Unquantified reliability)
* **ER**: 「対イオンの種類（ハライドvs.トリフラート）が経路を決定する」という結論は、Pd-X結合の配位能または配位子交換活性化エネルギーという定量的パラメータとの対応関係なしに、I/OTfの2点DFT計算のみで支持されている。経路選択の物理化学的制御パラメータを特定するには、Br/Clに対するDFT計算または実験的パラメータ（kOA, Pd-X結合エンタルピー, A-1の測定不能なトリフラートk）の系統的測定が必要である。
* **EP**: EP-05a (Quantitative-ranking substantiation pack); EP-08a (Replication / uncertainty pack)
* **Case-specific実装**: Br複合体B^Br_NO₂とCl複合体B^Cl_NO₂に対するDFT反応座標計算（Figure 10aに相当）の追加実施; あるいはI, Br, Cl, OTfの4系列に対するkOA（酸化的付加速度定数）のEyring測定（25–60°C）と中性/陽イオン経路選択率との定量的相関
* **注記**: B-14（V2=medium; Br/ClのDFT計算なし）, A-1（triflate kの測定不能は陽イオン経路エネルギープロファイルの実験的検証を困難にする）。RI-05とRI-08の共起：定性的順位（halide→中性, OTf→陽イオン）は観察されているが、その物理化学的連続性（どの結合強度パラメータが閾値を決めるか）は数値なしに主張されている。

---

### §3 現在のVQ判定

**現在判定: VQ-1 (Observation)**

**VQ-1 [Observation] — 通過（Non-fatalのRI-02残存あり）**
Pd(II)中間体（B, R, C, M, L）はいずれも独立に合成・³¹P NMR特性評価が行われており、固有の化学シフト値が報告されている。MとLは独立合成により構造が特定されており、Pd(II)錯体としての同定はRI-02の要件を実質的に満たす。Non-fatalのRI-02が残存する：Ra/Rb/Rc異性体はDFT予測に基づく化学シフト比較のみで帰属されており（ref 25のDFT計算³¹P化学シフト）、X線による個別確認はない。ただし、Ra/Rbの区別が個々の触媒サイクル帰属に必須ではなく、Ra の同定（最安定異性体、Figure 6により支持）が経路論証の根幹であるため非致命的。VQ-1通過はVQ-2以上の判定に継承される。

**VQ-2 [Method] — 未達**
VQ-1通過を前提とする。RI-01がSRG-1（DFT方法論記述の欠如）において致命的に未解消である：分散補正・溶媒和モデル・熱力学補正プロトコルが不明な状態では、TS0 = 20.2 kcal/molの障壁値の定量的信頼性が独立に評価できず、二経路結論の計算的根拠が成立しない。同様にRI-01がSRG-2（NMR取得パラメータの欠如）において致命的に未解消であり、kとV_maxの信頼性が評価不能である。RI-07はCLA-1（M検出下限）とCLA-2（基質代表性）において非致命的に残存する。

ただし**実験的観察層単独では**：定性的なV_max(B) > V_max(M)の観察と競争反応での3b選択的形成（Table 3, entries 1–6）はRI-01に依存しない観察であり、この層のみはVQ-2に到達している。これは§1のLayered structureが実験層と計算層の非対称なVQ水準として現れている。

**VQ-3 [Mechanism] — 未達**
VQ-2未達を継承。加えてSRG-4においてRI-03が致命的に未解消である：触媒サイクルの2つの素反応（塩基媒介脱プロトン化TS3 = 12.6 kcal/molとMからのRE）がDFTのみで支持され、実験的に直接検証されていない（U-1, U-2）。SRG-3においてRI-03（Table 1/4単一時点設計によるTEA不活性の動力学的対熱力学的解釈）が非致命的に残存する。RI-05がCLA-3において残存するため、VQ-3に到達した場合でも「Qualified（限定的）」となる：反応経路選択の物理化学的制御原理が定性的説明に留まっている。

**VQ-4 [Benchmark] — 未達**
VQ-3未達を継承。SRG-1においてRI-08（DFT障壁の不確かさが未定量）とRI-09（Mårtensson計算値との数値比較なし、C-1）が致命的に残存する。SRG-2においてRI-08（k, V_maxの誤差バー未報告）が致命的に残存する。CLA-3においてもRI-08が残存する（Br/Cl経路のDFT障壁なし）。計算・実験の両定量基盤にわたる系統的なRI-08である。

---

### §4 Era-Norm Annotation

**communication-era tolerated:**

- B-16（溶媒スクリーン8エントリのSI委任）: ACS Catalysis 2023のFull Paper形式では選択的SI委任は許容されており、主張の方向性（溶媒独立性）はentries 1–7の主テキストデータで実証されている。
- B-5（Table 4の単一時点平衡比率）: 合成有機金属化学の2023年慣行では、³¹P NMR比率の時間不変性確認は一般的に報告されない。
- B-4（V_max報告における速度論モデル未記述）: NMR速度論的研究を主とする合成化学論文での速度式の明示はACS Catalysis 2023において普遍的要件ではない。
- B-8（Table 1の単一時点設計）: 前駆体還元のスクリーニング実験として単一時点の変換率報告は合成化学全般で通常の慣行であり、10分時点での比較は許容される。

**modern-era deficient:**

- B-1（DFT方法論：分散補正なし、溶媒和モデル未記載）: 2023年のACS Catalysisを含む主要計算化学誌では、DFT方法論の完全記述（分散補正の有無・種別、溶媒和モデル名、熱力学補正プロトコル）は標準的要件であり、査読ガイドラインで明示的に要求されている。B-1はera-norm toleratedとは言えない。
- B-17（Eyring解析または実験kobs値との計算障壁比較なし）: 機構解明を主題とするDFT論文では、計算障壁と観察速度の定量的対応が2023年現在の標準的期待である。
- C-1（Mårtensson ref 13bとの数値比較なし）: 計算機構論文で先行DFT計算を名指しで否定する場合の数値比較は、2023年の機構化学コミュニティでは期待される標準的要件。
- B-7（HPLC応答係数較正なし）: 機構診断として定量的比較（3a/4a比）を使用する場合の較正データ報告は、2023年の機構研究における定量化要件として求められる。

**両タグ該当：**

- B-3（NMR T₁未測定）: 合成化学論文の2023年慣行では広く許容されるが（communication-era tolerated）、現代のIUPAC定量NMR勧告（2021年以降）では不足として記録される（modern-era deficient）。両タグを付与し、分野内での標準化が進行中であることを注記する。

---

### §5 最短補強ルート

**VQ-2 への最短ルート：**

1. EP-01a (Reporting-coherence pack) — PBE/def2-TZVP計算へのD3BJ分散補正追加の単点エネルギー、SMD(DMF)溶媒和モデルの明示的記述、³¹P T₁値（B°_NO₂, Ra, OPPh₃）の反転回復法測定と報告、Figure 5速度論トレースの速度則明記。RI-01をSRG-1（DFT層、致命）とSRG-2（NMR層、致命）で同時前進させる。情報利得最大。

2. EP-07a (Boundary-test pack) — PPh₃添加触媒条件下のMスパイク実験による³¹P NMR検出限界の定量化; B^I_CH₃またはB^I_Ph複合体での競争反応追加（entries 3–4に対応する定量データ取得）。RI-07をCLA-1とCLA-2で前進させる。

認定ゲート順注記：最終認定はVQ-1 → VQ-2 → VQ-3 → VQ-4の継承順で確定する。EP投入順（EP-01a優先→EP-07a）は情報利得順だが、VQ-2認定にはRI-01（致命）の解消が先決。

---

**VQ-3 への最短ルート：**

3. EP-03a (Direct-observation / state-assignment pack) — PhC≡CDを基質としたFigure 5相当の速度論トレース測定によるkH/kD（一次速度論的同位体効果; TS3 = 12.6 kcal/mol予測）; Table 4の各base/B°比率の2時点以上での時間不変性確認。RI-03をSRG-4（U-1, 致命）とSRG-3で前進させる。

4. EP-04a (Discrimination / replication pack) — 化学量論的NMRによるMからのRE速度定数kREの直接測定（M単独の経時追跡: M → 4a）とM + PhC≡CH競争の速度論的分割比（k_coord/kRE）。RI-04をSRG-4（U-2）で前進させる。

---

**VQ-4 への最短ルート：**

5. EP-08a (Replication / uncertainty pack) — Table 4全11エントリに対するn≥3の複数測定と95%信頼区間; Eyring解析（25–60°C）によるkobsとΔG‡_expの決定とTS0 = 20.2 kcal/molとの比較; ωB97X-D3またはDLPNO-CCSD(T)による主要TSの単点ベンチマーク。RI-08をSRG-1, SRG-2, CLA-3で前進させる。

6. EP-09a (Internal benchmark pack) — Mårtensson 2008（Organometallics 27, 2490–2498; ref 13b）の脱プロトン化機構DFT障壁を本論文Figure 10aと同一エネルギー座標上で数値比較した補充図の作成; 両計算の方法論的差異（PBE vs. B3LYP, 溶媒和モデル差異等）の定量的評価。RI-09をSRG-1/C-1で前進させる。

認定ゲート順注記：VQ-4認定は継承原則によりVQ-3通過が前提。VQ-3はEP-03a（kH/kD, 時間課程）とEP-04a（M速度論）の完了後に確定する。実験投入の情報利得順（EP-08a優先でEP-09aは分析的）はVQ-4認定確立の論理順（EP-01a → EP-03a/04a → EP-08a/09a）と一致する。

---

### §6 制度設計への寄与

**PRI-11の独立確認:**
本論文はPRI-11（Mechanism-kinetics decoupling）の独立確認事例を提供する。提案触媒サイクル（Figure 11a,b）から速度式が代数的に導出されず、観察される選択性（3b優先形成, V_max(B) > V_max(M)）との「定性的一致」のみで機構が支持されている。SRG-4の「DFT障壁はあるが実験的kobsとの比較がない」パターン（B-17）は、Breitenfeld 2014（提案）とPengfei 2024（確認）に続く第三の独立事例として、PRI-11の2報独立確認要件を超え、正式昇格の条件を完全に満たす。

**RI-08「デュアルメソッド偽相関」パターンの記録:**
本ケースでは計算（SRG-1）と実験NMR（SRG-2）という2つの独立した定量的手法が同一の機構的結論を支持しているが、両方においてRI-08が致命的に未解消である。このパターンは「DFT障壁は実験NMR動力学と整合する」という相関的印象を与えるが、両者それぞれの信頼性（DFTの定量的精度、NMRの定量的精度）が独立に評価不能であるため、相互独立的な検証とはならない。この「dual-method RI-08 spurious convergence」パターンを、2つの異なるSRGに属するRI-08の共起が論文全体の堅牢性の錯覚を生む際の特定可能なパターンとして記録することを提案する。

**RI-07否定的境界主張の代表的ケース事例登録:**
CLA-1で検出された「検出されない → 関与しない」パターンは、Codebook v0.2aで定義されたRI-07否定的境界主張拡張適用の典型的代表事例である。「PPh₃添加でMが³¹P NMRで検出されない」を「Mは標準的HCS反応に関与しない」と解釈する際に、境界条件（検出下限と「関与する」ための最低濃度の対比）の明示が構造的に省略されている。この「陰性証拠の不完全性」は、§6で特筆すべきとして列挙された「否定的証拠の不完全性」パターン（陰性実験を肯定的機構証拠として使用する際の境界条件明示の欠如）に完全に対応し、RI-07とRI-04の共起事例として記録する。

**RI共起パターン（SRG-1内のRI-08 + RI-09）:**
SRG-1においてRI-08（定量的信頼性）とRI-09（外部比較なし）が構造的に相乗的に共起する。RI-08が解消されないと（方法論詳細の欠如）、RI-09を実施しても（Mårtensson比較を追加しても）、その比較が等価な計算レベルで行われているかを確認できない。逆に、RI-09のみ解消してもRI-08が残存するため比較の有効性が保証されない。両者の同時解消が必要であり、EP-08aとEP-09aを組み合わせることが最小限の補強セットとなる。この「RI-08+RI-09共起」パターンは、計算的証拠が実験的証拠に替わって機構決定の主証拠とされる論文において繰り返し現れるパターンとして追跡すべき。

**Era-norm: 計算化学統合論文の報告基準非整合:**
2023年のACS Catalysis Full Paperにおけるb-1（DFT方法論報告の著しい不備）は、有機合成化学と計算化学の統合研究における報告基準の分野間非整合を示している。有機合成化学の出版慣行ではDFT方法論の詳細報告（D3補正、溶媒和モデル名）は著者の自発的努力に依存し、ACS Catalysisの査読指針でも明示的要件として構造化されていない。計算的裏付けを含む機構論文へのCI（Computational Information）標準の適用がJACS/ACS Catalysisで議論されているが未制度化であり、このera-norm所見は制度化の必要性を示す事例として記録できる。
```
