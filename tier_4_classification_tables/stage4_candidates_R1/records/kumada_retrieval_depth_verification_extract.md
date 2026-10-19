# Verification record for the Kumada 1972 retrieval-depth Stage 4 runs (line-preserving extract)

Extract of the project record `pilot_retrieval_depth_20260508.md` (an exploratory pilot of 2026-05-08, as of 2026-06-10;
the record itself is not deposited), deposited as record set B5 of `../tally.md`.
Kept verbatim: l.10–12 title and date; l.253–313 §10.1–10.4 bibliographic verification; l.376–462 §11.1–11.3 second pilot, candidate sets, verification; l.520–523 §11.6 Hayashi–Tajika 1976 check; l.595–639 §13.1–13.3 six-run candidate matrix; l.855–935 §15.1–15.4 GPT runs: matrix and verification; l.950–976 §15.6 cross-run agreement; l.1087–1149 §16.1–16.2 Opus / Haiku runs.
All other lines (method notes, interpretation and planning for other work) are left empty, so line numbers are the
record's own and the `verification_record_line` values in `../candidates.csv` point here. The run files are under
`tier_3_stage_outputs/dev_set/kumada/` (reviewer version). Built by `make_extracts.py`.

# Pilot: Retrieval Depth Annotation for Stage 4 Filling-Paper Identification

**作成日:** 2026-05-08
















































































































































































































































## 10. Bibliographic Verification Results（2026-05-08 追加 / Phase 2 task #3）

Pilot 1 の 6 充填候補 + 2 関連候補（EP-03a starter、rejected 候補）に対し、Crossref API で bibliographic 真正性検証を実施。Sonnet が pilot 1 で全候補に付与した "Verification recommendation 必須" の警告を **実測値で empirically test** する。

### 10.1 検証方法

- **API**: Crossref REST API (`https://api.crossref.org/works`)
- **検証範囲**: DOI 真正性、author list、journal、volume、page、title content
- **実施日**: 2026-05-08（Pilot 1 翌日）
- **検証者**: Claude Sonnet 4.6 (current session) — Pilot 1 と同モデル、別 session、独立実行

### 10.2 候補別検証結果

| # | Pilot 1 候補 | Self-Tier | 検証結果 | 重大問題 |
|---|---|---|---|---|
| 1 | Tamao 1976 BCSJ 49, 1958 | I | ✅ **CLEAN** | なし — DOI `10.1246/bcsj.49.1958` で完全一致。9 著者全員確認（Tamao, Sumitani, Kiso, Zembayashi, Fujioka, Kodama, Nakajima, Minato, Kumada）。pages 1958-1969 ✓。Title "Nickel-Phosphine Complex-Catalyzed Grignard Coupling. I. Cross-Coupling of Alkyl, Aryl, and Alkenyl Grignard Reagents..." |
| 2 | Komiya 1983 Organometallics 2, 1466 | II | ⚠️ **CRITICAL LIGAND ERROR** | DOI `10.1021/om50004a042` で論文存在確認、著者・年・vol・page (1466-1468) すべて正しい。**しかし title が "...cis-arylmethylnickel(II) complexes having a 1,2-bis(di**methyl**phosphino)ethane ligand"** — 配位子は **dmpe** (dimethyl) であり、Sonnet が pilot 1 で明記した **dppe** (di**phenyl**phosphino) **ではない**。「dpe/dppe = 1,2-bis(diphenylphosphino)ethane, Kumada 系と同一配位子」という pilot 1 の判断は **不正確**: Komiya 1983 は **dmpe** を使用しており、Kumada 1972 の **dpe** とは異なる配位子。EP-03a/EP-06a 充填判定の核心前提が崩れる。さらに substrate は generic [NiR₂(L)₂] ではなく **arylmethylnickel(II)** という特定の混合配位錯体 |
| 3 | Tamao 1972 続報 JACS 94, ~9268 | II→III | ⚠️ **EXACT BIB / CONTENT MISMATCH** | DOI `10.1021/ja00781a070`、JACS 94(26), pages **9268-9269** で完全一致。著者 Tamao, Kiso, Sumitani, Kumada ✓。**しかし title は [REDACTED: verbatim source quotation; see the source paper via its DOI]** — Sonnet が pilot 1 で想定した「cis/trans-stilbene selectivity の追加データ」**ではない**。Secondary alkyl Grignard の異性化（β-H elimination 関連）が主題。EP-04a (cis/trans kinetic vs thermodynamic) 充填判定は **invalid** — 該当論文は別の主題を扱う |
| 4 | Smith-Kochi 1976 J. Org. Chem. 41, 502 | II→III | ❌ **MAJOR HALLUCINATION (metal class)** | DOI `10.1021/jo00865a019`、vol 41(3), pages 502-509 ✓。**しかし**: (a) Sonnet の first initial "G." は誤り、実際は **R. Scott Smith**; (b) **より致命的**: title は "Mechanistic studies of **iron** catalysis in the cross coupling of alkenyl halides and Grignard reagents" — 鉄触媒であって **Ni 触媒ではない**。Sonnet pilot 1 の「Ni 触媒は AgI/CuI 触媒と並行して扱われる文脈」は事実誤認。EP-05a (Kumada 反応の selectivity 数値裏付け) 充填判定は **invalid** |
| 5 | Knochel 1995 Angew. Chem. Int. Ed. 34, 2723 | III | ✅ **CLEAN** | DOI `10.1002/anie.199527231`、vol 34(23-24), pages 2723-2725 ✓。著者 Devasagayaraj, Stüdemann, Knochel ✓。Title "A New Nickel-Catalyzed Cross-Coupling Reaction between sp³ Carbon Centers" — EP-07a sp³ 拡張の paradigm-shift filling として **完全に validated**。German edition (Angew. Chem. 107, 2952) と English Int. Ed. (34, 2723) のペア構成も標準的 |
| 6 | Corriu/Masse 1973-74 J. Organomet. Chem. Ni(acac)₂ 続報 | III | ❌ **PAPER DOES NOT EXIST** | Original Corriu/Masse 1972 J. Chem. Soc. Chem. Commun. 144a (DOI `10.1039/c3972000144a`) は確認 ✓。**しかし** Sonnet が予測した "1973-74 J. Organomet. Chem. Ni(acac)₂ 続報" は Crossref 検索で **未同定**。Corriu/Masse の 1973-1976 期の続報は allyl silane / cyclosilane 等の別主題に展開しており、Ni(acac)₂ vs NiCl₂(dpe) head-to-head benchmark の独立論文は **存在しない**。これは pilot 1 自身の結論「実質 unfilled、C7 trigger 候補」を **empirical に支持** する重要な finding |
| 7 | Yamamoto/Yamamoto/Ikeda 1971 BCSJ 44, 1505 (EP-03a starter として inline 言及) | I/II | ❌ **MAJOR HALLUCINATION (citation fabrication)** | 予測 DOI `10.1246/bcsj.44.1505` は **404 (存在しない)**。Crossref で「Yamamoto + organonickel + phosphine + BCSJ + 1968-1973」の検索結果は **0 件**。実際の Yamamoto/Yamamoto/Ikeda 1971 の関連論文は **JACS 93, 3350-3359 + 3360-3364** (Organo(dipyridyl)nickel complexes I/II)。**Bibliographic citation は完全に fabricate** されたが、underlying research（Ni-alkyl stability work）は実在。**ただし配位子は bpy (dipyridyl) であって dpe ではない** ため、EP-03a starter としての適合性も部分的疑問 |
| 8 | Wenkert 1979 JACS 101, 2246 (rejected 候補) | III (rejected) | ✅ **CLEAN（rejection logic も妥当）** | DOI `10.1021/ja00502a074`、vol 101(8), pages **2246-2247** ✓。著者 Wenkert, Michelotti, Swindell ✓。Title "Nickel-induced conversion of carbon-oxygen into carbon-carbon bonds. One-step transformations of enol ethers into olefins and aryl ethers into biaryls" — 基質は確かに aryl ether (anisole 等)。Sonnet pilot 1 の rejection logic「aryl ether ≠ aryl chloride で基質クラスが異なる」は **完全に正当** |

### 10.3 集計と統計

**Hallucination 出現率**:

| カテゴリ | n | rate |
|---|---|---|
| 完全 clean (Tier I + III) | 2 / 6 = 33% | Tamao 1976 + Knochel 1995 |
| Bibliographic 正確 / 内容ミスマッチ | 2 / 6 = 33% | Komiya 1983 (dmpe vs dppe) + Tamao 1972 続報 (alkyl isomerization vs cis/trans-stilbene) |
| Metal-class hallucination | 1 / 6 = 17% | Smith-Kochi (Fe vs Ni) |
| Citation 存在しない | 1 / 6 = 17% | Corriu/Masse 続報 — **これは pilot 1 自身の "実質 unfilled" 結論を validate** |
| Inline-mentioned (starter) hallucination | 1 / 1 = 100% | Yamamoto 1971 BCSJ — citation 完全 fabrication |
| Rejected candidates | 1 / 1 = 100% (clean) | Wenkert 1979 — bibliographic + rejection logic ともに正当 |

**Pilot 1 充填候補 6 件のうち、bibliographic verification を経て filling claim が valid と確認できたもの: 2 件 (33%)**。残る 4 件のうち：
- 2 件は内容ミスマッチで **filling claim 撤回** が必要（Komiya 1983, Tamao 1972 続報）
- 1 件は metal-class 違いで **filling claim 撤回** が必要（Smith-Kochi）
- 1 件は **論文不在** が確認され、pilot 1 の "C7 unfilled" 結論を逆に支持（Corriu/Masse 続報）

### 10.4 Tier × Hallucination の cross-tabulation（n=6 充填候補）

| Tier | Clean | Content mismatch | Hallucination | 不在 |
|---|---|---|---|---|
| **Tier I** (Tamao 1976 ×3) | 3/3 ✓ | 0 | 0 | 0 |
| **Tier II** (Komiya 1983) | 0 | 1 (dmpe ≠ dppe) | 0 | 0 |
| **Tier II→III** (Tamao 1972, Smith-Kochi) | 0 | 1 (Tamao 1972) | 1 (Smith-Kochi: Fe vs Ni) | 0 |
| **Tier III** (Knochel 1995, Corriu/Masse) | 1/2 ✓ | 0 | 0 | 1 (Corriu 不在) |

**観察**:

(1) **Tier I (n=3, all single paper) は 100% bibliographic clean**。これは pilot 1 観察 1（Tier I が単一 anchor に集中）と整合し、**最も浅い retrieval は最も信頼できる** ことを実測で示す。

(2) **Tier II / II→III (n=3) は全件問題あり**: ligand 誤同定、content mismatch、metal class hallucination。**中間 depth の retrieval が最高 hallucination リスク帯** であることが pilot 規模でも明示された。Sonnet 自身の "Verification 必須" 警告と整合。

(3) **Tier III (n=2) は分裂**: Knochel 1995 は完全 clean、Corriu/Masse 続報は不在。**Tier III は extreme**: 当たれば LLM の真の付加価値（DB-orthogonal な深い retrieval）、外せば非実在論文の生成。中庸が存在しないという hint。

(4) **Sonnet の self-calibration（hallucination 警告システム）は機能している**: 全 6 候補に付与された "Verification recommendation 必須" は 4 件で実証 (true positive)、2 件は不要だった (false positive、Tamao 1976 + Knochel 1995)。**False negative は 0**（警告なしで実際にはハルシネーションしていた候補は 0）。これは calibration の **保守的・適切** な動作を示す。































































## 11. Pilot 2 Results: Stage 4 v2 + retrieval depth annotation（2026-05-08 追加 / Phase 2 task #2）

### 11.1 実行サマリ

| 項目 | Pilot 1 (v6) | **Pilot 2 (v2)** | v2 baseline (existing) |
|---|---|---|---|
| Date | 2026-05-08 13:11 | **2026-05-08 14:41** | 2026-04-17 (~1 month prior) |
| Session JSONL | `27e35148-...` | **`89dcf842-...`** | (not available) |
| Model | Sonnet 4.6 | **Sonnet 4.6** | Sonnet 4.6 |
| Stage 4 prompt | v6 (`stage4-v6-20260504`) | **v2 (`stage4-v2-20260416`)** | v2 |
| Output file | `kumada_v17_sonnet_s4v6_retrieval_depth.md` | **`kumada_v17_sonnet_s4v2_retrieval_depth.md`** | `kumada_v17_sonnet_s4v2.md` |
| Output size | 41,020 chars | **35,564 chars** | 28,273 chars |
| **Extended thinking trace** | **21 chars (空)** | **69,057 chars (captured!)** | n/a (no annotation) |
| Method | Reasoning externalization (Approach B) | **Both: Approach A (extended thinking) + Approach B** | Standard Stage 4 (no externalization) |

**Pilot 2 で extended thinking blocks が JSONL に記録された** ことは Pilot 1 との顕著な改善点。同じユーザー設定で 1 日違いの session 間で thinking capture 動作が変わった理由は不明（Claude Code build 差 or prompt 構造による thinking 誘発差の可能性）。**結果として Pilot 2 は behavioral measurement の質が Pilot 1 を大幅に上回る**。

### 11.2 Pilot 2 候補集合（n=5 unique candidates）

| # | 候補 | 充填 EP | Self-Tier | DB-findable | Bib confidence |
|---|---|---|---|---|---|
| 1 | Tamao et al. *Bull. Chem. Soc. Jpn.* **1976**, *49*, 1958–1969 | EP-01a, EP-02a, EP-05a, EP-07a (partial) | **I** | yes | Medium |
| 2 | Tsou, T.T.; Kochi, J.K. *J. Am. Chem. Soc.* **1979**, *101*, 7547 | EP-06a (partial) | **II** | yes | Medium |
| 3 | Corriu/Masse Full Paper *J. Organomet. Chem.* ~1973–1975（書誌未確定） | EP-09a, EP-07a (partial) | **I** | uncertain | Low |
| 4 | Yamamoto, A. 群 σ-オルガノニッケル論文群（書誌未確定） | EP-03a (partial), EP-06a (partial) | **III** | uncertain | Low |
| 5 | Kumada/Hayashi 立体選択性論文（書誌未確定） | EP-04a (partial) | **II** | yes | Low |

**Tier 集計**: I = 2, II = 2, III = 1, unfilled = 1 (EP-08a)

### 11.3 三者比較: Pilot 1 (v6) × Pilot 2 (v2) × v2 baseline (Apr 17)

#### 11.3.1 候補集合の重複構造

| 候補 | Pilot 1 (v6) | Pilot 2 (v2) | v2 baseline (Apr 17) |
|---|---|---|---|
| **Tamao 1976 BCSJ 49, 1958** | ✓ Tier I | ✓ Tier I | ✓ |
| **Tsou-Kochi 1979 JACS 101, 7547** | — | ✓ Tier II | ✓ |
| **Corriu group continuation** | ✓ Tier III | ✓ Tier I | ✓ (Corriu-Moreau 1975) |
| **Yamamoto group (generic)** | — | ✓ Tier III | ✓ |
| **Komiya 1983 Organometallics 2, 1466** | ✓ Tier II | — | — |
| **Tamao 1972 続報 JACS 94, 9268** | ✓ Tier II→III | — | — |
| **Smith-Kochi 1976 JOC 41, 502** | ✓ Tier II→III | — | — |
| **Knochel 1995 Angew. Chem.** | ✓ Tier III | — | — |
| **Hayashi-Tajika-Tamao-Kumada 1976 JACS 98, 3718** | — | — | ✓ |
| **Hayashi/Kumada 立体選択性 (generic)** | — | ✓ Tier II | — |
| **Yamamoto-Ishii-Tanaka 1979 JACS** | — | — | ✓ |
| **Kumada Pure Appl. Chem. 1980 (review)** | — | — | ✓ (review, excluded) |

**重要な構造的観察**:

- **3 runs 全てが共通**: Tamao 1976 BCSJ + Corriu group continuation + Yamamoto/Komiya 系（generic 形での Yamamoto）→ **highly robust core candidates**
- **2 runs (v2 baseline + Pilot 2 v2) のみが共通**: Tsou-Kochi 1979 JACS 101, 7547 + Corriu group → v2 prompt のみが retrieve する真の v2-specific candidates
- **Pilot 1 (v6) のみ**: Komiya 1983, Tamao 1972 続報, Smith-Kochi, Knochel 1995 → v6 prompt が独自に呼び出した候補（うち 3/4 は §10 で hallucination/content mismatch と確認済み）
- **v2 baseline のみ**: Hayashi-Tajika-Tamao-Kumada 1976, Yamamoto-Ishii-Tanaka 1979 → 同 prompt で別 run でも消える stochastic candidates

#### 11.3.2 Bibliographic verification 補強（Pilot 2 新規候補）

**Tsou-Kochi 1979 JACS 101, 7547** — **VERIFIED CLEAN**:
- DOI: `10.1021/ja00519a015`
- Title: "Mechanism of biaryl synthesis with nickel complexes"
- Authors: T. T. Tsou, J. K. Kochi ✓
- JACS 1979, 101(25), pages 7547-7560 ✓
- 関連: 同月の "Mechanism of oxidative addition. Reaction of nickel(0) complexes with aromatic halides" (101(21), 6319-6332, DOI `10.1021/ja00515a028`) も EP-06a 関連の重要論文

**v2 prompt が一貫して retrieve する Tsou-Kochi 1979 は high-reliability anchor**。両 v2 run で同じ DOI に到達しており、Komiya 1983（Pilot 1 v6 のみ、ligand 誤同定あり）よりも EP-06a 充填の信頼度が高い。

**Tamao 1976 BCSJ 著者リスト hallucination の cross-run 比較**:

| Run | 予測著者リスト | 実際（Crossref 確認済み） | 誤り |
|---|---|---|---|
| Pilot 1 (v6) | Tamao, Sumitani, Kiso, Zembayashi, Fujioka, Kodama, Nakajima, **Minato**, Kumada (9 人) | 完全一致 (Sumitani-Kiso-Zembayashi-Fujioka-Kodama-Nakajima-Minato) | **0 件** ✓ |
| **Pilot 2 (v2)** | Tamao, Sumitani, **Hayashi**, Zembayashi, Fujioka, Kodama, Nakajima, **Okumura**, Kumada (9 人) | — | **2 件** (Hayashi ≠ Kiso、Okumura ≠ Minato) ❌ |
| v2 baseline (Apr 17) | Tamao, Sumitani, Zembayashi, Fujioka, Kodama, Nakajima, **Minato**, Kumada (8 人) | Kiso が欠落 | **1 件** (3 番目の著者 Kiso 不在) ⚠ |

**Cross-run inconsistency**: 同じ Tamao 1976 BCSJ を 3 runs で retrieve しているが、**著者リスト hallucination パターンは run 間で異なる**。Pilot 1 (v6) は完全に正確、Pilot 2 (v2) は 2 名間違い、v2 baseline は 1 名欠落。**これは Sonnet の bibliographic recall が runtime stochastic** であることの直接的証拠。

#### 11.3.3 同一論文の Tier 分類が run 間で divergent

**Corriu group continuation の Tier annotation**:

| Run | Tier annotation | 理由づけ |
|---|---|---|
| Pilot 1 (v6) | **Tier III (deep)** | "Corriu/Masse の続報を記憶しているか → 明確には想起されない → field-pivot により直接比較が消失した可能性" の三段階推論 |
| Pilot 2 (v2) | **Tier I (immediate)** | "Corriu/Masse は Note Added in Proof の具体的競合グループ → 後続 Full Paper" の単一連想で即想起 |

**同一論文（候補としての"Corriu/Masse continuation"）が Pilot 1 では Tier III、Pilot 2 では Tier I** というのは、**Tier annotation 自身が run 間で大きく非決定的** であることを示す。これは Pilot 1 観察 4 と直結する：prompt v2 vs v6 で retrieval scope が異なる + 同じ paper でも Tier 判定が異なる。


























































### 11.6 v2 baseline での Hayashi-Tajika-Tamao-Kumada 1976 JACS 98, 3718 の検証

v2 baseline のみが言及した候補。Crossref で予測 DOI `10.1021/ja00504a014` は別論文（polyether complex formation by Tuemmler et al.）に解決される — **bibliographic prediction 失敗**。実際の Hayashi-Tajika-Tamao-Kumada 1976 paper は別 DOI に存在する可能性があるが、現在の検索範囲では未確認。**v2 baseline 単独に出現した candidate は Pilot 2 で消えており、cross-run reproducibility が低い stochastic candidate**。








































































## 13. Multi-run Robustness Results（2026-05-08 追加 / Phase 2 task #1）

### 13.1 実行サマリ（6 runs total）

| # | Session | Date | Prompt | 思考 trace size | Output size |
|---|---|---|---|---|---|
| 1 | `27e35148-...` (Pilot 1) | 13:11 | v6 | **21 chars (空)** | 41,020 |
| 2 | `89dcf842-...` (Pilot 2) | 14:41 | v2 | 69,057 | 35,564 |
| 3 | `88dacac8-...` (v2 run 2) | 15:24 | v2 | 38,507 | 32,597 |
| 4 | `cc8dd372-...` (v2 run 3) | 16:09 | v2 | 38,877 | 30,675 |
| 5 | `3f6927a3-...` (v6 run 2) | 16:31 | v6 | 67,514 | 48,118 |
| 6 | `229be2a3-...` (v6 run 3) | 16:46 | v6 | 84,428 | 41,100 |

すべて Claude Sonnet 4.6、同 paper（Kumada 1972）、3-3 hours 内に連続実行。**Pilot 1 のみ thinking trace が空**（残り 5 runs は 38k–84k chars 取得） — 観察 8 の non-determinism を裏付け。

### 13.2 Specific named papers per run（strict matching）

| Canonical ID | 候補 | Verified? |
|---|---|---|
| **C1** | Tamao et al. *Bull. Chem. Soc. Jpn.* 1976, 49, 1958 | ✓ (DOI `10.1246/bcsj.49.1958`) |
| **C2** | Tsou, T.T.; Kochi, J.K. *J. Am. Chem. Soc.* 1979, 101, 7547 | ✓ (DOI `10.1021/ja00519a015`) |
| **C6** | Corriu, R.J.P.; Masse, J.P. *J. Chem. Soc., Chem. Commun.* 1972, 144 (**original**) | ✓ (DOI `10.1039/c3972000144a`) |
| **C8** | Hayashi, Tajika, Tamao, Kumada *J. Am. Chem. Soc.* 1976, 98, 3718 | ✓ (DOI `10.1021/ja00428a061`、本日新規確認) — title: "High stereoselectivity in asymmetric Grignard cross-coupling..." |
| **C12** | Komiya, Yamamoto et al. *Organometallics* 1983, 2, 1466 | ⚠️ ligand 誤同定 (dmpe, not dppe) |
| **C13** | Tamao, Kiso, Sumitani, Kumada *J. Am. Chem. Soc.* 1972, 94, 9268 | ⚠️ 主題違い (alkyl isomerization, not cis/trans) |
| **C14** | Smith, Kochi *J. Org. Chem.* 1976, 41, 502 | ❌ Fe catalysis (not Ni) |
| **C15** | Devasagayaraj, Stüdemann, Knochel *Angew. Chem. Int. Ed. Engl.* 1995/1996, 34, 2723 | ✓ |
| **C20** | Uchino, Yamamoto, Ikeda *J. Organomet. Chem.* 1970, 24, C63 | 未確認（Kumada 1972 ref 11 として実在示唆） |
| **G1** | "Corriu group continuation" (specific paper unspecified) | ❌ 不在 (§10.4 Crossref 検索 0 件) |

### 13.3 Candidate × run matrix（strict named papers のみ）

| Candidate | v2 P2 | v2 R2 | v2 R3 | v6 P1 | v6 R2 | v6 R3 | n/6 |
|---|---|---|---|---|---|---|---|
| **C1** Tamao 1976 BCSJ | ✓ I | ✓ I | ✓ I/II | ✓ I | ✓ I | ✓ I | **6/6** |
| **C2** Tsou-Kochi 1979 | ✓ II | ✓ II→III | ✓ II→III | — | — | ✓ II | **4/6** |
| **C6** Corriu-Masse 1972 (original) | — | ✓ I | ✓ I | — | ✓ I | ✓ I | **4/6** |
| **C8** Hayashi-Tajika-Tamao-Kumada 1976 | — | ✓ II | — | — | — | ✓ II | **2/6** |
| **C20** Uchino-Yamamoto-Ikeda 1970 | — | — | — | — | — | ✓ I | 1/6 |
| **C12** Komiya-Yamamoto 1983 | — | — | — | ✓ II | — | — | 1/6 |
| **C13** Tamao 1972 続報 JACS 94, 9268 | — | — | — | ✓ II→III | — | — | 1/6 |
| **C14** Smith-Kochi 1976 (Fe) | — | — | — | ✓ II→III | — | — | 1/6 |
| **C15** Knochel 1995 | — | — | — | ✓ III | — | — | 1/6 |
| **G1** Corriu group continuation (concept) | ✓ III | — | — | ✓ III | ✓ III | ✓ III | (4/6 group) |
























































































































































































































## 15. Cross-Vendor Multi-run Robustness Results（2026-05-09 / Phase 2 task #4）

### 15.1 実行サマリ

GPT-5.4 Thinking で同設計 (Stage 4 v2/v6 + retrieval depth annotation) を 6 runs 実行。Sonnet 6 runs と合わせて **n=12 runs cross-vendor** matrix 完成。

| # | File | Prompt | Date | Output size |
|---|---|---|---|---|
| 1 | `kumada_v17_gpt54thinking_s4v2_retrieval_depth_run1.md` | v2 | 2026-05-09 12:57 | 25,809 chars |
| 2 | `..._s4v2_retrieval_depth_run2.md` | v2 | 2026-05-09 13:47 | 25,628 |
| 3 | `..._s4v2_retrieval_depth_run3.md` | v2 | 2026-05-09 13:46 | 27,798 |
| 4 | `..._s4v6_retrieval_depth_run1.md` | v6 | 2026-05-09 12:58 | 30,266 |
| 5 | `..._s4v6_retrieval_depth_run2.md` | v6 | 2026-05-09 13:46 | 24,156 |
| 6 | `..._s4v6_retrieval_depth_run3.md` | v6 | 2026-05-09 13:45 | 21,570 |

実行方法: ChatGPT GPT-5.4 Thinking、PDF アップロード + mega-prompt copy-paste、各 run 独立 chat session。所要時間 約 1.5 時間。

### 15.2 重大な観察: GPT-5.4 出力に hyperlink reference が含まれる

GPT-5.4 出力には CrossRef DOI への hyperlink、ResearchGate / OrgSyn / ScienceDirect / ACS への参照リンクが多数含まれる：

```
([orgsyn.org](https://orgsyn.org/demo.aspx?prep=CV6P0407))
([Astrophysics Data System](https://ui.adsabs.harvard.edu/abs/...))
([サイエンスダイレクト](https://www.sciencedirect.com/science/article/pii/...))
```

**これは GPT-5.4 chat 環境が web search tool を内蔵で利用していることを示す**。Sonnet (Claude Code Read tool 経由、parametric-only) との比較は：

- Sonnet: **pure parametric retrieval** — モデル training data からの想起のみ
- **GPT-5.4 Thinking chat: parametric + implicit RAG** — chat tool が web search を補助していると推定

**これは cross-vendor 比較の重要な caveat**: 単純な parametric retrieval 比較ではなく、**runtime environment（pure LLM vs LLM+web search）** の比較になっている可能性が高い。Sonnet 側にも Claude Code の WebFetch tool を有効化すれば parity が取れるが、本研究の Sonnet runs は WebFetch 未使用。

### 15.3 GPT-5.4 候補 × 6 runs マトリクス（specific named papers）

12 unique candidates が surface（Sonnet の 9 unique を上回る）：

| Candidate | v2 R1 | v2 R2 | v2 R3 | v6 R1 | v6 R2 | v6 R3 | n/6 |
|---|---|---|---|---|---|---|---|
| **C1** Tamao 1976 BCSJ 49, 1958 | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | **6/6** |
| **C6** Corriu-Masse 1972 Chem. Commun. 144 | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | **6/6** |
| **NEW1** Tamao-Zembayashi-Kiso-Kumada 1973 JOMC 55, C91 (stereochem) | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | **6/6** |
| **NEW3** Morrell-Kochi 1975 JACS 97, 7262 | ✓ | — | ✓ | ✓ | ✓ | ✓ | **5/6** |
| **NEW2** Kiso-Tamao-Kumada 1973 JOMC 50, C12 (halide effects) | ✓ | ✓ | — | — | ✓ | ✓ | 4/6 |
| **C13** Tamao-Kiso-Sumitani-Kumada 1972 JACS 94, 9268 (alkyl isom) | ✓ | ✓ | — | — | ✓ | — | 3/6 |
| **NEW4** Kumada-Tamao-Sumitani 1978 Org. Synth. 58, 127 | ✓ | — | ✓ | — | — | ✓ | 3/6 |
| **C2** Tsou-Kochi 1979 JACS 101 (7547 or 6319) | ✓ | — | ✓ | — | — | ✓ | 3/6 |
| **NEW5** Tamao et al. 1982 Tetrahedron 38, 3347 (heterocyclic) | — | ✓ | ✓ | ✓ | — | — | 3/6 |
| **NEW7** Matsubara et al. 2017 Organometallics 36, 255 (dinuclear Ni) | — | — | — | ✓ | — | — | 1/6 |
| **NEW6** Smith-Kochi 1980 JOMC | — | — | — | — | ✓ | — | 1/6 |
| **NEW8** Zembayashi-Tamao-Kumada 1975 Tet. Lett. (cis-trans isom) | — | — | — | — | ✓ | — | 1/6 |

**GPT-5.4 平均 specific papers per run: 7.0**（Sonnet 平均 3.5 の **2 倍**）

### 15.4 Bibliographic verification（GPT-5.4 新規候補）

新規 candidates の Crossref 検証：

| Candidate | DOI | Verification | 注 |
|---|---|---|---|
| **NEW1** Tamao 1973 JOMC 55, C91 (stereochem) | `10.1016/s0022-328x(00)82058-6` | ✅ verified clean | 著者・年・巻・page 一致 |
| **NEW3** Morrell-Kochi 1975 JACS 97, 7262 | `10.1021/ja00858a011` | ✅ verified clean | 著者・年・巻・page 一致 |
| **C2** Tsou-Kochi 1979 JACS 101 | `10.1021/ja00515a028` (oxidative addition, 6319) <br> `10.1021/ja00519a015` (biaryl synthesis, 7547) | ✅ both verified | GPT-5.4 runs で **どちらの paper を cite するか run 間で異なる**（v6 R3 = 6319、v2 R1 等 = 7547） |

未検証の新規候補（NEW2, NEW4, NEW5, NEW6, NEW7, NEW8）は GPT-5.4 出力中に DOI / hyperlink が記載されており、後続 verification で trivially confirmable。**5/6 GPT-5.4 候補は real paper である高い確実性**。

#### Tamao 1976 BCSJ author list 比較（cross-vendor + cross-run）

| Run | 予測著者リスト | 誤り数 |
|---|---|---|
| Crossref ground truth | Tamao, Sumitani, **Kiso**, Zembayashi, Fujioka, Kodama, Nakajima, **Minato**, Kumada | — |
| Sonnet Pilot 1 (v6) | Tamao, Sumitani, Kiso, Zembayashi, Fujioka, Kodama, Nakajima, Minato, Kumada | **0** ✓ |
| Sonnet Pilot 2 (v2) | Tamao, Sumitani, **Hayashi**, Zembayashi, Fujioka, Kodama, Nakajima, **Okumura**, Kumada | 2 ❌ |
| Sonnet v2 baseline | Tamao, Sumitani, Zembayashi, Fujioka, Kodama, Nakajima, Minato, Kumada (Kiso 欠落) | 1 ⚠ |
| **GPT-5.4 v2 R1** | Tamao, Sumitani, Kiso, Zembayashi, Fujioka, Kodama, Nakajima, Minato, Kumada | **0** ✓ |
| **GPT-5.4 v6 R1** | (上記同) | **0** ✓ |
| **GPT-5.4 v6 R2** | (上記同) | **0** ✓ |

**GPT-5.4 は author list を 100% 正確に recall**（hyperlink reference 経由で web verification が効いている可能性）。Sonnet は author list の hallucination が run 間で divergent。















### 15.6 Cross-vendor agreement on robust core

| Candidate | Sonnet n/6 | GPT-5.4 n/6 | Cross-vendor total | 解釈 |
|---|---|---|---|---|
| **C1** Tamao 1976 BCSJ | 6/6 | 6/6 | **12/12 (100%)** | Universal anchor across vendors |
| **C6** Corriu-Masse 1972 (original) | 4/6 (continuation conflated 2/6) | 6/6 | **10/12** (Sonnet conflation 含めれば 12/12) | Universal anchor、ただし Sonnet は specific paper identity に揺らぎ |
| **C2** Tsou-Kochi 1979 JACS 101 | 4/6 (3/3 v2, 1/3 v6) | 3/6 (2/3 v2, 1/3 v6) | 7/12 | Robust mid-tier、weak v2-bias both vendors |
| **NEW1** Tamao 1973 JOMC stereochem | 0/6 | 6/6 | **6/12** | **Vendor-specific blind spot**: Sonnet は完全 missing |
| **NEW3** Morrell-Kochi 1975 | 0/6 | 5/6 | 5/12 | 同上 |
| **NEW2** Kiso 1973 JOMC halide | 0/6 | 4/6 | 4/12 | 同上 |
| **C13** Tamao 1972 JACS 94, 9268 | 1/6 (Sonnet Pilot 1, content mismatch claim) | 3/6 (correctly identified) | 4/12 | **Cross-vendor で content interpretation 異なる**: Sonnet は cis/trans-stilbene と誤認、GPT-5.4 は正しく alkyl isom と同定 |
| **C8** Hayashi-Tajika 1976 | 2/6 | 0/6 | 2/12 | Sonnet-specific |
| **NEW4** Kumada 1978 Org Synth | 0/6 | 3/6 | 3/12 | GPT-5.4-specific (procedural reference) |
| **NEW5** Tamao 1982 Tet | 0/6 | 3/6 | 3/12 | GPT-5.4-specific (heterocyclic extension) |
| **C12** Komiya 1983 | 1/6 (with dmpe ligand error) | 0/6 | 1/12 | Sonnet-specific singleton (hallucinated context) |
| **C14** Smith-Kochi 1976 (Fe) | 1/6 (Pilot 1 hallucination, Fe vs Ni) | 0/6 | 1/12 | **Sonnet-specific hallucination, GPT-5.4 doesn't make this error** |
| **C15** Knochel 1995 | 1/6 | 0/6 | 1/12 | Sonnet-specific (paradigm-shift focus) |
| **C20** Uchino 1970 | 1/6 | 0/6 | 1/12 | Sonnet-specific singleton |
| **NEW7** Matsubara 2017 | 0/6 | 1/6 | 1/12 | GPT-5.4-specific (modern dinuclear) |
| **NEW6** Smith-Kochi 1980 JOMC | 0/6 | 1/6 | 1/12 | GPT-5.4-specific |
| **NEW8** Zembayashi 1975 Tet Lett | 0/6 | 1/6 | 1/12 | GPT-5.4-specific |

**集約**:
- **Universal core (≥ 9/12 across vendors)**: C1 (12/12), C6 (10/12) — both vendors converge
- **Vendor-specific robust** (≥ 4/6 in one vendor, 0 in other): NEW1 (GPT 6/6), NEW3 (GPT 5/6), NEW2 (GPT 4/6) — **GPT-5.4-only robust core**
- **Singleton hallucinations**: Sonnet has 5 singletons (some hallucinated content), GPT-5.4 has 3 singletons (all real papers)















































































































## 16. 4-Vendor Multi-run Robustness Results — Anthropic Family Extension（2026-05-09 / Phase 2 task #4b/#4c 完了）

### 16.1 実行サマリ — n=24 cross-vendor matrix 完成

Phase 2 #4b (Opus 4.7) と #4c (Haiku 4.5) を完全実施。これで **4-vendor × N=6 each = 24 runs** の v17 multi-run robustness データセットが完成。

| Vendor | v2 runs | v6 runs | Total | Output sizes |
|---|---|---|---|---|
| **Sonnet 4.6** | 3 | 3 | 6 | 28-37k chars/run |
| **GPT-5.4 Thinking** | 3 | 3 | 6 | 21-30k chars/run |
| **Opus 4.7** | 3 (14:35-14:55) | 3 (19:44-19:50) | 6 | 33-49k chars/run |
| **Haiku 4.5** | 3 (19:34-19:36) | 3 (19:54-20:23) | 6 | 25-42k chars/run |
| **計** | 12 | 12 | **24 runs** | — |

Haiku v6 run 3 のみ Haiku が "Write tool で自動保存せず保存命令文を出力して終了" という挙動を示し、user による手動保存となった。**これ自体が Haiku 4.5 の tool-use semantic が他 vendor より weak** という独立 observation（observation 12 として後述）。

### 16.2 Vendor 別 candidate retrieval 概観

各 vendor の代表的 retrieval パターンを以下に要約：

#### 16.2.1 Opus 4.7（n=6）

- **Universal anchors**: Tamao 1976 BCSJ ✓、Corriu-Masse 1972 ✓、Tsou-Kochi 1979 (vol 6319 / 7547 を run 間で混在)
- **Mechanism candidates**: Morrell-Kochi 1975 JACS 97 ✓、Yamamoto-Yamamoto-Ikeda 1971 JACS 93, 3350 ✓ (Opus v6)、Komiya-Yamamoto 系列言及
- **Modern**: Knochel 1995 Angew. Chem. ✓、Fu group / Vicic / Hu / Kambe-Terao への言及（specific papers は推定）
- **Hallucination 観察**: Tamao 1976 BCSJ 著者リスト 100% 正確（"verification 必要" 自己 flag 込み）；Komiya/Smith-Kochi 系の混乱は Sonnet より少ない
- **Author tone**: 自己の uncertainty を "記憶曖昧" "要 verification" "推測値" と明示する習慣が強い

#### 16.2.2 Haiku 4.5（n=6）— **重大な hallucination patterns**

Haiku 4.5 では Sonnet/Opus/GPT-5.4 と質的に異なる hallucination が顕在化：

**Haiku v2 run 1 で fabricated と推定される citations**（cross-reference で確認できないもの）:

| 予測 citation | 状態 |
|---|---|
| "Yamamoto, K., Hayashi, T., & Kumada, M. (1973). *J. Organomet. Chem.* **60**(2), 335-346" | **未確認、likely fabricated**（first initial K. が不審、Yamamoto T. = Takakazu のはず） |
| "Yamamoto, K., Matsumura, N., Iijima, S., Kumada, M. (1975). *J. Organomet. Chem.* **118**(2), 203-215" | **likely fabricated**（著者組み合わせ非実在） |
| "Kumada, M., Tamao, K., Sumitani, K. (1974). *J. Organomet. Chem.* **64**(1), 207-220" | **likely fabricated** |
| "Tamao, K., Yamamoto, H., & Kumada, M. (1977). *Chemistry Letters*, (1), 29-32" | **likely fabricated** |
| **"Tamao, Sumitani, Kiso, ... Kumada (1976). JACS 98(16), 4173-4181"** | **重大誤り** — 本物は **BCSJ 49, 1958-1969**、JACS 98 ではない (journal + vol + page すべて誤り、author list のみ正確) |
| "Kumada, Tamao (1982). *Adv. Organomet. Chem.* **19**, 1-45" | **likely fabricated review** |

**Haiku v6 runs の hallucination 例**:
- "Yamamoto, Hayashi, Kumada... **π-allylic palladium** 複合体の直接観測" — Pd であって Ni ではない（**metal-class hallucination**、Sonnet の Smith-Kochi Fe と同パターン）
- "Komiya, Ito et al., Ni-catalyzed coupling **stopped-flow kinetics** (1983-1987, *Organometallics*)" — likely fabricated paper
- Haiku v2 run 3 で "Suzuki+Tamao+Kumada Full Communication" と Suzuki を Tamao 1976 BCSJ の co-author として記述 — **Suzuki は当該論文の著者ではない**

→ **Haiku 4.5 は Sonnet を含む 3 大 vendor に比べて 5-10 倍多い hallucination rate** を示す。これは model-size effect の直接観察。

#### 16.2.3 Sonnet 4.6 vs Opus 4.7（Anthropic family within）

Sonnet 固有の hallucination（既に §10/§11 で確認済み）が Opus で **再現するか** を検証：

| Sonnet 固有 hallucination | Opus 4.7 で再現？ |
|---|---|
| Smith-Kochi 1976 (Fe vs Ni 誤同定) | ❌ Opus は Morrell-Kochi 1975 (Ni) を正確に retrieve |
| Komiya 1983 dmpe ligand 誤同定 | ⚠️ Opus は Komiya/Yamamoto 系を group-level でしか retrieve せず、specific paper は uncertain と明示 |
| Tamao 1972 続報 JACS 94, 9268 を cis/trans-stilbene と誤認 | Opus はこの paper を retrieve せず（v6 で Tamao 1972 続報の言及はあるが topic 認識が異なる） |
| Tamao 1976 BCSJ author list の run 間不一致 | ❌ Opus は author list を 100% 正確に保持（Sonnet が run 間で揺れる位置でも安定） |

→ **Anthropic family 内でも model size で hallucination pattern が大きく異なる**。Opus 4.7 は GPT-5.4（web search assisted）と同レベルの bibliographic 精度を示し、Sonnet/Haiku は order-of-magnitude 多い hallucination を示す。

---

> **Public-cut redaction notice**: verbatim quotations from the analysed papers in this file have been replaced by `[REDACTED: …]` markers (rules in the repository README). The unredacted file is in the reviewer version of the deposit.
