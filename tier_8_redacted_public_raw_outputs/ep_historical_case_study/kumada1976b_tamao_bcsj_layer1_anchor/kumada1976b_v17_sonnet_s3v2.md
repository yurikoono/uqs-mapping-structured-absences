prompt_version: stage3-v2-20260416
model_info: claude-sonnet-4-6

# 科学的知見の再認定判定票

## Tamao et al. 1976（Bulletin of the Chemical Society of Japan, full paper）

---

### §1 Claim Architecture

**コア主張（要約）**

Novelty柱：ジハロジホスフィンニッケル(II)錯体——[Ni(dppp)Cl₂]（アルキル・アリールGrignard用）、[Ni(dmpe)Cl₂]（アルケニル・アリルGrignard用）、[Ni(PPh₃)₂Cl₂]（立体障害アリール基質用）——が「極めて高い触媒活性」を示してGrignard試薬とアリール・アルケニルハロゲン化物の選択的クロスカップリングを触媒すること。β-水素を持つGrignard試薬でも選択的に進行し、有機クロリドが最適基質となるという一般原則を含む。

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

* **Primary RI**: RI-06 Imported model（サイクルレベル輸入: Scheme 1全体を別系の化学量論的反応refs 30–32から構成。v0.2a RI-06スコープ注記「サイクルレベル輸入」に該当する典型事例）
* **Secondary RI**: RI-03 Unobserved explanatory; RI-04 Unreplicated discriminator
* **ER**: Scheme 1の各素反応ステップを本触媒系（Ni-ホスフィン触媒条件）に適用可能であることを示すため、(a) 触媒条件下または触媒モデル反応でのNi(0)→Ni(II)酸化的付加中間体またはジオルガノニッケル(II)中間体の直接観測、もしくは (b) Felkin-Corrieメカニズムを排除する交差実験または同位体標識実験が必要である。
* **EP**: EP-06a Analogy-validation pack; EP-03a Direct-observation/state-assignment pack; EP-04a Discrimination/replication pack
* **Case-specific実装**: (1) R-X（例：PhCl）とR'-X'（例：MesCl）の混合に触媒量[Ni(dppp)Cl₂]を加えてクロス生成物とホモ生成物の比を測定するクロスオーバー実験（Scheme 1の混合型L₂Ni(R)(R')経由還元的脱離 vs. Felkin-Corriu経路識別）；(2) [Ni(dppp)Cl₂]触媒存在下n-BuMgBr + PhClのin situ ³¹P NMRモニタリングによる触媒休止状態の同定；(3) U2解消：²H標識β-d₁ sec-アルキルMgBrを用いた[Ni(dmpe)Cl₂]触媒での異性化機構確認
* **注記**: A2（critical, 1/3収束：low_convergence_high_gap—V2のみcritical）、A6（high, V2）、A8（high, V2）、C3（stoichiometric analogy basis—RI-06サイクルレベル輸入の典型）、C4（ref 46単一引用）、U1（MgXX'未評価）、U2（β-消去自己矛盾）; PRI-11非適用：本論文は速度次数データ自体が皆無であり、「速度式を導出せずに観測速度次数と一致させる」という構造（PRI-11定義）に至っていない

---

**SRG-2 [主要限界の定量的実体の欠如]**

* **Primary RI**: RI-07 Unsupported boundary（否定的境界主張への拡張適用: v0.2a RI-07拡張適用「否定的境界主張」に該当。「最も深刻な限界」という否定的境界主張をデータなしに行うケース）
* **Secondary RI**: RI-05 Qualitative overread
* **ER**: アルキルGrignard試薬＋ジハロエチレン（例：n-BuMgBr + cis-ClHC=CHCl）の反応を少なくとも1例、[Ni(dppp)Cl₂]触媒・標準条件下でGLPC分析し、クロスカップリング生成物・ホモカップリング生成物・未反応原料を定量化するとともに主要生成物をスペクトル同定する必要がある。
* **EP**: EP-07a Boundary-test pack
* **Case-specific実装**: n-BuMgBr（2 mmol）+ 1,2-ジクロロエチレン（cis体/trans体別々に、1 mmol）、[Ni(dppp)Cl₂]（1 mol%）、Et₂O、RT、3 h・6 h・24 hの時間経過サンプルをGLPC分析（n-アルカン内標準）——n-オクタン（ホモカップリング）、クロロブチルエチレン（モノカップリング）、1,2-ジブチルエチレン（ビスカップリング）の各収率を報告
* **注記**: B2（3/3収束・最強：high_convergence_low_gap; V1=high×2, V2=high, V3=medium）、A1（「条件は最適化されていない」免責との連動）

---

**SRG-3 [GLPC定量基盤の測定信頼性の欠如]**

* **Primary RI**: RI-08 Unquantified reliability（内部矛盾型サブタイプ: v0.2a RI-08サブタイプ「内部矛盾型」に該当。U3のPhCl 2h: 収率81%>転化率80%は「同一サンプルから計算される2つの量が数学的矛盾を示す」ケース）
* **Secondary RI**: RI-01 Reporting integrity
* **ER**: ~60の収率値が横比較に耐えるためには、(a) 完全なGC操作条件（カラム温度・キャリアガス流量・検出器仕様・注入量）、(b) 各基質クラスの代表化合物の応答係数、(c) 少なくとも1エントリーの反復測定による測定不確かさの定量化、を報告する必要がある。
* **EP**: EP-08a Replication/uncertainty pack; EP-01a Reporting-coherence pack
* **Case-specific実装**: (1) 代表的生成物（例：n-ブチルベンゼン）の1点検量→3点検量曲線への置換とRSD報告；(2) n-ブチルベンゼン/メシチレン系とn-ブチルベンゼン/n-アルカン系の応答係数クロスバリデーション（B9解消）；(3) U3の問題（Table 3 PhCl 2h: 収率81%>転化率80%）について、同一サンプルの反復注入6回によるSD評価——U3の数値が測定誤差範囲内かを確認
* **注記**: B4（high, V3）、B5（high, V3）、B9（medium, V3）、U3（medium, V1+V3; 収率>転化率の内部矛盾——RI-08内部矛盾型サブタイプ）、B7（medium, V3）、B8（high_convergence_low_gap: V1=high, V3=critical; 2/3収束, gap=low）

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
* **Case-specific実装**: (1) [Ni(dppp)Cl₂]存在下、PhI（0.5 equiv）とPhCl（0.5 equiv）のn-BuMgBrとの競合反応——生成物比から相対速度定数比を算出；(2) パラ置換アリールクロリド（p-MeO, p-Me, p-H, p-Cl, p-NO₂）の[Ni(dppp)Cl₂]触媒反応でHammettプロット構築——ρ値の符号から酸化的付加または還元的脱離が律速段階かを判定；(3) ²H標識（α-d₁またはβ-d₁）を用いた[Ni(dmpe)Cl₂]触媒での二級アルキルGrignard反応における異性化機構のアイソトープ追跡
* **注記**: A3（2/3収束, gap=low: V1=medium, V2=high; high_convergence_low_gap）、A5（high, V2）、A6（high, V2—SRG-1とも共有）、A8（high, V2—SRG-1とも共有）、U2（high, V2—SRG-1とも共有）；SRG-5はSRG-1とA6/A8/U2を通じて重複するが、選択性特徴（halide order, β-elimination scope）の定量的検証という独立した問いを持つ

---

**SRG-6 [競合触媒系との数値的ベンチマーク欠如]**

* **Primary RI**: RI-09 External superiority
* **Secondary RI**: （なし）
* **ER**: Fe/Ag/Cu系（refs 15–17）およびPd-ホスフィン系（ref 22）に対する優位性の主張を検証するため、同一基質ペア（例：n-BuMgBr + PhCl）・同一条件下での直接比較実験が最低1例必要である。
* **EP**: EP-09a Internal benchmark pack
* **Case-specific実装**: n-BuMgBr（2 mmol）+ PhCl（2 mmol）、Et₂O、RT、3 h条件下で以下の触媒を同時並行試験：(a) [Ni(dppp)Cl₂] 1 mol%、(b) [Pd(PPh₃)₂Cl₂] 1 mol%（ref 22系）、(c) [Fe(acac)₃] 1 mol%（ref 15/16系）、(d) CuI 1 mol%；各反応をGLPC分析（同一条件・同一内標準）してn-ブチルベンゼン収率・ホモカップリング収率を一覧化
* **注記**: C1（Dropped Quantitative Benchmark; refs 15-17 Fe/Ag/Cu「極めて効果的」）、C2（Dropped Quantitative Benchmark; ref 22 Pd「類似の」）；TEMPERATURE_SUMMARY記録なし（C項目、単一エージェント観察）

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
- RI-01（残存、非致命的から致命的にまたがる）：SRG-3（GLPC操作条件・検量線不在、B4/B5/B9）とSRG-4（収率基準不統一、B1/B3）が未解消。U3（収率>転化率の内部矛盾）はRI-08の内部矛盾型サブタイプとして、少なくとも1エントリーで測定の一貫性が成立していない可能性を示す（RI-01と協同して致命的に作用）。
- RI-07（残存、境界主張に対し致命的）：SRG-2（B2）が未解消。アルキルGrignard＋ジハロエチレン「最も深刻な限界」の主張が、この基質クラスのデータ皆無のまま行われている（v0.2a RI-07否定的境界主張への拡張適用が致命性を確定する）。
→ RI-01およびRI-07が未解消のためVQ-2未達。

**VQ-3 Mechanism — 未達**

VQ-2未達のため継承条件も不成立。SRG-1（RI-06: サイクルレベル輸入）・SRG-5（RI-05, RI-03）がいずれも未解消。Scheme 1は別系の化学量論的反応から全体を輸入（RI-06）しており、Felkin-Corriu経路との識別実験がない（RI-04）。RI-06とRI-03の不分離共起（後述 §6）により、EP-06a単独ではRI-06を完全解消できず、EP-03aとの組み合わせが必要。

ただし**Layer (i)「高い触媒活性」単独では**：SRG-3/4（測定精度・報告フレーム）の問題が解消されれば、スコープパターンとしての主張はVQ-2相当の判定が可能。しかしScheme 1なしでは機構的含意（選択性の理由）はVQ-3未達のまま。

**VQ-4 Benchmark — 未達**

VQ-3未達のため不成立。SRG-6（RI-09）も未解消。

---

### §4 Era-Norm Annotation

**communication-era tolerated（1976年 BCSJ full paper）：**

- **B4（GLPC機器条件の不完全記述）**: 1976年のBCSJは定量GLPCの機器条件（カラム温度・キャリアガス流量・検出器仕様）の完全記述を義務付けておらず、「装置名＋カラム充填剤」は当時の標準的記述水準に収まる。
- **B5（検量線・応答係数の不記載）**: 内標準法による定量GLPCにおいて検量線の省略は1970年代の分析化学分野では通例であり、「authentic sampleとの比較」は当時の認証として有効とみなされた。
- **B9（内標準物質の選択根拠の不記載）**: 異なる実験間での内標準物質の変更（メシチレン vs. 正アルカン）は、当時の合成報告書では慣習的にフットノートで処理された。
- **B1（孤立収率とGC収率の混在表記）**: Table 7の括弧表記によるGC収率明示は、孤立収率との区別を示す当時の標準的BCSJ表記慣行である。
- **C3（別系からの機構類推）**: 1976年時点では遷移金属触媒サイクルを別系の化学量論的反応から類推することが機構的提案の標準的アプローチであり、触媒系内での独立検証は必須とされなかった。RI-06「サイクルレベル輸入」も当時は許容された慣行であった。
- **B7（一部エントリーでのベンゼン未定量）**: 特定の解析困難な副生成物を脚注で除外することは当時のBCSJ full paperでは許容された実務的記述である。

**modern-era deficient（現代基準）：**

- **B4/B5（GLPC条件・検量線の不記載）**: 現代の分析的収率報告では、完全なGC操作条件と代表的応答係数は再現性確保の必須要件であり、VQ-2達成のためにRI-01/RI-08の解消として要求される。両タグ：当時は許容されたが現代では不足。
- **U3（収率>転化率の内部矛盾）**: Table 3のPhCl 2h entry（収率81%>転化率80%）は現代誌では「measurement inconsistency」として訂正要求の対象となり、論文データの全体的信頼性に疑義を投じる；RI-08内部矛盾型の現代的致命基準として記録する。
- **B2（主要限界の代表データ皆無）**: 現代のスコープ論文では、著者が「最も深刻な限界」と明示した基質クラスの代表例を少なくとも1つ報告することが査読上の標準的要求であり、RI-07否定的境界主張の現代的致命基準に抵触する。
- **SRG-4（収率基準不統一）**: 現代のクロスカップリングスコープ論文では、全エントリーを統一された収率定義（通常は限定試薬基準の孤立収率またはGC収率）で報告することが必須とされ、RI-01の現代的致命基準に抵触する。
- **B8（PhF/ベンゼン共溶出下での収率報告）**: 現代の分析標準では、定量に使用した分析法で主要共存物質が干渉する場合、代替確認法（GC-MS、別カラム、¹H NMR）を提示せずに収率を報告することは許容されない；RI-01の現代的致命残存として記録する。両タグ：当時は許容されたが現代では不足。

---

### §5 最短補強ルート

**現在VQ：VQ-1 → 第一目的関数：VQ-2**

**VQ-2 への最短ルート：**

1. EP-08a Replication/uncertainty pack — [Ni(dppp)Cl₂]触媒n-BuMgBr + PhCl反応の6反復GLPC分析でRSD%を算出し、U3（収率>転化率）が測定誤差内か否かを確定；同時にn-ブチルベンゼン応答係数のメシチレン基準とn-アルカン基準のクロスバリデーションを実施。RI-08（内部矛盾型含む）およびRI-01（精度成分）を前進。

2. EP-01a Reporting-coherence pack — Table 7全エントリーをハロゲン化物基準GC収率（主値）に統一再集計し、孤立収率を別列表記；脚注t（Grignard試薬基準）エントリーの換算値を付記。完全なGC操作条件表（カラム温度プログラム・キャリアガス流量・FID条件・注入量）を付録に追加。RI-01（報告フレーム成分、B1/B3/B4/B5/B9）を前進。

3. EP-07a Boundary-test pack — n-BuMgBr + 1,2-ジクロロエチレン（cis/trans各1例）を標準条件（[Ni(dppp)Cl₂]・Et₂O・RT・3h/24h）でGLPC分析し、主生成物（ホモカップリング・モノカップリング・ビスカップリング）を同定・定量化してTable 7に追加。RI-07（SRG-2, B2）を解消。

**VQ-3 への最短ルート（VQ-2達成を前提）：**

4. EP-06a Analogy-validation pack — PhCl + n-BuMgBrを「クロスオーバー実験」設定（PhCl + MesMgBrおよびPhBr + n-BuMgBrの同時存在下[Ni(dppp)Cl₂]）で行い、Scheme 1のmixed L₂Ni(R)(R')経由還元的脱離（クロス積優先）vs. Felkin-Corriu（ホモ積優先）を識別。RI-06（SRG-1主要、サイクルレベル輸入の検証ファーストステップ）を前進。ただしRI-03との不分離共起により、EP-03aとの組み合わせが必要（§6参照）。

5. EP-04a Discrimination/replication pack — パラ置換アリールクロリド（5種）のHammett ρ値測定により律速段階を特定（ρ>0：酸化的付加律速、ρ<0または≈0：別段階律速）；PhI/PhCl競合動態で異常順序を定量的確認。RI-04（A3/SRG-5）を前進。

6. EP-03a Direct-observation/state-assignment pack — 触媒的条件下[Ni(dppp)Cl₂] + n-BuMgBrのin situ ³¹P NMRモニタリングで触媒休止状態を同定；²H標識（β-d₁ sec-アルキルMgBr）を用いて[Ni(dmpe)Cl₂]触媒での異性化のβ-水素脱離/再挿入経路を確認（U2解消）。RI-03（A6/A8/U2/SRG-5）を前進。

**VQ-4 への最短ルート（VQ-3達成を前提）：**

7. EP-09a Internal benchmark pack — n-BuMgBr + PhClを[Ni(dppp)Cl₂]・[Pd(PPh₃)₂Cl₂]・[Fe(acac)₃]・CuI各1 mol%で同一条件・同一GLPC分析（6反復）で比較——収率・選択性・基質汎用性を一覧化。RI-09（SRG-6: C1/C2）を解消。

（RI-08はEP-08aによりVQ-2ルートで対処済み）

**認定ゲート順注記：** 実験投入順は情報利得優先（EP-08a→EP-01a→EP-07a）だが、最終的なVQ認定は継承原則に従いVQ-1→VQ-2→VQ-3→VQ-4の順に確定する。EP-06aまでが完了してもVQ-3の認定はRI-01/RI-07（VQ-2要件）の解消後にのみ有効となる。EP-06aとEP-03aの共依存（RI-06 + RI-03の不分離共起）により、SRG-1の完全解消には両EPが必要であり、投入順は並列が望ましい。

---

### §6 制度設計への寄与

**既存RIコードのv0.2a新規規則に対する代表事例確認：**

- **RI-06「サイクルレベル輸入」（v0.2a追加）の典型事例**: Scheme 1は7ステップの完全な触媒サイクルを別系の化学量論的反応2報（refs 30–31: L₂NiR₂ + R'X' → reductive elimination; ref 32: L₂NiXR + RMgX → transmetalation）から構成する大規模モデル輸入であり、v0.2aが明示した「サイクルレベル輸入」の定義に完全に合致する。個別素反応の類推ではなくサイクル全体としての輸入という特徴が鮮明であり、この規則の適用例として記録する。

- **RI-07「否定的境界主張」（v0.2a追加）の典型事例**: SRG-2は「最も深刻な限界」という否定的境界主張をデータなしに行うケースであり、v0.2aが追加した「『〜が最も深刻な限界』という否定的境界主張をデータなしに行う場合にもRI-07を適用する」という拡張規則の典型事例として確認された。EP-07aの適用範囲を「著者が言及した限界・失敗基質に対する代表的データの提供」まで拡張することをEP辞書改訂候補として改めて提案する（v1報告からの継続）。

- **RI-08「内部矛盾型」（v0.2a追加）の典型事例**: U3（Table 3 PhCl 2h: 収率81%>転化率80%）は、v0.2aが「同一サンプルから計算される2つの量が数学的矛盾を示す場合、反復測定の欠如だけでなく測定一貫性の不在としてRI-08を適用する」と定めたサブタイプの典型事例として確認された。

**PRI評価：**

*PRI-10（Kinetic overclaim）の第二確認候補:*
本論文はabstractで「extremely high catalytic activity」を主張しているが、この主張の根拠は単一時点（20 h reflux）のGLPC収率値のみであり、ターンオーバー数（TON）・ターンオーバー頻度（TOF）・反応速度定数・反応次数は一切報告されていない。これはPRI-10（「動力学データなしに絶対的速度向上を主張」）の定義に合致する。Monnereau 2009での第一確認に続く第二確認候補として記録する。ただし、PRI-10の適用はRI-06（サイクルレベル輸入）と同一SRG（SRG-1）内で共起しており、「どのステップが速い」という主張の不在がScheme 1の輸入（RI-06）と相互支持する構造を成している。この共起は先行ケースでは確認されていない新パターンであり、PRI-10昇格の補足記録として追記する。

*PRI-11（Mechanism-kinetics decoupling）の非適用確認:*
PRI-11の定義「提案触媒サイクルから速度式を代数的に導出せずに、観測速度次数との一致のみで機構を支持」は本論文には適用されない。本論文は速度次数データ自体を一切持たず、「速度次数との一致」という操作が存在しないためである。PRI-11の前提条件は「速度論データが存在すること」であり、その欠如はRI-03/RI-08で記述される。本非適用の明示的記録はPRI-11の適用境界条件（「速度次数データが存在するケースのみ」）を確定する制度的意義を持つ。

**新検出パターン：**

*標識不整合（Labeling mismatch）:*
機構セクション（V節）では「Although the mechanism has not yet been fully clarified」「[REDACTED: verbatim source text; see the source paper via its DOI]」「[REDACTED: verbatim source text; see the source paper via its DOI]」という仮説標識が使用されている。しかし同節内の個別記述（「[REDACTED: verbatim source text; see the source paper via its DOI]」「[REDACTED: verbatim source text; see the source paper via its DOI]」）では、仮説標識の直後に事実的叙述語（"compete with," "responsible for"）が続くパターンを示す。仮説標識は節冒頭・節末尾に集約されており、個別の構造帰属は事実的言語で記述される傾向がある。これはRI-06（Imported model）と連動したlabeling mismatchパターンとして記録する。

*RI共起パターン（RI-06 + RI-03の不分離共起）:*
SRG-1においてRI-06（サイクルレベル輸入）とRI-03（未観測説明変数：Ni(0)/Ni(II)中間体）が共起しており、一方の解消のみでは不十分である。EP-06a（クロスオーバー実験）によりRI-06を部分的に前進させても、中間体の直接観測（EP-03a、RI-03解消）なしにはScheme 1の素反応ステップへの帰属が確定できない。逆にNi中間体の分光学的観測（EP-03a）のみでは、Felkin-Corriu経路との識別（RI-04、RI-06解消の前提）が成立しない。この「RI-06 + RI-03の不分離共起」は機構モデル輸入を含むケースで構造的に生じるパターンであり、EP投入順の最小化には両EPの並列実施が必要という設計上の含意を持つ。§5認定ゲート順注記に反映済み。

*通信→Full Paper遷移の自動解消の限界:*
本論文は1972年JACS通信（ref 21）のFull Paper展開である。通信→Full Paper遷移で自動解消が期待されたRI-01（報告フレーム）とRI-07（スコープ境界）は、Table 7の大幅拡張（~60エントリー）にもかかわらず部分的にのみ解消された——収率基準不統一（SRG-4）と主要限界の代表例欠如（SRG-2）が依然として残存する。自動解消を妨げた構造的要因は、「The reaction conditions are not necessarily optimum」（A1）という免責注記が、未完了の限界実証を不要と見なす著者の判断を支えた点に見出せる。この「免責注記による自動解消阻害」パターンは§4のEra-Norm Annotationで記録したB2（modern-era deficient）と直接対応する。

**EP辞書・Codebook更新候補（v0.2a→v0.2b）：**
- EP-07a定義の拡張：「著者が言及した限界・失敗基質に対する代表的データの提供」を適用範囲に明示追加（v1報告から継続、本報で再確認）
- PRI-10昇格判断材料：Kumada 1976をMonnereau 2009に続く第二確認として記録。2報の独立確認が揃ったが、両ケースでRI-06との共起が観察されており、PRI-10定義に「サイクルレベル輸入を伴う場合の特殊パターン」として注記追加を検討すること
