```
prompt_version: stage4-v6-20260504
model_info: claude-sonnet-4-6
experimental_variant: retrieval-depth-annotation (Multi-run robustness, v6 run 2)
related_pilot: papers/dev/kumada/kumada_v17_sonnet_s4v6_retrieval_depth.md (Pilot 1, v6 run 1)
note: Multi-run robustness check の v6 第 2 run。Pilot 1 と同 prompt で実行し、
      run 間の retrieval scope と Tier annotation の variance を測定する。
```

---

# EP充填選定マップ

## Tamao, Sumitani, Kumada 1972（Journal of the American Chemical Society, Communication）

---

## §A EP充填難易度の三群分類

**第一群（文献で明確に追跡可能）：** EP-01a, EP-02a, EP-03a, EP-04a, EP-05a, EP-06a, EP-09a

- **EP-01a（Reporting-coherence pack）**: 同一著者グループが JACS Communication の 4 年後に Bull. Chem. Soc. Jpn. で Full Paper を発表しており（C23 pattern: Letter→Full Paper auto-resolution が発火）、glpc 条件・反応時間・統一収率基準を含む詳細データが独立論文として存在する可能性が高い。
- **EP-02a（Identity/purity substantiation pack）**: 同上 Full Paper で per-entry 分光データが記載される典型パターンであり、単独論文として追跡可能。
- **EP-03a（Direct-observation / state-assignment pack）**: σ-organonickel 中間体の直接分光観測（³¹P NMR）は 1970 年代中葉の有機金属化学で独立研究テーマとして発表されやすい実験内容であり、Kumada グループの続報論文として存在する可能性が高い。
- **EP-04a（Discrimination / replication pack）**: ビニルハライドの立体化学（cis/trans 比の温度・時間依存性）は反応機構研究の独立テーマとなりうる; Hayashi–Kumada グループが立体特異的カップリングを精力的に研究した事実から追跡可能。
- **EP-05a（Quantitative-ranking substantiation pack）**: Full Paper（BCSJ 1976）が質量収支データを含む可能性が高く、第一群として追跡できる。
- **EP-06a（Analogy-validation pack）**: NiCl₂(dpe) 系での化学量論的素反応の実証実験は、Kumada グループが 1973–1977 年に機構論として独立論文化した可能性が高い; RI-06（サイクルレベル輸入）の検証は独立研究主題として現れやすい。
- **EP-09a（Internal benchmark pack）**: Corriu and Masse (1972) Chem. Commun. 144 が論文本文の Note Added in Proof に直接引用されており、Ni(acac)₂ 系の存在を起点として比較研究が追跡可能。

**第二群（間接的に追跡可能）：** EP-07a

- **EP-07a（Boundary-test pack）**: sp³ ハライドを失敗例として記録した独立論文は存在しにくい（否定的結果は publication bias で抑制される）。しかし Full Paper（BCSJ 1976）のスコープ節に sp² 選択性の実験的根拠が部分的に含まれる可能性があり、また塩化物/臭化物/ヨウ化物の活性比較（定量的基準）は速度論論文として登場しうる。Letter→Full Paper の C23 pattern とも部分的に重複するが、sp³ ハライドの失敗例そのものが独立論文主題になりにくい点で第二群と判定する。

**第三群（充填が見つからない可能性あり）：** EP-08a

- **EP-08a（Replication / uncertainty pack）**: 収率データの反復測定・統計的有意性評価は独立論文として出版されにくい（インセンティブ構造的未充填）。1970 年代の有機合成化学において、既存系の再現性統計は論文主題としてほぼ存在せず、分野慣行として系統的に回避されてきた。

**C23 Letter→Full Paper auto-resolution トリガー確認**:
本論文は JACS Communication 形式（BIB-7）であり、C23 が発火する。EP-01a, EP-02a, EP-05a について C23 pattern を §B で詳細に記録する。

---

## §B 各EPの充填論文候補

---

### 思考過程の externalization（§B 全体に先立つ retrieval log）

**Tier I 想起（EP description から直接浮かんだ候補）:**
- Tamao et al. Bull. Chem. Soc. Jpn. 1976 Full Paper：Kumada 1972 → BCSJ 1976 Full Paper という継承は有機金属化学史の常識として即座に浮かんだ。著者リストの詳細（Tamao + Sumitani + ????? + Kumada）の中間著者群は不確実。
- Corriu, Masse, Chem. Commun. 1972：論文本文の Note Added in Proof に直接登場するため、読み取った瞬間に保持されていた。

**Tier II 想起（2–3 段階の連想）:**
- 「Hayashi + Kumada + mechanism + stereospecificity」という系列：Hayashi Tamio が Kumada グループに所属し、立体特異的カップリングと機構を精力的に研究したという文脈知識から連想。具体的論文名は不確実。
- 「σ-organonickel complexes + dpe ligand + characterization」：RI-06（輸入機構サイクル）の充填には dpe-Ni 系の σ-中間体の直接観測が必要という手順から逆算。Kumada グループの J. Organomet. Chem. 1976–1977 系列が連想されたが、著者リストの確実性は Medium。

**Tier III 想起（複数候補の triangulation を経て浮上）:**
- sp³ ハライドの失敗例：①否定結果は発表されにくい、②Kumada グループが sp² 選択性の機構的根拠を与えた論文が別途存在する可能性、③後続の Ni-触媒 sp³ カップリング研究（1990 年代以降）を逆算すると 1972–1980 年の空白期が推定される、という 3 経路で triangulate した。

**棄却した候補（逐次記録）:**
- Heck, Suzuki, Negishi, Stille 各種 Pd カップリング論文：金属が違う。EP 充填には「同一系（NiCl₂(dpe)系）での実証」が要件であり、Pd 系は paradigm-shift 候補にはなるが直接的 EP 充填には不適。
- Hayashi et al. の不斉カップリング論文（BINAP-Ni 系）：応用・拡張論文であり、1972 年論文の EP に対応する基礎的実験内容（byproduct 定量、中間体観測）を含まない。
- Kumada 2002 回顧論文（Tamao 2002 mini-review）：レビューはEPを充填しない規則により棄却。ただし充填論文の同定に二次情報源として参照。

---

**EP-01a [Reporting-coherence pack]（第一群）**

* **充填するRI**: RI-01 [Reporting integrity] — glpc 条件不記載・収率計算基準不統一・反応時間不記載
* **充填開始点**: Tamao, Sumitani, Kiso, Zembayashi, Fujioka, Kodama, Nakajima, Minato, Kumada, *Bull. Chem. Soc. Jpn.* 1976, **49**, 1958–1969 — 同一 Kumada グループが発表した Full Paper I（NiCl₂(dpe) 触媒系のアリール・アルケニル Grignard 試薬のカップリング）において、Table I の全エントリに対して統一された glpc 条件・内部標準・収率計算基準が記載される。
* **充填確立点**: 同上
* **充填の性質**: Complete（RI-01 の報告形式問題は Full Paper 展開により実質的に解消）
* **Bibliographic confidence**: Medium — Tamao と Kumada は著者として確実だが、中間著者リスト（Kiso, Zembayashi, Fujioka, Kodama, Nakajima, Minato）の完全一致は保証できない; pp.1958–1969 の巻号も推測を含む。
* **Filling adequacy confidence**: High — Letter→Full Paper 遷移パターン（C23）の典型例であり、Full Paper が RI-01 要件を直接解消することは構造的に確実。
* **Verification recommendation**: [必須] — (a) 1976 年以前の古い論文 + (c) Kumada 反応（author-name 命名規則）+ (d) Medium confidence 候補 2 件以上、3 要因が重複
* **DOI**: 推定（未確認）; 著者名 + 雑誌 + 年で Crossref 検索可能
* **Filling timescale category**: format-driven (4 yr: 1972 → 1976)
* **Bibliographic verification status**: pending
```yaml
auto_resolution_type: "Letter→Full Paper"
expected_resolution_window: "1-5 yr"
auto_resolution_status: "occurred"
filling_timescale_category: "format-driven"
```
* **注記**: B-4（glpc 条件）, B-8（反応時間）, B-9（条件非最適化免責）が一括解消される。§3（Era-Norm Annotation）で communication-era tolerated とされた項目が Full Paper 展開で自動解消するパターンの代表例。Layer 1（合成実用性層）の VQ-2 到達に直結する最優先 EP。

**Retrieval depth（EP-01a）**: Self-Tier **I** — BCSJ 1976 Full Paper は「Kumada coupling の歴史」を想起した瞬間に浮かんだ。推論経路：JACS Communication (1972) → 同グループ BCSJ Full Paper (mid-1970s) という継承パターンは Kumada 系論文の知識として直接保持。DB-findable: **yes**（CAS/Web of Science で Tamao + Kumada + BCSJ + 1976 で検索可能）。Bib confidence: **Medium**（著者リスト中間部が不確実）。

---

**EP-02a [Identity/purity substantiation pack]（第一群）**

* **充填するRI**: RI-02 [Identification integrity] — Table I 全エントリの「and/or」構文による生成物同定の不完全性
* **充填開始点**: Tamao et al., *Bull. Chem. Soc. Jpn.* 1976, **49**, 1958–1969（EP-01a と同一論文） — Full Paper I において per-entry GC-MS または ¹H NMR データが記載され、RI-02 の non-fatal 残存が解消される。
* **充填確立点**: 同上
* **充填の性質**: Complete（バンドル充填: EP-01a と同一論文が EP-02a も同時充填）
* **Bibliographic confidence**: Medium（EP-01a と同一）
* **Filling adequacy confidence**: Medium — Full Paper に per-entry 分光データが含まれると判断するが、1972 年代の BCSJ Full Paper では全エントリに完全な NMR/MS が掲載されたかどうか、推論を含む。
* **Verification recommendation**: [必須]（同上 3 要因）
* **Filling timescale category**: format-driven (4 yr)
* **Bibliographic verification status**: pending
* **注記**: B-13（and/or 構文）が解消される典型的 Full Paper 遷移パターン。VQ-1 の non-fatal RI-02 残存を除去し、VQ-2 への通過条件を完全化する。EP-01a と同一論文によるバンドル充填。

**Retrieval depth（EP-02a）**: Self-Tier **I** — EP-01a と同一論文に分光データが含まれることを EP-01a を想起した流れで自明的に想起。推論経路：Full Paper は synthesis table + spectroscopic characterization を一体化するのが慣習。DB-findable: **yes**（EP-01a と同一文献）。Bib confidence: **Medium**（EP-01a と同一）。

---

**EP-03a [Direct-observation / state-assignment pack]（第一群）**

* **充填するRI**: RI-03 [Unobserved explanatory] — 中間体 1（L₂NiR₂）・2（L₂Ni(R')(X)）・3（L₂NiRR'）の直接観測・速度論的拘束なし
* **充填開始点**: Tamao, Hayashi, Kumada, *J. Organomet. Chem.* **1977** 頃（詳細不確実）— NiCl₂(dpe) と化学量論量の RMgX を低温で反応させた ³¹P{¹H} NMR 測定、または独立合成したジオルガノニッケル(II)-dpe 中間体の分光学的特性評価を含む論文として想定。
  *※著者リスト・年・巻号は推定値であり、Low–Medium の bibliographic confidence（後述）*
* **充填確立点**: 未特定（Kumada グループが複数報告を重ねた可能性があり、一報で決定的充填となったかは不明）
* **充填の性質**: Partial（推定） — dpe-Ni 系の個々の中間体を単離・同定する実験は技術的に困難であり、³¹P NMR による間接証拠による部分充填の可能性が高い。
* **Bibliographic confidence**: Low — 「Tamao, Hayashi, Kumada + J. Organomet. Chem. + 1976–1978」という組み合わせは連想的推論の産物であり、著者組み合わせ・雑誌・年を確認していない。「Tajima」を Hayashi の共著者として想起する傾向があるが、これが実在するかも不確認（著者組合せ捏造パターンへの注意）。
* **Filling adequacy confidence**: Medium — σ-organonickel intermediates の ³¹P NMR は技術的に実現可能であり、1970 年代後半の分光技術水準と整合するが、論文の具体的内容に確信はない。
* **Verification recommendation**: [必須]（(a) 1970 年代 + (c) Kumada 反応 + (b) 著者ネットワーク密）
* **Filling timescale category**: field-methodology (3-8 yr: NMR 技術の普及と有機金属化学の方法論発展が driving force)
* **Bibliographic verification status**: pending
* **注記**: SRG-1 の RI-06 + RI-03 不可分共起（§6 注記）に対応。EP-06a と合わせて検証する必要があり、どちらか一方の充填だけでは VQ-3 に到達しない（§5 VQ-3 ルート参照）。

**Retrieval depth（EP-03a）**: Self-Tier **II** — 「NiCl₂(dpe) の機構解明」→「Kumada グループが続報で示した」→「σ-diorganonickel intermediate の分光的証拠」という 3 段階の連想。推論経路：RI-03 の case-specific 実装（NiCl₂(dpe) + n-BuMgBr の低温 ³¹P NMR）を読んで、この実験を最初に実施したのは当然 Kumada グループだと推定し、Tamao/Hayashi という名前が浮かんだ。DB-findable: **uncertain**（特定の論文として確実に存在するか不確実）。Bib confidence: **Low**。

---

**EP-04a [Discrimination / replication pack]（第一群）**

* **充填するRI**: RI-04 [Unreplicated discriminator] — cis/trans 比の速度論的 vs. 熱力学的制御の区別実験なし; 単一測定値に機構的解釈
* **充填開始点**: Hayashi, Tajima（名前不確実）, Kumada —  *Tetrahedron Lett.* または *Bull. Chem. Soc. Jpn.* **1975–1978** 頃（詳細不確実）— ビニルハライドの立体化学（cis/trans stilbene 比）を時間・温度系列で測定し、速度論的産物であることを実証する論文として想定。
  *※著者リスト・年・掲載誌は低信頼度推定値*
* **充填確立点**: 上記と同一あるいは後続論文（不確実）
* **充填の性質**: Partial（推定） — 速度論/熱力学の区別を目的とした専用の時間系列実験が独立論文として発表されたかは不確実; 立体特異的カップリングの研究は Hayashi–Kumada の主要テーマだが、U-3 の問い（kinetic/thermodynamic indeterminacy）が直接的目的として検討されたかどうかは不明。
* **Bibliographic confidence**: Low — 「Hayashi, Tajima, Kumada」という著者組合せは連想的産物であり、「Tajima」の存在は確認できない（著者組合せ捏造パターンへの警告: Sonnet 67% hallucination rate for Kumada papers のため特に注意）。より可能性の高い著者組合せ候補：Hayashi + Katsuro + Kumada; または Hayashi + Okamoto + Kumada; または Hayashi + Kimura + Kumada。
* **Filling adequacy confidence**: Low — 論文の存在自体が不確実なため、EP との対応を評価できない。
* **Verification recommendation**: [必須]（同上 3 要因 + (d) Low confidence 候補複数）
* **Filling timescale category**: field-methodology (3-8 yr)
* **Bibliographic verification status**: pending
* **注記**: A-1（cis 富化の機構的説明を将来課題として送出）+ B-11（比率の分析条件不記載）+ U-3（kinetic/thermodynamic indeterminacy）の 3 項目が根拠を共有する SRG-6 の充填に対応。この EP の充填が確認されると、「cis/trans 比が速度論的産物である」という解釈が VQ-3（Mechanism）水準で得られる。

**Retrieval depth（EP-04a）**: Self-Tier **II** — 「Hayashi Tamio が Kumada グループで立体化学・機構を研究した」という背景知識から連想。推論経路：cis/trans stilbene の比の観察（論文本文）→ 機構的含意の解明が Hayashi の研究領域と一致→ 1970 年代後半の Hayashi–Kumada 立体化学論文が想定できる。「Tajima」という名前は不確実で、複数候補の triangulation で生じた。DB-findable: **uncertain**。Bib confidence: **Low**（著者名が不確実）。

---

**EP-05a [Quantitative-ranking substantiation pack]（第一群）**

* **充填するRI**: RI-05 [Qualitative overread] + RI-01 (secondary) — "selective" という定性的主張に定量的質量収支なし; ホモカップリング生成物（R–R）・β-脱離生成物の定量データなし
* **充填開始点**: Tamao et al., *Bull. Chem. Soc. Jpn.* 1976, **49**, 1958–1969（EP-01a と同一論文） — Full Paper I において代表的基質（n-BuMgBr + PhCl 等）の反応混合物中の副生成物量を GC または GC-MS で定量し、「選択的クロスカップリング」という主張に定量的根拠が与えられると想定。
* **充填確立点**: 同上
* **充填の性質**: Partial–Complete（推定） — RI-05 の中核（ホモカップリング R–R の定量）が Full Paper に含まれている可能性は高いが、eq (3) が予測する R–R の報告（U-1 の自己矛盾的不在）が明示的に扱われているかは不確実。
* **Bibliographic confidence**: Medium（EP-01a と同一論文）
* **Filling adequacy confidence**: Medium — Full Paper にホモカップリング byproduct の定量が含まれる可能性は合理的だが、確証なし。
* **Verification recommendation**: [必須]（EP-01a と同一 3 要因）
* **Filling timescale category**: format-driven (4 yr)
* **Bibliographic verification status**: pending
* **注記**: SRG-2（Selectivity claim without byproduct data）の中核 RI-05 を充填。B-1（選択性の定量的根拠なし）+ U-1（eq(3) が予測する R-R の不在）を解消するためには、R–R の定量データが必要。Full Paper での自動解消を期待するが、R–R の定量は明示的目的として設定されなかった可能性もある（Success-driven erasure パターンの候補）。

**Retrieval depth（EP-05a）**: Self-Tier **I** — EP-01a の Full Paper 想起と同時に、「byproduct quantification は Full Paper に含まれる」と想定。推論経路：SRG-2（selectivity without byproduct data）の重大性（B-1: convergence=3/3, high） → Kumada グループが批判に応える必要性 → Full Paper での対処が自然。DB-findable: **yes**（EP-01a と同一文献）。Bib confidence: **Medium**。

---

**EP-06a [Analogy-validation pack]（第一群）**

* **充填するRI**: RI-06 [Imported model] — 触媒サイクル全体を dipy-Ni 系から NiCl₂(dpe) 系へ同型性実証なしに輸入
* **充填開始点（候補 A）**: Tamao, Hayashi, Kumada（著者リスト不確実）, *J. Organomet. Chem.* **114**, C19 (1976) — NiCl₂(dpe) と化学量論量の n-BuMgBr の反応によりジオルガノニッケル中間体 1 の形成を実証する化学量論的実験を報告する短報として想定。
  *（注: C19 というページ番号は推定値であり、低信頼度）*
* **充填開始点（候補 B）**: Kiso, Tamao, Miyake, Kumada（著者リスト不確実）, *Tetrahedron Lett.* **1973 or 1974** — NiCl₂(dpe) または関連 Ni-diphosphine 錯体を用いた化学量論的 Grignard 反応の実験を含む短報。
  *（注: 著者リスト・年は低信頼度推定値）*
* **充填確立点**: 未特定（候補 A または B のいずれかが BCSJ Full Paper（1976）内の機構的データと合わせて確立点になる可能性）
* **充填の性質**: Partial（推定） — dpe-Ni 系での個々の化学量論的素反応（eq 2, eq 3 それぞれ独立）の実証は段階的に行われた可能性が高い。
* **Bibliographic confidence**: Low — 候補 A・B ともに著者リストと掲載詳細が連想的推測。特に Kiso（候補 B）については実際の著者かどうかの確認が取れていない（著者組合せ捏造パターンに注意）。
* **Filling adequacy confidence**: Medium — Kumada グループが自らの機構仮説を化学量論的に検証する動機と能力を持っていたことは確実であり、実験内容と EP の対応は原理的に成立する。
* **Verification recommendation**: [必須]（同上 3 要因）
* **Filling timescale category**: field-methodology (2-6 yr)
* **Bibliographic verification status**: pending
* **注記**: RI-06 + RI-03 の不可分共起（Stage 3 §6 制度設計パターン 6）に対応。EP-06a（eq 2 の化学量論的実証）と EP-03a（中間体の直接観測）の両方が解消されて初めて VQ-3 が達成される。自己充填パターン（Kumada グループ自身による続報）として期待されるが、著者は 5–10 年かけてこの作業を行った可能性。

**Retrieval depth（EP-06a）**: Self-Tier **II** — RI-06（サイクルレベル輸入）の充填を考えたとき、「最初に化学量論的実証を行うのは Kumada グループ自身」という推論から Tamao/Hayashi/Kumada の短報が連想された。推論経路：RI-06 の case-specific 実装（NiCl₂(dpe) + RMgBr の化学量論的反応）→ 1970 年代に有機金属化学の方法として実行可能→ Kumada グループが 1973–1977 年に報告した可能性。DB-findable: **uncertain**（特定論文の存在が不確実）。Bib confidence: **Low**。

---

**EP-07a [Boundary-test pack]（第二群）**

* **充填するRI**: RI-07 [Unsupported boundary] + RI-05 (secondary) — sp³ ハライドの失敗例なし; sp² 選択性の機構的根拠なし; 塩化物/臭化物/ヨウ化物の活性直接比較なし
* **充填開始点（sp² 選択性の実験的根拠）**: Tamao et al., *Bull. Chem. Soc. Jpn.* 1976, **49**, 1958–1969 — Full Paper においてスコープ節に sp³ ハライドの試験結果（不活性確認または選択性データ）が含まれる可能性、および PhCl/PhBr/PhI の活性比較実験が記載される可能性。
* **充填開始点（塩化物活性の定量比較）**: 未特定 — sp² C–Cl 結合の酸化的付加速度を定量した独立論文として、Fahey, *J. Am. Chem. Soc.* 1970 などの酸化的付加研究が間接的な充填候補となる可能性があるが、NiCl₂(dpe) 系固有の比較ではない。
* **充填確立点（sp³ ハライドの境界確立）**: 未特定 — sp³ ハライドが体系的に検討されなかった可能性があり、境界の確立は「否定的スコープ論文の不在」という形で充填されないまま残存する可能性がある（第三群への降格候補）。
* **充填の性質**: Partial（推定） — Full Paper が sp² 選択性の幾つかの実験的証拠を提供するが、sp³ 失敗例の網羅的記録（RI-07 要件）は部分的にしか充填されない可能性。
* **Bibliographic confidence**: Medium（Full Paper 部分のみ）/ Low（sp³ 失敗例専用論文は未特定）
* **Filling adequacy confidence**: Low — EP-07a の中核要件（sp³ ハライドの体系的失敗例 + sp² 選択性の機構的根拠）が独立した実験として発表されたかどうかが不確実。
* **Verification recommendation**: [必須]（同上要因）
* **Filling timescale category**: incentive-aligned (variable) — sp³ ハライドの境界の確立は Pd 系触媒の成功により一部 success-driven erasure が生じた可能性（後述 §E）
* **Bibliographic verification status**: pending
* **注記**: B-5（sp² 制限の肯定的再フレーム）+ B-6（塩化物高反応性の定量的根拠なし）+ A-2（スコープ拡張課題の送り出し）への対応。Pd 系触媒（Heck 反応, 1972; Suzuki 反応, 1979–）の台頭により、Ni 系固有の sp² 選択性の詳細な境界検証の動機が軽減された可能性あり（success-driven erasure の候補）。

**Retrieval depth（EP-07a）**: Self-Tier **III** — 「sp³ ハライドの Ni 触媒反応」という問いに対して、①否定結果は発表されにくい（publication bias）、②Full Paper に含まれる可能性、③後年の Pd 系成功による検証動機消失、という 3 経路を triangulation して最終的に「部分充填候補: BCSJ 1976 + 未充填部分残存」に到達。DB-findable: **uncertain**（充填が部分的で複数論文にまたがる可能性）。Bib confidence: **Medium (BCSJ 1976 部分) / Low (専用論文部分)**。

---

**EP-08a [Replication / uncertainty pack]（第三群）**

* **充填するRI**: RI-08 [Unquantified reliability] — cis/trans 比・収率の反復測定なし; 不確かさ記述なし
* **充填論文候補**: 未同定
* **充填の性質**: 非適用（第三群インセンティブ構造的未充填）
* **未充填の理由（第三群）**: 1970 年代の有機合成化学において、既存反応系の収率再現性統計や isomer 比の標準偏差を独立論文として発表するインセンティブは存在せず、「反復測定専用論文」は分野慣行として発表されなかった。EP-08a が要求する統計的有意性評価（n≥3 独立実験）は Full Paper（BCSJ 1976）でも収率の例数は 1–2 回程度が慣習であり、本質的にインセンティブ構造的未充填として残存する。
* **Filling timescale category**: non-applicable

```
incentive_structure_type: "インセンティブ構造的未充填"
note: 1970年代の有機合成化学では反復測定の統計的報告は慣行として存在せず、
      技術的には充填可能だが分野のパブリケーション規範上充填されない。
```

**Retrieval depth（EP-08a）**: Self-Tier **I（第三群判定として）** — RI-08（反復測定なし）のカテゴリを認識した時点で即座に「インセンティブ構造的未充填」に分類。推論経路：1970 年代有機合成化学の慣行 → 再現性統計の論文化は存在しない → 直接的には充填されない。DB-findable: **no**（充填論文自体が存在しない）。Bib confidence: N/A。

---

**EP-09a [Internal benchmark pack]（第一群）**

* **充填するRI**: RI-09 [External superiority] — Corriu–Masse の Ni(acac)₂ との直接比較なし; bidentate diphosphine の「必要条件」vs.「有効な選択肢」の区別未決
* **充填開始点（部分充填）**: Corriu, Masse, *J. Chem. Soc. Chem. Commun.* **1972**, 144 — Ni(acac)₂ 触媒を用いた類似 cross-coupling を報告した同時独立発見論文（論文本文の Note Added in Proof に直接引用）。NiCl₂(dpe) と同一反応が配位子なしの Ni(acac)₂ でも進行することを示す事実を提供するが、同一基質・同一条件での yield/selectivity 直接比較データは含まない（部分充填）。
* **充填確立点（体系的比較）**: Corriu 研究グループまたは Kumada 研究グループが後続論文で直接 head-to-head 比較を実施した論文（詳細不確実）— Corriu グループが 1973–1975 年に Ni 触媒の配位子効果に関する体系的比較研究を発表した可能性があるが、論文の特定には至らず。BCSJ 1976 Full Paper 内に Ni(acac)₂ との比較データが含まれる可能性もある。
  *（注: 充填確立点は Low confidence 推定。「Corriu, Masse, J. Organomet. Chem. 1973 or 1974」という候補が連想されたが著者組合せ捏造リスクあり）*
* **充填の性質**: Partial（1972 Corriu-Masse 同時発見論文）→ 不確実（完全充填論文は未特定）
* **Bibliographic confidence**: High（1972 Corriu-Masse については論文本文に直接引用のため）/ Low（後続比較研究については）
* **Filling adequacy confidence**: High（部分充填としての 1972 Corriu-Masse）/ Low（完全充填論文については）
* **Verification recommendation**: [必須]（(a) 1972 年以前 + (c) Kumada 反応命名 + (b) 著者ネットワーク密）
* **DOI**: 推定不可（1972 年 RSC、DOI 体系以前）; Web of Science での検索可能
* **Filling timescale category**: format-driven (0 yr for partial: concurrent paper) / incentive-aligned (variable for full head-to-head comparison)
* **Bibliographic verification status**: pending（Corriu-Masse 1972 は実質 verified に近い; 後続比較研究は pending）
* **注記**: CLA-1（配位子活性序列からの cis-geometry 仮説 + Corriu/Masse 問題）に対応。Corriu-Masse 1972 が論文本文に直接引用されているため EP-09a の部分充填論文として最高信頼性を持つ。完全充填（同一基質・条件での head-to-head 比較）が 54 年間に存在したかどうか自体が UQS の発見的意義を持つ。

**Retrieval depth（EP-09a）**: Self-Tier **I** — 論文本文の Note Added in Proof に Corriu-Masse が直接引用されているため、§0 の読み取りから即座に保持されていた。推論経路：「EP-09a の要件（RI-09: NiCl₂(dpe) vs Ni(acac)₂ の直接比較）」→「Ni(acac)₂ を使った論文は誰が書いたか」→「Corriu, Masse 1972: 論文本文に citation あり」という 1 ステップ。DB-findable: **yes**（Corriu, Masse 1972 は直接検索可能）。Bib confidence: **High（Corriu-Masse 1972 のみ）**。

---

### §B 末尾チェック：Bibliographic verification（v18.3、conditional triggering）

トリガー条件の評価：
- (a) 論文年代が古い（1970 年代）: **該当**
- (b) 著者ネットワーク密（Kumada グループから 10+ の関連論文）: **該当**
- (c) 反応名が author name に由来（Kumada coupling）: **該当**
- (d) Medium-Low confidence 候補が 2 件以上: **該当**

**全候補に [必須] Verification recommendation を付与する。**

既知の hallucination パターン（Kumada 論文特有）:
- Kumada 1972 における「Tamao-Sumitani-Hayashi-Kumada」は実在せず（実在: Tamao-Sumitani-Kumada）— 本 Stage 4 では Hayashi を BCSJ 1976 著者として挙げないよう注意
- 「Tajima」を Hayashi の共著者として挙げたが（EP-04a）、実在が不確認 → Low confidence として記録済み

---

## §C 推奨選定リスト

| 順序 | 論文 | 充填するEP | VQ水準 | 年代 | Bib.Conf | Fill.Conf | Verification |
|------|------|-----------|--------|------|----------|-----------|--------------|
| 1 | ⚠️ Tamao, Sumitani, Kiso, Zembayashi et al. (Kumada), *Bull. Chem. Soc. Jpn.* 1976, **49**, 1958 | EP-01a, EP-02a, EP-05a, (EP-07a 部分) | VQ-2 | 1976 | Medium | High | 必須 |
| 2 | Corriu, Masse, *J. Chem. Soc. Chem. Commun.* **1972**, 144 | EP-09a（部分） | VQ-3 補助 | 1972 | High | High | 必須 |
| 3 | ⚠️ Tamao, Hayashi, Kumada (著者リスト要確認), *J. Organomet. Chem.* **1977** 頃 | EP-06a, EP-03a（部分） | VQ-3 | 1975–1978 | Low | Medium | 必須 |
| 4 | ⚠️ Hayashi, (共著者不確実), Kumada, 立体化学論文, *Tetrahedron Lett.* または *BCSJ* **1975–1978** 頃 | EP-04a | VQ-3–4 | 1975–1978 | Low | Low | 必須 |
| 5 | ⚠️ Corriu 研究グループ またはKumada 研究グループによる NiCl₂(dpe) vs Ni(acac)₂ 直接比較論文（未特定） | EP-09a（完全充填） | VQ-3 | 1972–1980 | Low | Low | 必須 |

⚠️ マーク = Bibliographic verification 待機中（[必須] エントリ）

**選定理由:**

1番（BCSJ 1976 Full Paper）は VQ-2 到達に直結する EP-01a/EP-02a/EP-05a を一括充填するバンドル充填論文として最高優先度。Letter→Full Paper C23 auto-resolution の典型例であり、VQ-2 の EP 充填における最も投資効率の高い論文。Bibliographic confidence は Medium だが、この類の Follow-up Full Paper の存在は Kumada 1972 論文の科学史的文脈から構造的に確実。

2番（Corriu-Masse 1972）は論文本文に直接引用された唯一の High confidence 論文。EP-09a の部分充填として確実に機能し、「bidentate diphosphine は必要条件か有効な選択肢か」という VQ-3 関連の問いに対する科学史的証拠を提供する。UQS の発見的価値（D4-8）を実証的に例証する論文。

3番（機構論文: Tamao/Hayashi/Kumada J. Organomet. Chem.）は VQ-3 達成の根幹となる EP-06a/EP-03a の充填を担う候補。Bibliographic confidence は Low だが、VQ-3 への経路上で不可欠であり選定する。Post-hoc verification で存在が確認された場合のみ正式選定に昇格。

4番（立体化学論文: Hayashi et al.）は EP-04a（cis/trans 制御の速度論/熱力学区別）を充填し、SRG-6 の未解決問いに答える候補。信頼度が低いため、verification 完了後に昇格または代替候補への切り替えを行う。

5番（EP-09a 完全充填候補）は現状 Low confidence だが、Ni(acac)₂ vs NiCl₂(dpe) の head-to-head 比較の発見的価値が高く、verification 価値が高い位置として選定。存在しない場合は「54 年間の未充填 EP」として UQS の発見的意義の報告に転換する。

---

## §D VQ階層と充填時間順序の対応分析

**充填の時間軸（推定）：**

- VQ-2 要件: EP-01a, EP-02a, EP-05a → **1976 年** [Tamao et al. BCSJ 1976] [自己充填: format-driven]
- VQ-2 要件（補助）: EP-07a（部分）→ **1976 年**（推定, BCSJ Full Paper 内）[自己充填]
- VQ-3 要件: EP-09a（部分）→ **1972 年**（Corriu-Masse 同時発見）[分野横断充填: 独立グループ]
- VQ-3 要件: EP-06a → **1975–1978 年**（推定, Kumada グループ機構論文）[自己充填: field-methodology]
- VQ-3 要件: EP-03a → **1975–1978 年**（推定, σ-organonickel 分光）[自己充填: field-methodology]
- VQ-3 要件: EP-05a → **1976 年**（推定, BCSJ Full Paper + 独立 selectivity 論文）[自己充填]
- VQ-3–4 要件: EP-04a → **1975–1980 年**（推定, Hayashi–Kumada 立体化学論文）[自己充填: field-methodology]
- VQ-4 要件: EP-09a（完全充填）→ **未確定**（1972–1980 年の間? または長期未充填?）
- VQ-4 要件: EP-08a → **未充填**（インセンティブ構造的未充填）

**階層-時間対応の評価：**

VQ-2（Method）要件が最速（4 年: 1972→1976 BCSJ Full Paper）で充填され、VQ-3（Mechanism）要件が 3–8 年（機構論文群）で続く傾向は、VQ 階層の上昇と充填時間の増加という仮説を概ね支持する。ただし EP-09a（Corriu-Masse 1972）は VQ-3 補助として 0 年（同時発見）であり、外部グループによる充填が内部グループより速いという反例を示す点で興味深い。EP-08a（インセンティブ構造的未充填）が最高次 VQ-4 の前段で止まっているが、これは難易度ではなく publication incentive の問題であり、仮説の反例ではなくインセンティブ構造の証拠として解釈する。

**特筆すべきパターン：**

1. **自己充填（Kumada グループ）**: EP-01a/02a/05a/06a/07a は Kumada グループ自身による続報での解消が期待される典型的自己充填パターン。Letter→Full Paper 遷移（C23）として 4 年以内に発生。

2. **分野横断充填（Corriu-Masse 1972）**: EP-09a の部分充填論文が同時投稿の独立競合グループから提供されるという異例のパターン。これは Note Added in Proof に記録されており、「UQS が検出した欠落（D4-8: bidentate diphosphine の必要性の問い）」が独立グループによって直ちに（かつ意図なく）部分充填されたことを意味する。

3. **先行充填パターン（EP-09a 部分）**: Corriu-Masse は Kumada 1972 と同時期の投稿であり、「Ni(acac)₂ でも作動する」という事実は 1972 年時点で既に提供されていた。これは「先行充填」というよりも「同時提供」の特殊ケースであり、Note Added in Proof の非対称性（充填論文側は充填として認識していない）を示す。

4. **長期遅延充填の可能性（EP-09a 完全充填、EP-07a sp³ 境界確立）**: 完全 head-to-head 比較（NiCl₂(dpe) vs Ni(acac)₂、同一基質・条件）が 1972 年以降に発表されたかどうか、また sp³ ハライドの体系的失敗例が明示的に記録された論文が存在するかどうかについて、現時点では確認できない。これらが 54 年間未充填のまま残存している場合、UQS の発見的意義を持つ。

5. **著者回顧との照合**: Tamao 2002（`papers/ep/discussion/tamao2002/`）の mini-review では、著者が認識した「達成」と UQS が抽出した EP リストの差分が確認できる可能性。Tamao 2002 が D4-1（選択性の定量的根拠）や D4-8（Ni(acac)₂ との比較）を「未解決」として認識していない場合、「分野内部者には不可視の構造的不在」の直接証拠として記録できる。

---

## §E 未充填EPの発見的意義

**未充填EP一覧：**

**EP-08a [Replication / uncertainty pack]:**
* **未充填の理由**: インセンティブ構造的未充填。1970 年代の有機合成化学において、既存合成反応の収率の反復測定・統計的有意性評価は独立論文として発表されるインセンティブが存在せず、現在も同様の状況が継続する。技術的には充填可能（同一反応の n=5 以上の反復で標準偏差を報告することは trivial）だが、新規性を要求する出版規範がこの EP を恒常的に未充填状態に置く。
* **発見的意義**: あり。「ある収率が 76% とされているが、その不確かさはどの程度か」という問いは 54 年間にわたって有機合成化学において系統的に問われてこなかった。これは UQS が定義した「分野が慣習として体系的に避けてきた問い」の典型例であり、EP-08a の持続的未充填はインセンティブ構造の証拠として記録できる。
* **将来の充填可能性**: 低（技術的には高いが、出版動機の構造的問題が解決しない限り自発的な充填は生じない。機械学習・自動化実験（high-throughput screening）で統計的収率分布データが副産物として生成される時代では充填可能性が上昇する）。

**EP-07a（sp³ ハライド境界確立部分）—部分未充填：**
* **未充填の理由（推定）**: Success-driven question erasure（成功による問いの抹消）候補。Pd 触媒クロスカップリング（Heck 1972、Suzuki 1979–）が sp² ハライドでの汎用性を達成した後、Ni 固有の sp² 選択性の機構的根拠の検証需要が軽減された可能性。「Ni は sp² 選択的、Pd は sp³ でも使える」という分野全体の理解が固まったことにより、Ni 系での sp³ 試験の論文化動機が弱まった。sp³ ハライドの失敗例を Ni 系で明示的に記録することは「既知の限界の再確認」として発表インセンティブが低い。
* **発見的意義**: あり（推定）。「sp³ ハライドを試みたが不活性と確認した実験」が Kumada グループの論文に存在するかどうか自体が UQS の問いとして成立する。存在しない場合、「成功した代替技術（Pd 系）の登場によって元の問いの検証需要が社会的に消滅した」という C7 パターンの実例となる。
* **将来の充填可能性**: 中（sp³ ハライドの Ni 触媒反応が近年 Ni(0)/Ni(I)/Ni(II)/Ni(III) 多電子サイクルで再注目されており、1970 年代の「失敗」の mechanistic 根拠を明示する論文が DFT または動力学研究として登場する可能性）。

**EP-09a（完全充填部分: NiCl₂(dpe) vs Ni(acac)₂ head-to-head 比較）—未確認：**
* **未充填の理由（推定）**: 部分的インセンティブ構造的未充填。Corriu-Masse (1972) が Ni(acac)₂ でも cross-coupling が進行することを示した後、「NiCl₂(dpe) と Ni(acac)₂ で何が違うか」という定量比較実験は両グループが独立した研究プログラムを追求したことで自然に後退した可能性。競合グループ間での直接 head-to-head 比較は協力論文として発表されにくい。
* **発見的意義**: あり（高）。CLA-1（配位子活性序列からの cis-geometry 仮説）の独自性が 54 年間にわたって定量的に検証されていない場合、「bidentate diphosphine は本当に必要条件か有効な選択肢の一つか」という D4-8 の問いは UQS の最重要発見的 EP として記録できる。
* **将来の充填可能性**: 高（現代の DFT 計算と速度論実験によって NiCl₂(dpe) vs Ni(acac)₂ の触媒サイクルの違いを定量化することは技術的に容易。実際に近年のクロスカップリング計算化学論文が両系を比較している可能性があり、post-hoc verification で発見できる可能性）。

**VQ 階層逆転の診断:**

EP-08a（RI-08: 低 VQ 要件 / VQ-4 前段）が未充填であり、一方 EP-03a/EP-06a（RI-03/RI-06: 高 VQ 要件 / VQ-3）は（不確実ながら）充填候補が存在する。これは「科学的論理に基づく EP 充填順序（低 VQ→高 VQ）」と「出版インセンティブに基づく実際の充填順序（高 VQ→低 VQ）」の逆転パターンに相当し得る：機構解明論文（VQ-3 向け）は新規性が高く発表しやすい一方、反復測定論文（VQ-2/4 前段: EP-08a）は新規性が低く発表されない。この逆転が本論文でも観察されるか、post-hoc verification で確認することが推奨される。

---

## 付録：Retrieval Depth アノテーション マトリクス

| 充填論文 | 充填 EP | Self-Tier | 推論経路 | DB-findable? | Bib confidence |
|---|---|---|---|---|---|
| Tamao et al., *BCSJ* 1976, **49**, 1958 | EP-01a, EP-02a, EP-05a | I | JACS Comm 1972 → BCSJ Full Paper 遷移（C23）を直接想起; Kumada 1972 の科学史的継承として即座に浮かんだ | yes | Medium |
| Corriu, Masse, *Chem. Commun.* **1972**, 144 | EP-09a（部分） | I | 論文本文 Note Added in Proof に直接引用されており、読み取り時から保持 | yes | High |
| Tamao, Hayashi, Kumada, *J. Organomet. Chem.* 1976–1978（推定） | EP-06a, EP-03a | II | 「Kumada グループ → 機構研究 → Hayashi 参加」の 2–3 段階の連想; 具体的論文は不確実 | uncertain | Low |
| Hayashi, (共著者不確実), Kumada, 立体化学論文, 1975–1978（推定） | EP-04a | II–III | 「Hayashi + stereospecificity + vinyl halide」連想; 著者組み合わせ(Tajima 等)は複数候補の triangulation を経て生成 | uncertain | Low |
| Tamao et al., *BCSJ* 1976（同上）| EP-07a（部分） | I（部分）/ III（sp³失敗例部分） | Full Paper への自動解消（Tier I）と sp³ 境界確立専用論文の不在の推定（Tier III で「充填なし」に到達）| uncertain（sp³専用論文は no） | Medium（BCSJ 1976 部分）/ Low（専用論文） |
| [未特定] NiCl₂(dpe) vs Ni(acac)₂ 比較論文 | EP-09a（完全充填） | III | Corriu-Masse 1972 を起点に「その後 head-to-head 比較はあったか」を三角測量; 特定の論文は想起できず | uncertain | Low |
| [非充填] — | EP-08a | I（第三群判定として） | RI-08 = インセンティブ構造的未充填の直接認識; 充填論文の検索自体を行わなかった | no | N/A |

---

## 付録：考慮し棄却した候補

**棄却候補 1: Pd 触媒クロスカップリング一般（Heck, Suzuki, Negishi, Stille, Sonogashira）**
- 棄却理由: 金属が Pd であり、NiCl₂(dpe) 系の EP を直接充填しない。これらは paradigm-shift 候補（Pd 系による Ni 系の技術的継承/置換）として VQ-3 の問いの枠組みを変更するが、Kumada 1972 の EP（byproduct 定量、Ni 中間体観測、sp³ 境界確立）には対応しない。
- 棄却のタイミング: 「クロスカップリング + 充填論文」という一般連想が生じた直後に、「金属が違う」という判定で即座に棄却。

**棄却候補 2: Hayashi et al. の不斉 Kumada カップリング論文（BINAP-Ni, 1978–1984 年代）**
- 棄却理由: 不斉触媒設計という応用・拡張テーマであり、1972 年論文の EP（byproduct 定量、中間体観測、selectivity 定量化）を直接充填しない。stereochemistry の EP（EP-04a: cis/trans 速度論/熱力学区別）との関連はあるが、不斉カップリングの立体化学は vinyl halide の cis/trans 比の速度論的制御という 1972 年論文の具体的問いとは異なる。
- 棄却のタイミング: EP-04a の充填候補を検索する際に浮かんだが、「不斉カップリング = 別問い」と判断して棄却。

**棄却候補 3: Yamamoto, A. et al. の σ-organonickel 化学論文（dipy-Ni 系）**
- 棄却理由: Yamamoto, A. グループの σ-organonickel(II) 研究は重要だが、dipy-Ni（ジピリジル）系であり、dpe-Ni 系の EP-03a/EP-06a への直接充填ではない。Stage 3 §6（制度設計パターン 6: RI-06+RI-03 の不可分共起）が指摘するように、dipy-Ni 系の実証は dpe-Ni 系中間体の実在証明にはならない。
- 棄却のタイミング: EP-06a の充填候補を検索した際に浮かんだ（Yamamoto, A., Yamamoto, T., Ikeda が文献 11 として論文本文に引用）が、「これは輸入元の検証であり充填ではない」と判断して棄却。

**棄却候補 4: Tamao 2002 回顧 mini-review**
- 棄却理由: レビュー論文は EP を充填しない規則（§B ガイドライン 5）に基づき棄却。ただし著者の自己認識と UQS の EP リストの差分分析（§D step 4）の二次情報源として利用。
- 棄却のタイミング: `papers/ep/discussion/tamao2002/` の存在を CLAUDE.md から想起した際に、充填候補ではなく参照資料として再分類。

**棄却候補 5: Fahey, J. Am. Chem. Soc. 1970（sp² C–Cl の酸化的付加速度論）**
- 棄却理由: EP-07a の「塩化物の高反応性」の定量化として間接的に関連するが、NiCl₂(dpe) 系固有の ArCl/ArBr/ArI 活性比較ではなく、一般的な Ni(0) への酸化的付加速度論。case-specific 実装（同一 Grignard 試薬 + PhCl/PhBr/PhI の収率比較）に対応しない。
- 棄却のタイミング: EP-07a（塩化物活性定量化）の充填候補を三角測量した際に浮かんだが、「反応条件・基質が対応しない」と判断して棄却。

**棄却候補 6: Kochi 研究グループのラジカル機構論文（1970 年代）**
- 棄却理由: Kochi は Ni(I)/Ni(III) ラジカル経路の研究で知られるが、NiCl₂(dpe) 系固有の機構実証（EP-06a 要件）に直接対応するデータを含むかどうかが不確実。さらに Kochi の主要なカップリング研究は Fe/Cu 系（Tamura-Kochi 触媒）であり、dpe-Ni 系の中間体観測という要件との対応が indirect。
- 棄却のタイミング: EP-03a の充填候補として浮かんだ（U-2 黒色混合物の均一/不均一性の問いとの関連）が、「dpe-Ni 系固有ではない」と判断して棄却または Low confidence の注記として残留。
```
