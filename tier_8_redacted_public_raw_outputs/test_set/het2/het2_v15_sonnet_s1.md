```
prompt_version: stage1-v15-20260331
model_info: claude-sonnet-4-6

target_title:   Deconvoluting Substrates, Support, and Temperature Effects on Leaching and Deactivation of Pd Catalysts: An In Situ Study in Flow
target_authors: Oliver J. Newton, Matthew J. Takle, Jeffery Richardson, Klaus Hellgardt, and King Kuok Mimi Hii
target_start:   page 1: [REDACTED: paper boundary quote; see Tier 9]
target_end:     end of document

[Agent fields]
V1: Heterogeneous catalysis / continuous-flow Pd cross-coupling chemistry — primary platform of the paper (ACS Catalysis, tandem flow reactor, ICP-MS leaching quantification).
V2: Organometallic reaction mechanism / physical organic chemistry — V1 generated data-quality questions; mechanistic evidentiary basis for the paper's causal claims (α-hydride elimination, oxidative addition, cluster formation) was unaddressed.
V3: Analytical chemistry / measurement methodology (ICP-MS, HPLC, flow analytics) — V1 and V2 did not examine the metrological validity of the two primary measurement platforms (ICP-MS Pd quantification and HPLC conversion).

--- Step 0: Boundary recheck ---
All 33 quoted passages verified against target_start/target_end. All quotes are drawn from the target paper. No boundary violations detected.

--- Step 1: Cross-field temperature ---
See individual item entries and TEMPERATURE_SUMMARY below.

--- Step 2: Same-root groups (see META) ---

[A] A-1 | loc: P4:Rcol:30-40* (Results, Pd/Al2O3, iodobenzene) | quote: [REDACTED: substantial verbatim quotation; see Tier 9] | deferral_type: deferred | mixed_detail: n/a | reason_inferred: T1 ("we speculate" — explicit epistemic hedge) | linked_to: A-4, B-13, C-4 | cross_field_temperature: V2=high, V3=high (OV5); convergence: 2/3; temperature_gap: none

[A] A-2 | loc: P4:Lcol:15-30* (Results, PdEnCat, NEt3 section) | quote: [REDACTED: substantial verbatim quotation; see Tier 9] | deferral_type: suppressed | mixed_detail: n/a | reason_inferred: T1 (suppressed checklist: (1) "This was rather unexpected" — textual acknowledgment; (2) paper immediately invokes literature analogy from ref 53 without mechanistic evidence for 30 °C operation; (3) paper does not return to address the temperature discrepancy) | linked_to: A-3, B-13 | cross_field_temperature: V2-Q1=high; no additional overlap; convergence: 1/3

[A] A-3 | loc: P4:Lcol:30-45* (Results, FC-1001) | quote: [REDACTED: substantial verbatim quotation; see Tier 9] | deferral_type: deferred | mixed_detail: n/a | reason_inferred: T1 ("We believe" — epistemic hedge; no characterization of coordination provided) | linked_to: A-2, B-13 | cross_field_temperature: V2-Q2=high; convergence: 1/3

[A] A-4 | loc: P3:Lcol:40-50* (Results, PdEnCat, iodobenzene) | quote: [REDACTED: substantial verbatim quotation; see Tier 9] | deferral_type: deferred | mixed_detail: n/a | reason_inferred: T2 [paper-grounded inference] (described as supporting "the earlier hypothesis" — the paper endorses the hypothesis without providing new mechanistic evidence; speciation of leached Pd left unresolved) | linked_to: A-1, B-13 | cross_field_temperature: V2-Q4=high; convergence: 1/3

[A] A-5 | loc: P2:Rcol:5-15* (Results, "Solvent Effects", DMF) | quote: [REDACTED: substantial verbatim quotation; see Tier 9] | deferral_type: deferred | mixed_detail: n/a | reason_inferred: T1 ("consistent with" — mechanistic basis delegated to cited literature refs 45-48, not tested in paper) | linked_to: A-1, C-3, B-12 | cross_field_temperature: V1-Q6=medium, V2-OV1(V2)=high; convergence: 2/3; temperature_gap: low

[A] A-6 | loc: P2:Lcol:35-50* (Results, FC-1001 at 30 °C) | quote: [REDACTED: substantial verbatim quotation; see Tier 9] | deferral_type: deferred | mixed_detail: n/a | reason_inferred: T2 [paper-grounded inference] (difference in temperature response between FC-1001 and PdEnCat 30 stated as observation; structural explanation absent and not sent to future work explicitly, but no resolution attempted — forgotten) | linked_to: A-2, B-1 | cross_field_temperature: V2-Q8=medium; convergence: 1/3

[A] A-7 | loc: P4:Lcol:35-50* (Results, FC-1001 comparative) | quote: [REDACTED: substantial verbatim quotation; see Tier 9] | deferral_type: deferred | mixed_detail: n/a | reason_inferred: T2 [paper-grounded inference] (differential deactivation kinetics observed and attributed to different Pd species, but kinetic order and mechanism left unresolved) | linked_to: A-3 | cross_field_temperature: V2-Q11=medium; convergence: 1/3

[A] A-8 | loc: P5:Lcol:25-35* (Conclusions, final sentence) | quote: [REDACTED: substantial verbatim quotation; see Tier 9] | deferral_type: deferred | mixed_detail: n/a | reason_inferred: T1 (explicit prospective statement; specific future experiments not named) | linked_to: A-1, A-2, A-5 | cross_field_temperature: n/a

[B] B-1 | loc: P2:Lcol:1-5* (Results, "Nature of Support") | quote: [REDACTED: substantial verbatim quotation; see Tier 9] | classification: methodological_limitation | rhetorical_function: Justification of experimental design as enabling direct cross-catalyst comparison of leaching amounts. | note: Pd loading (wt%), dispersion, surface area, bed volume, void fraction, and PBR residence time are not reported for any of the three commercial catalysts. Equal Pd mass does not guarantee equivalent catalytic surface area, contact time, or Pd accessibility, so the claimed basis for direct comparison is not fully established. [metric incompleteness] | cross_field_temperature: V1-Q1=high, V1-Q2=high; convergence: 1 agent with multiple sub-questions; temperature_gap: n/a

[B] B-2 | loc: P3:Lcol:15-30* (Results, config 2 introduction) | quote: [REDACTED: substantial verbatim quotation; see Tier 9] | classification: mixed | rhetorical_function: Description of the modified reactor design used to isolate individual reaction component effects. | note: Configuration 2 eliminates the S1 sampling point used in configuration 1 to distinguish heterogeneous (PBR) from homogeneous (PFR) contributions. Any residual heterogeneous catalysis in the PBR cannot be detected; the conversion observed at the outlet is attributed entirely to leached Pd activity without verification. Also, the F2 mixing dilution factor and thermal equilibration between the two feed streams are unstated. [intentional_narrowing: design modification for component isolation; methodological_limitation: loss of PBR conversion monitoring] | cross_field_temperature: V1-Q3=high, V3-OV4(V3)=high; convergence: 2/3; temperature_gap: none

[B] B-3 | loc: P2:Lcol:30-40* (Results, "Nature of Support", FC-1001) | quote: [REDACTED: verbatim source quotation; see the source paper via its DOI] | classification: methodological_limitation | rhetorical_function: Quantitative cross-catalyst ranking of leaching by ICP–MS values. | note: No replicate ICP–MS experiments are reported for any catalyst or condition in the main text; no measurement uncertainty (expanded uncertainty, k=2), internal standard, or calibration range is stated. Without these, the numerical rankings (735 vs. 455 ppm, 96 vs. 6 ppm) lack statistical support. [metric incompleteness; negative result as evidence] | cross_field_temperature: V1-Q12=high, V2-OV2(V2)=medium, V3-OV1(V3)=critical; convergence: 3/3; temperature_gap: medium (critical(4)–medium(2) = 2 steps)

[B] B-4 | loc: P3:Rcol:5-20* (Results, Pd/Al2O3 at 30 °C) and P4:Rcol:5-15* (Pd/Al2O3, NEt3) | quote: [REDACTED: substantial verbatim quotation; see Tier 9] | classification: methodological_limitation | rhetorical_function: Claim that Pd/Al2O3 is effectively stable (no significant leaching) at ambient temperature in DMF. | note: The smallest Pd values in the paper (6, 10, 30, 36 ppm) are reported without a procedural blank, limit of detection, or limit of quantification for the ICP–MS protocol. "No significant leaching" claims rest on values that may be within measurement noise. [metric incompleteness; negative result as evidence] | cross_field_temperature: V1-Q9=medium, V3-OV3(V3)=high; convergence: 2/3; temperature_gap: low

[B] B-5 | loc: P3:Lcol:30-50* ("Assessment of Individual Reaction Components") | quote: [REDACTED: substantial verbatim quotation; see Tier 9] | classification: methodological_limitation | rhetorical_function: Statement of the analytical method for leaching quantification in configuration 2 experiments. | note: The protocol for fraction collection is not described: whether effluent was continuously pooled (180-min average) or collected as timed fractions. Time-averaged Pd concentrations cannot distinguish a burst of leaching (upon temperature step from 30 to 90 °C) from steady-state leaching, preventing kinetic interpretation of the leaching process. [metric incompleteness] | cross_field_temperature: V3-Q2=high; convergence: 1/3

[B] B-6 | loc: P2:Rcol:20-35* (Results, flow reactor, S1 vs. S2) | quote: [REDACTED: substantial verbatim quotation; see Tier 9] | classification: methodological_limitation | rhetorical_function: Claim that the tandem reactor design enables direct determination of leached Pd catalytic activity. | note: HPLC conversion measurements are presented as time-series plots (Figs. 4–9) but the minimum detectable conversion difference between S1 and S2 is not stated; no integration uncertainty or replicate injection RSD is reported. The claim of "identical" S1/S2 profiles (e.g., Fig. 4C,D) cannot be distinguished from profiles within measurement noise without this information. [metric incompleteness] | cross_field_temperature: V3-Q3=high; convergence: 1/3

[B] B-7 | loc: P1:Rcol:15-25* (Introduction) | quote: [REDACTED: substantial verbatim quotation; see Tier 9] | classification: methodological_limitation | rhetorical_function: Framing of prior approach that this paper improves upon by tracking catalytic activity of leached species. | note: No carbon balance, isolated yield, or mass balance for the Heck reaction product (methyl cinnamate) is reported in this paper either; only HPLC-based percent conversion is provided. Side products (biphenyl, stilbene) are not quantified. This leaves the overall material balance uncharacterized and prevents assessment of whether leached and heterogeneous Pd catalyze the same reaction pathway. [metric incompleteness] | cross_field_temperature: V1-Q5=medium; convergence: 1/3

[B] B-8 | loc: P3:Rcol:1-15* (Results, Pd/Al2O3, pseudosteady state) and P4:Rcol:20-30* (PhI section) | quote: [REDACTED: substantial verbatim quotation; see Tier 9] and [REDACTED: substantial verbatim quotation; see Tier 9] | classification: methodological_limitation | rhetorical_function: Claim of stability (pseudosteady state / no deactivation) for Pd/Al2O3 under specific conditions. | note: The Pd/Al2O3 experiments in DMF at 90 °C (Fig. 5C, 90 min) and in iodobenzene at 90 °C (Fig. 9A, 60 min) are terminated before long-term behavior is established; the claim of no deactivation is limited to the observation window. Whether the pseudosteady state persists, declines, or leads to catalyst regeneration beyond the observation period is not shown. | cross_field_temperature: V1-Q7=medium, V1-Q10=medium; convergence: 1 agent

[B] B-9 | loc: P2:Lcol:15-25* (Results, batch section) | quote: [REDACTED: substantial verbatim quotation; see Tier 9] | classification: methodological_limitation | rhetorical_function: Batch reactor data used to establish solvent effect context before flow reactor studies. | note: Batch reaction aliquots were not subjected to ICP–MS; color change is used as the sole proxy for leaching and Pd species formation. The quantitative extent of leaching in batch vs. flow is therefore not comparable, limiting the interpretation of batch vs. flow differences discussed in the Conclusions. | cross_field_temperature: V1-Q8=medium; convergence: 1/3

[B] B-10 | loc: P5:Lcol:1-10* (Conclusions) | quote: [REDACTED: substantial verbatim quotation; see Tier 9] | classification: mixed | rhetorical_function: Claim that the single-pass flow design eliminates boomerang catalysis and halide salt contributions. | note: [intentional_narrowing: single-pass flow is cited as a deliberate design feature that suppresses redeposition] [methodological_limitation: the PBR residence time is not reported and no quantitative comparison with Pd redeposition timescales is made; "not likely to be significant" is an inference without supporting data. The dismissal of halide salt leaching (ref 57) is similarly made without measuring PhI-derived iodide concentration in the effluent.] | cross_field_temperature: V1-Q11=medium, V2-Q9=medium; convergence: 2/3; temperature_gap: none

[B] B-11 | loc: P3:Rcol:15-30* (Results, Pd/Al2O3, NEt3 section) | quote: [REDACTED: substantial verbatim quotation; see Tier 9] | classification: mixed | rhetorical_function: Cross-reference to prior result used to highlight the generality of base effects on leaching from Pd/Al2O3. | note: [intentional_narrowing: the contrast between K2CO3/EtOH (leaching) and NEt3/DMF (no leaching) is acknowledged as interesting] [methodological_limitation: the paper identifies the contrast but provides no mechanistic explanation for why an inorganic base attacks the alumina support while the organic base does not; the structural/electronic basis for the differential behavior is not discussed and not deferred to future work — it is dropped.] | cross_field_temperature: V2-Q7=medium; convergence: 1/3

[B] B-12 | loc: P2:Rcol:35-45* (Results, dioxane and toluene) | quote: [REDACTED: substantial verbatim quotation; see Tier 9] | classification: intentional_narrowing | rhetorical_function: Conclusion that leached Pd is catalytically inactive in non-DMF solvents based on equivalent S1/S2 profiles. | note: The claim rests on HPLC conversion sensitivity (uncharacterized, see B-6). With 140 ppm Pd in solution (toluene case), the absence of detectable S2 > S1 activity is attributed to catalytic inactivity rather than sub-detection-threshold activity. The conclusion conflates "no detectable activity" with "catalytically inactive" — a metric limitation with mechanistic implications for the DMF stabilization narrative. [negative result as evidence; linked to A-5] | cross_field_temperature: V1-Q14=medium, V2-OV4(V2)=medium; convergence: 2/3; temperature_gap: none

[B] B-13 | loc: P4:Lcol:1-10* (Results, PdEnCat, NEt3 conclusion) | quote: [REDACTED: substantial verbatim quotation; see Tier 9] | classification: methodological_limitation | rhetorical_function: Quantitative comparison across two different reactor configurations used as the primary evidence that NEt3 is the dominant leaching agent. | note: The 182 ppm (configuration 2, NEt3 at F1, PhI + acrylate at F2) and 194 ppm (configuration 1, full reaction mixture) values originate from different experimental setups run at different times, with potentially different flow rates, dilution factors at F2, and fraction collection protocols. The paper does not verify experimental equivalence between the two conditions being compared. In addition, both values lack measurement uncertainty (see B-3); the 6% difference (182 vs. 194 ppm) may be within ICP-MS variability. The conclusion that "NEt3 is the biggest culprit" depends entirely on the validity of this comparison. [metric incompleteness; categorically discontinuous conditions] | cross_field_temperature: V1-Q4=high, V2-OV3(V2)=high, V3-OV2(V3)=critical; convergence: 3/3; temperature_gap: low

[B] B-14 | loc: P3:Lcol:15-30* (config 2 description) | quote: [REDACTED: substantial verbatim quotation; see Tier 9] | classification: methodological_limitation | rhetorical_function: Description of fluid mixing in configuration 2 enabling catalytic activity testing of leached Pd. | note: The F1:F2 volumetric flow ratio (dilution factor at F2) is not stated; if the F1 and F2 streams have different flow rates, the Pd concentration entering the PFR is not equal to the concentration leaving the PBR. Thermal equilibration between two streams at different temperatures before the PFR is also unstated. These parameters affect the calculated catalytic activity of the leached species. | cross_field_temperature: V1-Q13=medium, V3-Q6=medium; convergence: 2 questions from different agents

[B] B-15 | loc: P2:Lcol:30-45* (Results, FC-1001 at 30 °C) | quote: [REDACTED: substantial verbatim quotation; see Tier 9] | classification: methodological_limitation | rhetorical_function: Quantitative description of catalytic performance of FC-1001 leachate. | note: No turnover number (TON) or turnover frequency (TOF) is calculated for any leached Pd species across any experiment; catalytic performance is presented as time-course conversion only, preventing comparison with homogeneous Pd catalysts or assessment of catalyst efficiency. [metric incompleteness] | cross_field_temperature: V3-Q8=medium; convergence: 1/3

[C] C-1 | loc: P1:Rcol:5-15* (Introduction) | citation: refs 10, 11 (Chagunda et al. 2023, Organometallics; Gorunova et al. 2018, Organometallics — mercury poisoning test unreliability) | textual_function: Cited to undermine the credibility of mercury poisoning tests, justifying the use of the tandem flow reactor approach instead. | reason_severed: The paper dismisses the mercury test as unreliable and then proceeds with its own method; no further engagement with refs 10/11 or their experimental methodology. | affects_claims: yes — this citation supports the positioning of the paper's approach as necessary, but if the mercury test results for these specific catalysts were still available, they could complement or contextualize the flow reactor data. | symmetric_pattern: yes

[C] C-2 | loc: P1:Rcol:20-35* (Introduction) | citation: refs 18, 19 (Rothenberg/Thathagar nanofiltration two-compartment reactor) | textual_function: Cited as the earliest example of a two-compartment in situ leaching study using physical separation, as context for the current tandem flow approach. | reason_severed: "not stated in paper" — no comparison of results or detection sensitivity between nanofiltration and flow reactor approaches. | affects_claims: medium — the Rothenberg approach also uses physical separation; a direct comparison would clarify whether the tandem flow reactor offers superior sensitivity or mechanistic resolution, but this comparison is not made. | symmetric_pattern: no

[C] C-3 | loc: P2:Rcol:5-15* (Results, DMF stabilization) | citation: refs 45-48 (Yano et al. 2013, J. Organomet. Chem.; Ishida et al. 2020, ACS Omega; Nagata et al. 2019, RSC Adv.; Onishi et al. 2018, RSC Adv. — DMF-stabilized Pd nanoclusters) | textual_function: Cited as supporting evidence that DMF generates and stabilizes catalytically active Pd nanoclusters in cross-coupling reactions. | reason_severed: The claim "consistent with literature reports" is made without engaging with the specific size ranges, preparation conditions, or turnover data of the cited nanocluster studies. | affects_claims: yes — the Pd nanocluster stabilization claim is a key mechanistic inference for why leached Pd is active in DMF but inactive in dioxane/toluene; the unsupported delegation to literature weakens A-5. | symmetric_pattern: yes (all four cited uniformly to support the same claim by analogy)

[C] C-4 | loc: P4:Rcol:30-40* (Results, Pd/Al2O3 cluster speculation) | citation: refs 54, 55 (Heinz et al. 2013, Phys. Chem. Chem. Phys.; Polynski & Ananikov 2019, ACS Catal. — computational ArX leaching from Pd surfaces) | textual_function: Cited to provide mechanistic precedent for the speculative claim that leached Pd/Al2O3 species are clusters. | reason_severed: The computational results are not described, compared to the experimental observations, or used to generate testable predictions. | affects_claims: yes — the Pd cluster hypothesis for Pd/Al2O3 leachate (A-1) is the primary mechanistic claim distinguishing Pd/Al2O3 from polymer-supported catalysts; its evidential basis rests entirely on these unsummarized computational papers. | symmetric_pattern: yes

[C] C-5 | loc: P5:Lcol:1-10* (Conclusions) | citation: ref 56 (Gruttadauria et al. 2013, Green Chem. — "release and catch" boomerang catalysis); ref 57 (de Vries et al. 2002, Adv. Synth. Catal. — halide salt leaching) | textual_function: Cited to name two potential contributions to catalytic activity that are then immediately dismissed as unlikely under the experimental conditions. | reason_severed: Both references are dismissed without quantitative engagement (no estimate of redeposition rate or halide concentration). | affects_claims: medium — if boomerang catalysis or halide salt leaching does contribute, the attribution of activity entirely to leached Pd species would require revision; the dismissal is qualitative only. | symmetric_pattern: yes (both cited and dismissed with the same rhetorical move)

[U] U-1 | loc: not recoverable | quote: [REDACTED: substantial verbatim quotation; see Tier 9] | question: What is the activation energy for α-hydride elimination by NEt3 in the context of the polyurea matrix, and does confinement lower the effective barrier relative to solution-phase Pd(OAc)2 + amine? | originating_agent: V2 (V2-Q10) | severity: medium | note: T3 [external inference]; speculative mechanism not mentioned in the paper, requires computational or kinetic study outside the paper's scope. Retained as a D-4 candidate for its structural novelty (polyurea confinement effect on amine-Pd reaction temperature).

[META]
  linked_items:
    - A-1 ↔ A-4: Both address unresolved speciation of leached Pd from different support types
    - A-1 ↔ B-13: Cluster speculation (A-1) relies on the same absent speciation data that B-13 flags as a measurement gap
    - A-2 ↔ A-3: Both concern the NEt3–Pd interaction mechanism; A-2 (reduction at 30 °C) and A-3 (coordination of amine to Pd(0)) are sequential steps in the proposed pathway
    - A-5 ↔ B-12: DMF stabilization hypothesis (A-5) is the mechanistic counterpart to the "inactive in dioxane/toluene" claim (B-12)
    - A-5 ↔ C-3: The DMF deferral (A-5) is operationalized by the uncontinued citation of Pd nanocluster literature (C-3)
    - A-1 ↔ C-4: The Pd cluster speculation (A-1) is supported only by the uncontinued computational citations (C-4)
    - B-3 ↔ B-13: Absence of measurement uncertainty (B-3) is the metrological reason why the central quantitative comparison (B-13) cannot be evaluated
    - B-10 ↔ C-5: Boomerang/halide dismissal in Conclusions (B-10) is operationalized by the cite-and-dismiss of refs 56, 57 (C-5)

  same_root_groups:
    - SRG-1 [ICP-MS measurement validity absent]: B-3, B-4, B-5, B-13
      root: [REDACTED: substantial verbatim quotation; see Tier 9]
    - SRG-2 [Leached Pd species never directly characterized]: A-1, A-3, A-4, B-13
      root: [REDACTED: substantial verbatim quotation; see Tier 9]
    - SRG-3 [Catalyst characterization absent]: B-1
      root: [REDACTED: substantial verbatim quotation; see Tier 9]
    - SRG-4 [Configuration 2 measurement blind spot]: B-2, B-14
      root: [REDACTED: substantial verbatim quotation; see Tier 9]
    - SRG-5 [DMF role mechanistically underdetermined]: A-5, B-12, C-3
      root: [REDACTED: substantial verbatim quotation; see Tier 9]
    - SRG-6 [NEt3 mechanism suppressed]: A-2, A-3, A-6
      root: [REDACTED: substantial verbatim quotation; see Tier 9]

  symmetric_citations:
    - C-3, C-4: Both cited uniformly to support speculative claims without engaging individual results
    - C-1: symmetric (two references cited to dismiss a technique)
    - C-5: symmetric (two references cited to dismiss a mechanism)

  unreported_data:
    - Replicate ICP-MS experiments (implied by use of single values; Section S1.2 and Table S1 may contain raw data, but completeness not stated)
    - LOD/LOQ and procedural blank for ICP-MS
    - Pd speciation data (no reference to attempted measurement)
    - Batch reaction ICP-MS (mentioned as not done in main text for batch experiments)
    - Catalyst surface area, Pd wt%, dispersion for PdEnCat 30, FC-1001, Pd/Al2O3
    - PBR bed volume, void fraction, and calculated residence time for each catalyst

  series_signal: no — paper references prior work by same group (refs 22, 23, 26, 28) and announces future directions but does not announce a planned series. T2 [paper-grounded inference].

[TEMPERATURE_SUMMARY]
  high_convergence_high_gap:
    - B-3 (convergence 3/3; temperature_gap: medium — V1=high, V2=medium, V3=critical)
  high_convergence_low_gap:
    - B-13 (convergence 3/3; temperature_gap: low — V1=high, V2=high, V3=critical)
    - B-2 (convergence 2/3; temperature_gap: none — V1=high, V3=high)
    - B-10 (convergence 2/3; temperature_gap: none — V1=medium, V2=medium)
    - B-12 (convergence 2/3; temperature_gap: none — V1=medium, V2=medium)
    - B-4 (convergence 2/3; temperature_gap: low — V1=medium, V3=high)
    - A-5 (convergence 2/3; temperature_gap: low — V1=medium, V2=high)
    - A-1 (convergence 2/3; temperature_gap: none — V2=high, V3=high)
  low_convergence_high_gap:
    - (none: all critical-severity items from V3 are also covered by high-convergence groups above)

[GAP]
  GAP-1 | type: 1 | priority: high | description: Ref 23 (Newton, Ferri, Mulligan et al. 2020, Catal. Sci. Technol.) — own earlier in situ XAS study of K2CO3-induced Pd leaching from Pd/Al2O3 — cited for the K2CO3 vs. NEt3 contrast (B-11) but not retrieved; the structural mechanism of alumina attack by inorganic base vs. organic base stability is directly relevant to A-1 and B-11. | candidate_paper: Newton M.A. et al., Catal. Sci. Technol. 2020, 10, 466-474 | inference_label: T1 | status: pending
  GAP-2 | type: 1 | priority: high | description: Refs 54, 55 (Heinz et al. 2013; Polynski & Ananikov 2019) — computational studies of ArX-induced atom leaching from Pd nanoparticles — cited in support of Pd cluster speculation (A-1) but not described; computational predictions about cluster vs. atom leaching would constrain A-1. | candidate_paper: Ramezani-Dakhel et al., Phys. Chem. Chem. Phys. 2013, 15, 5488; Polynski & Ananikov, ACS Catal. 2019, 9, 3991 | inference_label: T1 | status: pending
  GAP-3 | type: 3 | priority: high | description: A study directly characterizing Pd speciation in flow reactor effluents (XAS, ESI-MS, or SEC-ICP-MS) would resolve A-1, A-4, and the SRG-2 root; ref 20 (Reimann et al. 2011, JACS) and ref 21 (Yuan et al. 2018, JACS) are relevant prior art for operando XAS speciation. | candidate_paper: Reimann et al., J. Am. Chem. Soc. 2011, 133, 3921; Yuan et al., J. Am. Chem. Soc. 2018, 140, 8206 | inference_label: T2 [paper-grounded inference] | status: pending
  GAP-4 | type: 2 | priority: medium | description: Unacknowledged contemporaneous studies on amine-induced low-temperature reduction of supported Pd(II) to Pd(0) as a leaching mechanism; the 30 °C α-hydride elimination claim (A-2) appears novel but no systematic literature search for this specific temperature window is cited. | candidate_paper: not identified | inference_label: T2 [paper-grounded inference] | status: pending

inference_time_sec: not available — inject externally
```

---

> **Tier 8 redaction notice**: This file is a redacted copy of the corresponding Tier 3 / Tier 9 output. Verbatim source-paper quotations have been replaced by `[REDACTED: see source paper §<loc>; full text retained in Tier 9 reviewer-only deposit]` markers, preserving location references and our own analytical content. Bibliographic fields (title, authors, journal, year, DOI), analytical labels (`evidence_chain:` with B-/U-/A-/C- internal IDs), short technical terms, and our own analytical text are not redacted. The redaction was applied by `scripts/redact_for_tier8.py` and, for this version, by `scripts/build_paperA_R1_public.py` with `scripts/redact_source_ngram_runs.py` (scripts of the project repository; they are not deposited).
