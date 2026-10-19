```text
prompt_version: stage4-v2
model_info: gpt-5.4-thinking
experimental_variant: retrieval-depth-annotation (Cross-vendor multi-run, GPT-5.4 v2)
related_pilot_sonnet: papers/dev/kumada/kumada_v17_sonnet_s4v2_retrieval_depth.md (Sonnet Pilot 2)
related_baseline_gpt: papers/dev/kumada/gpt54thinking/kumada_v17_gpt54thinking_s4.md (April 19 baseline, no annotation)
note: Multi-run robustness の cross-vendor extension。Sonnet v2 multi-run 3 runs と
      比較して GPT-5.4 の retrieval pattern と Tier annotation の安定性を測定する。
date: 2026-05-08
stage4_prompt_version: stage4-v2-20260416
```

## §A. EP充填難易度の三群分類

Stage 4 の目的は、Stage 3 §5 の EP を、後続文献がどの程度「充填」したかで選定マップ化することである。今回の追加条件として、各候補に retrieval Tier、推論経路、DB-findability、bibliographic confidence を付す必要がある。

### 第一群：文献で明確に追跡可能

| EP                                                    | 判定   | 理由                                                         |
| ----------------------------------------------------- | ------ | ------------------------------------------------------------ |
| **EP-07a Boundary-test pack**                         | 第一群 | 1976 年の同一グループ full paper が “General Scope and Limitations” を明示し、約 60 例、chloride 適性、ether/THF、基質範囲を扱う。 |
| **EP-04a Discrimination / replication pack**          | 第一群 | cis/trans olefinic halide の stereospecific vs nonstereospecific-stereoselective 問題は 1973 年 JOMC paper として独立主題化されている。([ResearchGate](https://www.researchgate.net/publication/300871938_Phosphine-Nickel_Complex_Catalyzed_Cross-Coupling_of_Grignard_Reagents_with_Aryl_and_Alkenyl_Halides_12-Dibutylbenzene)) |
| **EP-10a Kinetic / stereochemical verification pack** | 第一群 | stilbene cis enrichment、olefinic halide stereochemistry、secondary alkyl isomerization が 1972–1973 年の follow-up 群で直接扱われる。([OUCI](https://ouci.dntb.gov.ua/en/works/7PAgWVe4/?utm_source=chatgpt.com)) |
| **EP-09a Internal benchmark pack**                    | 第一群 | 1976 BCSJ full paper と Org. Synth. checked procedure が、1972 communication の短報的主張を fuller method/procedure として再提示している。 ([オーガニックシンセシス](https://orgsyn.org/demo.aspx?prep=CV6P0407)) |

### 第二群：間接的に追跡可能

| EP                                               | 判定   | 理由                                                         |
| ------------------------------------------------ | ------ | ------------------------------------------------------------ |
| **EP-01a Reporting-coherence pack**              | 第二群 | 1976 full paper と 1978 Org. Synth. により相当程度補強されるが、1972 Table I の GLPC internal standard、response factor、entry-by-entry uncertainty を完全に後追い充填した論文とは限らない。 |
| **EP-02a Identity / purity substantiation pack** | 第二群 | Org. Synth. の checked procedure と full paper が補強するが、1972 全 entry の raw spectral assignment を完全復元するものではない。([オーガニックシンセシス](https://orgsyn.org/demo.aspx?prep=CV6P0407)) |
| **EP-08a Replication / uncertainty pack**        | 第二群 | Org. Synth. は independent check として有力だが、現代的な replicate statistics / uncertainty table そのものではない。([オーガニックシンセシス](https://orgsyn.org/demo.aspx?prep=CV6P0407)) |

### 第三群：充填が見つからない可能性あり

| EP / 下位要求                                             | 判定   | 理由                                                         |
| --------------------------------------------------------- | ------ | ------------------------------------------------------------ |
| **EP-03a のうち black-mixture catalyst-state assignment** | 第三群 | Ni-phosphine cross-coupling では R–R 定量と black-mixture catalyst-state assignment を一体で要求する、という case-specific 要求は Stage 3 で明確化されているが、1972 の [NiCl₂(dpe)] 条件そのものの black mixture を後続で完全解析した論文は直ちには同定しにくい。 |
| **EP-01a / EP-08a の raw calibration level**              | 第三群 | 1972 Table I の内部標準・response factor・反復誤差を retrospective に完全補完する独立論文は、通常の文献単位では存在しにくい。 |

------

## §B. 推奨充填論文候補

### F1. Tamao et al., 1976, BCSJ — general scope and limitations

**Candidate paper**
Kohei Tamao, Koji Sumitani, Yoshihisa Kiso, Michio Zembayashi, Akira Fujioka, Shun-ichi Kodama, Isao Nakajima, Akio Minato, Makoto Kumada, [REDACTED: substantial verbatim quotation; see Tier 9] *Bulletin of the Chemical Society of Japan* 49, 1958–1969 (1976). DOI: 10.1246/bcsj.49.1958.

**充填 EP**
EP-01a, EP-02a, EP-07a, EP-08a partial, EP-09a, EP-10a partial.

**対応する 1972 欠落**
1972 paper は Table I を “not necessarily optimum” とし、代表例・GLPC/internal-standard/isolated yield を混在させ、scope boundary と solvent superiority を短報内で提示した。 後続の 1976 paper は “General Scope and Limitations” として、約 60 例、β-H を持つ alkyl Grignard、aryl/alkenyl Grignard、aryl/alkenyl halide、chloride 適性、ether vs THF、phosphine ligand の安定化を扱うため、VQ-2 への最重要充填論文である。

**VQ impact**
VQ-2 Method への最短コア。VQ-3 Mechanism には部分寄与に留まる。

**Retrieval annotation**
Self-Tier: **Tier I**
推論経路: EP-07a / EP-01a → “extension, refinement, and application” → same-group full paper → “General Scope and Limitations.”
DB-findable: **yes**
Bib confidence: **High**。ただし、EP-01a/08a の raw calibration 完全性は full text table 確認推奨。

------

### F2. Tamao, Zembayashi, Kiso, Kumada, 1973, JOMC — stereochemistry of olefinic halides

**Candidate paper**
Kohei Tamao, Michio Zembayashi, Yoshihisa Kiso, Makoto Kumada, [REDACTED: substantial verbatim quotation; see Tier 9] *Journal of Organometallic Chemistry* 55, C91 (1973). ([ResearchGate](https://www.researchgate.net/publication/300871938_Phosphine-Nickel_Complex_Catalyzed_Cross-Coupling_of_Grignard_Reagents_with_Aryl_and_Alkenyl_Halides_12-Dibutylbenzene))

**充填 EP**
EP-04a, EP-10a.

**対応する 1972 欠落**
1972 paper は cis- and trans-1,2-dichloroethylene から cis/trans-stilbene mixture が “anomalously enriched with the cis isomer” と述べるが、生成段階と後異性化を分離していない。 この 1973 paper は monohalo-olefins と 1,2-dihaloethylenes の stereospecific / nonstereospecific-stereoselective behavior を主題化しており、SRG-4 の中心的充填候補である。([ResearchGate](https://www.researchgate.net/publication/300871938_Phosphine-Nickel_Complex_Catalyzed_Cross-Coupling_of_Grignard_Reagents_with_Aryl_and_Alkenyl_Halides_12-Dibutylbenzene))

**VQ impact**
VQ-3 stereochemical interpretation への主要充填。ただし catalyst-state の direct observation ではない。

**Retrieval annotation**
Self-Tier: **Tier I**
推論経路: EP-04a → cis/trans stilbene anomaly → stereochemistry follow-up → Tamao/Kumada 1973 JOMC.
DB-findable: **yes**
Bib confidence: **High**。巻・ページ詳細は JOMC 本文確認推奨。

------

### F3. Tamao, Kiso, Sumitani, Kumada, 1972, JACS — alkyl group isomerization

**Candidate paper**
Kohei Tamao, Yoshihisa Kiso, Koji Sumitani, Makoto Kumada, [REDACTED: substantial verbatim quotation; see Tier 9] *Journal of the American Chemical Society* 94, 9268–9269 (1972). DOI: 10.1021/ja00781a070. ([OUCI](https://ouci.dntb.gov.ua/en/works/7PAgWVe4/?utm_source=chatgpt.com))

**充填 EP**
EP-03a partial, EP-10a, EP-07a partial.

**対応する 1972 欠落**
1972 paper は β-H を持つ alkylmagnesium reagents でも高収率と主張するが、β-hydride elimination / alkyl isomerization / side-product distribution を示していない。 この JACS follow-up は secondary alkyl Grignard における alkyl group isomerization を直接主題化するため、β-H 問題の最初期充填候補である。

**VQ impact**
VQ-3 の side-path / isomerization 部分に寄与。1972 の general method claim を無条件に強めるというより、むしろ β-H substrate claim の boundary を明確化する。

**Retrieval annotation**
Self-Tier: **Tier II**
推論経路: EP-03a → β-H-containing alkyl Grignard → alkyl isomerization → same-group 1972 JACS follow-up.
DB-findable: **yes**
Bib confidence: **High**。

------

### F4. Kiso, Tamao, Kumada, 1973, JOMC — halide effects on alkyl isomerization

**Candidate paper**
Yoshihisa Kiso, Kohei Tamao, Makoto Kumada, [REDACTED: substantial verbatim quotation; see Tier 9] *Journal of Organometallic Chemistry* 50, C12 (1973). ([ResearchGate](https://www.researchgate.net/publication/300871938_Phosphine-Nickel_Complex_Catalyzed_Cross-Coupling_of_Grignard_Reagents_with_Aryl_and_Alkenyl_Halides_12-Dibutylbenzene))

**充填 EP**
EP-03a partial, EP-07a, EP-10a.

**対応する 1972 欠落**
Stage 3 は EP-07a として chloride/bromide/iodide、Csp2/non-Csp2、ether/THF などの matched matrix を要求している。 この paper は “nature of halides” と secondary alkyl isomerization を接続するため、halide-dependent boundary と side-path の両方を補強する。

**VQ impact**
VQ-2 boundary と VQ-3 side-path の橋渡し。1972 の “chlorides remarkable” claim を単純支持するのではなく、halide identity が反応経路に影響することを明示する方向の充填。

**Retrieval annotation**
Self-Tier: **Tier II**
推論経路: EP-07a → halide identity → secondary alkyl isomerization → Kiso/Tamao/Kumada 1973.
DB-findable: **yes**
Bib confidence: **Medium–High**。JOMC full text で scope table 確認推奨。

------

### F5. Morrell and Kochi, 1975, JACS — arylalkylnickel(II) intermediates

**Candidate paper**
Dennis G. Morrell, Jay K. Kochi, [REDACTED: substantial verbatim quotation; see Tier 9] *Journal of the American Chemical Society* 97, 7262–7270 (1975). DOI: 10.1021/ja00858a011. ([Mindat](https://www.mindat.org/reference.php?id=1294618&utm_source=chatgpt.com))

**充填 EP**
EP-03a, EP-10a.

**対応する 1972 欠落**
1972 paper は L₂NiR₂、L₂Ni(R′)(X″)、L₂NiRR′ 型の intermediates を含む catalytic cycle を提示するが、intermediate / byproduct を直接観測していない。 Morrell–Kochi は arylalkylnickel(II) species の intermediate role を主題化しており、同一 substrate class ではない部分を含むとしても、RI-03 の mechanistic filling として強い。

**VQ impact**
VQ-3 Mechanism への強い外部充填。Kumada original system の完全再現ではなく、mechanistic analogue として扱うべき。

**Retrieval annotation**
Self-Tier: **Tier II**
推論経路: EP-03a → proposed organonickel intermediates → arylalkylnickel(II) mechanistic literature → Morrell–Kochi.
DB-findable: **yes**
Bib confidence: **High**。

------

### F6. Tsou and Kochi, 1979, JACS — oxidative addition of aryl halides to Ni(0)

**Candidate paper**
T. T. Tsou, Jay K. Kochi, [REDACTED: substantial verbatim quotation; see Tier 9] *Journal of the American Chemical Society* 101, 7547–7560 (1979). DOI: 10.1021/ja00515a028. ([ADS](https://ui.adsabs.harvard.edu/abs/1979JAChS.101.6319T/abstract?utm_source=chatgpt.com))

**充填 EP**
EP-03a, EP-07a, EP-09a.

**対応する 1972 欠落**
1972 paper は sp² C–Cl bond の反応性と oxidative addition literature に依拠しつつ、chloride advantage の step-specific basis を自前で示していない。 Tsou–Kochi は Ni(0) complexes と aromatic halides の oxidative addition mechanism を直接扱うため、chloride/bromide/iodide boundary claim の mechanistic 補助線になる。

**VQ impact**
VQ-3 への補助。Kumada reaction の complete catalytic cycle ではなく、oxidative addition step の外部 mechanistic standard。

**Retrieval annotation**
Self-Tier: **Tier II–III**
推論経路: EP-07a → chloride reactivity claim → oxidative addition step → Ni(0)/aryl halide mechanism → Tsou–Kochi.
DB-findable: **yes**
Bib confidence: **High**。

------

### F7. Kumada/Tamao/Sumitani, 1978, Organic Syntheses — checked procedure

**Candidate paper / procedure**
Makoto Kumada, Kohei Tamao, Koji Sumitani, [REDACTED: substantial verbatim quotation; see Tier 9] *Organic Syntheses* 58, 127 (1978). DOI: 10.15227/orgsyn.058.0127. ([オーガニックシンセシス](https://orgsyn.org/demo.aspx?prep=CV6P0407))

**充填 EP**
EP-01a, EP-02a, EP-08a partial, EP-09a partial.

**対応する 1972 欠落**
1972 communication は representative procedures を示すが、reproducibility / independent verification はない。 Org. Synth. procedure は independent checker を伴う実験手順として、method reproducibility の外部確認に近い位置を占める。([オーガニックシンセシス](https://orgsyn.org/demo.aspx?prep=CV6P0407))

**VQ impact**
VQ-2 Method の procedural robustness を補強。現代的な uncertainty statistics ではないが、EP-08a の practical substitute として重要。

**Retrieval annotation**
Self-Tier: **Tier I–II**
推論経路: EP-01a/08a → reproducible preparative method → Organic Syntheses checked procedure.
DB-findable: **yes**
Bib confidence: **High**。

------

### F8. Corriu and Masse, 1972, Chem. Commun. — concurrent benchmark

**Candidate paper**
R. J. P. Corriu, J. P. Masse, [REDACTED: substantial verbatim quotation; see Tier 9] *Journal of the Chemical Society, Chemical Communications* 1972, 144. ([TCIchemicals.com](https://www.tcichemicals.com/OP/en/product/tci-topics/ProductHighlights_20211220?utm_source=chatgpt.com))

**充填 EP**
EP-09a partial; GAP-2 comparator.

**対応する 1972 欠落**
1972 Kumada paper itself notes after submission that a similar nickel-catalyzed cross-coupling communication by Corriu and Masse appeared. これは後続充填というより、novelty / external benchmark の軸を補う同時代 comparator である。

**VQ impact**
VQ-2 の external benchmark map には有用。ただし Kumada paper の mechanistic / reporting gaps を直接埋めるものではない。

**Retrieval annotation**
Self-Tier: **Tier I**
推論経路: Note Added in Proof → concurrent nickel-catalyzed Grignard cross-coupling → Corriu–Masse 1972.
DB-findable: **yes**
Bib confidence: **High**。

------

## §C. EP → 充填論文マップ

| EP                                                    | Primary filler | Secondary filler | 充填度 | 残る不足                                                     |
| ----------------------------------------------------- | -------------- | ---------------- | ------ | ------------------------------------------------------------ |
| **EP-01a Reporting-coherence pack**                   | F1             | F7               | 中〜高 | 1972 Table I の raw GLPC calibration / response factor は未確認。 |
| **EP-02a Identity / purity substantiation pack**      | F1             | F7               | 中     | 全 1972 entry の entry-by-entry spectral assignment までは保証しない。 |
| **EP-03a Mechanistic intermediate / byproduct pack**  | F5             | F3, F4, F6       | 中     | Original [NiCl₂(dpe)] black mixture の catalyst-state assignment は未充填に近い。 |
| **EP-04a Discrimination / replication pack**          | F2             | F3, F4           | 高     | Time-course / product-alone heating controls の具体的有無は full text 確認が必要。 |
| **EP-07a Boundary-test pack**                         | F1             | F4, F6           | 高     | Csp2/non-Csp2 の完全 matched failure matrix までは要確認。   |
| **EP-08a Replication / uncertainty pack**             | F7             | F1               | 中     | Independent check はあるが、modern replicate statistics ではない。 |
| **EP-09a Internal benchmark pack**                    | F1             | F8, F7           | 中〜高 | Tamura–Kochi との同一条件直接比較は限定的。                  |
| **EP-10a Kinetic / stereochemical verification pack** | F2             | F3, F4, F5       | 中〜高 | Full kinetic time-course の程度は個別論文確認が必要。        |

------

## §D. VQ昇格に対する最短選定セット

### VQ-2 Method への最短セット

**必須セット:** F1 + F7

- **F1** は 1972 communication の “extension, refinement, and application” を最も直接に受ける full paper であり、scope / limitation / solvent / halide / ligand の整理を与える。
- **F7** は checked procedure として、少なくとも exemplar-level reproducibility を補強する。([オーガニックシンセシス](https://orgsyn.org/demo.aspx?prep=CV6P0407))

**判定:** VQ-2 はかなり前進。ただし modern reaccreditation としては、raw calibration、反復誤差、failure matrix の完全性を full text で再確認する必要がある。

### VQ-3 Mechanism / stereochemistry への最短セット

**必須セット:** F2 + F3/F4 + F5 + F6

- **F2** は 1972 の cis-enriched stilbene anomaly を stereochemistry 問題として後続充填する。([ResearchGate](https://www.researchgate.net/publication/300871938_Phosphine-Nickel_Complex_Catalyzed_Cross-Coupling_of_Grignard_Reagents_with_Aryl_and_Alkenyl_Halides_12-Dibutylbenzene))
- **F3/F4** は β-H-containing / secondary alkyl Grignard の isomerization と halide effect を補う。([OUCI](https://ouci.dntb.gov.ua/en/works/7PAgWVe4/?utm_source=chatgpt.com)) ([ResearchGate](https://www.researchgate.net/publication/300871938_Phosphine-Nickel_Complex_Catalyzed_Cross-Coupling_of_Grignard_Reagents_with_Aryl_and_Alkenyl_Halides_12-Dibutylbenzene))
- **F5** は arylalkylnickel(II) intermediate の mechanistic role を扱い、1972 catalytic cycle の外部充填になる。([Mindat](https://www.mindat.org/reference.php?id=1294618&utm_source=chatgpt.com))
- **F6** は oxidative addition step の mechanistic underpinning を補う。([ADS](https://ui.adsabs.harvard.edu/abs/1979JAChS.101.6319T/abstract?utm_source=chatgpt.com))

**判定:** VQ-3 は部分的に成立可能。ただし “1972 original catalyst under original conditions” の完全機構確定ではなく、後続文献を束ねた mechanistic reaccreditation である。

### VQ-4 Benchmark-grade への到達可能性

**判定:** 未達。
理由は、EP-01a/08a の modern statistical reliability、EP-03a の original black-mixture catalyst-state assignment、EP-07a の full matched failure matrix が、現時点の候補セットだけでは完全に満たされないためである。Stage 3 も、現代基準では reporting / boundary / mechanism の複数欠落を deficiency として整理している。

------

## §E. Retrieval Depth Annotation 統合マトリクス

| 充填論文                                                    | 充填 EP                                                      | Self-Tier | 推論経路                                                     | DB-findable? | Bib confidence                  |
| ----------------------------------------------------------- | ------------------------------------------------------------ | --------- | ------------------------------------------------------------ | ------------ | ------------------------------- |
| Tamao et al., BCSJ 1976, “General Scope and Limitations”    | EP-01a, EP-02a, EP-07a, EP-08a partial, EP-09a, EP-10a partial | I         | EP-07a/01a → extension/refinement → same-group full paper    | yes          | High; full text table 確認推奨  |
| Tamao/Zembayashi/Kiso/Kumada, JOMC 1973, stereochemistry    | EP-04a, EP-10a                                               | I         | cis/trans stilbene anomaly → stereochemistry follow-up       | yes          | High; page/table 確認推奨       |
| Tamao/Kiso/Sumitani/Kumada, JACS 1972, alkyl isomerization  | EP-03a partial, EP-10a, EP-07a partial                       | II        | β-H claim → secondary alkyl Grignard → isomerization         | yes          | High                            |
| Kiso/Tamao/Kumada, JOMC 1973, halide effects                | EP-03a partial, EP-07a, EP-10a                               | II        | halide boundary → alkyl isomerization → halide effect paper  | yes          | Medium–High; full text 確認推奨 |
| Morrell/Kochi, JACS 1975, arylalkylnickel(II) intermediates | EP-03a, EP-10a                                               | II        | catalytic cycle → organonickel intermediates → mechanistic JACS | yes          | High                            |
| Tsou/Kochi, JACS 1979, oxidative addition                   | EP-03a, EP-07a, EP-09a                                       | II–III    | chloride reactivity → oxidative addition → Ni(0)/aryl halide mechanism | yes          | High                            |
| Kumada/Tamao/Sumitani, Org. Synth. 1978                     | EP-01a, EP-02a, EP-08a partial, EP-09a partial               | I–II      | reporting/reproducibility → checked preparative procedure    | yes          | High                            |
| Corriu/Masse, Chem. Commun. 1972                            | EP-09a partial; GAP-2 comparator                             | I         | Note Added in Proof → concurrent nickel Grignard coupling    | yes          | High                            |

------

## 付録. 棄却候補ログ

| 一瞬考慮した候補                                             | 棄却の判定キー                 | 棄却理由                                                     |
| ------------------------------------------------------------ | ------------------------------ | ------------------------------------------------------------ |
| Tamura & Kochi, JACS 1971 / Synthesis 1971                   | Prior-art comparator           | 1972 Kumada paper の比較背景として重要だが、Kumada の EP を後続充填した論文ではない。GAP-1 用。 |
| Corriu & Masse, Chem. Commun. 1972                           | Concurrent, not follow-up      | Novelty benchmark として残すが、primary filler ではない。    |
| Kiso et al., Tetrahedron Lett. 1974, asymmetric cross-coupling | Scope extension                | Chiral/asymmetric extension として有用だが、1972 の reporting / boundary / cis-stilbene anomaly の主充填ではない。([ResearchGate](https://www.researchgate.net/publication/300871938_Phosphine-Nickel_Complex_Catalyzed_Cross-Coupling_of_Grignard_Reagents_with_Aryl_and_Alkenyl_Halides_12-Dibutylbenzene)) |
| Hayashi/Tajika/Tamao/Kumada, 1976, asymmetric high stereoselectivity | Later asymmetric application   | EP-04a の一般 stereochemistry ではなく asymmetric catalyst development 寄り。([ResearchGate](https://www.researchgate.net/publication/300871938_Phosphine-Nickel_Complex_Catalyzed_Cross-Coupling_of_Grignard_Reagents_with_Aryl_and_Alkenyl_Halides_12-Dibutylbenzene)) |
| Tamao/Minato/Miyake/Kumada, 1975, hindered biaryls / atropisomers | Application paper              | “extension/application” には該当するが、VQ-2/3 の最短補強にはならない。([ResearchGate](https://www.researchgate.net/publication/300871938_Phosphine-Nickel_Complex_Catalyzed_Cross-Coupling_of_Grignard_Reagents_with_Aryl_and_Alkenyl_Halides_12-Dibutylbenzene)) |
| Tamao/Kodama/Nakatsuka/Kiso/Kumada, 1975, metacyclophanes    | Application paper              | dihalide/di-Grignard cyclocoupling の応用であり、1972 core gaps の primary filler ではない。([ResearchGate](https://www.researchgate.net/publication/300871938_Phosphine-Nickel_Complex_Catalyzed_Cross-Coupling_of_Grignard_Reagents_with_Aryl_and_Alkenyl_Halides_12-Dibutylbenzene)) |
| Tamao et al., 1982, heterocyclic compounds                   | Later scope extension          | Heterocycle scope には有用だが、1972 の first-order EP 充填としては優先度が低い。 |
| Modern Ni-catalyzed Kumada DFT papers                        | Mechanistic analogue           | 現代的機構理解には有用だが、1972 Ni-phosphine / aryl-vinyl chloride system の歴史的充填論文としては距離がある。 |
| Negishi / Suzuki cross-coupling foundational papers          | Different organometallic class | Cross-coupling field の発展史には重要だが、Grignard–Ni-phosphine EP 充填ではない。 |

---

> **Tier 8 redaction notice**: This file is a redacted copy of the corresponding Tier 3 / Tier 9 output. Verbatim source-paper quotations have been replaced by `[REDACTED: see source paper §<loc>; full text retained in Tier 9 reviewer-only deposit]` markers, preserving location references and our own analytical content. Bibliographic fields (title, authors, journal, year, DOI), analytical labels (`evidence_chain:` with B-/U-/A-/C- internal IDs), short technical terms, and our own analytical text are not redacted. The redaction was applied by `scripts/redact_for_tier8.py` and, for this version, by `scripts/build_paperA_R1_public.py` with `scripts/redact_source_ngram_runs.py` (scripts of the project repository; they are not deposited).
