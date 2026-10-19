```text
prompt_version: stage4-v2
model_info: gpt-5.4-thinking
experimental_variant: retrieval-depth-annotation (Cross-vendor multi-run, GPT-5.4 v2)
related_pilot_sonnet: papers/dev/kumada/kumada_v17_sonnet_s4v2_retrieval_depth.md (Sonnet Pilot 2)
related_baseline_gpt: papers/dev/kumada/gpt54thinking/kumada_v17_gpt54thinking_s4.md (April 19 baseline, no annotation)
note: Multi-run robustness の cross-vendor extension。Sonnet v2 multi-run 3 runs と
      比較して GPT-5.4 の retrieval pattern と Tier annotation の安定性を測定する。
date: 2026-05-08
```

source_basis: Stage 4 v2 の出力形式と retrieval-depth annotation 要求は添付 markdown に従った。対象論文側では、Table I、GLPC/isolated yield の混在、提案 catalytic cycle、scope/ligand/stereochemistry/solvent claim、および future-work 文を基礎情報として用いた。

# EP充填選定マップ

## Tamao–Sumitani–Kumada 1972（JACS communication）

### §A EP充填難易度の三群分類

**第一群（文献で明確に追跡可能）：** EP-03a, EP-04a, EP-06a, EP-07a, EP-10a
— **EP-03a Direct-observation / state-assignment pack**: organonickel intermediate、oxidative addition、Ni speciation は独立した機構論文の主題になり得る。
— **EP-04a Discrimination / replication pack**: cis/trans-1,2-dichloroethylene coupling の stereochemical anomaly は、後続の stereochemistry 論文として直接追跡可能。
— **EP-06a Mechanistic causal-linkage pack**: ligand order / cis-diorganonickel interpretation / elementary-step assignment は、Kochi 系の organonickel mechanistic studies と接続可能。
— **EP-07a Boundary-test pack**: chloride/bromide/iodide, Csp² halide scope, β-H-containing Grignards, solvent effect は Full Paper の “scope and limitations” で直接追跡可能。
— **EP-10a Kinetic / stereochemical verification pack**: stereospecific versus nonstereospecific coupling、post-formation scrambling の切り分けは部分的に独立論文化されている。

**第二群（間接的に追跡可能）：** EP-02a, EP-05a, EP-09a
— **EP-02a Identity / purity substantiation pack**: product identity / purity は独立論文の主題というより、Full Paper や Organic Syntheses procedure 内で補強される性質が強い。
— **EP-05a Qualitative-overread calibration pack**: “anomalously cis-enriched” の質的過読は、stereochemistry follow-up と総合的解釈で補正されるが、単独 EP としては現れにくい。
— **EP-09a Internal benchmark pack**: ether/THF、chloride/bromide/iodide、Corriu–Masse/Tamura–Kochi との比較は Full Paper・手順論文・歴史的総説に分散する。

**第三群（充填が見つからない可能性あり）：** EP-01a, EP-08a
— **EP-01a Reporting-coherence pack**: yield basis、GLPC calibration、entry-by-entry analytical mapping は communication→Full Paper で改善され得るが、通常は独立した科学論文の主題ではない。
— **EP-08a Replication / uncertainty pack**: checked procedure による部分的再現性は得られるが、全 Table I の反復・不確かさ評価として体系的に充填される可能性は低い。

------

### §B 各EPの充填論文候補

#### **EP-01a Reporting-coherence pack（第三群）**

**充填開始点 / 確立点**

- **Tamao et al. 1976, Bull. Chem. Soc. Jpn.**: “General Scope and Limitations” として約 60 例を扱い、1972 communication の代表例を method-level に拡張する自己充填 Full Paper と位置づけられる。Abstract は、primary/secondary alkyl, aryl, alkenyl Grignard reagents、各種 halides、chlorides の適性、ether/THF 差、catalyst aging effect まで含む。
- **Kumada–Tamao–Sumitani 1978, Organic Syntheses**: 1,2-dibutylbenzene の checked preparation として、apparatus, drying, addition order, workup, forerun byproduct, isolated yield range を明示し、communication の report-coherence gap を部分的に補う。([orgsyn.org](https://orgsyn.org/demo.aspx?prep=CV6P0407))

**充填判定**
部分充填。Full Paper と checked procedure により method-level の記述は大きく改善するが、1972 Table I 全体の GLPC response factor・internal standard・entry-by-entry uncertainty までは完全には埋まらない。

**Retrieval annotation**

- Self-Tier: **Tier I**
- 推論経路: communication の “not necessarily optimum” + representative Table → expected Full Paper → Tamao/Kumada 1976 BCSJ.
- DB-findable?: **yes**
- Bib confidence: **High**。BCSJ 1976 と Org. Synth. 1978 は書誌的に確認可能。

------

#### **EP-02a Identity / purity substantiation pack（第二群）**

**充填開始点 / 確立点**

- **Tamao et al. 1976, BCSJ** が広範な substrate/product scope を提供し、product identity を communication より詳細化する起点。
- **Organic Syntheses 1978** は少なくとも 1,2-dibutylbenzene について、distillation fraction, forerun, checked yield を明示するため、selected exemplar の purity substantiation として強い。([orgsyn.org](https://orgsyn.org/demo.aspx?prep=CV6P0407))

**充填判定**
部分充填。代表的 preparative example ではかなり補われるが、1972 Table I の全 entry について NMR/IR/MS/GC の対応表を与えるものではない。

**Retrieval annotation**

- Self-Tier: **Tier II**
- 推論経路: “glpc, nmr, ir, and/or mass spectra” の未対応 → detailed procedure / checked synthesis → Organic Syntheses.
- DB-findable?: **uncertain**
- Bib confidence: **High for selected exemplar / Medium for full-table filling**。

------

#### **EP-03a Direct-observation / state-assignment pack（第一群）**

**充填開始点 / 確立点**

- **Morell & Kochi 1975, JACS**: aryl halides と alkylmetals の nickel-catalyzed cross-coupling において、arylalkylnickel(II) species を intermediate として扱う機構研究。Kumada 1972 の L₂NiR₂ / L₂Ni(R′)(X) 型 working hypothesis に対し、外部グループによる mechanistic filling として重要。([ACS Publications](https://pubs.acs.org/doi/10.1021/ja00858a011?utm_source=chatgpt.com))
- **Tsou & Kochi 1979, JACS**: Ni(0) complex と aryl halide の oxidative addition を IR/EPR などで追跡し、halide, substituent, solvent, ligand による Ni species 分布を扱う。これは 1972 論文の “chloride reactivity” と “low-valent nickel oxidative addition” の機構的裏づけに相当する。([ACS Publications](https://pubs.acs.org/doi/10.1021/ja00515a028?utm_source=chatgpt.com))

**充填判定**
中核機構については強い部分充填。ただし、1972 Example 1 の “black mixture / much salt” そのものについて、可溶/不溶 Ni mass balance、solid-state assignment、filtration/re-addition test を行ったわけではないため、case-specific state-assignment としては未充填が残る。

**Retrieval annotation**

- Self-Tier: **Tier III**
- 推論経路: black mixture + proposed homogeneous cycle → Ni speciation / arylalkylnickel intermediates → Kochi mechanistic papers.
- DB-findable?: **yes**
- Bib confidence: **High for mechanistic relevance / Medium for exact case-specific filling**。

------

#### **EP-04a Discrimination / replication pack（第一群）**

**充填開始点 / 確立点**

- **Tamao, Zembayashi, Kiso & Kumada 1973, J. Organomet. Chem.**: [REDACTED: substantial verbatim quotation; see Tier 9]。検索結果および Organic Syntheses の引用リストから、monohalo-olefins は stereospecific、1,2-dihaloethylenes は nonstereospecific だが cis-olefins を stereoselectively に与える、という 1972 年の stereochemical anomaly を直接扱う論文と確認できる。([サイエンスダイレクト](https://www.sciencedirect.com/science/article/pii/S0022328X00820586?utm_source=chatgpt.com))

**充填判定**
強い充填。1972 communication の “rather nonstereospecifically” かつ “anomalously enriched with cis isomer” という単発観測を、反応類型として再記述する。

**Retrieval annotation**

- Self-Tier: **Tier I**
- 推論経路: cis/trans-dichloroethylene anomaly → stereochemistry of nickel-catalyzed coupling → Tamao/Zembayashi/Kiso/Kumada 1973.
- DB-findable?: **yes**
- Bib confidence: **High**。ただし本文確認には JOMC 原文照合を推奨。

------

#### **EP-05a Qualitative-overread calibration pack（第二群）**

**充填開始点 / 確立点**

- **Tamao et al. 1973 JOMC stereochemistry paper** が、単発の “cis enrichment” を一般的な stereospecific / nonstereospecific-stereoselective 分類へ変換するため、qualitative-overread の補正として機能する。([サイエンスダイレクト](https://www.sciencedirect.com/science/article/pii/S0022328X00820586?utm_source=chatgpt.com))
- **Organic Syntheses 1978 comments** も、monohaloalkenes は stereospecific、1,2-dihaloethylenes は nonstereospecific で Z-alkene を与える、という簡潔な再整理を与える。([orgsyn.org](https://orgsyn.org/demo.aspx?prep=CV6P0407))

**充填判定**
部分充填。1972 年の qualitative claim は整理されるが、effect-size calibration、time-course、thermal isomerization exclusion まで完全に満たすわけではない。

**Retrieval annotation**

- Self-Tier: **Tier II**
- 推論経路: qualitative overread → anomaly を category 化する stereochemical follow-up → 1973 JOMC + 1978 Org. Synth. comments.
- DB-findable?: **yes**
- Bib confidence: **Medium–High**。EP-05a label 自体は Stage 3 snippet からの再構成を含む。

------

#### **EP-06a Mechanistic causal-linkage pack（第一群）**

**充填開始点 / 確立点**

- **Morell & Kochi 1975 JACS** は arylalkylnickel(II) species を reaction intermediate として扱い、1972 年の “diorganonickel / halo(organo)nickel” cycle に mechanistic support を与える。([ACS Publications](https://pubs.acs.org/doi/10.1021/ja00858a011?utm_source=chatgpt.com))
- **Tsou & Kochi 1979 JACS** は oxidative addition step 側の species distribution を追跡し、halide/solvent/ligand による mechanistic branch を示すため、1972 年の ligand-order → cis-diorganonickel interpretation をより精密な elementary-step 問題へ置き換える。([RSC出版](https://pubs.rsc.org/en/content/articlehtml/2021/cy/d1cy00374g?utm_source=chatgpt.com))

**充填判定**
部分充填。機構の実体化は進むが、1972 年の特定の ligand order が “cis configuration first requisite” を意味するという主張を、そのまま決定的に証明するわけではない。

**Retrieval annotation**

- Self-Tier: **Tier III**
- 推論経路: ligand order / cis-diorganonickel inference → elementary-step assignment → arylalkylnickel + oxidative-addition literature.
- DB-findable?: **yes**
- Bib confidence: **Medium–High**。

------

#### **EP-07a Boundary-test pack（第一群）**

**充填開始点 / 確立点**

- **Tamao et al. 1976 BCSJ**: “General Scope and Limitations” がまさに boundary-test pack の自己充填であり、primary/secondary alkyl, aryl, alkenyl Grignards、各種 aryl/alkenyl halides、chloride suitability、ether vs THF、limitations を扱う。
- **Organic Syntheses 1978**: halide/catalyst notes と expanded table により、chloride/bromide/iodide、fluoride の一部適用、catalyst identity、secondary Grignard isomerization などを手順レベルで補強する。([orgsyn.org](https://orgsyn.org/demo.aspx?prep=CV6P0407))
- **Tamao et al. 1982, Tetrahedron**: heterocyclic halides への展開は、original Csp² boundary の外延的拡張として記録できる。([国立国会図書館サーチ（NDLサーチ）](https://ndlsearch.ndl.go.jp/books/R100000136-I1360574094295030784?utm_source=chatgpt.com))

**充填判定**
強い充填。1972 年の “Only Csp² halides”, “chlorides remarkable”, “β-H-containing Grignards” という scope rhetoric は、1976 Full Paper で method-level boundary claim に近づく。

**Retrieval annotation**

- Self-Tier: **Tier I**
- 推論経路: “extension, refinement, application” → full scope and limitations → Tamao/Kumada 1976 BCSJ.
- DB-findable?: **yes**
- Bib confidence: **High**。

------

#### **EP-08a Replication / uncertainty pack（第三群）**

**充填開始点 / 確立点**

- **Organic Syntheses 1978**: checked by independent chemists, yield range 79–83% for 1,2-dibutylbenzene, detailed operational notes. This is the strongest available partial filling for reproducibility.([orgsyn.org](https://orgsyn.org/demo.aspx?prep=CV6P0407))
- **Tamao et al. 1976 BCSJ**: broader scope data indirectly improves robustness but does not provide modern replicate/uncertainty statistics.

**充填判定**
部分充填。checked preparation は強いが、1972 Table I 全 entry の replicate statistics ではない。

**Retrieval annotation**

- Self-Tier: **Tier II**
- 推論経路: unreported run-to-run variability → independently checked procedure → Organic Syntheses.
- DB-findable?: **uncertain**
- Bib confidence: **High for procedure reproducibility / Low–Medium for full EP completion**。

------

#### **EP-09a Internal benchmark pack（第二群）**

**充填開始点 / 確立点**

- **Tamao et al. 1976 BCSJ**: catalyst classes, organic chloride suitability, ether vs THF, and about sixty experimental results provide the strongest internal benchmark filling.
- **Organic Syntheses 1978**: catalyst comparison notes and halide comments offer procedure-level benchmark reinforcement.([orgsyn.org](https://orgsyn.org/demo.aspx?prep=CV6P0407))
- **Corriu & Masse 1972 Chem. Commun.**: concurrent similar nickel-catalyzed cross-coupling is a novelty-boundary comparator, but not a direct internal benchmark because it is a parallel communication rather than the same design matrix.([TCIchemicals.com](https://www.tcichemicals.com/CH/en/product/tci-topics/ProductHighlights_20211220?utm_source=chatgpt.com))

**充填判定**
中程度〜強い部分充填。Full Paper ではかなり補われるが、Tamura–Kochi / Corriu–Masse と完全同一条件での matched benchmarking ではない。

**Retrieval annotation**

- Self-Tier: **Tier II**
- 推論経路: unsupported superiority claim → scope/full-paper benchmark + concurrent comparator → BCSJ 1976 / Org. Synth. / Corriu–Masse.
- DB-findable?: **yes**
- Bib confidence: **High for BCSJ/OrgSynth; Medium for Corriu–Masse as comparator**。

------

#### **EP-10a Kinetic / stereochemical verification pack（第一群）**

**充填開始点 / 確立点**

- **Tamao et al. 1973 JOMC stereochemistry paper**: olefinic halides の stereospecific vs nonstereospecific-stereoselective distinction を直接扱うため、formation-selectivity と stereochemical outcome の切り分けに最も近い。([サイエンスダイレクト](https://www.sciencedirect.com/science/article/pii/S0022328X00820586?utm_source=chatgpt.com))
- **Tamao et al. 1972 JACS alkyl group isomerization paper** and **Kiso–Tamao–Kumada 1973 JOMC halide-effect paper**: secondary alkyl Grignards の isomerization と halide effects を扱い、β-H / isomerization side-path の mechanistic verification に接続する。([ACS Publications](https://pubs.acs.org/doi/10.1021/ja00781a070?utm_source=chatgpt.com))

**充填判定**
部分充填。stereochemical classification と isomerization pathway は補われるが、1972 年の cis/trans-stilbene 系に対する explicit time-course, quench-timing, product-alone heating control まで確認できるわけではない。

**Retrieval annotation**

- Self-Tier: **Tier II**
- 推論経路: stereochemical anomaly + prolonged reflux → stereochemical verification / isomerization side-path → 1973 JOMC + 1972/1973 isomerization papers.
- DB-findable?: **yes**
- Bib confidence: **Medium–High**。

------

### §C 推奨選定リスト

| 優先 | 論文                                                         | 主に充填する EP                           | 選定理由                                                     |
| ---- | ------------------------------------------------------------ | ----------------------------------------- | ------------------------------------------------------------ |
| 1    | **Tamao et al. 1976, BCSJ, “General Scope and Limitations”** | EP-01a, EP-07a, EP-09a, partly EP-02a/08a | 1972 communication の自己充填 Full Paper。scope, limitations, catalyst, solvent, chloride suitability を一括して補う。 |
| 2    | **Tamao et al. 1973, JOMC stereochemistry paper**            | EP-04a, EP-05a, EP-10a                    | cis/trans dichloroethylene anomaly を直接扱う最重要 stereochemical filling。([サイエンスダイレクト](https://www.sciencedirect.com/science/article/pii/S0022328X00820586?utm_source=chatgpt.com)) |
| 3    | **Tamao et al. 1972, JACS alkyl group isomerization**        | EP-07a, EP-10a                            | β-H-containing / secondary alkyl Grignards の side-path を初期に補強。([ACS Publications](https://pubs.acs.org/doi/10.1021/ja00781a070?utm_source=chatgpt.com)) |
| 4    | **Kiso–Tamao–Kumada 1973, JOMC halide-effect paper**         | EP-07a, EP-09a, EP-10a                    | halide identity と alkyl isomerization の関係を扱い、chloride/bromide/iodide boundary を補う。([サイエンスダイレクト](https://www.sciencedirect.com/science/article/pii/S0022328X00950630?utm_source=chatgpt.com)) |
| 5    | **Morell & Kochi 1975, JACS mechanistic study**              | EP-03a, EP-06a                            | arylalkylnickel(II) intermediate の機構的実体化。Kumada working hypothesis の外部検証軸。([ACS Publications](https://pubs.acs.org/doi/10.1021/ja00858a011?utm_source=chatgpt.com)) |
| 6    | **Tsou & Kochi 1979, JACS oxidative addition mechanism**     | EP-03a, EP-06a, EP-09a                    | Ni(0) oxidative addition、Ni species、halide/solvent/ligand effects を機構的に分解。([RSC出版](https://pubs.rsc.org/en/content/articlehtml/2021/cy/d1cy00374g?utm_source=chatgpt.com)) |
| 7    | **Kumada–Tamao–Sumitani 1978, Organic Syntheses**            | EP-01a, EP-02a, EP-08a, EP-09a            | independent checked procedure と operational reproducibility の補強。([orgsyn.org](https://orgsyn.org/demo.aspx?prep=CV6P0407)) |

------

### §D VQ階層と充填時間順序の対応分析

| 時期                               | 代表論文                                            | VQ上の意味                                                   |
| ---------------------------------- | --------------------------------------------------- | ------------------------------------------------------------ |
| 1972 original communication        | Tamao–Sumitani–Kumada 1972                          | **VQ-1 Observation**: Ni-phosphine-catalyzed Grignard / Csp²-halide coupling が起こることを示す。ただし Stage 3 判定どおり VQ-2 Method / VQ-3 Mechanism は未達。 |
| 1972–1973 immediate follow-ups     | alkyl isomerization; halide effect; stereochemistry | **VQ-2/VQ-3 の局所補強**: β-H / halide / stereochemistry の異常点を先に補う。 |
| 1975–1979 Kochi mechanistic papers | Morell & Kochi; Tsou & Kochi                        | **VQ-3 Mechanism の外部確立**: organonickel intermediate / oxidative addition / Ni speciation を実体化。ただし Kumada 1972 の black mixture そのものは未解消。 |
| 1976 Full Paper                    | Tamao et al. BCSJ                                   | **VQ-2 Method への再認定**: scope, limitations, solvent, catalyst, chloride suitability が method-level に上がる。 |
| 1978 Organic Syntheses             | Kumada–Tamao–Sumitani checked procedure             | **VQ-2 reproducibility 補強**: selected preparation の操作的再現性と yield reliability を補う。 |
| 1982 heterocyclic extension        | Tamao et al. Tetrahedron                            | **VQ-4 Extension/Application**: original method の外延を heterocyclic substrates へ広げるが、1972 EP の直接充填としては二次的。([国立国会図書館サーチ（NDLサーチ）](https://ndlsearch.ndl.go.jp/books/R100000136-I1360574094295030784?utm_source=chatgpt.com)) |

**特筆パターン**

1. **通信→Full Paper 自己充填**が明瞭。1972 年時点で未提示だった scope, limitations, catalyst/solvent comparison は 1976 BCSJ で大きく補われる。
2. **機構充填は外部グループが強い**。Kumada group の stereochemical/scope follow-up に対し、organonickel intermediate / oxidative addition の深い分光・機構充填は Kochi group が担う。
3. **VQ-3 の一部が VQ-2 より早く進む**。stereochemistry と isomerization は 1972–1973 に早く追跡されるが、method-level full scope は 1976 に整理される。
4. **EP-08a は時代慣行として残りやすい**。checked procedure はあるが、現代的な replicate statistics / uncertainty reporting とは異なる。

------

### §E 未充填EPの発見的意義

**未充填EP一覧：**

**EP-03a [Direct-observation / state-assignment pack]**

- **未充填の理由**: 部分未充填。organonickel intermediate と oxidative addition は外部機構研究で強く補われるが、1972 Example 1 の black mixture / salt-rich state について、可溶/不溶 Ni mass balance や solid-state assignment が直接行われたとは確認できない。
- **発見的意義**: あり。単なる “intermediate not observed” ではなく、本文中の visible state change と homogeneous catalytic-cycle claim の緊張を抽出する事例として有用。
- **将来の充填可能性**: 中。再実験・in situ spectroscopy・solid characterization により可能だが、歴史的系の再現が必要。

**EP-08a [Replication / uncertainty pack]**

- **未充填の理由**: 部分未充填。Organic Syntheses checked procedure は selected example の再現性を補うが、1972 Table I 全体の replicate/uncertainty matrix ではない。
- **発見的意義**: あり。communication-era の “high yield representative table” と現代的 reproducibility standard の差を明確化する。
- **将来の充填可能性**: 低〜中。再実験すれば可能だが、独立論文としての動機は弱い。

**EP-10a [Kinetic / stereochemical verification pack]**

- **未充填の理由**: 部分未充填。stereochemical follow-up はあるが、1972 cis/trans-stilbene 系での full time-course, quench timing, product-alone heating control までは確認できない。
- **発見的意義**: あり。single stereochemical anomaly を formation selectivity と post-formation scrambling に分解する設計原理を与える。
- **将来の充填可能性**: 中。現代 GC/NMR time-course で比較的容易に実施可能。

------

## Retrieval Depth Matrix

| 充填論文                                                | 充填 EP                                   | Self-Tier | 推論経路                                                     | DB-findable? | Bib confidence                               |
| ------------------------------------------------------- | ----------------------------------------- | --------- | ------------------------------------------------------------ | ------------ | -------------------------------------------- |
| Tamao et al. 1976 BCSJ, “General Scope and Limitations” | EP-01a, EP-07a, EP-09a, partly EP-02a/08a | I         | “Investigations continuing” → self-fill Full Paper → scope/limitations | yes          | High                                         |
| Tamao et al. 1973 JOMC stereochemistry                  | EP-04a, EP-05a, EP-10a                    | I         | cis/trans anomaly → stereochemistry of nickel-catalyzed coupling | yes          | High; original text verification recommended |
| Tamao et al. 1972 JACS alkyl group isomerization        | EP-07a, EP-10a                            | II        | β-H / secondary alkyl issue → alkyl isomerization side-path  | yes          | Medium–High                                  |
| Kiso–Tamao–Kumada 1973 JOMC halide effect               | EP-07a, EP-09a, EP-10a                    | II        | chloride/bromide/iodide boundary → halide effect on isomerization | yes          | Medium–High                                  |
| Morell & Kochi 1975 JACS mechanistic study              | EP-03a, EP-06a                            | II        | proposed organonickel cycle → arylalkylnickel intermediate evidence | yes          | High                                         |
| Tsou & Kochi 1979 JACS oxidative addition               | EP-03a, EP-06a, EP-09a                    | III       | chloride reactivity + Ni species → oxidative-addition mechanism / IR-EPR speciation | yes          | High                                         |
| Kumada–Tamao–Sumitani 1978 Organic Syntheses            | EP-01a, EP-02a, EP-08a, EP-09a            | II        | reporting/reproducibility gap → checked synthetic procedure  | uncertain    | High                                         |

------

## 付録：棄却候補の記録

| 棄却候補                                             | 一瞬考慮した理由                                             | 棄却の判定キー                        | 棄却理由                                                     |
| ---------------------------------------------------- | ------------------------------------------------------------ | ------------------------------------- | ------------------------------------------------------------ |
| Corriu & Masse 1972 Chem. Commun.                    | 1972 Note Added in Proof に出る concurrent similar nickel-catalyzed coupling | filling paper か comparator か        | novelty-boundary comparator として重要だが、Kumada 1972 の EP を直接充填する実験設計ではない。 |
| Tamura & Kochi 1971 JACS / Synthesis                 | prior-art problem statement の中心                           | 原論文以後かどうか                    | 1972 以前の prior art であり、EP filling ではなく背景比較。  |
| Corey–Posner cuprate / π-allylnickel reagent papers  | alternative C–C bond formation として関連                    | catalyst method EP との対応           | reagent chemistry の代替解であり、Ni-phosphine catalytic EP の充填ではない。 |
| Tamao 2002 historical review                         | 発見史と Corriu–Masse 関係を整理                             | review exclusion                      | 実験的充填論文ではなく二次情報源。                           |
| 1982 heterocyclic Grignard coupling paper            | scope extension として関連                                   | original EP への直接性                | EP-07a の外延的充填には有用だが、1976 BCSJ の方が original boundary filling として優先される。 |
| 1974–1980 asymmetric / chiral Kumada-coupling papers | 応用・高度化として重要                                       | EP-specific filling か application か | 1972 の reporting, boundary, mechanism, stereochemistry anomaly を直接埋めるより、後続応用・発展に近い。 |

---

> **Tier 8 redaction notice**: This file is a redacted copy of the corresponding Tier 3 / Tier 9 output. Verbatim source-paper quotations have been replaced by `[REDACTED: see source paper §<loc>; full text retained in Tier 9 reviewer-only deposit]` markers, preserving location references and our own analytical content. Bibliographic fields (title, authors, journal, year, DOI), analytical labels (`evidence_chain:` with B-/U-/A-/C- internal IDs), short technical terms, and our own analytical text are not redacted. The redaction was applied by `scripts/redact_for_tier8.py` and, for this version, by `scripts/build_paperA_R1_public.py` with `scripts/redact_source_ngram_runs.py` (scripts of the project repository; they are not deposited).
