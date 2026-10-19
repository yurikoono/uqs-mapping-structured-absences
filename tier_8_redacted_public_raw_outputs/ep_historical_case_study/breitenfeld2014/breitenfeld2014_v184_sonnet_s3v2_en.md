```
prompt_version: stage3-v2-en-20260419
model_info: claude-sonnet-4-6
```

# Re-certification Assessment Sheet for Scientific Knowledge

## Breitenfeld, Wodrich, and Hu 2014 (Organometallics, full_paper)

---

### §1 Claim Architecture

**Core claim summary:**

The paper's core claim is that the nickel pincer complex Nickamine catalyzes alkyl−aryl Kumada coupling via a bimetallic oxidative addition mechanism, and that within this mechanism the turnover-determining step (TDS) is not oxidative addition but transmetalation — specifically a bimetallic "redistributive" transmetalation of two Ni(II) adduct molecules. The Novelty pillar rests on two independent demonstrations: (a) radical-clock experiments with substrate 7 (6-bromo-1-hexene + PhMgCl) establish that the linear:cyclized product ratio is first-order in catalyst, thereby excluding cage-rebound and mandating either escape-rebound or bimetallic OA; DFT free-energy profiles then discriminate in favor of bimetallic OA by a claimed 18.7 kcal/mol margin. (b) Kinetic measurements establish rate orders of approximately 2 in catalyst, 2 in Grignard reagent, and 0 in alkyl iodide, which the paper assigns to a redistributive transmetalation step by analogy with Yamamoto's Ni(0)/biaryl system. The Utility pillar is the unification of alkyl−aryl and alkyl−alkyl Nickamine-catalyzed coupling under a single mechanistic framework, with the implicit suggestion that the framework extends to all four Nickamine reaction types listed in the Introduction.

**Layered structure judgment:**

The paper's claims are organized in three structurally independent layers: (Layer 1) cage-rebound excluded by radical-clock first-order dependence on catalyst; (Layer 2) bimetallic OA preferred over escape-rebound by DFT energetics; (Layer 3) transmetalation is TDS, not oxidative addition, by kinetics. The three layers use non-overlapping evidence streams: radical-clock ratios, DFT barriers, and rate-order log-log plots, respectively. Refuting Layer 2 (DFT energetics) does not collapse Layer 1 (radical-clock exclusion of cage-rebound) or Layer 3 (kinetic TDS assignment). However, cross-layer dependencies exist: (a) Layer 3 relies on Layer 1's radical-clock framework to confirm that oxidative addition proceeds via radicals at all; (b) Layer 2's escape-rebound exclusion reinforces Layer 3 by making bimetallic OA the only plausible radical pathway. A single refutation of Layer 1 (radical-clock quantitative incompleteness) would not collapse Layers 2 or 3, but would weaken the paper's overall mechanistic narrative. The weakest inter-layer link is that neither Layer 2 nor Layer 3 directly validates the comproportionation step that closes the catalytic cycle (Figure 8), making Layer 3's proposed catalytic cycle formally open at the Ni(I)/Ni(III) bimetallic transmetalation closure point.

---

### §2 SRG / CLA → RI / ER / EP Crosswalk

**SRG-1 [radical clock quantitative incompleteness]**

* **Primary RI**: RI-08 [Unquantified reliability]
* **Secondary RI**: RI-01 [Reporting integrity]
* **ER**: For the first-order catalyst dependence of the linear:cyclized ratio to serve as mechanistic evidence, the paper must report (i) the standard deviation or confidence interval on each ratio, (ii) total GC yields and conversions at each loading (from the C₁₂H₂₆-internal-standard GC-MS procedure described in the Experimental Section), and (iii) the specific catalyst loadings explored with substrate 2 + PhMgCl rather than the qualitative "various loadings." Without these data, the precision of the order determination and the mass-balance validity of the ratio analysis are unestablished.
* **EP**: EP-08a [Replication / uncertainty pack]; EP-01a [Reporting-coherence pack]
* **Case-specific implementation**: Report the standard deviation of the linear (8):cyclized (9) ratio across the three independent trials at each of the five catalyst loadings (2, 4, 7, 10, 15 mol%). Report GC yields and conversions for 8 and 9 at each loading using the C₁₂H₂₆ internal standard already in the described procedure. Disclose the catalyst concentrations (mol%) used in the substrate 2 + PhMgCl control experiment (Scheme 3). A systematic variation in total conversion with catalyst loading (e.g., 30% at 3 mol% vs. 90% at 15 mol%) would confound the ratio analysis and require a correction or acknowledgment.
* **Notes**: Member items B-1, B-2, B-7. Position in TEMPERATURE_SUMMARY: high_convergence_low_gap (V1-Q1 + V2-OV4, convergence 2/3, temperature_gap low). The data quality gap is non-fatal to Layer 1's cage-rebound exclusion if conversions are uniform across loadings — which is plausible given that the reaction is run at ≤10% yield for kinetics, but this is not stated for the radical-clock experiments.

---

**SRG-2 [DFT barrier quantitative reliability — composite protocol uncertainties]**

* **Primary RI**: RI-04 [Unreplicated discriminator]
* **Secondary RI**: RI-06 [Imported model]; RI-08 [Unquantified reliability]
* **ER**: For the claimed 18.7 kcal/mol selectivity of bimetallic OA over escape-rebound to be operationally reliable, the paper must provide: (i) benchmarking of the PBE0-dDsC/TZ2P//M06/def2-SVP protocol against a higher-level method (DLPNO-CCSD(T) or CASPT2) for at least one Ni(III) d7 organometallic stationary point; (ii) a quasi-RRHO or related entropy correction for the B1 + Pr• → B2 bimetallic association step to quantify the known RRHO overestimation; (iii) a PES scan extended beyond 4.0 Å or a MD-based free energy estimate for the Pr• dissociation energy acknowledged as imprecise by the paper's own text. Without these three elements, the 18.7 kcal/mol figure carries unquantified systematic uncertainty that the paper itself acknowledges is non-trivial for the B2 reference point.
* **EP**: EP-04a [Discrimination / replication pack]; EP-06a [Analogy-validation pack]; EP-08a [Replication / uncertainty pack]
* **Case-specific implementation**: For the Nickamine system, the critical benchmarking target is the reductive-elimination TS (TSB2,B3, 3.4 kcal/mol above B2) and the escape-rebound TS (TSE1,E2, 22.1 kcal/mol above E1). A DLPNO-CCSD(T)/cc-pVTZ single-point on the M06/def2-SVP geometries for these two transition states, compared to the PBE0-dDsC/TZ2P values, would establish whether the 18.7 kcal/mol margin is robust to ±1 kcal/mol or ±5 kcal/mol functional error. Applying Grimme's quasi-RRHO entropy correction (Chem. Eur. J. 2012, ref 31 in that body of literature) to the B1 + Pr• → B2 step would replace the RRHO-overestimated entropic penalty with a physically motivated value, directly testing whether the B2 formation free energy of −0.4 kcal/mol is stable to the correction or reverses sign.
* **Notes**: Member items U-1, U-5, B-5. Position in TEMPERATURE_SUMMARY: low_convergence_high_gap for U-1 (critical severity at Turn 4 synthesis level, compound of V1-Q4 + V3-Q2 + V3-Q5). The paper's own text explicitly acknowledges that B2 energetics "is best accomplished through molecular dynamics simulations," making the unquantified uncertainty partially self-acknowledged. The RI-06 secondary applies because PBE0-dDsC was developed and validated primarily for closed-shell main-group systems and is imported to open-shell Ni(III) d7 without demonstrated isomorphism.

---

**SRG-3 [open-shell singlet / spin state treatment]**

* **Primary RI**: RI-03 [Unobserved explanatory]
* **Secondary RI**: RI-08 [Unquantified reliability]
* **ER**: For the 22.1 kcal/mol escape-rebound barrier (TSE1,E2, described as an open-shell singlet) to be accepted as the discriminating energy value, the paper must report: (i) the ⟨S²⟩ value for TSE1,E2 to establish the degree of spin contamination; (ii) whether Yamaguchi/Noodleman spin correction was applied and, if so, the corrected energy; (iii) the triplet-surface energy at the TSE1,E2 geometry. Additionally, the Ni(III) spin-density assignment of E1 (reported via Supporting Information Figure S10) must be confirmed with a basis-set-independent population method (NPA or Hirshfeld) at the TZ2P level, not only at the M06/def2-SVP geometry-optimization level.
* **EP**: EP-03a [Direct-observation / state-assignment pack]; EP-08a [Replication / uncertainty pack]
* **Case-specific implementation**: For the Nickamine Ni(III) system, BS-DFT at the M06/def2-SVP level of TSE1,E2 should report the ⟨S²⟩ of the broken-symmetry wavefunction before and after spin-correction. If J (the exchange coupling constant between the unpaired electron on Ni and the alkyl radical) falls in the 1–5 kcal/mol range typical for organometallic Ni(III)-radical systems, the spin-corrected TSE1,E2 barrier could be 17–21 kcal/mol rather than 22.1 kcal/mol, measurably reducing the discrimination margin. The spin-density assignment of E1 should be reproduced with NBO/NPA analysis at the TZ2P basis to confirm that the majority spin density remains on Ni rather than migrating to the pincer nitrogen or bromide.
* **Notes**: Member item U-3. High-convergence at V1-Q5 + V3-OV3 (convergence 2/3, temperature_gap none). The RI-03 primary applies because the spin-corrected energy of TSE1,E2 is an explanatory state central to the pathway discrimination but is neither directly reported nor kinetically constrained: it is computed using an uncorrected BS-DFT procedure without disclosure of spin-contamination metrics that are standard output of the calculation.

---

**SRG-4 [kinetic pre-equilibrium validity / rate-law derivation]**

* **Primary RI**: PRI-11 [Mechanism–kinetics decoupling]
* **Secondary RI**: RI-03 [Unobserved explanatory]
* **ER**: For the proposed eq-3 redistributive transmetalation mechanism (two molecules of [(MeN2N)Ni-X](ArMgCl) (12) undergoing redistribution as TDS) to be consistent with the observed rate orders (≈2 in catalyst, ≈2 in Grignard, ≈0 in alkyl iodide), the paper must present an algebraic derivation of the rate law from the proposed catalytic cycle (Figure 8) under explicitly stated limiting assumptions (e.g., pre-equilibrium approximation for 11 + ArMgCl ⇌ 12, with 12 in low steady-state concentration). The derivation must show that the integer orders 2, 2, 0 emerge from the mechanism under independently justifiable conditions. The paper must also provide direct or indirect evidence for intermediate 12 ([(MeN2N)Ni-X](ArMgCl)) as a distinct species, beyond the analogy to the alkyl Grignard case (ref 20).
* **EP**: EP-03a [Direct-observation / state-assignment pack]; EP-04a [Discrimination / replication pack]
* **Case-specific implementation**: For the Nickamine alkyl−aryl system, the algebraic rate-law derivation from eq 3 via pre-equilibrium in [11] and [12] gives: rate = k_TDS × K_eq² × [11]² × [ArMgCl]². This predicts second order in both catalyst-equivalent [11] and Grignard [ArMgCl], consistent with the observed orders, provided [11] ≈ [catalyst]_total and the 10 ⇌ 13 equilibrium does not introduce additional ArMgCl dependence. The paper should show this derivation explicitly and specify which equilibria are assumed fast. For intermediate 12, a low-temperature NMR experiment in which [(MeN2N)Ni-X] is mixed with PhMgCl at −40 °C in THF-d₈ would directly probe the formation of the adduct species; its absence from the paper constitutes RI-03 for the open-shell singlet subtype "available-but-unutilized characterization" (if the experiment is feasible) or "prerequisite-absence" (if it has not been attempted).
* **Notes**: Member items B-3, U-4. Position in TEMPERATURE_SUMMARY: high_convergence — V1-Q9 + V2-OV3, convergence 2/3, temperature_gap none. PRI-11 promotion status: proposed in this paper, isomorphic pattern confirmed in Pengfei 2024 per prompt codebook v0.2a; two-paper independent confirmation is satisfied. This SRG provides direct evidence for PRI-11 promotion (see §6).

---

**SRG-5 [temperature change and mechanistic scope]**

* **Primary RI**: RI-07 [Unsupported boundary]
* **Secondary RI**: RI-01 [Reporting integrity]
* **ER**: The claim that the mechanistic assignments (TDS = transmetalation, second order in catalyst, second order in Grignard, zeroth order in alkyl iodide) characterize the synthetically relevant reaction requires either (i) activation parameters (ΔH‡, ΔS‡) measured at two or more temperatures, enabling extrapolation to room temperature, or (ii) an explicit acknowledgment that the kinetic characterization is restricted to 0 °C and may not apply to the room-temperature preparative conditions. The paper presents the 0 °C kinetic results as the mechanism of the catalytic reaction without qualification, constituting an unsupported boundary claim that "the rate-determining step is transmetalation" without failure examples at alternative temperatures.
* **EP**: EP-07a [Boundary-test pack]; EP-01a [Reporting-coherence pack]
* **Case-specific implementation**: For the Nickamine system, measuring initial rates at 0 °C and −20 °C (accessible with the ice/water and dry ice/acetone baths already available in the described setup) would provide the minimum two-temperature data needed for an Eyring analysis. If ΔH‡ and ΔS‡ for the TDS are obtained, the rate at room temperature (25 °C) can be calculated and the question of whether the TDS assignment changes with temperature can be addressed. Alternatively, the paper should explicitly state: [REDACTED: substantial verbatim quotation; see Tier 9]
* **Notes**: Member items A-2, B-4. Position in TEMPERATURE_SUMMARY: high_convergence — V1-Q6 + V2-OV2, convergence 2/3, temperature_gap none. The RI-07 primary applies because "the mechanism of the alkyl−aryl coupling" is stated as a general conclusion without restriction to the 0 °C measurement window; no failure examples at other temperatures are shown.

---

**SRG-6 [kinetic non-integer orders mechanistic significance]**

* **Primary RI**: RI-05 [Qualitative overread]
* **Secondary RI**: RI-08 [Unquantified reliability]
* **ER**: The non-integer catalyst order (1.7, Figure 5B) and the mildly negative alkyl iodide order (−0.3, Figure 7B) carry mechanistic information that the paper suppresses by reporting them as "about second order" and "zeroth order," respectively. For the kinetic characterization to support the TDS assignment, the paper must discuss whether the 1.7 catalyst order is consistent with second-order kinetics within the experimental uncertainty (two independent trials per data point) or indicates a mechanistically distinct situation (partial catalyst dimerization, non-integer stoichiometry in the TDS, or parallel pathways). The −0.3 alkyl iodide order must similarly be addressed: genuine zeroth order, mild product inhibition, ion-pairing effects, or substrate inhibition of an auxiliary equilibrium each have different mechanistic implications.
* **EP**: EP-05a [Quantitative-ranking substantiation pack]; EP-08a [Replication / uncertainty pack]
* **Case-specific implementation**: For the Nickamine system, confidence intervals on the log-log slopes require more than two independent trials per data point. At minimum, three independent trials with consistent Grignard addition rate would reduce the uncertainty on the catalyst-order slope from "range of individual runs" (as shown in Figure 5B error bars) to a true standard deviation from which a statistical test of integer vs. non-integer order can be performed. A mechanistic discussion should address whether 1.7 vs. 2.0 catalyst order is distinguishable given the experimental uncertainty, and should propose a mechanism fragment that would predict 1.7 if the two-run uncertainty range does encompass 2.0.
* **Notes**: Member item B-4 (consolidated SRG). Position in TEMPERATURE_SUMMARY: high_convergence — V1-Q7 + V2-OV1, convergence 3/3, temperature_gap none. RI-05 primary applies because structural (mechanistic) implications are derived from the kinetic order values without numerical support for the rounding from 1.7 → 2 and −0.3 → 0. Non-fatal to Layer 3's TDS assignment if the true orders are statistically indistinguishable from integers, but this indistinguishability is asserted rather than demonstrated.

---

**SRG-7 [comproportionation and bimetallic transmetalation evidence]**

* **Primary RI**: RI-03 [Unobserved explanatory]
* **Secondary RI**: RI-06 [Imported model]
* **ER**: The proposed catalytic cycle (Figure 8) includes the comproportionation step Ni(I) 16 + Ni(III) 14 → Ni(II) 11 + Ni(II) 13 as a mechanistically necessary turnover step. For this step to be accepted as part of the proposed cycle, the paper must provide at least: (i) computation of the free-energy profile for the comproportionation (16 + 14 → 11 + 13) in the alkyl−aryl system (analogous to the DFT profiles shown for oxidative addition and escape-rebound), or (ii) a kinetic or spectroscopic observation demonstrating that Ni(I) 16 is consumed at a rate commensurate with catalytic turnover rather than decomposing. The observed "quick" catalyst decomposition upon fast Grignard addition at room temperature is consistent with Ni(I) 16 accumulation and failure of comproportionation but is treated in the paper as a purely practical problem (solved by cooling to 0 °C) rather than as a mechanistic observable.
* **EP**: EP-03a [Direct-observation / state-assignment pack]; EP-06a [Analogy-validation pack]
* **Case-specific implementation**: For the Nickamine alkyl−aryl system, the simplest test of comproportionation kinetic competence is a stoichiometric reaction: independently generate [(MeN2N)Ni]-type Ni(I) species (by the reduction of Ni(II) complex 11 with 0.5 equiv Mg or Zn in THF) and mix with an authentic sample of a Ni(III) species (e.g., generated by oxidation of complex 13 with PhICl₂) at 0 °C, monitoring by UV-Vis or EPR for Ni(II) product formation. If the comproportionation proceeds cleanly on the timescale of catalysis (seconds), the mechanistic assumption is validated. Alternatively, DFT calculations of the comproportionation free-energy profile in the alkyl−aryl system would establish whether it is thermodynamically and kinetically feasible, complementing the DFT profiles already shown for oxidative addition and escape-rebound.
* **Notes**: Member items A-1, U-2. Position in TEMPERATURE_SUMMARY: high_convergence_low_gap — V1-Q12 + V2-Q4, convergence 2/3, temperature_gap low. RI-06 secondary applies because the comproportionation step is imported from the alkyl−alkyl predecessor (ref 20) without demonstrated isomorphism in the alkyl−aryl system, which differs in the nature of the Ni(II) aryl species and its reactivity toward Grignard reagents.

---

**SRG-8 [DFT model truncation — propyl vs. hex-5-en-1-yl]**

* **Primary RI**: RI-01 [Reporting integrity]
* **Secondary RI**: RI-04 [Unreplicated discriminator]
* **ER**: The DFT calculations use a propyl radical (CH₃CH₂CH₂•) as a truncated model for the experimentally deployed hex-5-en-1-yl radical. For the computed barriers (3.4 kcal/mol reductive elimination, 22.1 kcal/mol escape-rebound, 27 kcal/mol Pr• dissociation) to be applicable to the experimental system, the paper must provide a truncation-error validation: at minimum, a single-point energy calculation at the TZ2P level on the M06/def2-SVP geometries for the key stationary points (B2, TSB2,B3, E1, TSE1,E2) using the actual hex-5-en-1-yl or a close structural analogue (e.g., pent-4-en-1-yl), establishing that the truncation introduces less than ±1 kcal/mol error in the discriminating barriers.
* **EP**: EP-01a [Reporting-coherence pack]; EP-04a [Discrimination / replication pack]
* **Case-specific implementation**: For the Nickamine system, the hex-5-en-1-yl radical differs from propyl in: (i) chain length affecting steric interactions with the pincer ligand at the bimetallic encounter complex B2; (ii) a terminal alkene that could weakly coordinate to Ni(II) at the B2 geometry; (iii) a longer carbon framework affecting the radical-dissociation scan asymptote. A single-point energy comparison at the TSB2,B3 geometry using propyl vs. hex-5-en-1-yl (or a 3-butenyl surrogate) would bound the truncation error. The Supporting Information already contains the xyz coordinates file (from "Associated Content"), making this a low-cost post-hoc validation.
* **Notes**: Member items B-5 consolidated (V1-Q10, V3-Q9). Position in TEMPERATURE_SUMMARY: convergence 2/3, temperature_gap low. Non-fatal if the truncation error is small (expected for a chain-end truncation in a reaction dominated by the Ni center geometry), but unverified.

---

**Outside the SRGs: CLAs**

**CLA-1: Scope of the unifying mechanism claim (alkyl−alkynyl Kumada and alkyl−aryl Suzuki)**

* **Primary RI**: RI-07 [Unsupported boundary]
* **ER**: The Conclusion claims [REDACTED: substantial verbatim quotation; see Tier 9] covering four reaction types listed in the Introduction (alkyl−alkyl Kumada, alkyl−aryl Kumada, alkyl−alkynyl Kumada, alkyl−aryl Suzuki). Mechanistic data are presented only for alkyl−alkyl (ref 20) and alkyl−aryl (this paper) Kumada coupling. The boundary claim that the unification extends to alkyl−alkynyl Kumada and alkyl−aryl Suzuki coupling is asserted without failure examples or mechanistic data for those two reaction types.
* **EP**: EP-07a [Boundary-test pack]
* **Case-specific implementation**: For the Nickamine scope claim, the paper should either restrict the "unifying" conclusion explicitly to "alkyl−alkyl and alkyl−aryl Kumada couplings" or provide a prospective acknowledgment that "whether the bimetallic OA and redistributive transmetalation framework extends to alkyl−alkynyl Kumada and alkyl−aryl Suzuki couplings remains to be established." Radical-clock experiments with the alkyl−alkynyl coupling (e.g., 6-bromo-1-hexene + PhC≡C−MgCl) would be the minimal experiment needed to extend the radical-clock first-order argument.
* **Notes**: Grounded in A-4, C-5. Not captured in any SRG (A-4 is an A-item with no SRG assignment). This CLA satisfies the CLA eligibility criteria: it directly bears on the D-1 Novelty claim #4 (unifying mechanism), and the B/A items grounded in it (A-4 and C-5) are not members of any SRG.

---

**Self-contradictory-absence CLA check:**

Two self-contradictory absences already captured in SRGs: (i) Rate-law non-derivation captured in SRG-4 (PRI-11); (ii) Comproportionation prediction without evidence captured in SRG-7.

Additional self-contradictory absence: The paper's GC-MS analytical procedure with C₁₂H₂₆ internal standard (Experimental Section) generates both ratio data and yield/conversion data — but only the ratio is reported. This is captured in SRG-1 (B-7).

No additional CLAs from the self-contradictory-absence check beyond CLA-1.

---

### §3 Current VQ assessment

**Current judgment: VQ-2 (Method) — qualified**

**VQ-1 [Observation] — Pass**

VQ-1 requires resolution of RI-02 (product/catalyst structure and purity not established at a granularity that excludes alternative candidates). The paper identifies the linear (8) and cyclized (9) coupling products by GC-MS, NMR, and comparison with literature, and demonstrates the Nickamine catalyst is well-defined and characterized (refs 12–17, with resting-state identification of [(MeN2N)Ni-Ph] in ref 15). The key organometallic intermediates (11, 13) are characterized by independent synthesis (refs 13–15). RI-02 is non-fatal: product identity is adequately established for a 2014 Organometallics article, and catalyst identity is supported by an extensive prior characterization record. VQ-1 holds on the premise that the RI-02 qualification on the homogeneous-catalyst assignment under 0 °C kinetic conditions (B-6) is non-fatal.

**VQ-2 [Method] — Qualified**

VQ-2 (inheriting VQ-1) additionally requires resolution of RI-01 (inconsistent measurement frames) and RI-07 (unsupported boundary). SRG-1 carries RI-08 as primary (unquantified reliability in radical-clock statistics) with RI-01 secondary — the absence of GC yields and conversion data from the same procedure that generates them (B-7) constitutes an RI-01 sub-case that is internally inconsistent: the measurement frame (GC-MS with C₁₂H₂₆ standard) produces two quantities but only one (ratio) is reported. SRG-5 carries RI-07 (unsupported boundary): the claim that the kinetic characterization at 0 °C reflects "the mechanism of the alkyl−aryl coupling" without restriction to the measurement temperature. SRG-8 carries RI-01 (propyl truncation without cross-frame validation). CLA-1 carries RI-07 (unifying claim without boundary test for alkyl−alkynyl and Suzuki).

The RI-01 instances in SRG-1 and SRG-8 are non-fatal individually (the radical-clock conclusion would likely survive conversion-uniform conditions, and propyl truncation error is expected to be small), but they are unverified. The RI-07 instances in SRG-5 and CLA-1 are serious: the 0 °C restriction affects the paper's central claim about "the mechanism of the alkyl−aryl coupling" (not just the kinetics at one temperature), and the four-reaction-type unifying claim is directly falsified if any of the other two reaction types do not follow the bimetallic OA framework.

**VQ-2 is qualified** (rather than fail) because the most serious RI-07 instance (SRG-5) reflects a measurement-condition limitation rather than a logical impossibility: the paper could in principle be correct that the same mechanism operates at room temperature, but has not established this. The RI-05 instance in SRG-6 (non-integer orders reported as integers without uncertainty analysis) further qualifies VQ-2 by introducing doubt about whether the kinetic evidence uniquely supports the proposed TDS. Combined, these render the kinetic stream's evidence as "consistent with but not uniquely establishing" the proposed mechanism.

**VQ-3 [Mechanism] — Fail**

VQ-3 (inheriting VQ-2) requires resolution of RI-03, RI-04, and RI-06. Three SRGs individually fail VQ-3:

- SRG-2 carries RI-04 (primary): the 18.7 kcal/mol pathway-selectivity figure is a single DFT result with no uncertainty quantification, no benchmarking against higher-level methods, no quasi-RRHO correction for the bimetallic association entropy — and the paper itself acknowledges the B2 reference point cannot be rigorously computed with static DFT. An unreplicated discriminator (RI-04 primary) that is acknowledged as imprecise in the paper's own text is fatal to the DFT mechanistic claim at VQ-3.
- SRG-3 carries RI-03 (primary): the spin-corrected energy of TSE1,E2 is neither observed nor kinetically constrained; the ⟨S²⟩ and spin-correction status are unreported. For an open-shell singlet TS, the uncorrected BS-DFT energy is not a reliable representation of the true singlet energy.
- SRG-4 carries PRI-11 (primary, promoted per v0.2a): the proposed catalytic cycle predicts a specific algebraic rate law but the paper does not derive it, making the consistency between the mechanism and the observed kinetics unverifiable — a mechanism–kinetics decoupling pattern.
- SRG-7 carries RI-03 (primary) and RI-06 (secondary): the comproportionation step (Ni(I) + Ni(III) → 2 Ni(II)) is a species central to the catalytic cycle but is neither directly observed nor kinetically constrained for the alkyl−aryl system; it is imported from ref 20 (alkyl−alkyl) without demonstrating isomorphism.

VQ-3 fails. The paper establishes a mechanistic framework that is consistent with available evidence but does not achieve the evidentiary threshold at which the specific mechanistic assignments (bimetallic OA preferred over escape-rebound by 18.7 kcal/mol; redistributive transmetalation as TDS) can be accepted as demonstrated rather than proposed.

**However, Layer 1 (cage-rebound exclusion) on its own:** The first-order catalyst-dependence of the linear:cyclized ratio is a relatively robust experimental conclusion (assuming uniform conversions across loadings, which is plausible at ≤10% yield). This sub-claim — that cage-rebound is excluded — reaches a higher VQ level than the paper as a whole. Specifically, if SRG-1's RI-08 instance is non-fatal (uniform conversions), Layer 1 holds at VQ-2 without the SRG-3/SRG-4 failures that affect the DFT and kinetic streams.

**VQ-4 [Benchmark] — Fail (by inheritance)**

VQ-4 additionally requires RI-08 (replicate measurements / uncertainty) and RI-09 (direct comparison for superiority claims). VQ-4 cannot be reached while VQ-3 fails. Additionally, SRG-1 carries RI-08 (non-fatal but unresolved), and SRG-6 carries RI-08 secondary (two independent trials per kinetic data point, insufficient for confidence intervals on log-log slopes). RI-09 is not a primary issue (the paper does not assert catalyst superiority over direct experimental comparators).

---

### §4 Era-Norm Annotation

**communication-era tolerated:**

- **B-3 (absence of algebraic rate-law derivation):** In 2014, Organometallics full papers in the mechanistic organometallic chemistry space routinely accepted "the kinetics can be explained by mechanism X" conditional assertions without algebraic derivation; the journal's 8-page format and editorial standards of the era did not require explicit pre-equilibrium derivations as a condition of publication. The Yamamoto analogy (refs 47–48) for second-order-in-catalyst behavior was accepted as sufficient kinetic precedent.

- **U-3 (absence of ⟨S²⟩ and spin-correction reporting for TSE1,E2):** The standard of reporting BS-DFT results in organometallic communication-era papers (2010–2014) did not uniformly require spin-contamination metrics in the main text; placement in Supporting Information was accepted. The ADF software's spin-density outputs (Figure S10 cited in the paper) demonstrate that spin analysis was performed; the absence of ⟨S²⟩ in the main text reflects the era's Supporting Information–first convention rather than suppression.

- **B-7 (absence of total GC yields/conversions from radical-clock experiments):** The radical-probe methodology in organometallic chemistry (Bergman 1978 precedent, refs 28–29) was established using ratio analyses without requiring parallel quantitative yield reporting; the convention of reporting linear:cyclized ratios without conversion data was accepted as the primary datum in 2014.

- **B-4 (two independent trials per kinetic data point):** The initial-rate method with two independent trials was an accepted practice for kinetic order determination in organometallic chemistry in 2014; the Journal of the American Chemical Society and Organometallics did not require three or more independent replicates for log-log slope determination in mechanistic studies of this type.

**modern-era deficient:**

- **U-1 (cumulative DFT uncertainty — RRHO, PES-scan truncation, benchmarking absence):** Modern computational mechanistic papers (post-2016) are expected to report quasi-RRHO corrections for bimetallic association/dissociation steps, following Grimme's 2012 recommendation (which was available in 2014 but not yet a universal expectation). The 2014 paper's explicit acknowledgment that B2 energetics "is best accomplished through molecular dynamics simulations" — combined with its decision not to perform MD and not to apply even the simpler quasi-RRHO correction — is deficient by contemporary standards that treat uncertainty propagation for bimetallic DFT as mandatory for claims of pathway selectivity.

- **U-5 (absence of benchmarking for PBE0-dDsC/TZ2P on open-shell Ni(III)):** By 2018 standards (following the Misal et al. and related DLPNO-CCSD(T) benchmarking literature for first-row transition metals), a paper claiming an 18.7 kcal/mol barrier difference as the primary mechanistic discriminator for an open-shell Ni(III) d7 system is expected to provide benchmarking data or cite a validated benchmark for the functional/basis-set combination in that electronic-structure class.

- **B-4 (non-integer orders interpreted as integer without confidence intervals):** Modern reporting standards (post-2018) for organometallic kinetics require confidence intervals or standard deviations on log-log slopes; the "about second order" qualitative rounding of 1.7 to 2 and −0.3 to 0 without statistical support would not meet current expectations of journals such as ACS Catalysis or JACS for mechanistic papers claiming a specific TDS assignment on the basis of kinetic order.

- **B-6 (catalyst homogeneity not re-established under kinetic conditions):** Modern mechanistic papers are expected to reproduce key catalyst-identity controls (Hg-poisoning test, resting-state isolation) under the exact conditions of the reported kinetic measurements, rather than relying on prior-literature results obtained under different temperature and addition-rate conditions.

---

### §5 Shortest-reinforcement route

**Objective function 1: VQ-3 [Mechanism]**

Current state: VQ-2 qualified → target VQ-3.
Unresolved at VQ-3: RI-03 (SRG-3, SRG-7), RI-04 (SRG-2), RI-06 (SRG-7), PRI-11 (SRG-4).

**Shortest route to VQ-3:**

1. **EP-04a [Discrimination / replication pack]** — Apply quasi-RRHO entropy correction (Grimme 2012) to the B1 + Pr• → B2 step and perform DLPNO-CCSD(T)/cc-pVTZ single-point energies at the M06/def2-SVP geometries for TSB2,B3 and TSE1,E2; report the uncertainty-corrected 18.7 kcal/mol selectivity value with error bounds. Advances RI-04 (SRG-2), and partially advances RI-03 (SRG-3) by establishing a benchmarked reference for the escape-rebound barrier.

2. **EP-08a [Replication / uncertainty pack] — kinetic extension** — Report ⟨S²⟩ for TSE1,E2 and the spin-corrected open-shell singlet energy; confirm the Ni(III) spin-density assignment of E1 with NPA analysis at TZ2P. Advances RI-03 (SRG-3).

3. **EP-03a [Direct-observation / state-assignment pack]** — Provide algebraic derivation of the rate law from Figure 8 (eq 3) under the pre-equilibrium approximation, specifying the limiting assumptions required to obtain the integer orders 2, 2, 0 from the observed non-integer values 1.7, 2.0, −0.3. Advances PRI-11 (SRG-4); this is an analytical rather than experimental investment.

4. **EP-06a [Analogy-validation pack]** — Compute the DFT free-energy profile for the comproportionation step (Ni(I) 16 + Ni(III) 14 → Ni(II) 11 + Ni(II) 13) in the alkyl−aryl system at the PBE0-dDsC/TZ2P//M06/def2-SVP level, establishing whether it is thermodynamically and kinetically feasible on the timescale of catalysis. Advances RI-03 and RI-06 (SRG-7).

*Information-gain ordering rationale:* EP-04a is first because it advances two RIs simultaneously (RI-04 and partially RI-03) and uses existing calculated geometries (no new experimental work required). EP-08a (spin correction) is second because it requires only re-analysis of existing Gaussian09/ADF output files. EP-03a is third because it is a pencil-and-paper derivation from an already proposed mechanism. EP-06a is fourth because it requires new DFT calculations but is relatively routine given the established workflow.

Certification-gate note: The experimental investment order follows information gain (EP-04a → EP-08a → EP-03a → EP-06a), but the final VQ-3 certification requires that RI-01 (SRG-1, SRG-8) and RI-07 (SRG-5, CLA-1) from VQ-2 are simultaneously resolved or judged non-fatal, consistent with the inheritance principle.

---

**Objective function 2: VQ-4 [Benchmark]**

Prerequisite: VQ-3 certification. Additional requirements beyond VQ-3:

**Shortest route to VQ-4 (after VQ-3):**

1. **EP-08a [Replication / uncertainty pack] — radical clock** — Report GC yields and conversions at each catalyst loading for substrate 7 + PhMgCl (from the C₁₂H₂₆ internal standard already described); report standard deviations on the linear:cyclized ratios from ≥3 independent trials. Advances RI-08 (SRG-1).

2. **EP-05a [Quantitative-ranking substantiation pack]** — Conduct kinetic order determination with ≥3 independent trials per data point; report 95% confidence intervals on the log-log slopes for catalyst, Grignard, and alkyl iodide orders; provide a mechanistic interpretation of the 1.7 catalyst order and −0.3 alkyl iodide order or establish statistically that they are indistinguishable from 2 and 0 respectively. Advances RI-05 (SRG-6) and RI-08 secondary (SRG-6).

3. **EP-07a [Boundary-test pack]** — Measure initial rates at two temperatures (0 °C and −20 °C) to obtain Eyring activation parameters and allow temperature extrapolation of the TDS assignment to room temperature. Advances RI-07 (SRG-5).

Certification-gate note: The experimental investment order follows information gain (EP-08a radical clock is low-cost from existing GC data → EP-05a kinetic replication is moderate-cost → EP-07a temperature study is moderate-to-high cost), but the final certification follows the gate order VQ-1 → VQ-2 → VQ-3 → VQ-4.

---

### §6 Contribution to institutional design

**PRI-11 confirmation (Mechanism–kinetics decoupling):**

This paper provides the original case for PRI-11 [Mechanism–kinetics decoupling] as noted in the prompt codebook v0.2a: [REDACTED: substantial verbatim quotation; see Tier 9] The specific form here is: the proposed catalytic cycle (Figure 8) and redistributive transmetalation (eq 3) predict a specific rate law, but the paper does not perform the algebraic derivation. Instead, the paper states [REDACTED: substantial verbatim quotation; see Tier 9] — a conditional assertion that records kinetic consistency without derivation. Combined with the confirmation in Pengfei 2024, PRI-11 promotion from provisional to established is supported by this analysis.

**Labeling mismatch pattern:**

A clear labeling mismatch is present in this paper: the catalytic cycle (Figure 8) is presented as a complete mechanism with factual prose ([REDACTED: substantial verbatim quotation; see Tier 9]), yet the comproportionation step has no experimental or computational support within the paper and is explicitly imported by analogy from ref 20. The factual-verb narrative ("regenerates," [REDACTED: verbatim source quotation; see the source paper via its DOI]). This co-occurs with RI-06 (SRG-7) as anticipated by the codebook application note.

**RI co-occurrence pattern:**

SRG-2 exhibits a three-way RI co-occurrence: RI-04 (unreplicated discriminator — single DFT barrier with no uncertainty quantification) + RI-06 (imported model — PBE0-dDsC protocol from main-group to open-shell Ni(III)) + RI-03 subtype (available-but-unutilized: spin-correction data available in Gaussian09 output but not reported, SRG-3). Resolving only RI-04 (via benchmarking) is insufficient without also addressing RI-06 (via functional validation for the electronic-structure class) and RI-03 (via spin-correction reporting). This three-way co-occurrence at SRG-2/3 represents a structurally interlinked EP cluster: EP-04a, EP-06a, and EP-03a must all be applied before VQ-3 is achievable via the DFT stream.

**Incomplete negative evidence pattern:**

The radical-clock argument for bimetallic OA (over escape-rebound) relies on the DFT barrier comparison (22.1 vs. 3.4 kcal/mol) as positive mechanistic evidence. However, the paper also invokes as supporting evidence that [REDACTED: substantial verbatim quotation; see Tier 9] due to the high endergonicity (+26.5 kcal/mol) of the E-surface interconversion reaction (B1 abstracting bromine from CH₃CH₂CH₂Br). This constitutes incomplete negative evidence: the high endergonicity of the escape-rebound entry point is used as positive evidence against escape-rebound without mass-balance analysis of whether any fraction of the reaction proceeds via the B1-to-E-surface pathway under the actual reaction conditions. This is a case-specific implementation of RI-04 in the radical-clock context.

**Era-norm boundary condition — new insight:**

This paper provides a clear example of the dual-classification pattern identified in §4 (B-3, U-3, B-7): items that were communication-era tolerated in 2014 but are modern-era deficient in 2026. The pattern is especially pronounced for computational papers in organometallic chemistry: the RRHO entropy issue and the BS-DFT spin-correction issue were both known in the computational chemistry community by 2014 (Grimme 2012; BS-DFT methodology established since the 1990s) but were not uniformly required in organometallic mechanistic papers of that period. This dual-classification pattern should be added to the EP dictionary as a note under EP-03a and EP-04a: [REDACTED: substantial verbatim quotation; see Tier 9]

**New PRI candidate: none detected** beyond the PRI-11 confirmation above. The SRG-5 RI-07 pattern (temperature boundary without failure examples) is covered by the existing RI-07 extended use note in codebook v0.2a.

**EP dictionary case-specific additions:**

- **EP-04a in radical-clock context (Ni organometallic systems):** Add implementation note — [REDACTED: substantial verbatim quotation; see Tier 9]
- **EP-06a in bimetallic catalytic cycle context:** Add implementation note — [REDACTED: substantial verbatim quotation; see Tier 9]

This case confirms existing institutional design for RI-01 through RI-09 and extends PRI-11 toward promotion. No new PRI candidate is proposed.

---

> **Tier 8 redaction notice**: This file is a redacted copy of the corresponding Tier 3 / Tier 9 output. Verbatim source-paper quotations have been replaced by `[REDACTED: see source paper §<loc>; full text retained in Tier 9 reviewer-only deposit]` markers, preserving location references and our own analytical content. Bibliographic fields (title, authors, journal, year, DOI), analytical labels (`evidence_chain:` with B-/U-/A-/C- internal IDs), short technical terms, and our own analytical text are not redacted. The redaction was applied by `scripts/redact_for_tier8.py` and, for this version, by `scripts/build_paperA_R1_public.py` with `scripts/redact_source_ngram_runs.py` (scripts of the project repository; they are not deposited).
