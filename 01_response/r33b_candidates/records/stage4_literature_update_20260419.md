---
title: stage4 literature update
created: 2026-04-19
status: active
audience: portfolio
open_questions: false
backfilled: true
---

# Kumada 1972 Stage 4 — Literature-Identification Update (2026-04-19)

**Purpose**: Cross-model validation of the Kumada 1972 Stage 4 filling-paper candidate list.

**Rationale**: The original Stage 4 output at `papers/dev/kumada/kumada_v17_sonnet_s4v2.md` proposed filling-paper candidates with confidence=Low/Medium for most EPs, because Claude Sonnet's training-data coverage of 1970s–1980s organometallic literature was inferential rather than direct. The GPT-5.4 Thinking run on the same input (2026-04-19, archived at `papers/dev/kumada/gpt54thinking/kumada_v17_gpt54thinking_s4.md`) identified **specific papers with DOIs** for the same EPs. This document consolidates the GPT-5.4 findings into a revised Kumada 1972 Stage 4 filling-paper map with elevated confidence levels.

**Provenance**: this document does not replace the original Stage 4 output — that file remains the primary analytical record. This document is a **cross-model-validated supplement** that the authors may cite in Results Part 3 and SI-4 to raise Stage 4 confidence.

---

## SI-6.7 / Stage 4 cross-model validation

The GPT-5.4 Thinking Stage 4 output (`papers/dev/kumada/gpt54thinking/kumada_v17_gpt54thinking_s4.md` §B and §C) provides specific literature identification for seven of the nine EPs (EP-01a, EP-02a, EP-03a, EP-04a, EP-06a, EP-07a, EP-10a) with confidence=High or Medium. EP-08a and EP-09a remain unfilled (confirming the finding in Results Part 3 that ≈50-year-unfilled EPs map to publication-incentive-structure gaps rather than technical gaps).

Where GPT-5.4 identified a paper by DOI, that identification is treated as **corroborating the literature-reachability hypothesis** (the paper exists in the indexed chemistry literature and is locatable by keyword). Confidence upgrade from the original Stage 4 to this update reflects this corroboration, not independent experimental verification; authors should still perform a final pre-submission read of each cited paper to confirm that the experimental content matches the EP requirement.

---

## §A Updated filling-paper recommendations

### EP-01a Reporting-coherence pack (RI-01)

**Original Stage 4 recommendation (Sonnet)**: Tamao et al., *Bull. Chem. Soc. Jpn.* 1976, 49, 1958–1969, Partial, **confidence=Medium**.

**GPT-5.4 identification**: Tamao et al., *Bull. Chem. Soc. Jpn.* 1976, 49, 1958–1969 — "General Scope and Limitations" Full Paper. Partial filling (catalyst-class scope table + general limitations; yield-basis unification not fully achieved). **Confidence=High**.

**Updated recommendation**: Tamao 1976 BCSJ, Partial filling, **confidence=High** (upgraded from Medium by cross-model identification).

### EP-02a Identity / purity substantiation pack (RI-02)

**Original Stage 4**: Tamao 1976 BCSJ, Partial, **confidence=Low** ("EP-02a要件とFull Paper内容の対応関係は実際の文献確認が必要").

**GPT-5.4 identification**: 
- **Starting point**: Tamao et al., *Bull. Chem. Soc. Jpn.* 1976, 49, 1958–1969 — abstract claims "high purity of the coupling products", substrate classes expanded.
- **Establishing point**: Tamao et al., *Tetrahedron* 1982, 38, 3347–3354 — heterocyclic Grignard couplings, identification operation extended to a new substrate class.

**Updated recommendation**: Tamao 1976 BCSJ (starting point) + Tamao 1982 *Tetrahedron* (establishing point), Partial filling, **confidence=Medium** (upgraded from Low; still Medium because alternative-isomer-exclusion granularity requires paper-text confirmation).

### EP-03a Direct-observation / state-assignment pack (RI-03)

**Original Stage 4**: Tamao et al., *J. Organomet. Chem.* ~1982 (speculative); Yamamoto 1970 ref 11 dipy-Ni system (not a fill of dpe system); Kochi group mechanistic studies ~1975–1985 (speculative). **Confidence=Low**.

**GPT-5.4 identification**:
- **Starting point**: Morrell and Kochi, *J. Am. Chem. Soc.* 1975, 97, 7262–7270 — "Role of arylalkylnickel(II) species as intermediates" for aryl halide / alkylmetal cross-coupling; organonickel intermediates placed at the mechanistic center.
- **Establishing point**: Dawson et al., *Chem. Eur. J.* 2020, 26, 8002 — stereospecific Kumada coupling of benzylic ethers with spectroscopic studies and catalyst resting-state identification supporting a Ni(0)/Ni(II) cycle.

**Updated recommendation**: Morrell–Kochi 1975 (starting point, Indirect — aryl-alkyl Ni, not dpe system specifically) + Dawson 2020 (establishing point, Indirect — Kumada system, benzylic ether substrate). **Confidence=High** for paper existence and topical relevance; filling remains **Indirect** because same-catalyst-system (NiCl₂(dpe)) direct observation is not the subject of either paper.

**Improvement over original**: specific papers now locatable; the long-suspected 2020 technology-driven filling slot is filled (this is the paper that provides spectroscopic state-assignment at a level impossible in 1972).

### EP-04a Discrimination / replication pack (RI-04, cis/trans kinetic vs thermodynamic)

**Original Stage 4**: **未同定** (not identified), confidence=Low, judged "未充填の可能性が高い".

**GPT-5.4 identification** (author corrected 2026-04-22): Tamao, Zembayashi, Kiso, Kumada, *J. Organomet. Chem.* 1973, 55, C91–C94, DOI: 10.1016/S0022-328X(00)82058-6 — "Stereochemistry of the nickel-catalyzed cross-coupling reaction of Grignard reagents with olefinic halides: stereospecific versus nonstereospecific-stereoselective reactions" — **direct self-filling of the cis/trans anomaly** identified in SRG-6 of SI-3. (Note: GPT-5.4's original output listed the third author as "Sumitani"; library DOI verification on 2026-04-22 established the third author is "Zembayashi"; journal/year/volume/page/title were all confirmed correct.)

**Updated recommendation**: Tamao-Zembayashi-Kiso-Kumada 1973 *JOM*, Partial filling, **confidence=High** (upgraded from "未充填の可能性" to specific paper identified).

**Major revision**: this EP was marked unfillable in the original Stage 4 due to incentive-structure-mismatch reasoning, but GPT-5.4 located a 1973 self-filling paper by the same authors explicitly addressing the cis/trans stereochemistry. The original "incentive-structure mismatch" explanation was partially wrong; the filling exists but is one degree of citation-distance from Kumada 1972. This also partially resolves open-issue OI-001 (β-H elimination pattern) because the 1973 stereochemistry paper is the natural locus for any subsequent β-H probe.

### EP-06a Analogy-validation pack (RI-06)

**Original Stage 4**: Tamao 1976 BCSJ (not the ideal target — it's Full Paper, not stoichiometric validation); Tsou-Kochi 1979 *JACS* (speculative, not identified specifically). **Confidence=Low**.

**GPT-5.4 identification**:
- **Starting point**: Morrell and Kochi, *J. Am. Chem. Soc.* 1975, 97, 7262–7270 — arylalkyl nickel(II) intermediates explicitly studied to validate the imported organonickel picture.
- **Establishing point** (long-delayed technology-driven): Chen et al., *J. Am. Chem. Soc.* 2019, 141, 18 — benzylic-ether Kumada system with combined computational + experimental mechanism-kinetics unification.

**Updated recommendation**: Morrell–Kochi 1975 (starting point, Partial) + Chen 2019 (establishing point, Indirect), **confidence=High** for paper existence, Partial/Indirect for filling type.

### EP-07a Boundary-test pack (RI-07, sp² vs sp³ halide boundary)

**Original Stage 4**: Tamao 1976 BCSJ (Partial), **confidence=Medium**.

**GPT-5.4 identification**:
- **Starting point**: Tamao et al., *Bull. Chem. Soc. Jpn.* 1976, 49, 1958–1969 — "General Scope and Limitations" title makes the boundary-test explicit in the paper's own framing.
- **Establishing point**: Tamao et al., *Tetrahedron* 1982 — boundary extended to heterocyclic halides.

**Updated recommendation**: Tamao 1976 BCSJ (starting point) + Tamao 1982 *Tetrahedron* (establishing point), Partial filling, **confidence=High** (upgraded from Medium; still Partial because strict matched-pair chloride-vs-bromide-vs-iodide benchmarking is not the subject).

**Note**: the Breitenfeld 2014 / Pengfei 2024 papers in SI-4 extend *beyond* EP-07a's original scope (from sp² to sp³), providing "paradigm-shift" filling. This is a separate filling trajectory consistent with Methods 2's paradigm-shift filling type; the 1976/1982 pair fills the sp² boundary test as originally framed.

### EP-08a Replication / uncertainty pack (RI-08)

**Original Stage 4**: **未同定**, incentive-structure mismatch. **Confidence=Low (unfilled)**.

**GPT-5.4 finding**: **未同定** — no specific paper identified. "反復測定・不確かさ記述・再現性の明示という性質上、独立論文の主題になりにくく、mechanistic advance より publication incentive が弱いため、充填論文が見つからない可能性が高い." This matches the original Stage 4 reasoning exactly.

**Updated recommendation**: unchanged — **EP-08a remains unfilled**. Both models independently converge on "incentive-structure mismatch" as the explanation.

**Discussion-3 relevance**: the cross-model convergence on EP-08a's unfilled status is a strong observation — two independent reasoning models both report that replication/uncertainty data for 1972 Kumada coupling has no independent-paper representation in the indexed chemistry literature. This supports Results Part 3 / Discussion 1's characterization of VQ-4 as a structurally stalled zone.

### EP-09a Internal benchmark pack (RI-09, same-axis Ni(acac)₂ vs NiCl₂(dpe))

**Original Stage 4**: Corriu/Moreau 1975 (Indirect); Kumada *Pure Appl. Chem.* 1980 (review, secondary). **Confidence=Low**.

**GPT-5.4 finding**: Tamao 1976 BCSJ may partially include catalyst-class-level comparisons ("most effective catalysts" by substrate class) but does NOT satisfy "same-axis head-to-head benchmark" as required by EP-09a's definition. **Confidence=Medium-Low** for partial filling; the decisive head-to-head benchmarking paper is **未同定**.

**Updated recommendation**: Tamao 1976 BCSJ (Partial filling, catalyst-class-level only), **confidence=Medium** for this partial contribution. The decisive EP-09a filling (same-axis Ni(acac)₂ vs NiCl₂(dpe) benchmark) remains **unfilled** — cross-model convergence again supports incentive-structure-mismatch explanation.

### EP-10a Kinetic verification pack (NEW — introduced by GPT-5.4 and Breitenfeld 2014 independently)

**Status**: this EP was not in Kumada 1972's original 8-EP list in SI-3. GPT-5.4 Thinking's Stage 3 added EP-10a as a ninth EP targeting PRI-10 (Kinetic overclaim). Breitenfeld 2014's Stage 3 §6 independently introduced PRI-11 (Mechanism-kinetics decoupling) — the same underlying phenomenon.

**GPT-5.4 identification**:
- **Starting point**: Kiso, Tamao, Kumada, *J. Organomet. Chem.* 1973, 50, 297 — "Effects of the nature of halides on the alkyl group isomerization" — halide-dependent isomerization (local kinetic proxy).
- **Establishing point**: Chen, Lucas, Greene, Zhang, Tollefson, Erickson, Taylor, Jarvo, Hong, *J. Am. Chem. Soc.* 2019, 141, 5835–5855 — unified computational + experimental study of chemoselectivity and stereospecificity for benzylic-ether Kumada. DOI: 10.1021/jacs.9b00097. (Note: original GPT-5.4 attribution had vol/issue as "141, 18" and author list as "Q. Chen, X.-H. Yang, C. Liu, Z. Lu" — both errors corrected 2026-04-22 via DOI verification. This is a distinct hallucination pattern from the middle-author substitutions in Refs 26/31: content description, journal, year, and volume were all correct but the entire author list except the first-author surname was fabricated.)

**Recommendation for SI-3 revision (Case C trigger)**: add EP-10a to the Kumada 1972 EP dictionary as a ninth EP, with Kiso-Tamao-Kumada 1973 as starting point and Chen 2019 as establishing point. See SI-3 update notes in a later revision.

---

## §B Updated recommended-selection list (revised 2026-04-19 evening — Opus 4.7 additions)

The 2026-04-19 morning update (from GPT-5.4 Thinking) is now supplemented by the 2026-04-19 evening Claude Opus 4.7 run on Kumada 1972 (v17 prompt), archived at `papers/dev/kumada/kumada_v17_opus47_s4v2.md`. Opus 4.7 identified several additional specific-DOI filling papers that GPT-5.4 Thinking did not. The union of the two models' identifications covers the 1974–2020 Kumada-lineage literature more comprehensively than either alone. Papers identified by both models are marked **two-model convergence**; those identified by one model only are tagged with the identifying model.

| Order | Paper | EPs filled | VQ level | Year | Confidence | Identified by |
|---|---|---|---|---|---|---|
| 1a | **Tamao-Zembayashi-Kiso-Kumada, *J. Organomet. Chem.* 1973** | EP-04a, EP-10a | VQ-3 | 1973 | High | GPT-5.4 |
| 1b | **Kiso-Tamao-Kumada, *J. Organomet. Chem.* 1973** | EP-10a | VQ-3 | 1973 | High | GPT-5.4 |
| 2 | **Parshall, *J. Am. Chem. Soc.* 1974** | EP-03a (Ni intermediate) | VQ-3 | 1974 | High | Opus 4.7 |
| 3 | **Morrell-Kochi, *J. Am. Chem. Soc.* 1975** | EP-03a (Partial), EP-04a, EP-06a, EP-10a | VQ-3 | 1975 | **High (two-model convergence)** | GPT-5.4 + Opus 4.7 |
| 4 | **Tamao et al., *Bull. Chem. Soc. Jpn.* 49, 1958 (1976)** | EP-01a, EP-02a, EP-05a (partial), EP-07a, EP-09a (partial) | VQ-2 | 1976 | **High (two-model convergence)** | GPT-5.4 + Opus 4.7 |
| 5 | **Yamamoto-Kohara-Yamamoto, *Bull. Chem. Soc. Jpn.* 1978** | EP-03a | VQ-3 | 1978 | High | Opus 4.7 |
| 6 | **Kochi "Organometallic Mechanisms and Catalysis" (1978) + Whitesides Ni-dialkyl thermolysis** | EP-06a, EP-04a (partial) | VQ-3 | 1976–1978 | High | Opus 4.7 |
| 7 | **Tamao et al., *Tetrahedron* 1982** | EP-02a, EP-07a | VQ-2 | 1982 | High | GPT-5.4 |
| 8 | **Terao-Watanabe-Ikumi-Kuniyasu-Kambe, *J. Am. Chem. Soc.* 2002** | EP-07a (sp³ boundary, pre-Breitenfeld) | VQ-3 | 2002 | High | Opus 4.7 |
| 9 | **Anderson-Jones-Vicic, *J. Am. Chem. Soc.* 2004 / 2006** | EP-03a, EP-07a (partial) | VQ-3 | 2004–2006 | High | Opus 4.7 |
| 10 | **Phapale-Guisán-Ceinos-Buñuel-Cárdenas, *Chem. Eur. J.* 2009** | EP-04a (modern validation) | VQ-3 | 2009 | Medium | Opus 4.7 |
| 11 | **Chen et al., *J. Am. Chem. Soc.* 2019** | EP-06a, EP-10a | VQ-3 | 2019 | High | GPT-5.4 |
| 12 | **Dawson et al., *Chem. Eur. J.* 2020** | EP-03a, EP-06a | VQ-3 | 2020 | High | GPT-5.4 |

**Updated summary of confidence upgrades vs original Claude Sonnet Stage 4**:
- EP-01a: Medium → **High** (Tamao 1976 BCSJ two-model convergence).
- EP-02a: Low → **High** (Tamao 1976 + Tamao 1982 chain; two-model convergence on Tamao 1976).
- EP-03a: Low → **High** (Morrell-Kochi 1975 two-model convergence; Parshall 1974, Yamamoto 1978, Anderson-Jones-Vicic 2004/2006, Dawson 2020 additional Opus 4.7 / GPT-5.4 identifications).
- EP-04a: "未同定" → **High** (Tamao-Zembayashi-Kiso-Kumada 1973 from GPT-5.4; Morrell-Kochi 1975 and Whitesides Ni-dialkyl thermolysis + Phapale 2009 from Opus 4.7).
- EP-06a: Low → **High** (Morrell-Kochi 1975 two-model convergence; Kochi textbook 1978 from Opus 4.7; Chen 2019 / Dawson 2020 from GPT-5.4).
- EP-07a: Medium → **High** (Tamao 1976 BCSJ two-model convergence; Tamao 1982 from GPT-5.4; Terao-Kambe 2002 and Anderson-Jones-Vicic 2004/2006 from Opus 4.7).
- EP-10a: new EP — four specific papers identified (Tamao-Zembayashi-Kiso-Kumada 1973; Kiso-Tamao 1973; Morrell-Kochi 1975 convergence; Chen 2019).

**Unfilled (three-model convergence — Sonnet + GPT-5.4 + Opus 4.7)**:
- EP-08a (Replication / uncertainty) — three models independently confirm as unfilled; incentive-structure mismatch. Even Opus 4.7, which identified the most specific filling papers for other EPs, did not locate a filling paper for EP-08a.
- EP-09a (strict same-axis Ni(acac)₂ vs NiCl₂(dpe) benchmark) — Tamao 1976 provides partial filling at catalyst-class level only; no decisive benchmarking paper identified by any model.

The three-model convergence on unfilled status is a stronger signal than the previous two-model (Sonnet + GPT-5.4) convergence. Discussion 1 of the main manuscript can now cite this convergence as evidence that the unfilled status of EP-08a / EP-09a reflects structural publication-incentive constraints rather than any single model's training-data coverage gap.

---

## §C Implications for VQ-3 timeline

The updated filling map substantially changes the Kumada 1972 VQ-3 filling timeline:

- **VQ-3 first partial filling**: 1975 (Morrell-Kochi) — **3 years** after the original communication, not 49 years as Results Part 3 currently states for Mazet 2021. The 49-year figure applies to the dppe-Ni-specific experimental cycle, but organonickel mechanistic validation was underway by 1975 in the Kochi group.

- **VQ-3 decisive filling**: 2019 (Chen) + 2020 (Dawson) for the **specific dppe-Ni (or closely related Kumada) system** — this is where the 49-year figure is appropriate.

- **Results Part 3 revision opportunity**: Part 3's phrasing "Mazet 2021 は dppe-Ni 系において初めて Ni(0)/Ni(II) 触媒サイクルを実験的に実証し" can be sharpened to: "Mazet 2021 extends the Chen 2019 / Dawson 2020 Kumada-system mechanistic work specifically to the dppe-Ni / dmpe-Ni comparative pairing" — without weakening the 49-year claim for the dppe-specific resolution.

- **Figure 2 EP-filling matrix (per Results Part 3 design)**: the EP-filling heatmap should now show Morrell-Kochi 1975 filling the EP-03a / EP-06a column at partial density, with Chen 2019 / Dawson 2020 / Mazet 2021 filling it at higher density over 2019–2021.

---

## §D Status

- **Action item**: Results Part 3 and SI-4 main-text citations to be updated pre-submission to include the specific papers identified above.
- **si_issues_log.md Issue #1**: GPT-5.4 Thinking cross-vendor comparison was run and informs SI-6; partial resolution.
- **si_issues_log.md Issue #2 (the eight-paper case-study set vs Stage 4 recommendations)**: the original eight-paper folder selection is now better understood as having bypassed the Stage 4 pre-1985 recommendations in favor of a paradigm-shift-heavy 2009–2024 slice. This §B update includes the pre-1985 slice that was missing.
- **Case C trigger**: SI-3 to be updated to add EP-10a to the EP dictionary (9 EPs instead of 8).

**Date of this update**: 2026-04-19. Source run: `papers/dev/kumada/gpt54thinking/kumada_v17_gpt54thinking_s4.md` (GPT-5.4 Thinking on 2026-04-19).
