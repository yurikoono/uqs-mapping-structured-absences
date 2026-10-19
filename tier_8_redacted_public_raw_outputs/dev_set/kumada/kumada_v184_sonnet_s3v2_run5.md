```
prompt_version: stage3-v2-20260416
model_info: claude-sonnet-4-6
```

---

# 科学的知見の再認定判定票

## Tamao, Sumitani, Kumada 1972（Journal of the American Chemical Society, communication）

---

### §1 Claim Architecture

**コア主張の要約:**

本論文のコア主張は「グリニャール試薬とビニルまたはアリールハライドを、ニッケル-ジホスフィン錯体（主に [NiCl₂(dpe)]）の触媒量を用いて、選択的にクロスカップリングさせる新しい実用的合成法を確立した」というものである。Novelty柱は「遷移金属触媒によるクロスカップリングにおける選択性の実現」——すなわちホモカップリングや不均化副生成物を抑制した高選択的C–C結合形成——であり、Utility柱は「β-水素含有アルキルグリニャール試薬を含む多様な試薬への適用性、sp²クロリドの高い反応性、およびm-ジ-n-ブチルベンゼン等の従来法では容易に得られない化合物への一段階的アクセス」である。

**Layered structureの判定:**

主張は独立した三層で構成されており、単一の反証では全体が崩れない構造となっている。

- **層1（実用的収率層）**: Table I の 10 基質組合せで 76–98% の収率を達成したという実験的事実。この層は単離収率または glpc 収率の数値で直接支持されており、最も証拠基盤が堅牢な層である。ただし測定基準の不均一性（B-2）と反復実験の欠如（B-9）という内部的な弱点を抱える。
- **層2（触媒機構層）**: eqs 2–4 で提案された Ni(II)/Ni(0) 触媒サイクルと、配位子活性順（feature 3）。この層は (dipy)Ni 化学との類推（refs 11–12）に全面的に依存しており、[NiCl₂(dpe)] 系での直接的機構検証を欠く。層1とは独立しているが、層1の「選択性」という主張の機構的説明を担っているため、層2の崩壊は層1の解釈の信頼性を間接的に低下させる。
- **層3（競合系差別化層）**: Tamura-Kochi 系（sp² ハライド限定制約の克服）および Corriu-Masse 系（後発 Note Added in Proof）に対する位置づけ。この層は定性的主張のみで数値的根拠を欠き（SRG-6）、三層の中で最も実証基盤が薄い。

層間依存関係: 層3が崩れても（競合系との優位性差別化が成立しない）、層1の収率データ自体は独立して成立する。しかし層2が崩れる（触媒の実体が均一系でない、または eq 3 の予測と実験的不整合が解消されない）と、層1の「選択的」という形容の機構的正当化が失われ、論文のコア主張の一部が実証的に弱体化する。

---

### §2 SRG / CLA → RI / ER / EP Crosswalk

---

**SRG-1 [触媒機構証拠の空白]**

* **Primary RI**: RI-06 [Imported model] — (dipy)Ni の化学量論的反応から導出されたサイクル（refs 11–12）が、[NiCl₂(dpe)] 触媒条件での同型性実証なしに輸入されている。これは個別の素反応ステップの類推ではなく、触媒サイクル全体の大規模モデル輸入（RI-06 スコープ注記: サイクルレベル輸入）に該当する。
* **Secondary RI**: RI-03 [Unobserved explanatory] — 触媒サイクルの中核を担う中間体 1（L₂NiR₂）、中間体 2（L₂Ni(R')(X'')）、中間体 3（L₂NiR'R）はいずれも [NiCl₂(dpe)] 触媒条件下で直接観測されず、速度論的拘束も行われていない。さらに黒色物質（B-12 / U-2）という観察は均一系仮定と矛盾しうる。
* **ER**: 触媒サイクルの各素反応（酸化的付加 → トランスメタル化 → 還元的脱離）を [NiCl₂(dpe)] 系において独立した速度論的実験または分光学的中間体捕捉によって実証すること。あるいは、黒色物質の組成解析（粉末 X 線回折、元素分析、磁気感受率測定）によって均一系触媒の実体を確認すること。
* **EP**: EP-06a [Analogy-validation pack]; EP-03a [Direct-observation / state-assignment pack]
* **Case-specific実装**: [NiCl₂(dpe)] / n-BuMgBr / PhCl 系において低温で反応を停止し、Ni 中間体（L₂NiR₂、L₂NiR'R 等）を単離または ³¹P / ¹H NMR でその場観測すること。黒色固体の生成時期・量と触媒活性の時間的相関を取ることで、均一系 vs 不均一系活性種を区別する。crossover 実験（二種のグリニャール試薬混合）による eq 3 の化学量論的予測の検証も含む。
* **注記**: member_items: A-2（V1=high, V2=high; convergence=2/3; gap=none）、U-1（V2=high, V3=high; convergence=2/3; gap=none）、U-2（medium severity, self-contradictory absence）、B-12（convergence=1/3）。TEMPERATURE_SUMMARY: A-2 は highest combined weight, U-1 は high_convergence_low_gap 上位項目。RI-06 と RI-03 の共起: 両者の解消が独立して必要であり（RI-06 は類推の妥当性、RI-03 は実体の直接確認）、一方の解消だけでは SRG-1 は前進しない。

---

**SRG-2 [クロス/ホモ選択性定量化の空白]**

* **Primary RI**: RI-04 [Unreplicated discriminator] — クロス選択性の主張の核となるのは Table I の収率データ（単一の試みによる）であるが、ホモカップリング生成物（R–R）の同定・定量がなく、クロス対ホモの比率という最重要識別データが完全に欠落している。単一の収率値から「選択的」と主張しており、代替経路（ホモカップリング経路）を排除する実験を欠く。
* **Secondary RI**: RI-08 [Unquantified reliability] — 10 エントリー全てが単回測定であり、Table I の収率差（94% vs 76%）の統計的有意性を評価できない。
* **ER**: 少なくとも代表的な基質（EtMgBr/PhCl、n-BuMgBr/PhCl 等）についてクロスカップリング生成物とホモカップリング生成物（Et-Et、n-Bu-n-Bu 等）の両方を同時定量し、クロス:ホモ比を報告すること。反応系の質量収支（クロス + ホモ + 未反応出発原料 ≈ 100%）を明示すること。
* **EP**: EP-04a [Discrimination / replication pack]; EP-08a [Replication / uncertainty pack]
* **Case-specific実装**: EtMgBr/PhCl 反応の終点で反応液を glpc 分析（適切な内部標準と応答係数を用いて）し、スチレン（クロス）、ビフェニル（Ph-Ph ホモ）、ブタン（Et-Et ホモ）を同時定量する。複数回（n≥3）繰り返し、クロス:ホモ比と標準偏差を報告する。
* **注記**: member_items: B-6（V2=high, V3=high; convergence=2/3; gap=none）、U-1（high severity, self-contradictory absence — eq 3 が予測する R–R の不在）、C-1（Tamura-Kochi との数値比較の欠落）。U-1 は SRG-2 の中核問題（eq 3 ↔ Table I の自己矛盾）として最も重い。

---

**SRG-3 [sp² 制限と否定的証拠の不在]**

* **Primary RI**: RI-07 [Unsupported boundary] — [REDACTED: substantial verbatim quotation; see Tier 9] という exclusion claim が、sp³ ハライドとの失敗実験データなしに提示されている（RI-07 拡張適用: 否定的境界主張に該当）。
* **Secondary RI**: なし（B-4 の intentional_narrowing 側面は RI-07 に吸収、reporting_omission 側面は EP-07a の case-specific 実装として処理）
* **ER**: sp³ アルキルハライドまたはアリルハライドとの反応を少なくとも一例試みて、収率（0% または痕跡量）を報告すること。失敗の原因として β-水素脱離競合、酸化的付加の速度問題、または別のメカニズムの可能性を示す記述を添えること。
* **EP**: EP-07a [Boundary-test pack]
* **Case-specific実装**: n-BuCl（1-クロロブタン）を PhMgBr と [NiCl₂(dpe)] 存在下で Table I 条件（Et₂O、還流）で反応させ、glpc で生成物（PhBu、Ph-Ph、Bu-Bu）を分析し、クロスカップリング収率 ≤5% を確認する失敗例として報告する。
* **注記**: member_items: B-4（V1=medium, V2=medium, V3=medium; convergence=3/3; gap=none — 最高 convergence 項目）、A-3（V1=medium, V3=medium; convergence=2/3）。B-4 の convergence=3/3 はこの SRG を high priority とする根拠。

---

**SRG-4 [立体化学的結果とその機構的基盤]**

* **Primary RI**: RI-05 [Qualitative overread] — cis:trans 比（cis-DCE → 80:20、trans-DCE → 43:57）という観察から「非特異的（nonstereospecifically）」という機構的含意を導出しているが、分析法の開示がなく、数値的不確かさの評価もない。とりわけ 43:57 は ±5% の測定誤差で「ほぼランダム」から「部分的保持」まで幅広い解釈が可能であり、定性的語彙から構造的含意を導く RI-05 パターンを示す。
* **Secondary RI**: RI-08 [Unquantified reliability] — cis:trans 比の測定法（¹H NMR 積分、glpc 面積比等）と不確かさが未開示（B-11）。
* **ER**: cis:trans 比の測定法を明示し（選択した方法の不確かさを評価し）、少なくとも二法による確認を行うこと。
* **EP**: EP-05a [Quantitative-ranking substantiation pack]; EP-08a [Replication / uncertainty pack]
* **Case-specific実装**: cis- および trans-1,2-DCE + PhMgBr 反応の生成物を ¹H NMR（ビニルプロトンの化学シフト差による cis/trans 識別）と独立した glpc（既知比率の標準混合物で校正）の両法で定量し、結果の一致を確認する。不確かさ評価（±SD または ±測定誤差）を添える。
* **注記**: member_items: A-1（V1=medium, V2=medium; convergence=2/3; gap=none）、B-11（V3=medium; convergence=1/3）。RI-05 が重大に残存するため、この SRG に関連する VQ-3 は qualified として扱う（VQ 判定基準マトリクス注1 参照）。

---

**SRG-5 [収率データ解析品質]**

* **Primary RI**: RI-01 [Reporting integrity] — Table I における単離収率と glpc 収率の混在（B-2）、内部標準・応答係数・校正プロトコルの非開示、および反復測定の欠如（B-9）が組み合わさり、10 エントリー間の横比較可能性が損なわれている。
* **Secondary RI**: RI-08 [Unquantified reliability] — 単回測定（B-9）かつ製品純度の独立確認なし（B-7、B-8）。
* **ER**: 全エントリーを統一された測定基準（単離収率または校正 glpc 収率のいずれか一方）で記録し、glpc 定量には内部標準の同定と応答係数を明示すること。主要基質（少なくとも 3 エントリー）について反復実験（n≥3）の平均と標準偏差を示すこと。
* **EP**: EP-01a [Reporting-coherence pack]; EP-08a [Replication / uncertainty pack]
* **Case-specific実装**: EtMgBr/PhCl（98% glpc）、n-BuMgBr/PhCl（76% 単離）、n-BuMgBr/PhBr（90% 単離）の三エントリーについて glpc 単離収率の両方を測定し（ドデカン内部標準、応答係数事前校正）、混在データの影響を評価する。
* **注記**: member_items: B-2（V1=medium, V3=medium; convergence=2/3; gap=none）、B-7（V3=medium; convergence=1/3）、B-9（V3=medium; convergence=1/3）、B-11 も部分的に重複（B-11 は SRG-4 に主帰属）。RI-01 + RI-08 の共起: RI-01 解消（統一測定基準）だけでは反復測定欠如（RI-08）は残存する。両者の独立した解消が必要。

---

**SRG-6 [先行研究との数値比較欠落]**

* **Primary RI**: RI-09 [External superiority] — Tamura-Kochi 触媒（"seldom employed in synthetic practice"）および Corriu-Masse 系（Note Added in Proof）に対する優位性を、直接数値比較なしに外部文献の記述のみで主張している。
* **Secondary RI**: RI-05 [Qualitative overread] — "definitely superior" (B-5) という確定的表現が溶媒比較の数値根拠なしに使用されている。
* **ER**: Tamura-Kochi 条件と同一基質（例: n-BuMgBr + PhCl または CH₂=CHCl）での平行反応実験を実施し、収率・選択性（クロス:ホモ比）を数値比較すること。
* **EP**: EP-09a [Internal benchmark pack]
* **Case-specific実装**: PhMgBr + CH₂=CHCl について [NiCl₂(dpe)]（本法）と FeCl₃（Tamura-Kochi 系）を同一条件（Et₂O、同温度）で並行実施し、スチレン収率とホモカップリング生成物量を glpc 同時分析で比較する。
* **注記**: member_items: C-1（Tamura-Kochi との数値比較欠落、convergence=1/3 だが affects_claims=yes）、C-2（cuprate/allylnickel との比較欠落）、A-4（Corriu-Masse との差別化欠落、convergence=1/3）。RI-09 の適用: 先行系との直接比較データなしに"seldom employed"という劣後評価を基に本法の優位性が主張されている。

---

**SRG外：CLA（Claim-level Adjunct）**

---

**CLA-1: 触媒効率の定量的実証欠落（TON・触媒量依存性）**

* **Primary RI**: RI-05 [Qualitative overread] — "catalytic amount" という語と Table I 注 a の触媒量範囲（10⁻²–10⁻³ mol 比）が提示されているが、TON、ターンオーバー頻度、触媒量依存性実験が欠落しており、「触媒として機能している」という主張の定量的根拠が不在。"not necessarily optimum"という免責文がこの欠落を覆い隠す構造となっている。
* **Secondary RI**: RI-04 [Unreplicated discriminator] — 触媒量下で反応が完結するというシングルデータポイント（各 Table I エントリーの一回の収率）をもって触媒的有効性を主張。
* **ER**: 触媒量を系統的に変化させた実験（0.1, 0.5, 1, 5, 10 mol%）で収率プロファイルを測定し、最適触媒量と対応する TON を報告すること。
* **EP**: EP-04a [Discrimination / replication pack]; EP-10a [Kinetic verification pack（暫定）]
* **Case-specific実装**: n-BuMgBr/PhCl 系で [NiCl₂(dpe)] 量を 0.1–10 mol% まで変化させ、glpc で PhBu 収率を測定し、触媒量 1 mol% で TON ≥ 76（収率 76% から）を実証する。
* **CLA判定根拠**: grounded_in: B-1（V1=medium, V3=low; convergence=2/3; gap=low）。B-1 に対応する直接の SRG メンバーは SRG-1（A-2, U-1, U-2, B-12）であるが、B-1 はそのメンバーリストには含まれない。B-1 はタイトル「触媒」という主張に直結するため（D-1 のコア主張: "catalysis by nickel-phosphine complexes"）、CLA として記録する。

---

**CLA-2: 立体化学非特異性の機構的起源未同定（自己矛盾的不在）**

* **Primary RI**: RI-03 [Unobserved explanatory] — "anomalously enriched with the cis isomer" という観察は、cis 選択的生成物形成の起源が eqs 2–4 の触媒サイクルのどの段階に帰属するかを問うが、該当する elementary step での立体化学情報（酸化的付加での立体選択性、cis-L₂Ni(Ph)(X) の幾何配置保持・反転等）は直接観測されていない。
* **Secondary RI**: RI-06 [Imported model] — eqs 2–4 の機構が [NiCl₂(dpe)] 系での独立検証なしに適用されており、立体化学のどの段階で記憶が失われるかを類推モデルから説明しようとすることは RI-06 の構造を持つ。
* **ER**: cis- および trans-1,2-DCE それぞれについて反応を途中停止し、ビニルニッケル中間体（L₂Ni(Ph)(vinyl) 等）の立体配置を分光学的に確認すること。あるいは重標識体（cis/trans 区別可能な²H 標識 DCE）を用いた crossover 実験で立体化学情報の消失地点を同定すること。
* **EP**: EP-03a [Direct-observation / state-assignment pack]; EP-06a [Analogy-validation pack]
* **Case-specific実装**: cis-1,2-DCE と PhMgBr の反応において、低温（−30°C）でニッケル中間体を ³¹P{¹H} NMR でその場モニタリングし、cis-PhNi(dpe)(vinyl) の立体配置が反応温度上昇とともに変化するかを追跡する。
* **CLA判定根拠**: grounded_in: A-1（V1=medium, V2=medium; convergence=2/3）、B-11（V3=medium; convergence=1/3）。A-1 は SRG-4 のメンバーであるが、この CLA が問うのは「立体化学情報消失の機構的起源（直接観測の欠如）」という RI-03 固有の問いであり、SRG-4 が問う「測定法・定量的信頼性」（RI-05/RI-08）とは区別される独立問い。論文が "anomalous" と自ら評した観察の機構的説明が完全に不在であることが自己矛盾的不在として検出された。

---

### §3 現在のVQ判定

**現在判定: VQ-2 (Method)**

---

**VQ-1 [Observation] の判定: 通る（Non-fatal条件付き）**

VQ-1 の必須解消項目は RI-02（Object identification）。本論文では二つの詳細な実験手順（m-ジ-n-ブチルベンゼン、α-ビニルナフタレン）と Table I に物理定数・沸点・屈折率が示されており、主要生成物の同定は glpc/NMR/IR/MS の組み合わせによって行われている。"and/or"という表現（B-7）は一部製品が単一法での同定にとどまる可能性を示すが、論文の中心主張を支える主要生成物（m-ジ-n-ブチルベンゼン、スチルベン）については bp/n²⁰D の確認と複数分析法が充当されており、RI-02 は「Non-fatal（主張の成立を根底からは覆さないが残存）」と判定する。

ただし bp の文献値との不一致（B-8）および "pure" 主張の独立確認の欠如は、現代標準では生成物純度の再評価対象である（§4 modern-era deficient 参照）。

**VQ-2 [Method] の判定: 通る（限定的）**

VQ-2 の必須解消項目は RI-01（Reporting integrity）と RI-07（Unsupported boundary）。VQ-1 通過を前提とする。

- **RI-01 の状態**: Table I における収率基準の混在（B-2: glpc 収率 vs 単離収率の混在、内部標準非開示）は Method レベルの横比較可能性を損なっているが、測定が全く行われていない（measurement absence）ではなく「基準が混在している（basis mismatch）」という RI-01 の類型。Communication 形式での first report として、測定自体は実施されており手続き的 Method は一応存在する——したがって RI-01 は「Non-fatal（VQ-2 を根底から覆さないが残存）」と判定。
- **RI-07 の状態**: "Only C_{sp²} halides" という境界主張は sp³ での失敗実験を欠く（B-4）が、この制限は論文の positive claim（sp² での選択的カップリング）の反証ではなく、境界の実証的根拠の欠如である。したがって RI-07 も「Non-fatal」と判定し、Method 水準の主張は「sp² 系において機能する」という限定的な意味で通過できる。

ただし **VQ-2 は qualified（限定的）** と記録する。理由: 収率データの横比較可能性が RI-01 の残存によって制限されており、10 エントリー間の収率差（94% vs 76%）が測定法の差によるものか実際の反応性の差によるものかを本論文内では弁別できないため、Method レベルの実証は「定性的範囲内」に留まる。

**VQ-3 [Mechanism] の判定: 未達**

VQ-3 の必須解消項目は RI-03、RI-04、RI-06（+ VQ-2 継承）。

- **RI-06**: (dipy)Ni モデルの [NiCl₂(dpe)] 系への類推（SRG-1）は同型性実証を欠いており、未解消（Fatal）。触媒サイクルの eqs 2–4 は同型性実証なしの輸入モデルであり、[NiCl₂(dpe)] 触媒条件での機構主張を原理的に支持できない。
- **RI-03**: 中間体 1、2、3 の直接観測がなく（SRG-1）、また黒色固体（U-2）の性状未確認が均一系仮定に疑問を残す。未解消（Fatal）。
- **RI-04**: Table I の収率がシングルデータポイントであり（B-9）、ホモカップリング生成物の同時定量がなく（U-1、SRG-2）、クロス選択性の識別データとして機能しない。未解消（Fatal）。
- **RI-05（注1 該当）**: SRG-4 の cis:trans 比から "nonstereospecifically" という機構的語彙への overread が残存するため、Mechanism 層の主張は「VQ-3 qualified」以前に VQ-3 未達として確定。

RI-03/RI-04/RI-06 三者の同時残存により VQ-3 は未達と確定する。

**VQ-4 [Benchmark] の判定: 未達（前提条件不充足）**

VQ-3 未達のため継承原則により VQ-4 は評価対象外（前提条件不充足）。なお仮に VQ-3 が通過できたとしても、RI-08（収率の反復測定欠如: B-9）および RI-09（Tamura-Kochi / Corriu-Masse との直接数値比較なし: SRG-6）が残存するため VQ-4 は未達となる。

---

**層別VQ非対称性:**

§1 の Layered structure 分析で同定された「層1（実用的収率層）」単独では:
層1は「sp² 基質に対して高収率のクロスカップリング生成物が得られる」という観察的主張として VQ-2 (Method) に到達しており、これは論文全体の VQ 判定と一致する。ただし「選択的（selective）」という形容は層2（触媒機構層）の SRG-2 が未解消であるため、層1単独でも完全な VQ-2 通過とは言えない（qualified）。

「層2（触媒機構層）」単独では VQ-3 に到達しない（RI-03/RI-04/RI-06 すべてが致命的）。

---

### §4 Era-Norm Annotation

**communication-era tolerated（当時の Communication 形式で許容された欠落）:**

- **B-1**（TON 値・触媒量依存性の不在）: 1972 年当時の有機金属触媒報告において、TON の定量的記述は必須慣行ではなく、「触媒量使用」という事実自体が触媒的であることの証拠として受理されていた。
- **B-9**（反復実験・標準偏差なし）: JACS Communication 形式の 3 頁という字数制約のもとで、全 10 エントリーの反復実験データを掲載することは当時の Communication 慣行として求められていなかった。
- **B-7**（"and/or" による分析法の曖昧記述）: 1972 年当時の合成化学 Communication では、新規化合物について「グリニャール試薬の文脈で自明な構造」であれば bp/n²⁰D と glpc 保持時間の一致で同定を受理する慣行が存在した。
- **B-10**（グリニャール試薬の力価検定法非開示）: グリニャール試薬の調製・力価は当時の有機化学研究室の標準技術であり、詳細な検定プロトコルの開示は Communication 形式では期待されていなかった。
- **B-13**（基質依存の条件変更の非説明）: 動力学的詳細の欠落は 1972 年の Communication 形式の構造的制限の範囲内であった。
- **B-14**（20 時間反応時間の根拠欠落）: 反応時間の最適化データは当時の first-report Communication では系統的に省略される項目であった。
- **A-4 / C-3**（Corriu-Masse との数値比較不在）: Note Added in Proof という形式は査読後に文書を修正できない制度的制約に起因しており、この段階での直接比較実験は制度的に不可能であった。

---

**modern-era deficient（現代の再認定基準では不足）:**

- **B-2**（収率基準の混在・内部標準非開示）: 現代の方法論論文では、定量 glpc 法の内部標準・応答係数・校正曲線の開示が再現性確保の必須要件とされており、単離収率と glpc 収率の混在は横比較可能性を損なう現代的欠落として評価される。
- **B-3**（配位子活性順の数値根拠なし）: 現代の触媒スクリーニング報告では、順位付けに使用した条件の完全な数値データ（各触媒での収率値）の開示が求められる。定性的順位のみでは RI-05 が致命的になる。
- **B-4**（sp² 制限の否定的証拠なし）: 現代のスコープ評価は、少なくとも代表的な失敗基質を一例含めることを標準とする（Org. Synth. チェックリスト等）。
- **B-6 / U-1**（ホモカップリング生成物の未定量・eq 3 との自己矛盾）: 現代の選択性主張では、クロス:ホモ比の定量（または質量収支）が必須であり、特に機構モデルが副生成物を予測している場合（U-1 の自己矛盾的不在）の放置は現代基準では受理されない。
- **U-2 / B-12**（黒色固体の未特性解析・均一系仮定との矛盾）: 現代の均一系触媒化学では、反応中の触媒変性（Ni⁰ ナノ粒子生成等）の確認が再現性に関わる重要事項として標準的に要求される（例: mercury drop test、Hg(0) 中毒実験、動的光散乱による粒子検出）。
- **B-8**（"pure" 主張の独立確認なし）: 現代では GC 純度 ≥ 95%（または HPLC）または元素分析を "pure" の独立確認として要求する。

---

### §5 最短補強ルート

**目的関数: VQ-2 (Method) → VQ-3 (Mechanism)**（現在 VQ-2 qualified）

---

**VQ-3 への最短ルート:**

1. **EP-04a [Discrimination / replication pack]** — EtMgBr/PhCl および n-BuMgBr/PhCl について終点の反応混合液を定量 glpc（ドデカン内部標準、応答係数校正済み）で分析し、クロスカップリング生成物（PhEt、PhBu）と対応するホモカップリング生成物（Et-Et、n-Bu-n-Bu）を同時定量して クロス:ホモ比を報告する（n≥3 反復）。RI-04（SRG-2: U-1 解消）と RI-08（SRG-5: B-9 部分解消）を同時前進させる最大情報利得 EP。

2. **EP-03a [Direct-observation / state-assignment pack]** — [NiCl₂(dpe)] / n-BuMgBr 混合物を低温（−30°C）で調製し、³¹P{¹H} NMR および ¹H NMR でその場観測することで diorganonickel 中間体（L₂Ni(n-Bu)₂）の生成を確認する。次いで PhCl 添加後の NMR 変化で eq 3 の素反応進行を追跡する。RI-03（SRG-1: 中間体直接観測）を前進させ、均一系 vs 不均一系の問いに部分的に答える。

3. **EP-06a [Analogy-validation pack]** — 黒色固体（実験例 1 手順記録）を単離し、粉末 X 線回折と磁気感受率測定で Ni⁰ / NiI / NiII の同定を行う。あるいは Hg(0) 毒化実験で均一系触媒活性の確認を試みる。RI-06（SRG-1: (dipy)Ni モデルの妥当性）と RI-03（均一系仮定の確認）を同時に前進させる。Ni 中間体が均一系であれば eqs 2–4 の類推モデルが事後的に支持され、RI-06 の severity が低下する。

4. **EP-07a [Boundary-test pack]** — n-BuCl（sp³ハライド）と PhMgBr の [NiCl₂(dpe)] 触媒反応を 2–3 例実施し、glpc でクロスカップリング生成物 ≤5% を実証することで sp² 制限の実験的証拠を得る。RI-07（SRG-3: B-4）を前進させる。実験コスト最小で高い情報価値を持つ（既存インフラで即時実行可能）。

5. **EP-01a [Reporting-coherence pack]** — 全 10 エントリーを統一した測定基準（校正 glpc 収率を推奨）で再測定し、glpc vs 単離収率の混在を解消。内部標準（ドデカン等）、応答係数、校正プロトコルを完全開示する。RI-01（SRG-5: B-2）を解消。

---

**VQ-4 への最短ルート（VQ-3 通過後）:**

1. **EP-08a [Replication / uncertainty pack]** — 代表的な 5 基質組合せについて n≥3 の反復実験を実施し、平均収率と標準偏差を報告する。RI-08（SRG-5: B-9 完全解消）を解消。

2. **EP-09a [Internal benchmark pack]** — [NiCl₂(dpe)]（本法）と FeCl₃（Tamura-Kochi 系）を同一基質（PhMgBr + CH₂=CHCl）で並行実験し、スチレン収率とホモカップリング生成物量を比較。RI-09（SRG-6: C-1, A-4）を解消し、competitive positioning の数値的根拠を確立する。

---

**認定ゲート順注記:** 実験投入順は情報利得の大きい EP-04a（RI-04 + RI-08 同時解消）を優先しているが、最終的な VQ 認定は継承原則に従い VQ-1 → VQ-2 → VQ-3 → VQ-4 の順序で確定する。VQ-3 の認定は RI-03、RI-04、RI-06 の三者すべての解消を要し、上記 EP の①②③を組み合わせて達成する。単一 EP の投入のみでは VQ-3 昇格は原理的に不可能である。

---

### §6 制度設計への寄与

**既存 RI コードの新しい代表事例:**

- **RI-06（サイクルレベル輸入）の典型事例**: Kumada 1972 論文は、RI-06 スコープ注記「サイクルレベル輸入」の典型事例として記録する。(dipy)Ni 化学からの触媒サイクル全体の輸入は、個別素反応の類推ではなく三ステップサイクルの構造ごと輸入しており、v0.2a 注記の「大規模モデル輸入」に完全に対応する。本ケースは RI-06 の代表事例として Codebook v0.2a に追加可能である。

- **RI-07 拡張適用の例示**: "Only C_{sp²} halides can be used" は RI-07 拡張適用注記（「〜のみ有効」という肯定的境界だけでなく否定的境界主張にも適用）の具体例を提供する。sp³ ハライドでの失敗実験なしに sp² 限定を「特徴」として提示した事例として記録する。

**新しい PRI 候補の検出:**

本ケースでは新規 PRI 候補の提案には至らない。PRI-11（Mechanism-kinetics decoupling）のパターン候補として B-1/B-14（動力学データなしの触媒サイクル提案）を照合したが、本論文は速度次数の観測値との比較を試みていないため、PRI-11 の定義（「観測速度次数との一致のみで機構を支持」）には厳密には合致しない——速度次数データ自体が存在しない（RI-03 の問題）。したがって PRI-11 の本論文への適用は保留とし、PRI-11 の適用対象は「速度次数を測定した上で機構との比較を省略するケース」に限定するという確認的知見として記録する。

**VQ 判定基準の境界条件に関する新知見:**

- **RI-06 × RI-03 の共起における VQ-3 の致命性**: 本ケースでは RI-06 と RI-03 が同一 SRG（SRG-1）で共起している。両者の共起では、RI-03（中間体の未観測）の解消なしに RI-06（類推モデルの妥当性）を実証することができず（中間体が観測されて初めてモデルの同型性が検証可能）、逆に RI-06 の解消なしには RI-03 の解消が意義を持たない（どの機構に基づいて中間体を探すかが決まらない）という循環的依存関係が存在する。この「RI-06 × RI-03 循環的共起」は §2 の SRG-1 注記として記録済みであるが、VQ 判定基準の視点からは、このパターンを持つ論文では VQ-3 への昇格コストが線形加算ではなく非線形に高まるという知見として記録する。

- **自己矛盾的不在の Era-norm 分類**: U-1（eq 3 が予測する R–R の不在）は「communication-era tolerated」にも「modern-era deficient」にも該当する両属性ケースとして §4 に記録した。当時の Communication 形式では質量収支の完全報告は求められなかった（tolerated）が、現代では機構モデルが副生成物を予測している場合の定量的確認は必須とされる（deficient）。この両属性ケースは Era-norm Annotation の適用例として記録する。

**EP 辞書への追加 case-specific 実装例:**

- **EP-06a（Analogy-validation pack）の Ni 系実装**: Hg(0) 毒化実験または動的光散乱による Ni⁰ 粒子検出 + 粉末 X 線回折による黒色固体同定——この組み合わせは均一系 vs 不均一系の区別に使用可能な EP-06a の Ni 触媒系固有の実装例として辞書に追加可能。

- **EP-04a（Discrimination / replication pack）の Grignard coupling 系実装**: クロス/ホモカップリング生成物の同時 glpc 定量（ドデカン内部標準 + 応答係数事前校正）——この実装は Kumada 型クロスカップリング論文において SRG-2 解消のための標準 EP-04a 実装として辞書に追加可能。

**標識不整合（Labeling mismatch）の確認:**

著者は "working hypothesis" という限定的語彙を eqs 2–4 の提案に付しているが（"apart from the working hypothesis described above" — A-1 key_quote）、本文中の eqs 2–4 の叙述語は "is oxidatively added," "is then transmetalated," "undergoes reductive elimination" という事実的記述語で構成されており、仮説標識が末尾一文のみに集約されるパターンが確認された。これは §6 の「標識不整合（Labeling mismatch）」パターンとして記録する。RI-06 と連動している（類推モデルが事実的記述語で記述されている）。

**通信→Full Paper 遷移の自動解消パターン:**

B-1（TON / 触媒量最適化）、B-9（反復実験）、B-5（溶媒比較数値）はいずれも Communication 形式の紙幅制約に起因しており（§4 communication-era tolerated）、Full Paper 展開で自動解消される候補として記録する。実際に Kumada グループのその後の Full Paper（1976 年前後）ではこれらの多くが補完されていることが想定される（T2）。

**本ケースは既存の制度設計を複数の観点から追加確認するとともに、RI-06 サイクルレベル輸入の典型事例、RI-06 × RI-03 循環的共起の VQ 非線形コスト、および自己矛盾的不在の Era-norm 両属性分類という三点の新知見を制度設計に提供した。**

---

> **Tier 8 redaction notice**: This file is a redacted copy of the corresponding Tier 3 / Tier 9 output. Verbatim source-paper quotations have been replaced by `[REDACTED: see source paper §<loc>; full text retained in Tier 9 reviewer-only deposit]` markers, preserving location references and our own analytical content. Bibliographic fields (title, authors, journal, year, DOI), analytical labels (`evidence_chain:` with B-/U-/A-/C- internal IDs), short technical terms, and our own analytical text are not redacted. The redaction was applied by `scripts/redact_for_tier8.py` and, for this version, by `scripts/build_paperA_R1_public.py` with `scripts/redact_source_ngram_runs.py` (scripts of the project repository; they are not deposited).
