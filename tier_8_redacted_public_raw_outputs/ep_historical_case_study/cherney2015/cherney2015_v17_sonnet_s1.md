prompt_version: stage1-v17-20260415
model_info: claude-sonnet-4-6

target_title:   Enantioselective and Enantiospecific Transition-Metal-Catalyzed Cross-Coupling Reactions of Organometallic Reagents To Construct C−C Bonds
target_authors: Alan H. Cherney, Nathaniel T. Kadunce, and Sarah E. Reisman
target_start:   page 1: [REDACTED: paper boundary quote; see Tier 9]
target_end:     end of document

[Agent fields]
V1: Transition-metal-catalyzed asymmetric synthesis — the journal (Chem. Rev.), paper format (review), and methodology (systematic literature survey of enantiocontrolled C–C bond formations) identify this as the primary disciplinary home; V1 interrogates scope consistency, classification rationale, and mechanistic claim grounding from the perspective of a practitioner in asymmetric catalysis.
V2: Mechanistic / physical organic chemistry — the review proposes and discusses numerous catalytic cycle mechanisms (DYKAT, DKR, SE2(cyclic)/SE2(open), radical OA, DET) without kinetic evidence; V2 interrogates rate-determining steps, kinetic/thermodynamic control of selectivity, and the evidentiary basis for mechanistic assignments.
V3: Analytical chemistry / systematic review methodology — the primary evidence is compiled ee/es and yield values across 40 years of literature from diverse research groups; V3 interrogates comparability of analytical methods, yield-type consistency, and systematic coverage completeness.
V4: Synthetic applications / complex molecule synthesis — V1–V3 do not address whether the surveyed methods have been validated in multi-step synthesis of complex targets, which is the primary practical utility test for a synthetic methodology review.

[V4 insert — Agent V4]
field: Synthetic applications / complex molecule synthesis
field_rationale: V1–V3 interrogated classification consistency, mechanistic evidence quality, analytical reporting standards, and kinetic/thermodynamic interpretation; none asked whether the enantiocontrolled cross-coupling methods surveyed have been demonstrated in multi-step synthesis of structurally complex targets—a critical criterion for assessing practical synthetic value and the one most directly accessible to the review's stated audience of synthetic chemists.

V4-Q1
loc: P38:Lcol:1–20* (Section 6, Conclusion and Future Outlook)
quote: [REDACTED: see `loc:` above; full text in Tier 9]
question: The conclusion asserts that these methods "streamline the synthesis of complex molecules," but the body of the review discusses applications in natural product or drug synthesis only in isolated examples (e.g., the goniofurane synthesis in Section 3.1.2, glucokinase activator in Section 3.1.4, (+)-bourgenic acid in Section 4.2.3). Is there a systematic inventory of which methods surveyed have been applied in multi-step synthesis of natural products or pharmaceutical compounds, and what fraction of the 100+ methods described have been validated beyond a single test substrate?
severity: medium
inference_tier: T2 [paper-grounded inference]

V4-Q2
loc: P9:Rcol:28–40* (Section 2.2.1, Fu group, α-bromoamide Negishi, loading)
quote: [REDACTED: see `loc:` above; full text in Tier 9]
question: Many reactions in this review use catalyst loadings of 5–15 mol%, which are standard in academic methodology development but impractical for industrial or large-scale synthesis (typically <1 mol% is required). The review does not discuss whether any of the enantioselective cross-coupling methods surveyed have been demonstrated at catalyst loadings ≤1 mol% or at scale (>10 mmol). Have any of the methods in Sections 2–5 been reduced to practice at lower loading or demonstrated at multi-gram scale?
severity: medium
inference_tier: T2 [paper-grounded inference]

V4-Q3
loc: P2:Lcol:10–25* (Introduction, definition of cross-coupling)
quote: [REDACTED: see `loc:` above; full text in Tier 9]
question: Many of the organometallic reagents discussed in this review (especially enantiopure sec-alkylboron, sec-alkylsilane, and sec-alkylstannane compounds) are not commercially available and require multi-step preparation. The review does not discuss the synthetic accessibility of these coupling partners, which is a practical barrier to broad adoption. For what fraction of the enantiospecific methods in Section 3 does the preparation of the required enantiopure organometallic reagent require more synthetic steps than the cross-coupling itself?
severity: medium
inference_tier: T2 [paper-grounded inference]

V4-Q4
loc: P16:Rcol:1–10* (Section 3.1.2, Stille cross-coupling, (+)-goniofurane synthesis)
quote: [REDACTED: see `loc:` above; full text in Tier 9]
question: The goniofurane synthesis is one of few total synthesis applications presented in detail. However, the review does not report the overall yield and ee of the final natural product, nor whether the Stille coupling step was the enantioselectivity-limiting step in the synthesis. Without this information, the application does not demonstrate that the surveyed enantiospecific coupling is compatible with the overall synthetic sequence rather than merely with the isolated test substrates.
severity: medium
inference_tier: T2 [paper-grounded inference]

V4-Q5
loc: P11:Rcol:20–35* (Section 2.2.3, Fu group Suzuki-Miyaura for homobenzylic systems)
quote: [REDACTED: see `loc:` above; full text in Tier 9]
question: The review notes that "heterocyclic scaffolds could be prepared with good efficiency" in Ni-catalyzed Suzuki-Miyaura reactions. Heterocycles are ubiquitous in pharmaceuticals, and their compatibility with Ni catalysis (which is known to be sensitive to basic nitrogen donors that can coordinate and inhibit the catalyst) is a critical practical consideration. The review does not discuss whether the heterocyclic examples required protecting group manipulation or modified conditions, nor whether the nitrogen-containing products were obtained with the same level of enantioselectivity as carbocyclic analogs.
severity: medium
inference_tier: T2 [paper-grounded inference]

V4-Q6
loc: P25:Lcol:15–30* (Section 4.1, Cu-catalyzed allylic substitution, scope review)
quote: [REDACTED: see `loc:` above; full text in Tier 9]
question: The difficulty of aryl Grignard allylic substitution is noted, but the review does not discuss whether this limitation affects access to pharmacologically relevant motifs—specifically, whether any of the Cu-catalyzed enantioselective allylic substitution methods have been applied to the synthesis of FDA-approved drugs or clinical candidates bearing the allylic stereocenters that these methods are designed to install. Not stated in paper.
severity: low
inference_tier: T1

V4-Q7
loc: P38:Rcol:1–20* (Section 6, Conclusion)
quote: [REDACTED: see `loc:` above; full text in Tier 9]
question: The review identifies the preparation of enantiopure C(sp³) boron and tin reagents as the primary bottleneck for stereospecific coupling methods. However, it does not survey the most recent (2012-2014) asymmetric hydroboration, C-H borylation, and deprotonation/borylation methods that might provide routes to such starting materials. Are there methods in the literature that address this bottleneck and have not been incorporated into the review's prospective assessment?
severity: medium
inference_tier: T2 [paper-grounded inference]

V4-Q8
loc: P13:Rcol:30–45* (Section 2.3.2, Pd-catalyzed desymmetrization of meso-ditriflate)
quote: [REDACTED: see `loc:` above; full text in Tier 9]
question: The review presents moderate yield (not stated quantitatively for this example) combined with good ee as a satisfactory outcome. In complex target synthesis, the yield of each step is compounded through the synthesis. A step with 40% yield at good ee would limit synthetic utility regardless of ee. The review does not provide a systematic analysis of yield-ee trade-offs across the desymmetrization reactions in Section 2.3, nor does it identify which reactions achieve simultaneously high yield (>80%) and high ee (>90%).
severity: medium
inference_tier: T2 [paper-grounded inference]

V4-OV1 | overlaps_with: V1-Q13 | severity_V4: medium | note: V1 notes the undefined relationship between amide substituent identity and ee; from a synthetic applications perspective, the limitation to specific amide structures restricts the direct synthetic utility of the Fu α-bromoamide Negishi method because amide identity is dictated by the target molecule's structure, not by catalyst optimization.

V4-OV2 | overlaps_with: V1-Q10 | severity_V4: medium | note: The ligand synthesis accessibility issue (V1-Q10) is directly relevant to synthetic applications: if a chiral ligand requires >5 steps to prepare and is not commercially available, it constitutes a practical barrier to adoption that the review does not quantify.

V4-OV3 | overlaps_with: V3-Q6 | severity_V4: medium | note: From a synthetic applications perspective, GC vs. isolated yield is especially critical: a reaction reporting 95% GC yield for a volatile product may give <50% isolated yield, fundamentally changing the assessment of synthetic utility for the method.

---

[A] A-1
loc: P38:Lcol:1–20* (Section 6, Conclusion)
quote: [REDACTED: see `loc:` above; full text in Tier 9]
deferral_type: deferred
mixed_detail: n/a
reason_inferred: T1
linked_to: B-5
cross_field_temperature: V1-Q11=medium; convergence=1/3; temperature_gap=n/a

[A] A-2
loc: P38:Lcol:20–40* (Section 6, Conclusion)
quote: [REDACTED: see `loc:` above; full text in Tier 9]
deferral_type: deferred
mixed_detail: n/a
reason_inferred: T1
linked_to: B-5
cross_field_temperature: V4-Q7=medium; convergence=1/3; temperature_gap=n/a

[A] A-3
loc: P38:Rcol:1–15* (Section 6, Conclusion)
quote: [REDACTED: see `loc:` above; full text in Tier 9]
deferral_type: deferred
mixed_detail: n/a
reason_inferred: T1
linked_to: n/a
cross_field_temperature: V4-Q1=medium; convergence=1/3; temperature_gap=n/a

[A] A-4
loc: P8:Lcol:35–45* (Section 2.1.3, photoredox)
quote: [REDACTED: see `loc:` above; full text in Tier 9]
deferral_type: deferred
mixed_detail: n/a
reason_inferred: T1
linked_to: B-6, U-3
cross_field_temperature: V1-Q14=medium, V2-OV5=high; convergence=2/3; temperature_gap=low

[B] B-1
loc: P3:Lcol:40–55* (Section 2.1.1, DYKAT)
quote: [REDACTED: see `loc:` above; full text in Tier 9]
classification: reporting_omission
rhetorical_function: Mechanistic framework statement establishing DYKAT as the operative mechanism for enantioselective cross-coupling of labile organometallic reagents.
note: The review invokes DYKAT as the standard mechanistic explanation for enantioselective sec-alkylmagnesium coupling throughout Sections 2.1 and 2.2, but no cited reaction reports the ratio krac/kproductive needed to verify the kinetic requirement for DYKAT (krac >> kproductive); conversion-dependent ee profiles that would distinguish DYKAT from kinetic resolution are also absent. [SRG-1 anchor]
cross_field_temperature: V1-Q4=high, V2-Q1=high (OV1), V3-OV3=high; convergence=3/3; temperature_gap=none

[B] B-2
loc: P1:Rcol:1–10* (Table of Contents / Introduction)
quote: [REDACTED: see `loc:` above; full text in Tier 9]
classification: reporting_omission
rhetorical_function: Scope statement defining the temporal and thematic coverage of the review.
note: No search methodology, databases consulted, inclusion/exclusion criteria, or PRISMA-style transparency statement is provided; the completeness of literature coverage is unverifiable. [SRG-3 partial anchor; V3-Q7]
cross_field_temperature: V3-Q7=medium; convergence=1/3; temperature_gap=n/a

[B] B-3
loc: P4:Lcol:5–20* (Figure 5 caption)
quote: [REDACTED: see `loc:` above; full text in Tier 9]
classification: mixed (methodological_limitation + reporting_omission)
rhetorical_function: Footnote-style disclaimer qualifying the comparability of ee values in Figure 5.
note: The caution is applied locally to Figure 5 but not extended systematically throughout the review, where analogous cross-study comparisons are made without comparable disclaimers. The inconsistent application of the caveat constitutes a reporting_omission for all other cross-study comparisons; the methodological_limitation component is that different analytical methods and reaction conditions make comparison inherently unreliable, which is acknowledged only here. [SRG-3 anchor; V3-Q2]
cross_field_temperature: V3-Q2=medium, V1-Q5=medium (SRG-3 related); convergence=2/3; temperature_gap=none

[B] B-4
loc: P9:Rcol:25–40* (Section 2.2.1, scope limitation with disubstituted alkenes)
quote: [REDACTED: see `loc:` above; full text in Tier 9]
classification: methodological_limitation
rhetorical_function: Scope limitation statement identifying disubstituted alkene electrophiles as poorly performing substrates.
note: The cause of the limitation (competing β-hydride elimination from the alkyl-Pd intermediate, steric effects on transmetalation, or geometric effects on reductive elimination) is not stated in the paper; the limitation is presented as observed fact without mechanistic attribution or proposal for how to overcome it. [SRG-2 related; V1-Q6]
cross_field_temperature: V1-Q6=medium; convergence=1/3; temperature_gap=n/a

[B] B-5
loc: P38:Lcol:1–20* (Section 6, Conclusion)
quote: [REDACTED: see `loc:` above; full text in Tier 9]
classification: intentional_narrowing
rhetorical_function: Prospective statement identifying two underdeveloped areas as future targets.
note: The distinction between "no reported attempts" and "attempted but failed" for the tert-alkyl and sec×sec categories is not made explicit; several reactions in Sections 3.1–3.2 do couple sec-electrophiles with sec-nucleophiles, and the criteria for "stereocontrolled" vs. "not yet realized" are not stated. The narrowing is intentional in that the authors chose not to review these areas, but the rationale (no good examples exist) is not documented with negative results from the cited literature. [linked: A-1, A-2]
cross_field_temperature: V1-Q11=medium; convergence=1/3; temperature_gap=n/a

[B] B-6
loc: P8:Rcol:1–15* (Section 2.1.3, Ni/Ir photoredox)
quote: [REDACTED: see `loc:` above; full text in Tier 9]
classification: mixed (methodological_limitation + reporting_omission)
rhetorical_function: Proof-of-concept presentation introducing dual Ni/Ir photoredox catalysis as a new approach to asymmetric cross-coupling.
note: The 50% ee result is presented as a "proof of concept" (methodological_limitation: low ee acknowledged), but the oxidation potentials of the organoboron substrate and excited-state Ir complex are not reported, leaving the thermodynamic feasibility of the proposed SET step unverified (reporting_omission). No Stern–Volmer quenching data is provided to establish that the organoboron actually quenches *Ir excited state. [SRG-6 anchor; linked: A-4, U-3]
cross_field_temperature: V1-Q14=medium, V2-Q10=high, V2-OV5=high; convergence=3/3; temperature_gap=low

[B] B-7
loc: P25:Lcol:5–15* (Section 4.2.1, Pd π-allyl intermediate convergence argument)
quote: [REDACTED: see `loc:` above; full text in Tier 9]
classification: methodological_limitation
rhetorical_function: Mechanistic argument using convergent product formation to infer a common π-allyl intermediate.
note: Convergence to a common product is necessary but not sufficient evidence for a π-allyl intermediate; the alternative (direct SN2' from different faces via DET-type trajectories) would also produce convergent products. No spectroscopic observation of the π-allyl Pd complex is reported. The limitation is that the review inherits this mechanistic inference from the primary paper without noting its logical incompleteness. [SRG-2; V2-Q7]
cross_field_temperature: V2-Q7=medium; convergence=1/3; temperature_gap=n/a

[B] B-8
loc: P3:Rcol:15–25* (Section 2.1.1, Kumada's early results with L3)
quote: [REDACTED: see `loc:` above; full text in Tier 9]
classification: mixed (reporting_omission + methodological_limitation)
rhetorical_function: Historical framing presenting early results as proof of concept while acknowledging mechanistic ambiguity.
note: Mass balance data for unreacted Grignard reagent, homodimerization, and protiodemetalation products are not reported in the review or stated to be absent in the primary papers; the ambiguity between KR and DYKAT (acknowledged explicitly here) is therefore also a reporting_omission since mass balance would constrain the mechanism. [SRG-1; V3-Q3]
cross_field_temperature: V3-Q3=medium; convergence=1/3; temperature_gap=n/a

[C] C-1
loc: P2:Lcol:1–15* (Introduction, references 4–6)
citation: refs 4–6 (Alexakis, Cu-catalyzed allylic substitution reviews, Chem. Rev. 2008 and related)
textual_function: Cited to justify the scope restriction: [REDACTED: substantial verbatim quotation; see Tier 9]
reason_severed: The review uses these citations to exclude Cu-catalyzed allylic substitution prior to 2008 without engaging their specific findings or discussing whether their scope coverage boundary coincides with the review's own boundary.
affects_claims: yes — the 2008 cutoff for Cu allylic substitution coverage is justified only by these three citations; if those reviews do not cover the same substrate/nucleophile combinations as the present review, the cutoff may create unacknowledged gaps.
symmetric_pattern: yes

[C] C-2
loc: P14:Rcol:20–35* (Section 3.1.1, Crudden Rh hydroboration citation)
citation: ref 162 (Edwards et al., Rh-catalyzed hydroboration for enantioselective secondary organoboronate synthesis)
textual_function: Cited to establish that the Crudden laboratory developed Rh-catalyzed hydroboration as a route to benzylic boronates used as substrates in subsequent stereospecific Suzuki-Miyaura coupling.
reason_severed: The specific enantioselectivity and substrate scope of the hydroboration step are not reported in the review; the review only states that [REDACTED: substantial verbatim quotation; see Tier 9] without noting whether the ee of 163 from hydroboration was reproduced in 164 (i.e., what the es of the coupling step was independently of the ee of the starting boronate).
affects_claims: yes — the es of the Suzuki-Miyaura step cannot be separately assessed from the overall ee of 164 unless the ee of the boronate starting material 163 is reported.
symmetric_pattern: no

[C] C-3
loc: P15:Lcol:10–20* (Section 3.1.2, Falck Stille coupling, Cu-mediated transmetalation refs 141–142)
citation: refs 141–142 (Lange et al. 2008, Falck Cu(I)-catalyzed stereospecific coupling of α-stannylated benzyl carbamates)
textual_function: Cited as examples of Cu-catalyzed stereospecific Stille coupling where Cu stabilizes the organocopper intermediate through coordination, preventing β-hydride elimination.
reason_severed: The review describes the mechanism (Cu stabilization via coordination) attributed to these papers but does not compare the es values achieved in these Cu-mediated reactions with those of the Pd-catalyzed Stille couplings discussed in the same subsection; a dropped quantitative benchmark — the es values from refs 141–142 are cited as support for a mechanistic hypothesis but are not tabulated alongside the Pd data.
affects_claims: medium — the claim that Cu-mediated Stille coupling is useful for this substrate class is supported by the cited references, but without comparative es data the practical advantage over Pd is not demonstrated.
symmetric_pattern: no

[C] C-4
loc: P25:Rcol:10–25* (Section 4.1.2, organozinc allylic substitution, Knochel refs 257 and related)
citation: refs 255–256 (Fiaud/Aribi-Zouioueche Pd-catalyzed allylic substitution with arylzinc, J. Organomet. Chem. 1985)
textual_function: Cited as the first report of Pd-catalyzed stereospecific allylic arylation with organozinc, establishing the precedent that the 1985 reaction gives product in "good yield and modest es."
reason_severed: The specific es value from the 1985 paper (ref 255) is not cited; only the qualitative assessment "good yield and modest es" appears, making it impossible to evaluate progress over the subsequent 15 years of development discussed in Section 4.2.
affects_claims: medium — the claim of progress in the field requires a baseline numerical comparison that this citation-without-data omits; dropped quantitative benchmark pattern.
symmetric_pattern: no

[C] C-5
loc: P13:Lcol:40–55* (Section 2.3.1, Breit enantiospecific Kumada-Corriu synthesis)
citation: ref 127 (Brand et al. 2009, iterative synthesis of (oligo)deoxypolypropionates via Zn-catalyzed enantiospecific sp³-sp³ cross-coupling)
textual_function: Cited to note that the Rh-catalyzed desymmetrization of meso-anhydrides constitutes [REDACTED: substantial verbatim quotation; see Tier 9]
reason_severed: The review does not compare the ee/yield/step-count of the Rh desymmetrization route with the Breit enantiospecific route for the same target compounds; the characterization as an "alternative" is asserted without data comparison; dropped quantitative benchmark.
affects_claims: medium — the claim that these are comparable routes to deoxypolypropionates is not supported by a performance comparison.
symmetric_pattern: no

[U] U-1
loc: P22:Lcol:10–25* (Section 4.1.1, DET for Cu-catalyzed cyclic allylic substitution)
quote: [REDACTED: see `loc:` above; full text in Tier 9]
question: Under DET, ee is predicted to be conversion-independent (distinguishing DET from KR where ee increases monotonically with conversion). Has the DET assignment been experimentally validated by time-course ee monitoring in the reaction of Figure 64?
originating_agent: V2-Q6
severity: high
note: Does not fit B (reporting_omission) alone because the paper's own proposed DET mechanism predicts a specific experimental signature (conversion-independent ee) that should be directly testable; the absence of this test constitutes a self-contradictory absence — the computational DET model predicts observable kinetic behavior that is not reported anywhere in the review or indicated as having been tested in the cited primary papers.

[U] U-2
loc: P30:Lcol:15–30* (Section 5.1.1)
quote: [REDACTED: see `loc:` above; full text in Tier 9]
question: Is the observed conversion-ee profile of 470 quantitatively consistent with s ≈ 5 as predicted by the Kagan-Durst equation, and does the reported 90% ee (Figure 91) correspond to the conversion expected for s = 5?
originating_agent: V2-Q9
severity: medium
note: The self-contradictory absence rule applies: the review's own mechanistic description (kinetic resolution with s ≈ 5) predicts a specific quantitative conversion-ee relationship, but no conversion data is reported alongside the 90% ee value in Figure 91; readers cannot verify whether the reported ee is kinetically consistent with the stated selectivity factor.

[U] U-3
loc: P8:Rcol:1–15* (Section 2.1.3, Ni/Ir dual catalysis)
quote: [REDACTED: see `loc:` above; full text in Tier 9]
question: The proposed mechanism generates IrII as a byproduct of the SET step and NiIII as an intermediate. Are either of these species spectroscopically characterized (UV-vis, EPR) or their redox potentials measured to confirm the thermodynamic feasibility of the electron transfer cascade?
originating_agent: V2-Q10
severity: high
note: Self-contradictory absence: the proposed dual catalytic cycle predicts the formation of specific paramagnetic intermediates (NiIII, IrII) with characteristic spectroscopic signatures; neither their direct observation nor their oxidation/reduction potentials are reported, and this absence prevents the mechanistic proposal from being distinguished from alternative pathways. B-6 records the thermodynamic feasibility gap as a reporting_omission; U-3 records the failure to test the paper's own proposed mechanism against its intermediate predictions.

[U] U-4
loc: P2:Lcol:30–50* (Introduction, enantiospecific definition)
quote: [REDACTED: see `loc:` above; full text in Tier 9]
question: The definition of enantiospecific reactions implies that the substrate's ee is fully transmitted to the product's ee. However, several "enantiospecific[REDACTED: substantial verbatim quotation; see Tier 9]partially enantiospecific" or discuss whether es erosion is a systematic function of reaction conditions, substrate structure, or catalyst identity.
originating_agent: V1-Q3 (extended)
severity: medium
note: Does not fit B (this is not a standard reporting omission) or C (not an uncontinued citation); the review's own definition of enantiospecific reactions implies 100% transmission, but the reported data (es values of 65-99% for many reactions in Section 3) contradicts this, making the classification framework internally inconsistent without discussion of where the stereochemical information is lost.

[META]
  linked_items:
    A-1 ↔ B-5 (both address sec×sec cross-coupling gap; B-5 is the in-review narrowing that motivates A-1's deferral)
    A-2 ↔ B-5 (preparative bottleneck for sp³ boron/tin is the practical reason for the deferred status in A-2)
    A-4 ↔ B-6 ↔ U-3 (photoredox proof-of-concept: A-4 defers optimization, B-6 reports the methodological limitation, U-3 records the self-contradictory absence)
    B-1 ↔ U-1 (DYKAT assumption: B-1 is the reporting_omission for krac/kproductive; DET analogue in U-1 is distinct but mechanistically related)

  same_root_groups:
    SRG-1: B-1, B-8, U-2 — root: the distinction between DYKAT, kinetic resolution, and kinetic-resolution-boosted ee requires conversion-dependent ee data that is absent throughout the review.
    SRG-2: B-4, B-7, U-1, U-3 — root: catalytic cycle mechanistic proposals (DYKAT, DET, π-allyl convergence, radical OA, SET) are discussed without direct experimental verification of the key mechanistic assignment step.
    SRG-3: B-2, B-3 — root: the comparability and completeness of compiled ee/yield data across research groups and time periods is systematically unaddressed.
    SRG-4: B-6, U-3, A-4 — root: the Ni/Ir photoredox dual catalytic cycle is proposed without thermodynamic or spectroscopic evidence for the key SET step.
    SRG-5: A-1, A-2, A-3, B-5 — root: the conclusion's prospective statements identify areas where the review itself is deliberately thin, but the boundary between "no literature exists" and "literature was excluded" is not documented.

  symmetric_citations: C-1 (refs 4–6 cited symmetrically to exclude pre-2008 Cu allylic substitution)

  unreported_data:
    - krac/kproductive ratios for DYKAT-assigned Ni-catalyzed reactions (would directly distinguish DYKAT from KR; referenced as the mechanistic basis for enantioselectivity throughout Sections 2.1–2.2)
    - Oxidation potentials of organoboron substrates and excited-state Ir photocatalyst in Section 2.1.3 (would establish SET thermodynamic feasibility)
    - Conversion-ee profiles for the DET reaction in Figure 64 (would validate DET vs. KR)
    - Conversion data alongside the 90% ee value for 470 in Figure 91 (needed to verify s ≈ 5 kinetic resolution model)
    - Mass balance data for early DYKAT reactions with low yields (Section 2.1.1, B-8)
    - Absolute configuration determinations for "100% es" reactions in Section 3 (V3-Q8)

  series_signal: no

[TEMPERATURE_SUMMARY]
  high_convergence_high_gap: [] (empty — normal case; no item shows convergence ≥ 2/3 with temperature_gap = medium or high)
  high_convergence_low_gap:
    B-1 [convergence=3/3, temperature_gap=none, all agents=high]
    B-6 [convergence=3/3, temperature_gap=low, V1=medium/V2=high/V2-OV5=high]
    B-3 [convergence=2/3, temperature_gap=none, V1=medium/V3=medium]
    A-4 [convergence=2/3, temperature_gap=low, V1=medium/V2=high]
  low_convergence_high_gap:
    U-1 [convergence=1/3, V2-Q6=high — DET conversion-ee test absent]
    U-3 [convergence=1/3, V2-Q10=high — SET thermodynamic evidence absent]

[GAP]
GAP-1 | type=1 | priority=high | description: Retrieve the computational DFT study proposing DET for Cu/L32-catalyzed cyclic allylic substitution of 313 (cited as ref 252/253 in the review) to assess what level of theory was used and whether conversion-ee predictions were generated | candidate_paper: Langlois, J.-B.; Alexakis, A. Chem. Commun. 2009 or Langlois 2012 Adv. Synth. Catal. (refs 252-253) | inference_label: T1 | status: pending

GAP-2 | type=1 | priority=high | description: Retrieve Fu group's primary papers on the Ni/Ir photoredox dual catalysis reaction (Science 2014, ref 63, Tellis et al.) to determine whether Stern-Volmer quenching data, oxidation potentials, or EPR evidence for NiIII/IrII intermediates was reported in the primary paper but not mentioned in the review | candidate_paper: Tellis, J.C.; Primer, D.N.; Molander, G.A. Science 2014, 345, 433 (ref 63) | inference_label: T1 | status: pending

GAP-3 | type=3 | priority=medium | description: Papers reporting kinetic studies (krac/kproductive ratios) for DYKAT-operative Ni-catalyzed sec-alkylmagnesium coupling, needed to validate or refute the mechanistic classification used throughout Sections 2.1-2.2 | candidate_paper: Hayashi, T.; Tajika, M.; Tamao, K.; Kumada, M. J. Am. Chem. Soc. 1976, 98, 3718 or subsequent kinetic studies | inference_label: T3 [external inference] | status: pending

GAP-4 | type=2 | priority=medium | description: Systematic review / meta-analysis of enantioselective cross-coupling ee determination methods (chiral HPLC column types, optical rotation standards, NMR Mosher analysis) — would address the analytical comparability gap (SRG-3) that the review does not discuss | candidate_paper: not identified — general chiral analysis review | inference_label: T3 [external inference] | status: pending

GAP-5 | type=3 | priority=low | description: Papers reporting the synthesis of PPFA (L13) and related chiral ferrocenylphosphine ligands at scale, needed to evaluate whether the practical barrier to adoption of Ni/PPFA enantioselective coupling (noted in V4-Q2, V1-Q10) is a real bottleneck for synthetic applications | candidate_paper: Hayashi et al. accounts or commercial availability data | inference_label: T3 [external inference] | status: pending

inference_time_sec: not available — inject externally

---

> **Tier 8 redaction notice**: This file is a redacted copy of the corresponding Tier 3 / Tier 9 output. Verbatim source-paper quotations have been replaced by `[REDACTED: see source paper §<loc>; full text retained in Tier 9 reviewer-only deposit]` markers, preserving location references and our own analytical content. Bibliographic fields (title, authors, journal, year, DOI), analytical labels (`evidence_chain:` with B-/U-/A-/C- internal IDs), short technical terms, and our own analytical text are not redacted. The redaction was applied by `scripts/redact_for_tier8.py` and, for this version, by `scripts/build_paperA_R1_public.py` with `scripts/redact_source_ngram_runs.py` (scripts of the project repository; they are not deposited).
