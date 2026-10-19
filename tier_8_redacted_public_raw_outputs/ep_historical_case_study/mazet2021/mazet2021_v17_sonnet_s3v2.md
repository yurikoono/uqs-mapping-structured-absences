```
prompt_version: stage3-v2-20260416
model_info: claude-sonnet-4-6

# 科学的知見の再認定判定票

## Poisson, Tran, Besnard, Mazet 2021（ACS Catalysis, full_paper）

---

### §1 Claim Architecture

**コア主張の要約**

本論文は、Niビスホスフィン触媒によるエノールリン酸のクマダビニル化において、[(dppe)NiBr₂]（4c）と[(dmpe)NiBr₂]（4d）の二つの前駆体がともにNi(0)/Ni(II)マニフォールドを経由するが、互いに異なる素反応経路を辿ることを主張する。

**Novelty柱：**
1. **急速リン酸/臭化物イオン交換**（dppe系）：Ni(0)/Ni(II)サイクルにおいてトランスメタル化に先立つイオン交換が「この系の重要な特徴」として同定される——従来の「テキストブック的」OA/TM/RE経路との区別。
2. **二核ニッケル間トランスメタル化**（dmpe系）：前駆体活性化で生成したビニルNi種（I-a）が触媒サイクル中のα-スチリルNi(II)中間体（III-b）をインターセプトするという「異例な」機構——見かけ二次の速度論的依存性と化学量論実験が根拠。
3. **前駆体活性化の同定**：I → I-a → I-b → IIの二重トランスメタル化/還元的脱離配列が「現在の文献でほとんど記録されていないプロセス」として実証。

**Utility柱：** 「この研究で同定された異例な機構的特徴は、より複雑なビニルシントンのカップリングに向けた次世代触媒の開発を促進するだろう」（T1）。

**Layered structureの判定**

三つの主張は部分的に独立した層構造をなす。
- **層A**（Ni(0)/Ni(II)マニフォールドの確認）：ラジカルクロック・TEMPO捕捉・常磁性Ni(I)種の非検出に根拠を持ち、層B・Cから独立して成立しうる。
- **層B**（dppe系：イオン交換機構）：³¹P NMR監視・静止状態同定（9c/III-b）に根拠。層Cの反証は層Bに影響しない。
- **層C**（dmpe系：二核TM仮説）：見かけ二次速度論とFigure 9化学量論実験のみに依拠。層A・Bの成立は層Cの証拠強度を強化しない。

層Cが反証されても層AとBは残る。層Bが部分的に修正されても層Aは残る。ただし「比較機構論文」としての中心的価値は層B（dppe）と層C（dmpe）の両方が成立することで実現するため、層Cの弱体化は論文全体の主張の信頼性に実質的に影響する。

---

### §2 SRG / CLA → RI / ER / EP Crosswalk

**SRG-1 [VTNA kinetic-order validity]**（B1, B2, B3, B4, B5, B6）

* **Primary RI**: RI-04 [Unreplicated discriminator] — dppe/dmpe両系の速度論的次数（dppe: 基質零次、触媒一次；dmpe: 触媒二次）は、条件内レプリケートなし・グッドネスオブフィット基準なし・グラフィカルオーバーレイのみで「最適」と判定されており、代替次数（dmpe: 一次など）が統計的に排除されていない。
* **Secondary RI**: RI-08 [Unquantified reliability] — 触媒分解による有効触媒濃度の低下が補正されておらず、見かけ次数の信頼性が構造的に不確定。
* **ER**: dmpe系の二次依存性が一次と識別されるためには、（i）条件内で3回以上のレプリケートによるノイズベースラインの確立、（ii）一次・二次モデルの正式な適合品質比較（残差二乗和またはAIC）、（iii）t=0での実効Ni(0)濃度の³¹P NMR定量（前駆体活性化消費分の補正）が必要。
* **EP**: EP-04a [Discrimination/replication pack]; EP-08a [Replication/uncertainty pack]
* **Case-specific実装**:
  - 同一[4d]初期濃度（例：2.5 mol%）でVTNA実験を3回反復し、ラン間ばらつきをin situ IRシグナルの標準偏差として定量する。
  - 一次・二次モデルのグラフィカルオーバーレイについてΣ(残差²)を計算し、改善率（一次→二次）をF検定または類似基準で判定する。
  - 4c/4dの反応前にin situ IRまたは³¹P NMRで活性化完了時点を同定し、t=0の有効Ni(0)濃度をVTNA正規化の入力値として使用する。
* **注記**: B1はhigh_convergence_low_gap（V1=V2=V3=high, convergence=3/4, gap=none）—— 本SRGの最重要項目。B2はconvergence=3/4, gap=low。RI-04 + RI-08の共起パターン: RI-04（識別力不足）単独の解消だけでは不十分であり、RI-08（分解補正なし）も同時に解消しなければVTNA次数の信頼性は回復しない。

---

**SRG-2 [dmpe cycle mechanistic evidence]**（B1, B8, U1, U3）

* **Primary RI**: RI-03 [Unobserved explanatory] — dmpe触媒サイクルの速度決定ステップとして提案されたI-a/III-b間のトランスメタル化は、直接観測も中間体補足もなく、静止状態の同定も失敗している（「not met with success」）。
* **Secondary RI**: RI-04 [Unreplicated discriminator] — Figure 9の化学量論実験（U1）は1a/8a等量使用で7%/8%の収率を与えており、統計的スクランブルとの区別に必要な対照実験（単一求電子剤）が実施されていない。**PRI-11 [Mechanism-kinetics decoupling]** も適用される: 論文はFigure 8B（dmpe系）の触媒サイクルから速度式を代数的に導出せずに、観測された見かけ二次の触媒依存性との「一致」のみでI-a/III-b間二核TM機構を支持している——提案サイクルから[Ni]²依存の速度式が導出されるかどうかの検討が欠如している。
* **ER**: dmpe系の二核TM仮説を機構的主張として成立させるためには、（i）dmpe触媒サイクルの静止状態の同定、（ii）見かけ二次速度論の代替解釈（Ni二量化平衡など）の排除、（iii）Figure 9設計の単一求電子剤対照による選択的クロスオーバーの実証、（iv）Figure 8Bのサイクルから代数的に導出した速度式と観測次数の一致の確認が必要。
* **EP**: EP-03a [Direct-observation/state-assignment pack]; EP-04a [Discrimination/replication pack]
* **Case-specific実装**:
  - dmpe系の触媒反応（[4d]=2.5 mol%、−10°C）をin situ ³¹P NMRで監視し、触媒回転中に蓄積する最大濃度のP-含有種をI-aまたはIII-bの合成標準品と比較して静止状態を同定する。
  - [(dmpe)Ni(3g)] 6dを調製し、0.5 equiv 1aのみを添加したコントロール実験（8a不在）を実施し、3aa収率とバックグラウンド（ランダムカップリング）を確立する。
  - Figure 8Bの定常状態近似を適用してd[3aa]/dtを代数的に導出し、[I-a]および[III-b]が触媒総濃度の関数として速度式に[Ni]²項を生むかどうかを確認する。
* **注記**: B8はSRG-2の致命的要素（Fatal RI-03）。U1はself-contradictory absenceとしてU分類。PRI-11はBreitenfeld 2014で提案、Pengfei 2024で同型確認済みの暫定コード。本論文は3報目の独立確認となり、PRI-11の正式昇格を支持する材料となる。

---

**SRG-3 [Ion exchange step evidence]**（B7, U2）

* **Primary RI**: RI-03 [Unobserved explanatory] — サブタイプ: **Available-but-unutilized characterization** — イオン交換の速度は未測定；交換の前提条件であるリン酸塩の配位様式（κ¹-O vs κ²-O,O'）はX線構造（CCDC 2116220）が存在するにもかかわらず主テキストに記載されていない。
* **Secondary RI**: RI-05 [Qualitative overread] — 「迅速な」交換はトランスメタル化速度との比較なしに断言されており、「迅速性」の定量的根拠がない。
* **ER**: イオン交換をdppe機構の「重要な特徴」として確立するためには、（i）CCDC 2116220に寄託された9cの結晶構造からNi–O結合距離・O–P–O角・配位様式を確認・主テキストに報告し、（ii）低温NMRキネティクスまたはストップトフロー実験でイオン交換速度定数（またはk_exchange > k_transmetalation の不等式として）を推定する必要がある。
* **EP**: EP-03a [Direct-observation/state-assignment pack]; EP-05a [Quantitative-ranking substantiation pack]
* **Case-specific実装**:
  - CCDC登録済み構造（2116220）から9cのNi–O距離とO-P-O角を抽出し、κ¹-O結合を確認する（既存データからの無実験的補強）。
  - THF-d₈中−40°Cで4c + 1a（またはモデルリン酸塩）を混合し、BrMgX添加後の³¹P NMRシグナル変化を時間分解測定してk_exchangeを推定する。
* **注記**: U2はself-contradictory absenceとして分類（取得済みX線構造の機構的未活用）。B7はconvergence=3/4, gap=low。

---

**SRG-4 [Ligand-effect attribution without benchmark]**（B10, C3）

* **Primary RI**: RI-06 [Imported model] — %V_Burモデルと「低い活性化障壁」（refs 14–15の計算予測）が、この化学系での同型性実証なしに輸入されている。dppe/dmpe間の反応性差異の「立体的起源」帰属は、σドナー能と咬角を同時に変化させる2点比較のみに基づく。RI-06サイクルレベル輸入サブタイプには相当しないが、個別素反応ステップの計算モデルを対象系で検証せずに利用した典型例。
* **Secondary RI**: RI-05 [Qualitative overread] — 2点データ（dppe vs dmpe）から三変数（立体・電子・幾何）の支配因子を定性的に解釈している。
* **ER**: 立体効果の支配を確立するためには、中間の%V_Burを持つ追加ビスホスフィン配位子（例：dppp、dppbz）での酸化的付加収率測定が必要。計算予測（低い障壁）を実験データと接続するためには、推定されたΔG‡（Arrhenius/Eyring解析）との数値比較が必要。
* **EP**: EP-06a [Analogy-validation pack]; EP-05a [Quantitative-ranking substantiation pack]
* **Case-specific実装**:
  - dppp（%V_Bur ~dppe/dmpe中間）を用いた[(dppp)NiBr₂]の前駆体活性化実験を実施し、adamantylエノールリン酸1dへの酸化的付加収率を測定してdppe/dmpeとの%V_Bur相関を確認する。
  - 速度論データ（VTNA）から活性化パラメータ（ΔH‡, ΔS‡）を抽出し、refs 14–15の計算障壁と数値比較する。
* **注記**: C3はDropped Quantitative Benchmark（計算障壁値が主テキスト未記載）。B10はconvergence=3/4, gap=low。

---

**SRG-5 [E/Z selectivity origin]**（A1, B12）

* **Primary RI**: RI-03 [Unobserved explanatory] — 基質3ceでの温度依存的E/Z逆転（4b系: 40:60 → 04:96、17°C上昇で）と触媒依存的E/Z相違（4aと4bで正反対）の構造的起源が、提案された触媒サイクル内で特定されていない。還元的脱離段階のNi(II)中間体IVの配座・立体化学が未検討。
* **Secondary RI**: RI-05 [Qualitative overread] — 立体化学データ（E/Z比、温度依存性）が機構的考察なしに提示される。
* **ER**: E/Z選択性の機構的起源を確立するためには、IV中間体のcis/trans配置の計算的評価（または低温VT-NMRによる直接観測）と、温度依存的E/Z比のEyring解析（ΔΔG‡の符号変化の確認）が必要。
* **EP**: EP-03a [Direct-observation/state-assignment pack]; EP-05a [Quantitative-ranking substantiation pack]
* **Case-specific実装**:
  - 3ceに対応するβ-メチル置換ビニルエノールリン酸での反応をVT条件（−40°C〜40°C、8点）で実施し、E/Z比のEyring plot（lnRE/Z vs 1/T）によりΔΔH‡・ΔΔS‡を決定する。
  - DFTでdppe/dmpe系のIV中間体（4配位正方平面Ni(II)-ジビニル錯体）のcis/trans異性体エネルギーを比較し、E/Z選択性の設定ステップ（トランスメタル化か還元的脱離か）を特定する。
* **注記**: A1（forgotten型）。SRG-5は機構論文の本来的スコープ内にあるにもかかわらず未着手。B12はconvergence=1/4（単一エージェントV2=high）。

---

**SRG-6 [Quantitative NMR claims without uncertainty]**（B13, B14, B15, B17）

* **Primary RI**: RI-08 [Unquantified reliability] — 化学量論的実験のNMR収率（11c: 70%など）、質量収支（「excellent」）、基質スコープ収率がすべて単一測定・不確かさ記述なしで報告されている。
* **ER**: 機構的証拠として使用するNMR収率はn≥2レプリケートと標準偏差の記載が必要。質量収支は百分率（±x%）で報告されるべき。
* **EP**: EP-08a [Replication/uncertainty pack]
* **Case-specific実装**: 11cのNMR収率（70%）測定を3回反復し、³¹P内部標準法の再現性（SD）を記載する。
* **注記**: SRG-6はNon-fatal（機構的主張の根底を覆さない）。

---

**SRG外：CLA**

**CLA: Negative evidence detection limits**（B11, B16）

* **Primary RI**: RI-04 [Unreplicated discriminator] — ラジカル環化生成物12/13の非検出（B16）とIV中間体の非観測（B11）がラジカル排除・還元的脱離迅速性の積極的証拠として使用されているが、各観測の検出下限が未記載。
* **Secondary RI**: RI-03 [Unobserved explanatory] — IV中間体は非観測であるが、捕捉実験（CO挿入、イソシアニド付加、低温単離）が実施されていない。
* **ER**: 「検出されない」という観察を機構的証拠として使用するためには、使用した分析手法の検出下限（¹H/³¹P NMRのS/N閾値、またはHRMSによる<x%の存在確認）を記載し、「存在しない」と「検出感度以下」を区別する必要がある。ラジカルクロックについては、基質1gのプローブ基の環化速度定数（文献値）から導かれる各素反応ステップの速度下限値を明記すべき。さらに質量収支の閉鎖確認（12/13が形成されないなら炭素はどこへ行ったか）と速度論的ウィンドウ評価（ラジカルクロック1gの環化速度定数k_cyclと反応速度の比較）が欠如している。
* **EP**: EP-04a [Discrimination/replication pack]; EP-03a [Direct-observation/state-assignment pack]
* **Case-specific実装**:
  - ラジカルクロック実験（Figure 6A）において、基質1gのシクロプロピルカルビニル型プローブの環化速度定数k_cyclを文献から引用し、12/13の検出下限（例：<1%、GC-MSによる）と組み合わせてカップリング素反応の速度下限（k > k_cycl/[12の検出下限]）を明示する。
  - 反応粗混合物の完全な¹H NMR質量収支を計算し、12/13不在時に全炭素が3agに収束することを定量的に確認する。

---

### §3 現在のVQ判定

現在判定: **VQ-2 (Method)**

**VQ-1 [Observation]（RI-02要件）: 通る**
提案された鍵中間体（7c、7d、9c）がX線結晶解析（CCDC 2116218–2116220）とNMRで同定・構造決定されており、RI-02は実質的に充足されている。Non-fatalな残存としてB17/SRG-6（NMR収率の不確かさ未記載）があるが、観察水準の主張成立を覆すものではない。

**VQ-2 [Method]（RI-01, RI-07要件 + VQ-1継承）: 通る（Non-fatal残存あり）**
VQ-1継承を前提として、RI-01（Reporting integrity）はNMR収率と単離収率の混在（B17）、IRバンド未特定（B5）で部分的に未充足だが、機構的主張の根底を覆さない（Non-fatal）。RI-07（Unsupported boundary）は試験した配位子がdppe/dmpeの2種のみだが、「両触媒はNi(0)/Ni(II)で動作する」という層A主張の境界は実験範囲内で適切に設定されている（Non-fatal）。

**VQ-3 [Mechanism]（RI-03, RI-04, RI-06要件 + VQ-2継承）: 未達**
VQ-3には以下の理由で到達しない：
- **RI-03（Fatal）**: dmpe系の静止状態が同定されておらず（B8、SRG-2）、速度決定ステップ（I-a/III-b間TM）が直接観測されていない。また、dppe系のイオン交換に必須のκ¹-O配位様式がX線データから確認されていない（U2、SRG-3 — Available-but-unutilized characterization）。dmpe層Cについては致命的；dppe層Bについては非致命的。
- **RI-04（Fatal）**: dmpe系の見かけ二次速度論は条件内レプリケートなし・グッドネスオブフィット基準なし・触媒分解補正なしで導かれており（SRG-1、B1）、一次との統計的区別が達成されていない。U1の化学量論実験も統計的スクランブルとの区別に必要な対照が欠ける（U1、SRG-2）。
- **PRI-11（Fatal for VQ-3 dmpe）**: Figure 8Bのdmpe触媒サイクルから[Ni]²依存の速度式が代数的に導出されておらず、観測次数との一致のみで機構を支持している。これはRI-04のFatal性をさらに深刻化させる。
- **RI-06（Non-fatal）**: %V_Burモデルおよび計算RE障壁の輸入（SRG-4、B10、C3）は残存するが、dppe系の機構主張には致命的でない。
- **RI-05（残存）**: 「迅速な」イオン交換（B7、SRG-3）の定性的主張はRI-05に対応し、VQ-3を「Qualified」以下に留める。

ただし**dppe系**（層B）単独では：RI-03がほぼ充足（静止状態III-b同定済み、Non-fatal残存はκ¹-O配位未確認）、RI-04は非致命的、RI-06は非致命的であり、VQ-3 (Qualified)に到達している（RI-05のイオン交換「迅速性」未定量が「Qualified」限定の理由）。

**VQ-4 [Benchmark]（RI-08, RI-09要件）: 未評価**
VQ-3未達のため評価対象外。なお、VQ-3到達後もRI-08（SRG-6：NMR収率の不確かさ）およびRI-09（直接比較なしの優位性主張、refs 14–15の計算値）が未解消であり、VQ-4への追加投入が必要。

---

### §4 Era-Norm Annotation

**communication-era tolerated（2021年基準で許容される欠落）:**

- **B17** (NMR収率、単離収率なし): 2021年のACS Catalysis合成・機構論文においてNMR収率（内部標準法）の不確かさ非記載は標準的慣行であり、多くの同時期論文で同様。
- **B4** (X線品質指標のSI収録): 結晶構造品質データのCCDC寄託＋SI記載は2021年時点での標準フォーマットであり、本文省略は正当。
- **B14** (「excellent mass balance」定性的記述): 機構研究でのNMR質量収支の定性的記述は2021年時点で一般的。
- **A2** (活性化パラメータ未抽出): VTNA法からのEyring解析は2021年時点でまだ確立されていない分析手法であり、当時の機構論文での不在は許容される。

**modern-era deficient（現代再認定基準では許容できない欠落）:**

- **B1/SRG-1** (VTNA次数決定のレプリケートなし・グッドネスオブフィットなし): 現代の速度論的機構研究ではVTNA適用に際しレプリケート実験と適合品質の明示が求められる——特にdmpe系の「見かけ二次」という中核的主張の根拠として使われる場合。
- **B8/SRG-2** (dmpe静止状態の未同定): 2020年代以降の機構論文では、提案された触媒サイクルの全てのRDSに対して静止状態の分光学的同定が期待される。
- **U2/SRG-3** (X線データからのNi–O配位様式未報告): 「迅速なイオン交換」という機構的主張の構造的前提を検証するために必要なX線パラメータが、利用可能な構造から報告されていない——時代基準に関係なく、利用可能なデータの不完全な活用（Available-but-unutilized）である。
- **U1/SRG-2** (化学量論クロスオーバー実験の対照欠如): dmpe系の機構を支持する核心的実験が統計的スクランブルと区別できないのは、当時・現代を問わず実験デザインの不備。
- **PRI-11/SRG-2** (触媒サイクルからの速度式非導出): 現代の機構論文では、速度論的次数の一致を主張する際に提案サイクルからの代数的導出が期待される——Burés VTNA法の普及（2016年以降）はこの要求を実質的に新興基準にした。

---

### §5 最短補強ルート

**第一目的関数：VQ-3 — 特にdmpe系（層C）の機構主張の成立**

致命的項目（RI-03 Fatal、RI-04 Fatal、PRI-11）から順番に対処する：

**VQ-3 への最短ルート：**
1. EP-03a [Direct-observation/state-assignment pack] — CCDC 2116220から9cのNi–O距離・リン酸結合様式を抽出し主テキストに記載（無実験）し、さらにin situ ³¹P NMRで[4d]の触媒回転中の最大蓄積種をI-aまたはIII-bと同定する。RI-03を前進。
2. EP-04a [Discrimination/replication pack] — 同一[4d]でVTNA実験を3回反復してGOFを定量し（一次/二次をAICで識別）、かつ単一求電子剤コントロール実験（6d + 1aのみ）を実施してU1の統計的スクランブル解釈を排除する。RI-04を前進。Figure 8Bの定常状態近似から速度式を代数的に導出し[Ni]²依存条件を確認することでPRI-11を前進。
3. EP-05a [Quantitative-ranking substantiation pack] — THF-d₈中−40°Cで4c + 1aのイオン交換を時間分解³¹P NMRで監視し、k_exchangeを推定してB7「迅速性」を定量化する。RI-05を前進。

**第二目的関数：VQ-4 — Benchmarkレベルへの到達（VQ-3到達後）**
4. EP-08a [Replication/uncertainty pack] — 全ての機構的NMR収率（11c：70%を含む）を n≥2 反復で報告し、標準偏差を付記。RI-08を前進。
5. EP-09a [Internal benchmark pack] — VTNAデータからEyring解析でΔH‡・ΔS‡を抽出し、refs 14–15の計算RE障壁と数値比較。dppp配位子系（中間%V_Bur）での酸化的付加収率測定で3点相関を確立。RI-09、RI-06を前進。

認定ゲート順注記: 実験投入順は情報利得順（Step 1a → 1b → 2a → 2b → 2c → 3）だが、最終的なVQ認定はVQ-1 → VQ-2 → VQ-3 → VQ-4のゲート順で確定する。

---

### §6 制度設計への寄与

**1. PRI-11（Mechanism-kinetics decoupling）の第3独立確認事例**

本論文は、提案触媒サイクル（Figure 8B）から速度式を代数的に導出せずに、観測された見かけ二次の触媒依存性との「一致」のみでdmpe系の二核TM機構を支持するという、PRI-11の典型例を提供する。具体的には、Figure 8Bが定常状態近似の下でd[3aa]/dt ∝ [I-a][III-b]という形の速度式を与えるかどうか——そしてそれが[Ni_total]²依存性を生むかどうか——という代数的検証が欠如している。Breitenfeld 2014（PRI-11提案）、Pengfei 2024（同型確認）に続く3報目の確認であり、PRI-11の正式昇格（暫定→正式RIコード）を支持する材料となる。

定義の精緻化提案: PRI-11の定義「提案触媒サイクルから速度式を代数的に導出せずに、観測速度次数との一致のみで機構を支持」に、次の限定条件を追加することを提案する：「複数の触媒サイクルモデルが同一の観測次数パターンを予測しうる場合（等速度論的多機構）に特に適用する」。本ケースでは、Ni二量化平衡を含む代替機構も[Ni]²依存性を生みうるため、PRI-11が最も深刻な形で現れている。

**2. 標識不整合（Labeling mismatch）パターンの検出**

本論文はAbstractで「[REDACTED: verbatim source text; see the source paper via its DOI]」（"we establish"という事実的叙述語と"likely"という仮説標識の混在）と述べ、Conclusions（p.15047）でも同一パターンを継続している。一方、Results & Discussion（p.15046-7）では「we propose that」「I-a also intervenes」「corroborated by independent supporting organometallic investigations」という言語を使用し、仮説性を明示している。

この構造は層C（dmpe系）の証拠的弱体化を本文内で著者が自己認識していることを示す。AbstractとConclusionsでの"we establish"（叙述語）と"likely"（仮説標識）の共存は、著者が確信度を節の種類（主張節 vs. 証拠節）によって使い分けていることを示す典型例であり、仮説標識の位置が末尾修飾に集約されているパターンとして記録する価値がある。PRI-11と連動：証拠的基盤が弱い機構的主張において事実的叙述語が使用されるパターンは、RI-04とPRI-11の共起と対応している。

**3. 否定的証拠の不完全性パターン（v0.2aガイドライン適用）**

本論文のラジカルクロック実験（Figure 6A）は、陰性の実験結果（12/13の非検出）を肯定的機構証拠として使用する際に、（1）**質量収支の閉鎖**（12/13が形成されないなら全炭素が3agに収束することの定量的確認）と（2）**速度論的ウィンドウ評価**（基質1gのシクロプロピルカルビニルプローブのk_cyclと推定カップリング速度の比較）が欠けているパターンを示す。「excellent conversion」という記述は質量収支の閉鎖を示唆するが数値がない（B14類似の問題）。またFigure 6BのTEMPO捕捉実験でも、TEMPOがNi配位子として機能しうる（ref 16を自己引用）という開示が機構的排除の根拠を揺るがしている。

EP-04a [Discrimination/replication pack] のcase-specific実装として記録すべき標準チェックリスト: (a) 質量収支の百分率報告、(b) ラジカルクロック速度定数k_cyclの文献値引用と速度論的ウィンドウの数値化、(c) TEMPOが有効なラジカルトラップとして機能したことの陽性対照（TEMPOが既知ラジカル系で効果を示す条件と本反応条件の比較）。

**4. SRG-1: VTNAに特化したEP-04a実装ガイドラインの継続強化**

SRG-1（6 B項目: B1–B6）に示されるVTNA法の複合的脆弱性（IRバンド未特定・レプリケートなし・GOF基準なし・触媒分解未補正・グリニャール凝集）は、VTNAを採用する機構論文群に系統的に観察されるパターンである。v0.2aでのRI-04 + RI-08共起パターン記述と組み合わせて、VTNA採用論文向けの標準報告チェックリスト（報告必須項目: 監視IRバンド・波数・セル長、内部標準物質の同定、条件内レプリケート数n≥3、GOF指標（Σ残差²またはAIC）、触媒分解の補正有無と補正法、グリニャール凝集の排除実験）をStage 3テンプレートに追加することを提案する。

本ケースはVQ-3未達だが、dppe系単独ではVQ-3 (Qualified)に到達するという二系統間の非対称性を示した初めての例として記録し続ける。「単一論文内での層別VQ判定」の代表事例として、v0.2aでの制度設計参照事例に追加することを推奨する。
```
