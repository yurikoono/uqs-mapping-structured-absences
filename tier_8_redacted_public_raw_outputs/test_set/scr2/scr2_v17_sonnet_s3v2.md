```
prompt_version: stage3-v2-20260416
model_info: claude-sonnet-4-6

# 科学的知見の再認定判定票

## Templ, Hwang, Schwemin, Baltaci, Borchardt 2025（RSC Mechanochemistry, full_paper）

---

### §1 Claim Architecture

**コア主張:**
本論文のノベルティ柱は「直接メカノ触媒によるMizoroki–Heck反応の初の実行可能プロトコル」（Pdボールを唯一の触媒として機械的エネルギーと熱エネルギーの組み合わせで駆動する）であり、既報のSuzuki/Sonogashira直接メカノ触媒に続いてHeckを完成させ、パラジウム触媒C–C結合形成の網羅性を確立する位置づけを取る。ユーティリティ柱は三層：（a）C(sp²)–I選択性（溶液系Heckがブロマイドにも反応するのに対して高い選択性が生じることを合成的長所として提示）、（b）one-pot Wittig/Heck連続反応によるスチルベン誘導体への直接アクセス、（c）無溶媒・不活性雰囲気不要・触媒回収容易という操作的実用性（リサイクル主張を含む）。

**Layered structure:**
主張は構造的に独立した3層を持つ。（1）直接メカノ触媒Heckプロトコルの存在証明：14種アリールヨージド・8種ビニル基質スコープで支持され、単一の実験的反証で全体が崩れることはない。（2）C(sp²)–I選択性：ArBr/ArClの不活性例とともに独立に支持され、（1）の反証が（2）を直接崩さない。（3）one-pot Wittig/Heck：2基質のみを以て実証されており、（1）または（2）が崩れても（3）は実験事実として残る。ただし、3層すべてに共通する前提——「反応がPdボール表面で起きている」——が崩れれば3層の主張はいずれも根拠の再評価を迫られる。この共通前提の証拠強度の欠如がSRG-1の核心である。

---

### §2 SRG / CLA → RI / ER / EP Crosswalk

---

**SRG-1 [surface catalysis vs. leaching ambiguity]**

* **Primary RI**: RI-03 Unobserved explanatory — 触媒的に活性な種（Pdボール表面サイト vs. 溶液中溶出Pd種/ナノ粒子）が直接観測も速度論的拘束もされていない。「not mainly mediated by abraded palladium particles」という部分否定修飾語は定量的閾値を含意するが、その閾値は未設定。
  * **RI-03 subtype注記（Available-but-unutilized characterization）**: 浸出実験のデータはESIに存在する（「see ESI† for details」という明示的参照）。これは「未測定」ではなく「測定済みだが定量的含意が主テキストで抽出されていない」パターンである。ICP-MS等の数値は取得済みの可能性が高いが、「not mainly」という部分否定が活性化閾値との比較なしに提示されている。この Available-but-unutilized 構造はRI-03の典型事例として登録すべき形式。
* **Secondary RI**: RI-04 Unreplicated discriminator — ESI参照の浸出実験が単一点評価であり、「触媒的に有意な均一系反応を起こすPd濃度の閾値」が設定されていない。フェノール毒化も0.5当量単一点（B-5）。
* **ER**: 濾液中Pd濃度の定量値（検出下限付きICP-MS/ICP-OES）と、その濃度が速度論的に有意な均一系触媒を起こせないことの計算、またはホットフィルトレーション試験（ボール除去後の変換率進行確認）かHg毒化試験（300当量以上）のいずれかを本文に提供すること。
* **EP**: EP-03a Direct-observation / state-assignment pack; EP-04a Discrimination / replication pack
* **Case-specific実装**: （i）反応30分時点でPdボールを除去し、残余30分での変換率進行をNMRで確認（ホットフィルトレーション）；（ii）Hg(0) 300当量添加対照実験（Pdナノ粒子選択的毒化）；（iii）ICP-MSによる反応濾液Pd定量（検出下限 < 1 ppb）と公知の均一系Pd触媒活性閾値との数値比較；（iv）反応前後のPdボール表面XPS（Pd 3d領域：Pd(0) 335.1 eV vs. PdO 336.5 eV）。
* **注記**: B-1 [high_convergence_low_gap, 3/3, gap=none]。U-1（self-contradictory absence: 閾値未設定）、U-2（同: ホットフィルトレーション/Hg試験不在）。B-9, B-15, B-16, B-18も同根。D-4-1およびD-4-8の核心SRG。RI-03 + RI-04共起構造（詳細は§6参照）。

---

**SRG-2 [chemoselectivity mechanism — C(sp²)–I vs C(sp²)–Br]**

* **Primary RI**: RI-03 Unobserved explanatory — C–I/C–Br選択性の起源となる素反応ステップが直接観測されていない。著者が提示する「Pd(II)–Br種がミグラトリー挿入を阻害する」という仮説は、Pd表面系ではなく溶液相Pd化学の反応サイクルから転用された機構的帰属である。
* **Secondary RI**: RI-06 Imported model（サイクルレベル輸入）— 酸化的付加→配位・挿入→β-H脱離→還元的脱離という標準的Heck触媒サイクル全体が溶液相系から表面Pd系に移植されており、各素反応が不均一表面条件下で同型に進行するという実証がない。これは個別素反応の類推ではなく触媒サイクル全体の大規模輸入であり、v0.2aの「サイクルレベル輸入」適用ケースに相当する。
* **ER**: ArI/ArBr等量混合の競合基質実験（Pd表面上での選択的変換を直接実証）；C–X切断段階と後続段階（挿入/脱離）を区別するためのArBr/ArI単独反応の時系列変換率比較；Pd(II)–Br中間体相当のモデル錯体でのオレフィン挿入速度比較（溶液相モデルの表面系への転用を検証）。
* **EP**: EP-03a Direct-observation / state-assignment pack; EP-06a Analogy-validation pack
* **Case-specific実装**: 等量PhI/PhBr + スチレン標準条件での競合実験（NMR収率比）；PhBr単独の0–90分時系列実験（反応が遅いのか全く進まないのかを区別）；K₂CO₃→KOtBu置換でブロマイドの塩基依存性を確認；可能であればin-situ Ramanによるボール表面吸着基質の観察。
* **注記**: A-1 [high_convergence_low_gap, V1=high, V2=critical, 2/3, gap=low]。ピボット: A-1 ↔ B-16。機構的猶予（A-1）が表面触媒未証明（SRG-1）の重要性を後景化する構造（priority_structureで記録済み）。RI-05残存（定性的順位から機構的含意を導出）のため、VQ-3到達時もVQ-3 (Qualified)と判定される可能性がある。PRI-11候補については§6参照。

---

**SRG-3 [recyclability — claim without data]**

* **Primary RI**: RI-07 Unsupported boundary — 「活性を失わずに再利用可能」（"without loss of activity"）という境界主張がこのHeck反応について実験的根拠を持たない。RI-07 v0.2a拡張適用：「〜のみ可能」という肯定的境界だけでなく「〜が最も深刻な限界」という否定的境界、さらに「〜において活性を損なわない」という肯定的性能境界主張にもRI-07を適用し、データなしの境界主張として分類する。
* **Secondary RI**: RI-02 Object identification — リサイクル後のPdボール表面状態（質量変化、XPS、SEM）が特定されていないため、何を再利用しているかの同定が不完全。
* **ER**: このHeck反応条件（PhI/スチレン、K₂CO₃、DMF、120°C、30 Hz）で少なくとも3–5回の連続リサイクル実験を実施し、各サイクルの単離収率・Pdボール質量変化・表面状態（目視・SEM）を報告すること。
* **EP**: EP-07a Boundary-test pack; EP-02a Identity / purity substantiation pack
* **Case-specific実装**: 標準基質（PhI + スチレン）で5サイクル連続Heck反応；各サイクル後ボール取り出し・秤量・再仕込み（洗浄プロトコルを明記）；5サイクル後ボール表面SEM撮影；ICP-MSによる各サイクル濾液Pd定量（リサイクル間での浸出量推移確認）。
* **注記**: B-8 [high_convergence_low_gap, V1=high, V2=high, 2/3, gap=none]。U-3（Pd(II)→Pd(0)再還元機構の不在）、U-4（self-contradictory absence: リサイクルデータが主テキスト・ESI双方に不在）。D-4-3, D-4-7の根拠SRG。

---

**SRG-4 [quantitative data quality and replication]**

* **Primary RI**: RI-01 Reporting integrity — NMR収率（最適化テーブルFig.2、1時間）と単離収率（スコープテーブルFig.3、2時間）の混在により横比較が不能。ブリッジ実験（同一基質3aの1h単離収率）なし。
  * **RI-08 内部矛盾型subtype**: B-7/B-23が示す「82% NMR (1h) vs. 75% isolated (2h)」の乖離は、同一基質（3a）から関係づけ可能な2量（NMR収率と単離収率）が時間条件の変更と収率基準の変更を同時に行うことで数学的整合性を失っているケースである。単純なRI-01（測定基準変更）にとどまらず、RI-08の「内部矛盾型」サブタイプ（同一サンプルから計算される2量の不整合）として記録する。
* **Secondary RI**: RI-08 Unquantified reliability — いかなるエントリーにも反復測定値・標準偏差・範囲が提供されていない。
* **ER**: 最適化テーブルの標準条件エントリを少なくとも3回繰り返しNMR収率 ± SDを報告；スコープとの比較を可能にするブリッジ実験（3aの1時間での単離収率）；スコープ全エントリに質量収支を付記すること。
* **EP**: EP-01a Reporting-coherence pack; EP-08a Replication / uncertainty pack
* **Case-specific実装**: Fig. 2 entry 5（標準条件、1h）の3回反復（NMR収率 ± σ）；Fig. 3条件（2h）でも3aのNMR収率を測定し1h/2h差を時間変数単独で切り分ける；Fig. 3全スコープエントリの反応後質量収支計算（回収出発物+生成物+副生物推定）。
* **注記**: B-7 [high_convergence_low_gap, V1=medium, V3=high, 2/3, gap=low]。B-21（複数回測定なし、1/3）、B-23（1h vs. 2h不整合、1/3）、B-25（質量収支なし、1/3）。D-4-4の根拠SRG。

---

**SRG-5 [one-pot Wittig/Heck characterization]**

* **Primary RI**: RI-04 Unreplicated discriminator — 2基質のみから構成されるスコープで、かつKOtBu（強塩基）とPh₃P=O（化学量論的副生物）という2つの変数が同時に変化しており、結果の弁別力が低い。
* **Secondary RI**: RI-07 Unsupported boundary — 「スチルベン誘導体への直接アクセス」という汎用性主張が2例のみで裏付けられており、「アルデヒドからスチルベン誘導体への適用が可能」という範囲主張が境界テストを欠く。
* **ER**: （a）Ph₃P=Oを標準Heck反応（K₂CO₃、PhI、スチレン）に添加した対照実験；（b）KOtBu単独でのHeck対照実験；（c）Wittig段階の中間変換率の中間確認（30分後停止）；（d）スコープを最低5基質に拡大。
* **EP**: EP-04a Discrimination / replication pack; EP-07a Boundary-test pack
* **Case-specific実装**: 1.4当量Ph₃P=O添加標準Heck（K₂CO₃）収率；K₂CO₃→KOtBu置換Heck単独収率；one-pot反応30分後の¹H NMRでアルデヒド残存量定量；4-Cl-ベンズアルデヒド以外の電子的多様なアルデヒド3種以上を追加。
* **注記**: B-11 [high_convergence_low_gap, V1=medium, V3=medium, 2/3, gap=none]。B-10（Ph₃P=O対照なし、1/3）、B-20（KOtBu混交、1/3）、B-26（工程別収率なし、1/3）。D-4-5の根拠SRG。

---

**SRG-6 [bulking agent / surface inhibition mechanism]**

* **Primary RI**: RI-06 Imported model（サイクルレベル輸入） — 「Cl⁻/OAc⁻によるPd表面サイト配位（配位子型阻害）」という機構は溶液相Pd化学の触媒被毒モデルをPdボール表面系に移植したものであり、表面系での同型性実証がない。「snowballing」（物理的被覆）と配位子型阻害という2つの機構が区別されていない。
* **Secondary RI**: RI-04 Unreplicated discriminator — 4-ヒドロキシビフェニルによる毒化実験が0.5当量の単一濃度（B-5）であり、12%残余変換率が不完全阻害を示すにもかかわらず用量-応答系列がない。
* **ER**: KCl/KOAc使用後のPdボール表面顕微鏡観察（snowballingの視覚的確認）；NaCl vs. KCl（カチオン/アニオン効果の分離）；フェノール毒化の用量-応答系列（0.1–1.0当量）。
* **EP**: EP-06a Analogy-validation pack; EP-04a Discrimination / replication pack
* **Case-specific実装**: KCl・KOAc・K₂SO₄使用後の各Pdボール光学顕微鏡またはSEM撮影；KCl vs. NaCl等当量対照でsnowballing vs. Cl⁻配位効果を分離；フェノール毒化用量系列（0.1, 0.25, 0.5, 1.0, 2.0当量）でIC₅₀推定とメカニズム類推の検証。
* **注記**: B-4 [high_convergence_low_gap, 2/3, gap=none]。B-5 [high_convergence_low_gap, 2/3, gap=none]。このSRGはSRG-1の傍証的機能を持つが、阻害機構としての独立性を保つ。

---

SRG外：CLA

**CLA: [E/Z ratio and stereochemical characterization]**

* **Primary RI**: RI-01 Reporting integrity — Heck反応スコープ論文の標準的記述要件であるE/Z比が全生成物にわたって欠落している（B-14）。
* **Secondary RI**: RI-08 Unquantified reliability — "(E)-isomers"という帰属が数値比なしに全基質に適用されており、特にアクリレート系（3u–3w）での選択性が未定量。
* **ER**: 全スコープ生成物のE:Z比（¹H NMRビニルプロトン積分）を報告。E:Z > 95:5の場合は数値で記載。
* **EP**: EP-01a Reporting-coherence pack; EP-08a Replication / uncertainty pack
* **Case-specific実装**: 粗生成物¹H NMRスペクトルのビニル領域（5.0–7.5 ppm）での(E)体/(Z)体積分比較；特に3u（tert-ブチルアクリレート）、3v（アクリロイルモルホリン）、3w（ヘキシルアクリレート）のアクリレート系で優先して確認。
* **注記**: B-14 [high_convergence_low_gap, V2=medium, V3=medium, 2/3, gap=none]。いずれのSRGにも属さない独立CLA。D-4-6の根拠。

---

### §3 現在のVQ判定

**現在判定: VQ-1 (Observation)**

---

**VQ-1 [Observation] → 通過（非致命的RI-02残存）**

生成物の構造同定は¹H NMRおよび単離により達成されており、主要なスコープ生成物（スチルベン誘導体、アクリレート誘導体）の構造的帰属は代替候補を排除できる粒度で記述されている。Pdボールは元素金属として明確に定義される。残存RI-02は3点：（a）Pdボール表面の酸化状態（Pd(0) vs. PdO）が反応条件下で確認されていない（B-18）；（b）E/Z比が全スコープ生成物で欠落（B-14, CLA）；（c）3u–3wの単離収率が精製なしで報告されており純度の分析的実証がない（B-24）。これらはいずれも現行の生成物同定を根底から覆すものではなく、非致命的と判定する。

**継承条件の明示**: VQ-2以降の判定はVQ-1の上記条件付き通過を前提とする。

---

**VQ-2 [Method] → 未達**

VQ-2通過にはRI-01（報告の整合性）とRI-07（境界主張の裏付け）の解消が必要（VQ-1継承）。

RI-01**未解消**（SRG-4）: NMR収率（最適化Table, 1h）と単離収率（スコープTable, 2h）の混在（B-7）、反応時間不整合（B-23）、全エントリでの複数回測定なし（B-21）により、最適化データとスコープデータの横比較が無効化されている。特に82% NMR (1h) vs. 75% isolated (2h)の乖離はRI-08の内部矛盾型サブタイプに相当し、RI-01の単純な「測定基準変更」より深刻な報告整合性の欠如を示す。

RI-07**未解消**（SRG-3, SRG-5）: 「活性を失わずに再利用可能」という境界主張がHeck反応に対して実験的根拠を持たない（B-8, U-4）。さらに、one-pot「スチルベン誘導体への直接アクセス」という汎用性主張が2例のみで境界テストを欠く（SRG-5、B-11）。

**層別VQ非対称性**: §1の独立3層を評価すると、**層（2）[C(sp²)–I選択性]単独**では、ArBr/ArClの不活性がデータで実証されており失敗例が存在するため、RI-07が実質的に解消されている。ただし同層のRI-01（収率報告の不整合）は継承する。したがって、**層（2）はRI-07を満たしRI-01のみが残存する点で、VQ-2に最も近い層**である（RI-01解消によってVQ-2を単独で通過しうる）。層（1）と層（3）はRI-07も未解消のためVQ-2未達。

---

**VQ-3 [Mechanism] → 未達（VQ-2に独立して）**

VQ-3通過にはRI-03、RI-04、RI-06の解消が必要（VQ-2継承）。

RI-03**未解消**（SRG-1, SRG-2）: 触媒的活性種（Pdボール表面 vs. 溶出Pd種）が主テキストの証拠から特定されていない。B-1のAvailable-but-unutilizedパターンはRI-03の特に明示的な形態である。SRG-2でも選択性の起源となる素反応が未観測。

RI-04**未解消**（SRG-1, SRG-6）: 浸出実験はESI参照で定量的弁別基準なし（B-1, U-1）；フェノール毒化が0.5当量単一点（B-5）。

RI-06**未解消**（SRG-2, SRG-6）: 溶液相Heck機構の触媒サイクル全体の輸入（SRG-2）と表面阻害機構の輸入（SRG-6）がいずれも対象系での同型性実証なし。

注：RI-05が中程度残存（C(sp²)–I選択性が定性的順位から機構的含意を導出; SRG-2）のため、VQ-3に到達した場合もVQ-3 **(Qualified)** となる。

---

**VQ-4 [Benchmark] → 未達（VQ-3に独立して）**

VQ-4通過にはRI-08、RI-09の解消が必要（VQ-3継承）。

RI-08**未解消**（SRG-4）: 反復測定・不確かさ記述がいかなる実験値にも存在しない（B-21）。RI-08内部矛盾型も未解消（B-7/B-23）。

RI-09**未解消**（C-1, C-2）: 先行Pdパウダー型mechanochemical Heckプロトコル（refs 7–10）との定量的性能比較が結果部に存在しない。自グループ先行Pd球Suzuki/Sonogashiraとの効率比較も欠落。

---

### §4 Era-Norm Annotation

**communication-era tolerated（2025, RSC Mechanochemistry 5ページ全論文）:**

- B-2（外部温度vs内部温度の未報告）: ミリング反応中の内部温度リアルタイム計測は2025年時点でメカノケミストリー分野で非標準であり、外部ジャケット設定温度のみを報告することが分野全体の慣行として許容されている。
- B-21（最適化テーブルの複数回測定なし）: 短報フォーマットの合成論文における最適化スクリーニングでの単一測定値掲載は、2025年時点でも一般的に許容されている慣行（スコープ部分での再現性確認が暗黙の補完とみなされる）。
- B-25（スコープの質量収支なし）: RSC Mechanochemのような短報専門誌では、ページ制約上スコープ全エントリの質量収支列挙は省略が許容されている。
- B-14（E/Z比の欠落）: 高選択的(E)体生成はHeck反応の分野知識として扱われており、数値列挙の省略は2025年時点では一部誌で許容されている（境界線上）。ただし(E)-帰属の根拠（coupling constantsやNOE）が示されていない点で許容の条件が弱い。

**modern-era deficient（2025年現代水準では不足）:**

- B-1（浸出実験の定量的閾値不在）: 直接メカノ触媒の論文で「not mainly」という部分否定修飾語を主テキストに使用しながら、ESIに委任した定量値を閾値比較に使わないことは、2025年の表面触媒帰属の最低要件（ICP-MS定量＋閾値設定またはホットフィルトレーション/Hg毒化）を満たさない。Available-but-unutilizedパターンは特に現代的批判の対象となる。
- B-8（Heck反応固有のリサイクルデータの完全不在）: Suzuki/Sonogashira先行論文からリサイクル主張を概念転用しつつ、Heck固有条件でのリサイクル実験を主テキスト・ESIともに示さないことは、2025年の査読では「unsupported positive performance boundary claim」（RI-07）として指摘される水準。
- B-16（ホットフィルトレーション/Hg毒化試験の不在）: 不均一表面触媒の帰属を主張する2025年の論文では、これら2試験の少なくとも一方は標準的要件とみなされている。
- A-1 + SRG-1の組み合わせ（活性種帰属と選択性機構の双方未特定）: 「反応を担う活性種が何か」（SRG-1）と「なぜC–I選択性が生じるか」（A-1）が同時に未特定であることは、2025年の機構論的査読では2つの独立した必須解明事項として同時にフラグが立てられる組み合わせ。

**両タグ該当（当時許容されたが現代では不足）:**
- B-9（Pdアブレーション定量化のESI委任）: RSC Mechanochem 5ページ形式では2025年にもESI委任は許容されるが、主テキストに定量的要約値（mg/run等）が一切ない点は現代基準では不足。

---

### §5 最短補強ルート

**目的関数1: VQ-2 (Method) への到達**

```
VQ-2 への最短ルート：

1. EP-01a Reporting-coherence pack —
   Fig. 2 entry 5（標準条件、1h）の3回反復でNMR収率 ± SDを確認し、
   同条件での単離収率（ブリッジ実験）を追加して1h/2hおよびNMR/単離
   の不整合（RI-08内部矛盾型を含む）を解消する。RI-01（SRG-4）を前進。

2. EP-08a Replication / uncertainty pack —
   スコープ代表エントリ（3a、3s、3v）の3回反復単離収率 ± SDと
   全スコープの質量収支を報告する。RI-08（SRG-4）を前進。
   ※EP-01aと同一実験セットとして実装可能（バンドル実行が効率的）。

3. EP-07a Boundary-test pack —
   標準基質で5サイクル連続Heck反応を実施し、
   「活性を失わずに再利用可能」という境界主張（RI-07, SRG-3）を実証する。
   並行してPh₃P=O対照実験（RI-07, SRG-5）も実施し2つのRI-07を同時に前進。
```

認定ゲート順注記: 実験投入順は情報利得順（EP-01a/EP-08aが小規模で実行可能なため先行）だが、最終認定はVQ-1 → VQ-2 → VQ-3 → VQ-4の継承ゲートで確定する。

---

**目的関数2: VQ-3 (Mechanism) への到達（VQ-2通過後）**

```
VQ-3 への最短ルート（VQ-2通過後）：

1. EP-03a Direct-observation / state-assignment pack —
   ホットフィルトレーション試験（反応中間点でのPdボール除去後の
   変換率進行確認）またはHg(0)毒化試験（300当量）のいずれかと、
   ICP-MSによる濾液Pd定量（検出下限 < 1 ppb）・触媒的有意閾値比較を実施。
   並行してXPS（Pd 3d領域）でボール表面の反応前後酸化状態を確認。
   RI-03（SRG-1）と残存RI-02を前進。
   ※ESIに存在する浸出データの定量的含意を主テキストで展開するだけでも
   RI-03（Available-but-unutilized解消）の部分前進が可能。

2. EP-06a Analogy-validation pack —
   等量ArI/ArBr競合実験とArBr単独時系列実験でC–I/C–Br選択性の
   起源を動力学的に拘束し、溶液相機構モデルの転用（RI-06, SRG-2）を
   部分的に検証する。KCl/NaCl対照でRI-06（SRG-6: 表面阻害機構の転用）
   も前進させる（バンドル実行）。

3. EP-04a Discrimination / replication pack —
   フェノール毒化の用量-応答系列（0.1–1.0当量）で単一点実験
   （RI-04, SRG-1/SRG-6）を補強する。
```

認定ゲート順注記: EP-03a（活性種帰属）が機構論的証拠として最高情報利得を持ちSRG-1の核心に対応するため先行する。RI-05残存によりVQ-3到達時はVQ-3 (Qualified)となることを予告する。最終認定はVQ-1 → VQ-2 → VQ-3の継承ゲートで確定する。

---

**目的関数3: VQ-4 (Benchmark) への到達（VQ-3通過後）**

```
VQ-4 への最短ルート（VQ-3通過後）：

1. EP-09a Internal benchmark pack —
   refs 7–10（先行mechanochemical Heck、Pd粉末系）の収率・
   スコープ幅・反応時間・E-factorを本プロトコルと並べた
   比較表をResults/Discussionに掲載する。RI-09（C-1, C-2）を前進。

2. EP-08a Replication / uncertainty pack —
   VQ-2段階で実施したリプリケーションデータを基に、
   スコープ全エントリのNMR/単離収率 ± SDを完備する。
   RI-08（SRG-4）を確定的に前進。
   ※VQ-2段階でのEP-08a実施がVQ-4への布石となる。
```

認定ゲート順注記: VQ-4への実験投入はVQ-2段階から布石を打つことができる（EP-08aのデータ蓄積）。最終認定はVQ-1 → VQ-2 → VQ-3 → VQ-4の継承ゲートで確定する。

---

### §6 制度設計への寄与

**1. RI-03「Available-but-unutilized characterization」サブタイプの代表事例**

scr2のB-1は、RI-03 v0.2aで定義された「Available-but-unutilized characterization」サブタイプの典型事例を提供する。通常のRI-03（「未観測」）とは異なり、この事例では浸出実験データがESIに存在する（「see ESI† for details」という明示的な参照）。問題は「データがない」のではなく「データの定量的含意が主テキストで抽出されていない」ことである。「not mainly」という部分否定修飾語は閾値設定を含意するシグナルとして機能しており、こうした修飾語（"not mainly," "primarily," "predominantly"）を有するクレームは定量的閾値の要求を内包すると解釈すべきことを、本事例が確認する。将来のRI-03適用において「Available-but-unutilized」識別フラグとして「ESI参照付き定性的部分否定クレーム」パターンを検索条件とすることを提案する。

**2. PRI-11候補（Mechanism-kinetics decoupling）の適用可能性評価**

本論文はHeck触媒サイクル（酸化的付加→配位・挿入→β-H脱離→還元的脱離）を参照しながら「Pd(II)–Br種がミグラトリー挿入を阻害する可能性」という機構的帰属を行っている。PRI-11（「提案触媒サイクルから速度式を代数的に導出せずに、観測速度次数との一致のみで機構を支持」）の適用を検討したが、本論文では（a）速度次数データが全く存在しない（速度式との一致を検証していない）；（b）機構的帰属は「仮説」として明示的に限定されている（"leading us to hypothesize"）。したがってPRI-11は「機構仮説を速度データなしで提示した」というより「速度データも機構データも存在しない」ケースであり、A-1型の明示的猶予を伴う。PRI-11は**部分的に適用可能**だが典型事例とはならない。PRI-11の昇格判断には別の独立2報の典型事例が必要であり（v0.2a時点で昇格候補として1報確認済み）、本ケースはその条件を満たさない。

**3. 標識不整合（Labeling mismatch）パターンの検出**

本論文で以下の標識不整合が確認された：「[REDACTED: verbatim source text; see the source paper via its DOI]」（B-1）。「confirmed」という強認識動詞を使用しながら、直後の命題は「not mainly」という部分否定修飾語（閾値未設定）を含んでいる。閾値が設定されなければ「not mainly」は空の主張であるにもかかわらず、「confirmed」によって確認済み事実として提示されている。仮説標識や限定語句なしに強認識動詞が使用されており、この組み合わせが証拠強度を実際より高く見せる効果を持つ。このパターンはRI-03とRI-05の共起構造と連動する（§2 SRG-1参照）。SRG-1がRI-03（主）とRI-04（副）の共起を持つことを踏まえると、この標識不整合は証拠の実際の強度（単一点ESI参照）と叙述語の強度（"confirmed"）の乖離として、RI共起パターンの語用論的表出と位置づけられる。

**4. RI共起パターン（RI-03 + RI-04）の構造的記録**

SRG-1においてRI-03（活性種の未観測）とRI-04（単一点弁別実験）が共起している。この共起は相互補完的な弱化構造を持つ：浸出実験（RI-04: 定量的弁別基準なし）の弱さが表面触媒帰属（RI-03）を支持する証拠体系全体を弱化させ、逆にRI-03未解消がRI-04（単一点実験の不十分さ）の深刻度を増幅させる。いずれか一方の解消だけでは不十分であり、EP-03a（RI-03向け: ホットフィルトレーション+ICP-MS定量）とEP-04a（RI-04向け: 用量-応答系列）を組み合わせた実験設計が必要である。この RI-03 + RI-04 共起パターンはCodebook v0.2aの「RI共起パターン」として記録する。「表面/均一系触媒帰属問題」に関わるSRGで繰り返し確認されれば、この共起を「帰属問題SRGの標準共起形式」として規定できる。

**5. 否定的証拠の不完全性（Incompleteness of negative evidence）の検出**

B-5（フェノール毒化実験：0.5当量で12%残余収率）はRI-04の「否定的証拠の不完全性」パターンを示している。0.5当量での12%残余変換率は完全な表面阻害と矛盾するにもかかわらず、「[REDACTED: verbatim source text; see the source paper via its DOI]」という機構的結論に使用されている。この実験は：（a）質量収支が閉じていない（12%の生成物以外の行方が不明）；（b）用量-応答ウィンドウが評価されていない（0.5当量一点では完全/部分/不完全阻害の種別が不能）；（c）速度論的ウィンドウが評価されていない（表面阻害が速度低下か全停止かが不明）。これはRI-04の「否定的証拠の不完全性」サブタイプ（陰性実験を肯定的機構証拠として使用する際の質量収支閉鎖と速度論的ウィンドウ評価の欠如）のcase-specific実装例として登録する。

inference_time_sec: not available — inject externally
```
