```
prompt_version: stage3-v2-20260416
model_info: claude-sonnet-4-6

# 科学的知見の再認定判定票

## Meck, Omer et al. 2025（Journal of the American Chemical Society, Communication）

### §1 Claim Architecture

**コア主張の要約：**
本論文はPd(OAc)₂/キラルホスホロアミダイト配位子L1を用いた不斉aza-Heck環化反応により、医薬品として重要なクアタナリーヒダントイン（5,5-二置換体）をエナンチオ豊富な形で合成する方法を報告する。Novelty柱は二つ：（1）クアタナリーヒダントインへの不斉aza-Heck反応という反応様式の初例（先行するaza-Heck反応はいずれも三級炭素中心の形成にとどまる）、（2）α,β-不飽和アミドからの1工程基質調製による操作簡便性。Utility柱は、(R)-メフェニトイン（抗てんかん薬）の最初の不斉合成による医薬品合成応用実証。定量的達成指標は「21化合物、最高98% ee」。

**Layered structure：**
Stage 2 D-1が同定したように、主張は4層の独立構造を持つ。

- 第1層（反応の新規性）：クアタナリーヒダントインへの最初の不斉aza-Heck環化。この層はスコープ品質や機構的理解とは独立して成立する。
- 第2層（基質アクセシビリティ）：α,β-不飽和アミドから1工程でaza-Heck基質を調製するスキーム（Scheme 1）。完全な手順・収率（最高86%）が主テキストに記述されており、4層中で最も方法論的に透明。
- 第3層（エナンチオ選択性・スコープ）：21化合物の基質スコープと「最高98% ee」の定量的主張。ee決定法・収率基盤・再現性データの欠落（SRG-4）により独立検証が阻害されている。
- 第4層（医薬品合成応用）：(R)-メフェニトイン最初の不斉合成。グラムスケール収率急落（B-06）・中間体の絶対配置決定法の不在（B-07）・最終生成物eeの未報告（B-07）により実証の基盤に空白がある。

第2層は4層中で最も堅牢であり、第3層・第4層は測定基盤の不透明性によって独立した検証に抵抗する。第1層（反応新規性）は最も多くの反証に対して生き残るが、機構的証拠の完全な欠落（SRG-1）により「なぜ立体制御が起きるか」という問いには答えられない。

---

### §2 SRG / CLA → RI / ER / EP Crosswalk

**SRG-1 [mechanism absent]**（A-01, B-16, U-01）

* **Primary RI**: RI-03 [Unobserved explanatory] — 提案されたPd(0)/Pd(II)触媒サイクル（Figure 3）の全中間体（Pd-N酸化的付加体、パラジウサイクル、Pd-H種）がいずれも捕捉・同定されておらず、速度論的拘束もなされていない。
* **Secondary RI**: RI-06 [Imported model] — carbo-Heck反応で確立されたPd(0)/Pd(II)サイクルを、N-O基質に対して同型性の実証なしにサイクルレベルで輸入している（Codebook v0.2a: RI-06 スコープ注記「サイクルレベル輸入」に該当）。
* **ER**: aza-Heck触媒サイクルの少なくとも一つの素反応ステップ（N-O酸化的付加、移行的挿入、またはβ-ヒドリド脱離）について、直接観測・速度論的拘束・同位体標識のいずれかによる実験的証拠を提供すること。
* **EP**: EP-03a [Direct-observation / state-assignment pack]; EP-06a [Analogy-validation pack]
* **Case-specific実装**: （1）Pd(0)/L1（Pd₂(dba)₃/2L1当量）と基質4を–40°CのBuCN中で当量反応させ、³¹P NMRおよびESI-MSによりPd-N酸化的付加体の存在を確認する（EP-03a）。（2）²Hラベル化アルケン基質（α-²H₁または末端CD₂）を合成し、生成物5中の²H位置をNMRで確認することでsyn挿入→syn β-ヒドリド脱離の立体化学的経路を実証する（EP-06a）。
* **注記**: A-01はhigh_convergence_low_gap（V1=high, V2=critical; convergence=2/3）。U-01は自己矛盾的不在（論文が予測するPd-N中間体・パラジウサイクルの不在）。RI-03とRI-06が同一SRGで共起しており、RI-06（輸入モデルの同型性検証）の解消にはRI-03（中間体の直接観測）の解消が前提条件となる依存関係が存在する。

---

**SRG-2 [scope outliers unexplained]**（B-01, B-02, B-03, B-04）

* **Primary RI**: RI-07 [Unsupported boundary] — 化合物10（4-Br基質：12%収率, 63% ee）、化合物18–19（テトラ置換アルケン：63–43% ee）、N,N-ジアルキル基質（完全不反応）、N-Ph基質（不反応）の各スコープ失敗・異常値について、境界主張が系統的試験なしに提示されている。
* **Secondary RI**: RI-05 [Qualitative overread] — 「pharmaceutically relevant hydantoins」という主張の射程を、ハロゲン感受性・N置換基制約という系統的制限の定量的含意なしに維持している（D-4-4）。
* **ER**: 各失敗クラス（ハロゲン感受性、N-Ph不反応、N,N-ジアルキル不反応、高温での選択性低下）について、パラメトリックな変数系列（電子的・立体的系列）を実施し、境界が連続的か離散的かを実験的に確立すること。
* **EP**: EP-07a [Boundary-test pack]; EP-05a [Quantitative-ranking substantiation pack]
* **Case-specific実装**: （1）N1置換基系列（N-H, N-Me, N-Et, N-nPr, N-Cy, N-Bn, N-Ph, N,N-ジアルキル）全体にわたるee・収率マッピングを実施し、N置換基依存性の連続的プロファイルを確立する（EP-07a）。（2）ハロゲン系列（p-F, p-Cl, p-Br, p-I）のベンジル基質について、各ハロゲンでの競合副反応（C-X活性化生成物）を定量し、Br基質10の異常値の原因を特定する（EP-07a）。（3）BIRT-377・GLGP-0492・Mesantoin骨格の置換パターンが本法で合成可能か境界外かを系統的に評価する（EP-05a）。
* **注記**: B-02はhigh_convergence_low_gap（V1=high, V2=high; convergence=2/3, temperature_gap=none）; B-03はhigh_convergence_low_gap（V1=high, V3=high; convergence=2/3, temperature_gap=none）; B-01, B-04はV1のみ（high severity）。

---

**SRG-3 [aza-Wacker byproduct]**（B-05, B-15）

* **Primary RI**: RI-04 [Unreplicated discriminator] — aza-Heckメカニズムを支持する主要な実験的根拠（化合物26がラセミ体）が、単一基質・単一時点の観察（Scheme 4の5%副生物）に基づいており、時系列的な質量収支閉鎖も21化合物スコープ全体にわたる系統的確認もなされていない。
* **Secondary RI**: RI-01 [Reporting integrity] — aza-Wacker副生物量がスコープ21化合物で一切報告されておらず、競合経路の寄与の横比較ができない。
* **ER**: 代表的なモデル基質（化合物4）について、反応の時系列をchiral SFCで追跡し、[5]・[26]・ee(5)の時間プロファイルを取得すること；また21化合物のスコープ全体にわたり、反応終了時の26の量を報告すること。
* **EP**: EP-04a [Discrimination / replication pack]; EP-01a [Reporting-coherence pack]
* **Case-specific実装**: （1）化合物4の反応（標準条件）を0, 2, 4, 8, 12, 24時間後にaliquotとして取り出し、chiral SFC-MSで[5]・[26]・ee(5)を定量する。追加実験として外部添加したラセミ体26を24時間後の反応混合物に投入し、ee(5)の変化を追跡することで26→5変換の寄与を定量する（EP-04a）。（2）Scheme 3の全21化合物について、反応終了時のcrude混合物に対してchiral SFC分析を実施し、副生物量を表の脚注として報告する（EP-01a）。
* **注記**: B-05はhigh_convergence_low_gap（convergence=3/3: V1=medium, V2=high, V3=medium）で、3エージェント中最高のcross-field convergenceを持つ。

---

**SRG-4 [quantitative claim disclosure]**（B-08, B-11, B-14）

* **Primary RI**: RI-01 [Reporting integrity] — Scheme 3の21化合物にわたり、ee決定法（カラム種・条件）が主テキストに記載されず、単離収率とNMR収率が化合物ごとの明示なしに混在し、再現性データが存在しないため、定量的主張（「最高98% ee」）の横比較評価基盤が成立していない。
* **Secondary RI**: RI-08 [Unquantified reliability] — 天井値付近のee（97–99%）について反復測定・誤差推定がなく、精度評価ができない。
* **ER**: （1）全21化合物について使用したキラルカラム・移動相・流速・検出法を開示すること。（2）化合物ごとに収率決定法（単離/NMR）を明示すること。（3）代表的な化合物（最低でも5, 11, 18, 19）について独立した2回以上の反応でのee値を報告すること。
* **EP**: EP-01a [Reporting-coherence pack]; EP-08a [Replication / uncertainty pack]
* **Case-specific実装**: （1）Table 1の脚注にSFC-MS分析（ref 20参照）が記載されているため、全スコープ化合物への適用を明示し、カラム種（例: OD-H, IC）と保持時間を開示する（EP-01a）。（2）Scheme 3の各エントリに上付き記号を付けて単離/NMR収率を化合物単位で区別する（EP-01a）。（3）化合物5（最頻出モデル基質）および化合物19（最低ee）について3回の独立実験でee値を報告し、標準偏差を付与する（EP-08a）。
* **注記**: SRG-4の各項目はV3のみ（medium severity）。「up to 98% ee」という主張の定量的信頼性はee決定法・収率基盤・再現性という三開示項目の組として機能しており、個々の省略より連動した構造的不在として重要（D-4-5）。

---

**SRG-5 [scale/utility claim]**（B-06, B-07）

* **Primary RI**: RI-08 [Unquantified reliability] — グラムスケールでの収率急落（78% → 31%、化合物6）は原因分析なしに単一データポイントとして報告され、かつ(R)-メフェニトイン最終生成物（化合物30）のee値が報告されていない。
* **Secondary RI**: RI-09 [External superiority] — 「最初の不斉合成」という優位性主張が、Atkinson 2015（ref 27）との工程数・通算収率・ee の数値比較なしに維持されている。
* **ER**: （1）グラムスケール実験の収率急落について原因変数（濃度・撹拌・触媒分解等）を系統的に検討し、原因を同定すること。（2）(R)-メフェニトイン30の光学純度（ee）を報告すること。（3）Atkinson (2015) 合成と本法の工程数・通算収率・最高ee の比較表を提示すること。
* **EP**: EP-08a [Replication / uncertainty pack]; EP-09a [Internal benchmark pack]
* **Case-specific実装**: （1）化合物6のグラムスケール反応を複数の濃度（0.1, 0.25, 0.5 M）・撹拌条件で実施し、濃度依存的収率プロファイルを取得する（EP-08a）。（2）化合物30のキラルSFC分析を実施しee値を報告する（EP-08a）。（3）Atkinson 2015経路と本法の全工程（基質調製含む）を並列表示し、工程数・総収率・ee・触媒量を数値比較する（EP-09a）。
* **注記**: B-06はhigh_convergence_low_gap（V1=medium, V3=high; convergence=2/3; temperature_gap=low）; B-07はhigh_convergence_low_gap（V3=high, V1=medium; convergence=2/3; temperature_gap=low）。

---

**SRG-6 [optimization opacity]**（B-17）

* **Primary RI**: RI-01 [Reporting integrity] — 48配位子のHTEスクリーニングについて、配位子の構造クラス・選別基準（収率・ee・複合指標）・規模が記載されず、Scheme 2の「selected examples」8条件のみが提示されている。
* **ER**: スクリーニングに用いた全48配位子のリスト（またはその構造クラス分類）、一次スクリーニングの評価基準、および規模を開示すること。
* **EP**: EP-01a [Reporting-coherence pack]
* **Case-specific実装**: 全48配位子スクリーニング結果をSIに補足表として収録し（各配位子の収率・ee・主要副生物観測を記録）、L1が「uniquely effective」であることの根拠を構造的に示す。主テキストではScheme 2の8例が「selected」であることを明示する（EP-01a）。
* **注記**: V1=low (V1-Q15), V3=low (V3-Q4); convergence=2/3; temperature_gap=none。SRG-6はstandaloneであり、L1選択の合理性評価という点でSRG-1と間接的なつながりを持つ。

---

**SRG外：CLA**

**CLA-1: 配位子L9の一般性（D-4-7, grounded_in: B-09）**

* **Primary RI**: RI-07 [Unsupported boundary] — 「L1が標準スコープに最適」という境界は、mephenytoin基質（化合物28）に対してL9がL1より顕著に優れた成績（70% → 91% ee）を示した後も再検討されていない。
* **ER**: L9をL1と、代表的なサブクラス（官能基系列、スピロ環、テトラ置換アルケン、N置換体）から各1化合物以上で比較し、L9の一般性またはmephenytoin特異性を実験的に判定すること。
* **EP**: EP-07a [Boundary-test pack]
* **Case-specific実装**: 化合物5, 11, 18, 22を用いたL1 vs. L9のhead-to-head比較実験（標準条件下）を実施し、ee差を定量する。
* **注記**: B-09はV1のみ（medium severity）。D-1の第3層（selectivity claims）に直接関わる：L9が一般的に優れていれば「最高98% ee」の主張はL9を基準として再評価が必要となる。

---

**CLA-2: 塩基の触媒サイクルにおける機能的地位（D-4-8, grounded_in: B-12）**

* **Primary RI**: RI-03 [Unobserved explanatory] — nBu₂N（5当量）がN-H脱プロトン化（→ Pd-N中間体生成）として機能するか、HX補足剤（β-ヒドリド脱離後）として機能するか、または両段階に関与するかが特定されておらず、Figure 3の触媒サイクルにおける塩基の化学量論的関与が未観測のまま。
* **ER**: 塩基量を変化させた速度論実験（反応次数の決定）、または塩基を段階的に加える制御実験によって、塩基が関与するステップを同定すること。
* **EP**: EP-03a [Direct-observation / state-assignment pack]
* **Case-specific実装**: nBu₂Nを0, 1, 2, 5当量に変化させた反応の初期速度（0–2時間の収率/ee）を測定し、塩基量に対するee・収率の依存性プロファイルから塩基の機能的役割を推定する。
* **注記**: B-12はV2のみ（medium severity）。根拠のうちB-16（SRG-1のmember）との重複部分はSRG-1で処理済み。CLA-2はB-12固有の「塩基役割」という要素を独立した欠落として記録する。

---

### §3 現在のVQ判定

**現在判定: VQ-1 (Observation)**

**VQ-1 [Observation]（RI-02要件）：通る（Non-fatal残存あり）**
主要スコープ生成物（化合物5–24）の化学構造は、NMRデータとキラルSFC分析によって同定されている。絶対配置は化合物25のPMB脱保護体を既知(S)-異性体と対照することで確立されている（eq 2）。(R)-メフェニトイン（化合物30）については光学回転の文献値との一致が絶対配置の根拠とされているが、比較した文献値・条件の詳細が主テキストに記載されていない（B-07: RI-02の非致命的残存として記録）。テトラ置換アルケン系（化合物18）についてはNMR収率での報告があり単離物のキャラクタリゼーションが明示されていないが、これも非致命的。全体としてVQ-1は通る。

**VQ-2 [Method]（RI-01, RI-07要件 + VQ-1継承）：未達**
RI-01はSRG-4（ee決定法の主テキスト未記載、収率基盤の混在）に起因して部分的に残存するが、Table 1の脚注にSFC-MS分析（ref 20）が参照されており、SI（ref 16）に詳細条件が含まれると推定されるため非致命的と判定する。一方、RI-07はSRG-2（ハロゲン感受性・N,N-ジアルキル不反応・N-Ph不反応の境界について系統的境界試験なし）において致命的に残存する：現在のデータから境界が連続的か離散的かを判定することができず、「pharmaceutically relevant hydantoins」という主張の射程の定量化が不可能。**VQ-2の主要ブロッカーはRI-07（SRG-2）**。CLA-1（L9一般性: RI-07）もVQ-2の阻害要因だが、SRG-2が論文の中心的スコープ主張に直結するため優先度が高い。

ただし**第2層（基質合成アクセシビリティ）単独では**：Scheme 1の完全な手順と収率が記述されており、RI-01・RI-07いずれも致命的には残存しない → VQ-2に到達。

**VQ-3 [Mechanism]（RI-03, RI-04, RI-06要件 + VQ-2継承）：未達**
VQ-2が未達であることを前提として、RI-03（SRG-1: Pd中間体の未観測）、RI-04（SRG-3: aza-Wacker排除証拠の非再現性）、RI-06（SRG-1: carbo-Heckサイクルの無検証輸入）の全てが残存する。特にRI-03はU-01（自己矛盾的不在）を伴う致命的残存：論文が提案するサイクルが予測する中間体が、論文の実験範囲内でいずれも観測・探索されていない。RI-05（SRG-2の二次RI: 「pharmaceutically relevant」の定性的過読）も残存しており、VQ-3はQualifiedにも達しない。

**VQ-4 [Benchmark]（RI-08, RI-09要件 + VQ-3継承）：未達**
VQ-3が未達の状態で、RI-08（SRG-4: 再現性データなし; SRG-5: グラムスケール収率急落の根本原因未解明）、RI-09（SRG-5, C-01, C-03: Archambeau/Atkinson両文献との数値比較なし）が残存。

---

### §4 Era-Norm Annotation

**communication-era tolerated:**

- B-08（ee決定法の主テキスト未記載）: JACS Communication（2025年）はキラルカラム種・保持時間・移動相をSIに委ねることが慣行であり、ref 20（Korch et al., ACS Catal. 2022）によるSFC-MS法のレファレンスがTable 1に存在するため当時の基準で許容される。
- B-11（収率基盤の混在を脚注のみで示す）: 通信形式では規模制限のある化合物でNMR収率を用いることは標準的であり、脚注での開示が通常の実践。
- B-14（反復測定・誤差推定なし）: JACS Communicationにおいて全スコープ化合物の反復測定は紙幅的に不可能であり、当時の基準で許容。
- B-16（基底状態配座エネルギー計算の理論レベル・ソフトウェア未記載）: 計算結果のみを主テキストに示しSI（ref 16）に詳細を委ねることは通信形式の通例。
- B-17（HTEスクリーニング詳細の省略）: 48配位子スクリーニングの全データをSIに委ね、主テキストに選択例8条件のみを示すことは通信形式の紙幅制約に照らして許容。

**modern-era deficient:**

- B-07（絶対配置決定法の不記載）: 2025年のJACS Communicationで「最初の不斉合成」を主張する場合、X線結晶構造解析またはVCD/ECD計算による絶対配置確定の明示が現代標準；光学回転の文献値との一致のみでは（参照値の記載すらないため）deficient。これはVQ-1の非致命的残存に対応し、現代基準では主テキストへの明示が必要。
- SRG-1（機構的検証の完全欠落）: 2025年のJACS Communicationで新規Pd/キラルリガンド触媒系を報告する場合、少なくとも一つの非線形効果（NLE）試験または動力学同位体効果（KIE）測定が現代的標準として期待される；本論文ではこれらが全て欠如しており現代査読基準に照らしてdeficient。
- B-02, B-03（スコープ内外れ値の無説明）: 現代のJACS Communicationでは、スコープ表の顕著な外れ値（19: 33%, 43% ee）に対する1–2文の説明が期待されるが、本論文では無コメント。
- B-06（グラムスケール収率急落の根本原因未提示）: 薬剤合成への応用を主張する論文で、グラムスケール実験での収率の半減以下を原因分析なしに提示することは、現代の応用訴求型Communicationではdeficient。

---

### §5 最短補強ルート

**第一目的関数: VQ-2 (Method) への到達**

VQ-2の主要ブロッカー: RI-07（SRG-2: 境界未試験）。非致命的残存: RI-01（SRG-4）。

**VQ-2 への最短ルート：**
1. EP-07a [Boundary-test pack] — N置換基系列（N-H, N-Me, N-Et, N-nPr, N-Cy, N-Bn, N-Ph, N,N-ジアルキル）とハロゲン系列（p-F, p-Cl, p-Br, p-I）の2系列の基質を合成し、各系列でのee・収率プロファイルを取得することでスコープ境界を連続的データで確立する。RI-07を前進させる。
2. EP-01a [Reporting-coherence pack] — Scheme 3の脚注を改訂して各化合物の収率決定法を化合物単位で明示し、SFC分析法（カラム・条件）を表形式で開示することで横比較基盤を確立する。RI-01（非致命的）を完全解消しVQ-2認定の残存障壁を除去する。

認定ゲート順注記：実験投入は情報利得順（EP-07a優先）だが、VQ認定はVQ-1 → VQ-2 → VQ-3 → VQ-4の継承ゲートで確定する。

---

**第二目的関数: VQ-3 (Mechanism) への到達**（VQ-2通過後）

**VQ-3 への最短ルート：**
1. EP-03a [Direct-observation / state-assignment pack] — Pd(0)/L1と基質4の当量反応を低温で実施し、³¹P NMR・ESI-MSによってPd-N酸化的付加体の存在を確認する。触媒サイクルの第一ステップを実験的に拘束する。RI-03を前進させる（注記: RI-06解消にはRI-03解消が前提条件）。
2. EP-04a [Discrimination / replication pack] — 時系列chiral SFC監視（0–24時間）と外部添加ラセミ26実験により、aza-Wacker排除証拠の質量収支を閉鎖し、NLE試験（配位子ee対生成物ee）で不斉決定ステップの触媒化学量論を確立する。RI-04を前進させる。
3. EP-06a [Analogy-validation pack] — ²Hラベル化アルケン基質を用いた同位体実験、またはHammett解析（電子効果のσ–ee/σ–log k相関）によりcarbo-Heckサイクルのaza-Heck転用の妥当性を実験的に検証する。RI-06を前進させる（EP-03aの後に実施）。

認定ゲート順注記：VQ-3認定はVQ-2の全要件を前提として継承する。

---

**VQ-4 (Benchmark) への到達**（VQ-3通過後、参考）

**VQ-4 への最短ルート：**
1. EP-08a [Replication / uncertainty pack] — グラムスケール最適化（濃度・撹拌系列）と化合物30のキラルSFC分析（最終生成物eeの確認）。RI-08を前進させる。
2. EP-09a [Internal benchmark pack] — Atkinson 2015との工程数・収率・ee比較表、およびArchambeau ref 10と構造的に重複するエントリの収率・ee比較。RI-09を前進させる。

---

### §6 制度設計への寄与

**1. RI-06「サイクルレベル輸入」の高透明性実例**
本ケースはCodebook v0.2aの「RI-06 スコープ注記: サイクルレベル輸入」の典型的実例を提供する。aza-Heck触媒サイクル全体（Pd(0)/Pd(II)、N-O酸化的付加、syn移行的挿入、syn β-ヒドリド脱離）がcarbo-Heck文献から個別素反応の類推ではなくサイクル単位で輸入されており、N-O基質に特有の素反応（N-O vs. C-X酸化的付加速度・選択性・Pd-N中間体安定性）は一切検証されていない。

**2. RI-03/RI-06共起における依存関係構造の記録**
SRG-1でRI-03とRI-06が共起しており、RI-06（輸入モデルの同型性検証）の解消にはRI-03（中間体の直接観測）の解消が論理的前提となる「依存関係付き共起」が確認された。この依存構造はEP投入順序設計（EP-03a→EP-06aの順序制約）に反映した。今後の複数ケース分析で同パターンが確認されれば、「RI-03+RI-06共起は順序制約付き」という規則としてCodebookへの追記を検討すること。

**3. 標識不整合（Labeling mismatch）の記録**
Figure 3のキャプション「Proposed aza-Heck mechanism」と本文の "we favor a Heck-like pathway" という仮説標識が、素反応の記述語 [REDACTED: substantial verbatim quotation; see Tier 9] という事実的記述語と並列されている。仮説標識が文頭の1文のみに集約され、以降の叙述が事実的語で記述されるパターンは、RI-06とRI-03が連動した標識不整合の典型例として記録する。

**4. 否定的証拠の不完全性（RI-04）の実例確認**
SRG-3（B-05）は「aza-Wacker生成物26がラセミ体 → aza-Heck経路が正しい」という否定的証拠の肯定的解釈の典型例。Codebook注記「否定的証拠の不完全性」のcase-specific実装として以下の欠如を記録する：（a）質量収支の閉鎖（26の生成量の全スコープ報告）、（b）速度論的ウィンドウ評価（26→5変換が主反応に対してどの程度の速度で起きるか）、（c）26のラセミ化が形成後にin-situで起きる可能性の排除（26が立体化学的に非ランダムに形成されてからラセミ化する経路を排除していない）。

**5. 通信→Full Paper遷移の自動解消パターンの予測**
SRG-4（RI-01: B-08, B-11, B-14）とSRG-6（RI-01: B-17）はいずれも通信→Full Paper遷移で自動解消される高い蓋然性を持つ。ただしSRG-5（RI-08: グラムスケール収率急落）とSRG-1（RI-03: 中間体未観測）はFull Paper展開では自動解消されない（前者は新規実験、後者は独立した機構研究を要する）。§4のEra-Norm Annotationとの対応が確認される。

**6. 新PRI候補：なし**
本ケースで新しいPRI候補は検出されなかった。本ケースは既存の制度設計（RI-03, RI-04, RI-06, RI-07）の典型的共起パターンを確認し、RI-06のサイクルレベル輸入サブタイプの代表事例を提供した点で制度的価値がある。
```

---

> **Tier 8 redaction notice**: This file is a redacted copy of the corresponding Tier 3 / Tier 9 output. Verbatim source-paper quotations have been replaced by `[REDACTED: see source paper §<loc>; full text retained in Tier 9 reviewer-only deposit]` markers, preserving location references and our own analytical content. Bibliographic fields (title, authors, journal, year, DOI), analytical labels (`evidence_chain:` with B-/U-/A-/C- internal IDs), short technical terms, and our own analytical text are not redacted. The redaction was applied by `scripts/redact_for_tier8.py` and, for this version, by `scripts/build_paperA_R1_public.py` with `scripts/redact_source_ngram_runs.py` (scripts of the project repository; they are not deposited).
