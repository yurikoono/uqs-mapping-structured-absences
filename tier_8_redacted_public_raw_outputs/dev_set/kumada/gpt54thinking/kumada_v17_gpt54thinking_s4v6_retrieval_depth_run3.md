```text
prompt_version: stage4-v6
model_info: gpt-5.5-thinking
experimental_variant: retrieval-depth-annotation (Cross-vendor multi-run, GPT-5.4 v6-compatible execution)
related_pilot_sonnet: papers/dev/kumada/kumada_v17_sonnet_s4v6_retrieval_depth.md (Sonnet Pilot 1)
related_baseline_gpt: papers/dev/kumada/gpt54thinking/kumada_v17_gpt54thinking_s4.md (April 19 baseline)
note: Multi-run robustness の cross-vendor extension。Sonnet v6 multi-run 3 runs と比較して retrieval pattern と Tier annotation の安定性を測定する。
date: 2026-05-08
source_basis: uploaded PASTE_PROMPT_v6 + uploaded Kumada 1972 PDF
```

入力プロンプトと retrieval annotation 要求はアップロードされた `PASTE_PROMPT_v6.md` に基づく。原論文の主要事実は、Kumada 1972 PDF の Table I、機構仮説、scope/ligand/solvent/stereochemistry claims、および「Further studies…」「Investigations are continuing…」の明示的 deferral に基づく。

# EP充填選定マップ

## Tamao / Sumitani / Kumada 1972（JACS communication）

## §A EP充填難易度の三群分類

**第一群（文献で明確に追跡可能）:**
EP-04a, EP-07a, EP-09a, EP-10a
— stereochemistry、scope / limitations、halide / solvent / ligand comparison は、同じ Kumada group の 1973–1976 follow-up と Organic Syntheses procedure に明確な後続データがある。1976 BCSJ full paper は “General Scope and Limitations” として約60例、chloride suitability、ether superiority、ligand最適性、β-H-containing Grignard の適用を明示的に拡張している。

**第二群（間接的に追跡可能）:**
EP-01a, EP-02a, EP-03a, EP-08a
— reporting / purity / reproducibility は 1976 BCSJ と 1978 Organic Syntheses checked procedure で部分的に補われるが、1972 Table I の全 entry について内部標準・response factor・entry-by-entry spectra が完全に回収されるわけではない。Organic Syntheses procedure は GC purity 99.5%、IR/NMR assignment、checkers による再現性確認を与えるため、特定 substrate については強い補強である。([orgsyn.org](https://orgsyn.org/demo.aspx?prep=CV6P0407))

**第三群（充填が見つからない可能性あり）:**
EP-05a, EP-06a
— exact NiCl₂(dpe) / NiCl₂(dppp) catalytic mixture の black-mixture catalyst-state assignment、catalyst-free / ligand-free / nickel-salt-only controls、1972 Table I の全 byproduct mass balance は、後続文献でも完全充填ではなく、Morell–Kochi 1975 や Tsou–Kochi 1979 による mechanistic analog filling に留まる。([ACS Publications](https://pubs.acs.org/doi/10.1021/ja00858a011?utm_source=chatgpt.com))

C23 trigger: **applicable**。1972 JACS は communication であり、1976 BCSJ “General Scope and Limitations” は Letter→Full Paper 的な自己充填に近い。ただし window は典型的 1–3 年より長い **4 年**なので、`auto_resolution_status: occurred_delayed` とするのが妥当。

------

## §B 各EPの充填論文候補

### EP-01a Reporting-coherence pack（第二群）

- **充填するRI**: RI-01 Reporting integrity
- **充填開始点**: Tamao et al., Bull. Chem. Soc. Jpn. 1976, 49, 1958–1969 — 約60例を提示し、GC / isolated yield、条件、触媒・溶媒・基質範囲を体系化。
- **充填確立点**: Kumada / Tamao / Sumitani, Org. Synth. 1978, 58, 127 — 1,2-dibutylbenzene について checked procedure、GC purity、IR/NMR assignment を提示。([orgsyn.org](https://orgsyn.org/demo.aspx?prep=CV6P0407))
- **充填の性質**: Partial
- **残存未充填**: 1972 Table I 全 entry の内部標準、response factor、run-to-run variability は直接回収されない。
- **filling_timescale_category**: medium-term / format-driven delayed
- **Retrieval Tier**: Tier I
- **推論経路**: EP が yield-basis coherence を要求しており、1976 full paper と Organic Syntheses checked procedure が直結。
- **DB-findability**: yes
- **Bib confidence**: High

### EP-02a Identity / purity substantiation pack（第二群）

- **充填するRI**: RI-02 Object identification
- **充填開始点**: Tamao et al., Bull. Chem. Soc. Jpn. 1976 — scope expansion と product purity / high-yield claims を提示。
- **充填確立点**: Org. Synth. 1978 procedure — GC purity 99.5%、IR/NMR assignment を checked preparation として提示。([orgsyn.org](https://orgsyn.org/demo.aspx?prep=CV6P0407))
- **充填の性質**: Partial
- **残存未充填**: 1972 Table I 全生成物の spectral assignment を entry-wise に補完するものではない。
- **filling_timescale_category**: medium-term
- **Retrieval Tier**: Tier I
- **推論経路**: “glpc, nmr, ir, and/or mass spectra” の曖昧性を、後続 checked synthesis が最も具体的に補う。
- **DB-findability**: yes
- **Bib confidence**: High

### EP-03a Byproduct / intermediate / catalyst-state accounting pack（第二群）

- **充填するRI**: RI-03 Mechanistic accounting / RI-06 Catalyst-state uncertainty
- **充填開始点**: Morell and Kochi, JACS 1975, 97, 7262–7270 — arylalkylnickel(II) species as intermediates を扱う mechanistic study。([ACS Publications](https://pubs.acs.org/doi/10.1021/ja00858a011?utm_source=chatgpt.com))
- **充填確立点**: Tsou and Kochi, JACS 1979, 101, 6319–6332 — Ni(0) complexes と aromatic halides の oxidative addition mechanism を扱う。([ACS Publications](https://pubs.acs.org/doi/10.1021/ja00515a028?utm_source=chatgpt.com))
- **充填の性質**: Indirect / Partial
- **残存未充填**: Kumada 1972 の exact Ni-phosphine / Grignard / black-mixture system の operando catalyst-state assignment ではない。
- **filling_timescale_category**: short-to-medium-term
- **Retrieval Tier**: Tier II
- **推論経路**: EP から “organonickel intermediates / oxidative addition / arylalkylnickel” に展開し、Kochi mechanistic literature に到達。
- **DB-findability**: yes
- **Bib confidence**: High

### EP-04a Discrimination / replication pack（第一群）

- **充填するRI**: RI-04 Unreplicated discriminator
- **充填開始点 / 確立点**: Tamao, Zembayashi, Kiso, Kumada, J. Organomet. Chem. 1973, 55, C91–C94, “Stereochemistry of the nickel-catalyzed cross-coupling reaction…” — monohalo-olefins は stereospecific、1,2-dihaloethylenes は nonstereospecific かつ cis-olefin stereoselective という形で、1972 の cis-stilbene anomaly を直接展開。([サイエンスダイレクト](https://www.sciencedirect.com/science/article/pii/S0022328X00820586?utm_source=chatgpt.com))
- **充填の性質**: Complete に近い Partial
- **残存未充填**: time-course / post-formation isomerization control の詳細は要確認。
- **filling_timescale_category**: short-term, 1 yr
- **Retrieval Tier**: Tier I
- **推論経路**: EP が cis/trans dichloroethylene と stilbene ratio を名指ししており、1973 stereochemistry paper が直結。
- **DB-findability**: yes
- **Bib confidence**: High

### EP-05a Negative-control / catalytic sufficiency pack（第三群）

- **充填するRI**: RI-06 Control insufficiency
- **充填開始点**: 未同定
- **充填確立点**: 未同定
- **充填の性質**: Unfilled / constraint-disclosure-impossible に近い
- **理由**: catalyst-free、ligand-free、nickel-salt-only controls を 1972 の全条件に対して同一 assay で示す論文は確認できない。1976 BCSJ は scope / catalyst comparison を拡張するが、negative-control matrix の完全提示とは別物。
- **filling_timescale_category**: non-applicable
- **Retrieval Tier**: Tier III
- **推論経路**: catalyst sufficiency → controls → later full paper / OrgSyn を確認したが、baseline controls は主目的ではない。
- **DB-findability**: uncertain
- **Bib confidence**: Medium-Low; full 1976 PDF と experimental tables の直接確認推奨

### EP-06a Catalyst-state validation pack（第三群）

- **充填するRI**: RI-06 Catalyst-state uncertainty
- **充填開始点**: Morell and Kochi 1975 — arylalkylnickel(II) intermediates の mechanistic evidence。([ACS Publications](https://pubs.acs.org/doi/10.1021/ja00858a011?utm_source=chatgpt.com))
- **充填確立点**: Tsou and Kochi 1979 — oxidative addition mechanism の step-specific evidence。([ACS Publications](https://pubs.acs.org/doi/10.1021/ja00515a028?utm_source=chatgpt.com))
- **充填の性質**: Indirect
- **残存未充填**: 1972 Example 1 の “black mixture” を homogeneous / heterogeneous / decomposition のいずれかに割り当てる直接データではない。
- **filling_timescale_category**: medium-term
- **Retrieval Tier**: Tier II
- **推論経路**: black mixture の catalyst-state 問題から、直接 follow-up ではなく Kochi mechanistic nickel literature に移動。
- **DB-findability**: yes
- **Bib confidence**: High for indirect candidate; Low for exact-system filling

### EP-07a Boundary-test pack（第一群）

- **充填するRI**: RI-07 Unsupported boundary
- **充填開始点**: Kiso / Tamao / Kumada, J. Organomet. Chem. 1973, 50, C12–C14 — secondary alkyl Grignard の isomerization と halide identity の効果を扱う。([サイエンスダイレクト](https://www.sciencedirect.com/science/article/abs/pii/S0022328X00950630?utm_source=chatgpt.com))
- **充填確立点**: Tamao et al., Bull. Chem. Soc. Jpn. 1976 — primary / secondary alkyl、aryl、alkenyl Grignard、aryl / alkenyl halides、chloride suitability、ether preference、limitations を体系的に提示。
- **充填の性質**: Complete に近い Partial
- **残存未充填**: Csp² / non-Csp² の failure matrix は “alkyl halides give complex mixtures” として補われるが、全 matched-pair matrix ではない。OrgSyn discussion も alkyl halides が complex mixture を与えると述べる。([orgsyn.org](https://orgsyn.org/demo.aspx?prep=CV6P0407))
- **filling_timescale_category**: short-to-medium-term
- **Retrieval Tier**: Tier I
- **推論経路**: “scope boundary” から 1976 “General Scope and Limitations” に直行。
- **DB-findability**: yes
- **Bib confidence**: High

### EP-08a Replication / uncertainty pack（第二群）

- **充填するRI**: RI-08 Unquantified reliability
- **充填開始点**: Org. Synth. 1978 checked procedure — 1,2-dibutylbenzene preparation が Chan and Masamune により checked。([orgsyn.org](https://orgsyn.org/demo.aspx?prep=CV6P0407))
- **充填確立点**: 同上
- **充填の性質**: Partial
- **残存未充填**: checked procedure は代表反応の再現性を強めるが、1972 Table I 全体の N 数・標準偏差ではない。
- **filling_timescale_category**: medium-term
- **Retrieval Tier**: Tier II
- **推論経路**: replication / uncertainty から、研究論文ではなく Organic Syntheses checked protocol が最も該当。
- **DB-findability**: yes
- **Bib confidence**: High

### EP-09a Internal benchmark pack（第一群）

- **充填するRI**: RI-09 External superiority / benchmark integrity
- **充填開始点**: Corriu and Masse, Chem. Commun. 1972, 144 — concurrent nickel-catalyzed Grignard activation / trans-stilbenes and polyphenyls synthesis。Kumada 1972 の Note Added in Proof にも類似報告として現れる。([orgsyn.org](https://orgsyn.org/demo.aspx?prep=CV6P0407))
- **充填確立点**: Tamao et al., Bull. Chem. Soc. Jpn. 1976 — catalyst, solvent, halide, substrate breadth を internal benchmark 化。
- **充填の性質**: Partial
- **残存未充填**: Tamura–Kochi / Corriu–Masse / Kumada を完全同一条件で横並び比較した benchmark paper ではない。
- **filling_timescale_category**: immediate + medium-term consolidation
- **Retrieval Tier**: Tier I
- **推論経路**: Note Added in Proof と “in contrast with Tamura and Kochi” から、concurrent / prior-art benchmark に直接到達。
- **DB-findability**: yes
- **Bib confidence**: High

### EP-10a Kinetic verification pack（第一群）

- **充填するRI**: RI-05 Qualitative overread / RI-04 Discriminator validation
- **充填開始点**: Tamao, Zembayashi, Kiso, Kumada, J. Organomet. Chem. 1973, 55, C91–C94 — monohalo-olefin と 1,2-dihaloethylene の stereochemical divergence を整理。([サイエンスダイレクト](https://www.sciencedirect.com/science/article/pii/S0022328X00820586?utm_source=chatgpt.com))
- **充填確立点**: 1976 BCSJ full paper — stereochemical feature を scope discussion 内に統合し、Z-stilbene formation と ligand dependence を参照。([orgsyn.org](https://orgsyn.org/demo.aspx?prep=CV6P0407))
- **充填の性質**: Partial
- **残存未充填**: 真の kinetic time-course と quench-timing study まで満たすかは未確認。
- **filling_timescale_category**: short-term
- **Retrieval Tier**: Tier I
- **推論経路**: cis/trans anomaly から stereochemistry follow-up へ直接。
- **DB-findability**: yes
- **Bib confidence**: High

------

## §C 推奨選定リスト

| 優先 | 充填論文                                                   | 主に充填するEP        | 選定理由                                                     |
| ---- | ---------------------------------------------------------- | --------------------- | ------------------------------------------------------------ |
| 1    | Tamao et al., BCSJ 1976, 49, 1958–1969                     | EP-01, 02, 07, 09, 10 | 1972 communication の delayed full-paper / scope-limitations consolidation。約60例、chloride suitability、ether preference、ligand最適化、β-H-containing Grignard applicability をまとめる中核文献。 |
| 2    | Tamao / Zembayashi / Kiso / Kumada, JOMC 1973, 55, C91–C94 | EP-04, 10             | 1972 の最も目立つ stereochemical anomaly を直接追跡する最短 follow-up。([サイエンスダイレクト](https://www.sciencedirect.com/science/article/pii/S0022328X00820586?utm_source=chatgpt.com)) |
| 3    | Kiso / Tamao / Kumada, JOMC 1973, 50, C12–C14              | EP-07, 10             | secondary alkyl Grignard、halide nature、isomerization の境界条件を扱う。([サイエンスダイレクト](https://www.sciencedirect.com/science/article/abs/pii/S0022328X00950630?utm_source=chatgpt.com)) |
| 4    | Morell / Kochi, JACS 1975, 97, 7262–7270                   | EP-03, 06             | organonickel intermediate 問題への最も重要な mechanistic analog filling。([ACS Publications](https://pubs.acs.org/doi/10.1021/ja00858a011?utm_source=chatgpt.com)) |
| 5    | Tsou / Kochi, JACS 1979, 101, 6319–6332                    | EP-03, 06, 07         | oxidative addition step を切り出す mechanistic filling。chloride reactivity claim の step-specific 検証軸を与える。([ACS Publications](https://pubs.acs.org/doi/10.1021/ja00515a028?utm_source=chatgpt.com)) |
| 6    | Kumada / Tamao / Sumitani, Org. Synth. 1978, 58, 127       | EP-01, 02, 08         | checked procedure として、purity / practical reproducibility / safety を補う。([orgsyn.org](https://orgsyn.org/demo.aspx?prep=CV6P0407)) |
| 7    | Corriu / Masse, Chem. Commun. 1972, 144                    | EP-09                 | 同時発見・競合 benchmark。Kumada 1972 の novelty space を切るが、完全な filling paper というより competitive-positioning paper。([orgsyn.org](https://orgsyn.org/demo.aspx?prep=CV6P0407)) |

------

## §D VQ階層と充填時間順序の対応分析

**VQ-1 / reporting coherence:**
1976 BCSJ と 1978 OrgSyn により、1972 communication の compressed reporting はかなり補われる。ただし、完全な entry-wise analytical audit ではない。

**VQ-2 / boundary and scope reliability:**
1973–1976 の Kumada group follow-up により、halide、ligand、solvent、β-H-containing Grignard の boundary は最もよく補強された。これは 1972 論文の “extension, refinement, and application” deferral が実際に自己充填された領域。

**VQ-3 / mechanistic assignment:**
Morell–Kochi 1975 と Tsou–Kochi 1979 は mechanistic plausibility を強く補強するが、Kumada 1972 の exact black mixture / exact catalyst species を直接可視化するものではない。ここは “general organonickel mechanism filled, exact original catalyst-state not filled” という非対称が残る。

**VQ-4 / benchmark-grade comparison:**
Corriu–Masse 1972、Tamura–Kochi prior-art、1976 BCSJ により競争文脈は整理されるが、同一条件・同一 assay による cross-vendor 的 benchmark ではない。したがって VQ-4 は部分到達。

**時間順序:**
1972 同年に competitive benchmark、1973 に stereochemistry / isomerization、1975 に mechanistic analog、1976 に delayed full scope、1978 に checked procedure、1979 に oxidative addition mechanism。最も早く充填されたのは「異常な観測の追試・展開」で、最も遅く残ったのは「触媒状態の直接同定」である。

------

## §E 未充填EPの発見的意義

**EP-05a Negative-control / catalytic sufficiency pack**

- **未充填の理由**: incentive-structure unfilled。成功反応として定着したため、catalyst-free / ligand-free / nickel-salt-only controls を全条件で systematically publish する動機が弱い。
- **発見的意義**: あり。1972 の “catalytic sufficiency” claim を現代基準で再構築するなら、この EP は最も制度的に重要。
- **将来の充填可能性**: 中。historical replication study としてなら可能だが、通常の synthetic-methods paper では優先度が低い。

**EP-06a Exact catalyst-state validation pack**

- **未充填の理由**: constraint-disclosure-impossible に近い。1972 条件下の black mixture について、当時の operando spectroscopy / kinetics / catalyst-state separation は困難。
- **発見的意義**: あり。Ni catalysis の homogeneous / heterogeneous / decomposition boundary を問う現代的再解析に直結する。
- **将来の充填可能性**: 高。現代なら in situ EPR, XAS, NMR, stopped-flow, GC/MS mass balance, poisoning tests, TEM / ICP で再検証可能。

------

# Retrieval Depth Matrix

| 充填論文                                      | 充填EP                | Self-Tier | 推論経路                                                     | DB-findable? | Bib confidence |
| --------------------------------------------- | --------------------- | --------- | ------------------------------------------------------------ | ------------ | -------------- |
| Tamao et al., BCSJ 1976, 49, 1958–1969        | EP-01, 02, 07, 09, 10 | I         | “extension / refinement / application” + “General Scope and Limitations” に直結 | yes          | High           |
| Org. Synth. 1978, 58, 127                     | EP-01, 02, 08         | II        | reporting / purity / reproducibility → checked procedure     | yes          | High           |
| Tamao et al., JOMC 1973, 55, C91–C94          | EP-04, 10             | I         | cis/trans anomaly → stereochemistry follow-up                | yes          | High           |
| Kiso / Tamao / Kumada, JOMC 1973, 50, C12–C14 | EP-07, 10             | II        | β-H / secondary alkyl issue → alkyl isomerization / halide nature | yes          | High           |
| Morell / Kochi, JACS 1975, 97, 7262–7270      | EP-03, 06             | II        | proposed organonickel intermediates → arylalkylnickel mechanistic study | yes          | High           |
| Tsou / Kochi, JACS 1979, 101, 6319–6332       | EP-03, 06, 07         | II        | chloride / oxidative addition claim → Ni(0) oxidative addition mechanism | yes          | High           |
| Corriu / Masse, Chem. Commun. 1972, 144       | EP-09                 | I         | Note Added in Proof → concurrent benchmark                   | yes          | High           |

------

# Appendix: 棄却候補の記録

| 棄却候補                                              | 棄却理由                                                     |
| ----------------------------------------------------- | ------------------------------------------------------------ |
| Corey / Posner organocuprate papers                   | 1972 Kumada が alternative reagent chemistry として認識しているが、transition-metal catalyst EP の直接充填ではない。 |
| π-allylnickel reagent literature                      | selective cross-coupling の先行概念として重要だが、Ni-phosphine catalytic Grignard coupling の EP を case-specific に埋めない。 |
| Tamura–Kochi soluble catalyst papers                  | comparative backdrop として必須だが、Kumada 1972 の missing controls / mechanism / analytical details を充填するより、競合 prior-art として機能する。 |
| Kumada 1980 Pure Appl. Chem. review                   | 有用な二次整理だが、Stage 4 ルール上、review は原則として EP filling paper ではない。 |
| Modern Ni-catalysis mechanistic papers after 2000     | black-mixture / Ni-state 問題への現代的 insight は与えるが、1972 EP の historical filling としては時代・系が離れすぎる。 |
| Negishi / Suzuki / Stille cross-coupling developments | cross-coupling field の発展として重要だが、Kumada 1972 の specific EP を直接充填しない。 |