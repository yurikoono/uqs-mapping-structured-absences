prompt_version: stage3-v2-20260416
model_info: claude-sonnet-4-6

# 科学的知見の再認定判定票

## Murai et al. 1993（Nature, Articles）

---

### §1 Claim Architecture

**コア主張の要約**

本論文は「RuH₂(CO)(PPh₃)₃が芳香族ケトンのC-H結合をオレフィンに対して触媒的に付加させる」という反応発見を核心とし、その成立要因として「キレーション補助によるC-H結合の位置選択的開裂」という機構原理を提示する。Novelty柱は二つ：（1）従来のC-H官能化触媒が1〜2種の基質にしか適用できなかったのに対し、13例の芳香族ケトン/オレフィン組み合わせにわたる汎用的な触媒系の発見、（2）キレーション補助という設計原理が実用的な有機合成に求められる効率・選択性・汎用性を同時達成する手段となることの提示。Utility柱は「新しいアルキル化芳香族化合物群の合成を可能にする実用的触媒」としての位置付けであり、Nature Abstract の最終文「[REDACTED: verbatim source text; see the source paper via its DOI]」に集約される。

**Layered structure の判定**

Stage 2 D-1で確認された通り、論文の主張はLayered structureを持つ——効率（TOF）・選択性（regioselectivity）・汎用性（substrate scope）の三軸が独立層を形成する。この構造は、単一軸の反証が他軸を自動的に崩さないことを意味する。例えばGC収率の再検討で効率層が修正されても、ortho選択性の観察や基質スコープの事実は独立して残る。

ただし、三軸すべての根拠として「キレーション補助機構」が共有されているため、機構層は三軸すべてに対するCommon Foundation（共通基盤）を形成している。具体的には、D-4-1（中間体の実在）→D-4-9（C-H開裂機構の判別）→D-4-7（先例引用の整合性）という連鎖的依存関係が機構層に存在し、これらが未解消のまま残ると三軸の「なぜ機能するか」という説明が全体として不確定になる。

したがって本論文の構造は「三軸独立 × 機構共通基盤依存」であり：
- 観察層（何が起きたか）：独立。収率・選択性・スコープはデータとして相互に独立。
- 機構説明層（なぜ機能するか）：単一基盤（キレーション補助中間体）に依存。この層の崩壊は効率・選択性・汎用性すべての因果説明を無効化する。

---

### §2 SRG / CLA → RI / ER / EP Crosswalk

**2a. SRG の取得（Stage 1 Turn 4 META より）**

- SRG-1: Quantitative evidence base（B-1, B-2, B-3, B-4）
- SRG-2: Catalytic cycle evidence absent（A-1, U-1, U-2）
- SRG-3: Selectivity basis absent（B-8, B-9, B-10, U-4）
- SRG-4: Scope claims exceed data（B-5, U-3, B-7）
- SRG-5: Prior art not engaged numerically（C-1, B-2）

**2b. CLA 候補の同定**

D-4候補のうちSRGに属さない、またはSRGの既存membersでは捕捉されないD-4候補を検討する。

- D-4-7（キレーション補助先例引用の酸化状態マニホールド不整合）: grounded_inはC-2, C-4, B-11, A-1。B-11はSRG-2/SRG-3に部分的関連と記録されているが、C-2・C-4はいずれのSRGのmember_itemsにも登録されていない。この問いはD-1の機構主張（「成功の鍵はキレーション補助」）の直接的な引用根拠を問うものであり、タイトルレベルの主張に直結する。CLA-1として記録する。

- D-4-8（「実用的有機合成に必要な効率・選択性・汎用性」の外挿可能性）: grounded_inはB-6, B-7, B-1。B-6はSRGに未登録。B-1はSRG-1に属するが、B-6・B-7が「実用条件外挿」という独立した問いを構成する。この問いはD-1のUtility柱（「practical organic synthesis」）に直接関わる。CLA-2として記録する。

自己矛盾的不在のCLAチェック：U-1（環状メタレート中間体の観測未実施）はSRG-2に含まれているが、「提案された触媒サイクルの中間体が分光学的に観測可能であるはずだが、観測が未実施」というパターンに正確に該当する。これはSRG-2の一部として§2内で十分に捕捉されている（CLA重複登録回避）。

---

**SRG-1 [Quantitative evidence base]**（B-1, B-2, B-3, B-4）

* **Primary RI**: RI-01 [Reporting integrity] — GC収率とその算出基盤（内部標準・較正曲線）が不明で、13例中10例で単離収率が未報告のため、横比較不能。
* **Secondary RI**: RI-08 [Unquantified reliability] — 反復測定なし・不確かさ記述なし（B-1の収率、B-2のTOF比較主張に直接抵触）。
* **ER**: GC収率は内部標準種・較正曲線・定量下限を明示して初めて比較可能な値となり、少なくともruns 1, 9, 10（TOF比較を主張するラン）では単離収率が必要。
* **EP**: EP-01a [Reporting-coherence pack]; EP-08a [Replication / uncertainty pack]
* **Case-specific実装**: 
  - EP-01a: 内部標準（例：n-ドデカン）を使用したGC定量法の明示 + runs 1, 9, 10での実際のTOF値（初期速度または最終収率/反応時間から算出）の報告。比較対象であるrefs 11/12のTOF値と同条件での再現値を並記。
  - EP-08a: 代表的2〜3ランでの三連測定（または二連測定＋統計）によるGC収率の±σ記述。B-3（触媒比較）では各触媒について同一基質・同一条件でのGC収率と反応時間を数値で報告。
* **注記**: B-1（V1=high, V3=high; convergence 2/3; TEMPERATURE: high_convergence_low_gap）; B-2（V1=high, V3=high; convergence 2/3; high_convergence_low_gap）; B-3（V1=medium, V2=medium, V3=medium; convergence 3/3; high_convergence_low_gap）; B-4（V3関連; 「standard methods」未定義）。SRG-5（C-1, B-2）と部分的重複：TOF優位性主張はRI-01（報告基盤不在）とRI-09（外部比較なし）の両面を持つ。

---

**SRG-2 [Catalytic cycle evidence absent]**（A-1, U-1, U-2）

* **Primary RI**: RI-03 [Unobserved explanatory] — 触媒サイクルの速度決定的中間体（環状メタレート錯体、Fig. 1）が直接観測も速度論的拘束もされていない。Ru(0)活性種の実在も未確認。
* **Secondary RI**: RI-06 [Imported model] — 触媒サイクル全体がRu(0)酸化的付加モデルとして提案されているが、直接支持証拠なし。refs 14/15の化学量論的Mn(I)/Ru(II)先例をRu(0)触媒サイクルへ輸入（B-11, C-2）。RI-06スコープ注記「サイクルレベル輸入」が適用される。
* **ER**: 触媒サイクルの「速度決定的中間体」は、化学量論的条件での単離またはin situ NMR観測（³¹P{¹H}, ¹H NMRのHM-H相互作用確認）によって存在を実証するか、D₂ラベル実験でC-H/C-D結合開裂をトレースすることが規範的要件。前触媒活性化はRu(0)源（例：RuH₂(CO)(PPh₃)₃ + 熱処理後の溶液ESIまたはRu(0)直接投入の等価性試験）で確認される必要がある。
* **EP**: EP-03a [Direct-observation / state-assignment pack]; EP-06a [Analogy-validation pack]
* **Case-specific実装**:
  - EP-03a: RuH₂(CO)(PPh₃)₃とアセトフェノンの化学量論反応（toluene, 135 °C、1:1）を実施し、生成する錯体を³¹P{¹H}および¹H NMRで同定。または環状メタレート中間体の類似体（例：アセトフェノン/Ru(0)源）を単離し、X線結晶構造解析で構造確認。
  - EP-06a: C-H酸化的付加（Ru(0)→Ru(II)）と求電子的メタレーション（Ru(II), Mn(I)）の生成物が同一構造を持つかをDFT計算（1993年当時はMM/PM3、現代ではDFT/B3LYP）で比較。輸入元の機構的差異を定量的に評価。
* **注記**: U-1（V2=critical, V3=critical; convergence 2/3; TEMPERATURE: high_convergence_low_gap）; U-2（V2 high severity のみ; TEMPERATURE: low_convergence_high_gap境界）; A-1（V2 critical, single-agent; TEMPERATURE: low_convergence_high_gap）。D-4-9（KIE不在：C-H開裂律速判定）もSRG-2の延長としてRI-03に該当する。D-4-7の一部（RI-06成分）もSRG-2と連結。

---

**SRG-3 [Selectivity basis absent]**（B-8, B-9, B-10, U-4）

* **Primary RI**: RI-05 [Qualitative overread] — ラン10（0.5 h, 100%）対ラン11（20 h, 88%）の速度差が「リング歪みの重要性を示す」と帰属されるが、速度定数・活性化パラメータなし。「virtually 100%」の位置選択性も非観察異性体の検出下限が不明。
* **Secondary RI**: RI-04 [Unreplicated discriminator] — 1-インダノンの不反応という単一の否定的実験結果（B-9）を「リング歪み」帰属の証拠として使用。「not shown」と明記されており、データが存在するにもかかわらず報告されていない。
* **ER**: 速度差の帰属には活性化エネルギー（アレニウスプロット）または少なくとも複数温度での収率時間プロフィール比較が必要。位置選択性は主要異性体の単離同定と副異性体のGC/HPLC検出下限（定量下限）の両方を記述してはじめて「virtually 100%」の数値根拠となる。
* **EP**: EP-05a [Quantitative-ranking substantiation pack]; EP-04a [Discrimination / replication pack]
* **Case-specific実装**:
  - EP-05a: ラン10・11に対する反応速度プロフィール（時間点を4点以上取り初期速度を算出）と、少なくとも2温度（例：110°C vs 135°C）でのk比から活性化エネルギー差（ΔΔG‡または ΔΔEa）を算出。
  - EP-04a: 位置選択性実験（runs 8, 13）で単離した主生成物の¹H NMR帰属に加え、クルード反応混合物のGC分析で4種の可能な位置異性体ピークの存在/不在を確認し、最大不純物ピークを特定して「virtually 100%」の数値根拠を示す。1-インダノン実験は生成物/出発物質のGC回収率を含めて報告。
* **注記**: B-8（V1=medium, V2=high; convergence 2/3; TEMPERATURE: high_convergence_low_gap; gap: low）; B-9（V1=medium, V2=high; convergence 2/3; gap: low; 否定的証拠as evidence パターン）; B-10（V2-Q9; reporting_omission）; U-4（medium severity）。§6でRI-04「否定的証拠の不完全性」パターンとして記録予定。

---

**SRG-4 [Scope claims exceed data]**（B-5, U-3, B-7）

* **Primary RI**: RI-07 [Unsupported boundary] — 「a variety of aromatic systems」という表現は芳香族ケトン以外の指向基を示唆するが、全13ランはカルボニル指向基のみ。「practically applicable」という境界主張も、実用条件への外挿が未試験のまま。
* **Secondary RI**: RI-01 [Reporting integrity] — B-7（「both starting materials」からの定量収率）はオレフィンの物質収支が未追跡であり、報告単位が一貫していない。
* **ER**: 「variety of aromatic systems」の主張には最低限、カルボニル以外の指向基（アルデヒド、エステル、イミン）の少なくとも1例のpositive controlまたはexplicitな適用範囲の限定が必要。オレフィンの物質収支は、特にトリエトキシビニルシラン（runs 1, 8–12）で副反応（異性化、加水分解）の有無を確認する必要がある。
* **EP**: EP-07a [Boundary-test pack]; EP-01a [Reporting-coherence pack]
* **Case-specific実装**:
  - EP-07a: ケトン以外の指向基（アセトアルデヒド、アセタート、アセトアニリド）との反応を3例試験し、不反応の場合は原料回収率をGCで報告。または抄録・本文の「aromatic systems」を「aromatic ketone systems」に限定記述。
  - EP-01a: オレフィン消費率をGCで追跡（runs 1, 8–12で特に重要）。1H NMRまたはGCによりオレフィンの異性化ピーク・二量化生成物の有無を報告。
* **注記**: U-3（V1 high severity, V1のみ; single-agent）; B-5（mixed: intentional_narrowing + methodological_limitation）; B-7（reporting_omission; 物質収支未追跡）。CLA-2（D-4-8）は実用条件外挿という別次元でSRG-4の延長を構成する。

---

**SRG-5 [Prior art not engaged numerically]**（C-1, B-2）

* **Primary RI**: RI-09 [External superiority] — 「among the highest reported for this type of reaction」（B-2）という主張に対し、refs 11/12の数値（TON, TOF, 収率）との直接比較がない（C-1 Dropped Quantitative Benchmark）。
* **Secondary RI**: RI-01 [Reporting integrity] — TOFの実際の数値がTable 1にも本文にも不記載（分子：生成物mol数、分母：活性触媒mol数と反応時間、いずれも未定義）。
* **ER**: TOF比較を主張するには、少なくともruns 1, 9, 10でのTOF値（h⁻¹単位）を本文またはTable 1に記載し、引用対象（refs 11/12）の対応する数値と共通基質または等価条件で比較する必要がある。
* **EP**: EP-09a [Internal benchmark pack]; EP-01a [Reporting-coherence pack]
* **Case-specific実装**:
  - EP-09a: runs 1, 9, 10の反応速度プロフィール（時間点≥3）からTOF（h⁻¹）を算出し、refs 11（Jordan & Taylor, 1989）とref 12（Moore et al., 1992）の報告値と対照表を作成。共通の実験条件が存在しない場合は「直接比較不可」と明記し定性的比較に留める。
  - EP-01a: 「equally effective」（B-3, Ru(CO)₂(PPh₃)₃）の記述を収率・基質・時間を付して定量化。
* **注記**: C-1（Dropped Quantitative Benchmark; affects_claims: yes; symmetric_pattern: partial）; B-2（V1=high, V3=high; convergence 2/3; TEMPERATURE: high_convergence_low_gap）。SRG-1（B-2）と部分的重複：B-2はRI-01（基盤不在）とRI-09（外部比較不在）の両面を持つ。SRG-1はPrimaryをRI-01に、SRG-5はPrimaryをRI-09に設定して分担。

---

**SRG 外：CLA**

**CLA-1: キレーション補助先例引用の酸化状態マニホールド不整合**（D-4-7）

* **Primary RI**: RI-06 [Imported model] — Mn(I)求電子的メタレーション（ref 14）とRu(II)カルボキシラートサイクル（ref 15）からの「類似中間体」がRu(0)酸化的付加機構の先例として輸入されているが、酸化状態・metal center・反応条件のいずれも異なる（B-11, C-2, C-4）。
* **Secondary RI**: RI-05 [Qualitative overread] — 「products similar to the intermediate postulated in Fig. 1」という定性的類似性から機構的先例を推論している。
* **ER**: refs 14/15の類似性を機構的先例として使用するには、少なくとも①Ru(0)からの酸化的付加と②Mn(I)/Ru(II)からの求電子的メタレーションが同一の金属-炭素結合を生成することを実験的または計算的に示すか、③酸化状態の差異を明示して「構造的類似体」と「機構的前例」を区別する必要がある。
* **EP**: EP-06a [Analogy-validation pack]
* **Case-specific実装**: Ru(0)（例：Ru(CO)₂(PPh₃)₂）とアセトフェノンの化学量論反応で生成する錯体をrefs 14/15の生成物（Mn/Ru系環状メタレート）と¹H/³¹P NMRスペクトルで直接比較。または現代のDFT計算でRu(0)酸化的付加経路の遷移状態エネルギーを算出し、求電子的メタレーション経路と区別する。
* **注記**: C-2（affects_claims: yes; Mn(I)先例の酸化状態差異）; C-4（affects_claims: yes; refs 8-10のキレーション化学量論先例）; B-11（mixed: intentional_narrowing + methodological_limitation）。SRG-2（RI-03が Primary）と連動するが、CLA-1のPrimaryはRI-06（モデル輸入）であり、「中間体が存在するか（RI-03）」と「モデルが正当に輸入されているか（RI-06）」は論理的に独立した問い。RI-06とRI-05の共起パターンを§6で記録予定。

---

**CLA-2: 「実用的有機合成」主張の実用条件外挿可能性**（D-4-8）

* **Primary RI**: RI-07 [Unsupported boundary] — 「efficiency, selectivity and generality required for practical organic synthesis」という境界主張を2 mol%・135℃・実験室スケールのデータのみから導出（B-6: 触媒量の非対称な増量あり; B-7: オレフィン物質収支未追跡）。
* **Secondary RI**: RI-08 [Unquantified reliability] — 「practical」を支持する反復・スケールアップ試験が存在しない。
* **ER**: 「実用的」の主張には触媒量削減実験（≤0.5 mol%でのTON試験）またはmmolスケール以上での単離収率確認のいずれかが最低限必要。135℃還流という高温条件の工業的有用性に言及するならば、スケールアップ時の熱管理または代替溶媒/温度条件の評価も必要。
* **EP**: EP-07a [Boundary-test pack]; EP-08a [Replication / uncertainty pack]
* **Case-specific実装**:
  - EP-07a: 代表基質（run 9: ピバロフェノン/トリエトキシビニルシラン）でのTON試験（触媒量0.1 mol%および0.5 mol%）。または0.5 mmol→5 mmolへのスケールアップ実験での単離収率報告。
  - EP-08a: B-6で三連投入（6 mol%×3）によりrun 5/6の収率再現性を確認。
* **注記**: B-6（触媒量の非対称性・rationale未記述）; B-7（オレフィン消費・物質収支未追跡）; B-1と部分的重複（単離収率の大部分が不明）。SRG-4（RI-07が共通）と連続するが、SRG-4のRI-07は「スコープ境界の根拠」であり、CLA-2のRI-07は「実用条件境界の根拠」という異なる対象。

---

### §3 現在のVQ判定

**現在判定: VQ-1 (Observation)** ——VQ-2 未達

---

**VQ-1 [Observation]** ← RI-02 の解消が必要

13例の反応生成物は「standard methods で構造を確認した」と記述されており、GC収率または単離収率（一部）が報告されている。RI-02（Object identification）の観点では、1993年のNature Communications の genre convention 内で、GCによる同定と「standard methods」への言及が最低限の構造確認として受理される水準にある。

**致命性判定**: Non-fatal（Era-norm依存）——B-4（「standard methods」未定義）は現代基準では不十分だが、1993年当時のNature format では許容される水準であった（§4参照）。VQ-1は通過するが、B-4の現代的意味でのRI-02解消は不完全である点を留保する。

→ **VQ-1 [Observation] は通る**（era-norm non-fatal として留保付き）。

---

**VQ-2 [Method]** ← RI-01 + RI-07 の解消が必要（VQ-1 継承）

VQ-2継承前提：VQ-1の通過を確認（上記）。

RI-01（Reporting integrity）：SRG-1が示す通り、GC収率の算出基盤（内部標準・較正曲線）が不明であり、13例中10例で単離収率が未報告。TOF比較主張（B-2, SRG-5）に必要なTOF数値そのものが不記載。これはmethod levelでの横比較不能を意味し、**Fatal**（Era-norm依存：1993年Nature communicationでは部分的に許容されたが、TOF優位性主張を伴う場合は現代では致命的）。

RI-07（Unsupported boundary）：SRG-4とCLA-2が示す通り、「a variety of aromatic systems」および「practical organic synthesis」という境界主張が、ケトン指向基のみ・実験室スケールのみのデータから導出されており未検証。**Fatal**（現代基準）。

VQ-2到達には少なくともRI-01の解消（EP-01a: GC定量法の明示 + runs 1,9,10の実TOF値記載）とRI-07の最低限の解消（EP-07a: 適用範囲の明示的限定または境界試験）が必要。

→ **VQ-2 [Method] は未達**。未解消RI: RI-01（Fatal, Era-norm依存）、RI-07（Fatal）。

---

**VQ-3 [Mechanism]** ← RI-03 + RI-04 + RI-06 の解消が必要（VQ-2 継承）

VQ-2が未達のため、VQ-3は継承原則上到達不能。ただし分析的情報として評価する：

RI-03（Unobserved explanatory）：SRG-2の中核。環状メタレート中間体（Fig. 1）が直接観測されておらず、Ru(0)活性種の実在も未確認。機構の「速度決定的説明種」の非存在は**Fatal**（現代基準では機構主張の基礎として受理不能）。

RI-04（Unreplicated discriminator）：SRG-3。1-インダノン不反応（B-9）という単一否定的証拠がリング歪み帰属の唯一の根拠として使用されており、代替解釈（電子・立体効果）が排除されていない。**Non-fatal**（観察の事実性は損なわれないが機構帰属は限定的）。

RI-06（Imported model）：SRG-2とCLA-1。Ru(0)触媒サイクル全体がMn(I)/Ru(II)先例から輸入されており、酸化状態の差異を議論していない。**Fatal**（機構の信頼性根拠が崩れる）。

*注：RI-05が重大に残る場合はVQ-3(qualified)となるが、SRG-3のRI-05（速度差のqualitative overread）はVQ-3到達の妨げとなり、VQ-3 qualified が上限となる。*

→ **VQ-3 [Mechanism] は未達**（VQ-2が前提条件として未達のため、加えてRI-03/RI-06が致命的なため）。

---

**VQ-4 [Benchmark]** ← RI-08 + RI-09 の解消が必要（VQ-3 継承）

VQ-3未達のため、VQ-4は到達不能。

---

**層別VQ非対称性の検出**

§1で確認した「三軸独立 × 機構共通基盤依存」構造に基づき、層別評価を行う：

- **観察層（Observation layer: 収率・選択性・スコープのデータ事実）単独では**：VQ-1は通る（RI-02: Era-norm non-fatal）。基質スコープと収率の観察事実は独立して保持される。この層は論文の最も堅牢な部分。
- **定量報告層（Quantitative reporting layer: SRG-1, SRG-5）**：VQ-2未達（RI-01, RI-09が未解消）。効率・TOF優位性の数値的根拠が最も脆弱な部分。
- **機構説明層（Mechanism layer: SRG-2, CLA-1）**：VQ-3未達（RI-03, RI-06が致命的）。「なぜ機能するか」の説明は実験的根拠を持たない。

→ **論文の主張のうち最も堅牢なのは「13例の反応が高収率・位置選択的に進行するという観察事実」であり、最も脆弱なのは「Ru触媒サイクルの機構説明」および「TOF比較優位性の定量的根拠」である。**

---

### §4 Era-Norm Annotation

**communication-era tolerated（1993年 Nature 3頁 Articles format で許容された欠落）：**

- **B-1（GC収率の較正法未記載）**: 1993年当時のNatureおよびJACS communicationsでは、GC収率の内部標準・較正曲線の詳細は Method/SI に記載せず本文は「GC収率」のみとする慣行が広く許容されていた。デジタルSIの普及は1990年代後半以降。
- **B-4（「standard methods」の未定義）**: 1993年のNature Articlesにおける構造確認の記述として「standard methods」への言及は受理される最低限の記述であった。¹H NMR + 元素分析またはHRMSが要求され始めたのは2000年代以降のACS/RSC journals。
- **B-3（触媒比較の定性記述のみ）**: 3頁コミュニケーション形式の紙幅制約の範囲内で、「equally effective」「not effective」の定性表現が許容された。数値データはfull-paper展開で補完されることが期待される genre convention 内。
- **B-9（1-インダノンの「not shown」）**: Negative resultを「not shown」で参照することは、1993年のNature Articles format での許容範囲内。現代のACS Catalysisでは "see SI" が必須。
- **B-6（runs 5/6での触媒量増量の rationale 未記述）**: 3頁コミュニケーションの条件変動は本文での詳細説明なしが許容された。
- **B-7（オレフィン消費・物質収支の未追跡）**: 触媒的C-H官能化の初期報告として、生成物の確認を優先し出発オレフィンの物質収支追跡を省略することは1993年コミュニケーション形式では許容範囲内であった。

---

**modern-era deficient（現代の再認定では許容できない欠落）：**

- **B-2（TOF値の不記載）**: 「among the highest reported」という比較優位主張を行いながら数値を示さないことは、現代のACS Catalysis、Nature Catalysis、Angew. Chemieでは受理不能。VQ-2到達に直接抵触するRI-01の致命的インスタンス。
- **C-1（refs 11/12との定量比較なし）**: 効率・汎用性の優位性主張の根拠として必要な対照実験が欠如。現代の競争的触媒化学では直接比較実験なしの優位性主張は査読で否定される（RI-09, VQ-4前提）。
- **U-1（中間体の実験的未確認）**: 触媒サイクルの律速的中間体を実験的に示さずに機構を主張することは、現代のorganometallic catalysis journalでは致命的（RI-03）。RI-03のFatal判定は現代基準に基づく。
- **U-2（Ru(0)活性種の未確認）**: 前触媒の活性化機構（Ru(II)→Ru(0)変換）を未確認のまま「low-valent Ru」を前提とすることは、現代のin situ分光分析（NMR, XANES）が標準化された環境では受理不能。
- **B-10 / U-4（位置選択性の検出下限未記述）**: 「virtually 100%」の主張に対し非観察異性体の検出下限が不明なことは、現代のchiral HPLC・高感度GC分析が利用可能な環境では RI-01 の致命的インスタンス。
- **D-4-9（KIE未測定）**: C-H結合開裂が律速段階かどうかの判定に不可欠なkH/kD測定の不在は、現代の機構化学では機構論文として受理されるための必須要件（RI-03と連動）。

*注：B-2とB-4は「communication-era tolerated（形式的）かつmodern-era deficient（実質的）」の両タグに記載。B-2のTOF未記載は当時の紙幅制約で免除されたが、「最高レベル」という優位性主張を行った以上、現代基準では免除されない。*

---

### §5 最短補強ルート

**5a. 目的関数の設定**

現在VQ-1（通過, era-norm留保） → **第一目的関数: VQ-2 [Method] への到達**
VQ-2 → **第二目的関数: VQ-3 [Mechanism] への到達**（VQ-2前提）

---

**VQ-2 への最短ルート：**

1. **EP-01a [Reporting-coherence pack]** — GC収率の定量基盤（内部標準種・較正曲線）を明示し、runs 1, 9, 10の単離収率と実際のTOF値（h⁻¹）をTable 1に追記することでRI-01を前進させ、RI-08も部分的に前進。
   → RI-01を前進（SRG-1 Primary + SRG-5 Secondary）。

2. **EP-09a [Internal benchmark pack]** — refs 11/12の文献TOF/収率値を掘り起こし、runs 1, 9, 10のTOF値と対照表を作成（共通条件不在なら明記）することでRI-09を前進。
   → RI-09を前進（SRG-5 Primary）。

3. **EP-07a [Boundary-test pack]** — 非ケトン指向基（アルデヒド・エステル1例ずつ）の適用試験または抄録の明示的限定（「aromatic ketone systems」）によりRI-07を前進。実用条件試験（触媒量低減: 0.5 mol%試験）をCLA-2のRI-07同時対応として実施。
   → RI-07を前進（SRG-4 + CLA-2）。

**VQ-2到達には手順1+3が最小限必要。手順2はVQ-4前提条件のため早期に実施が望ましい。**

---

**VQ-3 への最短ルート（VQ-2到達後）：**

4. **EP-03a [Direct-observation / state-assignment pack]** — 化学量論的環状メタレーション反応（RuH₂(CO)(PPh₃)₃ + アセトフェノン, toluene, 135°C）の¹H/³¹P{¹H} NMR観測でFig. 1中間体の存在を確認。またはD₂ラベル実験（重水素化アセトフェノン）によるC-D結合開裂のトレース（KIE測定を兼ねる）。
   → RI-03を前進（SRG-2 Primary + D-4-9連動）。最大情報利得（RI-03 + D-4-9のKIE問題を同時解消）。

5. **EP-06a [Analogy-validation pack]** — Ru(0)酸化的付加 vs 求電子的メタレーションの生成物同一性をNMR比較またはDFT計算で評価し、CLA-1のRI-06を前進。
   → RI-06を前進（SRG-2 Secondary + CLA-1 Primary）。

6. **EP-05a [Quantitative-ranking substantiation pack]** — ラン10/11の反応速度プロフィール（初期速度算出）でリング歪み帰属に速度論的根拠を付与し、RI-05を前進。
   → RI-05を前進（SRG-3 Primary）。VQ-3 qualified → VQ-3 の条件。

**VQ-3到達には手順4+5が必須（RI-03とRI-06が致命的）。手順6はRI-05残存によるVQ-3 qualified → VQ-3解消のために追加。**

**情報利得順位：EP-03a（D-4-9 KIEを兼ねRI-03+KIEを同時前進）> EP-01a（RI-01+RI-08部分前進）> EP-09a（RI-09）> EP-06a（RI-06）> EP-07a（RI-07）> EP-05a（RI-05）**

**Top-3 EP（情報利得順）:**
1. EP-03a — 最大情報利得（RI-03: SRG-2 Fatal + D-4-9 KIE同時前進）
2. EP-01a — VQ-2到達の必須要件（RI-01: SRG-1 Fatal前進）
3. EP-09a — SRG-5の根本解消（RI-09: TOF比較定量化）

認定ゲート順注記：実験投入順は情報利得順（EP-03a > EP-01a > EP-09a ...）だが、最終的なVQ認定は継承原則に従い VQ-1 → VQ-2 → VQ-3 → VQ-4 のゲート順で確定する。EP-03aはVQ-3前進だが、VQ-2未達のままVQ-3が正式に認定されることはない。

---

### §6 制度設計への寄与

**1. 既存 RI コードの新代表事例**

**RI-06「サイクルレベル輸入」の明確な事例提供：**
本論文のSRG-2・CLA-1は、RI-06の「サイクルレベル輸入」スコープ注記（v0.2a）の典型事例を提供する。個別素反応（ref 17: アクリル酸エステルのRu酸化的付加）だけでなく、触媒サイクル全体の構築にMn(I)/Ru(II)求電子的メタレーション先例（refs 14/15）を輸入しており、酸化状態マニホールドの差異（Ru(0)→Ru(II) vs Mn(I)→Mn(III)求電子的）が議論されていない。Kumada 1972（Ni触媒の先例なし輸入）と異なり、Murai 1993は先例を引用しているにもかかわらず機構的差異を議論しないパターンであり、「先例引用あり・機構差異未議論」という RI-06の distinct subtype を構成する可能性がある。

**RI-03「Available-but-unutilized characterization」との区別：**
本論文ではRI-03は「取得済みデータの未活用」（RI-03サブタイプ: Available-but-unutilized）ではなく「実験そのものが未実施」（classic RI-03）の形で現れる。1-インダノンの「not shown」（B-9）は実験済みデータの非報告であり、RI-03サブタイプの境界事例となる。

---

**2. 否定的証拠の不完全性パターン（RI-04 case-specific実装の追加）**

SRG-3のB-9（1-インダノン不反応→リング歪み帰属）は、§6指示の「否定的証拠の不完全性」パターンに正確に合致する：
- 陰性実験（1-インダノンが全く反応しない）が肯定的機構証拠（「リング歪みが阻害する」）として使用。
- 質量収支閉鎖（原料回収率のGC確認）が欠如。
- 速度論的ウィンドウ評価（検出可能な反応速度の下限）が未記述。
- さらに「not shown」という形で元データが原著に公開されていない。

これはKumada 1972のような「データが原著内に一部存在するが機構帰属に活用されていない」場合と異なり、「実験済みデータが公開されないまま帰属に使用」されているという特有のパターン。RI-04 case-specific実装に「陰性実験のデータ非公開 + 機構帰属への使用」という条件を追記することを提案する。

---

**3. 標識不整合（Labeling mismatch）パターンの確認**

A-1（「[REDACTED: verbatim source text; see the source paper via its DOI]」）という明示的機構留保が論文末尾（p.531 Possible mechanisms節末尾）に置かれているにもかかわらず、Abstract（「[REDACTED: verbatim source text; see the source paper via its DOI]」）では事実的記述語が使用されている。これは「仮説標識が末尾1文に集約」される「標識不整合」パターンの典型事例：

- 仮説標識の位置: p.531 Possible mechanisms節末尾（「[REDACTED: verbatim source text; see the source paper via its DOI]」）。
- 事実的記述語の位置: Abstract（p.529 右段 "the low-valent ruthenium becomes coordinated..."）および Fig. 1 caption（中間体を「the cyclometallated intermediate」として叙述）。

Abstract（読者への第一印象）で機構が事実として叙述され、Possible Mechanisms節末尾で「まだ明確でない」と留保される構造は、読者の機構理解に系統的なバイアスを与える。これはRI-06（Imported model）と連動し、§6指示に従い記録する。

---

**4. 通信→Full Paper 遷移の自動解消パターン**

SRG-1（B-1, B-3, B-4）とSRG-4（B-7）の複数B項目は、Nature 3頁コミュニケーション形式に起因しており（Stage 2 D-3 journal_constraint参照）、Full Paper展開で自動的に解消される可能性が高い。実際、Kakiuchi & Chataniグループは1993年以降J. Am. Chem. Soc.やJ. Org. Chem.でのFull Paper展開でGC較正データ・触媒スクリーニング詳細・機構研究を順次報告したことが外部推論として期待される（GAP-3）。

この「通信→Full Paper遷移の自動解消パターン」は§4のcommunication-era toleratedと整合しており、Era-NormとA項目の対応関係の好例を提供する。RI-01とRI-07の通信形式起因インスタンス（B-1, B-3, B-7）はFull Paper展開で解消される一方、B-2（TOF値不記載 + 優位性主張）とU-1（中間体未観測）は形式的制約を超えた設計的省略であり、Full Paper遷移で自動解消されない modern-era deficient 項目として区別される。

---

**5. PRI昇格候補の検討**

**PRI-10（Kinetic overclaim）の確認事例としての評価：**
SRG-3（B-8, B-9）はPRI-10の定義「動力学データなしに絶対的速度向上を主張」に部分的に合致する（「most efficient chelation-assisted catalyst」的主張 + 速度差の帰属）。ただしMurai 1993では速度"向上"の主張よりも速度"差の説明帰属"が主眼であり、PRI-10よりもRI-05（Qualitative overread）とRI-04（Unreplicated discriminator）の共起として捉える方が正確。PRI-10の独立確認例としては採用しない（Monnereau 2009と同型確認には不十分）。

**PRI-11（Mechanism-kinetics decoupling）の確認：**
本論文はD-4-9（KIE不在）とSRG-2（触媒サイクル機構の動力学非接続）によりPRI-11（定義：「提案触媒サイクルから速度式を代数的に導出せずに、観測速度次数との一致のみで機構を支持している」）のパターンを呈するが、厳密にはMurai 1993は速度次数すら測定していないため「速度次数との一致」すら主張していない。PRI-11の前提「速度次数の観測」が存在しないため、PRI-11の正確な確認例ではなく「PRI-11の前段階（速度データ自体の欠如）」として位置づける。

**新PRI候補の提案はなし**（既存RI-03/RI-06/RI-05の組み合わせで捕捉可能）。

---

**6. VQ判定境界条件の新知見**

「VQ-1通過（era-norm non-fatal, RI-02）+ VQ-2未達（RI-01 Fatal）」という判定パターンは、1993年Nature Communicationsという高プレステージ誌のコミュニケーション形式が、VQ-1は通過させるがVQ-2には届かないという判定をもたらすことを示している。これは「掲載誌のプレステージ」と「VQ水準」が必ずしも一致しないことを確認する知見であり、VQ判定がjournal statusではなくRI解消状況に基づくという制度設計の基本原則を支持する実例として記録する。

本ケースは既存の制度設計（RI codebook v0.2, VQ判定基準マトリクス, EP辞書）をほぼ全面的に活用できる事例であり、制度設計の適用範囲の広さを確認した。主要な追加知見は：（a）RI-06「サイクルレベル輸入」の「先例引用あり・機構差異未議論」distinct subtype候補、（b）否定的証拠不完全性に「データ非公開 + 機構帰属への使用」条件の追記提案、（c）標識不整合パターンの典型事例（Abstract事実記述語 vs Possible Mechanisms末尾留保）、（d）「通信→Full Paper自動解消」と「設計的省略（modern-era deficient）」の区別基準の精緻化、の4点。
