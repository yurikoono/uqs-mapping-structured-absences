prompt_version: stage4-v6
stage4_prompt_version: stage4-v6-20260504
model_info: gpt-5.4-thinking
experimental_variant: retrieval-depth-annotation (Cross-vendor multi-run, GPT-5.4 v6)
related_pilot_sonnet: papers/dev/kumada/kumada_v17_sonnet_s4v6_retrieval_depth.md (Sonnet Pilot 1)
related_baseline_gpt: papers/dev/kumada/gpt54thinking/kumada_v17_gpt54thinking_s4.md (April 19 baseline)
date: 2026-05-08

添付プロンプトでは、Stage 4 の目的は EP 充填論文の同定と選定マップ生成であり、追加要件として各候補に Self-Tier、推論経路、DB-findability、bibliographic confidence、統合マトリクス、棄却候補記録を付すことが指定されている。
対象論文は Table I に代表例・収率・分析法注記をまとめ、同時に diorganonickel / halo(organo)nickel を含む作業仮説的触媒サイクルを提示している。 末尾では “Only Csp2 halides”、chloride reactivity、ligand order、cis-stilbene anomaly、ether superiority を挙げつつ、mechanistic / stereochemical details を future work に送っている。

# §A. EP 充填難易度の三群分類

## 第一群：文献で明確に追跡可能

**EP-07a Boundary-test pack**
Kumada 1972 が “Only Csp2 halides”、chloride advantage、ether superiority、β-hydrogen-containing alkyl Grignards を claim しているため、scope / limitation の full paper 展開として追跡しやすい。Stage 3 の case-specific 実装でも chloride/bromide/iodide、Csp2/non-Csp2、ether/THF の matched comparison が要求されている。

**EP-04a Discrimination / replication pack**
cis/trans-1,2-dichloroethylene から cis-rich stilbene が出る anomaly は、後続の stereochemistry 論文として独立主題化されやすい。Kumada 1972 本文でもこの anomaly は明示されている。

**EP-10a Kinetic verification pack**
EP-04a と結合して追跡可能。ただし “time-course / product-alone heating / quench timing” まで要求すると、後続論文が完全充填しているかは不確実。第一群だが完全充填ではなく部分充填候補。

**EP-03a Direct-observation / state-assignment pack**
diorganonickel / halo(organo)nickel intermediates の検証は organonickel mechanism 文献として追跡可能。ただし original [NiCl2(dpe)] / Grignard / aryl-vinyl halide system そのものの direct observation ではなく、Kochi 系などの analogical mechanism filling になりやすい。

**EP-06a Analogy-validation pack**
EP-03a と同じ文献群で部分充填される。原論文の working hypothesis は先行 stoichiometric organonickel chemistry に依存しており、その analogy が後続 mechanistic work でどこまで検証されたかが焦点になる。

## 第二群：間接的に追跡可能

**EP-09a Internal benchmark pack**
Corriu–Masse 1972、Tamura–Kochi 系、Kumada full paper との比較で追跡可能。ただし “same-metric internal benchmark” として完全に設計された論文は見つかりにくい。

**EP-02a Identity / purity substantiation pack**
full paper や Organic Syntheses procedure で部分的に充填されるが、EP が要求する entry-by-entry の NMR/IR/MS/GC 対応、isomer assignment、response factor までは論文主題になりにくい。

## 第三群：充填が見つからない可能性あり

**EP-01a Reporting-coherence pack**
communication → full paper でかなり自動解消されるが、isolated yield / GC yield の一元化、内部標準、response factor、回収補正までを主題化する独立論文は通常存在しない。Stage 3 でも reporting-coherence は yield-basis coherence の問題として位置づけられている。

**EP-08a Replication / uncertainty pack**
1970年代 organometallic synthetic communication / full paper の genre では、反復数・標準偏差・run-to-run variability が独立主題化される可能性は低い。部分的な “many examples / robust procedure” はあっても、統計的 reliability filling ではない。

# §B. 各 EP の充填論文候補

## EP-01a Reporting-coherence pack（第三群、Letter→Full auto-resolution）

**充填する RI**: RI-01 Reporting integrity
**充填開始点 / 充填確立点**:
Kohei Tamao, Koji Sumitani, Yoshihisa Kiso, Michio Zembayashi, Akira Fujioka, Shun-ichi Kodama, Isao Nakajima, Akio Minato, Makoto Kumada, [REDACTED: substantial verbatim quotation; see Tier 9] *Bull. Chem. Soc. Jpn.* 1976, 49, 1958–1969. DOI: 10.1246/bcsj.49.1958. The abstract reports roughly sixty experimental results and explicitly frames the paper as general scope and limitations.

**充填判定**: 部分充填。communication の compressed reporting は full paper 化で大きく改善されるが、modern EP-01a が求める calibrated yield-basis unification までは確認できない。
**Timescale**: field-methodology / delayed full-paper consolidation（4年）。
**Self-Tier**: Tier I.
**推論経路**: Kumada 1972 の末尾 “extension, refinement, and application” から、同一グループの full paper “General Scope and Limitations” が直接想起される。
**DB-findable?** yes.
**Bib confidence**: High.

------

## EP-02a Identity / purity substantiation pack（第二群）

**充填する RI**: RI-02 Object identification; RI-01 Reporting integrity
**充填開始点 / 充填確立点**:
同じ 1976 BCSJ full paper が第一候補。加えて Organic Syntheses の [REDACTED: substantial verbatim quotation; see Tier 9] は、specific exemplar について GC purity, spectral data, and practical workup を与えるため、selected exemplar の identity/purity substantiation を補強する。Organic Syntheses discussion は product purity 99.5% by GC and spectral confirmation を示し、β-hydride side products や catalyst/ligand effects にも触れている。([orgsyn.org](https://orgsyn.org/demo.aspx?prep=CV6P0407))

**充填判定**: 部分充填。selected exemplar では強いが、Kumada 1972 Table I 全 entry の entry-by-entry assignment ではない。
**Timescale**: field-methodology.
**Self-Tier**: Tier II.
**推論経路**: EP-02a は “product identity / purity” なので、full paper と validated preparative procedure を候補化した。
**DB-findable?** yes.
**Bib confidence**: High for OrgSyn and 1976 BCSJ; full entry-by-entry 対応は要本文確認。

------

## EP-03a Direct-observation / state-assignment pack（第一群、ただし analogical filling）

**充填する RI**: RI-03 Mechanistic non-observation; RI-06 Analogical warrant
**充填開始点**:
D. G. Morrell and J. K. Kochi, *J. Am. Chem. Soc.* 1975, 97, 7262–7270. DOI: 10.1021/ja00858a011. This paper is repeatedly cited in later Kumada/Ni-catalysis contexts as a mechanistic study relevant to nickel-catalyzed cross-coupling of aryl halides with alkylmetals.([ACS Publications](https://pubs.acs.org/doi/10.1021/jacs.6b00250?utm_source=chatgpt.com))

**充填確立点**:
G. Smith and J. K. Kochi, [REDACTED: substantial verbatim quotation; see Tier 9] *J. Organomet. Chem.* 1980. Search snippets describe isolation / decomposition behavior of arylmethylnickel(II) complexes and note their relevance to catalytic Kumada cross-coupling with aryl chlorides and bromides.([ResearchGate](https://www.researchgate.net/publication/300871938_Phosphine-Nickel_Complex_Catalyzed_Cross-Coupling_of_Grignard_Reagents_with_Aryl_and_Alkenyl_Halides_12-Dibutylbenzene?utm_source=chatgpt.com))

**充填判定**: 部分充填。Kumada 1972 の exact [NiCl2(dpe)] black-mixture system を直接観測したものではなく、organonickel elementary-step plausibility を強化する analogical / mechanistic filling。
**Timescale**: field-methodology.
**Self-Tier**: Tier III.
**推論経路**: EP-03a は “diorganonickel / halo(organo)nickel intermediate” を要求するため、Kumada group ではなく Kochi group の mechanistic organonickel literature に triangulate した。
**DB-findable?** yes.
**Bib confidence**: Medium. Morrell/Kochi の DOI と pages は確認できるが、title-level verification は追加確認推奨。

------

## EP-06a Analogy-validation pack（第一群、EP-03a と bundle）

**充填する RI**: RI-06 Analogical warrant; RI-03 Mechanistic non-observation
**充填開始点 / 充填確立点**:
EP-03a と同じ Morrell–Kochi / Smith–Kochi mechanistic organonickel literature。Kumada 1972 は “two independent facts concerning organonickel complexes” から catalytic cycle を構築しており、後続 mechanistic papers はその analogy を実験的に点検する文献群として機能する。

**充填判定**: 部分充填。analogy の妥当性は強まるが、Kumada 1972 の exact catalytic state assignment は未完全。
**Timescale**: field-methodology.
**Self-Tier**: Tier III.
**推論経路**: 原論文中の eq. 2–4 は直接観測というより literature-warranted mechanism なので、充填論文も “same reaction exact proof” ではなく “organonickel elementary-step validation” として選定した。
**DB-findable?** yes.
**Bib confidence**: Medium.

------

## EP-07a Boundary-test pack（第一群）

**充填する RI**: RI-07 Unsupported boundary
**充填開始点**:
Kohei Tamao, Yoshihisa Kiso, Koji Sumitani, Makoto Kumada, [REDACTED: substantial verbatim quotation; see Tier 9] *J. Am. Chem. Soc.* 1972, 94, 9268. DOI: 10.1021/ja00781a070. This immediate follow-up directly develops the β-hydrogen / secondary-alkyl boundary problem.([Astrophysics Data System](https://ui.adsabs.harvard.edu/abs/1972JAChS..94.9268T/abstract))

**充填確立点**:
1976 BCSJ full paper. Its abstract explicitly states wide applicability to primary and secondary alkyl, aryl, and alkenyl Grignard reagents, limitations for alkyl Grignards with dihaloethylenes, effective catalysts, organic chlorides generally most suitable, and ether favored over THF.

**補助候補**:
Yoshihisa Kiso, Kohei Tamao, Makoto Kumada, [REDACTED: substantial verbatim quotation; see Tier 9] *J. Organomet. Chem.* 1973, 50, C12. DOI: 10.1016/S0022-328X(00)95063-0. Search records state that isomerization extent depends on the nature of halides.([サイエンスダイレクト](https://www.sciencedirect.com/science/article/pii/S0022328X00950630?utm_source=chatgpt.com))

**充填判定**: 強い部分充填〜実質充填。Csp2/non-Csp2 failure matrix までは未確認だが、halide nature, β-H, solvent, catalyst, and scope boundaries は大幅に充填される。
**Timescale**: rapid self-fill + field-methodology.
**Self-Tier**: Tier I.
**推論経路**: Kumada 1972 の boundary claims から、同一グループの “scope and limitations” full paper と “alkyl isomerization / halide effects” follow-up が直接出る。
**DB-findable?** yes.
**Bib confidence**: High for 1976 BCSJ and 1972 JACS; High/Medium for 1973 JOMC depending on page verification.

------

## EP-09a Internal benchmark pack（第二群）

**充填する RI**: RI-09 External superiority; RI-07 Unsupported boundary
**充填開始点**:
R. J. P. Corriu and J. P. Masse, [REDACTED: substantial verbatim quotation; see Tier 9] *J. Chem. Soc., Chem. Commun.* 1972, 144a. DOI: 10.1039/C3972000144A. This is the concurrent communication acknowledged in Kumada 1972 and provides an immediate external comparator for nickel-activated Grignard cross-coupling.([RSC出版](https://pubs.rsc.org/en/content/articlelanding/1972/c3/c3972000144a?utm_source=chatgpt.com))

**充填確立点**:
1976 BCSJ full paper, because it consolidates scope and limitations from the Kumada group’s side.

**充填判定**: 部分充填。Corriu–Masse and Kumada full paper provide comparators, but not necessarily a deliberately matched internal benchmark against Tamura–Kochi, Corriu–Masse, and classical transition-metal halide systems.
**Timescale**: immediate external comparator + delayed self-consolidation.
**Self-Tier**: Tier II.
**推論経路**: EP-09a は “superiority / benchmark” なので、Note Added in Proof の Corriu–Masse と、later Kumada full paper を paired comparator として選ぶ。
**DB-findable?** yes.
**Bib confidence**: High.

------

## EP-04a Discrimination / replication pack（第一群）

**充填する RI**: RI-04 Unreplicated discriminator; RI-05 Qualitative overread
**充填開始点 / 充填確立点**:
Kohei Tamao, Michio Zembayashi, Yoshihisa Kiso, Makoto Kumada, [REDACTED: substantial verbatim quotation; see Tier 9] *J. Organomet. Chem.* 1973, 55, C91. DOI: 10.1016/S0022-328X(00)82058-6. Search records summarize the key finding: monohalo-olefins react stereospecifically, whereas 1,2-dihaloethylenes react nonstereospecifically to form cis-olefins stereoselectively in many cases.([サイエンスダイレクト](https://www.sciencedirect.com/science/article/pii/S0022328X00820586?utm_source=chatgpt.com))

**充填判定**: 実質充填。Kumada 1972 の cis/trans dichloroethylene anomaly を独立主題として直接扱っている。
**Timescale**: rapid self-fill.
**Self-Tier**: Tier I.
**推論経路**: EP-04a の “cis/trans anomaly” から、同一グループの 1973 stereochemistry communication が直接想起される。
**DB-findable?** yes.
**Bib confidence**: High.

------

## EP-10a Kinetic verification pack（第一群だが完全充填不明）

**充填する RI**: RI-04 Unreplicated discriminator; RI-05 Qualitative overread
**充填開始点**:
1973 stereochemistry paper above. It distinguishes stereospecific monohalo-olefin cases from nonstereospecific / cis-selective 1,2-dihaloethylene cases.([サイエンスダイレクト](https://www.sciencedirect.com/science/article/pii/S0022328X00820586?utm_source=chatgpt.com))

**補助候補**:
Michio Zembayashi, Kohei Tamao, Makoto Kumada, “Nickel-catalyzed cis-trans isomerization of 1-alkenyl Grignard reagents,” *Tetrahedron Lett.* 1975. Search records identify this as a related later paper on cis-trans isomerization of 1-alkenyl Grignard reagents.([ResearchGate](https://www.researchgate.net/publication/322279338_A_General_Nickel-Catalyzed_Kumada_Vinylation_for_the_Preparation_of_2-Substituted_13-Dienes?utm_source=chatgpt.com))

**充填判定**: 部分充填。stereochemical discrimination は進むが、EP-10a が要求する time-course, product-alone heating, quench timing を完全に満たすかは本文確認が必要。
**Timescale**: rapid self-fill + later mechanistic refinement.
**Self-Tier**: Tier II.
**推論経路**: cis-rich anomaly の発生源を “formation selectivity vs post-formation scrambling” に分けるため、stereochemistry paper と alkenyl Grignard isomerization paper を組み合わせた。
**DB-findable?** yes.
**Bib confidence**: Medium; 1975 paper の exact pages / DOI 要確認。

------

## EP-08a Replication / uncertainty pack（第三群）

**充填する RI**: RI-08 Unquantified reliability
**充填開始点 / 充填確立点**:
未同定。1976 BCSJ full paper は多数例を示すため robustness の実務的証拠にはなるが、replicate runs, variance, analytical uncertainty を主題化する論文ではない。

**充填判定**: 未充填または genre-level partial filling。
**Timescale**: non-applicable / incentive-structurally unfilled.
**Self-Tier**: Tier III.
**推論経路**: 反復・不確かさは modern reporting requirement であり、1970年代 synthetic methodology の独立主題になりにくい。
**DB-findable?** uncertain.
**Bib confidence**: Low for any claimed full filling.

# §C. 選定マップ：最小充填セット

| 優先 | 充填論文                                                     | 主に充填する EP                                | 判定                           |
| ---- | ------------------------------------------------------------ | ---------------------------------------------- | ------------------------------ |
| 1    | Tamao et al., *Bull. Chem. Soc. Jpn.* 1976, 49, 1958–1969    | EP-01a, EP-02a, EP-07a, EP-09a, EP-08a partial | 最重要 bundle filling          |
| 2    | Tamao, Kiso, Sumitani, Kumada, *JACS* 1972, 94, 9268         | EP-07a, EP-03a partial                         | β-H / secondary alkyl boundary |
| 3    | Kiso, Tamao, Kumada, *JOMC* 1973, 50, C12                    | EP-07a, EP-09a                                 | halide effect / isomerization  |
| 4    | Tamao, Zembayashi, Kiso, Kumada, *JOMC* 1973, 55, C91        | EP-04a, EP-10a partial                         | stereochemistry anomaly        |
| 5    | Corriu, Masse, *Chem. Commun.* 1972, 144a                    | EP-09a                                         | concurrent comparator          |
| 6    | Morrell, Kochi, *JACS* 1975, 97, 7262–7270 / Smith, Kochi, *JOMC* 1980 | EP-03a, EP-06a                                 | mechanistic analog filling     |

# §D. 充填タイムスケール評価

| EP     | filling timescale                            | コメント                                                     |
| ------ | -------------------------------------------- | ------------------------------------------------------------ |
| EP-07a | rapid self-fill → full consolidation         | 1972 immediate follow-up and 1976 full paperで scope boundary が急速に埋まる。 |
| EP-04a | rapid self-fill                              | 1973 stereochemistry paper が anomaly を直接主題化。         |
| EP-10a | rapid partial → later refinement             | stereochemical discrimination は早いが kinetic controls は完全確認が必要。 |
| EP-03a | field-methodology                            | exact system ではなく organonickel mechanism literature による analogical filling。 |
| EP-06a | field-methodology                            | analogy validation は mechanistic organonickel field の発展に依存。 |
| EP-09a | immediate comparator + delayed consolidation | Corriu–Masse は即時、Kumada full paper は 1976。             |
| EP-01a | Letter→Full auto-resolution, partial         | full paper が改善するが、modern calibration は未充填。       |
| EP-02a | method/procedure-level partial               | Organic Syntheses / full paper で exemplar は強化。          |
| EP-08a | likely unfilled                              | 反復・不確かさは当時の publication incentive と合わない。    |

# §E. Retrieval Depth 統合マトリクス

| 充填論文                                                  | 充填 EP                                        | Self-Tier | 推論経路                                                     | DB-findable? | Bib confidence                         |
| --------------------------------------------------------- | ---------------------------------------------- | --------- | ------------------------------------------------------------ | ------------ | -------------------------------------- |
| Tamao et al., *Bull. Chem. Soc. Jpn.* 1976, 49, 1958–1969 | EP-01a, EP-02a, EP-07a, EP-09a, EP-08a partial | I         | “extension/refinement/application” → same-group full paper “General Scope and Limitations” | yes          | High                                   |
| Tamao, Kiso, Sumitani, Kumada, *JACS* 1972, 94, 9268      | EP-07a, EP-03a partial                         | I         | β-H claim → secondary alkyl Grignard isomerization follow-up | yes          | High                                   |
| Kiso, Tamao, Kumada, *JOMC* 1973, 50, C12                 | EP-07a, EP-09a                                 | II        | halide boundary → halide nature / alkyl isomerization paper  | yes          | High/Medium                            |
| Tamao, Zembayashi, Kiso, Kumada, *JOMC* 1973, 55, C91     | EP-04a, EP-10a partial                         | I         | cis/trans anomaly → stereochemistry paper                    | yes          | High                                   |
| Corriu, Masse, *Chem. Commun.* 1972, 144a                 | EP-09a                                         | I         | Note Added in Proof / concurrent nickel-Grignard method      | yes          | High                                   |
| Morrell, Kochi, *JACS* 1975, 97, 7262–7270                | EP-03a, EP-06a                                 | III       | diorganonickel mechanism → Kochi organonickel mechanistic literature | yes          | Medium; title verification recommended |
| Smith, Kochi, *JOMC* 1980                                 | EP-03a, EP-06a                                 | III       | reductive elimination / arylmethylnickel species → elementary-step validation | yes          | Medium                                 |
| Organic Syntheses 1,2-dibutylbenzene procedure            | EP-02a, EP-07a partial                         | II        | product identity/purity and practical reproducibility → checked preparative procedure | yes          | High                                   |

# §F. 棄却候補記録

| 棄却候補                                                     | 棄却理由                                                     |
| ------------------------------------------------------------ | ------------------------------------------------------------ |
| General reviews on Kumada–Corriu coupling                    | レビューは EP を直接充填しない。候補同定の補助には有用だが、新しい experimental evidence ではない。 |
| Negishi / Suzuki / Stille high-citation cross-coupling papers | Kumada 1972 の方法を歴史的に継承するが、EP-03a/07a/09a の case-specific 実験を直接充填するものではない。 |
| Modern computational Ni-catalyzed Kumada papers              | β-H elimination や C–X activation を現代的に解析するが、1972 [Ni-phosphine]/Grignard/Csp2-halide system の immediate filling paper ではない。補助的背景に留める。 |
| Tamura–Kochi 1971 papers                                     | 原論文以前の比較対象であり、post-1972 EP filling ではない。ただし EP-09a の benchmark backdrop としては重要。 |
| Corriu–Masse 1972 as sole filling paper                      | concurrent comparator として重要だが、Kumada paper の internal omissions を単独で充填するものではない。 |
| Organic Syntheses procedure as full EP-01a/08a filling       | practical reproducibility は強いが、full Table I の calibrated reporting / statistical replication ではない。 |

# §G. 最終判定

Kumada 1972 の EP 充填は、**同一グループによる rapid self-fill** と **1976 full paper consolidation** が中核である。特に EP-07a と EP-04a は後続論文でかなり明確に充填される。一方、EP-03a / EP-06a は Kochi 系を含む organonickel mechanism literature による **analogical filling** に留まり、exact catalytic mixture の direct state assignment までは弱い。EP-01a / EP-08a は現代的 reporting standard から見ると未充填が残る。これはデータが存在しないというより、1970年代 communication / methodology paper の incentive structure が、calibration・replication・uncertainty を独立成果として出す方向に働いていなかったためと見るのが妥当である。

---

> **Tier 8 redaction notice**: This file is a redacted copy of the corresponding Tier 3 / Tier 9 output. Verbatim source-paper quotations have been replaced by `[REDACTED: see source paper §<loc>; full text retained in Tier 9 reviewer-only deposit]` markers, preserving location references and our own analytical content. Bibliographic fields (title, authors, journal, year, DOI), analytical labels (`evidence_chain:` with B-/U-/A-/C- internal IDs), short technical terms, and our own analytical text are not redacted. The redaction was applied by `scripts/redact_for_tier8.py` and, for this version, by `scripts/build_paperA_R1_public.py` with `scripts/redact_source_ngram_runs.py` (scripts of the project repository; they are not deposited).
