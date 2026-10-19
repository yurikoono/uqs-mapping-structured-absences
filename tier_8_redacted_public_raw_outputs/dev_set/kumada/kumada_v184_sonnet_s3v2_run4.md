```
prompt_version: stage3-v2-20260416
model_info: claude-sonnet-4-6
run_id: run4
```

# 科学的知見の再認定判定票

## Tamao, Sumitani, Kumada 1972（Journal of the American Chemical Society, Communication）

---

### §1 Claim Architecture

**コア主張の要約**

本論文は二本の柱から成る主張を展開している。**Novelty 柱**：ニッケル-ジホスフィン錯体 [NiCl₂(dpe)] が触媒として機能し、グリニャール試薬と sp² ハロゲン化物（ビニル・アリール）の**選択的クロスカップリング**を達成するという新規触媒系の存在証明。**Utility 柱**：β-水素含有アルキルグリニャール試薬を含む多様な基質に適用可能で「yields are generally very high」（Table I, 76–98%）という合成実用性の実証、および塩化物の高反応性・ジホスフィン配位子の優位性という触媒設計上の指針。触媒サイクル（eqs 2–4）は明示的に "working hypothesis" として位置付けられており、機構的主張は第一層と論理的に独立している。

**Layered structure の判定**

D-1 が記述したとおり、主張は明確な三層構造を持ち、層間の依存関係は非対称である。

- **第一層（合成法の存在証明）**：Table I の収率データのみで自立する。機構的理解がなくても崩れない。この層は単一の反証（一つの収率不正確）では崩れにくい。
- **第二層（選択性の達成）**：「cross-coupling over homo-coupling」という中心的差別化点に依存する。定量的根拠（cross:homo 比率）が不在であり、eq 3 が homo 生成物（R–R）を化学量論的副生成物として予測するにもかかわらず R–R の報告がないという自己矛盾を内包する。この層は B-6 + U-1 への批判によって単独反証が理論上可能。
- **第三層（機構的理解 = working hypothesis）**：著者自身が "further studies are required" と留保しており、反証の対象として設定されていない。

**層間非対称性**：第三層への批判は第一層を傷つけない設計。ただし第二層（選択性）への批判は Novelty 柱の core に関わり、第一層の「有用な合成法」という Utility 柱は損なわれないが、「選択的」という Novelty 柱の形容詞は定量的支持を欠く。

---

### §2 SRG / CLA → RI / ER / EP Crosswalk

#### Stage 1 SRG の取得

S1 META の same_root_groups：SRG-1（触媒機構証拠ギャップ）、SRG-2（Cross/homo 選択性定量化の不在）、SRG-3（スコープ制限と失敗実験の不在）、SRG-4（立体化学的結果とその機構的基盤）、SRG-5（収率データの分析的質）、SRG-6（先行研究との数値比較の欠如）。

#### CLA 候補の同定

D-4 候補 9（TON の不在）は SRG に属さない（grounded_in: B-1 はいずれの SRG member_items にも含まれない）。B-1 は SRG-5 に入っていない（SRG-5 の members は B-2, B-7, B-9, B-11）。したがって D-4 候補 9 は CLA として記録する。

**自己矛盾的不在のCLAチェック**：U-1（eq 3 が予測するホモカップリング副生成物 R–R の不在）は SRG-2 の member（B-6, U-1, C-1）として既に収容されている。U-2（黒色析出物）は SRG-1 の member（A-2, U-1, U-2, B-12）として収容されている。追加の CLA は D-4 候補 9 のみ。

---

**SRG-1 [触媒機構証拠ギャップ]**（members: A-2, U-1, U-2, B-12）

* **Primary RI**: RI-06 [Imported model] — 触媒サイクル eqs 2–4 の全体が (dipy)Ni 系（refs 11–12）からの大規模モデル輸入であり、[NiCl₂(dpe)] 触媒条件下での任意の素反応ステップも直接実験的に検証されていない。
* **Secondary RI**: RI-03 [Unobserved explanatory] — 機構的提案の核心を担う中間体 1・2・3 が [NiCl₂(dpe)] 触媒条件下で直接分光観測も速度論的拘束もされていない。RI-02 [Object identification] — 黒色析出物の組成（Ni⁰ vs 残存 Ni(II) 錯体）が未同定であり、実際の触媒活性種が代替候補（不均一系 Ni⁰）を排除できる粒度で確定していない。
* **ER**: [NiCl₂(dpe)] 触媒条件下で中間体 1・2・3 のうち少なくとも一種を分光学的に同定し、(dipy)Ni 系からの類推の妥当性を実証する必要がある。触媒活性種が均一系 Ni(II) であるか不均一系 Ni⁰ であるかの識別が前提要件。
* **EP**: EP-06a [Analogy-validation pack]; EP-03a [Direct-observation / state-assignment pack]; EP-02a [Identity / purity substantiation pack]
* **Case-specific 実装**:
  - EP-06a: [NiCl₂(dpe)] 触媒条件下での stoichiometric model reaction（例：dpe-Ni ジエチル錯体の独立合成 + PhCl との反応追跡）により (dipy)Ni→(dpe)Ni 類推の同型性を検証する。
  - EP-03a: 触媒反応中間の ³¹P NMR または EPR による Ni 種のリアルタイムモニタリング；黒色析出物の XRD / ICP-MS による Ni⁰ / Ni(II) 識別。
  - EP-02a: 単離された [NiCl₂(dpe)] 触媒の反応前後の回収・再利用実験；黒色固形物のキャラクタリゼーション（元素分析・X 線粉末回折）。
* **注記**: A-2（high_convergence_low_gap: V1=high, V2=high, convergence=2/3）が最高温度項目。U-2 は medium severity の自己矛盾的不在として独立保護。B-12 は U-2 の報告的補完。SRG-1 は RI-06 と RI-03 の共起パターンを含む（§6 で詳述）。

---

**SRG-2 [Cross/homo-coupling 選択性定量化の不在]**（members: B-6, U-1, C-1）

* **Primary RI**: RI-04 [Unreplicated discriminator] — 「selective cross-coupling」の中心的主張が cross:homo 比率の定量データなしに提示されており、eq 3 が化学量論的に予測する R–R 副生成物が単一のエントリーでも報告されていない。
* **Secondary RI**: RI-09 [External superiority] — Tamura-Kochi 系に対する優位性（"seldom employed due to homo coupling"）が共通基質上の直接数値比較なしに文献引用のみで主張されている。
* **ER**: Table I の少なくとも代表的 1 エントリー（例：EtMgBr/PhCl）において cross/homo 生成物比を定量（glpc または NMR）し、R–R ホモカップリング生成物の検出または検出下限の明示が必要。Tamura-Kochi 系との shared substrate 比較として同条件での収率・選択性データを提示する必要がある。
* **EP**: EP-04a [Discrimination / replication pack]; EP-09a [Internal benchmark pack]
* **Case-specific 実装**:
  - EP-04a: EtMgBr + PhCl 反応混合物中の Et-Et ホモカップリング生成物を glpc（キャリブレーション済み内部標準法）または ¹H NMR で定量、またはその glpc 検出下限（mol% 単位）を報告する。cross:homo 比率の統計的有意性を担保するため 3 回以上の独立実験を含める。
  - EP-09a: n-BuMgBr + PhCl を共通基質として Tamura-Kochi 系（Fe 触媒、THF）と [NiCl₂(dpe)]（Et₂O）の並行実験を行い収率・cross:homo 比率を直接比較する。
* **注記**: U-1（high severity, self-contradictory absence; V2=high, V3=high）が高温度項目。B-6（V2=high, V3=high; convergence=2/3）が補完的。この SRG は §1 第二層の単独反証可能性に直結する最重要 SRG。

---

**SRG-3 [スコープ制限と失敗実験の不在]**（members: B-4, A-3）

* **Primary RI**: RI-07 [Unsupported boundary] — "Only C_sp² halides … can be used"（P3:Lcol, feature 2）という排他的境界主張が、sp³ ハロゲン化物（alkyl chloride, benzyl chloride 等）での失敗実験データ（収率 0%、副反応の観察）を一例も提示せずに行われている。
* **Secondary RI**: なし（RI-07 が支配的；A-3 はスコープ拡張の prospective deferral として RI-07 の補完）
* **ER**: sp³ ハロゲン化物（少なくとも 1 基質）での反応試行結果（収率・副生成物・条件）を報告し、なぜ sp² 基質に限定されるかの実験的根拠（β-脱離優位、酸化的付加不活性、触媒分解など）を提示する必要がある。
* **EP**: EP-07a [Boundary-test pack]
* **Case-specific 実装**:
  - EP-07a: n-BuCl（代表的な alkyl chloride）と n-BuMgBr を [NiCl₂(dpe)] 存在下で反応させ、生成物分布（n-Bu-n-Bu ホモカップリング、β-脱離生成物、回収原料）を glpc で定量する。n-BuBr + EtMgBr でも同様の試験を行い、sp³ 基質の不活性性の化学的原因を絞り込む。
* **注記**: B-4（V1=medium, V2=medium, V3=medium; convergence=3/3、S1 フォールバック規則 (b) 最優先候補）。A-3 は A-2 と同一文（"Further studies are required…"）で宣言された先送りであり B-4 と SRG-3 の共通根「証拠なき境界設定 + 先送り」を構成。通信→Full Paper 遷移での自動解消候補（§6 参照）。

---

**SRG-4 [立体化学的結果とその機構的基盤]**（members: A-1, B-11）

* **Primary RI**: RI-04 [Unreplicated discriminator] — cis-DCE → cis:trans = 80:20、trans-DCE → cis:trans = 43:57 という識別力の高い立体化学データが分析方法（¹H NMR / glpc）の明示なしに報告されており、±5% の分析誤差が存在すれば 43:57 比率は "partial retention" と "statistical scrambling" の間で揺れる。
* **Secondary RI**: RI-05 [Qualitative overread] — 「anomalously enriched with the cis isomer」という定性的異常性の宣言から、触媒設計への示唆（"the cis configuration … is the first requisite"）が機構的根拠なしに導かれている。
* **ER**: cis/trans-DCE 反応の cis:trans 比率を測定方法（¹H NMR、glpc、GC-MS のいずれか）・カラム条件・参照化合物を明示した形で少なくとも 3 回の独立測定から提示し、分析不確かさを数値で示す。機構的解釈（cis エンリッチが酸化的付加 / 転位金属化 / 還元的脱離のいずれの段階で決まるか）についての実験的識別が追加要件。
* **EP**: EP-04a [Discrimination / replication pack]; EP-08a [Replication / uncertainty pack]
* **Case-specific 実装**:
  - EP-04a: ¹H NMR（ビニルプロトンの化学シフト差を利用）と glpc（既知混合物でのキャリブレーション）の両方で cis:trans 比を独立に測定し、方法間の一致を確認する。
  - EP-08a: 3 回の独立実験から平均値 ± 標準偏差を報告し、43:57 比率が "near-statistical" (50:50 ± 測定誤差) と有意に異なるかを t 検定または同等の統計検定で評価する。
* **注記**: A-1（V1=medium, V2=medium; convergence=2/3）。RI-04 と RI-05 の共起パターン（§6 参照）。

---

**SRG-5 [収率データの分析的質]**（members: B-2, B-7, B-9, B-11）

* **Primary RI**: RI-01 [Reporting integrity] — Table I が glpc 収率（footnote e）と孤立収率（footnote d）を同一列に混在させ、glpc 定量の内部標準・応答係数・キャリブレーションプロトコルを非開示にしており、収率データの横比較可能性が損なわれている。
* **Secondary RI**: RI-08 [Unquantified reliability] — 全エントリーが一回測定のみで標準偏差がなく、76% と 95% の収率差が実験的に有意かどうかを評価できない。
* **ER**: 全 Table I エントリーについて同一測定基盤（孤立収率または glpc 収率のいずれか、混在不可）で報告し、glpc 使用時は内部標準の同定・応答係数・キャリブレーション曲線を開示する。最低限、主要エントリーで n ≥ 2 の独立実験から収率の平均 ± 標準偏差を記載する。
* **EP**: EP-01a [Reporting-coherence pack]; EP-08a [Replication / uncertainty pack]
* **Case-specific 実装**:
  - EP-01a: glpc 収率のみで報告された 5 エントリー（EtMgBr/PhCl, n-C₅H₁₁MgCl/CH₂=CHCl, PhMgBr/CH₂=CHCl, α-NpMgBr/CH₂=CHCl, n-BuMgBr/p-DCB）について、なぜ孤立収率が入手できないかを明示するか、または孤立収率を追加報告する。glpc 定量に使用した内部標準（化合物名、濃度）と各生成物への応答係数（または補正係数の入手方法）を Experimental に記載する。
  - EP-08a: 代表的 3 エントリー（例：n-BuMgBr/PhCl 76%、n-BuMgBr/m-DCB 94%、n-C₅H₁₁MgCl/CH₂=CHCl 95%）について n = 3 独立実験を実施し、収率の標準偏差を算出する。B-11（cis:trans 比率の分析法不記載）も EP-08a 実装に組み込み（独立測定 ≥ 3 + 方法明示）。
* **注記**: B-2（V1=medium, V3=medium; convergence=2/3）、B-7（V3=medium; convergence=1/3）、B-9（V3=medium; convergence=1/3）、B-11（V3=medium; convergence=1/3）。RI-08 サブタイプ: 内部矛盾型に非該当（数値矛盾ではなく測定基盤の異種混在）。

---

**SRG-6 [先行研究との数値比較の欠如]**（members: C-1, C-2, A-4）

* **Primary RI**: RI-09 [External superiority] — Tamura-Kochi 系（refs 5–6）に対する優位性、π-allylnickel・cuprate（refs 8–10）に対する選択的対比、および同時期 Corriu-Masse（footnote 3a）との差別化がいずれも直接数値比較なしに citation + dismissal 構造で処理されている。
* **Secondary RI**: RI-07 [Unsupported boundary] — C-2 での π-allylnickel・cuprate の categorical 排除が「our interest centers on…」という意図表明のみで正当化されており、実験的境界（触媒 vs 化学量論試薬の収率・選択性・スケール比較）が提示されていない。
* **ER**: Tamura-Kochi 系との比較に際して共通基質（例：n-BuMgBr + vinyl chloride）を用いた直接的な並行実験を実施し、収率・cross:homo 比率・条件（触媒量、温度、時間）を表として示す。Corriu-Masse との差別化については Note 段階では不可能だが Full Paper では基質スコープ表の比較が必要。
* **EP**: EP-09a [Internal benchmark pack]
* **Case-specific 実装**:
  - EP-09a: n-BuMgBr + PhCl を共通基質として、（i）Tamura-Kochi 系（Fe(acac)₃ / THF）と（ii）[NiCl₂(dpe)]（Et₂O）を同一条件下で並行実験し、孤立収率・反応時間・cross:homo 比率を直接比較した 2 × 3 表（基質 × 触媒系）を作成する。Corriu-Masse 系との比較は vinylchloride を共通基質として基質スコープ表を対応させる。
* **注記**: C-1（Tamura-Kochi, affects_claims: yes）、C-2（cuprate/allylnickel, affects_claims: medium）、A-4（Corriu-Masse, forgotten deferral; V1=low）。SRG-6 は §1 の competitive_positioning の核にある RI-09 の代表事例であり、Priority が低い（C-1 が最優先）。

---

**SRG 外：CLA**

**CLA: 触媒量と実用的合成スケールへの外挿——TON の不問**（grounded_in: D-4 候補 9, B-1）

* **Primary RI**: RI-05 [Qualitative overread] — 「useful preparative method」という Utility 柱の核心的主張が、触媒効率の基本指標である TON を提示せずに高収率データのみによって支持されている。「catalytic amount」（mol% で 0.1–1%）という表現が TON への言及を暗黙的に期待させるにもかかわらず、触媒回転数の定量評価が欠如している。
* **Secondary RI**: なし
* **ER**: Table I の全触媒負荷量（mol%）から計算可能な理論 TON を少なくとも代表的 1 エントリーで報告するか、または「The experimental conditions are not necessarily optimum」という免責が TON の算出を意図的に回避する理由を説明する。
* **EP**: EP-05a [Quantitative-ranking substantiation pack]
* **Case-specific 実装**:
  - EP-05a: m-DCB + n-BuMgBr 反応（[NiCl₂(dpe)] = 0.72 mol%, Example 1）の全触媒量と最終生成物量から TON = 生成物 mol / Ni mol ≈ 138（Example 1 の数値から計算可能）を明示的に報告し、これが触媒的動作を示すことを主張する根拠として位置付ける。さらに触媒負荷量を 0.01–1 mol% で変化させた yield vs. mol% [Ni] プロットを提示する。
* **注記**: B-1（V1=medium, V3=low; convergence=2/3, temperature_gap=low）。§1 の Utility 柱の定量的担保に関わるが主張の崩壊には直結しないため CLA として処理（§3 では Non-fatal 判定）。

---

### §3 現在のVQ判定

**現在判定: VQ-1 (Observation)** ——到達。ただし **VQ-2 (Method) は未達**。

---

**VQ-1 [Observation]**：通過（RI-02 の致命的残存なし）

RI-02 への対応を検討する。Table I に示される生成物は glpc, NMR, IR, および/または MS によるキャラクタリゼーションを受けており（footnote c）、二つの代表例（m-di-n-butylbenzene: bp, n²⁰D; α-vinylnaphthalene: bp, n²⁵D）については物理定数と文献値の照合が行われている。Example 1 で "pure" の根拠が不十分（B-8）で B-12 の黒色析出物が Ni⁰ である可能性（U-2）があるが、いずれも主要生成物の同一性を原理的に崩すほどの反証ではなく、Non-fatal と判定する。

**結論**：VQ-1 は Non-fatal な RI-02 残存を抱えつつ通過。SRG-1（触媒活性種の同定）が RI-02 の最重要項目（黒色析出物 = Ni⁰ の可能性）だが、生成物同定という VQ-1 要件には触媒活性種の完全同定は必須でないため通過とする。

---

**VQ-2 [Method]**：未達

VQ-2 の必須解消項目は RI-01（Reporting integrity）と RI-07（Unsupported boundary）である。

- **RI-01**（SRG-5）：Table I の glpc / 孤立収率の混在と内部標準の非開示が解消されていない。Fatal：方法の一貫性が欠如しており、全 10 エントリーの収率データの横比較可能性が保証されない。glpc と孤立収率が系統的に異なる基盤（副生成物計上有無）を持つため、測定フレームの不統一は現代基準では致命的。
- **RI-07**（SRG-3）：sp³ ハロゲン化物の排除が失敗実験データなしに行われている。Fatal："Only C_sp² halides … can be used" という method の境界条件を実験的に検証する負の証拠が一例も存在しない。これは方法的主張の核心（適用範囲）を empirically 根拠なく設定する致命的欠落。

**結論**：VQ-2 は RI-01（Fatal）と RI-07（Fatal）の解消なしに未達。

ただし**第一層（合成法の存在証明）単独では**：Table I の各エントリーが「その反応が起きること」を示す VQ-1 水準の観察として読める。第一層は RI-02 Non-fatal のみであり VQ-1 に留まる。**第二層（選択性の達成）単独では**：RI-04（SRG-2, U-1）が Fatal であり VQ-1 すら Qualified（選択性という「観察」自体が定量的根拠を欠く）。この層別非対称性は §1 の三層構造と対応する。

---

**VQ-3 [Mechanism]**：未達（VQ-2 が未達のため継承原則により不成立）

VQ-2 継承前提が満たされない。仮に VQ-2 が解消されても、RI-03（SRG-1: 中間体の未観測）と RI-06（SRG-1: (dipy)Ni 系からのモデル輸入）が残存する。RI-03 は Fatal：機構的主張の核心を担う中間体 1・2・3 が [NiCl₂(dpe)] 条件下で一例も直接観測されていない。RI-06 は Fatal：触媒サイクル全体を別系から構成する大規模モデル輸入。なお RI-05（SRG-4: feature 3 の "cis configuration is the first requisite" が数値なき定性推論）が残存するため VQ-3 は「limited (qualified)」となる見込みだが、VQ-2 未達のため現時点では到達しない。

---

**VQ-4 [Benchmark]**：未達（VQ-3 が未達のため不成立）

RI-08（SRG-5）と RI-09（SRG-6）の双方が未解消。仮に VQ-3 解消後も、RI-08（再現性・不確かさ記述の欠如）と RI-09（Tamura-Kochi 系との直接数値比較の欠如）が残存する。

---

**層別 VQ 非対称性のまとめ**

| 層 | VQ 水準 | 制限要因 |
|---|---|---|
| 第一層（合成法存在証明） | VQ-1 通過（Non-fatal RI-02 残存） | B-7, B-8（"and/or" 特性評価、"pure" 根拠）|
| 第二層（選択性の達成） | VQ-1 Qualified | U-1 Fatal（RI-04: homo 副生成物の定量不在）|
| 第三層（working hypothesis） | VQ-2 以下（著者が明示的に限定） | A-2, RI-06, RI-03 |
| **論文全体** | **VQ-1 通過 / VQ-2 未達** | RI-01 Fatal, RI-07 Fatal |

---

### §4 Era-Norm Annotation

**communication-era tolerated（1972年 JACS Communication として許容される欠落）**

- **B-1（TON の不在）**：1972年当時の合成化学コミュニティにおいて触媒効率の指標として TON が JACS communication レベルで標準的に要求されていたという根拠はなく、"catalytic amount" という表現での提示は当時のフォーマット慣習の範囲内である。
- **B-9（再現性データの欠如）**：1970年代の JACS communication において n = 1 の反応収率報告は標準的な実務であり、標準偏差・平均値の記載要件は当時の投稿規則に含まれていなかった（T2）。
- **B-8（"pure" の根拠欠如）**：bp と n²⁰D の報告で文献値との一致を示す方式は 1970 年代 JACS の標準的な生成物同定様式であり、GC 純度・HRMS を必須とする現代の要求水準とは異なる。
- **B-10（Grignard 試薬の滴定法不記載）**：Grignard 試薬の molarity 検証プロトコルの記載は 1972 年当時の JACS communication における Experimental の標準構成要素ではなかった（T2）。
- **B-13（PhMgBr/Cl₂C=CH₂ の強制条件の非説明）**：通信形式の紙幅制約により、基質ごとの条件選択根拠を全エントリーで説明することは当時の JACS communication では要求されなかった。
- **B-5（Et₂O 優位性の比較データ不在）**：溶媒選択の根拠を comparative data で示すことは 1972 年時点の JACS communication の報告要件に含まれていなかった（T2）。
- **B-14（反応時間の非説明）**：反応時間のみの記録は手順記述として当時の標準内。

**modern-era deficient（現代の再認定基準では許容できない欠落）**

- **B-2（glpc / 孤立収率の混在 + 内部標準の非開示）**（SRG-5, RI-01, Fatal）：現代の JACS は glpc 定量収率の報告に内部標準の明示と応答係数の記録を要求する；測定基盤の混在は横比較を妨げる致命的欠落として現代では受理不可。
- **B-4（sp³ 基質除外の失敗実験不在）**（SRG-3, RI-07, Fatal）：現代の JACS・JACS Au・Nature Chem では scope restriction を主張する際に representative failed substrate の提示が必須と見なされる。
- **B-6 / U-1（cross:homo 比率の完全不在）**（SRG-2, RI-04, Fatal for VQ-2 層）：「selective」という中心的 Novelty 主張を支持する定量的選択性データ（cross:homo 比率 ≥ 3 エントリーの平均 ± SD）は現代では必須；eq 3 が予測するホモカップリング副生成物 R–R の不在説明も現代基準では必須。
- **B-3（配位子活性順の数値なし）**（SRG-1 周辺, RI-05, Non-fatal）：現代では順序主張には各点の実測値（% 収率）の提示が要求される；当時は ranking の提示のみが許容されていたが現代では不足（両タグ対象）。
- **U-2（黒色析出物の未同定）**（SRG-1, RI-02, Non-fatal）：現代では触媒の活性種同定（均一系 vs 不均一系の識別）が機構論文の前提条件として要求される；1972年当時は観察の記録のみで許容されたが現代では不足（両タグ対象）。

---

### §5 最短補強ルート

**目的関数：VQ-2 (Method) への到達（第一目的）→ VQ-3 (Mechanism) への到達（第二目的）**

現在 VQ-1 通過 / VQ-2 未達。第一目的は RI-01（Fatal）と RI-07（Fatal）の同時解消。

---

**VQ-2 への最短ルート：**

1. **EP-01a [Reporting-coherence pack]** — Table I の全 10 エントリーについて収率報告基盤を統一（孤立収率を主軸とし、孤立不能な 5 エントリーについては理由を明記）し、glpc 定量の内部標準（化合物名）・応答係数・キャリブレーション条件を Experimental に記載する。**RI-01 を解消**（SRG-5 の致命的欠落を閉じる）。また B-7（"and/or" 特性評価）への対応として各生成物に使用した分析方法の組み合わせを product table または SI に明示する。

2. **EP-07a [Boundary-test pack]** — n-BuCl（または EtBr のアルキル版）と n-BuMgBr を [NiCl₂(dpe)] 存在下で反応させ、生成物分布（ホモカップリング、β-脱離生成物、回収原料）と収率（0% または trace であれば glpc 検出下限を添えて）を报告する。**RI-07 を解消**（SRG-3 の「失敗実験なき境界主張」を閉じる）。

これら 2 実験は既存のラボインフラ（glpc + Grignard 化学）で追加できる最小単位の補強であり、VQ-2 達成に十分である。

---

**VQ-3 への最短ルート（VQ-2 通過後）：**

3. **EP-06a [Analogy-validation pack]** — [NiCl₂(dpe)] 条件下での stoichiometric model reaction（dpe-Ni ジエチル錯体の独立合成 + PhCl との反応追跡、または n-BuMgBr + [NiCl₂(dpe)] の低温 NMR 観察）により、(dipy)Ni 類推の [NiCl₂(dpe)] 系への同型性を最低 1 素反応ステップで検証する。**RI-06 を前進**（SRG-1 の大規模モデル輸入を部分的に解消）。

4. **EP-03a [Direct-observation / state-assignment pack]** — 触媒条件下での ³¹P NMR または EPR によるリアルタイム Ni 種モニタリング（少なくとも反応前・反応中・反応後の 3 時点）を実施し、中間体 2 に相当する (halo)(organo)Ni(II) 種の分光同定またはその存在下限を示す。黒色析出物の XRD または ICP-MS による Ni⁰ / Ni(II) 識別を実施する。**RI-03 と RI-02 を前進**（SRG-1 の中間体未観測と活性種未同定を閉じる）。

5. **EP-04a [Discrimination / replication pack]** — EtMgBr + PhCl 反応混合物中の Et-Et ホモカップリング生成物を glpc（キャリブレーション済み）で定量し、cross:homo 比率を少なくとも 3 回の独立実験から報告する。**RI-04 を前進**（SRG-2 の self-contradictory absence を閉じる）。

VQ-3 到達後は RI-05（SRG-4 での定性的過剰解釈：feature 3 の "cis configuration is the first requisite"）が残存するため VQ-3 は Qualified となる可能性が高い（cis:trans 比率の方法明示と独立測定による RI-05 軽減が必要）。

---

**VQ-4 への最短ルート（VQ-3 通過後）：**

6. **EP-08a [Replication / uncertainty pack]** — Table I の全エントリーについて n ≥ 3 の独立実験から収率の平均 ± SD を算出して報告し、cis:trans 比率も同様に統計的評価を付与する。**RI-08 を解消**（SRG-5 の不確かさ記述欠如を閉じる）。

7. **EP-09a [Internal benchmark pack]** — n-BuMgBr + PhCl を共通基質として Tamura-Kochi 系（Fe(acac)₃ / THF）と [NiCl₂(dpe)]（Et₂O）の並行実験を行い収率・cross:homo 比率・条件の比較表を提示する。**RI-09 を解消**（SRG-6 の外部比較欠如を閉じる）。

---

**認定ゲート順注記**：実験投入順は情報利得順（EP-01a, EP-07a → EP-06a, EP-03a, EP-04a → EP-08a, EP-09a）だが、最終認定は VQ-1 → VQ-2 → VQ-3 → VQ-4 の継承原則ゲート順で確定する。VQ-2 の RI-01・RI-07 解消なしに VQ-3 以上の認定は成立しない。EP-04a（SRG-2, RI-04）は VQ-3 要件（RI-04 解消）に属するが、情報利得の観点から SRG-1 関連実験（EP-06a, EP-03a）と並行実施が効率的である。

---

### §6 制度設計への寄与

**1. 既存 RI コードの代表事例**

- **RI-06（Imported model）**の典型的大規模輸入事例：SRG-1 は RI-06 の "cycle-level import[REDACTED: substantial verbatim quotation; see Tier 9]サイクルレベル輸入" 定義を確認する。

- **RI-07（Unsupported boundary）の否定的境界主張への拡張適用**（Codebook v0.2a RI-07 拡張適用に記載）：SRG-3（sp³ 基質除外）は肯定的境界（"only sp² halides work"）として記述されているが、失敗実験データなき境界設定という構造は RI-07 の典型例として機能する。通信 → Full Paper 遷移での自動解消パターン（Codebook v0.2a §6 に記載）の代表事例でもある（Full Paper で sp³ 基質試験が追加されれば RI-07 は自動解消される）。これは **communication→Full Paper遷移の自動解消パターン**として記録すべき事例。

**2. RI 共起パターンの記録**

- **SRG-1 における RI-06 + RI-03 の共起**：「(dipy)Ni モデルの大規模輸入（RI-06）」と「中間体の直接未観測（RI-03）」が同一 SRG で共起しており、いずれか一方のみの解消では VQ-3 に到達しない。EP-06a（analogy validation）は RI-06 を前進させるが RI-03 は残る；EP-03a（direct observation）は RI-03 を前進させるが RI-06 の根本的問題（(dipy)Ni との同型性未実証）は残る。両者が独立した解消実験を要するという共起構造は Codebook §6「RI 共起パターン」の記録候補。

- **SRG-4 における RI-04 + RI-05 の共起**：cis:trans 比率の「分析方法不記載による識別力への疑義（RI-04）」と「"the cis configuration is the first requisite" という定性的過剰解釈（RI-05）」が SRG-4 で共起する。RI-04 の解消（測定法明示 + 独立測定）は RI-05 を直接解消しない（定性的推論の根拠は別の mechanistic 実験で対応が必要）。この共起は Codebook §6 の事例として追加。

**3. 標識不整合（Labeling mismatch）パターン**

本論文において、著者は触媒サイクルを "working hypothesis" と明示しているが（P3:Lcol：「apart from the working hypothesis described above」）、これは本文末尾の1文に集約されており、eqs 2–4 および "These facts suggest …" の記述語（"is subsequently converted to", "reacts with … to form", [REDACTED: substantial verbatim quotation; see Tier 9]）はすべて事実的記述語（factual indicative）を使用している。仮説標識（"working hypothesis"）が末尾1文に集約され、それ以外の触媒サイクル記述は事実的語で展開されるパターンは「仮説標識の末尾集約型」として Codebook §6 の「標識不整合（Labeling mismatch）」記録候補。RI-06 と連動するパターンとして明示すべき。

**4. 否定的証拠の不完全性（Codebook §6 パターン）**

SRG-2（U-1）は「eq 3 が予測する R–R の不在」という否定的観察を肯定的選択性証拠として使用しているが、R–R の glpc 検出下限・質量収支の閉鎖（side products の総計）・反応時間内の R–R 生成ウィンドウ（もし eq 3 の速度が十分速ければ R–R が消費される可能性）のいずれも評価されていない。RI-04 の case-specific 実装として記録する：「eq 3 の反応性副生成物が検出されないことを陰性証拠として使用する場合、glpc 検出感度・質量収支・速度論的ウィンドウの評価が必要」。これは Codebook §6「否定的証拠の不完全性」の合成化学版として新規追記候補。

**5. PRI 候補**

本ケースでは新規 PRI 候補は提案しない。SRG-1 の RI-06（cycle-level import）は既存コードの範囲内で処理できる。PRI-11（Mechanism-kinetics decoupling）の適用可能性を検討したが、本論文は速度論データを一切提示していないため PRI-11 の「速度式との一致のみで機構支持」パターンの適用対象外（速度式自体が存在しない）。RI-03 の「未観測説明変数」として処理するのが適切。

**6. VQ 境界条件の知見**

- **第一層と第二層の VQ 非対称性**は、1 つの論文内に VQ 水準が異なる複数の主張層が共存するケースとして Codebook の VQ 判定境界条件記録に追記価値がある：「論文全体の VQ 判定はすべての主張層を統合して行うが、層別 VQ 非対称性は論文の知的設計の脆弱点を同定する分析的情報を持つ（§3 の層別 VQ 非対称性の検出を参照）」。
- **SRG-2 の U-1（self-contradictory absence）が VQ-1 Qualified（選択性の層）の根拠となるケース**：通常 VQ-1 は生成物同定（RI-02）で判定されるが、中心的 Novelty 主張が「selective cross-coupling」の場合、選択性の定量的根拠の欠如（RI-04）が VQ-1 の Qualified 化をもたらす。これは VQ-1 に RI-04 が致命的に関わる初出事例として記録価値がある。

**総括**

本ケース（Kumada 1972 JACS Communication）は既存の制度設計の多面的な確認と代表例の追加を提供した。新規 PRI の提案には至らないが、（a）RI-06 cycle-level import の典型例、（b）RI-07 否定的境界 + communication→Full Paper 自動解消パターン、（c）RI-06 + RI-03 の共起構造、（d）否定的証拠の不完全性（合成化学版）、（e）層別 VQ 非対称性の事例として Codebook v0.2a に追記できる知見を複数提供する。

---

> **Tier 8 redaction notice**: This file is a redacted copy of the corresponding Tier 3 / Tier 9 output. Verbatim source-paper quotations have been replaced by `[REDACTED: see source paper §<loc>; full text retained in Tier 9 reviewer-only deposit]` markers, preserving location references and our own analytical content. Bibliographic fields (title, authors, journal, year, DOI), analytical labels (`evidence_chain:` with B-/U-/A-/C- internal IDs), short technical terms, and our own analytical text are not redacted. The redaction was applied by `scripts/redact_for_tier8.py` and, for this version, by `scripts/build_paperA_R1_public.py` with `scripts/redact_source_ngram_runs.py` (scripts of the project repository; they are not deposited).
