prompt_version: stage3-v3-20260425
model_info: claude-sonnet-4-6

# 科学的知見の再認定判定票

## Tamao, Sumitani, Kumada 1972（JACS Communication）

---

### §1 Claim Architecture

**コア主張：**
本論文は、Ni–ホスフィン錯体触媒を用いたグリニャール試薬のビニル/アリールハライドへの選択的クロスカップリングという「新しい実用的合成法」を提案している。Novelty柱は「触媒的C–C結合形成における選択性（クロス対ホモカップリング）」と「β-H含有アルキルグリニャール試薬の高収率使用」の二つ。Utility柱は「従来法では困難な化合物（m-ジブチルベンゼン等）をワンステップで得る実際的経路」および「塩化物の高反応性が提供する実用上の優位性」である。

**Layered structure：**
D-1が示すように、本論文の主張は4つの独立層を持つ。

- **Layer 1（合成的実用性）**: Table I収率データ（主に単離収率）。この層は他の3層とは独立しており、機構仮説が誤りであっても収率データは有効である。
- **Layer 2（触媒サイクル仮説）**: eqs 2–4によるNi(II)/Ni(II)サイクル（working hypothesisとして提示）。Layer 1の成立に論理的依存なし。ただし後述するように、自身の観測（黒色沈殿）との矛盾を含む。
- **Layer 3（sp²ハライド特異性とスコープ境界）**: 「Onlysp²halides can be used」という境界主張。実験的ネガティブコントロールなしに提示。
- **Layer 4（配位子活性序列とcis要件）**: 定性的活性序列から中間体の構造要件（cis配置）を推論。数値データなし。

Layer 1とLayer 4の間には部分的な依存関係がある（最も活性な配位子[NiCl₂(dpe)]を選択する根拠がLayer 4の定性序列に依存する）が、Layer 1の主要な収率データはそれ自体で自立している。単一の実験的反証でLayer 1が崩れることはなく、機構層（Layer 2）の反証もLayer 1を無効化しない。

---

### §2 SRG / CLA → RI / ER / EP Crosswalk

---

**SRG-1 [selectivity evidence absent]**

* **Primary RI**: RI-01 [Reporting integrity] — 収率測定枠（単離 vs. glpc）が混在し横比較不能（B-8）、glpc条件未記載で再現性なし（B-9）、ホモカップリング生成物が全エントリで未報告（B-1）、マスバランス不在（B-2）
* **Secondary RI**: RI-08 [Unquantified reliability] — 収率の反復測定・不確かさ記述なし
* **ER**: Table Iの全エントリについてホモカップリング生成物（R–RおよびR'–R'）収率を定量内部標準glpcで報告すること。glpc条件（カラム、固定相、温度、検出器、応答係数）を実験の部に全記載すること。単離/glpc収率の混在を解消するか、代表エントリで両法を並行測定して交差検証すること。
* **EP**: EP-01a [Reporting-coherence pack]; EP-08a [Replication / uncertainty pack]
* **Case-specific実装**: n-BuMgBr/PhCl系（Table I主要エントリ）について、クロスカップリング生成物（n-Pr–Ph）とホモカップリング生成物（n-Pr–n-Pr、Ph–Ph）の収率を同一glpc系で定量。既報のdorane系内部標準を用いたキャリブレーションカーブを作成。各エントリのマスバランス（合計収率+未回収分）を記録。
* **注記**: TEMPERATURE_SUMMARY high_convergence_low_gap（B-1: V1=high, V2=high, V3=high, convergence=3/3, temperature_gap=none）。U-1（eq 3が予測するR–R生成量が未報告）はself-contradictory absenceとしてB-1に対応。

---

**SRG-2 [catalytic cycle lacks mechanistic support]**

* **Primary RI**: RI-03 [Unobserved explanatory] — 提案触媒サイクルの鍵中間体（L₂NiR₂、L₂Ni(R')(X)、サイクル内のNi(0)）は直接観測も速度論的拘束も受けていない
* **Secondary RI**: RI-04 [Unreplicated discriminator] — 黒色沈殿という単一の未特性化観察が、Ni(II)/Ni(II)サイクルとNi(0)/Ni(II)サイクルの識別に関わる唯一の観察可能な証拠となっている（B-10）; RI-06 [Imported model] — eq 1の化学的根拠がdipy-Ni錯体（refs 11, 12）からdpe-Ni錯体への類推輸入であり（C-3）、dpe配位子下でのリガンド特異的速度・選択性が検証されていない
* **ER**: 提案サイクルの各素反応ステップを触媒実験と同じdpe-Ni系で独立に実証すること。具体的には：(a) L₂Ni(n-Bu)₂（dpe）の合成・同定、(b) これとPhClの反応によるn-Bu₂（R-Rホモカップリング物）放出とL₂Ni(Ph)(Cl)生成の確認、(c) 黒色沈殿の分光学的同定（元素分析、XRD、またはXAS）によりNi(0)/Ni(II)サイクルを排除または採用すること。
* **EP**: EP-03a [Direct-observation / state-assignment pack]; EP-04a [Discrimination / replication pack]; EP-06a [Analogy-validation pack]
* **Case-specific実装**: [NiCl₂(dpe)]とn-BuMgBrを化学量論的条件で反応させ、[Ni(n-Bu)₂(dpe)]を単離・NMR・IR確認。次にPhClを添加してn-Bu₂の生成をglpcで定量（eq 3の化学量論確認）。Example 1の反応後の黒色固体をろ過・洗浄してXRD分析（金属Ni vs. Ni(0)錯体判定）。速度論的プロファイリング（NMRまたはglpcによるturnoverbf測定）で律速ステップを同定。
* **注記**: TEMPERATURE_SUMMARY high_convergence_high_gap（B-10: V1=medium, V2=critical, convergence=2/3, temperature_gap=medium）。これはTEMPERATURE_SUMMARYにおける最優先シグナル。U-2（Ni酸化状態の自己矛盾的不在）、U-3（二重置換機構の未説明）、U-4（速度論的/熱力学的制御の未検討）はすべてSRG-2の傘下。A-2（機構的詳細の全面的繰り延べ）はこれらの包括的フレームを提供。

---

**SRG-3 [product identity and purity underdetermined]**

* **Primary RI**: RI-02 [Object identification] — 生成物の特性評価が「and/or」によりエントリ間で不統一（B-6）、代表的な実験例（Examples 1, 2）でも純度がbpおよび屈折率のみで確認（B-7）、構造的純度（位置異性体不純物、ホモカップリング体混入）を排除できる粒度の分析が存在しない
* **Secondary RI**: RI-01 [Reporting integrity] — glpc条件未記載（B-9）、収率計算基準の混在（B-8）
* **ER**: 各Table I生成物について最低限の標準的同定（GC純度＋少なくとも1つの分光法：NMRまたはMS）を適用すること。代表例（Examples 1, 2）では¹H NMRの完全な化学シフトデータを報告すること。
* **EP**: EP-02a [Identity / purity substantiation pack]; EP-01a [Reporting-coherence pack]
* **Case-specific実装**: m-ジブチルベンゼン（Example 1）について¹H NMR（化学シフト・積分比・多重度）を記録し、o-およびp-異性体混入の排除を示す。α-ビニルナフタレン（Example 2）の¹H NMRで二重結合プロトンのシグナルを確認。全Table I生成物に対してglpc純度トレースを報告。
* **注記**: B-8（収率計算基準混在）はRI-01の内部矛盾型サブタイプに相当する（単離収率とglpc収率が同一Table内に混在し、直接比較不能）。

---

**SRG-4 [comparative claims without data]**

* **Primary RI**: RI-05 [Qualitative overread] — 配位子活性の定性的序列から中間体のcis配置を機構的要件として導出（B-3）; 「エーテルがTHFより確実に優れる」という断言（B-4）
* **Secondary RI**: RI-09 [External superiority] — Tamura-Kochi鉄触媒系との優位性を外部文献値のみで主張（C-1）; 比較基質での直接実験なし
* **ER**: 6種の配位子について同一条件下（同一触媒量、同一基質、同一反応時間）での収率データを報告すること。エーテルとTHFを同一基質で比較した収率データを報告すること。Tamura-Kochi鉄触媒系と本系を共通のビニルハライド基質で直接比較すること。
* **EP**: EP-05a [Quantitative-ranking substantiation pack]; EP-09a [Internal benchmark pack]
* **Case-specific実装**: n-BuMgBr/PhClを基質として、[NiCl₂(dpp)]・[NiCl₂(dpe)]・[NiCl₂(dmpe)]・[NiCl₂(PPh₃)₂]・[NiCl₂(PEt₃)₂]・[NiCl₂(PPh₂Me)₂]を0.5 mol%、室温→還流、4時間で平行反応し収率を測定。エーテル対THFの比較を同基質・同条件（同一触媒量・時間）で実施。TamuraeKochi系（FeCl₃/THF）との比較をβ-スチレン塩化物で実施。
* **注記**: C-1（Tamura-Kochi比較）はRI-09とRI-05の共起（RI-09: 外部文献値のみ; RI-05: 定性的序列から構造的含意）。両者の独立解消が必要であり、一方のみの解消では不十分（RI共起パターン、§6参照）。

---

**SRG外：CLA**

---

**CLA-A: sp²境界主張（B-5, A-3）**

* **Primary RI**: RI-07 [Unsupported boundary] — 「Only sp² halides can be used」という境界主張にsp³ハライドの否定的試験が存在しない。「使用できない」と「使用を試みていない」の区別が不明
* **Secondary RI**: なし（A-3による明示的繰り延べが存在するが、繰り延べ自体がRI-07を正当化しない）
* **ER**: 少なくとも2種のsp³ハライド（例：n-BuCl、i-PrBr）をn-BuMgBrとの反応に適用し、低収率・低選択性であることを確認することで境界の実験的根拠を提供すること。
* **EP**: EP-07a [Boundary-test pack]
* **Case-specific実装**: n-BuCl（sp³一次）とi-PrBr（sp³二次、β-H脱離が特に問題となる可能性）をTable Iの条件Aで処理し、収率・副生成物プロファイルをglpcで測定。sp³ハライドでの低活性/低選択性の結果を報告することでsp²特異性を実験的に確立する。
* **注記**: A-3（「Investigations are continuing...」）は将来的自動解消の候補。CLA-Aは通信→Full Paper遷移で自動解消される典型例（§6参照）。

---

**CLA-B: Corriu-Masse同時提出論文および化学量論的試薬との比較不在（C-2, C-4）**

* **Primary RI**: RI-09 [External superiority] — Corriu-Masse（Ni(acac)₂系）との比較が皆無（C-4）; π-アリルニッケルおよびクプラート試薬（C-2）との収率比較なし
* **Secondary RI**: なし（C-2は「cite-and-dismiss」であり直接優位性主張は控えめだが、フレーミングが暗示的優位性を構築している）
* **ER**: 少なくとも代表的な1基質（PhCl等）について[NiCl₂(dpe)]触媒系、Ni(acac)₂触媒系、クプラート化学（RLi/CuI）の3系での収率・選択性を直接比較すること。
* **EP**: EP-09a [Internal benchmark pack]
* **Case-specific実装**: n-BuMgBr/m-Cl₂C₆H₄系（Table I代表エントリ）を用い、[NiCl₂(dpe)]0.5 mol%（条件A）とNi(acac)₂5 mol%（Corriu-Masse条件）を並行反応。生成物収率・単離収率・ホモカップリング体比率をglpcで比較。
* **注記**: D-4候補6のうちC-2およびC-4の部分がSRG-4（B-4, C-1）でカバーされない範囲。SRG-4のRI-09はTamura-Kochi比較（C-1）を対象とし、Corriu-Mass/クプラート比較（C-2, C-4）は独立CLAとして記録。

---

**PRI-12チェック（v18新規）：**

**Cluster A（Self-referential validation）チェック：**
本論文は実験的合成通信であり、新しい数学的記述子・指標・スコア関数を提案していない。検証指標と被検証対象が同一の数学的構成物に依存する構造（条件a〜d）は成立しない。**PRI-12 Cluster A: 非該当。**

**Cluster B（Deductive-retrospective circularity）チェック：**
本論文の機構仮説（eqs 2–4）は演繹的構造を持つ：既知の化学量論的反応（dipy-Ni系, eq 1; Ni–XとRMgXの交換）を類推により触媒サイクルとして組み合わせ、「working hypothesis」として提示し、検証を後続研究（A-2）に委ねている。

- 条件(a): 部分的に成立 — 機構提案の検証が著者自身による選定事例（refs 11, 12のdipy-Ni実験）のみに依存
- 条件(c): 成立 — 機構的検証が後続論文に委譲（A-2: "Further studies are required..."）
- 条件(d): 部分的に成立 — C-3（refs 11, 12、dipy-Ni事例）が遡及的に「eq 1の根拠」として引用されているが、これらはdpe-Ni系での実証ではない

ただし本論文は「working hypothesis」という明示的仮説標識を用いており、機構を確立済みとして提示していない。演繹遡及循環は**Secondary**パターンとして記録（PRI-12 Cluster B, subtype B2 + B4の弱い形態）。PrimaryはRI-03とRI-06。VQ判定への直接的影響は、RI-03 Fatal（→VQ-3未達）として既にキャプチャされている。

---

### §3 現在のVQ判定

**現在判定: VQ-2 [Method]（qualified）**

---

**VQ-1 [Observation]：通過（Non-fatal、Era-Norm依存）**

RI-02の解消状況：SRG-3が指摘する通り、Table I生成物の特性評価は「and/or」で統一基準なし（B-6）。しかし2つの代表的製造例（Examples 1, 2）は、既知化合物についてbpおよび屈折率の文献値との一致を示しており、1972年のJACSコミュニケーション基準では許容される同定として機能する。生成物が既知化合物であることが主要文脈であり、RI-02はNon-fatal。VQ-1は通過。ただしこの判定はEra-Norm依存：現代基準ではRI-02はFatalとなる（§4参照）。

---

**VQ-2 [Method]：通過（qualified）— VQ-1継承前提**

RI-01の解消状況：Table Iのうち単離収率エントリ（多数）は再現可能な収率記録として機能する（RI-01 Non-fatal for isolated yield layer）。しかし5つのglpc収率エントリはglpc条件未記載（B-9）のため再現不能であり、これらのエントリに限ってRI-01はFatal。sp²境界主張（CLA-A）のRI-07はFatal（ネガティブコントロールなし）。

**層別VQ非対称性：**
- **Layer 1（単離収率エントリ）単独では：** RI-01 Non-fatal → VQ-2到達。Table IのうちB-8の影響を受けない単離収率15エントリ程度は、合成的実用性のMethodレベルの主張として成立する。
- **Layer 2（機構仮説）**: VQ-1（Observation）止まり — RI-03, RI-04, RI-06がすべてFatal（後述）。
- **Layer 3（sp²境界）**: VQ-2未達 — RI-07 Fatal。
- **Layer 4（配位子活性序列・cis要件）**: VQ-2 qualified — RI-05が重大に残存（数値データなし、qualitative overread）。

全体の判定としては、Qualified VQ-2：「合成的実用性（単離収率エントリ）に関してはVQ-2に到達しているが、glpc収率エントリ、sp²境界主張、配位子選択根拠においてVQ-2が限定的（RI-01 partial fatal、RI-07 fatal、RI-05 persistent）。」

---

**VQ-3 [Mechanism]：未達**

RI-03（Unobserved explanatory）：Fatal。触媒サイクルを構成する3つの中間体（L₂NiR₂、L₂Ni(R')(X)、およびニッケル種の酸化状態）のいずれも、直接観測・速度論的拘束・トラップ実験によって確認されていない（U-2のNi酸化状態問題を包含）。Ni(0)/Ni(II)サイクルとNi(II)/Ni(II)サイクルの識別が未解決のまま機構を提案している。

RI-04（Unreplicated discriminator）：Fatal。黒色沈殿（B-10、U-2）という単一の未特性化観察が、Ni(0)析出の唯一の記録であり、提案サイクルとの整合性は議論されていない。複数回の実験から体系的に確認されたデータではない。

RI-06（Imported model）：Fatal。eq 1（dipy-Ni系）からdpe-Ni系への類推（C-3）は、dpe系での独立検証なしにサイクルの化学的根拠を構成している。dpe配位子のπ-受容能・結合距離・立体環境がdipy系とは大きく異なるにもかかわらず、この差異は検討されていない。

RI-05が重大に残存（配位子序列→cis要件の定性的過読）するため、VQ-3に到達した場合もVQ-3 (qualified)が上限となる。

VQ-3は未達。未解消RI: RI-03（Fatal）、RI-04（Fatal）、RI-06（Fatal）、RI-05（VQ-3 qualified化）。

---

**VQ-4 [Benchmark]：未達（VQ-3未達のため前提欠如）**

---

### §4 Era-Norm Annotation

**communication-era tolerated（1972年JACS Communication基準で許容）:**

- **B-1（ホモカップリング定量なし）**: 1972年の遷移金属触媒C–C結合形成コミュニケーションでは、クロスカップリング生成物の収率報告が主体であり、副生成物プロファイルの定量は慣行外だった。選択性は多くの場合「高収率が得られた」をもって暗示的に示された。
- **B-2（マスバランス不在）**: 収率の全組み合わせ報告（生成物+副生成物+未回収物）はフルペーパーで要求される記述であり、2頁コミュニケーションでは省略が当然とされた。
- **B-3（配位子活性の数値データなし）**: スクリーニング結果の定性的序列提示は1970年代初頭の合成報告で標準的であり、数値データはフルペーパーに収録される慣行だった。
- **B-4（溶媒比較データなし）**: 溶媒効果の定性的主張（「superior to THF」）は経験的知見として許容され、定量的比較はフォローアップ研究に委ねられた。
- **B-6（特性評価の可変基準）**: "and/or"による複数法の併記は、スペース制約下で各生成物の同定に柔軟性を持たせる慣行として許容されていた。
- **B-7（bp+屈折率のみによる純度確認）**: 既知化合物については文献物理定数との一致が十分な同定とみなされており、1970年代初頭にNMR純度確認は必須ではなかった。
- **B-9（glpc条件未記載）**: glpcパラメータの完全記載は1970年代のJACSコミュニケーションでは慣例外であり、実験の再現性は主に単離収率で保証された。
- **B-12（触媒量の範囲指定）**: コミュニケーション形式では条件の完全記述よりも代表的条件の提示が優先された。
- **A-2（機構的詳細の繰り延べ）**: コミュニケーションの常套的終結フレーズ（"Further studies are required..."）であり、合成法の有用性を示すことに特化した通信では機構解明の後回しが正当化される慣行だった。

**modern-era deficient（現代の再認定基準では許容不可）:**

- **B-9（glpc条件未記載）**: 現代では分析データの再現性確保のために全クロマトグラフィー条件の記載が必須であり、形式（コミュニケーション/フルペーパー）を問わず要求される。
- **B-10（黒色沈殿の未特性化・未言及）**: 提案機構と矛盾しうる観察（黒色固体の析出）を記録しながら議論しないことは、現代の機構論文では許容されない。XRDまたはEDX分析による組成の簡易確認が期待される。
- **U-2（Ni酸化状態の自己矛盾的不在）**: 現代のクロスカップリング論文では触媒前駆体から活性種への変換と酸化状態サイクルの明示が要求される。「black mixture」の記録と「Ni(II)-only cycle」の提案を並列するのは現代基準では不十分。
- **U-4（選択性の機構的根拠なし）**: 「selective」を冠する論文で選択性の比（クロス/ホモ）を報告しないことは、現代の編集基準では受理されない。
- **B-1（ホモカップリング定量なし）**: 現代のクロスカップリング報告では副生成物プロファイルの定量が標準であり、選択比（cross/homo）の記載が期待される。
- **B-8（収率計算基準の混在）**: 現代では単離収率とglpc収率が同一表内に混在する場合、各エントリに明示的なフラグと交差検証が要求される。

**両タグに該当（当時許容・現代は不足）:**
- B-3（配位子活性の数値なし）: 1972年当時は許容されたが、現代では定性的序列から機構的含意（cis要件）を導出する論文ではその根拠となる数値データが必須。Era-Normとして記録しつつ、RI-05のFatal化はModern基準に依存。

---

### §5 最短補強ルート

**現在VQ: VQ-2 (qualified)**

---

**VQ-3 への最短ルート（第一目的関数）：**

1. **EP-03a [Direct-observation / state-assignment pack]** — [NiCl₂(dpe)]とn-BuMgBrからL₂Ni(n-Bu)₂を化学量論的に合成・単離・NMR/IR同定し、触媒回転中の中間体としての実在を実証する（RI-03を前進）。同時に反応後の黒色固体をXRD/EDX分析してNi(0)または金属ニッケルと同定し（RI-04を前進）、Ni(0)/Ni(II)対Ni(II)/Ni(II)サイクルの識別を行う（RI-04, RI-03を並列前進）。**最高情報利得ステップ：RI-03・RI-04を同時前進。**

2. **EP-06a [Analogy-validation pack]** — L₂Ni(n-Bu)₂（dpe）にPhClを添加してn-Bu₂のglpc定量と[NiCl₂(dpe)]生成の分光確認を行うことで、eq 1の化学量論（C-3のdipy-Ni類推）をdpe-Ni系で独立実証する（RI-06を前進）。Step 1のL₂Ni(n-Bu)₂合成と連続実施することで効率化可能。

3. **EP-05a [Quantitative-ranking substantiation pack]** — 6種配位子の収率スクリーニングを定量的に実施し（Step 1–2と同一基質系）、定性的活性序列（B-3）を数値化する（RI-05を前進。VQ-3 → VQ-3 qualified解消 → VQ-3 non-qualifiedへ）。

認定ゲート順注記：EP投入は情報利得順（EP-03a → EP-06a → EP-05a）だが、最終的なVQ認定はVQ-1 → VQ-2 → VQ-3のゲート順で確定する。VQ-3認定にはRI-03・RI-04・RI-06のすべての解消が必要。EP-03aとEP-06aは連続実施可能だが、VQ-3認定はこれら両方の完了を要する。

---

**VQ-4 への最短ルート（第二目的関数、VQ-3前提）：**

4. **EP-08a [Replication / uncertainty pack]** — 代表的Table Iエントリ（n-BuMgBr/PhCl、n-BuMgBr/m-Cl₂C₆H₄）について反復実験（n≥3）を実施し収率の標準偏差を報告する（RI-08を前進）。

5. **EP-09a [Internal benchmark pack]** — n-BuMgBr/styrene chloride（または同等のビニルハライド）系でTamura-Kochi鉄触媒系およびCorriu-Masse Ni(acac)₂系との直接収率比較を実施する（RI-09を前進）。

認定ゲート順注記：VQ-4への最終認定はVQ-3が確立された後にRI-08・RI-09の解消をもって確定する。

---

### §6 制度設計への寄与

**1. 標識不整合（Labeling mismatch）パターンの代表事例：**

本論文はA-2において「working hypothesis described above」という仮説標識を使用しているが、eqs 2–4の本文記述は事実的叙述語で一貫している（"L₂NiX₂ reacts with...", "subsequently converted to", "cross-coupling product is released by..."）。仮説を示す文言は機構説明段落の末尾1文の免責条項（"Further studies are required before..."）に集約されており、各機構ステップには仮説標識が付与されていない。これはLabeling mismatch（§6の検出対象パターン）の典型例であり、RI-06（類推輸入）と連動している：dipy-Ni系からの輸入モデルが事実的記述語で提示されるため、読者にとってその仮説的性質が見えにくい。Codebookへの追記候補：「RI-06 + labeling mismatch の共起パターンは、機構サイクル全体が他系から輸入された場合に頻出する。仮説標識の位置（末尾集約型）はCommunicationフォーマットで特に多く見られ、Era-Norm annotationで記録すること。」

**2. 通信→Full Paper遷移の自動解消パターン：**

CLA-A（sp²境界主張、RI-07）とA-3（「Investigations are continuing...」）の対応は、RI-07が通信形式の紙幅制約に起因し、著者自身が後続研究による解消を明示したケースである。これはA項目（prospective deferral）とRI-07の組み合わせとしてUQS分析で繰り返し確認されるパターンに一致する。この対は§4 Era-Norm（communication-era tolerated）と連動しており、Codebookへの追記候補：「A項目 + RI-07の共起（特にA-3型の汎用スコープ拡張繰り延べ）は通信→Full Paper自動解消パターンの典型。§4で'自動解消候補'として記録し、RI-07の致命性判定にEra-Norm補正を適用すること。」

**3. RI共起パターン（SRG-2）：**

SRG-2においてRI-03 + RI-04 + RI-06が三重共起している。このパターンの構造的特徴：RI-06（類推輸入）によってサイクルが構築されているため、サイクル内の中間体は定義上「当該系では未観測」（RI-03）であり、それを支持または反証する唯一の観察可能なシグナル（黒色沈殿）は単一未特性化観察（RI-04）に留まる。この三つのRIは依存的共起（independent resolutionではなく、EP-03aによる直接観測でRI-03とRI-04を同時前進させ、EP-06aによる化学量論確認でRI-06を前進させることが最効率）を形成しており、一方だけの解消では不十分な構造となっている。Codebookへの追記候補：「RI-03 + RI-04 + RI-06の三重共起は触媒サイクル論文における典型的な機構的脆弱性クラスターを形成する。EP-03a（直接観測）がRI-03・RI-04を並列前進、EP-06a（類推検証）がRI-06を前進する設計が最短補強ルートとなる。」

**4. PRI-12 Cluster B（Secondary pattern）の境界事例：**

§2のPRI-12チェックで指摘した通り、本論文の機構仮説提示はCluster Bのsubtype B2（遡及的確認引用、C-3）とB4（演繹・遡及の方向混同）の弱い形態を示す。しかし「working hypothesis」という明示標識がこのパターンを部分的に緩和している。Codebookへの追記候補：「実験的合成論文において'working hypothesis'と明示された機構提案は、PRI-12 Cluster Bの閾値に達しない場合が多い。閾値は'演繹的導出が主主張であること'であり、合成論文での機構仮説は補足的位置づけのため閾値を下回る。RI-03 + RI-06でVQ判定上は十分に捕捉される。」

**5. Layer 1（合成的実用性）の歴史的特異性：**

本論文はKumadaカップリングの創始的コミュニケーションである。Layer 1（Table I収率）は単離収率として自立的に機能し、VQ-2（Method）に到達している。一方Layer 2（機構）はVQ-1止まりである。この非対称性（VQ-2の合成的実用性 vs. VQ-1の機構層）は、後続の一連のフルペーパー・機構研究（Kumadaグループ、Kochiグループ）によって段階的に解消されていったことが歴史的に確認されている。これはUQS分析における「著名な草創期コミュニケーション」の典型的VQ非対称性プロファイルを示しており、VQ判定の時間的進化を議論する際のベンチマーク事例として機能する。

**6. 既存RI・EP体系の追加確認：**

- RI-03のcase-specific実装：触媒サイクル中間体の「直接観測」はNi系では¹³Cまたは³¹P NMRモニタリングが有効。Pd系でのEP-03a事例との比較で、中間体安定性の違いがNi系でのRI-03への実装難度を高めることをCodebookに追記すること。
- EP-07a（境界テスト）のcase-specific実装追加例：sp³ハライドの"complete inactivity vs. low selectivity"の識別は、glpc分析でアルカン副生成物（β-H脱離生成物）の検出が鍵となる。この実装パターンをEP-07aのNi触媒系事例として記録する。
