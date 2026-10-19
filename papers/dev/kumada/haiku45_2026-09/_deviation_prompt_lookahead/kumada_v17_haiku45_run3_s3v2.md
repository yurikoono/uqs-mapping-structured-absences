<!-- model_info: claude-haiku-4-5-20251001 -->
```
prompt_version: stage3-v2-20260416
model_info: claude-haiku-4-5-20251001

[§1] Claim Architecture

Core claim (Novelty + Utility): Nickel-phosphine complexes catalyze selective cross-coupling of Grignard reagents with vinyl/aryl halides, demonstrating a new preparative method with broad substrate scope (diverse Grignard reagents, diverse halides) and high yields, tolerating β-hydride-bearing Grignard reagents.

Layered structure: YES. Four independent claim layers—(a) catalytic coupling exists, (b) selectivity for cross-coupling over homo-coupling, (c) broad substrate scope, (d) β-hydride tolerance—are logically independent. Refutation of layer (b) does not collapse (a), (c), or (d). Interdependence: Layers (a) and (c) are interconnected (broader scope is demonstrated within the catalytic framework). Layer (d) requires layer (a) as prerequisite but not vice versa. Layer (b) (selectivity) is central to utility but could theoretically be disproven while (a) and (c) remain intact.

---

[§2] SRG / CLA → RI / ER / EP Crosswalk

**SRG-1: Mechanism hypothesis without experimental evidence**
* **Primary RI**: RI-03 [Unobserved explanatory]
* **Secondary RI**: RI-06 [Imported model]
* **ER**: The proposed catalytic cycle (eq 2–4) must be validated by direct observation of intermediates, kinetic rate-law derivation, or mechanistic probes (crossover, isotope labeling, radical clocks).
* **EP**: EP-03a [Direct-observation / state-assignment pack]; EP-06a [Analogy-validation pack]
* **Case-specific実装**: Ni(II)diorgano intermediate 1, (halo)(organo)intermediate 2, and reductive-elimination step 3 must be characterized by NMR (in situ), stopped-flow kinetics, or stoichiometric intermediate synthesis; mechanism must be distinguished from π-allyl pathways by spectroscopy and isotope labeling (e.g., D-labeled Grignard to detect stereoselectivity retention).
* **注記**: A-1, A-2, A-3, A-4, A-5, A-7, A-12, A-14, B-11; high_convergence_high_gap (A-1, A-14); high_convergence_low_gap (A-7, A-10); same_root_group; convergence 3/3, 2/3; gap=high, none, medium

**SRG-2: Yield measurement basis inconsistency**
* **Primary RI**: RI-01 [Reporting integrity]
* **Secondary RI**: RI-08 [Unquantified reliability]
* **ER**: Yield calculation must use uniform basis (isolated yield for all entries, or glpc-only with explicit calibration) and must include mass-balance closure and replicate measurements with uncertainty reporting.
* **EP**: EP-01a [Reporting-coherence pack]; EP-08a [Replication / uncertainty pack]
* **Case-specific実装**: Table I entries must distinguish isolated yield vs glpc yield in footnotes; isolated yields ≥3 replicates with SD reported; glpc calibration standard specified (internal vs external, calibration curve); mass balance for each substrate (recovered starting material + cross-coupled product + homo-coupling byproduct + other byproducts = 100%, within analytical uncertainty).
* **注記**: B-2, B-15, V1-Q6, V1-Q15, V3-Q1, V3-Q6, V3-Q10; high_convergence_high_gap (B-2); high_convergence_low_gap (B-15); exception to consolidation per OI-004; convergence 3/3, 2/3

**SRG-3: Catalyst state characterization absent**
* **Primary RI**: RI-02 [Object identification]
* **Secondary RI**: RI-03 [Unobserved explanatory]
* **ER**: Black mixture formed during reaction must be chemically identified (elemental analysis, powder XRD, SEM, XPS) and its fate documented (removed vs carried into product); this data is necessary to distinguish viable Ni(II) cycles from decomposition pathways.
* **EP**: EP-02a [Identity / purity substantiation pack]; EP-03a [Direct-observation / state-assignment pack]
* **Case-specific実装**: Black solid isolated from Example 1 and Example 2 reactions, analyzed by elemental analysis (C/H/Ni ratio), powder XRD pattern (vs NiCl2, Ni(0), NiO), SEM/TEM (particle size, morphology), X-ray photoelectron spectroscopy (Ni 2p, 3p oxidation states). Catalyst recycling test: black solid recovered from reaction, reused in fresh coupling, product yield measured to assess reversibility.
* **注記**: B-7, U-2; self-contradictory_absence flag; convergence 3/3; same_root_group

**SRG-4: Experimental parameter documentation gaps**
* **Primary RI**: RI-08 [Unquantified reliability]
* **ER**: Reaction conditions must be specified as single values or narrow ranges, with time-course data provided; stoichiometry, catalyst loading, temperature, and time must be held constant across substrates for direct scope comparison.
* **EP**: EP-01a [Reporting-coherence pack]; EP-08a [Replication / uncertainty pack]
* **Case-specific実装**: Grignard reagent/halide ratio standardized to 1.2 (±0.1) for all entries; catalyst loading reported as exact mol% (e.g., 1.0 ± 0.1 mol% or a single concentration value, not a range 1–0.1%); reaction time and temperature held constant (exception noted when substrate-specific variation is required; in that case, rationale stated). Time-course study (glpc sampling at 1, 5, 10, 20 hr) for at least 2 representative substrates to establish whether yield vs time curve plateaus (rate-limiting step assessment).
* **注記**: B-5, B-9, B-14, B-18, B-19; high_convergence_high_gap (B-5); high_convergence_low_gap (B-9); convergence 2/3, 2/3

**SRG-5: Selectivity mechanism uninvestigated**
* **Primary RI**: RI-03 [Unobserved explanatory]
* **Secondary RI**: RI-05 [Qualitative overread]
* **ER**: Suppression of homo-coupling and regioselectivity of the cross-coupling product must be explained by kinetic or thermodynamic analysis (relative rates of competing reductive eliminations, equilibrium distributions); selectivity cannot rest on qualitative observation alone.
* **EP**: EP-03a [Direct-observation / state-assignment pack]; EP-05a [Quantitative-ranking substantiation pack]; EP-10a [Kinetic verification pack]
* **Case-specific実装**: Cross-coupling yield / (cross-coupling + homo-coupling) ratio measured and reported for each substrate; byproduct distribution analyzed by glpc (or HPLC if hydro-silanes). Kinetic selectivity test: reaction under same conditions but stopped at earlier timepoints; ratio of cross-/homo-product vs time measured to assess whether selectivity is kinetically controlled (ratio constant over time) or thermodynamic (ratio changes as starting material depletes). For cis/trans-dichloroethylene: extended reaction time (20 hr → 50 hr) to determine whether stereoselectivity ratio is stable (kinetic) or changes (thermodynamic equilibration).
* **注記**: B-3, B-4, B-20, A-5, A-6, A-13; high_convergence_high_gap (A-5, B-20); convergence 3/3, 3/3

**CLA-1: Turnover number quantification**
* **Primary RI**: RI-04 [Unreplicated discriminator]
* **Secondary RI**: RI-03 [Unobserved explanatory]
* **ER**: Catalytic turnover must be quantified (moles of product / moles of Ni) to distinguish true catalysis from stoichiometric coupling; without TON data, the claim "catalytic cycle" cannot be verified.
* **EP**: EP-04a [Discrimination / replication pack]; EP-10a [Kinetic verification pack]
* **Case-specific実装**: For each reaction in Table I, calculate TON = (moles of isolated product) / (moles of [NiCl2(dpe)] used). Report TON values and compare across substrates. Construct Ni-loading series (varying [NiCl2(dpe)] from 0.5 mol% to 5 mol%) on one substrate; plot TON vs mol% Ni to establish whether TON is constant (true catalysis) or decreases with Ni loading (stoichiometric coupling). High-TON demonstration: scale-up experiment using catalytic Ni loading (≤1 mol%) on 1 mol scale of coupling to prove catalyst is genuinely regenerated and reused.
* **grounded_in**: A-1, A-4, B-6, U-1 (self-contradictory absence)
* **temperature_note**: high_convergence_high_gap (A-1, convergence 3/3 gap=high; B-6 convergence 3/3 gap=none); U-1 self_contradictory
* **same_root_group**: "Mechanism hypothesis without experimental evidence"

---

[§3] 現在のVQ判定

**VQ-1 [Observation]**: 未達。RI-02（object identification）が未解消。触媒の黒色混合物の化学的同定がないため、生成物がNi(0)などの副産物を含有する可能性が排除されない。また収率のglpc vs分離のばらつき（RI-01）により観測の信頼性が限定的。

**VQ-2 [Method]**: 未達。RI-01（reporting integrity）が未解消。化学量論パラメータが「範囲」で報告され、各基質での値が不明。RI-07（unsupported boundary）が未解消。「sp2のみ可能」と限界が述べられるが、sp3基質の失敗例（yield, reaction time等の詳細）が報告されていない。B-5, B-9の「最適化欠如」「パラメータ不統一」がVQ-2突破を阻害。

**VQ-3 [Mechanism]**: 未達（qualified）。RI-03（unobserved explanatory）と RI-06（imported model）が重大に未解消。提案された機構（eq 2–4）は原論文テキストに仮説（working hypothesis）と明記され、実験的根拠（NMR中間体、kinetics、mechanistic probes）が全く欠如。RI-05（qualitative overread）も残存：ホモカップリング抑制を「高選択性」と称するが、定量的な cross/homo比が報告されていない。A-1~A-12, B-11の機構演繹系全体がVQ-3を阻止。ただし**substrate scope実証**（Table I）単独では、基質適用性の方法論的妥当性のみに限定すればVQ-2相当に到達する可能性あり。

**VQ-4 [Benchmark]**: 未達。RI-08（unquantified reliability）と RI-09（external superiority）が未解消。Table I は単一測定（replicate測定なし、SD記載なし）。Tamura-Kochi（Fe catalyst）との数値ベンチマーク比較が主テキスト内で実施されていない。B-15（glpc vs分離の混在）と§3全体のVQ-2未達が VQ-4 継承を阻止。

**Era-Norm依存性**: B-2, B-5, B-6, B-7, B-11（機構仮説）は1972年 JACS通信形式では許容される。一方、現代基準ではRI-01, RI-03が致命的（fatal）。

---

[§4] Era-Norm Annotation

**communication-era tolerated（1972年 JACS 通信形式の慣行内で許容）:**
- **B-2** (yield basis mixing, glpc vs isolated): 通信形式の2ページ紙幅制約では、全基質について分離収率を報告することは物理的に不可能。glpc速報値の報告は当時の慣行。
- **B-5** (optimization absence): 通信形式は「新規方法論の初報表」であり、最適化study（parameter screening）は Full Paper 後続報論文に委ねるのが慣例。
- **B-11** (mechanism は hypothesis): 提案機構を「working hypothesis」と明記し、詳細研究は「Further studies required」と explicitly defer することで、当時の論文倫理では許容された。
- **A-14** (deferred mechanistic details): 通信は現象提示に限定され、機構的深掘りは後続研究予告で closure とするのが genre convention。

**modern-era deficient（現代基準では不足と判定）:**
- **B-2** (yield basis): 現代は全基質について isolated yield を報告するのが standard（紙幅の制約は PDF supplement で解決可能）。glpc値だけでは定量性評価が困難。
- **B-6** (black mixture 未同定): 触媒再利用・ニッケル-ハライドサイクル検証に必須。現代は XRD, XPS 等で $10分で同定可能。当時は技術制約だが、現代は怠慢。
- **B-11** (mechanism hypothesis): NMR, kinetics 等の証拠手法は1970年代でも available（Monnereau 2009, Breitenfeld 2014 parallels）。現代はRI-03 未解消は mechanism claim の根拠不足として致命的。
- **RI-01, RI-04**: 通信形式では tolerance限度だが、VQ-3/VQ-4評価の際は現代基準を適用すれば「不足」と判定される。

**両方に該当（当時は許容、現代は不足）:**
- A-1~A-12 (全機構演繹の defer): 当時は「通信その後の full paper 予告」で許容。現代は「発表時点で機構check が必須」と期待度が上昇（分子レベル理解の重視）。

---

[§5] 最短補強ルート

**VQ-2 到達の最短ルート（VQ-1 通過を前提）:**
1. **EP-01a** [Reporting-coherence pack] — Table I 全基質について isolated yield に統一し、glpc 標準品の調製方法・キャリブレーション曲線を記載。 RI-01 を前進。
2. **EP-02a** [Identity / purity substantiation pack] — 黒色固体の XRD、XPS（Ni 酸化状態）、元素分析（Ni ratio）。 RI-02 を前進。
3. **EP-07a** [Boundary-test pack] — sp3 基質（例：n-BuI）の失敗実験（yield 0%, 転化率 10% 等）を報告し、「sp2 のみ有効」の限界主張に根拠を付与。 RI-07 を前進。
4. **EP-08a** [Replication / uncertainty pack] — 3 基質について 3 重測定、SD 記載。パラメータ（stoichiometry, Ni mol%, 反応時間）を固定値で統一報告。 RI-01, RI-08 を前進。

認定ゲート順注記：実験投入順は情報利得順（RI複数同時前進を優先）だが、最終的な VQ-2 認定は RI-01 → RI-07 → RI-08 全解消時点で成立。

**VQ-3 到達の最短ルート（VQ-2 通過を前提）:**
1. **EP-03a** [Direct-observation / state-assignment pack] — (a) in situ ³¹P NMR (CD₂Cl₂, -40°C) で Ni(II)diorgano, Ni(II)-halide intermediate の observation；(b) Stopped-flow kinetics で各 elementary step の rate constant 測定；(c) Isotope labeling（D-Grignard, ¹³C-halide）で 各 step の stereo/regiochemistry を検証。 RI-03 を前進。
2. **EP-04a** [Discrimination / replication pack] — π-allyl pathway を排除するため、cyclopropane clock（例：cyclopropylmethyl Grignard）を使用；σ-alkyl 経由なら rearrangement なし、π-allyl 経由なら ring-opening product 観測。 RI-04 を前進。
3. **EP-06a** [Analogy-validation pack] — Proposed Ni(II) cycle の各 step（oxidative addition, transmetalation, reductive elimination）を stoichiometric Ni(II) complex 実験で検証；例えば [NiCl(dppe)](R') + R-X → R-R' を分離された Ni(II) intermediate で実証。 RI-06 を前進。

認定ゲート順注記：VQ-3 認定は RI-03, RI-04, RI-06 全解消を継承原則で要求。

**VQ-4 到達の最短ルート（VQ-3 通過を前提）:**
1. **EP-08a** [Replication / uncertainty pack] — Table I を「異なる 5 試験者、異なる装置」で reproduce；inter-lab reproducibility variance を報告。 RI-08 を前進。
2. **EP-09a** [Internal benchmark pack] — Tamura-Kochi (Fe catalyst) ニッケル counterpart を同一条件で並行実施；coupled product yield の直接比較。 RI-09 を前進。

---

[§6] 制度設計への寄与

**既存 RI コードの代表事例提供：**
- **RI-03 (Unobserved explanatory)**: Kumada は「機構仮説を立てながら中間体を全く観測していない」典型例。RI-03 の「工業的応用期への遡及拡張」検討材料。
- **RI-06 (Imported model)**: π-allylic complex 文献（Corey-Posner）を cited only で、σ-alkenyl path との区別実験なく選択。RI-06 の「catalytic cycle level import」好例。

**新しい PRI 候補の提案なし（但し 検証検討項目）：**
- PRI-10 (Kinetic overclaim) との関連：「high yield」主張が速度論データなしで asserted される点は PRI-10 類似。しかし本論文は「速度向上」を主張していないため PRI-10 不適用。

**VQ 判定基準の境界条件への知見：**
- **Era-norm 依存性の明確化**: 1972 年通信形式では B-2, B-5, B-11 は許容。現代では同じ internal 証拠に基づき致命的。これは VQ 基準の時代相対性を示す（相対性ではなく、現代基準の厳密化と解釈）。
- **Layered claim 層別 VQ**: Substrate scope（層1）は methodological 妥当性（RI-07 検証で VQ-2 相当）達成可能。Selectivity mechanism（層2）は RI-03 未解消で VQ-2 未達のまま。層別 VQ 非対称性が論文の「強さの非均質性」を露呈。

**EP 辞書への case-specific 実装例追加：**
- **EP-03a** [Direct-observation]: Ni(II) diphosphine intermediate characterization は NMR (³¹P, ¹H)、stopped-flow kinetics、isotope labeling の bundle として実装。単独 NMR では insufficient（intermediate 寿命が秒以下なら in situ detection 困難）。
- **EP-07a** [Boundary-test]: Sp2/sp3 区別は「失敗例報告」が必須（「sp3 は試していない」では RI-07 未解消）。失敗例は yield 数値 + 反応条件（time, temp）+ 側生物検出限界を記載。

**Labeling mismatch 検出：**
- Title: "Selective ... Catalysis by Nickel-Phosphine Complexes" → suggests broad-scope claim
- S0-1 core claim: "new and useful preparative method" → suggests utility-centered claim
- Actual text: "working hypothesis" + "Further studies required" → deferred mechanism claim
  
**通信→Full Paper 遷移での自動解消パターン：**
- B-2, B-5, B-11 は Kumada group の後続論文（1973-1975）でどの程度解消されたかが検証ポイント。推定：B-2 (yield basis) は Full Paper で機械的に分離収率に統一されるはず（SRG-2 自動解消）。B-11 (mechanism) は後続 kinetics 論文の有無で決定。

inference_time_sec: not available
```
