prompt_version: stage3-v2-20260416
model_info: claude-sonnet-4-6

# 科学的知見の再認定判定票

## Tellis, Kelly, Primer, Jouffroy, Patel, Molander 2016（Accounts of Chemical Research, Account）

### §1 Claim Architecture

**コア主張：**
本論文は「単電子トランスメタル化」をCsp³–Csp²結合形成の新しい機構パラダイムとして提示する。Novelty柱は二つ：（1）光触媒/Ni二元触媒系が、二電子トランスメタル化では最も反応性の低いCsp³炭素を最も反応しやすいカップリングパートナーへ変換するという機構的反転の概念（有機トリフルオロボラートおよびアルキルビス（カテコラト）シリケートを主要ラジカル前駆体として使用）；（2）NiIII中間体のC–Ni結合ホモリシス/再結合平衡（DKR機構）が、ラセミ体アルキルBF₃Kからのエナンチオリッチ生成物形成を可能にするという立体制御モデル。Utility柱：室温・可視光という温和条件、高官能基許容性（未保護アミン、複素環、プロトン性官能基）、ベンチスタブルな試薬の組み合わせ。

**Layered structureの判定：**
D-1で確認された通り、論文の主張は少なくとも3つの独立した層を形成する。（1）パラダイム概念層：「単電子活性化モードがCsp³反応性階層を反転させる」という機構原理の主張。（2）合成スコープ層：有機トリフルオロボラート、アルキルシリケート、チオエーテル化を含む複数基質クラスにわたる合成的実証（Figures 5–7, 11–15）。（3）機構/立体化学モデル層：DFT計算とDKR機構によるPathway B優位性と立体制御の説明（Figures 9–10）。これらの層は独立しており、一つの反証によって全体が崩れる単一階層構造ではない。層間の依存関係：層3（DFT/DKR）は層1（パラダイムの計算的支柱）を部分的に支持しており、層3の弱体化は層1の実験的支柱不在をより顕著にする。しかし層2（合成スコープ）は層3の成否に依存しない。

---

### §2 SRG / CLA → RI / ER / EP Crosswalk

**SRG-1 [触媒サイクル素反応の実験的不在]**

* **Primary RI**: RI-03 [Unobserved explanatory] — 触媒サイクルの説明中核を担うNiI, NiIII中間体が、EPR・in situ UV-Vis・ストイキオメトリックモデル反応のいずれによっても直接観測されておらず、速度論的拘束も受けていない。また、PC*の選択的消光種がStern-Volmer実験で同定されておらず、量子収率が未測定のためラジカル連鎖機構との識別が不可能
* **Secondary RI**: RI-04 [Unreplicated discriminator] — 「制御実験が明確に支持した（unequivocally supported）」（B-1）という識別力の高い機構的主張が、実験データの提示なしに使用されており、肯定的機構証拠として機能している
* **ER**: 提案触媒サイクルの各素反応を個別に実験的に支持することが必要：（a）PC*の主要消光種の同定（Stern-Volmer消光定数kq測定）；（b）NiI（EPR活性d⁹）およびNiIII（d⁷）の分光学的直接観測またはストイキオメトリックモデル反応での生成確認；（c）自由ラジカル中間体の存在証明（ラジカルクロック基質）；（d）量子収率測定（ΦP）によるラジカル連鎖機構の排除
* **EP**: EP-03a [Direct-observation / state-assignment pack]
* **Case-specific実装**: （a）触媒6（[Ir{dF(CF₃)ppy}₂(bpy)](PF₆)）とPhCH₂BF₃Kをアセトン/MeOH中でStern-Volmer消光実験に付し、BF₃K、Ni(COD)₂、amine additive（2,6-ルチジン）の各kqを比較して主要消光種を同定；（b）触媒量NiCl₂(dme)存在下でのin situ EPR測定によるNiI（g≈2.1–2.2、超微細結合）の検出；（c）シクロプロピルカルビニルBF₃Kまたは5-ヘキセニルBF₃Kをラジカルクロック基質として使用し、開環/環化生成物の同定；（d）PhCH₂BF₃K + 4-bromoanisole系での量子収率測定（ferrioxalate actinometry等）
* **注記**: B-1（収束度=2/3 high, gap=none）、U-1（PC*消光種, V2 high）、U-2（NiI/NiIII酸化状態, V2 high）、U-3（ラジカルクロック, 収束度=2/3 high）、U-6（量子収率, V2 medium）、U-8（PC⁻→NiII SET, V2 medium）。high_convergence_low_gapに位置するB-1, U-3がコアの未観測問題を構成する。RI-04の「否定的証拠の不完全性」パターン（§6参照）：「unequivocally」という修辞的強調が実データ不在を隠蔽。

---

**SRG-2 [DFT計算モデル系の代表性不足]**

* **Primary RI**: RI-06 [Imported model] — ベンジルラジカル+ブロモベンゼン系（共鳴安定化ラジカル）で構築されたDFTモデル（Figure 9）による結論——pathway B（ラジカル付加→酸化的付加）優位性、DKR機構の熱力学的成立——が、論文が合成的に最重要と位置づける二級未活性化アルキル系（ラジカル安定化エネルギーが大幅に異なる）への対象系での同型性実証なしに輸入されている
* **Secondary RI**: RI-01 [Reporting integrity] — DFT計算条件の不統一（SMD-water対実験溶媒acetone/MeOHまたはDMF；分散補正D3BJ不記載；スピン汚染⟨S²⟩非監視；TS検証の正規モード解析不記載；IRC不記載）により独立評価不能
* **ER**: DKRモデルおよびpathway B優位性が、合成的に重要な二級未活性化アルキルラジカル系（例：シクロヘキシルBF₃K）においても成立することを、実験溶媒SMD・D3BJ分散補正付きの同一計算レベルで実証する必要がある；同時に、DFT計算条件の標準的報告要素の完全な開示が必要
* **EP**: EP-06a [Analogy-validation pack]
* **Case-specific実装**: 化合物38（シクロペンチルBF₃K）および化合物50（シクロヘキシルOTf含有系の類型）に相当するシクロアルキルラジカル＋ブロモベンゼン系について、SMD-ジオキサン（実験溶媒）・D3BJ補正・LANL2DZ → 6-311+G(d,p)での計算でNiIII C–Ni結合ホモリシスΔGとpathway A/B活性化エネルギー差を計算し、ベンジル系との定量的比較（ラジカル安定化エネルギー差の影響）を提示する
* **注記**: U-7（収束度=3/3 all high, gap=none — high_convergence_low_gap最優先候補）、B-8（DFT方法論, 収束度=2/3 medium）。RI-06 Codebook注記（v0.2a）「サイクルレベル輸入」の明確な事例：pathway B優位性という触媒サイクル全体の機構的結論がベンジル系から輸入されている。

---

**SRG-3 [DKR立体化学モデルの動力学的検証不在]**

* **Primary RI**: RI-03 [Unobserved explanatory] — DKR機構の動力学的核心（khomolysis >> kRE、すなわちNiIII C–Ni結合ホモリシスが還元的脱離より速いという仮定）が、温度依存性er測定・速度論的同位体効果（KIE）・速度定数実測のいずれによっても実験的に拘束されていない
* **Secondary RI**: RI-08 [Unquantified reliability] — 計算値vs実測値の立体選択性相関（Figure 10B）がn=3データ点であり、R²・RMSE・誤差範囲の記載なし；Hammett解析による立体的vs電子的寄与の分離なし
* **ER**: DKR機構の速度論的優位性を（1）温度依存性er測定（−20°C〜+60°Cの範囲でerの温度依存性を測定し、DKR≡速度論的制御の特徴的な温度依存パターンを確認）；（2）重水素標識によるKIE；（3）n≥8の立体的・電子的に多様なアリールブロミドによる拡張実験と統計的相関（R²、RMSE付き）で実証する必要がある
* **EP**: EP-03a [Direct-observation / state-assignment pack]; EP-08a [Replication / uncertainty pack]
* **Case-specific実装**: （a）eq 2の系（PhCH(Me)BF₃K + 4-CO₂Me-C₆H₄Br + L1配位子）について−20°C, 0°C, 25°C, 40°C, 60°Cでのer測定とArrheniusプロット；（b）同系でのα-重水素標識基質（PhCD(Me)BF₃K）を用いたKIE測定；（c）para-, meta-, ortho-置換アリールブロミド（n=8以上）での立体選択性測定とHammett σ相関
* **注記**: B-6（er=75:25の単一条件, 収束度=2/3 medium）、B-13（n=3相関, 収束度=2/3 medium）、U-4（DKR動力学仮定, V2 high）。SRG-1とSRG-3の依存関係：DKR機構はNiIII中間体（SRG-1未観測）のホモリシスを前提とするため、SRG-1が解消されなければSRG-3の速度論的検証は前提を欠く。

---

**SRG-4 [Dropped Quantitative Benchmark]**

* **Primary RI**: RI-09 [External superiority] — 序論で定量的根拠として引用した先行法の条件（refs 7a–7f: 95–115°C、24–110 h；ref 9: Csp>Csp²>Csp³速度階層）が、結果節において共通基質を用いた数値比較によって裏付けられていない
* **Secondary RI**: なし
* **ER**: 先行Pd触媒二電子Suzuki–Miyaura法（少なくともref 7cまたは7dの一条件）と共通基質（二級アルキルBF₃K＋ArBr）を用いた直接比較実験（収率、反応時間、副生成物プロファイル）が必要
* **EP**: EP-09a [Internal benchmark pack]
* **Case-specific実装**: 化合物38（シクロペンチルBF₃K + 4-CO₂Me-C₆H₄Br）を代表基質として、Dreher/Sandrock/Molander 2008条件（Pd(OAc)₂, n-Bu₂PAd, Cs₂CO₃, PhMe/H₂O, 100°C, 24h）と本法（Ni(COD)₂/dtbbpy/光触媒6, 26 W CFL, rt）を同一基質で並行実験し、収率・選択性・質量収支を比較
* **注記**: C-1（refs 7a–7f, Dropped Quantitative Benchmark, symmetric_pattern=yes）、C-2（ref 9, 速度階層の定量的根拠のみ引用）。

---

**SRG-5 [合成スコープの質量収支・再現性不在]**

* **Primary RI**: RI-08 [Unquantified reliability] — 全スコープ収率（Figures 5–7, 11–15）が単回実験の単離収率であり、標準偏差・繰り返し実験なし；低収率基質（≤65%）での副生成物同定と質量収支の閉鎖なし
* **Secondary RI**: なし
* **ER**: 少なくとも代表的ベンチマーク基質（3–5化合物）について繰り返し実験（n≥3）による収率平均と標準偏差の報告；低収率基質での副生成物の同定（LC-MS等）と質量収支の閉鎖
* **EP**: EP-08a [Replication / uncertainty pack]
* **Case-specific実装**: 化合物7（75%）、化合物38（72%）、化合物75（alkylsilicate-azaborine, 71%）について繰り返し実験（n=3）を実施してSD報告；化合物20（54%）、化合物64（32%）等の低収率例でのプロト脱ボロン化、ホモカップリング、アミン酸化生成物の同定と収率合計（目標値：≥90%）
* **注記**: B-3（質量収支, V1 high）、B-11（再現性, V1 high）。Account形式ではcommunication-era toleratedだが、方法論的完全性の観点からmodern-era deficient。

---

**SRG-6 [分析条件の開示不在]**

* **Primary RI**: RI-01 [Reporting integrity] — ee/er測定（キラルHPLC条件：カラム名・移動相・温度・ラセミ体キャリブレーション）およびCV測定（溶媒・支持電解質・作用電極・走査速度・内部標準・数値的Eox）が主テキストに不在であり、定量的主張の横比較・独立評価が不能
* **Secondary RI**: なし
* **ER**: Figure 10Bのer値について：HPLC分析条件の完全開示と生成物の絶対配置の確認（CD等）；B-10のCV測定について：測定溶媒中でのEox数値（V vs SCE）の報告と光触媒の励起状態ポテンシャルとの数値的ΔE比較
* **EP**: EP-01a [Reporting-coherence pack]
* **Case-specific実装**: 化合物32（57% ee、Figure 10B）のHPLC分析：カラム（Chiralpak IA/IBまたは同等品）・移動相（ヘキサン/IPA比）・温度・フロー速度の記載と、ラセミ体32のHPLCキャリブレーションデータ；アルキルシリケート基質類のCVデータ：DMF/Bu₄NPF₆中でのEox（V vs SCE）数値と触媒6の*E(PC+/PC*)との比較（ΔE > 0の実証）
* **注記**: B-9（HPLC条件不在, V3 medium）、B-10（CV条件・数値不在, V1 medium）。Account形式のcommunication-era toleratedに該当するが、定量的機構主張の独立検証を妨げる点でmodern-era deficient。

---

**SRG-7 [SET熱力学の定量的不在]**

* **Primary RI**: RI-05 [Qualitative overread] — PC⁻からNiII種XへのSET（触媒サイクルの閉鎖ステップ）の熱力学的自発性が、実験溶媒中での数値ポテンシャル比較なしに「favorable」と定性的に主張されている
* **Secondary RI**: RI-03 [Unobserved explanatory] — このSETに対応する速度論的証拠（速度定数kSET）も存在しない
* **ER**: 実験溶媒（acetone/MeOH, DMF）中での触媒6還元体の酸化ポテンシャルE(PC⁻/PC)と、NiII-dtbbpy種Xの還元ポテンシャルE(NiII/Ni⁰)を電気化学的に測定または文献値から取得し、ΔE = E(NiII/Ni⁰) − E(PC⁻/PC) > 0（ΔG < 0）を数値的に確認する
* **EP**: EP-05a [Quantitative-ranking substantiation pack]
* **Case-specific実装**: DMF/Bu₄NPF₆電解液中での触媒6の還元電位（E(PC⁻/PC)）とNiCl₂(dtbbpy)系のE(NiII/Ni⁰)をCV（走査速度100 mV/s、Fc/Fc⁺内部標準）で測定し、ΔEとΔGを報告
* **注記**: C-3（refs 14, 15を定性引用、symmetric_pattern=yes）、U-8（PC⁻→NiII SET thermodynamics, V2 medium）。SRG-1との連結：このSETが熱力学的に不成立であればNi⁰再生が困難となり、触媒サイクル全体の閉鎖機構が崩れる。

---

SRG外：CLA

**CLA: [競合実験化学選択性の速度論的起源]**（D-4候補5、U-5/B-12）

* **Primary RI**: RI-05 [Qualitative overread] — 競合実験（eq 3）で観察されたCsp³-BF₃K対Csp²-ArBF₃Kの化学選択性（91% vs 0%）が、速度論的制御か熱力学的制御かの議論なしに「反応性階層の逆転」として機構的に帰属されている
* **Secondary RI**: RI-04 [Unreplicated discriminator] — 単一の基質比・単一条件での競合実験データから、機構的に高い識別力を持つ結論を導出
* **ER**: 各BF₃Kの独立した反応速度測定（kobs）または反応進行率の時間分解測定によって、化学選択性の速度論的起源を実証する；異なる[Csp³-BF₃K]/[Csp²-ArBF₃K]比での競合実験を実施して選択性の比依存性を確認
* **EP**: EP-05a [Quantitative-ranking substantiation pack]; EP-04a [Discrimination / replication pack]
* **Case-specific実装**: PhCH₂BF₃K（33）とPhBF₃K（34）の各々を単独でPhBr（35）と反応させ、kobsを比較；競合実験を[33]/[34] = 1:1, 2:1, 1:2で実施してkobs比と選択性比の対応を確認
* **注記**: U-5（chemoselectivity origin, V2 medium, 独立）、B-12（単一データ点, V1 medium）。D-1 layered structureの「パラダイム概念層」に直結する項目。

---

**CLA: [チオエーテル化HAT機構と選択性制御]**（D-4候補7、B-14）

* **Primary RI**: RI-05 [Qualitative overread] — チオエーテル化のHAT機構がBDE論拠（C–H vs S–H BDE差14 kcal/mol）のみから推論されており、同位体標識・ラジカルトラップによる直接証拠がない
* **Secondary RI**: RI-07 [Unsupported boundary] — C–C（クロスカップリング）とC–S（チオエーテル化）の選択性を制御するパラメーターが実験的に調査されておらず、条件による選択性制御の境界が未定義
* **ER**: 重水素標識実験または速度論的同位体効果によるHAT機構の直接証拠；温度・チオール濃度・光触媒/Ni比等を体系的に変えたC–C/C–S選択比の定量的マッピング
* **EP**: EP-05a [Quantitative-ranking substantiation pack]; EP-07a [Boundary-test pack]
* **Case-specific実装**: （a）PhSD（重水素標識チオフェノール）を用いた反応での生成物の重水素組み込み率のNMR/MS測定；（b）alkylsilicate 99、ArBr、チオール濃度（0–2 equiv）・温度（0–60°C）を系統的に変えたC–C生成物とC–S生成物のGC-MS定量実験
* **注記**: B-14（thioetherification, V1 medium, 独立）。D-4候補7に対応。CLA-2のRI-07は拡張適用（v0.2a）：「C–Cカップリングが不可能でチオエーテル化のみが進行する条件」という否定的境界主張が実験的データなしに暗示されている。

---

### §3 現在のVQ判定

**現在判定: VQ-2 (Method)**

**VQ-1 [Observation] は通る。**
生成物の構造同定（RI-02）は原著論文（refs 16–21, 32, 36, 39等）のレベルで実施されており、化合物番号に対応するキャラクタリゼーション（NMR、MS等）は一次文献に存在する。本Account内では構造式が化合物番号で明示されており、RI-02の実質的な要件は満たされている。Non-fatalとして、B-11（単回実験収率）は残存するがRI-02の定義内では致命的でない。

**VQ-2 [Method] は通る。**
VQ-1継承を前提に、RI-01（SRG-6：HPLC・CV条件不在）はAccountジャンル慣行（2016年）内でcommunication-era toleratedとして非致命的。RI-07（B-4：失敗基質不記載、B-7：光触媒比較なし）も紙幅制約内で非致命的。SRG-5（RI-08：再現性）は残存するがmethod全体の成立を根底からは覆さない。ただし、SRG-6（RI-01）とSRG-5（RI-08）はmodern-era deficientに該当し、現代の再認定では補強が必要。

**VQ-3 [Mechanism] は未達。**
未解消Fatal RI：
- RI-03（SRG-1）：NiI/NiIII中間体の直接観測なし、各素反応の速度論的拘束なし、量子収率未測定——触媒サイクルの説明中核を担う種が未観測のまま機構が「確立」として語られており、VQ-3の必須条件を原理的に満たさない。
- RI-03（SRG-3）：DKR動力学的仮定（khomolysis >> kRE）の実験的検証なし——立体制御モデルの核心が速度論的に拘束されていない。
- RI-06（SRG-2）：ベンジル系DFT結論の二級アルキル系への外挿——機構モデルの対象系での同型性が未実証であり、DFT-based機構結論が対象系に適用可能かどうかが原理的に不明。
RI-05（SRG-7）も残存し、VQ-3を限定する（SRG-7のSETが実際には熱力学的に不利な場合、サイクル閉鎖機構が成立しない可能性）。RI-04（SRG-3、CLA: 競合実験）はNon-fatalだが主張の強度を弱める。

**VQ-4 [Benchmark] は未達。**
VQ-3未達を継承。加えてRI-08（SRG-5）とRI-09（SRG-4）も未解消。

**層別VQ非対称性：**
§1のLayered structureで同定された3独立層について：
- **合成スコープ層（層2）単独では：** RI-02は解消、RI-07はAccount形式内で許容。この層は機構的主張を持たないためRI-03・RI-06の致命的未解消がVQ水準を制限しない。Full Paper展開（refs 16–21等）でのデータ開示を前提にすれば、合成スコープ層はVQ-2相当に到達済みであり、再現性（RI-08）の解消によってVQ-4要件を部分的に満たせる水準にある。
- **パラダイム概念層（層1）単独では：** RI-09（ベンチマーク不在）がVQ-4への障壁。機構的原理の主張はRI-03・RI-06に間接依存するためVQ-3充足には機構層の解消が前提。現在VQ-2。
- **DKR/機構モデル層（層3）単独では：** RI-03（DKR速度論）とRI-06（ベンジル系外挿）が致命的。VQ-2止まり。この層がVQ-3に到達するためにはSRG-1・SRG-2・SRG-3の全解消が必要であり、3層中最も高い補強コストを要する。

---

### §4 Era-Norm Annotation

**communication-era tolerated:**

- **B-1（制御実験データ不記載）**: Accounts of Chemical Research形式では実験詳細を一次論文（ref 16）に委ねることが確立された慣行であり、「制御実験が明確に支持した」という記述は2016年当時のAccountの記述文体として許容された。
- **B-3, B-11（質量収支・再現性不在）**: 2016年当時のAccount形式の紙幅制約と単離収率の単回報告慣行の範囲内であり、一次論文（Full Paper群）への参照が期待されていた。
- **B-7（Ir/Ru光触媒の定量比較なし）**: Account形式では選択された最適条件の提示のみが期待され、選択の定量的根拠の記載は2016年当時必須ではなかった。
- **B-9, B-10（HPLC・CV条件不記載）**: Account形式では実験条件詳細は原著論文（refs 32, 34）に委ねられる慣行があり、2016年当時のAccount文体では主テキストへの完全開示は必須でなかった（modern-era deficientにも該当）。
- **C-4（背景引用のengagement不在）**: 概念的文脈設定引用として許容される背景情報の提示であり、個別データの結果節での利用は当時のAccount形式では期待されていなかった。
- **B-8の一部（LANL2DZ選択・IRC不記載）**: 2016年当時、Ni錯体のDFT計算におけるLANL2DZ使用とIRC省略はNJOC・OLレベルの計算論文でも一般的であり、当時の報告基準内として許容された。

**modern-era deficient:**

- **B-8（DFT方法論の多重欠落）**: 現代（2024年）のcomputational organic chemistry基準では、実験溶媒一致のSMDモデル（SMD-water対acetone/MeOHは誤り）、D3BJ分散補正、TS検証（1虚の正規モード解析）、IRC、スピン汚染⟨S²⟩の監視が必須報告要素であり、特にΔΔG‡ ≈ 0.1 kcal/molレベルのDKR立体選択性予測においてSMD溶媒ミスマッチは結論を無効化しうる。
- **U-7（ベンジル系モデルの代表性不在）**: 現代のNi/photoredox DFT論文では、主要基質クラスへの外挿妥当性の計算的検証（cross-validation）が標準的に要求される。
- **SRG-1（量子収率測定不在）**: 2018年以降の主要光触媒研究誌（JACS, JORG, ACS Cat.等）では量子収率測定が機構的主張の必須補強として定着しており、現代基準では標準的報告要件。
- **SRG-3（n=3統計的不十分）**: 現代の立体選択性モデル検証では、少なくともn=6–8のデータ点とR²/RMSEの統計的指標の報告が期待される。
- **B-9, B-10（分析条件）**: 現代の定量的ee・Eox主張には分析条件の完全開示が必須（両タグに該当）。
- **C-1（ベンチマーク比較不在）**: 現代の方法論論文では、SIに少なくとも1件の先行法との共通基質比較が標準的に要求される。

---

### §5 最短補強ルート

**VQ-3への最短ルート（第一目的関数）：**

1. **EP-03a [Direct-observation / state-assignment pack]（SRG-1対応）** — [Ir触媒6]/PhCH₂BF₃K系でのStern-Volmer消光実験（PC*の主要消光種同定）・in situ EPRによるNiI検出・シクロプロピルカルビニルBF₃Kラジカルクロック・量子収率測定を組み合わせて実施することで、RI-03（SRG-1）の複数サブ問題を同時前進させる最大情報利得EP。RI-03（SRG-1）を前進。

2. **EP-06a [Analogy-validation pack]（SRG-2対応）** — 代表的二級未活性化アルキルラジカル系（シクロヘキシル、シクロペンチル）でのDFT計算（SMD-ジオキサン・D3BJ補正付き）によるpathway B優位性とDKR ΔGの再現的検証。RI-06（SRG-2）を前進。

3. **EP-03a [Direct-observation / state-assignment pack]（SRG-3対応）** — eq 2系での温度依存性er測定（−20°C〜+60°C）とKIE実験によるkhomolysis >> kRE仮定の実験的拘束。EP-08aの一部（n=3→n≥8への拡張）を同時実施することでSRG-3を包括的に前進。RI-03（SRG-3）、RI-08（SRG-3部分）を前進。

認定ゲート順注記：実験投入順は情報利得順（EP-03a → EP-06a → EP-03a/SRG-3）だが、最終認定はVQ-1 → VQ-2 → VQ-3 → VQ-4のゲート順で確定する。VQ-3認定にはRI-03（SRG-1, SRG-3）とRI-06（SRG-2）の両者の解消が必須であり、上記3ステップはいずれも欠かせない。

**VQ-4への最短ルート（第二目的関数、VQ-3通過を前提）：**

4. **EP-09a [Internal benchmark pack]（SRG-4対応）** — 代表的二級アルキルBF₃K基質を用いた先行Pd法との共通基質直接比較実験によりRI-09（SRG-4）を解消。RI-09を前進。

5. **EP-08a [Replication / uncertainty pack]（SRG-5対応）** — 代表基質（n≥3）の繰り返し実験と低収率基質の副生成物同定によりRI-08（SRG-5）を解消。RI-08を前進。

認定ゲート順注記：VQ-4達成はVQ-3の全要件継承後にRI-08とRI-09の両解消を必要とする。

---

### §6 制度設計への寄与

**RI-06「サイクルレベル輸入」の新代表事例：**
本ケースはRI-06（Imported model）のCodebook注記v0.2a「サイクルレベル輸入」の明確な代表事例を提供する。個別素反応ステップの類推ではなく、触媒サイクル全体の機構的結論（pathway B優位性、DKR機構の成立）をベンジル系から二級アルキル系に一括輸入する構造が確認された。このモデル系選択がcomputation-feasibility（ベンジルラジカルの計算容易性）に主導されており、合成的重要性の高い基質クラス（二級未活性化アルキル）に対してcross-validationなしに結論が外挿されている。

**PRI-11（Mechanism-kinetics decoupling）昇格候補の追加確認：**
本論文でもPRI-11の定義パターンが確認された：「提案触媒サイクル（Figure 4B, 9）から速度式を代数的に導出せずに、DFT計算によるエネルギー面のみで機構的結論を支持している」。Breitenfeld 2014（提案）、Pengfei 2024（確認）に続く独立3報目。PRI-11の昇格基準（独立2報確認）を超えており、Codebook v0.3への正式昇格を推奨する。

**RI-03「Predicted-but-unpursued」サブタイプの提案：**
SRG-1の分析において、RI-03のCodebook注記v0.2aで定義された「Available-but-unutilized characterization」（取得済みデータの未活用）とは異なる新サブタイプが観察された：「提案モデルが中間体の存在を明示的に予測するにもかかわらず、その観測が試みられてすらいない」パターン。NiI/NiIIIの直接観測やラジカルクロック実験は技術的に実行可能であるにもかかわらず実施されていない（量子収率測定も同様）。このパターンを「Predicted-but-unpursued」としてRI-03の注記に追加候補として記録する。

**否定的証拠の不完全性パターンの典型事例：**
B-1の「Control experiments unequivocally supported」という記述が§6で記録すべき典型例である：陰性の対照実験（触媒なし・光なし条件での生成物不形成）が「明確な機構的支持」として使用されているが、質量収支の閉鎖も速度論的ウィンドウ評価もなく、「unequivocally」という修辞的強調語が実際のデータ不在を隠蔽する構造を形成している。RI-04のcase-specific実装例として記録する。

**VQ判定のEra-norm分類に関する新知見：**
Account形式が複数のRI（RI-01, RI-07, RI-08）をcommunication-era toleratedに系統的に分類させる構造が明確になった。同一実験内容がFull Paperとして発表された場合のVQ水準とAccount形式でのVQ水準の間に系統的乖離が生じる。本論文のAccount判定（VQ-2）と、対応するFull Paper群（refs 16–22等）の推定VQ水準（VQ-2〜3）の間の非対称性は、Account形式特有の評価バイアスとして記録する。この乖離はVQ判定基準マトリクスに「形式係数（Format Factor）」として組み込む可能性を検討すべき制度設計的知見である。
