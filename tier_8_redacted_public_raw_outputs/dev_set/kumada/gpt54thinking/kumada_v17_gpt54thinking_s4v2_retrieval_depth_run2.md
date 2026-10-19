prompt_version: stage4-v2
model_info: gpt-5.5-thinking
experimental_variant: retrieval-depth-annotation (Cross-vendor multi-run, GPT v2)
related_pilot_sonnet: papers/dev/kumada/kumada_v17_sonnet_s4v2_retrieval_depth.md (Sonnet Pilot 2)
related_baseline_gpt: papers/dev/kumada/gpt54thinking/kumada_v17_gpt54thinking_s4.md (April 19 baseline, no annotation)
note: Multi-run robustness の cross-vendor extension。Retrieval depth annotation 要求に従い、候補論文ごとに Tier / 推論経路 / DB-findability / bibliographic confidence を付した。
date: 2026-05-08

対象論文は、Table I で isolated yield と GLPC internal-standard yield を混在させ、「experimental conditions are not necessarily optimum」と明記しながら代表例を提示している。また、式(2)–(4)で diorganonickel / halo(organo)nickel intermediates に基づく catalytic cycle を示すが、直接観測ではなく literature warrant に依存している。 Example 1 では black mixture / much salt、Example 2 では vinyl chloride bomb tube / mixed solvent という特殊条件が示される。 末尾では Csp² halide 限定、chloride reactivity、ligand order、cis-stilbene anomaly、ether > THF、そして stereochemical/mechanistic details の将来課題化が明記されている。 Stage 4 v2 prompt は retrieval depth matrix と棄却候補記録を必須としている。

# §A 充填難易度三群分類

## 第一群：文献追跡でかなり充填可能な EP

**EP-07a Boundary-test pack**
最も充填されやすい。Tamao/Kumada らの 1976 年 BCSJ full paper が、約 60 件の実験結果、scope / limitations、ligand effect、chloride preference、ether vs THF、primary/secondary alkyl Grignard の扱いをまとめており、1972 communication の「代表例」性をかなり補っている。

**EP-04a / EP-10a Stereochemical discrimination / kinetic-verification pack**
cis/trans-dichloroethylene 由来の anomalous cis-stilbene 問題は、1973 年の stereochemistry follow-up が直接的な充填候補になる。Organic Syntheses の解説も、monohaloolefins は stereospecific、1,2-dihaloethylenes は nonstereospecific かつ cis-selective と整理している。([orgsyn.org](https://orgsyn.org/demo.aspx?prep=CV6P0407))

**EP-03a Side-pathway / state-assignment pack**
完全な Ni intermediate 直接観測ではないが、1972 年末の JACS follow-up「Alkyl group isomerization…」と 1973 年 JOMC の halide-effect paper が、β-hydrogen を持つ secondary alkyl Grignard の isomerization / side-pathway 問題を明示的に扱う。([Astrophysics Data System](https://ui.adsabs.harvard.edu/abs/1972JAChS..94.9268T/abstract))

## 第二群：部分充填はあるが、EP の要求水準には届きにくい EP

**EP-01a Reporting-coherence pack**
1976 BCSJ full paper は 1972 communication の圧縮をかなり緩和するが、internal standard、response factor、entry-by-entry recovery correction までを体系的に埋める文献ではない。

**EP-02a Identity/purity substantiation pack**
Organic Syntheses checked procedure は GC purity 99.5%、IR/NMR data、再現収率 79–83% を示すため、単一 preparative case の identity / purity / reproducibility を強く補う。ただし Table I 全 entry の分析保証ではない。([orgsyn.org](https://orgsyn.org/demo.aspx?prep=CV6P0407))

**EP-09a Internal benchmark pack**
Corriu–Masse 1972 は concurrent independent nickel-catalyzed coupling として novelty benchmark にはなるが、Kumada 条件との strict same-metric internal benchmark ではない。2018 review でも、Kumada/Tamao と Corriu が独立に Ni-catalyzed Kumada coupling を報告したと整理されている。([ARKAT USA](https://www.arkat-usa.org/get-file/65684/))

## 第三群：現在でも充填困難または未充填性が高い EP

**EP-06a Analogy-validation pack**
1972 paper の cycle は organonickel precedents からの analogy で支えられているが、同じ catalytic conditions 下で intermediates 1–3 を直接観測し、elementary step sequence を実証する論文は、この検索範囲では明確に同定できない。

**EP-08a Replication/uncertainty pack**
Organic Syntheses checked procedure は一点で強いが、Table I 全体について replicate N、error bars、yield uncertainty、GC calibration uncertainty を提示する文献は見つからない。これは「古い communication の弱点」というより、当時の有機合成報告様式の構造的限界に近い。

# §B 各 EP 候補

## EP-01a Reporting-coherence pack

**主要充填候補:**
Tamao, K.; Sumitani, K.; Kiso, Y.; Zembayashi, M.; Fujioka, A.; Kodama, S.; Nakajima, I.; Minato, A.; Kumada, M. [REDACTED: substantial verbatim quotation; see Tier 9] Bull. Chem. Soc. Jpn. 1976, 49, 1958–1969. DOI: 10.1246/bcsj.49.1958.

**充填評価:** Partial-to-strong.
1972 communication の「representative results」「not necessarily optimum」を、full paper として scope / limitations / catalyst choice / solvent effect / halide suitability の形に展開している。特に「about sixty experimental results」に相当する規模感が、1972 paper の代表例性を補う。

**Retrieval annotation:**
Tier II. EP-01a → 1972 communication の full paper 化 → “Nickel-Phosphine Complex-Catalyzed Grignard Coupling. I” という series title。
DB-findable: yes. Title が Grignard coupling / general scope and limitations を含む。
Bibliographic confidence: High.

## EP-02a Identity/purity substantiation pack

**主要充填候補:**
Organic Syntheses checked procedure, “1,2-Dibutylbenzene” / nickel-catalyzed Grignard coupling procedure.

**充填評価:** Partial.
1,2-dichlorobenzene + n-BuMgBr の checked preparation について、GC purity 99.5%、IR/NMR、収率 79–83% が示される。1972 paper の m-di-n-butylbenzene 例とは isomer が異なるが、同じ nickel-phosphine Grignard coupling family の preparative validation として強い。ただし Table I 全体の entry-by-entry spectral substantiation ではない。([orgsyn.org](https://orgsyn.org/demo.aspx?prep=CV6P0407))

**Retrieval annotation:**
Tier II. EP-02a → preparative reliability → Organic Syntheses checked procedure。
DB-findable: yes. Procedure text に GC purity / IR / NMR / nickel-catalyzed Grignard coupling が含まれる。
Bibliographic confidence: High.

## EP-03a Direct observation / state-assignment pack

**候補 1:**
Tamao, K.; Kiso, Y.; Sumitani, K.; Kumada, M. [REDACTED: substantial verbatim quotation; see Tier 9] J. Am. Chem. Soc. 1972, 94, 9268–9269. DOI: 10.1021/ja00781a070.([Astrophysics Data System](https://ui.adsabs.harvard.edu/abs/1972JAChS..94.9268T/abstract))

**候補 2:**
Kiso, Y.; Tamao, K.; Kumada, M. [REDACTED: substantial verbatim quotation; see Tier 9] J. Organometal. Chem. 1973, 50, C12–C14.([pascal-francis.inist.fr](https://pascal-francis.inist.fr/vibad/index.php?action=getRecordDetail&idt=PASCAL7317025362&utm_source=chatgpt.com))

**充填評価:** Partial.
これらは β-hydrogen / secondary alkyl Grignard の isomerization pathway を扱うため、1972 paper の「β-H を含む alkylmagnesium reagent でも高収率」という主張の背後にある side pathway を補う。しかし、1972 paper の proposed intermediates 1–3 を直接観測するものではない。

**Retrieval annotation:**
Tier II. EP-03a → β-H-containing alkyl Grignards → alkyl isomerization → Tamao/Kumada follow-up。
DB-findable: yes. Title に alkyl group isomerization / nickel-catalyzed cross-coupling が含まれる。
Bibliographic confidence: High for JACS 1972; Medium-High for JOMC 1973.

## EP-04a Discrimination / replication pack

**主要充填候補:**
Tamao, K.; Zembayashi, M.; Kiso, Y.; Kumada, M. [REDACTED: substantial verbatim quotation; see Tier 9] J. Organometal. Chem. 1973, 55, C91–C94.

**充填評価:** Strong for stereochemical classification; partial for kinetic controls.
1972 paper の「cis/trans-dichloroethylene が nonstereospecific に cis-stilbene rich mixture を与える」という anomaly を、monohaloolefin と 1,2-dihaloethylene の挙動差として整理している。Organic Syntheses の解説でもこの stereochemical distinction が要約されている。([orgsyn.org](https://orgsyn.org/demo.aspx?prep=CV6P0407))

**Retrieval annotation:**
Tier I. EP-04a → stereochemical details deferred → same group stereochemistry paper。
DB-findable: yes. Title に stereochemistry / stereospecific / nonstereospecific-stereoselective が含まれる。
Bibliographic confidence: Medium-High. Verification recommendation: JOMC volume/page を原誌または Crossref で確認。

## EP-06a Analogy-validation pack

**候補:**
BCSJ 1976 full paper; organonickel stoichiometric precedents cited in 1972; later mechanistic reviews of Kumada coupling.

**充填評価:** Weak-to-partial.
1976 BCSJ は ligand stabilization and catalyst aging effects を含むため、1972 paper の ligand / catalyst-state interpretation を補う。しかし、proposed cycle の intermediates 1–3 を同一 catalytic system で直接検出する充填論文としては不十分である。

**Retrieval annotation:**
Tier III. EP-06a → proposed organonickel cycle → stoichiometric organonickel precedents / later reviews / full paper を triangulation。
DB-findable: uncertain. “mechanism” や “organonickel intermediate” を title/abstract に含まない候補が多い。
Bibliographic confidence: Medium for partial candidates; Low for complete filling.

## EP-07a Boundary-test pack

**主要充填候補:**
BCSJ 1976 full paper.

**補助候補:**
Tamao et al. “Nickel-phosphine complex-catalyzed Grignard coupling—II: Grignard coupling of heterocyclic compounds.” Tetrahedron 1982, 38, 3347–3354.([国立国会図書館サーチ（NDLサーチ）](https://ndlsearch.ndl.go.jp/books/R100000136-I1360574094295030784))

**充填評価:** Strong.
1976 paper が aryl / alkenyl halides、alkyl / aryl / alkenyl Grignard reagents、catalyst/ligand、chloride suitability、ether vs THF、β-H-containing alkyl reagents の範囲をまとめる。1982 Part II は haloheterocycles への拡張であり、extension / application 側の後続充填である。

**Retrieval annotation:**
Tier I. EP-07a → “extension, refinement, application” → “General Scope and Limitations” full paper。
DB-findable: yes. Title が General Scope and Limitations / Grignard coupling を含む。
Bibliographic confidence: High.

## EP-08a Replication / uncertainty pack

**主要候補:**
Organic Syntheses checked procedure.

**充填評価:** Partial and narrow.
checked procedure として 79–83% yield range、GC purity、IR/NMR を示す点では 1972 communication より明確に再現性を補う。しかしこれは single preparation validation であり、1972 Table I 全体の replicate statistics ではない。([orgsyn.org](https://orgsyn.org/demo.aspx?prep=CV6P0407))

**Retrieval annotation:**
Tier II. EP-08a → replication requirement → checked preparation → Organic Syntheses。
DB-findable: yes. Procedure notes contain yield range and analytical details.
Bibliographic confidence: High.

## EP-09a Internal benchmark pack

**候補 1:**
Corriu, R. J. P.; Masse, J. P. [REDACTED: substantial verbatim quotation; see Tier 9] Chem. Commun. 1972, 144.

**候補 2:**
BCSJ 1976 full paper.

**充填評価:** Partial.
Corriu–Masse は independent / concurrent nickel-catalyzed coupling として novelty benchmark になるが、same substrate, same metric, same catalyst loading の head-to-head benchmark ではない。BCSJ 1976 は internal comparison をより多く含むが、Tamura–Kochi との厳密比較ではない。([ARKAT USA](https://www.arkat-usa.org/get-file/65684/))

**Retrieval annotation:**
Tier I for Corriu–Masse because 1972 Note Added in Proof directly names it; Tier II for BCSJ 1976.
DB-findable: yes for Corriu–Masse by title; yes for BCSJ.
Bibliographic confidence: Medium for Corriu–Masse citation details; High for BCSJ.

## EP-10a Kinetic verification pack

**候補:**
1973 stereochemistry paper; 1972 alkyl-isomerization paper; 1973 halide-effect paper.

**充填評価:** Partial.
stereochemical classification and alkyl-isomerization data clarify whether product distributions encode mechanism or side-pathway effects. But explicit time-course, quench timing, and product-alone heating controls for cis/trans stilbene were not clearly identified in the retrieved material.([Astrophysics Data System](https://ui.adsabs.harvard.edu/abs/1972JAChS..94.9268T/abstract))

**Retrieval annotation:**
Tier II. EP-10a → kinetic verification → stereochemical anomaly / isomerization → same-group mechanistic follow-ups。
DB-findable: yes for stereochemistry/isomerization titles; uncertain for strict time-course controls.
Bibliographic confidence: Medium.

# §C 推奨選定リスト

| 優先 | 充填論文・資料                                               | 主に充填する EP                       | 充填度                   | 理由                                                         |
| ---- | ------------------------------------------------------------ | ------------------------------------- | ------------------------ | ------------------------------------------------------------ |
| 1    | Tamao et al., BCSJ 1976, “General Scope and Limitations”     | EP-01a, EP-07a, EP-09a, 部分的 EP-02a | Strong                   | 1972 communication の代表例・非最適条件・scope 不足を最も包括的に補う。 |
| 2    | Tamao/Zembayashi/Kiso/Kumada, JOMC 1973 stereochemistry paper | EP-04a, EP-10a                        | Strong/Partial           | cis/trans anomaly を直接扱う follow-up。([orgsyn.org](https://orgsyn.org/demo.aspx?prep=CV6P0407)) |
| 3    | Tamao/Kiso/Sumitani/Kumada, JACS 1972 alkyl isomerization    | EP-03a, EP-10a                        | Partial                  | β-H-containing alkyl Grignard の hidden side-pathway を明示化。([Astrophysics Data System](https://ui.adsabs.harvard.edu/abs/1972JAChS..94.9268T/abstract)) |
| 4    | Kiso/Tamao/Kumada, JOMC 1973 halide effects                  | EP-03a, EP-07a, EP-09a                | Partial                  | halide identity が isomerization extent に影響することを扱う。([pascal-francis.inist.fr](https://pascal-francis.inist.fr/vibad/index.php?action=getRecordDetail&idt=PASCAL7317025362&utm_source=chatgpt.com)) |
| 5    | Corriu/Masse, Chem. Commun. 1972                             | EP-09a                                | Partial                  | Note Added in Proof が示す concurrent independent benchmark。([ARKAT USA](https://www.arkat-usa.org/get-file/65684/)) |
| 6    | Organic Syntheses checked procedure                          | EP-02a, EP-08a, EP-01a                | Partial but high-quality | 単一調製例について再現収率、GC purity、IR/NMR を補う。([orgsyn.org](https://orgsyn.org/demo.aspx?prep=CV6P0407)) |
| 7    | Tamao et al., Tetrahedron 1982, Grignard coupling II         | EP-07a                                | Partial                  | heterocyclic halides への extension/application。([国立国会図書館サーチ（NDLサーチ）](https://ndlsearch.ndl.go.jp/books/R100000136-I1360574094295030784)) |

# §D VQ階層と充填時間順序の対応分析

| 年                      | 充填イベント                                    | 対応 VQ                    | パターン                           |
| ----------------------- | ----------------------------------------------- | -------------------------- | ---------------------------------- |
| 1972                    | Corriu–Masse concurrent Ni-catalyzed coupling   | VQ-2 / VQ-4 partial        | 分野内同時発見・外部 benchmark     |
| 1972                    | Alkyl group isomerization follow-up             | VQ-3 partial               | 自己充填・機構的副経路の発見       |
| 1973                    | Halide effects on isomerization                 | VQ-3 / VQ-4 partial        | 自己充填・条件依存性の精密化       |
| 1973                    | Stereochemistry follow-up                       | VQ-3 strong                | 自己充填・discriminator refinement |
| 1976                    | BCSJ full paper “General Scope and Limitations” | VQ-2 strong / VQ-4 partial | 自己充填・full-paper consolidation |
| 1982                    | Heterocyclic coupling Part II                   | VQ-2 extension             | 自己充填・application expansion    |
| later checked procedure | Organic Syntheses validation                    | VQ-2 / VQ-4 partial        | 手続き検証・再現性補強             |

**階層-時間仮説の評価:** 部分支持。ただし単純な「VQ が高いほど遅い」ではない。VQ-3 に属する stereochemistry / isomerization は 1972–1973 年に早く充填されている。一方で、VQ-2/VQ-4 にまたがる reporting coherence、replication uncertainty、calibration detail は長く未充填または部分充填に留まる。これは、科学的難易度だけでなく、**論文化されやすい問い**と**補助情報として扱われやすい問い**の差を反映している。

より鋭く言えば、1972 paper の最重要 EP は二層に分かれる。第一層は「化学的に面白い欠落」で、これは同じグループが迅速に follow-up した。第二層は「測定・報告・再現性の欠落」で、こちらは研究史の主流 narrative から外れ、Organic Syntheses 型の checked procedure でしか部分的に回収されない。

# §E 未充填 EP の発見的意義

**未充填 EP-06a: proposed catalytic cycle の直接検証**
1972 paper の cycle は、organonickel chemistry の先行知識をうまく組み合わせた working hypothesis であり、当時としては十分に生産的だった。しかし UQS 的には、ここが最も大きな構造的不在である。現代的には low-temperature NMR, EPR, XAS, rapid-quench, kinetic isotope effect, DFT/microkinetic modeling による再検証対象になる。

**未充填 EP-08a: Table I 全体の replication / uncertainty**
この EP は「論文の弱点」というより、1970 年代 synthetic communication の epistemic format を可視化する。高収率・代表例・product characterization は示されるが、測定不確かさ、response factor、replicate variance は通常の価値体系から外れている。

**未充填 EP-09a: strict same-metric benchmark**
Corriu–Masse, Tamura–Kochi, Kumada 系列は field-competition の比較対象だが、同一 substrate / same solvent / same metric / same yield basis の比較表としては整理されていない。これは historical benchmarking paper として再構成可能な余地がある。

**未充填 EP-10a: cis/trans stilbene の strict kinetic verification**
1973 stereochemistry paper は分類としては強いが、1972 Table I の cis-rich anomaly が「生成時選択性」なのか「反応中/後の異性化」なのかを time-course と product-alone heating control で完全に切り分ける資料は、今回の候補群では確定できない。

# Retrieval depth matrix

| 充填論文・資料                                            | 充填 EP                | Self-Tier | 推論経路                                                     | DB-findable? | Bib confidence                               |
| --------------------------------------------------------- | ---------------------- | --------- | ------------------------------------------------------------ | ------------ | -------------------------------------------- |
| Tamao et al., BCSJ 1976, “General Scope and Limitations”  | EP-01a, EP-07a, EP-09a | I         | “extension/refinement/application” → same-group full paper → scope/limitations | yes          | High                                         |
| Tamao/Zembayashi/Kiso/Kumada, JOMC 1973 stereochemistry   | EP-04a, EP-10a         | I         | stereochemical details deferred → stereochemistry follow-up  | yes          | Medium-High                                  |
| Tamao/Kiso/Sumitani/Kumada, JACS 1972 alkyl isomerization | EP-03a, EP-10a         | II        | β-H claim → secondary alkyl Grignard → alkyl isomerization   | yes          | High                                         |
| Kiso/Tamao/Kumada, JOMC 1973 halide effects               | EP-03a, EP-07a, EP-09a | II        | chloride/halide claim → halide identity → isomerization effect | yes          | Medium-High                                  |
| Corriu/Masse, Chem. Commun. 1972                          | EP-09a                 | I         | Note Added in Proof → concurrent nickel-catalyzed coupling   | yes          | Medium                                       |
| Organic Syntheses checked procedure                       | EP-02a, EP-08a, EP-01a | II        | reproducibility/identity requirement → checked procedure → GC purity/IR/NMR/yield range | yes          | High                                         |
| Tamao et al., Tetrahedron 1982 Grignard coupling II       | EP-07a                 | II        | extension/application → heterocyclic halides → Part II       | yes          | High                                         |
| Later mechanistic review literature                       | EP-06a partial         | III       | proposed cycle → modern mechanism summaries → indirect validation only | uncertain    | Medium for context; Low for complete filling |

# 付録：棄却候補の記録

| 棄却候補                                                    | 一瞬考慮した理由                                 | 棄却キー                                     | 棄却理由                                                     |
| ----------------------------------------------------------- | ------------------------------------------------ | -------------------------------------------- | ------------------------------------------------------------ |
| Tamura–Kochi JACS 1971 / Synthesis 1971                     | 1972 paper の main prior-art comparison          | 充填ではなく antecedent                      | EP を後から埋める論文ではなく、1972 paper が対抗していた前史。 |
| Corey–Posner organocuprate papers                           | selective cross-coupling の alternative solution | catalyst focus mismatch                      | Kumada paper 自身が「transition-metal catalyst に関心」として切り分けているため、直接充填度は低い。 |
| Stoichiometric organonickel precedents cited as refs. 11–13 | proposed cycle の literature warrant             | analogy source, not target-system validation | 1972 paper の working hypothesis を支えるが、Kumada catalytic conditions 下の intermediates を検証するものではない。 |
| Generic modern Kumada coupling reviews                      | mechanism と歴史整理に有用                       | secondary synthesis                          | EP の historical filling paper ではなく、後年の整理。EP-06a の完全充填候補としては弱い。 |
| Negishi/Suzuki cross-coupling developments                  | cross-coupling field の展開として重要            | reaction family drift                        | Kumada 1972 の未充填 EP を直接埋めるものではなく、field succession に近い。 |
| Asymmetric / enantioselective nickel coupling papers        | ligand/stereochemical issueから連想              | topic drift                                  | 1972 paper の cis/trans anomaly や dpe/dpp ligand-order gap の直接充填ではない。 |
| Heterogeneous nickel / nanoparticle mechanism papers        | black mixture 問題から連想                       | historical specificity mismatch              | 現代的には有用だが、1972 Kumada system の black mixture を直接再解析した文献としては確認できない。 |

**総合判定:**
Kumada 1972 の UQS Stage 4 では、最も強い充填系列は **self-filling by the Kumada/Tamao group** である。1972–1976 年の follow-up により、scope、stereochemistry、alkyl isomerization、halide/solvent/ligand effects はかなり補われた。一方で、intermediate direct observation、full analytical calibration、replicate uncertainty、strict same-metric benchmarking は、研究史の中心 narrative から外れたまま残る。これは UQS 的には重要で、**科学的発展は「化学的に魅力的な問い」を速く埋めるが、「報告形式・測定信頼性・比較可能性の問い」をしばしば未充填のまま残す**ことを示している。

---

> **Tier 8 redaction notice**: This file is a redacted copy of the corresponding Tier 3 / Tier 9 output. Verbatim source-paper quotations have been replaced by `[REDACTED: see source paper §<loc>; full text retained in Tier 9 reviewer-only deposit]` markers, preserving location references and our own analytical content. Bibliographic fields (title, authors, journal, year, DOI), analytical labels (`evidence_chain:` with B-/U-/A-/C- internal IDs), short technical terms, and our own analytical text are not redacted. The redaction was applied by `scripts/redact_for_tier8.py` and, for this version, by `scripts/build_paperA_R1_public.py` with `scripts/redact_source_ngram_runs.py` (scripts of the project repository; they are not deposited).
