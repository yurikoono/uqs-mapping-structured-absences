```
prompt_version: stage3-v2-20260416
model_info: claude-sonnet-4-6
input_s2: kumada_v184_sonnet_s2_run3.md
run_id: run3
```

---

# 科学的知見の再認定判定票

## Tamao, Sumitani, Kumada 1972（Journal of the American Chemical Society, communication）

---

### §1 Claim Architecture

**コア主張の要約：**

本論文は、ジハロジホスフィンニッケル錯体（主に[NiCl₂(dpe)]）が触媒量で機能し、グリニャール試薬とvinylic/aryl炭素ハロゲン化物の選択的クロスカップリングを実現するという、新規かつ実用的な合成法を報告する。**Novelty柱**は「触媒量のニッケルーホスフィン錯体による選択的炭素—炭素結合形成」であり、再利用可能な遷移金属触媒という設計思想がπ-アリルニッケル・リチウムジオルガノクプレートのモル当量試薬系との差別化点として明示される。**Utility柱**は「β水素含有グリニャール試薬の適用可能性」「sp²炭素塩化物の高反応性」「通常困難なジアルキルベンゼン類の一段階合成」であり、Table Iの10基質エントリー（収率76–98%）が証拠基盤を構成する。

**Layered structureの判定：**

複数の主張が積層されており、独立層構造を持つ。

- **最外層（事実主張）**: ニッケルホスフィン錯体が触媒として機能し、クロスカップリング生成物が高収率で得られる — Table I で10エントリー実証済み。反証には複数の実験的否定が必要であり、堅牢。
- **中間層（選択性主張）**: クロスカップリングがホモカップリングより選択的に進行する — ホモカップリング副生物の定量的報告がなく、選択性は主張のみ（U-1に対応）。最外層とは独立。
- **最内層（比較優位性主張）**: 先行系（Tamura-Kochi、cuprate系）に対して本系が優れる — 同一基質での直接数値比較なし（C-1, C-2に対応）。最外層・中間層から独立。

独立層構造であるため、最外層（触媒機能の事実）が成立していても、中間層（選択性の定量）・最内層（比較優位）は各々追加根拠なしには成立しない。最外層が反証された場合のみ全主張が崩れる。

---

### §2 SRG / CLA → RI / ER / EP Crosswalk

#### SRG-1 【触媒メカニズム証拠ギャップ】

構成員: A-2, U-1, U-2, B-12

**Primary RI**: RI-06 Imported model  
**Secondary RI**: RI-03 Unobserved explanatory

**ER（規範的要件）**: eqs. 2–4で提案される三段階触媒サイクルが[NiCl₂(dpe)]条件下で実際に機能することを、少なくとも一つの中間体（L₂NiR₂: 1 または L₂Ni(R')(X''): 2）の同定または速度論的拘束によって支持する必要がある。輸入元モデル（(dipy)Ni系, refs 11–12）との同型性は実証が要件。

**EP**: EP-06a Analogy-validation pack; EP-03a Direct-observation / state-assignment pack

**Case-specific実装**:
- [NiCl₂(dpe)]存在下でのGrignard試薬との反応混合物から、ジオルガノニッケル中間体1またはハロ(オルガノ)ニッケル中間体2を独立合成または原位置分光同定（¹H NMR, ³¹P NMR, EPR）する実験。
- 対照として(dipy)Ni系との同一反応での中間体挙動比較を行い、(dpe)系でのcis-二有機体形成の必須性を確認する実験。
- 黒色混合物（U-2）の正体を反応後のTEM, XRD, EPRで特定し、Ni⁰粒子か均一系Ni(II)錯体かを判別する実験。

**注記**: A-2はTEMPERATURY_SUMMARYのhigh_convergence_low_gap（V1=high, V2=high; convergence=2/3; gap=none）に位置する。U-1はhigh severity（self-contradictory absence）; U-2はmedium severity。B-12はconvergence=1/3, gap=n/a。RI-06の主要事例：触媒サイクル全体を(dipy)Ni系から[NiCl₂(dpe)]系へ「サイクルレベル輸入」（RI-06スコープ注記適用）しており、素反応各ステップの独立検証なし。

---

#### SRG-2 【クロス/ホモカップリング選択性定量化】

構成員: B-6, U-1, C-1

**Primary RI**: RI-08 Unquantified reliability  
**Secondary RI**: RI-09 External superiority

**ER（規範的要件）**: 論文の中心的主張「選択的クロスカップリング」は、クロス:ホモ比の定量値（またはホモカップリング副生物の検出下限以下の明示的な陰性報告）によって支持される必要がある。先行系（Tamura-Kochi）との優位性主張には同一基質での直接比較が要件。

**EP**: EP-08a Replication / uncertainty pack; EP-09a Internal benchmark pack

**Case-specific実装**:
- Table Iの代表エントリー（EtMgBr/PhCl, n-BuMgBr/PhCl）について、反応終了後の粗混合物からEt-Et（またはBu-Bu）ホモカップリング生成物を内部標準glpcまたはNMRで定量し、クロス:ホモ比を報告する実験。
- ホモカップリング副生物が検出下限以下の場合、glpc検出下限（< X%）を明記する陰性データ実験。
- 同一基質（例: n-BuMgBr / PhCl）でTamura-Kochi系（Feまたは Cu触媒）と本系を並行実施し、収率・選択性・副生物プロファイルを直接比較する実験。

**注記**: B-6はhigh_convergence_low_gap（V2=high, V3=high; convergence=2/3; gap=none）。U-1はSRG-1とSRG-2の交点に位置するが、RI-08の代表根拠としてSRG-2では独立して機能する。C-1はconvergence=1/3。SRG-2はRI-08の「内部矛盾型サブタイプ」の典型例：eq. 3が副生物R-Rを計量論的に予測する一方で、R-Rの収率が未報告であるという測定一貫性の不在。

---

#### SRG-3 【scope制限なしの否定的結果】

構成員: B-4, A-3

**Primary RI**: RI-07 Unsupported boundary  
**Secondary RI**: （なし）

**ER（規範的要件）**: 「sp²ハロゲン化物のみ使用可能」というscope制限主張は、sp³炭素ハロゲン化物との試験（失敗例または低選択性例）によって実験的に確立する必要がある。引用文献（脚注19）によるsp²-Cl結合の間接的根拠は代替例として不十分。

**EP**: EP-07a Boundary-test pack

**Case-specific実装**:
- n-BuMgBrと1-ブロモブタン（sp³ハロゲン化物）を[NiCl₂(dpe)]存在下で反応させ、収率・選択性・生成物同定を報告する失敗実験（予想: 反応なし、または不選択的）。
- ベンジル塩化物（sp³ではあるが活性化されたsp³系）との結果を含め、sp²とsp³の境界条件を確認する系統的scope実験。
- A-3（拡張の明示的延期）との連動：sp³試験の欠如とscope拡張の延期が重なることで、scope境界の実験的根拠自体が先送りされた構造であることを記録。

**注記**: B-4はconvergence=3/3（全3エージェント一致）、high_convergence_low_gap（gap=none）。フォールバック規則(b)の最優先候補。RI-07の「拡張適用：否定的境界主張」に該当：肯定的境界「sp²のみ」を否定的データなしに主張。通信→Full Paper遷移で自動解消候補（§4参照）。

---

#### SRG-4 【立体化学的結果とその機構的基盤】

構成員: A-1, B-11

**Primary RI**: RI-04 Unreplicated discriminator  
**Secondary RI**: RI-05 Qualitative overread

**ER（規範的要件）**: cis-1,2-DCEとtrans-1,2-DCEからcis富化スチルベン混合物が生成するという立体化学的観察は、(i) 分析法の開示（NMR/glpc/その他）と測定誤差の評価、(ii) 少なくとも2回の独立測定、を経て初めて「異常な」値として確立できる。

**EP**: EP-04a Discrimination / replication pack; EP-08a Replication / uncertainty pack

**Case-specific実装**:
- cis-1,2-DCEおよびtrans-1,2-DCE各エントリーについて、¹H NMR（ビニルプロトン化学シフトと結合定数）によるcis/trans比の定量を行い、測定法・積分誤差を報告する実験。
- 独立した2回以上の実験でcis:trans比の再現性を確認する実験（43:57という比率が誤差±5%の範囲で再現されるか）。
- 両異性体のDCEから共通のcis富化生成物が生じるという「共通異常」が酸化的付加段階での立体情報消失（E/Z異性化）によるものか、還元的脱離段階の選択性によるものかを判別する交差実験（isotope labeling等）。

**注記**: A-1はhigh_convergence_low_gap（V1=medium, V2=medium; convergence=2/3; gap=none）。B-11はconvergence=1/3, gap=n/a。RI-05の二次的適用：「cis異性体に異常に富む」という定性的記述から「cis配置の幾何条件が触媒要件」という含意（D-4-4参照）への overreadが起きている。43:57という比率はRI-04の「識別力の高い単一データに分析精度なく高位解釈」に該当し、測定誤差によっては「near-random」に収まる可能性がある。

---

#### SRG-5 【収率データの分析品質】

構成員: B-2, B-7, B-9, B-11

**Primary RI**: RI-01 Reporting integrity  
**Secondary RI**: RI-08 Unquantified reliability

**ER（規範的要件）**: Table Iの収率データは、glpc収率と単離収率の区別基準の明示、内部標準・応答因子の開示、複数回測定の報告、という最低限の分析メタデータを持つことで、エントリー間・先行系との横比較が可能な情報として機能する。

**EP**: EP-01a Reporting-coherence pack; EP-08a Replication / uncertainty pack

**Case-specific実装**:
- Table Iの各エントリーについて、glpc収率採用の理由（揮発性、分離困難等）を明記し、内部標準の同定と応答因子のキャリブレーション結果を補足として追加する。
- 最高収率エントリー（EtMgBr/PhCl: 98%、glpc専用）について、単離収率での検証実験を実施する。
- 全エントリーを少なくとも2回繰り返し、標準偏差を記載する。
- 製品の同定に使用した具体的な分析法の組み合わせ（glpc + NMR + IR 等）を各エントリーで個別開示する（"and/or" 一括記述の解消）。

**注記**: B-2はhigh_convergence_low_gap（V1=medium, V3=medium; convergence=2/3; gap=none）。B-7はconvergence=1/3; B-9はconvergence=1/3; B-11はSRG-4とも共有（cis:trans比の分析法不明）。RI-01の典型パターン：同一の "Yield" 列に異なる測定基準を混在させることで、エントリー間比較の前提条件である測定フレームの均一性が失われている。最高値が最も弱い分析根拠（glpcのみ）を持つという「逆説」がSRG-5の中核。

---

#### SRG-6 【先行研究との数値比較ギャップ】

構成員: C-1, C-2, A-4

**Primary RI**: RI-09 External superiority  
**Secondary RI**: （なし）

**ER（規範的要件）**: Tamura-Kochi系（refs 5–6）・cuprate/allylnickel系（refs 8–10）との優位性主張は、同一基質での直接比較実験（または文献データを明示的に引用した定量的比較）によって支持される必要がある。Corriu-Masse並行論文（Note Added in Proof）への言及は、scope・収率の差異を少なくとも1基質で示さないと novelty主張の排他性確認として機能しない。

**EP**: EP-09a Internal benchmark pack

**Case-specific実装**:
- n-BuMgBr/PhClという共通基質について、Tamura-Kochi系（Fe触媒）と[NiCl₂(dpe)]系を同一条件（温度、溶媒、量比）で並行実施し、収率・副生物プロファイルを表として対比する実験。
- Corriu-Masse (Chem. Commun., 144, 1972) のNi(acac)₂系と[NiCl₂(dpe)]系を共通基質で比較し、配位子（dpe vs acac）の効果を定量する実験。

**注記**: C-1はconvergence=1/3、affects_claims: yes（論文のcore positioning）。C-2はconvergence=1/3、affects_claims: medium。A-4はconvergence=1/3。SRG-6全体の収束は低いが、D-1のcompetitive positioning主張（最内層）に直結する。通信形式の紙幅制約（D-3 journal_constraint）による部分的許容可能性あり（§4参照）。

---

#### SRG外：CLA（Claim-level Adjuncts）

以下のD-4候補はいずれのSRG member_itemsにも属さない根拠項目を主な根拠とし、かつD-1の主張の成否に直接関わる。

---

**CLA-1: 触媒活性リガンド序列の数値基盤の不在**

grounded_in: B-3（A-2が間接的背景）

**Primary RI**: RI-05 Qualitative overread  
**Secondary RI**: RI-07 Unsupported boundary

**ER**: 活性序列 [NiCl₂(dpp)] > [NiCl₂(dpe)] > ... の提示は、各触媒での収率値の開示と、少なくとも2基質での再現確認を要する。「cis-diorganonickel中間体3の幾何条件が第一要件」というメカニズム的解釈は、bite angle vs 電子効果の定量的解析を要する。

**EP**: EP-05a Quantitative-ranking substantiation pack

**Case-specific実装**:
- 脚注21の条件（n-BuMgBr/PhCl）において、6種の[NiCl₂(L₂)]触媒それぞれの収率値を定量し、活性序列の数値根拠を確立する。
- dppe系（bite angle大）とdmpe系（bite angle小）および単座PPh₃系でのKinect測定を行い、bite angleと電子パラメータの寄与を分離する実験。

**注記**: B-3はhigh_convergence_low_gap（V1=medium, V2=medium; convergence=2/3; gap=none）。SRG-1と部分的に関連するが、配位子効果の定量化という固有の問いとして独立。RI-05の「数値なき序列から構造的・因果的含意を導出」に合致：活性序列からcis幾何要件という機構的含意が数値的支持なく導かれている。

---

**CLA-2: 触媒実用条件の定量的根拠の不在（TON未記載）**

grounded_in: B-1

**Primary RI**: RI-05 Qualitative overread  
**Secondary RI**: RI-08 Unquantified reliability

**ER**: 「新規かつ有用な調製法」という主張は、触媒量（mol%）とTONの報告によって「触媒」という用語の実用的意味を定量的に確立する必要がある。"conditions are not necessarily optimum" という但し書きと「有用な調製法」という主張は論理的に緊張関係にあり、少なくとも最低限のTON値の提示が必要。

**EP**: EP-05a Quantitative-ranking substantiation pack; EP-08a Replication / uncertainty pack

**Case-specific実装**:
- 触媒量を0.01 mol%から1 mol%の5段階に変えた系統的最適化実験（n-BuMgBr/PhClを代表基質として）でTON—収率曲線を作成し、最低有効触媒量とTONを確立する。
- 触媒の再利用可能性実験（反応後の触媒を分離して再投入）を実施し、均一系触媒としての機能継続を確認する。

**注記**: B-1はhigh_convergence_low_gap（V1=medium, V3=low; convergence=2/3; gap=low）。"useful preparative method" という論文の自己定義とTON不在の組み合わせが、D-1の Utility柱に直接関わる。RI-05を主とする理由：「有用」という定性的主張が、触媒効率の定量的根拠なく主張されている。U-2（Ni⁰問題）と連動し、均一触媒としての継続機能確認も未実施。

---

**CLA-3: ジエチルエーテル優位性の対照実験の不在**

grounded_in: B-5

**Primary RI**: RI-09 External superiority  
**Secondary RI**: RI-08 Unquantified reliability

**ER**: "Definitely superior" という表現が示す溶媒優位性主張は、同一Ni触媒・同一基質でのエーテル対THF比較実験によって支持される必要がある。Tamura-Kochi系との溶媒選好の逆転という比較主張も、同一触媒系での対照実験を要する。

**EP**: EP-09a Internal benchmark pack

**Case-specific実装**:
- n-BuMgBr/PhCl + [NiCl₂(dpe)]の系において、ジエチルエーテル、THF、ベンゼン/エーテル混合溶媒での収率・副生物プロファイルを並行比較する実験。
- Tamura-Kochi系（Fe触媒）との溶媒選好の逆転を、同一基質・同一温度で確認する対照実験（溶媒効果と触媒効果の分離）。

**注記**: B-5はhigh_convergence_low_gap（V1=low, V2=low; convergence=2/3; gap=none）。SRG-6の隣接問題として位置するが、grounded_inのB-5がSRG-6のmember_itemsに含まれないためCLAとして独立記録。RI-09の典型：「definitely superior」という優位性主張が自己実験データではなく外部文献の文脈的参照に依存している。

---

### §3 現在のVQ判定

**現在判定: VQ-2 (Method) — ただし VQ-2 は Era-norm 依存条件付き（Qualified）**

---

**VQ-1 (Observation) の判定：通過（ただしNon-fatalの未解消あり）**

VQ-1の必須解消項目はRI-02（Object identification）である。生成物の同定はglpc, NMR, IR, mass spectraによって行われており（B-7: "and/or" の不透明性を除き）、主要生成物（m-di-n-butylbenzene, α-vinylnaphthaleneの2例）については物性値の文献比較が行われている。[NiCl₂(dpe)]触媒自体はBooth-Chatt (ref 14)で既報の既知化合物であり、触媒同一性は参照可能。

非致命的残存：B-7（"and/or"による同定法の不透明性）は、一部製品が単一手法（glpcのみ）で同定された可能性を残すが、2例の詳細実験とTable I全体のパターンからVQ-1の通過を妨げるほどの致命性はない。B-12（黒色沈殿の未同定）は触媒の同一性（U-2）に関わり、厳密にはRI-02の補助問題だが、VQ-1の通過基準である「反応生成物の同定」とは分離して扱える。

---

**VQ-2 (Method) の判定：Era-norm 依存で条件付き通過**

VQ-2の必須解消項目はRI-01（Reporting integrity）+ RI-07（Unsupported boundary）であり、VQ-1を前提とする。

RI-01（SRG-5）：glpc収率と単離収率の混在（B-2）、内部標準・応答因子の非開示（B-2）、全エントリーが単一決定値（B-9）は現代基準では致命的にRI-01に抵触するが、1972年のJACS communication形式では許容されていた（D-3 journal_constraint）。Era-norm依存で「当時は通過、現代では再確認要」と判定。

RI-07（SRG-3）：sp²制限の否定的データ不在（B-4）は「通信→Full Paper遷移で自動解消」パターン（§6参照）に該当し、当時のcommunication形式で許容範囲内。

**VQ-2は Era-norm 依存（communication-era tolerated）を条件に通過判定。現代基準での再認定では RI-01・RI-07の両者が Non-fatal から Era-norm-deficient に格上げされる。**

---

**VQ-3 (Mechanism) の判定：未達**

VQ-3の必須解消項目はRI-03（Unobserved explanatory）+ RI-04（Unreplicated discriminator）+ RI-06（Imported model）であり、VQ-2を前提とする。

- **RI-06（SRG-1: 輸入モデル）：致命的**。eqs. 2–4の触媒サイクルは(dipy)Ni系からのサイクルレベル輸入であり、[NiCl₂(dpe)]条件下での中間体1・2の独立同定は未実施（A-2, B-12）。これはVQ-3の前提条件に根本的に抵触する。
- **RI-03（SRG-1: 未観測中間体）：致命的**。中間体1（L₂NiR₂）・中間体2（L₂Ni(R')(X'')）のどちらも直接観測されておらず、速度論的拘束もない。
- **RI-04（SRG-4: 単一測定）：致命的**。cis:trans比（80:20, 43:57）の分析法が不開示、単一決定値。「非立体特異的」という機構的解釈の根拠として機能できない。

さらに、RI-05が重大に残存（CLA-1: リガンド序列から機構的含意を数値なしに導出; SRG-4）するため、VQ-3の判定は「限定的（Qualified）」以下にとどまる。

**未解消RI（致命的）: RI-03, RI-04, RI-06。VQ-3は未達。**

---

**VQ-4 (Benchmark) の判定：未達（VQ-3 未達のため評価不能）**

VQ-4の必須解消項目はRI-08（Unquantified reliability）+ RI-09（External superiority）であり、VQ-3を継承する。VQ-3が未達であるため評価不能だが、参考として：SRG-2（RI-08: 選択性定量化の不在）とSRG-6（RI-09: 先行系との直接比較なし）がいずれも未解消であり、VQ-4は独立して見ても未達。

---

**層別VQ非対称性：**

§1で同定した独立層別の評価：

- **最外層（触媒機能の事実）単独**: Table Iの10エントリーと2例の詳細実験が事実層を支持する。RI-02は概ね解消。**VQ-1 到達**。
- **中間層（選択性主張）単独**: SRG-2のRI-08（ホモカップリング副生物定量なし）が致命的に残存。**VQ-1未満（Observation水準にも至らない）**。
- **最内層（比較優位性主張）単独**: SRG-6のRI-09（直接比較なし）が致命的。**VQ-1未満**。

論文全体のVQ（VQ-2 qualified）は最外層の堅牢性によって支えられており、中間層・最内層の脆弱性とは非対称な構造を持つ。

---

### §4 Era-Norm Annotation

**communication-era tolerated（1972年 JACS communication 様式で許容）：**

- **B-1（TON未記載）**: 1972年のJACS communicationでは触媒効率の定量化（TON, TOF）は標準的報告項目ではなかった。短報形式の紙幅制約下では省略が慣行的に許容されていた。
- **B-2（glpc/単離収率混在）**: 1970年代初頭の合成化学communicationでは、glpc収率と単離収率の混在は珍しくなく、測定フレームの統一は現代的要件。
- **B-3（リガンド序列の数値なし）**: 最初の報告論文では探索的な序列提示が許容され、定量化はfull paperに委ねられた。
- **B-4（sp³ハロゲン化物の失敗実験なし）**: 通信→Full Paper遷移で自動解消が期待されるパターン。Scope characterizationの全体像は後続論文に譲ることが一般的。
- **B-5（溶媒比較データなし）**: 「diethyl ether definitely superior」という観察的記述は、対照実験なしの報告が短報では許容範囲内だった。
- **B-7（"and/or" 同定法）**: 全生成物の分析法個別記載は短報では不要とされた。
- **B-9（単一決定値）**: 1970年代の合成報告では単一実験の収率記載が標準。標準偏差の報告は例外的だった。

---

**modern-era deficient（現代の再認定では許容できない欠落）：**

- **U-1 / B-6（ホモカップリング副生物の未報告）**: eq. 3が計量論的に予測する副生物R-Rが報告されていない構造は、現代では自己矛盾として必須記載。陰性データ（検出下限以下）の明示が現代的要件。
- **U-2 / B-12（黒色沈殿の未キャラクタリゼーション）**: 均一触媒系を主張する論文でNi⁰粒子の疑いがある黒色沈殿を無処理で通過させることは、現代的機構論文では致命的欠落として扱われる。EPR, TEM等の利用可能な手法が当時から存在した点でEra-normの免責は部分的のみ。
- **B-2（glpc/単離収率の混在 + 最高値がglpcのみ）**: 最高値（EtMgBr/PhCl: 98%）が最も弱い分析根拠（glpcのみ・単一点）を持つという逆説的配置は、現代では報告バイアスとして批判される。
- **A-2 / SRG-1（メカニズム証拠全般の延期）**: 提案触媒サイクルに対応する中間体の独立同定なしの機構提案は、現代では Speculation / Hypothesis の明示的ラベリングが必要。"working hypothesis" という記述（論文テキスト）は方向として正しいが、本文の叙述語（eqs. 2-4での事実的記述）との乖離が問題（§6「標識不整合」参照）。

**両タグ該当（当時許容、現代では不足）：**

- **B-4（sp²制限の否定的データ不在）**: 当時はcommunication様式で許容されたが、現代のscope論文では陰性基質の明示が標準要件。通信→Full Paper遷移で自動解消が期待された項目だが、後続のFull Paper（Tamao et al., 1972-1980年代）で改訂されたかどうかは本論文単体からは判断できない。

---

### §5 最短補強ルート

**第一目的関数: VQ-3 (Mechanism) への到達**（現在VQ-2 qualified から）

**第二目的関数: VQ-4 (Benchmark) への到達**（VQ-3を前提）

---

**VQ-3への最短ルート：**

1. **EP-06a Analogy-validation pack** — [NiCl₂(dpe)]条件下でジオルガノニッケル中間体1またはハロ(オルガノ)ニッケル中間体2を独立合成し（または原位置³¹P NMR/¹H NMR同定し）、(dipy)Ni系からのサイクルレベル輸入（RI-06）を実証的に検証する。RI-06を前進。**最優先**（SRG-1の致命的RI-06を直接解消、かつRI-03の前進にも寄与）。

2. **EP-03a Direct-observation / state-assignment pack** — 反応終了後の黒色混合物をTEM, EPR, ³¹P NMR で解析し、残存触媒の形態（均一系Ni(II)錯体 vs Ni⁰ナノ粒子）を同定する。RI-03を前進。（SRG-1のU-2、B-12を直接解消）

3. **EP-04a Discrimination / replication pack** — cis-DCE、trans-DCEエントリーの¹H NMR定量（cis:trans比）を2回以上独立実施し、分析誤差付きで報告する。RI-04を前進。（SRG-4のA-1、B-11を直接解消）

4. **EP-05a Quantitative-ranking substantiation pack** — 6種[NiCl₂(L₂)]触媒の収率値（n-BuMgBr/PhCl）を測定し、リガンド序列の数値根拠を確立。同時にbite angle vs 電子効果の分離実験を実施。RI-05を前進。（CLA-1を解消し、VQ-3 qualifiedの「限定」要因を除去）

認定ゲート順注記: 実験投入順は情報利得順（EP-06a → EP-03a → EP-04a → EP-05a）だが、最終的なVQ-3認定は継承原則に従い VQ-1 → VQ-2 → VQ-3 のゲート順で確定する。VQ-2のEra-norm依存条件（RI-01現代版再確認）として、EP-01a・EP-08a（§5下記）の実施が前提。

---

**VQ-4への最短ルート（VQ-3達成後）：**

5. **EP-08a Replication / uncertainty pack** — Table I代表エントリー（EtMgBr/PhCl, n-BuMgBr/PhCl, n-BuMgBr/m-DCB）について3回以上の独立実験を実施し、収率の標準偏差とglpc/単離収率の両方を報告する。RI-08を前進。（SRG-2のB-6、SRG-5のB-9を解消）

6. **EP-09a Internal benchmark pack** — n-BuMgBr/PhClにおいて[NiCl₂(dpe)]系とTamura-Kochi Fe触媒系・cuprate系を同一条件で並行実施し、収率・クロス:ホモ比・副生物プロファイルを直接対比する表を作成する。RI-09を前進。（SRG-6のC-1、C-2、A-4を解消）

7. **EP-07a Boundary-test pack** — sp³ハロゲン化物（1-ブロモブタン等）との[NiCl₂(dpe)]触媒反応を実施し、失敗例または低選択性例を報告する。RI-07を前進。（SRG-3のB-4を最終解消）

認定ゲート順注記: VQ-4認定は VQ-1 → VQ-2 → VQ-3 → VQ-4 のゲート順で確定。VQ-3未達のまま EP-08a/EP-09a のみを投入してもVQ-4には到達しない。

---

### §6 制度設計への寄与

**1. RI-06の代表事例：サイクルレベル輸入の典型ケース**

本論文は RI-06（Imported model）の「サイクルレベル輸入」スコープ注記（v0.2a）の典型事例を提供する。(dipy)Ni系（refs 11–12）から[NiCl₂(dpe)]系へ、素反応単位ではなく三段階の触媒サイクル全体が移植されており、「個別素反応の類推」と「サイクル全体の構成的輸入」の区別を制度設計上明確化するケースとして記録する。今後の分析でRI-06を適用する際、「どの粒度でモデルが輸入されているか」（素反応レベル / サイクルレベル / パラダイムレベル）を明示することを推奨する。

**2. 標識不整合（Labeling mismatch）パターンの検出**

論文はeqs. 2–4を事実的記述語（"reacts with", "is subsequently converted to", "forms a new diorgano complex", "the cross-coupling product is released"）で記述しているが、これらは直接観測されていない提案機構のステップである。論文テキストには "apart from the working hypothesis described above" という仮説標識が1箇所存在するが、その直前の段落（eqs. 2–4の記述部分）との乖離がある：仮説標識は「これ以上の詳細を理解するためにはfurther studiesが必要」という文脈で使用されており、eqs. 2–4の各ステップが「確認済みの仮説」として提示されているわけではないが、事実的叙述語の使用は読者に実証的事実として受け取られうる。RI-06と連動する「標識不整合」の典型例として記録する。仮説標識の位置が論文末尾1文に集約されており、実験記述部との距離が大きい。

**3. 通信→Full Paper遷移の自動解消パターン（SRG-3/RI-07）**

SRG-3（sp²制限の否定的データ不在, RI-07）は、通信形式の紙幅制約に起因し、Full Paper展開で自動解消が期待されるパターンの典型例を提供する。§4のEra-Norm Annotationで「communication-era tolerated」と判定した項目（B-4）が、このパターンに対応する。制度設計上、RI-07の致命性判定に「通信→Full Paper自動解消可能性」を明示的なサブタグとして追加することを提案する（例：RI-07 [auto-resolvable in full-paper context]）。これにより、communicationとfull-paperで致命性評価を区別できる。

**4. RI共起パターン：RI-06 + RI-03の共起構造**

SRG-1では RI-06（輸入モデル）と RI-03（未観測中間体）が共起し、いずれか一方の解消だけでは VQ-3 に到達できない構造を持つ。具体的には：RI-06を解消（アナログ同型性の実証）しても RI-03が残れば中間体の実証的根拠は依然不在であり、RI-03を解消（中間体の直接観測）しても RI-06が残れば輸入元との同型性が未確認のままである。この共起は「輸入モデル + 未観測種」が同一SRGで重なる典型パターンとして記録し、今後の分析での RI-03 + RI-06 共起事例の系統的追跡を推奨する。

**5. RI-08の「内部矛盾型サブタイプ」（SRG-2）**

SRG-2（クロス/ホモカップリング選択性定量化）は、RI-08の「内部矛盾型サブタイプ」の事例を提供する：eq. 3が副生物R-Rの生成を計量論的に要求（モデルが測定値を予測）しているにもかかわらず、R-Rの収率が未報告という「測定一貫性の不在」が生じている。これは単なる反復測定の欠如ではなく、「提案機構の自己予測と報告データの不整合」として区別される。制度設計上、RI-08の「内部矛盾型」の定義（v0.2aのサブタイプ注記）に本事例を代表例として追加することを提案する。

**6. PRI候補の検討**

本論文単独では新たな PRI昇格候補は同定されない。ただし、SRG-1のRI-06（サイクルレベル輸入）+ RI-03（未観測中間体）の共起パターンが、Breitenfeld 2014で同定されたPRI-11（Mechanism-kinetics decoupling）の前段階的構造と類似する可能性がある。PRI-11が「速度式を代数的に導出せずに機構を支持」するパターンであるのに対し、本論文のSRG-1は「触媒サイクルを速度論的検証なしに輸入」するパターンであり、定義上の重複はないが、「機構論文でありながら速度論的検証が伴わない」という親カテゴリを共有する。今後の分析でこのパターンの独立確認が得られた場合、PRI-12（Mechanism-without-kinetic-substrate, Cycle-level analogy）候補として提案することを検討する（1報目の予備記録）。

**総括**: 本ケースは RI-06（サイクルレベル輸入）・RI-08（内部矛盾型）・RI共起パターン（RI-06 + RI-03）・標識不整合・通信→Full Paper自動解消パターンの複合事例として、既存の制度設計を複数の観点から追加確認・具体化した。新たな PRI昇格には追加1報の確認が必要。

---

*inference_time_sec: not available — inject externally*
