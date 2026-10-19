prompt_version: stage3-v2-20260416
model_info: claude-sonnet-4-6

# 科学的知見の再認定判定票

## Race, Faulkner, Shaw, Bower 2016（Chemical Science, Edge Article）

### §1 Claim Architecture

**コア主張の要約：**

本論文はPd触媒によるオキシムエステルの環化において、ホスフィン配位子の電子的性質のみによって二元的な機構が切り替わることを主張する。電子不足ホスフィン（例: P(3,5-(CF₃)₂C₆H₃)₃）はaza-Heck環化（2電子経路）を促進し、電子豊富ホスフィン（例: P(t-Bu)₃）はSETを経由するイミニルラジカル経路（1電子経路）へ偏向させる。**Novelty柱：**「Pd触媒において配位子選択のみで二元的機構が切り替わる初の例」（脚注3:[REDACTED: substantial verbatim quotation; see Tier 9]）。**Utility柱：**「毒性・高価・スケールアップ困難な従来法に依らないイミニルラジカルヒドロアミノ化の新手法」（Table 2, 47–82%収率）。

**Layered structure：**

| 層 | 主張内容 | 反証可能性 |
|:---|:---------|:----------|
| Layer 1（合成） | 電子豊富Pdで5aが47–88%で得られる | 生成物非形成があれば崩壊 |
| Layer 2（機構） | 4つの独立プローブがラジカル経路と一致 | 複数プローブの同時失敗が必要 |
| Layer 3（概念） | 配位子制御機構スイッチはPd触媒化学で前例がない | 見落とされた先行例の発見で崩壊 |

**層間依存性：** Layer 2はLayer 1を支持するが、Layer 3はLayer 1/2と論理的に独立。Layer 1の収率への反証はLayer 3を崩さず、Layer 3への反証（先行例の発見）はLayer 1の合成的事実を無効化しない。Layer 2の崩壊はLayer 1の「機構的意味」を喪失させるが合成的事実は残る。4プローブは相互補完的であり、単一プローブの失敗でLayer 2全体は崩れない。

---

### §2 SRG / CLA → RI / ER / EP Crosswalk

---

**SRG-1「全機構実験でのマスバランス体系的不在」**（B-1, B-3, B-4, B-5, A-1）

* **Primary RI**: RI-04 Unreplicated discriminator
* **Secondary RI**: RI-08 Unquantified reliability
* **ER**: ラジカル経路の実験的証拠として提示する各プローブ実験（TEMPO捕捉、Newcomb時計、エストロン反転）において、主生成物収率に加えてマスバランスを計測・報告し、「陽性結果が支配的反応経路を代表している」ことを定量的に示すこと。
* **EP**: EP-04a Discrimination / replication pack
* **Case-specific実装**: (i) Newcomb時計プローブ（Scheme 3A）の再実験において、基質7aおよびγ-テルピネンの消費量・生成物10・未同定成分を質量収支として計測し、25%収率の改善または原因解明を報告する; (ii) Scheme 2A（TEMPO捕捉）で付加体6の収率と同時に未反応基質・他生成物の収率を示す; (iii) Scheme 4（エストロン）において50%収率の残余50%の帰属を化学的に同定する。
* **注記**: B-3（V1=high, V2=high, V3=high; convergence 3/3; gap=none）が最高収束項目。SRG-1全体はRI-04の代表的集合事例を構成し、D-4候補1の同定根拠となった。

---

**SRG-2「非Pd・非ラジカル経路を排除する対照実験の不在」**（B-2, U-2）

* **Primary RI**: RI-07 Unsupported boundary
* **Secondary RI**: RI-03 Unobserved explanatory
* **ER**: 「Pd(0)媒介SETがイミニルラジカル生成に必須である」という境界主張を支持するために、(a) Pdなし（塩基＋DMF＋熱のみ）での対照実験でラジカル環化生成物5aが得られないことを定量的に示し、(b) 熱/光/塩基による自発的N–O均一開裂経路が存在しないことを独立に確認すること。
* **EP**: EP-07a Boundary-test pack; EP-03a Direct-observation / state-assignment pack
* **Case-specific実装**: 基質1b、DMF、Et₃N、γ-テルピネン、90°C、Pdなし条件での対照実験（5aの生成量をGCまたは¹H NMRで定量、検出下限を明記）; 既存文献でのオキシムエステルN–O熱開裂の動力学データとの対比。
* **注記**: U-2は自己矛盾的不在（論文のPd(0)-SET機構がPd必須性を予測するにもかかわらず、その予測が未検証）。B-2（V1=medium, V2=high; convergence 2/3; gap=low）。

---

**SRG-3「ラジカル素反応の速度定数データの不在」**（A-5, B-11, C-5）

* **Primary RI**: RI-04 Unreplicated discriminator
* **Secondary RI**: RI-05 Qualitative overread
* **ER**: Newcomb時計プローブから公表されたシクロプロピルカルビニルラジカルの開環速度定数（~10⁸ s⁻¹; refs 19a–19b）を用いて、反応系内のラジカル捕捉または再結合の速度上限を算出し、「5-exo環化がN–Pd再結合より速い」という主張（A-5）を速度論的に裏付けること。
* **EP**: EP-04a Discrimination / replication pack
* **Case-specific実装**: Scheme 3Aの実験データ（選択的10形成、25%収率）にkring-openを適用して競合する再結合過程の速度上限をラジカル時計の論理で計算する。可能であれば時計プローブの収率を>50%に改善した条件（基質、温度、Pd負荷）での再実験を行い、速度計算の信頼性を高める。
* **注記**: C-5は引用切断（Newcomb refs 19a–19bの速度定数が適用されていない）、B-11は同実験の定量的分析ステップの省略として記録。A-5はV2=critical（convergence 2/3; gap=low）であり、機構的主張の中で最高agent評価を持つ項目。

---

**SRG-4「配位子制御SETスイッチの熱力学的・電子論的基盤の不在」**（A-5, A-6, A-7, B-10, U-1）

* **Primary RI**: RI-03 Unobserved explanatory
* **Secondary RI**: RI-05 Qualitative overread
* **ER**: 「電子豊富配位子→Pd(0)の酸化電位低下→SETが熱力学的に実行可能」という因果連鎖を定量的に裏付けるために、(a) Pd(0)/dt-bpfおよびPd(0)/P(3,5-(CF₃)₂C₆H₃)₃のサイクリックボルタモメトリーによる酸化電位測定、(b) O-ピバロイルオキシムエステルのN–O結合の還元電位測定を行い、SETの熱力学的実行可能性を確認すること。
* **EP**: EP-03a Direct-observation / state-assignment pack; EP-05a Quantitative-ranking substantiation pack
* **Case-specific実装**: (a) Pd(0)/dt-bpf錯体のDMF中サイクリックボルタモメトリー測定、および電子不足ホスフィン錯体との比較; (b) 同条件下でのO-ピバロイルオキシムエステル1bのN–O結合の還元波測定; (c) Table 1の配位子系列（Entries 6–10）においてTolman電子パラメータχとラジカル生成物収率をプロットし、機構切り替えの定量的閾値を特定するHammett/LFER解析。
* **注記**: U-1（自己矛盾的不在）がこのSRGのコアを構成。B-10（V2=high; convergence 1/3）はU-1の報告省略版として記録。SRG-4は最多A/B/U項目（5項目）を含む最大グループ。

---

**SRG-5「Scheme 5機構ステップの実験的未検証」**（A-4, A-7, U-3）

* **Primary RI**: RI-03 Unobserved explanatory
* **Secondary RI**: RI-06 Imported model
* **ER**: Scheme 5の触媒サイクルが予測する観測量——(a) p-シメン（γ-テルピネンからH移動後の副生成物）、(b) Pd(II)-ヒドリド中間体——を実験的に検出・定量し、触媒サイクルの自己整合性を確認すること。さらに、イミノ-Pd(II)中間体18の生成（N–Pd再結合）とその後のN–Pdホモリシスという代替経路の可否を独立実験で検証すること。
* **EP**: EP-03a Direct-observation / state-assignment pack; EP-06a Analogy-validation pack
* **Case-specific実装**: (a) GC-MSによるp-シメンの検出・定量（反応液中の理論量との比較）; (b) アルケン非存在下でのPCy₃/Pd(0)＋オキシムエステルの低温NMR追跡によるイミノ-Pd(II)中間体18の直接観測（Hartwig/Stahl条件に準拠）、続いてアルケン添加後の反応追跡。
* **注記**: A-4とU-3のリンク（A-4はScheme 5の未検証ステップを「deferred」として、U-3はp-シメン不検出を「自己矛盾的不在」として記録）。RI-06のスコープ注記（サイクルレベル輸入）が適用される：Scheme 5はHartwig/Stahl系とPd(I)/ラジカル系文献からの大規模モデル輸入。

---

**SRG-6「機構スイッチの配位子帰属を曖昧にする実験デザイン上の交絡」**（B-6, B-15, B-16）

* **Primary RI**: RI-01 Reporting integrity
* **Secondary RI**: RI-07 Unsupported boundary
* **ER**: 「配位子の選択のみで機構が切り替わる」という中心的主張を支持するために、配位子以外の実験変数（温度、基質種（1aまたは1b）、Pd前駆体、添加剤）を固定したうえで配位子のみを変えるマッチドペア比較実験を実施すること。
* **EP**: EP-01a Reporting-coherence pack; EP-07a Boundary-test pack
* **Case-specific実装**: 同一基質（1b）・同一Pd前駆体（Pd₂(dba)₃）・同一温度（70°C）・同一溶媒（DMF）・同一添加剤（γ-テルピネン400 mol%）の条件下で、配位子のみをP(3,5-(CF₃)₂C₆H₃)₃（電子不足）からP(t-Bu)₃またはdt-bpf（電子豊富）に変えた対比実験を実施し、3a対5aの生成モル比とマスバランスを測定する。
* **注記**: B-6（V1=medium, V3=medium; convergence 2/3; gap=none）、B-15（V3=medium）、B-16（V3=medium）。3項目の共起によりRI-01（複数変数同時変化による横比較不能）とRI-07（「solely by choice of ligand」という境界主張の実験的基盤欠如）の共起パターンを形成する。

---

**SRG外：CLA**

---

**CLA-1「電子豊富配位子クラス内収率不均一性」**（B-7）

* **Primary RI**: RI-05 Qualitative overread
* **Secondary RI**: なし
* **ER**: Table 1 Entries 6–10における電子豊富配位子の収率不均一性（S-Phos 10%〜dt-bpf 72%; 7倍超の差）について、配位子の電子的・立体的パラメータ（Tolman χ、錐角等）との相関を示し、「電子豊富配位子は一般的にラジカル経路を促進する」という一般化の定量的基盤を提供すること。
* **EP**: EP-05a Quantitative-ranking substantiation pack
* **Case-specific実装**: Tolman電子パラメータχ（またはBursted法のburied volume）をx軸、5a収率をy軸としてTable 1のEntries 1–13をプロットし、収率の電子的または立体的決定因子を特定する。
* **注記**: B-7は単一エージェント評価（V1=medium）。D-1の一般化主張「[REDACTED: verbatim source text; see the source paper via its DOI]」に直結するためCLAとして記録。

---

**CLA-2「先行イミニルラジカル法との定量的比較の不在」**（C-1, A-2）

* **Primary RI**: RI-09 External superiority
* **Secondary RI**: なし
* **ER**: 「既存プロトコルは高価・毒性・スケールアップ困難な条件を必要とする」という優位性主張を定量的に支持するために、refs 14a–14fのプロトコルと本法（Table 2）とを同一基質・同一指標（収率、基質範囲、官能基許容性）で比較したデータを提示すること。
* **EP**: EP-09a Internal benchmark pack
* **Case-specific実装**: Ref 14c（Portela-Cubillo/Walton）またはref 14f（Davies/Leonori）のプロトコルで使用されている代表的基質を本法の条件下で試験し、収率・diastereoselectivity・反応時間を並べて報告する。
* **注記**: A-2（「preliminary scope」）はTable 2の範囲の不完全さを示し、C-1は比較ベンチマークの欠如を示す。両者は合わせて「実用的優位性の主張の証拠基盤」の不在を構成する。

---

### §3 現在のVQ判定

**現在判定: VQ-1（Observation）**

**VQ-1 [Observation] は通る**
RI-02（Object identification）は非致命的。TEMPO付加体6の主ジアステレオマーはX線回折で確認（CCDC 1429194）。Newcomb時計生成物10の結合b選択的切断は2D NMR分析で同定（ESIに記載）。主生成物5a、3aの化学的同定は達成されており、構造的不確実性が機構的主張の中核を崩す状況にはない。非致命的RI-02の残存：B-9（Newcombプローブの2D NMR相関がESIに限定）、B-17（X線品質指標の欠如）。これらは構造同定の実施を否定するものではなく、完全性の問題として記録する。

**VQ-2 [Method] は未達**
VQ-1を前提として、RI-01（Reporting integrity / SRG-6）とRI-07（Unsupported boundary / SRG-2, SRG-6）が未解消。
- RI-01（SRG-6に対して致命的）: 「標準aza-Heck条件」と「ラジカル条件」の比較で、配位子・基質・温度・Pd前駆体・添加剤が同時に変化しており、「配位子のみが機構を決定する」という主張に対して測定フレームの一貫性が欠如。
- RI-07（SRG-2に対して致命的）: Pd非存在下対照実験の欠如により、「Pd(0)媒介SETが境界条件」という主張が実験的に支持されていない。

ただし**Layer 1（合成層）単独では**: Table 1のEntries 3対4/5の収率対比（93% 3a対72% 5a）はaza-HeckとSET産物の明確な切り替えを示しており、RI-01が非致命的となる水準にある。Layer 1はVQ-2（conditional）に到達している。

**VQ-3 [Mechanism] は未達**
VQ-2が未達（継承原則）、加えてRI-03、RI-04、RI-06がいずれも未解消。
- RI-03（SRG-4, SRG-5 / 致命的）: Pd(0)酸化電位・オキシムエステルN–O還元電位（SET熱力学）未測定; p-シメン・Pd(II)-ヒドリド（Scheme 5予測種）未検出; イミノ-Pd(II)中間体18（代替イミニルラジカル源）の挙動未観測。機構の説明的中核を担う種がすべて未観測。
- RI-04（SRG-1, SRG-3 / 致命的）: Newcomb時計（25%収率）からの速度定数未抽出; 全プローブ実験でマスバランス未計測; Scheme 4エストロン反転（単一実験）から機構的結論。
- RI-06（SRG-5 / 非致命的）: Scheme 5触媒サイクルはHartwig/Stahl系とPd(I)/ラジカル系文献からの大規模モデル輸入であり、本系での同型性検証なし。モデルの方向性は正しい可能性が高いが、VQ-3の本質的要件である直接検証が欠如。

RI-05が複数SRG/CLAで残存（SRG-3, SRG-4, SRG-6, CLA-1）するためVQ-3はqualifiedにすらならず、完全未達。

**VQ-4 [Benchmark] は未達**
VQ-3が未達（継承原則）、加えてRI-08（B-14: 反復測定なし）とRI-09（CLA-2: 先行法との数値比較なし）が未解消。

---

### §4 Era-Norm Annotation

**communication-era tolerated:**

- **B-1（Table 1/2マスバランス省略）**: Chemical Science Edge Article形式（5–6頁）における2016年通信慣行として、孤立収率のみの報告は標準的。
- **B-14（反復測定データなし）**: 通信形式での単回実験による収率報告は当時の慣行内。
- **B-9（Newcomb 2D NMR帰属のESI委託）**: 詳細な構造帰属データをESIに委託することは通信形式では許容されていた。
- **B-17（X線品質指標の欠如）**: CCDCアクセッション番号の提供のみで品質指標を省略することは2016年当時の短報慣行として許容範囲内。
- **B-7（配位子クラス内収率不均一性の無説明）**: 5–6頁の紙幅制約では電子的相関の系統的議論は困難であり、当時は一般化的記述で代替されることが多かった。
- **B-8（HCO₂H実験収率未記載）**: 通信形式での定性的陰性結果の記述は当時の慣行内。

**modern-era deficient:**

- **B-3（Newcomb時計25%収率の機構証拠としての使用）**: 現代の機構化学論文では、単一実験・25%収率のプローブ反応から機構的結論を導くことは不十分。反応プロファイルまたは改善条件での追試が標準となっている。
- **U-1/B-10（SETの熱力学的実行可能性の電気化学的検証の欠如）**: 2016年以降、光レドックス触媒化学の隆盛によりCVによるレドックス電位測定がSET機構を含む論文の標準的要件となっており、現代の再審査ではこれが必須とみなされる。
- **U-2（Pd非存在下対照実験の欠如）**: 現代のラジカル機構論文では、金属「必須性」を確認する対照実験が標準的に期待される。
- **SRG-6（B-6, B-15: 交絡する比較条件）**: 現代の機構化学論文では「単一変数変化の原則」に基づくマッチドペアデザインが要求され、複数変数が同時に変化する比較は主要な機構的主張の根拠として不十分とみなされる。communication-era toleratedでもあるが（当時は許容された）、現代基準では致命的に不足。

---

### §5 最短補強ルート

**VQ-2 への最短ルート：**

1. EP-01a Reporting-coherence pack — 同一基質(1b)・同一Pd前駆体(Pd₂(dba)₃)・同一温度(70°C)・同一溶媒(DMF/γ-テルピネン)の条件下で、配位子のみをP(3,5-(CF₃)₂C₆H₃)₃からP(t-Bu)₃またはdt-bpfに変えたマッチドペア実験を実施し、3aおよび5aのモル収率とマスバランスを報告する。RI-01（SRG-6）を前進させ、「solely by choice of phosphine ligand」主張の測定フレーム一貫性を確立する。

2. EP-07a Boundary-test pack — Pd非存在下（基質1b、DMF、Et₃N、γ-テルピネン、90°C）での対照実験を実施し、5aの非形成を定量的に確認する（GCまたは¹H NMR、検出限界を明記）。RI-07（SRG-2）を前進させ、「Pd必須性」という境界条件を実験的に支持する。

認定ゲート順注記：情報利得はEP-01a > EP-07aであるが（EP-01aはSRG-6の核心的RI-01を解消）、VQ-2認定はRI-01とRI-07の両解消を必要とする継承原則に従う。

---

**VQ-3 への最短ルート（VQ-2通過後）：**

3. EP-03a Direct-observation / state-assignment pack — (a) Pd(0)/dt-bpfおよびPd(0)/P(3,5-(CF₃)₂C₆H₃)₃錯体のDMF中CVによる酸化電位測定と、O-ピバロイルオキシムエステル1bのN–O還元電位測定（SETの熱力学的実行可能性を確認）; (b) GC-MSによる触媒反応液中のp-シメン検出・定量（Scheme 5触媒サイクルの予測を検証）; (c) アルケン非存在下でのPd(0)/PCy₃＋1bの低温NMR追跡によるイミノ-Pd(II)中間体18の観測。RI-03（SRG-4, SRG-5）を前進させる。

4. EP-04a Discrimination / replication pack — Newcomb時計プローブ（Scheme 3A）を改良条件で再実施して収率を>50%に改善し、refs 19a–19bの速度定数（kring-open ~10⁸ s⁻¹）を適用してN–Pd再結合の速度上限を算出する; 全成分を定量してマスバランスを閉じる。RI-04（SRG-1, SRG-3）を前進させる。

5. EP-06a Analogy-validation pack — PCy₃/Pd(0)をアルケン基質1bと低温で反応させ、中間体18を捕捉してNMR・IRで特性評価後、γ-テルピネン存在下で反応再開してラジカル生成物5aへの転化を確認する。RI-06（SRG-5）を前進させ、Scheme 5モデルの対象系における同型性を実証する。

6. EP-05a Quantitative-ranking substantiation pack — Table 1の配位子系列（Entries 1–13）に対してTolman電子パラメータχをx軸、[5a/(3a+5a)]比率をy軸とするHammett型プロットを作成し、機構スイッチの定量的電子閾値を特定する。RI-05（SRG-4, SRG-6, CLA-1）を前進させる。

認定ゲート順注記：情報利得順はEP-03a > EP-04a > EP-06a > EP-05aであるが、VQ-3認定はRI-03・RI-04・RI-06の全解消を必要とする継承原則に従う。RI-05残存はVQ-3をqualified扱いに留める可能性があるため、EP-05aの実施が正規VQ-3認定の前提となる。

---

**VQ-4 への最短ルート（VQ-3通過後）：**

7. EP-08a Replication / uncertainty pack — Table 2の主要エントリ（22a, 22b, 22d）について少なくとも重複実験を行い、標準偏差を付した収率を報告する。RI-08を解消。

8. EP-09a Internal benchmark pack — refs 14c（Portela-Cubillo/Walton）および14f（Davies/Leonori）の代表基質を本法条件で試験し、収率・選択性・反応時間を並記した直接比較表を作成する。RI-09を解消。

---

### §6 制度設計への寄与

**1. 否定的証拠の不完全性パターンの典型事例（RI-04 case-specific実装）：**

本論文はRI-04の「否定的証拠の不完全性」パターンの代表的事例を提供する。Newcomb時計（Scheme 3A: 10のみ形成、25%収率）、TEMPO捕捉の陰性（aza-Heck条件では6非生成）、β-ヒドリド脱離生成物の非観測（Scheme 3B）のいずれも、陰性または限定的な実験結果を「強い機構的証拠」として使用しているが、(i) マスバランスの閉鎖、(ii) 検出限界の明示、(iii) 観測された選択性が支配的反応経路を代表するという定量的保証がない。EP-04aのcase-specific実装として「Newcomb時計プローブにおいてkring-openを適用した速度上限計算と同時質量収支計測の組み合わせが必要」という実装例を追加できる。

**2. 標識不整合パターン（Labeling mismatch）：**

Scheme 5は明示的に「a working mechanistic hypothesis」「a plausible mechanism」と標識されているが、周辺の本文は事実的叙述語を使用している:[REDACTED: substantial verbatim quotation; see Tier 9]（generates, results in）。仮説標識はScheme 5キャプションと末尾1文（"At the present stage...cannot be discounted"）に集約され、本文の事実的記述語と対照的な構造を形成する。RI-06と連動するパターンとして記録。

**3. RI-03 + RI-06 共起パターン（SRG-5）：**

SRG-5においてRI-03（未観測説明因子: p-シメン、Pd(II)-H、イミノ-Pd(II)中間体18の未検出）とRI-06（輸入モデル: Scheme 5はHartwig/Stahl系とPd(I)/ラジカル系文献から構成）が共起する。RI-03のみの解消（中間体を観測する）では不十分であり、RI-06の解消（本系でのモデル同型性の実証）も必要。RI-03 × RI-06の共起は、Pd-N化学においてHartwig/Stahl系から機構を輸入した系において繰り返し現れるパターンとなり得る。

**4. PRI-11（Mechanism-kinetics decoupling）の追加補強事例：**

PRI-11の定義「提案触媒サイクルから速度式を代数的に導出せずに、観測速度次数との一致のみで機構を支持」はScheme 5にも適用可能:Table 2の触媒的収率（47–82%）はScheme 5のサイクル完結の暗黙的支持として機能しているが、速度式（TON ~ f(kSET, kcyclization, kHAT)）は導出されていない。SRG-3のB-11/C-5（速度定数の不適用）と連動する。既存のBreitenfeld 2014とPengfei 2024での確認があるため本論文はPRI-11昇格の追加補強事例として記録する（独立の昇格根拠ではなく補強）。

**5. Era-norm遷移型項目の境界条件：**

B-6/B-15（交絡する比較条件）が「communication-era toleratedかつmodern-era deficient」の両タグに該当する事例として記録した。この「Era-norm遷移」型の項目は通信→Full Paper遷移で自動解消されない性質のものであり（新しい実験が必要）、§4での判定境界条件の具体例としてCodebookに追加できる:「条件交絡による境界主張の実験的基盤欠如は、通信形式の紙幅制約に起因するが、Full Paper展開では自動解消されず独立実験（マッチドペア比較）が必要」。これはRI-07の拡張適用（否定的境界主張）とも連動し、era-norm判定とRI致命性判定の交差点の事例を提供する。

---

> **Tier 8 redaction notice**: This file is a redacted copy of the corresponding Tier 3 / Tier 9 output. Verbatim source-paper quotations have been replaced by `[REDACTED: see source paper §<loc>; full text retained in Tier 9 reviewer-only deposit]` markers, preserving location references and our own analytical content. Bibliographic fields (title, authors, journal, year, DOI), analytical labels (`evidence_chain:` with B-/U-/A-/C- internal IDs), short technical terms, and our own analytical text are not redacted. The redaction was applied by `scripts/redact_for_tier8.py` and, for this version, by `scripts/build_paperA_R1_public.py` with `scripts/redact_source_ngram_runs.py` (scripts of the project repository; they are not deposited).
