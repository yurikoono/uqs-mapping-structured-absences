```
prompt_version: stage3-v2-20260416
model_info: claude-sonnet-4-6
```

# 科学的知見の再認定判定票

## Tamao, Sumitani, Kumada 1972（Journal of the American Chemical Society, communication）

---

### §1 Claim Architecture

**コア主張の要約**

本論文の主張は二本柱で構成される。**Novelty柱**：ニッケル–ジホスフィン錯体触媒（代表: [NiCl₂(dpe)]）が、Grignard 試薬とビニル/アリールハライドのクロスカップリングを高収率・高選択的に媒介する全く新しい触媒クラスを開示すること（NC-1）。従来の遷移金属ハライド系が「大量のホモカップリング・不均化生成物」を与えるのに対し、本系は実用的な収率（76–98%）でクロス生成物のみを与えると主張する。**Utility柱**：先行法では多段階を要した通常のアルキル置換芳香族化合物（di-n-butylbenzenes 等）が一工程で得られること（NC-2）。加えて副次的主張として、アリール/ビニルクロリドの「remarkable」反応性（NC-3）、二座ホスフィン配位子の活性序列（NC-4）、および均一系 Ni(II)/Ni(II) 触媒サイクル（NC-5）が提示される。

**Layered structure 判定**

独立層が存在する（**yes**）。層間の依存関係は以下の通り：

- **Layer-P（preparative claim）**：NC-1（選択的クロスカップリング）とNC-2（一工程合成）は Table I の収率データのみで成立する。機構論争（NC-5）や配位子序列の数値的根拠（NC-4）が崩れても Layer-P の主張は独立して残存する。
- **Layer-M（mechanistic claim）**：NC-5（均一系 Ni(II)/Ni(II) サイクル、式 2–4）は Layer-P の観察とは独立して成否が判定される。NC-5 が誤り（例: 実際の活性種は Ni⁰ ナノ粒子）でも Layer-P の化学変換の事実は残る。ただし NC-3（クロリドの反応性）の機構的解釈は NC-5 に依存するため、NC-5 が完全否定されると NC-3 の説明は再考を要する。
- **Layer-L（ligand SAR claim）**：NC-4 は Layer-P とは部分的に独立だが、数値的根拠を欠くため（B-3）、他層を支持する二次的主張に留まる。

単一の反証で全主張が崩れることはない。NC-5 否定は Layer-M を崩すが Layer-P を崩さない。Layer-P は「高収率 Table I データ」という単一点への依存度が高く、それ自体の分析的信頼性（SRG-5）が唯一の集中的脆弱点である。

---

### §2 SRG / CLA → RI / ER / EP Crosswalk

#### SRG-1「触媒機構の証拠ギャップ」

**SRG-1 [Catalytic mechanism evidence gap]**

* **Primary RI**: RI-06 [Imported model]
* **Secondary RI**: RI-03 [Unobserved explanatory]
* **ER**: 触媒サイクル（式 2–4）を支持するためには、[NiCl₂(dpe)] 条件下で中間体 1（L₂NiR₂）・中間体 2（L₂Ni(R')(X'')）・中間体 3 の少なくとも一つが直接同定されるか、速度論的拘束または交差実験によって仮定の素反応ステップが検証される必要がある。
* **EP**: EP-06a [Analogy-validation pack]; EP-03a [Direct-observation / state-assignment pack]
* **Case-specific実装**: (i) (dipy)Ni → (dpe)Ni の類推の正当性を確認するため、[NiCl₂(dpe)] + Et₂Mg または EtMgBr の化学量論的反応から中間体 1 相当の L₂NiEt₂ 複合体を単離し、X線または NMR で同定する。(ii) 式 3 に対応する L₂NiEt₂ + PhCl の化学量論的反応において Et-Et が定量的に生成することを確認（U-1 の自己矛盾的不在への直接的回答）。(iii) Ni(0) への分解を排除するため、反応後の黒色固体を X線または XPS で同定し、均一系触媒の維持を確認する（U-2 への回答）。
* **注記**: members: A-2（機構的証拠の体系的不在）、U-1（式 3 予測のホモカップリング副生物不在）、U-2（黒色析出物未同定）、B-12（黒色析出物の未記録）。TEMPERATURE_SUMMARY: A-2 (V1=high, V2=high; convergence=2/3)、U-1 (V2=high, V3=high; convergence=2/3)。RI-06 が Primary である理由: (dipy)Ni 化学から (dpe)Ni 触媒サイクル全体を構成するという大規模モデル輸入（RI-06 スコープ注記: サイクルレベル輸入）が最も構造的に重い欠落である。RI-03 は中間体の直接観測不在として二次的に適用される。

---

#### SRG-2「クロス/ホモ選択性の定量化」

**SRG-2 [Cross/homo selectivity quantification]**

* **Primary RI**: RI-04 [Unreplicated discriminator]
* **Secondary RI**: RI-01 [Reporting integrity]
* **ER**: 論文の中心的選択性主張（クロスカップリングがホモカップリングを抑制する）を支持するためには、少なくとも一エントリーにおいてホモカップリング生成物（例: Et-Et, n-Bu-n-Bu）の収率または検出下限が定量的に報告され、クロス生成物との質量収支が閉じていることを示す必要がある。
* **EP**: EP-04a [Discrimination / replication pack]; EP-01a [Reporting-coherence pack]
* **Case-specific実装**: (i) EtMgBr/PhCl または n-BuMgBr/PhCl 反応の粗生成物を GC-MS 分析し、Et-Et または n-Bu-n-Bu のピーク面積を内部標準と対比して定量する（検出下限の明記を含む）。(ii) 式 3 の化学量論的反応（L₂NiEt₂ + PhCl）における Et-Et の生成を確認し、触媒条件下での不在との対比を行う。(iii) Tamura-Kochi 系（Ref. 5–6）における同一基質のホモカップリング収率との直接数値比較を実施し、選択性改善の定量的根拠を確立する。
* **注記**: members: B-6（選択性定量データ不在）、U-1（自己矛盾的不在）、C-1（Tamura-Kochi との数値比較なし）。TEMPERATURE_SUMMARY: B-6 (V2=high, V3=high; convergence=2/3)、U-1 (V2=high, V3=high; convergence=2/3)。RI-04 が Primary である理由: 式 3 が明示的にホモカップリング副生物を予測しているにもかかわらず、それを報告せずに「選択的」と主張する構造は識別力の高い単一データ（存在/不在の記録）への依存として RI-04 に最もよく適合する。

---

#### SRG-3「sp² 制限と否定的証拠の不在」

**SRG-3 [Scope restriction without negative-result evidence]**

* **Primary RI**: RI-07 [Unsupported boundary]
* **Secondary RI**: RI-05 [Qualitative overread]
* **ER**: 「Only C_sp² halides can be used」という境界主張を支持するためには、sp³ アルキルハライドまたはベンジルハライドとの反応試行（少なくとも1例）を報告し、失敗の原因（反応なし、ホモカップリング優勢、触媒失活等）を記録する必要がある。
* **EP**: EP-07a [Boundary-test pack]
* **Case-specific実装**: (i) n-BuMgBr と n-BuCl、BnCl、または allyl chloride を [NiCl₂(dpe)] 触媒下に反応させ、クロス生成物の収率（またはその非生成）を定量する。(ii) sp³ ハライドとの反応失敗の原因を同定する: 酸化的付加速度（β-H 脱離との競合）または Ni(0) 分解（U-2 との連関）を動態的に区別する実験を行う。
* **注記**: members: B-4（sp² 制限の根拠なし宣言）、A-3（範囲拡張の明示的先送り）。TEMPERATURE_SUMMARY: B-4 (V1=medium, V2=medium, V3=medium; convergence=3/3; gap=none)。RI-07 拡張適用: 「Only sp² halides can be used」は肯定的境界主張に該当。RI-05 は「high reactivity of chlorides」という定性的観察から「most remarkable」という構造的含意を導出する記述に対して二次的に適用する。

---

#### SRG-4「立体化学的帰結とその機構的根拠」

**SRG-4 [Stereochemical outcome and mechanistic basis]**

* **Primary RI**: RI-05 [Qualitative overread]
* **Secondary RI**: RI-01 [Reporting integrity]
* **ER**: cis:trans 比の報告には、分析法（¹H NMR または GC）と測定誤差の明記が必要であり、その比から「nonstereospecific」かつ「anomalously enriched with cis isomer」という機構的結論を導くためには、少なくとも立体化学的記憶の消失ステップ（酸化的付加 vs. 還元的脱離）を同定する実験的根拠が必要である。
* **EP**: EP-05a [Quantitative-ranking substantiation pack]; EP-01a [Reporting-coherence pack]
* **Case-specific実装**: (i) cis- および trans-1,2-ジクロロエチレンとの PhMgBr 反応生成物 cis/trans-スチルベン混合物の比率を ¹H NMR（ビニルプロトンの化学シフト差）および GC（キャピラリーカラム）の両法で独立に決定し、誤差範囲（±X%）を明記する。(ii) cis-1,2-ジクロロエチレンの単純酸化的付加生成物 [NiCl(R)(dpe)] の立体配置をモデル反応で確認し、立体化学的記憶の喪失ステップを同定する。
* **注記**: members: A-1（立体化学的詳細の先送り）、B-11（cis:trans 比の分析法不開示）。TEMPERATURE_SUMMARY: A-1 (V1=medium, V2=medium; convergence=2/3; gap=none)。RI-05 が Primary である理由: cis:trans 比から「nonstereospecifically」「anomalously」という機構的含意語を経由して「further studies are required」と先送りする構造は、数値なき定性的順位からの構造的・因果的含意の導出（RI-05）に最も適合する。

---

#### SRG-5「収率データの分析的品質」

**SRG-5 [Yield data analytical quality]**

* **Primary RI**: RI-01 [Reporting integrity]
* **Secondary RI**: RI-08 [Unquantified reliability]
* **ER**: Table I の収率データを横断的に比較するためには、収率基盤（単離収率 vs. glpc 収率）の混在に対する測定系の等価性説明、glpc 定量における内部標準同定・応答係数・検量線の記述、および少なくとも代表的 1 エントリーにおける反復実験が必要である。
* **EP**: EP-01a [Reporting-coherence pack]; EP-08a [Replication / uncertainty pack]
* **Case-specific実装**: (i) glpc 収率を報告する 5 エントリー（EtMgBr/PhCl: 98%、n-C₅H₁₁MgCl/CH₂=CHCl: 95%、PhMgBr/CH₂=CHCl: 89%、α-NpMgBr/CH₂=CHCl: 80%、n-BuMgBr/p-DCB: 95%）について内部標準（化合物名）と応答係数を開示し、対応する単離収率測定を追加する。(ii) n-BuMgBr/m-DCB（94%、単離）エントリーについて n=3 の反復実験を行い、標準偏差を報告する。
* **注記**: members: B-2（収率基盤混在）、B-7（"and/or" による特性評価非開示）、B-9（単独測定、標準偏差なし）、B-11（cis:trans 比の分析法不開示）。TEMPERATURE_SUMMARY: B-2 (V1=medium, V3=medium; convergence=2/3; gap=none)。RI-08 サブタイプ: 内部矛盾型とまでは言えないが、glpc 収率と単離収率の系統的バイアスの評価不能として RI-08 が適用される。

---

#### SRG-6「先行研究との数値比較の欠落」

**SRG-6 [Prior work numerical comparison gap]**

* **Primary RI**: RI-09 [External superiority]
* **Secondary RI**: RI-07 [Unsupported boundary]（Corriu-Masse 比較の欠落から NC-4 の支持根拠が境界未確定になる点）
* **ER**: 「homocoupling products in substantial amounts」（先行系の限界）および「promising reaction」（本系の優位性）という比較主張を支持するためには、少なくとも一つの共通基質（例: n-BuMgBr/PhCl）における Tamura-Kochi 系 vs. [NiCl₂(dpe)] 系の収率と選択性の直接数値比較が必要である。Corriu-Masse との関係では、dpe 配位子の必要性（NC-4）を示すために Ni(acac)₂ との基質スコープ比較が必要である。
* **EP**: EP-09a [Internal benchmark pack]
* **Case-specific実装**: (i) n-BuMgBr + PhCl の反応を Tamura-Kochi 条件（THF 中の Fe または Cu 塩触媒）と [NiCl₂(dpe)] 条件（Et₂O）で並列に実施し、収率・選択性（クロス:ホモ比）を比較する。(ii) Ni(acac)₂（配位子なし）と [NiCl₂(dpe)] を同一基質・条件で比較し、dpe 配位子の寄与を定量する。
* **注記**: members: C-1（Tamura-Kochi との数値比較なし）、C-2（cuprate/allylNi との数値比較なし）、A-4（Corriu-Masse との比較なし）。TEMPERATURE_SUMMARY: A-4 (V1=low; convergence=1/3)。RI-09 が Primary である理由: 直接比較データなしに外部文献値（先行系の限界）のみで優位性を主張する構造に RI-09 が最も適合する。

---

#### SRG 外: CLA

**CLA-1: ホモカップリング副生物の自己矛盾的不在（式3 予測 vs. Table I 非報告）**

* **Primary RI**: RI-03 [Unobserved explanatory]（サブタイプ: Available-but-unutilized characterization）
* **Secondary RI**: RI-04 [Unreplicated discriminator]
* **ER**: 式 3 が L₂NiR₂ + R'X'' → L₂Ni(R')(X'') + R-R と明示的にホモカップリング副生物 R-R を化学量論的に予測しているのであれば、Table I の全エントリーにおいて R-R の定量（または検出下限以下であることの確認）が報告されなければならない。
* **EP**: EP-03a [Direct-observation / state-assignment pack]; EP-04a [Discrimination / replication pack]
* **Case-specific実装**: EtMgBr/PhCl 反応（98% glpc 収率）における Et-Et 収率を GC-MS で定量し、質量収支を記録する。式 3 モデル反応（化学量論的 L₂NiEt₂ + PhCl）と触媒条件を比較することで、触媒サイクルにおける Et-Et 蓄積抑制機構（存在するとすれば）を明示する。
* **注記**: grounded_in: U-1（自己矛盾的不在）、B-6（選択性定量データ不在）。いずれの SRG の member_items にも属さない独立 D-1 関連の CLA として記録する。D-1 の NC-1（「selective cross-coupling」という最上位主張）に直結する。TEMPERATURE_SUMMARY では U-1 が high_convergence_low_gap に位置する。CLA-1 は SRG-2 と強い連関を持つが、「式 3 モデルが自ら副生物を予測しているにもかかわらず実験的に確認しない」という自己矛盾的構造が SRG-2 とは独立した論点を構成するため CLA として独立記録する。

**CLA-2: 黒色析出物の機構的帰属問題（均一系 vs. 不均一系触媒の区別）**

* **Primary RI**: RI-02 [Object identification]
* **Secondary RI**: RI-06 [Imported model]
* **ER**: Example 1 で観察された「black mixture」および「much salt」は実験記録として記述されているが、均一系触媒サイクル（式 2–4）の前提となる [NiCl₂(dpe)] の触媒中への維持を確認するために、反応中・後の黒色固体の組成同定（XPS, X線回折、または溶解性試験）が必要である。
* **EP**: EP-02a [Identity / purity substantiation pack]; EP-03a [Direct-observation / state-assignment pack]
* **Case-specific実装**: Example 1 の反応後スラリーを濾過し、黒色固体を X線回折または XPS で分析して Ni⁰ ナノ粒子 vs. NiX₂(dpe) 副生成物塩を区別する。また、均一系触媒であることを確認するためにマーキュリー試験（Hg(0) 添加による不均一触媒失活確認）を実施する。
* **注記**: grounded_in: U-2（黒色析出物と均一系触媒仮定の矛盾）、B-12（黒色色の未記録）。いずれの SRG の member_items にも属さない（SRG-1 は機構的証拠ギャップを扱うが、触媒の物理的同一性は異なる論点である）。D-1 の NC-5（均一系触媒サイクル主張）に直結する。

---

### §3 現在のVQ判定

**現在判定: VQ-2 (Method)（qualified: RI-05 残存）**

---

**VQ-1 [Observation] — 通る（Non-fatal条件付き）**

VQ-1 の必須解消項目は RI-02（Object identification）であり、これは CLA-2 として記録した問題（黒色析出物の物理的同一性）に対応する。CLA-2 は「均一系触媒としての [NiCl₂(dpe)] の同一性」に疑義を呈するが、致命性判定は **Non-fatal** とする。根拠: Table I の観察事実（クロスカップリング生成物の単離収率と物理定数）は触媒の物理的形態の確定とは独立に成立する。生成物の同一性は bp, n²⁰D, glpc 保持時間, nmr, ir の複数法で確認されており、生成物 RI-02 は十分に満たされている。したがって VQ-1 は通る（触媒の同一性疑義は Non-fatal として残存）。

ただし **VQ-1 継承の前提**: 生成物の同一性確認は「and/or」条項により製品ごとの特性評価方法が不開示であり（B-7）、glpc 収率エントリーの質量収支が開示されていない（B-2）。これらは VQ-2 以降で累積的問題となる。

---

**VQ-2 [Method] — 通る（Non-fatal条件付き、RI-05 qualified残存）**

VQ-2 の必須解消項目は RI-01（Reporting integrity）および RI-07（Unsupported boundary）。VQ-1 継承を前提とする。

- **RI-01 について**: SRG-5（収率データの分析的品質）として記録された収率基盤の混在（単離 vs. glpc）、内部標準の非開示、反復測定の不在は RI-01 違反として残存する。しかし 1972 年の JACS Communications 形式において、これらの省略は journal_constraint（D-3）によってほぼ標準的に許容されており、致命性は **Era-norm 依存** と判定する（当時: 許容; 現代: 要改善）。VQ-2 通過の前提として「Era-norm 依存」の Non-fatal と見なす。
- **RI-07 について**: SRG-3（sp² 制限と否定的証拠の不在）として記録した境界主張（"Only C_sp² halides can be used"）は、失敗例の未報告という意味で RI-07 に該当する。しかし論文は明示的に「Only...can be used」と述べており、complete exclusion ではなく preparative scope limitation の宣言として読むことができる。通信形式での紙幅制約（D-2, D-3）とあわせて致命性は **Era-norm 依存** (Non-fatal) と判定する。

**RI-05 (Qualitative overread) qualified 残存**: SRG-4 で記録した「cis:trans 比から'anomalously enriched with the cis isomer'という機構的含意への飛躍」は RI-05 として残存し、VQ-2 を **qualified (limited)** とする。機構的主張（VQ-3 要件）への入口条件として、この定性的過剰読みが VQ-3 の障壁となる。

**結論: VQ-2 (Method) は qualified（RI-05 残存）として通る**。VQ-1 の Non-fatal 条件（CLA-2）を継承する。

---

**VQ-3 [Mechanism] — 未達**

VQ-3 の必須解消項目は RI-03（Unobserved explanatory）、RI-04（Unreplicated discriminator）、RI-06（Imported model）。VQ-2 継承を前提とするが、VQ-3 は以下のいずれも未解消であるため未達である。

- **RI-06 未解消（Fatal）**: 触媒サイクル（式 2–4）は (dipy)Ni 化学量論反応との類推に完全に依存しており（SRG-1、Primary RI）、[NiCl₂(dpe)] 触媒条件下での中間体の直接同定も、素反応速度論も存在しない。(dipy)Ni → (dpe)Ni の類推の有効性は本論文では実証されていない。**Fatal**: この欠落は均一系触媒サイクルという機構的主張が原理的に不成立であることを意味する。
- **RI-03 未解消（Fatal）**: 中間体 1（L₂NiR₂）、2（L₂Ni(R')(X'')）、3 は間接的に推定されるのみであり、[NiCl₂(dpe)] 触媒条件下での直接観測も速度論的拘束も存在しない（CLA-1, CLA-2）。
- **RI-04 未解消（Fatal）**: 式 3 が予測する Et-Et ホモカップリング生成物が未報告のまま「選択的」と主張している（SRG-2, CLA-1）。この単一観察（副生物不在の主張）に代替経路の排除なしに高位の機構的解釈が付与されている。

**層別VQ非対称性**: §1で同定した Layer-P（preparative claim）単独では: VQ-2 に到達している（高収率クロスカップリングの実証という観察事実の層では Method 水準の要件をおおむね満たす）。Layer-M（mechanistic claim）は VQ-1 を超えることができない（活性種の同一性すら未確定）。この非対称性は、論文の準備的貢献（Layer-P）の堅牢性と機構的主張（Layer-M、NC-5）の脆弱性を示す重要な分析情報である。

---

**VQ-4 [Benchmark] — 未達**

VQ-3 未達のため VQ-4 の評価は繰り越し不可。VQ-3 到達後に RI-08（Unquantified reliability: SRG-5 の反復測定不在）および RI-09（External superiority: SRG-6 の先行系との直接比較なし）の解消が必要となる。

---

### §4 Era-Norm Annotation

**communication-era tolerated:**

- **B-1（TON 不記載）**: 1972年の JACS Communications は触媒ターンオーバー数の定量的報告を求める確立した規範が存在しなかった。触媒量の記述（mol% レベル）と「yields are generally very high」という定性的表現が当時は許容されていた。
- **B-2（収率基盤の混在）**: 通信形式の紙幅制約（3ページ）のもとで、Table の脚注を収率基盤の開示代替として使用することが当時の報告慣行として許容されていた。
- **B-3（配位子活性序列の数値なし）**: 脚注（fn. 21）で測定条件を特定し、序列のみを提示することは、通信形式では十分な情報開示とみなされていた。
- **B-7（"and/or" 特性評価）**: 複数分析法の適用対象を製品ごとに開示しないことは、1972年の synthetic communications では標準的な簡略化であった。
- **B-9（単独測定・標準偏差なし）**: 触媒的反応の再現性の統計的報告（SD 記載）は1970年代初頭には実験的 JACS 論文においても一般的でなく、通信形式ではなおさら許容されていた。
- **B-5（"definitely superior" の数値根拠なし）**: 溶媒の質的な優劣比較を副詞で強調することは当時の化学通信の文体的慣行の範囲内であった。

**modern-era deficient:**

- **B-2（収率基盤の混在、グロス定量化不備）**: 現代では、GC 収率報告には内部標準の同定・応答係数・検量線のキャラクタリゼーションが最低限必要とされ、単離収率と GC 収率を同一カラムに混在させる場合には等価性の明示が要求される（RI-01）。
- **B-9（反復測定の不在）**: 現代の基準では、主要エントリー（特に方法の適用範囲を代表するもの）は n≥3 の反復と標準偏差報告が求められる（RI-08）。
- **U-1 / CLA-1（ホモカップリング副生物の未定量）**: 現代の選択性化学では、排除される副生物経路の定量（または検出下限の明示）は中心的選択性主張の支持に不可欠とされる（RI-03, RI-04）。これは「両方に該当する項目」であり: 当時は通信形式の紙幅制約の中で許容されたが（communication-era tolerated 側面）、現代では致命的欠落である（modern-era deficient）。
- **U-2 / CLA-2（黒色析出物の機構的帰属なし）**: 現代の均一系触媒研究では、マーキュリー試験・動的光散乱・TEM 観察等による不均一触媒（Ni⁰ ナノ粒子）の排除が標準的要件である（RI-02, RI-06）。
- **B-5（溶媒依存性の機構的説明なし）**: 現代では、溶媒効果の主張には Grignard 試薬のスペシエーション研究または触媒安定性測定（UV-Vis, NMR）との連動が期待される。
- **A-2（機構的証拠の完全な先送り）**: 1972年の通信として先送り自体は当時許容されたが（communication-era tolerated: 「Investigations are continuing...」の文言）、現代においてこれほど広範な機構的不確定性（中間体同定なし、速度論なし、活性種同定なし）をもつ触媒系の機構的主張（VQ-3）は、Full Paper の後続論文なしには現代レビューに耐えられない（modern-era deficient）。

---

### §5 最短補強ルート

**目的関数設定**

現在の判定: VQ-2 (qualified, RI-05 残存)
第一目的関数: **VQ-3 [Mechanism] への到達**
第二目的関数: VQ-3 到達後の VQ-4 [Benchmark] への到達（第二目的として記載）

---

**VQ-3 への最短ルート（RI-03, RI-04, RI-06 の同時解消）:**

1. **EP-06a [Analogy-validation pack]** — (dipy)Ni から (dpe)Ni への類推を検証するため、[NiCl₂(dpe)] + RMgX の化学量論的反応から中間体 1（L₂NiR₂）を単離し、X線結晶解析または ³¹P/¹H NMR で同定する; 次いで L₂NiR₂ + R'X'' → L₂Ni(R')(X'') + R-R の化学量論的反応でホモカップリング副生物 R-R を定量確認する。**RI-06 を前進させ、RI-03 を部分的に前進させる**（2つの必須 RI を同時前進させる最大情報利得点）。

2. **EP-03a [Direct-observation / state-assignment pack]** — 反応後の黒色固体を X線回折または XPS で分析し、Ni⁰ ナノ粒子 vs. NiX₂ 系生成物を区別する; マーキュリー試験で均一/不均一を区別する。**RI-03 の残余部分（中間体の均一系存在確認）および CLA-2 の RI-02 を前進させる**。

3. **EP-04a [Discrimination / replication pack]** — EtMgBr/PhCl 反応の粗生成物を GC-MS 定量し、Et-Et 収率（または検出下限）を記録して質量収支を閉じる; 式 3 の化学量論反応との Et-Et 生成量比較を行う。**RI-04 を前進させ、CLA-1 を解消する**。

4. **EP-05a [Quantitative-ranking substantiation pack]** — cis-/trans-1,2-ジクロロエチレン反応の生成物比を ¹H NMR と GC の両法で独立定量し、分析誤差を明記する; RI-05 の「定性的過剰読み」を定量的基盤の上に置き直す。**VQ-2 のqualified 条件（RI-05）を解消し、VQ-3 評価の前提を改善する**。

認定ゲート順注記: 実験投入順は情報利得の大きさ（EP-06a が RI-06+RI-03 を同時前進）を優先するが、最終認定は VQ-1 → VQ-2 → VQ-3 → VQ-4 の継承原則に従って順次確定する。VQ-2 の qualified 条件（RI-05）は VQ-3 評価の妨げにはならないが（注1 の「*注1: RI-05が重大に残る場合、VQ-3は「限定的（Qualified）」」条件として引き継がれる）、EP-05a による解消で VQ-3 を qualified なしに確定できる。

---

**VQ-4 への最短ルート（VQ-3 到達後、RI-08 + RI-09 の解消）:**

5. **EP-08a [Replication / uncertainty pack]** — n-BuMgBr/m-DCB（代表エントリー）を n=3 で再実施し、平均収率と標準偏差を報告する; glpc 収率エントリーについて対応する単離収率測定を追加する。**RI-08 を前進させ、SRG-5 を解消する**。

6. **EP-09a [Internal benchmark pack]** — n-BuMgBr/PhCl 反応を Tamura-Kochi 条件（Fe または Cu 触媒、THF）と [NiCl₂(dpe)] 条件（Et₂O）で並列実施し、収率・クロス:ホモ比の数値を対比する; Ni(acac)₂ との並列実験で dpe 配位子の寄与を定量する。**RI-09 を前進させ、SRG-6 を解消する**。

認定ゲート順注記（VQ-4 向け）: VQ-3 到達を前提とし、RI-08（EP-08a）とRI-09（EP-09a）の独立した解消後に VQ-4 が確定する。両者は相互に独立した実験であり並列実施可能。

---

### §6 制度設計への寄与

**1. RI-06 スコープ注記「サイクルレベル輸入」の代表事例確立**

本論文は Codebook v0.2a に記載された「RI-06 スコープ注記: サイクルレベル輸入」の典型事例を提供する。(dipy)Ni 化学量論反応（Refs. 11–12）から [NiCl₂(dpe)] 均一系触媒サイクル全体（式 2–4）を構成するという輸入は、個別素反応ステップの類推ではなくサイクル全体の移植であり、RI-06 のコアケースである。この事例は「1972年代の有機金属 communications における触媒サイクル仮説の記述様式」として Era-norm Annotation（§4）と連動する重要な歴史的記録である。

**2. RI-04 の「否定的証拠の不完全性」パターンの新バリアント記録**

U-1 / CLA-1 で記録した「式 3 がホモカップリング副生物を明示的に予測しているにもかかわらず、その副生物が Table I で報告されず、かつ検出下限の記述もない」というパターンは、Codebook v0.2a §6 に記載された「否定的証拠の不完全性」の新バリアントである: 従来の記述は「陰性の実験結果（ラジカルクロック、TEMPO 捕捉等）を肯定的機構証拠として使用する際に質量収支の閉鎖が欠ける」ものであったが、本ケースは「著者自身の提案モデルが予測する副生物を著者自身が報告しない（自己矛盾的不在）」という構造であり、RI-04 の case-specific 実装として記録価値が高い。EP-04a の対応する case-specific 実装（化学量論的モデル反応による副生物定量の先行検証）として EP 辞書に追加すべきである。

**3. 「標識不整合（Labeling mismatch）」の典型パターン確認**

本論文の機構記述（式 2–4）は事実的記述語（"is converted to", "forms", "reacts with"）を用いて提案触媒サイクルを記述しているが、本文末尾（P3:Lcol:25*）で「working hypothesis」として一括して仮説であることを明示している。仮説標識が末尾 1–2 文に集約される典型的パターン（Labeling mismatch）がここで確認される。RI-06 と連動し、「均一系機構を事実として提示→末尾で先送り」という構造は 1970年代 JACS 通信に広範に観察されるパターンとして記録する。

**4. 「通信→Full Paper 遷移の自動解消パターン」への適合確認**

D-2 の timing_pressure 分析（「Investigations are continuing...」）および D-3 の journal_constraint（3ページ制約）と §4 の Era-norm Annotation を照合すると、B-1（TON）、B-2（収率基盤）、B-3（配位子序列数値）、B-7（特性評価範囲）、B-9（再現性）の 5 項目は Full Paper 展開で自動的に解消されるカテゴリーに属する。これらは Codebook §6 の「通信→Full Paper 遷移の自動解消パターン」の確認ケースであり、同様の Era-norm 判定を要する他論文の基準点として利用できる。

**5. VQ 層別非対称性: Layer-P (preparative) vs. Layer-M (mechanistic) の構造的分離**

§1 の Layered structure 判定と §3 の VQ 判定を統合すると、Kumada 1972 は「Layer-P（preparative claim）= VQ-2」「Layer-M（mechanistic claim）= VQ-1 未満」という顕著な層別 VQ 非対称性を示す。これは UQS が「科学的貢献の準備的側面と機構的側面は独立した VQ 水準に到達しうる」という分析的洞察を定式化する代表事例となる。VQ 判定基準マトリクスへの注記として「同一論文内の独立層が異なる VQ 水準に到達する場合、論文全体の VQ 判定は最も低い必須 RI 水準に従う」という運用細則が確認された。

**6. PRI 候補提案なし**

本ケースで新たな PRI 候補パターンは検出されなかった。PRI-10（Kinetic overclaim）・PRI-11（Mechanism-kinetics decoupling）は該当しない（本論文は速度論データを提示しておらず、速度次数との一致による機構支持という PRI-11 の定義を満たさない）。本ケースは既存 RI コードの代表事例群に追加確認を提供する形での貢献に留まる。
