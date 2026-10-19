```
prompt_version: stage1-v17-20260415
model_info: claude-sonnet-4-6

target_title:   New Mechanistic Insights into the Copper-Free Heck−Cassar−Sonogashira Cross-Coupling Reaction
target_authors: Chiara Palladino, Tommaso Fantoni, Lucia Ferrazzano, Beatrice Muzzi, Antonio Ricci, Alessandra Tolomelli, Walter Cabri
target_start:   page 1: [REDACTED: paper boundary quote; see Tier 9]
target_end:     end of document

[Agent fields]
V1: Mechanistic palladium catalysis / organometallic chemistry — primary field of the paper (ACS Catalysis, Pd cross-coupling mechanism via stoichiometric NMR/HPLC and DFT).
V2: Computational chemistry / quantum chemical reaction modeling — the paper's mechanistic conclusions rest substantially on DFT energy profiles; V2 applied the DFT reporting checklist and assessed catalytic-cycle experimental corroboration.
V3: Quantitative NMR spectroscopy / chemical kinetics — V2 pre-empted computational; V3 addressed whether the ³¹P NMR quantification protocol (T₁, relaxation delay, reference standards) and kinetic data quality (model, error, equilibrium verification) are adequate.

---

[A] A-1 | loc: P5:Rcol:* (Table 4, entry 11, footnote c) | quote: [REDACTED: substantial verbatim quotation; see Tier 9] | deferral_type: suppressed | mixed_detail: n/a | reason_inferred: T1 | linked_to: B-18 | cross_field_temperature: V1=medium; convergence=1/3; temperature_gap: n/a
note: Suppressed classification checklist satisfied: (1) authors explicitly acknowledge that k cannot be calculated; (2) the acknowledgment is relegated to a footnote with no further discussion; (3) the paper does not return to discuss the mechanistic implications (does the unmeasurably large k for triflate imply a barrierless PPh₃ → TMG exchange, and how does this affect the cationic energy profile?). The Rd → Rg conversion barrier and its relationship to TS0^OTf are left unaddressed.

[A] A-2 | loc: P10:Lcol:* (Conclusions, final paragraph) | quote: [REDACTED: substantial verbatim quotation; see Tier 9] | deferral_type: deferred | mixed_detail: n/a | reason_inferred: T1 | linked_to: U-1, B-18 | cross_field_temperature: V1=medium; convergence=1/3; temperature_gap: n/a
note: The paper explicitly defers the question of how the base's role (coordination vs. external deprotonation) is divided between the anionic, cationic, and ionic sub-pathways. V1-Q13 identified the absence of experimental evidence (isotope labeling, NOE, crossover) for amine coordination during carbopalladation; this is the experimental analogue of the deferred mechanistic question.

---

[B] B-1 | loc: P9:Lcol:* (DFT Calculations section) | quote: [REDACTED: substantial verbatim quotation; see Tier 9] | classification: reporting_omission | rhetorical_function: States the computational level of theory used for reaction-coordinate calculations. | note: Consolidates V1-Q8, V2-Q1, V2-Q2, V2-Q3, V2-Q4, V2-Q7, V2-Q12. Six standard DFT methodology reporting elements are entirely absent: (1) dispersion correction — no D3BJ or equivalent stated, despite PPh₃/π-alkyne/Pd-π interactions dominated by London dispersion; (2) solvation model — named model (PCM, SMD, COSMO-RS) absent despite ionic intermediates (Rd, Rg, S, T, N) in DMF; (3) thermochemical correction protocol — RRHO vs quasi-RRHO not specified, critical for low-frequency PPh₃ torsional modes; (4) conformational sampling — method for identifying lowest-energy TS conformers not described; (5) ECP/relativistic treatment — not specified for Pd (4d metal) or I; (6) basis set completeness — not tested for anionic intermediates. No benchmark against experimental activation parameters is reported. | cross_field_temperature: V1=high, V2=high, V3=medium(V3-OV4); convergence=3/3; temperature_gap=low

[B] B-2 | loc: P8:Lcol:* (DFT Calculations, productive pathway text) | quote: [REDACTED: substantial verbatim quotation; see Tier 9] | classification: mixed (intentional_narrowing + methodological_limitation) | rhetorical_function: Asserts that the cis/trans isomerization of intermediate C is irrelevant and therefore excluded from analysis. | note: V1-Q7, V2-OV3. The paper makes a kinetic claim (isomerization is irrelevant) without providing a calculated isomerization barrier or a measured cis/trans ratio under catalytic conditions. No DFT value is given for the cis→trans barrier or for the trans-C → RE barrier vs. the cis-C → RE barrier (TS4 = 10.8 kcal/mol). The paper's own DFT framework provides the natural tool to test this assertion. | cross_field_temperature: V1=medium, V2=medium; convergence=2/3; temperature_gap=none

[B] B-3 | loc: P5:Lcol:* (Table 4, footnote b) and P3:Lcol:* (Table 1, footnote) | quote: [REDACTED: substantial verbatim quotation; see Tier 9] | classification: reporting_omission | rhetorical_function: Directs the reader to SI for the quantitative NMR method used to derive equilibrium constants. | note: Consolidates V3-Q1, V3-Q9. No ³¹P T₁ values or relaxation delay parameters are reported. OPPh₃ T₁ can be 10–30 s in CDCl₃, substantially longer than Pd-coordinated phosphines; if the recycle delay was calibrated for Pd-bound species, OPPh₃ (Table 1, footnote b: "two equivalents of OPPh₃ observed") would be systematically underestimated. The OPPh₃ stoichiometry check for Pd(II) reduction hinges on this integration accuracy. | cross_field_temperature: V3=high; convergence=1/3; temperature_gap: n/a

[B] B-4 | loc: P6:Lcol:* (Figure 5) | quote: [REDACTED: substantial verbatim quotation; see Tier 9] | classification: reporting_omission | rhetorical_function: Reports V_max values for stoichiometric kinetic traces as evidence that direct coordination from B is faster than via M. | note: Consolidates V1-Q4, V3-Q3, V3-Q4. The kinetic model underlying V_max (initial tangent, Michaelis–Menten fit, first-order rate law, or other) is not stated. Sampling interval for NMR acquisitions is not reported. No error bars, standard deviations, or replication count are given for V_max or k. Without these, it is impossible to assess whether the ≈1.7-fold difference between B and M V_max values, or the ≈5-fold k differences in Table 4, are statistically meaningful. | cross_field_temperature: V1=medium, V3=high (V3-OV1); convergence=2/3; temperature_gap=low

[B] B-5 | loc: P5:Rcol:* (Table 4, base/B°₂ ratio columns) | quote: [REDACTED: substantial verbatim quotation; see Tier 9] | classification: reporting_omission | rhetorical_function: Presents equilibrium ratios at three base loadings as the basis for calculating equilibrium constant k. | note: V3-Q5, V3-Q10. Neither time-invariance of the ratios (confirming true equilibrium vs. kinetic trapping) nor replicate measurements are reported. At 10 equiv base, where the ratio is 68/32, ³¹P NMR integration is sensitive to phasing and baseline correction; the uncertainty in k at this loading cannot be assessed without stated precision data. The statistical significance of differences among entries 1–9 in Table 4 cannot be evaluated.

[B] B-6 | loc: P6:Rcol:* (Table 3 context) | quote: [REDACTED: substantial verbatim quotation; see Tier 9] | classification: reporting_omission | rhetorical_function: Claims solvent-independent selectivity for cross-coupling product based on HPLC quantification. | note: V3-Q8. Mass balance is not reported for stoichiometric competition reactions. Without mass balance, unquantified side products, oligomers, or precipitated Pd black cannot be excluded. The claim of selectivity is meaningful only if total carbon recovery is known. Flag: metric incompleteness.

[B] B-7 | loc: P4:Rcol:* (Table 2, footnote d) | quote: [REDACTED: verbatim source quotation; see `loc:`] | classification: reporting_omission | rhetorical_function: States the analytical method for the diagnostic 3a/4a ratio used to infer the presence or absence of complex M. | note: V3-Q7. Relative UV response factors (molar absorptivities) for 3a (aryl alkyne) and 4a (1,3-enyne homodimer) are not reported. These structurally distinct chromophores may differ substantially at the detection wavelength, making the raw HPLC ratio unreliable without calibration. The 3a/4a ratio is the paper's primary diagnostic for M formation/absence.

[B] B-8 | loc: P3:Lcol:* (Table 1, footnote a) and P4:Lcol:* (Table 2, footnote a) | quote: [REDACTED: substantial verbatim quotation; see Tier 9] / [REDACTED: substantial verbatim quotation; see Tier 9] | classification: methodological_limitation | rhetorical_function: Specifies the fixed observation timepoints for the precatalyst reduction (Table 1) and Pd(II) complex stability (Table 2) experiments. | note: V1-Q11, V3-Q6. Both Table 1 (10 min) and Table 2 (30–60 min) use single observation timepoints with no time-course data. Without kinetic traces, it is impossible to determine whether the reported conversions represent true equilibria, kinetically trapped states, or still-evolving systems. In particular, the conclusion that TEA cannot reduce the precatalyst may reflect only that TEA is slow, not that it is mechanistically incapable. | cross_field_temperature: V1=medium, V3=medium (V3-OV2); convergence=2/3; temperature_gap=none

[B] B-9 | loc: P3:Lcol:* (Catalytic Cross-Coupling Reactions section, Scheme 2) | quote: [REDACTED: substantial verbatim quotation; see Tier 9] | classification: reporting_omission | rhetorical_function: States the stoichiometric requirement of the Pd(II) precatalyst reduction step. | note: V1-Q12. The precatalyst reduction requires one equivalent of water, but experiments are conducted in nominally anhydrous deuterated solvents (CDCl₃, DMF-d₇). The source of water is not stated. No experiment tests whether rigorously dried solvents inhibit reduction. Not stated in paper.

[B] B-10 | loc: P3:Lcol:* (Table 1) | quote: [REDACTED: substantial verbatim quotation; see Tier 9] | classification: reporting_omission | rhetorical_function: States that ³¹P NMR was used to calculate Pd(II) → Pd(0) conversion. | note: V3-Q2. Pd(0) is ³¹P NMR-silent (no phosphorus signal). Conversion to Pd(0) must be inferred from disappearance of precatalyst signals plus appearance of OPPh₃. The reference species, calibration standard, and arithmetic procedure for calculating Pd(0) fraction are not described in the main text. The method is delegated to SI without summary.

[B] B-11 | loc: P9:Rcol:* (Figure 10 caption) | quote: [REDACTED: substantial verbatim quotation; see Tier 9] | classification: reporting_omission | rhetorical_function: Specifies the thermodynamic state function and temperature used for the DFT free-energy profiles. | note: V2-Q6. Catalytic experiments are conducted at both 25 °C (298 K) and 60 °C (333 K). For steps with large ΔS (PPh₃ dissociation, bimolecular amine coordination), ΔG at 333 K can differ by several kcal/mol from ΔG at 298 K. No recalculation at 333 K is reported.

[B] B-12 | loc: P9:Rcol:* (Figure 10a energy profile) | quote: [REDACTED: verbatim source quotation; see `loc:`] (zero-energy reference) | classification: reporting_omission | rhetorical_function: Sets the energy reference for the iodide-pathway DFT profile. | note: V2-Q5. The zero-energy reference is the isolated oxidative addition complex B_NO₂ rather than the catalytic resting state. Under catalytic conditions (excess base present), Ra or Rb may be the actual resting state; the effective barrier from the resting state to TS0 would differ from the reported value. The choice of reference is not justified.

[B] B-13 | loc: P8:Rcol:* (DFT cationic pathway discussion) | quote: [REDACTED: substantial verbatim quotation; see Tier 9] | classification: reporting_omission | rhetorical_function: Reports the rate-determining transition state barrier for the triflate (cationic) pathway. | note: V2-Q9. TS0^OTf is a bimolecular step (Rg + alkyne 2a → TS0^OTf). The standard bimolecular entropic penalty (~5–10 kcal/mol at 1 M standard state) should be added to the effective barrier when comparing with unimolecular steps. No bimolecular concentration correction is reported. The stated 24.0 kcal/mol may underestimate the effective catalytic barrier.

[B] B-14 | loc: P10:Lcol:* (Conclusions, paragraph 2) | quote: [REDACTED: substantial verbatim quotation; see Tier 9] | classification: mixed (methodological_limitation + reporting_omission) | rhetorical_function: States the central two-pathway conclusion derived from combined experimental and DFT evidence. | note: V2-Q8. DFT calculations were performed only for the iodide and triflate counterion pathways. Bromide and chloride, both studied experimentally in Table 4 (entries 2–3), are assigned to the neutral pathway by inference only. Whether bromide's different OA kinetics shift the barrier ordering is neither calculated nor discussed.

[B] B-15 | loc: P4:Lcol:* (Catalytic Cross-Coupling Reactions section) | quote: [REDACTED: substantial verbatim quotation; see Tier 9] | classification: methodological_limitation | rhetorical_function: Specifies the model substrate used for the catalytic mechanistic study. | note: V1-Q3. The 4-nitrophenyl iodide model is electronically extreme — the nitro group slows the RE step (enabling intermediate trapping) and strongly activates the aryl iodide toward OA. No discussion is offered of whether the mechanism, intermediate distributions, or pathway selectivity would differ for electronically neutral or electron-rich aryl halides. Substrate representativeness is not acknowledged as a limitation.

[B] B-16 | loc: P6:Rcol:* (Table 3 context, SI delegation) | quote: [REDACTED: substantial verbatim quotation; see Tier 9] | classification: reporting_omission | rhetorical_function: Claims solvent independence of cross-coupling selectivity while delegating the supporting data entirely to SI. | note: V1-Q5, V3-OV3. Eight solvent experiments (entries 8–15) are entirely in SI without any quantitative summary (yields, selectivities, conversions) in the main text. Flag: metric incompleteness. | cross_field_temperature: V1=medium, V3=medium (V3-OV3); convergence=2/3; temperature_gap=none

[B] B-17 | loc: P9:Rcol:* (DFT Calculations, Figure 10a) | quote: [REDACTED: verbatim source quotation; see `loc:`] | classification: mixed (reporting_omission + methodological_limitation) | rhetorical_function: Reports the DFT-calculated barriers for the TMG-assisted (TS0) and unassisted (TS1^PPh3) carbopalladation pathways in the iodide mechanism. | note: V1-Q9, V2-OV2. No Eyring analysis, measured kobs, or estimated ΔG‡ from kinetic data is reported to validate the TS0 = 20.2 kcal/mol barrier experimentally. The reconciliation between computed and observed kinetics is entirely absent. | cross_field_temperature: V1=high, V2=high (V2-OV2); convergence=2/3; temperature_gap=none

[B] B-18 | loc: P3:Lcol:* (Table 1, entries 5–6) | quote: [REDACTED: substantial verbatim quotation; see Tier 9] | classification: reporting_omission | rhetorical_function: Documents total failure of TEA to reduce the precatalyst and quantitative formation of bis-alkyne complex M. | note: V1-Q1. The paper provides no physical-organic explanation for TEA's failure — no pKₐ comparison, no redox potential argument, no DFT barrier for TEA-mediated phosphine oxidation vs. TMG/PYR. TEA is widely used as base in Sonogashira protocols; the finding that it promotes M formation rather than precatalyst reduction is mechanistically significant but unexplained. Not stated in paper.

[B] B-19 | loc: P3:Rcol:* (Catalytic Cross-Coupling Reactions) | quote: [REDACTED: substantial verbatim quotation; see Tier 9] | classification: reporting_omission | rhetorical_function: Reports that added PPh₃ suppresses detectable M formation under stoichiometric NMR conditions. | note: V1-Q2. The ³¹P NMR detection threshold for complex M is not stated. Sub-stoichiometric M formation below detection limit under catalytic conditions with added PPh₃ cannot be excluded.

[B] B-20 | loc: P4:Rcol:* (Figure 4b context) | quote: [REDACTED: substantial verbatim quotation; see Tier 9] | classification: methodological_limitation | rhetorical_function: Describes the stoichiometric NMR experiment demonstrating the effect of added PPh₃ on detected Pd intermediates. | note: V1-Q10. The effect of added PPh₃ on catalytic yield and 3a/4a ratio in a full turnover catalytic run is not reported. The NMR experiment is stoichiometric; whether the intermediate-distribution change translates to measurable differences in catalytic performance is left untested.

---

[C] C-1 | loc: P2:Lcol:* (Introduction) | citation: [REDACTED: substantial verbatim quotation; see Tier 9] | textual_function: Cited to establish the prior mechanistic consensus (deprotonation mechanism) that the present paper's results are designed to supersede. | reason_severed: Dropped Quantitative Benchmark — Mårtensson's DFT study reports calculated barriers for the deprotonation pathway; the paper's own TS0 = 20.2 kcal/mol for carbopalladation is never numerically compared against Mårtensson's barriers on the same energy coordinate, despite this being the central mechanistic claim. | affects_claims: yes — the paper claims to supersede Mårtensson's mechanistic conclusion but without direct numerical comparison, the reader cannot assess whether the two computations are quantitatively inconsistent or differ only in interpretation. | symmetric_pattern: no

[C] C-2 | loc: P1:Lcol:* (Introduction, ref 5) | citation: [REDACTED: substantial verbatim quotation; see Tier 9] | textual_function: Cited as a recent comprehensive Sonogashira review in the introductory background paragraph. | reason_severed: Cited as background context; no specific finding, rate constant, or selectivity value from the review is discussed or compared. | affects_claims: no — background citation that does not affect primary mechanistic claims. | symmetric_pattern: partial — grouped with refs 1–3 as introductory background citations.

[C] C-3 | loc: P2:Lcol:* (Introduction, ref 11) | citation: [REDACTED: substantial verbatim quotation; see Tier 9] | textual_function: Cited for background on guanidines (including TMG) as nucleophilic base catalysts. | reason_severed: TMG is the paper's primary base throughout; Taylor's quantification of TMG's nucleophilicity vs. basicity is directly relevant to the claim that TMG coordinates to Pd rather than acting only as an external base, but Taylor's data are never invoked or compared. | affects_claims: medium — Taylor's nucleophilicity data for guanidines would strengthen or weaken the claim that secondary-amine character of TMG drives coordination; the severed engagement leaves this mechanistic premise unsupported by literature citation. | symmetric_pattern: no

---

[U] U-1 | loc: P8:Lcol:* (Figure 10a, proposed catalytic cycle) | quote: [REDACTED: substantial verbatim quotation; see Tier 9] | question: The proposed neutral-pathway catalytic cycle includes a base-mediated deprotonation of the coordinated alkyne C–H bond (intermediate N → cis-C, via TS3). This step is supported only by DFT (ΔG_TS3 = 12.6 kcal/mol); no experimental probe (kH/kD primary kinetic isotope effect with deuterated alkyne, ¹H/²H incorporation, or intermediate trapping) is reported anywhere in the paper. | originating_agent: V2-Q10, V1-Q13 | severity: high | note: Self-contradictory absence — the paper's proposed catalytic cycle predicts that deprotonation of the alkyne C–H bond occurs at a specific stage (N → cis-C) with a calculated barrier, but no experimental test of this elementary step is reported or acknowledged as untested. An isotope experiment (PhC≡CD instead of PhC≡CH) is a standard test; its absence is not noted as a limitation. Also carries B component (reporting_omission for not reporting kH/kD); U classification added because the paper's own mechanism predicts an experimentally accessible isotope effect.

[U] U-2 | loc: P10:Lcol:* (Conclusions) and P4:Lcol:* (Table 2 context) | quote: [REDACTED: substantial verbatim quotation; see Tier 9] | question: The paper concludes that M is kinetically unable to compete with direct coordination. M is independently synthesized and shown to be stable for ≥30 min at 25 °C in CDCl₃ (Table 2). No rate constant for M + alkyne (direct coordination) vs. M undergoing RE to give 4a is reported or calculated. The paper explicitly states [REDACTED: substantial verbatim quotation; see Tier 9] yet RE from M is the mechanism producing the diagnostic homocoupling product 4a. | originating_agent: V1-Q14 | severity: high | note: Self-contradictory absence — the paper uses 3a/4a ratio as a diagnostic for M formation and invokes M's kinetic fate as central to the mechanistic argument, yet neither the RE rate from M nor the rate of M + alkyne are characterized experimentally or computationally. The paper's proposed mechanism predicts these rates should be measurable via the same stoichiometric NMR platform used for B_NO₂ kinetics (Figure 5).

---

[META]
  linked_items:
    A-1 ↔ B-13 (triflate k unmeasurable and bimolecular entropy correction both concern cationic pathway energy profile)
    A-2 ↔ U-1 (deferred amine role and experimentally untested deprotonation step are facets of the same gap)
    B-1 ↔ B-11, B-12, B-13, B-17 (DFT methodology deficiencies and barrier interpretation issues share computational root)
    B-3 ↔ B-4, B-5, B-10 (all concern adequacy of quantitative NMR measurements underlying equilibrium and kinetic data)
    U-1 ↔ U-2 (both are elementary steps in proposed catalytic cycle characterized computationally but not experimentally)
    C-1 ↔ B-1, B-17 (Dropped Quantitative Benchmark gap and DFT methodology gap both prevent comparison of barriers against Mårtensson's prior values)

  same_root_groups:
    SRG-1 [DFT methodology reporting completeness]: B-1, B-11, B-12, B-13, B-17 — derive from the same absent set: DFT methodology details needed to assess barrier reliability and compare with prior work.
    SRG-2 [Quantitative NMR measurement protocol]: B-3, B-4, B-5, B-10 — derive from the same absent data: NMR acquisition parameters (T₁, relaxation delay, reference standard) needed to evaluate quantitative ³¹P NMR integrations.
    SRG-3 [Single-timepoint experimental design]: B-8, B-5 — derive from same absent data: time-course profiles for Tables 1 and 2.
    SRG-4 [Experimental verification of elementary steps]: A-2, U-1, U-2 — derive from same absent experiment: direct experimental evidence for elementary steps proposed in catalytic cycle.
    SRG-5 [Product quantification methodology]: B-6, B-7, B-16 — derive from same absent data: HPLC calibration and mass balance reporting for selectivity claims.

  symmetric_citations: C-2 symmetric with introductory background refs 1–3 (all cited without substantive numerical engagement).

  unreported_data:
    - Solvent-screen entries 8–15 (Table 3): data exist in SI (S93–S103) but not summarized numerically in main text.
    - Equilibrium constant k derivation for all Table 4 entries: SI Paragraph 9.
    - Pd(0) conversion calculation method: SI (section unspecified).
    - Mårtensson (ref 12b) calculated DFT barriers: in cited paper, not retrieved or reproduced.

  series_signal: no

[TEMPERATURE_SUMMARY]
  high_convergence_high_gap: none
  high_convergence_low_gap:
    B-1 (V1=high, V2=high, V3=medium; convergence=3/3; temperature_gap=low)
    B-17 (V1=high, V2=high; convergence=2/3; temperature_gap=none)
    B-2 (V1=medium, V2=medium; convergence=2/3; temperature_gap=none)
    B-4 (V1=medium, V3=high; convergence=2/3; temperature_gap=low)
    B-8 (V1=medium, V3=medium; convergence=2/3; temperature_gap=none)
    B-16 (V1=medium, V3=medium; convergence=2/3; temperature_gap=none)
    C-1 (V1=medium, V2=medium; convergence=2/3; temperature_gap=none)
  low_convergence_high_gap: none

[GAP]
  GAP-1 | type: 1 | priority: high | description: Retrieve Mårtensson's DFT-computed barriers for the Soheili deprotonation mechanism (ref 12b) to enable direct numerical comparison with this paper's TS0 = 20.2 kcal/mol for carbopalladation. | candidate_paper: Mårtensson (ref 12b; full citation not resolved from available text) | inference_label: T1 | status: pending
  GAP-2 | type: 3 | priority: high | description: Papers reporting kH/kD primary kinetic isotope effects for Pd-catalyzed alkyne activation or deprotonation would directly address U-1 (untested deprotonation step TS3). | candidate_paper: not specified | inference_label: T3 | status: pending
  GAP-3 | type: 3 | priority: medium | description: DFT benchmarking studies for Pd(II)/PPh₃ complexes comparing PBE vs. hybrid functionals with D3BJ would allow assessment of whether B-1 (dispersion omission) materially alters barrier ordering. | candidate_paper: not specified | inference_label: T3 | status: pending

inference_time_sec: not available — inject externally
```

---

> **Tier 8 redaction notice**: This file is a redacted copy of the corresponding Tier 3 / Tier 9 output. Verbatim source-paper quotations have been replaced by `[REDACTED: see source paper §<loc>; full text retained in Tier 9 reviewer-only deposit]` markers, preserving location references and our own analytical content. Bibliographic fields (title, authors, journal, year, DOI), analytical labels (`evidence_chain:` with B-/U-/A-/C- internal IDs), short technical terms, and our own analytical text are not redacted. The redaction was applied by `scripts/redact_for_tier8.py` and, for this version, by `scripts/build_paperA_R1_public.py` with `scripts/redact_source_ngram_runs.py` (scripts of the project repository; they are not deposited).
