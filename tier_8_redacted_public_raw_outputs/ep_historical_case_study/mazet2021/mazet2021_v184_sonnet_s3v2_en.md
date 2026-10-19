```
prompt_version: stage3-v2-en-20260419
model_info: claude-sonnet-4-6
```

# Re-certification Assessment Sheet for Scientific Knowledge

## Poisson, Tran, Besnard, and Mazet 2021 (ACS Catalysis, full_paper)

---

### §1 Claim Architecture

**Core claim summary:**

The paper's central claim is that two structurally related bisphosphine–Ni(II) precatalysts, [(dppe)NiBr₂] (4c) and [(dmpe)NiBr₂] (4d), which are both competent catalysts for the Ni-catalyzed Kumada vinylation of enol phosphates, operate via *distinct* Ni(0)/Ni(II) reaction mechanisms despite sharing the same set of elementary steps. The **Novelty pillar** rests on two sub-claims: (i) for the dppe system, a phosphate-to-bromide ion exchange preceding transmetalation is identified as "a process barely documented in the current literature"; and (ii) for the dmpe system, the [REDACTED: verbatim source quotation; see the source paper via its DOI]

**Layered structure judgment:**

The claims are hierarchically layered, and a single refutation does not collapse all claims simultaneously. Three independent layers are identifiable:

- **Layer A (Ni(0)/Ni(II) manifold assignment):** Argued independently by radical-clock, TEMPO trapping, and paramagnetic NMR monitoring for both systems. This layer is logically separable from Layers B and C.
- **Layer B (dppe mechanism — ion exchange):** Argued by NMR monitoring and X-ray crystallographic characterization of 9c, independently of kinetics. Refuting the kinetic orders does not undermine the ion-exchange finding, which is structurally established.
- **Layer C (dmpe mechanism — bimetallic transmetalation):** The most novel and most exposed layer. It depends on the VTNA kinetic orders (SRG-1) and the stoichiometric proof-of-concept (SRG-2). If the VTNA orders are invalidated (Candidate 2), or if the stoichiometric evidence is quantitatively insufficient (Candidate 3), Layer C is undermined while Layers A and B remain intact.

Inter-layer dependencies: Layer C presupposes Layer A (the bimetallic TM proposal is only meaningful if Ni(0)/Ni(II) is established). Layer B is fully independent of Layer C. The comparative claim — that dppe and dmpe operate via *distinct* mechanisms — requires both Layer B and Layer C, meaning that if Layer C collapses to "consistent with but unconfirmed," the comparative novelty is substantially weakened. **The paper's structure is resilient at Layers A and B but fragile at Layer C, which is where its primary novelty resides.**

---

### §2 SRG / CLA → RI / ER / EP Crosswalk

---

**SRG-1 [Kinetic foundation under deactivation]**

*Member items: A-3, A-4, A-5, B-5, B-7, U-1, U-2*

* **Primary RI**: RI-04 [Unreplicated discriminator]
* **Secondary RI**: RI-01 [Reporting integrity]; RI-08 [Unquantified reliability]
* **ER**: The kinetic rate orders that support the proposed rate-determining steps (transmetalation for dppe; bimetallic Ni–Ni transmetalation for dmpe) must be derived from VTNA experiments satisfying the method's precondition of approximately constant catalyst concentration, and must be accompanied by goodness-of-fit statistics sufficient to distinguish the assigned order from alternative functional forms. Furthermore, the Grignard reagent order must be unambiguously determined or its indeterminacy must be shown not to confound the other derived orders.
* **EP**: EP-04a [Discrimination / replication pack]; EP-01a [Reporting-coherence pack]; EP-08a [Replication / uncertainty pack]
* **Case-specific implementation**: (a) Repeat VTNA kinetic experiments for both the [(dppe)NiBr₂] and [(dmpe)NiBr₂] systems using catalyst loadings that span a wider range (e.g., 5 distinct loadings spanning one order of magnitude) with explicit catalyst deactivation profiling by UV-Vis or in situ IR to obtain corrected concentration profiles; include goodness-of-fit statistics (residuals, R², or Bayesian model comparison) for second-order vs. 1.5-order vs. composite-order fits for the dmpe data. (b) Characterize the Schlenk equilibrium speciation of vinyl magnesium bromide 2a in THF at −40°C by ²⁵Mg NMR or conductimetry to determine the kinetically active Grignard species and re-measure the Grignard order using the corrected speciation. (c) Construct and numerically integrate the differential rate equation system for the proposed dmpe cycle (including I-a, III-b, IV, and a deactivation term) and confirm that the model reproduces the observed VTNA overlays at all three catalyst loadings.
* **Notes**: SRG-1 is the largest same-root group (7 items) and governs the evidentiary weight of *both* mechanistic proposals, not only the dmpe system. Position in TEMPERATURE_SUMMARY: A-3 and B-5 are high_convergence_low_gap (3/3 convergence); A-4/U-2 and B-7 are high_convergence_low_gap (2/3 and 3/3 respectively). U-1 is low_convergence_high_gap (critical severity). The compound nature of the kinetic failure — deactivation distorts orders, Grignard speciation is undefined, and no numerical integration is provided — means that resolving only one of these three sub-problems is insufficient; all three must be addressed for the kinetic evidence to carry mechanistic weight.

---

**SRG-2 [Bimetallic transmetalation — three-level evidentiary gap]**

*Member items: A-3, B-6, C-3*

* **Primary RI**: RI-03 [Unobserved explanatory]
* **Secondary RI**: RI-04 [Unreplicated discriminator]
* **ER**: The bimetallic Ni–Ni transmetalation intermediate (I-a + III-b → IV), which is the central novel mechanistic species for the dmpe system, must either be directly observed spectroscopically under stoichiometric or catalytic conditions, or its existence must be demonstrated by a stoichiometric experiment in which the expected product distribution (including mass-balance closure) is quantitatively consistent with the proposed mechanism.
* **EP**: EP-03a [Direct-observation / state-assignment pack]; EP-04a [Discrimination / replication pack]
* **Case-specific implementation**: (a) DFT calculation (M06L/def2-TZVP or comparable) of the bimetallic transmetalation transition state (I-a + III-b → IV) to obtain the activation barrier and confirm it is consistent with the apparent second-order kinetics at −40°C; compare against the conventional Ni–Mg transmetalation barrier in the same system. (b) Redesign the stoichiometric proof-of-concept (Figure 9): use separately pre-formed and isolated I-a and III-b (or their synthetic equivalents) at defined ratios, derive the expected cross-product yield distribution from the proposed statistical transmetalation model using measured OA rates of 6d toward 1a and 8a as inputs, and verify that observed yields of 3aa (7–17%) and diene 14 (8%) are within the predicted range, with full mass-balance accounting for the remaining ~75–85% of material.
* **Notes**: SRG-2 provides three independent levels at which the bimetallic TM claim lacks quantitative support: no computed barrier (A-3 — RI-03 subtype: unobserved explanatory), low stoichiometric yields with unaccounted mass balance (B-6 — RI-04), and a dropped quantitative benchmark from the RE barrier reference that licenses rapid product release (C-3 — RI-06 scope note). Position in TEMPERATURE_SUMMARY: A-3 (3/3 convergence, high_convergence_low_gap); B-6 (2/3, high_convergence_low_gap); C-3 is a CLA-level dropped benchmark not in TEMPERATURE_SUMMARY.

---

**SRG-3 [dmpe system undercharacterization — asymmetric evidentiary depth]**

*Member items: A-2, A-7, A-8, B-8*

* **Primary RI**: RI-02 [Object identification]
* **Secondary RI**: RI-08 [Unquantified reliability]
* **ER**: For the comparative mechanistic claim to be evaluated symmetrically, the dmpe system must reach the same characterization depth as the dppe system at each mechanistic node: quantifiable Ni(0) activation intermediate (6d), isolable OA complex (9d) with full mass-balance, observable product-bound complex (11d), and mechanistic rationalization of dmpe-specific anomalies with Grignard reagents 2b and 2c.
* **EP**: EP-02a [Identity / purity substantiation pack]; EP-08a [Replication / uncertainty pack]
* **Case-specific implementation**: (a) Optimize the preparation of 6d to achieve quantifiable NMR yields (e.g., by use of THF-d₈ with added 1,5-COD or low-temperature quench) and propagate the uncertainty in [6d] into the kinetic analyses. (b) Optimize the isolation of OA complex 9d from enol phosphate 1a to achieve >40% yield (currently 16%) by adjusting temperature, concentration, or reaction time; account for the mass-balance gap (remaining ~84%). (c) Apply the "different protocol" (currently in Supporting Information only) for estimating 11d conversion to the main-text mechanistic narrative, with numerical yield and uncertainty. (d) Rationalize the complete failure of 2b (cyclopropylmagnesium bromide) and the alkenyl isomerization with 2c within the proposed Figure 8B dmpe cycle, identifying the mechanistic step at which these anomalies arise.
* **Notes**: The asymmetry between dppe (fully characterized: 7c X-ray, 9c X-ray, 11c NMR 70%) and dmpe (6d not quantifiable, 9d 16% NMR yield, 11d not observable) is the structural condition that allows the bimetallic TM proposal to be presented at the same narrative level as the well-established dppe mechanism. Position in TEMPERATURE_SUMMARY: B-8 and A-8 are low_convergence_high_gap (1/3 convergence, high severity). A-2 is high_convergence_low_gap (2/3).

---

**SRG-4 [E/Z selectivity reversal — unanalyzed mechanistic constraint]**

*Member items: A-6, U-4*

* **Primary RI**: RI-05 [Qualitative overread]
* **Secondary RI**: RI-03 [Unobserved explanatory] (subtype: available-but-unutilized characterization)
* **ER**: The temperature-dependent reversal of E/Z selectivity for product 3ce in the dmpe system (E/Z = 40:60 at 23°C → 04:96 at −40°C) is a quantitative observation within the paper's own dataset that is directly relevant to the proposed dmpe catalytic cycle; the paper must either identify the E/Z-determining elementary step within the cycle and provide a qualitative physical-organic rationalization, or explicitly acknowledge that this selectivity pattern is outside the scope of the current mechanistic model.
* **EP**: EP-05a [Quantitative-ranking substantiation pack]; EP-03a [Direct-observation / state-assignment pack]
* **Case-specific implementation**: Perform an Eyring analysis of the E/Z ratio for 3ce as a function of temperature (minimum 4 temperatures between −40°C and 23°C) using the dmpe precatalyst 4b; extract ΔΔH‡ and ΔΔS‡ for the competing E/Z-selective pathways. The sign change in E/Z preference between −40°C and 23°C implies that ΔΔH‡ and ΔΔS‡ have opposite signs — an entropy-controlled selectivity reversal that would constrain the geometry of the rate-determining transition state (specifically whether the bimetallic transmetalation TS I-a + III-b → IV is geometrically selective for E or Z).
* **Notes**: This SRG is notable because the observation (E/Z reversal) is *within the paper's own dataset* and is the only substrate-level probe of the dmpe mechanism's stereochemical predictions. The paper introduces it in the Introduction as motivating the mechanistic study (alongside 2b failure and 2c isomerization) but never returns to it in the Results section. Footnote 21 offers a single qualitative sentence ("longer-lived alkenyl–nickel intermediates when 4b is employed") without quantitative grounding. Position in TEMPERATURE_SUMMARY: A-6/U-4 are high_convergence_low_gap (convergence 3/3 counting OV entries from V2 and V3). RI-05 applies because selectivity implications are derived from a qualitative attribution (longer-lived intermediates) without numerical support.

---

**SRG-5 [Ni(I) exclusion — NMR-only detection with insufficient sensitivity]**

*Member items: B-10, U-5, C-1*

* **Primary RI**: RI-04 [Unreplicated discriminator]
* **Secondary RI**: RI-02 [Object identification]
* **ER**: Exclusion of Ni(I) intermediates — on which the Ni(0)/Ni(II) mechanistic assignment centrally depends — requires either EPR spectroscopy at μM sensitivity or a quantitative statement of the NMR detection limit for paramagnetic Ni(I) species under the conditions used, such that the upper bound on any Ni(I) concentration is demonstrably below mechanistic relevance.
* **EP**: EP-04a [Discrimination / replication pack]; EP-02a [Identity / purity substantiation pack]
* **Case-specific implementation**: Monitor the NMR activation experiments (treating 4c or 4d with 2a in THF at −40°C) in parallel by X-band EPR at 77 K or at the reaction temperature; integrate the EPR signal (if present) against a Ni(I) standard (e.g., [Ni(dppe)Cl]·spin standard) to derive an upper bound on [Ni(I)] relative to total [Ni]. Alternatively, report the NMR concentration threshold below which Ni(I) would not produce observable line-broadening under the conditions of Figure 2A, and confirm that this threshold is below mechanistically relevant concentrations. Apply the EPR methodology established in the cited references (C-1: Park, Hazari, Bajo) to the dppe/dmpe enol phosphate systems.
* **Notes**: The NMR-based exclusion and the fluxional assignment for 6c at 298 K rely on the same spectroscopic method under conditions (298 K, where comproportionation rates are highest) where their discrimination is hardest. This circularity is the structural weakness of SRG-5. Position in TEMPERATURE_SUMMARY: B-10 is high_convergence_low_gap (2/3); U-5 is medium severity. The cited Ni(I) EPR references (C-1: refs 3a, 3b, 3c) are not engaged for their EPR methodology.

---

**Outside the SRGs: CLAs**

---

**CLA-1: Radical-clock experiment — ring-opening rate constant absent**

*Grounded in: U-3, A-1, B-9*

* **Primary RI**: RI-04 [Unreplicated discriminator]
* **ER**: A radical-clock experiment is only as strong as the clock's rate constant is documented; the non-detection of ring-opening products 12/13 from cyclopropylmethyl-containing substrate 1g must be combined with the ring-opening rate constant of the specific clock moiety in 1g to derive an upper bound on the radical lifetime, and this upper bound must be shown to exclude the fastest known Ni(I)/Ni(III) radical-rebound pathways.
* **EP**: EP-04a [Discrimination / replication pack]
* **Case-specific implementation**: Report the ring-opening rate constant of the cyclopropylmethyl unit in substrate 1g (by literature reference or independent calibration), calculate the maximum radical concentration consistent with the non-detection of 12/13 at the reported GC/NMR detection limit, and compare this upper bound against published rate constants for Ni(I)/Ni(III) radical rebound in bisphosphine–Ni systems. If the TEMPO experiment (Figure 6B) is to be retained as corroborating evidence, repeat it at standard catalytic conditions (1–5 mol% catalyst, −40°C) with a non-coordinating radical trap or with explicit control for TEMPO-ligation (footnote 16 already flags this concern).
* **Notes**: This CLA is not captured in existing SRGs. Its member items (A-1 ↔ B-9: sequential radical-exclusion experiments with linked limitations; A-1 ↔ U-3: clock experiment generates the prerequisite-absence) show that both approaches to radical exclusion contain unquantified assumptions. The TEMPO experiment's non-standard conditions (50 mol% catalyst, 0°C vs. standard 1–10 mol%, −40°C to 23°C) and the acknowledged TEMPO-ligation caveat mean neither experiment individually constitutes a firm exclusion. CLA-1 bears directly on Layer A of the claim architecture (Ni(0)/Ni(II) manifold assignment), making it more consequential than its non-SRG status suggests.

---

**CLA-2: Steric origin of OA selectivity — unquantified steric/electronic attribution**

*Grounded in: B-3, B-4*

* **Primary RI**: RI-05 [Qualitative overread]
* **Secondary RI**: RI-06 [Imported model] (scope note: %VBur from non-catalytic cod intermediate imported to characterize OA transition state)
* **ER**: The attribution of differential OA reactivity (0% conversion for [(dppe)Ni(0)] toward adamantyl enol phosphate 1d vs. ~50% for the corresponding vinyl bromide 8d) to steric factors requires either (a) computation of %VBur or %VS for the OA transition state or for the characterized OA complex 9c (not the cod complex 7c), or (b) a Hammett-type correlation using substituted enol phosphates and vinyl bromides to quantify the electronic C–O vs. C–Br bond contribution.
* **EP**: EP-05a [Quantitative-ranking substantiation pack]; EP-06a [Analogy-validation pack]
* **Case-specific implementation**: Using the X-ray structure of OA complex 9c (already available), compute the topographic steric map and %VBur for the dppe ligand in the OA complex geometry rather than in the cod complex (7c). Compute the corresponding value for a model OA complex with dmpe. The difference in %VBur between the OA geometries (not the cod geometries) is the operationally relevant steric descriptor for the OA step.
* **Notes**: The %VBur values for 7c (48.9%) and 7d (43.1%) are measured in cod complexes where cod occupies two coordination sites absent from the catalytic cycle. The 5.8 percentage-point difference in the cod complexes may not reflect the difference at the OA step. This CLA is methodologically independent from SRG-1 and SRG-2 and bears on the mechanistic interpretation of the dppe vs. dmpe OA reactivity difference, which is cited as structural motivation for the mechanistic divergence.

---

### §3 Current VQ assessment

**Current judgment: VQ-2 (Method) — qualified at VQ-3**

---

**VQ-1 [Observation] — Pass (with non-fatal qualification)**

RI-02 (Object identification): The dppe system intermediates are characterized at a level that establishes their structural identity: 7c and 9c are X-ray characterized, 11c is observed by NMR in 70% yield with consistent spectroscopic signatures, and the precatalyst 4c is commercially sourced and independently verified. The dmpe system intermediates (6d, 9d, 11d) are identified by NMR symmetry arguments and consistency with the proposed structures, which is non-fatal given that X-ray characterization of 7d is available and 9d's NMR parameters are consistent with the dppe analogue. However, the 16% NMR yield of 9d from enol phosphate 1a (vs. 73% for 9c) and the unquantifiable 6d constitute non-fatal RI-02 issues that weaken the evidentiary basis for the dmpe system's object identification at catalytic intermediate nodes. **VQ-1 holds with the non-fatal qualification that dmpe intermediate identification is partially inferred rather than directly established.**

---

**VQ-2 [Method] — Pass (on the premise that the non-fatal RI-02 issues at VQ-1 are accepted)**

RI-01 (Reporting integrity): The paper reports consistent measurement frames across the two catalyst systems — identical substrates (1a, 2a), solvent (THF-d₈), temperature (−40°C for stoichiometric NMR, 23°C for kinetics), and analytical method (in situ IR + NMR). The primary cross-comparison between dppe and dmpe systems is internally consistent in measurement frame. Non-fatal RI-01 issues arise from the asymmetric characterization depth (6d not quantifiable, B-3 steric maps from cod complexes) but do not render cross-comparison impossible. RI-07 (Unsupported boundary): The paper does not make explicit "only X is possible" boundary claims for the Ni(0)/Ni(II) manifold beyond what is supported by the radical-clock and TEMPO results; the radical exclusion is presented as supporting rather than proving, and the Ni(I) exclusion is bounded by the acknowledged NMR detection limit. **VQ-2 holds on the premise that RI-02 at VQ-1 is non-fatal, and given that RI-01 and RI-07 issues are non-fatal at the measurement-frame and boundary-claim levels.** Note that CLA-2 (steric attribution — RI-05) introduces a qualified element but does not invalidate the method-level reporting.

---

**VQ-3 [Mechanism] — Fails (Layer C); qualified for Layer B**

RI-03 (Unobserved explanatory) is fatal for VQ-3 at the whole-paper level: the bimetallic transmetalation intermediate (I-a + III-b → IV), which is the paper's most novel mechanistic species and the central explanatory object for the dmpe system's apparent second-order kinetics, is neither directly observed nor kinetically constrained at a level that would allow it to function as the paper's claimed rate-determining step. The SRG-2 three-level gap (no computed barrier, no mass-balance-complete stoichiometric test, and a dropped quantitative benchmark for RE) collectively makes the RI-03 lethality judgment: **Fatal for Layer C (dmpe bimetallic TM claim).**

RI-04 (Unreplicated discriminator) is fatal for VQ-3 at the kinetic-evidence level: the three-point VTNA dataset for the second-order catalyst assignment under acknowledged deactivation (SRG-1, B-5) is a single discriminator without statistical support adequate to distinguish second-order from alternative functional forms, and without numerical integration of the proposed kinetic model (U-1, critical severity). **Fatal for Layer C.**

RI-06 (Imported model): The rapid reductive elimination barrier (licensed from ref 15, C-3) is imported from a different Ni system without demonstrating isomorphism to the dppe/dmpe enol phosphate system at −40°C. **Non-fatal for Layer B; fatal for Layer C's mass-balance prediction.**

**However, Layer B (dppe mechanism — ion exchange) on its own:** The phosphate-to-bromide ion exchange conclusion (III-a → III-b) is supported by NMR monitoring of the dppe system (Figure 4A, excellent mass balance between consumption of 1a and formation of 9c), by X-ray crystallographic characterization of 9c, and by the kinetically consistent picture that III-b (not III-a) undergoes transmetalation. RI-03 does not apply to the ion-exchange step because the OA complex 9c is directly observed. RI-04 for the dppe system is non-fatal: the VTNA apparent first-order catalyst dependence is distorted by deactivation, but the paper's central claim for the dppe system is not the order in catalyst but the identity of the rate-determining step (transmetalation of III-b) and the ion-exchange pathway, both of which are supported by the stoichiometric NMR evidence independently of the kinetics. **Layer B on its own reaches VQ-3 (qualified) — with the qualification that RI-08 (unquantified reliability) at the kinetic level makes the VQ-3 judgment for the dppe system "qualified" rather than "pass."**

---

**VQ-4 [Benchmark] — Fails**

RI-08 (Unquantified reliability): The VTNA kinetic orders for both systems lack replicate measurements or uncertainty descriptions. The three-point datasets for the dmpe second-order assignment contain no goodness-of-fit statistics. The stoichiometric proof-of-concept (Figure 9) has no mass-balance accounting for ~75–85% of material. **Fatal for both systems.** RI-09 (External superiority): The paper does not assert superiority over external benchmarks in a way that would engage RI-09 specifically. VQ-4 fails on RI-08 grounds.

---

### §4 Era-Norm Annotation

**communication-era tolerated:**

- **B-5 (three-point VTNA dataset without goodness-of-fit statistics):** ACS Catalysis in 2021 routinely published VTNA-based kinetic assignments from visual overlay of 3–5 experiments without requiring formal statistical model-comparison; the visual overlap method as codified in ref 18 (Burés 2016) was accepted practice for the journal and period. The paper's three-point dataset is at the lower bound of community norm but within range.

- **B-6 (stoichiometric experiment with unaccounted mass balance):** Proof-of-concept stoichiometric experiments with low yields for cross-products are standard in mechanistic communication papers for Ni catalysis in this era; the expectation of mass-balance closure in exploratory stoichiometric experiments was not uniformly enforced by ACS Catalysis reviewers at this time, particularly for bimetallic experiments where multiple side-reaction pathways are expected.

- **B-8 (16% NMR yield of 9d with no mass-balance discussion):** In full papers reporting comparative organometallic mechanistic studies, asymmetric characterization depth between catalyst systems was tolerated when the less-characterized system's key structural parameters (coordination geometry, NMR shifts) were consistent with analogy to the better-characterized system. The paper's NMR symmetry argument for 9d is consistent with this norm.

- **B-10 (NMR-only Ni(I) exclusion):** In 2021, EPR monitoring was not yet standard practice in experimental mechanistic Ni-catalysis papers in ACS Catalysis; NMR-based Ni(I) exclusion via absence of paramagnetic broadening was accepted without EPR corroboration. The referenced Ni(I) EPR studies (C-1: Park, Hazari) were specialist characterization work, not routine inclusion in synthetic-mechanistic papers.

**modern-era deficient:**

- **U-1 (no numerical integration of the bimetallic kinetic model):** By 2024–2025 community standards for mechanistic proposals invoking unusual rate-determining steps, a numerically integrated kinetic model reproducing the observed VTNA overlays at all catalyst loadings is expected as supporting information when the proposed mechanism predicts a non-trivial apparent rate order. The absence of this integration is a modern-era deficiency.

- **U-2 (VTNA applied under acknowledged catalyst deactivation):** The 2022 update to VTNA methodology (Nielsen/Burés 2019 Visual Kinetic Analysis) made explicit that deactivation profiles must be measured and corrected before VTNA orders can be interpreted mechanistically. Applying VTNA under acknowledged deactivation without correction is deficient by current standards.

- **B-7 (undefined Grignard order in both systems):** Modern mechanistic papers in organometallic catalysis are expected to characterize Grignard speciation or to acknowledge the Schlenk equilibrium as an explicit confound in the kinetic analysis; "tentative" attribution to aggregation without speciation measurement is not acceptable in a paper whose central claims rest on kinetic orders.

- **U-3 (radical-clock without ring-opening rate constant):** The 2020–2025 literature on Ni(I)/Ni(III) radical mechanisms has established that radical-clock experiments require reporting the ring-opening rate constant and deriving an upper bound on radical concentration; the current paper's binary non-detection statement is deficient by this standard.

- **B-3 (steric maps from cod complexes used to characterize OA reactivity):** The SambVca 2.0 tool explicitly supports %VBur calculation from any input structure; using cod complexes rather than the available X-ray structure of OA complex 9c for the steric attribution is a design choice that is deficient by current standards where the catalytically relevant geometry should be used.

---

### §5 Shortest-reinforcement route

**Objective function 1: Reach VQ-3 (pass, unqualified) for the paper as a whole**

Current status: VQ-2 pass; VQ-3 fails on RI-03 (Layer C: unobserved explanatory — bimetallic TM) and RI-04 (Layers B/C: kinetic discriminator quality). Layer B already reaches VQ-3 qualified. The principal investment required is for Layer C.

**Shortest route to VQ-3:**

1. **EP-03a [Direct-observation / state-assignment pack]** — DFT calculation of the bimetallic transmetalation transition state (I-a + III-b → IV) at a level consistent with the Ni(0)/Ni(II) OA barriers already documented in related systems (e.g., M06L/def2-TZVP with THF PCM); confirm that the computed barrier is thermally accessible at −40°C and lower than the conventional Ni–Mg transmetalation barrier.
   Advances RI-03 (SRG-2): directly addresses the unobserved explanatory object at the bimetallic TM step.

2. **EP-04a [Discrimination / replication pack]** — Redesign the stoichiometric proof-of-concept (Figure 9) with separately pre-formed I-a and III-b equivalents, derive the expected cross-product yield distribution from measured OA rates, and close the mass balance to >90%; this converts the "notion-supporting" experiment into a mechanism-testing experiment.
   Advances RI-03 (SRG-2, B-6) and RI-04 (SRG-2): addresses both unobserved explanatory and unreplicated discriminator for the central novel claim.

3. **EP-04a [Discrimination / replication pack]** — Repeat the VTNA analysis for the dmpe system with 5 catalyst loadings, explicit deactivation correction via catalyst activity profiling, and goodness-of-fit statistics comparing order-2 vs. order-1.5 vs. composite-order models; also implement the numerically integrated kinetic model (addresses U-1).
   Advances RI-04 (SRG-1, B-5) and RI-01 (SRG-1, A-4): resolves the statistical and methodological insufficiency of the three-point kinetic dataset.

4. **EP-05a [Quantitative-ranking substantiation pack]** — Perform Eyring analysis of E/Z ratio for 3ce (4 temperature points, dmpe system) to determine whether entropy- or enthalpy-controlled selectivity governs the reversal.
   Advances RI-05 (SRG-4): converts the unanalyzed selectivity observation into a quantitative mechanistic constraint on the bimetallic TM step's geometry.

*Investments 1–2 are highest priority because they address the RI-03 fatal gap at Layer C. Investment 3 addresses RI-04. Investment 4 is an additional discriminant that would strengthen the mechanistic picture without being prerequisite for VQ-3 passage.*

*Certification-gate note: Investments are ordered by information gain toward VQ-3, but the final VQ certification follows the fixed inheritance order VQ-1 → VQ-2 → VQ-3 → VQ-4; confirmation at each gate is required before the higher level is assessed.*

---

**Objective function 2: Reach VQ-4 (Benchmark), contingent on VQ-3 pass**

**Shortest route to VQ-4:**

1. **EP-08a [Replication / uncertainty pack]** — Add independent replicate VTNA experiments for both dppe and dmpe systems (minimum n = 3 per catalyst loading, minimum 5 loadings) with propagated uncertainty in rate orders; report standard deviations on all derived kinetic parameters.
   Advances RI-08 (SRG-1, B-5).

2. **EP-09a [Internal benchmark pack]** — Direct comparison of the bimetallic transmetalation rate (from integrated kinetic model) against the conventional Ni–Mg transmetalation rate in the same dmpe system under identical conditions, to establish the quantitative advantage (or absence thereof) of the bimetallic pathway.
   Advances RI-09 (not currently coded as RI-09 since no external superiority claim is made, but internal benchmark comparison is the natural analogue for the comparative mechanistic claim).

*Certification-gate note: VQ-4 requires VQ-3 to hold. The experimental investment order above follows information gain, but the final certification is fixed by the gate order VQ-1 → VQ-2 → VQ-3 → VQ-4.*

---

### §6 Contribution to institutional design

**1. Confirmed representative case for RI-04 (Unreplicated discriminator) — kinetic manifestation**

This paper provides a new implementation pattern for RI-04: a VTNA order assignment from a three-point dataset under acknowledged catalyst deactivation. Prior RI-04 applications in the UQS corpus focused on single data points with high discriminatory power (e.g., one key experiment interpreted at a high level without replication). This paper extends RI-04 to the kinetics domain: a statistically insufficient experimental design (three data points, no goodness-of-fit statistics) with strong mechanistic implications. The case-specific implementation for RI-04 in a kinetics context is: [REDACTED: substantial verbatim quotation; see Tier 9]

**2. Confirmed representative case for RI-03 subtype — Available-but-unutilized characterization at the computational level**

The paper's X-ray structure of OA complex 9c is available but not used to compute the topographic steric map at the OA-relevant geometry (CLA-2, B-3). This extends the "available-but-unutilized characterization" subtype (defined in v0.2a as [REDACTED: substantial verbatim quotation; see Tier 9]) to the *computational post-processing* of crystallographic data: the structural data are acquired and characterized, but the downstream steric computation that would validate the mechanistic attribution uses a non-catalytic proxy (cod complex) instead.

**3. Confirmed co-occurrence pattern: RI-03 + RI-04 in SRG-2**

SRG-2 (bimetallic TM claim) shows a co-occurrence of RI-03 (bimetallic intermediate unobserved) and RI-04 (stoichiometric proof-of-concept with insufficient evidentiary power). Resolving only RI-03 via DFT computation would not be sufficient to establish the claim at VQ-3: the stoichiometric experiment (Figure 9) must also be redesigned to provide a mass-balance-complete discrimination test (RI-04). This co-occurrence is structurally similar to the RI-04 + RI-06 co-occurrence noted in the v0.2a prompt, and constitutes an additional co-occurrence pattern to register: **RI-03 (unobserved explanatory) + RI-04 (unreplicated discriminator)** frequently co-occur when a novel mechanistic intermediate is invoked to explain kinetic data from a single experiment.

**4. Labeling mismatch pattern — detected**

The paper uses "we propose" and "must be analyzed cautiously" (in the bimetallic TM section) but then uses factual verbs in the Conclusions: "transmetalation is likely to occur between vinyl nickel intermediates" and [REDACTED: substantial verbatim quotation; see Tier 9] The hypothesis label ("we propose[REDACTED: substantial verbatim quotation; see Tier 9]proposal" framing without resolving the underlying evidentiary gaps. This is a textbook labeling mismatch: hypothesis vocabulary in the Results, near-factual vocabulary in the Conclusions, co-occurring with RI-03 (as predicted by the v0.2a prompt).

**5. PRI-11 relevance — potential connection to Mechanism–kinetics decoupling**

PRI-11 (Mechanism–kinetics decoupling, promoted via Breitenfeld 2014 and Pengfei 2024) has direct relevance here: the proposed dmpe catalytic cycle (Figure 8B) is not used to derive a rate law algebraically; the apparent second-order catalyst dependence is supported only by agreement with the observed VTNA overlay. The proposed mechanism predicts rate ∝ [I-a][III-b], but [I-a] and [III-b] as functions of total [Ni] are not derived from the proposed cycle. This is an exact match to the PRI-11 definition: [REDACTED: substantial verbatim quotation; see Tier 9] **This paper independently confirms PRI-11 and constitutes a second cross-coupling case (after Breitenfeld 2014 and Pengfei 2024) supporting the promoted definition.** If PRI-11 promotion had not already been confirmed, this case would qualify as the necessary second confirmation.

**6. Incomplete negative evidence pattern — detected (CLA-1)**

The radical-clock experiment (Figure 6A) and TEMPO trapping experiment (Figure 6B) together constitute the Incomplete negative evidence pattern defined in the v0.2a prompt: negative experimental results (non-detection of ring-opening products 12/13; unsuccessful TEMPO trapping) are used as positive mechanistic evidence (Ni(0)/Ni(II) assignment, exclusion of radical pathways) without quantification of the detection sensitivity (ring-opening rate constant absent; TEMPO-ligation confound acknowledged but unresolved). This is a case-specific implementation of RI-04 where the "unreplicated discriminator" is a negative result used as binary evidence without specifying the detection threshold.

**7. New EP dictionary insight — EP-04a implementation for bimetallic stoichiometric experiments**

The Figure 9 experiment (stoichiometric proof-of-concept for Ni–Ni transmetalation) represents a new EP-04a implementation context: a *predictive stoichiometric test* for a bimetallic mechanistic step, where the discriminating power of the experiment depends on deriving the expected product distribution from the proposed mechanism and comparing it against observation. The current EP-04a description ("case-specific implementation: discrimination experiments with replication") does not explicitly cover the case where the predicted yield must first be calculated from the proposed mechanism before discrimination can be assessed. The addition of [REDACTED: substantial verbatim quotation; see Tier 9] would add value to the EP dictionary.

---

> **Tier 8 redaction notice**: This file is a redacted copy of the corresponding Tier 3 / Tier 9 output. Verbatim source-paper quotations have been replaced by `[REDACTED: see source paper §<loc>; full text retained in Tier 9 reviewer-only deposit]` markers, preserving location references and our own analytical content. Bibliographic fields (title, authors, journal, year, DOI), analytical labels (`evidence_chain:` with B-/U-/A-/C- internal IDs), short technical terms, and our own analytical text are not redacted. The redaction was applied by `scripts/redact_for_tier8.py` and, for this version, by `scripts/build_paperA_R1_public.py` with `scripts/redact_source_ngram_runs.py` (scripts of the project repository; they are not deposited).
