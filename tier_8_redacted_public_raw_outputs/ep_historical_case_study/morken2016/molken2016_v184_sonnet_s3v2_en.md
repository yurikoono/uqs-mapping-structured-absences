prompt_version: stage3-v2-en-20260419
model_info: claude-sonnet-4-6

# Re-certification Assessment Sheet for Scientific Knowledge

## Eno, Lu, and Morken 2016 (Journal of the American Chemical Society, communication)

---

### §1 Claim Architecture

**Core claim summary:**
The paper claims a new enantioselective desymmetrization strategy for asymmetric Kumada coupling using prochiral symmetric cyclic sulfates as electrophiles and Ni(acac)₂/(R,R)-L5 (PyBox ligand) as the catalyst. The Novelty pillar rests on two interlocked sub-claims: (a) a substrate-design claim — cyclic sulfates enforce two-electron inner-sphere C–O cleavage, attenuate the second C–O bond after first coupling, and restrict conformational diversity relative to acyclic bis-electrophiles (N-2); and (b) a mechanistic claim — oxidative addition of the Ni(0)(PyBox) complex to the cyclic sulfate C–O bond proceeds by a stereoinvertive SN2-like mechanism that is the enantioselectivity-determining step (N-4). The Utility pillar is the synthetic outcome: products bearing asymmetric tertiary carbon centers are delivered with up to 96:4 er across a 17-entry substrate scope (N-3), along with gram-scale operation, chroman synthesis, and isolable sulfate half-ester (N-1/N-3 utility extensions).

**Layered structure judgment:**
The claim architecture is explicitly three-layered (as confirmed by D-1 layered_structure): Layer 1 — the substrate class (prochiral cyclic sulfates as bis-electrophiles); Layer 2 — the synthetic result (enantioselective tertiary carbon center construction with high er); Layer 3 — the mechanistic assignment (SN2-like stereoinvertive Ni(0)/Ni(II) oxidative addition). The three layers are non-overlapping in the sense that refuting one layer does not collapse the others. However, the layers are not fully independent: the mechanistic claim (Layer 3) provides the interpretive framework for the substrate-design advantages claimed in Layer 1 (two-electron inner-sphere C–O cleavage requires the Ni(0)/Ni(II) manifold specifically), so a radical mechanism demonstration would not merely refute Layer 3 but would also undermine the stereoelectronic design rationale of Layer 1 (feature (a) of N-2). The most fragile layer is Layer 3 (mechanistic), because it rests on two qualitatively insufficient mechanistic probe experiments and no independent intermediate characterization; the most robust layer is Layer 2 (synthetic result), because er values are directly reported regardless of mechanism. A single refutation of Layer 3 does not collapse Layer 2, but it does destabilize the substrate-design logic of Layer 1.

---

### §2 SRG / CLA → RI / ER / EP Crosswalk

---

**SRG-1 [Mechanistic probe reliability — radical clock and deuterium labeling]**

* **Primary RI**: RI-04 Unreplicated discriminator
* **Secondary RI**: RI-03 Unobserved explanatory
* **ER**: The proposed two-electron Ni(0)/Ni(II) SN2-like mechanism requires that the mechanistic probe experiments (radical clock eq 7; deuterium-labeling eq 8) rule out the Ni(I)/Ni(III) radical manifold and independently establish the stereochemical course of each elementary step. A single radical clock at cyclopropylcarbinyl rates (~10⁸ s⁻¹) cannot discriminate Ni(0)/Ni(II) from Ni(I)/Ni(III) if reductive elimination from Ni(III) is faster than ring-opening; the ds measurement (eq 8) is interpretable only under the unstated and unverified assumption that C–C reductive elimination from a PyBoxNi(II)(alkyl)(aryl) complex proceeds with retention of configuration.
* **EP**: EP-04a Discrimination / replication pack; EP-03a Direct-observation / state-assignment pack
* **Case-specific implementation**: (1) Radical clock: replace the cyclopropylcarbinyl clock with a slower clock (vinyl epoxide ring-opening, ~10⁶ s⁻¹) to widen the temporal window for Ni(I)/Ni(III) radical recombination; or add a TEMPO trapping experiment and report a detection limit for the ring-opened product 25 by GC-MS at ≥5 mg/mL sensitivity. (2) Deuterium-labeling: establish the reductive elimination stereochemistry assumption independently by treating an isolated or in-situ-generated PyBoxNi(II)(alkyl-d₁)(Ph) complex — prepared from the same cyclic sulfate using stoichiometric Ni — with a base or reducing agent and measuring the stereochemical course of C–C bond formation by ²H NMR or chiral GC on a product of known absolute configuration.
* **Notes**: Members B-5, B-6, U-1. Both the radical clock (B-5) and the deuterium-labeling experiment (B-6) share a single root: the paper proposes a four-intermediate Ni(0)/Ni(II) catalytic cycle but provides no independently validated evidence for any elementary step or any intermediate. B-5 has convergence=3/3, temperature_gap=low (V1=high, V2=high, V3=medium); B-6 has convergence=3/3, temperature_gap=none (V1=high, V2=high, V3=high). U-1 is in the high_convergence_low_gap category (V1=high, V2=high). RI-04 is Primary because the two data points (one radical clock, one ds measurement) carry strong discriminatory power for the paper's mechanistic assignment but are interpreted at a high level without adequately excluding alternative pathways (Ni(I)/Ni(III) manifold; reductive elimination with inversion). RI-03 is Secondary because the key intermediates proposed in Scheme 4 (C, D, E, TS) are neither directly observed nor kinetically constrained by any stoichiometric experiment.

---

**SRG-2 [Ni oxidation-state and catalytic cycle characterization]**

* **Primary RI**: RI-03 Unobserved explanatory
* **Secondary RI**: RI-06 Imported model
* **ER**: The proposed catalytic cycle (Scheme 4) requires that four named intermediates (the PyboxNi(Ar) complex C, the Ni(II) alkyl-aryl complex D, the TS for stereoinvertive oxidative addition, and the Ni(II) sulfate E) are kinetically competent and spectroscopically accessible; these intermediates are central to the mechanistic explanation of enantioselectivity but are neither directly observed nor constrained by electrochemical, EPR, stoichiometric, or kinetic measurements. The Ni(0)/Ni(II) redox manifold is imported from the general mechanistic literature on Ni-catalyzed cross-coupling without demonstrating its isomorphism for the PyBox-Ni/cyclic sulfate system specifically.
* **EP**: EP-03a Direct-observation / state-assignment pack; EP-06a Analogy-validation pack
* **Case-specific implementation**: (a) Synthesize and characterize a stoichiometric PyboxNi(0)(arene) complex by XRD and cyclic voltammetry to confirm the Ni(0)/Ni(II) redox window under the reaction conditions; (b) Perform a kinetic study of the reaction rate vs. [PhMgBr], [1], and [Ni] to derive a rate law and assess whether it is consistent with the proposed catalytic cycle (turnover-limiting step assignment for C → TS vs. E → C transmetalation); (c) Assess by EPR whether Ni(I) or Ni(III) species accumulate during turnover — even negative EPR evidence at 10⁻⁴ M Ni would constrain the radical manifold contribution.
* **Notes**: Members U-1, B-13. SRG-2 shares the root with SRG-1 (both derive from the total absence of mechanistic characterization) but has a distinct evidentiary boundary: SRG-1 concerns the probe experiments that are presented, while SRG-2 concerns the intermediate characterization that is entirely absent. B-13 records that the transmetalation step (Ni(II) sulfate E → C with ArMgBr) is kinetically unassessed; for Ni(II) alkoxy/sulfonyloxy complexes this step can be rate-limiting, making the omission mechanistically consequential. RI-06 is Secondary because the Ni(0)/Ni(II) two-electron manifold is applied from the general Ni cross-coupling literature (ref 11) without demonstrating isomorphism for the sterically encumbered PyBox ligand + cyclic sulfate C–O electrophile system specifically.

---

**SRG-3 [Enantioselectivity basis — kinetic control and reaction coordinate]**

* **Primary RI**: RI-05 Qualitative overread
* **Secondary RI**: RI-06 Imported model
* **ER**: The proposed axial reactive conformation A as the stereocontrolling element requires that (a) the interpretation of substituent-size-insensitive er (products 2, 3, 4: methyl, ethyl, isopropyl → 96:4, 95:5, 96:4 er) uniquely supports axial C5 positioning of the C5 substituent in the TS, and (b) the reaction proceeds under kinetic control rather than thermodynamic control. Both requirements are derived qualitatively (the word "suggests" in Scheme 4 text) from a single set of er values without computational or temperature-dependent numerical support.
* **EP**: EP-05a Quantitative-ranking substantiation pack; EP-06a Analogy-validation pack
* **Case-specific implementation**: (a) Measure er for substrate 1 (methyl) at five temperatures from −40 °C to 0 °C and construct an Eyring plot to discriminate kinetic from thermodynamic control and to determine ΔΔH‡ and ΔΔS‡; (b) Prepare a conformationally biased cyclic sulfate in which the C5 group is forced equatorial by a gem-dimethyl constraint (1,3-dioxane analog) or axial by a trans-fused decalin constraint, and measure er; if axial conformation A is the reactive conformer, the equatorial-locked substrate should give dramatically lower er; (c) Perform DFT/M06-2X geometry optimization of the SN2-like approach of a model PyboxNi(0) fragment to cyclic sulfate conformers A and B, comparing the TS energies.
* **Notes**: Members B-9, U-2. B-9 records the absence of computational or discrimination experiments for the reactive conformation proposal (convergence=2/3, temperature_gap=none; V1=medium, V2=medium). U-2 records the non-uniqueness of the interpretation: er-insensitivity is equally consistent with equatorial conformation + backside attack from the less-hindered face, or with thermodynamic control. RI-05 is Primary because structural/causal implications (axial reactive conformation governs enantioselectivity) are derived from qualitative ranking (size-insensitive er values 96:4/95:5/96:4) without numerical support (no ΔΔG‡, no TS energies, no Eyring analysis). RI-06 is Secondary because the axial-attack geometry for SN2-like Ni(0) oxidative addition is imported from the general principle of backside SN2 attack without demonstrating isomorphism for the PyBox–Ni system's coordination geometry.

---

**SRG-4 [Grignard speciation and aging protocol]**

* **Primary RI**: RI-03 Unobserved explanatory
* **Secondary RI**: RI-01 Reporting integrity
* **ER**: The active transmetalating species (ArMgBr, Ar₂Mg, or mixed magnesiate) must be identified, and the mechanism by which the 15 h aging at 4 °C improves both yield and er must be specified, for the proposed catalytic cycle's transmetalation step (E → C, Scheme 4) to be defined; in the absence of this identification, the reaction's enantioselectivity and scope limitations cannot be mechanistically interpreted. Additionally, the er of the ligand-free Ni(cod)₂ background pathway (20% conversion) must be reported to decompose the apparent er in Table 1/2 into chiral-catalyst and background contributions.
* **EP**: EP-03a Direct-observation / state-assignment pack; EP-01a Reporting-coherence pack
* **Case-specific implementation**: (a) Prepare independently Ar₂Mg (from 2 ArMgBr + 1 MgBr₂ precipitation) and compare yield and er against freshly prepared ArMgBr and against aged ArMgBr in the coupling of 1 under otherwise identical conditions at −25 °C; (b) Measure the ²⁵Mg or ¹H NMR (in THF-d₈ at −25 °C) of freshly prepared and 15 h-aged PhMgBr to characterize Schlenk equilibrium speciation; (c) Report the er of the Ni(cod)₂-catalyzed background coupling of 1 with PhMgBr (20% conversion, 0 °C) to separate chiral and background contributions to the observed apparent er.
* **Notes**: Members B-2, B-4, B-10, U-4. SRG-4 is the largest SRG (4 members) and relates to the nucleophile side of the catalytic cycle. B-10 (background er absent; convergence=2/3, temperature_gap=none, V1=medium, V2=medium) and B-4 (failure-case data absent for ortho-Ar, alkyl, alkenyl Grignard reagents; V1 only, medium severity) together mean the paper cannot determine whether near-racemic failure cases arise from catalyst failure or from background pathway competition. U-4 is a prerequisite-absence item: the proposed catalytic cycle specifies the transmetalation step (E + ArMgBr → C) but the actual transmetalating species is unidentified. RI-01 is Secondary because the failure to report the background er prevents cross-comparison of the chiral-catalyst's true enantioselectivity against the apparent selectivity reported in Tables 1 and 2.

---

**SRG-5 [SFC analytical validation across substrate scope]**

* **Primary RI**: RI-08 Unquantified reliability
* **Secondary RI**: RI-01 Reporting integrity
* **ER**: The er values for all 17 Table 2 entries and all Table 1 entries constitute the primary evidentiary claim (enantioselectivity of a new asymmetric reaction), and their reliability requires that the SFC analytical method is documented to a level that permits independent verification: column identity, mobile phase, column temperature, flow rate, and resolution factors (Rs) for representative substrates must be reported, and run-to-run reproducibility (SD or range for the duplicate averages) must be stated alongside the means.
* **EP**: EP-08a Replication / uncertainty pack; EP-01a Reporting-coherence pack
* **Case-specific implementation**: (a) Report in SI: column manufacturer, column length/ID, mobile phase composition (CO₂/co-solvent ratio), flow rate, back pressure, and column temperature for each of the 17 Table 2 substrates; include representative SFC chromatograms showing baseline resolution with calculated Rs values for the two weakest entries (products 5 and 6, both 88:12 er); (b) Report the range of the two individual er measurements whose average constitutes each Table 2 entry (e.g., "runs: 87.8:12.2 and 88.3:11.7" for product 5), or report the SD; for entries near the 88:12 threshold, demonstrate that the analytical uncertainty is ≤ ±1 er unit.
* **Notes**: Members U-3, B-8. U-3 is the high-severity, low-convergence item (V3 primary, severity=high) identifying the total absence of SFC column/method documentation. B-8 is the medium/high-severity, convergence=2/3 item (V1=medium, V3=high, temperature_gap=low) identifying the absence of SD/range. Together they constitute a paired analytical integrity gap: neither the systematic (method documentation) nor the random (run-to-run reproducibility) component of the er measurement uncertainty is reported for the paper's central evidentiary claim. RI-08 is Primary because the enantioselectivity dataset lacks replicate measurements with uncertainty descriptions (mean ± SD) and the SFC resolution infrastructure for evaluating the data's analytical validity. RI-01 is Secondary because the unreported column identity and conditions prevent cross-comparison of er values with those that could be obtained in an independent laboratory using the same or a different chiral column.

---

**SRG-6 [Table 1 deprotection-time confounding]**

* **Primary RI**: RI-01 Reporting integrity
* **Secondary RI**: RI-08 Unquantified reliability
* **ER**: The ligand-ranking derived from Table 1 is only valid if the er values for each ligand reflect the enantioselectivity of the coupling step rather than a mixture of alcohol product 2 and sulfate half-ester 20 arising from incomplete (6 h) hydrolysis; reporting the SFC resolution of 2 from 20 and re-measuring the top-performing ligands (L4, L5, L6) under the optimized 24 h protocol is required to establish the reliability of the L5 selection.
* **EP**: EP-01a Reporting-coherence pack; EP-08a Replication / uncertainty pack
* **Case-specific implementation**: Re-run the coupling of 1 with PhMgBr using at minimum L5 and the next-best candidate L4 under the 24 h deprotection protocol; compare the er of the isolated alcohol product 2 under 6 h vs. 24 h protocols to determine whether the ranking is unchanged. Alternatively, confirm that SFC resolves 2 from 20 as separate baseline-resolved peaks, and report the er of each compound separately for a representative Table 1 entry.
* **Notes**: Members B-7. B-7 has convergence=2/3, temperature_gap=none (V1=medium, V3=medium). SRG-6 is the smallest SRG in terms of evidentiary burden: the confounding is acknowledged in the paper ([REDACTED: substantial verbatim quotation; see Tier 9]), making this a reporting omission rather than a concealed problem. However, the paper proceeds to select L5 as optimal on the basis of potentially confounded er data without confirming the ranking under the corrected protocol for any ligand other than L5. RI-08 is Secondary because the deprotection-protocol confounding introduces an unquantified error into the ligand-ranking data.

---

**SRG-7 [Mass balance and by-product identification]**

* **Primary RI**: RI-07 Unsupported boundary
* **Secondary RI**: RI-08 Unquantified reliability
* **ER**: The paper's design claim (b) — that electronic attenuation of the second C–O bond after first coupling minimizes bis-coupling — requires a mass-balance experiment under optimal conditions showing that the bis-coupling product is either absent or present in negligible yield (≤5%); this boundary claim ("minimizing competing bis(coupling) reaction") is stated as a design principle but is never tested against a failure example or quantified.
* **EP**: EP-07a Boundary-test pack; EP-08a Replication / uncertainty pack
* **Case-specific implementation**: (a) Run the coupling of 1 (1 equiv) with PhMgBr (3 equiv, to favor bis-coupling by excess Grignard) under the optimal Ni(acac)₂/(R,R)-L5 conditions and analyze the crude mixture by GC or ¹H NMR to identify and quantify the bis-coupled product (1-phenyl-3-phenyl-2-propanol derivative) alongside mono-coupled product 2, recovered starting material 1, and the MgBr₂-derived ring-opened by-product; (b) Report GC conversion (of starting sulfate 1) alongside isolated yield for at least three representative Table 2 entries to establish whether yield losses reflect chromatographic losses, incomplete conversion, or by-product formation.
* **Notes**: Members B-1, B-12. B-1 (absent GC conversion data; V1 only, medium severity) and B-12 (untested bis-coupling prediction; V1 only, medium severity) share the root that the fate of both substrates under optimal conditions is unaccounted from two complementary vantage points. RI-07 is Primary because the boundary claim ("minimizing bis-coupling") is made as a positive design principle without any failure examples, quantitative threshold, or negative control experiment demonstrating that bis-coupling does occur under modified conditions (e.g., excess Grignard or longer reaction time). The claim functions as an unsupported upper-bound assertion.

---

**Outside the SRGs: CLAs**

**CLA-1: Mechanistic basis for substrate failure (quaternary centers and tertiary alcohol derivatives)**

* **Primary RI**: RI-07 Unsupported boundary
* **ER**: The paper states that the current catalyst system is "ineffective[REDACTED: substantial verbatim quotation; see Tier 9]ineffective") is asserted without the data that would make the limitation interpretable as a design target.
* **EP**: EP-07a Boundary-test pack
* **Case-specific implementation**: Report at minimum a qualitative outcome for the two inset failure substrates (recovered starting material, decomposition, or <5% yield) and one candidate mechanism (steric inhibition of oxidative addition, catalyst deactivation, or background pathway competition) supported by a single discriminating experiment (e.g., rate of Ni(cod)₂ background coupling for the failure substrates vs. substrate 1).
* **Notes**: Grounded in A-1, B-3. Not captured in any SRG (A-1 ↔ B-3 is a linked pair, not a same-root group). This is a CLA because B-3's scope restriction statement directly bears on whether the D-1 claim holds as a general strategy: the paper's own framing ([REDACTED: substantial verbatim quotation; see Tier 9]) is not met by the demonstrated scope (tertiary hydrocarbon centers only), and the failure data for the claimed extension targets are entirely absent. The items grounded_in (A-1, B-3) are not members of any SRG. RI-07 applies in its "negative boundary claim" extended use: the claim that the current system is ineffective for quaternary centers is a strong boundary assertion made without supporting failure data.

**CLA-2: Self-contradictory absence — Grignard-only transmetalation assumed in the catalytic cycle but alternative species not excluded**

* **Primary RI**: RI-03 Unobserved explanatory
* **ER**: The proposed catalytic cycle (Scheme 4) specifies that [REDACTED: substantial verbatim quotation; see Tier 9] (i.e., ArMgBr), but the paper's own description of the aging protocol identifies Ar₂Mg as a likely constituent of the active Grignard solution; no experiment tests whether ArMgBr, Ar₂Mg, or a mixed magnesiate effects the transmetalation, making the mechanistic species in the cycle's closing step unobserved and the cycle internally inconsistent.
* **EP**: EP-03a Direct-observation / state-assignment pack
* **Case-specific implementation**: See SRG-4 implementation (a) and (b) above — the CLA-2 experiment requirement is a subset of the SRG-4 resolution experiments, specifically addressing the identity of the transmetalating species in the cycle closure step (E → C).
* **Notes**: Grounded in U-4, B-2. This satisfies the self-contradictory-absence CLA check: the paper proposes a catalytic cycle with an ArMgBr-mediated transmetalation step, but the paper's own mechanistic narrative acknowledges that the actual speciation of the aged Grignard solution is different from freshly prepared ArMgBr ("we suspect the aging process allows precipitation of MgBr₂"), which would shift the equilibrium toward Ar₂Mg. The catalytic cycle's closing step is therefore drawn with a reagent species whose identity is inconsistent with the paper's own account of the active Grignard solution. Not captured in SRG-2 (which addresses the absence of intermediate characterization broadly) or SRG-4 (which addresses Grignard speciation as a B/U gap); the CLA captures the internal logical inconsistency between the cycle drawing and the Grignard aging narrative.

---

### §3 Current VQ assessment

**Current judgment: VQ-2 (Method) — fails at VQ-2 boundary due to RI-07 (unsupported boundary for bis-coupling claim) and RI-01 (SFC documentation gap preventing cross-comparison); qualified at VQ-3 due to RI-05.**

---

**VQ-1 (Observation) — FAILS**

Required: RI-02 resolved (product identity / purity established at granularity excluding alternative candidates).

Grounds for failure: The enantioselectivity data (er for 17 Table 2 entries) — the paper's primary observational evidence — are generated by SFC analysis on an unspecified chiral stationary phase with no column identity, mobile phase, resolution factors, or pre/post-purification measurement protocol documented (U-3, SRG-5). For a communication whose central observation is the er values of products bearing asymmetric tertiary carbon centers, the failure to document the analytical instrument identity means that the products' enantiomeric compositions cannot be independently reproduced or verified. RI-02 ([REDACTED: substantial verbatim quotation; see Tier 9]) applies here in a specific sense: the enantiomeric compositions reported are not substantiated at the level of analytical documentation required to rule out the alternative interpretation that the SFC resolution was marginal or that enantiomers were incompletely resolved for some substrates. Additionally, the er values in Table 1 (ligand survey) were obtained under incomplete deprotection conditions (6 h protocol, B-7/SRG-6), meaning those data reflect a mixture of unknown composition (alcohol 2 + sulfate half-ester 20) rather than a single compound.

Non-fatal note: the structural identity of the coupling products (characterized by ¹H NMR, ¹³C NMR, IR, HRMS — deferred to SI) is not in dispute; the failure is on the enantiomeric purity/analytical validity dimension of RI-02, not on molecular identity.

---

**VQ-2 (Method) — FAILS (conditional on RI-02 non-fatal treatment)**

Inherits VQ-1 requirements. On the premise that the RI-02 failure is judged era-norm tolerated (see §4) and the product identities are accepted as established, VQ-2 is assessed.

Required: RI-01 and RI-07 resolved.

Grounds for failure:
- RI-01 (Reporting integrity): The SFC method documentation absence (U-3/SRG-5) prevents cross-comparison of er values across laboratories or with values obtained by alternative SFC methods. The background er (B-10/SRG-4) is absent, preventing quantitative assessment of the chiral catalyst's true selectivity separate from the background pathway's contribution. The Table 1 deprotection confounding (B-7/SRG-6) prevents reliable cross-comparison of ligand er values under a consistent protocol.
- RI-07 (Unsupported boundary): The bis-coupling attenuation claim (N-2 feature (b)) is a boundary assertion ("minimizing competing bis(coupling) reaction") without a supporting mass-balance experiment or failure example (SRG-7/CLA-1 for the quaternary-center limitation). The "ineffective" substrate claim (B-3) is a negative boundary assertion without data.

Non-fatal assessment: The RI-01 failures are individually consistent with the JACS Communication format constraints (see §4). The RI-07 failure for the bis-coupling claim is non-fatal in the sense that the observed yields (59–98%) are consistent with monocoupling being dominant, but the design principle is not tested. The RI-07 failure for the quaternary/tertiary failure substrates (CLA-1) is non-fatal for the paper's demonstrated scope but is fatal for any claim that the paper has characterized the method's boundaries.

---

**VQ-3 (Mechanism) — FAILS (inherits VQ-1 and VQ-2 failures)**

Required: RI-03, RI-04, RI-06 resolved.

Grounds for failure:
- RI-04 (Unreplicated discriminator): The radical clock (B-5/SRG-1) is a single data point ("only the usual Kumada coupling product 24 was detected") interpreted as evidence for a nonradical mechanism without detection-limit specification and without discriminating Ni(0)/Ni(II) from Ni(I)/Ni(III) where radical recombination from Ni(III) may exceed ring-opening. The ds measurement (B-6/SRG-1) is a single data point (90% ds) interpreted as supporting SN2-like oxidative addition stereoinversion under an explicitly stated but unverified assumption about reductive elimination stereochemistry.
- RI-03 (Unobserved explanatory): No named intermediate in the proposed catalytic cycle (C, D, E, TS) has been directly observed or kinetically constrained by stoichiometric experiments, kinetics, or spectroscopy (SRG-2). The axial reactive conformation A (SRG-3) is proposed as the stereocontrolling element but is neither observed crystallographically nor constrained computationally; conformational energy data from ref 21 (Lowe and Thatcher) is cited without reproducing the relevant values for the cyclic sulfate substrate class.
- RI-06 (Imported model): The Ni(0)/Ni(II) two-electron redox manifold is imported from the general Ni cross-coupling mechanistic literature (ref 11) without demonstrating its isomorphism for the PyBox-Ni/cyclic sulfate C–O electrophile system (SRG-2 secondary RI). The axial-attack SN2-like geometry is imported without DFT validation for the specific PyBox–Ni coordination geometry (SRG-3 secondary RI).

RI-05 note: The axial conformation argument (SRG-3) involves qualitative overread in a serious form (U-2: er-insensitivity is a non-unique interpretation of the proposed model). VQ-3, even if RI-03/04/06 were resolved, would remain "qualified" due to the unresolved RI-05 unless a positive discrimination experiment for the reactive conformation is performed.

---

**VQ-4 (Benchmark) — FAILS (inherits VQ-1 through VQ-3 failures)**

Required: RI-08 and RI-09 resolved.

Grounds for failure:
- RI-08 (Unquantified reliability): The enantioselectivity dataset (17 Table 2 entries) is reported as averages of two experiments without SD, range, or individual run data (B-8/SRG-5). Combined with the unspecified SFC method (U-3), neither the systematic nor the random component of the measurement uncertainty is documented. The gram-scale er erosion (92:8 vs. 96:4) lacks a quantitative uncertainty baseline for the analytical-scale reference value (B-14/B-8).
- RI-09 (External superiority): The paper's positioning claim (N-1) — a new strategy for enantioselective Kumada coupling with nonactivated alkyl electrophiles — is established by citation of prior methods (refs 3–9) without direct experimental comparison (er, yield, substrate scope overlap) with any cited method. No prior-method result is reproduced or directly benchmarked against the current system's results (C-1 through C-6). The Jarvo group's Ni-catalyzed C–O coupling papers (refs 9a–9d, the closest structural analog) receive the same cite-and-contrast treatment as more distant references.

**However, Layer 2 (synthetic result) on its own:** the demonstrated er values (up to 96:4 er, 84% yield for the optimal substrate pair) are internally consistent and mutually corroborating across 17 substrates. If the SFC method were documented (EP-08a + EP-01a resolution of SRG-5), Layer 2 would be able to reach VQ-4 as a stand-alone observational claim within the scope actually demonstrated (tertiary hydrocarbon centers from aryl Grignard reagents). The failure of VQ-4 for the paper as a whole is driven by RI-09 (no external benchmark) and RI-08 (no uncertainty documentation), not by intrinsic implausibility of the er values themselves.

---

### §4 Era-Norm Annotation

**communication-era tolerated:**

- **B-5 (radical clock detection limit absent):** In a 2016 JACS Communication, the convention for mechanistic probe experiments is to report the qualitative outcome (observed vs. not observed) without specifying GC detection limits for ring-opened products; detection-limit reporting is standard practice in dedicated mechanistic studies (full articles) but not in communications. The note "only the usual Kumada coupling product 24 was detected" follows the communication-era convention.

- **B-6 (ds measurement method absent; reductive elimination assumption unverified):** The convention for stereochemical probe experiments in 2016 JACS Communications is to report the ds value and state the assumption explicitly (as the paper does: "Assuming that..."), deferring independent validation of the reductive elimination stereochemistry to follow-up full papers. The explicit labeling of the assumption is present and distinguishes this from an unacknowledged limitation.

- **B-3, B-4 (failure substrate data qualitative only):** JACS Communications routinely report scope limitations qualitatively for failure cases, without numerical yield or er data for each failed substrate. The convention is to acknowledge the limitation and defer characterization of failure modes to the full paper. This is era-norm tolerated for the 4-page communication format.

- **B-8 (no SD/range for Table 2 averages):** Reporting the mean of duplicate experiments without SD is consistent with the 2016 JACS Communication convention for synthetic scope tables; footnoting "Results are an average of two experiments" is the standard reporting level at this format.

- **U-3 (SFC column identity absent in communication):** SFC column identity was routinely reported in the Supporting Information rather than in the communication text in 2016. The absence from the main text is communication-era tolerated; the SI lists "procedures, characterization, and spectral data" and would conventionally contain chiral stationary phase details.

- **D-4-5 (Table 1 6 h vs. 24 h deprotection; B-7):** The deprotection protocol discrepancy was discovered post-hoc and acknowledged in the communication, which is consistent with era norms for honest reporting of an experimental finding within a constrained format. Re-measuring all Table 1 ligands under the corrected 24 h protocol is a best practice but was not a 2016 era requirement in this context.

**modern-era deficient:**

- **U-3 (SFC column identity absent):** By contemporary standards (2024+), all primary enantioselectivity data must be accompanied by chiral stationary phase identity, mobile phase, and at minimum a representative chromatogram with resolution factors. Without this documentation, the data cannot be reproduced, which is now a mandatory reproducibility requirement in asymmetric catalysis publications. Modern-era deficient. Direct conflict with VQ upgrade requirements (RI-08, RI-01 resolution).

- **B-8 (no SD/range; duplicate mean without uncertainty):** Contemporary standards require that enantioselectivity data reported as averages include a standard deviation or range; reproducibility documentation at ≥ ±1 er unit resolution is expected. Modern-era deficient for the primary er dataset.

- **B-5 (radical clock without detection limit and Ni(I)/Ni(III) discrimination assessment):** Contemporary mechanistic studies distinguish Ni(0)/Ni(II) from Ni(I)/Ni(III) explicitly; the use of a cyclopropylcarbinyl clock alone, without EPR or a rate-matched clock, is now considered insufficient for mechanistic discrimination in Ni cross-coupling papers. Modern-era deficient.

- **B-6 (reductive elimination stereochemistry assumption unverified):** Contemporary expectations for stereochemical probe experiments in enantioselective Ni catalysis require that the stereochemical assumption (reductive elimination proceeds with retention) be independently established for the specific Ni/ligand system used. Modern-era deficient.

- **CLA-1 (failure substrate data entirely absent):** The contemporary expectation for scope characterization includes at minimum a qualitative result (e.g., "≤5% conversion") for representative failure cases shown in the communication's own scheme. The complete absence of data for the inset failure substrates in Scheme 2 is modern-era deficient.

*Dual classification (tolerated then, deficient now):*
- U-3 (SFC column identity): era-norm tolerated in the 2016 communication format (could be in SI); modern-era deficient if the SI does not contain the column identity and representative chromatograms. This dual classification depends on whether the SI fulfills the documentation obligation the communication defers to it. If the SI (not assessed in this certification) fully documents SFC methods, U-3 is resolved as era-norm tolerated; if SI is also silent, the item is modern-era deficient in both eras.

---

### §5 Shortest-reinforcement route

**Objective function 1: VQ-3 (Mechanism)**
Prerequisite: VQ-1 (RI-02) and VQ-2 (RI-01, RI-07) are addressed as part of the route below.

**Shortest route to VQ-3:**

1. **EP-08a (Replication / uncertainty pack) — SFC documentation + duplicate SD** — Report SFC column identity, mobile phase, and resolution factors for all Table 2 entries; confirm baseline resolution of the two lowest-er entries (products 5 and 6, 88:12 er) with representative chromatograms; report the range of the two individual er measurements for each Table 2 entry. This single EP simultaneously advances RI-08 (SRG-5 / VQ-4) and RI-01 (cross-comparison enabled; SRG-5 / VQ-2), and addresses the RI-02 analytical documentation gap in VQ-1. **Advances RI-08, RI-01, and clears the RI-02 documentation gap.** (Feasibility: very high — requires only SI documentation and is retroactively achievable if SFC records are available.)

2. **EP-04a (Discrimination / replication pack) — Rate-appropriate radical clock + TEMPO trap + detection limit** — Replace or supplement the cyclopropylcarbinyl clock experiment with (a) a TEMPO-trapping experiment reporting a GC detection limit for TEMPO-adduct formation, and (b) an EPR experiment at 10⁻⁴ M Ni under catalytic turnover conditions to assess whether Ni(I) or Ni(III) species accumulate. This addresses the mechanistic ambiguity of RI-04 (SRG-1) without requiring intermediate isolation. **Advances RI-04 (SRG-1).** (Feasibility: medium — EPR and TEMPO trapping are standard but require additional reaction design.)

3. **EP-03a (Direct-observation / state-assignment pack) — Reductive elimination stereochemistry verification** — Establish the reductive elimination stereochemistry of a PyBoxNi(II)(alkyl-d₁)(Ar) complex independently, using stoichiometric Ni and a well-defined isotopically labeled alkyl group; this validates or refutes the key assumption underlying the D-4-1 mechanistic assignment. **Advances RI-03 (SRG-1/SRG-2) and RI-04 (SRG-1).** (Feasibility: medium-high — stoichiometric Ni(II) alkyl-aryl complex synthesis is established for PyBox-Ni systems.)

4. **EP-03a (Direct-observation / state-assignment pack) — Transmetalating species identification** — Characterize the Grignard speciation before and after aging by ¹H or ²⁵Mg NMR; compare yield and er for independently prepared Ar₂Mg vs. ArMgBr under otherwise identical conditions. **Advances RI-03 (SRG-4) and RI-01 (CLA-2).** (Feasibility: medium — NMR speciation of Grignard reagents is established in the literature; Ar₂Mg can be prepared independently.)

5. **EP-07a (Boundary-test pack) — Mass balance and bis-coupling detection** — Run the coupling with excess PhMgBr (3 equiv) and analyze the crude mixture by GC to detect and quantify the bis-coupling product; report GC conversion alongside isolated yield for three representative Table 2 entries. **Advances RI-07 (SRG-7).** (Feasibility: very high — requires only crude GC analysis of existing reaction mixtures.)

6. **EP-06a (Analogy-validation pack) — Reactive conformation discrimination** — Prepare one conformationally biased cyclic sulfate (axial-locked or equatorial-locked C5 substituent) and measure the er; measure er at three temperatures for substrate 1 to establish Eyring parameters. **Advances RI-05 (SRG-3) toward VQ-3 "qualified" → VQ-3 (unqualified).** (Feasibility: medium — requires synthesis of conformationally biased substrates, ~2–3 months.)

**Certification-gate note:** The experimental investment order (EP-08a first for maximum information gain with minimum effort, then EP-04a and EP-03a for mechanism, then EP-07a for boundary, then EP-06a for quantitative stereocontrol model) follows information gain and feasibility; the final certification is fixed by the gate order VQ-1 → VQ-2 → VQ-3 → VQ-4, meaning RI-02 (product identity/purity documentation) must be cleared before RI-01 (method reporting integrity), which must be cleared before RI-03/RI-04/RI-06 (mechanism), which must be cleared before RI-08/RI-09 (benchmark).

---

**Objective function 2: VQ-4 (Benchmark)**
Prerequisite: VQ-3 achieved.

**Shortest route to VQ-4 (after VQ-3):**

1. **EP-08a (Replication / uncertainty pack) — replication across substrates** — Already initiated in route to VQ-3 (step 1); extend to report SD for yield across the 17 Table 2 entries and confirm that the gram-scale er erosion (92:8 vs. 96:4) falls outside the analytical-scale SD range. **Advances RI-08 (final resolution).** (Feasibility: very high — requires only SI data reporting.)

2. **EP-09a (Internal benchmark pack) — direct comparison with at least one Jarvo/Fu/Nakamura prior-method entry** — Select one representative substrate that is structurally accessible by both the current method and a prior enantioconvergent or enantiospecific Kumada coupling method (e.g., a secondary benzylic electrophile), and report the current method's er and yield for that substrate alongside a direct comparison with the literature er/yield. **Advances RI-09 (SRG-4/D-2 competitive positioning).** (Feasibility: medium — requires selection of a bridging substrate and one additional coupling experiment.)

**Certification-gate note:** VQ-4 certification follows the inheritance principle from VQ-1 through VQ-3.

---

### §6 Contribution to institutional design

**New representative case for RI-08 (Unquantified reliability) in the paired-absence variant:**
The molken2016 case introduces a specific variant of RI-08 that differs from the usual "single measurement, no replicate" pattern: the paper reports averages of two experiments (acknowledging replication was performed) but withholds the individual run values, range, or SD. This "acknowledged-replication-without-uncertainty-documentation" pattern is a distinct subtype of RI-08 not previously recorded in the Codebook. Proposed addition to RI-08 subtype notes: **[REDACTED: substantial verbatim quotation; see Tier 9]**

**RI-06 scope note — cycle-level and geometry-level import:**
The molken2016 case confirms the RI-06 scope note (cycle-level import) from the Codebook: the entire Ni(0)/Ni(II) two-electron catalytic cycle is imported from the general Ni cross-coupling mechanistic literature without demonstrating isomorphism for the PyBox-Ni/cyclic sulfate C–O system. A new sub-case is documented: the SN2-like attack geometry (in-line approach of a Ni(0) complex to a cyclic C–O bond) is imported from organic SN2 chemistry without DFT validation of whether the PyBox ligand's coordination geometry allows this approach angle. This "attack-geometry-level import" extends RI-06 beyond cycle-level and elementary-step-level analogies to the TS geometry level. Proposed addition to RI-06 scope note: **[REDACTED: substantial verbatim quotation; see Tier 9]**

**Labeling mismatch pattern:**
A labeling mismatch is present in the mechanistic section. The paper uses explicit hypothesis labeling in one location ([REDACTED: substantial verbatim quotation; see Tier 9]) but then proceeds immediately to state the conclusion in factual language: [REDACTED: substantial verbatim quotation; see Tier 9] — and in the Abstract: [REDACTED: substantial verbatim quotation; see Tier 9] The explicit assumption label is concentrated in Scheme 3 eq 8 text; by the time the abstract is written, the mechanistic claim is stated as a pointer from "experiments" without the assumption qualifier. This labeling mismatch co-occurs with RI-06 (imported SN2-like geometry) and RI-04 (single discriminating experiment), as expected per the Codebook pattern note.

**Incomplete negative evidence pattern:**
The radical clock experiment (B-5) is a case of the "incomplete negative evidence" pattern from §6 of the prompt: the qualitative non-observation of ring-opened product 25 ("only the usual Kumada coupling product 24 was detected") is used as positive mechanistic evidence for a nonradical mechanism without (a) reporting a detection limit for 25, (b) establishing the clock rate appropriate to the Ni(I)/Ni(III) reductive elimination timescale, or (c) performing a mass-balance closure for the 44% of starting material 23 that did not yield product 24. This is the standard "incomplete negative evidence" case-specific implementation of RI-04 in an asymmetric Ni cross-coupling system: the negative result (non-observation of radical ring-opening) is deployed as primary mechanistic evidence under conditions where the detection window and mass-balance are both unverified.

**RI co-occurrence pattern (SRG-1):**
SRG-1 exhibits a co-occurrence of RI-04 and RI-03 in which resolving only one is insufficient: even if RI-04 is resolved by a rate-appropriate clock or EPR experiment (establishing that the Ni(0)/Ni(II) manifold is operative), RI-03 remains because no named intermediate in the proposed catalytic cycle has been directly observed. Conversely, if an intermediate is observed (e.g., isolation of a stoichiometric PyboxNi(II)(alkyl)(aryl) complex — RI-03 resolution), this does not itself discriminate Ni(0)/Ni(II) from Ni(I)/Ni(III) for the catalytic turnover (RI-04 resolution requires kinetic discrimination, not just intermediate isolation). Both RI-04 and RI-03 must be resolved for VQ-3 to be reached. This co-occurrence structure adds a case-specific example to the Codebook's RI co-occurrence pattern section.

**PRI-10 and PRI-11 relevance:**
PRI-10 (Kinetic overclaim) is not triggered: the paper makes no absolute rate enhancement claims.
PRI-11 (Mechanism–kinetics decoupling) is partially relevant: the paper proposes a catalytic cycle (Scheme 4) but does not derive an algebraic rate law from it; however, the paper does not claim a specific rate order or rate enhancement, so PRI-11 applies in its weaker "mechanism supported without algebraic rate law derivation" form rather than the "rate order matched without derivation" form. The molken2016 case supports the PRI-11 provisional code as the mechanism is supported only by two qualitative probe experiments (agreement with observed nonradical and stereoinvertive behavior), without an algebraic derivation of the rate law from the proposed cycle. This provides a third independent paper supporting PRI-11 promotion beyond Breitenfeld 2014 and Pengfei 2024.

**New EP dictionary case-specific implementation additions:**
- EP-03a in a Ni(PyBox)/cyclic sulfate system: direct-observation is achievable by stoichiometric synthesis of PyboxNi(0)(cyclooctadiene) or PyboxNi(II)(phenyl)(alkyl) complexes and characterization by XRD + CV + EPR.
- EP-04a in a Ni radical-clock context: discrimination of Ni(0)/Ni(II) from Ni(I)/Ni(III) requires either a rate-matched clock at the Ni(III)→Ni(I) reductive elimination timescale or EPR at turnover conditions; the cyclopropylcarbinyl clock alone is insufficient for this discrimination, establishing a protocol standard for future Ni mechanistic assessment sheets.

---

> **Tier 8 redaction notice**: This file is a redacted copy of the corresponding Tier 3 / Tier 9 output. Verbatim source-paper quotations have been replaced by `[REDACTED: see source paper §<loc>; full text retained in Tier 9 reviewer-only deposit]` markers, preserving location references and our own analytical content. Bibliographic fields (title, authors, journal, year, DOI), analytical labels (`evidence_chain:` with B-/U-/A-/C- internal IDs), short technical terms, and our own analytical text are not redacted. The redaction was applied by `scripts/redact_for_tier8.py` and, for this version, by `scripts/build_paperA_R1_public.py` with `scripts/redact_source_ngram_runs.py` (scripts of the project repository; they are not deposited).
