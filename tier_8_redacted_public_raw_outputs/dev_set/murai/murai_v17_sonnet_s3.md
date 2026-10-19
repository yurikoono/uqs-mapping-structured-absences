prompt_version: stage3-v1-20260402
model_info: claude-sonnet-4-6

# 科学的知見の再認定判定票

## Murai et al. 1993（Nature, communication）

---

### §1 Claim Architecture

**コア主張の要約：**

本論文は、RuH₂(CO)(PPh₃)₃を触媒として用い、キレーション支援によって芳香族C–H結合をオレフィンに付加する反応を初めて実用的な催触サイクルとして実証したと主張する。

Novelty柱（先行研究との差異を構成する主張）：
- **Novelty-1（効率性）**: 「両原料に基づきほぼ定量的な収率が得られた——これは触媒的C–H結合官能化において前例がない」
- **Novelty-2（選択性）**: 「4種の可能な位置異性体のうち1種のみが生成し、位置選択性は事実上100%」
- **Novelty-3（汎用性）**: アシルベンゼン・アシルヘテロ芳香族・多様な末端オレフィンに適用可能

Utility柱（実用的価値の主張）：
- 「実用的有機合成に要求される効率・選択性・汎用性を達成した」
- 「アルキル化芳香族化合物の新たな範囲を利用可能にする」

**Layered structureの判定：**

Layered structure あり。効率性（runs 8–13の定量的収率）、選択性（runs 8・13のarene選択性、全runs のolefin選択性）、汎用性（Table 1全体の基質スコープ）はそれぞれ異なるrunで独立に証拠立てられており、いずれか1つの反証が他の主張を自動的に崩す構造にはなっていない。

ただし、3主張の定量的根拠はすべてGC収率という単一の証拠形式に集約されており、そのGC収率の信頼性（SRG-2）が揺らぐと3主張が同時に動揺する構造的脆弱性をもつ。さらに機構鍵主張（キレーション支援）は選択性主張（B-8）の根拠として機能しており、機構の「不明」宣言（B-3）が選択性の説明責任を事実上免除するピボット構造が存在する。

---

### §2 SRG / CLA → RI / ER / EP Crosswalk

---

**SRG-1 [機構実験の完全不在]**（B-3, B-14, B-18, U-1, U-2）

* **Primary RI**: RI-03 Unobserved explanatory
* **Secondary RI**: RI-06 Imported model
* **ER**: 提案された触媒サイクル（Ru(II)→Ru(0)前活性化、C–H酸化的付加、M–H/M–C挿入、還元的脱離）の各中間体のうち少なくとも1種を速度論的または分光学的に拘束し、類似系からの輸入モデルを本系で検証すること。
* **EP**: EP-03a Direct-observation / state-assignment pack; EP-06a Analogy-validation pack
* **Case-specific実装**: ① RuH₂(CO)(PPh₃)₃をアセトフェノン存在下で加熱したときのH₂放出・³¹P NMR変化の追跡によるRu(0)生成確認。② 重水素標識アセトフェノン（芳香環ortho-d）を用いたKIE測定によるC–H切断の律速性判定。③ M–H対M–C挿入経路を区別するための重水素標識オレフィン（CH₂=CDCH₃等）の投入。④ Ru(0)/Ru(II)の電位・配位圏を固定した化学量論モデル反応によるRI-06解消。
* **注記**: B-3はhigh_convergence_low_gap（V1=high, V2=critical, convergence=2/3）。U-1（Ru(II)→Ru(0)の自己矛盾的不在）とU-2（β-水素脱離抑制の自己矛盾的不在）がSRG-1に統合されており、論文自身の機構モデルが予測するデータ（H₂、異性化オレフィン）が報告されていない点がself-contradictory absence として最高優先度を付与。

---

**SRG-2 [定量的実証の信頼性欠如]**（B-1, B-4, B-5, B-9, B-15）

* **Primary RI**: RI-01 Reporting integrity
* **Secondary RI**: RI-08 Unquantified reliability
* **ER**: GC収率の校正プロトコル（内標準・応答係数）の明示、13例中少なくとも代表的3例の再現実験によるsd記載、全run対象のマスバランス集計（回収出発物・副生成物）。
* **EP**: EP-01a Reporting-coherence pack; EP-08a Replication / uncertainty pack
* **Case-specific実装**: ① ビフェニルまたは類似安定化合物を内標準としてGC校正曲線を作成し、新規生成物の応答係数を独立に測定。② runs 1, 9, 10（TOF根拠run）を3重複で再実施しSD提示。③ runs 1–3, 5–6のマスバランス回収をGCで定量し、残留オレフィン・異性化副生成物の有無を明示。
* **注記**: B-1はhigh_convergence_low_gap中で唯一convergence=3/3（V1=high, V2=medium, V3=high）。フォールバック規則(b)最優先候補。RI-01はVQ-2の致命的未解消項目。

---

**SRG-3 [選択性の定性的帰因]**（B-6, B-7, B-8, B-19）

* **Primary RI**: RI-05 Qualitative overread
* **Secondary RI**: RI-04 Unreplicated discriminator
* **ER**: 位置選択性（arene ortho対比、olefin anti-Markovnikov）・生成物比（run 9の1:1比）の各観察について、速度論的対熱力学的制御を判別する実験（温度変化、反応時間依存性）または競合基質実験を実施すること。
* **EP**: EP-05a Quantitative-ranking substantiation pack; EP-04a Discrimination / replication pack
* **Case-specific実装**: ① 電子的に対称なアリールケトン（para置換体のみ）を用いたortho選択性の定量的確認（立体起源か電子起源かの分離）。② run 9のアクリル酸エチル濃度変化によるkobs測定（速度論的選択性の傍証）。③ 1-インダノンの不反応確認：同条件・延長反応時間（90 h）でGC定量を実施し「検出下限以下」と「真にゼロ」を区別。④ 6員環形成に必要なtether長境界を固定するためのフェニル酢酸メチル（5員環）・フェニルプロピルケトン（7員環）の比較実験。
* **注記**: B-7（V2=high）、B-8（V2=high）はhigh_convergence_low_gap。RI-05が実質的に未解消の場合、VQ-3はqualified止まり（注1）。

---

**SRG-4 [触媒構造–活性データの定性限定]**（B-10, B-18）

* **Primary RI**: RI-05 Qualitative overread
* **Secondary RI**: RI-01 Reporting integrity
* **ER**: 比較触媒スクリーニングについて、少なくとも同一基質・同一条件での収率またはTOF値を数値で示すこと。
* **EP**: EP-05a Quantitative-ranking substantiation pack; EP-01a Reporting-coherence pack
* **Case-specific実装**: Ru(CO)₂(PPh₃)₃・RuH₂(PPh₃)₄・Ru(CO)₃(PPh₃)₂・RuHCl(CO)(PPh₃)₃について、アセトフェノン/アクリル酸エチルrun（run 9条件）でのGC収率をすべて同一実験者が同一日に取得し、相対的活性を数値化。
* **注記**: SRG-4は2項目のみで優先度は中程度。触媒活性化機構（SRG-1のU-1）と連動するため、SRG-1解消後に意味が増す。

---

**SRG-5 [優位性主張の数値的未閉鎖]**（B-9, C-2）

* **Primary RI**: RI-09 External superiority
* **Secondary RI**: RI-08 Unquantified reliability
* **ER**: runs 1, 9, 10について単位時間あたりのTON（TOF）を実験エンドポイントの明示とともに算出し、Jordan & Taylor (1989) および Moore et al. (1992) の文献値と同一軸（基質・温度・Ru mol%相当換算）で比較する数値表を提示すること。
* **EP**: EP-09a Internal benchmark pack; EP-08a Replication / uncertainty pack
* **Case-specific実装**: ① runs 1, 9, 10の反応時間中間点でサンプリングし、GC時間コースからTOF(h⁻¹)を計算。② Jordan & Taylor (1989) の113 h⁻¹ / Moore et al. (1992) の文献TOF値を本反応条件（135°C）相当に補正し内部比較表を作成。③ SRG-2のRI-01解消後に初めて計算値が意味を持つことを注記（依存関係）。
* **注記**: C-2はDropped Quantitative Benchmarkとして識別済み（GAP-1, GAP-2 pending）。SRG-5はSRG-2の解消なしには部分解消に留まる（RI-08依存）。

---

**SRG外：CLA**

**CLA-1: キレーション支援の構造的境界（D-4候補7）**（B-17, A-1）

* **Primary RI**: RI-07 Unsupported boundary
* **Secondary RI**: なし
* **ER**: 「より広く適用可能」（A-1）と「キレーション支援が成功の鍵」（B-17）の両主張を整合させるために、5員・6員金属環を形成する基質（アセトフェノン系→○、フェニルプロピルケトン系→予測×）による境界実験を実施すること。
* **EP**: EP-07a Boundary-test pack
* **Case-specific実装**: フェニルプロピルケトン（7員前駆体）およびフェノキシエタノール誘導体（チレーター変換）をrun 9標準条件に投じ、反応性の有無とGC収率を比較。1-インダノン（B-6）、テトラロン（run 11）、アセトフェノン（主基質）の三者比較により環サイズ依存性を確定。
* **注記**: D-1のNovelyty-3（汎用性）主張のスコープ境界に直接関わる。TEMPERATURE_SUMMARY上の直接対応なし。A-1との連動で高重要度。

**CLA-2: 合成標的との接続（D-4候補8）**（A-1）

* **Primary RI**: RI-07 Unsupported boundary
* **Secondary RI**: なし
* **ER**: 「新たなアルキル化芳香族化合物の範囲を利用可能にする」（A-1）という実用価値主張を実質化するために、少なくとも1例の既知天然物・医薬品中間体・機能性材料の合成への適用例を示すこと。
* **EP**: EP-07a Boundary-test pack
* **Case-specific実装**: 例えばイブプロフェン前駆体フェニルエチルケトン系への適用試験、または既知液晶材料を標的とした合成経路の設計。
* **注記**: D-1のUtility柱（「practical organic synthesis」）に直結。独立CLA。優先度は低（後続論文群が対応する標的合成を示している可能性が高い）。

---

### §3 現在のVQ判定

**現在判定: VQ-1 (Observation)**

---

**VQ-1 [Observation]: 通る（RI-02: Non-fatal残存）**

RI-02（Object identification）の状態：B-2で「標準法により構造を確実に確定した」「分析純粋」と記述されるが、具体的な分析手法・純度基準・スペクトルデータは一切示されていない。ただし生成物はすべて化学的に明確に定義された構造（既知クラスの芳香族ケトン誘導体）であり、構造の帰属自体に文献上の異議は生じていない。これはreporting gapであり構造同定の失敗ではないため、RI-02はNon-fatalと判定し、VQ-1は通過とする。

---

**VQ-2 [Method]: 未達（RI-01 Fatal, RI-07 partially Fatal）**

VQ-1継承を前提とする。

RI-01（Reporting integrity）：GC収率の校正プロトコルが完全に不在であり（SRG-2）、13例中9例は単離収率なし、全例で再現なし。一次定量証拠の測定枠が独立検証不可能な形式で報告されており、これは主張の方法論的成立を根底から制限する。Fatal判定。

RI-07（Unsupported boundary）：B-16（不活性ガス雰囲気・溶媒乾燥の記載なし）は、低原子価Ruを用いる有機金属反応の独立再現に必要な条件記述を欠いており、この省略単独で再現性を担保できない。Partially Fatal（大気安定な高温反応の可能性も排除されないため原理的には非致命的だが、独立再現への障壁として機能する）。

→ RI-01のFatal残存によりVQ-2は未達。

---

**VQ-3 [Mechanism]: 未達（VQ-2継承 + RI-03 Fatal, RI-04 Fatal, RI-05重大残存）**

VQ-2が未達のためVQ-3も未達。独立判定を以下に記す。

RI-03（Unobserved explanatory）：提案された活性種Ru(0)、シクロメタル化中間体（Fig. 1）、M–HまたはM–C挿入中間体のいずれも直接観測されず、速度論的拘束もない（SRG-1）。Fatal。

RI-04（Unreplicated discriminator）：M–H対M–C挿入経路を区別する実験が皆無であり（B-3）、2経路が並置されたまま判定を保留している。Fatal。

RI-05（Qualitative overread）：位置選択性・生成物比・インダノン不反応をすべて構造的直観（環歪み、立体閉塞、キレーション幾何）に帰因させており（SRG-3）、定量的実験的根拠なし。重大残存。RI-05が重大に残るためVQ-3は原理上 Qualified（限定的）にも届かない。

---

**VQ-4 [Benchmark]: 未達（VQ-3継承 + RI-08 Fatal, RI-09 Fatal）**

VQ-3が未達のためVQ-4も未達。独立判定を以下に記す。

RI-09（External superiority）：「最高水準のTOF」を主張するが（B-9）、TOF値自体が算出されておらず、Jordan & Taylor (1989) / Moore et al. (1992) の数値も本文に再掲されていない（SRG-5）。Fatal。

RI-08（Unquantified reliability）：比較基準となる自らの定量データに不確かさ記述がなく（B-15）、外部比較への前提が成立していない。Fatal。

---

### §4 Era-Norm Annotation

**communication-era tolerated:**

以下の項目は、1993年のNature communication（3ページ）というgenre conventionの範囲内で当時許容されたと判断する：

- **B-1**（GC校正記述なし）: 1990年代初頭の有機合成communications ではGC収率の校正省略は標準的であった。応答係数の明示要求は2000年代以降に標準化された。
- **B-2**（「standard methods」による特性評価）: 3ページ形式では化合物毎のスペクトルデータ掲載スペースがなく、supporting information が制度化される以前であり、簡略記述は許容されていた。
- **B-15**（再現なし）: 発見報告communicationsに再現実験を課す規範は1990年代には存在せず、単一回の数値報告が慣行であった。
- **B-16**（雰囲気記述なし）: 条件の簡略化はcommunication形式の暗黙了解であり、有機金属反応でも雰囲気省略が見られた。
- **B-3**（機構「不明」の一段落記述）: 機構を未確定のまま認め、詳細を後続論文に委ねるスタイルは優先権確立型communicationsの標準形式であった。

**modern-era deficient:**

以下の項目は現代の再認定水準では許容できない欠落と判定する：

- **B-1**（GC校正プロトコル不在）: 現在のNatureはSupplementary Information必須であり、校正データ・応答係数・内標準の明記が要求される。新規化合物のGC収率のみの主張は現代では査読通過しない。
- **B-15**（再現なし）: 現代の有機合成論文では代表的収率の再現実験が標準要件であり、±5–10% SDの提示が期待される。
- **B-16**（雰囲気・溶媒乾燥記述なし）: Ru(0)系の低原子価反応の再現条件として雰囲気・乾燥条件は現代では必須記述。
- **U-1**（Ru(II)前駆体からRu(0)活性種への変換未検証）: 自己矛盾的不在として現代査読では指摘が避けられない。前活性化に関する最低限の証拠（H₂ガス発生、³¹P NMRの変化）の提示が要求されるはずである。
- **U-2**（β-水素脱離抑制の未説明）: 提案機構の内的一貫性に関わるself-contradictory absenceとして、現代の機構的考察に必須の記述。
- **B-9**（TOF数値の不記載）: 「最高水準」という比較優位性主張に対し、いかなる数値的根拠も示さない報告は現代では成立しない。

**両タグ該当（当時は許容・現代では不足）：**
B-1, B-15, B-16 は上記の両カテゴリに記載済み。当時のgenre conventionの範囲内だったが、現代基準でのVQ再認定においてはfatalまたはpartially fatalとして機能する。

---

### §5 最短補強ルート

**現在VQ: VQ-1 → 第一目的関数: VQ-2 / 第二目的関数: VQ-4（VQ-3前提）**

---

**VQ-2 への最短ルート：**

1. **EP-01a** Reporting-coherence pack — アセトフェノン/アクリル酸エチル系でビフェニル内標準・応答係数校正を用いたGC法を確立し、Table 1全13例を定量的に再実施する。**RI-01を解消。**

2. **EP-07a** Boundary-test pack — 不活性ガス（N₂またはAr）封管条件および乾燥溶媒使用の明示により再現性を確立する（1日の実験追加のみ）。**RI-07（B-16）を解消。**

3. **EP-08a** Replication / uncertainty pack — runs 1, 9, 10を3重複実施し収率のSDを算出。TOF計算の入力値として使用。**RI-08を前進（SRG-2）。**

認定ゲート順注記：実験投入順は情報利得順（EP-01a優先）だが、最終認定は VQ-1 → VQ-2 → VQ-3 → VQ-4 のゲート順で確定する。

---

**VQ-3 への最短ルート（VQ-2達成後）：**

1. **EP-03a** Direct-observation / state-assignment pack — RuH₂(CO)(PPh₃)₃の135°C加熱時のH₂発生を容量法で確認し、³¹P NMRで前駆体消費を追跡してRu(0)生成を帰属する。さらにアセトフェノン/Ru系の停止反応で中間体をNMRまたはESI-MSで観測試行。**RI-03を前進（U-1、SRG-1）。**

2. **EP-04a** Discrimination / replication pack — ortho-d₁-アセトフェノンをrun 9条件に投じてKIEを測定（C–H対C–D挿入の律速確認）。CH₂=CDCH₃（crotyl-d₁類似）でM–H/M–C経路を区別するラベル実験を設計。**RI-04を前進（B-3）。**

3. **EP-05a** Quantitative-ranking substantiation pack — 電子的に対称なaryl基質でortho選択性の温度依存性を測定し（VT-GC）、速度論的対熱力学的制御を判別。run 9条件のアクリル酸エチル濃度変化kobs実験で挿入step選択性の速度論パラメータを取得。**RI-05を前進（SRG-3）。**（RI-05の完全解消はVQ-3 qualifiedの回避に必要）

4. **EP-06a** Analogy-validation pack — Ru(CO)₂(PPh₃)₃またはRu(PPh₃)₃による化学量論モデル反応（アセトフェノン + RuH₂系）を室温でNMR追跡し、cyclometallated intermediateの単離または分光的同定を試みる。**RI-06を前進（SRG-1）。**

認定ゲート順注記：EP-03a/04a/05a/06aは情報利得上は並行投入可能だが、VQ-3認定のためにはRI-03・RI-04・RI-06の三者を同時解消する必要がある（継承原則）。RI-05重大残存下では VQ-3 (qualified) 止まり。

---

**VQ-4 への最短ルート（VQ-3達成後）：**

1. **EP-09a** Internal benchmark pack — Jordan & Taylor (1989) のZr系条件（α-ピコリン/プロペン）をrun 9相当温度に補正した等価TOF計算表を作成し、Ru系の測定TOF（EP-08a由来）と同一軸で比較する。Moore et al. (1992) のRu/pyridine/CO系についても同様。**RI-09を解消（SRG-5）。**

2. **EP-08a**（完全版） — 全13例の3重複によるSD付きデータセット完成。RI-08を完全解消（SRG-2 + SRG-5）。

認定ゲート順注記：VQ-4認定にはVQ-3の完全達成（RI-05の実質解消を含む）が前提。EP-09aは独立実施可能だが、VQ-4認定としては VQ-3 gate の通過後に初めて有効となる。

---

### §6 制度設計への寄与

**1. RI-03 + RI-06 の共起パターンの代表事例**

SRG-1（B-3, B-14, U-1, U-2）は、RI-03（Unobserved explanatory）とRI-06（Imported model）が高優先度の発見論文に同時に現れる典型事例を提供する。提案された触媒サイクルの中核種（Ru(0)、シクロメタル化中間体）が直接観測されないまま、類似系からの類推で構築されるという構造は、有機金属触媒発見communicationに繰り返し現れるパターンである。RI-03/RI-06の共起はSRGレベルで記録しておくと、Stage 2Fにおけるrecurring_root識別に利用できる。

**2. Self-contradictory absence の制度的認識**

U-1・U-2は「論文自身が提案する機構モデルがその存在を予測する中間体・副生成物が報告されていない」という自己矛盾的不在（self-contradictory absence）の定義事例を提供する。これは通常のreporting_omission（B項目）と区別して高優先度を付与するロジックの実証として、Codebookの注記（RI-03の適用例）に追記すべき価値がある。

**3. VQ-1/VQ-2境界のera-norm依存性の較正点**

本論文はVQ-1（通過、RI-02 Non-fatal）とVQ-2（未達、RI-01 Fatal）の境界に位置する。RI-02が非致命的で通過できる理由は「生成物の化学的同一性自体は争われていないが、報告方法が不十分」というera-normに依存する。RI-01がFatalになるのは測定方法論そのものの不在による。この境界条件は将来の判定において「RI-02の致命性はcommunication formatと生成物の新規性水準に依存する」という注記をVQ判定基準マトリクスに追加する根拠となる。

**4. 層状主張構造とSRG-2 single point of failureのパターン**

D-1の layered structure（3主張が独立に証拠立てられる）と、SRG-2（GC収率という単一証拠形式に3主張が依存する）の共存は、「独立に見える主張が実際には共通の測定インフラに依存している」というパターンを記録する。このパターンは §2 crosswalk で SRG-primary RI が RI-01 になる場合に再現しやすく、Claim Architecture（§1）でlayered_structureと同時にsingle-point-of-failure分析を記述する項目を追加する提案の根拠となる。

**5. 新規PRI候補の不在を確認**

PRI-10（Kinetic overclaim）は本論文には適用されない（TOFを「最高水準」と述べるものの、絶対的速度向上値を数値で主張していない——むしろ値不記載がRI-09を構成している）。新たなPRI候補となるパターンも本ケースでは検出されない。本ケースは既存の制度設計（RI-01~RI-09, VQ-1~4, EP-01a~09a）で完全に記述可能であり、Codebook v0.2の十分性を有機金属触媒communicationのクラスにおいて追加確認した。

inference_time_sec: not available — inject externally
