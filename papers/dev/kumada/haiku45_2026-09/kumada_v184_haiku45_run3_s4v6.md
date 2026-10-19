<!-- model_info: claude-haiku-4-5-20251001 -->
prompt_version: stage4-v6-20260504

# EP充填選定マップ

## Tamao, Sumitani, Kumada 1972（Journal of the American Chemical Society, Communication）

### §A EP充填難易度の三群分類

**第一群（文献で明確に追跡可能）：** EP-10a, EP-03a, EP-02a, EP-07a
— EP-10a (kinetic verification): Ni-diphosphine coupling のkinetics測定は独立研究テーマとして多くの後続論文で実施された可能性が高い（初期速度測定、温度依存、Eyring パラメータは触媒設計研究で標準的）。EP-03a (intermediate NMR): Ni-π-alkenyl中間体の分光学的同定は、1970–1980年代の有機金属化学でも可能な独立テーマであり、後続研究による直接観測の試みが期待できる。EP-02a (product characterization): 全生成物の¹H/¹³C NMR, MS記録は、後続のより大規模なスコープ研究で実施されやすい。EP-07a (boundary test): Csp³ ハロゲン化物やelectronic variation の試験は、scope拡張研究として独立論文化される可能性がある。

**第二群（間接的に追跡可能）：** EP-08a, EP-09a
— EP-08a (replication/uncertainty): 反復測定と統計的評価は、通信形式から完全論文への自動展開（Letter→Full Paper C23パターン）で部分的に解消される可能性がある（Kumada group による同一基質系の続報で詳細データが報告される見込み）。ただしindependent replication（他研究グループによる再確認）は出版インセンティブの問題で論文化されにくい。EP-09a (competitive benchmark): Tamura-Kochi系との定量比較は、方法論review論文や Kumada group自身の comparative paper に含まれやすく、独立論文としては限定的。

**第三群（充填が見つからない可能性あり）：** なし
— 本論文の6つのEPはいずれも、触媒化学の標準的研究テーマ（kinetics, intermediate characterization, product scope）に対応しており、第三群に分類されるincentive-structural unfilling または constraint-disclosure-impossible パターンは当てはまらない。

---

### §B 各EPの充填論文候補

**EP-10a [Kinetic verification pack]（第一群）**

* **充填するRI**: RI-03 [Unobserved explanatory], RI-04 [Unreplicated discriminator], RI-06 [Imported model]

* **充填開始点**: Tamao et al., 1973–1975年前後の Kumada group による継続報告（推定）。推測根拠：Communication直後の organometallic kinetics は Kumada group の主要テーマであり、同一系での速度論的characterization がなされた可能性が高い（具体的な論文特定には verify 必須）。
  - **Bibliographic confidence**: Low
  - **Filling adequacy confidence**: Medium（推定のみ）
  - **Verification recommendation**: 必須（歴史的関連著者ネットワーク密）

* **充填確立点**: Kumada group が1970年代中～後期に公表した organometallic Ni-catalyzed coupling の速度論論文。特に、[NiCl₂(dpe)] の活性化エネルギー（diphosphine系での Ea 比較）を報告した論文があれば該当。別個に、他グループによる general nickel catalysis kinetics の methodological advance が並行充填となる可能性（例：1980年代の organometallic kinetics methodology papers）。
  - **Bibliographic confidence**: Low–Medium
  - **Filling adequacy confidence**: Medium
  - **Verification recommendation**: 必須（確定的論文特定が不可）

* **充填の性質**: Partial（初期速度測定や ligand効果定性化は予想されるが、full rate-law derivation や complete Eyring parametrization の確定までは推定不能）

* **Filling timescale category**: field-methodology (2–5 yr)（organometallic kinetics methodology の field-wide adoption が driving force 推定）

* **注記**: Kumada group自身による自己充填の可能性が高い（原著者の後続研究）。Communication→Full Paper遷移での自動解消パターン（C23）が適用されるか否かは、Full Paper候補の存在確認により判断。

---

**EP-03a [Direct-observation / state-assignment pack]（第一群）**

* **充填するRI**: RI-03 [Unobserved explanatory], RI-06 [Imported model]

* **充填開始点**: 未特定。Kumada group が1970年代後期に発表した π-alkenyl-Ni中間体のNMR characterization、あるいは関連する organometallic intermediate分光論文が候補。別個に、有機金属化学全般での Ni-diphosphine system の NMR study が行われた可能性がある。
  - **Bibliographic confidence**: Low
  - **Filling adequacy confidence**: Low–Medium
  - **Verification recommendation**: 必須

* **充填確立点**: 同上（未特定）

* **充填の性質**: Attempted or Partial（1970年代の NMR技術（¹H, ¹³C）は intermediate 観測に十分だったが、in-situ NMR による real-time observation の確立は1980年代以降の技術進展による）

* **Filling timescale category**: technical-barrier (10–20+ yr)（in-situ NMR technology の発展が barrier。real-time intermediate tracking は1980年代後期以降に standard化）

* **注記**: EP-03a の充填難度は high（intermediate の短寿命、rapid exchange への対応）。部分的充填（NMR tube実験での intermediate trapping）と完全充填（in-situ kinetic tracking）で timescale が大きく異なる。

---

**EP-02a [Identity / purity substantiation pack]（第一群）

* **充填するRI**: RI-02 [Object identification]

* **充填開始点**: Tamao et al. による同年代～数年以内の続報、あるいは Kumada group による larger-scope coupling study（例：様々な基質での Table 拡張）。当該論文では、全生成物について ¹H/¹³C NMR + MS を記録し、purity assay（glpc or elemental analysis）が明記されることが期待される。
  - **Bibliographic confidence**: Medium（Kumada group の出版パターンから推定）
  - **Filling adequacy confidence**: Medium–High（完全論文化の確率は高いが、文献実確認は要）
  - **Verification recommendation**: 推奨（1970年代、Kumada group 著者ネットワーク）

* **充填確立点**: 同上

* **充填の性質**: Complete（Full Paper では methodological completeness が通常採択要件）

* **Filling timescale category**: format-driven (1–3 yr)（Letter→Full Paper auto-resolution C23パターン）

* **注記**: EP-02a は communication→full paper 自動解消の最適候補。Kumada group が報告済みの communication data をfull paper で詳細化したケースであれば、1–3年以内での充填が期待される。

---

**EP-07a [Boundary-test pack]（第一群）

* **充填するRI**: RI-07 [Unsupported boundary]

* **充填開始点**: 1970年代中～後期の organometallic coupling scope拡張研究。特に、Csp³ halide の反応性、electronic effect (EWG/EDG on aromatic ring)、conjugated Grignard の試験が独立報告されたかどうかが査定対象。Kumada group あるいは他グループによる coupling scope study が候補。
  - **Bibliographic confidence**: Low–Medium
  - **Filling adequacy confidence**: Medium
  - **Verification recommendation**: 必須（著者ネットワーク密 + 1970年代）

* **充填確立点**: 同上（具体的論文は未特定）

* **充填の性質**: Partial（boundary の完全な mechanistic explanation は通常、scope paper では省略され、後続の method development paper で累積的に達成される）

* **Filling timescale category**: field-methodology (2–5 yr)

* **注記**: Scope拡張は synthesis literature の常套テーマであり、複数の報告が期待される。各報告が独立か derivative かの区別には、論文ネットワークの追跡が必要。

---

**EP-08a [Replication / uncertainty pack]（第二群）

* **充填するRI**: RI-08 [Unquantified reliability]

* **充填開始点**: Communication直後の Kumada group による continuation paper（予想）。Letter→Full Paper 遷移で、Example 1 と Example 2 の n≥3 replication data、glpc chromatograms、mass balance accounting が報告される可能性。
  - **Bibliographic confidence**: Medium（出版パターン推定）
  - **Filling adequacy confidence**: Medium–High
  - **Verification recommendation**: 推奨（Letter→Full Paper C23 auto-resolution pattern）

* **充填確立点**: 同上のFull Paper（未確認）

* **充填の性質**: Complete（Full Paper では replication と統計的評価が採択要件）

* **Filling timescale category**: format-driven (1–3 yr)

* **注記**: C23パターン（Letter→Full Paper within-issue or 1–3 yr follow-up）が典型。ただし、independent replication（他グループによる再測定）は low publication incentive のため論文化されない傾向（第三群「インセンティブ構造的未充填」の候補）。

---

**EP-09a [Internal benchmark pack]（第二群）

* **充填するRI**: RI-09 [External superiority]

* **充填開始点**: Kumada group による Tamura-Kochi系との comparative study（推定）。Tamura et al. の original paper の published data を参考に、同一基質 (PhMgBr + PhCl) での並行測定を報告したレビュー論文、method review、あるいは Kumada group の独立 comparative paper が候補。
  - **Bibliographic confidence**: Low–Medium
  - **Filling adequacy confidence**: Low（比較内容が EP要件を満たすか不確実）
  - **Verification recommendation**: 必須（確定論文が未特定）

* **充填確立点**: 同上

* **充填の性質**: Indirect or Attempted（方法論review が定量比較を含む可能性が高いが、fill としての独立性は限定的）

* **Filling timescale category**: field-methodology (variable)（review論文出版までの年数は variable）

* **注記**: EP-09a は、独立論文化より review/comparison context での充填が多い傾向。Kumada-group自身による comparative narrative（例：1980年代の retrospective や Kumada自身の受賞講演）があれば、それが partial filling として機能する可能性がある。

---

---

### §C 推奨選定リスト

以下は、充填論文候補の中から、最適な検証セットとして推奨する5報（または推定可能な候補核）を列挙する。確実な書誌特定に至っていないため、全エントリが **[必須] verification 待機** 状態。

| 順序 | 論文 | 充填するEP | VQ水準 | 年代 | Bib.Conf | Fill.Conf | Verification |
|------|------|-----------|--------|------|----------|-----------|--------------|
| 1 | Tamao et al., J. Amer. Chem. Soc., 1973–1975年推定 (Full Paper候補) | EP-02a, EP-08a | VQ-2 | ~1974 | Low–Med | Med | 必須 |
| 2 | Kumada group kinetics study, 1973–1978年推定 | EP-10a | VQ-3 | ~1975–77 | Low | Med | 必須 |
| 3 | Ni organometallic scope expansion (coupling, other substrates), 1975–1980年推定 | EP-07a | VQ-2 | ~1977–79 | Low | Med | 必須 |
| 4 | Tamao/Kumada comparison or benchmark review, 1980年代推定 | EP-09a | VQ-4 | ~1980–85 | Low | Low | 必須 |
| 5 | In-situ NMR or π-alkenyl Ni characterization, 1980年代後期推定 | EP-03a | VQ-3 | ~1985–90 | Low | Low | 必須 |

**選定理由：**
- 表中の5報は、EP-02a, EP-08a (VQ-2自動充填) → EP-10a, EP-03a (VQ-3 kinetics/characterization) → EP-09a (VQ-4 benchmark) という VQ階層的カバレッジを企図している。
- 年代多様性：1974年〜1990年で時間的展開を span。
- 第二群（Letter→Full Paper auto-resolution）と第一群（kinetics, scope, spectroscopy）の混合。
- **⚠️ 全エントリが Bibliographic confidence Low–Medium であり、post-hoc verification（Crossref検索、原著論文の実確認）が不可欠**。確定するまでは推定選定リストとして扱う。

---

### §D VQ階層と充填時間順序の対応分析

**充填の時間軸（推定）：**

- **VQ-2要件 (RI-01, RI-07 補填)**:
  - EP-02a (product characterization) → 1973–1974年推定 (Letter→Full Paper auto-resolution C23)
  - EP-08a (replication) → 1973–1974年推定 (同上)

- **VQ-3要件 (RI-03, RI-06 補填)**:
  - EP-10a (kinetics) → 1975–1977年推定 (field-methodology, Ni-catalysis kinetics の field-wide adoption)
  - EP-07a (boundary test) → 1977–1979年推定 (scope拡張)
  - EP-03a (spectroscopy) → 1985–1990年推定 (技術barrier による遅延, in-situ NMR technology 成熟)

- **VQ-4要件 (RI-08, RI-09 補填)**:
  - EP-09a (competitive benchmark) → 1980–1985年推定 (review/method papers)

**階層-時間対応の評価：**

推定パターンから、「**VQ階層が上がるほど、充填に要する時間が長くなる傾向がある**」という仮説が支持される可能性が認められる。VQ-2（reporting completeness）は communication→full paper の形式転換で1–3年で自動充填される一方、VQ-3（mechanism/characterization）は5–10年、VQ-4（benchmark/comparison）は10–15年の scale で充填されると推定される。これは、**VQ階層が、「報告形式で比較的容易に補填できるレイヤー」から「独立研究テーマとして長期競争を要するレイヤー」への上昇を反映**しているという解釈を支持する。

ただし、確定的な論文特定なしのため、この対応の妥当性は **verification 待機状態**。

**特筆すべきパターン：**

- **自己充填の高度予想**: Kumada group自身による後続報告（Full Paper, 続報研究）が複数EPを充填する「バンドル充填」パターンが優位と推定される。一般的に、landmark communication は同一グループの full paper 続報で methodological detail が補填される。
- **技術駆動充填**: EP-03a (intermediate NMR) は、in-situ NMR technology の成熟（1980年代後期）によって初めて完全充填される典型例。1970年代の NMR tube での静的 characterization と1980年代後期の real-time kinetic tracking の間に、10+ 年の技術barrier が存在。
- **letter-following pattern**: EP-02a, EP-08a が短期（1–3年）で充填される Letter→Full Paper C23パターンは、Kumada 1972 の出版形式（communication）から的確に予測できる。

---

### §E 未充填EPの発見的意義

**現状評価：**

§B で同定を試みた全 6 EP（EP-02a, EP-03a, EP-07a, EP-08a, EP-09a, EP-10a）に対し、文献上の確定的な充填論文の特定に至っていない。ただし、推定される充填論文候補（Kumada group の後続報告、organometallic kinetics methodology paper、scope拡張研究等）は複数存在し、確認待ち状態。

**未充填診断（推定）：**

- **完全未充填の可能性**: 
  - EP-09a (Tamura-Kochi との定量比較): 競争的benchmark論文として独立論文化される可能性は低い（review/narrative context での partial filling が主）。1970年代のアメリカ（Tamura-Kochi）とアメリカ（Kumada）の競争は、当時の literature中ではそれほど明示的に比較されなかった可能性（後年の回顧で初めて比較論述される傾向）。→ **インセンティブ構造的未充填**の候補。

- **部分未充填の可能性**:
  - EP-03a (intermediate NMR): 1970年代での部分充填（静的 NMR tube 実験）は予想されるが、1980年代まで完全充填にいたらない（in-situ kinetic NMR 技術の barrier）。→ **技術barrier 越境型の遅延充填**。

**発見的意義の試評：**

本論文のUnasked Questions を充填する論文群の（推定される）時間展開は、**organometallic catalysis の分野的発展の「必要な問い」と「出版インセンティブの一致性」を可視化**するケーススタディとなり得る。特に：

1. VQ-2要件（報告形式）は自動充填（format-driven 1–3年）: 分野のstandard化によって短期で解消される。
2. VQ-3要件（characterization/kinetics）は長期充填（5–15年）: 独立研究テーマとしての競争力を備えてはじめて論文化される。
3. EP-09a（benchmark比較）の未充填 / 部分充填は、分野内の「競争の顕在化」と「実験的検証需要の回避」（Tamura系への感応性回避？）の可能性を示唆。

ただし、確定的論文同定の欠落により、これらの発見的意義は **hypothetical status**（推定段階）。

**VQ階層逆転の診断（推定）：**

表面的には、充填EPが VQ-2（RI-01, RI-08：報告形式・反復測定）から VQ-3（RI-03, RI-06：mechanistic characterization）に、さらに VQ-4（RI-09：外部比較）へと ladder climb する pattern が観察される（推定）。これは **「scientific logic に基づく VQ階層の上昇」と「実際の充填時間（format-driven < field-methodology < technical-barrier）」の対応**を示唆する。

逆転パターンの可能性：VQ-4（EP-09a, RI-09外部比較）が最も長期未充填 / 部分充填に留まり、VQ-3（kinetics, characterization）が充填された場合、これは「出版インセンティブ（新規性・競争性）が高い frontier science（kinetics）は早期充填、一方 methodological comparison（benchmark）は出版価値が低いとみなされる」ことを示唆する → **分野の implicit 価値序列の露呈**として記録可能。

---

**注：**

全§C, §Dの推定値は、**post-hoc bibliographic verification を前提とした conditional output** である。Crossref API等による確定論文の自動検索、および原著論文実確認により、上記推定選定リストは大幅に修正される見込みが高い。現段階は「verification awaiting」状態として扱うこと。

