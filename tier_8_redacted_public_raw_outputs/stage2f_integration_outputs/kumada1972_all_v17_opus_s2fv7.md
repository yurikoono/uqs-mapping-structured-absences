prompt_version: stage2f-v7-20260417

---

**[F. Within-Group Comparison — Integration Mode]**

**Input:** Stage 2F v7 outputs from three sub-groups:
- G1: Direct lineage (kumada1972, kumada1976b, mazet2021) — 3 papers
- G2: Boundary breakthrough (kumada1972, breitenfeld2014, cherney2015, pengfei2024) — 4 papers
- G3: Methodological expansion (kumada1972, monnereau2009, molander2016, morken2016) — 4 papers

**Reference paper:** Kumada 1972 (shared across all three sub-groups)
**Stage 3 output available:** kumada1972_v17_sonnet_s3.md (VQ/RI/EP analysis)

**Total unique papers across sub-groups:** 9 (kumada1972, kumada1976b, mazet2021, breitenfeld2014, cherney2015, pengfei2024, monnereau2009, molander2016, morken2016)

---

**Patterns that emerged independently in multiple sub-groups**

The following patterns were identified independently in all three sub-groups without being seeded by the shared reference paper (Kumada 1972). Their independent emergence across sub-groups with different thematic foci (lineage, boundary, expansion) is the strongest evidence for field-wide structural conventions.

**IP-1: Catalytic cycle proposed without elementary step validation**

- G1: RP-1 (Kumada 1972 + 1976b + Mazet 2021 — spanning 49 years of the same catalyst system)
- G2: RP-1 (Kumada 1972 + Breitenfeld 2014 + Cherney 2015 + Pengfei 2024 — spanning paradigm shift from 2-electron to radical)
- G3: RP-1 (Kumada 1972 + Monnereau 2009 + Molander 2016 + Morken 2016 — spanning ligand design, photoredox, and asymmetric catalysis)

This pattern appears in all 9 papers across all paradigms (2-electron Ni(0)/Ni(II), radical Ni(I)/Ni(III), photoredox/Ni, electrochemical SET), all formats (communication, full paper, review, Account), and all journals (JACS, BCSJ, ACS Catal., Organometallics, Chem. Rev., Nature Catalysis, Adv. Synth. Catal., Acc. Chem. Res.). It is the single most universally recurring pattern in the corpus.

**IP-2: Quantitative analytical basis for primary data underreported**

- G1: RP-2 (glpc → partial GLPC → VTNA without statistical rigor)
- G2: RP-2 (glpc → rate orders without statistics → isolated yields without conversion)
- G3: RP-2 (glpc → GC without response factors → scope yields without replicates → SFC without method)

This pattern appears in all 9 papers. The specific analytical instrument changes (glpc → GC → VTNA → SFC → CV) but the structural gap (measurement conditions insufficient for independent replication) is invariant.

**IP-3: Self-contradictory absence — model predicts observables that are not tested**

- G1: RP-4 (R–R untested → β-elimination contradiction → VTNA unreliable but conclusions drawn)
- G2: RP-4 (R–R → intermediates 10–16 unobserved → DET conversion-ee untested → DFT/SWV discrepancy)
- G3: RP-3 (R–R → TOF denominator contradiction → NiIII unobserved → RE retention assumed)

This pattern appears in all 9 papers as U-items. Its universal recurrence across sub-groups confirms the G1/G2/G3 assessments that this is a genre convention rather than an individually chosen gap.

**IP-4: Benchmark superiority asserted without matched-pair comparison**

- G1: not prominently recurring (G1 papers are lineage rather than competitive)
- G2: RP-5 (selectivity claims without mass balance, plus Dropped Quantitative Benchmark in all 3 experimental papers)
- G3: RP-4 (every paper claims improvement without common-substrate comparison)

This pattern appears in at least 7 of 9 papers. G1's mazet2021 is partially exempt because it is a mechanistic study rather than a methodology paper, but even mazet2021's S2 positions itself against prior mechanistic studies without direct comparison.

---

**Cross-referencing recurring_roots across sub-groups**

| Recurring root | G1 | G2 | G3 | Field-wide? |
|---|---|---|---|---|
| Catalytic cycle from analogy, not validated | Yes (all 3 papers) | Yes (3/4 papers) | Yes (all 4 papers) | **Field-wide** |
| Quantitative measurement underreported | Yes (all 3 papers) | Yes (all 4 papers) | Yes (all 4 papers) | **Field-wide** |
| Selectivity without mass balance | Yes (1972, 1976b) | Yes (1972, 2024) | Partial (1972) | **Field-wide** (methodology papers) |
| Benchmark asserted, not verified | Partial | Yes (all 4) | Yes (all 4) | **Field-wide** (methodology papers) |
| DFT as sole pathway discriminant | No | Yes (2014, 2024) | Partial (2016 Molander) | **Paradigm-specific** (post-2005 radical mechanism papers) |
| Ligand effect from insufficient data | Yes (1972, 1976b, 2021) | No | Yes (2009) | **Paradigm-specific** (diphosphine ligand papers) |

**Field-wide patterns (independent of paradigm):** IP-1 (cycle validation), IP-2 (analytical underreporting), IP-3 (self-contradictory absence).

**Paradigm-specific patterns:** DFT as discriminant (radical mechanism papers only); ligand effect attribution (diphosphine papers only).

---

**Synthesis of sub-group group_unasked_questions**

**G1 group_unasked_question:** [REDACTED: substantial verbatim quotation; see Tier 9]

**G2 group_unasked_question:** [REDACTED: substantial verbatim quotation; see Tier 9]

**G3 group_unasked_question:** [REDACTED: substantial verbatim quotation; see Tier 9]

**Assessment: Facets of a single problem**

The three sub-group questions are **facets of a single underlying problem**, not independent questions. They can be unified as:

**Unified group_unasked_question:**

[REDACTED: substantial verbatim quotation; see Tier 9]

**Relationship of sub-group questions to the unified question:**
- G1 addresses facet (a) + (b): the complete speciation question for the original dpe-Ni system
- G2 addresses facet (b) + (c): selectivity quantification across the sp²→sp³ paradigm shift
- G3 addresses facet (c): the evidentiary standard for mechanistic discrimination

The unified question is more than the sum of its parts because it identifies a **methodological deficit at the field level**: no single paper in the 9-paper corpus has simultaneously achieved (a), (b), and (c) for any Ni-catalyzed cross-coupling system. Mazet 2021 comes closest — characterizing intermediates (a, partial) and proposing distinct mechanisms for two catalysts (c, partial) — but does not provide complete product distribution (b) and its VTNA data are compromised by decomposition artifacts.

evidence_chain: [Kumada_1972 : B-1 (selectivity w/o byproduct), B-2 (cycle w/o evidence) | Kumada_1976b : A2 (mechanism deferred), B2 (limitation uncharacterized) | Mazet_2021 : B1 (VTNA reliability), B8 (dmpe resting state unidentified) | Breitenfeld_2014 : U-1 (intermediates 10–16 unobserved), U-3 (DFT sole discriminant) | Cherney_2015 : B-1 (DYKAT w/o krac/kproductive) | Pengfei_2024 : B-3 (selectivity model in SI), U-1 (pathway undiscriminated) | Monnereau_2009 : U-1 (TOF denominator incorrect), U-2 (Ni oxidation state unknown) | Molander_2016 : U-1 (quencher unknown), U-2 (NiI/NiIII unobserved) | Morken_2016 : B-3 (Ni oxidation state unspecified), U-4 (intermediates unobserved)]

---

**Cross-reference with Stage 3 EP filling landscape**

The S3 output for Kumada 1972 identifies six SRGs and two CLAs, with EP packs assigned to each. The 2F sub-group analyses allow assessment of whether the EP filling landscape corresponds to the observed filling order across the 8 EP papers.

| S3 EP pack | S3 target (SRG/CLA) | Papers that partially fill this EP | Filling degree | Notes |
|---|---|---|---|---|
| EP-06a (Analogy validation) | SRG-1 (mechanism cycle) | Mazet 2021 (intermediate characterization for dppe); Breitenfeld 2014 (radical mechanism for Nickamine) | Partial | Mazet 2021 fills for dppe system specifically; Breitenfeld fills for a different catalyst. Neither validates the original dpe-Ni system's cycle. |
| EP-03a (Direct observation) | SRG-1 (mechanism cycle) | Mazet 2021 (9c/III-b observed by NMR/X-ray) | Partial | Only dppe system OA complex characterized; dmpe resting state unidentified (B8). |
| EP-04a (Discrimination/replication) | SRG-2 (selectivity claim) | Kumada 1976b (benzene monitored for some Table 3 entries); Pengfei 2024 (homo-coupling in model reaction only) | Minimal | Neither paper provides complete mass balance across the scope. |
| EP-01a (Reporting coherence) | SRG-3 (Table I analytical quality) | Kumada 1976b (GLPC instrument model stated) | Partial | Kumada 1976b improves over 1972 but still lacks calibration and has internal inconsistency (U3: yield > conversion). |
| EP-07a (Boundary test) | SRG-4 (scope restriction) | Breitenfeld 2014, Pengfei 2024 (sp³ coupling achieved) | Substantial | The sp² boundary is completely overcome by radical/electrochemical methods. However, this fills EP-07a by changing the mechanism, not by testing sp³ within the original 2-electron paradigm. |
| EP-05a (Quantitative ranking) | SRG-5 (solvent/condition effects) | Kumada 1976b (Table 5 solvent data) | Partial | THF data provided for some substrates; "definitely" claim partially addressed. |
| EP-09a (Internal benchmark) | CLA-1 (utility) + CLA-2 (Corriu/Masse) | Kumada 1976b (broader scope vs 1972); Monnereau 2009 (dppp benchmark) | Partial | No paper performs the specific Corriu/Masse Ni(acac)₂ vs Kumada NiCl₂(dpe) head-to-head comparison. |
| EP-08a (Replication/uncertainty) | SRG-2 + SRG-6 | Morken 2016 ("average of two experiments") | Minimal | Morken 2016 is the only paper to explicitly state replication (n=2), but without individual values or SD. |

**VQ hierarchy correspondence to filling order:**

The S3 analysis places Kumada 1972 at VQ-1 (Observation) with VQ-2 blocked by RI-01 (reporting integrity, SRG-3) and RI-07 (unsupported boundary, SRG-4).

- **SRG-4 / RI-07 (sp² boundary):** Substantially filled by G2 papers (Breitenfeld 2014, Pengfei 2024) which demonstrate sp³ coupling via radical mechanisms. However, this filling is paradigm-shifting rather than boundary-testing within the original 2-electron paradigm — the sp² boundary was not tested but circumvented.
- **SRG-3 / RI-01 (reporting coherence):** Only partially filled by Kumada 1976b. The 2009–2024 papers do not retroactively improve the 1972 data.
- **SRG-1 / RI-06 (mechanism by analogy):** Partially filled by Mazet 2021 (for dppe system) and by the radical mechanism papers (for different systems). The original dpe-Ni mechanism remains analogically derived 52 years later.
- **SRG-2 / RI-04 (selectivity without byproduct data):** Minimally filled. The mass balance gap is the most persistent across all 9 papers.

**Key observation:** The EP filling order does NOT follow the VQ hierarchy. The VQ-2-blocking RI-07 (sp² boundary) was filled substantially (by paradigm shift), while the equally VQ-2-blocking RI-01 (reporting coherence) was filled only partially. The VQ-3-level RIs (RI-03, RI-06 — mechanism) were partially filled (by Mazet 2021) before VQ-2 was fully resolved. This suggests that the field prioritizes paradigm expansion (RI-07 filling via new mechanisms) over analytical consolidation (RI-01 filling via improved reporting) — consistent with the incentive structure identified in IP-2.

---

**Integrated group_unasked_question**

[REDACTED: substantial verbatim quotation; see Tier 9]

This question integrates the three sub-group questions as follows:
- From G1: the demand for complete speciation and time-resolved product profiles
- From G2: the demand for a quantitative selectivity model spanning sp²→sp³
- From G3: the demand for an agreed evidentiary standard for mechanistic claims

The question is not answered by any paper in the 9-paper corpus. Its persistence across 52 years (1972–2024), 9 papers, 5 paradigms (2-electron, radical, photoredox, electrochemical, asymmetric), and 8 journals constitutes the strongest evidence that it represents a field-wide structural convention — the convention that scope demonstration takes priority over mechanistic proof, and that catalytic cycle proposals serve narrative rather than predictive functions.

evidence_chain: [All 9 papers contribute through their IP-1, IP-2, and IP-3 patterns as documented in G1/G2/G3 analyses]

TEMPERATURE_SUMMARY cross-reference: The strongest convergence items across all sub-groups share a common structure — they are the items where all viewpoints (synthetic, mechanistic, analytical) agree that a gap exists:
- Kumada 1972 B-1 (3/3 convergence) = selectivity without byproduct data
- Kumada 1976b B2 (3/3 convergence) = limitation without product data
- Breitenfeld 2014 B-1 (3/3 convergence) = kinetic measurement validity
- Pengfei 2024 B-1 (3/3 convergence) = isolated yields without mass balance
- Monnereau 2009 B-7 (3/3 convergence) = TOF denominator validity
- Morken 2016 B-1 (3/3 convergence) = radical clock mass balance
- Molander 2016 U-7 (3/3 convergence) = DFT model extrapolation

The 3/3 convergence items across the corpus collectively point to the same unified question: the field has not produced the complete, quantitative, experimentally validated account that the unified question demands.

---

*End of integration output.*

---

> **Tier 8 redaction notice**: This file is a redacted copy of the corresponding Tier 3 / Tier 9 output. Verbatim source-paper quotations have been replaced by `[REDACTED: see source paper §<loc>; full text retained in Tier 9 reviewer-only deposit]` markers, preserving location references and our own analytical content. Bibliographic fields (title, authors, journal, year, DOI), analytical labels (`evidence_chain:` with B-/U-/A-/C- internal IDs), short technical terms, and our own analytical text are not redacted. The redaction was applied by `scripts/redact_for_tier8.py` and, for this version, by `scripts/build_paperA_R1_public.py` with `scripts/redact_source_ngram_runs.py` (scripts of the project repository; they are not deposited).
