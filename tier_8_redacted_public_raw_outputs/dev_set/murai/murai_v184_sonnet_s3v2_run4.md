prompt_version: stage3-v2-20260416
model_info: claude-sonnet-4-6
run_id: run4
isolation_note: S2 input = murai_v184_sonnet_s2_run4.md のみ参照。他 run の S2/S3 は不参照。

# 科学的知見の再認定判定票

## Murai et al. 1993（Nature, Articles）

---

### §1 Claim Architecture

**コア主張の要約**

本論文の中心命題は「RuH₂(CO)(PPh₃)₃ が芳香族ケトンのオルト C–H 結合をキレーション補助によって選択的に活性化し、オレフィンへの触媒的付加反応を実現する」というものである。Novelty 柱は三層構造を持つ。第一は効率性（Efficiency）: 触媒的不活性 C–H 結合の官能化において、両出発材料基準で定量的収率を初めて達成したという T1 主張（[REDACTED: substantial verbatim quotation; see Tier 9]）。第二は一般性（Generality）: 従来の先行反応が [REDACTED: substantial verbatim quotation; see Tier 9] であったのに対し、アシルベンゼン（runs 1–11）および複素芳香族ケトン（runs 12–13）を含む広範な基質と多様なオレフィンの組み合わせに適用可能という T1 主張。第三は選択性（Selectivity）: 芳香族の *ortho* 位選択性とオレフィンの anti-Markovnikov 選択性を合わせた "virtually 100%" の位置選択性という T1 主張。Utility 柱は "required for practical organic synthesis" という実用合成への直接的訴求と、"chelation assistance" 原理が "applicable more widely for selective organometallic catalysis" という T2 展望的主張から構成される。

**Layered structure の判定**

独立層構造（layered structure）が成立している。効率性・選択性・一般性の三層はそれぞれ異なる実験的根拠（Table 1 の収率数値、位置選択性記述、基質スコープの数）に依拠しており、単一の反証で全体が崩れる構造ではない。さらに T2 の "chelation assistance" 原理の一般性はメタ主張として付加されており、Table 1 全体の反証によっても独立に生き残りうる。ただし、三層の主張はすべて「キレーション補助による C–H 活性化」という単一の機構的原理を前提としており、その原理的根拠（環状金属中間体の存在）が否定された場合には三層への遡及的損傷が生じる構造的依存関係が存在する。機構が "not yet clear" と明示的に延期されることによって、この依存関係は論文の主張体系から切り離されており、実験的主張と機構的主張が意図的に分離されている。

**層間依存関係:**
- 効率性・一般性・選択性の三層 → 実験的独立（Table 1 の数値に各々直接接続）
- 三層すべて → 機構的原理（キレーション補助）への潜在的依存（ただし論文内では意図的に切り離し済み）
- T1 効率性主張の「最高水準」という比較的側面 → 先行文献との定量的比較不在（SRG-5）に依存

---

### §2 SRG / CLA → RI / ER / EP Crosswalk

---

**SRG-1 [Quantitative evidence base]**
member_items: B-1, B-2, B-3, B-4

* **Primary RI**: RI-01 [Reporting integrity] — GC 収率報告の較正条件（内部標準・応答係数）が未記載、TOF 数値が Table 1 にも本文にも記載されず "among the highest" という比較主張を横比較不能にする、代替触媒の比較実験が定性的記述（"equally effective", "modestly effective", "not effective"）のみで条件・収率未記載。これらはすべて「報告単位・測定フレームの不統一による横比較不能」という RI-01 の定義に収まる。
* **Secondary RI**: RI-08 [Unquantified reliability] — 13 run のうち 10 run が単一測定の GC 収率のみ報告し、繰り返し測定や不確かさ記述がない（B-1）。B-6（runs 5–6 の触媒量 3 倍増加に理由なし）は内部矛盾型 RI-08 サブタイプとも対応する。
* **ER**: Table 1 の収率数値が独立再現の基準として機能するためには、少なくとも GC 較正方法（内部標準化合物名・応答係数）の開示、TOF 計算に用いた反応時間と転化率の明示、および代替触媒比較実験の定量的条件が必要である。
* **EP**: EP-01a [Reporting-coherence pack]; EP-08a [Replication / uncertainty pack]
* **Case-specific 実装**: （EP-01a）GC 較正用内部標準（例: n-テトラデカン、ドデカン）の導入と応答係数補正係数の Supplementary 開示。runs 1, 9, 10 の TOF 計算に必要な反応時間分割収率データ（0.5 h 時点、1 h 時点等）の Table 1 への追加。代替触媒 Ru(CO)₂(PPh₃)₃ 等の比較実験について、基質・溶媒量・温度・時間・GC 収率を統一フォーマットで記載。（EP-08a）少なくとも代表的 2 run（例: runs 9, 10）の反応を独立 n=3 で繰り返し、平均±標準偏差を報告。
* **注記**: B-1（TEMPERATURE_SUMMARY: high_convergence_low_gap, V1=high, V3=high, convergence 2/3）; B-2（high_convergence_low_gap, V1=high, V3=high, convergence 2/3）; B-3（high_convergence_low_gap, V1=medium, V2=medium, V3=medium, convergence 3/3）; B-4（単一エージェント V3、構造決定の詳細未記載）。

---

**SRG-2 [Catalytic cycle evidence absent]**
member_items: A-1, U-1, U-2

* **Primary RI**: RI-03 [Unobserved explanatory] — 触媒サイクルの中核を担う環状金属中間体（Fig. 1 の cyclometallated intermediate）が単離・NMR 観察・トラッピング実験いずれによっても直接観測されておらず、Ru(II) 前駆体 RuH₂(CO)(PPh₃)₃ から触媒的活性種 Ru(0) への変換機構も実験的に未確認である。提案サイクルの唯一の「可能な機構」としての Fig. 1 は、直接的実験的証拠のない推定種に全面的に依存している。
* **Secondary RI**: RI-06 [Imported model] — 環状金属中間体の構造的妥当性の唯一の根拠として、Mn(I) 化学量論的環状化（ref 14）と Ru(II) カルボキシラートからの化学量論的環状化（ref 15）を引用しているが、これらは本論文の提案する Ru(0) 触媒的酸化的付加機構とは異なる酸化状態・条件下の反応であり、同型性が実証されていないモデルの輸入（RI-06）に該当する（B-11, C-2）。
* **ER**: 提案された触媒サイクルが機構的議論の根拠として機能するためには、少なくとも (i) 環状金属中間体の化学量論的単離または低温 ³¹P{¹H} NMR による観測、あるいは (ii) Ru(II) 前駆体の活性化実験（誘導期測定、H₂ 発生確認、または Ru(0) ソース等価物の比較実験）のいずれかが必要である。
* **EP**: EP-03a [Direct-observation / state-assignment pack]; EP-06a [Analogy-validation pack]
* **Case-specific 実装**: （EP-03a）RuH₂(CO)(PPh₃)₃ と代表的芳香族ケトン（例: アセトフェノン）を化学量論比で混合し、低温（−30°C 等）での ³¹P{¹H} NMR を取得して Fig. 1 の環状金属中間体に対応するシグナルを帰属。KIE 実験として重水素化アセトフェノン（*d*-アセトフェノン）との競合実験を実施して C–H 切断が速度決定段階かどうかを確認。（EP-03a: Ru(II)→Ru(0) 活性化）RuH₂(CO)(PPh₃)₃ の反応開始時の誘導期を UV-Vis または ³¹P{¹H} NMR でモニタリングし、H₂ 発生確認のために反応系を閉管で実施して GC 分析。（EP-06a）Mn(I) 系（ref 14）および Ru(II) カルボキシラート系（ref 15）の単離中間体を本論文の触媒条件下で基質として用い、類比の成立を実験的に検証。
* **注記**: A-1（機構延期の明示的宣言 "not yet clear"）; U-1（TEMPERATURE_SUMMARY: high_convergence_low_gap, V2=critical, V3=critical, convergence 2/3, self-contradictory absence）; U-2（low_convergence_high_gap, V2 単独 critical; self-contradictory absence）。SRG-2 は論文の三層の novelty claims すべてへの潜在的依存経路を持ち、最も機構的に根本的な SRG である。RI-06: サイクルレベル輸入の注記（v0.2a）が該当: 触媒サイクル全体を Mn(I)/Ru(II) の別系から構成している。

---

**SRG-3 [Selectivity basis absent]**
member_items: B-8, B-9, B-10, U-4

* **Primary RI**: RI-05 [Qualitative overread] — runs 10/11 の速度差（0.5 h, 100% vs. 20 h, 88%）を ring strain のみで帰属し（B-8）、1-indanone の不反応性を ring strain で帰属する（B-9）いずれの場合も、速度定数・活性化パラメータ・競合経路の排除実験が提供されていない。"virtually 100%" の位置選択性主張（B-10, U-4）も、非観察異性体の検出下限が示されていない。
* **Secondary RI**: RI-07 [Unsupported boundary] — "did not react at all" という否定的境界主張が、1-indanone の不反応性を ring strain 仮説の証拠として使用しているが、不反応を確認するための対照実験条件・反応時間・GC 検出限界が示されていない（B-9; RI-07 拡張適用: 否定的境界主張）。
* **ER**: "virtually 100%" という選択性主張が機構的含意を持つためには、少なくとも (i) 代表的 run での GC/NMR による非観察 3 種の位置異性体の検出限界（%）の明示、および (ii) runs 10/11 の速度差帰属に対する速度定数測定または代替説明（立体・電子効果）の排除実験が必要である。
* **EP**: EP-05a [Quantitative-ranking substantiation pack]; EP-07a [Boundary-test pack]
* **Case-specific 実装**: （EP-05a）runs 8, 13（芳香族選択性）および全 run のオレフィン選択性について、非観察位置異性体を合成標品として調製し、反応混合物に既知量添加した標準添加 GC 法で検出下限（例: <0.5%）を決定。run 9（α-テトラロン）と run 11（β-テトラロン類似体）について時間分割 GC で収率プロファイルを取得し、初速度から速度定数を算出。（EP-07a）1-indanone を run 10 と同一条件で試験し、GC によって不反応（<1% 生成物）を定量的に確認。五員環 vs. 六員環チェラート中間体の ring strain 推定を分子モデリングまたは X 線構造比較で定量化。
* **注記**: B-8（TEMPERATURE_SUMMARY: high_convergence_low_gap, V1=medium, V2=high, convergence 2/3）; B-9（high_convergence_low_gap, V1=medium, V2=high, convergence 2/3, "negative result as evidence"フラグ）; B-10（reporting_omission, U-4 に連動）; U-4（medium severity, self-contradictory absence）。RI-05 が重大に残存するため、SRG-3 の解消なしには VQ-3 の "Qualified" 条件が維持される（*注1 参照）。

---

**SRG-4 [Scope claims exceed data]**
member_items: B-5, U-3, B-7

* **Primary RI**: RI-07 [Unsupported boundary] — アブストラクトの "a variety of aromatic systems" という表現は、ケトン指向基以外の芳香族系への適用性を示唆するが、Table 1 の全 13 run はアシルベンゼンまたはアシルヘテロ芳香族ケトンのみで構成されており、アルデヒド・エステル・アミド・イミン・非カルボニル指向基への適用は示されていない（B-5, U-3）。B-7（[REDACTED: substantial verbatim quotation; see Tier 9]）はオレフィンの消費経路（異性化・オリゴマー化）のモニタリングなしに断言されており、境界条件を試験せずに主張している。
* **Secondary RI**: RI-01 [Reporting integrity] — "based on both starting materials" という双方向定量的収率主張（B-7）が、オレフィン消費の独立的定量なしに提示されており、収率基準の不統一（芳香族ケトン基準 vs. 双方向基準）が横比較を困難にしている。
* **ER**: "a variety of aromatic systems" という一般性主張が支持されるためには、少なくとも 1 種の非ケトン指向基（例: アルデヒド、イミン、または 2-ピリジル）を持つ基質で同等の収率・選択性が実証される必要がある。"based on both starting materials" という双方向収率主張については、オレフィンの消費を独立した GC または ¹H NMR で定量する必要がある。
* **EP**: EP-07a [Boundary-test pack]; EP-01a [Reporting-coherence pack]
* **Case-specific 実装**: （EP-07a）非ケトン指向基として 2-アシルフラン（既に runs 12-13 で実証済み）を超えて、2-ピリジルカルボニル、ベンズアルデヒド、イミン（PhCH=NR）等の基質を標準条件下で試験。「不活性基質」として試験して境界を確認。（EP-01a）runs 8–13 の各実験について、仕込みオレフィン量と回収オレフィン量を GC で独立計測し、「both starting materials 基準の定量的収率」の数値的根拠を明示。
* **注記**: B-5（mixed classification, 意図的スコープ誇張としても読める）; U-3（high severity, self-contradictory absence; "a variety of aromatic systems" はアブストラクトの記述）; B-7（reporting_omission）。SRG-4 の解消は D-4-5 の問い（「多様な芳香族系とは実際には芳香族ケトンか」）に直接対応する。

---

**SRG-5 [Prior art not engaged numerically]**
member_items: C-1, B-2

* **Primary RI**: RI-09 [External superiority] — [REDACTED: substantial verbatim quotation; see Tier 9] という最上級比較主張が、refs 11（Jordan & Taylor 1989）および ref 12（Moore et al. 1992）の TOF/TON/収率数値を本文に引用せず、また本論文自身の TOF 数値も Table 1 に記載しないまま成立している（B-2, C-1）。外部文献値との直接数値比較なしに優位性を主張している。
* **Secondary RI**: RI-01 [Reporting integrity] — TOF 数値が Table 1 に存在しないため、"among the highest" という主張の報告単位が定義されていない（B-2）。
* **ER**: 外部文献比との TOF 優位性主張が成立するためには、少なくとも (i) 本論文 runs 1, 9, 10 の TOF 値（mol 生成物 / mol Ru / h）の明示、(ii) refs 11 および 12 の原報から抽出した対応 TOF/TON 値の本文中への引用、(iii) 共通する指標（TOF 計算法の定義）での数値比較が必要である。
* **EP**: EP-09a [Internal benchmark pack]
* **Case-specific 実装**: （EP-09a）runs 1, 9, 10 について時間分割収率測定から初速度 TOF を計算（単位: h⁻¹）。refs 11/12 の報告 TON/TOF を共通単位に換算した比較表を Table 1 の脚注または Supplementary に追加。共通 benchmark として、runs 1, 9, 10 と同一の芳香族ケトン基質での refs 11/12 系の再現実験（単一点 GC 収率のみで十分）を実施。
* **注記**: C-1（dropped quantitative benchmark: 共通基質上での定量比較なし）; B-2（TEMPERATURE_SUMMARY: high_convergence_low_gap, V1=high, V3=high, convergence 2/3）。SRG-5 は D-4-6 の問いに直接対応する。

---

**SRG 外：CLA**

---

**CLA-1: 機構的類比の酸化状態不整合**
grounded_in: B-11, C-2, C-4, C-5（SRG-2 の周辺接続だが独立 CLA として記録）

論文が Fig. 1 の環状金属中間体を支持するために用いる refs 14–15（Mn(I)/Ru(II) 化学量論的環状化）と ref 17（アクリル酸エステルへの Ru への酸化的付加）は、本論文の Ru(0) 触媒的酸化的付加機構と酸化状態・反応型が異なる。この不整合は RI-06 [Imported model]（サイクルレベル輸入）に対応し、SRG-2 に周辺接続するが、SRG-2 は「実験的未観測」を Primary RI としており、CLA-1 は「輸入モデルの同型性未実証」という独立した論点を持つため CLA として分離記録する。

* **Primary RI**: RI-06 [Imported model]
* **ER**: 機構的類比が有効であるためには、Mn(I)/Ru(II) 化学量論的系で単離された中間体と提案 Ru(0) 系の中間体が構造的（X 線結晶構造）または分光学的（³¹P{¹H} NMR, IR）に対比される必要がある。
* **EP**: EP-06a [Analogy-validation pack]
* **Case-specific 実装**: refs 14/15 の既知単離中間体と RuH₂(CO)(PPh₃)₃/アセトフェノン系の低温 ³¹P{¹H} NMR スペクトルを比較し、機構的類比の成立を判定。
* **注記**: CLA-1 は Stage 2 の D-4-8（機構的類比は成立するか）に直接対応する。

---

**CLA-2: 実用合成条件への外挿の根拠不在**
grounded_in: B-6, D-4-9（Stage 2 からの間接）; SRG-4 の周辺

"required for practical organic synthesis" という T1 主張に対して、全実験が 135°C 還流トルエン・runs 5–6 では 6 mol% 触媒（標準の 3 倍）という条件で実施されており、「実用合成」が想定する条件（適度な温度、低触媒量、多官能基基質）への外挿が実験的に未検証である。

* **Primary RI**: RI-07 [Unsupported boundary] — 高温・単一溶媒・2 mol% から 6 mol% 触媒量という制約条件を示しながら、"practical organic synthesis" という境界を失敗例なしに主張している。
* **ER**: "practical organic synthesis" という主張の境界を確認するために、少なくとも官能基許容性（エステル、ハロゲン、ニトロ基共存下）の試験または低温化実験（80–100°C での収率比較）が必要である。
* **EP**: EP-07a [Boundary-test pack]
* **Case-specific 実装**: 標準基質（アセトフェノン + トリエトキシビニルシラン, run 1 条件）を 80°C, 100°C, 135°C で各 2 h 反応させ、温度—収率プロファイルを取得。クロロ基やエステル基を持つ芳香族ケトン（例: 4-クロロアセトフェノン）を runs 1 と同条件で試験して官能基許容性の初期評価を提供。
* **注記**: CLA-2 は SRG-4 に間接接続するが、「実用性境界の未試験」という独立した論点を持つため CLA として記録する。

---

### §3 現在の VQ 判定

**現在判定: VQ-2 (Method)（RI-05 残存のため Qualified）**

---

**VQ-1 [Observation]**

VQ-1 は通る。

RI-02 [Object identification]（生成物・触媒の構造・純度が代替候補を排除できる粒度で未確定）について: 論文は [REDACTED: substantial verbatim quotation; see Tier 9]（B-4）と述べており、1993 年の Nature Communication 形式において ¹H NMR と元素分析（または高分解能 MS）による構造確認は当時の最低限の基準を満たす。同定の根拠となる分析データ自体は（開示されていないが）存在すると推定される。"unequivocally" という記述が構造の代替候補を排除したことを主張しており、これを覆す積極的な反証は Stage 1 において記録されていない。 B-4 は RI-02 の懸念を喚起するが、当時の Genre convention 内では Non-fatal と判定される（§4 参照）。ただし VQ-1 は Era-norm 依存の形で通過しており、現代基準では §4 で記録する。

**VQ-2 [Method]**

VQ-2 は通る（Qualified）。VQ-1 の通過を前提として成立している。

RI-01 [Reporting integrity] の最重要インスタンスである B-1（GC 較正未記載）と B-2（TOF 数値未記載）は SRG-1 として記録されているが、論文が Table 1 に収率と時間の数値を提供していること、そして 1993 年の Nature Communication という Form format 制約のもとでは GC 内部標準の省略は当時の field convention 内にあること（§4 communication-era tolerated 参照）から、Method 水準の主張の成立を根底から覆す Fatal 欠陥ではないと判定する。収率と反応時間の数値が提示されており、実験の主要な Method 記述（基質量、触媒量、溶媒、温度）が揃っている。

RI-07 [Unsupported boundary] の B-5/U-3（スコープ主張の過大記述）は SRG-4 として記録されているが、本文 Generality 節では "acylbenzene derivatives" および "acylheteroaromatics" という限定語を使用しており、アブストラクトの "a variety of aromatic systems" との乖離は部分的に内部の限定記述によって和らげられている。VQ-2 の通過は Non-fatal とする。

**ただし RI-05 [Qualitative overread] が重大に残存する（SRG-3）ため、VQ-2 は Qualified として記録する。** runs 10/11 の速度差の ring strain 帰属（B-8）と "virtually 100%" の位置選択性主張（B-10, U-4）において、数値なき定性的順位から構造的・因果的含意を導出している。これは VQ-2 の通過に対する限定的注記として扱うが、致命的には至らないと判断する。

**VQ-3 [Mechanism]**

VQ-3 は未達。

RI-03 [Unobserved explanatory]（SRG-2）: 触媒サイクルの中核を担う環状金属中間体（Fig. 1）が実験的に直接観測されておらず、Ru(II) → Ru(0) 活性化機構も未確認である（U-1, U-2）。これは VQ-3 の必須解消項目 RI-03 の未解消であり、致命的（Fatal）と判定する。単離・分光学的観測・トラッピングのいずれもない状態では、メカニズム水準の主張は成立しない。

RI-04 [Unreplicated discriminator]（SRG-3 の一部）: run 9（1:1 選択的形成）の解釈が立体混雑の単一説明に依存しており、代替説明を排除した複数実験的証拠がない。

RI-06 [Imported model]（CLA-1）: 環状金属中間体の根拠として異なる酸化状態・条件の系を引用しており、同型性が実証されていない（B-11, C-2, C-4, C-5）。

未解消 RI: RI-03（Fatal, SRG-2）、RI-06（Non-fatal だが残存、CLA-1）、RI-04（Non-fatal, SRG-3 の一部）。

**VQ-4 [Benchmark]**

VQ-4 は未達。VQ-3 が未達であるため、継承原則により VQ-4 の審査に至らない。

なお、VQ-4 固有の必須解消項目として RI-09 [External superiority]（SRG-5）が未解消であることを付記する。"among the highest reported for this type of reaction" という最上級 TOF 主張が refs 11/12 との直接数値比較なしに成立している。RI-08 [Unquantified reliability]（SRG-1 の Secondary）も、繰り返し測定の不在として残存している。

---

**層別 VQ 非対称性の検出:**

§1 で同定した独立層のうち、**効率性・一般性の実験的主張（Table 1 の収率数値・基質スコープ）単独では**: VQ-2 (Method, Qualified) に到達している（RI-03/RI-06 のいずれも実験的記述自体には関与せず、機構的解釈のみに関与するため）。すなわち、「Table 1 に記録された収率数値が当時の標準的手法によって取得されたこと」という限定された主張は VQ-2 通過である。

**選択性の実験的主張単独では**: SRG-3 の RI-05 残存（"virtually 100%" の検出下限未明示）により VQ-1 と VQ-2 の境界付近に留まり、VQ-2 Qualified が上限である。

**機構的主張（Fig. 1, "chelation assistance"）単独では**: VQ-3 の必須要件 RI-03 が Fatal に残存するため VQ-2 未達、実質 VQ-1 通過のみ。

---

### §4 Era-Norm Annotation

**communication-era tolerated:**

- **B-1（GC 収率の内部標準・較正未記載）**: 1993 年の Nature 3-page Communication 形式では、GC 較正の詳細は Full Paper または SI（当時 Nature には SI 形式が整備されていなかった）に委ねることが field convention として許容されていた。当時のスペース制約のもとでは標準的な省略である。
- **B-2（TOF 数値の Table 1 非記載）**: 1990 年代初頭の有機合成系コミュニケーションでは、TOF 数値を本文に明示せず "high TOF" と記述する慣行が広く許容されていた。
- **B-4（"standard methods" による構造決定の詳細未記載）**: 1993 年 Nature Communication において ¹H NMR・元素分析による確認を "standard methods" と包括的に述べることは当時の最低限基準を満たす記述として許容されていた。
- **B-3（代替触媒の定量的条件未記載）**: 触媒スクリーニングを定性的に報告することは 1990 年代初頭の有機金属化学コミュニケーションで広く行われており、Full Paper への委任が暗黙の慣行であった。
- **A-1（機構の明示的延期 "not yet clear"）**: 合成化学系コミュニケーションにおいて機構の解明を後続研究に委ねる慣行は 1993 年において許容されており、合成的有用性の実証を最優先することが audience targeting（D-2 参照）に整合していた。

**modern-era deficient:**

- **B-1（GC 収率の内部標準・較正未記載）**: 現代の有機化学誌（JACS, Angew. Chem. 等）では GC 収率には内部標準と応答係数の開示が求められ、現代の再認定においては独立検証の基盤を欠く。両タグに該当（当時許容、現代では不足）。
- **B-2（TOF 数値の Table 1 非記載）**: 現代基準では触媒系の比較論文において TOF 数値（単位: h⁻¹）の明示は必須であり、"among the highest" という最上級主張には数値的根拠が要求される。RI-09 に直接抵触するため modern-era deficient。両タグに該当。
- **U-1（環状金属中間体の実験的未確認）**: 現代の有機金属触媒機構研究では、提案中間体に対して少なくとも NMR 観測またはトラッピング実験が要求される。RI-03 の必須要件として VQ-3 到達の致命的障壁であり、現代基準では Fatal 欠陥。
- **U-2（Ru(II)→Ru(0) 活性化の未確認）**: 現代の触媒系報告では前駆体の活性化機構（誘導期、活性化エンタルピー等）への言及が標準的に要求される。
- **B-10/U-4（"virtually 100%" 選択性の検出下限未明示）**: 現代の位置選択性主張には GC または HPLC による異性体比の定量的確認（例: >99:1 と GC 検出下限）が要求される。
- **B-9（"did not react at all" という否定的証拠の定量的裏付けなし）**: 現代では否定的結果の主張に対して反応条件の同一性確認と GC 定量による不反応確認（<1%）が求められる。

---

### §5 最短補強ルート

**5a. 目的関数の設定**

現在 VQ-2 (Qualified) → 第一目的関数: **VQ-3 [Mechanism] の達成**
VQ-4 [Benchmark] → 第二目的関数（VQ-3 達成後）

**5b. EP 投入順序の設計**

---

**VQ-3 への最短ルート:**

1. **EP-03a [Direct-observation / state-assignment pack]** — RuH₂(CO)(PPh₃)₃ とアセトフェノンの化学量論的低温反応を ³¹P{¹H} NMR でモニタリングし、Fig. 1 の環状金属中間体に対応する Ru(II)-メタラサイクルシグナルを帰属・同定する（あるいはトラッピング試薬との反応で間接観測）; RI-03 を前進（SRG-2 の Primary RI を解消）。これが全 EP の中で最も多くの RI（RI-03: VQ-3 の Fatal 阻害因子）を一挙に前進させるため最優先。

2. **EP-03a 第二実装 [Ru(II)→Ru(0) 活性化確認]** — RuH₂(CO)(PPh₃)₃ の反応開始時の誘導期を UV-Vis または ³¹P{¹H} NMR でモニタリングし、H₂ 脱離による活性化（reductive elimination）の証拠を取得; RI-03 をさらに前進（U-2 を解消）。EP-03a の第一実装と同一のインフラ（NMR 設備）で実行可能であり、逐次実装が合理的。

3. **EP-06a [Analogy-validation pack]** — refs 14/15 の既知単離中間体と 2 の中間体候補を ³¹P{¹H} NMR・IR で比較し、機構的類比の成立を検証; RI-06 を前進（CLA-1）。EP-03a で中間体が同定された後に実施することで情報利得が最大化される。

4. **EP-05a [Quantitative-ranking substantiation pack]** — runs 10, 11 の時間分割収率測定で初速度 kobs を決定し、ring strain 帰属の定量的根拠を提供; RI-05 を前進（SRG-3、VQ-2 の Qualified 状態を解除）。VQ-3 到達後の補強として位置付けるが、RI-05 の解消は VQ-2 Qualified を Full VQ-2 にアップグレードするため早期実施も合理的。

5. **EP-07a [Boundary-test pack]** — 非観察位置異性体の標準添加 GC 法による検出下限確認 + 1-indanone の定量的不反応確認; RI-07（SRG-3 Secondary）を前進。EP-05a と同時に実施可能（同一の GC インフラ）。

認定ゲート順注記: 実験投入順は情報利得順（EP-03a → EP-03a 第二実装 → EP-06a → EP-05a/EP-07a）であるが、最終的な VQ 認定は継承原則に従い VQ-1 → VQ-2 → VQ-3 → VQ-4 の順でゲートを確定する。EP-03a による RI-03 の解消が VQ-3 のゲート通過の必要条件である。

---

**VQ-4 への最短ルート（VQ-3 達成後）:**

1. **EP-09a [Internal benchmark pack]** — runs 1, 9, 10 の時間分割収率測定から TOF 値（h⁻¹）を計算し、refs 11/12 の原報から抽出した TOF/TON 値との共通単位比較表を作成; RI-09 を前進（SRG-5）。

2. **EP-08a [Replication / uncertainty pack]** — runs 9, 10 の代表的 2 run について独立 n=3 反復測定を実施し、平均±標準偏差を報告; RI-08 を前進（SRG-1 Secondary）。

3. **EP-01a [Reporting-coherence pack]** — GC 較正条件（内部標準・応答係数）の開示; RI-01 を前進（SRG-1 Primary の補完）。

認定ゲート順注記: VQ-4 の認定には VQ-3 の全要件の継承が前提である。EP-09a → EP-08a → EP-01a の順での投入が情報利得と実験的実行可能性の両面で最適である。

---

### §6 制度設計への寄与

**1. RI-03 の代表事例としての確認**

本ケースは RI-03 [Unobserved explanatory] の典型事例を提供する。環状金属中間体が論文の "key to our success" として明示的に名指しされながら、単離・分光・トラッピングのいずれの観測も提示されない構造は、RI-03 の "説明の中核を担う種が直接観測も速度論的拘束もされていない" という定義の最も純粋な形態である。特に「論文が自ら中間体を中核と呼びながら、その直接証拠を持たない」という自己矛盾的構造（U-1 の "self-contradictory absence" ラベル）は、RI-03 の サブタイプに関する以下の知見を追加する:

**RI-03 新サブタイプ候補: Self-named mechanistic keystone without evidence** — 著者自身が "key" あるいは "central" と呼ぶ中間体・状態が直接観測を欠く場合、それは単なる「未観測」ではなく、著者が意図した重要性の主張と実験的証拠の完全な乖離を示すため、RI-03 の最高優先度バリアントとして識別すべきパターン。本ケースで初確認。

**2. RI-06 のサイクルレベル輸入適用の確認**

Codebook v0.2a の RI-06 スコープ注記（"サイクルレベル輸入[REDACTED: substantial verbatim quotation; see Tier 9]サイクルレベル輸入" サブタイプの代表事例として有効である。

**3. RI-05 と RI-07 の選択性主張における共起パターン**

SRG-3（Selectivity basis absent）において RI-05 [Qualitative overread] と RI-07 [Unsupported boundary] が共起している。"virtually 100%" という選択性主張（B-10/U-4）が RI-05（数値なき定性的順位から因果含意を導出）に、"did not react at all" という否定的境界主張（B-9）が RI-07（否定的境界主張を失敗例なしに主張）に対応し、両者は「選択性の観察と境界の設定」という同一実験行為の異なる側面を構成している。この共起では、RI-05 を解消するための定量的位置異性体分析（EP-05a）が RI-07 の境界確認（EP-07a）と同一の実験インフラ（GC 定量）で達成可能であり、共起する RI の同時前進が可能な RI 共起パターンの事例として記録する。

**4. 標識不整合（Labeling mismatch）の検出**

論文は "Possible mechanisms" 節冒頭で [REDACTED: substantial verbatim quotation; see Tier 9] と明示的に仮説標識を付しているが、直後に "The reaction **may** begin with the coordination..." という条件法を用いた後、[REDACTED: substantial verbatim quotation; see Tier 9] という事実的記述語（"results in", "give"）に移行している。仮説標識（"may begin"）が冒頭 1 文のみに集約され、以後の記述が事実的語法に切り替わる「仮説標識の局所化」パターンを検出した。これは RI-06 と連動し、提案サイクルが仮説であることの注意喚起が先頭に限定されることで読者の注意が薄れる可能性がある。このパターンを §6 記録として追加する: **仮説標識の局所化（Hypothesis-label localization）** — 仮説標識が段落冒頭 1 文に集約され、以後の素反応記述が事実的記述語に移行するパターン。RI-06 のケースで出現頻度が高い可能性がある。

**5. 通信→Full Paper 遷移の自動解消パターンの確認**

B-1（GC 較正）、B-2（TOF 数値）、B-3（代替触媒定量比較）、B-4（構造決定データ）は §4 で communication-era tolerated に分類されており、これらはすべて Full Paper 展開（例: 同 Murai グループの後続 JACS/JOJC 論文）によって原理的に自動解消されるパターンである。Stage 1 の GAP-3（"Post-1993 mechanistic studies"）はこの遷移の実際の発生を示している。RI-01 の通信形式起因インスタンスが Full Paper で自動解消される典型事例として記録する。

**6. 既存制度設計の全体的な確認**

本ケースは既存の RI-01, RI-03, RI-05, RI-06, RI-07, RI-08, RI-09 すべてが単一論文に共存する事例を提供しており、VQ マトリクスの継承原則（RI-03 の Fatal 残存が VQ-3 阻害）と致命性判定の設計が論文分析のフィルタリングとして適切に機能することを確認した。新規 PRI 候補は本ケースでは検出されない（PRI-10, PRI-11 に対応するパターンは本論文の形式では顕在化しない——本論文は速度式を議論しない）。

---

---

> **Tier 8 redaction notice**: This file is a redacted copy of the corresponding Tier 3 / Tier 9 output. Verbatim source-paper quotations have been replaced by `[REDACTED: see source paper §<loc>; full text retained in Tier 9 reviewer-only deposit]` markers, preserving location references and our own analytical content. Bibliographic fields (title, authors, journal, year, DOI), analytical labels (`evidence_chain:` with B-/U-/A-/C- internal IDs), short technical terms, and our own analytical text are not redacted. The redaction was applied by `scripts/redact_for_tier8.py` and, for this version, by `scripts/build_paperA_R1_public.py` with `scripts/redact_source_ngram_runs.py` (scripts of the project repository; they are not deposited).
