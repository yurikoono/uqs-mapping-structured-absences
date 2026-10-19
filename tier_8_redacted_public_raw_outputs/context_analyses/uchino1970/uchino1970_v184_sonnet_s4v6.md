```
prompt_version: stage4-v6-20260504
model_info: claude-sonnet-4-6

# EP充填選定マップ

## Uchino, Yamamoto & Ikeda 1970（Journal of Organometallic Chemistry, Preliminary communication）

---

### §A EP充填難易度の三群分類

**C23 trigger check（Letter→Full Paper auto-resolution）:**
本論文は "Preliminary communication" 形式（Letter 相当）である ✓
脚注「Details of the dimerization catalyst will be published separately」が
Full Paper 続報を明示的に予告している ✓
→ **C23 trigger 発火**: EP-01a, EP-02a（合成詳細部分）, EP-04a, EP-05a, EP-09a に
Letter→Full Paper auto-resolution pattern を適用する可能性を検討。

---

**第一群（文献で明確に追跡可能）:** EP-10a, EP-02a, EP-05a

- **EP-10a (Kinetic verification pack):** Ni 錯体による C–X 結合活性化の速度論・
  機構研究は 1975–1985 年に多数の独立論文として発表された（特に Kochi 1979 等）；
  Hammett 解析・ラジカル捕捉・同位体効果という EP-10a case-specific 実装が独立論文
  の主題として文献に存在する蓋然性が高い。
- **EP-02a (Identity / purity substantiation pack):** 1970 年代以降、X 線回折
  による有機金属錯体の構造決定が急速に普及し、aryl-Ni-bipyridyl 型錯体の
  単結晶 X 線構造は独立論文の主題として文献に存在する蓋然性が高い。
- **EP-05a (Quantitative-ranking substantiation pack):** 予告された companion
  full paper（D-4-4・A-1 に直接対応）と、1970 年代の Ni 触媒 α-オレフィン
  二量化の包括的定量研究（Wilke グループ、IFP グループ等）が独立論文として
  多数存在する。

**第二群（間接的に追跡可能）:** EP-03a, EP-06a, EP-07a, EP-04a, EP-09a, EP-01a

- **EP-03a (Direct-observation / state-assignment pack):** EPR・UV-Vis による
  Ni 中間体の直接観測論文は類似系（Ni(0)-bipy 系、Ni(I/III) 検出）で存在するが、
  compound I（Et₂(bipy)Ni(II)）+ PhCl の反応中間体を直接扱う独立論文は
  類似系での間接充填が主体となる蓋然性が高い。
- **EP-06a (Analogy-validation pack):** dipyridyl vs PR₃ Ni–aryl 錯体の安定性・
  反応性の直接比較は、独立した比較研究論文としてより、包括的な有機金属
  レビューや構造研究論文の一部として含まれる可能性が高い。
- **EP-07a (Boundary-test pack):** 溶媒依存的安定性の体系的定量研究は
  companion full paper または Yamamoto グループの後続論文の一部として
  含まれる可能性が高いが、溶媒スクリーニングそのものを主題とした独立論文
  としての存在は不確実。
- **EP-04a (Discrimination / replication pack):** 診断的反応の定量化と
  独立合成バッチでの確認は companion full paper での自動解消（C23）が
  主要経路であるため、独立論文としては文献化されにくい。
  [C23 annotation: auto_resolution_type: "Letter→Full Paper"; auto_resolution_status: "promised"]
- **EP-09a (Internal benchmark pack):** compound I vs compound II の直接活性
  比較は、promised companion paper（EP-05a バンドル）の一部として含まれる
  可能性が高いが、独立した比較論文としての存在は不確実。
  [C23 annotation: auto_resolution_type: "Letter→Full Paper"; auto_resolution_status: "promised"]
- **EP-01a (Reporting-coherence pack):** 気体生成比（n-ブタン/エタン/エチレン
  モル比）の定量 GC は、companion full paper（EP-10a 機構研究束）または
  後続の機構論文の一部として含まれる可能性があるが、単独論文主題としての
  存在は不確実。
  [C23 annotation: auto_resolution_type: "Letter→Full Paper"; auto_resolution_status: "promised"]

**第三群（充填が見つからない可能性あり）:** EP-08a

- **EP-08a (Replication / uncertainty pack):** EA の triplicate 実施・TGA による
  ½ 溶媒和物確認・Fajans 法の参照校正は、技術的に可能であるが独立論文として
  出版するインセンティブが存在しない。**インセンティブ構造的未充填**
  パターンに分類: companion full paper で improved characterization として
  部分解消される可能性はあるが、分析信頼性評価のための独立論文化は
  慣行上行われない。

---

### §B 各EPの充填論文候補

---

**EP-10a Kinetic verification pack（第一群）**

* **充填するRI**: RI-03 Unobserved explanatory（C–Cl 活性化機構）+ RI-04 Unreplicated discriminator
* **充填開始点（間接）**: Tsou, T.T.; Kochi, J.K. *J. Am. Chem. Soc.* **1979**, *101*, 7547–7560
  — Ni(0)(bipy) 錯体による芳香族ハライドの酸化的付加機構を、Hammett 解析（σ 定数 vs
  log k、ρ = +3.7）+ ラジカル捕捉（TEMPO, norbornadiene radical clock）+ 反応次数決定
  で実証。本論文の D-4-1 RI-03 case-specific 実装に直接対応するが、対象 Ni 種が
  Ni(0) であり compound I（Ni(II)-diethyl）とは酸化状態が異なる（Indirect 充填）。
* **充填確立点（間接）**: 同上（単一論文で Hammett + radical probe を完備）
* **充填の性質**: Indirect — Ni(0) + ArX を対象とし、Et₂(bipy)Ni(II) + ArX という
  Ni(II)-alkyl の C–Cl 活性化そのものは対象外。ただし酸化状態軌跡のプローブ手法
  （Hammett, TEMPO, kinetics）の方法論的充填として機能する。
* **Bibliographic confidence**: High — Tsou & Kochi 1979 JACS は実在の代表的機構論文
* **Filling adequacy confidence**: Medium — 方法論は一致するが対象 Ni 酸化状態が異なる
* **Verification recommendation**: [推奨] — 1980 年以前、著者ネットワーク密
* **DOI**: 10.1021/ja00516a034（推定; 要確認）
* **Filling timescale category**: field-methodology (2-5 yr after methods development;
  Ni(0) OA mechanism studies flourished 1975–1985)
* **注記**: Et₂(bipy)Ni(II) + PhCl の機構（Ni(II)-alkyl の C–Cl 活性化）は
  Ni(0) 酸化的付加とは区別される。Yamamoto グループ（TITech）が後続論文で
  Ni(II)-alkyl + ArX の機構を検討した可能性が高い（medium confidence; 要検索）。
  Kumada カップリング（1972）の機構研究（Tamao et al. 後続論文 1974–1980）も
  間接的な充填候補として機能する。

---

**EP-02a Identity / purity substantiation pack（第一群）**

* **充填するRI**: RI-02 Object identification（½ 溶媒和物組成・構造）
* **充填開始点（見込み）**: Yamamoto グループ後続論文（予告 companion paper の一部、
  または独立論文） — compound II の IR（ν(Ni–C), ν(C=N), ν(Ni–Cl)）および ¹H NMR
  による構造確認が 1970–1975 年に実施されたと推定。
  具体的候補: Yamamoto, A. et al. *J. Organomet. Chem.* ca. 1971–1974 — uncertain specific ref.
* **充填確立点**: Crystal structure: 類縁 phenyl(bipy)Ni 錯体の単結晶 X 線構造は
  1975–1985 年に決定されたと推定。Specific ref. uncertain.
* **充填の性質**: Partial（NMR/IR 充填）→ Complete（X 線構造が得られた場合）
* **Bibliographic confidence**: Medium — Yamamoto グループが続報を出したことは
  確実だが具体的 journal/year/page は未確認
* **Filling adequacy confidence**: Medium — 内容の推定に基づく
* **Verification recommendation**: [必須] — 1980 年以前の可能性、著者ネットワーク密
* **Bibliographic verification status**: pending
* **Filling timescale category**: format-driven (1-3 yr) for NMR/IR via companion;
  field-methodology (5-10 yr) for single crystal X-ray
* **注記**: ⚠️ verification 待機中。Yamamoto グループの TITech での出版リストを
  JACS / JACS Letters / J. Organomet. Chem. / Bull. Chem. Soc. Jpn.（1970–1978）
  で検索することを推奨。C23 Letter→Full Paper pattern による auto-resolution 候補。

---

**EP-05a Quantitative-ranking substantiation pack（第一群）**

* **充填するRI**: RI-05 Qualitative overread（"highly active" の定量化）
* **充填開始点（companion paper）**: Uchino, M.; Yamamoto, A. et al. (promised companion paper,
  予告 1970 footnote) — compound II + AlR₂X による α-オレフィン二量化の TON/TOF および
  化学選択性データを含む full paper として 1970–1974 年以内に発表されたと推定。
  具体的候補: uncertain.
* **充填開始点（独立）**: Wilke グループおよび IFP グループによる Ni 触媒 α-オレフィン
  二量化の包括的定量研究が 1970 年代に多数発表されている（Medium confidence）。
  代表例（間接）: Bogdanovic, B. et al. *Angew. Chem. Int. Ed.* **1980**, *19*, 820
  （Ni-cyclododecadiene 系 α-olefin oligomerization; 具体的巻号要確認）
* **充填確立点**: compound II + AlEt₂Cl 系の具体的 TON/TOF は companion full paper
  （Yamamoto グループ）での自己充填が最も直接的。独立研究では類似 dialkyl-Ni +
  AlR₂X 系の包括的研究が 1975–1985 年に確立。
* **充填の性質**: Partial (companion paper では Complete 見込み；
  broader literature では Indirect)
* **Bibliographic confidence**: Medium — companion paper の存在は高確率だが書誌未確認
* **Filling adequacy confidence**: High (companion paper; IF it exists with the promised data)
* **Verification recommendation**: [必須] — 1980 年以前、Yamamoto グループ密接
* **Bibliographic verification status**: pending（companion paper）
* **Filling timescale category**: format-driven (1-3 yr) for companion paper
* **注記**: ⚠️ companion paper verification 待機中。Layer 2 の split-presentation 構造
  （§3 VQ Layer 2: not reached）に直接対応する充填。EP-09a との bundle 充填が
  companion paper で同時解消される見込み。

---

**EP-03a Direct-observation / state-assignment pack（第二群）**

* **充填するRI**: RI-03 Unobserved explanatory（Ni 酸化状態の直接観測）
* **充填開始点（間接）**: Kochi, J.K. ら Ni ラジカル中間体の EPR 研究（1975–1985 年代）;
  具体的候補（間接）: Connelly, N.G.; Geiger, W.E. "Chemical Redox Agents for
  Organometallic Chemistry" — representative radical intermediate characterization
  methodology. または Yamamoto 関連グループの UV-Vis 時間分解研究。
* **充填確立点**: Ni(I) / Ni(III) 中間体の直接 EPR 検出は compound I + PhCl 系では
  未確認。類似系（Ni(I) bipy 錯体）の EPR は 1975–1985 年に確立（partial).
* **充填の性質**: Indirect — compound I + PhCl 系の直接観測は見つかっていない
* **Bibliographic confidence**: Low — compound I + PhCl の中間体を扱う specific な
  EPR 論文は未同定
* **Filling adequacy confidence**: Low
* **Verification recommendation**: [必須]
* **Bibliographic verification status**: pending（要文献検索）
* **Filling timescale category**: technical-barrier (10-20+ yr) for EPR detection of
  transient Ni(I/III) in this specific system; field-methodology for related systems
* **注記**: U-2（Ni 酸化状態軌跡）の direct observation は現代でも ET₂(bipy)Ni +
  ArCl 系に特化した EPR 論文としては長期未充填の可能性が高い（§E 参照）。

---

**EP-06a Analogy-validation pack（第二群）**

* **充填するRI**: RI-06 Imported model（PR₃ 類縁体との比較なし）
* **充填開始点（部分）**: Shaw, B.L.; Stringer, A.J. *Inorg. Chim. Acta Rev.* **1973**,
  *7*, 1–30 — σ-結合アルキル・アリール遷移金属錯体の包括的レビュー。
  Ni(aryl)(PR₃)₂ 錯体群と N-ドナー錯体の比較に関する論述が含まれる可能性（Medium）。
  注: review 論文は通常 EP を充填しないが、本 review が meta-analysis として
  stability 比較データを独自に提供している場合は例外扱い。Bibliographic confidence: Medium.
* **充填確立点（間接）**: 配位子電子効果（PR₃ vs NN-chelate）の体系的研究。
  Tolman, C.A. *Chem. Rev.* **1977**, *77*, 313–348（"Steric effects of phosphorus
  ligands in organometallic chemistry and homogeneous catalysis" — Ni–C 結合への
  配位子効果を扱う代表論文）— Indirect: 電子的比較の枠組みを提供するが
  compound II との直接比較はない。Bibliographic confidence: High.
* **充填の性質**: Indirect（類似系での充填; compound II との直接比較なし）
* **Bibliographic confidence**: Medium（Shaw review）/ High（Tolman）
* **Filling adequacy confidence**: Low（compound II を直接対象とした比較は未同定）
* **Verification recommendation**: [必須]（Shaw 1973 のみ; Tolman は省略可）
* **Filling timescale category**: field-methodology (5-10 yr)
* **注記**: compound II の dipyridyl vs Chatt–Shaw PR₃ の直接安定性比較を行った
  独立論文は未同定（§E の long-term 未充填候補）。

---

**EP-07a Boundary-test pack（第二群）**

* **充填するRI**: RI-07 Unsupported boundary（"stable only in chlorobenzene" の定量化）
* **充填開始点（see also EP-05a bundle）**: Yamamoto グループ companion full paper
  （compound II の溶媒安定性データを包含すると推定）。
  独立論文として: Yamamoto, A. et al. 後続論文（1971–1975; uncertain specific ref）
* **充填確立点**: compound II の溶媒安定性の定量的研究（k_decomp）は
  companion paper での自動解消（C23 format-driven）の可能性が最高（pending）。
* **充填の性質**: Partial（companion paper 経由）またはIndirect（類似系での溶媒効果研究）
* **Bibliographic confidence**: Medium（companion paper）/ Low（独立論文）
* **Filling adequacy confidence**: Medium（companion paper;IF it contains the data）
* **Verification recommendation**: [必須]
* **Bibliographic verification status**: pending
* **Filling timescale category**: format-driven (1-3 yr) via companion if included
* **注記**: ⚠️ verification 待機中。Solvent stability の body of work as independent
  topic for this specific compound は見つかっていない。

---

**EP-04a Discrimination / replication pack（第二群）**

* **充填するRI**: RI-04 Unreplicated discriminator（診断的反応の定量化・独立確認）
* **充填開始点**: Yamamoto グループ companion full paper（診断反応の quantitative
  yields を含む可能性）。
  auto_resolution_type: "Letter→Full Paper"
  auto_resolution_status: "promised"
  expected_resolution_window: "1-3 yr"
* **充填確立点**: companion full paper（pending）。独立文献での充填は未同定。
* **充填の性質**: Partial（companion paper での改良 characterization を仮定）
* **Bibliographic confidence**: Medium
* **Filling adequacy confidence**: Medium
* **Verification recommendation**: [必須]
* **Bibliographic verification status**: pending
* **Filling timescale category**: format-driven (1-3 yr)
* **注記**: ⚠️ C23 Letter→Full Paper pattern。診断的反応の定量化を独立論文主題と
  した文献は存在しない（第三群的性質を部分的に持つ）。

---

**EP-09a Internal benchmark pack（第二群）**

* **充填するRI**: RI-09 External superiority（compound I vs II の直接活性比較）
* **充填開始点**: Yamamoto グループ companion full paper（compound I および compound II
  + AlR₂X の直接 TON 比較を含む可能性）。
  auto_resolution_type: "Letter→Full Paper"
  auto_resolution_status: "promised"
* **充填確立点**: companion full paper（pending）。EP-05a とのバンドル充填が想定。
* **充填の性質**: Partial（companion paper; IF data included）
* **Bibliographic confidence**: Medium
* **Filling adequacy confidence**: Medium
* **Verification recommendation**: [必須]
* **Bibliographic verification status**: pending
* **Filling timescale category**: format-driven (1-3 yr)
* **注記**: ⚠️ EP-05a との bundle。compound I vs II の活性差は因果連鎖（U-3）の
  core 問いであり、対照実験（Cl⁻ 塩添加）を含む companion paper が理想。

---

**EP-01a Reporting-coherence pack（第二群）**

* **充填するRI**: RI-01 Reporting integrity（気体生成比 n-C₄H₁₀ / C₂H₆ / C₂H₄ の定量）
* **充填開始点**: Yamamoto グループの Et₂(bipy)Ni(II) 分解反応研究（機構研究の
  一部として気体組成が報告された可能性; ca. 1972–1978）。
  auto_resolution_type: "Letter→Full Paper" / "field-methodology"
  auto_resolution_status: "promised" (companion paper からの延長)
* **充填確立点**: compound I → compound II 変換における気体組成の定量
  GC データを特定の論文で確認できていない。EP-10a 充填論文（Tsou & Kochi
  型）では Ni(0) + PhCl 系のため gas evolution 情報なし。
* **充填の性質**: Indirect（Ni(II)-alkyl 分解ガス組成は関連文献に断片的に存在）
* **Bibliographic confidence**: Low（specific paper 未同定）
* **Filling adequacy confidence**: Low
* **Verification recommendation**: [必須]
* **Bibliographic verification status**: pending（要検索）
* **Filling timescale category**: format-driven (1-3 yr) if in companion;
  otherwise non-applicable (未充填可能性あり)
* **注記**: U-1（ガス組成の自己矛盾的不在）に対応する充填。
  Yamamoto グループ後続研究または Et₂Ni 錯体の熱分解研究に含まれる可能性。

---

**EP-08a Replication / uncertainty pack（第三群）**

* **充填するRI**: RI-08 Unquantified reliability（EA 反復測定、TGA 確認、Fajans 校正）
* **充填開始点**: **未同定** — EA トリプリケートの独立論文は慣行上存在しない。
  TGA を用いた溶媒和物同定は方法論論文（cf. 後述）に含まれる可能性。
* **充填確立点**: 未同定
* **充填の性質**: Non-applicable（インセンティブ構造的未充填）
* **Bibliographic confidence**: N/A
* **Filling adequacy confidence**: N/A
* **Verification recommendation**: [省略可]
* **Filling timescale category**: non-applicable
* **注記**: EA の繰り返し測定を独立論文として発表するインセンティブは
  現在まで存在しない。TGA による溶媒和物組成確認は compound II の
  follow-up で自然解消（companion paper）される性質だが独立論文化は
  されない。**インセンティブ構造的未充填**パターンに分類。

---

**§B 末尾 Bibliographic verification チェック**

**Trigger 条件評価:**
- (a) 論文年代が古い（1970 = 1980 年以前）→ ✓ 全候補に該当
- (b) 著者ネットワーク密（Yamamoto グループから 20+ 関連論文）→ ✓
- (c) 反応名由来命名なし（Kumada coupling とは別 group だが関連 era）→ 部分該当
- (d) Bibliographic confidence Medium-Low 候補が 5 件以上 → ✓

→ **全候補に [必須] Verification recommendation を適用**

Hallucination 警告（既知リスク）:
- Yamamoto グループ（TITech）の具体的論文（year, vol, page）は 1970 年代の
  日本系有機金属化学であり、LLM の training corpus coverage が低い可能性がある。
  Bibliographic confidence Medium の Japanese journal (Bull. Chem. Soc. Jpn.,
  J. Organomet. Chem.) 論文は特に cross-reference による DOI 確認を要する。
- "Tsou & Kochi 1979 JACS 101, 7547" は実在の論文として高確信するが、
  DOI 10.1021/ja00516a034 は推定値のため要確認。

---

### §C 推奨選定リスト

| 順序 | 論文 | 充填するEP | VQ水準 | 年代 | Bib.Conf | Fill.Conf | Verification |
|------|------|-----------|--------|------|----------|-----------|--------------|
| 1 | ⚠️ Yamamoto, A. et al. (companion full paper), *J. Organomet. Chem.* ca. 1971–1975 (pending) | EP-02a, EP-05a, EP-09a, EP-07a, EP-04a, EP-01a | VQ-2 → partial VQ-3 | 1971–75 | Medium | High (if exists) | **必須** |
| 2 | Tsou, T.T.; Kochi, J.K. *J. Am. Chem. Soc.* 1979, 101, 7547–7560 | EP-10a (Indirect) | VQ-3 | 1979 | High | Medium | 推奨 |
| 3 | ⚠️ Yamamoto グループ 機構論文 (compound I + ArX 系), ca. 1973–1982 (specific ref pending) | EP-10a (more direct), EP-03a | VQ-3 | 1973–82 | Low–Med | Medium | **必須** |
| 4 | Tolman, C.A. *Chem. Rev.* 1977, 77, 313–348 | EP-06a (Indirect) | VQ-3 Partial | 1977 | High | Low | 省略可 |
| 5 | ⚠️ Crystal structure paper: aryl-Ni-bipy complex, ca. 1975–1985 (specific ref pending) | EP-02a (Complete) | VQ-1 確立 | 1975–85 | Low | High (if exists) | **必須** |
| 6 | Bogdanovic, B. et al. *Angew. Chem. Int. Ed.* 1980 (Ni olefin oligomerization; specific ref pending) | EP-05a (Indirect, broader Ni dimerization) | VQ-4 Partial | 1980 | Medium | Medium | 推奨 |

**選定理由:**

推奨選定リストの核心は Entry 1（companion full paper by Yamamoto group）である。
A-1 で予告された本論文は、EP-02a（NMR/IR による compound II 構造確認）、
EP-05a（TON/TOF による Layer 2 量化）、EP-07a（溶媒安定性定量）、EP-09a
（compound I vs II の直接比較）をバンドルで充填する可能性が高く、
Stage 4 において最も情報利得が高い単一候補である。Bibliographic verification が
最優先課題。

Entry 2（Tsou & Kochi 1979）は EP-10a の間接充填として機能し、C–Cl 活性化
機構のための方法論的インフラ（Hammett + radical probe + kinetics）を提供する。
Ni(0) vs Ni(II) の酸化状態差を認識した上で間接充填として評価すべきである。

Entry 5（crystal structure）は RI-02 の完全解消として最も decisive な充填候補だが、
specific な論文が未同定のため ⚠️ pending。Entry 3（Yamamoto 機構論文）は
compound I + ArCl の直接機構研究として ideal だが同様に specific ref 未確認。

**全 6 entries のうち 3 entries が Bibliographic verification 必須（⚠️ pending）
であることは、1970 年代日本系有機金属化学の corpus coverage の限界を反映している。
Yamaoto Akio 教授の論文リスト（Scopus/WoS）からの直接確認を強く推奨する。**

---

### §D VQ階層と充填時間順序の対応分析

**充填の時間軸:**

- VQ-1 (RI-02) 確立: EP-02a →
  c. 1971–1975（companion full paper NMR/IR；自己充填 format-driven）
  c. 1975–1985（X 線構造；技術駆動充填）
  [⚠️ specific year pending verification]

- VQ-2 (RI-01, RI-07): EP-01a, EP-07a →
  c. 1971–1975（companion full paper での定量データ；自己充填 format-driven）
  [⚠️ pending]

- VQ-3 (RI-03, RI-04, RI-06): EP-10a, EP-03a →
  1979（Tsou & Kochi; 技術駆動充填; Indirect）
  c. 1973–1985（Yamamoto グループ機構論文; 推定; 要確認）
  [EP-03a は長期未充填の可能性; §E 参照]

- VQ-4 (RI-05, RI-09): EP-05a, EP-09a →
  c. 1971–1975（companion full paper での活性データ；自己充填 Layer 2）
  1980 以降（Wilke / IFP による分野定量化; Indirect）
  [⚠️ companion paper pending]

**階層-時間対応の評価:**

VQ-1/VQ-2 に対応する EP（構造確認・reporting completeness）は、
C23 Letter→Full Paper auto-resolution により最短（1-3 年）で自己充填が
発生したと推定される（Yamamoto グループの companion paper）。
VQ-3 に対応する EP-10a（機構）は 1979 年に Kochi グループが Indirect で充填（9 年後）、
EP-03a（直接観測）は現在まで長期未充填の可能性がある。
VQ-4 に対応する EP-05a（定量活性）は companion paper（format-driven, 1-3 yr）で
自己充填されたと推定されるが、独立 VQ-4 ベンチマーク（Wilke / IFP グループ）は
1980 年代以降に到達。

これは「VQ-1/2 は format-driven で速く、VQ-3/4 は field-methodology または
インセンティブ構造によって遅くなる（または未充填）」という一般的パターンを
支持する。ただし Layer 2（触媒活性）の VQ-4 要件が companion paper（format-driven）
経由で早期に自己充填されるという「Layer 非対称性」が際立つ特徴。

**特筆すべきパターン:**

1. **自己充填 + 分割提示充填（Split-presentation + Self-filling）**: Layer 2 全体
   が companion paper という「予告済み自己充填」構造を持つ。Layer 1（合成）の
   VQ-1/2 確立と Layer 2（触媒）の VQ-4 量化が同一の companion paper で
   同時解消される可能性が高い。これは Stage 3 §6 で指摘した split-presentation
   パターン（RI-09 拡張）の典型事例として充填時間分析で確認される。

2. **先行充填（Preceding filling）の候補**: Miller et al. JACS 1970（Ref 7 = C-3）は
   Uchino 1970 と同年の論文であり、EP-06a（Ni-aryl 安定性の配位子比較）への
   間接的貢献を持つ。ただし Uchino 1970 論文の問いへの「先行充填」ではなく、
   同時代の比較文脈（SRG-5 の参照断絶として記録済み）として扱う。

3. **長期遅延充填の可能性**: EP-03a（Ni 酸化状態の直接観測；U-2 critical）は、
   compound I + PhCl という特定系での EPR 研究が現在まで未発表である可能性が高く、
   54 年以上の長期遅延充填候補として §E に記録する。

---

### §E 未充填EPの発見的意義

**未充填EP一覧:**

---

**EP-08a Replication / uncertainty pack:**
* **未充填の理由**: **インセンティブ構造的未充填** — EA の反復測定・TGA 溶媒和物
  確認・Fajans 法の独立校正は、合成化学分野において独立論文として発表する
  インセンティブが 1970 年代から現在まで存在しない。companion full paper での
  "improved characterization" として部分解消される可能性はあるが、
  分析信頼性評価論文は自律的に出版されない。
* **発見的意義**: あり — ½ 溶媒和物という特異な化学式の信頼性問題（D-4-6 / SRG-2）は
  compound II の identity claim の基盤に関わるにもかかわらず、インセンティブ構造的
  に独立研究として問われてこなかった。これは「化合物同定の最小証明セット」という
  認識論的問い（Stage 2 E-変形 4）が分野で体系的に回避されてきたことの一例として
  記録できる。
* **将来の充填可能性**: 中 — TGA および X 線回折（単結晶構造）が得られれば
  compound II の ½ 溶媒和物組成は原理的に確認可能。現代の有機金属合成論文では
  X 線構造解析が standard になっており、化合物の再調製と単結晶取得で充填可能。

---

**EP-03a Direct-observation / state-assignment pack（部分未充填）:**
* **未充填の理由**: **技術的困難 + 関心の欠如** — Et₂(bipy)Ni(II) + PhCl という
  特定反応系の反応中間体（特に Ni(I) / Ni(III) ラジカル中間体）の直接 EPR / UV-Vis
  時間分解研究は、対象系に固有の研究として長期間発表されていない。1970 年代の
  有機金属化学は、Ni(0) + ArX（酸化的付加）という簡潔な反応へと関心が移行し
  （Kumada カップリング等）、Ni(II) アルキル + ArX という複雑系の機構研究への
  直接的インセンティブが低下した可能性がある（**成功による問いの抹消** 要素が
  部分的に作用している可能性）。
* **発見的意義**: あり — U-2（Ni 酸化状態軌跡の critical 自己矛盾的不在）は
  compound II 形成という本論文の中心事実の機構的根拠に関わる。この問いが
  54 年間（1970–2026）直接的に問われてこなかったとすれば、「Ni(II) アルキル錯体
  による C–Cl 活性化機構の未解決性」という認識論的空白として記録できる。
  現代の Ni-触媒クロスカップリング機構研究（Ni(0)/Ni(II)/Ni(I)/Ni(III) サイクル
  の競合議論）の文脈では、この問いへの関心が再び高まっている可能性がある。
* **将来の充填可能性**: 高 — 停止フロー UV-Vis + EPR（X-band / W-band）を用いた
  時間分解実験、または計算化学（DFT/CASSCF による中間体エネルギー面）で
  現代的に充填可能。特に Ni(I)/Ni(III) を介したラジカル機構 vs Ni(0)/Ni(II) の
  2 電子 OA の競合という問いは、Diao グループ・Engle グループ等の現代
  Ni 触媒機構研究者が類似問題に取り組んでいる文脈と重なる。

---

**EP-06a Analogy-validation pack（部分未充填）:**
* **未充填の理由**: **インセンティブ構造的未充填** — compound II（dipyridyl-Ni-Ph）と
  Chatt–Shaw / Miller の NiX(aryl)·2PR₃ の「直接比較」（同一条件下での安定性・
  反応性定量）を論文主題とした研究は、1970 年代以降に見当たらない。
  dipyridyl が PR₃ より Ni–aryl 結合を安定化するかという問いは、後にクロスカップリング
  触媒設計（N-heterocyclic carbene vs phosphine, bipy vs diphosphine の比較）として
  形を変えて問われるようになったが、compound II との直接比較としては問われていない
  可能性が高い。
* **発見的意義**: あり — SRG-5（Analogy references severed without comparative data）
  が示す「引用断絶」パターン（C-2/C-3 cited as analogy only）は、1970 年代の
  有機金属 Ni 化学において配位子比較研究が独立研究主題として成立しなかったことを
  示す可能性がある。dipyridyl の unique 安定化機構は現代でも興味深い問いとして残る。
* **将来の充填可能性**: 高 — 現代の DFT 計算（energy decomposition analysis）で
  dipyridyl vs PR₃ の Ni–C(Ph) 結合への電子的寄与の比較は比較的容易に実施可能。
  実験的には compound II と Ph(dppe)NiCl の solution 安定性比較（UV-Vis 分解速度）
  が現代ツールで充填可能。

---

**VQ 階層逆転の診断:**

充填済み EP の VQ 水準:
- format-driven で最速に充填: EP-01a, EP-04a, EP-07a, EP-09a（VQ-2 水準、1-3 yr）
- field-methodology 充填: EP-10a（VQ-3、9 yr 後 Tsou/Kochi; Indirect）

未充填傾向 EP の VQ 水準:
- EP-08a（RI-08; VQ-4 水準）: インセンティブ構造的未充填
- EP-03a（RI-03; VQ-3 水準の直接観測）: 長期未充填の可能性
- EP-06a（RI-06; VQ-3 水準の類推検証）: 部分未充填

本論文では VQ 階層逆転は**部分的に成立**する: EP-10a（VQ-3 機構）は 1979 年の
Kochi グループによる間接充填があるが、EP-03a（VQ-3 直接観測）と EP-06a（VQ-3
類推検証）は長期未充填または間接充填のみ。EP-08a（VQ-4 水準）は完全未充填。
しかし EP-05a（VQ-4 活性データ）は companion paper（format-driven; 1-3 yr）で
早期自己充填されたと推定され、これは「高VQ要件でも format-driven 自己充填が
低VQ要件未充填より速い」という逆転事例として記録できる。

この Layer 非対称性（Layer 2 = VQ-4 が Layer 1 = VQ-3 より速く充填された可能性）は、
「応用価値（触媒データ）の発表インセンティブが機構解明（C–Cl 活性化）より強い」
という分野のインセンティブ構造を反映している。

inference_time_sec: not available — inject externally
```
