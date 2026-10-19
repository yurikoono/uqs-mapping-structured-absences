prompt_version: stage2f-v7-20260417

---

**[F. Within-Group Comparison]**

**Group composition:** G2 — Boundary Breakthrough (Csp³ frontier, 1972–2024)
- Kumada 1972 (JACS Communication): Ni-catalyzed Csp²–Csp² and Csp²–Csp³ cross-coupling; Csp³ halides explicitly excluded.
- Breitenfeld 2014 (Organometallics Full Paper): Ni-pincer (Nickamine) catalyzed alkyl(sp³)–aryl Kumada coupling via radical bimetallic OA; transmetalation as TDS.
- Cherney 2015 (Chem. Rev. Review): comprehensive enantioselective/enantiospecific cross-coupling survey, organized around the DKR/KR/DYKAT framework and Ni¹/Ni³ manifold.
- Pengfei 2024 (Nature Catalysis): Ni-electrocatalyzed Csp³–Csp³ cross-electrophile coupling of unactivated alkyl halides via Ni(I/II/III) cycle.

---

**Repeated patterns**

**RP-1: Mechanistic cycle proposed without elementary-step validation under the operating catalytic system.**

All four papers propose multi-step catalytic cycles whose key intermediates and elementary steps are not directly observed under the conditions in which the cycle is claimed to operate.

evidence_chain: [Kumada_1972 : A-2, B-12, U-2 → [REDACTED: substantial verbatim quotation; see Tier 9] | Breitenfeld_2014 : A-1, B-3, U-1, U-2 → [REDACTED: substantial verbatim quotation; see Tier 9] | Cherney_2015 : U-1, B-6, C-5 → [REDACTED: substantial verbatim quotation; see Tier 9] | Pengfei_2024 : U-6, B-7, CLA-1 → "reductive elimination via dialkyl–Ni(III) complexes is preferred"]

- Kumada 1972: Ni(0)/Ni(II) cycle (eqs 2–4) imported by analogy with stoichiometric (dipy)Ni reactions; no intermediate 1, 2, or 3 directly observed under [NiCl₂(dpe)] conditions; "black mixture" observation consistent with Ni⁰ formation but not characterized.
- Breitenfeld 2014: Figure 8 catalytic cycle proposed with intermediates 10–16; none directly characterized under the alkyl–aryl operating conditions; the comproportionation step (16 + 14 → 11 + 13) is imported from the alkyl–alkyl predecessor (ref 20) without isomorphism demonstration; the observed catalyst decomposition at room temperature is treated as a practical problem solved by cooling rather than as a mechanistic observable.
- Cherney 2015: the Ni¹/Ni³ manifold underpinning sections 2.2.1–2.2.3 rests entirely on DFT (Lin et al.); no EPR, CV, or stoichiometric organometallic characterization of Ni¹ or Ni³ intermediates under catalytic turnover conditions is cited across 66 pages and ~427 references; the precoordination model (Figure 6) is similarly imported from organometallic coordination chemistry without kinetic isomorphism evidence in catalysis.
- Pengfei 2024: the Ni(I/II/III) cycle (Fig. 5c) rests on a 2.8 kcal mol⁻¹ DFT barrier preference (RE via Ni(III) at 13.4 vs. Ni(II) at 16.2 kcal mol⁻¹) without disclosed functional/basis set/solvation, without spin-state assignment for open-shell Ni(I/III), and without direct EPR detection of the Ni(I) species A; the anodic half-reaction is structurally absent from the proposed cycle despite a 55-pp yield difference between Fe and Zn anodes.

---

**RP-2: Quantitative analytical basis for primary data underreported.**

Across all four papers the central numerical claims rest on measurements whose reliability cannot be independently evaluated.

evidence_chain: [Kumada_1972 : B-2, B-7, B-9, B-11 | Breitenfeld_2014 : B-2, B-4, B-7 → "two independent trials were conducted for each experiment"; "about second order in catalyst" (slope 1.7) | Cherney_2015 : B-2, B-15 → "comparisons should be drawn with caution"; "approximately 5 times faster" | Pengfei_2024 : B-1, B-4, B-9 → "44%, from CH₃I" (only example using methyl iodide); no Faradaic efficiency at gram scale]

- Kumada 1972: Table I mixes glpc-only (5 entries) and isolated yields (5 entries); no internal-standard identity, no replicate runs, no analytical method disclosed for the cis:trans 80:20 / 43:57 ratios.
- Breitenfeld 2014: only two independent trials per kinetic data point (Figs. 5–7); rate-order slopes (1.7 catalyst, 2.0 Grignard, −0.3 alkyl iodide) reported as "about second order" / "zeroth order" without confidence intervals; radical-clock GC yields and conversions present in the procedure but not reported.
- Cherney 2015: Figure 5 ligand survey aggregates conditions across studies with explicit "comparisons should be drawn with caution" caveat but no corrective normalization; s ≈ 5 atropisomer kinetic resolution stated without Kagan–Duplomb conversion-dependent ee analysis method disclosed; no rate constants for any DKR/KR/DYKAT regime assignment.
- Pengfei 2024: 63 isolated yields with no replicate measurements; mass balance not closed (cross product 85% on substrate 1, secondary homo 17% on substrate 2, primary homo 13% on substrate 1 — fates of remaining ~15% / ~70% unaccounted); gram-scale yields drop substantially (85→69%, ~60→45%) without Faradaic efficiency or cathode potential reported.

---

**RP-3: Self-contradictory absence — proposed model generates predictions that are not tested.**

In all four papers a proposed model (catalytic cycle, mechanistic regime, selectivity model) generates specific observables that the paper does not test, while the model is retained as the explanatory framework.

evidence_chain: [Kumada_1972 : U-1 → eq 3 predicts R–R, no R–R reported | Breitenfeld_2014 : U-1, U-3, U-4 → DFT barriers asserted with acknowledged but unquantified uncertainty; rate law not derived | Cherney_2015 : U-1, U-3, U-8 → Ni¹/Ni³ predicts EPR; DKR predicts k_rac ≫ k_coup; DET predicts equal rates from both enantiomers — none tested | Pengfei_2024 : U-1, U-4, U-5 → selectivity model predicts negligible primary homocoupling at 1° deficiency; CV vs. kinetic data point to different rate-determining steps]

- Kumada 1972: catalytic cycle eq 3 ("L₂NiR₂ + R'X'' → L₂Ni(R')(X'') + R–R") explicitly predicts R–R as stoichiometric byproduct of the propagation step; Table I reports no R–R from any entry, neither as detection limit nor as upper bound.
- Breitenfeld 2014: "complete catalytic cycle" predicts intermediates 10–16 (none observed), eq 3 redistributive transmetalation predicts a specific algebraic rate law (never derived), bimetallic-OA-vs-escape-rebound discrimination via DFT acknowledges B2 energetics "is best accomplished through molecular dynamics simulations" but uses static DFT for the mechanistic conclusion.
- Cherney 2015: Ni¹/Ni³ predicts EPR-active intermediates (no EPR cited); DKR regime predicts k_rac/k_coup inequalities (no rate constants measured); DET predicts equal product ee and equal rates from enantiopure (R)- vs. (S)-313 (single experiment never run); SET cycle predicts Ir(II) and Ni(III) intermediates (never spectroscopically observed).
- Pengfei 2024: DFT-calculated Ni(I)/Ni(0) potential (−2.38 V) and SWV-measured value (−2.74 V) disagree by 360 mV without discussion; the selectivity model predicts secondary homo suppression under 3:1 secondary excess and negligible primary homo under 1° deficiency, yet 17% + 13% homocoupling persists; the DFT initiation barrier (~20 kcal mol⁻¹) implies SET is overall RDS while the kinetic interpretation of Fig. 4b assumes radical addition is rate-controlling.

---

**RP-4: Selectivity / scope claim without complete byproduct or boundary accounting.**

Papers making selectivity or scope claims report product yields without quantifying competing pathways or substantiating exclusion boundaries with negative-result data.

evidence_chain: [Kumada_1972 : B-1, B-4, B-6 → "selective" without cross:homo ratio; "Only Csp² halides … can be used[REDACTED: substantial verbatim quotation; see Tier 9]unifying reaction pathway[REDACTED: substantial verbatim quotation; see Tier 9]excellent chemoselectivity" supported by single competition experiment; "underdeveloped area of great synthetic promise[REDACTED: substantial verbatim quotation; see Tier 9]general strategy" while 2°–2° / 1°–3° require different L11/DMA system in caption footnote; no head-to-head comparison with Lin (ref 60) or Gong (refs 29–30)]

- Kumada 1972: title-level "selective cross-coupling" claim with no cross:homo ratio for any of 10 entries; sp² restriction asserted as positive feature without a single failed sp³ datum.
- Breitenfeld 2014: radical-clock ratios reported without total yields/conversions (mass-balance artifact possible); "unifying reaction pathway" claim extends to alkyl–alkynyl Kumada and alkyl–aryl Suzuki without mechanistic data.
- Cherney 2015: "excellent chemo- and regioselectivity" for Cu/L101 supported by a single aryl bromide competition; five frontier areas defined as "underdeveloped" without an inventory of specific targets inaccessible by current methods or comparison with alternative methods (enzymatic, organocatalysis).
- Pengfei 2024: "general strategy" claim across four substrate classes is structurally undercut by an unexplained ligand bifurcation (L2/DMF for 1°–2°/1°–1° vs. L11/DMA for 2°–2°/1°–3°) disclosed only in a figure caption footnote; no head-to-head numerical comparison with Lin 2022 or Gong 2011/2013 prior art on shared substrates.

---

**RP-5: Computational / theoretical models deployed as mechanistic discriminants without protocol benchmarking or experimental cross-validation.**

Three of the four papers (the one pre-DFT exception is Kumada 1972) use computational results as the primary or sole basis for distinguishing mechanistic alternatives, without benchmarking the protocol against higher-level methods or experimental observables.

evidence_chain: [Breitenfeld_2014 : U-1, U-3, U-5, B-5 → 18.7 kcal mol⁻¹ pathway selectivity from PBE0-dDsC/TZ2P//M06/def2-SVP without benchmarking, RRHO entropy uncorrected, PES scan truncated at 4.0 Å, propyl model for hex-5-en-1-yl | Cherney_2015 : U-1, U-8, C-5, C-9, CLA-1 → Ni¹/Ni³ via Lin et al.; DET via unnamed computational study; Sawamura γ-arylation mechanism — three independent reaction types where DFT proposals are presented as operative without experimental tests | Pengfei_2024 : U-6, SRG-1, SRG-10 → 2.8 kcal mol⁻¹ Ni(III)-vs-Ni(II) RE preference without functional/basis set disclosed, without spin multiplicity, without uncertainty estimate]

Note: Kumada 1972 predates DFT; the analog in that paper is the import of stoichiometric (dipy)Ni mechanism by chemical analogy (RP-1).

---

**Cross-field temperature patterns**

temperature_pattern: RP-1 (mechanism validation) | papers: [Kumada_1972, Breitenfeld_2014, Cherney_2015, Pengfei_2024] | profile_consistency: consistent | note: Mechanism validation gaps receive consistently high severity from the mechanistic-agent perspective across all four papers (Kumada A-2 V1=high V2=high; Breitenfeld U-1 critical / V1+V3 compound; Cherney U-1 V1=high V2=high V3=high 3/3 convergence; Pengfei U-6 critical / 3/3 convergence). The convergence is highest in the two most recent papers (Cherney 2015 and Pengfei 2024 both reach 3/3 on the central mechanism-validation gap), suggesting that as the field matures the mechanism-validation expectation strengthens across viewpoints.

temperature_pattern: RP-2 (analytical underreporting) | papers: [Kumada_1972, Breitenfeld_2014, Cherney_2015, Pengfei_2024] | profile_consistency: consistent | note: Analytical reporting gaps receive medium-to-high severity from the analytical-agent perspective across all four papers. Cross-paper severity is roughly invariant: Kumada 1972 B-2 (V1=medium, V3=medium); Breitenfeld 2014 B-4 (3/3 convergence, all high); Cherney 2015 B-2 (single agent, explicit author caveat in text); Pengfei 2024 B-1 (V1=medium, single agent). Reporting conventions for replicate data and mass balance have not improved despite increased analytical capability across 52 years.

temperature_pattern: RP-3 (self-contradictory absence) | papers: [Kumada_1972, Breitenfeld_2014, Cherney_2015, Pengfei_2024] | profile_consistency: consistent | note: Self-contradictory absences receive high severity uniformly from whatever agent flagged them, but cross-field convergence on these items is variable: Kumada U-1 V2+V3=high 2/3; Breitenfeld U-1 critical at synthesis level (V1+V3 compound); Cherney U-1 3/3 V1+V2+V3=high; Pengfei U-1 V1+V2=medium 2/3, U-6 V1+V2+V3 3/3 critical at one of the two clusters. The pattern receives strongest cross-field convergence in the review (Cherney) where multiple agents read the same DFT-without-experimental-test pattern from different angles.

temperature_pattern: RP-4 (selectivity/scope without accounting) | papers: [Kumada_1972, Breitenfeld_2014, Pengfei_2024 strongly; Cherney_2015 partially] | profile_consistency: consistent | note: Selectivity and scope-boundary gaps receive convergent high severity in Kumada 1972 (B-1 / B-4 / B-6 across 2/3 to 3/3 convergence) and Pengfei 2024 (U-1 + B-3 across 2/3 convergence). Cherney 2015's scope-without-failure-inventory pattern (CLA-2) is single-agent V2 because review-format scope claims are diagnostic of V2's "field cartography" lens specifically.

temperature_pattern: RP-5 (DFT as discriminant) | papers: [Breitenfeld_2014, Cherney_2015, Pengfei_2024] | profile_consistency: consistent | note: DFT-without-experimental-validation receives 3/3 convergence at high or critical severity in all three post-DFT papers. Pengfei 2024 U-6 reaches 3/3 V1=high V2=high V3=high (the strongest convergence in any paper of the group). The temperature_gap is consistently small (none or low) across all three papers, indicating that the gap is recognized uniformly across mechanistic, synthetic, and computational viewpoints.

---

**Same-root group patterns**

recurring_root: Catalytic cycle assembled from imported analogy or DFT without elementary-step validation in the operating system | papers: [Kumada_1972, Breitenfeld_2014, Cherney_2015, Pengfei_2024] | member_items: [Kumada_1972: SRG-1 (A-2, U-1, U-2, B-12), Breitenfeld_2014: SRG-7 (A-1, U-2) + SRG-2 (U-1, U-5, B-5), Cherney_2015: SRG-2 (U-1, C-5, B-6), Pengfei_2024: SRG-1 (U-6 cluster) + SRG-9 (Path I/II discrimination)] | note: Field-wide structural pattern that persists across 52 years and across genres (communication, full paper, review, full paper) and across mechanistic regimes (2-electron Ni⁰/Ni², 1-electron Ni¹/Ni³, electrochemical Ni(I/II/III)). The mechanism is proposed by analogy or DFT; the elementary steps are not directly observed in the system claimed; the cycle is retained as the explanatory framework.

recurring_root: Quantitative measurement basis underreported (replicate, mass balance, internal standard, uncertainty) | papers: [Kumada_1972, Breitenfeld_2014, Cherney_2015, Pengfei_2024] | member_items: [Kumada_1972: SRG-5 (B-2, B-7, B-9, B-11), Breitenfeld_2014: SRG-1 (B-1, B-2, B-7) + SRG-6 (B-4), Cherney_2015: B-2 / B-15 (no SRG, review format aggregation), Pengfei_2024: SRG-8 (B-1, B-6) + B-4 (Faradaic efficiency)] | note: Genre convention across all four eras (1972 JACS Comm., 2014 Organometallics, 2015 Chem. Rev., 2024 Nat. Catal.) — none enforces replicate-based uncertainty, raw data deposition, or full mass balance closure; the format-specific manifestations differ but the gap is invariant.

recurring_root: Selectivity / scope claim without quantitative byproduct or boundary accounting | papers: [Kumada_1972, Breitenfeld_2014 (partial), Cherney_2015, Pengfei_2024] | member_items: [Kumada_1972: SRG-2 (B-6, U-1, C-1) + SRG-3 (B-4, A-3), Breitenfeld_2014: A-4 + C-5 (unifying claim across reactions not tested), Cherney_2015: SRG-5 (B-11) + CLA-2 (frontier prioritization without inventory), Pengfei_2024: SRG-7 (B-3) + SRG-8 (mass balance)] | note: The same gap appears across the 1972 founding paper and the 2024 extension despite 52 years of methodological development; in the review (Cherney) it manifests as frontier prioritization without target inventory; in the recent papers (Breitenfeld 2014, Pengfei 2024) as scope generalization across reaction types where mechanistic data exist for only some.

recurring_root: Computational mechanism deployed as discriminant without benchmarking or experimental cross-validation | papers: [Breitenfeld_2014, Cherney_2015, Pengfei_2024] | member_items: [Breitenfeld_2014: SRG-2 (U-1, U-5, B-5), Cherney_2015: SRG-8 (U-1, U-8, C-5, C-9), Pengfei_2024: SRG-1 + SRG-2 + SRG-10 (U-6 cluster)] | note: Emergent root present only in post-DFT papers. The pattern intensifies: by 2024 (Pengfei) the central mechanistic claim rests on a 2.8 kcal mol⁻¹ DFT difference whose uncertainty range likely exceeds the discriminating gap.

---

**Temporal trajectory of recurring patterns**

temporal_trajectory: RP-1 (mechanism validation) | classification: shifting | transition_point: ~2000 (emergence of radical Ni catalysis) and ~2010 (DFT becomes default mechanistic discriminant) | note: 1972 Kumada — 2-electron Ni(0)/Ni(II) cycle proposed by analogy with stoichiometric (dipy)Ni; era-tolerated as no radical-clock, no DFT, no in-situ spectroscopy was available. 2014 Breitenfeld — radical mechanism investigated with radical-clock probes and DFT; tools deployed but DFT becomes the sole pathway discriminant with acknowledged imprecision. 2015 Cherney — review formalizes the Ni¹/Ni³ manifold across an entire subfield (sections 2.2.1–2.2.3) on DFT alone, without any cited EPR/CV characterization across 427 references. 2024 Pengfei — electrochemical mechanistic probes (CV, SWV) deployed but Path I / Path II discrimination remains unresolved and the central 2.8 kcal mol⁻¹ DFT preference is reported without method disclosure. The gap shifts from "no tools" (1972) to [REDACTED: substantial verbatim quotation; see Tier 9] (2014–2024). Cherney 2015 is the documentation point at which the shift is visible as a field-level norm rather than an individual-paper choice.

temporal_trajectory: RP-2 (analytical underreporting) | classification: time-invariant | transition_point: n/a | note: Reporting standards have not improved despite increased analytical capability — 1972 reports glpc yields without conditions and ratios without methods; 2014 reports rate orders without confidence intervals and only two independent trials; 2015 review aggregates ee values across studies with explicit caveat but no normalization; 2024 reports 63 isolated yields with no replicates and no Faradaic efficiency at gram scale. The character of the gap is essentially unchanged across 52 years.

temporal_trajectory: RP-3 (self-contradictory absence) | classification: time-invariant | transition_point: n/a | note: The specific untested predictions change (R–R in 1972; intermediates 10–16 + rate law in 2014; EPR / k_rac/k_coup / DET enantioconvergence in 2015; selectivity model + CV-vs-kinetic / RDS assignment in 2024), but the structural pattern — model predicts observable, observable not tested, model retained as explanatory framework — is invariant across all four papers and all formats.

temporal_trajectory: RP-4 (selectivity/scope without accounting) | classification: time-invariant | transition_point: n/a | note: 1972 reports "selective" cross-coupling without cross:homo ratio and "Only Csp² halides can be used" without failed sp³ example; 2024 reports "general strategy" across four substrate classes while requiring an unexplained catalyst bifurcation for two of those classes. Mass balance closure is absent in both the founding paper and the 2024 extension.

temporal_trajectory: RP-5 (DFT as discriminant without benchmarking) | classification: emergent | transition_point: ~2005–2010 (DFT becomes routine in organometallics) | note: Pattern is absent in Kumada 1972 (predates DFT) and intensifying across the post-2010 corpus. By Cherney 2015 it is documented as a systemic field-level pattern (CLA-1 / SRG-8 spans three independent reaction types in a single review). By Pengfei 2024 the central mechanistic conclusion rests on a 2.8 kcal mol⁻¹ DFT preference without disclosed protocol — the uncertainty range likely exceeds the discriminating gap.

---

**Structural suppression vs. individual choice**

RP-1 (mechanism validation):
- *Era-dependent → individually chosen / methodologically limited.* In 1972 (Kumada), structurally suppressed: no radical probes, no DFT, no in-situ spectroscopy. By 2014 (Breitenfeld) and 2024 (Pengfei), tools exist (radical-clock, DFT, CV, SWV, EPR feasible) but are not deployed at the resolution that would discriminate alternatives. By 2015 (Cherney) the gap is field-level: 427 references span the field, EPR characterization of Ni(I)/Ni(III) was technically feasible by the time of review, yet no paper in the corpus had cited it under catalytic turnover conditions for the systems unified under the Ni¹/Ni³ framework.

RP-2 (analytical underreporting):
- *Incentive-suppressed.* Replicate kinetic data, calibrated GC mass balance, internal-standard disclosure, Faradaic efficiency, and Kagan–Duplomb conversion-dependent ee analysis are technically feasible across all four papers but constitute work that does not generate a publishable contribution in its own right. The incentive structure of organometallic / electrosynthesis / asymmetric catalysis journals does not reward replicate-based audit work; format constraints (communication 3-page, full paper 8-page, review 66-page over 427 refs, full paper Nature Catalysis) compound this by displacing analytical metadata to caveats, footnotes, and Supplementary material.

RP-3 (self-contradictory absence):
- *Individually chosen.* Each untested prediction is testable with the paper's own infrastructure: R–R formation testable by glpc (Kumada); intermediates 10–16 testable by stoichiometric NMR (Breitenfeld); EPR of Ni(I) / Ni(III) under turnover conditions feasible by 2010 (Cherney); CV-vs-kinetic reconciliation by Eyring analysis or steady-state derivation (Pengfei). The persistence of the gap across formats and eras suggests that "individually chosen" combines with "incentive-suppressed": each paper could test its own predictions but doing so is not rewarded by the publication system.

RP-4 (selectivity / scope without accounting):
- *Incentive-suppressed.* A complete byproduct audit and mass balance for any one of these systems would constitute a stand-alone analytical paper that no high-impact journal would publish; a complete frontier-prioritization inventory (Cherney CLA-2) would constitute a separate review of unmet need. No group in the field has published either kind of audit for Ni-catalyzed cross-coupling.

RP-5 (DFT as discriminant without benchmarking):
- *Era-dependent → individually chosen.* In 2014 (Breitenfeld), benchmarking against DLPNO-CCSD(T) for open-shell Ni(III) systems was possible but not yet a universal expectation. By 2018+, the expectation crystallizes (Houk-group recommendations, Grimme quasi-RRHO, organometallic DFT benchmarking literature). By 2024 (Pengfei), the absence of method disclosure and uncertainty quantification is a clear individually-chosen omission given that the protocols and benchmarks are widely available.

---

**Paradigm competition**

This group reveals a clear **paradigm succession** with one persistent field-invariant gap, plus a **co-existing paradigm tension** documented in the review.

**Paradigm A: Two-electron Ni(0)/Ni(II) closed-shell cycle (1972).**
Kumada 1972 proposes oxidative addition → transmetalation → reductive elimination via diorganonickel intermediate 1, with selectivity arising from the cis-geometry of the diorganonickel intermediate enforced by bidentate phosphine. Restricted to Csp² electrophiles.

Systematically unanswered question by Paradigm A:
- Why are Csp³ halides excluded? What mechanistic feature prevents oxidative addition or subsequent steps with Csp³ electrophiles?
  evidence_chain: [Kumada_1972 : B-4 → [REDACTED: substantial verbatim quotation; see Tier 9]; "no textual basis in Kumada_1972" for the mechanism of exclusion — the boundary is asserted but not explained]

**Paradigm B: One-electron radical Ni(I)/Ni(II)/Ni(III) cycle (2014, 2024).**
Breitenfeld 2014 and Pengfei 2024 propose that Csp³ halides undergo radical activation via SET from Ni(I) or Ni(0), generating carbon radicals that are captured by Ni(II) species to form Ni(III) alkyl intermediates that undergo reductive elimination. Cherney 2015 formalizes this paradigm as the standard framework for stereoconvergent coupling of secondary alkyl electrophiles across sections 2.2.1–2.2.3.

Systematically unanswered questions by Paradigm B:
- Are the proposed Ni(I) and Ni(III) intermediates directly observable under turnover conditions, or does the paradigm rest entirely on DFT?
  evidence_chain: [Breitenfeld_2014 : U-1 → DFT alone discriminates pathways; Cherney_2015 : U-1 → "no textual basis in Cherney_2015" for any cited EPR/CV characterization across 427 refs; Pengfei_2024 : U-6 → 2.8 kcal mol⁻¹ DFT preference without protocol]
- What is the quantitative selectivity mechanism that suppresses homocoupling between two radicals derived from two different alkyl halides?
  evidence_chain: [Pengfei_2024 : B-3, U-1 → "see Supplementary Discussion on the Selectivity for details"; Breitenfeld_2014 : B-3 → rate-law derivation absent]
- For the closely related DKR / KR / DYKAT regime assignments invoked by Cherney 2015, are the rate-constant inequalities (k_rac vs. k_coup) measured for any Grignard substrate?
  evidence_chain: [Cherney_2015 : U-3 → [REDACTED: substantial verbatim quotation; see Tier 9]]

**Succession relationship.** Paradigm B's founding problem (Csp³ coupling) is precisely Paradigm A's acknowledged blind spot. By 2014 no group proposes a 2-electron mechanism for Csp³ alkyl halide coupling under Ni catalysis; the radical paradigm has supplanted the closed-shell paradigm for this substrate class. This is paradigm succession, not paradigm competition.

**Co-existing paradigm tension within Paradigm B (Cherney 2015 documentation).** Within radical Ni catalysis, two sub-paradigms coexist for electronic-structure assignment: (a) Ni¹/Ni³ oxidation-state manifold (Lin et al. DFT, dominant in stereoconvergent secondary alkyl coupling); (b) Ni⁰/Ni² with radical pairs (alternative not foreclosed by experiment). Cherney 2015 documents the field's commitment to (a) without a single experimental demonstration that (b) has been excluded. This sub-paradigm tension is documented retrospectively by the review's own coverage gap: across 427 references, no EPR / CV characterization of Ni(I) or Ni(III) under catalytic conditions is cited.

**Field-invariant blind spot persisting across both paradigms.** Neither paradigm provides quantitative mass-balance accounting of cross-coupling vs. homo-coupling. Kumada 1972 (Paradigm A) reports no R–R; Pengfei 2024 (Paradigm B) reports 17% + 13% homocoupling without reconciliation against the proposed selectivity model; Cherney 2015 (review of Paradigm B) treats stereoconvergent yields as the primary metric without discussing homocoupling byproducts. The mass-balance gap is paradigm-invariant.

**Cherney 2015 as the documentation paper.** The review serves as the explicit cartographic moment at which the field's mechanistic commitments become legible as a coherent paradigm: Ni¹/Ni³ manifold + precoordination enantiocontrol + DKR/KR/DYKAT regime framework + radical-clock evidence pattern. Cherney 2015 organizes ~200 reactions under this framework (sections 2.2.1–2.2.3, 3.1.2, 4.1.1) without citing the experimental validation that would distinguish the paradigm from competing sub-paradigms — by aggregating 427 references under one mechanistic umbrella, the review crystallizes the paradigm even as its evidentiary basis remains open.

---

**Divergences**

**DV-1: Source of selectivity — geometric (1972) vs. kinetic-rate (2014) vs. concentration-electrochemical (2024) vs. catalyst-architectural (2015 review).**
Kumada 1972 attributes selectivity to ligand-enforced cis-geometry of the diorganonickel intermediate (structural argument). Breitenfeld 2014 attributes selectivity to bimetallic transmetalation kinetics (rate argument). Pengfei 2024 attributes selectivity to concentration differential and electrochemical characteristics of the two halides (thermodynamic/kinetic argument). Cherney 2015 inherits selectivity arguments from primary papers and organizes them under a precoordination + Ni¹/Ni³ framework (cartographic argument). These represent fundamentally different selectivity ontologies.

evidence_chain: [Kumada_1972 : B-3 → [REDACTED: substantial verbatim quotation; see Tier 9] | Breitenfeld_2014 : B-2 → "second order in both catalyst and Grignard reagent" | Cherney_2015 : U-2 → [REDACTED: substantial verbatim quotation; see Tier 9] | Pengfei_2024 : U-1 → [REDACTED: substantial verbatim quotation; see Tier 9]]

**DV-2: Role of DFT — absent (1972) vs. central + acknowledged-imprecise (2014) vs. cartographic-organizing (2015) vs. central + undisclosed (2024).**
Kumada 1972 has no computational component. Breitenfeld 2014 uses DFT as the sole pathway discriminant and explicitly acknowledges its limitations ("best accomplished through molecular dynamics simulations"). Cherney 2015 invokes DFT-derived mechanisms (Lin et al. Ni¹/Ni³, DET for Cu/L32, Sawamura γ-arylation) as the organizing framework across multiple sections without experimental validation. Pengfei 2024 deploys DFT as central evidence (2.8 kcal mol⁻¹ Ni(III)-vs-Ni(II) preference, redox potentials) without disclosing the functional, basis set, solvation, or spin-state assignments. The reliance on DFT inversely correlates with the disclosure of its protocol and the engagement with its uncertainty.

evidence_chain: [Kumada_1972 : none (pre-DFT) | Breitenfeld_2014 : U-3, B-5, A-3 → MD acknowledged as required but not performed | Cherney_2015 : CLA-1, SRG-8 → DFT mechanisms across three reaction types presented as established | Pengfei_2024 : U-6, SRG-1 → functional / basis set / solvation / spin states all undisclosed in main text]

**DV-3: Format-driven mechanism deferral — communication (1972) vs. full paper (2014) vs. review (2015) vs. full paper (2024).**
Kumada 1972 explicitly defers mechanism via "working hypothesis" + "Further studies are required" formula, era-canonical for JACS Communications. Breitenfeld 2014 uses an Organometallics full-paper format that compresses algebraic rate-law derivation, spin-correction reporting, and uncertainty analysis into Supporting Information without explicit deferral language. Cherney 2015 inherits mechanistic claims from primary papers and treats their DFT proposals as established without modal qualification, creating a new class of gap: review endorsement crystallizes claims that the primary papers presented as proposals. Pengfei 2024 displaces DFT methodology, mass-balance, and selectivity mechanism to Supplementary material and a "Supplementary Discussion on the Selectivity," using Nature Catalysis's compression format.

evidence_chain: [Kumada_1972 : A-1, A-2 → "working hypothesis" + "Further studies are required" | Breitenfeld_2014 : B-3, U-3, U-5 → derivation, ⟨S²⟩, benchmarking compressed | Cherney_2015 : B-1 (DYKAT without rate constants), B-6 (irreversibility stated without experiment), CLA-1 → review endorses primary-paper proposals as established | Pengfei_2024 : B-3 (caption footnote), B-7 (Supplementary Fig. 12), U-6 (Supplementary Figs. 15, 16) → main-text mechanistic claims rest on supplementary materials]

**DV-4: Review-specific gaps not present in primary papers (Cherney 2015 only).**
The review introduces gap classes that have no counterpart in the primary papers: (i) cross-study aggregation without normalization (B-2: ligand survey "comparisons should be drawn with caution"); (ii) frontier prioritization without target inventory (CLA-2: A-1–A-5 deferred areas without inventory of inaccessible structures); (iii) mechanistic-framework crystallization across independent reaction types (CLA-1: Ni¹/Ni³ + DET + Sawamura γ-arylation as DFT-derived mechanisms unified under the review's organizing logic); (iv) categorical-distribution claims without data (U-9: 4 mechanistic categories of Figure 1 without per-category frequency or performance distribution). These gaps are review-format-specific.

evidence_chain: [Cherney_2015 : B-2, U-9, CLA-1, CLA-2 → [REDACTED: substantial verbatim quotation; see Tier 9]; review enforces a temporal restriction without comparison to pre-2008 baseline]

---

**U-item patterns**

recurring_U: Self-contradictory absence — proposed model generates testable predictions that the paper does not test, while the model is retained | papers: [Kumada_1972, Breitenfeld_2014, Cherney_2015, Pengfei_2024] | item_ids: [Kumada_1972: U-1, U-2 | Breitenfeld_2014: U-1, U-2, U-3, U-4 | Cherney_2015: U-1, U-2, U-3, U-5, U-6, U-7, U-8, U-10 | Pengfei_2024: U-1, U-2, U-3, U-4, U-5, U-6, U-7] | note: This is the most densely recurring pattern across all four papers — Cherney 2015 alone records 8 U items where the A/B/C framework cannot capture the absence-of-test-of-own-prediction structure. The classification framework (A: deferred, B: reporting omission, C: severed citation) is designed for gaps within a paper's stated claims; self-contradictory absence is a gap between the paper's model and the model's own implications. The pattern intensifies in the review (8 U items in Cherney) because the review aggregates the primary papers' implicit predictions as if established, multiplying the cases where model predictions go untested.

recurring_U: Prerequisite-absence — operational condition for the paper's quantitative argument is not established | papers: [Breitenfeld_2014, Cherney_2015, Pengfei_2024] | item_ids: [Breitenfeld_2014: U-3, U-5 | Cherney_2015: U-2, U-6, U-7, U-10 | Pengfei_2024: U-2, U-3, U-6] | note: Distinct from self-contradictory absence in that the paper's argument requires a methodological prerequisite (DFT benchmarking, reference electrode harmonization, anode characterization, spin-state assignment) whose establishment is independent of the paper's mechanistic predictions. The pattern is emergent (absent in Kumada 1972, where the central claim does not require methodological prerequisites of this kind) and becomes more prominent in the post-DFT papers.

recurring_U: Single-data-point overinterpretation as conclusive evidence (incomplete-negative-evidence subtype) | papers: [Breitenfeld_2014, Cherney_2015, Pengfei_2024] | item_ids: [Breitenfeld_2014: B-2 (radical-clock), Cherney_2015: U-4 + U-7 (radical-clock for substrate 49), Pengfei_2024: U-7 (cyclopropylmethyl ring-opening)] | note: The radical-clock methodology is invoked across all three post-DFT papers as positive mechanistic evidence without TEMPO mass-balance, without the radical cyclization rate constant required to compute lifetime, and without cage-vs-free discrimination. The pattern is field-level — it is the same experimental design template applied with the same omissions across three independent groups, three substrate classes, and a 10-year span.

---

**Self-contradictory absence patterns**

self_contradictory: [Kumada_1972] : catalytic cycle eq 3 → R–R predicted as stoichiometric byproduct of intermediate 1 → 2 step → R–R unreported | item_id: U-1
self_contradictory: [Kumada_1972] : homogeneous Ni(II) cycle → "black mixture" observed → heterogeneous Ni⁰ possibility unanalyzed | item_id: U-2
self_contradictory: [Breitenfeld_2014] : "complete catalytic cycle" Figure 8 → intermediates 10–16 predicted → none directly characterized | item_id: U-1
self_contradictory: [Breitenfeld_2014] : eq 3 redistributive transmetalation → specific rate law predicted → algebraic derivation absent | item_id: U-4
self_contradictory: [Breitenfeld_2014] : bimetallic OA vs escape-rebound → DFT discriminates with author-acknowledged imprecision → imprecision not propagated to conclusion | item_id: U-1, U-3
self_contradictory: [Breitenfeld_2014] : Figure 8 cycle predicts comproportionation closure → catalyst decomposition observed → comproportionation kinetic competence not tested | item_id: U-2
self_contradictory: [Cherney_2015] : Ni¹/Ni³ mechanism → EPR-active Ni(I) / Ni(III) intermediates predicted → no EPR cited in 427 references | item_id: U-1
self_contradictory: [Cherney_2015] : DKR regime framework → k_rac ≫ k_coup predicted for both enantiomers → rate constants never measured for any Grignard | item_id: U-3
self_contradictory: [Cherney_2015] : DET mechanism for Cu/L32 → equal product ee and rate from (R)-313 vs (S)-313 → enantiopure-substrate experiment never run | item_id: U-8
self_contradictory: [Cherney_2015] : SET cycle for Ni/Ir → Ir(II) and Ni(III) predicted → never spectroscopically observed | item_id: U-1 / B-7
self_contradictory: [Cherney_2015] : Frontier prioritization → biological need for quaternary centers asserted → no inventory of inaccessible targets | item_id: U-5 / CLA-2
self_contradictory: [Pengfei_2024] : selectivity model (concentration + electrochemical asymmetry) → secondary homo suppressed under 3:1 secondary excess; primary homo negligible under 1° deficiency → 17% + 13% homo observed without reconciliation | item_id: U-1
self_contradictory: [Pengfei_2024] : DFT initiation barrier ≈ 20 kcal mol⁻¹ (highest in profile) → SET initiation rate-determining → kinetic data interpreted as radical-addition selectivity | item_id: U-5
self_contradictory: [Pengfei_2024] : DFT-calculated Ni(I)/Ni(0) potential −2.38 V → SWV-measured −2.74 V → 360 mV discrepancy undiscussed | item_id: U-2
self_contradictory: [Pengfei_2024] : Ni(I/II/III) cycle as central mechanism → 2.8 kcal mol⁻¹ Ni(III) RE preference is sole pathway discriminator → DFT protocol/uncertainty undisclosed | item_id: U-6

**Recurring pattern assessment.** Self-contradictory absence appears in all four papers across all paradigms (2-electron, radical, electrochemical) and all formats (communication, full paper, review, full paper). In the review (Cherney 2015) it intensifies dramatically (8 distinct instances) because the review aggregates primary-paper proposals as if established, creating new self-contradictory absences at the review level (e.g., the field-wide absence of EPR for Ni(I)/Ni(III) becomes visible only when the review treats the manifold as established across 200+ reactions).

This pattern reflects a **genre convention combined with a genuine analytical gap**. The genre convention: mechanism sections in cross-coupling papers serve a narrative function (contextualizing the scope or selectivity data within a plausible cycle) rather than a hypothesis-testing function (generating and testing falsifiable predictions). The convention is reinforced by review aggregation: when reviews accept primary-paper proposals as the field's mechanistic framework, the unrealized predictions of those proposals become field-level rather than paper-level absences. The genuine analytical gap: each individual prediction is testable with the originating paper's infrastructure, and several are testable with the review's own retrospective reach (Cherney 2015 could have flagged the field-wide EPR absence as a research priority but did not).

---

**Sub-group-specific findings not subsumed by field-wide patterns**

This is a single-group output (G2 alone), so no sub-group integration is performed here. However, two G2-specific observations warrant preservation because they identify chemically concrete gaps that would be lost if absorbed into broader RP categories during a later integration mode:

- **Boundary-traversal-specific gap (G2-only):** the Csp²/Csp³ boundary is the organizing structural feature of G2. The 1972 Kumada paper treats the boundary as a positive feature without negative-result data (B-4); the 2014 / 2024 papers cross the boundary into Csp³ but the mechanistic justification for why Csp³ now works rests on radical activation pathways whose elementary steps are themselves not validated under turnover (RP-1). The succession relationship — Paradigm B's founding problem is Paradigm A's blind spot — is specific to this group and would not appear in a "founder-only" or "extension-only" group.
- **Review-as-paradigm-crystallization (Cherney 2015 specific):** Cherney 2015 functions as the documentation moment at which the Ni¹/Ni³ + precoordination + DKR/KR framework becomes legible as a coherent paradigm. This role is unique to the review-genre paper in G2 and would be invisible in groups composed entirely of primary papers.

---

**Group-level unasked question**

[REDACTED: substantial verbatim quotation; see Tier 9]

evidence_chain: [Kumada_1972 : B-2 (no intermediates observed), B-12/U-2 (black mixture uncharacterized), B-1/U-1 (no cross:homo data) | Breitenfeld_2014 : U-1 (DFT precision insufficient), U-2 (comproportionation untested), U-4 (rate law not derived), B-7 (no GC mass balance) | Cherney_2015 : U-1 (Ni¹/Ni³ EPR absence across 427 refs), U-2 (precoordination kinetics absent), U-3 (DKR/KR rate constants never measured), CLA-1 (DFT-without-experiment systemic) | Pengfei_2024 : U-6 (DFT protocol undisclosed), U-3 (anode role absent), U-1 (selectivity model not reconciled with byproducts)]

TEMPERATURE_SUMMARY correspondence: In Pengfei 2024, U-6 (DFT methodology + 2.8 kcal mol⁻¹ reliability) is the only 3/3 high-convergence cluster in the entire TEMPERATURE_SUMMARY. In Cherney 2015, U-1 (Ni¹/Ni³ EPR/CV absence) is similarly 3/3 high. In Kumada 1972, B-1 (selectivity claim without byproduct data) is the strongest convergence item (3/3 all high). In Breitenfeld 2014, U-1 reaches critical at the Turn 4 synthesis level via compound V1+V3. The 52-year persistence of mechanism-validation + selectivity-quantification as the most convergent gap items — across paradigms (2-electron, radical, electrochemical), substrates (Csp², Csp³), formats (communication, full paper, review), and journals (JACS, Organometallics, Chem. Rev., Nat. Catal.) — indicates a field-wide structural convention that each paper inherits rather than chooses.

recurring_root correspondence: The group-level unasked question subsumes recurring_root 1 (catalytic cycle validation) and recurring_root 3 (selectivity without mass balance) as two facets of a single field-wide deficit: across 52 years and four paradigms, the field has produced no quantitative selectivity model validated by complete mass balance for any Ni-catalyzed cross-coupling, and has provided no direct experimental observation of the elementary steps of any proposed catalytic cycle under operating turnover conditions. The 1972 paper lacks Csp³ substrates to make the Csp²/Csp³ boundary visible; the 2014 paper has Csp³ substrates but treats the boundary by radical-clock + DFT without elementary-step observation; the 2015 review formalizes the radical paradigm without flagging the field-wide EPR absence as a priority; the 2024 paper extends to Csp³–Csp³ electrochemistry but reproduces the same mechanism-validation and mass-balance gaps under a new activation mode.

Cherney 2015 is the paper at which the group-level unasked question becomes most fully visible because the review's aggregation of 427 references documents the field-wide absence as a coherent pattern rather than as a paper-level omission. Without the review, the gap could be read as a series of individual choices; with the review, it is legible as a paradigm-level convention.

---

*End of G2 output.*

---

> **Tier 8 redaction notice**: This file is a redacted copy of the corresponding Tier 3 / Tier 9 output. Verbatim source-paper quotations have been replaced by `[REDACTED: see source paper §<loc>; full text retained in Tier 9 reviewer-only deposit]` markers, preserving location references and our own analytical content. Bibliographic fields (title, authors, journal, year, DOI), analytical labels (`evidence_chain:` with B-/U-/A-/C- internal IDs), short technical terms, and our own analytical text are not redacted. The redaction was applied by `scripts/redact_for_tier8.py` and, for this version, by `scripts/build_paperA_R1_public.py` with `scripts/redact_source_ngram_runs.py` (scripts of the project repository; they are not deposited).
