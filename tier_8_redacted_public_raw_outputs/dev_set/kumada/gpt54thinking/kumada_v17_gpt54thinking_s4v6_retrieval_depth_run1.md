prompt_version: stage4-v6
prompt_version_detail: stage4-v6-20260504
model_info: GPT-5.5 Thinking
experimental_variant: retrieval-depth-annotation (Cross-vendor multi-run; prompt originally specified GPT-5.4 v6)
related_pilot_sonnet: papers/dev/kumada/kumada_v17_sonnet_s4v6_retrieval_depth.md (Sonnet Pilot 1)
related_baseline_gpt: papers/dev/kumada/gpt54thinking/kumada_v17_gpt54thinking_s4.md (April 19 baseline)
note: Multi-run robustness の cross-vendor extension。Sonnet v6 multi-run 3 runs と比較するための Stage 4 retrieval pattern / Tier annotation 出力。
date: 2026-05-08

# EP充填選定マップ

## Tamao, Sumitani, Kumada 1972（JACS communication）

入力プロンプトは Stage 3 §5 の EP-01a〜EP-10a について、歴史的に充填または部分充填した論文を §A〜§E 形式で選定することを要求している。 また、出力には retrieval-depth annotation と末尾統合マトリクスが必須とされている。 原論文側では、Table I が isolated / glpc yield、internal standard、条件 A/B、exothermic/reflux などを footnote 圧縮しており、同じ箇所で diorganonickel / halo(organo)nickel cycle が作業仮説として提示されている。 さらに、末尾では chloride reactivity、bidentate ligand order、cis-rich stilbene anomaly、ether superiority、future mechanistic / scope work が明示されている。

------

## §A EP充填難易度の三群分類

**第一群（文献で明確に追跡可能）：** EP-04a, EP-07a, EP-09a, EP-10a, EP-06a

— **EP-04a / EP-10a** は cis/trans-1,2-dichloroethylene → stilbene の stereochemistry / time-course / isomerization control という明確な検索軸を持つため、後続の stereochemistry paper と直接対応しやすい。
— **EP-07a** は “scope and limitations” 型の full paper によって最も充填されやすい。Stage 3 側でも chloride/bromide/iodide、Csp2/non-Csp2、ether/THF、failure matrix が case-specific 実装として定義されている。
— **EP-09a** は Corriu–Masse、Tamura–Kochi、Morrell–Kochi との比較軸が明示的で、同時代 benchmark 文献として追跡可能。
— **EP-06a** は imported organonickel cycle を stoichiometric / mechanistic evidence で検証する課題であり、Kochi 系の mechanistic studies と現代の Ni-state assignment 論文で追跡可能。ただし、原論文と完全同一の [NiCl2(dpe)] 系に限定すると部分充填に留まる。

**第二群（間接的に追跡可能）：** EP-01a, EP-02a, EP-03a

— **EP-01a / EP-02a** は単独主題というより、1976 年 full paper、Organic Syntheses procedure、scope paper の footnote / experimental section / product characterization として充填される性質が強い。
— **EP-03a** は [REDACTED: substantial verbatim quotation; see Tier 9] のうち、mechanistic Ni-state assignment は追跡可能だが、1972 年 Example 1 の黒色混合物そのものを後続論文が直接同定した可能性は低い。Stage 3 の case-specific 実装でも、黒色混合物の Ni mass balance、solid phase analysis、filtration / re-addition test が要求されている。

**第三群（充填が見つからない可能性あり）：** EP-08a

— **EP-08a** は 1972 communication の key yields / cis-trans ratios / solvent comparisons に uncertainty を付与する課題であり、後続 full paper や Organic Syntheses procedure により operational reproducibility は改善されるが、1972 年代表 entry そのものの反復統計としては独立論文化されにくい。Stage 3 でも EP-08a は VQ-4 への拡張要件として位置づけられている。
— C26 的には、historical exact replication / uncertainty は “constraint-disclosure-impossible” に近い。未充填であること自体が、communication-era reporting norm の痕跡を示す。

------

## §B 各EPの充填論文候補

### EP-01a Reporting-coherence pack

**主要候補 1:** Kohei Tamao, Koji Sumitani, Yoshihisa Kiso, Michio Zembayashi, Akira Fujioka, Shun-ichi Kodama, Isao Nakajima, Akio Minato, Makoto Kumada, [REDACTED: substantial verbatim quotation; see Tier 9] *Bulletin of the Chemical Society of Japan* 49, 1958–1969 (1976), DOI: 10.1246/bcsj.49.1958.

- **充填度:** strong partial / format-driven auto-resolved
- **対応内容:** 1972 communication の “extension, refinement, and application” を full-paper 化し、約 60 例の experimental results、scope / limitation、catalyst / ligand / solvent / halide effects を体系化している。
- **C23 status:** occurred — Letter / Communication → Full Paper 型の auto-resolution。
- **timescale:** medium-lag, 4 years
- **Self-Tier:** Tier I
- **推論経路:** 原論文の A2 “extension, refinement, and application” と Stage 3 EP-01a の reporting-coherence 要求から、直後に想起される本命 full paper。
- **DB-findability:** yes
- **Bibliographic confidence:** High; DOI / journal metadata verified.

**主要候補 2:** [REDACTED: substantial verbatim quotation; see Tier 9] *Organic Syntheses*. ([オーガニックシンセシス](https://orgsyn.org/demo.aspx?prep=CV6P0407))

- **充填度:** partial / procedural validation
- **対応内容:** detailed preparation、GC purity、spectral characterization、operational notes を与え、1972 communication の reporting compression を実用手順として補強する。([オーガニックシンセシス](https://orgsyn.org/demo.aspx?prep=CV6P0407))
- **C23 status:** not full-paper auto-resolution; procedure-level consolidation
- **timescale:** medium-lag
- **Self-Tier:** Tier II
- **推論経路:** EP-01a は “再現可能な方法記述” を要求するため、研究論文より Organic Syntheses 型の verified procedure が自然に候補化する。
- **DB-findability:** yes
- **Bibliographic confidence:** High; source page verified.

------

### EP-02a Identity / purity substantiation pack

**主要候補 1:** Tamao et al., BCSJ 1976.

- **充填度:** strong partial
- **対応内容:** “high purity” products and broad applicability の scope paper として、1972 年 Table I の “glpc, nmr, ir, and/or mass spectra” という圧縮記述を entry-level に近づける。
- **timescale:** medium-lag, 4 years
- **Self-Tier:** Tier I
- **DB-findability:** yes
- **Bibliographic confidence:** High.

**主要候補 2:** Organic Syntheses 1,2-dibutylbenzene procedure. ([オーガニックシンセシス](https://orgsyn.org/demo.aspx?prep=CV6P0407))

- **充填度:** partial
- **対応内容:** GC purity と spectral details を procedure validation として明示し、少なくとも代表合成例の identity / purity substantiation を補強する。([オーガニックシンセシス](https://orgsyn.org/demo.aspx?prep=CV6P0407))
- **Self-Tier:** Tier II
- **DB-findability:** yes
- **Bibliographic confidence:** High.

------

### EP-03a Direct-observation / state-assignment pack

**主要候補 1:** D. G. Morrell and J. K. Kochi, [REDACTED: substantial verbatim quotation; see Tier 9] *Journal of the American Chemical Society* 97, 7262–7270 (1975), DOI: 10.1021/ja00858a011. ([ACS Publications](https://pubs.acs.org/doi/10.1021/ja00858a011?utm_source=chatgpt.com))

- **充填度:** partial / mechanistic analog fill
- **対応内容:** alkenyl halide / Grignard / nickel catalysis の mechanistic study として、1972 paper が imported analogy に依存した Ni cycle を対象領域内で検証する方向に進める。
- **限界:** [NiCl2(dpe)]/aryl chloride の黒色混合物そのものを state-assignment した論文ではない。
- **timescale:** short-to-medium-lag, 3 years
- **Self-Tier:** Tier II
- **推論経路:** EP-03a の “active Ni state / side-product / mechanistic constraint” から Kochi の nickel catalysis mechanistic program に連想的に到達。
- **DB-findability:** yes
- **Bibliographic confidence:** High; DOI metadata verified.

**主要候補 2:** Kouki Matsubara et al., [REDACTED: substantial verbatim quotation; see Tier 9] *Organometallics* 36, 255–265 (2017). ([Google Sites](https://sites.google.com/fukuoka-u.ac.jp/matsubara-lab/matsubara-lab/published-papers))

- **充填度:** partial / late mechanistic-state fill
- **対応内容:** Kumada–Tamao–Corriu cross-coupling における dinuclear nickel systems を扱い、Ni-state assignment / catalyst structure という EP-03a の現代的実装に対応する。
- **限界:** NHC / dinuclear modern system であり、1972 年の phosphine Ni system そのものではない。
- **timescale:** late-lag, 45 years
- **Self-Tier:** Tier III
- **推論経路:** 原論文の black mixture / imported Ni cycle から、直接の 1970s follow-up では不足するため、現代の KTC mechanistic-state literature に triangulation して浮上。
- **DB-findability:** yes
- **Bibliographic confidence:** Medium-High; bibliographic metadata verified via lab publication list; DOI verification recommended.

------

### EP-04a Discrimination / replication pack

**主要候補:** Kohei Tamao, Michio Zembayashi, Yoshihisa Kiso, Makoto Kumada, [REDACTED: substantial verbatim quotation; see Tier 9] *Journal of Organometallic Chemistry* 55, C91–C94 (1973). ([サイエンスダイレクト](https://www.sciencedirect.com/science/article/pii/S0022328X00820586?utm_source=chatgpt.com))

- **充填度:** strong partial / direct stereochemical fill
- **対応内容:** 1972 paper の “cis/trans-1,2-dichloroethylene gives anomalously cis-enriched stilbene” という単発 anomaly を、olefinic halide cross-coupling の stereochemistry という独立主題に展開している。
- **限界:** full kinetic time-course まで含むかは未確認。
- **C23 status:** promised mechanistic / stereochemical detail → partially occurred
- **timescale:** short-lag, 1 year
- **Self-Tier:** Tier I
- **推論経路:** EP-04a は stereochemical anomaly の replication / discrimination を要求するため、タイトルレベルで直接対応する後続 communication が即座に候補化する。
- **DB-findability:** yes
- **Bibliographic confidence:** Medium-High; title / journal / page verified, DOI verification recommended.

------

### EP-06a Analogy-validation pack

**主要候補 1:** Morrell and Kochi 1975. ([ACS Publications](https://pubs.acs.org/doi/10.1021/ja00858a011?utm_source=chatgpt.com))

- **充填度:** strong partial
- **対応内容:** 1972 paper は stoichiometric organonickel precedents を catalytic cycle の根拠として輸入していた。Morrell–Kochi は nickel-catalyzed Grignard / alkenyl halide cross-coupling の mechanistic studies として、この imported model を同時代の mechanistic evidence へ接続する。
- **限界:** Kumada group の exact ligand / substrate matrix とは異なる可能性がある。
- **Self-Tier:** Tier II
- **DB-findability:** yes
- **Bibliographic confidence:** High.

**主要候補 2:** Satoshi Miyazaki, Yuji Koga, Takahiro Matsumoto, Kouki Matsubara, [REDACTED: substantial verbatim quotation; see Tier 9] *Chemical Communications* 46, 1932–1934 (2010), DOI: 10.1039/b924716e. ([Google Sites](https://sites.google.com/fukuoka-u.ac.jp/matsubara-lab/matsubara-lab/published-papers))

- **充填度:** partial / late structural analog
- **対応内容:** Ni(I) species の isolation / structural characterization により、1972 paper が直接観測しなかった catalyst-state layer を現代的に補強する。
- **限界:** ligand class が NHC で、1972 年 phosphine system とは異なる。
- **Self-Tier:** Tier III
- **DB-findability:** yes
- **Bibliographic confidence:** High; DOI listed in source.

------

### EP-07a Boundary-test pack

**主要候補 1:** Tamao et al., BCSJ 1976.

- **充填度:** strong
- **対応内容:** “General Scope and Limitations” として、aryl / alkenyl halides、alkyl / aryl / alkenyl Grignard reagents、β-hydrogen-containing substrates、chloride reactivity、solvent / catalyst effectsを体系化している。
- **C23 status:** occurred — 1972 communication の method / scope deferral が full paper 化。
- **timescale:** medium-lag, 4 years
- **Self-Tier:** Tier I
- **DB-findability:** yes
- **Bibliographic confidence:** High.

**主要候補 2:** Kohei Tamao, Shun-ichi Kodama, Isao Nakajima, Makoto Kumada, Akio Minato, Kenji Suzuki, “Nickel-phosphine complex-catalyzed Grignard coupling—II: Grignard coupling of heterocyclic compounds,” *Tetrahedron* 38, 3347–3354 (1982), DOI: 10.1016/0040-4020(82)80117-8. ([サイエンスダイレクト](https://www.sciencedirect.com/science/article/pii/0040402082801178?utm_source=chatgpt.com))

- **充填度:** partial / extension of boundary
- **対応内容:** heterocyclic compounds への展開により、1972 paper の “extension, refinement, and application” のうち substrate-boundary layer をさらに拡張する。
- **timescale:** late-medium, 10 years
- **Self-Tier:** Tier II
- **DB-findability:** yes
- **Bibliographic confidence:** High; DOI / metadata verified.

------

### EP-08a Replication / uncertainty pack

**主要候補:** Organic Syntheses procedure. ([オーガニックシンセシス](https://orgsyn.org/demo.aspx?prep=CV6P0407))

- **充填度:** partial only
- **対応内容:** Organic Syntheses は procedure validation、operational reproducibility、purity confirmation を提供するため、1972 communication の exemplar-level reliability を補強する。
- **未充填部分:** key yields / cis-trans ratios / solvent comparisons への statistical uncertainty は、後続文献でも明示的に標準化されていない可能性が高い。
- **timescale:** medium-lag, but exact uncertainty non-applicable
- **Self-Tier:** Tier II
- **DB-findability:** yes
- **Bibliographic confidence:** High.

------

### EP-09a Internal benchmark pack

**主要候補 1:** R. J. P. Corriu and J. P. Masse, [REDACTED: substantial verbatim quotation; see Tier 9] *Journal of the Chemical Society, Chemical Communications* 1972, 144a–144a, DOI: 10.1039/C3972000144A. ([RSC Publishing](https://pubs.rsc.org/En/content/articlehtml/1972/c3/c3972000144a))

- **充填度:** partial / concurrent benchmark
- **対応内容:** 原論文の Note Added in Proof が “similar cross-coupling reactions” として明示した同時代 competitor であり、Ni catalyst による Grignard activation / aryl or olefinic halide coupling の novelty boundary を狭める。([RSC Publishing](https://pubs.rsc.org/En/content/articlehtml/1972/c3/c3972000144a))
- **限界:** 同一測定軸での head-to-head benchmark ではない。
- **timescale:** immediate / same year
- **Self-Tier:** Tier I
- **DB-findability:** yes
- **Bibliographic confidence:** High.

**主要候補 2:** Morrell and Kochi 1975. ([ACS Publications](https://pubs.acs.org/doi/10.1021/ja00858a011?utm_source=chatgpt.com))

- **充填度:** partial / mechanistic benchmark
- **対応内容:** Tamura–Kochi 系との関係で、nickel catalysis の mechanistic benchmark を与える。
- **限界:** EP-09a が要求する “same-substrate, same-metric, head-to-head” には届かない。
- **Self-Tier:** Tier II
- **DB-findability:** yes
- **Bibliographic confidence:** High.

------

### EP-10a Kinetic verification pack

**主要候補:** Tamao, Zembayashi, Kiso, Kumada 1973 stereochemistry paper. ([サイエンスダイレクト](https://www.sciencedirect.com/science/article/pii/S0022328X00820586?utm_source=chatgpt.com))

- **充填度:** partial
- **対応内容:** stereospecific versus nonstereospecific-stereoselective reactions という論点は、formation-stage stereochemistry と post-formation scrambling を分ける EP-10a の方向に最も近い。
- **限界:** time-course / heating controls / product-alone heating control が完全に記載されているかは verification required。
- **timescale:** short-lag, 1 year
- **Self-Tier:** Tier I
- **DB-findability:** yes
- **Bibliographic confidence:** Medium-High; DOI verification recommended.

------

## §B 末尾チェック：Bibliographic verification

**Trigger condition:** 必須。
理由: 1980 年以前の古い文献が多く、Kumada / Tamao / Corriu / Kochi という author-name reaction network に属し、同一著者群の関連論文が密であるため。

| 候補                                           | Verification status | 備考                                                         |
| ---------------------------------------------- | ------------------- | ------------------------------------------------------------ |
| Tamao et al., BCSJ 1976                        | verified            | DOI / journal / page verified.                               |
| Corriu & Masse 1972                            | verified            | DOI / RSC metadata verified.                                 |
| Morrell & Kochi 1975                           | verified            | DOI / ACS metadata verified.                                 |
| Tamao et al., JOMC 1973 stereochemistry        | pending             | title / journal / page-level metadata verified; DOI 未確認。 |
| Organic Syntheses 1,2-dibutylbenzene procedure | verified            | source page verified; exact publication year / collection volume should be normalized if used bibliographically. |
| Tamao et al., Tetrahedron 1982                 | verified            | DOI / journal / page verified.                               |
| Miyazaki et al., Chem. Commun. 2010            | verified            | DOI / bibliographic listing verified.                        |
| Matsubara et al., Organometallics 2017         | pending             | bibliographic listing verified; DOI should be Crossref-checked before final database registration. |

------

## §C 推奨選定リスト

| 優先 | 推奨充填論文                                                 | 主充填EP                               | 選定理由                                                     |
| ---- | ------------------------------------------------------------ | -------------------------------------- | ------------------------------------------------------------ |
| 1    | Tamao et al., BCSJ 1976, “Nickel-Phosphine Complex-Catalyzed Grignard Coupling. I…” | EP-01a, EP-02a, EP-07a, EP-08a, EP-09a | 1972 communication の full-paper auto-resolution として最重要。scope / limitations / catalyst / solvent / halide / β-H substrate layer を最も広く補う。 |
| 2    | Tamao, Zembayashi, Kiso, Kumada, JOMC 1973 stereochemistry paper | EP-04a, EP-10a                         | 1972 paper の cis-rich stilbene anomaly を直接引き継ぐ最短 stereochemical follow-up。([サイエンスダイレクト](https://www.sciencedirect.com/science/article/pii/S0022328X00820586?utm_source=chatgpt.com)) |
| 3    | Morrell & Kochi, JACS 1975                                   | EP-03a, EP-06a, EP-09a                 | imported organonickel cycle を mechanistic literature 側から検証するための最重要同時代 benchmark。([ACS Publications](https://pubs.acs.org/doi/10.1021/ja00858a011?utm_source=chatgpt.com)) |
| 4    | Corriu & Masse, Chem. Commun. 1972                           | EP-09a                                 | 原論文 Note Added in Proof が認めた concurrent similar nickel-catalyzed cross-coupling。novelty boundary の外部 benchmark として必須。([RSC Publishing](https://pubs.rsc.org/En/content/articlehtml/1972/c3/c3972000144a)) |
| 5    | Organic Syntheses 1,2-dibutylbenzene procedure               | EP-01a, EP-02a, EP-08a                 | procedure validation / purity / reproducibility layer を補う。primary research ではないが、EP-08a の実務的充填として価値が高い。([オーガニックシンセシス](https://orgsyn.org/demo.aspx?prep=CV6P0407)) |
| 6    | Tamao et al., Tetrahedron 1982 heterocyclic coupling         | EP-07a                                 | scope boundary の長期展開。1976 full paper で足りない heterocycle domain を補う。([サイエンスダイレクト](https://www.sciencedirect.com/science/article/pii/0040402082801178?utm_source=chatgpt.com)) |
| 7    | Matsubara et al., Organometallics 2017 / Miyazaki et al., Chem. Commun. 2010 | EP-03a, EP-06a                         | 原系そのものではないが、active Ni state / dinuclear or Ni(I) species の現代的 direct-state assignment として late mechanistic fill。([Google Sites](https://sites.google.com/fukuoka-u.ac.jp/matsubara-lab/matsubara-lab/published-papers)) |

------

## §D VQ階層と充填時間順序の対応分析

**VQ-1 Observation:**
1972 paper 自体で成立。Table I と preparative examples により、Ni-phosphine 条件で Grignard / aryl or vinyl halide cross-coupling が起こることは observation-level では保持される。

**VQ-2 Method:**
主に 1976 BCSJ full paper により medium-lag で補強された。これは C23 の “Letter→Full Paper auto-resolution occurred” と判定できる。特に EP-01a / EP-02a / EP-07a が bundled filling された。

**VQ-3 Mechanism:**
二段階で部分充填された。第一段階は 1973 stereochemistry paper と 1975 Morrell–Kochi mechanistic study による short-to-medium-lag fill。第二段階は 2010 / 2017 年以降の Ni(I) / dinuclear state assignment による late-lag fill。ただし、1972 年の [NiCl2(dpe)] 黒色混合物を直接同定したわけではない。([サイエンスダイレクト](https://www.sciencedirect.com/science/article/pii/S0022328X00820586?utm_source=chatgpt.com))

**VQ-4 Benchmark:**
完全充填は未達。Corriu–Masse 1972、Morrell–Kochi 1975、1976 BCSJ は external benchmark / scope benchmark を与えるが、EP-09a が要求する same-substrate / same-metric / uncertainty-bearing head-to-head 比較には届かない。([RSC Publishing](https://pubs.rsc.org/En/content/articlehtml/1972/c3/c3972000144a))

**特筆パターン:**
本ケースでは、VQ-2 の method-level filling が比較的早く、VQ-3 の mechanism-level filling は fragmentary かつ長期化している。これは [REDACTED: substantial verbatim quotation; see Tier 9] という cross-coupling 史に典型的な時間順序である。

------

## §E 未充填EPの発見的意義

**未充填EP一覧：**

**EP-03a Direct-observation / state-assignment pack**

- **未充填の理由:** partial fill。Morrell–Kochi や Matsubara 系により mechanistic / state-assignment は進んだが、1972 年 Example 1 の “black mixture” そのものの soluble / insoluble Ni mass balance、solid-state assignment、filtration / re-addition test は未同定。
- **発見的意義:** あり。成功した name reaction の裏側で、初期条件下の実際の catalyst state が後世の標準機構図からこぼれ落ちる構造を示す。
- **将来の充填可能性:** 中。archival exact replication は難しいが、historically informed replication と modern in situ spectroscopy で近似的に再構成できる。

**EP-08a Replication / uncertainty pack**

- **未充填の理由:** partial fill。Organic Syntheses procedure による operational reproducibility はあるが、1972 Table I の key yields / cis-trans ratios / solvent comparisons に statistical uncertainty を付け直す文献は未同定。
- **発見的意義:** あり。communication-era における “single-number yield culture” と現代の benchmark-grade method validation の距離を可視化する。
- **将来の充填可能性:** 低〜中。厳密な historical uncertainty は復元不能だが、代表条件の modern replication study は可能。

**EP-09a Internal benchmark pack**

- **未充填の理由:** partial fill。Corriu–Masse、Morrell–Kochi、Tamao 1976 は比較対象を与えるが、Tamura–Kochi 系、halide class、ether/THF を同一基質・同一測定軸で head-to-head に置く full benchmark は未同定。
- **発見的意義:** あり。name reaction の成立過程では、外部優位性の主張が “direct benchmark” ではなく “narrative comparison” として流通しやすいことを示す。
- **将来の充填可能性:** 中。現代的 benchmark study として実施可能だが、歴史的 incentive は低い。

------

## Retrieval Depth 統合マトリクス

| 充填論文                                                     | 充填 EP                                | Self-Tier | 推論経路                                                     | DB-findable? | Bib confidence                                               |
| ------------------------------------------------------------ | -------------------------------------- | --------- | ------------------------------------------------------------ | ------------ | ------------------------------------------------------------ |
| Tamao et al., BCSJ 1976, “Nickel-Phosphine Complex-Catalyzed Grignard Coupling. I…” | EP-01a, EP-02a, EP-07a, EP-08a, EP-09a | Tier I    | 原論文 A2 “extension, refinement, and application” と Stage 3 boundary / reporting EP から直接想起。 | yes          | High; DOI verified.                                          |
| Tamao, Zembayashi, Kiso, Kumada, JOMC 1973 stereochemistry paper | EP-04a, EP-10a                         | Tier I    | cis/trans stilbene anomaly → stereochemistry of nickel-catalyzed Grignard coupling という直接経路。 | yes          | Medium-High; DOI pending.                                    |
| Morrell & Kochi, JACS 1975                                   | EP-03a, EP-06a, EP-09a                 | Tier II   | imported organonickel cycle → nickel catalysis mechanism → Kochi mechanistic study。 | yes          | High; DOI verified.                                          |
| Corriu & Masse, Chem. Commun. 1972                           | EP-09a                                 | Tier I    | 原論文 Note Added in Proof から直接想起される concurrent comparator。 | yes          | High; DOI verified.                                          |
| Organic Syntheses 1,2-dibutylbenzene procedure               | EP-01a, EP-02a, EP-08a                 | Tier II   | reporting / reproducibility EP → verified synthetic procedure という方法論的連想。 | yes          | High; source verified; exact bibliographic normalization recommended. |
| Tamao et al., Tetrahedron 1982 heterocyclic coupling         | EP-07a                                 | Tier II   | scope boundary → heterocyclic extension → Kumada group sequel。 | yes          | High; DOI verified.                                          |
| Miyazaki et al., Chem. Commun. 2010                          | EP-03a, EP-06a                         | Tier III  | catalyst-state assignment が 1970s 文献だけでは不足するため、modern Ni(I) structural literature へ triangulation。 | yes          | High; DOI verified.                                          |
| Matsubara et al., Organometallics 2017                       | EP-03a, EP-06a                         | Tier III  | KTC cross-coupling active-state problem → dinuclear Ni systems → modern Organometallics paper。 | yes          | Medium-High; DOI verification recommended.                   |

------

## 付録：棄却候補の記録

1. **Kohei Tamao, “Discovery of the nickel-catalyzed Grignard cross-coupling reaction,” \*Journal of Organometallic Chemistry\* 653, 23–26 (2002).**
   - **棄却理由:** review / historical account であり、Stage 4 prompt の規則上、review は原則として EP 充填論文ではない。([サイエンスダイレクト](https://www.sciencedirect.com/science/article/abs/pii/S0022328X02011592))
   - **利用価値:** 充填論文探索の二次情報源としては有用。
2. **Zell et al., [REDACTED: substantial verbatim quotation; see Tier 9]**
   - **棄却理由:** C–Cl activation / NHC–Ni(0) chemistry として EP-03a / EP-06a に隣接するが、Grignard cross-coupling の historical fill というより modern related mechanistic chemistry。([サイエンスダイレクト](https://www.sciencedirect.com/science/article/abs/pii/S0022328X11000246))
3. **Nickamine / bimetallic oxidative addition studies on alkyl–aryl Kumada coupling.**
   - **棄却理由:** modern mechanistic relevance はあるが、alkyl–aryl / NHC system 寄りで、1972 aryl/vinyl halide + Ni-phosphine EP への case-specific 対応が弱い。([InfoScience](https://infoscience.epfl.ch/bitstreams/88976163-5e9d-4760-be95-27e0e8d3b8b0/download))
4. **Kiso / Tamao / Kumada early 1972–1973 papers on alkyl group isomerization during Grignard coupling.**
   - **棄却理由:** β-hydrogen / rearrangement layer には関連する可能性があるが、現時点で bibliographic verification が不足し、EP-07a / EP-10a は BCSJ 1976 と JOMC 1973 stereochemistry paper でより直接に充填される。
5. **一般的な Kumada coupling reviews / textbooks.**
   - **棄却理由:** EP を構造的に整理する二次情報源にはなるが、新規実験的証拠を提供しないため、充填論文としては不採用。

---

> **Tier 8 redaction notice**: This file is a redacted copy of the corresponding Tier 3 / Tier 9 output. Verbatim source-paper quotations have been replaced by `[REDACTED: see source paper §<loc>; full text retained in Tier 9 reviewer-only deposit]` markers, preserving location references and our own analytical content. Bibliographic fields (title, authors, journal, year, DOI), analytical labels (`evidence_chain:` with B-/U-/A-/C- internal IDs), short technical terms, and our own analytical text are not redacted. The redaction was applied by `scripts/redact_for_tier8.py` and, for this version, by `scripts/build_paperA_R1_public.py` with `scripts/redact_source_ngram_runs.py` (scripts of the project repository; they are not deposited).
