```
prompt_version: stage3-v1-20260402
model_info: claude-sonnet-4-6

# 科学的知見の再認定判定票

## Race, Faulkner, Shaw, Bower 2016（Chemical Science Edge Article）

---

### §1 Claim Architecture

**コア主張:**
本論文のNovelty柱は「Pd触媒によるオキシムエステルの環化において、配位子の電子性のみの選択によって反応機構が離散的に切り替わる（電子欠乏ホスフィン → 協奏的2e酸化的付加/aza-Heck; 電子豊富ホスフィン → SET/イミニルラジカル経路）」というPd触媒化学において前例のない機構二分岐の発見である。Utility柱は「高価な活性化基・毒性試薬・UV照射を不要とする実用的なイミニルラジカル環化プロトコルを提供する」という合成的有用性の主張である。両主張は独立して成立し得るが、前者がより直接的な証拠を要する。

**Layered structure:** 3層構造を持ち、部分的に独立している。
- Layer 1（合成的）: 電子豊富Pd系はイミニルラジカル生成物5aを与える（配位子最適化表および6基質スコープで実証）。この層は「生成物が得られる」という観察であり、機構的帰属なしに成立し得る。
- Layer 2（機構的）: 4つの独立した探針（TEMPO捕捉・Newcomb時計プローブ・重水素標識・エストロン立体反転）がラジカル経路と一致する。この層はLayer 1を支えるが、各探針は間接的であり、探針の多重性が直接観測の代替にはならない。
- Layer 3（概念的）: 「配位子の電子性のみ」によるPd触媒での2e/1e機構切り替えは前例がない。この層はLayer 1/2の結果から論理的に独立しており、Layer 1/2への反証がLayer 3を崩さない。

単一の反証（例：Newcomb実験の再現失敗）はLayer 2のみに影響し、Layer 3の概念的主張（機構の可能性としての存在）を崩さない。逆に、Layer 3（「solely by ligand」主張）の不成立はLayer 1/2を否定しない。この独立性が審査の難度を規定する。

---

### §2 SRG / CLA → RI / ER / EP Crosswalk

---

**SRG-1「全機構実験でのマスバランス体系的不在」**（member: B-1, B-3, B-4, B-5, A-1）

* **Primary RI**: RI-01 [Reporting integrity] — 測定フレームの不統一（「唯一の観測可能生成物」と25%収率の併記）と質量収支の体系的欠如により、各機構探針実験の信頼性を横断的に比較できない
* **Secondary RI**: RI-04 [Unreplicated discriminator] — Newcomb時計プローブ（25%収率、未同定75%）はラジカル経路の単一かつ不完全な識別子として機構的主張を担っている
* **ER**: 各機構探針実験において、基質の定量的回収（生成物、副生成物、回収出発物質の合計）が記録されていること。25%という低収率の時計反応では、時計反応の支配的経路としての解釈が可能かどうかを質量収支によって示す必要がある。
* **EP**: EP-01a [Reporting-coherence pack]; EP-04a [Discrimination/replication pack]
* **Case-specific実装**: Newcomb実験（Scheme 3A）の反応混合物をGCおよび1H NMRによって網羅的に分析し、環化生成物10・未反応7a・β開裂生成物・二量体等の全成分を定量する。TEMPO捕捉実験（Scheme 2A）・エストロン実験（Scheme 4）についても同様に全成分収支を報告する。
* **注記**: TEMPERATURE_SUMMARY high_convergence_low_gap: B-3 (V1=high, V2=high, V3=high; convergence 3/3; gap=none) が最高収束項目。B-1 (2/3, low gap), B-5 (2/3, none gap)も2剤収束。

---

**SRG-2「非Pd・非ラジカル経路を排除する対照実験の不在」**（member: B-2, U-2）

* **Primary RI**: RI-07 [Unsupported boundary] — 「Pd(0)によるSETがイミニルラジカルを生成する」という特定的機構帰属は、Pd触媒なし（熱/塩基のみ）での環化が起こらないことを示すPdフリー対照実験なしには「Pd不要条件では反応しない」という境界を主張できない
* **Secondary RI**: RI-03 [Unobserved explanatory] — N–O均一開裂のPd媒介性は直接観測も速度論的拘束もなしに仮定されている
* **ER**: (1) Pd源を除いた条件下（塩基+DMF+熱のみ）での基質の挙動が記録されていること; (2) TEMPOがPd(0)を酸化することへの対照実験が提示されること
* **EP**: EP-07a [Boundary-test pack]
* **Case-specific実装**: 基質1aを用いて、(dt-bpf)PdCl₂なし・Et₃N (400 mol%)・DMF・70°C・γ-テルピネンあり/なしの条件で反応を試みる。生成物5a・3aの収率および未反応出発物質を定量する。
* **注記**: U-2はself-contradictory absence (high severity, V3=high, convergence 1/3)。TEMPO実験のB-2は2/3収束 (V1=medium, V2=high; gap=low)。

---

**SRG-3「ラジカル素反応の速度定数データの不在」**（member: A-5, B-11, C-5）

* **Primary RI**: RI-03 [Unobserved explanatory] — 「5-exo環化がN-Pd再結合より速い」という機構的主張を支える速度定数は、Newcombのシクロプロピルカルビニルクロックのrate constant（〜10⁸ s⁻¹; refs 19a-19b）を適用すれば原理的に抽出可能であるが、抽出されていない
* **Secondary RI**: RI-05 [Qualitative overread] — 「速い5-exo環化」は生成物分布の定性的観察から速度論的含意を引き出す論法
* **ER**: Newcomb時計反応の温度および溶媒条件下でのβ開裂速度定数を引用し、実験条件下での環化速度定数の下限（または再結合の上限）を計算によって示すこと
* **EP**: EP-03a [Direct-observation/state-assignment pack]
* **Case-specific実装**: 既知のシクロプロピルカルビニルラジカル開環速度定数（Newcomb, 70–90°C, DMF中での温度補正値）を用いて、実験で観測された生成物10の選択性から「環化がどの程度の速さであれば生成物分布が成立するか」を計算報告する。可能であれば、γ-テルピネン存在下・非存在下での比較から再結合速度定数の上限を推定する。
* **注記**: A-5はhigh_convergence_low_gap (V1=high, V2=critical; convergence 2/3; gap=low)。C-5はDropped Quantitative Benchmarkとして記録。

---

**SRG-4「配位子制御SETスイッチの熱力学的・電子論的基盤の不在」**（member: A-5, A-6, A-7, B-10, U-1）

* **Primary RI**: RI-03 [Unobserved explanatory] — SET機構の核心的媒介変数（Pd(0)/配位子錯体の酸化電位、オキシムエステルN–O結合の還元電位）が直接観測・報告されておらず、「電子豊富配位子 → SET有利」という因果関係に熱力学的根拠がない
* **Secondary RI**: RI-05 [Qualitative overread] — 配位子を「電子豊富」「電子欠乏」という定性的二値分類から機構的離散切り替えを推論している; 連続的な電子パラメータ（Tolman電子パラメータ等）との定量的相関は示されていない
* **ER**: (1) 代表的な電子豊富配位子（dt-bpf, P(t-Bu)₃, PCy₃）と電子欠乏配位子（P(3,5-(CF₃)₂C₆H₃)₃）を持つPd(0)錯体の酸化電位（CVによる）; (2) O-ピバロイルオキシムエステルのN–O結合還元電位を測定し、ΔG_SET < 0を熱力学的に実証すること
* **EP**: EP-03a [Direct-observation/state-assignment pack]; EP-05a [Quantitative-ranking substantiation pack]
* **Case-specific実装**: CH₂Cl₂/Bu₄NPF₆中でのサイクリックボルタンメトリー: (dt-bpf)Pd(0)錯体、(P(t-Bu)₃)Pd(0)錯体の酸化電位を測定; O-ピバロイルオキシムエステルN–O結合の還元電位をCVまたはCVとDFTの組み合わせで推定; ΔG_SET = F(E_ox(Pd) − E_red(N-O))を計算してSETの熱力学的実行可能性を実証する。
* **注記**: U-1はself-contradictory absence (high severity); B-10はreporting_omission (V2=high, convergence 1/3); B-10↔U-1がlinked_items。SRG-4がD-4候補の最大グループ（5項目）。

---

**SRG-5「Scheme 5機構ステップの実験的未検証」**（member: A-4, A-7, U-3）

* **Primary RI**: RI-03 [Unobserved explanatory] — 触媒サイクルの閉環ステップ（γ-テルピネンからPd(I)へのHAT → p-シメン生成 → Pd(II)-ヒドリド → 塩基誘起還元的脱離）において、いずれの中間体・副生物も検出・確認されていない
* **ER**: 触媒量条件下でのγ-テルピネン消費量（1H NMRによる時間経過）とp-シメン生成量（GC-MSによる定量）が記録されていること; Pd(II)-ヒドリドの速度論的捕捉または直接NMR観測がなされていること
* **EP**: EP-03a [Direct-observation/state-assignment pack]
* **Case-specific実装**: 触媒量(dt-bpf)PdCl₂/5 mol%、γ-テルピネン400 mol%条件で、基質1aの反応を一定時間間隔でサンプリングし、GC-MS（標準p-シメンとの比較）によりp-シメンを定量する; 1H NMR積分によりγ-テルピネンの消費量を追跡し、化学量論的生成が触媒回転数と一致するかを確認する。
* **注記**: U-3はself-contradictory absence (medium severity); A-4はV1/V2それぞれmedium, convergence 1/3。A-4↔U-3はpriority_structureのピボット2。

---

**SRG-6「機構スイッチの配位子帰属を曖昧にする実験デザイン上の交絡」**（member: B-6, B-15, B-16）

* **Primary RI**: RI-07 [Unsupported boundary] — 「solely by choice of phosphine ligand」という排他的帰属主張は、ラジカル条件と標準aza-Heck条件が温度・Pd源・基質活性化基・溶媒添加剤の複数変数で同時に異なる条件比較から導かれており、配位子のみが変数の実験が存在しない
* **Secondary RI**: RI-05 [Qualitative overread] — 複数変数の同時変化を「配位子のみの効果」として解釈する因果的過読
* **ER**: 同一基質・同一温度・同一溶媒条件下で配位子のみを変えた対照実験（matched-pair control）が実施されていること; 温度効果の独立評価（電子豊富配位子で60°C vs 70°Cの両条件）が報告されていること
* **EP**: EP-07a [Boundary-test pack]
* **Case-specific実装**: 基質1b（O-ピバロイル）、DMF、70°C、Et₃N 400 mol%を固定し、(dt-bpf)PdCl₂とPd₂(dba)₃/P(3,5-(CF₃)₂C₆H₃)₃を並列実施する; 次に温度を60°Cに下げた同条件も実施し、配位子効果と温度効果の分離を示す。
* **注記**: B-6、B-15はconvergence 2/3 (V1=medium, V3=medium; gap=none)。B-16はV3=medium, convergence 1/3。SRG-6はD-4-4の核心グループ（OI-008対応）。

---

**SRG外：CLA**

---

**CLA-1: 電子豊富配位子クラス内の収率不均一性**（grounded_in: B-7, A-6）

* **Primary RI**: RI-05 [Qualitative overread] — 「電子豊富配位子では一般的にラジカル経路が促進される」という記述は、実際の収率がS-Phos 10%からdt-bpf/γ-テルピネン 88%と5倍以上変動する事実に対して定性的順位から構造的含意を引き出している
* **ER**: 電子豊富配位子クラス内の収率変動について、電子的パラメータ（Tolman電子パラメータ、%Vbur等の立体パラメータ）との定量的相関が示されていること
* **EP**: EP-05a [Quantitative-ranking substantiation pack]
* **Case-specific実装**: Table 1エントリー6–10の配位子に対してTolman電子パラメータ(χ)または測定可能なσ-Hammett定数を付与し、収率5a(%)vs.電子パラメータのHammettプロットを構築する; 立体パラメータ(%Vbur)との複数回帰も試みる。
* **注記**: B-7は単一エージェント(V1=medium)。A-6は1/3収束。SRG-4の部分的構成要素として機能するが、B-7自体はSRG-4に含まれていない。

---

**CLA-2: 既存イミニルラジカル法との定量的比較の不在**（grounded_in: C-1, A-2）

* **Primary RI**: RI-09 [External superiority] — 実用上の優位性（高価な活性化基・毒性試薬・UV照射不要）はrefs 14a–14fの具体的な収率・基質範囲と数値的に比較することなく、外部文献の性質の定性的特徴付けのみで主張されている
* **ER**: 代表的な先行プロトコル（例: Zardのキサンテート法、Leonoriの光化学的方法）と同一基質上での直接比較実験（収率・d.r.・反応条件）が提示されていること
* **EP**: EP-09a [Internal benchmark pack]
* **Case-specific実装**: 先行イミニルラジカルプロトコル（refs 14a–14fのうち少なくとも2つ）の標準基質の1つを選択し、本論文と同じ基質で並列実施し、収率・反応時間・d.r.を比較報告する。
* **注記**: C-1はDropped Quantitative Benchmark (symmetric_pattern: yes)。D-4-7の核心根拠。

---

### §3 現在のVQ判定

**現在判定: VQ-2 (Method) — RI-07にEra-norm依存の限定が付く**

---

**VQ-1 (Observation):**
VQ-1は通る。RI-02（生成物・触媒の同一性）は実質的に解消されている: TEMPO付加体6はX線結晶解析で構造確認（CCDC 1429194）; ジヒドロピロール10は2D NMR（ESI詳細）で帰属; エストロン誘導体16a/bも特性評価済み。Non-fatalとして残る問題はB-17（X線品質指標の主テキスト非記載）のみであり、構造の信頼性を根本から覆さない。

---

**VQ-2 (Method):**
VQ-2は通る（Era-norm qualifier付き）。VQ-1継承を前提とする。

- **RI-01**（Reporting integrity）: Non-fatal。マスバランスの体系的欠如（SRG-1）は定量的評価を困難にするが、TEMPO付加体80%・aza-Heck生成物93%・スコープ47–82%という主要データポイントは機能している。2016年のEdge Article形式では質量収支の省略は一般的であり（§4参照）、VQ-2の方法論的成立を根本から覆さない。

- **RI-07**（Unsupported boundary）: Era-norm依存（§4参照）。「solely by choice of phosphine ligand」の主張はmatched-pair experimentなしでは現代基準では不成立だが、2016年の配位子最適化研究では系統的な配位子変動（Table 1の13エントリー）が「配位子効果の実証」として許容された。現代基準に照らせばVQ-2レベルで致命的だが、Era-norm上は非致命的と判断し、VQ-2 (Method)を条件付きで通過とする。

→ **VQ-2 通過（RI-07: Era-norm依存, RI-01: Non-fatal)**

---

**VQ-3 (Mechanism):**
VQ-3は未達。VQ-2通過を前提とするが、以下が阻む。

- **RI-03**（Unobserved explanatory）: **Fatal**。本論文の機構的中核である「Pd(0)→N–O SET」ステップは直接観測なく、速度論的拘束もない。4つの機構探針はいずれも間接的（生成物分布・立体化学・標識取り込み）であり、提案されたSETステップの直接証拠を提供しない。Pd(0)/配位子錯体の酸化電位・N–O結合の還元電位のいずれも測定されておらず、熱力学的実行可能性すら未実証（SRG-4, U-1）。RI-03が解消されない限り、機構水準の主張は原理的に不成立。

- **RI-04**（Unreplicated discriminator）: Non-fatal。Newcomb時計実験（25%収率）・エストロン実験（50%収率）はいずれも単回・低収率だが、複数の独立した探針が同じ方向を指しており、一つの探針の失敗で全体が崩れる構造ではない。

- **RI-06**（Imported model）: Non-fatal。C–I結合へのPd(0) SET（refs 4a-4d）のN–O系への外挿は実証なしだが、本論文は直接N–O系でのラジカル生成物を実証しており、外挿への依存度は低い。

- **RI-05残存**（注1適用）: RI-05が電子豊富/貧配位子の定性的二値化（SRG-4, CLA-1）において重大に残存する。VQ-3が達成された場合も「VQ-3 (Qualified)」となる。

→ **VQ-3 未達（RI-03 Fatal; RI-05重大残存によりVQ-3達成時もQualified見込み）**

---

**VQ-4 (Benchmark):**
VQ-4は未達。VQ-3未達に加え:

- **RI-08**（Unquantified reliability）: Fatal。Table 1・Table 2のいかなるエントリーにも反復測定・標準偏差が存在しない（B-14）。収率値の再現性が不明の状態では比較データの信頼性が原理的に担保できない。

- **RI-09**（External superiority）: Fatal。先行イミニルラジカルプロトコル（refs 14a-14f）との直接数値比較なしに実用優位性を主張している（CLA-2）。

→ **VQ-4 未達（RI-08, RI-09 ともにFatal）**

---

### §4 Era-Norm Annotation

**communication-era tolerated（2016年, Chem. Sci. Edge Article, 5–6ページ形式）:**

- **B-1**（Table 1/2全エントリーの質量収支省略）: 2016年の合成方法論論文では、基質スコープ表での質量収支報告は必須ではなく、単離収率の記載で十分とされていた。Edge Articleの5–6ページ制約もあり、省略は許容範囲。
- **B-7**（電子豊富配位子クラスの一般化声明）: 定性的な配位子クラス一般化は機構的示唆として標準的な記述形式であり、Tolmanパラメータ等との定量相関は要求されなかった。
- **B-9**（2D NMR帰属の完全なESI委任）: 技術的NMR詳細のESI移管は2016年の確立された慣行であり、主テキストでの要点要約は義務ではなかった。
- **B-14**（全収率が単回測定）: 合成方法論論文での単回収率報告は2016年に普遍的であり、反復測定報告の義務化は現代の再現性危機以降の発展。
- **B-17**（X線品質指標の主テキスト非記載）: CCDCへのアクセスが確立されていた時期であり、主テキスト内の全結晶学的品質指標の記載は必須でなかった。
- **B-18**（d.r.決定法の非記載）: d.r.値の測定法（1H NMRかGCか）の明示は、2016年の論文では慣習的に省略されることが多かった。

**modern-era deficient（現代の再認定基準で不十分）:**

- **B-3 + SRG-1**（Newcomb時計実験25%収率・75%マスバランス欠損）: 現代の機構化学では、単回・低収率の探針実験は機構的判断の基礎として不十分; 少なくとも全成分収支と反復測定が要求される。
- **U-1 + B-10**（Pd(0)/配位子酸化電位・N–O還元電位の未測定）: 2020年代において、SET機構を主張する論文では電気化学的検証（CV）または高精度DFTによるΔG_SET推定が実質的に必要とされる; 現代基準ではRI-03 Fatal。
- **U-2**（Pdフリー対照実験の欠如）: 2016年には必ずしも要求されなかったが、現代の機構論文では「触媒必須性の実証」は基本的対照として求められる。
- **B-6, B-15, B-16 + SRG-6**（多変数差異を配位子効果に帰属する比較）: 現代の機構的研究では、主張「solely by ligand」に対するmatched-pair controlは必須と見なされる; RI-07がEra-norm依存から現代基準では致命的に移行。

**両カテゴリ（era-toleratedだが現代では不足）:**

- **B-2**（TEMPOが非決定的という論文自身の免責）: 論文が自ら限界を認識しているにもかかわらず代替ラジカル診断（EPR、速度論的インヒビション）を提示しなかった点は、当時は「正直な記述」として許容されたが、現代では補完的証拠の提示が期待される。

---

### §5 最短補強ルート

**第一目的関数: VQ-3 (Mechanism)** — 現在VQ-2から次水準への到達

---

**VQ-3 への最短ルート:**

1. **EP-03a** [Direct-observation/state-assignment pack] — 代表的Pd(0)/配位子錯体（(dt-bpf)Pd(0)、Pd(0)/P(t-Bu)₃、Pd(0)/P(3,5-(CF₃)₂C₆H₃)₃）のサイクリックボルタンメトリーによる酸化電位測定と、O-ピバロイルオキシムエステルN–O結合の還元電位測定（CV ± DFT）を実施し、ΔG_SETを計算してSETの熱力学的実行可能性を実証する。**RI-03を前進（SRG-4, U-1）** — 情報利得最大: SRGの最多項目グループ（5項目）かつ論文の中核的主張の熱力学的基盤を直接検証する。

2. **EP-07a** [Boundary-test pack] — Pd-free対照実験（塩基+DMF+熱、γ-テルピネンあり/なし、Pd源なし）を基質1aで実施し、ラジカル環化生成物5aの有無を確認する。**RI-07を前進（SRG-2, U-2）** — RIを2つ同時に前進させる（RI-07: Pd必須性の境界; RI-03: SRG-2の代替経路排除）; 実験的実行可能性が最高。

3. **EP-04a** [Discrimination/replication pack] — Newcomb時計実験（Scheme 3A）を改良条件で再実施: (a) GC-MS + 1H NMRによる全成分収支報告、(b) Newcomb rate constant（DMF中70–90°Cでの温度補正値）を適用してラジカル環化速度定数の下限を計算、(c) 生成物10の収率を最大化する条件スクリーニング。**RI-04（SRG-1, SRG-3）を前進**; SRG-3のRI-03残存要素（速度定数）も部分的に前進。

4. **EP-03a** [Direct-observation/state-assignment pack（別実装）] — 触媒量条件下での反応混合物からGC-MSによるp-シメン定量と1H NMRによるγ-テルピネン消費量追跡を実施し、触媒サイクル（Scheme 5）の化学量論的予測を検証する。**RI-03を前進（SRG-5, U-3）** — 触媒サイクルの閉環ステップの独立的実証。

5. **EP-07a** [Boundary-test pack（別実装）] — matched-pair control実験: 基質1b、DMF、70°C、Et₃N 400 mol%固定で(dt-bpf)PdCl₂ vs. Pd₂(dba)₃/P(3,5-(CF₃)₂C₆H₃)₃を並列実施; さらに温度を60°Cに変えた同実験も実施。**RI-07を前進（SRG-6）** — 「solely by ligand」主張の純粋な実験的根拠を提供。

認定ゲート順注記: 実験投入順序は情報利得順（EP-03a → EP-07a → EP-04a → EP-03a → EP-07a）だが、VQ-3の最終認定はVQ-1 → VQ-2 → VQ-3のゲート順で確定する。VQ-2のEra-norm qualifier（RI-07の現代的再評価）を解消するためにも、上記5のmatched-pair controlが必要である。

---

**第二目的関数: VQ-4 (Benchmark)** — VQ-3達成を前提とした追加要件

6. **EP-08a** [Replication/uncertainty pack] — Table 2の全6エントリーについて独立3回の反復実験を実施し、収率の平均値と標準偏差を報告する; Table 1のキーエントリー（entries 3, 11, 13）についても同様。**RI-08を解消**。

7. **EP-09a** [Internal benchmark pack] — 先行イミニルラジカルプロトコル（最低限refs 14a Walton法、14f Leonori法）から代表基質（可能であれば21aまたは21b相当基質）を選択し、本論文と並列実施して収率・反応時間・d.r.を報告する。**RI-09を解消**（CLA-2）。

認定ゲート順注記: VQ-4の認定にはVQ-3認定が前提であり、EP-08a/EP-09aはVQ-3達成後にのみVQ-4ゲートを開ける。

---

### §6 制度設計への寄与

**1. RI-07（Unsupported boundary）の因果帰属型サブパターン:**
comp1は、RI-07が「失敗例の不在」型（従来の典型例）ではなく「排他的因果帰属の実験的純化不足」型として現れる事例を提供する。「solely by choice of phosphine ligand」という主張は、実験デザイン（SRG-6）における多変数同時変化に起因するRI-07であり、「〜のみ可能」ではなく「〜のみが原因」という因果的境界の主張である。RI-07の定義に「排他的因果帰属型（失敗例不在型と区別して）」を例示として追記することが提案できる。

**2. RI-03の「探針多重性による希釈効果」パターン:**
comp1は、4つの独立した機構探針（TEMPO, Newcomb, D-ラベル, エストロン）を駆使しながらVQ-3に到達しない事例として、「探針の多重性がRI-03（直接観測）の解消の代替にはならない」というコードブックの重要な代表例を提供する。各探針は間接的であり、SET速度定数・Pd(0)酸化電位・N–O還元電位という提案機構の直接的根拠を一切提供しない。VQ判定基準において、「複数の間接的探針の一致 ≠ RI-03解消」というルールの具体的例示として記録する。

**3. Era-norm境界のキャリブレーション（2016年Chem. Sci. Edge Article）:**
本ケースは、2016年の英国王立化学会の主要ジャーナルにおいて、(a)マスバランス省略、(b)単回収率報告、(c)定性的配位子分類、がいずれも査読を通過したことを示す。一方、現代基準では(b)のRI-08と(c)のRI-07がともに致命的となる。この較正点は、同時期の他論文との比較に際してEra-norm注記の参照基準として活用できる。

**4. EP-03aの多面的case-specific実装の整理:**
comp1では、EP-03aが3つの独立した化学的問いに対して別々の実装を持つことが確認された: (i) SET熱力学的検証（CV）、(ii) Pdフリー対照（触媒省略実験）、(iii) p-シメン副生物検出（GC-MS）。EP-03aの定義に「提案機構の各ステップに対して最低限一つの直接的観測実験が必要」という要件を例示するケースとして追記できる。

**5. 新規PRI候補なし:**
本ケースで観察されたすべてのパターンは既存RIコード（RI-01, RI-03, RI-04, RI-05, RI-07, RI-09）の組み合わせで記述可能であった。「実験デザイン上の交絡変数」パターン（SRG-6）はRI-07の因果帰属型として位置づけ可能であり、独立したPRIを必要としない。Stage 2Fなし（単報モード）のため、recurring_patternに基づくPRI昇格判断は本ケース単独では実施できない。
```
