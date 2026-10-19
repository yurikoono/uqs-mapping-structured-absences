# Stage 3: 科学的知見の再認定判定票（Assessment Sheet）生成
<!-- prompt_version: stage3-v3-20260425 -->
**Language: 日本語（RI/EP/VQコード・技術用語は英語）**

出力の冒頭にプロンプトバージョンを記載すること：
```
prompt_version: stage3-v3-20260425
```

---

## 入力

以下を本プロンプトの前に貼り付けること：
1. **Stage 0出力**（BIB-1〜BIB-8b, S0-1〜S0-7）
2. **Stage 1 Turn 4出力**（A, B, C, U, META, TEMPERATURE_SUMMARY, GAP）
3. **Stage 2出力**（D-1〜E, confirmed_english）
4. **Stage 2F出力**（任意。グループモードで使用。貼り付けがない場合は単報モードで実行）

---

## 出力規律

以下の§1〜§6の構成に従い、構造化された判定票のみを出力すること。
説明的散文、フォローアップ質問、次ステップの提案、指定フィールド外の
テキストを付加しない。

**基本姿勢：** 過去の著者への「批判」ではなく、現代側からの「アップグレード
設計図」として記述すること。「〜すべきだった」ではなく「〜を投入すれば
VQ-Xに到達できる」という形式を用いる。

---

## 参照体系

### Root-Issue Codebook v0.2

| Code | Label | Definition |
|:-----|:------|:-----------|
| **RI-01** | Reporting integrity | 測定フレーム・条件記述・報告単位の不統一による横比較不能 |
| **RI-02** | Object identification | 生成物や触媒の構造・純度が代替候補を排除できる粒度で未確定 |
| **RI-03** | Unobserved explanatory | 説明の中核を担う種・状態が直接観測も速度論的拘束もされていない |
| **RI-04** | Unreplicated discriminator | 識別力の高い単一データに分析精度や代替経路排除なく高位解釈 |
| **RI-05** | Qualitative overread | 数値なき定性的順位から構造的・因果的含意を導出 |
| **RI-06** | Imported model | 他系モデルを対象系での同型性実証なしに輸入 |
| **RI-07** | Unsupported boundary | 失敗例なしに「〜のみ可能」と限界を主張 |
| **RI-08** | Unquantified reliability | 比較データに反復測定や不確かさ記述なし |
| **RI-09** | External superiority | 直接比較なしに外部文献値のみで優位性を主張 |
| **PRI-10** | Kinetic overclaim | 動力学データなしに絶対的速度向上を主張（暫定コード） |
| **PRI-11** | Mechanism-kinetics decoupling | 提案触媒サイクルから速度式を代数的に導出せずに、観測速度次数との一致のみで機構を支持（暫定コード） |
| **PRI-12** | Structural validation deficiency | 検証の構造的不全（v18新規昇格、二階層構造、詳細は本節末尾） |

**Codebook運用注記（v0.3、v18更新）：**

以下は8報以上の分析で繰り返し確認されたパターンであり、各RIの適用時に
参照すること。

- **RI-03 サブタイプ: Available-but-unutilized characterization** —
  取得済みの実験データ（X線構造、NMRスペクトル等）が機構的主張の
  検証に活用可能であるにもかかわらず、その含意が論文本文で抽出
  されていない。「未観測」ではなく「観測済みだが未活用」のケース。
- **RI-06 スコープ注記: サイクルレベル輸入** — 個別の素反応ステップ
  の類推ではなく、触媒サイクル全体を別系から構成する大規模モデル
  輸入にもRI-06を適用する。
<!-- v18 C3: methodology paper exemption note for RI-06 -->
- **RI-06 判定注記（v18追加）：方法論論文の分野標準慣行** — 方法論
  論文において先行手法の評価指標を参照することは分野標準慣行であり、
  RI-06の対象外となる場合がある。RI-06を適用する条件は以下の両方を
  満たす場合に限る：
    (a) 参照先の評価指標が対象論文の研究対象と異なる系・条件・モデル
        に由来する、かつ
    (b) その移転の妥当性が論文内で議論されていない
  単に「この種の論文では従来から使われている指標を引用した」場合は
  RI-06適用外。判定で迷う場合は「分野標準慣行であり、RI-06の閾値
  には達しない」と明記して見送る。
- **RI-07 拡張適用: 否定的境界主張** — 「〜のみ有効」という肯定的
  境界だけでなく、「〜が最も深刻な限界」という否定的境界主張を
  データなしに行う場合にもRI-07を適用する。
- **RI-08 サブタイプ: 内部矛盾型** — 同一サンプルから計算される
  2つの量（例：収率と転化率）が数学的矛盾を示す場合、反復測定の
  欠如だけでなく測定一貫性の不在としてRI-08を適用する。
<!-- v18 C5: split-presentation structure note for RI-09 -->
- **RI-09 拡張適用（v18追加）：分割提示構造（Paper I/II）** — 論文が
  「Paper I（理論・定式化）」として自己位置付けし、数値実証を「Paper II」
  などの続報に委譲する構造を持つ場合の扱い：
    (a) Paper II が既刊で参照可能な場合 → 結合してVQ判定
    (b) Paper II が予告のみ・未刊の場合 → Paper I 単独で VQ-2 (Method)
        上限とし、RI-09 を「数値ベンチマーク委譲（split-presentation）」
        として明示的に記録
  これはVQ階層逆転の変形（理論的定式化が先行し、数値実証が後続論文に
  先送りされる）であり、§6で「VQ非対称性パターン」として記述すること。

**PRI昇格基準：** 独立2報で同型確認、またはStage 2Fのrecurring_patternで
cross-case recurrence確認。既存RIに収まらない新パターンが検出された場合、
§6で「PRI-NN候補」として提案すること。

**PRI昇格状態（v0.3、v18時点）：**
- PRI-10（Kinetic overclaim）: 暫定。Monnereau 2009で確認。昇格に追加1報必要。
- PRI-11（Mechanism-kinetics decoupling）: 暫定。Breitenfeld 2014で提案、
  Pengfei 2024で同型パターン確認。2報の独立確認を満たしており昇格候補。
  定義：「提案触媒サイクルまたは反応機構から速度式を代数的に導出せずに、
  観測速度次数との一致のみで機構を支持している」。
- **PRI-12（Structural validation deficiency）: 正式昇格（2026-04-25）**。
  Nakanishi 2025引用文献群27報で23報（85%）に独立浮上。二階層構造を
  下記に登録。

<!-- v18 C2: PRI-12 two-cluster registration -->
**PRI-12: Structural validation deficiency（検証の構造的不全）— 二階層構造**

PRI-12は二つの上位クラスターからなる。

**クラスター A: Self-referential validation（自己参照的検証）**

定義：提案された計算量・指標・理論の妥当性検証において、独立した
外部基準が欠如し、検証が自己参照的構造を持つ。

適用対象：現代の計算化学・物理化学方法論論文。新しい記述子・指標・
スコア関数を提案する論文に頻出。

サブタイプ（適用時に該当するものを付記）：
- **A1: Descriptor-Causality overclaim** — 記述子（特定の量や指標）から
  因果性主張を導出するが、独立した因果検証が欠如
- **A2: Circular validation design** — 検証標準と検証目標が同一の数学的
  構成物に依存
- **A3: Construct-validity circularity** — 構成概念の操作的定義が循環
  （例：軌道局在性をIAO電荷で定義し、IAO電荷の妥当性を軌道局在性で
  検証）
- **A4: Epistemological closure claim** — 後付けの数学的対象が経験則と
  一致することを物理的実在性の証明として提示
- **A5: Multi-layer approximation stacking** — 複数の近似（IRC近似×
  軌道エネルギー近似×汎関数近似など）が累積するが、各層の独立検証
  なし
- **A6: Parameter portability overclaim** — 限定された系で校正された
  パラメータの異種ドメインへの無根拠転用
- **A7: Stochastic completeness overclaim** — 確率的探索手法で「全解
  発見」を主張するが、収束統計や網羅性の定量根拠なし
- **A8: Boundary-adjacent application without diagnostic** — 適用限界
  境界付近で診断（スピン純度、収束、安定性）を省略

**クラスター B: Deductive-retrospective circularity（演繹的遡及構造）**

定義：演繹的に導出された選択則・原理の「検証」が事後的な文献一致に
依存し、理論予測が先行し実験検証が後から（しかも著者自身が選定した
事例で）行われる。

適用対象：歴史的基礎理論論文、形式的理論提案論文（W-H 1965、Fukui
1952/1970、McWeeny 1960等）。1960年代の形式的理論論文に顕著で、
現代計算化学論文には見られない。

サブタイプ（適用時に該当するものを付記）：
- **B1: Composite model import** — 複数の理論モデル（光化学モデル＋
  二原子分子モデル等）を同一機構の説明に重層し、それぞれの妥当性
  検証なし（RI-06の歴史的論文向けサブタイプ）
- **B2: Retrospective Confirmation Bias** — 演繹的主張の後で、一致する
  既存文献を「確認」として遡及的に引用
- **B3: Axiomatic framework overclaim** — 少数の事例から派生した原理を
  全クラス・全反応に拡張適用
- **B4: Retroductive-foundation mismatch** — 演繹（原理から事例へ）と
  遡及（事例から原理へ）の論理的方向の混同
- **B5: Definitional closure protection** — 反証事例が現れた場合に
  再分類ルールにより反証不可能化する構造（「違反は違反ではない」）
- **B6: Algorithm convergence opacity** — 数学的収束保証なしのアルゴリズム
  適用主張（収束の証明や条件提示なし）

**PRI-12適用時の記載要件：**
1. クラスター（AまたはB）を明示
2. サブタイプID（A1〜A8、B1〜B6）を付記
3. 該当する既存RI（典型的にはRI-01、RI-06、RI-07）との関係を1文で
4. クラスターA・B両方に該当する場合は両方を記載（稀だが、複合パターン
   が存在し得る）
5. クラスター・サブタイプいずれにも収まらないがPRI-12の核となる定義
   （独立外部基準の欠如または演繹遡及循環）を満たす場合は、
   `PRI-12: cluster_other / subtype: [新規記述]` として記録し、§6で
   新サブタイプ提案として扱う

### VQ判定基準マトリクス

| 水準 | ラベル | 必須解消項目 |
|:-----|:-------|:-------------|
| **VQ-1** | Observation | RI-02 |
| **VQ-2** | Method | RI-01, RI-07（+ VQ-1継承） |
| **VQ-3** | Mechanism | RI-03, RI-04, RI-06（+ VQ-2継承）*注1 |
| **VQ-4** | Benchmark | RI-08, RI-09（+ VQ-3継承） |

**継承原則：** 上位VQは下位の全要件を継承する。
*注1: RI-05が重大に残る場合、VQ-3は「限定的（Qualified）」。

**致命性判定：**
- Fatal: 未解消なら当該VQ水準の主張が原理的に不成立。
- Non-fatal: 残存するが主張の成立を根底からは覆さない。
- Era-norm依存: 当時は非致命的だが現代基準では致命的。→ §4で記録。

### EP辞書（共通ラベル）

| EP Code | 共通ラベル |
|:--------|:-----------|
| **EP-01a** | Reporting-coherence pack |
| **EP-02a** | Identity / purity substantiation pack |
| **EP-03a** | Direct-observation / state-assignment pack |
| **EP-04a** | Discrimination / replication pack |
| **EP-05a** | Quantitative-ranking substantiation pack |
| **EP-06a** | Analogy-validation pack |
| **EP-07a** | Boundary-test pack |
| **EP-08a** | Replication / uncertainty pack |
| **EP-09a** | Internal benchmark pack |
| **EP-10a** | Kinetic verification pack（暫定） |

---

## 判定票の生成手順

### Step 1: §1 Claim Architecture

**入力：** Stage 2 D-1

以下を記述する：
- **コア主張**を1段落で要約。Novelty柱とUtility柱を明示。
- **Layered structure**の有無と構造。「単一の反証で全主張が崩れるか、
  それとも独立層か」を判定し、層間の依存関係があればそれも記述。

---

### Step 2: §2 SRG / CLA → RI / ER / EP Crosswalk

**入力：** Stage 1 Turn 4 META (same_root_groups) + Stage 2 D-4 candidates +
TEMPERATURE_SUMMARY

**手順：**

**2a. SRGの取得：**
Stage 1 Turn 4のsame_root_groupsをそのまま取得する。

**2b. CLA候補の同定：**
Stage 2 D-4候補のうち、いずれのSRGにも属さない候補を抽出する。
以下の条件を満たすものをCLA（Claim-level Adjunct）として記録する：
- D-1の主張の成否に直接関わる（タイトル・NC項目に直結）
- grounded_inに記載されたB/A項目がいずれのSRGのmember_itemsにも含まれない

**自己矛盾的不在のCLAチェック：**
Stage 1のU項目のうち、「論文が提案するモデル（触媒サイクル、反応機構等）が
予測する観測量が、論文自身のデータとして報告されていない」ケースを特に
検出する。このパターンは以下の形で現れる：
- 触媒サイクルがR-R（ホモカップリング）の生成を予測するが、R-R収率が
  未報告
- 提案された中間体が分光学的に観測可能であるはずだが、観測が未実施
- 速度式が導出可能であるはずだが、導出されていない
- DFT計算が実験値と比較可能な量を予測するが、比較が行われていない
これらが既存SRGに含まれない場合はCLAとして記録する。

<!-- v18 C8: Self-referential validation check (PRI-12 cluster A) -->
**Self-referential validation チェック（全論文で実施、v18新規）：**
論文の中核的検証構造に以下のいずれかが成立するか確認する：
(a) 検証指標と被検証対象が同一の数学的構成物に依存する
(b) 検証の成功基準が提案理論の前提と論理的に循環している
(c) 提案された記述子・指標・スコア関数の妥当性が、その記述子自身を
    用いた評価で確立されている（外部基準の欠如）
(d) 多層近似が累積するが、各層の独立検証が論文内で行われていない

→ 成立する場合：PRI-12 クラスターA（Self-referential validation）の
  該当サブタイプ（A1〜A8）を§2の Primary または Secondary RI に記録し、
  既存 RI-01・RI-06・RI-07 との関係を1文で付記する。CLA候補にも追加
  する（既存SRGに該当しない場合）。

<!-- v18 C4: Deductive-retrospective structure check (PRI-12 cluster B) -->
**Deductive-retrospective structure チェック（方法論・理論提案論文で実施、v18新規）：**
論文が「演繹的に導出された原理・選択則・形式的予測」を中心主張とする
場合、以下のいずれかが成立するか確認する：
(a) 論文の中心主張が演繹的導出であり、検証事例が著者自身による選定に
    限られる
(b) 反証条件が論文内で操作的に定義されておらず、事後的な再分類
    （違反例の「違反でない」化）によって反証を回避できる構造を持つ
(c) 理論提案が先行し、実験的検証を後続論文（予告のみの場合を含む）
    に委譲する
(d) 既存の文献事例との一致を「確認」として遡及的に引用するが、
    その事例が著者の選定であり、不一致事例の検討が省略されている

→ 成立する場合：
  - PRI-12 クラスターB（Deductive-retrospective circularity）の該当
    サブタイプ（B1〜B6）を§2の Primary または Secondary RI に記録
  - VQ-2 達成を慎重に評価する：RI-07（境界未定義）または RI-01
    （実証なし）の Fatal 判定を検討
  - VQ-1 止まり判定となる場合は §3 で「クラスター B により VQ-1 止まり」
    と主因を明示する
  - 歴史的基礎理論論文（一般に1970年以前）では本パターンが構造的に
    現れやすいため、§4の Era-Norm Annotation で「当時の理論論文の慣行」
    として併記すること

**2c. RIマッピング：**
各SRG/CLAについて、Codebook（上記）と照合し、以下のテンプレートで記録する：

```
**SRG-N [名称]**（またはCLA: [名称]）

* **Primary RI**: RI-XX [Label]
* **Secondary RI**: RI-YY [Label]（該当する場合。なければ省略）
* **ER**: [主張を採るための規範的要件。1–2文]
* **EP**: EP-XXa [共通ラベル]（; EP-YYa [共通ラベル]）
* **Case-specific実装**: [論文の具体的な化学に即した実験を記述]
* **注記**: [下位B/A/U項目のリスト。TEMPERATURE_SUMMARYでの位置
  （high_convergence_low_gap等）。convergence・gap情報]
```

**マッピングルール：**
- 1つのSRG/CLAに対し、Primary RIは1つ。最も構造的に重いRIを選ぶ。
- Secondary RIは必要に応じて列挙。EPはRI単位で引く。
- 1つのSRGが複数のRIに同程度に該当する場合、下位B項目の数が
  多い方をPrimaryとする。
- Case-specific実装は、論文の具体的な化学系（金属、配位子、基質、
  分析法）に即して記述する。同じEP-03aでもNi系とPd系では実装が異なる。

**Stage 2Fがある場合の追加処理（グループモード）：**
- Stage 2Fのrecurring_rootsと本論文のSRGを照合する。
  recurring_rootに対応するSRGがある場合、注記に
  「recurring_root: [記述], cross-case confirmed」と追記する。
- Stage 2Fのrecurring_Uに該当するU項目がある場合、CLA候補に追加する。

---

### Step 3: §3 現在のVQ判定

**入力：** §2のcrosswalk結果 + VQ判定基準マトリクス

**手順：**
VQ-1 → VQ-2 → VQ-3 → VQ-4の順に、各水準の通過/未達を判定する。

各水準について以下を記述：
- **通過の場合**: 「VQ-N [ラベル] は通る」＋根拠1–2文。
  致命性判定でNon-fatalとした項目があれば明記。
- **未達の場合**: 「VQ-N [ラベル] は未達」＋根拠1–2文。
  未解消RIを列挙。
- **Qualified（限定的）の場合**: RI-05等が残存する場合に使用。
  「VQ-N (qualified)」と記載し、限定の理由を1文で。

**継承原則の明示：** VQ-2以上の判定では、下位VQ要件の通過を前提として
明記する。例：「VQ-2はRI-02が非致命的であることを前提に成立している。」

**層別VQ非対称性の検出：** §1のLayered structureで独立層が同定された
場合、論文全体のVQ判定に加えて、独立層ごとのVQ水準を評価する。
ある層が論文全体より高いVQ水準に到達している場合、以下の形式で記録する：
「ただし**[層の名称]**単独では：[VQ-N到達の根拠]。」
この層別非対称性は、論文の主張のどの部分が最も堅牢で、どの部分が
最も脆弱かを示す分析的情報を持つ。

---

### Step 4: §4 Era-Norm Annotation

**入力：** Stage 2 D-2 (format_exploitation, timing_pressure) +
Stage 2 D-3 (journal_constraint, field_competition_state) +
Stage 0 (BIB-4 year, BIB-7 format)

**手順：**
VQとは別枠で以下の2タグに分類する：

- **communication-era tolerated**: 当該年代・雑誌・形式のgenre convention
  内で許容される欠落。該当するB/A項目を列挙し、なぜ当時は許容されたかを
  各1文で。
- **modern-era deficient**: 現代の再認定では許容できない欠落。該当する
  B/A項目を列挙し、なぜ現代では不足かを各1文で。

**判定基準：**
- Stage 2 D-3のjournal_constraintで挙げられた項目 → communication-era toleratedの候補。
- Stage 2 D-2のformat_exploitationで挙げられた項目のうち、VQ昇格の
  必須要件に直接抵触するもの → modern-era deficient。
- 両方に該当する項目（当時は許容されたが現代では不足）→ 両タグに記載し、
  その旨を注記。

---

### Step 5: §5 最短補強ルート

**入力：** §2のcrosswalk結果 + §3のVQ判定

**手順：**

**5a. 目的関数の設定：**
現在のVQ水準の次のVQ水準を第一目的関数とする。
例：現在VQ-2 → 第一目的関数はVQ-3。
VQ-4への到達も第二目的関数として記載する（VQ-3が前提）。

**5b. EP投入順序の設計：**
目的関数ごとに、以下の基準でEP投入順序を決定する：
- 情報利得の大きさ（最も多くのRIを同時に前進させるEPを先に）
- 実験的実行可能性（既存インフラで可能なEPを先に）

**5c. 認定ゲート順の明示：**
実験投入順とは別に、最終的なVQ認定は継承原則に従うことを明記する。
「実験投入順は情報利得順だが、認定は VQ-1 → VQ-2 → VQ-3 → VQ-4 の
ゲート順で確定する」と注記。

**出力形式：**
```
**VQ-N への最短ルート：**
1. EP-XXa [共通ラベル] — [case-specific実装の1文要約]。RI-XX を前進。
2. EP-YYa [共通ラベル] — [case-specific実装の1文要約]。RI-YY を前進。
...

認定ゲート順注記：[最終認定は継承原則に従う旨の1文]
```

---

### Step 6: §6 制度設計への寄与

**入力：** §2–§5の分析結果全体

この論文の分析がCodebook・VQ基準・EP辞書にもたらした知見を記述する。
以下の観点で検討する：

- 既存RIコードの新しい代表事例を提供したか
- 新しいPRI候補を提案すべきパターンが検出されたか
- VQ判定基準の境界条件（致命性、Era-norm）に関する新しい知見があったか
- EP辞書に新しいcase-specific実装例を追加すべきか
- Stage 2Fのrecurring_patternからRI昇格の判断材料が得られたか
  （グループモードの場合）

**特に以下のパターンを検出した場合は明示的に記録する：**

- **標識不整合（Labeling mismatch）**: 著者が仮説・限定を明記して
  いるにもかかわらず、本文の叙述語が事実的記述語（"reacts with",
  "forms", "is converted to"等）を使用しているパターン。RI-06と
  連動する場合が多い。仮説標識の位置（末尾1文に集約等）を記録する。
- **通信→Full Paper遷移の自動解消パターン**: RI-07やRI-01が
  通信形式の紙幅制約に起因し、Full Paper展開で自動解消される
  パターン。§4のEra-Norm AnnotationでA項目との対応を確認する。
- **RI共起パターン**: 2つ以上のRIが同一SRGで共起し、いずれか
  一方の解消だけでは不十分であるケース（例：RI-04 + RI-06の
  共起では両方の解消が必要）。共起の構造を記述する。
- **否定的証拠の不完全性**: 陰性の実験結果（ラジカルクロック、
  TEMPO捕捉等）を肯定的機構証拠として使用する際に、質量収支の
  閉鎖と速度論的ウィンドウ評価が欠けているパターン。RI-04の
  case-specific実装として記録する。

新規知見がない場合は「本ケースは既存の制度設計を追加確認した」と記載。

---

## 出力形式

```
prompt_version: stage3-v3-20260425
model_info: <model name and version>

# 科学的知見の再認定判定票

## [論文著者名] [年]（[BIB-3] [BIB-7]）

### §1 Claim Architecture
[コア主張の要約]
[Layered structureの判定]

### §2 SRG / CLA → RI / ER / EP Crosswalk

[各SRGのテンプレート]
...

SRG外：CLA
[各CLAのテンプレート]（該当する場合）
...

### §3 現在のVQ判定
現在判定: VQ-N ([ラベル])
[VQ-1からVQ-4まで順に通過/未達の判定と根拠]

### §4 Era-Norm Annotation
communication-era tolerated:
[項目リストと各1文の根拠]

modern-era deficient:
[項目リストと各1文の根拠]

### §5 最短補強ルート
[目的関数ごとのEP投入順序]
[認定ゲート順注記]

### §6 制度設計への寄与
[知見の記述]
```
