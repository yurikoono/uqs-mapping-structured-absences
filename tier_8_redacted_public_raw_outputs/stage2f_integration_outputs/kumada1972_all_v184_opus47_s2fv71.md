prompt_version: stage2f-v7-20260417

---

**[F. Within-Group Comparison — Integration Mode]**

**Input:** Stage 2F v7.1 outputs from three sub-groups (v18.4 / Sonnet S0–S3v2 / Opus 4.7 2F):
- G1: Direct lineage (kumada1972, kumada1976b, mazet2021) — 3 papers, dpe/dppe-Ni system, 1972–2021
- G2: Boundary breakthrough (kumada1972, breitenfeld2014, cherney2015, pengfei2024) — 4 papers, Csp³ frontier, 1972–2024
- G3: Methodological expansion (kumada1972, monnereau2009, molander2016, morken2016) — 4 papers, 1972–2016

**Reference paper:** Kumada 1972 (shared anchor across all three sub-groups)
**Reference Stage 3 (v18.4):** kumada_v184_sonnet_s3v2_en.md — 6 SRGs, 2 CLAs; EPs 03a/04a/06a/07a/08a/09a/01a/05a; VQ-1 PASS, VQ-2 conditional, VQ-3 FAIL.
**Total unique papers across sub-groups:** 9. Kumada 1972 appears in all three; the other 8 are sub-group-specific.

---

**Patterns that emerged independently in multiple sub-groups (Field-wide IPs)**

The following patterns were each identified in all three sub-groups by chains of evidence drawn from non-shared papers (i.e., excluding the Kumada 1972 anchor). Their independent emergence in 2 or 3 sub-groups, in addition to recurrence within each sub-group, is the integration-mode warrant for treating them as field-wide structural conventions rather than artefacts of one comparison frame.

**IP-1: Catalytic cycle proposed without elementary-step validation under operating conditions**

- G1 RP-1: kumada1976b A-1/U-1/U-2 + mazet2021 A-3/B-5/B-6/U-1 — spanning the same dpe/dppe-Ni system from 1976 to 2021.
- G2 RP-1: breitenfeld2014 A-1/U-1/U-2 + cherney2015 U-1/B-6/C-5 + pengfei2024 U-6/B-7/CLA-1 — spanning the closed-shell → radical paradigm shift.
- G3 RP-1: monnereau2009 A-1/U-1/U-2 + molander2016 B-5/U-1/U-2 + morken2016 B-5/B-6/U-1 — spanning ligand-architecture, photoredox, and asymmetric variants.

evidence_chain (non-anchor): [Kumada_1976b : A-1, U-1, U-2 | Mazet_2021 : A-3, B-5, U-1 | Breitenfeld_2014 : A-1, U-1, U-2 | Cherney_2015 : U-1, B-6 | Pengfei_2024 : U-6, B-7 | Monnereau_2009 : U-1, U-2, U-3 | Molander_2016 : B-5, U-1, U-2 | Morken_2016 : B-5, B-6, U-1]

The same structure — cycle drawn, intermediates named, elementary steps imported by analogy or DFT — recurs in 8 of 8 non-anchor papers across four mechanistic regimes (closed-shell Ni(0)/Ni(II), radical Ni(I)/Ni(III), photoredox NiI/NiIII, electrochemical Ni(I/II/III)) and four formats (Communication, Full Paper, Review, Account). This is the strongest field-wide signal in the corpus.

**IP-2: Quantitative analytical basis for primary data underreported**

- G1 RP-2: kumada1976b B-1/B-2/B-10 + mazet2021 B-5/B-7 — GLPC response factors → VTNA statistical adequacy.
- G2 RP-2: breitenfeld2014 B-2/B-4/B-7 + cherney2015 B-2/B-15 + pengfei2024 B-1/B-4/B-9 — replicate counts → cross-study aggregation → Faradaic efficiency.
- G3 RP-2: monnereau2009 B-1/B-2/B-7 + molander2016 B-1/B-9 + morken2016 U-3/B-8 — GC-only conversions → yield-type unspecified → SFC method missing.

evidence_chain: [Kumada_1976b : B-1, B-2, B-10 | Mazet_2021 : B-5, B-7 | Breitenfeld_2014 : B-2, B-4, B-7 | Cherney_2015 : B-2, B-15 | Pengfei_2024 : B-1, B-4, B-9 | Monnereau_2009 : B-1, B-2, B-7 | Molander_2016 : B-1, B-9 | Morken_2016 : U-3, B-8]

The specific analytical instrument changes (glpc 1972 → calibrated GLPC 1976 → multi-run GC + radical-clock 2014 → review-aggregated ee 2015 → in-situ IR/VTNA/X-ray 2021 → SFC + ³¹P 2016 → CV/SWV/electrolysis 2024). The structural absence — primary-measurement reliability cannot be evaluated from the published text — is invariant. None of the 8 non-anchor papers reports replicate-based uncertainty for its headline numbers.

**IP-3: Self-contradictory absence — model predicts observables that are not tested or whose results contradict the model**

- G1 RP-4: kumada1976b U-1/U-2/U-3/U-5 + mazet2021 U-1/U-2/U-3/U-4 — Scheme 1 normal-order C–X reactivity contradicted; β-suppression contradicted by sec→prim isomerization; VTNA acknowledged unreliable yet conclusions retained; E/Z reversal unanalyzed.
- G2 RP-3: breitenfeld2014 U-1/U-3/U-4 + cherney2015 U-1/U-3/U-8 + pengfei2024 U-1/U-4/U-5/U-6 — DFT-only pathway discrimination; rate-law unwritten; EPR-active intermediates predicted across 427 refs without one cited spectrum; selectivity model leaves 17%+13% homocoupling unreconciled; CV-vs-DFT redox potentials disagree by 360 mV undiscussed.
- G3 RP-3: monnereau2009 U-1/U-2/U-3 + molander2016 U-1–U-7 + morken2016 U-1/U-2/U-4/CLA-2 — bite-angle-dynamics rigid-analogue control acknowledged-then-deferred; PES applied to nine substrate classes without re-computation; ArMgBr vs Ar₂Mg active species unidentified despite aging-protocol implications.

evidence_chain: [Kumada_1976b : U-1, U-2, U-3, U-5 | Mazet_2021 : U-1, U-2, U-3, U-4 | Breitenfeld_2014 : U-1, U-3, U-4 | Cherney_2015 : U-1, U-3, U-8 | Pengfei_2024 : U-1, U-4, U-5, U-6 | Monnereau_2009 : U-1, U-2, U-3 | Molander_2016 : U-1–U-7 | Morken_2016 : U-1, U-2, U-4, CLA-2]

8/8 non-anchor papers carry the pattern. Cherney 2015 amplifies it to 8 distinct U items because the review aggregates primary-paper proposals as if established, multiplying the cases where model predictions go untested at field level.

**IP-4: Selectivity / scope / boundary claims without complete byproduct or negative-result accounting**

- G1 RP-3: kumada1976b A-2/U-4 (alkyl + dichloroethylene "complex mixture, homo coupling predominating" never characterized) + mazet2021 B-1/B-6 (Figure 9 ~75–85% mass-balance gap; Introduction-flagged scope failures never revisited).
- G2 RP-4: breitenfeld2014 B-7 (linear:cyclized ratio without total yields/conversions) + cherney2015 B-3/B-11/CLA-2 (frontier prioritization without inventory of inaccessible targets) + pengfei2024 B-3/B-6/B-8 (general-strategy claim with caption-footnote ligand bifurcation; no head-to-head with Lin/Gong prior art).
- G3 RP-6: monnereau2009 A-3 (bromomesitylene 780 h⁻¹ outlier under "high activities with congested bromoarenes") + molander2016 B-4/B-8 (amine-silicate "performed poorly" with no yields) + morken2016 A-1/B-3/B-4 (tertiary/quaternary "ineffective" with no values; ortho-Ar/alkyl/alkenyl Grignard "lower yield, nearly racemic" with no values).

evidence_chain: [Kumada_1976b : A-2, U-4 | Mazet_2021 : B-1, B-6 | Breitenfeld_2014 : B-7 | Cherney_2015 : B-3, B-11, CLA-2 | Pengfei_2024 : B-3, B-6, B-8 | Monnereau_2009 : A-3 | Molander_2016 : B-4, B-8 | Morken_2016 : A-1, B-3, B-4]

Field-wide. The shared structure: positive-feature framing of selectivity / scope / boundary without the negative-result data that would convert assertion into demonstration.

**IP-5: Benchmark superiority asserted without matched-pair comparison on shared substrate**

- G1 implicit (RP-5 ligand attribution): kumada1976b "exothermicity of reactions" qualitative ranking; mazet2021 dppe vs dmpe two-point %V_Bur from non-catalytic cod complexes.
- G2 RP-4 partial: pengfei2024 no head-to-head with Lin 2022 (ref 60) or Gong 2011/2013 (refs 29–30) on shared substrates.
- G3 RP-4 (named explicitly): monnereau2009 dppp comparison restricted to one substrate at non-headline loading + molander2016 Figure 2 prior-Pd-Suzuki six-protocol depiction without yield comparison + morken2016 Fu/Zhong-Bian/Nakamura/Jarvo cited symmetrically without er/yield comparison even for Jarvo (closest structural analog).

evidence_chain: [Kumada_1976b : A-5, B-11 | Mazet_2021 : B-3, B-4 | Pengfei_2024 : C-cluster (Lin, Gong) | Monnereau_2009 : B-3, B-4, C-10 | Molander_2016 : C-1, C-2, C-3 | Morken_2016 : C-1–C-7]

Independently named in G3 (RP-4); flagged in G2 within selectivity/scope; observable in G1 within ligand attribution. Field-wide, with the closest structural analogue routinely receiving the same cite-and-contrast treatment as more distant references.

**IP-6: Imported model — mechanistic framework adopted from non-isomorphous source**

- G1 RP-1 sub-pattern: kumada1976b imports (dipy)Ni precedent (Jolly-Wilke) with C-7 acknowledging Felkin-Corriu Ni(0) alternative not excluded; mazet2021 dmpe bimetallic TS lacks DFT corroboration.
- G2 RP-5: breitenfeld2014 PBE0-dDsC/TZ2P//M06/def2-SVP without benchmarking + cherney2015 Lin et al. Ni¹/Ni³ DFT applied across 427 references without EPR/CV cross-reference + pengfei2024 2.8 kcal mol⁻¹ Ni(III)-vs-Ni(II) preference with functional / basis set / solvation / spin states all undisclosed.
- G3 RP-5 (named explicitly): monnereau2009 Pd diphosphine bite-angle precedent applied to Ni without addressing Ni(I)/Ni(III) accessibility + molander2016 Gutierrez 2015 SMD-water PES (ε≈80) applied to dioxane/acetone/EtOAc/DMF (ε = 2.2–38) and to nine substrate classes + morken2016 generic Ni(0)/Ni(II) manifold + organic SN2 geometry without PyBox-Ni DFT.

evidence_chain: [Kumada_1976b : A-1, C-4, C-7 | Mazet_2021 : A-3 | Breitenfeld_2014 : U-1, B-5 | Cherney_2015 : U-1, C-5, CLA-1 | Pengfei_2024 : U-6, SRG-1, SRG-10 | Monnereau_2009 : C-14, U-4 | Molander_2016 : B-5, U-1 | Morken_2016 : U-1, U-2]

Field-wide and tightly co-occurring with IP-1: in 7/8 non-anchor papers, IP-1 (cycle without elementary-step validation) and IP-6 (cycle imported from non-isomorphous source) are the same gap viewed from two angles — the cycle is unobserved because it was never the target of measurement, and it was never the target of measurement because it was already accepted by analogy.

**IP-7: Computational model deployed as sole pathway discriminant without protocol benchmarking** *(emergent post-DFT; absent in pre-DFT papers)*

- G1: mazet2021 (DFT corroboration explicitly absent for bimetallic TM step).
- G2 RP-5 (named explicitly): breitenfeld2014 + cherney2015 + pengfei2024 — three reaction types in one review without experimental validation; 2.8 kcal mol⁻¹ pathway preference without method disclosure or uncertainty.
- G3 instances: monnereau2009 single ³¹P shift + molander2016 PES without ⟨S²⟩/ZPE/solvation sensitivity + morken2016 stoichiometric assumption without DFT for PyBox-Ni geometry.

evidence_chain: [Mazet_2021 : U-1 | Breitenfeld_2014 : U-1, U-3, U-5, B-5 | Cherney_2015 : U-1, U-8, C-5, C-9, CLA-1 | Pengfei_2024 : U-6, SRG-1, SRG-10 | Monnereau_2009 : U-1 | Molander_2016 : U-1, U-2, U-7 | Morken_2016 : U-1]

This is the only IP whose absolute magnitude scales with era. The structure is invariant once DFT becomes available; the visibility is era-dependent.

---

**IP couplings and dependencies (integration-only view)**

The seven IPs do not appear independently. The integration-mode reading reveals four tight couplings whose joint occurrence is the actual signature of the field convention:

**Coupling C-α: IP-1 ↔ IP-6 (cycle unobserved ↔ cycle imported).** In 7 of 8 non-anchor papers (all except cherney2015, where the review-aggregation amplifies both jointly), the cycle is unobserved *because* it was never the target of system-specific measurement, and it was never the target of system-specific measurement *because* the cycle was already accepted by analogy. The two IPs are not separable — closing IP-1 requires demonstrating isomorphism (closing IP-6), and closing IP-6 requires elementary-step characterization in the actual system (closing IP-1). The remediation is the same single experimental package. Stage 3 v18.4 EP-06a (analogy-validation pack) is the canonical instantiation: the EP requires both system-specific synthesis of analogue intermediates *and* demonstration that they reproduce catalytic-condition selectivity. EP-06a is one experiment; IPs 1 and 6 are two readings of the same gap.

**Coupling C-β: IP-3 ↔ IP-1 (self-contradictory absence ↔ mechanism unvalidated).** Self-contradictory absence is the *generation rule* by which IP-1 manifests as a paper-level observable. The cycle predicts X (eq 3 → R–R; comproportionation → catalyst recovery; bite-angle dynamics → rigid-analogue-slower; PES → ⟨S²⟩-stable; ion-exchange → κ¹/κ² distinction); the paper does not test X; IP-1 (mechanism unvalidated) is the abstract reading, IP-3 (specific prediction untested) is the concrete reading. EP-04a (discrimination/replication) is the canonical remediation for the IP-3 reading; EP-03a / EP-06a are the canonical remediations for the IP-1 reading. The corpus shows that the IP-3 remediations (EP-04a) achieve 0% filling rate while the IP-1 remediations (EP-06a) achieve ~25% — the more abstract gap attracts technological progress, the more concrete prediction-test does not.

**Coupling C-γ: IP-2 ↔ IP-4 (analytical underreporting ↔ selectivity without accounting).** Mass-balance closure (IP-4 closure) requires replicate-based uncertainty for the byproduct and main-product yields (IP-2 closure). The two IPs are operationally inseparable: a paper that fully closes IP-4 must report internal-standard identity, response factors, replicate measurements, and detection limits — the exact metadata IP-2 records as absent. Across the corpus, the joint failure rate of IP-2+IP-4 is 9/9. EP-08a + EP-09a + EP-01a are the canonical Stage 3 v18.4 remediations and all three exhibit 0% filling.

**Coupling C-δ: IP-5 ↔ IP-7 (benchmark superiority asserted ↔ DFT-as-discriminant).** A paradigm-claim paper deploys DFT as discriminant against a competing paradigm; the same paradigm-claim paper asserts superiority over prior art without head-to-head comparison; the two assertions are made under the same evidentiary regime (asserted, not demonstrated). Visible most clearly in pengfei2024 (DFT 2.8 kcal mol⁻¹ Ni(III)-vs-Ni(II) preference + no head-to-head with Lin 2022 / Gong 2011-2013) and in cherney2015 (Lin et al. Ni¹/Ni³ DFT framework + frontier prioritization without inventory of inaccessible targets). Coupling C-δ is the integration-mode pattern that is most strongly post-2010 and aligns with IP-7's emergent classification.

These four couplings tighten the integration-mode reading from "seven independent field gaps" to "four functional gap-clusters that the corpus exhibits jointly." Each cluster maps to a coherent experimental package: C-α → EP-03a + EP-06a; C-β → EP-04a; C-γ → EP-01a + EP-08a + EP-09a; C-δ → EP-05a + (post-DFT extension of EP-09a to computational benchmarks). The corpus's filling landscape (above) shows that the four packages have asymmetric filling rates: C-α partial, C-β zero, C-γ zero, C-δ zero. Only the cluster whose remediation aligns with technological progress shows any movement.

---

**Cross-field temperature patterns (integration view)**

temperature_pattern: IP-1 mechanism validation | papers: 9 of 9 | profile_consistency: rising-convergent | note: V1+V2+V3 3/3 convergence achieved by mazet2021 (G1), pengfei2024 + cherney2015 (G2), monnereau2009 + molander2016 + morken2016 (G3). Earlier papers reach 2/3. Severity recognition rises with era at constant structural gap, indicating field-wide expectation has tightened while paper-level practice has not.

temperature_pattern: IP-2 analytical underreporting | papers: 9 of 9 | profile_consistency: invariant-medium-to-high | note: V3-equivalent agents flag the gap at medium-to-high in every paper. The instrument changes; the severity rating does not.

temperature_pattern: IP-3 self-contradictory absence | papers: 9 of 9 | profile_consistency: high-uniform | note: Whatever agent flags it, severity is uniformly high. Cherney 2015 reaches 3/3 V1+V2+V3 because the review aggregates primary-paper proposals such that a single reading by any agent surfaces the field-level gap.

temperature_pattern: IP-4 selectivity / scope without accounting | papers: 9 of 9 | profile_consistency: consistent-medium | note: 3/3 medium convergence in kumada1972 anchor (B-1, B-4, B-6); 2/3 convergence in pengfei2024, monnereau2009, molander2016, morken2016. Recurs across paradigms but at slightly lower severity than IP-1/IP-3.

temperature_pattern: IP-5 benchmark superiority | papers: 9 of 9 | profile_consistency: consistent-low-to-medium | note: V2 (cartographic) flags reliably; V1/V3 less consistently. Convention is so naturalized that single-agent detection dominates.

temperature_pattern: IP-7 DFT as discriminant | papers: 7 of 9 (post-DFT) | profile_consistency: rising-with-era | note: Severity increases with year — pengfei2024 U-6 reaches 3/3 V1+V2+V3=high (the strongest convergence in any paper of the corpus). Field expectation crystallizes faster than disclosure practice.

**temperature_gap_increasing across later papers:** IP-7 (DFT-as-discriminant) shows the only systematic temperature-gap rise across the corpus: in 2014–2015 the gap is era-tolerated; in 2024 it reaches 3/3 high convergence with no method disclosure provided in main text. This is the field norm becoming most contested with time.

---

**Recurring roots across sub-groups (integration)**

recurring_root: Catalytic cycle assembled by analogy / DFT without elementary-step validation | sub-groups: G1 root #1 + G2 root #1 + G3 root #1 | papers: 9 of 9 | note: Field-wide structural gap. RI-06 (imported model) + RI-03 (unobserved explanatory) co-occurrence; the kumada1972 Stage 3 SRG-1 anchor (members A-2, U-2, B-12 with EP-06a + EP-03a remediation) is reproduced in identical form across the corpus with EPs differing only in their case-specific implementation. The cycle is, across 52 years and 4 paradigms, almost never the target of system-specific measurement.

recurring_root: Quantitative measurement basis underreported | sub-groups: G1 root #2 + G2 root #2 + G3 root #2 | papers: 9 of 9 | note: Genre convention. Spans JACS Communication / BCSJ Full Paper / Organometallics Full Paper / Adv. Synth. Catal. Full Paper / Acc. Chem. Res. Account / Chem. Rev. Review / ACS Catal. Full Paper / Nature Catalysis Full Paper. The kumada1972 SRG-5 anchor (B-2, B-7, B-9, B-11 with EP-08a + EP-01a remediation) reproduces verbatim across the corpus.

recurring_root: Selectivity / mass-balance closure | sub-groups: G1 root #3 + G2 root #3 + G3 root #3 (RP-6 specific subtype "scope failures undiagnosed") | papers: 9 of 9 | note: Recurs in all 9 papers. The kumada1972 SRG-2 anchor (B-6, U-1, C-1 with EP-04a + EP-09a remediation) exhibits the canonical structure: title-level "selective" claim, eq 3 predicts byproduct, byproduct unreported. The structure recurs in every paper at higher analytical infrastructure with the same closure deficit.

recurring_root: Self-contradictory absence around mechanism-derived predictions | sub-groups: G1 root #4 + G2 (within RP-3) + G3 (recurring U-1) | papers: 9 of 9 | note: A/B/C framework gap. The pattern accumulates in 28 distinct U items across the corpus (kumada1972: 2; kumada1976b: 4; mazet2021: 4; breitenfeld2014: 4; cherney2015: 8; pengfei2024: 7; monnereau2009: 3; molander2016: 7; morken2016: 4). The Stage 1 framework captures it as residual U items, signalling that "model → prediction → untested" is a distinct epistemic category not currently named in A/B/C. Cross-model verification (memory: project_v19_dev_cycle_state.md C27/C28/C29 codification proposals) suggests this is a stable detection target.

recurring_root: Ligand / structure–activity attribution from confounded comparisons | sub-groups: G1 root #5 + G3 (within RP-1/RP-5) | papers: 5 of 9 (kumada1976b, mazet2021, monnereau2009, breitenfeld2014, morken2016) | note: Structurally suppressed across decades — deconvoluting steric / electronic / geometric ligand effects requires a multi-ligand systematic series, a different research program than any single paper undertakes. Era-invariant.

recurring_root: Computational mechanism without benchmarking | sub-groups: G2 root #4 + G3 (within RP-1) | papers: 7 of 9 (post-DFT) | note: Emergent root. Becomes field-level (Cherney 2015 documents it as systemic) and intensifies through 2024.

recurring_root: Benchmark superiority without matched-pair comparison | sub-group: G3 root #4 (named) + G2 RP-4 partial + G1 implicit | papers: 9 of 9 | note: Not foregrounded as a recurring_root in G1 (the lineage frame muted competitive comparison) but present once read across G2 + G3 + the kumada1972 SRG-6 (C-1, C-2, A-4 with EP-09a remediation) anchor. Promoted to a field-wide root by integration mode.

---

**Temporal trajectory of recurring patterns (integration)**

temporal_trajectory: IP-1 (mechanism validation) | classification: shifting | transition_point: ~2010–2015 (in-situ tools become standard; review-level documentation crystallizes the gap as paradigm-level rather than paper-level) | note: Pre-2010 era-suppressed (no in-situ NMR, EPR, VTNA, DFT for catalytic intermediates). Post-2010 era — tools available, deployed, but at insufficient depth or with insufficient benchmarking. Cherney 2015 is the documentation point at which the shift is visible across an entire subfield.

temporal_trajectory: IP-2 (analytical underreporting) | classification: time-invariant | note: No journal across the corpus enforces replicate-based uncertainty, raw-data deposition, mass-balance closure, or response-factor disclosure. 52-year invariance.

temporal_trajectory: IP-3 (self-contradictory absence) | classification: time-invariant | note: The specific predictions vary; the structure (model predicts → unreported / contradicted / explained-away) is invariant.

temporal_trajectory: IP-4 (selectivity / scope without accounting) | classification: narrowing-then-stalling | note: Improved from 1972 (no byproduct data) to 1976 (some entries; one mass-balance violation) to 2021 (scope failures tabulated; ~75–85% gap remains in stoichiometric experiment) to 2024 (per-substrate homo coupling reported but unreconciled with selectivity model). Continuous improvement, no closure.

temporal_trajectory: IP-5 (benchmark superiority asserted) | classification: time-invariant | note: Tamura-Kochi citation pattern (1972) structurally identical to Jarvo citation pattern (2016). Closest analogue dismissed without matched comparison.

temporal_trajectory: IP-6 (imported model) | classification: shifting | note: Source shifts from precedent-experimental (1972 stoichiometric (dipy)Ni; 2009 Pd diphosphine) to precedent-computational (2014+ DFT PES from related but non-isomorphous systems). Absent isomorphism demonstration is invariant across the shift.

temporal_trajectory: IP-7 (DFT-as-discriminant) | classification: emergent | transition_point: ~2010 (DFT becomes routine) → intensifying through 2024 | note: The only IP whose existence is era-bound.

---

**Structural suppression vs. individual choice (integration synthesis)**

The three sub-groups converge on a 4-way partition of the IPs by suppression mode:

| IP | Suppression mode | Cross-subgroup agreement |
|---|---|---|
| IP-1 mechanism validation | Era-dependent: structurally suppressed pre-2010 → individually chosen / methodologically limited 2010+ | G1 + G2 + G3 all classify as era-dependent shifting |
| IP-2 analytical underreporting | Incentive-suppressed (audit work generates no publishable contribution) | G1 + G2 + G3 all classify as era-invariant + incentive-anchored |
| IP-3 self-contradictory absence | Individually chosen + incentive-suppressed (testable with paper's own infrastructure but testing yields either confirmation [unpublishable] or falsification [requires different paper]) | G1 + G2 + G3 all converge on this dual classification |
| IP-4 selectivity / scope w/o accounting | Incentive-suppressed (mass-balance audit not publishable as standalone) | G1 + G2 + G3 |
| IP-5 benchmark superiority | Incentive-suppressed (matched comparison risks demonstrating non-superiority on shared substrate) | G3 explicit; G1 + G2 implicit |
| IP-6 imported model | Era-dependent: structurally suppressed pre-2009 → individually chosen 2009+ (DFT/in-situ tools available for isomorphism testing) | G1 + G2 + G3 |
| IP-7 DFT-as-discriminant | Era-dependent emergent → individually chosen 2018+ (Houk / Grimme benchmarking literature establishes the expectation) | G2 + G3 |

The integration-level observation: IPs 2–5 are stably incentive-suppressed across the entire 52-year span. IPs 1, 6, 7 are era-shifting, all in the same direction (from structurally suppressed to individually chosen), at approximately the same transition point (~2010–2015). The corpus exhibits a coherent two-band structure: incentive-locked gaps (which no methodological development closes) and tool-locked gaps (which methodology has nominally unlocked but practice has not yet adopted).

---

**Paradigm competition / succession (integration synthesis)**

The three sub-groups expose three different relational structures:

- **G1 (lineage):** paradigm succession — scope-first methodology (1972, 1976) → mechanism-first investigation (2021). Each paradigm's blind spot is the next paradigm's founding problem.
- **G2 (boundary):** paradigm succession (closed-shell Csp² → radical Csp³ at the substrate boundary) plus *paradigm tension within Paradigm B*, documented by Cherney 2015's review-aggregation moment. The Ni¹/Ni³ vs Ni⁰/Ni² sub-paradigm tension within radical catalysis is unresolved across 427 review references.
- **G3 (expansion):** paradigm coexistence — three independent expansion axes (ligand architecture, photoredox activation, asymmetric desymmetrization) sharing the 1972 anchor but expanding orthogonally. Not succession; not direct competition; coexistence with shared blind spot.

**Integration-level synthesis.** The field exhibits *paradigm proliferation with a conserved core blind spot.* Whether the paradigm relationship is succession (G1, G2), tension (G2 sub-paradigm), or coexistence (G3), every paradigm preserves IP-1 (mechanism validation absence), IP-2 (analytical reliability gap), IP-3 (self-contradictory absence), and IP-4 (selectivity-without-accounting). The integration view rules out the hypothesis that any single paradigm's adoption would close these gaps: each paradigm change re-instantiates them in new manifestations. This is the strongest possible empirical case that the gaps are field-structural rather than paradigm-specific.

**Field-invariant blind spot persisting across all paradigms (integration):** the field has produced no quantitatively closed, time-resolved, mechanistically-validated account of any one Ni-catalyzed cross-coupling system that satisfies IPs 1–4 simultaneously. Across all 9 papers, no paper meets the standard for its own central mechanistic claim.

---

**Divergences across sub-groups**

**DV-A: Cherney 2015 review-genre amplification.** G2 alone contains a review paper, and the integration view confirms the G2 finding that the review is the documentation point for IP-1 + IP-3 + IP-7 as field-level patterns. Without the review, the gaps could be read as a series of individual choices; with the review, they are legible as paradigm-level conventions. This is a sub-group-specific structural feature that should be preserved separately (see "Sub-group-specific findings" below).

**DV-B: G1's narrower temporal × system span isolates ligand-attribution gap.** G1's RP-5 (ligand-effect attribution from confounded comparisons) is most clearly visible in G1 because G1 papers all use related dpe/dppe ligands; G2 and G3 papers use widely different ligands and thus the confound becomes a between-paper rather than within-paper observation. G1 is the optimal frame for diagnosing this pattern.

**DV-C: G3's success-metric divergence vs G1/G2's substrate divergence.** In G3, the four papers define success by four different metrics (yield, TOF, paradigm + scope, er); the divergence is in evaluation framework. In G1/G2, the divergence is in substrate class (Csp² vs Csp³, lineage extension). Each frame surfaces a different field-wide convention.

evidence_chain: [G2 unique: cherney2015 CLA-1 + CLA-2 + B-2 (review-aggregation gaps absent in primary papers) | G1 unique: mazet2021 dppe vs dmpe two-point %V_Bur (RP-5) | G3 unique: morken2016 D-1 success_criteria → er, vs molander2016 success_criteria → paradigm framing]

---

**Recurring U-item patterns (integration)**

recurring_U: Self-contradictory absence around mechanism-derived predictions | sub-groups: all three | papers: 9 of 9 | item count: 28 U items across corpus | note: The single largest recurring U class. Confirmed across paradigms (closed-shell, radical, photoredox, asymmetric, electrochemical), formats (Communication, Full Paper, Review, Account), journals, and 52 years. Strong evidence that "model → prediction → untested" is a distinct epistemic category not naturally captured by A (deferred) / B (reporting omission) / C (severed citation). Aligns with v19 codification candidate C27 (Success-driven question erasure, n=4 anchor in user memory).

recurring_U: Available-but-unutilized characterization | sub-groups: G1 + G2 + G3 partial | papers: 5 of 9 | note: Subtype of self-contradictory absence in which the analytical tool exists and (sometimes) has been deployed, but the analysis is not performed. Examples: kumada1976b U-8 (yellow species identified by color despite NMR/UV-vis available); mazet2021 U-5 + CLA-2 (X-ray of 9c acquired but binding-mode and OA-geometry %V_Bur unreported); pengfei2024 U-2 (CV/SWV vs DFT 360 mV discrepancy undiscussed); morken2016 U-3 (SFC method undisclosed despite its use). Distinct from era-suppressed analytical limitation. Implication: an "available-but-unutilized" subclass within U or B-items would improve A/B/C resolution.

recurring_U: Prerequisite-absence for primary evidentiary claim | sub-groups: G2 + G3 | papers: 6 of 9 (mostly post-2009) | note: Distinct from self-contradictory absence — a methodological prerequisite (DFT benchmarking, reference-electrode harmonization, anode characterization, spin-state assignment, SFC method) is asserted rather than established. Emergent post-2009 as the field's claim sophistication outpaces the evidentiary infrastructure deployed.

recurring_U: Mechanistic-discrimination test absent for competing mechanisms | sub-groups: G1 + G2 | papers: 4 of 9 (kumada1976b, mazet2021, breitenfeld2014, cherney2015) | note: When two mechanisms are formally consistent with the same data, the discriminating experiment is structurally privileged information; its absence is more consequential than a generic missing experiment. Era-tolerated 1976; era-deficient 2021+.

---

**Self-contradictory absence patterns (integration assessment)**

The pattern recurs in 9/9 papers and 28 distinct U items. Across sub-groups it is consistently classified as:

- **Genre convention** — mechanism diagrams in cross-coupling papers serve narrative-organizing rather than hypothesis-testing function (G1, G2, G3 all converge).
- **Genuine analytical gap** — each prediction is testable with the originating paper's infrastructure (R–R via glpc; intermediates 10–16 via stoichiometric NMR; EPR of Ni(I)/Ni(III); CV-vs-kinetic reconciliation; rigid-analogue control; ⟨S²⟩ + ZPE + solvation tests; reductive-elimination retention via stoichiometric experiment).
- **Incentive-locked** — testing one's own mechanistic proposal either confirms it (unpublishable as standalone) or falsifies it (requiring a different paper).

The integration view sharpens the assessment: the persistence of the pattern across all 4 paradigms and all 4 formats argues definitively against the "individual oversight" or "format-specific compression" hypotheses. The pattern is reproduced even in the Acc. Chem. Res. Account format (molander2016, 11 pp) and in the Chem. Rev. Review format (cherney2015, 66 pp + 427 refs) — both formats with abundant page budget. Format expansion does not eliminate the gap. The gap is preserved by the publication-incentive equilibrium.

---

**Cross-sub-group reconciliation of suppression-mode classifications**

A specific integration-mode question is whether the three sub-groups agree, when applied independently, on the suppression-mode classification of each IP. Disagreement would indicate that the lens choice biases the diagnosis; agreement would indicate the diagnosis is lens-independent.

| IP | G1 classification | G2 classification | G3 classification | Reconciled |
|---|---|---|---|---|
| IP-1 mechanism validation | Era-dependent (1972/1976 structurally suppressed → 2021 individually chosen) | Era-dependent (~2000 + ~2010 transitions) | Era-dependent (~2014–2016 transition) | **Agreement: era-dependent shifting**, with all three sub-groups identifying the same direction (suppressed → chosen) and approximately the same transition window (~2010–2015). |
| IP-2 analytical underreporting | Era-dependent (1972/1976 structurally suppressed → 2021 incentive-suppressed) | Incentive-suppressed (invariant across formats and instruments) | Incentive-suppressed (invariant across format and journal) | **Agreement: incentive-suppressed in the modern regime.** G1 reads the 1972/1976 era as additionally tool-limited, but the modern endpoint is identical across all three lenses. |
| IP-3 self-contradictory absence | Individually chosen | Individually chosen (with incentive-suppression noted) | Individually chosen | **Agreement: individually chosen.** All three sub-groups note that each untested prediction is testable with the paper's own infrastructure, and all three add the incentive-suppression observation that doing so yields no publishable contribution. |
| IP-4 selectivity / scope without accounting | Incentive-suppressed | Incentive-suppressed | Incentive-suppressed (with format-specific compression noted for Communication papers) | **Agreement: incentive-suppressed.** G3 adds the format-compression nuance for kumada1972 + morken2016 4 pp Communications, but the underlying classification is invariant. |
| IP-5 benchmark superiority | Implicit (not foregrounded) | Within-RP-4 (partial) | Incentive-suppressed (named explicitly as RP-4) | **Agreement on incentive-suppression where the IP is named.** G1's lineage frame deemphasizes competitive comparison; G3's expansion frame foregrounds it; the underlying mechanism is the same. |
| IP-6 imported model | Era-dependent (1972/1976 source-stoichiometric → 2021 source-DFT) | Field-wide (post-2009) without explicit era-classification | Era-dependent (1972 stoichiometric → 2009 Pd → 2016 DFT) | **Agreement: era-dependent in the source of imported model + invariant in the absent isomorphism demonstration.** All three sub-groups identify the same shifting structure. |
| IP-7 DFT-as-discriminant | Implicit (Mazet 2021 only) | Era-dependent (named explicitly as RP-5; emergent post-DFT) | Era-dependent (named explicitly as RP-5) | **Agreement: emergent post-DFT, era-dependent transition ~2010, individually chosen by 2018+.** |

**Reconciliation outcome.** For all 7 IPs, the three sub-groups arrive at compatible suppression-mode classifications when both apply the diagnostic. The disagreements are exclusively about *which IPs are foregrounded*, not about *how each IP should be classified*. The integration-mode reading therefore inherits the suppression-mode structure with high confidence: the field exhibits a 4-mode partition (era-dependent shifting / incentive-suppressed / individually chosen / emergent) that is lens-invariant. This is methodologically significant for UQS Phase 2 deliverables: the diagnostic (individually chosen / structurally suppressed / incentive-suppressed / era-dependent) appears to be reproducible across independent sub-group constructions, which is one of the criteria for promoting it from heuristic to formal protocol element.

---

**Sub-group-specific findings not subsumed by field-wide patterns**

Per v7.1 prompt requirement, each sub-group's output is checked for patterns that did NOT rise to field-wide IP status but have independent analytical significance.

**SG-G1-1: Genre-induced labeling mismatch (G1 RP-6).** Hypothesis vocabulary at one rhetorical location with declarative / near-factual verbs in surrounding mechanistic narrative. Visible in all three G1 papers (kumada1972 "working hypothesis" final sentence + factual eqs 2–4; kumada1976b "can be rationalized by" + substantive declarative conclusions; mazet2021 "we propose" / "we establish" rhetorical separation). Not foregrounded in G2 / G3 outputs (they observe similar patterns but do not name them as a recurring pattern). Worth preserving because (a) it identifies a chemically concrete linguistic mismatch and (b) it persists across journal/era/language community. Aligns with kumada Stage 3 §6 institutional codification candidate (Labeling mismatch, RI-06 co-occurrence note).

**SG-G2-1: Csp²/Csp³ boundary as paradigm-succession driver.** The boundary itself is the organizing structural feature of G2; the 1972 paper's positive-feature framing of sp³ exclusion (B-4, no failed sp³ datum) becomes the founding problem of the radical paradigm (Breitenfeld 2014 onward). Specific to G2's group composition; would not appear in lineage-only or expansion-only frames. Identifies the structural mechanism by which paradigm succession occurs — a positive-feature framing in one paradigm becomes a negative-result need in the next.

**SG-G2-2: Review-as-paradigm-crystallization (Cherney 2015 specific).** The review functions as the documentation moment at which the Ni¹/Ni³ + precoordination + DKR/KR/DYKAT framework becomes legible as a coherent paradigm; this role is unique to the review-genre paper in G2. Worth preserving because it identifies a distinct gap class (cross-study aggregation without normalization; frontier prioritization without target inventory; mechanistic-framework crystallization across independent reaction types) not present in primary papers.

**SG-G2-3: Anode characterization absent in electrocatalytic paper (Pengfei 2024 U-3).** The anodic half-reaction is structurally absent from the proposed cycle despite a 55-pp yield difference between Fe and Zn anodes. This is a chemically concrete gap (specific reagent comparison, specific yield difference, specific cycle component absent) that would be lost if absorbed into IP-1 (general mechanism-validation absence). G2-specific because no other paper in the corpus uses electrocatalysis.

**SG-G3-1: Single-³¹P-shift identification of "active species" (Monnereau 2009 U-1).** A chemically concrete gap: an oxidation state assignment based on a single chemical shift (δ = 41.8 ppm) without corroborating EPR / UV-Vis / multinuclear NMR. Distinct from generic IP-1 because it identifies a specific characterization step that was performed but truncated. Sub-group-specific to G3.

**SG-G3-2: PES re-use across nine substrate classes (Molander 2016 U-7).** A specific testable hypothesis: a PES computed in SMD-water for benzylic / PhBr cannot, without re-computation, predict ΔΔG‡ for α-CF₃ / alkylsilicate / azaborine classes. The hypothesis is testable; the prediction is computable; the absence is documented. Worth preserving as a concrete instance of IP-6 (imported model) not subsumable into the abstract field-wide statement.

**SG-G3-3: ArMgBr vs Ar₂Mg active-species ambiguity (Morken 2016 CLA-2).** Chemically specific Schlenk-equilibrium gap: the cycle is drawn with ArMgBr but the aging protocol implies Ar₂Mg dominance, and the active transmetalating species is unidentified. Unique to G3 within the corpus because no other Kumada-style paper in G2/G1 foregrounds aging protocols.

These six sub-group findings are preserved in the field-level summary as concrete instances; they should not be absorbed into the abstract IP-1/IP-3/IP-6 statements without losing their chemical specificity.

---

**Stage 3 EP filling cross-reference (kumada_v184_sonnet_s3v2_en)**

The Kumada 1972 Stage 3 output (v18.4 / Sonnet) identifies six SRGs and two CLAs, with EP allocations EP-03a + EP-04a + EP-06a + EP-07a + EP-08a + EP-09a + EP-01a + EP-05a. Mapping the corpus's filling landscape to these EPs reveals:

| EP | What kumada1972 needs | Filled by which non-anchor papers? | Filling depth |
|---|---|---|---|
| EP-04a (discrimination/replication: R–R quantification) | Quantify Et-Et byproduct from EtMgBr/PhCl entry | **NEVER FILLED** in any of the 8 non-anchor papers. kumada1976b (12 pp + ~60 entries) does not report a byproduct audit; mazet2021 reports Figure 9 mass balance with ~75–85% gap; pengfei2024 reports per-substrate homo-coupling for some entries but not as discrimination test against the cycle's prediction. | 0% — the prediction generated by eq 3 has never been quantitatively tested in any descendant paper. This is the most striking integration-mode finding. |
| EP-06a (analogy validation: independent (dpe)Ni intermediate synthesis) | Synthesize and characterize [dpe-Ni(n-Bu)(Cl)] and [dpe-Ni(n-Bu)₂] | **PARTIALLY FILLED.** mazet2021 obtains X-ray of OA complex 9c (analogue of intermediate 2). breitenfeld2014 characterizes a different Ni-pincer system. No paper reports independently synthesized intermediate 1 analogue (diorganonickel) under dpe conditions. | ~25% — single intermediate characterized in one paper for a related (not isomorphous) ligand. |
| EP-03a (direct observation / state assignment: black-mixture characterization, mercury-drop test) | Distinguish homogeneous Ni(II) from heterogeneous Ni⁰ | **NEVER FILLED.** No paper in the corpus performs mercury-drop / hot-filtration / X-ray powder diffraction on the Kumada 1972 reaction mixture or analogous mixtures. cherney2015 reviews 427 references without citing such a test for the Ni¹/Ni³ manifold. | 0%. |
| EP-07a (boundary test: failed sp³ entry) | Run n-BuMgBr + n-BuCl under standard conditions, report 0% / <LOD | **PARTIALLY ADDRESSED.** breitenfeld2014 + pengfei2024 demonstrate that Csp³ Kumada is feasible under different catalyst systems — this addresses the boundary by counter-example, not by negative-result data within the dpe system. The original dpe-system boundary remains structurally untested. | ~40% — boundary is now known to be system-dependent, but the dpe-specific negative-result datum is still absent. |
| EP-08a (replication / uncertainty: independent runs of Examples 1, 2) | Replicate preparative examples; report range | **NEVER FILLED.** No paper in the corpus replicates kumada1972 entries. | 0%. |
| EP-09a (internal benchmark: shared-substrate yield comparison vs Tamura-Kochi or Corriu-Masse) | Single head-to-head numerical comparison on one shared substrate | **NEVER FILLED.** Across 8 non-anchor papers and ~600 entries combined, no head-to-head comparison with Tamura-Kochi Fe or Corriu-Masse Ni(acac)₂ on the kumada1972 EtMgBr/PhCl or n-BuMgBr/PhCl substrate has been published. | 0%. |
| EP-01a (reporting coherence: Table I footnote with method disclosure) | Internal-standard identity, response factors, full analytical method | **NEVER FILLED** (retroactive remediation of the 1972 Table I is not in scope of any descendant paper). | 0%. |
| EP-05a (quantitative ranking / TON for the six-catalyst comparison) | Per-catalyst yield in supplementary table | **NEVER FILLED.** No paper reports the kumada1972 six-catalyst comparison data in publishable form. | 0%. |

**Integration-level observation on EP filling:** of the 8 EPs allocated to kumada1972 by Stage 3 v18.4, **6 are 0% filled** (EP-04a, EP-03a, EP-08a, EP-09a, EP-01a, EP-05a) and **2 are partially filled** (EP-06a ~25%, EP-07a ~40% via paradigm-succession counter-example) across the entire 52-year descendant corpus. This is the strongest possible empirical demonstration of incentive-suppression: the EPs that would close kumada1972's gaps are structurally unfilled in 8 papers across 4 paradigms and 8 journals. The field has not produced the discrimination data, the replication data, the benchmark comparison, the reporting metadata, or the TON ranking that the v18.4 Stage 3 analysis identifies as the minimal evidentiary investment.

**Correspondence between IP hierarchy and EP filling order:** the field-wide IP hierarchy (IP-1 mechanism > IP-2 analytical > IP-3 self-contradictory > IP-4 selectivity > IP-5 benchmark > IP-6 imported > IP-7 DFT) does NOT correspond to the observed filling order. The EPs that have been even partially filled (EP-06a analogy validation; EP-07a boundary test) are the EPs that benefit from technological progress (X-ray; new catalyst systems). The EPs that are 0% filled (EP-04a, EP-03a, EP-08a, EP-09a, EP-01a, EP-05a) are the EPs that would yield only audit-type contributions — replication, mass-balance accounting, head-to-head benchmarking, reporting metadata, parameter ranking. **VQ hierarchy and filling order are anticorrelated:** the highest-VQ EPs (mechanism-validation: EP-06a, EP-03a) achieve the highest partial-filling rates because their resolution is structurally publishable; the lowest-VQ EPs (analytical / benchmark / replication) achieve the lowest filling rates because their resolution is incentive-suppressed. This anticorrelation is the integration-mode finding most relevant to Phase 2 deliverables.

---

**Comparative reading: how each EP traverses the corpus**

A second integration-mode pass examines each Stage 3 EP individually, tracking its trajectory through the descendant papers. This converts the EP catalogue from a static remediation list into a longitudinal forensic record of which gaps the field has chosen to address and which it has reproduced.

**EP-04a (discrimination / replication, R–R quantification).** The canonical Kumada 1972 instantiation: detect Et-Et byproduct from the EtMgBr/PhCl entry. The descendant trajectory: kumada1976b reports cumulative ~60 entries with no byproduct quantification per entry; mazet2021 reports Figure 9 stoichiometric data with 75–85% mass balance gap and presents the result as supporting selective interception rather than as a discrimination test; pengfei2024 reports per-substrate homo-coupling (17%/13% on substrates 1/2) but does so as a scope datum rather than as a test of the proposed selectivity model's predictions; breitenfeld2014 reports linear:cyclized ratio without total yields; monnereau2009 reports global <3% homocoupling without per-substrate breakdown; molander2016 reports no mass balance for compound 11; morken2016 reports no bis-coupling quantification despite design-feature (b) explicitly predicting suppression. **Pattern:** the experiment that would be a discrimination test in the kumada1972 frame becomes a scope datum in descendant papers. The shift in framing — from "test of a prediction" to "feature of the substrate scope" — is the mechanism by which EP-04a remains 0% filled while individual byproduct numbers proliferate.

**EP-06a (analogy validation, intermediate synthesis).** Trajectory: mazet2021 obtains X-ray of OA complex 9c (~25% filling — analogue of intermediate 2 only, under dppe not dpe, in non-catalytic isolation). breitenfeld2014 characterizes a Ni-pincer system not isomorphous with [NiCl₂(dpe)]; cherney2015 cites no dpe-Ni intermediate characterization across 427 references; pengfei2024 deploys Ni(I)/Ni(II)/Ni(III) intermediates in a different ligand framework; monnereau2009 obtains a single ³¹P shift for the "active species" without structural assignment; molander2016 inherits a PES from a third-party group without intermediate isolation; morken2016 proposes intermediates C/D/E without any spectroscopic data. **Pattern:** EP-06a is partially filled by intermediates that are *similar to* but not isomorphous with the kumada1972 intermediates. The descendant corpus has performed analogue characterization without performing the analogy-validation experiment that would close the kumada1972 SRG-1.

**EP-03a (direct observation: black-mixture characterization, mercury-drop test).** Trajectory: zero filling. No paper in the corpus performs a mercury-drop test, hot-filtration test, X-ray powder diffraction of precipitate, or ICP analysis of filtrate vs residue on any Ni-Kumada system. cherney2015 reviews 427 references without citing such a test for the Ni¹/Ni³ manifold despite the manifold's central reliance on homogeneous-vs-heterogeneous discrimination. **Pattern:** the homogeneity question, identified as a U-2 in kumada1972 (black mixture), persists as an unaddressed structural ambiguity through all paradigm transitions.

**EP-07a (boundary test: failed sp³ entry).** Trajectory: ~40% addressed by paradigm succession rather than by within-system negative-result data. breitenfeld2014 demonstrates Csp³ Kumada is feasible under nickel-pincer conditions (the boundary is system-dependent). pengfei2024 demonstrates Csp³–Csp³ electrochemical coupling. cherney2015 reviews stereoconvergent Csp³ coupling across hundreds of substrates. The kumada1972 dpe-system-specific negative-result remains untested: no paper reports n-BuMgBr + n-BuCl under [NiCl₂(dpe)] conditions. **Pattern:** the boundary in kumada1972 is now known to be system-dependent (a mechanistic insight unavailable in 1972), but the original system-specific negative-result datum that would have substantiated the boundary as stated remains absent.

**EP-08a (replication / uncertainty: independent runs of Examples 1, 2).** Trajectory: zero filling. No paper in the corpus replicates kumada1972 Examples 1 or 2 or any of the Table I entries. breitenfeld2014 reports "two independent trials per kinetic data point" but for its own data. pengfei2024 reports 63 yields with no replicates. **Pattern:** replication of historical data is structurally outside the publication-incentive landscape; descendant papers replicate their own data (variably) but never the founding paper's data.

**EP-09a (internal benchmark: shared-substrate yield comparison vs Tamura-Kochi or Corriu-Masse).** Trajectory: zero filling. Across ~600 entries combined in the descendant corpus, no head-to-head comparison with Tamura-Kochi Fe (concurrent prior art) or Corriu-Masse Ni(acac)₂ (footnote 3a in kumada1972) on the kumada1972 EtMgBr/PhCl or n-BuMgBr/PhCl substrate has been published. The closest approach is monnereau2009's single dppp comparison at one loading (not at the headline 50,000:1 regime). **Pattern:** the matched-pair comparison gap (IP-5) is most starkly visible in EP-09a's filling history: the founding paper's central comparative claim (vs prior transition-metal methods) is reproduced in every descendant paper without ever being subjected to numerical benchmarking on a shared substrate.

**EP-01a (reporting coherence: Table I footnote with method disclosure).** Trajectory: zero filling (and not in scope of any descendant paper). The retroactive remediation of historical reporting is structurally outside the publication landscape. **Pattern:** EP-01a is the EP for which "field-level filling" is conceptually impossible — only the original authors could close it, and the publication system does not provide a mechanism for retroactive metadata correction.

**EP-05a (quantitative ranking / TON for the six-catalyst comparison).** Trajectory: zero filling. The six-catalyst activity order in kumada1972 ([NiCl₂(dpp)] > [NiCl₂(dpe)] > [NiCl₂(dmpe)] > [NiCl₂(PEt₃)₂] > NiCl₂ > [NiCl₂(PPh₃)₂]) has not been reproduced as numerical yield data by any descendant paper. monnereau2009 introduces a different ligand class (calix[4]arene-diphosphine) and benchmarks against dppp at one loading. morken2016 introduces PyBox ligands. mazet2021 compares dppe vs dmpe but on a different substrate (enol phosphate vinylation). **Pattern:** ligand-effect data are reproduced in expanded form (different ligand classes) without the within-system numerical ranking that the original ligand-activity hypothesis presupposed.

**Integration-level synthesis of EP-by-EP trajectory.** The eight EPs allocated by the v18.4 Stage 3 analysis trace four distinguishable trajectories through the corpus: (i) zero filling, structurally unaddressed (EP-04a, EP-03a, EP-08a, EP-09a, EP-01a, EP-05a — 6 of 8 EPs); (ii) partial filling via analogous-but-non-isomorphous experiments (EP-06a — 1 of 8 EPs); (iii) partial filling via paradigm succession providing counter-example rather than negative-result data (EP-07a — 1 of 8 EPs); (iv) zero filling because the EP is structurally retroactive (EP-01a — already in (i) but distinguished by being unfillable in principle by any descendant paper). The 6:1:1 split places the corpus far below the threshold where one would expect descendant papers to address founding-paper EPs. The integration view confirms what the kumada1972 Stage 3 §6 institutional design memo (memory: project_v19_dev_cycle_state.md C27 codification proposal — "Success-driven question erasure") suggested: the field's evidentiary debt to its founding papers is structurally non-collectible.

---

**Anomalies (integration mode)**

- **A-1: One paper (Cherney 2015 review) accumulates 8 distinct U items**, more than three times the median (kumada1972: 2; corpus median: 4). Anomaly attributable to genre — the review aggregates primary-paper proposals as if established, multiplying self-contradictory absences at field level. Not a paper-level anomaly; a genre-induced amplification.
- **A-2: kumada1976b's first C–F oxidative-addition claim with zero isolated yield via an analytical method declared inapplicable in the adjacent table** (G1 RP-4, U-5). This is the most extreme self-contradictory absence in the corpus: a landmark claim asserted with no positive analytical support and an explicit footnote stating the method is inapplicable to the substrate class. Anomaly: it appears in the same paper that, four years after kumada1972, would be expected to remediate the founding paper's gaps; instead it generates a new gap of the most extreme type.
- **A-3: pengfei2024 360 mV CV-vs-DFT redox potential discrepancy undiscussed.** A specific quantitative discrepancy (Ni(I)/Ni(0) DFT −2.38 V vs SWV −2.74 V) is observable in the published text and represents a directly testable inconsistency that the paper does not acknowledge. Anomaly: this is the only case in the corpus where two within-paper measurements directly contradict each other by a quantifiable margin without rhetorical reconciliation.
- **A-4: 100% of EP-04a (R–R discrimination) remains unfilled across 52 years and 8 papers**, even though the experiment is one glpc run with an authentic standard. This is the integration-mode anomaly: the simplest experiment in the entire EP catalogue is the most reliably unperformed.

---

**Sub-group lens comparison (what each sub-group's frame uniquely reveals)**

The three sub-groups were constructed to apply independent analytical lenses to a shared anchor (kumada1972). Integration mode permits us to assess what each lens revealed that the others missed.

**G1 (lineage lens) reveals:** the *temporal trajectory* of the same gap within the same chemical system. Because all three G1 papers use related dpe/dppe-Ni catalysts with related substrates, divergences across years can be attributed to era / tools / journal-format rather than to system change. G1's unique contribution is the demonstration that across 49 years of the same chemistry, IPs 1–6 persist with shifting manifestation but invariant structure. G1's RP-5 (ligand attribution from confounded comparisons) is most clearly diagnosed in G1 because the within-paper comparison structure isolates the confound; G2 and G3 see the same gap at between-paper resolution where it is harder to isolate. G1 also uniquely surfaces RP-6 (genre-induced labeling mismatch) as a stable rhetorical convention reproducible across 49 years and 3 journals.

**G2 (boundary lens) reveals:** the *paradigm-discrimination structure* of the field. By including a review paper (cherney2015), G2 captures the moment at which a paradigm becomes legible as a coherent framework, which is invisible from a primary-papers-only frame. G2's unique contributions are: (a) Csp²/Csp³ boundary as the structural feature whose traversal generates the closed-shell → radical paradigm succession; (b) review-genre amplification of self-contradictory absence (cherney2015's 8 U items vs corpus median of 4); (c) the 360 mV CV-vs-DFT discrepancy in pengfei2024 as the corpus's only quantifiable within-paper inconsistency that goes undiscussed. The G2 lens also uniquely surfaces the *paradigm tension within Paradigm B* (Ni¹/Ni³ vs Ni⁰/Ni² with radical pairs), which is invisible from G1 (no radical paradigm members) and from G3 (G3's photoredox member is post-paradigm-establishment).

**G3 (expansion lens) reveals:** the *axis-orthogonality structure* of methodological innovation. G3's four papers expand kumada1972 along three independent axes (ligand architecture, photoredox activation, asymmetric desymmetrization) plus the original axis (no expansion, founding paper as anchor). The lens uniquely surfaces: (a) success-metric divergence (yield / TOF / paradigm framing / er) precluding cross-paper quantitative comparison even within a coherent group; (b) format-driven evidentiary depth analysis (3 pp Communication → 11 pp Account → 4 pp Communication → 7 pp Full Paper) demonstrating that format expansion does not eliminate the IPs; (c) RP-4 (benchmark superiority asserted) as a recurring pattern in its own right — G3 is the only sub-group that names this pattern as an independent recurring root, which is what allows IP-5 to surface in the integration view. G3 also uniquely surfaces the available-but-unutilized characterization sub-pattern via morken2016's SFC-method-undocumented gap.

**Lens-aggregation signature.** When the three lenses are aggregated, four IPs (IP-1, IP-2, IP-3, IP-4) appear in all three lenses — the field-wide structural conventions. Two IPs (IP-5, IP-6) appear in two lenses but are differently emphasized — IP-5 is foregrounded only in G3, IP-6 is foregrounded as a separate root only in G2 + G3. One IP (IP-7) is emergent and post-DFT and appears in two lenses (G2, G3) where post-DFT papers are members. This 3+2+2+1 distribution is the integration-mode signature of the field convention: gaps that are universally present are universally detected; gaps that are post-DFT or that require a specific analytical framing emerge only when the lens is sensitive to them. The integration-mode value is precisely that no single sub-group could have surfaced all seven IPs.

---

**Forensic projection: what would close the gap?**

Integration mode permits a final forensic question: given the EP filling landscape and the field-convention structure, what experimental package would close the integrated group_unasked_question? This is not a planning exercise but a diagnostic — the existence of a definable closure package is itself evidence that the gap is incentive-locked rather than tool-locked.

**Closure package P-1 (system-specific completeness, 1 paradigm, 1 system, 1 paper):** for any one Ni-Kumada system (e.g., [NiCl₂(dppe)] + n-BuMgBr + PhCl in Et₂O at 25°C), produce simultaneously: (a) replicate-based yield data for cross-product and homo-products with internal standards and response factors disclosed (closes IP-2 + IP-4 for that system, EPs 01a + 04a + 08a); (b) in-situ ³¹P NMR + UV-Vis monitoring of the Ni species across one full turnover (closes IP-1 partially, EP-03a); (c) independent synthesis and stoichiometric reactivity of a [(dppe)Ni(R)(X)] intermediate analogue (closes IP-6 partially, EP-06a); (d) integrated kinetic model with derived rate law fitted to time-course data (closes IP-1 + IP-3 partially); (e) head-to-head yield comparison vs Tamura-Kochi Fe and Corriu-Masse Ni(acac)₂ on the same substrate (closes IP-5, EP-09a); (f) failure-mode boundary tests with negative-result data for one Csp³ halide and one ortho-substituted aryl halide under the same conditions (closes IP-4 partially, EP-07a). Estimated investment: 6–9 months one full-time PhD student. Output: zero novel methodology; one comprehensive system-validation paper.

**P-1 is unpublishable as currently structured.** No high-impact journal would accept [REDACTED: substantial verbatim quotation; see Tier 9] as a standalone contribution. This is precisely the integration-mode finding that the gap is incentive-locked: the closure package is technically feasible, scientifically sufficient, and strategically unfundable.

**Closure package P-2 (cross-paradigm discrimination, 1 substrate, multiple paradigms):** for one shared substrate (e.g., n-BuMgBr + PhCl), compare under matched conditions: (i) [NiCl₂(dpe)] (closed-shell), (ii) Nickamine (radical pincer), (iii) [Ni/photoredox] (Molander conditions), (iv) electrochemical Ni (Pengfei conditions), and report yields, cross:homo ratios, kinetic orders, EPR detection, and DFT predictions for each. This is the cross-paradigm benchmark that the cherney2015 review treats as established but for which no single experimental study exists. Estimated investment: 18–24 months, one team. Output: paradigm-discriminating data for the cross-coupling field.

**P-2 is closer to publishable** because the cross-paradigm comparison is a novel meta-experiment, but it is structurally inverted from the field's reward gradient — the project's contribution is comparative rather than additive (no new method introduced), which limits its trajectory in the dominant journal-incentive structure.

**Closure package P-3 (review-led field correction, no new experiments):** a review that documents, system-by-system, the EP filling landscape across the field's published literature; identifies the systems for which P-1 closure has come closest; and prioritizes the closure investments by EP × paradigm × system. cherney2015 is the closest analogue but the review's logic is paradigm-establishing rather than gap-cataloging; the corrective review would invert the orientation. Estimated investment: 12 months, one author. Output: a meta-paper that converts incentive-locked gaps into a roadmap.

**P-3 is the most structurally aligned with publication incentives** because reviews can prioritize and roadmap without needing to perform experiments; the cost is the lack of new closure data. The Cherney 2015 example shows that reviews in this space are genuinely impactful.

**Integration-mode forensic conclusion:** all three closure packages exist and are technically feasible. The field's failure to produce them is fully explained by the incentive structure. The corpus's 0% filling rate on EPs 04a/03a/08a/09a/01a/05a is not a tools gap, not a knowledge gap, and not a single-paper-author oversight — it is a stable equilibrium of the publication-reward system. This is the integration-mode finding most relevant to the user's UQS Phase 2 deliverables: the corpus demonstrates empirically that even when the gap is precisely identified by Stage 3 EP allocation, the gap is reproduced rather than closed across 52 years of descendant work.

---

**Group-level unasked question (integration mode)**

Sub-group questions were:
- G1: [REDACTED: substantial verbatim quotation; see Tier 9]
- G2: [REDACTED: substantial verbatim quotation; see Tier 9]
- G3: [REDACTED: substantial verbatim quotation; see Tier 9]

**Assessment: Facets of a single underlying problem.** The three sub-group questions differ in framing (G1: completeness within one system; G2: discrimination across paradigms; G3: certification standard) but share a common structural object: the absence of a quantitatively closed, mechanistically validated, paradigm-discriminated account of any Ni-catalyzed cross-coupling for which model and measurement can be directly compared.

**Integrated group_unasked_question:**

[REDACTED: substantial verbatim quotation; see Tier 9]

evidence_chain: [Kumada_1972 : SRG-1 (A-2, U-1, U-2, B-12) + SRG-2 (B-6, U-1, C-1) + SRG-5 (B-2, B-7, B-9, B-11) + SRG-6 (C-1, C-2, A-4) + Stage 3 EP-04a/03a/06a/08a/09a 0% filling | Kumada_1976b : A-1, B-1, B-2, U-1, U-3, U-4, U-5 | Mazet_2021 : A-3, B-5, B-6, U-1, U-4 | Breitenfeld_2014 : A-1, U-1, U-2, U-4 | Cherney_2015 : U-1, U-3, U-8, CLA-1, CLA-2 | Pengfei_2024 : U-1, U-3, U-4, U-6 | Monnereau_2009 : A-1, U-1, U-2, U-3 | Molander_2016 : B-5, U-1, U-2, U-7 | Morken_2016 : B-5, U-1, U-2, CLA-2]

The integration question is the *single* underlying problem of which the three sub-group questions are facets:
- G1 (lineage facet) = within-system completeness — what would close the gap for one paradigm in one system?
- G2 (boundary facet) = cross-paradigm discrimination — what would establish that one paradigm is operative rather than a competing manifold?
- G3 (expansion facet) = certification standard — what would be sufficient evidence in principle, and has any paper met it?

All three facets converge on the same evidentiary deficit. The integration-mode synthesis adds the publication-incentive question (the "and what … structure has preserved this absence" clause): the corpus demonstrates that the absence is stably reproduced across paradigm transitions, format changes, and tool generations, which is the empirical signature of an incentive-locked rather than a tool-locked or oversight-locked field convention.

**Correspondence to recurring_roots (integration):** the integrated group_unasked_question subsumes recurring_root #1 (mechanism validation), #2 (analytical underreporting), #3 (selectivity / mass balance), #4 (self-contradictory absence), #5 (ligand attribution), #6 (computational benchmarking), and #7 (benchmark superiority) as constitutive components of a single field-level deficit. The 0% filling of EP-04a, EP-08a, EP-09a, EP-01a, EP-05a in the descendant corpus is the empirical mark that the deficit is incentive-locked — even when the v18.4 Stage 3 specifies the exact experiment, the experiment is not performed across 52 years.

**TEMPERATURE_SUMMARY correspondence:** in every paper in the corpus, the highest-convergence Stage 1 items concentrate exactly on the gap between the central mechanistic claim and its experimental support (kumada1972 B-1/B-4 3/3; kumada1976b A-4/B-7/B-8 3/3; mazet2021 A-3/B-5/B-7 3/3; breitenfeld2014 B-4 3/3; cherney2015 U-1 3/3; pengfei2024 U-6 3/3 critical; monnereau2009 U-1/U-2 3/3; molander2016 B-5/U-1 3/3; morken2016 B-5/B-6 3/3). The integrated group_unasked_question maps directly onto the convergent multi-agent signal in 9 of 9 papers — the strongest multi-paper, multi-agent confirmation possible in the v18.4 Stage 1 framework that the deficit is field-wide rather than per-paper.

---

**Methodological note (integration mode): how the v18.4 prompt set surfaced these patterns**

The integration-mode reading is enabled by specific v18.4 features that were absent or weaker in earlier prompt versions. For the cross-model verification record (memory: project_v19_dev_cycle_state.md C27/C28/C29 codification proposals), this section records which v18.4 features carried which load.

**v18.4 Stage 1 features that surfaced the corpus's IP structure:**

(1) The cross_field_temperature data (V1/V2/V3 multi-agent severity profiles per item) made the convergence-vs-divergence distinction visible at item resolution. Without this, IPs would surface only at the recurring-root resolution of v17 and earlier, missing the gradient of confidence within each IP. The temperature-pattern analysis in this output (rising convergence for IP-1 across eras; high uniformity for IP-3 across all papers; rising-with-era for IP-7) is conditioned on this feature.

(2) The same_root_groups in META made the within-paper structural clustering of items machine-readable, which is the unit of evidence the integration mode aggregates across sub-groups. The recurring_root analysis would not have been possible without per-paper SRG identification.

(3) The U-item rubric (capturing items not classifiable as A/B/C/U) became more explicit in v18.x, allowing self-contradictory absence to surface as a coherent recurring pattern rather than as scattered residual items. Without this, the 28 U items across 9 papers would have been distributed across A/B/C as approximations, masking the integration-mode finding that "model → prediction → untested" is a distinct epistemic category.

(4) The Stage 3 v2 EP catalogue (RI → ER → EP crosswalk) provided the institutional design language that allows the EP filling cross-reference to function as an integration-mode forensic. Without explicit EP allocation per SRG/CLA, the corpus's filling landscape could not be quantified, and the 6:1:1 split (zero-filled / partial-via-analogue / partial-via-paradigm-succession) could not be derived.

(5) The Stage 3 v2 §6 institutional design notes (Labeling mismatch, RI-04+RI-06 co-occurrence, Automatic-resolution pattern) provide the theoretical scaffolding for the integration-mode IP-couplings (C-α through C-δ above). The Stage 3 v18.4 §6 codification candidates (PRI-12: mechanism-kinetics decoupling) are independently corroborated by the integration view across sub-groups.

**v18.4 Stage 2F v7.1 features that surfaced the integration view:**

(1) The integration-mode requirement to identify field-wide IPs *independent of the shared anchor* prevents the Kumada 1972 anchor from dominating the cross-paper signal. By drawing the IP evidence chains exclusively from non-anchor papers, the integration-mode reading isolates the field convention from the founding-paper structure.

(2) The sub-group-specific pattern preservation requirement (v7.1 addition) prevents the abstract field-wide IPs from absorbing chemically concrete sub-group findings. The 6 SG findings recorded above (Csp²/Csp³ boundary; review-as-paradigm-crystallization; anode characterization absent; single-³¹P-shift identification; PES re-use across substrate classes; ArMgBr vs Ar₂Mg ambiguity) would have been lost if absorbed into IP-1/IP-3/IP-6 statements without the v7.1 preservation rule.

(3) The integration-mode group_unasked_question synthesis instruction (assess sub-group questions as independent vs facets-of-single-problem) produced the unified question above. Without this instruction, the three sub-group questions would have been concatenated rather than synthesized.

**Cross-paper-batch Phase 2 implications:**

(a) The 0% filling rate of EP-04a, EP-08a, EP-09a, EP-01a, EP-05a across 8 descendant papers and 52 years is an empirical demonstration that the v18.4 EP catalogue identifies gaps that the publication-incentive system reproducibly fails to close. This confirms — at the corpus level — the user-memory observation (project_uqs_long_term_vision.md) that UQS captures a structural debt that the field's reward system cannot collect on its own. The integration-mode reading is the strongest available empirical evidence for this thesis.

(b) The lens-aggregation signature (3+2+2+1 IP-detection distribution across G1/G2/G3) suggests that single-sub-group analysis underestimates the field-wide convention by approximately 40% (IPs 5, 6, 7 are detectable only when the lens is sensitive to them). For Phase 2 cross-vendor / cross-language verification work, this implies that integration-mode multi-sub-group designs are required to achieve full IP enumeration — a single-frame Stage 2F output is sufficient for hypothesis generation but not for hypothesis exhaustion.

(c) The reconciliation table for suppression-mode classification (G1 = G2 = G3 for all 7 IPs) is methodologically significant because it demonstrates that the v18.4 suppression-mode diagnostic (individually chosen / structurally suppressed / incentive-suppressed / era-dependent) is lens-invariant. This is one of the criteria for promoting the diagnostic from heuristic to formal protocol — Phase 2 should examine whether the lens-invariance holds for other corpora (out-of-sample test).

(d) The integration-mode finding that IP-couplings (C-α through C-δ) tighten the seven independent IPs into four functional clusters has implications for the v19 codification proposals. Specifically, C-α (IP-1 ↔ IP-6) suggests that the imported-model RI (RI-06) and the unobserved-explanatory RI (RI-03) are operationally a single RI viewed from two angles; C-β (IP-3 ↔ IP-1) is the structural argument for the C27 codification proposal (Success-driven question erasure as a cross-paper anchor); C-γ (IP-2 ↔ IP-4) is the empirical foundation for an incentive-locked-pair codification candidate that has not yet been formally proposed but is implied by the corpus.

These methodological observations are records, not recommendations. Their formal integration into v19 prompt revisions or Phase 2 protocols is a separate task downstream of this 2F output.

---

*End of integrated "all" output.*

---

> **Tier 8 redaction notice**: This file is a redacted copy of the corresponding Tier 3 / Tier 9 output. Verbatim source-paper quotations have been replaced by `[REDACTED: see source paper §<loc>; full text retained in Tier 9 reviewer-only deposit]` markers, preserving location references and our own analytical content. Bibliographic fields (title, authors, journal, year, DOI), analytical labels (`evidence_chain:` with B-/U-/A-/C- internal IDs), short technical terms, and our own analytical text are not redacted. The redaction was applied by `scripts/redact_for_tier8.py` and, for this version, by `scripts/build_paperA_R1_public.py` with `scripts/redact_source_ngram_runs.py` (scripts of the project repository; they are not deposited).
