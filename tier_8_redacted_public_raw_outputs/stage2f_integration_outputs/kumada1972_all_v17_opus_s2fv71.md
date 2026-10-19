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

**Sub-group-specific findings not subsumed by field-wide patterns**

The following patterns did not rise to field-wide (IP) status but satisfy the preservation criteria: (a) chemically concrete gap, (b) multi-paper persistence within the sub-group, and (c) testable hypothesis lost if absorbed into abstract IP categories.

---

**SSP-1: MgX₂ byproduct fate and catalytic effect (G1 + G3)**

Originating sub-groups: G1 (kumada1972, kumada1976b, mazet2021), G3 (morken2016)

The stoichiometry of every Kumada-type cross-coupling generates one equivalent of MgX₂ (typically MgBrCl or MgCl₂) per catalytic turnover. This species is a Lewis acid capable of (a) coordinating to the Ni catalyst and altering its electronic properties, (b) reacting directly with electrophilic substrates, and (c) affecting the Schlenk equilibrium of the Grignard reagent in solution.

Persistence across papers:
- Kumada 1972: The overall equation predicts MgXX' formation; neither characterized nor mentioned as a variable (implicit in B-2 mechanism).
- Kumada 1976b: U1 explicitly flags MgXX' fate as an uncharacterized prediction of the catalytic stoichiometry. A6 notes that [REDACTED: substantial verbatim quotation; see Tier 9] but this is deferred, not investigated.
- Mazet 2021: D-4-7 of S2 identifies "MgBr₂ byproduct's kinetic role" as an unasked question. The same-excess VTNA experiment attributes non-overlay to "catalyst deactivation and product inhibition" but does not test MgBr₂ addition as a specific inhibitor (B3 in S1).
- Morken 2016: B-11 reports that [REDACTED: substantial verbatim quotation; see Tier 9] — a direct demonstration that MgBr₂ is not inert under reaction conditions. The 15-hour Grignard aging protocol is motivated by MgBr₂ precipitation.

Testable hypothesis: MgBr₂ generated during catalytic turnover acts as a Lewis acid catalyst poison (or activator) whose accumulation over the course of the reaction affects catalyst performance, selectivity, and the reliability of kinetic measurements. This hypothesis is testable by: (i) deliberate addition of 0.5–2.0 equiv MgBr₂ at t=0 and monitoring yield/selectivity/kinetics; (ii) running the reaction with in situ removal of MgBr₂ (e.g., dioxane precipitation) and comparing kinetic profiles.

Why not subsumed by IP-2: IP-2 captures "analytical basis underreported" as a structural category. The MgBr₂ question is not about analytical reporting quality — it is about a specific chemical species whose reactivity has been demonstrated (Morken 2016, B-11) but whose catalytic role has never been quantified in any Kumada coupling. A paper that fully addresses IP-2 (perfect analytical reporting) would still not answer whether MgBr₂ affects catalysis.

evidence_chain: [Kumada_1976b : U1, A6 | Mazet_2021 : B3 (same-excess non-overlay), D-4-7 | Morken_2016 : B-11 (MgBr₂ + cyclic sulfate direct reaction)]

---

**SSP-2: Homogeneous vs heterogeneous catalysis — the "black mixture" question (G1)**

Originating sub-group: G1 (kumada1972, kumada1976b)

Kumada 1972 reports [REDACTED: substantial verbatim quotation; see Tier 9] (B-10, U-2). A black reaction mixture is consistent with Ni(0) nanoparticle formation. The paper proposes a homogeneous Ni(0)/Ni(II) molecular cycle but does not perform any test to distinguish homogeneous from heterogeneous catalysis (mercury-drop test, filtration hot test, TEM). Kumada 1976b does not revisit this observation despite being the comprehensive scope paper.

Persistence: This specific question (is the active species molecular Ni or colloidal Ni?) persists in G1 across the 1972 and 1976b papers. By 2021 (Mazet), the question is not directly raised because the Mazet system uses a different precatalyst and characterizes intermediates spectroscopically, but the dmpe system's unidentified resting state (B8) leaves open whether the active species in that system is molecular.

In G3, Monnereau 2009 observes ~25% residual activity for ligand-free [NiCp(COD)]BF₄ (B-9, U-4), which is consistent with nanoparticle catalysis. No mercury-drop or TEMPO inhibition test is reported.

Testable hypothesis: The catalytic activity in early Kumada coupling reactions (1972, 1976b) may be partially or wholly attributable to Ni(0) nanoparticles rather than the proposed homogeneous molecular cycle. This would fundamentally change the mechanistic interpretation of the ligand activity order (B-3 in 1972, A4/A5 in 1976b) because nanoparticle catalysis has different ligand-dependence properties.

Why not subsumed by IP-1: IP-1 captures "catalytic cycle proposed without elementary step validation." The homogeneous/heterogeneous question is a precondition to IP-1 — if the catalysis is heterogeneous, the entire molecular cycle is irrelevant, not merely unvalidated. A paper that fully addresses IP-1 (validates all elementary steps of a homogeneous cycle) would simultaneously answer this question, but the converse is not true: demonstrating heterogeneous catalysis would not validate any molecular cycle. The question is logically prior to, not contained within, IP-1.

evidence_chain: [Kumada_1972 : B-10, U-2 (black mixture) | Monnereau_2009 : B-9, U-4 (ligand-free Ni residual activity)]

---

**SSP-3: E/Z selectivity origin in dpe-Ni vinyl halide coupling (G1)**

Originating sub-group: G1 (kumada1972, kumada1976b, mazet2021)

Kumada 1972 reports that both cis- and trans-1,2-dichloroethylene give [REDACTED: verbatim source quotation; see the source paper via its DOI]). Kumada 1976b reports E/Z selectivity data for vinyl halide coupling in Table 7 but provides no mechanistic interpretation. Mazet 2021 observes temperature-dependent and catalyst-dependent E/Z reversal (A1, B12: 4a gives E/Z 75:25 at 23°C; 4b gives E/Z 40:60 at 23°C → 04:96 at 40°C) in a related Ni-diphosphine system.

Persistence: The E/Z question spans all three G1 papers (49 years) without resolution. It constitutes G1 SRG-5 in Mazet 2021 and SRG-6 in Kumada 1972.

Testable hypothesis: The E/Z selectivity is kinetically controlled and determined at the reductive elimination step, where the geometry of the bis-vinyl Ni(II) intermediate (cis vs trans arrangement of vinyl groups) depends on the diphosphine bite angle. This predicts that (i) E/Z ratio should be temperature-dependent (kinetic control → Eyring analysis should show different ΔH‡ and ΔS‡ for cis and trans RE pathways), and (ii) E/Z ratio should correlate with the ligand bite angle across a series of diphosphines.

Why not subsumed by IP-1 or IP-3: IP-1 captures the general pattern of unvalidated catalytic cycles. IP-3 captures self-contradictory absence. The E/Z selectivity question is not about the cycle's validity — it is about a specific stereochemical outcome (cis-enrichment) that has been observed, documented, and deferred across 49 years. It has independent synthetic value: controlling E/Z selectivity in vinyl-vinyl coupling is a practical synthetic problem. Absorption into IP-1 or IP-3 would lose the chemical specificity of "why is cis-stilbene anomalously enriched?"

evidence_chain: [Kumada_1972 : A-1, B-11, U-3 (SRG-6) | Mazet_2021 : A1, B12 (SRG-5)]

---

**SSP-4: β-Hydride elimination suppression claim contradicted by isomerization (G1)**

Originating sub-group: G1 (kumada1976b)

Kumada 1976b claims β-hydride elimination is generally suppressed in Ni-alkyl intermediates (A8), attributing this to phosphine and Mg moiety effects (A6). However, the same paper reports [REDACTED: substantial verbatim quotation; see Tier 9] with [Ni(dmpe)Cl₂] (U2), which mechanistically requires β-hydride elimination/reinsertion. The paper treats both claims as independent observations without acknowledging their contradiction.

Persistence: This contradiction is unique to Kumada 1976b and does not recur verbatim in other papers. However, the underlying question — [REDACTED: substantial verbatim quotation; see Tier 9] — is relevant to all sp³ coupling papers in G2 (Breitenfeld 2014, Pengfei 2024) where radical pathways are invoked partly to avoid β-hydride elimination problems.

Testable hypothesis: β-Hydride elimination suppression in Ni-diphosphine cross-coupling is not a general feature but is condition-specific, with suppression depending on the diphosphine bite angle, the alkyl group structure, and the Ni oxidation state. With dmpe (small bite angle, strong σ-donor), Ni-alkyl intermediates have sufficient lifetime for β-hydride elimination/reinsertion; with dppp (larger bite angle), reductive elimination outcompetes β-elimination. This predicts a quantitative competition between RE and β-HE rates as a function of ligand parameters.

Why not subsumed by IP-1: IP-1 captures unvalidated catalytic cycles. The β-elimination/isomerization contradiction is about the validity of a specific mechanistic claim (suppression) within the cycle, not about the cycle's overall validation. Resolving IP-1 would not automatically resolve whether β-elimination is suppressed or operative under specific conditions.

evidence_chain: [Kumada_1976b : A8 (β-suppression claim), U2 (isomerization contradicts), A5 (dmpe anomaly)]

---

**SSP-5: DKR kinetic ordering (khomolysis >> kRE) untested for non-benzylic substrates (G2 + G3)**

Originating sub-groups: G2 (cherney2015), G3 (molander2016)

Molander 2016 proposes a DKR mechanism for enantioconvergent photoredox/Ni coupling where NiIII C–Ni bond homolysis/recombination must be fast relative to reductive elimination (khomolysis >> kRE). The DFT support (Figure 9) uses benzyl radical as the model, but the synthetically important substrates are secondary unactivated alkyls with substantially different radical stabilization energies. Cherney 2015 inherits this DKR classification for multiple reactions without independent kinetic verification (B-1, SRG-1).

Persistence: The DKR assumption persists across both Molander 2016 (U-4, B-6, B-13) and Cherney 2015 (B-1, U-1) as an untested kinetic ordering. Molander 2016's U-7 (convergence 3/3, all high) specifically flags the benzyl→secondary alkyl extrapolation as the strongest convergence item in that paper.

Testable hypothesis: The DKR khomolysis >> kRE condition may fail for secondary unactivated alkyl radicals, which have higher C–Ni bond dissociation energies than benzyl radicals. If khomolysis ≈ kRE for these substrates, the DKR mechanism predicts reduced ee at higher conversion — a testable conversion-ee profile experiment.

Why not subsumed by IP-1 or IP-3: IP-1 captures unvalidated catalytic cycles generally. IP-3 captures self-contradictory absence. The DKR extrapolation question is substrate-specific and has a concrete experimental prediction (conversion-dependent ee) that distinguishes it from the general pattern. Absorption into IP-1/IP-3 would lose the specific testable prediction about non-benzylic substrates.

evidence_chain: [Molander_2016 : U-4 (DKR kinetics untested), U-7 (benzyl model extrapolation, 3/3 convergence), B-13 (n=3 stereochemical validation) | Cherney_2015 : B-1 (DYKAT/DKR without krac/kproductive), U-1 (DET conversion-ee untested)]

---

**SSP-6: Electrochemical operating potential vs analytical CV potential (G2)**

Originating sub-group: G2 (pengfei2024)

Pengfei 2024 uses cyclic voltammetry (CV) and square wave voltammetry (SWV) under analytical conditions to characterize Ni redox potentials, but the actual cathode potential during constant-current electrolysis (5 mA, Fe anode, Ni foam cathode) is never measured (B-6). Furthermore, the DFT-calculated Ni(I)/Ni(0) potential (−2.38 V vs Ag/AgNO₃) disagrees with the SWV-measured value (−2.74 V vs Ag/AgNO₃) by 360 mV (U-2, B-13), and reference electrodes differ between figures without conversion factors (B-2).

Persistence: This specific electrochemistry gap is unique to Pengfei 2024 within the corpus (no other paper uses electrochemical activation). However, the underlying question — [REDACTED: substantial verbatim quotation; see Tier 9] — is a specific instance of a broader analytical gap that is not captured by IP-2.

Testable hypothesis: The operating cathode potential during 5 mA constant-current electrolysis in DMF with 0.33 equiv NaI may differ substantially from the potentials measured by analytical CV/SWV, because (a) the low electrolyte concentration creates significant ohmic drop, and (b) the Ni foam cathode has different surface area and mass transport properties than the analytical electrode. If the operating potential is less negative than −2.38 V (the DFT Ni(I)/Ni(0) value), the proposed Ni(0) generation via cathodic reduction may not be thermodynamically accessible.

Why not subsumed by IP-2: IP-2 captures "analytical basis underreported" as a measurement-quality concern. The electrochemical operating potential question is not about reporting quality — it is about whether the fundamental thermodynamic premise of the proposed mechanism (cathodic reduction to Ni(0)) is actually satisfied under reaction conditions. This is a mechanistic question, not an analytical one.

evidence_chain: [Pengfei_2024 : B-2 (reference electrode inconsistency), B-6 (cathode potential unmeasured), B-13/U-2 (DFT vs SWV 360 mV discrepancy), SRG-2 (electrochemical conditions unreported)]

---

**SSP-7: Dynamic bite-angle hypothesis — fanning motion as catalytic accelerator (G3)**

Originating sub-group: G3 (monnereau2009)

Monnereau 2009 proposes that the calixarene backbone's "fanning motion" periodically increases the P–Ni–P bite angle, accelerating reductive elimination and explaining the TOF advantage over dppp. This is a mechanistically specific and novel proposal, but (a) the fanning frequency was measured at −80°C/CD₂Cl₂ while catalysis occurs at 100°C/dioxane (B-10), (b) no rigid analogue was synthesized to test the hypothesis (A-2), (c) the RE acceleration model is in tension with the OA-limited ArCl result (U-3), and (d) the Pd/Rh analogy for bite-angle/RE rate correlation (C-3) is not validated for Ni.

Persistence: This hypothesis is unique to Monnereau 2009 within the corpus. However, the broader question — [REDACTED: substantial verbatim quotation; see Tier 9] — connects to the ligand effect attribution pattern identified in G1 (Kumada 1972 B-3/U-4, Kumada 1976b A4/A5) and G3 (Mazet 2021 B10). The specific testable experiment (rigid analogue synthesis) was proposed by the authors themselves.

Testable hypothesis: The record TOF of complex 2 is attributable to the dynamic bite-angle effect if and only if a structurally rigid analogue with the same static bite angle (102.8°) shows significantly lower TOF. This is the experiment the authors themselves proposed (A-2) but never executed.

Why not subsumed by IP-1: IP-1 captures unvalidated catalytic cycles. The dynamic bite-angle hypothesis is not about the identity of elementary steps — it is about the rate of one specific step (RE) being modulated by a specific structural dynamic (fanning). This is a testable rate-acceleration claim, not a cycle-identity claim.

evidence_chain: [Monnereau_2009 : A-2 (rigid analogue proposed), B-10 (dynamics/catalysis conditions incompatible), U-3 (RE/OA tension), C-3 (Pd/Rh analogy unvalidated for Ni)]

---

**Integrated group_unasked_question**

[REDACTED: substantial verbatim quotation; see Tier 9]

This question integrates the three sub-group questions as follows:
- From G1: the demand for complete speciation and time-resolved product profiles
- From G2: the demand for a quantitative selectivity model spanning sp²→sp³
- From G3: the demand for an agreed evidentiary standard for mechanistic claims

The question is not answered by any paper in the 9-paper corpus. Its persistence across 52 years (1972–2024), 9 papers, 5 paradigms (2-electron, radical, photoredox, electrochemical, asymmetric), and 8 journals constitutes the strongest evidence that it represents a field-wide structural convention — the convention that scope demonstration takes priority over mechanistic proof, and that catalytic cycle proposals serve narrative rather than predictive functions.

The sub-group-specific findings (SSP-1 through SSP-7) represent the chemically concrete experiments that would contribute to answering this unified question: MgBr₂ control experiments (SSP-1), homogeneity tests (SSP-2), E/Z selectivity probes (SSP-3), β-elimination competition kinetics (SSP-4), DKR conversion-ee profiles (SSP-5), operando electrochemistry (SSP-6), and rigid-analogue synthesis (SSP-7). Each SSP identifies a specific experiment; the unified question identifies the principle that organizes them.

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
