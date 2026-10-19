prompt_version: stage3-v3-20260425
model_info: claude-sonnet-4-6

# 科学的知見の再認定判定票

## Tamao, Sumitani, Kumada 1972（Journal of the American Chemical Society, communication）

### §1 Claim Architecture

**コア主張の要約：**

Novelty柱：ニッケル-二座ジホスフィン錯体（代表例：[NiCl₂(dpe)]）が、グリニャール試薬とビニルまたはアリールハロゲン化物のクロスカップリングを高収率・高選択的に触媒するという新しい合成法の確立。特に(i) 塩化物の高反応性、(ii) β水素を持つアルキルグリニャール試薬への適用、(iii) 二座ジホスフィンによる触媒活性という三つの実証的主張が独立した柱を構成する。

Utility柱：従来は実用困難だったアリール塩化物からのC–C結合形成（di-n-butylbenzene等）を一段階で達成する合成的実用性。

**Layered structure判定：**

独立層あり。三つの実証的主張（選択性、塩化物反応性、β水素許容性）は相互依存していないため、機構（eqs 2–4、「working hypothesis」）の論駁がいずれかの実証的主張を直接崩すことはない。ただし選択性主張（層1）は最も脆弱——ホモカップリング量が未定量であるため（U-1、B-7）、「selective」の定量的根拠が欠如している。層2（塩化物反応性）と層3（β水素許容性）は実験的に最も堅牢。

---

### §2 SRG / CLA → RI / ER / EP Crosswalk

**SRG-1 [Mechanistic validation absent]**（members: B-7, U-1, A-1）

* **Primary RI**: RI-03 [Unobserved explanatory] — 触媒サイクルの中核的説明種（Ni(0)/Ni(II)中間体、R–R副生物）が直接観測も速度論的拘束もされていない
* **Secondary RI**: RI-04 [Unreplicated discriminator] — 選択性の主張がR–R定量なしの高cross-coupling収率のみに依拠する
* **ER**: 触媒サイクル（eqs 2–4）の少なくとも一つの素反応ステップについて、本系固有の動力学的データ（反応次数、速度定数）または化学量論的制御実験（[NiCl₂(dpe)]とRMgXの当量反応）が必要。R–R副生物の定量が全エントリーで必要。
* **EP**: EP-03a [Direct-observation / state-assignment pack]; EP-04a [Discrimination / replication pack]
* **Case-specific実装**: (a) [NiCl₂(dpe)] + 2 RMgBr の化学量論反応を行い、diorganonickel中間体1を単離または分光学的検出; (b) EtMgBr/PhCl反応でEt–Etホモカップリング収率をGC-MS定量; (c) radical clock substrate（例：5-hexenylMgBr）を用いてラジカル経路の関与を評価
* **注記**: B-7 = TEMPERATURE_SUMMARY high_convergence_low_gap (3/3, gap=low); U-1 = low_convergence_high_gap (critical)

**SRG-2 [Quantitative yield reporting incompleteness]**（members: B-1, B-2, B-4, B-5）

* **Primary RI**: RI-01 [Reporting integrity] — 収率基準（isolated vs glpc）の混在、内部標準未記載、収率計算分母の不一致により横比較が不能
* **Secondary RI**: RI-08 [Unquantified reliability] — cis:trans比（80:20, 43:57）に反復測定や不確かさ記述なし
* **ER**: 全エントリーで収率基準を統一（isolated優先）し、glpc使用時は内部標準と応答係数を明記。cis:trans比は3回以上の反復の平均±SDで報告する必要がある。
* **EP**: EP-01a [Reporting-coherence pack]; EP-08a [Replication / uncertainty pack]
* **Case-specific実装**: (a) 全エントリーの単離収率を測定し収率基準混在を解消; (b) glpcに使用した内部標準化合物名と応答係数を明記; (c) cis/trans-stilbene比をn≥3で再測定
* **注記**: B-5 = high_convergence_low_gap (3/3, gap=none)

**SRG-3 [Catalyst structure–activity without quantification]**（members: B-3, U-2）

* **Primary RI**: RI-05 [Qualitative overread] — 定性的配位子活性序列から中間体3のcis配置という構造的因果結論を導出
* **Secondary RI**: RI-03 [Unobserved explanatory] — 中間体3の構造が直接観測されていない
* **ER**: 少なくとも二つの配位子系（[NiCl₂(dpe)] vs [NiCl₂(PPh₃)₂]）で同一基質・同一条件での定量的収率比較が必要。中間体3（diorganonickel complex）の分光学的同定（³¹P NMR, ¹H NMR）または単離が必要。
* **EP**: EP-05a [Quantitative-ranking substantiation pack]; EP-03a [Direct-observation / state-assignment pack]
* **Case-specific実装**: 各配位子での n-BuMgBr/PhCl 反応を統一条件で実施し単離収率を記録; [NiCl₂(dpe)] + 2 PhMgBr の化学量論反応でL₂Ni(Ph)₂のNMRスペクトル取得
* **注記**: U-2 = high severity; B-3 = high_convergence_low_gap (2/3, gap=none)

**Self-referential validation チェック（v18新規）：**
本論文はDFT計算・記述子・スコア関数を含まないため、PRI-12クラスターA（Self-referential validation）は該当しない。

**Deductive-retrospective structure チェック（v18新規）：**
本論文は実験的合成論文であり、演繹的原理提案ではないため、PRI-12クラスターB（Deductive-retrospective circularity）は該当しない。

**SRG外：CLA**

**CLA-1 [β水素排除回避の原理的根拠]**

* **Primary RI**: RI-03 [Unobserved explanatory] — β水素排除が抑制される原因種（Ni–アルキル中間体の安定化機構）が観測されていない
* **Secondary RI**: RI-07 [Unsupported boundary] — 「β水素を持つアルキルグリニャールに有効」という境界主張がdecomposition経路の除外なしに提示されている
* **ER**: deuterium-labeling実験（d₂-EtMgBr/PhCl反応）でエチレン生成（β-H排除の指標）を定量することが必要。
* **EP**: EP-03a [Direct-observation / state-assignment pack]; EP-07a [Boundary-test pack]
* **Case-specific実装**: d₂-EtMgBr（またはd₅-EtMgBr）とPhClの反応でGC-MSによりCH₂=CHD等のβ-H排除生成物を定量; n-BuMgBrでの内部オレフィン（1-ブテン、2-ブテン）生成量をGCで測定

**CLA-2 [Corriu–Masse concurrent system との区別]**

* **Primary RI**: RI-09 [External superiority] — Ni(acac)₂系（Corriu–Masse）との直接比較なしに、Ni-ジホスフィン系の独自性を主張
* **ER**: 同一基質（例：PhMgBr/PhCl）でNi(acac)₂とNiCl₂(dpe)を並行試験し、収率・選択性・反応時間を比較することが必要。
* **EP**: EP-09a [Internal benchmark pack]
* **Case-specific実装**: PhMgBr + PhCl反応でNi(acac)₂対照実験を実施し、cross:homo比と収率をNiCl₂(dpe)と比較

---

### §3 現在のVQ判定

現在判定: VQ-2 (Method) — Qualified

**VQ-1 [Observation] は通る。**
RI-02（Object identification）について：主要生成物（Ph-Et, Ph-n-Bu, di-n-butylbenzenes等）はglpc, NMR, IR, mass spectraで同定されており、既知化合物との物性比較（bp, nD）も行われている。RI-02はNon-fatalとして残存するが（新規化合物の完全な構造証明が簡潔）、生成物同定の基本要件は満たしている。VQ-1は通る。

**VQ-2 [Method] は通る（Qualified）。**
RI-01（Reporting integrity）: B-1の収率基準混在とB-2の内部標準未記載はRI-01の未解消項目だが、主要合成例（Example 1, 2）では単離収率+物性が記録されており、Non-fatalと判定できる。RI-07（Unsupported boundary）: sp2ハロゲン化物のみという境界は実験的に支持されている範囲では成立しており、Non-fatal。VQ-2 (Qualified) — SRG-2の収率報告不整合が残存するため限定的。

**VQ-3 [Mechanism] は未達。**
RI-03（Unobserved explanatory）: 触媒サイクルの中核中間体（Ni(0)種、diorganonickel 1、haloorganonickel 2）は直接観測されていない（SRG-1）。Fatal。
RI-04（Unreplicated discriminator）: 選択性主張はR–R定量なしの単一実験収率に依拠（U-1、B-7）。Fatal。
RI-06（Imported model）: 触媒サイクルはdipy-Ni系（ref 11）から輸入されており、dpe-Ni系での同型性が実証されていない。Fatal（VQ-3水準）。
未解消RIリスト: RI-03 (Fatal), RI-04 (Fatal), RI-06 (Fatal)

**VQ-4 [Benchmark] は未達（VQ-3未達のため評価対象外）。**
RI-08（Unquantified reliability）: cis:trans比に反復測定なし（B-5）。RI-09（External superiority）: Corriu–Masse系との直接比較なし（CLA-2）。VQ-3未達のため継承により到達不可。

**層別VQ非対称性：**
ただし**実証的合成層（層2: 塩化物反応性、層3: β水素許容性）単独では**：RI-03/RI-04が問題にならない範囲（合成実証の事実）であり、この2層のみについてはVQ-2に到達している。選択性層（層1）はU-1により最も脆弱（VQ-1とVQ-2の境界）。

---

### §4 Era-Norm Annotation

**communication-era tolerated:**
- B-1（収率基準混在）: 1972年のJACS Communicationsでは、glpc収率（with internal standard）は実用的な一次評価として許容されており、単離収率との混在は慣行の範囲内だった。
- B-2（内部標準未記載）: 1972年当時のglpc収率報告では内部標準の種類を本文に記載しない慣行が一般的だった。
- B-3（触媒活性序列の定性的記述）: 通信形式での定性的活性比較は、詳細なfull paperを予告する形式として当時許容されていた。
- B-6（溶媒比較データ不在）: 「definitely superior」という主観的記述は通信形式では許容された。
- A-1, A-2（機構・適用範囲の後回し）: "Further studies are required" / "Investigations are continuing" は1972年の通信論文における標準的な将来課題告知形式。

**modern-era deficient:**
- U-1 + B-7（ホモカップリング量の未定量）: 現代基準では "selective" を主張する論文でhomo-coupling byproductの定量は必須。cross:homo比の明示がなければ選択性主張は評価不能。現代のVQ-3審査要件に直接抵触。
- B-5（cis:trans比の再現性データなし）: 現代では定量的立体選択性データは反復測定（n≥3、±SD）が要求される。
- CLA-1（β水素排除の検証不在）: 現代のメカニズム意識の高い合成論文では、β-H排除の関与をdeuterium labelingで否定することが一般的に期待される。
- SRG-3（中間体の構造的証拠なし）: 現代では触媒設計の構造的根拠にはX線結晶解析または ³¹P NMR による中間体同定が求められる。

両方に該当する項目：B-3（当時は定性的序列で許容されたが、現代では定量的比較が必須）。

---

### §5 最短補強ルート

**VQ-3 [Mechanism] への最短ルート：**

1. EP-03a [Direct-observation / state-assignment pack] — [NiCl₂(dpe)] + 2 PhMgBrの化学量論反応でL₂Ni(Ph)₂を単離または³¹P/¹H NMRで観測し、中間体1の実在を確認。RI-03を前進。
2. EP-04a [Discrimination / replication pack] — EtMgBr/PhCl反応でEt–Etホモカップリング収率をGC定量（内部標準法）し、cross:homo比を数値化。U-1とRI-04を前進。
3. EP-06a [Analogy-validation pack] — radical clock substrate（例：5-hexenylMgCl）またはクロスオーバー実験で、eq 3のラジカル経路vs.極性経路を区別。RI-03（速度論的拘束）を前進、RI-06を部分前進。
4. EP-05a [Quantitative-ranking substantiation pack] — 各配位子系でn-BuMgBr/PhCl反応を統一条件で実施し単離収率を記録。B-3のRI-05を解消。

認定ゲート順注記：実験投入順は情報利得順だが、最終認定はVQ-1 → VQ-2 (Qualified解除) → VQ-3のゲート順で確定する。VQ-2のQualified解除にはSRG-2収率報告整合化（EP-01a）が先行して必要。

**VQ-4 [Benchmark] への最短ルート（VQ-3達成後）：**

1. EP-09a [Internal benchmark pack] — Ni(acac)₂（Corriu–Masse系）との直接収率・選択性比較。RI-09を前進。
2. EP-08a [Replication / uncertainty pack] — cis:trans比をn≥3で再測定し±SDを付与。RI-08を解消。

---

### §6 制度設計への寄与

**既存RIコードの代表事例：**

- **RI-03「Available-but-unutilized vs 純粋観測欠如」の区別の明確化** — 本ケースでは「取得済みデータの未活用」ではなく「予測される副生物の非測定」という純粋観測欠如型RI-03。RI-03 codebookに「純粋観測欠如サブタイプ（Prediction-not-tested）」を追記する価値がある。
- **RI-05の "Qualitative overread" 3段推論パターン** — 「配位子活性序列（定性）→中間体cis幾何（構造仮定）→選択性制御（因果）」という3段推論がRI-05の典型例として記録される。
- **RI-09の「Note Added in Proof後の非比較」パターン** — 並行論文を認識しながら直接比較を行わないケースはRI-09の典型的サブタイプ。「事後的認識後の非比較（Post-recognition non-comparison）」としてCodebookに追記推奨。

**新PRI候補の検討：**
新規パターンの検出なし。ただし「dipy-Ni系からdpe-Ni触媒サイクル全体への大規模モデル輸入」はRI-06の大規模サイクルレベル輸入（Codebook RI-06スコープ注記）の代表事例として記録できる。

**VQ判定境界条件の知見：**
本ケースは「実証的合成論文における層別VQ非対称性」の明確な事例を提供。機構層（VQ-3未達）と合成実証層（VQ-2到達）が同一論文内で独立している構造は、合成論文のVQ評価において層を分離する重要性を示す。

**通信→Full Paper遷移の自動解消パターン：**
A-1（機構詳細後回し）、A-2（適用範囲拡張継続）、B-3（触媒比較定性的）はいずれも "Full Paper展開で自動解消" パターンに該当。1972–1975年のKumada group論文群でこれらが解消されているかの確認はPhase 2の課題。

**否定的証拠の不完全性（RI-04 case-specific実装）：**
U-1のR–R非検出は "negative result as evidence" の典型（B-7フラグ）。「R–R生成なし → 高選択性」という推論は検出下限の明示なしに行われており、RI-04の否定的証拠不完全性パターンとして記録。
