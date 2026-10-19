```
prompt_version: stage1-v17-20260415
model_info: claude-sonnet-4-6

target_title:   Nickel-Catalyzed Asymmetric Kumada Cross-Coupling of Symmetric Cyclic Sulfates
target_authors: Meredith S. Eno, Alexander Lu, and James P. Morken
target_start:   page 1: [REDACTED: paper boundary quote; see Tier 9]
target_end:     end of document

[Agent fields]
V1: Asymmetric transition-metal catalysis / enantioselective cross-coupling — specialist in Ni-catalyzed C–C bond-forming selectivity, catalyst design, and substrate scope evaluation.
V2: Mechanistic and physical organic chemistry — specialist in reaction mechanism, oxidation-state assignment, kinetic/thermodynamic selectivity analysis, and evidentiary standards for catalytic cycle proposals.
V3: Analytical chemistry / stereochemical analysis and chromatographic method validation — specialist in er measurement validity (SFC), yield quantification, and statistical reporting standards.

--- Step 0: Boundary recheck ---
All quoted passages from Turns 1–3 originate from the single target paper (4 pp). No adjacent-paper contamination detected. All quotes pass boundary check.

--- Step 1: Cross-field temperature computations ---

V1-Q7 / B-1: V1=high, V2-OV1=high, V3-OV2=high → convergence 3/3, temperature_gap=none
V1-Q8 / B-2: V1=high, V2-OV2=critical → convergence 2/3, temperature_gap=low
V1-Q10 / B-3 (component): V1=high, V2-OV3=high → convergence 2/3, temperature_gap=none
V1-Q9 / B-13: V1=medium, V2-OV4=medium → convergence 2/3, temperature_gap=none
V1-Q6 / B-7 (component): V1=low, V3-OV1=medium → convergence 2/3, temperature_gap=low
V1-Q4 / B-4: V1=medium, V3-OV3=medium → convergence 2/3, temperature_gap=none
V2-Q3 / B-1 (component): V2=high, V3-OV4=high → convergence 2/3, temperature_gap=none
V1-Q14 / B-15: V1=medium, V3-OV5=medium → convergence 2/3, temperature_gap=none
B-2 aggregate (V1-Q8+V2-Q4+V3-Q3+V3-Q4): V1=high, V2=critical, V3=high → convergence 3/3, max=critical(4), min=high(3), temperature_gap=low
B-3 aggregate (V1-Q10+V2-Q2+V2-Q5): V1=high, V2=high/medium → convergence 2/3, temperature_gap=low (V2-Q5=medium)

--- Step 2: Same-root groups ---

SRG-1 "Radical clock — evidentiary sufficiency of negative result"
  Members: B-1 (V1-Q7+V2-Q3), U-1
  Shared root: The radical-clock negative result (no product 25 detected) is interpreted as proof of non-radical mechanism, but 44% mass balance is unaccounted for, detection sensitivity for product 25 is unstated, and no rate-window analysis is provided to bound the kinetic competitiveness of the probe.

SRG-2 "Stereospecificity experiment — measurement and interpretive validity"
  Members: B-2 (V1-Q8+V2-Q4+V3-Q3+V3-Q4), U-3
  Shared root: The 90% diastereospecificity value (eq 8, Scheme 3) and its mechanistic interpretation as evidence for SN2-like oxidative addition rest on three unverified elements: (a) the RE retention assumption, (b) uncharacterized reference compound purity, and (c) an unstated analytical method for ds determination.

SRG-3 "Catalytic cycle — Ni species and elementary step characterization"
  Members: B-3 (V1-Q10+V2-Q2+V2-Q5), U-4, B-18, B-19
  Shared root: The proposed Ni catalytic cycle (Scheme 4) assigns Ni oxidation states, identifies a pyboxNi(Ar) species as the reacting agent, and describes transmetalation to regenerate the catalyst, but none of these mechanistic elements has experimental support (spectroscopy, kinetics, stoichiometric reaction, or intermediate trapping).

SRG-4 "Scope failure — unquantified and undiagnosed substrate limitations"
  Members: B-4 (V1-Q4), B-5 (V1-Q5), A-1 (V2-Q11), B-14 (V1-Q13)
  Shared root: The paper identifies multiple substrate classes that fail or give diminished selectivity (ortho-ArMgBr, alkyl/alkenylMgX, glycerol substrate, tertiary alcohol/quaternary center substrates) but provides no quantitative yield/er data and no mechanistic diagnosis for any of these failures.

SRG-5 "Enantioselectivity measurement — analytical traceability"
  Members: B-6 (V3-Q1), B-7 (V1-Q6+V3-Q2)
  Shared root: Er values for 17 products are reported without specifying SFC column identity, conditions, or detector; and without reporting individual run values or uncertainty, making the enantioselectivity data non-reproducible and non-verifiable.

SRG-6 "MgBr2 side reaction — characterization and catalytic-condition relevance"
  Members: B-11 (V1-Q2+V2-Q8+V3-Q5)
  Shared root: The MgBr2 side reaction with cyclic sulfate 1 (giving a 3-bromopropanol derivative) is identified as a potential problem, the aging hypothesis is stated but untested, and the side-reaction product is uncharacterized; whether this side reaction competes under the catalytic conditions is unknown.

---

[A]
A-1 | P3:Rcol (conclusion) + P3:Lcol (Scheme 2 inset) | [REDACTED: substantial verbatim quotation; see Tier 9] | deferred | n/a | T1 | linked_to: B-4, B-5, B-14, U-4 | cross_field_temperature: V2-Q11=medium (V2), convergence 1/3

---

[B]
B-1 | P3:Lcol, Scheme 3 eq 7 | [REDACTED: substantial verbatim quotation; see Tier 9] [yield of 24: 56%] | mixed (reporting_omission + methodological_limitation) | Negative result used as sole evidence against radical intermediates. | note: 44% mass balance unaccounted for; "only detected" claim lacks stated detection limit for ring-opened product 25; no rate-window analysis to establish that the cyclopropylcarbinyl radical probe is kinetically competent within the Ni-catalyzed reaction rate — both the reporting gap (missing mass balance) and methodological gap (rate window) independently undermine the non-radical inference. Flags: negative_result_as_evidence; metric_incompleteness. See also U-1 (self-contradictory absence). | cross_field_temperature: V1=high, V2-OV1=high, V3-OV2=high; convergence 3/3, temperature_gap=none

B-2 | P3:Lcol–P3:Rcol, Scheme 3 eq 8 and following paragraph | [REDACTED: substantial verbatim quotation; see Tier 9] [diastereospecificity: 90%] | mixed (methodological_limitation) | Stereospecificity argument presented as mechanistic evidence for SN2-like oxidative addition. | note: (a) RE retention is explicitly stated as an assumption without experimental or cited support — if RE is not stereospecific, the deduced OA stereochemistry is undetermined; (b) the 10% ds erosion is unexplained (partial radical pathway, epimerization, or reference compound impurity); (c) purity of isotopically labeled reference compounds for the ds comparison is not stated; (d) the analytical method used to determine 90% ds (NMR integration, SFC, HPLC, MS?) is absent from the main text. Flags: negative_result_as_evidence; methodological_limitation. See also U-3 (self-contradictory absence). | cross_field_temperature: V1=high, V2-OV2=critical, V3-Q3/Q4=high; convergence 3/3, temperature_gap=low

B-3 | P3:Rcol, Scheme 4 and paragraph | [REDACTED: substantial verbatim quotation; see Tier 9] | mixed (methodological_limitation + reporting_omission) | Proposed catalytic cycle describing reactive Ni species, oxidative addition step, and transmetalation. | note: (a) Ni oxidation state at each step is unspecified — Ni(0)/Ni(II) and Ni(I)/Ni(III) pathways are both consistent with the proposed reactivity and have different stereoelectronic implications for the SN2-like OA claim; (b) no spectroscopic characterization of any Ni intermediate (NMR, EPR, UV-Vis, cyclic voltammetry) is reported; (c) no evidence for the transmetalation step (stoichiometric reaction, kinetics, byproduct identification) is presented. See also U-4 (self-contradictory absence). | cross_field_temperature: V1=high, V2-OV3=high (V1-Q10 component); V2-Q2=high, V2-Q5=medium; convergence 2/3, temperature_gap=low (due to V2-Q5=medium)

B-4 | P2:Rcol, last paragraph of substrate scope | [REDACTED: substantial verbatim quotation; see Tier 9] | reporting_omission | Scope limitation stated qualitatively without data for failed substrate classes. | note: No yield values, er values, or conversion data are tabulated for these failed classes; whether "lower yield" is <20% or <50% and whether "nearly racemic" is 50:50 or 60:40 cannot be assessed; standard synthetic chemistry scope reporting requires at least representative data points for stated limitations. Flags: metric_incompleteness; scope_failure_not_quantified. | cross_field_temperature: V1=medium, V3-OV3=medium; convergence 2/3, temperature_gap=none

B-5 | P3:Lcol, Scheme 2 inset | [REDACTED: substantial verbatim quotation; see Tier 9] | reporting_omission | Scope restriction framed by showing unreactive substrate structures only. | note: Two unreactive substrate structures shown but no yield, conversion, or recovered starting material data are given; "ineffective" is not defined (0% conversion? trace yield? poor selectivity?); no mechanistic attribution for the failure mode (steric, electronic, substrate coordination to Ni?) is offered; linked to A-1. Flags: metric_incompleteness; scope_failure_not_quantified.

B-6 | P2:Rcol, Table 2 footnote | [REDACTED: substantial verbatim quotation; see Tier 9] | reporting_omission | Analytical method citation for all er values in Table 2. | note: Column identity (manufacturer, stationary phase type), mobile phase composition, flow rate, co-solvent gradient, UV detection wavelength, and whether a single method was used for all 17 structurally diverse products are all absent; for aliphatic primary alcohols with weak UV chromophore, detector suitability is unverified; without these details the er data are non-reproducible. Flags: metric_incompleteness; analytical_method_undisclosed. SRG-5.

B-7 | P2:Rcol, Table 2 footnote | "Results are an average of two experiments." | reporting_omission | Statement of replication basis for all Table 2 yield and er values. | note: Individual run values, standard deviation, or range are not given; for entries near the lower end of selectivity (88:12 to 92:8), the combined analytical uncertainty of SFC integration (±0.5–1 er unit) and run-to-run variability may represent a substantial fraction of the deviation from high selectivity; the claim that selectivity is "maintained" across the scope cannot be evaluated without uncertainty intervals. Flags: metric_incompleteness. | cross_field_temperature: V1=low, V3-OV1=medium; convergence 2/3, temperature_gap=low

B-8 | P2:Lcol (Table 1 and Table 2 respectively) | Table 1: "58%: 92:8 er[REDACTED: substantial verbatim quotation; see Tier 9]2, 84% y, 96:4 er" (L5, −25 °C, 24-h hydrolysis) for the same product 2 with PhMgBr | reporting_omission | Yield and er values for compound 2 reported at two different temperatures and catalyst protocols without reconciliation. | note: The 26-percentage-point yield increase and 4-er-unit improvement on going from Table 1 conditions to Table 2 conditions are not explicitly attributed to the temperature change (0 °C → −25 °C) or other condition differences; the jump is not discussed in the text, making the relationship between the two data sets opaque to the reader.

B-9 | P2:Lcol, paragraph 2 | [REDACTED: substantial verbatim quotation; see Tier 9] [referring to Table 1 ligand survey done with incomplete 6-h hydrolysis] | reporting_omission | Disclosure that initial Table 1 yields were suboptimal due to incomplete hydrolysis. | note: Whether the er values in Table 1 were re-measured under the 24-h hydrolysis conditions is not stated; if yields differ significantly under incomplete hydrolysis (mixed sulfate-half ester / alcohol products), er values from the two conditions may not be directly comparable, complicating the ligand selectivity comparison.

B-10 | P1:Rcol, paragraph 3 | [REDACTED: substantial verbatim quotation; see Tier 9] | methodological_limitation | Grignard aging protocol specified as a requirement for the optimal coupling. | note: Whether the 15-h aging at 4 °C was validated as optimal for each ArMgBr used in the substrate scope (Table 2, compounds 8–18) is not stated; MgBr2 precipitation rates may differ across aryl Grignard reagents; if aging was only optimized for PhMgBr, the yield and selectivity data for other Grignard reagents may be sub-optimal and inconsistent.

B-11 | P1:Rcol, paragraph 3 | [REDACTED: substantial verbatim quotation; see Tier 9] | mixed (methodological_limitation + reporting_omission) | Disclosure of MgBr2 side reaction as rationale for Grignard aging protocol. | note: (a) The 3-bromopropanol derivative is named but not characterized (no NMR, MS, isolated yield); (b) the MgBr2 aging precipitation hypothesis is labeled as a suspicion ("we suspect") but no confirmatory experiment (deliberate MgBr2 addition/removal) is reported; (c) under catalytic conditions with Ni and Grignard reagent, the degree to which MgBr2 (if not fully precipitated) competes with the Ni catalyst for the cyclic sulfate substrate is not assessed. SRG-6.

B-12 | P2:Lcol, paragraph 2 | [REDACTED: substantial verbatim quotation; see Tier 9] | reporting_omission | Statement of temperature optimization outcome. | note: The magnitude of the er improvement on going from 0 °C to −25 °C is described as "slight" without quantification (e.g., 93:7 → 96:4?); the corresponding yield at −25 °C relative to 0 °C is also not reported; a selectivity–reactivity trade-off at lower temperature is a mechanistically and synthetically relevant question left unaddressed.

B-13 | P3:Rcol, Scheme 4 paragraph | [REDACTED: substantial verbatim quotation; see Tier 9] | methodological_limitation | Mechanistic proposal for the reactive substrate conformation. | note: The axial-conformation reactive rotamer is inferred from selectivity/efficiency similarity across substituents but without conformational NMR data, DFT minimization, or the specific conformational energy data from ref 21 applied to these substrates; the argument is a plausibility inference, not a demonstrated mechanistic assignment. | cross_field_temperature: V1=medium, V2-OV4=medium; convergence 2/3, temperature_gap=none

B-14 | P3:Lcol, Scheme 2 eq 6 | [REDACTED: substantial verbatim quotation; see Tier 9] | mixed (methodological_limitation + reporting_omission) | Data report for heteroatom-functionalized glycerol substrate. | note: The 75:25 er (approximately 1.4 kcal/mol ΔΔG‡ vs. ~1.9 kcal/mol for top performers) represents substantial erosion but no mechanistic explanation is offered (OBn group coordination to Ni? Different substrate conformation?); linked to A-1 (heteroatom scope is the stated future direction); the failure analysis would inform that future direction.

B-15 | P2:Rcol, Table 2 footnote b | "[REDACTED: verbatim source text; see the source paper via its DOI]" [standard: 3.0%, 3.3%] | reporting_omission | Non-standard catalyst loading for substrate 14. | note: Doubled catalyst loading for the para-fluorophenyl Grignard substrate is stated without rationale; whether doubling loading was required for reactivity (electronic deactivation by fluorine), selectivity, or reflects catalyst deactivation under these conditions is not stated; results with standard loading (3%) are not reported alongside, making the efficiency comparison ambiguous. Flags: substrate_selection_bias; categorically_discontinuous_conditions. | cross_field_temperature: V1=medium, V3-OV5=medium; convergence 2/3, temperature_gap=none

B-16 | P3:Lcol, Scheme 2 eq 5 | [REDACTED: substantial verbatim quotation; see Tier 9] [vs. 96:4 at small scale] | reporting_omission | Scale-up experiment result for compound 1/PhMgBr coupling. | note: The 4-er-unit erosion at gram scale (96:4 → 92:8) is described as "slight" without mechanistic comment; possible causes (heat-transfer effects, local temperature excursion during Grignard addition, catalyst concentration variation, incomplete MgBr2 precipitation at larger volume) are not discussed; synthetically, 92:8 vs. 96:4 is a meaningful difference for downstream applications.

B-17 | P2:Lcol, paragraph 1 | [REDACTED: substantial verbatim quotation; see Tier 9] | reporting_omission | Ligand screening conclusion from Table 1. | note: The structural basis for PyBox superiority (vs. BINAP, phosphoramide) is not discussed; 6 ligands are screened but the phosphorus-based ligands shown in Table 1 give near-racemic products (50:50 er) with no indication of whether this reflects an intrinsic selectivity limitation or a condition mismatch; no rationale for PyBox's selectivity advantage is offered even at the qualitative level.

B-18 | P3:Rcol, Scheme 4 paragraph | [REDACTED: substantial verbatim quotation; see Tier 9] | methodological_limitation | Argument for the identity of the enantioselectivity-determining step. | note: The argument uses er variation across ArMgBr reagents to infer that the ArMgBr-containing Ni complex is the reacting species, but whether enantioselectivity is kinetically or thermodynamically controlled is never tested; kinetic analysis (Eyring analysis, temperature-dependent er), isothermal rate measurements, or competition experiments between ArMgBr reagents are absent; a Curtin–Hammett scenario in which facial selectivity is set by the relative rates of competing TS diastereomers — not by the resting-state speciation — is neither excluded nor considered. Part of SRG-3.

B-19 | P3:Rcol, Scheme 4 paragraph | [REDACTED: substantial verbatim quotation; see Tier 9] | methodological_limitation | Proposal for the identity of the reacting Ni complex. | note: Kinetic order in ArMgBr concentration is not determined; NMR or spectroscopic evidence for the pyboxNi(Ar) complex in solution under catalytic conditions is absent; the claim rests on selectivity-pattern inference alone (different ArMgBr → different er). Part of SRG-3.

B-20 | P2:Rcol, Table 2 (products 8–16) | [REDACTED: substantial verbatim quotation; see Tier 9] | reporting_omission | Claim of selectivity uniformity across electronically varied Grignard reagents. | note: The er range for products 8–16 spans 91:9 to 96:4 (ΔΔG‡ variation of ~0.7 kcal/mol at −25 °C); no Hammett analysis or linear free-energy correlation is presented for the aryl Grignard series; the claim of "similar" selectivity implicitly asserts electronic insensitivity of the TS, but this is stated as an observation rather than a conclusion supported by analysis.

---

[C]
C-1 | P1:Lcol, introduction | Refs 3, 4, 5 (Lou/Fu JACS 2010; Mao/Zhong/Bian JACS 2014 and Wu/Zhong/Bian Tetrahedron:Asymm 2016; Jin/Nakamura JACS 2015) | Cited to introduce and motivate the [REDACTED: verbatim source quotation; see the source paper via its DOI]) relies on differentiation from these works, but no quantitative basis for the distinction (better er, broader scope, lower catalyst loading) is provided | symmetric_pattern: yes (all three follow the identical cite-and-introduce pattern without any numerical follow-through in the results)

C-2 | P1:Lcol, introduction | Refs 7, 8, 9 (Studte/Breit Angew. 2008; López-Pérez/Carretero Org. Lett. 2009; Taylor/Jarvo JACS 2011 and sequels) | Cited to introduce the "enantiospecific" class of Kumada couplings as the second established strategy. | reason_severed: Cited as a contrast class (enantiospecific vs. the present enantioselective work), but no quantitative comparison of their selectivity, substrate scope, or activation requirements is made in the results section; the mechanistic distinction (two-electron stereospecific with nonracemic substrates vs. the present prochiral approach) is described qualitatively in the introduction only. | affects_claims: medium — the paper's claim to offer a new strategy is partly validated by this contrast, but the absence of quantitative comparison leaves the scope of the advance unspecified | symmetric_pattern: yes

C-3 | P1:Rcol, paragraph 2 | Refs 12a, 12b (Sun/Morken JACS 2014; Potter/Morken JACS 2014) | Cited as intellectual precursor: [REDACTED: substantial verbatim quotation; see Tier 9] | reason_severed: The structural and mechanistic connection to the bis(boronate) work is invoked to motivate the present work, but no comparison of selectivity levels, mechanism, or substrate generality between the geminal bis(boronate) coupling and the present cyclic sulfate coupling is provided. | affects_claims: medium — the citation establishes precedent for the reaction design concept but the lack of comparison leaves the mechanistic analogy unvalidated | symmetric_pattern: no

C-4 | P1:Rcol, paragraph 2 | Refs 13 (Rovis review and subexamples), 14 (Hayashi/Kamikawa JACS 1995; Kamikawa/Hayashi Tetrahedron 1999) | Cited to establish that [REDACTED: substantial verbatim quotation; see Tier 9] | reason_severed: Ref 14 describes Hayashi/Kamikawa Kumada desymmetrization (with palladium, axially chiral substrates) as direct precedent, but no comparison of their er values, catalyst systems, or substrate scope to the present Ni/PyBox system is offered; the cite merely acknowledges prior Kumada desymmetrization without establishing the quantitative advance. | affects_claims: medium — ref 14 is the closest prior art for the present reaction class; the absence of a comparison leaves the improvement over prior Kumada desymmetrization unquantified | symmetric_pattern: partial (ref 13 is a review and is background; ref 14 is direct prior art and closer to the paper's claim)

C-5 | P3:Rcol, Scheme 4 paragraph | Ref 21 (Lowe, Thatcher, Turner, Waller, Watkin; J. Am. Chem. Soc. 1988, 110, 8512) | Cited as basis for the low-energy equatorial preference of the C5 substituent in cyclic sulfates, used to contrast with the proposed axially-reactive conformation A. | reason_severed: The reference is invoked to establish that the equatorial conformation (B) is the ground-state preference, which then makes the axial reactive conformation (A) a high-energy reactive conformer argument; however, no conformational energy data from this reference are reproduced or compared for the specific substituted cyclic sulfates used in the present paper; the applicability of 1988 conformational data to variously substituted cyclic sulfates is assumed. | affects_claims: yes — the mechanistic model in Scheme 4 depends on this conformational preference being applicable to these substrates, but the transfer is not validated | symmetric_pattern: no

---

[U]
U-1 | P3:Lcol, Scheme 3 eq 7 | [REDACTED: substantial verbatim quotation; see Tier 9] [yield: 56%] | Does the 44% unaccounted mass balance contain radical-derived, rearranged, or Ni-mediated byproducts that would undermine the non-radical inference? | V1+V2+V3 (SRG-1) | high (convergence 3/3) | note: self-contradictory absence — the paper's proposed non-radical Ni-mediated mechanism predicts that substrate 23 should give only the coupling product 24 (and sulfate byproduct E), yet 44% of the mass balance is unaccounted for and neither characterized nor acknowledged as a limitation; the "only detected" claim is dependent on an unstated detection limit for ring-opened product 25; this is both a reporting omission (B-1) and a self-contradictory absence because the proposed mechanism itself predicts what the missing 44% should not be.

U-2 | P3:Rcol, Scheme 4 paragraph | [REDACTED: substantial verbatim quotation; see Tier 9] | Is the enantioselectivity of the reaction kinetically or thermodynamically controlled, and does the enantioselection occur at the ring-opening (OA) step as assumed or at a later stage (e.g., transmetalation, reductive elimination)? | V2 | high | note: This question does not fit A (no explicit deferral to future work), B (it is not a standard reporting datum whose absence can be described as an omission — the experiment was not designed to test kinetic vs thermodynamic control), or C (no citation gap); it represents a fundamental mechanistic question that the paper's proposed model assumes to be resolved but provides no evidence for; the question is analytically important for evaluating whether the proposed TS model in Scheme 4 is correctly assigned.

U-3 | P3:Lcol–P3:Rcol, Scheme 3 eq 8 paragraph | [REDACTED: substantial verbatim quotation; see Tier 9] | If C–C reductive elimination does not proceed with strict retention, what is the actual stereochemical outcome of the oxidative addition step? | V1+V2+V3 (SRG-2) | high/critical (convergence 3/3) | note: self-contradictory absence — the paper's proposed SN2-like OA mechanism predicts that OA proceeds with stereoinversion; this prediction is deduced under the assumption that RE gives retention; the mechanism itself predicts that RE should proceed with retention (as part of the inner-sphere two-electron cycle), but this prediction of the paper's own mechanism is not tested; if the RE assumption fails, the stereochemical assignment of the OA step is indeterminate; this is both B-2 (methodological limitation — stated assumption without evidence) and a self-contradictory absence.

U-4 | P3:Rcol, Scheme 4 | [REDACTED: substantial verbatim quotation; see Tier 9] | The proposed catalytic cycle predicts the generation of specific Ni complexes (pyboxNi(Ar) C, Ni–sulfate complex E) — why are none of these intermediates detected, characterized, or isolated stoichiometrically? | V1+V2 (SRG-3) | high (convergence 2/3) | note: self-contradictory absence — the paper's proposed catalytic cycle in Scheme 4 predicts specific organometallic intermediates; the paper neither reports observing these intermediates nor acknowledges that their non-observation is a limitation; this is both B-3 (methodological limitation — catalytic cycle proposed without characterization) and a self-contradictory absence because the cycle's own logic predicts they must exist in solution during the reaction.

---

[META]
  linked_items:
    A-1 ↔ B-4 (scope failures are the boundary condition for the deferred future work)
    A-1 ↔ B-5 (unreactive substrates are the direct experimental correlate of A-1's deferred scope)
    A-1 ↔ B-14 (glycerol substrate erosion is a partial case of the heteroatom failure to be addressed)
    B-1 ↔ U-1 (same passage — reporting omission and self-contradictory absence are complementary)
    B-2 ↔ U-3 (same passage — methodological limitation and self-contradictory absence)
    B-3 ↔ U-4 (same passage — catalytic cycle limitation and self-contradictory absence)
    B-3 ↔ B-13 (Ni active species identity affects which reactive conformation is relevant)
    B-3 ↔ B-18 ↔ B-19 (all derive from catalytic cycle mechanistic underdetermination — SRG-3)
    C-1 ↔ C-2 (symmetric citation abandonment of both comparison classes in intro)
    C-3 ↔ C-4 (both are conceptual/precedent citations that established the reaction design but were not quantitatively engaged)
    U-3 ↔ B-13 (the reactive conformation assignment and RE retention assumption are both elements of the Scheme 4 stereochemical model)

  same_root_groups:
    SRG-1 [B-1, U-1]: Radical-clock negative result; shared root: inadequate evidentiary support for the non-radical mechanistic conclusion from a single negative-result experiment with unaccounted mass balance and no rate-window analysis.
    SRG-2 [B-2, U-3]: Stereospecificity experiment; shared root: the 90% ds value (eq 8) and its interpretation as evidence for stereoinvertive OA rest on an untested RE retention assumption, unstated reference compound purity, and an absent analytical method description.
    SRG-3 [B-3, U-4, B-18, B-19]: Catalytic cycle mechanistic support; shared root: the proposed Ni catalytic cycle assigns Ni species, oxidation states, and a reacting complex identity without any spectroscopic, kinetic, or stoichiometric experimental evidence.
    SRG-4 [B-4, B-5, B-14, A-1]: Scope failure characterization; shared root: all substrate classes that fail or underperform are described qualitatively without yield/er data or mechanistic attribution.
    SRG-5 [B-6, B-7]: Enantioselectivity analytical traceability; shared root: er values are the paper's primary quantitative claim but are reported without SFC method specification or uncertainty quantification.
    SRG-6 [B-11]: MgBr2 side reaction; shared root: the identified MgBr2/cyclic sulfate side reaction is stated but neither characterized nor assessed for impact under catalytic conditions.

  symmetric_citations: C-1 and C-2 (both abandoned after introduction introduction, same function)

  unreported_data:
    - Yield and er for ortho-ArMgBr, alkyl-, and alkenyl-MgX substrate classes (stated to fail; no data given)
    - Yield and conversion for unreactive substrates in Scheme 2 inset
    - Individual run values and SD for Table 2 yield and er averages
    - SFC analytical conditions (column, mobile phase, detector) for all 17 products
    - Analytical characterization of the 3-bromopropanol MgBr2 side-reaction product
    - Analytical method and reference compound characterization for 90% ds determination (eq 8)
    - Ni intermediate characterization (any form) under catalytic or stoichiometric conditions
    - Temperature at which er improvement occurs on going from 0 °C to −25 °C (magnitude)

  series_signal: yes [T2 paper-grounded inference] — "Studies in this connection are in progress" (P4:Lcol, conclusion) implies a planned follow-up study on heteroatom-substituted and quaternary-center substrates; linked to A-1.

[TEMPERATURE_SUMMARY]
  high_convergence_high_gap: (empty — no item has convergence ≥ 2/3 AND temperature_gap = medium or high; the largest gap is temperature_gap=low for B-1, B-2, B-3, B-7)

  high_convergence_low_gap: B-1 (3/3, gap=none), B-2 (3/3, gap=low), B-3 (2/3, gap=low), B-4 (2/3, gap=none), B-7 (2/3, gap=low), B-13 (2/3, gap=none), B-15 (2/3, gap=none), U-1 (3/3, gap=none), U-3 (3/3, gap=low)

  low_convergence_high_gap: (empty — no single-agent item has critical severity)

[GAP]
GAP-1 | Type 1 | high | Retrieve ref 21 (Lowe et al., JACS 1988, 110, 8512) to assess whether the conformational preferences of cyclic sulfates reported therein are applicable to the substituted substrates in Table 2 and quantitatively support the axial reactive-conformation proposal in Scheme 4 | Lowe, G.; Thatcher, G. R. J.; Turner, J. C. G.; Waller, A.; Watkin, D. J. J. Am. Chem. Soc. 1988, 110, 8512 | T1 | pending

GAP-2 | Type 1 | medium | Retrieve refs 3, 4, 5 (Fu JACS 2010; Zhong/Bian JACS 2014; Nakamura JACS 2015) to extract specific er values and substrate scope data for quantitative comparison with the present work, establishing the advance beyond prior enantioconvergent Kumada couplings | Lou/Fu; Mao/Zhong/Bian; Jin/Nakamura (see C-1 citations) | T1 | pending

GAP-3 | Type 1 | medium | Retrieve ref 14 (Hayashi/Kamikawa JACS 1995; Kamikawa/Hayashi Tetrahedron 1999) to extract er values and substrate scope for direct comparison as the most closely related prior Kumada desymmetrization | Hayashi, T.; Niizuma, S. et al. JACS 1995, 117, 9101; Kamikawa, T.; Hayashi, T. Tetrahedron 1999, 55, 3455 | T1 | pending

GAP-4 | Type 2 | high | Check for contemporaneous (2014–2016) studies on Ni(I)/Ni(III) vs. Ni(0)/Ni(II) oxidation-state manifolds in Ni-catalyzed cross-coupling reactions with nitrogen-donor (PyBox-type) ligands, which would establish mechanistic precedent relevant to the catalytic cycle assignment | candidate: Diao/Stahl and Engle/Sanford groups' work on Ni(I)/Ni(III) in cross-coupling (circa 2014–2016) [T3 external inference] | T3 | pending

GAP-5 | Type 3 | medium | Future publication from the Morken group on heteroatom-substituted cyclic sulfate coupling and quaternary center construction (explicitly signaled in series_signal) would directly answer A-1 and SRG-4 issues | not yet known | T2 | pending

inference_time_sec: not available — inject externally
```

---

> **Tier 8 redaction notice**: This file is a redacted copy of the corresponding Tier 3 / Tier 9 output. Verbatim source-paper quotations have been replaced by `[REDACTED: see source paper §<loc>; full text retained in Tier 9 reviewer-only deposit]` markers, preserving location references and our own analytical content. Bibliographic fields (title, authors, journal, year, DOI), analytical labels (`evidence_chain:` with B-/U-/A-/C- internal IDs), short technical terms, and our own analytical text are not redacted. The redaction was applied by `scripts/redact_for_tier8.py` and, for this version, by `scripts/build_paperA_R1_public.py` with `scripts/redact_source_ngram_runs.py` (scripts of the project repository; they are not deposited).
