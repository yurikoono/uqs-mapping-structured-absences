```
prompt_version: stage3-v3-20260425
model_info: claude-sonnet-4-6
```

# 科学的知見の再認定判定票

## Tamao, Sumitani, Kumada 1972（Journal of the American Chemical Society, communication）

---

### §1 Claim Architecture

**コア主張の要約:**

Novelty柱: Ni-ホスフィン錯体（代表: [NiCl₂(dpe)]）を触媒とするGrignard試薬×sp²-炭素ハライドの選択的クロスカップリング反応の確立。β-水素を持つアルキルGrignard試薬でも高収率（76–98%）が得られ、従来法では困難だったdi-n-ブチルベンゼン等の化合物が一段階で合成できる。

Utility柱: "a new and useful preparative method" — 反応の「実用性」（isolated yieldの高さ・アリールクロリドの使用可能性・従来困難だった化合物の合成）を前面に置く。

**Layered structure判定: yes — 独立3層構造**

Layer 1（合成実用性）: 高収率、Table I、Examples 1–2 — Table Iが直接支持。Layer 2の機構が否定されてもLayer 1は独立して成立。ただしLayer 1の核心命題「selective」は、ホモカップリング不在の実験的証明（未実施）に依拠するため、実際にはU-1（self-contradictory absence）によって脆弱化している。

Layer 2（機構的作業仮説）: eq.2–4の触媒サイクル — 著者自身が「working hypothesis」と明記。独立層だが全面的に未検証。

Layer 3（配位子設計論）: bidentate diphosphineの必要性・cis中間体3の要件 — Layer 2に論理的に依存。Layer 2が変更されるとLayer 3も変更される。

層間依存関係: Layer 3 → Layer 2 → （Layer 1とは独立）。

---

### §2 SRG / CLA → RI / ER / EP Crosswalk

#### Self-referential validation チェック（全論文で実施）

本論文の核心的検証構造を確認: 「選択的クロスカップリング」の検証は収率（high）と選択性（implied, not measured）に基づく。検証指標（収率）と被検証対象（選択性）は異なる量であり、PRI-12クラスターAの成立条件には該当しない。PRI-12クラスターBも1972年合成通信には適用対象外（演繹的形式理論論文でない）。PRI-12適用なし。

#### Deductive-retrospective structure チェック

eq.2–4の触媒サイクルは帰納的（観測事実からの仮説構築）であり、演繹的選択則論文ではない。PRI-12クラスターB適用なし。

---

**SRG-1 [触媒サイクルの機構的証拠の組織的不在]**

* **Primary RI**: RI-03 Unobserved explanatory — 触媒サイクルの中核種（中間体1: L₂NiR₂、中間体2: L₂Ni(R')(X'')、中間体3: diorgano-Ni）が直接観測も速度論的拘束もされていない
* **Secondary RI**: RI-06 Imported model — Uchino et al.（ref 11）のdipy-Ni系化学量論的反応（eq 1）をdpe-Niの触媒サイクル全体のアナロジーとして輸入
* **ER**: 触媒サイクルの機構的主張を採るためには、少なくとも1つの素反応ステップ（eq 2–4いずれか）の中間体観測または速度論的証拠が必要
* **EP**: EP-03a Direct-observation / state-assignment pack; EP-06a Analogy-validation pack
* **Case-specific実装**: NiCl₂(dpe)系でのジオルガノニッケル中間体（L₂NiR₂）の低温NMR同定または化学量論的反応による単離；ラジカルクロック基質（例: hex-5-en-1-yl Grignard）による有機金属経路の確認；クロスオーバー実験（RMgX + R'X'' + Ni触媒: 2種Grignard混合による生成物分布解析）
* **注記**: A-1（deferred, series_signal yes）、B-8, B-10（中間体状態の非記録）、U-1（R–R自己矛盾的不在）。TEMPERATURE_SUMMARY: A-1 high_convergence_low_gap (2/3, gap=low)

**SRG-2 [副生成物・質量収支の定量的不在]**

* **Primary RI**: RI-01 Reporting integrity — 収率基準の混在（isolated vs GC; Grignard基準 vs substrate基準）および副生成物の体系的未報告が横比較を不能にする
* **Secondary RI**: RI-08 Unquantified reliability — GLC内部標準較正情報なし（標準物質名・response factor未記録）
* **ER**: 収率主張の評価には統一された収率計算基準と、少なくとも主要副生成物（R–Rホモカップリング、β-H脱離生成物）の上限値が必要
* **EP**: EP-01a Reporting-coherence pack; EP-08a Replication / uncertainty pack
* **Case-specific実装**: 全Table Iエントリについての統一収率基準（substrate基準）への再計算；GLC内部標準（n-デカン等）の較正曲線と応答係数の開示；ホモカップリング生成物（Ph-Ph, n-Bu-n-Bu等）の検出下限と実測上限値
* **注記**: B-2（metric incompleteness）、B-6（GLC較正不在）、U-1（R–R自己矛盾）。TEMPERATURE_SUMMARY: B-2 high_convergence_low_gap (2/3, gap=none)

**SRG-3 [基質スコープ境界の実験的根拠不在]**

* **Primary RI**: RI-07 Unsupported boundary — "Only C_sp² halides can be used" という境界主張がsp³ハライドの実際の試みなしに主張されている
* **Secondary RI**: RI-05 Qualitative overread — 配位子活性順位が定量データなし（1基質ペアでの定性的観察）で構造的含意（cis中間体の必要性）まで展開されている
* **ER**: スコープ境界の主張を採るためには、少なくとも代表的なsp³ハライド（例: n-BuCl、BnCl）での収率データ（0%または低収率）と配位子各系での少なくとも2基質ペアでの収率数値が必要
* **EP**: EP-07a Boundary-test pack; EP-05a Quantitative-ranking substantiation pack
* **Case-specific実装**: sp³ハライド（1-クロロブタン、ベンジルクロリド等）とPhMgBrの反応でのNiCl₂(dpe)触媒での収率測定；配位子系全6種での同一基質ペア（PhMgBr/PhCl等）での数値収率対比
* **注記**: B-3（intentional_narrowing）、B-4（配位子数値なし）、A-4（ハライド種比較deferred）

**SRG-4 [立体選択性の機構的帰属と測定信頼性の同時不在]**

* **Primary RI**: RI-04 Unreplicated discriminator — cis/trans-DCE→スチルベン比率（80:20 と 43:57）が単一測定値であり、GLC分解能・較正・replication なしに立体化学的解釈の根拠として使用されている
* **Secondary RI**: RI-05 Qualitative overread — "anomalously enriched with the cis isomer" という立体化学的観察から機構的含意（「interesting mechanistic implications」）が即座に引き出されているが、速度論的/熱力学的制御の区別なし
* **ER**: 立体選択性データを機構的証拠として使用するためには、cis/trans比の測定再現性・GLC分解能確認（co-injection）・および少なくとも温度変化実験（速度論的制御の確認）が必要
* **EP**: EP-04a Discrimination / replication pack; EP-01a Reporting-coherence pack
* **Case-specific実装**: cis-/trans-スチルベンのGLC co-injection確認と分解能評価；同一反応条件での2–3回の独立反応による比率の再現性確認；異なる反応温度（-20°C, 0°C, 25°C）でのcis:trans比のtemperature dependence測定
* **注記**: A-2（deferred）、B-5（GLC reliability）。TEMPERATURE_SUMMARY: A-2+B-5は3/3収束、gap=none

**SRG-5 [分析的信頼性根拠の不在]**

* **Primary RI**: RI-01 Reporting integrity — GLC内部標準法の較正情報なし・キャラクタリゼーション基準の "and/or" 不統一・収率基準の混在
* **ER**: 定量的収率主張を評価するために、内部標準名・response factor・line range・測定精度（±%）の開示が必要
* **EP**: EP-01a Reporting-coherence pack
* **Case-specific実装**: 各収率エントリについての使用内部標準・較正条件・測定精度（例: ±3%）の開示；glpc、nmr、ir、mass spectraのエントリ別適用表
* **注記**: B-6（GLC校正不在）、B-7（and/or）。SRG-2と根が重複するが、分析的報告整合性の観点として独立に記録

---

SRG外: CLA

**CLA-1: 触媒のTON・均一系/不均一系問い**

* **Primary RI**: RI-02 Object identification — 黒色化混合物（example 1）が Ni(0)コロイド（不均一系）への転換を示唆するが、触媒の化学的同一性（均一系であり続けるか）が確認されていない
* **ER**: 触媒が均一系として機能していることを確認するためには、反応中のTON測定・反応後の溶液状態確認（遠心・ろ過の触媒活性比較）が必要
* **EP**: EP-02a Identity / purity substantiation pack
* **Case-specific実装**: 遷移金属ナノ粒子（不均一系）と均一系触媒を区別するためのHg中毒試験または反応溶液のろ過・触媒活性試験
* **注記**: A-3（deferred）、B-8（黒色化の非記録）。D-4-6として記録済み。

**CLA-2: Corriu-Masse同時投稿との化学的差別化不在**

* **Primary RI**: RI-09 External superiority — Ni-ホスフィン系の優位性がNi(acac)₂との実験的比較なしに主張されている
* **ER**: Note Added in Proof（脚注3a）で認識した同様のNiカップリング系との化学的差別化（基質スコープ・選択性・配位子効果の定量比較）が必要
* **EP**: EP-09a Internal benchmark pack
* **Case-specific実装**: NiCl₂(dpe)とNi(acac)₂の同一基質ペアでの収率・選択性の直接比較
* **注記**: C-3（Corriu-Masse、affects_claims: yes）、D-4-5として記録済み。

**Self-contradictory absence CLAチェック:**

U-1（eq.3がR–Rを予測するがTable IにR–Rデータなし）はSRG-1・SRG-2に属するが、独立CLA的重要性を持つ。上記SRG-1およびSRG-2の注記に記録済みのため追加CLAは不要。

---

### §3 現在のVQ判定

現在判定: **VQ-2 (Method)**

**VQ-1 (Observation) — 通過（条件付き）:**
Table I の 10 エントリは製品の生成を glpc・nmr・ir・mass（and/or）で確認しており（B-7が reporting_omission であることは non-fatal — era-norm toleranced）、VQ-1 要件の RI-02（生成物同一性確認）は基本的に満たされる。ただし確認方法の不統一（B-7: "and/or"）は Non-fatal で残存する。VQ-1は通る。

**VQ-2 (Method) — 通過（限定的）:**
VQ-2 要件: RI-01（条件記述・収率報告の一貫性）と RI-07（境界主張の実験的根拠）。

- RI-01: B-2（収率基準混在・質量収支不在）・B-6（GLC較正不在）として残存するが、通信形式のera-norm（下記§4）を考慮するとNon-fatal（当時の genre convention内）。
- RI-07: B-3（sp²限定の根拠不在）は残存するが、著者が boundary を positively framed しており intentional limitation として記録（Non-fatal for Method claim）。

→ VQ-2 は通る（SRG-2のRI-01・SRG-3のRI-07がnon-fatal前提）。ただし「限定的（Qualified）」: RI-05（配位子活性の定性的順位から構造的含意への overread、B-4）が残存するため VQ-2 (qualified)。

**VQ-3 (Mechanism) — 未達:**
VQ-3 要件: RI-03（観測されない説明変数）・RI-04（未複製の識別子）・RI-06（輸入モデル）（+ VQ-2継承）。

- RI-03（Fatal）: 触媒サイクルの中核種（中間体1・2・3）が未観測のまま。SRG-1のPrimary RI。
- RI-06（Fatal）: dipy-Ni系（ref 11）から dpe-Ni 触媒サイクル全体への類推が未検証。SRG-1のSecondary RI。
- RI-04（Non-fatal）: cis:trans比の単一測定（B-5、SRG-4）。

→ VQ-3 は未達。RI-03・RI-06が致命的に未解消。

**VQ-4 (Benchmark) — 未達（VQ-3未達のため継承原則により評価不可）:**
RI-08（SRG-2のSecondary RI: GLC較正不在）・RI-09（CLA-2: Corriu-Masse比較なし）も残存。

**層別VQ非対称性:**

Layer 1（合成実用性）単独では: Table I + Examples 1–2 のデータはVQ-2水準に到達している（方法としての記述は成立）。ただしU-1（R–R自己矛盾的不在）により "selective" の部分は実際にはVQ-1より下に留まる可能性。

Layer 2（機構的作業仮説）単独では: VQ-1止まり（eq.2–4は観察の定性的解釈に過ぎず、RI-03・RI-06が致命的）。

---

### §4 Era-Norm Annotation

**communication-era tolerated:**

- B-2（収率基準混在・質量収支不在）: 1972年JACS通信の standard genre では mass balance の完全開示は必須でなく、Table I形式での代表収率提示が許容慣行。当時は GC内部標準の詳細も通常省略された。
- B-6（GLC内部標準較正不在）: 分析化学的校正の詳細開示は1972年の合成通信には一般的に要求されなかった。
- B-7（キャラクタリゼーションの "and/or" 不統一）: 通信形式では全生成物への均一なキャラクタリゼーション開示は genre convention外であった。
- B-4（配位子活性順の数値なし）: 予備的なスクリーニング結果を順位のみで示すことは、詳細な比較研究を予告する通信の文脈では許容されていた（series_signal: yes）。
- A-3（TON・触媒失活の deferred）: 触媒の turnover 研究は Full Paper の領域であり、通信での省略は era-norm tolerated。

**modern-era deficient:**

- U-1（R–R ホモカップリングの自己矛盾的不在）: "selective cross-coupling" という主張の核心に関わるホモカップリング副生成物の定量が modern review では必須。「選択性の数値定義」は現代では VQ-2 要件として要求される。
- B-3（sp³ハライドの不反応性：実験なしの境界主張）: 現代基準では boundary claim には少なくとも失敗例の提示（0%収率または trace）が必須（RI-07 era-norm non-fatal → modern deficient）。
- SRG-4全体（cis:trans比の機構的帰属と再現性）: 現代の立体化学論文では replication と速度論的 / 熱力学的制御の区別が標準要件。当時は「anomalous」と記述するのみで通っていたが、現代基準では不足。
- CLA-2（Corriu-Masse比較の不在）: 同時投稿との化学的差別化は現代の novelty claim 審査では必須とされる。Note Added in Proof で認識しながら比較を行わないことは modern review では採択困難。

---

### §5 最短補強ルート

**目的関数: VQ-3 (Mechanism) への到達**（現在 VQ-2 qualified）

**VQ-3 への最短ルート:**

1. **EP-03a Direct-observation / state-assignment pack** — ジオルガノニッケル中間体（L₂NiR₂）の低温 ³¹P NMR または ¹H NMR による同定；stoichiometric 反応（NiCl₂(dpe) + 2 PhMgBr → Ph₂Ni(dpe), then + PhCl → PhNi(dpe)Cl + Ph-Ph）による個別素反応の確認。RI-03 を前進。

2. **EP-06a Analogy-validation pack** — dipy-Ni系（ref 11, Uchino et al.）の素反応とdpe-Ni触媒サイクルの対応関係を同一条件での化学量論的実験で検証；あるいはラジカルクロック基質を用いたラジカル経路の排除実験。RI-06 を前進。

3. **EP-04a Discrimination / replication pack** — cis/trans-DCE 実験の3回独立反応での比率再現性確認；異なる温度での cis:trans 比分布（速度論的制御の確認）。RI-04 を前進（VQ-3 qualified→ unqualified）。

**VQ-4 への最短ルート（VQ-3 達成後）:**

4. **EP-01a Reporting-coherence pack** — 全エントリの収率を substrate 基準に統一；GLC 内部標準（n-デカン）の response factor と校正曲線の開示；主要副生成物（R–R, olefin）の GLC 検出上限値の記録。RI-01・RI-08 を前進。

5. **EP-09a Internal benchmark pack** — 同一基質ペア（n-BuMgBr/PhCl）での NiCl₂(dpe)・NiCl₂(dpp)・Ni(acac)₂ の収率・TON 直接比較；エーテル vs THF の収率数値比較。RI-09 を前進。

認定ゲート順注記: 実験投入順は情報利得順（EP-03a → EP-06a → EP-04a → EP-01a → EP-09a）だが、最終認定は VQ-1 → VQ-2 → VQ-3 → VQ-4 のゲート順で確定する。EP-01a・EP-09a の投入は VQ-3 達成後に行う（VQ-2継承が確保された後）。

---

### §6 制度設計への寄与

**既存RIコードの代表事例:**

- **RI-06 サイクルレベル輸入（大規模モデル輸入サブタイプ）の典型事例**: Uchino et al.（ref 11）のdipy-Ni化学量論的反応が「Ni触媒クロスカップリング全サイクル」のアナロジーとして使用される。これはRI-06 scope注記（v0.3）の「個別素反応ではなく触媒サイクル全体の別系からの輸入」に完全に合致する事例として記録できる。
- **RI-07 拡張適用（否定的境界主張）の代表事例**: "Only C_sp² halides can be used" という境界主張（B-3）がsp³ハライドの実験的試みなしに提示される。これはRI-07の「〜のみ可能」境界主張のケースの合成化学における典型として記録。

**通信→Full Paper遷移の自動解消パターン:**

series_signal（A-1, A-2, A-3, A-4）のA項目全てが通信→Full Paper遷移での自動解消候補となる。SRG-2（収率報告の一貫性）・SRG-5（分析的信頼性）はFull Paper展開で典型的に自動解消される。これはera-norm §4で記録した項目（B-2, B-6, B-7, B-4）の通信→Full Paper遷移自動解消パターンとして制度設計に追加できる。

**RI共起パターン:**

SRG-1でRI-03とRI-06が共起しており、「輸入モデルが中間体の直接観測の代替として機能する」パターンが観察される。RI-06の解消（アナロジーの検証）だけではRI-03（中間体直接観測）の要件は満たされない——両方の独立解消が必要。この共起パターンは合成有機金属触媒サイクル論文の典型として記録する。

**否定的証拠の不完全性パターン（V2-Q10/U-1）:**

「R–Rが検出されなかった＝選択性の証拠」という使用において、R–Rの検出限界が示されないため「検出されない = 不在」と「検出されない = 感度以下」の区別がつかない。これはB-item flag "negative result as evidence" + U-1（self-contradictory absence）の組み合わせとして記録されており、RI-04 case-specific実装（mass balance 閉鎖と速度論的ウィンドウ評価なしの否定的証拠利用）の合成化学版として制度設計に追加できる。

**PRI候補への新規貢献:**

本ケースでは新規PRI候補は検出されなかった。既存PRI-11（Mechanism-kinetics decoupling）への貢献: 触媒サイクル（eq.2–4）から速度式を代数的に導出せずに選択性（cross vs homo）のみを観察で確認しているパターンはPRI-11定義に合致する（2報目の独立確認事例候補）。ただし現在Breitenfeld 2014 + Pengfei 2024の2報で確認済みのため、本ケースは3報目の追加確認として記録する。

本ケースは既存の制度設計を追加確認した（RI-03, RI-06, RI-07, RI-04の新事例として機能）。
