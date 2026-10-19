prompt_version: stage3-v2-20260416
model_info: claude-sonnet-4-6

# 科学的知見の再認定判定票

## Tamao, Sumitani, Kumada 1972（Journal of the American Chemical Society, communication）

---

### §1 Claim Architecture

**コア主張の要約**

本論文は、Grignard試薬とビニル・アリールハライドの選択的クロスカップリングをニッケル-ホスフィン錯体（主として[NiCl₂(dpe)]）で触媒する新しい調製法を報告する。**Novelty柱**は三つである：（1）従来法（Fe/Cu系、Tamura–Kochi）で問題となっていたホモカップリングおよび不均化副生物を実質的に抑制した選択的クロスカップリングの実現、（2）β水素を含むアルキルマグネシウム試薬を含む多様なGrignard試薬への適用性、（3）安価なsp²クロリドが使用可能という実用的優位性。**Utility柱**は、従来法では困難だったm-di-n-butylbenzene等の一段階合成として具体化される。触媒サイクル（式2–4）は「working hypothesis」として提示され、三つの素反応（形式的Ni(II)/Ni(0)酸化還元サイクル）からなる均一系機構が類推的に記述される。

**Layered structureの判定**

S2のD-1が記述するとおり、論文は三層構造を持ち、各層は部分的に独立している：

- **第一層（合成実用性）**: 多様なGrignard試薬と高収率のTable I、二つの詳細実験手順。この層は機構的説明なしに成立する。
- **第二層（触媒設計原理）**: 二座ホスフィン優位、sp²選択性、溶媒効果。この層は実用層（第一層）の観察から帰納的に引き出されており、機構的検証なしに主張されている。
- **第三層（機構仮説）**: 式2–4の触媒サイクルを「working hypothesis」と明示。第三層が否定されても第一・第二層の中核は崩落しない。

**層間依存関係**：第三層の機構的詳細（素反応の実験的検証）は第二層の設計原理解釈（「cis配置が必要条件」）を根拠付けているため、完全には独立していない。すなわち第二層は第三層が正しいことを暗黙に前提する推論を含む。第一層は第二・第三層のいずれとも独立し、単一の反証で崩れない堅牢な基盤を提供している。

---

### §2 SRG / CLA → RI / ER / EP Crosswalk

**Stage 1 META same_root_groupsの取得（SRG-1〜SRG-6）：**

SRG-1: 触媒機構証拠ギャップ（members: A-2, U-1, U-2, B-12）
SRG-2: クロス/ホモカップリング選択性定量（members: B-6, U-1, C-1）
SRG-3: スコープ制限と否定的証拠（members: B-4, A-3）
SRG-4: 立体化学アウトカムと機構的基盤（members: A-1, B-11）
SRG-5: 収率データ分析的品質（members: B-2, B-7, B-9, B-11）
SRG-6: 先行研究定量比較ギャップ（members: C-1, C-2, A-4）

**CLA候補の同定（Step 2b）：**

D-4-8（「新たで有用な調製法」の実用条件外挿可能性、grounded_in: B-1, B-13, A-3）について確認する。B-1とB-13はSRG-1〜6のいずれのmember_itemsにも含まれない（SRG-3のmembersはB-4とA-3であり、B-1・B-13は別項目である）。D-4-8のA-3はSRG-3に含まれるが、grounded_inの中核であるB-1・B-13が独立である点、かつD-4-8はD-1「new and useful preparative method」という主張の成否に直結（Utility柱の検証に関わる）するため、CLAとして記録する。

---

**SRG-1 [触媒機構証拠ギャップ]**

* **Primary RI**: RI-06 [Imported model]
  式2–4の触媒サイクルは(dipy)Ni錯体を用いた化学量論的反応（refs 11–12）からの大規模なサイクルレベル輸入であり、[NiCl₂(dpe)]触媒下での実際の条件での同型性実証がない。

* **Secondary RI**: RI-03 [Unobserved explanatory]
  中間体1（ジオルガノニッケル）、2（ハロゲノオルガノニッケル）、3（新規ジオルガノ錯体）のいずれも単離・同定されておらず、速度論的拘束もない。さらにRI-04 [Unreplicated discriminator]として、「黒色混合物」（Ni⁰生成の可能性）という唯一の観察が機構的証拠として未分析のまま残されている。

* **ER**: [NiCl₂(dpe)]触媒下の実際の反応条件において、提案された素反応のうち少なくとも律速段階の中間体が直接観測または速度論的拘束によって確認され、かつ類推元（(dipy)Ni系）との同型性が定量的に実証される必要がある。また、「黒色混合物」の組成が同定され、均一系vs.不均一系の二者択一が排除される必要がある。

* **EP**: EP-06a [Analogy-validation pack]; EP-03a [Direct-observation / state-assignment pack]

* **Case-specific実装**:
  (a) EP-06a: [NiCl₂(dpe)]を基質とする化学量論的反応でジオルガノNi(II)中間体（L₂NiR₂型）を独立合成し、¹H NMR・X線結晶解析により構造確認したのちに、有機ハライドとの反応でR–Rのホモカップリング産物生成を定量する。(dipy)Ni類縁体との速度論的パラメータ比較（kobs at 25°C in Et₂O）を実施し、dpe配位子での同型性を検証する。
  (b) EP-03a: 反応中間体（黒色混合物）をX線粉末回折またはTEM-EDXで分析し、Ni⁰ナノ粒子の存在/非存在を確定する。反応途中でサンプリングを行い、[NiCl₂(dpe)]の消耗速度をICP-OESまたはUV-Visで追跡する。均一系活性種が確認された場合はESIMS等による中間体同定を試みる。

* **注記**: 下位項目A-2（最高収束: V1=high, V2=high, convergence=2/3, gap=none）、U-2（medium severity）、B-12（low）、U-1（high）が収束。SRG-1はhigh_convergence_low_gapのトップカテゴリーに位置する。RI-06にRI-06スコープ注記（サイクルレベル輸入）を適用。RI-03 + RI-04の共起（§6参照）。

---

**SRG-2 [クロス/ホモカップリング選択性定量]**

* **Primary RI**: RI-04 [Unreplicated discriminator]
  論文の中心的主張（「選択的クロスカップリング」）を支えるべき選択性の定量データ（cross:homo比）が、いずれのTable Iエントリーにも存在しない。U-1が示すとおり、論文自身の触媒サイクル（式3）がR–Rを予測するにもかかわらず、この自己矛盾的不在が未報告のまま。

* **Secondary RI**: RI-09 [External superiority]
  「ホモカップリングを生じる」先行法に対する優位性は、外部文献記述のみに依拠し、共通基質での直接数値比較がない（C-1）。

* **ER**: すべてのTable Iエントリーにおいてホモカップリング生成物（R–R）の収率または検出下限値が開示され、クロス:ホモ選択性比が定量されることが必要。さらに、少なくとも一つの代表基質においてTamura–Kochi系との並列実験が実施される必要がある。

* **EP**: EP-04a [Discrimination / replication pack]; EP-09a [Internal benchmark pack]

* **Case-specific実装**:
  (a) EP-04a: EtMgBr/PhClおよびn-BuMgBr/PhClの反応について、反応終了後の粗混合物をGC-MSで分析し、Et-Et、n-Bu-n-Bu、Ph-Phの各ホモカップリング産物の絶対収率をGC内部標準法（デカンまたはドデカン）で定量する。検出限界（0.5 mol%相当）以下であれば「不検出」として定量化する。
  (b) EP-09a: n-BuMgBr/CH₂=CHClの反応を[NiCl₂(dpe)]とFe(acac)₃（ref 5のTamura-Kochi条件）で並列実施し、n-C₅H₁₁CH=CH₂のGC収率・n-Bu-n-Buの収率を同時測定する。

* **注記**: 下位項目B-6（V2=high, V3=high, convergence=2/3, gap=none; high_convergence_low_gap）、U-1（severity=high; 自己矛盾的不在として独立記録）、C-1（affects_claims=yes）が収束。SRG-1との交差（U-1がSRG-1とSRG-2の両方に属する）。

---

**SRG-3 [スコープ制限と否定的証拠]**

* **Primary RI**: RI-07 [Unsupported boundary]
  「Only C_{sp²} halides can be used」という境界主張は、sp³ハライドとの失敗実験の報告なしに「特徴」として肯定的に提示されている（B-4: intentional_narrowing + reporting_omission）。失敗例（アルキルハライドでの0%収率、副反応生成等）なしに「のみ可能」と境界を主張する典型的RI-07パターン。

* **Secondary RI**: RI-07（否定的境界主張への拡張適用）
  「Investigations are continuing on the extension」（A-3）は将来への外置きであり、現時点では sp²-sp³境界の実験的根拠が論文内に存在しない。

* **ER**: sp³ハライド（n-BuCl、c-HexBr等の代表例）との反応試みを報告し、所見（0%収率、副反応の種類と収率、触媒失活等）を記述することが必要。

* **EP**: EP-07a [Boundary-test pack]

* **Case-specific実装**:
  EP-07a: n-BuCl、n-BuBr、シクロヘキシルクロリドを基質として[NiCl₂(dpe)]・n-BuMgBr/PhMgBrとの反応を試み（条件A: 0°〜還流、20時間）、クロスカップリング産物・ホモカップリング産物・未反応原料をGCで定量する。「sp³が使用できない」という主張の根拠となるデータ（収率、主要副反応の同定）を報告する。

* **注記**: 下位項目B-4（convergence=3/3、最高収束候補、high_convergence_low_gap）、A-3（将来外置き）。3/3エージェント収束はTable I全体で唯一の事例。「Features」として肯定的に提示された境界がRI-07として機能するパターンは§6で記録。

---

**SRG-4 [立体化学アウトカムと機構的基盤]**

* **Primary RI**: RI-04 [Unreplicated discriminator]
  cis-1,2-DCEとtrans-1,2-DCEの両者からcis-エンリッチスチルベン（80:20, 43:57）が得られるという観察が、測定手法の記述なし（B-11）で単一測定値として報告されている。43:57という比率は測定不確かさ（±5%）によって「partial retention」と「near-random」の解釈が逆転する可能性がある。

* **Secondary RI**: RI-03 [Unobserved explanatory]
  速度論的制御と熱力学的平衡のいずれがcis-エンリッチを生じさせているか（反応温度・時間・初期基質立体化学依存性）が直接観測されていない（A-1）。

* **ER**: cis:trans比の測定手法（¹H NMR積分比またはGC面積比）と測定精度を明示し、少なくとも2回の独立実験から平均値±標準偏差を報告すること。また、反応時間を変えた収率-立体化学の時間プロファイルを取得し、速度論的産物か熱力学的産物かを識別すること。

* **EP**: EP-04a [Discrimination / replication pack]; EP-08a [Replication / uncertainty pack]

* **Case-specific実装**:
  (a) EP-04a: cis- および trans-1,2-DCEとPhMgBrの反応をn=3の独立実験で実施し、¹H NMR（ビニル水素カップリング定数J = 12 Hz trans / 8 Hz cis で区別）とGC（蒸留分画後面積比）で独立測定した結果を平均±標準偏差で報告する。
  (b) EP-08a: 反応時間2 / 4 / 8 / 20時間でのスチルベンcis:trans比の時間依存性を測定し、熱力学的平衡（時間とともに一定比に収束）vs 速度論的凍結（時間変化なし）を識別する。

* **注記**: 下位項目A-1（V1=medium, V2=medium, convergence=2/3, gap=none）、B-11（V3=medium, convergence=1/3）が収束。SRG-4のD-4-4候補は「速度論vs熱力学的制御」という独立した問いの軸を持つ。

---

**SRG-5 [収率データ分析的品質]**

* **Primary RI**: RI-01 [Reporting integrity]
  Table Iの収率値は、5エントリーがglpc内部標準法（内部標準の種類・応答係数・キャリブレーション曲線不記載）、残り5エントリーが孤立収率（単一測定値）として報告されており、両者を同一列で比較できない（B-2）。製品特徴付けは「and/or」の組み合わせ（B-7）で記述され、エントリーごとにどの手法が適用されたか不明。

* **Secondary RI**: RI-08 [Unquantified reliability]
  反復実験・標準偏差が存在しないため（B-9）、98%と89%の収率差が統計的に有意かどうかを評価できない。

* **ER**: 各収率エントリーについて：（1）glpc定量か孤立収率かを明示、（2）glpc定量の場合は内部標準名・応答係数・キャリブレーション範囲を注記、（3）少なくとも代表例（m-di-n-butylbenzene、α-vinylnaphthalene）についてn≥2の反復実験を実施して標準偏差を報告することが必要。

* **EP**: EP-01a [Reporting-coherence pack]; EP-08a [Replication / uncertainty pack]

* **Case-specific実装**:
  (a) EP-01a: Table Iを改訂し、各エントリーに「yield basis（glpc/isolated）」列と「internal standard（compound name）」列を追加。glpc収率は「89 ± 3%（n=3, internal std: decane, RRF=1.02）」の形式で報告する。
  (b) EP-08a: EtMgBr/PhClの「98%」エントリーをn=3で反復実施し、PhCH=CH₂の「89%」（PhMgBr/vinyl chloride）と比較可能な測定基盤を確立する。

* **注記**: 下位項目B-2（convergence=2/3）、B-7（convergence=1/3）、B-9（convergence=1/3）、B-11（SRG-4と共有）。SRG-5はB-11を介してSRG-4と連結している。

---

**SRG-6 [先行研究定量比較ギャップ]**

* **Primary RI**: RI-09 [External superiority]
  「[REDACTED: verbatim source text; see the source paper via its DOI]」（Tamura–Kochi系の問題）という主張は定性的外部記述のみで、共通基質での並列実験による数値的優位性実証がない（C-1）。π-allylニッケル/クプラート試薬を「excellent reagents」と認めた後に数値比較なく除外（C-2）。Corriu–Masse（Ni(acac)₂）との比較（A-4）も皆無。

* **Secondary RI**: RI-05 [Qualitative overread]
  定性的な先行法の評価から「our method is superior」という実質的な含意を導出しており、定量的な根拠なしに順位付けを行っている。

* **ER**: 少なくとも一つの共通基質について本法とTamura–Kochi系（Fe(acac)₃またはCuX触媒）の並列反応を実施し、クロスカップリング収率・ホモカップリング収率・反応時間を同条件下で比較する数値データを提供すること。

* **EP**: EP-09a [Internal benchmark pack]

* **Case-specific実装**:
  EP-09a: n-BuMgBr + PhClを共通基質として、[NiCl₂(dpe)]（本法条件A）、FeCl₂（Tamura–Kochi条件）、CuBr（Tamura–Kochi条件）の三条件を並列実施し、n-BuPhの収率とn-Bu-n-Bu・Ph-Phの収率をGC内部標準法で定量し同一表に掲載する。

* **注記**: 下位項目C-1（affects_claims=yes）、C-2（symmetric_pattern=partial）、A-4（forgotten deferral）。SRG-6はhigh_convergence_low_gap外（SRG内A/C項目のみで重要性を判定）。RI-05が重大に残るためVQ-3 qualificationに影響（§3参照）。

---

**SRG外：CLA**

**CLA: 「新たで有用な調製法」の実用条件外挿可能性**

* **Primary RI**: RI-01 [Reporting integrity]
  触媒量（mol%）の最低有効値とTONが報告されていない（B-1）。「conditions are not necessarily optimum」という自己制限的留保が付された状態で「useful preparative method」を主張しており、報告収率が最低保証値かどうか不明。Ph₂C=CH₂生成（B-13）では「20時間還流」が「反応を確実にするため」と記述されるが、一般条件との比較がない。

* **Secondary RI**: RI-08 [Unquantified reliability]
  触媒量・反応時間・スケールのパラメトリックデータがなく、実用性の信頼範囲が不定。

* **ER**: 代表基質について触媒量（0.1–2 mol%）のスクリーニングデータと対応するTONを報告し、「optimum」に近い条件と「minimum viable」条件の両方を開示することが必要。

* **EP**: EP-01a [Reporting-coherence pack]; EP-08a [Replication / uncertainty pack]

* **Case-specific実装**:
  EP-01a: n-BuMgBr/PhClのクロスカップリングについて[NiCl₂(dpe)]の触媒量を0.1 / 0.5 / 1.0 / 2.0 mol%で変化させ（反応時間20時間、条件A）、n-BuPhのGC収率を内部標準法で定量してTON（= mol product / mol Ni）と収率の関係を報告する。PhMgBr/Cl₂C=CH₂（20時間還流必要例）と標準例（EtMgBr/PhCl、短時間完結）の反応時間コントラストを数値で明示する。

* **注記**: grounded_in B-1（convergence=2/3, gap=low）、B-13（convergence=1/3）、A-3（SRG-3 member）。D-1のUtility柱（「useful preparative method」）に直結するため CLAに分類（B-1・B-13がいずれのSRGのmember_itemsにも含まれない）。

---

### §3 現在のVQ判定

**現在判定: VQ-2 (Method)（限定的 / Qualified）**

---

**VQ-1 [Observation]**: 通る（Non-fatal残存あり）

VQ-1の必須解消項目はRI-02（Object identification）である。本論文では二つの詳細実験手順とTable Iにおける複数の物性定数（bp、屈折率）が報告されており、製品同定は最低限の水準を満たす。ただしB-7（「and/or」特徴付け）とB-8（「pure」の定量根拠なし）が残存しており、いくつかのエントリーでは単一の手法（glpc保持時間のみ）による同定の可能性がある。これはNon-fatalと判定する——物性定数と文献値の一致（bp、n²⁰D）は代替構造の大半を排除しており、VQ-1の成立を根底から覆さないため。

**VQ-2 [Method]**: 限定的に通る（Qualified）、RI-01, RI-07が部分的残存

VQ-2はRI-01（Reporting integrity）とRI-07（Unsupported boundary）の解消を要求する。

- **RI-01**（SRG-5, CLA）: 収率報告の混在（glpc vs. 孤立）と内部標準の非開示は、エントリー間横比較を原理的に阻害するため、「Method」水準の完全通過には障害となる。ただしSRG-5のRI-01は全体のVQ-2を「原理的に不成立」にするほど致命的ではなく、主たる合成的主張（複数の新規基質組み合わせでの高収率）は引き続き成立する。Non-fatal判定。
- **RI-07**（SRG-3）: 「Only sp² halides can be used」というスコープ境界主張は失敗実験なしに提示されており、これはMethod水準のEra-norm依存の致命性問題である（§4参照）。現代基準ではFatalだが、1972年の通信論文フォーマットにおいてはcommunication-era toleratedとして許容される。

**VQ-2は条件付きで通ると判定する：RI-01のNon-fatal残存とRI-07のEra-norm依存致命性（当時は許容）を前提とする。**

**VQ-3 [Mechanism]**: 未達

VQ-3の必須解消項目はRI-03（Unobserved explanatory）、RI-04（Unreplicated discriminator）、RI-06（Imported model）であり、いずれも本論文では未解消。

- RI-06（SRG-1、Primary）: 触媒サイクルは(dipy)Ni化学量論系からの大規模輸入であり、[NiCl₂(dpe)]系での同型性実証がない。Fatal。
- RI-03（SRG-1、Secondary）: 中間体1・2・3のいずれも直接観測されていない。Fatal。
- RI-04（SRG-2、SRG-4）: ホモカップリング産物の未定量（式3の予測値の検証なし）と立体化学比の単一測定値（手法不明）が残存。Fatal。
- RI-05（SRG-6、Secondary）: 定性的序列から触媒設計原理を導出（D-4-7）。VQ-3 qualificationをさらに強化する方向に作用するが、致命性の主体はRI-06。

**VQ-3未達：RI-06（Fatal）、RI-03（Fatal）、RI-04（Fatal）が未解消。SRG-1の触媒機構証拠ギャップ全体がVQ-3の壁を形成している。**

**VQ-4 [Benchmark]**: 未達

VQ-3が未達のため継承原則によりVQ-4も未達。個別にRI-08（SRG-5、CLA）とRI-09（SRG-2、SRG-6）も未解消であり、VQ-3通過後もVQ-4には追加投入が必要。

---

**層別VQ非対称性：**

ただし**第一層（合成実用性）**単独では：Table I全体の収率データと二つの実験手順を根拠として、複数のGrignard・ハライド組み合わせでの高収率クロスカップリングという「操作的主張」はVQ-2相当の水準（Method）に到達している。第一層は機構的検証（VQ-3要件）を必要とせず、独立して成立する。

ただし**第三層（機構仮説）**単独では：VQ-2にすら到達しておらず、「working hypothesis」の文字通りの性格（観察レベルの示唆）に相当する。

---

### §4 Era-Norm Annotation

**communication-era tolerated（1972年JACS communication形式内で許容される欠落）:**

- **B-1（TON・最低有効触媒量の非開示）**: 1972年の合成通信論文では触媒量の定量的最適化データの掲載は必須でなく、「catalytic amount」の実証だけで掲載要件を満たした（D-3 journal_constraintによる根拠）。
- **B-7（「and/or」製品特徴付け）**: 通信論文の字数制限（3ページ）のもとで、各生成物への手法特定は慣習的に省略されており、文献bp・屈折率との一致による同定が標準的実践であった。
- **B-8（「pure」の定量的根拠なし）**: GC純度%またはNMR純度の明示は1970年代初頭の合成化学報告において必須でなく、物性定数の文献一致が「純粋」の証拠として受け入れられていた。
- **B-9（反復実験・標準偏差の欠如）**: 合成通信論文において単一測定収率の報告は当時の標準的記述形式であり、統計的有意差の評価は要求されていなかった。
- **B-10（Grignard試薬濃度の滴定根拠なし）**: 1972年の合成化学実験報告において、Grignard試薬の滴定確認の開示は慣習的に省略されていた。
- **B-13（基質依存的強制反応条件の説明なし）**: 通信論文の長さ制限内でのkinetic rationaleの省略は許容範囲内。
- **RI-07（sp²境界主張の失敗例なし / B-4）**: 1972年の合成通信論文では、スコープの「特徴」として境界を記述する際に対照失敗実験を明示的に報告する規範が確立されていなかった。この項目は§3のEra-norm依存致命性判定とも整合する。

**modern-era deficient（現代の再認定では許容できない欠落）:**

- **B-6（ホモカップリング産物の完全未報告）**: 論文の中心的主張「選択的クロスカップリング」の定量的根拠として、cross:homo比の報告は現代の触媒化学論文では必須であり、単一の「selectivity」数値なしにタイトルの選択性主張を行うことは2020年代の再認定では受け入れられない。VQ-3未達の主因の一つ（SRG-2）。
- **A-2（触媒サイクルの実験的根拠の完全欠如）**: 現代の触媒化学論文では、提案機構の少なくとも一つの中間体を分光学的・反応化学的に特徴付けることが標準的要件であり、「類推のみ」の機構提案はVQ-3未達として再認定できない（SRG-1）。
- **U-1（機構が予測する副産物の自己矛盾的不在）**: 論文自身のモデルが予測するR–Rの未報告は、現代基準ではデータの完全性の重大な欠陥として分類される。Era-normとしても本来許容外——1972年でも論文内で式3を書いておきながらR–Rの定量をしないことは、フォーマット制約（3ページ）で完全には説明できない内容的省略である（D-2 format_exploitationで指摘されている点）。
- **B-11（cis:trans比の測定手法未記載）**: 現代の分析化学基準では、立体異性体比の報告においては測定手法（NMR J-value, GC分離条件）を明示することが必須であり、単一の比率値のみの記述では再認定できない（SRG-4, RI-04）。
- **U-2（「黒色混合物」の未分析）**: 現代のホモ均一触媒化学では、反応系の触媒の状態（均一系か不均一系か）の同定は機構的主張の検証に不可欠であり、特徴付けなしに均一系触媒サイクルを提案することは現代基準で許容されない。

**両タグに該当する項目（当時許容・現代不足）:**

- **B-4（sp²境界主張の失敗例なし）**: 1972年当時は許容されたが（communication-era tolerated）、現代の合成方法論論文では少なくとも代表的な陰性例の報告が必要（modern-era deficient）。境界主張の経験的根拠として、RI-07の適用が当時は許容されたが現代では不足。
- **B-3（配位子活性序列の数値なし）**: 当時の通信論文形式では定性的序列の提示は許容されたが（communication-era tolerated）、現代では少なくとも代表的収率数値と標準偏差の報告が必要（modern-era deficient, RI-05）。

---

### §5 最短補強ルート

**現在のVQ水準: VQ-2（Qualified）**

**第一目的関数: VQ-3（Mechanism）への到達**

VQ-3への必須解消項目：RI-06（SRG-1: 機構モデルの同型性実証）、RI-03（SRG-1: 中間体の直接観測）、RI-04（SRG-2, SRG-4: 単一データの多重検証）。

情報利得とEP投入順序：

**1. EP-03a [Direct-observation / state-assignment pack]** — [NiCl₂(dpe)]系でのジオルガノNi(II)中間体（L₂NiEt₂またはL₂Ni(Ph)(Et)型）を独立合成・¹H NMR・X線で確認し、黒色種をXRD/TEMで同定する。**RI-03を直接前進**（SRG-1中核）。最優先：均一系機構の可否を決定するゲーティング実験であり、結果によってRI-06とRI-04の後続設計が変わる。実験的実行可能性は中（合成化学設備で可能、X線は外部依頼）。

**2. EP-06a [Analogy-validation pack]** — 独立合成したL₂NiEt₂をPhClと反応させ、Et-Et（ホモカップリング）とPh-Et（クロスカップリング）の比率をGC定量し、(dipy)Ni系（ref 11）との速度論的パラメータを比較して（dipy)→(dpe)の同型性を検証する。**RI-06を前進**（SRG-1）。EP-03a実施後に実行可能（中間体確認が前提）。

**3. EP-04a [Discrimination / replication pack]** — Table I全エントリーにおけるホモカップリング産物（R–R）をGC-MSで定量し（EP-04aのSRG-2実装）、かつcis:trans比をNMR n=3で再測定する（EP-04aのSRG-4実装）。**RI-04を前進**（SRG-2, SRG-4同時前進）。EP-03aと並行実施可能（独立実験）。情報利得が2 SRGに波及するため優先度は高い。

VQ-3到達のための最小構成：EP-03a + EP-06a + EP-04a（上記1–3の完了）。EP-03aが不成立（均一系否定）の場合は、代替機構（Ni⁰不均一系またはNi(I)/Ni(III)ラジカルサイクル）の設計に転換する必要があり、EP-06aの設計が変更される。

---

**第二目的関数: VQ-4（Benchmark）への到達**（VQ-3通過が前提）

VQ-4への追加必須解消項目：RI-08（SRG-5, CLA: 反復測定・不確かさ記述）、RI-09（SRG-2, SRG-6: 直接比較なしの外部優位性主張）。

**4. EP-08a [Replication / uncertainty pack]** — Table Iの全収率をn≥2の独立実験で再測定し、平均値±標準偏差（またはglpcの場合は±%相対標準偏差）を報告する。cis:trans比も反応時間依存性（2/4/8/20時間）とともにn=3で測定する。**RI-08を前進**（SRG-5, CLA, SRG-4の残余部分）。EP-03a/06a/04aと並行実施可能（独立実験）。

**5. EP-09a [Internal benchmark pack]** — 代表基質（n-BuMgBr + PhCl）でFe(acac)₃（Tamura–Kochi条件）と並列実験を実施し、クロス収率・ホモ収率を同条件下で比較する。Corriu–Masse（Ni(acac)₂）との比較もNi(acac)₂条件を実施して追記する。**RI-09を前進**（SRG-2, SRG-6同時前進）。

**認定ゲート順注記:** EP投入の実験実施順は情報利得順（上記1→3, 4–5並行）で設計されているが、VQの最終認定はVQ-1 → VQ-2 → VQ-3 → VQ-4の継承ゲート順で確定する。EP-04a（RI-04前進）がVQ-3の認定に先行して実施される場合でも、RI-06（SRG-1）とRI-03（SRG-1）が未解消の間はVQ-3は認定されない。

---

**EP投入の優先順位まとめ（Top-3）:**

| 順位 | EP | 対象RI | 対象SRG | 理由 |
|:-----|:---|:-------|:--------|:-----|
| 1 | **EP-03a** | RI-03 | SRG-1 | ゲーティング実験：均一系か不均一系かの決定がすべての後続設計を変える |
| 2 | **EP-04a** | RI-04 | SRG-2, SRG-4（2 SRG同時前進） | 論文の中心的「選択性」主張の定量と立体化学測定の検証を一括 |
| 3 | **EP-06a** | RI-06 | SRG-1 | (dipy)→(dpe)同型性の検証：EP-03a完了後に実施可能であり、VQ-3必須 |

---

### §6 制度設計への寄与

**1. RI-06スコープ注記（サイクルレベル輸入）の具体事例として記録**

本論文のSRG-1は、個別素反応ではなく触媒サイクル全体（式2–4の三ステップ連鎖）を別系（(dipy)Ni化学量論）から輸入する大規模モデル輸入の典型事例である。Codebook v0.2aのRI-06スコープ注記「サイクルレベル輸入」の最初期の代表事例として記録する。本ケースでは輸入元と輸入先の違いは（1）配位子（dipy→dpe：二座性は維持、電子的・立体的特性は異なる）、（2）反応条件（化学量論→触媒量）、（3）基質（有機ハライド種類）の三点に及ぶ大規模な変更を含む。

**2. RI-03 + RI-04 + RI-06の三重共起パターンの記録**

SRG-1において、RI-06（モデル輸入）・RI-03（中間体未観測）・RI-04（単一観察の過大解釈）の三つが共起している。このパターンでは、RI-06だけを解消しても（同型性が確認できても）、RI-03とRI-04が残存する限りVQ-3は成立しない。三重共起の解消はEP-06a（RI-06）→EP-03a（RI-03）→EP-04a（RI-04）という順序依存の連鎖を要する。§6でパターン記録：「均一系触媒サイクル提案論文における RI-03 + RI-04 + RI-06 三重共起は、VQ-3 到達に 3 EP 連鎖を必要とする高コスト構造を形成する。」

**3. 標識不整合（Labeling mismatch）パターンの確認**

本論文の式2–4は「L₂NiX₂ + 2RMgX' → L₂NiR₂ + 2MgXX'」「L₂NiR₂ + R'X'' → L₂Ni(R')(X'') + R–R」等、事実的記述語（矢印の右辺に確定産物として記述）を使用している。一方で末尾の結言（「the working hypothesis described above」）に限定標識が集約されている。Codebook v0.2aで定義するラベリング不整合（機構仮説に対して事実的記述語を使用し、限定標識を末尾1文に集約）の典型事例として記録する。RI-06と強く連動するパターン。

**4. 通信→Full Paper遷移の自動解消パターン（部分的）**

SRG-5（RI-01, B-2/B-7/B-9）とCLAのRI-01（B-1, B-13）は、通信論文の3ページ制限に起因する省略であり、Full Paper展開においてはAppendix/Supporting Informationへの移行で自動的に解消可能である。RI-07（SRG-3、B-4）も追加実験で解消できるが、実験追加が必要なため「自動解消」ではなく「構造的解消」として区別する。一方、A-2（触媒サイクルの実験的根拠欠如）とB-6（ホモカップリング産物未報告）はフォーマット制約を超えた内容的省略であり、Full Paper展開では自動解消されない。両者の区別を§4と合わせて記録する。

**5. 「否定的特徴提示」型RI-07の初出事例として記録**

SRG-3のRI-07は、「Only sp² halides can be used」という境界を「最も顕著な特徴の一つ」（Feature 2）として肯定的に提示しながら、失敗実験データなしに境界を主張するパターンである。Codebook v0.2aのRI-07拡張適用（「〜のみ有効」という肯定的境界主張への適用）の具体的事例として記録する。このパターンは後続の類似論文（scope-as-feature型の合成触媒論文）で繰り返し現れる可能性があり、PRI候補の予備観察として登録する（独立2報での確認前のため、PRI番号は付与しない）。

**6. 自己矛盾的不在（U-1）のCLA自動変換ルールの適用確認**

Stage 1のU-1（「式3がR–Rを予測するが報告なし」）は、SRG-1とSRG-2の両方のmemberとして記録されており、本来CLAとして独立記録する候補であったが、U-1のgrounded_inであるV2-Q6/V3-OV3がSRG-2のmember B-6に包含されているため、CLA変換よりもSRG-2の注記でより強力に取り扱われた。§2 Step 2bの「自己矛盾的不在のCLAチェック」と「既存SRGに含まれる場合はCLAとして記録しない」というルールの整合性を確認した。本ケースでは当該ルールが正しく機能しており、制度設計の既存ロジックを追加確認した。

**7. PRI-12候補の提案（暫定）**

本論文のD-4-2（ホモカップリング産物の自己矛盾的不在）は、「論文が提示するモデルが予測する観測量を、論文が自身の実験データで検証しない」パターンの代表事例である。これはRI-04（単一データへの過大解釈）の一形態として位置づけられるが、「モデル自身が予測する副産物・中間体・速度論量が、同一論文内の実験データの不在として記録される」という構造は、RI-04よりも特定的なパターンを示す。本ケース単独ではPRI昇格基準（独立2報）を満たさないため、「PRI-12候補: Model-predicted absence（モデル予測量の自己矛盾的不在）」として暫定登録する。次報での確認を推奨。
