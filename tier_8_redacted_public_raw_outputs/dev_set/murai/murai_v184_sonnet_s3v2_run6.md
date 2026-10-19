prompt_version: stage3-v2-20260416
model_info: claude-sonnet-4-6

# 科学的知見の再認定判定票

## Murai et al. 1993（Nature, Articles）

---

### §1 Claim Architecture

**コア主張の要約**

本論文は、RuH₂(CO)(PPh₃)₃を触媒として芳香族ケトン類のortho C–H結合とオレフィンとがC–C結合を形成するカップリング反応を、触媒的条件で達成したことを報告する。Novelty柱は「触媒的C–H/オレフィンカップリングの実証（13 runs, GC収率最大定量的）」であり、Utility柱は「効率性・選択性・汎用性の三条件が実用的有機合成レベルで一体的に達成されている」という点にある。成功の鍵として「キレーション補助（chelation assistance）」が明示的に提示されており、カルボニル基がRuを ortho C–H 結合に配向させることで部位選択的な酸化的付加が可能になると提案する。論文は Fig. 1 にシクロメタル化中間体を描いて機構を提案するが、同時に「[REDACTED: verbatim source text; see the source paper via its DOI]」と自認している。

**Layered structure 判定**

Stage 2 D-1 が明示したように、本論文の主張は三層構造を持つ：

- **層1（合成的達成層）**: 高収率・高TOF の実験的観察事実。Table 1（13 runs）の GC 収率データに基づく。単一の反証で全体が崩れる構造ではなく、各 run が独立した証拠単位として機能する。
- **層2（選択性層）**: 芳香族 ortho 選択性・オレフィンの anti-Markovnikov 選択性が「virtually 100%」であるという観察。層1と部分的に独立するが、選択性の分析的根拠（検出下限）の問題は層1の収率主張とは独立して存在する。
- **層3（設計原理層）**: キレーション補助によるC–H活性化機構の提案。実験的中間体証拠を持たない仮説的層。層3が否定されても層1・2は生き残る。

層間の依存関係：層3（設計原理）が実証されれば層1・2の選択性起源が帰属可能となるが、層3の仮説性は層1・2の実験事実の信頼性を直接は損なわない。ただし層1の「性能比較（TOF最高）」主張と層3の「設計原理の一般化可能性」主張はともに証拠基盤が脆弱であり、論文の実質的な強度は層1の観察事実部分に集中する。

---

### §2 SRG / CLA → RI / ER / EP Crosswalk

**2a. SRGの取得（Stage 1 Turn 4より）**

- SRG-1 [Quantitative evidence base]: B-1, B-2, B-3, B-4
- SRG-2 [Catalytic cycle evidence absent]: A-1, U-1, U-2
- SRG-3 [Selectivity basis absent]: B-8, B-9, B-10, U-4
- SRG-4 [Scope claims exceed data]: B-5, U-3, B-7
- SRG-5 [Prior art not engaged numerically]: C-1, B-2

**2b. CLA候補の同定**

D-4候補のうちいずれかのSRGにも主として属さないものを検討する。

- D-4-6（選択性の速度論/熱力学フレームの不在）: grounded_in = B-8, A-1。B-8はSRG-3のメンバー、A-1はSRG-2のメンバー。ただしD-4-6が提起する問い——「速度論制御か熱力学制御か」——は、SRG-3（選択性根拠不在）およびSRG-2（触媒サイクル証拠不在）のいずれにも部分的に帰属されているが、「速度論/熱力学フレームという概念的次元の不在」として独立したCLAとして記録する価値がある。D-1の選択性主張（novelty柱の一要素）に直接関わる。→ **CLA-1** として記録。

- D-4-8（引用類推の機構的整合性）: grounded_in = B-11, C-2, C-5。B-11はSRGに直接列挙されていないが、SRG-2の補助的証拠として連動する。D-4-8は「Ru(0) OA サイクルに対して Mn(I) 電求型・Ru(II) カルボキシレート型を類推根拠として引用した構造的問題」であり、RI-06（輸入モデル）の典型ケースとして独立記録が有益。→ **CLA-2** として記録。

- D-4-10（具体的合成標的との接続の不在）: grounded_in = B-7, B-5。いずれもSRG-4のメンバーまたは関連項目であり、独立したCLAとはしない。SRG-4の注記内で扱う。

**自己矛盾的不在のCLAチェック：**
- U-1（シクロメタル化中間体の不在）: 触媒サイクルが予測する中間体（Fig. 1に描かれた有機金属種）が、「分光学的に観測可能であるはずだが観測未実施」の典型。SRG-2のメンバーとして記録済みだが、CLA形式でも確認する。→ SRG-2内で処理（独立CLAとしない）。
- U-2（前触媒 Ru(II) → Ru(0) 活性化機構）: 触媒サイクルが Ru(0) 活性種を必要とするが活性化過程が未提案・未観測。→ SRG-2内で処理。

Stage 2F 入力なし（単報モード）。

---

**2c. RIマッピング**

---

**SRG-1 [Quantitative evidence base]**

* **Primary RI**: RI-01 [Reporting integrity] — GCキャリブレーション条件・内部標準・応答係数の非記載と、13 runs中10 runsにおける単離収率の欠落により、横比較の測定フレームが不統一。
* **Secondary RI**: RI-09 [External superiority] — 「turnover frequencies ... among the highest reported」という優位性主張を、実際のTOF数値と文献値の並置なしに記述（refs 11/12との定量比較なし）。
* **ER**: 収率主張の信頼性には、GC定量の分析的前提（内部標準または応答係数、検量曲線）と全runs単独分の単離収率が必要であり、「最高TOF」比較主張には実測TOF絶対値と対象文献のTOF値の並置が必要。
* **EP**: EP-01a [Reporting-coherence pack]; EP-09a [Internal benchmark pack]
* **Case-specific実装**: (1) GC収率の内部標準（例：シメン、ドデカン）・応答係数、全13 runs の単離収率をSupporting Informationに記載する。(2) runs 1, 9, 10 の時間解像度データ（yield vs. time）から初速TOF（時間1/2における微分TOF）を算出し、refs 11（Jordan & Taylor, JACS 111, 778, 1989）および12（Moore et al., JACS 114, 5888, 1992）の報告TON/TOFと同一基準で数値比較する。
* **注記**: B-1（high_convergence_low_gap, V1=high, V3=high, convergence 2/3）、B-2（high_convergence_low_gap, V1=high, V3=high, convergence 2/3）、B-4（V3=high）、B-7（収率主張と関連）。SRG-5（Prior art not engaged numerically）と B-2 を共有する。

---

**SRG-2 [Catalytic cycle evidence absent]**

* **Primary RI**: RI-03 [Unobserved explanatory] — 論文の選択性の「成功の鍵」として中心的役割を担うシクロメタル化中間体（Fig. 1）が、単離・NMR観測・トラッピングのいずれによっても直接確認されていない。活性 Ru(0) 種の同定および前触媒 Ru(II) からの活性化過程も同様に未観測。
* **Secondary RI**: RI-06 [Imported model] — Mn(I)電求型（ref 14）・Ru(II)カルボキシレート型（ref 15）の化学量論的シクロメタル化を触媒的 Ru(0) OA サイクルの中間体の「類似物」として引用（後述 CLA-2 と連動）。
* **ER**: シクロメタル化中間体の存在を支持するために、化学量論的条件下での単離（元素分析 + ³¹P{¹H} NMR）またはトラッピング実験（CO 捕捉または重水素化基質を用いた速度論的同位体効果測定）が必要。前触媒活性化を支持するために、誘導期測定または RuH₂ → Ru(0) + H₂ の分光学的（IR/NMR）確認が必要。
* **EP**: EP-03a [Direct-observation / state-assignment pack]
* **Case-specific実装**: (i) RuH₂(CO)(PPh₃)₃と過剰アセトフェノンを化学量論的にトルエン中で加熱し、³¹P{¹H} NMR および IR（Ru–H 伸縮 ca. 2000 cm⁻¹）によってシクロメタル化中間体を観測する（類似系での先行例として McGuiggan & Pignolet 1982 を適用 限界付きで参照）。(ii) 重水素化アセトフェノン（ArCOCD₃ ではなく ArD/COMe など ortho-D₅ 基質）を用いた KIE 測定（kH/kD の決定）によって C–H 切断の律速段階への寄与を評価する。(iii) RuH₂(CO)(PPh₃)₃ の 135 ℃ トルエン中での分解挙動を IR によって観測し、H₂ 放出または Ru(0) 種の生成を確認する。
* **注記**: A-1（機構先送り自認）、U-1（critical: 中間体の自己矛盾的不在）、U-2（high: 前触媒活性化機構の不在）。A-1 ↔ U-1 ↔ U-2 はいずれも low_convergence_high_gap（V2 critical, 単独エージェント）と high_convergence_low_gap（U-1: V2=critical, V3=critical）の組み合わせで記録されている。

---

**SRG-3 [Selectivity basis absent]**

* **Primary RI**: RI-05 [Qualitative overread] — run 10（0.5 h, 100%）と run 11（20 h, 88%）の反応速度差をリング歪みのみに帰属（B-8）し、1-インダノンの非反応性を同じ帰属で説明（B-9）するが、活性化パラメータ・電子効果の定量化なしに速度差から構造的因果関係を導出している。
* **Secondary RI**: RI-04 [Unreplicated discriminator] — 「virtually 100%」位置選択性の主張が、非観測の3種のレジオ異性体を特定のGC/NMR感度限界で探索した結果として述べられていない（B-10, U-4）。
* **ER**: 選択性の速度論的・熱力学的起源を区別するために、速度論的同位体効果（KIE）測定または Hammett 相関（σ vs. log k）が必要。「virtually 100%」選択性主張のためには、非観測異性体のGC/NMR探索条件（感度・検出下限）の明示が必要。
* **EP**: EP-05a [Quantitative-ranking substantiation pack]; EP-04a [Discrimination / replication pack]
* **Case-specific実装**: (1) run 10（1-テトラロン）と run 11（2-テトラロン）および対照基質について、同一温度・触媒量・濃度での反応速度プロファイル（yield vs. time）を取得し、速度定数（kobs）を比較して活性化エネルギー差を推定する。(2) アセトフェノン/triethoxyvinylsilane系（run 1）の粗生成物を、非観測の3種のレジオ異性体（標準品合成または分離）を用いたGC検量で探索し、1%未満または0.1%未満の検出下限を報告する。(3) Hammett 相関実験（para-置換アセトフェノン vs. kobs）によって電子的選択性要因を定量化する。
* **注記**: B-8（high_convergence_low_gap, V1=medium, V2=high, convergence 2/3, gap low）、B-9（medium）、B-10（関連）、U-4（medium）。D-4-6（CLA-1として別途記録）と連動する。

---

**SRG-4 [Scope claims exceed data]**

* **Primary RI**: RI-07 [Unsupported boundary] — 「a variety of aromatic systems」というアブストラクトの記述（B-5/U-3）および「should be applicable more widely for selective organometallic catalysis」という一般化主張が、実際には芳香族ケトン13 examples のみのデータで支持されており、非ケトン配向基（アルデヒド、エステル、アミド、イミン）を含む「aromatic systems」への境界が実験的に確認されていない。
* **Secondary RI**: RI-01 [Reporting integrity] — 「[REDACTED: verbatim source text; see the source paper via its DOI]」（B-7）という収率主張においてオレフィンの消費・副反応（異性化・オリゴマー化）が未追跡であり、両基準での収率という測定フレームが検証されていない。
* **ER**: 「多様な芳香族系」への適用可能性を支持するために、非ケトン配向基質（アルデヒド・イミン・ピリジン型）の代表例での収率データが必要。「両基質基準の定量的収率」主張のためには、オレフィンの質量収支（反応前後のGC定量）が必要。D-4-10（具体的合成標的への適用例）もこの境界問題の目的論的側面として連動する。
* **EP**: EP-07a [Boundary-test pack]; EP-01a [Reporting-coherence pack]
* **Case-specific実装**: (1) アルデヒド（例: ベンズアルデヒド）・イミン（例: N-フェニルベンズアルデヒドイミン）・ピリジン型（例: 2-アセチルピリジン）を同一条件（135 ℃, トルエン, 2 mol% Ru）で試験し、反応性 / 非反応性の境界を実験的に定義する。(2) run 9（アセトフェノン / triethoxyvinylsilane, 0.5 h, 100%）において出発オレフィン・生成物・副生成物を含む全炭素収支を GC で定量し、「両基準での収率」を明示する。
* **注記**: B-5（mixed分類: intentional narrowing + 定義超過）、U-3（high: self-contradictory absence）、B-7（両基質基準収率の未証明）。SRG-4の目的論的側面（D-4-10: 合成標的接続の不在）はここで統合処理する。

---

**SRG-5 [Prior art not engaged numerically]**

* **Primary RI**: RI-09 [External superiority] — refs 11（Jordan & Taylor 1989）・12（Moore et al. 1992）に対する優位性（高収率・高TOF・広汎な基質一般性）が定量的数値比較なしに質的記述のみで主張されている（C-1, B-2）。
* **Secondary RI**: RI-08 [Unquantified reliability] — 先行系との比較における「among the highest reported」という序列主張に反復測定・不確かさ記述がない。
* **ER**: 「効率性・汎用性で先行系を凌駕する」という主張を支持するために、refs 11/12のTON/TOF/収率数値と本論文の実測値（runs 1, 9, 10）を同一評価基準（初速TOF: mol_product / mol_Ru / h）で並置した表が必要。
* **EP**: EP-09a [Internal benchmark pack]; EP-08a [Replication / uncertainty pack]
* **Case-specific実装**: refs 11（Zr触媒, α-ピコリン/プロペン, TON/TOF報告あり）および12（Ru触媒, ピリジン/CO/ヘキセン, TON/TOF報告あり）の数値を文献から取得し、本論文の run 1, 9, 10 の GC 時間プロファイルから算出したTOFと同一表に並置する。比較を同一基質・条件で行うことができない場合は、その旨を明記した上で可能な範囲での比較を行う。
* **注記**: B-2（high_convergence_low_gap, V1=high, V3=high, convergence 2/3）、C-1（severed: refs 11/12の定量比較が切除された）。SRG-1（B-2）と共有項目あり。

---

**SRG外：CLA**

---

**CLA-1: 選択性の速度論/熱力学フレームの不在**

* **Primary RI**: RI-03 [Unobserved explanatory] — 「easier, highly site-selective C–H bond cleavage」という選択性の記述が速度論制御か熱力学制御かという概念フレームなしに提示されており、選択性の説明機構（どの素反応段階の遷移状態エネルギー差が選択性を決定するか）が観測的に拘束されていない。
* **Secondary RI**: RI-05 [Qualitative overread] — run 10/11 比較をリング歪みによる速度差に帰属する（B-8）際に、速度論的パラメータなく速度差から構造的因果関係を推定している。
* **ER**: 選択性の起源を速度論的・熱力学的に区別するためには、同位体標識（ortho-D₅ 芳香族基質での KIE）または置換基効果（Hammett 相関）の実験的データが必要。
* **EP**: EP-03a [Direct-observation / state-assignment pack]; EP-04a [Discrimination / replication pack]
* **Case-specific実装**: ortho-D₅ 標識アセトフェノン（ArCOMe, D₅ at ortho-2H₄ positions）を用いた KIE 測定（kH/kD：³H²NMR または GC での生成物分析）によって C–H 切断段階が律速か否かを判定し、速度論制御 / 熱力学制御の区別を行う。
* **注記**: grounded_in: B-8, A-1（SRG-3とSRG-2に部分的に帰属するが、速度論/熱力学フレームの不在という概念次元は独立）。D-4-6 に対応。

---

**CLA-2: 引用類推の機構的整合性（Imported catalyst cycle model）**

* **Primary RI**: RI-06 [Imported model] — Mn(I)電求型シクロメタル化（ref 14: Knobler et al.）および Ru(II)カルボキシレート型シクロメタル化（ref 15: McGuiggan & Pignolet）を、Ru(0) 酸化的付加サイクルの中間体の「類似物」として引用しているが、機構的な差異（Mn(I) C–M electrophilic attack vs. Ru(0) oxidative addition）が論文本文で議論されていない。ref 17（Komiya & Yamamoto: アクリル酸エステルのRuへのOA）も芳香族C–H OAとは化学的に異なる過程を示す。
* **Secondary RI**: RI-03 [Unobserved explanatory] — 機構的に不整合な先行例が「類似する中間体を与える」として代替証拠として機能しており、実際の中間体の直接観測の代替として機能している。
* **ER**: 引用類推の機構的妥当性を確立するために、ref 14/15 の電求型メカニズムと提案 Ru(0) OA メカニズムの酸化状態・遷移状態の差異を明示した上で、その類推の適用限界を議論する必要がある。
* **EP**: EP-06a [Analogy-validation pack]
* **Case-specific実装**: ref 14（CH₃Mn(CO)₅ / アセトフェノン系: 電求型 C–Mn 結合形成, Mn(I)→Mn(III)）と本反応（Ru(0)→Ru(II) OA）の酸化状態変化・配位幾何の差異を表として示し、どの構造的特徴が類推として有効で、どの部分が発散するかを明示する。代替として、Ru(0) 源（例: Ru(COD)(COT) または Ru₃(CO)₁₂ の光分解）を用いた化学量論的シクロメタル化実験によって Ru(0) OA 中間体を直接同定する。
* **注記**: grounded_in: B-11（mixed分類）, C-2（symmetric_pattern: yes）, C-5（非対称引用）。D-4-8 に対応。RI-06 の「サイクルレベル輸入」サブタイプの適用事例。

---

### §3 現在のVQ判定

現在判定: **VQ-1 (Observation)**

---

**VQ-1 [Observation] は通る（Non-fatal 条件付き）**

RI-02（Object identification）の要件——生成物および触媒の構造・純度が代替候補を排除できる粒度で確定しているか——を検討する。「[REDACTED: verbatim source text; see the source paper via its DOI]」（B-4）と記述されており、1993年の Nature Articles の慣行として NMR + 元素分析または high-resolution MS が含意されている。シリル含有生成物の同定に ²⁹Si NMR や HRMS が活用されたかは記載されていないが、「unequivocally」という記述を当該時代の genre convention として額面通りに採用すれば、RI-02 は non-fatal の欠落として扱える（§4 参照）。生成物の基本的同定は達成されていると判定する。

ただし、B-3（代替触媒比較の「equally effective」「modestly effective」という記述）に対応する触媒構造の同定問題（RI-02 の境界）がある。比較実験の生成物同定が明示されておらず、同一生成物から同一収率かどうかが不明である。これは non-fatal と判定する（主要な 13 runs の生成物同定が主張されているため）。

**→ VQ-1 は通る（RI-02: non-fatal）。**

---

**VQ-2 [Method] は未達**

VQ-2 の要件: RI-01（Reporting integrity）および RI-07（Unsupported boundary）の解消。

- **RI-01 [Reporting integrity]**: SRG-1 として記録済み。GC キャリブレーション未記載・13 runs 中 10 runs で単離収率なし・TOF 数値の非掲載（B-1, B-2, B-3）。これは VQ-2 未達の直接理由である。収率報告の測定フレームが不統一であり、主要な性能主張（efficiency 柱）の評価が分析的に不可能な状態にある。**Fatal**（性能比較の横断的評価が原理的に不能）。

- **RI-07 [Unsupported boundary]**: SRG-4 として記録済み。「a variety of aromatic systems」「applicable more widely」という境界主張が芳香族ケトンのデータのみで支持されていない（B-5, U-3）。これも VQ-2 の境界テスト（method scope）に直接関わる。**Fatal**（「どこまで適用可能か」という方法論的境界が未確定）。

**→ VQ-2 は未達（RI-01: Fatal; RI-07: Fatal）。**

継承原則：VQ-2 は VQ-1（RI-02 non-fatal 通過）を前提とするが、RI-01 および RI-07 の未解消によりブロックされている。

---

**VQ-3 [Mechanism] は未達**

VQ-3 の要件: RI-03（Unobserved explanatory）、RI-04（Unreplicated discriminator）、RI-06（Imported model）の解消（+ VQ-2 継承）。

- **RI-03 [Unobserved explanatory]**: SRG-2 として記録済み。シクロメタル化中間体（U-1: critical）および前触媒活性化機構（U-2: high）が直接観測されていない。論文の機構提案の中核に位置する種が未観測。**Fatal**（触媒サイクルの機構的評価が原理的に不能）。

- **RI-04 [Unreplicated discriminator]**: SRG-3 として記録済み。「virtually 100%」位置選択性の主張が非観測異性体の探索条件なしに記述（B-10, U-4）。**Non-fatal**（選択性の実用的結論は単一観察の確認範囲内で成立するが、「virtually」の定量化には必要）。

- **RI-06 [Imported model]**: CLA-2 として記録済み。Mn(I)/Ru(II) 先行例を Ru(0) OA サイクルの類推根拠として使用（B-11, C-2, C-5）。**Fatal**（機構的に不整合な類推が Fig. 1 の唯一の間接証拠として機能している）。

注: VQ-3 は VQ-2 を継承するため、VQ-2 が未達である以上 VQ-3 への到達には VQ-2 要件の先解消が前提となる。

**→ VQ-3 は未達（RI-03: Fatal; RI-06: Fatal; RI-04: Non-fatal残存）。VQ-2 継承未達により二重ブロック。**

---

**VQ-4 [Benchmark] は未達**

VQ-4 の要件: RI-08（Unquantified reliability）、RI-09（External superiority）の解消（+ VQ-3 継承）。

- **RI-09 [External superiority]**: SRG-5 として記録済み。refs 11/12 との定量的 TON/TOF 比較なし（C-1, B-2）。**Fatal**（先行系との優位性主張が数値的に検証不能）。

- **RI-08 [Unquantified reliability]**: SRG-5 内で記録済み。比較データに反復測定・不確かさ記述なし。**Non-fatal**（単一観察として読むことは可能だが、ベンチマーク水準の主張には不足）。

**→ VQ-4 は未達（RI-09: Fatal; VQ-3 継承未達）。**

---

**層別VQ非対称性：**

§1 の Layered structure 分析に基づき、層別評価を行う：

- **層1（合成的達成）単独**: GC 収率データ（単離収率の部分的補完を含む）は観察として記録されており、RI-02 non-fatal 条件下で **VQ-1 に到達**。ただし収率の分析的前提（RI-01）が未解消のため VQ-2 には届かない。
- **層2（選択性）単独**: 「virtually 100%」選択性の観察事実として VQ-1 相当だが、RI-04（選択性の検出下限）および RI-05（速度差の定性的帰属）が残存するため、VQ-2（Qualified）に留まる。
- **層3（設計原理）単独**: RI-03（中間体の直接観測なし）および RI-06（輸入モデル）が fatal であり、VQ-1 通過後 VQ-2 どまり（設計原理の方法論的境界が未確認: RI-07 も関連）。

この層別非対称性は、層1（合成的達成）が本論文の最も堅牢な主張であり、層3（設計原理・機構）が最も脆弱であることを示す。

---

### §4 Era-Norm Annotation

**communication-era tolerated:**

- **B-1 / B-4**（GC キャリブレーション詳細の非記載・「standard methods」による同定）: 1993 年の Nature Articles は 1〜3 ページの短報形式であり、SI 制度が現在ほど発達していなかった。GC 収率報告における内部標準・応答係数の省略、および NMR + 元素分析の「standard methods」への集約は、当時の genre convention として許容される範囲内にあった。
- **B-2**（TOF 数値の非記載）: 1993 年時点でも TOF の定義（時間解像度・触媒活性種の mol 基準）は分野内で統一されておらず、「among the highest reported」という質的比較は競合する同時期の記述スタイルと整合する。定量的 TOF 報告が field standard として確立したのは 2000 年代以降の触媒科学である。
- **B-3**（代替触媒の比較条件詳細なし）: 短報における構造—活性相関データの省略は 1993 年 Nature 形式では標準的であり、主となる触媒系の scope 実証に紙面を集中させる編集方針と整合する。
- **C-1**（refs 11/12 との定量的比較なし）: 先行系が異なる反応系（Zr vs. Ru、異なる基質）である以上、共通基質での直接数値比較は 1993 年時点では実施困難であり、質的限界の列挙による間接比較は慣例的に許容されていた。
- **B-9**（1-インダノンの「not shown」否定的証拠）: 陰性データの「not shown」としての言及は、限られた紙面で結果の幅を示す当時の標準的記述スタイルである。

**modern-era deficient:**

- **B-1 / B-7**（GC キャリブレーション未記載・オレフィン消費未追跡）: 現代の触媒論文では SI への GC キャリブレーション詳細の掲載が標準的であり、「both starting materials」基準の定量的収率には反応物消費の GC 定量が必須とされる。VQ-2（RI-01）の解消に直接必要。
- **U-1 / U-2**（中間体の直接観測なし・前触媒活性化証拠なし）: 現代の有機金属触媒論文では、提案された触媒サイクルの少なくとも主要中間体について ESI-MS・NMR・X 線結晶解析による同定が期待される。シクロメタル化中間体の非観測は VQ-3（RI-03）の解消に直接関わり、現代基準では fatal と判定される。
- **B-5 / U-3**（「a variety of aromatic systems」という過剰一般化）: 現代の総合化学誌では、abstract の scope 記述がデータと乖離する場合、査読段階で修正が要求される標準となっている。非ケトン基質ゼロのデータで「variety of aromatic systems」と記述することは現代基準では不可（RI-07: Fatal）。
- **SRG-5 / C-1**（refs 11/12 との定量的 TOF 比較なし）: 現代の触媒論文では先行系との定量的 TON/TOF 比較表は標準的な要求事項である（RI-09: Fatal）。

**両タグ該当項目：**
- B-1（GC キャリブレーション省略）: 当時は紙幅制約で許容されていたが、現代では SI 掲載が標準であり modern-era deficient に該当。両タグに記載。

---

### §5 最短補強ルート

**目的関数：第一目的関数 = VQ-2 到達。第二目的関数 = VQ-3 到達（VQ-2 前提）。**

---

**VQ-2 への最短ルート：**

1. **EP-01a [Reporting-coherence pack]** — 全 13 runs の単離収率・GC 内部標準・応答係数を SI として開示し、runs 1, 9, 10 の時間解像度データ（yield vs. time, 少なくとも 3 時点）から初速 TOF を算出する。RI-01 を前進（fatal 解消）。

2. **EP-07a [Boundary-test pack]** — 非ケトン配向基質（アルデヒド・イミン各 1 例、ピリジン型 1 例）の試験反応（135 ℃, 4 h, 2 mol% Ru）を実施し、反応性 / 非反応性の境界を定義する。RI-07 を前進（fatal 解消）。

認定ゲート順注記：実験投入順は情報利得順（EP-01a → EP-07a）だが、VQ-2 認定は継承原則に従い VQ-1（RI-02 non-fatal 通過）が前提として確認された後、RI-01 および RI-07 の解消をもって VQ-2 が確定する。

---

**VQ-3 への最短ルート（VQ-2 達成後）：**

1. **EP-03a [Direct-observation / state-assignment pack]** — RuH₂(CO)(PPh₃)₃ と基質の化学量論的反応（トルエン, 135 ℃, 10〜60 min）における ³¹P{¹H} NMR / IR 観測によってシクロメタル化中間体または Ru(0) 活性種を同定する。RI-03 を前進（fatal 解消の最大寄与）。

2. **EP-06a [Analogy-validation pack]** — refs 14/15（Mn(I)/Ru(II) 電求型）と本提案 Ru(0) OA サイクルの酸化状態差・遷移状態差を明示した比較表を提示し、類推の有効範囲と限界を定義する。あるいは Ru(0) 源（例: Ru(COD)(COT)）を用いた対照シクロメタル化実験。RI-06 を前進（fatal 解消）。

3. **EP-04a [Discrimination / replication pack]** — 「virtually 100%」選択性の非観測異性体 GC 探索（標準品使用、検出下限 < 1 mol%）。RI-04 を前進（non-fatal → 解消）。

4. **EP-05a [Quantitative-ranking substantiation pack]** — ortho-D₅ 基質 KIE または Hammett 相関（4〜5 種 para-置換アセトフェノン）による選択性の速度論的帰属。RI-05 残存を軽減し VQ-3 (qualified) からの昇格を支援（CLA-1 解消）。

認定ゲート順注記：VQ-3 認定には VQ-2 の全要件解消が前提。EP-03a → EP-06a の順で RI-03/RI-06 の fatal を解消した後、EP-04a および EP-05a による non-fatal の軽減をもって VQ-3 が確定する。RI-05 が重大に残る場合は VQ-3 (Qualified) として記録する。

---

**VQ-4 への最短ルート（VQ-3 達成後）：**

1. **EP-09a [Internal benchmark pack]** — refs 11（Jordan & Taylor）および 12（Moore et al.）の文献 TOF 値を取得し、本論文 runs 1, 9, 10 の実測 TOF（EP-01a で算出）と同一評価基準（mol product / mol Ru / h, 初期 20% 転化率時）で表に並置する。RI-09 を前進（fatal 解消）。

2. **EP-08a [Replication / uncertainty pack]** — runs 9 および 10（最短反応時間・定量的収率）の独立繰り返し（n ≥ 3）を実施し、収率の標準偏差・TOF の不確かさを報告する。RI-08 を前進（non-fatal 解消）。

認定ゲート順注記：VQ-4 認定は VQ-3 の全要件解消が前提。

---

### §6 制度設計への寄与

**1. 既存 RI コードの代表事例の確認**

- **RI-03（Unobserved explanatory）のパラダイム事例**: Murai 1993 は RI-03 の最も典型的かつ影響力の大きい事例の一つである。「論文の成功の鍵」として明示的に中心化された中間体（Fig. 1 のシクロメタル化種）が単離・分光観測・速度論的拘束のいずれも欠くまま、機構提案の核として機能している構造は、後続のC–H活性化論文群（2000〜2010年代の Pd/Rh/Ir 系触媒 C–H 官能基化）が解決すべき問題の先例として位置付けられる。RI-03 の適用基準の代表事例として Codebook に記録する。

- **RI-06（Imported model）の「サイクルレベル輸入」サブタイプの確認**: Mn(I) 電求型・Ru(II) カルボキシレート系を Ru(0) OA 系の「類似物」として引用する CLA-2 は、RI-06 の「サイクルレベル輸入」サブタイプ（個別素反応ではなく触媒サイクル全体を別系から構成する大規模モデル輸入）の典型事例であり、Codebook v0.2a の注記との適合を確認する。

**2. 標識不整合（Labeling mismatch）パターンの検出**

本論文は「[REDACTED: verbatim source text; see the source paper via its DOI]」（A-1）という機構的限定を明示しながら、本文の他の箇所では「[REDACTED: verbatim source text; see the source paper via its DOI]」（U-1 key_quote）という事実的記述語（"results in", "give"）を使用している。

限定表明（「not yet clear」）が本文末尾の Possible mechanisms 節に集約されており、Results・Abstract・Applications の叙述語が事実的記述を維持しているため、構造的な仮説標識不整合が存在する。§4 で記録した「modern-era deficient」の B-5/U-3（scope 記述の過剰一般化）とも類似のパターンを共有する。**Labeling mismatch を Murai 1993 の代表事例として Codebook に記録することを推奨する。**

**3. 通信→Full Paper 遷移の自動解消パターン**

B-1（GC キャリブレーション省略）・B-3（代替触媒比較の条件詳細なし）・B-4（「standard methods」）は、Nature Letters 形式から Full Paper 形式への遷移で自動解消が期待されるパターン（SI 掲載による解消）である。§4 の Era-Norm Annotation の「communication-era tolerated」項目との対応が確認される。**RI-01 における「通信→Full Paper 自動解消」パターンの適用事例として記録する。**

**4. RI-05 の重大残存と VQ-3 (Qualified) 境界条件**

B-8（run 10 vs. 11 速度差のリング歪み帰属）は RI-05（数値なき定性的順位から構造的含意を導出）の典型であり、これが VQ-3 の「RI-05 が重大に残る場合は VQ-3 (Qualified)」という注記条件に該当するかを検討した。本ケースでは、速度差が活性化エネルギー差に相当する量的差（run 10: 0.5 h, 100% vs. run 11: 20 h, 88%）を示しており、RI-05 が VQ-3 (Qualified) 境界を定める境界事例となる。Codebook の RI-05 に「速度比率が 40:1 程度の定性的帰属での境界事例: Murai 1993 run 10 vs. 11」として記録することを推奨する。

**5. PRI 候補の検出**

- **PRI-11（Mechanism-kinetics decoupling）との関連**: D-4-6 / CLA-1 が提起した「速度論/熱力学フレームの不在」は PRI-11 の定義（「提案触媒サイクルから速度式を代数的に導出せずに、観測速度次数との一致のみで機構を支持」）に部分的に対応する。本論文では速度式自体を導出・観測していないため PRI-11 の直接適用は難しいが、「速度式を導出も観測もせずに機構を提案した」パターンとして PRI-11 の拡張（速度式の不在そのものを問う）を §6 で記録する。PRI-11 の定義範囲の拡張を検討する際の新規事例として提案する。

- **新規 PRI 候補: 「Bilateral-yield claim without mass closure（双方向収率主張の質量収支不閉鎖）」**: B-7（「両基質基準での定量的収率」主張とオレフィン消費の未追跡）は、反応物の一方（オレフィン）の消費を追跡せずに両基質基準の収率を主張するパターンである。このパターンは SRG-4（Scope claims exceed data）の一事例だが、独立した RI コードとして定義できるかを検討する価値がある。2 報以上での同型確認後に PRI 候補として提案する。現段階では RI-01 の サブタイプ（RI-08 内部矛盾型の変形）として記録する。

**6. Stage 2F なし（単報モード）**

本ケースは Stage 2F 入力なし（単報モード）で実行されているため、recurring_pattern からの RI 昇格判断材料は本ケースでは取得不能。multi-run sentinel 運用の文脈では、Stage 3 の出力を cross-run で比較する上位集約が必要。
