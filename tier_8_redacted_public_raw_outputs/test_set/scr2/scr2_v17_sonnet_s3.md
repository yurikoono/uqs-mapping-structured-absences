```
prompt_version: stage3-v1-20260402
model_info: claude-sonnet-4-6

# 科学的知見の再認定判定票

## Templ, Hwang, Schwemin, Baltaci, Borchardt 2025（RSC Mechanochemistry, full_paper）

---

### §1 Claim Architecture

**コア主張:**
本論文のノベルティ柱は「直接メカノ触媒によるMizoroki–Heck反応の初の実行可能プロトコル」（Pd粉末ではなくPdボールを触媒として用い、機械的エネルギーと熱エネルギーの組み合わせで駆動する）であり、既報のSuzuki/Sonogashira直接メカノ触媒に続いてHeckを家族に加えることでパラジウム触媒C–C結合形成の網羅性を完成させる位置づけを取る。ユーティリティ柱は三層：（a）C(sp²)–I選択性（溶液系Heckがブロマイドにも反応するのに対して選択性が生じること自体が新しい特徴として提示される）、（b）one-pot Wittig/Heck連続反応、（c）無溶媒・不活性雰囲気不要・触媒回収容易という操作的実用性。

**Layered structure:**
主張は構造的に独立した3層を持つ。（1）直接メカノ触媒Heckプロトコルの存在証明：基質スコープで支持され、単一の実験的反証で全体が崩れることはない（他の基質が反応することは実証される）。（2）C(sp²)–I選択性：ArBr/ArClが不活性であることで独立に支持され、（1）の反証が（2）を直接崩さない。（3）one-pot Wittig/Heck：2基質のみを以て実証されており、（1）または（2）が崩れても（3）は実験事実として残る。ただし、論文の「直接メカノ触媒」という最重要概念は3層すべてに共通する前提——「反応がPdボール表面で起きている」——に依存しており、この前提が崩れれば3層の主張はいずれも再定義を迫られる（D-4-1のpriority_structure）。

---

### §2 SRG / CLA → RI / ER / EP Crosswalk

---

**SRG-1 [surface catalysis vs. leaching ambiguity]**

* **Primary RI**: RI-03 Unobserved explanatory — 触媒的に活性な種（Pd表面サイト vs. 溶液中溶出Pd種）が直接観測も速度論的拘束もされていない。「not mainly mediated by abraded palladium particles」という部分否定修飾語は観測の不在ではなく閾値の未設定を内包している。
* **Secondary RI**: RI-04 Unreplicated discriminator — ESIに委任された浸出実験が単一点評価であり、定量的弁別基準（触媒的に有意なPd濃度の閾値）が本文から欠落している。
* **ER**: 濾液中Pd濃度の定量値（検出下限付きICP-MS/ICP-OES）と、その濃度が速度論的に有意な均一系触媒を起こせないことの計算、または少なくともホットフィルトレーション試験（ボール除去後の残余変換率）かHg毒化試験の一方を提供すること。
* **EP**: EP-03a Direct-observation / state-assignment pack; EP-04a Discrimination / replication pack
* **Case-specific実装**: （i）反応30分時点でPdボールを除去し、残余30分での変換率進行を確認（ホットフィルトレーション）；（ii）Hg(0) 300当量（Pdボール表面原子数見積もり比）添加対照実験；（iii）ICP-MSによる反応濾液Pd定量（検出下限 < 1 ppb水準）と、公知のPd(0)/Pd(II)触媒活性の文献閾値との比較；（iv）反応前後のPdボール表面XPS（Pd 3d領域でPd(0) vs. PdO同定）。
* **注記**: B-1 [high_convergence_low_gap, 3/3, gap=none, 全エージェントhigh]。U-1（self-contradictory absence: 表面触媒モデルが予測する検出下限が未設定）、U-2（同: ホットフィルトレーション/Hg試験が主テキストから不在）。B-9, B-15, B-16, B-18も同根。D-4-1およびD-4-8の核心SRG。

---

**SRG-2 [chemoselectivity mechanism — C(sp²)–I vs C(sp²)–Br]**

* **Primary RI**: RI-03 Unobserved explanatory — C–I/C–Br選択性の起源となる素反応ステップ（酸化的付加段階の速度差 vs. 後続サイクルでのPd(II)–Br阻害）が直接観測されていない。
* **Secondary RI**: RI-05 Qualitative overread — アリールブロマイド不活性を「高い化学選択性」という構造的・合成的長所として提示し、かつ「Pd(II)–Br種がミグラトリー挿入を阻害する」という機構仮説を数値証拠なく提示している。
* **ER**: ArI/ArBr等量混合の競合基質実験、または各ArXの個別反応速度の比較測定。Pd(II)–Br錯体モデルと代替Pd(II)–I錯体のオレフィン挿入速度の比較（NMR滴定またはストップトフロー）によって「後段での阻害」仮説を検証すること。
* **EP**: EP-03a Direct-observation / state-assignment pack; EP-05a Quantitative-ranking substantiation pack
* **Case-specific実装**: 等量PhI/PhBr + スチレンの競合実験（標準条件）でNMR収率比を測定；別途、PhBr単独実験のみで変換率を0–30分の時系列で確認（反応が遅いのか全く進まないのかを区別する）；さらにK₂CO₃置換によってブロマイドの塩基依存性を確認。
* **注記**: A-1 [high_convergence_low_gap, V1=high, V2=critical, 2/3, gap=low]。ピボット: A-1 ↔ B-16。機構的猶予（A-1）が表面触媒未証明（SRG-1）の重要性を後景化する構造（priority_structureで記録済み）。RI-05が残存するため、VQ-3に到達した場合もVQ-3 (Qualified)と判定される可能性がある。

---

**SRG-3 [recyclability — claim without data]**

* **Primary RI**: RI-07 Unsupported boundary — 「活性を失わずに再利用可能」という境界主張がこのHeck反応について実験的根拠を持たない。
* **Secondary RI**: RI-02 Object identification — リサイクル後のPdボール表面状態（質量、XPS、SEM）が特定されていないため、何を再利用しているかの同定が不完全。
* **ER**: このHeck反応条件（PhI/スチレン、K₂CO₃、DMF、120°C、30 Hz）で少なくとも3回の連続リサイクル実験を実施し、各サイクルの単離収率とPdボール質量変化を報告すること。
* **EP**: EP-07a Boundary-test pack; EP-02a Identity / purity substantiation pack
* **Case-specific実装**: 標準基質（PhI + スチレン）で5サイクル連続Heck反応；各サイクル後にボールを取り出し秤量し、反応を仕込む（ボール洗浄プロトコルを明記）；5サイクル後のボール表面SEM撮影；ICP-MSによる各サイクル濾液Pd定量。
* **注記**: B-8 [high_convergence_low_gap, V1=high, V2=high, 2/3, gap=none]。U-3（Pd(II)→Pd(0)再還元機構の不在）、U-4（self-contradictory absence: リサイクルデータが主テキストにも言及なし）。D-4-3, D-4-7の根拠SRG。

---

**SRG-4 [quantitative data quality and replication]**

* **Primary RI**: RI-01 Reporting integrity — NMR収率（最適化テーブル、1時間）と単離収率（スコープテーブル、2時間）の混在による横比較不能。ブリッジ実験なし。
* **Secondary RI**: RI-08 Unquantified reliability — いかなるエントリーにも反復測定値・標準偏差・範囲が存在しない。
* **ER**: 最適化テーブルの標準条件エントリを少なくとも3回繰り返し、NMR収率 ± SDを報告；スコープテーブルとの比較を可能にするブリッジ実験（3aの1時間での単離収率）；スコープ全エントリに質量収支を付記すること。
* **EP**: EP-01a Reporting-coherence pack; EP-08a Replication / uncertainty pack
* **Case-specific実装**: Fig. 2エントリ5（標準条件、1h）の3回反復（NMR収率±σ）；Fig. 3条件（2h）でも3aのNMR収率を測定し、1h/2hの差を収率基準ではなく時間基準で切り分ける；Fig. 3全スコープエントリの反応後質量収支計算（回収出発物 + 生成物 + 副生物推定）。
* **注記**: B-7 [high_convergence_low_gap, V1=medium, V3=high, 2/3, gap=low]。B-21（最適化表の複数回測定なし、1/3）、B-23（1h vs 2h不整合、1/3）、B-25（質量収支なし、1/3）。D-4-4の根拠SRG。

---

**SRG-5 [one-pot Wittig/Heck characterization]**

* **Primary RI**: RI-04 Unreplicated discriminator — 2基質のみから構成されるスコープで、かつ3変数（塩基種、Ph₃P=O、反応順序）が同時に変化しており、結果の弁別力が低い。
* **Secondary RI**: RI-07 Unsupported boundary — スチレン誘導体スコープが「スチルベン誘導体への直接アクセス」として提示されるが、実証は2例のみ。
* **ER**: （a）Ph₃P=Oを標準Heck反応（K₂CO₃、PhI、スチレン）に添加した対照実験；（b）KOtBu単独でのHeck対照実験；（c）Wittig段階での出発物変換率の中間確認；（d）スコープを最低5基質に拡大。
* **EP**: EP-04a Discrimination / replication pack; EP-07a Boundary-test pack
* **Case-specific実装**: （a）1.4当量Ph₃P=Oを標準Heck（K₂CO₃）に添加し変換率を比較；（b）K₂CO₃→KOtBu置換のHeck単独収率；（c）one-pot反応の30分後停止・¹H NMR分析でアルデヒド残存量定量；（d）4-Cl-ベンズアルデヒド以外の電子的に多様なアルデヒド3種以上を追加。
* **注記**: B-11 [high_convergence_low_gap, V1=medium, V3=medium, 2/3, gap=none]。B-10（Ph₃P=O対照なし、1/3）、B-20（KOtBu混交、1/3）、B-26（工程別収率なし、1/3）。D-4-5の根拠SRG。

---

**SRG-6 [bulking agent / surface inhibition mechanism]**

* **Primary RI**: RI-06 Imported model — 「snowballing」（物理的表面被覆）と「Cl⁻/OAc⁻によるPd表面サイト配位」という2つの異なる阻害機構が区別されず、後者は溶液相Pd化学から転用されている。
* **Secondary RI**: RI-04 Unreplicated discriminator — 4-ヒドロキシビフェニルによる毒化実験が0.5当量の単一濃度であり、用量-応答関係なし。
* **ER**: KCl/KOAc使用後のPdボール表面の顕微鏡観察（「snowballing」の視覚的確認）；アニオン置換対照実験（NaCl vs KClでカチオン/アニオン効果を分離）；4-ヒドロキシビフェニルの用量-応答系列（0.1–1.0当量）。
* **EP**: EP-06a Analogy-validation pack; EP-04a Discrimination / replication pack
* **Case-specific実装**: KCl、KOAc、K₂SO₄を用いた各反応後のPdボール光学顕微鏡またはSEM撮影；KCl vs NaCl（各等当量）対照でsnowballing vs Cl⁻配位を分離；フェノール毒化用量系列（0.1, 0.25, 0.5, 1.0, 2.0当量）でIC₅₀推定。
* **注記**: B-4 [high_convergence_low_gap, V1=medium, V2=medium, 2/3, gap=none]。B-5 [high_convergence_low_gap, V1=medium, V2=medium, 2/3, gap=none]。このSRGに直接対応するD-4候補なし（SRG-6はD-4-1の傍証として機能）。

---

SRG外：CLA

**CLA: [E/Z ratio and stereochemical control]**

* **Primary RI**: RI-01 Reporting integrity — Heck反応スコープ論文の標準的な記述要件であるE/Z比が全生成物にわたって欠落している。
* **Secondary RI**: RI-08 Unquantified reliability — "(E)-isomers"という帰属が数値比なしに全基質に適用されており、特にアクリレート系（3u–3w）での選択性が未定量。
* **ER**: 全スコープ生成物のE:Z比（¹H NMRビニルプロトン積分）を報告すること。E:Z > 95:5の場合はその旨を数値で記載。
* **EP**: EP-01a Reporting-coherence pack; EP-08a Replication / uncertainty pack
* **Case-specific実装**: 粗生成物¹H NMRスペクトルのビニル領域（5.0–7.5 ppm）で(E)体/(Z)体（存在する場合）の積分比較；特に3u（tert-ブチルアクリレート）、3v（アクリロイルモルホリン）、3w（ヘキシルアクリレート）のアクリレート系で確認。
* **注記**: B-14 [high_convergence_low_gap, V2=medium, V3=medium, 2/3, gap=none]。いずれのSRGにも属さない独立CLA。D-4-6の根拠。

---

### §3 現在のVQ判定

**現在判定: VQ-1 (Observation)**

---

**VQ-1 [Observation] → 通過（非致命的RI-02残存）**

生成物の構造同定は¹H NMRおよび単離により達成されており、構造的異性体との誤帰属を排除できる粒度でスコープが記述されている。Pdボールは元素金属として市販品から明確に定義される。残存RI-02は2点：（a）Pd表面の酸化状態（Pd(0) vs. PdO）が反応条件下で確認されていない（B-18）、（b）E/Z比が全生成物で欠落（B-14, CLA）。いずれも現行の生成物同定を根底から覆すものではなく、非致命的と判定する。

---

**VQ-2 [Method] → 未達**

VQ-2通過にはRI-01（報告の整合性）とRI-07（境界主張の裏付け）の解消が必要。RI-01未解消：NMR収率（最適化Table, 1h）と単離収率（スコープTable, 2h）の混在（B-7）、反応時間不整合（B-23）、全エントリでの複数回測定なし（B-21）により、最適化データとスコープデータの横比較が原理的に無効化されている。RI-07未解消：「活性を失わずに再利用可能」という境界主張がHeck反応に対して実験的根拠を持たない（B-8, U-4）。機能基許容性のスコープは部分的に試験されているが、「broad tolerance」という主張と不活性基質（ArBr、ArCl、フェノール、3t）の組み合わせが、明示的な境界条件の定義なしに提示されている。

---

**VQ-3 [Mechanism] → 未達（VQ-2に独立して）**

VQ-3通過にはRI-03、RI-04、RI-06の解消が必要（かつVQ-2継承）。RI-03未解消：触媒的活性種（Pdボール表面 vs. 溶出Pd種）が主テキストの証拠から特定されていない（SRG-1, U-1, U-2）。RI-04未解消：浸出実験はESI参照（単一点）であり、フェノール毒化は0.5当量の単一濃度（用量-応答系列なし、B-5）。RI-06未解消：snowball機構と配位子型阻害機構の区別がなく、溶液相Pd化学の知見がPdボール表面系に転用されている（SRG-6）。注：RI-05が中程度残存（C(sp²)–I選択性が定性的順位から機構的含意を導出: SRG-2）のため、VQ-3に到達した場合もVQ-3 (Qualified) となる。

---

**VQ-4 [Benchmark] → 未達（VQ-3に独立して）**

VQ-4通過にはRI-08、RI-09の解消が必要（かつVQ-3継承）。RI-08未解消：反復測定・不確かさ記述がいかなる実験値にも存在しない（B-21）。RI-09未解消：先行Pdパウダー型Heckプロトコル（refs 7–10）との定量的性能比較が結果部に存在しない（C-1: Dropped Quantitative Benchmark）。自グループ先行Pd球Suzuki/Sonogashiraとの効率比較も欠落（C-2）。

---

### §4 Era-Norm Annotation

**communication-era tolerated（2025, RSC Mechanochemistry 5ページ短報）:**

- B-2（外部温度vs内部温度の未報告）: 2025年時点でのメカノケミストリー分野では、ミリング中の内部温度をリアルタイム計測することは技術的に非標準であり、外部ジャケット設定温度のみを報告するのがほぼ普遍的な慣行。当時の分野ノルムに照らして許容される欠落。
- B-21（最適化テーブルの複数回測定なし）: 合成論文の最適化スクリーニングにおいて単一測定値のみを掲載することは2025年時点でも短報フォーマットでは一般的に許容される慣行（詳細再現性はスコープ部分で暗黙に担保されるとみなされる）。
- B-25（スコープの質量収支なし）: 合成スコープ論文における質量収支の全例列挙は2025年においても必須ではなく、RSC Mechanochemのような短報専門誌では特にページ制約上省略が許容されている。
- B-14（E/Z比の欠落）: Heck反応の(E)体支配的生成は分野の暗黙知であり、特に高度に選択的な生成物に対してE/Z比の数値列挙を省略することは、2025年時点では一部の専門誌で許容されている（ただし境界線上）。

**modern-era deficient（2025年現代水準では不足）:**

- B-1（浸出実験の定量的閾値不在）: 直接メカノ触媒の論文で「not mainly」という部分否定修飾語を定量的閾値なしに主張の根拠として使用することは、2025年の水準ではRI-03の未解消として判定される。ICP-MSによるPd定量と触媒的有意濃度の設定、またはホットフィルトレーション/Hg毒化の一方は、「不均一 vs 均一触媒」の帰属を主張する論文の現代的最低要件。
- B-8（Heck反応固有のリサイクルデータの完全不在）: Suzuki/Sonogashiraの先行論文から再利用可能性の主張を概念転用しながら、Heck固有の条件でのリサイクル実験を一切示さないことは、2025年の査読では「unsupported novelty claim」として指摘される水準。
- C-1（先行mechanochemical Heck protocols [refs 7–10]との定量比較なし）: 先行プロトコルを導入部で数値なしに引用し結果部で比較しないDropped Quantitative Benchmarkパターンは、2025年において研究意義の評価上の重大な欠落とみなされるようになっている。
- A-1 + SRG-1の組み合わせ（活性種と選択性機構の双方未特定）: 「反応を担う活性種が何か」（SRG-1）と「なぜC–I選択性が生じるか」（A-1）の両者が同時に未特定であることは、2025年の機構論的基準では2つの独立した必須解明事項として査読上フラグが立てられる組み合わせ。

---

### §5 最短補強ルート

**目的関数1: VQ-2 (Method) への到達**

```
VQ-2 への最短ルート：

1. EP-01a Reporting-coherence pack —
   Fig. 2 entry 5（標準条件、1 h）の3回反復でNMR収率 ± SDを確認し、
   Fig. 3（2 h）条件でのブリッジ実験（3aの単離収率）を実施して
   時間・収率基準の不整合を解消する。RI-01 を前進。

2. EP-07a Boundary-test pack —
   標準基質（PhI + スチレン）で5サイクル連続Heck反応を実施し、
   各サイクルの単離収率とPdボール質量変化を報告して
   「活性を失わずに再利用可能」という境界主張を実証する。RI-07 を前進。
```

認定ゲート順注記: 実験投入順は情報利得順（EP-01aが小規模再実験で実行可能なため先行）だが、認定はVQ-1 → VQ-2 → VQ-3 → VQ-4の継承原則に従って確定する。

---

**目的関数2: VQ-3 (Mechanism) への到達（VQ-2通過後）**

```
VQ-3 への最短ルート（VQ-2通過後）：

1. EP-03a Direct-observation / state-assignment pack —
   ホットフィルトレーション試験（30分時点でPdボールを除去し
   残余30分の変換率進行を確認）またはHg(0)毒化試験（300当量）
   のいずれかを実施し、さらにICP-MSによる反応濾液Pd定量（検出下限付き）
   を提供することで活性種の帰属を固める。
   並行してXPS（Pd 3d領域）によるボール表面の反応前後比較で
   Pd(0) vs. PdO状態を確認する。RI-03 および残存RI-02 を前進。

2. EP-04a Discrimination / replication pack —
   ArI/ArBr等量混合競合実験（標準条件下のNMR収率比）と
   フェノール毒化の用量-応答系列（0.1–1.0当量）を実施し、
   単一点実験の弁別力を高める。RI-04 を前進。

3. EP-06a Analogy-validation pack —
   KCl・KOAc使用後のPdボール表面SEM撮影（snowballing確認）と
   NaCl vs KCl対照実験（アニオン vs カチオン効果の分離）により、
   溶液相Pd化学から転用された阻害機構モデルを
   Pdボール系で直接検証する。RI-06 を前進。
```

認定ゲート順注記: EP-03a（活性種帰属）が機構論的証拠として最高情報利得を持ち先行する。最終認定はVQ-1 → VQ-2 → VQ-3の継承ゲートを順次通過して確定する。

---

**目的関数3: VQ-4 (Benchmark) への到達（VQ-3通過後）**

```
VQ-4 への最短ルート（VQ-3通過後）：

1. EP-08a Replication / uncertainty pack —
   スコープ全エントリの質量収支報告と、
   代表的エントリ（3a、3s、3v）の複数回測定による
   単離収率 ± SDを提供する。RI-08 を前進。

2. EP-09a Internal benchmark pack —
   refs 7–10（先行mechanochemical Heck）の収率・スコープ幅・
   反応時間・E-factorを本プロトコルと並べた比較表を
   Results/Discussionに掲載する。RI-09 を前進。
```

---

### §6 制度設計への寄与

**既存RIコードの代表事例:**

scr2はRI-03（Unobserved explanatory）の「不均一触媒の活性種帰属」型の新たな典型事例を提供する。この論文の特徴は、RI-03問題の存在を示す語用論的マーカー——「not mainly mediated by」という部分否定修飾語——が主テキストに明示されている点にある。このマーカーは「閾値が設定されていないため部分否定は空の主張に等しい」という構造を読解者に伝える。将来のRI-03事例評価において、こうした部分否定修飾語（"not mainly," "primarily," "predominantly"）は定量的閾値の要求を含意するシグナルとして検索可能な形で記録する価値がある。

RI-01（Reporting integrity）については、単一論文内での「収率測定基準の切り替え（NMR→単離）」と「反応時間の不整合（最適化1h/スコープ2h）」の組み合わせが、最適化-スコープ間の横比較を無効化する事例を追加確認した。これはCodebook定義の「測定フレームの不統一」に直接収まる既存事例の追加確認。

**新規PRI候補の提案:**

今回のケースで検出されたパターンは既存RI-01〜RI-09の範囲内に収まり、新規PRIコードの提案は不要と判断する。

**VQ判定基準の境界条件に関する新知見:**

§4のEra-Norm Annotationで示したように、「ESIに定量データを委任しつつ定性的結論（"not mainly"）を主テキストに記載する」構造は、communication-era toleratedとmodern-era deficientの境界を横断する事例として記録価値がある。この境界位置は論文年（2025）・ジャーナル（RSC Mechanochemistry、新興誌）・分野ノルム（表面触媒の帰属要件の成熟度）の3変数に依存しており、将来の同分野論文のEra-norm評価の参照事例となる。

また、SRG-1とA-1が同一論文に共存する構造——「活性種が不明（SRG-1）+ 選択性機構が先送り（A-1）」の組み合わせ——は、どちらの未解消でも相手方の機構的説明責任を免除する「相互依存的先送り」として機能することが確認された。このパターンはpriority_structureで記録されたが、VQ判定においても「RI-03がSRG-1で未解消 + RI-03がSRG-2でA-1として先送り」が互いを強化する構造として、VQ-3の複合的未達要因として位置づけられる。この相互依存パターンはVQ基準マトリクスの将来的な注記候補として提案する。

**EP辞書への追記:**

EP-03a (Direct-observation / state-assignment pack) のcase-specific実装として、「不均一金属触媒の活性種帰属」用のサブプロトコル——(i) ホットフィルトレーション、(ii) Hg(0)毒化、(iii) ICP-MSによる濾液Pd定量＋触媒的有意閾値との比較、(iv) XPS表面分析——の4点セットが、scr2の事例から構造化されたテンプレートとして提供される。このサブプロトコルは電気化学触媒（金属溶出問題）や光触媒（表面/ラジカル均一系帰属）にも転用可能であり、EP-03aのcross-domain実装例として記録する。

inference_time_sec: not available — inject externally
```
