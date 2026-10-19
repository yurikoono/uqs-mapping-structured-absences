prompt_version: stage2f-v6-20260329

group: ALL — 統合分析 (Integrated 2F)
input: G1 (Kumada 1972, Kumada 1976b, Mazet 2021), G2 (Kumada 1972, Breitenfeld 2014, Cherney 2015, Pengfei 2024), G3 (Kumada 1972, Monnereau 2009, Molander 2016, Morken 2016)
papers covered: 9 total — Kumada 1972 (original), Kumada 1976b, Mazet 2021, Breitenfeld 2014, Cherney 2015, Pengfei 2024, Monnereau 2009, Molander 2016, Morken 2016
model_info: claude-opus-4-6

---

[F] Integrated Within-Group Comparison

---

## Recurring patterns across all subgroups

### Cross-subgroup recurring_roots

**CRR-1: Ni catalytic cycle proposed without direct observation of key intermediates**

This root appears in every subgroup and in every paper that proposes a mechanism (8 of 9 papers; Cherney 2015, as a review, inherits mechanisms from cited works).

| Subgroup | Papers | Root manifestation |
|----------|--------|-------------------|
| G1 | Kumada 1972, Kumada 1976b, Mazet 2021 | Ni(0)/Ni(II) cycle from analogy (1972/1976); partially characterized but dmpe resting state unidentified (2021) |
| G2 | Breitenfeld 2014, Pengfei 2024 | Ni(I)/Ni(III) radical cycles; Figure 8 intermediates unobserved (2014); Path I/II unresolved (2024) |
| G3 | Monnereau 2009, Molander 2016, Morken 2016 | Active species unidentified (2009); no EPR/UV-Vis for NiI/NiIII (2016 Molander); Ni oxidation state unspecified (2016 Morken) |

**Temporal trajectory**: The gap narrows but never closes. From pure analogy (1972) through partial intermediate characterization (Mazet 2021) to DFT-supported proposals (2014–2024), the evidential basis improves, but no paper in the corpus achieves full catalytic cycle validation under catalytic conditions. The 2016–2024 papers have access to EPR, in situ IR, XANES, and transient absorption spectroscopy, yet none deploys these tools for the specific catalytic system under study. The gap's character shifts from **structurally suppressed** (1972: tools unavailable) to **individually chosen** (2016–2024: tools available, not applied).

---

**CRR-2: Selectivity/yield claims without quantitative mass balance or byproduct accounting**

Present in all three subgroups and in every original research paper.

| Subgroup | Papers | Root manifestation |
|----------|--------|-------------------|
| G1 | Kumada 1972 (B-1, U-1), Kumada 1976b (B2, B7), Mazet 2021 (B14) | "Selective" in title but R–R unreported (1972); benzene not determined for key entries (1976b); mass balance qualitative (2021) |
| G2 | Breitenfeld 2014 (B-6, B-7), Pengfei 2024 (B-1, B-11, B-12) | Rate constant unreported (2014); >90 substrates with isolated yields only, TEMPO 59% unaccounted (2024) |
| G3 | Monnereau 2009 (B-4), Molander 2016 (B-3, B-11), Morken 2016 (B-1: 44% unaccounted) | <3% homo-coupling without scope-wide verification (2009); no mass balance across scope tables (2016) |

**Temporal trajectory**: This gap is **time-invariant**. From 1972 to 2024, across GC/GLPC/NMR/HPLC analytical eras, no paper in the corpus provides complete mass balance for its scope table. The highest-convergence items across all subgroups share this root: Kumada 1972 B-1 (3/3, all high), Pengfei 2024 B-1 (3/3, all high), Morken 2016 B-1 (3/3, all high). This is a **field-wide norm**, not a paper-specific or era-specific choice.

---

**CRR-3: Competing systems cited without substrate-matched quantitative comparison**

Present in all three subgroups. Every paper in the corpus positions itself against prior art without performing a head-to-head experiment.

**Temporal trajectory**: Also **time-invariant**. Kumada 1972 does not compare to Tamura-Kochi; Pengfei 2024 does not compare to Lin eXEC; Morken 2016 does not compare to Fu/Nakamura. The convention of asserting rather than demonstrating superiority persists regardless of field maturity.

---

**CRR-4: Self-contradictory absence — proposed mechanisms generate untested predictions**

Present in all three subgroups as a recurring U-item pattern.

| Subgroup | Papers | Specific instances |
|----------|--------|-------------------|
| G1 | Kumada 1972 (U-1, U-2), Kumada 1976b (U1, U2), Mazet 2021 (U1, U3) | R–R predicted but unreported; MgXX' uncharacterized; stoichiometric experiment consistent with statistical scrambling |
| G2 | Breitenfeld 2014 (U-1, U-2), Pengfei 2024 (U-1, U-2) | Rate law not derived algebraically; DFT-SWV 360 mV discrepancy undiscussed |
| G3 | Monnereau 2009 (U-1, U-2, U-3), Molander 2016 (U-1, U-2, U-3, U-6), Morken 2016 (U-1, U-3, U-4) | TOF denominator contradicted by own data; RE retention assumed without test; no intermediate observed despite cycle prediction |

**Temporal trajectory**: This pattern is **structurally invariant**. Each paper proposes a mechanism, that mechanism predicts specific observables, and those observables go untested. This is arguably the most analytically significant pattern in the corpus: it suggests that the function of a catalytic cycle diagram in synthetic methodology papers is **narrative** (providing a mechanistic rationale that contextualizes the scope data) rather than **predictive** (generating testable hypotheses that constrain future experiments).

---

### Recurring U-items across subgroups

```
recurring_U: Self-contradictory absence between proposed mechanism and untested predictions | papers: all 8 original research papers | note: This is the single most recurrent U-pattern in the 9-paper corpus. Its universality across 7 research groups, 4 journals, 3 activation modes (thermal, photoredox, electrochemical), and 52 years suggests it is an intrinsic feature of synthetic methodology publication, not a gap specific to any paradigm or era. The A/B/C classification framework captures what is absent (B) and what is deferred (A) but does not have a dedicated category for [REDACTED: substantial verbatim quotation; see Tier 9] This may represent a genuine limitation of the classification framework — or it may represent a deliberate feature, given that testing mechanism-derived predictions would require a mechanistic paper, not a synthetic methodology paper.
```

---

## VQ hierarchy and EP filling order

### Stage 3 VQ assessment (Kumada 1972)

From Stage 3 (§3):
- **VQ-1 (Observation)**: Passed — Table I observations are valid for known compounds under 1972 norms.
- **VQ-2 (Method)**: Not reached — RI-01 (reporting integrity, SRG-3) and RI-07 (unsupported boundary, SRG-4) unresolved.
- **VQ-3 (Mechanism)**: Not reached — RI-03, RI-04, RI-05, RI-06 unresolved.
- **VQ-4 (Benchmark)**: Not reached — RI-08, RI-09 unresolved.

### EP filling by the 8 充填論文

**EP-01a (Reporting-coherence pack)** — targets SRG-3 / RI-01
- Kumada 1976b **partially fills**: GLPC conditions partially specified (column, stationary phase stated; temperature/carrier gas absent); reaction times for scope entries absent; internal standard identity inconsistent (B9). Partial fill — SRG-3 narrowed but not closed.
- Other papers: Do not address Kumada 1972's specific analytical gaps.
- **Status**: Partially filled by Kumada 1976b. VQ-2 gate: RI-01 remains open.

**EP-03a (Direct-observation / state-assignment pack)** — targets SRG-1 / RI-03
- Mazet 2021 **substantially fills**: Independent synthesis of Ni(0)-butadiene (6c/6d), OA complexes (7c/7d, 9c), product-bound Ni(0) (11c) with NMR and X-ray characterization. However, the dmpe resting state is unidentified (B8), and the dppe-Ni system studied differs from Kumada 1972's dpe-Ni. **Partial fill**: intermediates characterized in a related but non-identical system.
- Breitenfeld 2014: DFT-only; no experimental intermediate characterization. **No fill**.
- **Status**: Partially filled by Mazet 2021. RI-03 reduced but not eliminated for the specific dpe-Ni system.

**EP-04a (Discrimination / replication pack)** — targets SRG-2 / RI-04
- Kumada 1976b **partially fills**: Benzene (homo-coupling index) quantified for some Table 3 entries (3–9%) but absent for others (B7). Selectivity partially characterized but mass balance still incomplete.
- Morken 2016: Radical clock experiment (44% unaccounted, U-1); stereospecificity experiment (RE retention assumed, U-3). **Fills a different dimension**: stereochemical discrimination, not cross/homo selectivity.
- **Status**: Partially filled. RI-04 remains open for Kumada 1972's specific selectivity claim.

**EP-05a (Quantitative-ranking substantiation pack)** — targets SRG-5 / RI-05
- Kumada 1976b **partially fills**: Expanded catalyst survey (Tables 1, 6) with dppp, dppe, dmpe, PPh₃ etc., but activity data still qualitative for most catalysts (B3 in Kumada 1976b).
- Monnereau 2009 **provides one data point**: Complex 2 vs dppp at one substrate/condition (B-5). Insufficient for multi-variable deconvolution.
- **Status**: Partially filled. RI-05 remains open.

**EP-06a (Analogy-validation pack)** — targets SRG-1 / RI-06
- Kumada 1976b: Scheme 1 still based on same external analogies (refs 30–32, C3). **No fill**.
- Mazet 2021: Stoichiometric experiments within a dppe-Ni system **partially validate** the analogy for dppe (not dpe). **Partial fill for the dpe→dppe analogy direction**.
- **Status**: Partially filled by Mazet 2021. The original dpe-Ni analogy from dipy-Ni remains unvalidated.

**EP-07a (Boundary-test pack)** — targets SRG-4 / RI-07
- Kumada 1976b **partially fills**: Scope extended to ~60 entries but "Only Csp² halides" restriction maintained; dihaloethylene limitation named but not quantified (B2).
- Breitenfeld 2014, Pengfei 2024 **fill the sp³ boundary**: Both demonstrate Ni-catalyzed sp³ cross-coupling, showing that the original sp² boundary was a limitation of Kumada 1972's specific catalyst system, not an intrinsic limitation of Ni catalysis.
- Cherney 2015 **documents the boundary crossing**: Review covers enantioselective sp³ coupling methods.
- Morken 2016 **fills with non-halide electrophile**: Cyclic sulfates as C(sp³) electrophiles.
- **Status**: Substantially filled. The original "Only Csp² halides" boundary has been demonstrated to be system-specific rather than fundamental.

**EP-08a (Replication / uncertainty pack)** — targets SRG-2, SRG-6 / RI-08
- No paper in the corpus provides replicate measurements with uncertainty estimates for Kumada 1972's specific system. Morken 2016 reports "average of two experiments" (B-7) but without individual values or SD.
- **Status**: Not filled. RI-08 remains open across the entire corpus.

**EP-09a (Internal benchmark pack)** — targets SRG-2, SRG-4, CLA-1, CLA-2 / RI-09
- No paper in the corpus performs a substrate-matched comparison between NiCl₂(dpe) and Tamura-Kochi Fe/Cu or Corriu/Masse Ni(acac)₂.
- Kumada 1976b compares NiCl₂(dppp) to NiCl₂(dppe) internally but not to external prior art.
- **Status**: Not filled. RI-09 remains open.

### VQ advancement summary

| VQ Level | Pre-EP Status | Post-EP Status | Key remaining gaps |
|----------|--------------|----------------|-------------------|
| VQ-1 | Passed | Passed | — |
| VQ-2 | Not reached | Partially advanced | RI-01 narrowed (Kumada 1976b); RI-07 substantially filled (G2 papers). Still not formally reached: RI-01 not fully closed. |
| VQ-3 | Not reached | Partially advanced | RI-03 partially filled (Mazet 2021 for dppe); RI-06 partially filled (Mazet 2021). RI-04, RI-05 still open. |
| VQ-4 | Not reached | Not advanced | RI-08 and RI-09 remain fully open. No paper in the corpus provides replicate data or matched-pair benchmarks for the original system. |

---

## Cross-subgroup independently emerging patterns

Three patterns emerged independently in multiple subgroups without being seeded by the original Kumada 1972 analysis:

**1. DFT as unvalidated mechanistic discriminant** (G2: RP-4, G3: RP-1 partial)
- Breitenfeld 2014 (DFT sole discriminant between bimetallic OA and escape-rebound)
- Pengfei 2024 (DFT potentials 360 mV from SWV)
- Molander 2016 (DFT DKR model on benzyl radical, extrapolated to unactivated alkyl)
- Monnereau 2009 (PM3 fanning dynamics without kinetic validation)

This pattern was absent in Kumada 1972 (pre-DFT era) and emerges only in post-2009 papers. It is an **era-specific structural gap** reflecting the rapid adoption of DFT in organic chemistry without concurrent development of DFT validation protocols for catalytic systems.

**2. Scope failures described qualitatively without quantitative data or mechanistic diagnosis** (G2: within divergences, G3: RP-5)
- Kumada 1972: sp³ restriction without stating whether tested (B-5)
- Monnereau 2009: Bromomesitylene 15.6% without attribution (B-12)
- Molander 2016: Amine-containing silicates fail without diagnosis (B-4)
- Morken 2016: ortho-ArMgBr, alkyl-MgX failures without data (B-4, B-5)
- Pengfei 2024: Condition changes for 2°–2° and 1°–3° without rationale (B-16)

This pattern is **universal**: every scope-oriented paper in the corpus describes failures without quantifying them. It suggests a publication norm where scope tables present only successes, with failures relegated to qualitative footnotes.

**3. MgX₂ byproduct effects unaddressed** (G1: DV-3, G3: Morken 2016 SRG-6)
- Kumada 1972: not discussed
- Kumada 1976b: MgXX' predicted by stoichiometry but never characterized (U1)
- Mazet 2021: MgBr₂ not discussed despite VTNA analysis where salt effects could confound
- Morken 2016: MgBr₂ directly reacts with cyclic sulfate substrate; aging protocol developed but not validated (B-11)

This pattern spans 44 years and multiple research groups. MgBr₂ is generated stoichiometrically in every Grignard cross-coupling, yet its catalytic, inhibitory, or side-reaction effects are essentially never characterized under catalytic conditions.

---

## Integrated group_unasked_question

[REDACTED: substantial verbatim quotation; see Tier 9]

This question integrates the three cross-subgroup recurring roots:
- **CRR-1** (active species uncharacterized): no paper identifies the active Ni species under catalytic conditions.
- **CRR-2** (mass balance absent): no paper provides complete mass balance for its scope table.
- **CRR-4** (untested predictions): every paper proposes a mechanism that predicts outcomes it does not test.

The question is simultaneously the group-level unasked question of G1 ("selectivity + mechanism for dpe-Ni"), G2 ("rate law for cross/homo selectivity across mechanistic manifolds"), and G3 ("active species identity across catalyst variants"). Its integration reveals that the three questions are not independent — they are three facets of a single unsolved problem: **the complete quantitative description of a Ni-catalyzed cross-coupling reaction, from catalyst speciation through rate law to product distribution**.

```
evidence_chain: Kumada_1972 : B-1 (selectivity unquantified), B-2 (cycle unvalidated); Kumada_1976b : A2 (mechanism deferred), U1 (MgXX' uncharacterized); Mazet_2021 : B8 (dmpe resting state unidentified), B1 (VTNA unreliable); Breitenfeld_2014 : U-2 (rate law not derived); Cherney_2015 : B-1 (DYKAT krac/kproductive absent); Pengfei_2024 : B-3 (selectivity in SI), U-1 (Path I/II unresolved); Monnereau_2009 : U-1 (TOF denominator contradicted), U-2 (Ni oxidation state unknown); Molander_2016 : U-2 (NiI/NiIII unassigned); Morken_2016 : B-3 (Ni species uncharacterized), U-4 (no intermediate observed)
```

### Correspondence to Stage 3 §5 EP ordering

The Stage 3 analysis identified EP-01a → EP-07a → EP-06a → EP-04a → EP-03a → EP-05a → EP-09a → EP-08a as the optimal filling order. The integrated 2F reveals the following filling landscape:

- **EP-07a (Boundary test)**: **Most filled**. G2 papers collectively demonstrate that Kumada 1972's sp² boundary was system-specific. Breitenfeld 2014, Cherney 2015, Pengfei 2024, and Morken 2016 all operate beyond this boundary.
- **EP-06a / EP-03a (Analogy validation / Direct observation)**: **Partially filled**. Mazet 2021 provides the most substantial intermediate characterization in the corpus, but for dppe-Ni rather than dpe-Ni.
- **EP-01a (Reporting coherence)**: **Minimally filled**. Kumada 1976b partially addresses but does not close the analytical reporting gaps.
- **EP-04a / EP-05a (Discrimination / Ranking)**: **Weakly filled**. Partial byproduct data (Kumada 1976b) and partial catalyst comparison (Monnereau 2009) exist but are insufficient.
- **EP-08a / EP-09a (Replication / Benchmark)**: **Not filled**. No paper in the corpus provides replicate measurements or matched-pair comparisons for Kumada 1972's system.

The filling pattern is **inverted relative to the VQ hierarchy**: the highest-VQ-level EPs (boundary testing, mechanism) receive the most attention from subsequent work, while the lowest-VQ-level EPs (reporting coherence, replication, benchmarking) are systematically neglected. This inversion reflects the incentive structure of the field: publishing novel boundary-breaking chemistry (G2) and novel mechanisms (G1, G3) is rewarded, while replicating or benchmarking existing systems is not.

---

> **Tier 8 redaction notice**: This file is a redacted copy of the corresponding Tier 3 / Tier 9 output. Verbatim source-paper quotations have been replaced by `[REDACTED: see source paper §<loc>; full text retained in Tier 9 reviewer-only deposit]` markers, preserving location references and our own analytical content. Bibliographic fields (title, authors, journal, year, DOI), analytical labels (`evidence_chain:` with B-/U-/A-/C- internal IDs), short technical terms, and our own analytical text are not redacted. The redaction was applied by `scripts/redact_for_tier8.py` and, for this version, by `scripts/build_paperA_R1_public.py` with `scripts/redact_source_ngram_runs.py` (scripts of the project repository; they are not deposited).
