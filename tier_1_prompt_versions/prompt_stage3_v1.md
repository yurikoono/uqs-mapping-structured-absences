# Stage 3: 科学的知見の再認定判定票（Assessment Sheet）生成
<!-- prompt_version: stage3-v1-20260402 -->
**Language: 日本語（RI/EP/VQコード・技術用語は英語）**

出力の冒頭にプロンプトバージョンを記載すること：
```
prompt_version: stage3-v1-20260402
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

**PRI昇格基準：** 独立2報で同型確認、またはStage 2Fのrecurring_patternで
cross-case recurrence確認。既存RIに収まらない新パターンが検出された場合、
§6で「PRI-NN候補」として提案すること。

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

新規知見がない場合は「本ケースは既存の制度設計を追加確認した」と記載。

---

## 出力形式

```
prompt_version: stage3-v1-20260402
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
