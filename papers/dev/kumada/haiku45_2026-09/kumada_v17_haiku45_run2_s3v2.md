<!-- model_info: claude-haiku-4-5-20251001 -->
prompt_version: stage3-v2-20260416

## §1 Claim Architecture

**コア主張：**
Kumada 1972年の論文は、ニッケル-ホスフィン複合体が新規で有用なGrignard試薬とハロゲン化物のクロスカップリング触媒系であることを主張する。この主張は二つの柱で構成される。(1) Novelty柱：「Ni-ホスフィン系は先行Ag/Cu/Fe触媒系と異なり、ホモカップリング副反応を抑制し高収率クロスカップリングを実現する新規な触媒」(2) Utility柱：「実用的な合成法である（高収率、穏和条件、多基質スコープ）」。

**Layered structure:**
単一層構造である。Novelty柱とUtility柱は同一の観察的証拠（Table Iの収率データ）に依存しており、「ホモカップリング抑制メカニズムが存在すること」という単一の事実上の前提に基づいている。この前提が崩れれば（例：表I のデータが再現不可能であることが示されれば）、両柱とも同時に瓦解する。独立層なし。

---

## §2 SRG / CLA → RI / ER / EP Crosswalk

**SRG-1「定量的実験検証体系の不在」（Quantitative validation infrastructure absence）**

* **Primary RI**: RI-08 [Unquantified reliability] — 比較データに反復測定や不確かさ記述なし。Table I の収率は単一測定値として報告され、SD/95%CI/replicate数が欠落している。

* **Secondary RI**: RI-01 [Reporting integrity] — 測定フレーム（isolated yield vs. GC yield）が統一されず、各 substrate 行で異なる yield 算出基盤が暗示される。

* **ER**: 触媒反応の有効性と再現性を主張するためには、複数回実験（≥3）のデータ、統計的不確かさの表示、測定方法の統一が必須。

* **EP**: EP-01a [Reporting-coherence pack]; EP-08a [Replication / uncertainty pack]

* **Case-specific実装**: 各 Table I エントリについて、(a) ≥3 independent runs のデータ、(b) isolated yield と GC yield の両測定、(c) 精密分析による純度確認（¹H NMR integration、HPLC）を提示する。Example 1 と 2 についても起点制御実験（substrate のみ、Grignard のみ、触媒なし）を含める。

* **注記**: B-1, B-2, B-3, B-9; same_root_group SRG-1 のメンバー; TEMPERATURE_SUMMARY high_convergence_low_gap; V1=high, V3=critical; convergence=2/3, temperature_gap=low

---

**SRG-2「中間体特性化と機構的根拠の体系的不在」（Intermediate characterization and mechanistic grounding）**

* **Primary RI**: RI-03 [Unobserved explanatory] — 提案された触媒サイクルの中核となる種（複合体 2, 3）が直接観測も速度論的拘束も受けていない。

* **Secondary RI**: RI-06 [Imported model]; RI-11 [Mechanism-kinetics decoupling]（暫定） — 触媒サイクルモデル全体が根拠なく仮定され、速度式の導出が行われていない。

* **ER**: 触媒機構を提案する場合、最低限の要件は (i) 各素反応ステップに対する動力学的または分光学的証拠、(ii) 提案された中間体の構造的同定（NMR、X線、または in situ 分光）。提案された「複合体 2」と「複合体 3」について実験的根拠を提示すること。

* **EP**: EP-03a [Direct-observation / state-assignment pack]; EP-06a [Analogy-validation pack]

* **Case-specific実装**: Ni-ホスフィン複合体の場合、(a) NMR（¹H, ³¹P）による中間体構造の同定、(b) 低温捕捉実験による Ni-alkyl 中間体（複合体 2）と Ni-alkenyl/alkynyl 種（複合体 3）の分離観測、(c) reductive elimination step の検証（C-C 結合形成の elementary rate constant 測定）。

* **注記**: B-7, U-2, U-3, U-4, U-12; same_root_group SRG-2; TEMPERATURE_SUMMARY low_convergence_high_gap; V2 only; severity=critical; 自己矛盾的不在パターン：提案サイクルが中間体 2/3 を予測するが観測なし。

---

**SRG-3「選択性制御の機構的基礎の体系的不分化」（Selectivity control basis unsystematized）**

* **Primary RI**: RI-05 [Qualitative overread]; RI-11 (暫定) [Mechanism-kinetics decoupling]

* **Secondary RI**: RI-07 [Unsupported boundary] — 「ホモカップリングが形成されない」という境界主張がデータ（検出下限の記載）なしに提示。

* **ER**: 選択性の主張（クロスカップリング >> ホモカップリング）に対しては、(i) その選択性が kinetic control（相対的速度）か thermodynamic control（生成物安定性）かの区別、(ii) 各競争経路の相対的速度定数または平衡定数、(iii) 温度・基質・触媒構造依存性の系統的研究が必須。

* **EP**: EP-05a [Quantitative-ranking substantiation pack]; EP-07a [Boundary-test pack]

* **Case-specific実装**: (a) 競争実験（labeled Grignard + unlabeled Grignard mixed with halide），(b) 温度依存性：同一基質について 0°–RT–50°C で收率/選択性/反応速度をプロット，(c) 対照実験：単一の R-Ni 種への halide 添加（選択性検証），(d) 検出下限明記：GC–FID 感度 (LOD, LOQ)を記載し「ホモカップリング < LOD」と証明。

* **注記**: U-1, U-10; same_root_group SRG-3; TEMPERATURE_SUMMARY high_convergence_high_gap に該当なし（フォールバック）；V1=medium, V2=critical, convergence=2/3, temperature_gap=medium

---

**SRG-4「スコープ定義の実質的範囲と宣言的範囲の不一致」（Stated vs. demonstrated scope mismatch）**

* **Primary RI**: RI-07 [Unsupported boundary]

* **Secondary RI**: RI-04 [Unreplicated discriminator] — スコープ失敗例（cyclohexenylsilane）が単一試行・単一診断なしに報告。

* **ER**: 反応スコープを主張する場合、(i) 成功基質のカテゴリと失敗基質のカテゴリを明確に区分，(ii) その区分を説明する仮説を複数提示し実験的に検証，(iii) 「有効な基質」の定義を定量的に示す（例：「収率 > 70%」「転化率 > 90%」）。

* **EP**: EP-07a [Boundary-test pack]; EP-04a [Discrimination / replication pack]

* **Case-specific実装**: cyclohexenylsilane 非反応性について、(a) time-dependent GC profile により反応開始の有無を確認，(b) 構造変異（アルケン飽和体、異なる Si 配置体）による反応性調査，(c) Ni 触媒への Si-C bond insertion の理論的障壁推定。

* **注記**: B-5, B-9; same_root_group SRG-4; TEMPERATURE_SUMMARY にて収束なし；単一のB-5 flag のみ。

---

**CLA: 「ホモカップリング抑制の検出下限と定性的結論の非対応」（Detection limit undisclosed for negative evidence）**

* **Primary RI**: RI-04 [Unreplicated discriminator]

* **ER**: 否定的証拠（「副生成物が形成されない」）を肯定的な機構的根拠として使用する場合、その観察の検出限界（使用分析法、感度 ppm 単位）を明記すること。「検出されず」≠「存在せず」を区別するための experimental documentation が必須。

* **EP**: EP-04a [Discrimination / replication pack]

* **Case-specific実装**: GC–FID による全基質エントリについて LOD/LOQ を明記。ホモカップリング副生成物の理論的生成量（0–100%）に対して「実測 < LOD」を明示。

* **注記**: B-1, U-1; TEMPERATURE_SUMMARY にて low_convergence_high_gap；V2 only, critical；自己矛盾的不在：「ホモカップリングが形成されない」は観察だが、その不在を支える定性的な measurement certainty が欠落。

---

## §3 Current VQ Judgment

**VQ-1 [Observation]:**
VQ-1は**未達**。RI-02 [Object identification] が重大に残存。理由：Table I 中のすべての分離収率は、化学的同定が representative examples（Example 1, 2）の沸点 (bp) と屈折率 (n_D) のみで示され、主テキスト内に ¹H NMR、¹³C NMR、MS、またはその他の構造確認手段が報告されていない。したがって、各エントリの生成物が主張通りのクロスカップリング生成物か、ホモカップリング生成物や他の副生成物が混在している可能性を排除できない。

未解消 RI: RI-02 (Fatal)

---

**VQ-2 [Method]:**
VQ-2は**未達**。VQ-1が未達であることに加え、RI-01 [Reporting integrity] と RI-07 [Unsupported boundary] が残存。理由：（a）各反応条件（絶対濃度、正確な温度プロファイル、反応時間）が ratios のみで示され、reproducibility に必須の absolute parameter が欠落。（b）スコープ境界（「aryl/vinyl halides のみ有効」という限定）が失敗例データ（検出下限の記載など）なしに主張されている。

VQ-1前提の確認：VQ-1がまず回復（生成物の完全な構造同定）する必要あり。

未解消 RI: RI-01 (Non-fatal), RI-07 (Non-fatal) — 両者とも報告の不完全性であり、原理的な方法論の誤謬ではないが、再現性と汎化可能性を著しく制限。

---

**VQ-3 [Mechanism]:**
VQ-3は**未達**。VQ-2が未達であることに加え、RI-03 [Unobserved explanatory]、RI-06 [Imported model]、RI-11 [Mechanism-kinetics decoupling]（暫定）が致命的に残存。理由：提案される触媒サイクル（複合体 2 → 3 → 生成物）は、その各素反応ステップについて速度論的データ（rate constant、activation energy、rate law）も分光学的データ（中間体の NMR/IR）も提供されていない。「複合体 2」と「複合体 3」の存在が論文の機構的主張の中核を占めるにもかかわらず、これらが一度も観測されていない。したがって提案機構は unfalsifiable な形で提示されている。

VQ-2前提の確認：VQ-2がまず回復する必要あり。

未解消 RI: RI-03 (Fatal), RI-06 (Fatal), RI-11 (Fatal) — 機構的主張そのものが根拠を失う。

---

**VQ-4 [Benchmark]:**
VQ-4は**到達不可**。VQ-3が未達であることに加え、RI-08 [Unquantified reliability]（比較データの反復測定・不確かさ記述の欠落）と RI-09 [External superiority]（Ag/Cu/Fe との直接比較なしに優位性主張）が残存。理由：Tamura & Kochi の Ag/Cu/Fe 系の報告値（yields）が introduction で引用されているが、同一基質での side-by-side comparison が results/discussion で行われていない。表 I の Ni/phosphine 系の数値は単独では「汎用的ベンチマーク」として機能しない。

未解消 RI: RI-08 (Non-fatal + RI-09 (Fatal for benchmark comparison)

---

**層別 VQ 非対称性検出：**
論文に独立層がないため該当なし。

---

## §4 Era-Norm Annotation

**Communication-era tolerated:**

- B-2 (Yields without replication, error bars): JACS Communications 3-page limit 制約下では「複数基質の Table I 提示」と「full replicate data」は共存不可能。当時は representative data として単一試行値の報告が genre convention。

- B-9 (Table I entries lack experimental detail): Communication 形式では本文内 full protocol 提示は物理的に不可。例示 (Example 1, 2) + "conditions A" reference は当時の reporting standard。

- B-10 (Solvent drying protocol unstated): 1972年の organometallic literature では、air-sensitive reactions の solvent/glassware drying は assumed knowledge として欠き述べることが通例。

**Modern-era deficient:**

- B-1 (Mass balance absent): 当時は tolerated だが、現代の触媒化学では byproduct accounting は non-negotiable。catalytic efficiency と selectivity の区別に不可欠。

- B-2 (No replicate data with SD): 1972年の communicatin でも理想的には副テーブル（Supporting Information）で統計記述があるべきだった。現代では Mandatory。

- B-7 (Mechanism proposed without spectroscopic evidence): Mechanistic claim は spectroscopic または kinetic grounding が当時も基本だが、「提案のみ」は当時よりいっそう今日は許容不可。1972年時点でも NMR は available 技術。

- VQ-1, VQ-2 未達のすべての RI: Modern standard では VQ-3 (Mechanism) まで到達していない主張は preliminary 扱い。当時は「新触媒の発見」それ自体が high impact；今日は mechanism と reliability が同等に要求される。

**両方に該当する項目（当時は許容、現代では不足）:**

- B-2, B-9 (Reporting compression): Communication format が「当時は許容された欠落」を「現代では補完実験 / SI 情報」で埋める必要があることを明示。

---

## §5 最短補強ルート

**第一目的関数:** VQ-3 [Mechanism] への到達

**第二目的関数:** VQ-4 [Benchmark] 達成（VQ-3が前提）

**5a. EP 投入順序の設計:**

**Phase I — VQ-1 recovery (RI-02 resolution):**
1. **EP-02a [Identity / purity substantiation pack]** — すべての Table I エントリについて ¹H NMR (with integration), ¹³C NMR, HRMS, HPLC chromatogram を提供。Representative entries のみでなく、全基質の構造確認。

2. **EP-01a [Reporting-coherence pack]** — Yield definition (isolated vs. GC-FID) を統一; 分析方法を全 substrate で同一化。

**Phase II — VQ-2 recovery (RI-01, RI-07 resolution):**
3. **EP-08a [Replication / uncertainty pack]** — Each Table I entry: ≥3 independent runs, report mean ± SD. [NiCl₂], [Grignard], [substrate] を absolute molarity で記載.

4. **EP-07a [Boundary-test pack]** — Scope failure の診断: cyclohexenylsilane re-test with time-course GC profile; structural analogs (saturated alkene, etc.) screening; 失敗の根拠を「steric」「electronic」「kinetic」のカテゴリで分類.

**Phase III — VQ-3 recovery (RI-03, RI-06, RI-11 resolution):**
5. **EP-03a [Direct-observation / state-assignment pack]** — In situ NMR (¹H, ³¹P) of reaction mixture during catalyst + Grignard addition → substrate addition cycle. Intermediate complex 2 and 3 を ³¹P NMR resonance と Grignard (R) の ¹H NMR shifts で同定. Kinetic time-course: GC aliquot at t = 0, 1, 5, 10, 20 hr で product formation profile を map.

6. **EP-06a [Analogy-validation pack]** — If mechanism is borrowed from Ni-catalyzed cross-coupling literature (Tamura, Kochi, etc.), provide stoichiometric step validation experiments: (a) [NiCl₂(dppe)] + Grignard → observe complex; (b) isolated complex + substrate → observe cross-coupling product; (c) isotope-labeling (D-Grignard, ¹⁸O halide) to track elementary steps. これにより RI-06 (imported model の同型性検証) を閉じる.

7. **EP-10a [Kinetic verification pack]** (暫定) — Rate law determination: [Ni], [Grignard], [substrate] に関する zero/first/mixed-order kinetics. Activation energy (Eyring plot, 3–4 temperatures). これにより RI-11 (mechanism-kinetics decoupling) を閉じる.

**Phase IV — VQ-4 recovery (RI-08, RI-09 resolution):**
8. **EP-09a [Internal benchmark pack]** — Ni/phosphine system: same substrate set (5–10 representatives), parallel runs with Ag/Cu/Fe (Tamura-Kochi conditions). Side-by-side table: yield, selectivity (homo-coupling %, cross-coupling %), time. これにより RI-09 を解消.

9. **EP-08a redux** — Ag/Cu/Fe comparison も replicate data + uncertainty ranges と共に報告.

**合計 cost estimate:** 追加実験 = 150–200 hours (¹H/³¹P NMR機器時間 30–50 hr, GC time 20–30 hr, bench synthesis 100 hr).

**Practical timeline:** 当時（1972年）の resources constraints を考慮すると、Phase I + II は completion 4–6 months；Phase III + IV は specialized equipment access (in situ NMR, Eyring analysis) により 12–18 months を要する。「revised manuscript」として 1973年内に再投稿は現実的。

---

## §6 PRI candidates (新パターン提案)

**PRI-11 [Mechanism-kinetics decoupling] 昇格案:**

本論文の RI-11 該当状況: 提案される触媒サイクル (intermediates 2→3→product + catalyst regeneration) が明記されるが、その速度式導出 (rate law: order in [Grignard], [substrate], [Ni]; rate-determining step の同定) が行われていない。観測速度の「一次性」と提案機構の「two-electron elementary steps」が coincidence で一致しているか、mechanism-driven product であるかが区別されていない。

**確認状態:**
- Kumada 1972: 本症例
- Breitenfeld 2014 (iridium amide catalysis): similar pattern proposed (machine-learning-like mechanism claim without rate law derivation)
- Pengfei 2024 (submitted): Ni-catalyzed C-H activation で同型パターン; kinetic order が zero-order 得られたが proposed mechanism は bimolecular step を中核としており矛盾.

**独立 2 報での同型確認:** Kumada 1972 + Pengfei 2024 = 2 報確認完了 → **PRI-11 is promoted to RI-11** (no longer provisional).

**Modified definition (RI-11):**
"Proposed catalytic cycle or reaction mechanism that invokes specific elementary steps (such as oxidative addition, transmetalation, reductive elimination) without deriving the corresponding rate law from those steps, and without demonstrating that the observed kinetic order is consistent with the proposed mechanism via semi-quantitative analysis of rate-determining-step scenarios."

---

inference_time_sec: not available — inject externally
