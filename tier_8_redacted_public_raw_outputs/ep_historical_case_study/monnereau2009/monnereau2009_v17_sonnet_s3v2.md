```
prompt_version: stage3-v2-20260416
model_info: claude-sonnet-4-6

# 科学的知見の再認定判定票

## Monnereau et al. 2009（Advanced Synthesis & Catalysis, Full Paper）

### §1 Claim Architecture

**コア主張:**
本論文のコア主張は2本の柱から構成される。

Novelty柱：カリクサレン骨格に由来する動的バイトアングル変動を持つカチオン性Ni錯体2が、Kumada–Tamao–Corriuカップリングにおいてジホスフィン系触媒として史上最高のTOF（21250 mol(ArBr)·mol(2)⁻¹·h⁻¹）を達成した。高活性の機構的起源は、カリクサレン骨格のファニング運動が周期的にPNiPバイトアングルを拡大し、還元的脱離を促進することにある（動的バイトアングル仮説）。

Utility柱：1,3-カリクサレンジホスフィン配位子の空気安定性（PCy₃等に対する実用的優位性）、低触媒量（1×10⁻³ mol%）、電子的に多様なArBrおよびArClへの幅広い適用性。

**Layered structure:** 独立層あり。

- 層1（保護基盤層）：性能主張（記録的TOF値）、基質スコープ、空気安定性。これらは機構仮説とは原理的に独立しており、動的バイトアングル仮説が否定されても、TOF値の観察自体は成立する。
- 層2（露出層）：動的バイトアングル仮説（ファニング運動→RE促進→TOF向上）。剛直類縁体との比較が唯一の直接反証手段として著者自身に認識されており、単一の実験で崩れる可能性がある。

層間依存関係：層2の崩壊が層1を無効にしないが、SRG-1が指摘するようにTOF値の分母（活性触媒量）が内部矛盾を抱えており、層1の定量的主張（「最速」という順序的主張）の信頼性にも影響する。

---

### §2 SRG / CLA → RI / ER / EP Crosswalk

---

**SRG-1 "TOF values unreferenced to defined catalyst quantity"**

* **Primary RI**: RI-02 Object identification — 触媒活性種（41.8 ppm種）の同一性（酸化状態を含む）が代替候補を排除できる粒度で未確定
* **Secondary RI**: RI-03 Unobserved explanatory — 活性化種のNi酸化状態が直接観測も速度論的拘束もされていない；RI-08 Unquantified reliability — 活性化収率が定量されずTOF分母が不定義（論文自身の観察と矛盾）
* **ER**: TOFを明確に定義された触媒量に帰属するには、（i）100°Cジオキサン中の活性化後溶液に対する分光学的完全同定（酸化状態の確定）、（ii）定量NMRによる活性化収率の測定、が必要最低限の規範的要件である。
* **EP**: EP-02a Identity / purity substantiation pack; EP-03a Direct-observation / state-assignment pack
* **Case-specific実装**: ESI-MS（m/z、同位体パターン）および定量³¹P-NMR（内部標準：亜リン酸トリフェニル等）による41.8 ppm種の同定と残存前駆体割合の定量；EPRまたはXANESによるNi酸化状態の直接決定（Ni(0)とNi(I)の区別）
* **注記**: B-7（convergence 3/3、V3=critical）、B-6（convergence 2/3、V2=critical）、U-1（3剤収束、critical）、U-2（V2=critical単独、low_convergence_high_gap）を包含。フォールバック規則(a)(b)両方に該当する最優先SRG。RI-02とRI-03の共起パターン：RI-02解消（種の同定）だけでは触媒サイクル中間体の直接観測（RI-03）は依然未解消のため、両方の解消が必要。

---

**SRG-2 "Outperformance claim rests on insufficient benchmarking"**

* **Primary RI**: RI-09 External superiority — Introduction で「prominent diphosphines」として列挙されたdppp/dppb/dppf/DPEphosのうちdppとの一対比較のみで「全ジホスフィン系触媒を凌駕する」と主張；外部文献の活性序列（Tamao 1972）を自論文の条件では再現していない
* **Secondary RI**: RI-08 Unquantified reliability — 3.8パーセントポイントの差（50.9% vs 47.1%）に統計的不確かさが付与されていない
* **ER**: 「最速ジホスフィン系触媒を凌駕する」という比較優位性主張には、（i）Introductionで名前を挙げた全ての触媒（dppp, dppb, dppf, DPEphos）との対応条件での直接比較、（ii）識別力のある差については反復測定（n≥3）が必要である。
* **EP**: EP-09a Internal benchmark pack; EP-08a Replication / uncertainty pack
* **Case-specific実装**: 同一条件（dioxane、100°C、PhMgBr/ArBr=2:1、前活性化、ArBr/触媒=5000）での[NiCl₂(dppb)]、[NiCl₂(dppf)]、[NiCl₂(DPEphos)]との比較実験（各n=3）、および4-ブロモアニソール/dppp比較のn=3反復
* **注記**: B-5（V1=high、V3=high；2/3収束；high_convergence_low_gap）、B-2（V3=high）、C-1（Tamao活性序列未再現）、C-2（dppb/dppf/DPEphos未試験）を包含。

---

**SRG-3 "Dynamic bite-angle hypothesis lacks direct experimental support"**

* **Primary RI**: RI-06 Imported model — Pd・Rh系のバイトアングル-RE加速の関係（Marcone & Moloy 1998, Hartwig et al. 1998）を、d電子数・幾何学的選好が異なるNi系にサイクルレベルで輸入；同型性の実証なし
* **Secondary RI**: RI-03 Unobserved explanatory — 提案触媒中間体[Ni(Ar)(Ar')·1]が触媒条件下で直接観測されていない；RI-05 Qualitative overread — ArClの電子的傾向（3点）からOA律速の結論を速度論データなしに導出
* **ER**: バイトアングル動性と触媒活性の因果関係を主張するには、（i）同一骨格で動性を制限した剛直類縁体との直接触媒活性比較、（ii）Ni(II)ジアリール錯体の化学量論的RE速度測定（バイトアングル関数）、が必要最低限の規範的要件である。
* **EP**: EP-06a Analogy-validation pack; EP-03a Direct-observation / state-assignment pack
* **Case-specific実装**: (i) カリクサレン骨格を架橋基で固定した剛直類縁体Ni錯体の合成と同一条件でのKumada coupling活性比較（本論文著者が「非常に有益」と認めた実験）；(ii) NiII(Ph)(Ph')(calixdiphosphine)錯体の単離と化学量論的RE（ビフェニル生成）速度定数のEyring解析、対照ジホスフィン（dppp）との比較
* **注記**: A-2（V2-Q10=high；剛直類縁体の不在）、U-3（ArBrのRDS未特定・RE/OA律速の矛盾）、B-10（動性と触媒回転の速度比較条件不一致；3/3収束medium）、C-3（Pd/Rh外挿）を包含。high_convergence_low_gapのフォールバック(b)に該当。U-3は自己矛盾的不在：ArClではOA律速と主張するが、動性がRE促進なら、ArBrでのRDSの同定が動性仮説の内的整合性に不可欠。

---

**SRG-4 "GC quantification methodology lacks analytical validation"**

* **Primary RI**: RI-01 Reporting integrity — 17種の構造的に多様なビアリール生成物に対して同一のデカン内部標準校正を適用し、各生成物のFIDレスポンスファクターが未検証；測定基盤の均一性が担保されていない
* **Secondary RI**: RI-08 Unquantified reliability — 全エントリが単回測定であり、不確かさ推定が存在しない
* **ER**: GC変換率を17種の生成物にわたって比較可能な定量指標として使用するには、各生成物のデカン対比レスポンスファクター較正曲線の独立測定・報告が必要であり、代表的エントリでは反復測定と標準偏差が必要である。
* **EP**: EP-01a Reporting-coherence pack; EP-08a Replication / uncertainty pack
* **Case-specific実装**: 各ビアリール生成物について独立した検量線作成（濃度5点、デカン対比）；最高活性エントリ（1-bromonaphthalene/50000、4-bromotoluene/50000、4-bromoanisole/dppp比較）についてn=3反復
* **注記**: B-1（V3=high；1/3収束）、B-2（V3=high；1/3収束）、B-3（V3=high；1/3収束）、B-4（V1=medium；1/3収束）を包含。各B項目は1〜2エージェントのみの評価だが、グループとして論文の全定量的主張の測定基盤を構成する。

---

**SRG-5 "Active catalyst species and reaction pathway uncharacterised"**

* **Primary RI**: RI-03 Unobserved explanatory — Ni(0)/Ni(II)触媒サイクルを支持する種・状態が直接観測も速度論的拘束もされていない（活性種のNi酸化状態未同定；触媒サイクル中間体未検出）
* **Secondary RI**: RI-04 Unreplicated discriminator — 配位子なし対照実験（B-9）が65°C/THFという単一条件で実施され、主触媒条件（100°C/dioxane）との不一致により均一系対不均一系の区別として機能しない
* **ER**: Ni(0)/Ni(II)触媒サイクルを提案する論文には、（i）活性種のNi酸化状態同定、（ii）触媒条件と一致した条件での均一系の実証（水銀試験またはTEMPO阻害）が必要である。
* **EP**: EP-03a Direct-observation / state-assignment pack; EP-04a Discrimination / replication pack
* **Case-specific実装**: (i) 水銀滴下試験（100°C、dioxane中で5当量のHg(0)を添加した対照実験）；(ii) TEMPO（5 mol%）添加実験（Ni(I)ラジカル経路の探索）；(iii) 100°C dioxane条件での配位子なし対照実験（主触媒条件とのmatched-pair control）
* **注記**: U-2（V2=critical；SRG-1とも共有）、U-4（V1=high、V2=high；均一系対不均一系）、B-9（V1=high、V2=high；non-matched control）を包含。SRG-5はSRG-1と一部重複するが（U-2共有）、SRG-1はTOF分母の定義問題に焦点を当て、SRG-5は触媒機構の均一性と経路同定に焦点を当てる独立した問い。

---

**SRG外：CLA**

**CLA-1: ブロモメシチレンのスコープ失敗未説明**

* **Primary RI**: RI-07 Unsupported boundary — 立体的に嵩高い基質での著しい低変換率（15.6%、同条件の4-bromotolueneの約1/6）が帰属なしに提示されており、「congested aryl bromidesを効率的に変換する」という本文の記述（Table 3エントリ10の直前）と不整合
* **Secondary RI**: なし
* **ER**: 基質スコープ表中に顕著な外れ値（同構造カテゴリ内で5倍以上低い変換率）が存在する場合、その立体的・電子的要因の帰属または高触媒量での再試験が必要である。
* **EP**: EP-07a Boundary-test pack
* **Case-specific実装**: ブロモメシチレン/触媒=1000（1 mol%）での反応実施；2,6-ジメチルブロモベンゼン（単軸立体障害）との比較によるオルト置換基の立体効果の定量化
* **注記**: B-12（V1=medium；1/3収束）単独。D-4候補6に対応。いずれのSRGのmember_itemsにも含まれない。D-1のnc-3（基質スコープの幅）に直接抵触する。

---

### §3 現在のVQ判定

**現在判定: VQ-1 (Observation)**

---

**VQ-1 Observation（RI-02）: 通過（Non-fatal残存あり）**

論文の観察水準の主張——「化合物2がPhMgBrとArXのKTCカップリングを触媒する」および「1-ブロモナフタレンとのカップリングで最高変換率42.5%が得られた」——は、活性種のNi酸化状態（RI-02）が未同定であっても成立する。触媒活性の「存在」という観察そのものは否定されない。RI-02はNon-fatalとして残存する。

ただし、SRG-1のRI-02は性能定量層（特定TOF値の帰属）に対してはFatalに近い。層別VQ非対称性を参照。

---

**VQ-2 Method（RI-01、RI-07 + VQ-1継承）: 未達**

VQ-1がNon-fatalとして通過することを前提として評価する。

SRG-4のRI-01（GCレスポンスファクター未検証）が未解消であり、17種の生成物にわたる変換率数値の絶対的信頼性が保証されていない。CLA-1のRI-07（ブロモメシチレンのスコープ失敗未説明）も未解消。「どの基質/条件でこの触媒が機能するか」という方法水準の問いに答えるためには、測定の信頼性と基質境界の説明が必要であり、両者が残存する限りVQ-2は未達である。

---

**VQ-3 Mechanism（RI-03、RI-04、RI-06 + VQ-2継承）: 未達**

VQ-2が未達であるため継承原則により未達。個別評価: RI-03（SRG-1: 活性種未観測；SRG-5: 触媒サイクル中間体未観測）、RI-04（SRG-5: 均一系実証なし）、RI-06（SRG-3: Pd/Rhモデルの輸入未検証）がすべて未解消。

*注: RI-05が重大に残る（SRG-3: ArClの3点電子的傾向からOA律速を導出）ため、VQ-3に到達してもqualified（限定的）となる。*

---

**VQ-4 Benchmark（RI-08、RI-09 + VQ-3継承）: 未達**

VQ-3が未達のため継承原則により未達。個別評価: RI-09（SRG-2: 単一触媒との一対比較のみで「最速」を主張）、RI-08（SRG-2、SRG-4: 反復測定不在）が未解消。

---

**層別VQ非対称性:**

§1のLayered structureに対応する層別評価:

- **層1の定性的観察部分**（「化合物2がKTCカップリングを触媒する」「ArClはArBrより低活性」という順序的観察）単独では：VQ-1通過（RI-02 Non-fatalとして）。
- **層1の定量的性能部分**（特定TOF値の絶対値、dpppとの3.8%差）単独では：RI-01（GCレスポンスファクター）とU-1（TOF分母矛盾）の残存によりVQ-2未達。
- **層2（機構仮説）**: RI-03、RI-06の未解消によりVQ-3未達。

この非対称性は、「定性的な触媒活性の観察」と「機構帰属を伴う定量的優位性主張」が異なるVQ水準にあることを示す。

---

### §4 Era-Norm Annotation

**communication-era tolerated:**

- B-1（GCレスポンスファクター未検証）: 2009年のAdvanced Synthesis & Catalysis誌の触媒スコープ論文では、デカン内部標準を使用したGC変換率の定量精度に関する詳細な検証（各生成物のRF測定）は慣行的に要求されておらず、この種の省略は当時のgenre conventionの範囲内だった。
- B-2（全エントリの反復測定なし）: 17エントリのスコープ表を有する触媒論文において全エントリの反復測定を要求することは、2009年当時の論文形式では紙幅・慣行の観点から許容されていた。
- B-4（ホモカップリング量<3%の範囲が明確でない）: Table 2のcontext限定での選択性報告はfull paper形式でも許容範囲内。
- B-3（単一時点TOF）: 2009年時点では1時間変換率からのTOF算出は触媒化学論文の慣行的な一次評価法であり、許容されていた（ただし現代では不足）。

**modern-era deficient:**

- B-7 + U-1（活性化収率未定量・TOF分母矛盾）: 現代の触媒論文では、前駆体の活性化収率の定量（定量NMR、内部標準法）は基本的要件であり、論文自身が活性化不完全を認識しながらTOF計算を補正しないことは現代基準で許容不可。
- B-6 + U-2（活性化種のNi酸化状態未同定）: 現代では活性触媒種の同定（ESI-MS、EPR、XANESの少なくとも一つ）はメカニズム論文の基本要件。
- B-9 + U-4（均一系触媒の実証欠如）: 現代のNi触媒論文では水銀試験またはTEMPO阻害は標準的なチェックとして要求される。
- C-3（Pd/RhバイトアングルモデルのNiへの外挿）: 現代ではDFT計算または化学量論的実験による同型性の検証なしに、異金属間の機構モデル輸入は許容されない。

**両タグに該当:**

- B-3（単一時点TOF）: 2009年当時は慣行的に許容されていたが（communication-era tolerated）、現代基準では誘導期や速度変化を検出するための複数時点データが要求される（modern-era deficient）。本件は両タグに記載し、Era-norm依存として記録する。

---

### §5 最短補強ルート

**VQ-2 への最短ルート（第一目的関数）:**

1. EP-01a Reporting-coherence pack — 主要ビアリール生成物10種以上のデカン対比GCレスポンスファクターを独立測定・報告し、補正後のTOF値を再算出する。RI-01を解消（SRG-4前進）。
2. EP-08a Replication / uncertainty pack — 4-bromoanisole/5000、1-bromonaphthalene/50000、dppp比較エントリの3回反復測定と標準偏差の報告。RI-08を前進（SRG-2、SRG-4）。
3. EP-07a Boundary-test pack — ブロモメシチレンについて触媒量1 mol%での再試験と2,6-ジメチルブロモベンゼンとの立体効果比較。RI-07を解消（CLA-1）。

認定ゲート順注記: 実験投入順は情報利得順（EP-01aが最大情報利得）だが、最終認定はVQ-1 → VQ-2の継承順で確定する。

---

**VQ-3 への最短ルート（第二目的関数、VQ-2前提）:**

1. EP-02a Identity / purity substantiation pack — 100°Cジオキサン中の活性化後溶液に対してESI-MS・定量³¹P-NMR（内部標準）を適用し、41.8 ppm種の分子式確認と活性化収率の測定（±5%精度）。RI-02を前進（SRG-1核心）。
2. EP-03a Direct-observation / state-assignment pack — XANES（Niのエッジエネルギー）またはEPR（Ni(I)の検出）による酸化状態の直接決定。RI-03を前進（SRG-1、SRG-5）。
3. EP-04a Discrimination / replication pack — 水銀滴下試験（100°C、dioxane）とTEMPO阻害実験（主触媒条件と一致したmatched-pair）による均一系の実証。RI-04を前進（SRG-5）。
4. EP-06a Analogy-validation pack — (i) 剛直化カリクサレン類縁体Ni錯体の合成と触媒活性直接比較；(ii) Ni(II)(Ph)(Ph')(calixdiphosphine)錯体の化学量論的RE速度測定によるPd/Rhモデルの同型性検証。RI-06を前進（SRG-3）。
5. EP-09a Internal benchmark pack — dppp比較を複数基質・複数条件（ArBr/50000、立体障害基質を含む）に拡張し、dppb・dppf・DPEphosとの比較を追加。RI-09を前進（SRG-2）。

認定ゲート順注記: 実験投入順は情報利得順だが、VQ-3認定はVQ-2到達を前提としてVQ-1 → VQ-2 → VQ-3のゲート順で確定する。

---

### §6 制度設計への寄与

**1. PRI-10（Kinetic overclaim）の代表事例の確認:**

SRG-1はPRI-10（「動力学データなしに絶対的速度向上を主張」）の独立した代表事例を提供する。TOF分母の内部矛盾（論文が自ら活性化の不完全を認識しながらTOF計算を補正しない）は、PRI-10の「暫定」状態解除に向けた追加事例として記録できる。これはMonnereau 2009がPRI-10の「昇格に追加1報必要」という要件を満たす可能性を示す（Codebook v0.2a参照）。

**2. PRI-11（Mechanism-kinetics decoupling）の追加証拠:**

U-3（ArClではOAが律速と述べるがArBrのRDSを特定せず、かつ提案触媒サイクルからの速度式導出なし）はPRI-11の定義——「提案触媒サイクルから速度式を代数的に導出せずに、観測速度次数との一致のみで機構を支持」——に対応する。Breitenfeld 2014およびPengfei 2024に続く3例目として記録できる。本例の特徴：ArCl（OA律速）とArBr（RDS未特定）の「選択的な機構帰属」という形式で現れる点。

**3. RI-02とRI-03の共起パターン（§2 SRG-1）:**

SRG-1においてRI-02（活性種同定）とRI-03（未観測説明変数）が共起する。RI-02を解消（41.8 ppm種の同定）しても、触媒サイクル中間体の直接観測（RI-03）は独立した要件として残存する。この共起構造では両RIの解消が必要であり、どちらか一方の解消だけでは不十分。Codebook v0.2の「RI共起パターン」注記の具体例として記録。

**4. 標識不整合（Labeling mismatch）の確認:**

論文の動的バイトアングル帰属部分（P5 right column）には "likely to rely on" という仮説標識が存在するが、Abstract末尾では [REDACTED: verbatim source quotation; see the source paper via its DOI] として仮説標識を末尾1文に集約する形で提示されている。一方、Table 3のTOF数値と本文の比較記述（P5 left column）は事実的記述語を使用。RI-06との連動が明確であり、「仮説標識の末尾1文集約」パターンとして記録。

**5. RI-06 スコープ注記（サイクルレベル輸入）の実装確認:**

SRG-3においてRI-06は個別素反応の類推ではなく、触媒サイクル全体（Pd/Rh系のバイトアングル-RE関係をNi系に全体移植）の大規模モデル輸入に適用される。Codebook v0.2の「サイクルレベル輸入」注記を正確に実装したケースとして記録。Niのd電子数（d⁸ vs. Pd・Rh）の差が正面から議論されていない点が本例の特徴。

**6. VQ階層逆転の予兆（§5との接続）:**

§3の層別VQ非対称性と§5の最短ルートを組み合わせると、以下のVQ階層逆転が予測される：SRG-3に対応する実験（剛直類縁体合成、EP-06a）は高VQ要件（RI-06: VQ-3相当）であるにもかかわらず、著者自身が「非常に有益」と認識する研究として先行して実施される可能性がある一方、低VQ要件（RI-01のGCレスポンスファクター検証: VQ-2相当）は独立論文として出版されにくいインセンティブ構造のため充填されない可能性がある。この構造的逆転はStage 4の§E（未充填EP分析）で追跡される。
```

---

> **Tier 8 redaction notice**: This file is a redacted copy of the corresponding Tier 3 / Tier 9 output. Verbatim source-paper quotations have been replaced by `[REDACTED: see source paper §<loc>; full text retained in Tier 9 reviewer-only deposit]` markers, preserving location references and our own analytical content. Bibliographic fields (title, authors, journal, year, DOI), analytical labels (`evidence_chain:` with B-/U-/A-/C- internal IDs), short technical terms, and our own analytical text are not redacted. The redaction was applied by `scripts/redact_for_tier8.py` and, for this version, by `scripts/build_paperA_R1_public.py` with `scripts/redact_source_ngram_runs.py` (scripts of the project repository; they are not deposited).
