prompt_version: stage3-v1-20260402
model_info: claude-sonnet-4-6

# 科学的知見の再認定判定票

## Tamao et al. 1976（Bulletin of the Chemical Society of Japan, full paper）

---

### §1 Claim Architecture

**コア主張（要約）**

Novelty柱：ジハロジホスフィンニッケル(II)錯体——代表として[Ni(dppp)Cl₂]（アルキル・アリールGrignard用）、[Ni(dmpe)Cl₂]（アルケニル・アリルGrignard用）、[Ni(PPh₃)₂Cl₂]（立体障害アリール基質用）——が「極めて高い触媒活性」を示してGrignard試薬とアリール・アルケニルハロゲン化物の選択的クロスカップリングを触媒すること。β-水素を持つGrignard試薬でも選択的に進行し、有機クロリドが最適基質となるという一般原則を含む。

Utility柱：温和な条件下（エーテル系溶媒、室温〜還流）、安価で入手容易な有機クロリドを用い、触媒はGrignard試薬中で16時間経時しても活性低下がない。Table 7の~60エントリーが実用的な合成有用性を実証する。

**Layered structureの判定**

Layer (i)「高い触媒活性」：GLPC収率値が根拠。SRG-3（GLPC精度）とSRG-4（収率基準不統一）への攻撃を受けるが、個別収率の不確かさはスコープパターンの全体を崩さない。

Layer (ii)「広い基質スコープ」：Layer (i)の一部信頼性を前提とするが、多数のエントリーの合算として成立するため、単一エントリーへの反証では崩れない。A1（「条件は最適化されていない」）注記がさらにLayer (ii)を保護する。

Layer (iii)「実用性」：有機クロリドの優位性・触媒安定性・スケール実証が独立に主張されるため、Layer (i)/(ii)への攻撃でも直ちには崩れない。

層間依存関係：Layer (i)の定量的精度はLayer (ii)の「高収率」という強調を支えるが、Layer (ii)の「スコープが広い」という定性的主張には不可欠ではない。Layer (iii)の実用性はLayer (ii)のスコープの実在を前提とする。Scheme 1（機構、SRG-1）はどの主張層にも支持を提供するが、どれの成立にも必須ではない——機構の誤りは観察された触媒活性を打ち消さない。

---

### §2 SRG / CLA → RI / ER / EP Crosswalk

---

**SRG-1 [触媒サイクル実験的正当化の欠如]**

* **Primary RI**: RI-06 Imported model
* **Secondary RI**: RI-03 Unobserved explanatory; RI-04 Unreplicated discriminator
* **ER**: Scheme 1の各素反応ステップを本触媒系（Ni-ホスフィン触媒条件）に適用可能であることを示すため、(a) 触媒条件下または触媒モデル反応でのNi(0)→Ni(II)酸化的付加中間体またはジオルガノニッケル(II)中間体の直接観測、もしくは (b) Felkin-Corrieメカニズムを排除する交差実験または同位体標識実験が必要である。
* **EP**: EP-06a Analogy-validation pack; EP-04a Discrimination/replication pack; EP-03a Direct-observation/state-assignment pack
* **Case-specific実装**: (1) R-X（例：PhCl）とR'-X'（例：MesCl）の混合に触媒量[Ni(dppp)Cl₂]を加えてクロス生成物とホモ生成物の比を測定するクロスオーバー実験——混合型L₂Ni(R)(R')中間体経由の還元的脱離を検証（Scheme 1 step 3-4 vs. Felkin-Corriu）；(2) [Ni(dppp)Cl₂]触媒存在下n-BuMgBr + PhClのin situ ³¹P NMRモニタリングによる触媒休止状態の同定；(3) refs 30-31のL₂NiR₂モデル錯体をTHFに溶解してPhClを加え、触媒的ターンオーバーが起きることを示す
* **注記**: A2（critical, 1/3収束：low_convergence_high_gap—V2のみcritical）、A6（high, V2）、A8（high, V2）、C3（stoichiometric analogy basis）、C4（ref 46単一引用）、U1（MgXX'未評価）、U2（β-消去自己矛盾）

---

**SRG-2 [主要限界の定量的実体の欠如]**

* **Primary RI**: RI-07 Unsupported boundary
* **Secondary RI**: RI-05 Qualitative overread
* **ER**: アルキルGrignard試薬＋ジハロエチレン（例：n-BuMgBr + cis-ClHC=CHCl）の反応を少なくとも1例、[Ni(dppp)Cl₂]触媒・標準条件下でGLPC分析し、クロスカップリング生成物・ホモカップリング生成物・未反応原料を定量化するとともに主要生成物をスペクトル同定する必要がある。
* **EP**: EP-07a Boundary-test pack
* **Case-specific実装**: n-BuMgBr（2 mmol）+ 1,2-ジクロロエチレン（cis体/trans体別々に、1 mmol）、[Ni(dppp)Cl₂]（1 mol%）、Et₂O、RT、3 h・6 h・24 hの時間経過サンプルをGLPC分析（n-アルカン内標準）——n-オクタン（ホモカップリング）、クロロブチルエチレン（モノカップリング）、1,2-ジブチルエチレン（ビスカップリング）の各収率を報告
* **注記**: B2（3/3収束・最強：high_convergence_low_gap; V1=high×2, V2=high, V3=medium）、A1（「条件は最適化されていない」免責との連動）

---

**SRG-3 [GLPC定量基盤の測定信頼性の欠如]**

* **Primary RI**: RI-08 Unquantified reliability
* **Secondary RI**: RI-01 Reporting integrity
* **ER**: ~60の収率値が横比較に耐えるためには、(a) 完全なGC操作条件（カラム温度・キャリアガス流量・検出器仕様・注入量）、(b) 各基質クラスの代表化合物の応答係数、(c) 少なくとも1エントリーの反復測定による測定不確かさの定量化、を報告する必要がある。
* **EP**: EP-08a Replication/uncertainty pack; EP-01a Reporting-coherence pack
* **Case-specific実装**: (1) 代表的生成物（例：n-ブチルベンゼン）の1点検量→3点検量曲線への置換とRSD報告；(2) n-ブチルベンゼン/メシチレン系とn-ブチルベンゼン/n-アルカン系の応答係数クロスバリデーション（B9解消）；(3) U3の問題（Table 3 PhCl 2h: 収率81%>転化率80%）について、同一サンプルの反復注入6回によるSD評価——U3の数値が測定誤差範囲内かを確認
* **注記**: B4（high, V3）、B5（high, V3）、B9（medium, V3）、U3（medium, V1+V3; 収率>転化率の内部矛盾）、B7（medium, V3）、B8（high_convergence_low_gap: V1=high, V3=critical; 2/3収束, gap=low）

---

**SRG-4 [Table 7収率比較可能性の欠如]**

* **Primary RI**: RI-01 Reporting integrity
* **Secondary RI**: （なし—SRG-3とは独立した報告フレームの問題）
* **ER**: Table 7全エントリーについて、共通の収率定義（限定試薬＝有機ハロゲン化物基準のGC収率を主値）に統一し、孤立収率はその差（精製損失）として別列または脚注に記載すること。Grignard試薬基準の収率は、その基準を選択した化学的理由（例：Grignard試薬が限定試薬のエントリー）とともに報告する。
* **EP**: EP-01a Reporting-coherence pack
* **Case-specific実装**: 現行Table 7の再構成——欄1：有機ハロゲン化物基準GC収率（GLPC測定値）、欄2：孤立収率（精製後）、欄3：収率基準の注記（G=Grignard試薬基準を選んだ場合）；B3の脚注t対象エントリーをハロゲン化物基準に換算して数値的差異を確認
* **注記**: B1（high_convergence_low_gap: V1=high, V3=high; 2/3収束, gap=none）、B3（high, V3）

---

**SRG-5 [選択性特徴の機構的根拠の欠如]**

* **Primary RI**: RI-05 Qualitative overread
* **Secondary RI**: RI-03 Unobserved explanatory
* **ER**: PhI>PhCl>PhBrという「奇妙な」反応性順序の「複数の律速段階」仮説を検証するため、少なくともPhI/PhCl競合速度論実験またはパラ置換アリールクロリドのHammett ρ値測定が必要である。
* **EP**: EP-05a Quantitative-ranking substantiation pack; EP-03a Direct-observation/state-assignment pack
* **Case-specific実装**: (1) [Ni(dppp)Cl₂]存在下、PhI（0.5 equiv）とPhCl（0.5 equiv）のn-BuMgBrとの競合反応——生成物比から相対速度定数比を算出；(2) パラ置換アリールクロリド（p-MeO, p-Me, p-H, p-Cl, p-NO₂）の[Ni(dppp)Cl₂]触媒反応でHammettプロット構築——ρ値の符号から酸化的付加または還元的脱離が律速段階かを判定；(3) U2解消：[Ni(dmpe)Cl₂]触媒での二級アルキルGrignard反応における²H標識（α-d₁またはβ-d₁）を用いた異性化機構の確認——β-水素脱離/再挿入経路のアイソトープ追跡
* **注記**: A3（2/3収束, gap=low: V1=medium, V2=high; high_convergence_low_gap）、A5（high, V2）、A6（high, V2—SRG-1とも共有）、A8（high, V2—SRG-1とも共有）、U2（high, V2—SRG-1とも共有）；SRG-5はSRG-1とA6/A8/U2を通じて重複するが、選択性特徴（halide order, β-elimination scope）の定量的検証という独立した問いを持つ

---

**SRG-6 [競合触媒系との数値的ベンチマーク欠如]**

* **Primary RI**: RI-09 External superiority
* **Secondary RI**: （なし）
* **ER**: Fe/Ag/Cu系（refs 15–17）およびPd-ホスフィン系（ref 22）に対する優位性の主張を検証するため、同一基質ペア（例：n-BuMgBr + PhCl）・同一条件下での直接比較実験が最低1例必要である。
* **EP**: EP-09a Internal benchmark pack
* **Case-specific実装**: n-BuMgBr（2 mmol）+ PhCl（2 mmol）、Et₂O、RT、3 h条件下で以下の触媒を同時並行試験：(a) [Ni(dppp)Cl₂] 1 mol%、(b) [Pd(PPh₃)₂Cl₂] 1 mol%（ref 22系）、(c) [Fe(acac)₃] 1 mol%（ref 15/16系）、(d) CuI 1 mol%；各反応をGLPC分析（同一条件・同一内標準）してn-ブチルベンゼン収率・ホモカップリング収率を一覧化
* **注記**: C1（Dropped Quantitative Benchmark; refs 15-17 Fe/Ag/Cu「极めて効果的」）、C2（Dropped Quantitative Benchmark; ref 22 Pd「類似の」）；TEMPERATURE_SUMMARY記録なし（C項目、単一エージェント観察）

---

SRG外：CLA

D-4全候補がいずれかのSRGに帰属しており、CLAは存在しない。

---

### §3 現在のVQ判定

**現在判定：VQ-1（Observation）**

**VQ-1 Observation — 通る**

RI-02（Object identification）の要件：主要生成物の同定はNMR・IR・MSおよび商業品との比較によって実施されており（Experimental Section）、生成物の構造的同定は1976年標準として満たされている。新規化合物には元素分析が付与されている。RI-02は非致命的に残存するとすれば、PhF反応（B8: GC上ベンゼンと共溶出、変換率未測定）においてクロスカップリング生成物の収率が代替的検証なしに報告されている点のみだが、これはVQ-1の成立を根底からは覆さない。VQ-1は通る。

**VQ-2 Method — 未達**

VQ-2の要件はRI-01（Reporting integrity）とRI-07（Unsupported boundary）の解消（＋VQ-1継承）。
- RI-01（残存、非致命的から致命的にまたがる）：SRG-3（GLPC操作条件・検量線不在、B4/B5/B9）とSRG-4（収率基準不統一、B1/B3）が未解消。U3（収率>転化率の内部矛盾）はRI-01の致命的残存として、少なくとも1エントリーで測定の一貫性が成立していない可能性を示す。
- RI-07（残存、境界主張に対し致命的）：SRG-2（B2）が未解消。アルキルGrignard＋ジハロエチレン「最も深刻な限界」の主張が、この基質クラスのデータ皆無のまま行われている。正のスコープ主張に対しては非致命的だが、境界主張に対しては致命的。
→ RI-01およびRI-07が未解消のためVQ-2未達。

**VQ-3 Mechanism — 未達**

VQ-2未達のため継承条件も不成立。SRG-1（RI-06）・SRG-5（RI-05, RI-03）がいずれも未解消。Scheme 1は外部類推（RI-06）に全面依存し、Felkin-Corriu経路との識別実験がない（RI-04）。

**VQ-4 Benchmark — 未達**

VQ-3未達のため不成立。SRG-6（RI-09）も未解消。

---

### §4 Era-Norm Annotation

**communication-era tolerated（1976年 BCSJ full paper）：**

- **B4（GLPC機器条件の不完全記述）**: 1976年のBCSJ誌は定量GLPCの機器条件（カラム温度・キャリアガス流量・検出器仕様）の完全記述を義務付けておらず、「装置名＋カラム充填剤」は当時の標準的記述水準に収まる。
- **B5（検量線・応答係数の不記載）**: 内標準法による定量GLPCにおいて検量線の省略は1970年代の分析化学分野では通例であり、「authentic sampleとの比較」は当時の認証として有効とみなされた。
- **B9（内標準物質の選択根拠の不記載）**: 異なる実験間での内標準物質の変更（メシチレン vs. 正アルカン）は、当時の合成報告書では慣習的にフットノートで処理された。
- **B1（孤立収率とGC収率の混在表記）**: Table 7の括弧表記によるGC収率明示は、孤立収率との区別を示す当時の標準的BCSJ表記慣行である。
- **C3（別系からの機構類推）**: 1976年時点では遷移金属触媒サイクルを別系の化学量論的反応から類推することが機構的提案の標準的アプローチであり、触媒系内での独立検証は必須とされなかった。
- **B7（一部エントリーでのベンゼン未定量）**: 特定の解析困難な副生成物を脚注で除外することは当時のBCSJ full paperでは許容された実務的記述である。

**modern-era deficient（現代基準）：**

- **B4/B5（GLPC条件・検量線の不記載）**: 現代の分析的収率報告では、完全なGC操作条件と代表的応答係数は再現性確保の必須要件であり、VQ-2達成のためにRI-01/RI-08の解消として要求される。
- **U3（収率>転化率の内部矛盾）**: Table 3のPhCl 2h entry（収率81%>転化率80%）は現代誌では「measurement inconsistency」として訂正要求の対象となり、論文データの全体的信頼性に疑義を投じる；RI-08の致命的残存として記録する。
- **B2（主要限界の代表データ皆無）**: 現代のスコープ論文では、著者が「最も深刻な限界」と明示した基質クラスの代表例を少なくとも1つ報告することが査読上の標準的要求であり、RI-07の現代的致命基準に抵触する。
- **SRG-4（収率基準不統一）**: 現代のクロスカップリングスコープ論文では、全エントリーを統一された収率定義（通常は限定試薬基準の孤立収率またはGC収率）で報告することが必須とされ、RI-01の現代的致命基準に抵触する。
- **B8（PhF/ベンゼン共溶出下での収率報告）**: 現代の分析標準では、定量に使用した分析法で主要共存物質が干渉する場合、代替確認法（GC-MS、別カラム、¹H NMR）を提示せずに収率を報告することは許容されない；RI-01の現代的致命残存として記録する。

---

### §5 最短補強ルート

**現在VQ：VQ-1 → 第一目的関数：VQ-2**

**VQ-2 への最短ルート：**

1. EP-08a Replication/uncertainty pack — [Ni(dppp)Cl₂]触媒n-BuMgBr + PhCl反応の6反復GLPC分析でRSD%を算出し、U3（収率>転化率）が測定誤差内か否かを確定；同時にn-ブチルベンゼン応答係数のメシチレン基準とn-アルカン基準のクロスバリデーションを実施。RI-08およびRI-01（精度成分）を前進。

2. EP-01a Reporting-coherence pack — Table 7全エントリーをハロゲン化物基準GC収率（主値）に統一再集計し、孤立収率を別列表記；脚注t（Grignard試薬基準）エントリーの換算値を付記。完全なGC操作条件表（カラム温度プログラム・キャリアガス流量・FID条件・注入量）を付録に追加。RI-01（報告フレーム成分、B1/B3/B4/B5/B9）を前進。

3. EP-07a Boundary-test pack — n-BuMgBr + 1,2-ジクロロエチレン（cis/trans各1例）を標準条件（[Ni(dppp)Cl₂]・Et₂O・RT・3h/24h）でGLPC分析し、主生成物（ホモカップリング・モノカップリング・ビスカップリング）を同定・定量化してTable 7に追加。RI-07（B2）を解消。

**VQ-3 への最短ルート（VQ-2達成を前提）：**

4. EP-06a Analogy-validation pack — PhCl + n-BuMgBrを「クロスオーバー実験」設定（PhCl + MesMgBrおよびPhBr + n-BuMgBrの同時存在下[Ni(dppp)Cl₂]）で行い、Scheme 1のmixed L₂Ni(R)(R')経由還元的脱離（クロス積優先）vs. Felkin-Corriu（ホモ積優先）を識別。RI-06（SRG-1主要）を前進。

5. EP-04a Discrimination/replication pack — パラ置換アリールクロリド（5種）のHammett ρ値測定により律速段階を特定（ρ>0：酸化的付加律速、ρ<0または≈0：別段階律速）；PhI/PhCl競合動態で異常順序を定量的確認。RI-04（A3/SRG-5）を前進。

6. EP-03a Direct-observation/state-assignment pack — 触媒的条件下[Ni(dppp)Cl₂] + n-BuMgBrのin situ ³¹P NMRモニタリングで触媒休止状態を同定；²H標識（β-d₁ sec-アルキルMgBr）を用いて[Ni(dmpe)Cl₂]触媒での異性化のβ-水素脱離/再挿入経路を確認（U2解消）。RI-03（A6/A8/U2/SRG-5）を前進。

**VQ-4 への最短ルート（VQ-3達成を前提）：**

7. EP-09a Internal benchmark pack — n-BuMgBr + PhClを[Ni(dppp)Cl₂]・[Pd(PPh₃)₂Cl₂]・[Fe(acac)₃]・CuI各1 mol%で同一条件・同一GLPC分析（6反復）で比較——収率・選択性・基質汎用性を一覧化。RI-09（SRG-6: C1/C2）を解消。

（RI-08はEP-08aによりVQ-2ルートで対処済み）

**認定ゲート順注記：** 実験投入順は情報利得優先（EP-08a→EP-01a→EP-07a）だが、最終的なVQ認定は継承原則に従いVQ-1→VQ-2→VQ-3→VQ-4の順に確定する。EP-06aまでが完了してもVQ-3の認定はRI-01/RI-07（VQ-2要件）の解消後にのみ有効となる。

---

### §6 制度設計への寄与

**既存RIコードの代表事例として：**

- **RI-07（Unsupported boundary）の新型事例**: 本論文のSRG-2は、RI-07の典型（「〜のみ有効」という過剰な肯定的境界主張）ではなく、「〜が最も深刻な限界」という否定的境界主張をデータなしに行うケースを提供する。著者が自ら名指した主要限界にスコープ表の1エントリーも割り当てていないという構造は、RI-07の境界外挿規則が「限界の主張」にも適用されることを示す代表事例として追加すべきである。

- **RI-08（Unquantified reliability）の内部矛盾型事例**: U3（収率81%>転化率80%）は、RI-08が単に「反復測定の欠如」だけでなく、「同一サンプルから計算される2つの量（収率と転化率）が数学的矛盾を示す」という症状を持ちうることを示す。この「内部矛盾型RI-08」は既存の典型例には含まれておらず、Codebook補足事例として記録する価値がある。

- **RI-06（Imported model）の規模的事例**: Scheme 1は7ステップの完全な触媒サイクルを別系の化学量論的反応2報（refs 30-31, 32）のみから構成する大規模モデル輸入であり、個別素反応の類推ではなく「サイクル全体の類推」としてRI-06が適用される。これはRI-06の「サイクルレベル」適用例として記録する。

**新PRI候補：なし**

SRG-1（触媒サイクル丸ごと輸入）はRI-06の既存定義「他系モデルを対象系での同型性実証なしに輸入」に完全に収まる。PRI新設は不要。

**VQ Era-Norm境界条件：**

SRG-3（GLPC精度）の複数B項目（B4/B5/B9）はcommunication-era toleratedかつmodern-era deficientという両面性を持ち、VQ-2判定におけるRI-01を「期待水準依存型」として扱った。この種の項目は§4のEra-Norm Annotationで両面記録することで、過去文献の再評価と現代基準の設計を同時に行うCodebook運用例として確認された。

**EP-07a（Boundary-test pack）の範囲拡張：**

標準的EP-07aは「〜のみ有効」という過剰スコープ主張への反証実験を想定するが、本ケースでは「主要な限界」という著者自身の否定的記述に対してBoundary-test packを適用した。EP-07aの定義を「著者が言及した限界・失敗基質に対する代表的データの提供」まで拡張することをEP辞書改訂候補として提案する。

**本ケースは既存の制度設計を以下の点で追加確認した：** RI-09（External superiority）がDropped Quantitative Benchmark（C1/C2）と直結するパターンは先行ケースと同型であり、SRG-6の分析は既存のRI-09→EP-09a投入の基本ルートを再現した。
