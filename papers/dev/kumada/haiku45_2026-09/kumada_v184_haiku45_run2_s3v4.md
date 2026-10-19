<!-- model_info: claude-haiku-4-5-20251001 -->

prompt_version: stage3-v4-20260427
model_info: claude-haiku-4-5-20251001

# 科学的知見の再認定判定票

## Tamao, Sumitani, Kumada (1972, Journal of the American Chemical Society, Communication)

---

### §1 Claim Architecture

**コア主張**

ニッケル-二座ジホスフィン複合体 [NiCl₂(dpe)] が触媒となり、グリニャール試薬と塩化ビニル・芳香族ハライドの選択的クロスカップリング反応を実現する。中心的主張は、この反応が「一般的に非常に高い収率」（76–98%）を与え、従来法（Tamura-Kochi の Ag/Cu/Fe 系）と異なり「ホモカップリング・ジスプロポーショネーション生成物が substantial amounts で形成される」問題を解決することである。

**Novelty 柱**：ニッケル-ジホスフィン触媒系による、新規の C-C クロスカップリング法。

**Utility 柱**：合成実用性。「ほとんどアクセス困難な」化合物（m-ジ-n-ブチルベンゼン、α-ビニルナフタレン）の一段階合成。

**Layered structure**

層1（中核）：反応は動作する。基質スコープ 11 エントリー、収率 76–98%。この層の主張は VQ-1 に依存。

層2（機構）：提案される触媒循環（式 2–4）。ジオルガノニッケル複合体 1、ハロ(オルガノ)ニッケル複合体 2、ジオルガノ複合体 3 の存在を仮定。この層は層1の成否に独立していない。層1の「反応が動作する」が真であっても、層2の「この機構で説明される」が偽である可能性は高い。

層3（最適化）：ジホスフィン配位子設計の原理。「活性の順序 [NiCl₂(dpp)] > [NiCl₂(dpe)] > [NiCl₂(dmpe)] >> [NiCl₂(PPh₃)₂]」と、二座ジホスフィンの「cis 配置」が触媒活性の必須要件であるとの主張。この層は層1の成否に独立して評価される。

層2と層3の間に依存はない。層2（機構）が正しくても層3（配位子設計原理）は別検証が必要である。

---

### §2 SRG / CLA → RI / ER / EP Crosswalk

#### **Group 1: 選択性定量化の不在**

**グルーピング**: V1-Q9, V2-Q3, U-3

**Primary RI**: **RI-09** (External superiority)

**Secondary RI**: RI-05 (Qualitative overread)

**ER**: クロスカップリング vs ホモカップリングの選択性定量化。Prior methods (Tamura-Kochi) との収率・選択性・反応時間の直接比較データ。

**EP**: EP-09a (Internal benchmark pack)

**Case-specific 実装**：
表 I の各エントリーについて、粗収率と分離収率から生成物分布を推算する。例1では 120 mmol Grignard から ~60 mmol 生成物を回収し、残り 60 mmol が何に消費されたか（未反応ハライド、ホモカップリング、ジスプロポーショネーション等）を GC-MS または ¹H NMR で定量化。表 I 全体について、クロスカップリング選択性（cross:homo 比）が [NiCl₂(dpe)] 系で Tamura-Kochi の Fe-catalyzed coupling より優越するかを数値で示す。

**注記**: TEMPERATURE_SUMMARY に high_convergence_low_gap (V1-Q9, V2-Q3). U-3 は質量バランス欠落の自己矛盾的不在として独立の高重要度。

---

#### **Group 2: Cis/trans 立体化学機構と分析的検証**

**グルーピング**: V1-Q8, V2-Q2, V3-Q8, A-2, B-9, U-4

**Primary RI**: **RI-03** (Unobserved explanatory)

**Secondary RI**: RI-04 (Unreplicated discriminator)

**ER**: 
- 機構的層：両方の cis と trans 開始物質が cis-富化スチルベンを与える理由の説明。σ-ビニル中間体仮説と観測される立体幾何学的非特異性の矛盾の解決。
- 分析的層：cis/trans 比（80:20, 43:57）がどの分析法で決定されたか（GC、NMR、他）の明記。GC コラムの基線分解能、NMR 積分準拠（遠距離カップリング検証、NOE 確認）の実施。

**EP**: EP-03a (Direct-observation / state-assignment pack); EP-04a (Discrimination / replication pack)

**Case-specific 実装**：
- 低温 ¹H NMR (−40°C, CD₂Cl₂) でスチルベン異性体の化学シフト・カップリング定数を記録。vinyl proton の coupling pattern (¹J_HH for cis/trans) で確実に区別。積分面積から ratio を再決定。
- 異なる GC コラム（スピロキサン、OV-101 等）での分析を実施し、基線分解能を確認。
- 反応時間を変化させ（1 時間、5 時間、20 時間），cis:trans ratio の時間依存性を測定。平衡到達が観測されるか（速度論的 vs 熱力学的制御の区別）。

**注記**: TEMPERATURE_SUMMARY に high_convergence_low_gap (A-2, convergence 3/3, low gap). U-4 は「提案機構が予測する立体特異性と矛盾」する自己矛盾的不在の critical severity.

---

#### **Group 3: 触媒回転と機構的探針**

**グルーピング**: V1-Q10, V1-Q11, V2-Q4, V2-Q6, A-1, U-1, U-2

**Primary RI**: **RI-03** (Unobserved explanatory) — 触媒循環の中間体（複合体 1, 2, 3）の未観測

**Secondary RI**: **PRI-11** (Mechanism-kinetics decoupling)

**ER**:
- 触媒回転数（TON）の測定と報告。ニッケルが触媒的に消費されるか、化学量論的に消費されるかの確認。
- 触媒循環の各中間体の分光学的特性付け（¹H/¹³C NMR chemical shifts, IR stretches, ESR for potential radicals）。
- 提案サイクルから速度式を代数的に導出し、実験的速度則（各成分の反応次数）と比較。

**EP**: EP-10a (Kinetic verification pack); EP-03a (Direct-observation / state-assignment pack)

**Case-specific 実装**：
- 初期速度法（excess halide と Grignard をアルゴン下で混合，異なる [Ni], [RMgX], [R'X] で反応速度を測定）。
- 温度依存性（298–333 K）から活性化パラメータ ΔH‡, ΔS‡ を抽出。
- ¹H/¹³C NMR による中間体の追跡：L₂NiEt，L₂NiPh などの Ni-alkyl/aryl chemical shifts は文献（例：Yamamoto et al., organometallic NMR databases）と比較。
- 制御実験：
  - 触媒なし（反応は進行しない予想）
  - ホスフィン配位子なし（活性喪失予想）
  - 化学量論的 Ni（回転せず、1:1 Ni:product のみ）

**注記**: TEMPERATURE_SUMMARY に high_convergence_low_gap (A-1, convergence 2/3). U-1, U-2 は critical/high severity で、触媒循環仮説の実験的根拠の完全な欠如を示す。

---

#### **Group 4: 収率決定と生成物純度検証**

**グルーピング**: V1-Q6, V3-Q1, V3-Q2, V3-Q9, B-5, B-6, U-3, U-5

**Primary RI**: **RI-01** (Reporting integrity)

**Secondary RI**: RI-08 (Unquantified reliability)

**ER**: 
- GC 内部標準法の標準化：応答係数の決定法・較正曲線範囲・直線性・再現性の記載。
- 分離収率の報告形式の統一：分離重量 × (GC purity %)。蒸留時の頭部・尾部分取データ。
- 質量バランス：投入有機ハライドの質量 = （回収生成物 + 回収ハライド + 推定ホモカップリング + その他）。各項をパーセンテージで閉鎖。

**EP**: EP-01a (Reporting-coherence pack); EP-08a (Replication / uncertainty pack)

**Case-specific 実装**：
- 例1（m-ジクロロベンゼン）について：投入物 7.93 g m-dichlorobenzene，回収生成物 9.63 g（報告済）。crude residue の総質量は？加水分解・抽出後、乾燥前の重量。蒸留による損失（6%）はどの副産物か（未反応ハライド の揮発性？ホモカップリング生成物のエーテルへの溶解？）。GC-MS で crude mixture を分析し、全ピーク面積の 100% 帳尻が合うか確認。
- 表 I の各エントリーについて、GC 較正曲線データを提示。arylethanes (Ph-Et)，vinylbenzenes (PhCH=CH₂)，disubstituted benzenes (di-n-Bu-benzene) 等の異なる化学クラスについて FID 応答係数が統一仮定（外部標準 n-dodecane）でよいか実験確認。
- 蒸留時の分取条件：目的物のみの単一分取か、あるいは複数フラクションからの合算か。沸点範囲（例：±0.5°）、圧力補正（5 mmHg のみか、別圧での測定も含むか）。

**注記**: TEMPERATURE_SUMMARY に high_convergence_high_gap (B-5: convergence 3/3, temperature_gap medium). これは V1 (high), V2 (高), V3 (critical) の三者が同一の問題（収率報告の基礎が検証されていない）に収束しながら、温度（重要度の段差）が 2 段階（medium=2）ある。

---

#### **Group 5: 反応条件最適化と機構的根拠**

**グルーピング**: V1-Q4, V1-Q5, V2-Q7, B-3

**Primary RI**: **RI-07** (Unsupported boundary)

**Secondary RI**: RI-01 (Reporting integrity の条件最適化の側面)

**ER**: 反応条件（温度プロファイル、触媒濃度、溶媒）を変化させた系統的研究。各条件セットで収率・選択性（cis:trans, cross:homo）を測定。条件が「最適」であること（例：報告條件で収率が最大か）、または「等価」であること（例：−78°から室温への昇温が他の温度プロファイルと同等か）の実験的根拠。

**EP**: EP-07a (Boundary-test pack)

**Case-specific 実装**：
- 触媒濃度の系統的変化：[NiCl₂(dpe)] = 1, 5, 10 mol% に対し、一つの代表的基質ペア（例：n-BuMgBr + PhCl）で反応を実施。各について、収率・反応時間・ホモカップリング%（GC 推算）を記録。10 倍の濃度範囲で速度はどう変化するか（1次？0次？）。
- 溶媒の比較：例1（純 Et₂O）vs 例2（Et₂O:benzene:THF = 2:3:1）vs 純 THF で、同一基質ペアの反応性を直接比較。収率・cis:trans 比・反応速度・副産物分布を測定。Et₂O の優越性が定量化されるか。
- 温度プロファイル：例1（0°で添加 10 分、加熱 20 時間）と異なる加熱条件（25°で添加、即加熱；0°から 25°への徐々の昇温）で反応歩留まりを比較。加熱時間の短縮可能性（例2 の 20 時間は必須か？）。
- 外熱反応条件（例1 entry 1 で「発熱」と記載）の温度制御：温度プローブを反応混合物に直接挿入し、発熱時の温度上昇幅・到達最高温度・冷却時間を記録。発熱の放置と外部冷却で収率が異なるか。

**注記**: B-3 は mixed classification（intentional narrowing と reporting omission の混合）。B-2（触媒濃度の 10 倍範囲）の根拠未説明と連動。

---

#### **CLA（SRG に属さないもの）: D-4-1 から D-4-9**

**CLA-1: D-4-1「触媒回転数と中間体の実験的検証の不在」（A-1 ↔ B-5）**

**Primary RI**: RI-03 + RI-01

**Content**: 触媒循環式（式 2–4）は触媒再生と回転を前提としているが、回転数（TON）測定もニッケルの化学量論的消費の検証も報告されていない（U-1）。同時に、収率は「分離」または「GC 内部標準」で報告されているが、GC 較正曲線・応答係数の標準化が記載されていない（B-5）。この二つの欠落は機構的陳述と定量的陳述の双方の検証が後回しにされている自己矛盾的不在。

**ER**: 触媒効率（TON, TOF）の実験的確立。定量的収率の分析的根拠の透明化。

**EP**: EP-10a (Kinetic verification pack); EP-01a (Reporting-coherence pack)

**Case-specific 実装**: 
一つの代表的反応（例1: m-dichlorobenzene + n-BuMgBr）について：
- 分析的収率：GC 較正曲線から得た molar yield (%) × 分離生成物の質量 ÷ 理論値，を報告。
- 触媒回転数：(mol product)/(mol Ni catalyst)。
- 反応後の Ni 錯体の回収と分析（例：ニッケル標準物質の希釈系列と比較，ICP-MS または原子吸光で確認）。回転が報告値と一致するか。

---

**CLA-2: D-4-2「Cis/trans 選択性のメカニズムと分析的根拠の同時的欠落」（A-2）**

**Primary RI**: RI-03

**Secondary RI**: RI-04

**Content**: 両方の幾何異性体（cis/trans）が「異常に」cis-富化スチルベンを与える現象は、機構的・分析的・熱力学的の三層で説明されていない。提案された σ-ビニル中間体の立体特異性の仮説と矛盾する。分析的には cis/trans 比の決定方法が未記載（GC か NMR か不明確；基線分解能未確認）。

**ER**: Cis/trans 異性体の構造的区別と定量分析。選択性（速度論的 vs 熱力学的）の判定実験。

**EP**: EP-03a (Direct-observation / state-assignment pack); EP-04a (Discrimination / replication pack)

---

**CLA-3: D-4-3「グリニャール試薬過剰量の消費経路と質量バランスの未説明」（U-3）**

**Primary RI**: RI-08 (Unquantified reliability — 内部矛盾型)

**Content**: 触媒条件では Grignard 試薬を 1.1–1.3 倍過剰に供給（表 I）。例1 では 120 mmol Grignard が ~54 mmol dichlorobenzene に添加。生成物が 60 mmol 以下であれば、残りの Grignard 等価物の運命が不明確。ホモカップリング（R–R'）、ジスプロポーショネーション、未同定副反応か。

**ER**: Grignard 過剰の消費経路の定量化。質量バランスの閉鎖。

**EP**: EP-09a (Internal benchmark pack)

---

**CLA-4: D-4-4「ニッケル中間体（1, 2, 3）の分光学的実体化の不在」（U-2）**

**Primary RI**: RI-03 (Unobserved explanatory)

**Content**: 提案された触媒循環（式 2–4）は特定の中間体（ジオルガノニッケル複合体 1、ハロ(オルガノ)ニッケル複合体 2、ジオルガノ複合体 3）を名指ししているが、分光学的特性（化学シフト、カップリング定数、赤外吸収）が報告されていない。

**ER**: 中間体の NMR / IR / ESR による特性付け。

**EP**: EP-03a (Direct-observation / state-assignment pack)

---

**CLA-5: D-4-5「速度論的制御 vs 熱力学的駆動の問い——選択性と収率の分離」（独立高 critical）**

**Primary RI**: RI-06 (Imported model)

**Content**: スチルベン cis/trans 選択性とホモカップリング vs クロスカップリング選択性の両方について、観察された結果（80:20, 43:57；高収率）を報告しているが、それらが速度論的制御（競争する消滅速度）か熱力学的駆動（中間体・生成物の安定性）かを区別していない。

**ER**: 温度変化実験、異なる溶媒下での選択性、活性化パラメータ測定。

**EP**: EP-10a (Kinetic verification pack)

---

**CLA-6: D-4-6「Tamura-Kochi 比較の定量的ギャップ」（C-1）**

**Primary RI**: RI-09 (External superiority)

**Content**: 論文は Tamura-Kochi の Ag/Cu/Fe 触媒を背景として引用し、「substantial amounts」のホモカップリング・ジスプロポーショネーション生成が問題であると述べ、Ni-dpe 系がこの問題を「解決する」と暗に主張するが、直接的な数値比較（収率・選択性）が提供されていない。

**ER**: Tamura-Kochi の同一基質ペアでの結果との並行比較。

**EP**: EP-09a (Internal benchmark pack)

---

**CLA-7: D-4-7「触媒配位子選択の説明的根拠の不在」（B-1）**

**Primary RI**: RI-07 (Unsupported boundary)

**Content**: 脚注 21 で [NiCl₂(dpp)] > [NiCl₂(dpe)] の活性順が確立されているにもかかわらず、表 I の基質スコープは [NiCl₂(dpe)] でのみ実行。最適配位子ではなく劣位配位子を選んだ理由が述べられていない。

**ER**: [NiCl₂(dpp)] と [NiCl₂(dpe)] の直接比較（表 I の代表的エントリー複数で並行実施）。活性度の差が無視できるか、または dpe を選んだ実用的根拠（入手性、合成容易性）の記載。

**EP**: EP-07a (Boundary-test pack)

---

**CLA-8: D-4-8「溶媒選択の機構的根拠の不在」（B-3）**

**Primary RI**: RI-07 (Unsupported boundary)

**Content**: 「[REDACTED: verbatim source text; see the source paper via its DOI]」と述べられるが、この優越性の機構的基盤（速度論的か熱力学的か？）が問われていない。例2 で使用された混合溶媒（ether:benzene:THF = 2:3:1）との比較も説明されていない。

**ER**: 溶媒の系統的比較。

**EP**: EP-07a (Boundary-test pack)

---

**CLA-9: D-4-9「Corriu-Masse 並行報告との機構的差異の未検討」（C-2）**

**Primary RI**: RI-06 (Imported model)

**Content**: Note Added in Proof で Corriu-Masse による Ni(acac)₂ を用いた並行通信が言及されるが、この並行系との機構的関係（同一の触媒循環か、異なる経路か？）が検討されていない。

**ER**: Ni(acac)₂ と [NiCl₂(dpe)] の機構的・動力学的比較研究。

**EP**: EP-04a (Discrimination / replication pack)

---

### §3 現在のVQ判定

**Step 3a: Modern reassessment baseline での判定**

**VQ-1（Observation）: 通過（限定的）**
- RI-02（Object identification）の要件：生成物の構造・純度が代替候補を排除できる粒度で確定されているか。
- 達成度：物理定数（bp, n_d）と文献値の比較により、生成物の同定は大まかには確立。しかし GC purity は報告されていない（B-6）。文献値からの偏差（例2 で n_d 差が ±0.0018）が許容範囲内か不明。
- **判定**：**VQ-1 achieved（限定的）— RI-02 は非致命的に残存するが、同定の骨子は成立。**

**VQ-2（Method）: 未達**
- RI-01（Reporting integrity）の要件：測定フレーム・条件記述の一貫性。
  - 現状：GC 内部標準と分離収率の混用（B-5）；較正曲線なし；応答係数の標準化なし。
  - 判定：**RI-01 未解消（Fatal）**。Table I の 11 エントリーの収率が同一の方法論基準で報告されていない。
- RI-07（Unsupported boundary）の要件：条件の「最適性」が実験で支持されているか。
  - 現状：触媒濃度 10^{-2}–10^{-3}（10 倍範囲）、溶媒（Et₂O vs 混合 vs THF）、温度プロファイル（0°添加 vs −78° 冷却等）が実験的に比較されていない。
  - 判定：**RI-07 未解消（Fatal）**。
- **判定**：**VQ-2 not reached**（RI-01 と RI-07 の両方が未解消で、継承要件 VQ-1 達成も限定的）。

**VQ-3（Mechanism）: 未達**
- RI-03（Unobserved explanatory）の要件：提案メカニズムが予測する観測量の報告。
  - 現状：触媒循環の中間体（1, 2, 3）が分光学的に観測されていない（U-2）；回転数が測定されていない（U-1）；速度式の導出と実験速度則の比較がない（PRI-11）。
  - 判定：**RI-03 未解消（Fatal）**。メカニズムの「検証」段階に到達していない。
- RI-04（Unreplicated discriminator）の要件：cis/trans 比等の識別的データが分析精度・代替経路排除なく報告されているか。
  - 現状：cis:trans 比（80:20, 43:57）の分析法が未記載（GC か NMR か不明確）；基線分解能確認なし（B-9）。
  - 判定：**RI-04 未解消（Fatal）**。
- RI-06（Imported model）の要件：σ-ビニル中間体の仮説が対象系（Ni-halide + Grignard）でのローカル検証を受けているか。
  - 現状：σ-ビニル機構は Pd や Ni の有機金属化学の慣例に基づくが、本反応での立体特異性の実験的観測（U-4）は σ-モデルと矛盾する。代替経路（π-アリル中間体、ラジカル経路）の排除実験がない。
  - 判定：**RI-06 未解消（Fatal）**。
- **判定**：**VQ-3 not reached**（RI-03, RI-04, RI-06 の全て未解消）。

**VQ-4（Benchmark）: 未達**
- RI-08（Unquantified reliability）の要件：質量バランス・反復測定・不確かさ。
  - 現状：crude yield と分離収率の関係が未記載（例1 で 6% の損失は未説明；U-3）；単一実施（replication 数未記載）；測定不確かさなし。
  - 判定：**RI-08 未解消（Fatal）**。
- RI-09（External superiority）の要件：Tamura-Kochi との直接数値比較。
  - 現状：比較データなし（C-1）。優越性は暗に仮定されるのみ。
  - 判定：**RI-09 未解消（Fatal）**。
- **判定**：**VQ-4 not reached**（RI-08, RI-09 未解消）。

**総合判定**

```
現在判定: VQ-1 achieved（限定的）
  → VQ-2 not reached（RI-01, RI-07 Fatal）
  → VQ-3 not reached（RI-03, RI-04, RI-06 Fatal）
  → VQ-4 not reached（RI-08, RI-09 Fatal）
```

---

### §4 Era-Norm Annotation

**communication-era tolerated:**

1. **B-5（GC・分離収率の混用）**: 1972 年 JACS Communications（3 ページ）では、複数の収率基準の混用が許容された。完全な GC 較正曲線は Supporting Information 等で補足されることが慣例。**era-norm toleration**: Yes. 通信形式では詳細な分析方法の記載は常に省略された。

2. **B-6（蒸留詳細の略記）**: 1970 年代では、有機合成の精製は「標準的な操作」と仮定され、蒸留時の頭部・尾部分取、収集温度幅などは付加記載されなかった。文献値との bp・nd 一致が純度の代理指標と見なされた。**era-norm toleration**: Yes. 現代でも Full Paper では Experimental に詳細が記載されるが、Communication では省略常態。

3. **B-2（触媒濃度の 10 倍範囲）**: 1972 年では、新規触媒系の報告は実験的最適化の完全性よりも「反応が動作する」ことの実証を優先した。条件の「未最適性」を明示する選別はなく、「representative conditions」として報告された。**era-norm toleration**: Yes. 後続論文で最適化が行われることが期待された。

4. **U-1（触媒回転数未測定）**: 新規触媒報告において、回転数の絶対測定は 1970 年代では「将来の課題」と明記されることで許容された（A-1 で「Further studies are required」と明示）。ただし明示がない場合は toleration が弱まる。本論文では明示されているため toleration: Marginal（明示されているため許容但し現代基準では不十分）。

5. **A-1（機構的検証の後送り）**: 同様に「将来の課題」明示による toleration.

**modern-era deficient:**

1. **RI-02（生成物純度の GC% 未報告）**: 現代の化学出版（Nature Chem., JACS, etc.）では、有機合成の全出力物について GC purity または NMR assay を最小限報告することが基準。本論文の「colorless liquid」という描写のみでは不十分。→ **modern deficiency**: 深刻。

2. **RI-01（報告一貫性の欠落）**: GC 較正曲線・応答係数の完全な記載は現代では必須（ISO 基準、GC-MS 定量分析の best practice に合致）。1972 年では FID の「定量性」自体が自明視されていたが、現代では器械依存性の明示が必須。→ **modern deficiency**: 高。

3. **RI-03（中間体未観測）**: 1970 年代では理論的提案の「機構」が完全に検証されないまま、観測される反応結果と consistency を示すだけで許容された。現代では、提案機構の各段階（oxidative addition, reductive elimination）が少なくとも NMR spectroscopy で追跡されることが基準に近づいている。→ **modern deficiency**: 最も深刻。

4. **PRI-11（動力学データなし）**: 1972 年では「触媒循環」の提案が、kinetic rate law の導出なしに行われることが標準的であった。現代では、提案サイクルから速度式を代数的に導出し、実験的速度則と照合することが Mechanism validation の必須条件と見なされるようになった（特に 2010 年代以降）。→ **modern deficiency**: 重大（50 年間の methodological shift）。

5. **RI-07（最適性未実証）**: 条件が「最適」か「representative」かの区別は 1972 年では明記されないことが多かった。現代では、報告条件が single-point data であることを明示するか、または複数条件の systematic variation を示すことが期待される。→ **modern deficiency**: 中程度。

---

### §5 最短補強ルート

**目的関数**

現在 VQ-1 (limited) → 第一目的：**VQ-2 達成**（Method として認可）。第二目的：VQ-3, VQ-4（現実的には VQ-2 達成後の multi-year project）。

**Step 5a: VQ-2 到達のための最短 EP 投入順序**

根拠：VQ-2 は RI-01（Reporting integrity）と RI-07（Unsupported boundary）の同時解消を要する。情報利得と実行可能性から以下の順序を推奨：

**1. EP-01a（Reporting-coherence pack）**

目的：Table I の全エントリーについて、統一された収率報告基準を確立。

実装の詳細：
- (1a) GC 較正の標準化：
  - 各化学種（arylethanes Ph-Et, vinylbenzenes PhCH=CH₂, disubstituted benzenes di-n-Bu-Ph 等）について、複数濃度（0.1, 0.5, 1.0, 2.0, 5.0 mM）の FID 応答を測定。
  - 同一サンプルを 3 反復測定。内部標準 n-dodecane (1.0 mM) との応答係数を個別に決定。
  - 線形性（R² > 0.999）と再現性（RSD < 2%）を確認。
- (1b) 例1・例2 の生成物について、GC-MS で精密質量と fragmentation pattern から構造確認。
- (1c) 蒸留後の生成物を GC（上記較正曲線を用いた定量分析）と NMR（¹H NMR で anomeric/vinyl proton の積分）で purity 決定。例1 なら m-di-n-butylbenzene の純度を % で報告；例2 なら α-vinylnaphthalene の異性体純度（α vs β）を確認。
- (1d) Table I の 11 エントリー全体について、分離収率を「分離生成物の質量 × (GC purity %) / 理論値」で再計算。

期待される改善：GC の定量的根拠が透明化され、RI-01（Reporting integrity）の RI subtype「内部矛盾型（RI-08 style）」が解消。

**2. EP-07a（Boundary-test pack）**

目的：報告条件（[Ni], solvent, temperature profile）が「最適」か「representative」かの区別を実験で示す。

実装の詳細：
- (2a) 触媒濃度の系統的変化：[NiCl₂(dpe)] = 1, 5, 10 mol% を n-BuMgBr + PhCl（例1 の基質）に適用。各について、反応時間・粗収率・GC selectivity（cis:trans, cross:homo）を測定。
  - 予想：10 mol% が最高収率を与える場合、その条件を「optimal」と名付ける；1 mol% でも競争力がある場合、「representative」と明記。
- (2b) 溶媒の直接比較：同一の n-BuMgBr + PhCl で、Et₂O （例1）vs 混合溶媒（例2）vs THF を並行実施。収率・反応時間・副産物分布（GC-MS）を比較。
  - 予想：Et₂O が優越する場合、その機構的根拠（例：ホモカップリングの Ni-alkyl intermediate の安定性が Et₂O で低下）を初期速度法で検証。
- (2c) 温度プロファイルの最適化：
  - 0° で添加，即座に 70°C 加熱（従来の 20 時間）vs 0° で 2 時間 stirring 後に加熱 vs −78° から徐々に昇温。
  - 各プロファイルで収率・反応時間・副産物を測定。加熱時間の短縮可能性を評価。

期待される改善：条件の「最適性」が実験的に根拠付けられ、RI-07（Unsupported boundary）が解消。

**3. EP-08a（Replication / uncertainty pack）（オプション）**

目的：測定の不確かさと再現性を定量化。

実装：
- 例1 および例2 について、同一実験を 3 反復実施。分離収率・bp・nd の平均値と標準偏差を報告。
- 蒸留環境（気圧、室温）の月ごとの変動が bp に及ぼす影響を補正。

期待される改善：RI-08（Unquantified reliability）の「反復測定不足」が解消。

**認定ゲート順の明示**

EP 投入順は情報利得・実行可能性に基づくが、**VQ 認定は VQ-1 → VQ-2 → VQ-3 → VQ-4 の継承順で確定する**。

- EP-01a を完成させた後、RI-01 達成を確認してから，EP-07a による RI-07 解消に進む。
- RI-01 と RI-07 の両方が非致命的（Fatal でない）状態になって初めて，VQ-2 達成と認定。
- VQ-2 達成まで，VQ-3 の評価開始は推奨されない（継承原則）。

---

**Step 5b: VQ-3 達成のための後続 EP（VQ-2 達成後）**

**4. EP-10a（Kinetic verification pack）**

目的：触媒循環と速度式の統御。

実装：
- 初期速度法（−40°C in CD₂Cl₂）でリアル [Ni], [RMgX], [R'X] の各反応次数を決定。
- 提案サイクル（式 2–4）から速度式を代数導出し、実験速度則と照合。
- 温度依存性（298–333 K）から Arrhenius parameters を抽出。

**5. EP-03a（Direct-observation / state-assignment pack）**

目的：触媒循環の中間体の分光学的追跡。

実装：
- 低温 NMR で L₂NiR species の化学シフト・カップリング定数を記録。
- IR で Ni-R stretch の帰属。
- 文献の organometallic Ni-R NMR data と比較し，中間体の structure assignment を検証。

期待される改善：RI-03, RI-04, RI-06 が同時に解消され，VQ-3 達成。

---

### §6 制度設計への寄与

**1. RI-03 subtype 提案: 「Unobserved catalytic-cycle intermediates」**

本論文は RI-03（Unobserved explanatory）の canonical example として機能するが、より細分化が有用と考えられる：

- **RI-03a: Unobserved catalytic-cycle intermediates** — 触媒循環が特定の中間体（例：L₂NiR₂, L₂Ni(R)(R'X)）を仮定するが、分光学的確認（NMR, IR, ESR）がない。循環の stoichiometry と elementally step の検証が後送りされている。

対象論文群：触媒報告論文、特に 1970–1990 年代の transition metal catalysis 報告。

本論文の位置付け：PRI-11（Mechanism-kinetics decoupling）と連動。機構的「仮説」と動力学的「証拠」の双方が後回しにされる同期的パターン。

---

**2. PRI-11（Mechanism-kinetics decoupling）の exemplar 登録**

本論文（Kumada 1972）は PRI-11 の founding exemplar として正式登録推奨。

根拠：
- 触媒循環（式 2–4）を提案しながら，速度初期化・反応次数・活性化エネルギー・isotope effects が報告されていない。
- [REDACTED: verbatim source quotation; see the source paper via its DOI] との明示的な deferral.
- 50 年後の現代基準（2025 年）では，このような deferral は許容されない；同時代（1970 年代）では標準慣行であった。

他 exemplar との位置付け：Breitenfeld 2014 (Pd-catalyzed coupling, kinetic measurement あり但し mechanism detail 省略)，Pengfei 2024（DFT prediction without kinetic validation）と並列.

---

**3. VQ non-symmetry pattern の検出: 「Bifurcated validation structure」**

本論文は **VQ asymmetry** を示唆する：

- **実用的成果層**（Table I: yields 76–98%）→ VQ-1 達成（with qualification）
- **機構説明層**（Equations 2–4: catalyst cycle）→ pre-VQ-1（unobserved intermediates；no kinetics）
- **最適化層**（ligand superiority, solvent choice）→ VQ-1 以下（unsupported boundary）

この bifurcation は「反応が動作する」という操作的事実と「なぜ動作し、なぜこの条件が最適か」という理解的主張が逆相関する構造を示す。設計含意：*新規催化反応報告では、実用的成果と機構理解の VQ 非対称性を明示する reporting standard の導入を検討すべき。*

---

**4. Era-Norm Toleration の boundary case: 「communication format implicit deferred claims」**

本論文のように Note「Further studies required」を明示する communication は，明示なしのそれと区別すべき：

- **明示型**（本論文）: A-1, A-2 が explicitly deferred → communication-era tolerated として分類.
- **非明示型**: 同等の mechanistic gaps が明記されず、mechanism language（indicative mood）で述べられている → modern-era deficient として classification.

提案：era-norm annotation で「deferral explicitness」を metacode として記録。

---

**5. 新規 PRI 候補の未発見**

本論文の分析では、既存 RI / PRI framework に収まらない新パターンは検出されなかった。RI-03, RI-04, RI-06, RI-07, RI-08, RI-09, PRI-11 の既存 codebook で網羅可能。

制度設計への寄与：本ケースは既存 codebook（v0.3）の cross-domain applicability を追認した。

---

**6. Self-referential validation check（PRI-12 cluster A）の該当性**

本論文において、self-referential validation の閉ループは検出されない：

- (a) 検証指標と被検証対象の数学的依存性なし（「収率」で「収率」を検証していない）
- (b) 検証基準が提案理論の前提と循環していない（「触媒循環の検証」が「触媒循環の仮説」で定義されていない）
- (c) 記述子の妥当性が記述子自身で評価されていない

判定：**PRI-12 cluster A 不該当**。本論文の問題は「検証の欠落」（deferred）であり、「循環的検証」（circular）ではない。

---

**7. Deductive-retrospective structure check（PRI-12 cluster B）の該当性**

本論文は理論提案論文ではなく、実験的方法論報告であるため、PRI-12 cluster B（演繹的遡及構造）は原則不該当。ただし、proposed mechanism（式 2–4）の演繹的性質（Grignard と Ni-dpe から σ-ビニル中間体を推論）に限定した検討：

- (b) 反証条件が operationally 定義されていない：「非stereospecific」な観察（cis/trans convergence）が提案機構の予測と矛盾するが、反証と解釈されず「anomalous」と標記。
- (c) 理論提案（触媒循環）の検証が後続論文に委譲されている（A-1, A-2 の deferred）。

判定：**PRI-12 cluster B 部分的該当** — (b), (c) の traits が観察される。但し主問題は PRI-11（kinetics decoupling）として既に捕捉済。

---

**8. Labeling mismatch pattern の検出**

表現上のパターン：
- 假说標示：A-1 "Further studies are required..."（Explicit deferral）
- 述語選択：本文「[REDACTED: verbatim source text; see the source paper via its DOI]」（indicative mood の "react", "give"）

これらの乖離は RI-01（reporting integrity）の subtype として記録可：

- **RI-01b: Prospective-mechanism labeling mismatch** — 提案機構が仮説的であることを Deferral sentence（末尾 1 文）に限定し、本文の述語は機構を事実的に述べている。読者が mechanism claim の status（仮説 vs 立証済み）を誤識する可能性。

---

**Codebook への推奨追記**

以下の細分化を v0.4 で検討：

1. **RI-03a: Unobserved catalytic-cycle intermediates** — Kumada 1972 を exemplar として登録.
2. **RI-01b: Prospective-mechanism labeling mismatch** — 本論文を exemplar.
3. **PRI-11 exemplar**: Kumada 1972 を founding exemplar として正式登録.
4. **Era-norm Meta-code「deferral-explicitness」**: 「Future studies」の明示有無で communication toleration の可否を subclassify.

---

**制度設計への根本的寄与**

本論文は **「反応は動作する」と「反応はなぜこの機構で動作するか」の VQ 乖離**を顕在化させた。Reporting standard を「実用的成果」と「理解的主張」の独立 VQ 追跡に移すことで、communication format の信頼性を向上させうる。

---

**END OF ASSESSMENT SHEET**

inference_time_sec: not available — inject externally

---

> **Public-cut redaction notice**: verbatim quotations from the analysed papers in this file have been replaced by `[REDACTED: …]` markers (rules in the repository README). The unredacted file is in the reviewer version of the deposit.
