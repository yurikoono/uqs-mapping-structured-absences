prompt_version: stage3-v2-20260416
model_info: claude-sonnet-4-6

# 科学的知見の再認定判定票

## Murai et al. 1993（Nature, Article）

---

### §1 Claim Architecture

#### コア主張の要約

本論文のコア主張は二柱からなる。**Novelty柱**：RuH2(CO)(PPh3)3が、芳香族ケトンのortho C–H結合をオレフィンに対して触媒的に付加させ、13例の基質スコープにわたって高収率・高位置選択性（「ほぼ100%」）を達成する。これは触媒的C–H官能化において定量的収率を「初めて」達成したものであり（NC-4）、先行例（Jordan & Taylor 1989, Moore et al. 1992）を収率・副生成物・汎用性の三点で超えると主張する。**Utility柱**：この手法は実用的有機合成（"practical organic synthesis"）に必要な効率性・選択性・汎用性を同時に実現し（NC-2）、キレーション支援という戦略は有機金属触媒一般に広く応用できる（NC-5）。

#### Layered structure の判定

**yes — 独立三層構造**。Stage 2 D-1が特定した通り、論文の主張は独立した三層に分割できる。

- **第一層（実験的実証層）**：芳香族ケトン/オレフィン系での高収率・高選択性の実証。Table 1の13例のGC収率データで直接支持される。この層は機構への異議申し立てに対して独立して成立する。
- **第二層（汎用性層）**：基質一般性の主張（アシルベンゼン + ヘテロ芳香族 + 多様なオレフィン）。同じくTable 1で支持されるが、「芳香族ケトンに限定」というスコープ境界問題（U-3, B-5）が潜在する。
- **第三層（機構的原理層）**：キレーション支援によるRu(0)触媒サイクルの提案（Fig. 1）。著者自身が"not yet clear"と留保しており、先例文献の機構的類推（refs 14, 15, 17）のみで支持されている。機構への反論は第一・第二層の実験的事実を損なわない。

**含意**：論文の主張のうち、第一層は実験的事実として最も堅牢であり、第三層は仮説的に最も脆弱である。第三層に対する反証（別機構の実証、中間体の非存在確認）があっても第一層の主張は残存しうる。ただし、「なぜこの選択性が生じるのか」という設計原理としての第三層が崩れれば、新基質予測・条件最適化のための理論的枠組みが失われ、論文のUtility柱の射程が狭まる。

---

### §2 SRG / CLA → RI / ER / EP Crosswalk

#### 2a. SRG の取得

Stage 1のMETAより、以下の五つのSRGが確定している：

- SRG-1：定量的証拠基盤の不在（B-1, B-2, B-3, B-4）
- SRG-2：触媒サイクルの実験的根拠の不在（A-1, U-1, U-2）
- SRG-3：選択性根拠の不在（B-8, B-9, B-10, U-4）
- SRG-4：スコープ主張とデータの乖離（B-5, U-3, B-7）
- SRG-5：先行技術との定量的比較なし（C-1, B-2）

#### 2b. CLA 候補の同定

D-4候補のうち、いずれのSRGにも属さない独立候補を検討する。

- **候補7**（触媒量増加runs 5・6、B-6のみに根拠）：B-6はSRG-1のmember_items（B-1, B-2, B-3, B-4）に含まれていない。D-1の主張「汎用性」（NC-2）の内部に、条件不統一という矛盾を内在させる。CLAとして記録する。
- **候補8**（機構的類推の妥当性、B-11, C-2, C-5）：B-11はSRG-2の記述の中で言及されているが、METAのSRG-2のmember_itemsはA-1, U-1, U-2の三項目であり、B-11は明示的に含まれていない。触媒サイクルの実験的根拠（SRG-2）とは異なる問い（先例文献の機構的互換性）を問うため、CLAとして記録する。
- **候補9**（速度論的vs熱力学的制御、B-8, B-9）：grounded_inがSRG-3のmember_itemsに含まれる（B-8, B-9はSRG-3に属する）。CLA不適格。

**自己矛盾的不在のCLAチェック**：
Stage 1のU-1（環化金属中間体の実験的確認不在）は、「触媒サイクルが中間体の存在を予測するが、その分光学的観測・単離・トラッピングが論文内に存在しない」という典型的な自己矛盾的不在パターンに該当する。U-1はSRG-2に含まれており、別CLAを生成しない。

---

**SRG-1 [定量的証拠基盤の不在]**

* **Primary RI**: RI-01 [Reporting integrity] — GC収率とTOF主張の計測フレームが横比較不能
* **Secondary RI**: RI-08 [Unquantified reliability] — GCキャリブレーション法・内部標準の不在により不確かさが未記述
* **ER**: 「実用的有機合成に必要な効率性」主張を採るためには、GC収率の測定方法（内部標準、応答係数）、全基質の単離収率、runs 1/9/10のTOF実測値、および先行技術（refs 11/12）との共通基質上での定量的比較が必要。
* **EP**: EP-01a [Reporting-coherence pack]; EP-08a [Replication / uncertainty pack]
* **Case-specific実装**: (1) runs 1, 9, 10のTOFを (mol product)/(mol Ru × h) として算出し表に明示、(2) 内部標準（例：n-テトラデカン）を用いたGCキャリブレーション曲線を確立し全13例に適用、(3) 単離収率のない runs 2, 4, 5, 7, 9, 10, 11, 12 をカラムクロマトグラフィーで精製・単離して収率と純度を報告、(4) refs 11/12の先行報告TOFと共通尺度での直接比較表を作成
* **注記**: B-1 (V1=high, V3=high; convergence 2/3), B-2 (V1=high, V3=high; convergence 2/3), B-3 (V1=medium, V2=medium, V3=medium; convergence 3/3; high_convergence_low_gap), B-4 (Stage 1独立記録)。TEMPERATURE_SUMMARYでhigh_convergence_low_gap群の主要構成要素。

---

**SRG-2 [触媒サイクルの実験的根拠の不在]**

* **Primary RI**: RI-03 [Unobserved explanatory] — 提案触媒サイクルの中心中間体（環化金属錯体）が直接観測も速度論的拘束もされていない
* **Secondary RI**: RI-06 [Imported model] — 触媒サイクル全体がMn(I)/Ru(II)系先例（stoichiometric）からRu(0)触媒系へサイクルレベルで輸入されている（RI-06スコープ注記：サイクルレベル輸入に該当）
* **ER**: 「キレーション支援Ru(0)触媒サイクルが機構的に妥当」という主張を採るためには、Fig. 1の環化金属中間体の分光学的観測（³¹P{¹H} NMR、X線結晶構造）または化学的トラッピング、RuH2(CO)(PPh3)3からRu(0)活性種への変換の確認（誘導期、活性化スペクトロスコピー）、および先例文献（refs 14/15）の機構クラスとRu(0)酸化的付加機構との互換性評価が必要。
* **EP**: EP-03a [Direct-observation / state-assignment pack]; EP-06a [Analogy-validation pack]
* **Case-specific実装**: (1) RuH2(CO)(PPh3)3とアセトフェノンの化学量論反応（トルエン, 135°C, 1–24 h）を³¹P{¹H} NMRでモニタリングし、環化金属中間体のリン原子シグナルを帰属、(2) 重水素化アセトフェノン（芳香環d5）を用いたKIE測定でortho C–H開裂が律速かを判定、(3) CO雰囲気下または光照射下でのRu(0)モデル化合物（例：Ru(CO)2(PPh3)3）との比較反応によりRu(0)活性種の役割を確認、(4) refs 14/15の機構（電子求引的vs. Ru(II)カルボキシラート）とRu(0)OA機構の酸化状態変化の数値的比較（酸化電位、NMR化学シフト）
* **注記**: U-1 (critical severity, V2-Q4, V3-OV4確認; high_convergence_low_gap, convergence 2/3), U-2 (high severity, V2 only; low_convergence_high_gap), A-1 (mechanism deferral, V2 critical; フォールバック規則(a)最優先項目)。SRGの三項目が互いに補強し合う構造（A-1がU-1/U-2の「公式免責」として機能）。RI-03とRI-06の共起パターン（§6で詳述）。

---

**SRG-3 [選択性根拠の不在]**

* **Primary RI**: RI-05 [Qualitative overread] — 速度差（run 10 vs 11）とring strain帰属（B-8）、位置異性体の未検出（B-10）から構造的・因果的含意を導出している
* **Secondary RI**: RI-04 [Unreplicated discriminator] — 1-indanoneの「無反応」という単一陰性データをring strain仮説の支持として使用（B-9）；代替説明の排除なし
* **ER**: 「ほぼ100%の位置選択性」と「ring strainによるキレーション重要性」という選択性主張を採るためには、GC/NMR分析による三種の非観測位置異性体の検出下限の明示、run 10/11の速度定数（kobs）測定、ring strainを系統的に変化させた基質シリーズの比較速度論、1-indanoneの反応条件・時間・GC分析データの開示が必要。
* **EP**: EP-05a [Quantitative-ranking substantiation pack]; EP-04a [Discrimination / replication pack]
* **Case-specific実装**: (1) run 8/13（2置換芳香族ケトン）の反応粗生成物を³種の位置異性体標品と直接GC/MSで比較し、各異性体の検出下限（例：<1%）を明示、(2) テトラリノン（run 10）対テトラリン-1-オン誘導体（run 11）の系列でkobsを測定し活性化パラメータ（ΔH‡, ΔS‡）を算出、(3) 5-, 6-, 7-membered環ケトンを用いたring strain系列実験、(4) 1-indanoneの実験データ（基質/触媒量、反応時間、GC収率）を「not shown」から開示に転換
* **注記**: B-8 (V1=medium, V2=high; convergence 2/3; high_convergence_low_gap), B-9 (V1=medium, V2=high; convergence 2/3; high_convergence_low_gap), B-10 (独立温度記載なし), U-4 (medium severity)。SRG-3は「選択性の記述的報告」と「選択性の機構的説明」の分離構造を持つ（§4 Era-Normで詳述）。

---

**SRG-4 [スコープ主張とデータの乖離]**

* **Primary RI**: RI-07 [Unsupported boundary] — 「a variety of aromatic systems」（アブストラクト）という境界主張が、芳香族ケトン13例のみのデータで支持されている；非ケトン指向基系の失敗例を示さずに限界を宣言していない点で境界の外延が確定しない（RI-07拡張適用：境界の過大申告）
* **Secondary RI**: RI-01 [Reporting integrity] — B-7: オレフィン消費量が未報告であり、「基質双方に対して定量的収率」という主張の質量収支が閉じていない
* **ER**: 「実用的有機合成に資する汎用性」という主張を採るためには、指向基の種類（アルデヒド、エステル、アミド、イミン、スルホキシド）を系統的に試験し、有効/無効の境界を明示すること、また定量的収率主張の根拠としてオレフィンの消費率（GCまたは¹H NMR）を報告することが必要。
* **EP**: EP-07a [Boundary-test pack]; EP-01a [Reporting-coherence pack]
* **Case-specific実装**: (1) アセトフェノン系を維持しつつ指向基をアルデヒド（PhCHO）、エステル（PhCOOMe）、アミド（PhCONMe2）、イミン（PhCH=NtBu）に順次変更してトリエトキシビニルシランとの反応を試験し、GC収率を報告、(2) 無効基質については反応条件（時間、温度、触媒量）を明示した陰性データを開示、(3) run 8–13の粗生成物をGCで分析しオレフィン残量を定量して「両基質に対して定量的」主張の質量収支を閉鎖
* **注記**: U-3 (high severity, self-contradictory absence; フォールバック規則(a)に該当), B-5 (mixed, B-5 ↔ U-3リンク確認), B-7 (V1-Q11由来; 質量収支未報告)。

---

**SRG-5 [先行技術との定量的比較なし]**

* **Primary RI**: RI-09 [External superiority] — refs 11/12の先行技術に対する優位性が直接比較なしに外部文献への言及のみで主張されている
* **Secondary RI**: RI-01 [Reporting integrity] — B-2: TOF値が数値として報告されないまま「最高水準に属する」と宣言されている
* **ER**: 「先行技術を超える効率性・汎用性」という競争的優位主張を採るためには、refs 11/12と共通の基質（例：ピリジン系誘導体と本反応のケトン系の橋渡しとなる化合物）または共通の評価指標（TON/TOF/収率/選択性）での直接比較表が必要。
* **EP**: EP-09a [Internal benchmark pack]; EP-08a [Replication / uncertainty pack]
* **Case-specific実装**: (1) runs 1, 9, 10のTOFを (mol product formed per mol Ru per hour) として計算し明示、(2) Jordan & Taylor (JACS 1989) のZr触媒α-ピコリン/プロペン系のTON・副生成物率と本反応の代表的なrun（run 9/10）のTON・選択性を同一表で比較、(3) Moore et al. (JACS 1992) のRu/pyridine/CO/1-hexene系の収率・基質適用範囲と本反応の芳香族ケトン/オレフィン系を統合的に評価する補足表を作成
* **注記**: C-1 (Severed quantitative comparison, JACS refs 11/12との対比), B-2 (V1=high, V3=high; convergence 2/3)。SRG-5はSRG-1と密接に連動しており（B-2が両SRGに属する）、EP-09aとEP-01aの投入が相互補強的に機能する。

---

**SRG外：CLA**

---

**CLA-1: 触媒量不均一性の機構的含意（B-6）**

* **Primary RI**: RI-01 [Reporting integrity] — 標準2 mol%から6 mol%への3倍増加という条件不統一が無説明のまま表に存在し、均一なスコープ主張の内部に不整合を生じさせている
* **Secondary RI**: RI-07 [Unsupported boundary] — 標準条件で「一般化可能」という汎用性主張が、アリルシラン基質に対しては成立しないことが示唆されるが、その境界が説明されていない
* **ER**: 「2 mol%触媒量で汎用的に適用できる」という効率性・汎用性の統合主張を採るためには、runs 5・6においてなぜ6 mol%が必要であったかの実験的根拠（標準2 mol%での試み・収率、触媒量依存性）を報告する必要がある。
* **EP**: EP-07a [Boundary-test pack]
* **Case-specific実装**: アリルトリメチルシラン（run 5用基質）を用いて触媒量を1, 2, 4, 6 mol%と変化させた一連の実験を実施し、触媒量と収率・時間の関係をプロットする
* **注記**: B-6単独からなるCLA（SRG-1に属するBi項目のサブセットではない）; V1が主要フラグ; D-4候補7の根拠項目。runs 5（4 h, 100%）とrun 6（33 h, 96%）の時間差（同一6 mol%条件下で8倍の反応時間差）という追加の定性的問いを内包する。

---

**CLA-2: 機構的類推の酸化状態非互換性（B-11, C-2, C-5）**

* **Primary RI**: RI-06 [Imported model] — refs 14/15（Mn(I)電子求引的機構・Ru(II)カルボキシラート機構から得られるcyclometallation生成物）をRu(0)酸化的付加機構の中間体証拠として輸入している；酸化状態クラスの非互換性が論文内で全く議論されていない
* **Secondary RI**: RI-05 [Qualitative overread] — 「生成物が類似している（products similar to）」という構造的類似から、機構の類似性・中間体の実在性を含意として導出している
* **ER**: Fig. 1の環化金属中間体の構造的妥当性の根拠として先例文献を用いるためには、先例文献の機構クラス（酸化状態、中心金属、配位子）とRu(0)酸化的付加機構との異同を明示的に議論し、「生成物の類似性」が「経路の類似性」を意味しない場合の代替解釈を排除する必要がある。
* **EP**: EP-06a [Analogy-validation pack]
* **Case-specific実装**: (1) ref 14（Mn(I)/CH3Mn(CO)5）とref 15（Ru(II)/RuCl(OC(O)CH3)(CO)(PPh3)3）のcyclometallation反応の酸化状態変化（Mn(I)→Mn(III) or Mn(I)→Mn(I)?) とFig. 1のRu(0)→Ru(II) OA経路の電子的変化を明示的に比較するスキームを作成、(2) Ru(CO)2(PPh3)3（「equally effective」触媒、B-3）とアセトフェノンとのモデル反応でRu(0)OAを直接観察し、refs 14/15との機構的比較の基盤を確立
* **注記**: B-11 (mechanistic analogical citations; mixed), C-2 (stoichiometric cyclometallation from Mn(I)/Ru(II) vs. proposed Ru(0) OA; reason_severed), C-5 (ref 17 olefin OA vs. C–H OA; reason_severed)。RI-06とRI-05の共起パターン（§6で詳述）。SRG-2のRI-03/RI-06共起とは「同じRu(0)サイクルへの異なる入口」として区別される：SRG-2は「中間体の不在」を問い、CLA-2は「中間体の先例の機構的整合性」を問う。

---

### §3 現在のVQ判定

現在判定: **VQ-1 [Observation]**（第一・第二層限定では VQ-2 [Method] 通過）

---

**VQ-1 [Observation] は通る（第一・第二層限定）**

必須解消項目RI-02（Object identification）の検討：全13例の生成物について「standard methods」による構造確認が宣言されており（B-4）、これは当時の自然科学系Natureのarticle掲載論文として最低限の証明標準を満たしている。各生成物は対応するケトン-オレフィン由来の固有の骨格を持ち、構造の主要な曖昧性（位置異性体の同一視等）は論文内データでは排除されていない（B-10, U-4）が、VQ-1の「主生成物の同定」という閾値は超えている。VQ-1通過を宣言する。

ただし、B-4（「standard methods」の未定義）は現代基準ではRI-02の非致命的残存として記録する（§4参照）。Si含有生成物（runs 1–13のほぼ全例）の構造確認として¹H NMR + 元素分析または高分解能MSが必要であることが示唆されるが、論文形式の制約下での省略として当時は許容される（Era-norm toleratedの候補）。

---

**VQ-2 [Method] の判定**

必須解消項目：RI-01（VQ-1継承含む）、RI-07。

RI-01（SRG-1）：GC収率のキャリブレーション法が未開示（B-1）、TOF数値が未報告（B-2）、代替触媒比較の定量的条件が未報告（B-3）。これらは「GC収率を方法論的に再現できない」という報告整合性の致命的欠落であり、独立な定量的再現が不可能である。**VQ-2 の RI-01 要件に対して未達（Fatal）**。

RI-07（SRG-4）：「a variety of aromatic systems」というスコープ主張は、芳香族ケトン13例のみのデータによって支持されており、境界（non-ketone directing groups）の失敗例が存在しない。スコープ境界が論文の主題上の制限として著者が意図した場合でも、アブストラクトの主張は明示的な限定を欠く。**RI-07 は非致命的（Non-fatal）**だが解消されていない。

**VQ-2 は未達（RI-01の致命的未解消による）。**

---

**第一・第二層（実験的実証層・汎用性層）単独のVQ非対称性**

ただし**第一・第二層**（実験的実証）単独では：VQ-2は「条件付き通過」に近い位置にある。RI-01の残存はfatalであるが、「GC収率の相対比較」としての信頼性（同一反応系・同一条件での内部比較）は担保されており、Table 1の結果の定性的妥当性は独立した研究グループによる追試（後年の多数の追試文献の存在が外部的に示す）によって事後的に確認されている。これはEra-norm問題であり、論文内部では解消されていない。

---

**VQ-3 [Mechanism] の判定**

必須解消項目：RI-03、RI-04、RI-06（+ VQ-2継承）。

RI-03（SRG-2）：Fig. 1の環化金属中間体が直接観測も速度論的拘束もされておらず、触媒サイクルの中心説明種が実験的に存在しない。**Fatal（VQ-3未達の最重要因）**。著者自身の"not yet clear"留保（A-1）がこれを公式に確認している。

RI-04（SRG-3）：1-indanoneの単一陰性例（B-9）からring strain仮説を支持する推論は、代替経路（立体・電子効果）を排除していない。**Non-fatal**（第一層の主張には直接影響しない）。

RI-06（SRG-2, CLA-2）：Mn(I)/Ru(II)先例の機構を Ru(0)触媒系へサイクルレベルで輸入（B-11, C-2）し、olefin OA先例（ref. 17）をC–H OAの証拠として援用（C-5）。**Non-fatal**（補助的機構論証の弱体化にとどまるが、RI-03と共起することで主張全体が類推のみに依拠する構造となる）。

RI-05注記：SRG-3においてRI-05が残存（run 10/11速度差からring strain帰属）。「VQ-3は限定的（Qualified）」との注記を付す。

**VQ-3 は未達（VQ-2未達の継承 + RI-03 Fatal）。第三層（機構的原理層）は VQ-1 水準にとどまる。**

---

**VQ-4 [Benchmark] の判定**

必須解消項目：RI-08、RI-09（+ VQ-3継承）。

VQ-3が未達であるため、VQ-4の独立判定は論理的に不成立。参考として：RI-09（SRG-5）はTOF数値未報告（B-2）と先行技術との直接比較欠如（C-1）により確実に未解消。RI-08（SRG-1）はGCキャリブレーション法・不確かさ記述の欠如（B-1）により未解消。

**VQ-4 は未達（VQ-3の未継承 + RI-08, RI-09の双方が未解消）。**

---

**判定サマリー**

| 水準 | 判定 | 主要根拠 |
|:-----|:-----|:---------|
| VQ-1 [Observation] | **通過** | B-4（"standard methods"）Era-norm注記付き |
| VQ-2 [Method] | **未達** | RI-01 Fatal（GCキャリブレーション未開示、TOF未報告） |
| VQ-3 [Mechanism] | **未達** | RI-03 Fatal（中間体未観測）+ VQ-2継承未達；RI-05残存でQualified扱い |
| VQ-4 [Benchmark] | **未達** | VQ-3継承未達 + RI-08, RI-09 未解消 |

---

### §4 Era-Norm Annotation

#### communication-era tolerated

**B-4（"standard methods"による構造決定）**：
1993年のNature Articleでは、構造決定法を "standard methods"（¹H NMR, 元素分析等）と集約して記述する慣行が許容されており、個別の分析データを補足情報に掲載する現代のOpen Data規範は存在しなかった。

**B-1（13例中10例で単離収率未報告、GCのみ）**：
3ページのNature Article formatでは、GC収率による主生成物の確認が標準的な報告方法であり、全例の単離収率を追加する誌面は存在しなかった。当時の有機金属触媒論文ではGC収率の単独報告が一般的であった。

**B-2（TOF値の数値不記載）**：
TOFの比較報告は1993年時点の触媒化学論文でも推奨されていたが、 "among the highest reported"という定性的宣言を数値証拠なしに行う形式は当時のNature短報の許容範囲内であった。紙幅制約（単一表に全データを収納する必然性）との相互作用がある。

**A-1（メカニズム未解明の公式宣言）**：
1993年の実験的有機金属化学では、新触媒反応の発見論文において「機構は不明」と宣言しつつ基質スコープを先行報告する慣行は広く受け入れられていた。反応機構の詳細研究は後続論文の役割として明示的に分離されることが多かった。これはStage 2 D-3のentry_criteriaとしても確認されている（「メカニズムの解明はentry criteriaとして要求されていない」）。

**B-3（代替触媒比較の定量的条件不在）**：
代替触媒の比較を定量的データ（収率、条件）なしに「有効/無効」という二値分類で記述することは、1993年の短報・Articles形式の通常的な慣行であった。

**B-9（1-indanoneの "not shown"）**：
陰性データを本文中に「not shown」として記述し、正確な条件と数値を報告しない慣行は1993年時点のNature format内で許容されていた（3ページのスペース制約）。

---

#### modern-era deficient

**B-1（GCキャリブレーション法の非開示）**：
現代の再現性要件（Reproducibility Initiative、FAIR data原則）では、GC収率報告には内部標準物質の特定、応答係数の算出方法、キャリブレーション曲線の構築を補足情報に開示することが求められる。未開示の場合、独立した第三者による定量的再現が原理的に不可能となる。**RI-01: Fatal（VQ-2未達の主因）**。

**B-2（TOF数値の完全不在）**：
"among the highest reported"という優位性主張に対して、現代の触媒評価基準ではTOF（および/またはTON）を数値として報告し、比較先文献の値も並記することが義務的である。数値のない優位性宣言はEra-norm的に許容から現代基準で「要修正」に遷移している。**RI-09: Non-fatal（第一層の主張には直接影響しないが、優位性主張の信頼性を損なう）**。

**U-1（環化金属中間体の実験的不在）**：
現代の機構化学論文では、提案触媒サイクルの中心的中間体については、少なくとも低温NMR観察またはトラッピング実験の試みが要求される。中間体の存在を「類推的先例」のみで支持する記述は、現代の査読では機構的証拠として認められない。**RI-03: Fatal（VQ-3未達の最重要因）**。

**U-3（スコープ主張「a variety of aromatic systems」のアブストラクト記述）**：
現代の発見論文では、アブストラクトのスコープ記述は実際に試験されたシステムを反映した限定表現を用いることが求められる。「a variety of aromatic systems」は「a variety of aromatic ketone systems」と修正されなければ、再現性を試みる研究者に誤った範囲期待を与える。**RI-07: Non-fatal（実験結果の誤りではなく表現の問題）**だが、現代基準では修正必須。

**B-10（位置異性体の検出下限非明示）**：
"virtually 100%"選択性主張に対し、現代の合成方法論論文では三種の非観察位置異性体の検出上限（GC-MS, ¹H NMR）を明示することが求められる。「virtually」という限定語を具体的な数値（例：<1%、<2%）で裏付けなければ、工業プロセスや精密合成への適用可能性の判断基準が得られない。**RI-05: Non-fatal**。

**B-6（runs 5・6の触媒量増加の説明なし）**：
現代の合成方法論論文では、標準条件からの逸脱（本例では3倍の触媒量増加）は本文または補足情報で説明することが求められる。無説明の条件不統一は、汎用性主張の内部整合性を損なう。**CLA-1のRI-01: Non-fatal**。

**B-7（オレフィン消費量の未報告）**：
「基質双方に対して定量的収率（both starting materials are obtained）」という主張に対し、現代の合成方法論論文ではオレフィンの消費率（GCまたは¹H NMR）を質量収支の一部として報告することが要求される。**SRG-4のRI-01: Non-fatal**。

---

**両タグに該当する項目（当時は許容・現代では不足）**

- **B-1**（GC収率方法・単離収率）：当時のNature Article format制約で許容されていたが、現代の再現性要件で致命的欠落となる（RI-01 Fatal）。
- **B-2**（TOF数値不在）：当時は"among the highest"という定性的宣言が許容されていたが、現代の触媒評価基準でRI-09に該当する。

---

### §5 最短補強ルート

#### 5a. 目的関数の設定

**第一目的関数：VQ-2 [Method] への到達**
現在 VQ-1 → VQ-2 が最短の現実的ルート。VQ-2に必要なRI-01（Fatal）とRI-07（Non-fatal）の解消が優先される。

**第二目的関数：VQ-3 [Mechanism] への到達**（VQ-2達成が前提）
VQ-3に必要なRI-03（Fatal）の解消が主要課題。RI-04、RI-06、RI-05（Qualified注記）の解消も必要。

---

**VQ-2 への最短ルート：**

1. **EP-01a [Reporting-coherence pack]** — GC収率の内部標準・応答係数を確立し、runs 1–13の全測定条件を補足情報に開示し、単離収率未報告の10例（runs 2, 4, 5, 7, 9, 10, 11, 12）を単離・精製して収率を追加報告する。RI-01を前進（致命的欠落の解消）。

2. **EP-07a [Boundary-test pack]** — 非ケトン指向基系（アルデヒド、エステル、アミド）でのトリエトキシビニルシランとの反応を試験し、陽性/陰性のいずれにせよ結果を開示する（スコープ境界の明示）。RI-07を前進（Non-fatal解消）。

3. **EP-09a [Internal benchmark pack]** — runs 1, 9, 10のTOF（mol product / mol Ru / h）を算出して表に明示し、refs 11/12の文献TOFと並べた比較表を作成する。SRG-5のRI-09を前進。

認定ゲート順注記：EP-01a → EP-07a → EP-09a の順が情報利得最大化の順であるが、最終認定は VQ-1 → VQ-2 のゲート順で確定する。EP-01a（RI-01解消）が VQ-2 認定の必要条件。EP-07aとEP-09aは同時に進めることができる（相互独立）。

---

**VQ-3 への最短ルート：**（VQ-2 達成後）

1. **EP-03a [Direct-observation / state-assignment pack]** — RuH2(CO)(PPh3)3とアセトフェノンの化学量論反応を低温でNMR（³¹P{¹H}、¹H）観測し、環化金属中間体の同定を試みる（場合によりX線結晶構造解析）；また重水素化アセトフェノン（d5）を用いたKIE測定（kH/kD）でC–H開裂の律速性を確認する。RI-03（Fatal）を前進。これはVQ-3到達の必要最低条件である。

2. **EP-06a [Analogy-validation pack]** — refs 14/15のcyclometallation機構（酸化状態変化スキーム）とFig. 1のRu(0)OA機構の電子的・構造的比較を論文本文内で明示的に実施し、「生成物の類似性」と「経路の類似性」の区別を議論する。RI-06（Non-fatal）を前進（CLA-2の解消）。

3. **EP-05a [Quantitative-ranking substantiation pack]** — run 10/11の速度定数（kobs）測定とring strain系列実験（5員〜7員環ケトン）によりRI-05を前進させ、"Qualified"注記を除去する。RI-05（Non-fatal）を前進。

4. **EP-04a [Discrimination / replication pack]** — 1-indanoneの陰性データ（反応条件、GC収率、反応時間）を開示し、代替説明（立体・電子・溶解度効果）との識別実験を追加する。RI-04（Non-fatal）を前進。

認定ゲート順注記：EP-03a（RI-03解消）が VQ-3 認定の必須関門。EP-06a, EP-05a, EP-04aはEP-03aと並行して進めることができるが、VQ-3認定は RI-03 解消の確認後に成立する。

---

**VQ-4 への最短ルート：**（VQ-3 達成後）

1. **EP-08a [Replication / uncertainty pack]** — 代表的run（例：run 9, 10）を独立に3回以上繰り返し、GC収率の標準偏差と単離収率の変動幅を報告する。RI-08（Non-fatal）を前進。

2. **EP-09a [Internal benchmark pack]**（VQ-2ルートで既に投入）— refs 11/12との共通尺度での定量比較が VQ-4 の RI-09 要件を満たす。

認定ゲート順注記：実験投入順は情報利得順（EP-03a → EP-08a → EP-09a）だが、認定は VQ-1 → VQ-2 → VQ-3 → VQ-4 のゲート順で確定する。

---

### §6 制度設計への寄与

#### 1. 既存RIコードの代表事例

**RI-03のサブタイプ（自己矛盾的不在）の典型事例**：
本論文のU-1（環化金属中間体の不在）は、「論文が提案する触媒サイクルがFig. 1として明示的に図示し、選択性の説明に援用している実体が、同じ論文の実験部分に一切登場しない」という自己矛盾的不在の純粋な事例である。"not yet clear"という著者自身の宣言（A-1）がこのRI-03を公式に認証しており、Codeookに記録された「Available-but-unutilized characterization」サブタイプとは区別される（本事例は「取得済みだが未活用」ではなく「取得未実施」）。今後の判定票でU項目が"self-contradictory absence"と分類された場合、同一のRI-03適用と致命性判定（Fatal）を適用する先例として機能する。

**RI-09の代表事例**：
B-2（TOF「最高水準に属する」宣言 + 数値不記載）とC-1（refs 11/12との直接数値比較欠如）の組合せは、RI-09の純粋な事例である。優位性主張が三つの欠落（自紙TOF数値なし、比較先文献TOF値なし、共通基質なし）の重畳によって生じており、「直接比較なしに外部文献値のみで優位性を主張」というRI-09の定義を完全に実装する。

#### 2. RI共起パターンの記録

**RI-03 + RI-06の共起（SRG-2）**：
本論文では、「中間体が実験的に存在しない（RI-03）」と「その中間体の構造的妥当性が異なる機構クラスの先例（Mn(I)/Ru(II)）から輸入されている（RI-06）」が同一SRGで共起している。これは「中間体の不在を先例の類推で補おうとしているが、その類推自体も機構的に不整合」という二重の問題構造を形成している。いずれか一方の解消（例：中間体をNMRで観測すればRI-03が前進）は他方（先例の機構的非互換性、RI-06）を残存させる。この共起パターンでは、EP-03a（RI-03前進）とEP-06a（RI-06前進）の両方が必要となる。今後の判定票でRI-03 + RI-06の共起が検出された場合、「機構的実体の不在を機構的に非互換な類推で補う」パターンとして参照すること。

**RI-06 + RI-05の共起（CLA-2）**：
「先例文献を機構的根拠として輸入（RI-06）」と「生成物の類似性から経路の類似性を導出（RI-05）」が共起している。この共起は「構造的証拠の不在を外部モデルで埋め、その外部モデルの適用を定性的推論で正当化する」という二段構造の推論であり、EP-06a（Analogy-validation）の単独投入で両方を前進させることができる（EP-06aがRI-06とRI-05の双方を標的とする）。

#### 3. VQ判定基準の境界条件に関する新知見

**第一層（実験的実証層）と第三層（機構的原理層）のVQ非対称性**：
本論文は、著者が[REDACTED: substantial verbatim quotation; see Tier 9]と明示的に宣言することで、第一層（Table 1の実験結果）と第三層（Fig. 1の触媒サイクル）のVQ水準を意図的に分離している。第一層の主張は著者によってVQ-1（観察）のみを要求するものとして提示されており、第三層はVQ-3（機構）水準の仮説として提示されている。この構造は、VQ判定票において「論文が自己申告するVQ水準」と「現代基準でのVQ水準」が一致する珍しい事例を構成する。VQ判定の継承原則の下では、第一層はVQ-2にさえ未達（RI-01 Fatal）であるが、この未達は著者の設計意図（第三層の留保）とは別のレベル（報告完全性）に由来する。今後の判定票で「著者が意図的に機構を保留した論文」を扱う場合、「保留の明示」はRI-03のFatal判定を変更しない（意図的保留であることは機構的主張を弱めるが、VQ水準の達成要件は変わらない）という解釈を適用すること。

#### 4. EP辞書への新しいcase-specific実装例

**EP-03a（Direct-observation / state-assignment pack）のcase-specific実装例（Ru触媒C–H活性化系）**：
（1）低温³¹P{¹H} NMRによる環化金属中間体の観測プロトコル、（2）重水素化基質を用いたKIE測定によるC–H開裂律速の確認プロトコル、（3）Ru(0)活性化のための誘導期測定プロトコル——の三点を、第二世代Ru触媒C–H活性化論文に適用可能なEP-03aの実装例として辞書に追加する。これはKumadaやHeck系（Pd触媒）とは異なる金属・基質・検出手段の組合せであり、case-specific実装の多様性を拡張する。

#### 5. PRI候補の検出

**PRI-10（Kinetic overclaim）の確認的適用**：
SRG-3（B-8: run 10/11の速度差からring strain帰属）は、「動力学データ（速度定数、活性化パラメータ）なしに絶対的速度向上（ring strainが唯一の原因）を主張する」という構造を持つ。これはPRI-10（Kinetic overclaim、暫定コード）の定義に合致する。Monnereau 2009（先行確認）に続く2例目の確認事例として記録する。ただし、PRI-10の昇格条件（独立2報の確認）は本論文を含めて達成されるため、昇格判断の最終決定をStage 2Fまたは次回判定票の時点で行うことを推奨する。

**標識不整合（Labeling mismatch）の記録**：
本論文の"Possible mechanisms"節では、Fig. 1の触媒サイクルが"The reaction may begin with..."という仮説標識で開始されているが、直後の[REDACTED: substantial verbatim quotation; see Tier 9]では事実的記述語（"results in", "to give"）に遷移している。仮説標識が段落冒頭に集中し、その後の記述が事実的記述語に切り替わる「冒頭仮説・後続事実記述」パターンは、§6指定パターン（標識不整合）の事例として記録する。RI-06（Imported model）およびRI-03（Unobserved explanatory）と連動している。

**通信→Full Paper遷移の自動解消パターン**：
B-1（GC収率の一部不在）、B-2（TOF数値不在）、B-3（代替触媒比較の定量的条件不在）、B-4（"standard methods"への集約）は、いずれもNature Article 3ページ format の紙幅制約に起因する。これらのB項目は、Full Paper展開（通常の合成論文誌へのFollow-up論文）において自動的に解消される可能性が高い。Kakiuchi/Chatani グループの後続論文（1994–2000年代）がこの自動解消パターンを示す事例群として参照できる（外部推論：T3）。

---

以上、Murai et al. 1993の判定票を完了した。

inference_time_sec: not available — inject externally

---

> **Tier 8 redaction notice**: This file is a redacted copy of the corresponding Tier 3 / Tier 9 output. Verbatim source-paper quotations have been replaced by `[REDACTED: see source paper §<loc>; full text retained in Tier 9 reviewer-only deposit]` markers, preserving location references and our own analytical content. Bibliographic fields (title, authors, journal, year, DOI), analytical labels (`evidence_chain:` with B-/U-/A-/C- internal IDs), short technical terms, and our own analytical text are not redacted. The redaction was applied by `scripts/redact_for_tier8.py` and, for this version, by `scripts/build_paperA_R1_public.py` with `scripts/redact_source_ngram_runs.py` (scripts of the project repository; they are not deposited).
