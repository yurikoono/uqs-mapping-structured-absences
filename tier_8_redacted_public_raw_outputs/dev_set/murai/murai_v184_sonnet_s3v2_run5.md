prompt_version: stage3-v2-20260416
model_info: claude-sonnet-4-6

# 科学的知見の再認定判定票

## Murai et al. 1993（Nature, vol. 366, pp. 529–531, communication）

---

### §1 Claim Architecture

**コア主張の要約：**

本論文のコア主張は、RuH2(CO)(PPh3)3を前触媒とするキレーション補助型C–H/オレフィンカップリング反応が、従来のC–H官能基化反応を凌駕する効率性・選択性・汎用性を達成したというものである。Novelty柱は「触媒的条件下でのアリールケトン芳香族C–H結合とオレフィンの直接カップリング（初例）」であり、Utility柱は「実用有機合成に要求される効率・選択性・汎用性の同時達成」である。機構的根拠としてキレーション補助（chelation assistance）概念が前面に出されているが、論文自身が「[REDACTED: verbatim source text; see the source paper via its DOI]」と機構的確認を明示的に保留している点が、主張構造の核心的張力となっている。

**Layered structure の判定：**

主張は独立した四層構造を持ち、単一の反証では全主張が崩れない設計になっている。第一層（効率性：定量的収率・高TOF）は最も実験的に検証可能であるが、GC収率の定量的基盤の不備（B-1）とTOF数値の不在（B-2）により独立評価ができない弱点を持つ。第二層（選択性：virtually 100%の位置選択性）は非観測異性体の探索実験が不在であり（U-4、B-10）、「virtually」という留保語が量的根拠なしに使用されている。第三層（汎用性：「a variety of aromatic systems」）はデータが全て芳香族ケトンに限定されており（U-3、B-5）、抽象の主張がデータを超過するという内部矛盾を抱える。第四層（戦略的汎化性：キレーション補助の一般的適用可能性）は機構的実証なしに提案されており（A-1、U-1、U-2）、先行研究との機構的非対称性が補強の妥当性を弱めている（B-11、C-2）。第一層が崩れても第三・第四層は独立して残存し、第三層が否定されても第四層の戦略的主張は存続し得る設計である。ただし機構の中核である環状金属化中間体（SRG-2）が実験的に確認されれば、第二・第四層が一括して補強されるという依存関係がある。

---

### §2 SRG / CLA → RI / ER / EP Crosswalk

**SRG-1 [定量的証拠基盤]**（B-1, B-2, B-3, B-4）

* **Primary RI**: RI-01 [Reporting integrity] — 測定フレーム（GC収率の較正基準、TOF定義・算出根拠、触媒比較の条件）が統一されず横比較不能。
* **Secondary RI**: RI-05 [Qualitative overread] — 定量的数値なしに「最高水準のTOF」「equally effective」等の量的序列を主張。
* **ER**: 収率報告は内部標準・応答係数を明示したGC較正曲線に基づく数値を要し、TOF主張は触媒活性種のモル数定義・測定時間・参照文献値の三点セットを必要とする。B-3の触媒比較には基質・条件・収率の数値記述が必要。
* **EP**: EP-01a [Reporting-coherence pack]; EP-08a [Replication / uncertainty pack]
* **Case-specific実装**: アセトフェノン/triethoxyvinylsilane系（run 9またはrun 10）を基準run として、(i) GC較正：既知量のn-テトラデカン内部標準を用いた応答係数の事前決定、(ii) TOF算出：30分・1時間・2時間の時点別サンプリングによる初期速度プロファイル、(iii) 代替触媒比較：同一基質・同条件での数値収率の並列報告。
* **注記**: B-1（V1=high, V3=high; convergence 2/3）、B-2（V1=high, V3=high; convergence 2/3）はhigh_convergence_low_gapに分類される高収束項目。B-3（V1=medium, V2=medium, V3=medium; convergence 3/3）は三エージェント完全収束。B-4は記述制約によるフォールバック。

---

**SRG-2 [触媒サイクルの直接証拠不在]**（A-1, U-1, U-2）

* **Primary RI**: RI-03 [Unobserved explanatory] — 反応の選択性決定種として提案されている環状金属化中間体（Fig. 1）が、直接観測も速度論的拘束も受けていない。
* **Secondary RI**: RI-06 [Imported model] — Fig. 1のRu(0)酸化的付加機構を、Mn(I)求電子的経路（ref 14）およびRu(II)カルボキシレート条件（ref 15）という機構的に非対称な先行研究から構成（サイクルレベル輸入）。
* **ER**: 提案触媒サイクルにおける律速中間体は、少なくとも化学量論的単離または原位置分光観察（31P{1H} NMRまたはX線構造）によって同定されなければならない。前触媒Ru(II)からRu(0)活性種への変換機構は、誘導期間測定またはRu(0)源直接投入による対照実験で検証を要する。
* **EP**: EP-03a [Direct-observation / state-assignment pack]; EP-06a [Analogy-validation pack]
* **Case-specific実装**: (i) 化学量論的条件（1当量のアセトフェノン + 1当量のRuH2(CO)(PPh3)3、トルエン、60–80°C）での31P{1H} NMR追跡による環状金属化中間体の観察または同定、(ii) 聚合的なRu3(CO)12やRu(CO)2(PPh3)3等の形式的Ru(0)源を前触媒として用いた触媒実験との比較（「not effective」報告との整合性確認）、(iii) 重水素化アセトフェノン（d5またはortho-d）を用いた動力学的同位体効果（kH/kD）の測定によるC–H切断の律速ステップ同定。
* **注記**: U-1（V2=critical, V3=critical; convergence 2/3）はhigh_convergence_low_gapの最高温度項目。A-1は「機構不明の明示的保留」であり、論文テキスト上はT1（事実的記述）として機能しつつも、U-1・U-2と連動してself-contradictory absence構造を形成する。SRG-2の解消はVQ-3到達の必要条件。

---

**SRG-3 [選択性根拠の不在]**（B-8, B-9, B-10, U-4）

* **Primary RI**: RI-04 [Unreplicated discriminator] — run 10対run 11の反応速度差（0.5 h / 100% vs. 20 h / 88%）という単一比較データから、電子的・立体的・溶解性要因を排除せずに環ひずみに速度差を帰属。1-インダノン不反応という単一の否定的結果を機構的証拠として使用。
* **Secondary RI**: RI-07 [Unsupported boundary] — 非観測の位置異性体3種について失敗例確認なしに「virtually 100%」という境界主張。
* **ER**: 速度論的比較は速度定数または半減期として数値化し、電子的・立体的・溶解性要因の対照実験によって速度差の原因を同定することを要する。位置選択性の主張は、GC/NMRにより非観測異性体を定義された検出限界以下と確認する実験を必要とする。
* **EP**: EP-04a [Discrimination / replication pack]; EP-07a [Boundary-test pack]
* **Case-specific実装**: (i) run 10（6員環メタラサイクル形成可能基質）とrun 11（6員環とは環ひずみが異なる7員環基質）について時間対収率プロファイル（0.1 h, 0.3 h, 0.5 h, 1 h, 3 h, 5 h）を測定し初期速度定数を比較、(ii) 同等の電子密度・立体構造を持つが環ひずみが異なる一連の基質（例：4員環ケトン・5員環ケトン・6員環ケトン）での速度比較、(iii) triethoxyvinylsilaneカップリング生成物のGCによる全異性体サーベイ（検出限界：GC面積比で0.5%以下を示すこと）、(iv) 1-インダノン不反応の定量的確認（GC収率0.1%以下の検出限界での追跡）。
* **注記**: B-8・B-9はhigh_convergence_low_gap（V1=medium, V2=high; convergence 2/3; gap: low）。U-4はmediun severity、B-10と連動。SRG-3のうちRI-07（境界主張）はEP-07aで解消するが、RI-04（速度論的根拠）はEP-04aと連動する実験セットが必要。

---

**SRG-4 [スコープ主張がデータを超過]**（B-5, U-3, B-7）

* **Primary RI**: RI-07 [Unsupported boundary] — 全データがアリールケトン系に限定されるにもかかわらず、「a variety of aromatic systems」という境界を未検証で設定し、「almost quantitative yields based on both starting materials」という双方向定量主張がオレフィン消費の追跡なしに行われている。
* **Secondary RI**: RI-05 [Qualitative overread] — 特定の基質群の結果から、定量的根拠なく汎用的スコープを推論。
* **ER**: 「a variety of aromatic systems」の主張は、少なくとも非カルボニル配向基系（例：エステル・アミド・イミン）での実験試行と結果（適用可能・不可能の何れかのデータ）を必要とする。「両基質に対して定量的」の主張はオレフィンの収支（消費量、異性化・オリゴマー化副生成物）の追跡を要する。
* **EP**: EP-07a [Boundary-test pack]; EP-01a [Reporting-coherence pack]
* **Case-specific実装**: (i) アセトフェノン（ケトン）とエチルベンゾエート（エステル）・ベンズアルデヒド（アルデヒド）・N,N-ジメチルベンズアミド（アミド）のtriethoxyvinylsilaneとの反応を並行実施し、収率を同一条件で比較、(ii) run 8–13の標準条件でのオレフィン消費をGC追跡し、未反応オレフィン・異性化体・オリゴマーを定量して質量バランスを閉じること、(iii) triethoxyvinylsilaneの加水分解副生成物を明示的に追跡する（Si–O結合切断検出）。
* **注記**: U-3はhigh severity self-contradictory absence（V1-Q12; single-agent）。B-5はB/Uの両分類を受ける「mixed」項目。B-7はフォールバック規則(c)経由で生成。SRG-4の解消はVQ-2（Method）のRI-07クリアに必要。

---

**SRG-5 [先行技術との数値比較不在]**（C-1, B-2）

* **Primary RI**: RI-09 [External superiority] — refs 11（Jordan & Taylor）およびref 12（Moore et al.）のTON/TOF/収率に対して数値直接比較なしに「最高水準」「前例なし」を主張。
* **Secondary RI**: RI-08 [Unquantified reliability] — TOF主張に反復測定・不確かさ記述がない。
* **ER**: 「最高水準のTOF」という比較的優位主張は、共通基質系または近似基質での参照文献値を数値として引用し、本論文の算出TOF値と直接比較することを要する。
* **EP**: EP-09a [Internal benchmark pack]; EP-08a [Replication / uncertainty pack]
* **Case-specific実装**: (i) refs 11/12のTON・TOF・収率・基質条件を抽出し、本論文のruns 1, 9, 10と最近接比較可能な条件で数値並列表示、(ii) runs 9または10の反応を少なくとも3回独立に繰り返し、GC収率の平均・標準偏差を記録。
* **注記**: B-2（V1=high, V3=high; convergence 2/3）はhigh_convergence_low_gap。C-1はSRG-5の構造的対（severed referenceとして記録）。SRG-5の解消はVQ-4（Benchmark）の必要条件。

---

**SRG外：CLA**

**CLA-1 [前触媒活性化の自己矛盾的不在]**

* grounded_in: U-2（D-4-2の根拠）
* **Primary RI**: RI-03 [Unobserved explanatory]（サブタイプ：self-contradictory absence — 触媒サイクルが予測するRu(0)活性種の生成が、前触媒Ru(II)のどの条件でどのように生成するかについて観測も提案も不在）
* **ER**: Ru(II)→Ru(0)変換の活性化機構（例：H2還元的脱離）を、誘導期間測定または31P{1H} NMRの反応初期追跡によって検証することを要する。
* **EP**: EP-03a [Direct-observation / state-assignment pack]
* **Case-specific実装**: RuH2(CO)(PPh3)3の熱分解（トルエン還流）における31P{1H} NMRのリアルタイム追跡、H2発生の気相GC確認、誘導期間の有無（run 9の0.5 h完全転化は誘導期間なしか、それとも誘導期間0.1 h未満か）の検証。
* **注記**: SRG-2のA-1・U-1と密接に連動するが、「前触媒活性化」という固有の問いはSRGのいずれのmember_itemsにも明示的に収まらないため、CLA-1として独立記録。U-2を直接根拠とする。

---

**CLA-2 [先行文献引用の機構的非対称性]**

* grounded_in: B-11, C-2, C-4, C-5（D-4-7の根拠）
* **Primary RI**: RI-06 [Imported model]（スコープ注記：サイクルレベル輸入 — Mn(I)求電子的経路・Ru(II)カルボキシレート経路・オレフィン酸化的付加経路という機構的に異質な3系統を単一の触媒サイクル支持証拠として輸入）
* **Secondary RI**: RI-05 [Qualitative overread] — 「products similar to the intermediate postulated in Fig. 1」という定性的類似性から、機構的同型性を推論。
* **ER**: 引用先行研究の反応機構が提案機構と同型であることを、酸化状態・配位子環境・活性化モードの3軸で明示的に議論することを要する。機構的に非同型の先行研究を引用する場合は、異なる機構にもかかわらず中間体の構造的類似性が支持証拠となる論理を示さなければならない。
* **EP**: EP-06a [Analogy-validation pack]
* **Case-specific実装**: refs 14（Mn(I)/CH3Mn(CO)5）、ref 15（Ru(II)カルボキシレート）、ref 17（オレフィン/Ru OA）それぞれについて、酸化状態変化・配位子の役割・C–H切断モードを3行の比較表として記述し、提案Ru(0)/OA経路との異同を明示。
* **注記**: B-11はmixed（intentional_narrowing + methodological_limitation）。B-11 ↔ C-2 ↔ C-5はSTAGE 1のlinked_itemsとして記録済。CLA-2はSRG-2（RI-06 Secondaryとして記録）と連動するが、引用実践の問題として独立した制度的価値を持つためCLAに記録。

---

### §3 現在のVQ判定

**現在判定: VQ-2 (Method) — Qualified**

**VQ-1 [Observation] の判定：通過（条件付き）**

RI-02（生成物・触媒の構造・純度が代替候補を排除できる粒度で未確定）について：論文はB-4（「standard methods」）により全13生成物の構造確定を主張する。Nature 1993年の通信形式では分光データの個別掲載が紙面上困難であり、当時の標準的ジャーナル慣行の範囲内にある。Ru前触媒RuH2(CO)(PPh3)3はref 13から調製され、構造既知の化合物である。RI-02は当時の文脈では非致命的と判定する。ただしB-4は**era-norm依存**であり、現代基準では個別スペクトルデータの補足資料提出が求められる（§4参照）。

**VQ-1 [Observation] はNon-fatalなRI-02を条件に通過する。** ただしこの通過はera-normに依存しており、現代基準での再審では条件が強化される。

**VQ-2 [Method] の判定：通過（Qualified — RI-05が重大に残存）**

VQ-2の必須要件RI-01およびRI-07について：

- **RI-01（Reporting integrity）**: SRG-1が示す通り、GC収率の較正基準（B-1）・TOF定義（B-2）・触媒比較条件（B-3）のいずれも未充足。ただし当時のNature通信形式での紙面制約を考慮すると、これらはcommunication-era tolerated（§4参照）に分類される。このRI-01の残存は、発表時点での「非致命的」扱いが可能だが、現代再認定においては致命的に転化する。
- **RI-07（Unsupported boundary）**: SRG-4・SRG-3で示した通り、スコープ主張（「a variety of aromatic systems」）および選択性境界（「virtually 100%」）がいずれもデータなしに主張されている。ただしSRG-4は通信形式の制約内でも試みることができた最小限の対照実験を欠いており、完全なcommunication-era tolerationを認めにくい。

**RI-05（Qualitative overread）が重大に残存する（SRG-1, SRG-3, SRG-5に共通）ため、VQ-2は「限定的（Qualified）」とする。**

VQ-2はVQ-1継承を前提として成立する。ただしRI-01のcommunication-era tolerationが「現代基準では致命的」と反転する点を明記する。

**VQ-3 [Mechanism] の判定：未達**

VQ-3の必須要件であるRI-03・RI-04・RI-06が、いずれも解消されていない：

- **RI-03**: SRG-2（A-1, U-1, U-2）が示す通り、触媒サイクルの律速中間体（環状金属化中間体）は直接観測されておらず、前触媒活性化機構（CLA-1）も未観測。自己矛盾的不在（self-contradictory absence）として最高温度の未解消項目。**Fatal**：VQ-3の機構主張が原理的に不成立。
- **RI-04**: SRG-3（B-8, B-9）の速度論的帰属が単一比較データに依拠し、代替要因排除なし。Non-fatal（機構主張の根底を覆さないが弱体化する）。
- **RI-06**: SRG-2（B-11/CLA-2）の機構的サイクルレベル輸入が解消されていない。CLA-2との連動でFatalに準ずる。

**VQ-3 [Mechanism] は未達：RI-03がFatalとして残存するため、機構主張の水準での知見認定は現時点で成立しない。**

ただし **効率性の実証（層別非対称性）** — 第一層（13例の基質スコープ実証、定量的収率の記述、芳香族ケトン/オレフィン系での反応性実証）については：「反応が起きる」という観察レベルの主張はVQ-1到達の範囲にある。「高収率・高選択性を同時達成する」という第二・三層はVQ-2 Qualifiedの状態。機構層（第四層）はVQ-3未達。層別VQ非対称性：**観察実証層（層1）→ VQ-1、実用性実証層（層2/3）→ VQ-2 Qualified、機構・汎化性層（層4）→ VQ-3未達**。

**VQ-4 [Benchmark] の判定：未達**

VQ-4の必須要件RI-08（反復測定・不確かさ記述）およびRI-09（直接数値比較）が未解消（SRG-5）。VQ-3未達であるため、継承原則上VQ-4も未達。

---

### §4 Era-Norm Annotation

**communication-era tolerated（当時の通信形式で許容される欠落）：**

- **B-1**（GC収率の内部標準・応答係数不在）：1993年Nature通信の3ページ紙面では較正手順の詳細記述は慣行上省略が許容されており、GC収率の報告自体はjournal convention内。
- **B-2**（TOF数値の不記載）：TOF算出値を表に収録しない形式はNature短報の通常実践であり、「among the highest」という比較主張も参照文献の定性的評価として当時の通信形式内。
- **B-3**（触媒比較の定性的記述）：探索的な触媒評価の定性結果（effective/not effective）をmain textに埋め込む形式は1993年の通信形式として許容範囲内。
- **B-4**（「standard methods」による構造確定）：1993年のNature通信では補足資料制度が未整備であり、「standard methods」という省略記述は当時の誌面慣行として通常。
- **B-6**（runs 5, 6の触媒担持量の不連続性）：試行錯誤的な条件探索過程の断片的記録として短報ではしばしば見られる。
- **B-9**（「not shown」否定的結果）：短報で全データを掲載できない際に「not shown」と注記する実践は1993年の通信慣行として許容範囲内。

**modern-era deficient（現代再認定では許容できない欠落）：**

- **B-1**（GC収率の定量的基盤不在）：現代の再現性・データ共有基準（FAIR原則、Nature Research Reporting Checklist等）では、GC定量の較正手順・内部標準・応答係数の記述または補足資料掲載が必須。収率の独立検証を不可能にする点でmodern-era deficientに転化。
- **B-2**（TOF数値の不記載）：現代の触媒性能評価では、TOFまたはTONの数値算出と参照文献値との直接数値比較（表形式）が要求される。「among the highest」という定性的最優秀主張のみでは現代の査読を通過しない。
- **U-1**（環状金属化中間体の直接観測不在）：現代の機構研究基準では、提案中間体の少なくとも間接的証拠（速度論的同位体効果、原位置NMR、計算化学的エネルギープロファイル）が期待される。これは1993年でも議論可能であったが現代ではより強く要求される。
- **U-2**（Ru(II)→Ru(0)活性化機構の不在）：現代の触媒サイクル論文では、前触媒活性化の確認（インダクション期間・活性種同定）が要求される。
- **B-7**（オレフィン消費の追跡不在）：「both starting materials」に基づく定量的収率主張に対し、現代では質量バランスの閉鎖が必須要件とみなされる。
- **B-10 / U-4**（位置選択性の検出限界記述不在）：現代の選択性主張では、非観測異性体の探索と定量的な検出限界（例：GC面積比<0.5%）の明示が要求される。

**両タグ該当項目（当時は許容・現代は不足）：**

B-1, B-2, B-4はcommunication-era toleratedとmodern-era deficientの両方に該当する。当時の紙面制約内での省略として許容されたが、現代の再現性・データ透明性基準ではこれらの不在が独立検証を妨げるとして致命的に転化する。

---

### §5 最短補強ルート

**第一目的関数：VQ-3（Mechanism）到達**

VQ-3到達に必要な必須RI解消：RI-03（Primary）、RI-04（Secondary）、RI-06（Secondary）

**VQ-3 への最短ルート：**

1. **EP-03a [Direct-observation / state-assignment pack]** — RuH2(CO)(PPh3)3とアセトフェノンの化学量論的条件でのトルエン加熱において、31P{1H} NMRによる環状金属化中間体の原位置観察または単離同定を実施。RI-03（SRG-2, CLA-1）を直接前進させる最大情報利得の実験。RI-03 (Fatal) を解消する唯一の経路。

2. **EP-06a [Analogy-validation pack]** — refs 14（Mn系）、ref 15（Ru(II)カルボキシレート系）、ref 17（オレフィンOA）と提案Ru(0)/OA機構の機構的同型性を酸化状態・配位子環境・C–H切断モードの3軸で対照比較し、文献援用の妥当性を明示的に議論。RI-06（CLA-2）を前進させる。

3. **EP-04a [Discrimination / replication pack]** — run 10対run 11の初期速度定数を時間対収率プロファイルから算出し、電子的・立体的対照実験（環ひずみが系統的に異なる基質系列）で環ひずみ帰属を検証。RI-04（SRG-3）を前進させる。

認定ゲート順注記：実験投入順は情報利得順（EP-03a → EP-06a → EP-04a）だが、最終的なVQ認定はVQ-1 → VQ-2 → VQ-3 → VQ-4のゲート順で確定する。EP-03aが先に投入されても、VQ-2（RI-01, RI-07解消）が確定していない状態ではVQ-3として認定されない。したがって実際の補強順は：**SRG-1解消（RI-01のFull Paper展開またはSupplementary Material記述）→ SRG-4解消（RI-07の対照基質実験）→ EP-03a（RI-03解消）→ EP-06a（RI-06解消）→ EP-04a（RI-04解消）** の順でゲートが開く。

**第二目的関数：VQ-4（Benchmark）到達**（VQ-3が前提）

**VQ-4 への補強ルート：**

4. **EP-09a [Internal benchmark pack]** — refs 11（Jordan & Taylor, TON/TOFデータ）、ref 12（Moore et al., 収率・基質条件）の数値を文献から抽出し、本論文のruns 1, 9, 10と近似基質条件での並列数値比較表を作成。RI-09（SRG-5）を前進させる。

5. **EP-08a [Replication / uncertainty pack]** — runs 9–11について独立3回繰り返し実験を実施し、GC収率の平均・標準偏差を記録。RI-08（SRG-5 Secondary）を解消する。

認定ゲート順注記：VQ-4の認定はVQ-3継承を前提とする。EP-09a + EP-08aを実施してもVQ-3が未達のままではVQ-4認定は成立しない。

---

### §6 制度設計への寄与

**1. 既存RIコードの代表事例**

**RI-06（Imported model）のサイクルレベル輸入事例として価値が高い：** 本論文は個別の素反応ステップの類推（例：「Rh系でのC–H酸化的付加をRuに類推する」）ではなく、Mn(I)求電子的経路・Ru(II)カルボキシレート経路・オレフィン酸化的付加という機構的に異質な3系統を組み合わせて、Ru(0)/OA型の触媒サイクル全体を構成している。これはRI-06 v0.2aスコープ注記「サイクルレベル輸入」の最も明瞭な事例の一つであり、Codebookに代表事例として追加する価値がある。

**RI-07（Unsupported boundary）の「mixed B/U」判定事例：** SRG-4のU-3は同一の記述が「B-5」（mixed: intentional_narrowing + methodological_limitation）と「U-3」（self-contradictory absence）の二重分類を受ける。「abstract scope claim」と「data-constrained reality」の乖離という構造は、RI-07の「否定的境界主張の拡張適用」ケースとして記録に値する。

**2. 標識不整合（Labeling mismatch）の検出**

本論文のMechanism節における標識不整合パターン：論文はA-1で「[REDACTED: verbatim source text; see the source paper via its DOI]」と明示的に保留しながら、直後に「[REDACTED: verbatim source text; see the source paper via its DOI]」という仮説標識を使用する。しかし続く「[REDACTED: verbatim source text; see the source paper via its DOI]」では事実的記述語（"results in", "to give"）に切り替わり、Fig. 1は仮説的中間体を確定構造として描く。この標識不整合は**仮説を事実に転換する語法の漸進的移行**として現れており、RI-06と連動している。仮説標識の位置は「may begin with」という1文目に集約されているが、後続の記述が事実語を使用することで仮説的性格が希薄化するパターンは、§6の制度的記録として有用。

**3. 通信→Full Paper遷移の自動解消パターン**

SRG-1（B-1, B-2, B-3, B-4）のRI-01的問題は、対応するフルペーパー展開（例：Chatani/Kakiuchiグループの後続論文）において、GCの詳細条件・TOF算出値・触媒スクリーニングデータが記載されることで自動的に解消される可能性が高い。これは「通信→Full Paper遷移の自動解消パターン」の典型事例であり、§4のEra-Norm Annotationで記録したcommunication-era toleratedとの対応が明確。VQ昇格のためには通信論文単独での評価よりも、後続フルペーパーとの連動評価が有効であることを示す事例として記録する。

**4. RI共起パターン：RI-03 + RI-06の必須共起**

SRG-2において、RI-03（Unobserved explanatory）とRI-06（Imported model）が共起しており、いずれか一方の解消だけでは不十分である。RI-03を解消（中間体の直接観測）しても、その中間体がMn系・Ru(II)系の先例と同一機構で生成するかが問われ（RI-06）、逆にRI-06を解消（機構的同型性の議論）しても中間体が直接確認されなければ（RI-03）、機構主張はVQ-3に達しない。この「RI-03 + RI-06の必須共起」パターンは、Codebook v0.2aの「RI共起パターン」記述に追加すべき事例である。

**5. 否定的証拠の不完全性パターン（SRG-3）**

B-9（1-インダノン不反応）はRI-04の「否定的証拠の不完全性」として典型的な事例を提供する。「did not react at all」という陰性結果を機構的証拠（環ひずみ仮説の支持）として使用する際に、(a) 質量収支の閉鎖（1-インダノンの回収率確認）、(b) 速度論的ウィンドウ評価（検出下限の明示）、(c) 代替要因排除（立体・電子効果の対照）がいずれも欠如している。§6の制度的記述「否定的証拠の不完全性」の代表事例として本論文のB-9を記録する。

**6. PRI候補の評価**

**PRI-11（Mechanism-kinetics decoupling）の適用可能性：** 本論文はB-8・B-9での速度論的帰属において、提案触媒サイクルから速度式を代数的に導出することなく観測速度差（run 10 vs. run 11の反応時間比較）を機構的解釈に使用している。ただし本論文のMechanismセクションが速度次数の測定を報告していないため、厳密には「速度式との一致のみで機構を支持」という構造を完全に満たさない（速度次数自体が測定されていない）。本事例はPRI-11の「速度論データ不在での機構的帰属」という弱形として記録するが、昇格のためのトリガーは「速度次数を測定した上でサイクルから導出された速度式と照合しない」事例の追加確認が必要。

本ケースは既存制度設計を追加確認しつつ、RI-06サイクルレベル輸入・標識不整合パターン・RI-03+RI-06必須共起・否定的証拠の不完全性の4点について、Codebook収録に値する新しい代表事例を提供した。
