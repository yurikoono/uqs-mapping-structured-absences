prompt_version: stage3-v2-20260416
model_info: claude-sonnet-4-6

# 科学的知見の再認定判定票

## Murai et al. 1993（Nature, Communication）

---

### §1 Claim Architecture

**コア主張の要約：**

本論文のコア主張は、ルテニウム錯体 RuH₂(CO)(PPh₃)₃ がキレーション補助を鍵機構として芳香族ケトンのオルト位 C–H 結合を活性化し、オレフィンとのカップリングを「実用合成に要求される効率性・選択性・汎用性」をもって実現したというものである。

**Novelty柱（新規性）：** 先行する触媒的 C–H 官能化反応（ref. 11: Jordan & Taylor、ref. 12: Moore et al.）が副生成物・異性体混合・狭い基質適用範囲という限界を抱えていたのに対し、本反応は 13 種の基質組み合わせにわたって高収率（大半のランで 88〜100%）を示し、芳香族・オレフィンの両成分について「virtually 100%」の位置選択性を達成した点が新規性の核である。さらに、キレーション補助というコンセプト（「低原子価 Ru がカルボニル基に配位してオルト C–H 切断を誘導する」）を実用触媒設計の原理として提示した点が第二の Novelty 柱を構成する。

**Utility柱（実用性）：** 「実用的有機合成に要求される効率・選択性・汎用性」という明示的宣言のもと、原子効率的な C–H 官能化の実用化への道筋を示す。アシルベンゼン類とアシル複素芳香族に加え、単置換・二置換末端オレフィンの双方に適用可能であることが示されており、将来的に「分子変換分野に多くの機会を開く」と展望される。

**Layered structure の判定：独立層構造（あり）**

主張は以下の三つの独立層として構成されており、一層の反証が他層を必ずしも崩さない：

- **層 I（実験的収率データ層）：** 13 run にわたる GC 収率・孤立収率の実測値。これはキレーション補助のメカニズムとは独立して存在し、仮に機構が修正されても実測収率データは残る。
- **層 II（位置選択性・基質適用範囲層）：** 芳香族・オレフィン双方で「virtually 100%」の位置選択性と、アシルベンゼン〜アシル複素芳香族への広い適用範囲。これもメカニズムから独立した実験的主張を構成する。
- **層 III（機構概念層）：** キレーション補助によるシクロメタル化中間体を鍵とする触媒サイクルの提案。Fig. 1 に描写された中間体は「postulated」（提案）であり、A-1 の明示的宣言（「機構はまだ不明」）が層 III を実験的主張から切り離す。層 III の修正・棄却は層 I・II を直接には崩さない。

ただし、論文の中心的な**設計原理の主張**（「キレーション補助が成功の鍵」）は層 III に属し、これが反証されると「なぜこの反応がうまくいくか」という説明が失われる。層 I・II が残っても、論文が提供する「設計論理」の価値は著しく損なわれる。層 I・II は「何が起きるか」を、層 III は「なぜ起きるか」を担い、後者への答えは層 I・II と循環的に依存している（U-1: critical; U-2: high）。

---

### §2 SRG / CLA → RI / ER / EP Crosswalk

#### Stage 1 Turn 4 のSRG取得

Stage 1 Turn 4 の same_root_groups:
- SRG-1: B-1, B-2, B-3, B-4（定量的証拠基盤の不在）
- SRG-2: A-1, U-1, U-2（触媒サイクル証拠の不在）
- SRG-3: B-8, B-9, B-10, U-4（選択性根拠の不在）
- SRG-4: B-5, U-3, B-7（スコープ主張がデータを超える）
- SRG-5: C-1, B-2（先行研究との定量比較の不在）

#### CLA候補の同定

D-4 候補のうち、いずれのSRGにも属さないものを確認する：

D-4-3（実用合成への外挿可能性）は grounded_in: B-6, B-2, B-7。B-2 は SRG-1 および SRG-5 のメンバー、B-7 は SRG-4 のメンバーだが、B-6（run 5・6 の 6 mol% 高触媒ローディング）はいずれの SRG にも含まれていない。D-4-3 は「高温・特殊条件と実用性宣言のギャップ」という独立した主張軸を扱うため、**CLA-1** として記録する。

D-4-8（触媒サイクル参照類似体の機構的妥当性）は grounded_in: B-11, C-2, C-5。C-2 は SRG-2 に含まれるが、B-11 と C-5 の「異なる酸化状態・金属のモデル輸入」という固有の問題軸は、SRG-2 の「直接観測なし」とは原因が異なる（RI コードとして RI-06 が対応）。しかし B-11 は SRG-2 と密接に連動しており、独立 CLA とするよりも SRG-2 の Secondary RI として扱うのが適切と判断する（下記 SRG-2 の注記に統合）。

**CLA-1：実用条件外挿の未検証（Practical condition gap）**

* **Primary RI**: RI-07 Unsupported boundary
* **Secondary RI**: RI-08 Unquantified reliability
* **ER**: 「実用的有機合成に要求される」という境界主張は、論文内で達成されたとする条件（135℃還流、特定触媒ローディング）と実用合成の標準条件を比較するデータを要求する。
* **EP**: EP-07a Boundary-test pack; EP-08a Replication / uncertainty pack
* **Case-specific実装**: run 5・6（触媒 6 mol%、標準の 3 倍）の高ローディング選択根拠の明示、および「実用条件」として認定できる温度・触媒量・反応時間の下限値定義。run 4（オートクレーブ、6 kg cm⁻²エチレン加圧）の条件と実用実験室条件との比較。
* **注記**: B-6（run 5・6 高ローディング無説明）、B-2（TOF 数値なし）が直接アンカー。SRG 外の独立クラスタ。D-4-3 の展開。

---

#### SRG ごとの RI / ER / EP マッピング

---

**SRG-1 [定量的証拠基盤の不在]**（B-1, B-2, B-3, B-4）

* **Primary RI**: RI-01 Reporting integrity
* **Secondary RI**: RI-09 External superiority（B-2 に対応：直接比較なしの「最高 TOF」主張）; RI-08 Unquantified reliability（B-1 に対応：GC キャリブレーションなし）
* **ER**: 触媒性能（収率・TOF・選択性）の主張は、GC 定量の方法論（内部標準・レスポンスファクター・検量線）、孤立収率の全 run への記載、および先行反応との同一基板上の直接数値比較を必要とする。
* **EP**: EP-01a Reporting-coherence pack; EP-09a Internal benchmark pack; EP-08a Replication / uncertainty pack
* **Case-specific実装**: 全 13 run について内部標準（例：ドデカン）を用いた GC 定量値と孤立収率の両方を記載。runs 1, 9, 10 の TOF 計算に必要な時間分解収率プロファイルを取得し、Jordan & Taylor (1989) および Moore et al. (1992) と同一条件換算での TOF 数値比較を実施。触媒 SAR 比較実験（Ru(CO)₂(PPh₃)₃, RuH₂(PPh₃)₄, Ru(CO)₃(PPh₃)₂）について代表基質（例：アセトフェノン + トリエトキシビニルシラン）での定量収率を記載。
* **注記**: high_convergence_low_gap（B-1: V1=high, V3=high; B-2: V1=high, V3=high; B-3: V1=V2=V3=medium convergence 3/3）。フォールバック規則(b)(c) の主要候補。RI-01 と RI-09 の共起構造：RI-01 の解消（キャリブレーション記載）だけでは TOF 優位性主張を支える数値が得られないため、RI-09 の解消（直接数値比較）を別途行う必要がある。

---

**SRG-2 [触媒サイクル証拠の不在]**（A-1, U-1, U-2）

* **Primary RI**: RI-03 Unobserved explanatory
* **Secondary RI**: RI-06 Imported model（B-11, C-2 に対応：Mn(I)/Ru(II) ストイキオメトリック系からの触媒サイクル中間体の類推輸入）; RI-04 Unreplicated discriminator（U-1 に対応：中間体の構造的実在を示す直接観測なし）
* **ER**: 提案された触媒サイクルの中心中間体（シクロメタル化 Ru 錯体）は、ストイキオメトリック条件での孤立または³¹P NMR による観測、あるいはトラッピング実験による同定が求められる。さらに前触媒 Ru(II)→活性種 Ru(0) の変換に関する直接実験的証拠が要求される。
* **EP**: EP-03a Direct-observation / state-assignment pack; EP-06a Analogy-validation pack; EP-04a Discrimination / replication pack
* **Case-specific実装**: （RI-03）ストイキオメトリック量の RuH₂(CO)(PPh₃)₃ + アセトフェノンを用いた低温での反応を行い、シクロメタル化中間体を³¹P{¹H} NMR または X 線結晶解析で観測・同定する。（RI-06）Knobler 1975（CH₃Mn(CO)₅, Mn(I)）および McGuiggan 1982（RuCl(OC(O)CH₃)(CO)(PPh₃)₃, Ru(II) カルボキシラート）の生成物を合成し、本論文の提案中間体と同一性を構造的に比較する；また Ru(0) 源（例：Ru₃(CO)₁₂ + PPh₃ 還元条件）を用いた対照実験でRu(0)が活性種であることを確認する。（RI-04）重水素化アセトフェノン（ortho-d₁）を用いた KIE 実験で C–H 切断が速度決定段階かどうかを判定する。
* **注記**: low_convergence_high_gap（V2 単独 critical、A-1 系列）からの昇格。U-1（critical）とU-2（high）が self-contradictory absence として記録済み。RI-03 と RI-06 の共起：refs 14/15 の類推輸入（RI-06）は、中間体が直接観測されていないこと（RI-03）の補填として機能しているが、両方の解消が独立して必要（RI-06 の類推を適切化しても RI-03 は残る）。「Labeling mismatch」の典型：Fig. 1 が提案中間体を確立した構造式として描写しており、本文の "gives the cyclometallated intermediate shown in Fig. 1" という叙述語が事実的記述語として使用されているにもかかわらず、直後に「[REDACTED: verbatim source text; see the source paper via its DOI]」という仮説標識が置かれている。A-1 は仮説標識として機能するが、Fig. 1 の描写が視覚的に事実標識として機能する矛盾。

---

**SRG-3 [選択性根拠の不在]**（B-8, B-9, B-10, U-4）

* **Primary RI**: RI-05 Qualitative overread
* **Secondary RI**: RI-07 Unsupported boundary（B-9：1-インダノンの「全く反応しない」という境界主張、検出下限なし）; RI-04 Unreplicated discriminator（B-10, U-4：位置異性体の不存在が確認されていない）
* **ER**: 反応速度の差（run 10 vs. 11）を ring strain に帰属するには速度定数または活性化パラメータの測定が、「virtually 100%」選択性の主張には非観察位置異性体についての GC/NMR 検出下限の明示が要求される。
* **EP**: EP-05a Quantitative-ranking substantiation pack; EP-07a Boundary-test pack; EP-04a Discrimination / replication pack
* **Case-specific実装**: （RI-05）run 10（テトラロン / 6員環ケトン）と run 11（4-クロマノン / 5員環ケトン相当）を含む系列について、定義された温度での初速度測定と Eyring プロットを実施し、ΔΔG‡を ring strain 由来の DFT 計算値と比較する。1-インダノン（「反応しない」）について、標準条件での転化率の GC 検出下限（例：<0.5%）を明示して測定を実施（RI-07）。芳香族 ortho 選択性について、para および meta 位置異性体を標準品として合成し、GC での定量下限（例：<0.1%）を設定して非存在を確認（RI-04、B-10、U-4）。
* **注記**: high_convergence_low_gap（B-8: V1=medium, V2=high; B-9: V1=medium, V2=high; 各 convergence 2/3）。RI-05 と RI-07 の共起：ring strain 帰属（RI-05: 速度論データなしの定性的因果推論）と 1-インダノン負の境界主張（RI-07: 境界の実験的確認なし）は同一の機構主張の両面を構成しており、RI-05 の解消（速度論的測定）が同時に RI-07 の解消にも貢献しうるが、B-10/U-4 の位置異性体確認（RI-04）は独立した実験が必要。

---

**SRG-4 [スコープ主張がデータを超える]**（B-5, U-3, B-7）

* **Primary RI**: RI-07 Unsupported boundary
* **Secondary RI**: RI-01 Reporting integrity（B-7：オレフィン消費の質量収支未確認）
* **ER**: 「a variety of aromatic systems」という抽象スコープ宣言は、ケトン以外の directing group（アルデヒド、エステル、アミド、イミン）での基質試験結果、または明示的な適用範囲の制限（「芳香族ケトンに限定」）が要求される。
* **EP**: EP-07a Boundary-test pack; EP-01a Reporting-coherence pack
* **Case-specific実装**: アセトフェノン基質系で達成した 100% 収率の条件を、ベンズアルデヒド、エチルベンゾアート、ベンズアミド、アセトフェノンのイミン誘導体に適用して反応性を定量的に比較し、ketone directing group の特殊性を実験的に確定する。また runs 1–13 全体について、GC によるオレフィン消費率とオレフィン由来副生成物（異性化体、二量化体など）の検出・定量を実施してオレフィン側の質量収支を閉じる。
* **注記**: U-3（high severity, self-contradictory absence）が中心。B-5（mixed: intentional_narrowing + scope overstating）が補助アンカー。B-7 の「both starting materials に基づく定量的収率」主張は RI-01 の観点でオレフィン消費の報告を要求するが、RI-07（スコープ境界）の解消が D-1 の主要主張に直接関わるためこちらを Primary とした。

---

**SRG-5 [先行研究との定量比較の不在]**（C-1, B-2）

* **Primary RI**: RI-09 External superiority
* **Secondary RI**: RI-08 Unquantified reliability（B-2 からの継承）
* **ER**: 「these latter two cases were exceptionally high」と認めながら本反応が superior であると主張するには、ref. 11（Jordan & Taylor）および ref. 12（Moore et al.）と同一換算基準（mol 生成物 / mol Ru / 時間）での TOF 数値比較、または直接対照実験が要求される。
* **EP**: EP-09a Internal benchmark pack; EP-05a Quantitative-ranking substantiation pack
* **Case-specific実装**: Jordan & Taylor (1989) の α-ピコリン/プロペン系（Zr 触媒）および Moore et al. (1992) の ピリジン/CO/1-ヘキセン系（Ru 触媒）それぞれの最高 TOF 値を原論文から抽出し、本論文 runs 1, 9, 10 の TOF（時間分解収率プロファイルから算出）と mol/mol/h 単位で比較する表を作成する。直接対照（同一基質で先行触媒と本触媒を並走させる実験）が不可能な場合はその理由と代替措置を明示する。
* **注記**: C-1（B-2 とのリンク：TOF 主張が数値なし ↔ 先行研究との定量比較なし）。convergence: B-2（V1=high, V3=high）。SRG-1 と一部重複（B-2 は両グループ）するが、C-1 が SRG-1 の member でないため独立 SRG として維持。RI-09 の典型事例：先行文献の数値を自論文の数値なしに「以下」と宣言するパターン。

---

### §3 現在のVQ判定

**現在判定: VQ-1 (Observation)（達成）、VQ-2 (Method)（条件付き通過、non-fatal残存）、VQ-3 (Mechanism)（未達）**

---

**VQ-1 [Observation] — 通過（非致命的留保付き）**

VQ-1 の必須解消項目は RI-02（Object identification）である。全 13 run の生成物は「standard methods」（¹H NMR、元素分析等が標準的）で同定されており、生成物の化学構造が Table 1 の構造式として提示されている。Si 含有生成物（runs 1, 2, 8–13）についても構造式が示されており、実用的に「生成物が何であるか」は確定している。RI-02 は非致命的なレベルで残存する（「standard methods」の非特定：B-4）が、13 run にわたる構造同定の主張を原理的に覆すものではない。VQ-1 は通過する。

---

**VQ-2 [Method] — 通過（non-fatal残存条件付き）**

VQ-2 の必須解消項目は RI-01 および RI-07（VQ-1 継承含む）である。

- **RI-01（Reporting integrity）**: SRG-1 の全項目（B-1: GC 定量の方法論未記載、B-2: TOF 数値未記載、B-3: SAR 比較の定量根拠なし）が残存する。GC 収率の記述は存在し定量的な数値は提示されているが、その定量の根拠（内部標準、キャリブレーション）が示されていない。この欠落は **non-fatal** と判定する：GC を用いた相対収率の比較という観点では報告数値に一定の信頼性があり、論文の基本的な「どの基質で反応が進行するか」という観察報告の有効性は損なわれない。しかし「最高 TOF」という優位性主張（B-2、SRG-5）の定量基盤としては **fatal** に近い。
- **RI-07（Unsupported boundary）**: SRG-4（U-3: 「a variety of aromatic systems」の過大宣言）と CLA-1（「実用合成に要求される」という実用条件境界の未検証）が残存する。これらも**non-fatal**と判定する：論文の主要実験データ（13 run）は method 水準の主張として有効であり、スコープ宣言の過大さが 13 run の実験的有効性を崩すものではない。

VQ-2 は non-fatal 項目が残存する条件付きで通過する。「実用合成への適用可能性」という主要 utility 主張に対してはより厳しく、VQ-2 の限界近傍に位置する。

VQ-2 は VQ-1 通過を前提として成立している。

---

**VQ-3 [Mechanism] — 未達**

VQ-3 の必須解消項目は RI-03、RI-04、RI-06（VQ-2 継承含む）である。

- **RI-03（Unobserved explanatory）**: SRG-2 全体が直接解消されていない。シクロメタル化中間体（U-1: critical）も Ru(0) 活性種（U-2: high）も直接観測・確認されておらず、触媒サイクルの中核に実験的証拠が存在しない。**Fatal**: 機構水準の主張は原理的に成立しない。
- **RI-06（Imported model）**: refs 14（Mn(I) 電子求引シクロメタル化）と 15（Ru(II) カルボキシラート条件）は、本論文が提案する Ru(0) 酸化的付加とは酸化状態・金属種・反応機構が根本的に異なる先例として引用されており、同型性の実証なしに輸入されている（B-11, C-2）。**Fatal**: 機構類推の根拠が機構的に整合していない。
- **RI-04（Unreplicated discriminator）**: 位置選択性「virtually 100%」（B-10, U-4）の主張が、非観察位置異性体の積極的探索・定量なしに提示されており、SRG-3 の ring strain 帰属（B-8, B-9）も速度定数なしの単一ランの比較に依存している。**Non-fatal**（VQ-3 水準では致命的要件の一つだが、RI-03/RI-06 が先行して Fatal であるため独立致命性は RI-03 が主）。

VQ-3 は RI-03 および RI-06 が致命的に未解消のため**未達**である。これは論文自身が A-1 で「機構はまだ不明」と宣言していることと整合する。

なお、**RI-05（Qualitative overread）**が SRG-3 に残存しており、VQ-3 (qualified) に該当する兆候があるが、VQ-3 自体が未達のため qualified 表記は留保する。

**層別VQ非対称性：**

§1 の Layered structure で同定された独立層について：

- **層 I（実験的収率データ層）単独**: VQ-2 (Method) の境界近傍まで到達している。GC 収率の reporting は RI-01 の non-fatal 残存条件下で VQ-2 を満たす水準にある。ただし TOF 優位性主張（B-2）については RI-09 の未解消により VQ-2 の境界内でも不安定。
- **層 III（機構概念層）単独**: VQ-1 のみ（実験的観察は Fig. 1 の提案中間体の構造式として存在するが、直接観測がない）。RI-03 致命的未解消により、機構層は VQ-2 にさえ到達していない。
- **論文全体**: VQ-2（non-fatal条件付き通過）、VQ-3 未達。

---

### §4 Era-Norm Annotation

**communication-era tolerated（1993年 Nature communication 形式の規範内で許容）:**

- **B-1（GC キャリブレーション・内部標準の非記載）**: 1993 年代の Nature 短報では定量的 GC データの詳細な方法論記載を求める規範が未確立であり、GC 収率の提示のみで許容された。反応のスコープを示す初報 communication では、精密な定量方法論よりも基質の多様性と収率の傾向が評価された。
- **B-4（「standard methods」による構造同定の非特定）**: 1993 年当時の Nature communication では ¹H NMR + 元素分析（または high-resolution MS）が「standard methods」として読者に暗黙的に了解されており、具体的手法の列挙は Full Paper へ委ねられていた。
- **B-3（触媒 SAR 比較の定量的根拠なし）**: 新触媒の初報 communication において代替触媒の定性的な活性分類（「equally effective」「modestly effective」「not effective」）は、全て定量数値を要求せずに許容された。
- **A-1（「機構はまだ不明」の明示的宣言）**: 機構解明を次段階の研究へ委ねつつ実験的成果の速報を行うパターンは、1993 年代の有機金属触媒 communication において広く認められていた。重要な新触媒反応の発見報告として、メカニズム解明の先送りは制度的に受容されていた。

**modern-era deficient（現代の再認定では許容できない欠落）:**

- **B-2（TOF 数値の非記載）**: 「among the highest reported」という優位性主張が TOF 数値を提示せずに行われている点は、現代の触媒化学論文では VQ-4 (Benchmark) の必須要件（RI-09: External superiority の解消）として受け入れられない。現代の触媒性能主張は mol/mol/h 単位での数値と先行文献との直接比較を要求する。
- **U-1（シクロメタル化中間体の実験的非確認）**: 論文が設計原理として提示するシクロメタル化中間体が、Fig. 1 に明示された構造式として提示されているにもかかわらず直接的な実験的証拠を持たない点は、現代の機構論文では RI-03 の致命的未解消として扱われる。
- **U-2（前触媒 Ru(II)→活性種 Ru(0) 変換の未証明）**: 触媒サイクルの開始ステップが実験的に未確認のまま議論が展開されている点は、現代では基礎的な触媒化学の要件として不可欠と見なされる。
- **B-10 / U-4（位置選択性の検出下限未記載）**: 「virtually 100%」という選択性主張が非観察位置異性体の積極的確認なしに行われている点は、現代の選択性研究では RI-04 の致命的未解消として扱われる。現代的な選択性報告では GC または NMR による位置異性体の検出下限（例：<0.1%）を明示した上での「virtually 100%」主張が要求される。

**両タグ該当（当時は許容されたが現代では不足）:**

- **B-2 / SRG-5**: TOF 最高水準の主張は 1993 年当時は定性的な比較が許容されていたが（communication-era tolerated）、現代では数値比較が必須（modern-era deficient）。両タグを記載し、「era transition で致命性が変化した項目」として記録する。
- **B-1（GC 定量基盤）**: 1993 年の format では許容されていたが（communication-era tolerated）、現代の再現性基準（RI-01）では方法論の完全記載が必須（modern-era deficient）。

---

### §5 最短補強ルート

**目的関数の設定：**
- **第一目的関数**: VQ-3 (Mechanism) への到達（現在 VQ-2 conditional から VQ-3 への昇格）
- **第二目的関数**: VQ-4 (Benchmark) への到達（VQ-3 達成後）

---

**VQ-3 への最短ルート：**

1. **EP-03a [Direct-observation / state-assignment pack]** — ストイキオメトリック量の RuH₂(CO)(PPh₃)₃ とアセトフェノンを低温で反応させ、シクロメタル化中間体を ³¹P{¹H} NMR（または X 線結晶解析）で直接観測・同定する。**RI-03（Unobserved explanatory）を前進**（SRG-2 の最大Fatal RI、U-1 critical を直接解消）。情報利得: 最大（単一実験で VQ-3 不通過の最大原因を解消）。実行可能性: 中〜高（ストイキオメトリック反応はルーティン有機金属化学の範囲内）。

2. **EP-06a [Analogy-validation pack]** — refs 14（Knobler 1975, Mn(I) 条件）および 15（McGuiggan 1982, Ru(II) カルボキシラート条件）の化合物と提案中間体の構造同一性を結晶構造データで照合し、Ru(0) 酸化的付加との機構的差異を明示的に議論する；あわせて Ru(0) 源（例：Ru₃(CO)₁₂/PPh₃ 系）による対照実験を実施する。**RI-06（Imported model）を前進**（SRG-2 の第二 Fatal RI）。情報利得: 大（RI-06 解消は EP-03a と独立して要求される）。実行可能性: 中（既存文献構造データの参照 + 対照実験）。

3. **EP-04a [Discrimination / replication pack]** — 重水素化アセトフェノン（ortho-d₁ または全芳香族重水素化）を用いた KIE 実験（k_H/k_D 測定）で C–H 切断が速度決定段階かを判定し、速度論的機構論の基盤を確立する。**RI-04（Unreplicated discriminator）を前進**（SRG-3 の ring strain 帰属根拠の強化）。情報利得: 中（VQ-3 達成に向けた RI-04 の部分解消）。実行可能性: 中（KIE 実験は有機金属化学のルーティン）。

認定ゲート順注記: 実験投入順は情報利得順（EP-03a → EP-06a → EP-04a）であるが、最終認定は VQ-1 → VQ-2 → VQ-3 → VQ-4 の継承ゲート順で確定する。VQ-3 認定には RI-03、RI-04、RI-06 の解消が必要であり、EP-03a と EP-06a の両方の完了が VQ-3 通過の前提条件となる。

---

**VQ-4 への最短ルート（VQ-3 達成後）：**

4. **EP-09a [Internal benchmark pack]** — runs 1, 9, 10 について時間分解収率プロファイル（例：30 分ごとのアリコート GC 分析）を取得して TOF（mol 生成物 / mol Ru / h）を算出し、Jordan & Taylor (1989) と Moore et al. (1992) の TOF 値と mol/mol/h 単位で直接比較する表を作成する。**RI-09（External superiority）を前進**（SRG-5 の核）。

5. **EP-08a [Replication / uncertainty pack]** — 代表的ランについて n≥3 の独立繰り返し実験を実施し、収率の平均値・標準偏差・信頼区間を記載する；全 13 run について GC 定量の内部標準・レスポンスファクターを明示する。**RI-08（Unquantified reliability）および RI-01（Reporting integrity）を前進**（SRG-1 の RI-01/RI-08 解消）。

6. **EP-07a [Boundary-test pack]** — ケトン以外の directing group（アルデヒド、エステル、アミド、イミン）での基質試験を実施して適用範囲境界を定量的に確定し、「a variety of aromatic systems」主張の根拠とするか適用範囲を明示的に制限する。**RI-07（Unsupported boundary）を前進**（SRG-4 / CLA-1 の核）。

認定ゲート順注記: VQ-4 認定には RI-08 および RI-09 の解消が必要。EP-09a（RI-09）と EP-08a（RI-08）は並行実施が可能であり、EP-07a（RI-07）は SRG-4/CLA-1 の解消として VQ-3→VQ-4 の中間段階で実施できる。

---

### §6 制度設計への寄与

**1. 既存 RI コードの新しい代表事例：**

- **RI-03（Unobserved explanatory）の代表事例として特に強い事例：** 本論文の U-1/U-2 ペア（シクロメタル化中間体 + 前触媒活性化）は、「論文自体が A-1 で『機構不明』と宣言しつつ、その機構を前提とした設計原理を中心的主張として同一論文内で展開する」という RI-03 の自己参照型事例を提供する。この「宣言的な機構留保と叙述的な機構依存の共存」は、従来の RI-03 事例（単に中間体が未確認）より構造的に複雑であり、Codebook の RI-03 解説に「機構留保宣言型（declared-but-maintained）」サブタイプとして追記する価値がある。

- **RI-06（Imported model）の「サイクルレベル輸入」事例：** B-11/C-2 が示す「Mn(I) および Ru(II) ストイキオメトリック系を Ru(0) 触媒サイクルの中間体類似体として輸入する」パターンは、RI-06 の Codebook 注記「サイクルレベル輸入」の典型事例を提供する。酸化状態が 2 段階異なる金属種の生成物を「similar products」と記述して機構的中間体の先例として用いる点は、同型性実証なしの大規模モデル輸入の明確な例として記録する。

**2. Labeling mismatch パターンの明確な事例：**

本論文は「Labeling mismatch」（仮説・限定の標識が本文叙述語と整合しないパターン）の典型事例を提供する。仮説標識（A-1: "not yet clear"）は文末の Possible mechanisms 節の冒頭一文に集約されているが、Fig. 1 の視覚的描写（確立された構造式で中間体を示す）と本文の "gives the cyclometallated intermediate shown in Fig. 1"（事実的叙述語）が組み合わさることで、読者に対して視覚的・叙述的に「確立された機構」として提示する効果が生まれている。この「テキスト仮説標識 + 図版事実標識」の分裂は RI-06 の Labeling mismatch 記録として §6 に追記する。プロンプト指定の「仮説標識の位置（末尾1文に集約等）」の記録として: 本論文では仮説標識は Possible mechanisms 節の**冒頭一文**に集約されており、その後の叙述がすべて事実的語法で展開されている（末尾集約ではなく冒頭集約後の事実語法展開という変形パターン）。

**3. 通信→Full Paper 遷移の自動解消パターン：**

B-1（GC キャリブレーション）、B-3（SAR 定量）、B-4（「standard methods」の非特定）は、Full Paper 展開（Kakiuchi et al. が後続で発表した詳細論文）において自動解消が期待される典型パターンである。これらは §4 の communication-era tolerated 項目と整合する。一方、A-1（機構宣言）と U-1/U-2（中間体・活性種の非確認）は、Full Paper 化による自動解消ではなく、独立した機構解明研究（KIE、中間体トラッピング、DFT 計算）を要求する。この「Full Paper 遷移で自動解消されるもの vs. 独立研究を要するもの」の区別は、RI の重みを評価する上で有用な軸として記録する。

**4. RI-09（External superiority）の Era-norm 依存性：**

B-2/SRG-5（TOF 最高水準主張）が §4 で「両タグ該当」として記録された点は、RI-09 の致命性が era-norm に依存することの典型事例を提供する。1993 年には定性的優位性宣言が許容されたが、現代ではRI-09 は VQ-4 の致命的要件として扱われる。Codebook の RI-09 解説に「era-norm 依存性の主要事例」として Murai 1993 を参照事例に追加することを提案する。

**5. 新規 PRI 候補の検出：なし**

本ケースで検出されたパターンは、既存 RI-01/RI-03/RI-04/RI-05/RI-06/RI-07/RI-08/RI-09 の適用範囲内に収まる。PRI-10（Kinetic overclaim）は SRG-3 の B-8/B-9 に部分的に対応するが、本論文は「速度論データなしに絶対的速度向上を主張」というよりも「速度論データなしに速度差を構造的因子に帰属する」という RI-05 Qualitative overread に近い。PRI-10 の暫定コード適用を検討したが、一致度は中程度であり、追加事例での確認を待つことが適切と判断する。

**6. VQ 判定境界条件の新知見：**

本論文の「層 I 収率データ層（VQ-2）と層 III 機構概念層（VQ-1 以下）の大きな VQ 非対称性」は、Layered structure を持つ論文における VQ 判定の境界条件として有用な知見を提供する。単一の VQ 水準を論文全体に適用する際に「どの層の VQ 水準を代表させるか」という問いが生じる。本論文では論文全体の VQ = VQ-2（conditional）としつつ、層別非対称性を §3 に明記する扱いが適切であった。この「層別 VQ 非対称性の記録形式」を VQ 判定手順の標準として確認した。

本ケースは既存の制度設計を複数の観点から追加確認し、RI-03 の「機構留保宣言型」サブタイプ、Labeling mismatch の「冒頭集約後事実語法展開」変形パターン、および RI-09 の era-norm 依存性という三点で制度設計への具体的な寄与を提供した。
