prompt_version: stage3-v2-en-20260419
model_info: claude-sonnet-4-6

# Re-certification Assessment Sheet for Scientific Knowledge

## Cherney, Kadunce, and Reisman 2015 (Chemical Reviews, review)

---

### §1 Claim Architecture

**Core claim:**

The paper's core claim is a comprehensive cartographic claim: enantioselective and enantiospecific transition-metal-catalyzed cross-coupling reactions of organometallic reagents now constitute a mature subfield of synthetic chemistry, organized around a dual mechanistic taxonomy (enantioselective vs. enantiospecific) and three chirality modes (centro, axial, planar). The Novelty pillar is the dual-category organizational framework applied comprehensively for the first time across all nucleophile classes and chirality modes through the end of 2014, superseding earlier reviews with narrower scope (pre-2008 Cu catalysis, individual reaction types). The Utility pillar is that the cartography defines the research frontier by identifying five specific underdeveloped areas (tert-alkyl coupling, two-sec-alkyl coupling, C(sp³) B/Sn nucleophiles, aryl-nucleophile quaternary centers, general atroposelective methods) and provides practitioners with a structured literature guide for selecting catalyst systems by reaction type and nucleophile class.

A second, embedded claim runs through sections 2.2.1–2.2.3: the Ni¹/Ni³ oxidation-state manifold is the operative mechanistic framework for stereoconvergent cross-coupling of secondary alkyl electrophiles, enabling the review's unification of the DKR/KR/DYKAT regime assignments, the precoordination enantiocontrol model, and the radical clock interpretation under a single mechanistic architecture. This embedded mechanistic claim is presented as established rather than proposed.

**Layered structure:**

The claim architecture has three independent layers. Layer 1 (comprehensive coverage) is a meta-claim about the review itself and cannot be refuted by any experimental result from the field — only by showing that important literature was missed or misclassified. Layer 2 (dual-category organizational framework) is refutable only if the enantioselective / enantiospecific distinction is shown to be empirically indistinguishable (i.e., if a single catalytic system were shown to operate by both mechanisms simultaneously without predictable switching). Layer 3 (frontier identification in the Conclusion) is in principle refutable if any of the five deferred areas (A-1 through A-5) had already been solved in published literature by December 2014 and was merely missed. These three layers are independent: a counterexample to Layer 3 would not collapse Layer 1 or Layer 2. The embedded Ni¹/Ni³ mechanistic claim is not formally presented as a layer of the main review claim, but it is load-bearing for sections 2.2.1–2.2.3 and for the DKR/KR interpretations. If the Ni¹/Ni³ mechanism were shown to be incorrect, the mechanistic unification across those sections would require revision without necessarily invalidating the cartographic claim of Layer 1 or Layer 2.

**Inter-layer dependency:** Layer 3 (frontier identification) depends implicitly on Layer 1 (comprehensive coverage) — the frontier areas are defined as absent from the review's own corpus, which assumes comprehensive coverage. If coverage is incomplete, the frontier identification is unreliable.

---

### §2 SRG / CLA → RI / ER / EP Crosswalk

**SRG-1 [Ni–heteroatom precoordination mechanistic basis for enantiocontrol]**

* **Primary RI**: RI-03 [Unobserved explanatory]
* **Secondary RI**: RI-06 [Imported model]
* **ER**: The claim that Ni–heteroatom precoordination determines enantioselectivity across the PPFA-type amine series, the carbamate/sulfonamide series, and the ether/halohydrin series requires spectroscopic detection of the Ni–N or Ni–O precoordination complex (NMR, EXAFS, X-ray) or kinetic evidence for precoordination (saturation kinetics in [Grignard] or inhibition by exogenous tertiary amine). Without one of these demonstrations, the precoordination model is an imported analogy from organometallic coordination chemistry rather than an established mechanistic assignment for any of the cited catalytic systems.
* **EP**: EP-03a [Direct-observation / state-assignment pack]; EP-06a [Analogy-validation pack]
* **Case-specific implementation**: For the PPFA/Ni system (Figure 6, p. 9591), run saturation kinetics of the coupling rate as a function of [sec-BuMgX] in PhBr at the reaction temperature; a hyperbolic rate dependence would confirm precoordination, a linear dependence would refute it. For the Fu-group Ni/L45 system (sections 2.2.3), add exogenous N,N-dimethylcyclohexylamine at the reaction concentration of the Grignard reagent and measure the resulting ee change; amine inhibition would confirm Ni–N precoordination as a kinetically relevant step. For structural confirmation, add the isolated ligand L38 to Ni(cod)₂ and the α-bromo amide substrate 62 (without Grignard) and look for a Ni–substrate nitrogen complex by ¹H NMR or ESI-MS.
* **Notes**: SRG-1 encompasses U-2 (PPFA amine precoordination prerequisite-absence; severity: high; convergence 3/3, temperature_gap=low), U-10 (oxygen/carbamate directing series prerequisite-absence; severity: medium), and B-5 (Weinreb amide scope failure without mechanistic explanation). Position in TEMPERATURE_SUMMARY: high_convergence_low_gap. The RI-06 secondary code applies because the precoordination model originates from organometallic coordination chemistry (Ni–amine precoordination in PPFA synthesis) and is imported wholesale into the catalytic context, where neither isomorphism nor kinetic equivalence has been demonstrated (RI-06 cycle-level import, per v0.2a scope note).

---

**SRG-2 [Ni¹/Ni³ oxidation-state manifold experimental validation]**

* **Primary RI**: RI-03 [Unobserved explanatory]
* **Secondary RI**: RI-04 [Unreplicated discriminator]
* **ER**: The claim that Ni¹ and Ni³ are the operative oxidation states (rather than Ni⁰/Ni²) in the stereoconvergent cross-coupling of α-bromo amides, α-bromo ketones, benzylic electrophiles, and 1-bromoindanes requires either: (a) direct detection of Ni¹ (EPR: S=1/2, g ~ 2.0) and Ni³ (EPR: S=1/2, distinct g-tensor) intermediates under catalytic turnover conditions, or (b) stoichiometric organometallic synthesis and characterization of Ni¹ and Ni³ complexes bearing the L38-type ligand and an alkyl group, demonstrating that such species are on-cycle (i.e., kinetically competent at reaction rates). DFT-computed energy orderings alone do not constitute operational validation.
* **EP**: EP-03a [Direct-observation / state-assignment pack]; EP-04a [Discrimination / replication pack]
* **Case-specific implementation**: For EPR detection, conduct the Ni/L38 α-bromo amide Negishi coupling under freeze-quench conditions (quench at 5, 30, 120 s after mixing at −20 °C) and record X-band EPR at 77 K; paramagnetic species (Ni¹, Ni³) would appear at g ~ 2.0 and g ~ 2.2 respectively, distinguishable from diamagnetic Ni⁰/Ni². For CV: record the Ni¹/Ni³ couple for Ni/L38 in DMF (−60 °C) and verify that the observed reversible wave is accessible from Ni¹ under the reaction's reductant (Zn, organozinc). For the radical clock discrimination (Scheme 4, substrate 49): measure the radical cyclization rate constant k_cyc of the homoallylic radical from 49 in DMF at −20 °C (reference clock rate constants for primary radicals are available from the literature); this converts the uncyclized:cyclized ratio into an intermediate lifetime (τ = [cyclized]/([uncyclized]·k_cyc)) and permits classification as free radical (τ > 10⁻⁸ s), cage radical (10⁻¹⁰ < τ < 10⁻⁸ s), or organonickel-bound (τ < 10⁻¹⁰ s).
* **Notes**: SRG-2 encompasses U-1 (critical severity; convergence 3/3, temperature_gap=none — highest-priority item in the analysis), C-5 (Lin computational study cited as mechanistic authority without experimental follow-through), and B-6 (irreversibility of OA stated without experimental citation). Position in TEMPERATURE_SUMMARY: high_convergence_low_gap (none gap = highest priority). The RI-04 secondary code applies because the single radical clock experiment (substrate 49) with a linear [Ni]-dependence is interpreted as conclusive evidence for a freely diffusing radical — a high-discriminatory interpretation from a single data point, without the rate constants needed to verify it (RI-04 case-specific: incomplete negative evidence pattern, per v0.2a codebook notes).

---

**SRG-3 [KR/DKR/DYKAT rate constant absence]**

* **Primary RI**: RI-05 [Qualitative overread]
* **Secondary RI**: RI-08 [Unquantified reliability]
* **ER**: The assignment of a secondary Grignard reagent to the DKR, KR, or DYKAT kinetic regime requires that the racemization rate constant k_rac and the coupling rate constant k_coup be measured at the reaction temperature; ratio-dependence of ee (excess reagent dependence) is a necessary but not sufficient condition for distinguishing DKR (k_rac >> k_coup, both enantiomers react at equal rates) from KR (k_rac << k_coup) from DYKAT (thermodynamic equilibration followed by selective reaction). Without at least one k_rac / k_coup ratio measured for any Grignard substrate in sections 2.1–2.2, all regime assignments carry an unquantified uncertainty.
* **EP**: EP-05a [Quantitative-ranking substantiation pack]; EP-08a [Replication / uncertainty pack]
* **Case-specific implementation**: For Grignard 13 (Scheme 2b, the benchmark case where "might suggest" KR language is used explicitly), measure the racemization half-life of 13 at −78 °C and at 0 °C in THF by quench-labeling (add D₂O at timed intervals, determine the deuterium incorporation ratio by ²H NMR); separately measure the pseudo-first-order coupling rate constant at −78 °C by initial-rate monitoring (e.g., GC sampling at 1, 2, 5, 10 min). The ratio k_rac/k_coup at the reaction temperature would place 13 unambiguously in the DKR, KR, or intermediate zone.
* **Notes**: SRG-3 encompasses U-3 (high severity; convergence 2/3, temperature_gap=none) and B-4 (KR/DKR for Grignard 13). RI-05 is primary because the regime assignment is derived from qualitative observations (ee changes with reagent ratio) rather than from numerical rate data; the observation pattern is consistent with the assigned regime but does not quantitatively support it. RI-08 secondary applies because all regime assignments are made without replicate rate measurements or uncertainty descriptors. Position in TEMPERATURE_SUMMARY: high_convergence_low_gap.

---

**SRG-4 [Radical chain pathway quantitative kinetics]**

* **Primary RI**: RI-04 [Unreplicated discriminator]
* **Secondary RI**: RI-03 [Unobserved explanatory]
* **ER**: The conclusion that the Ni-catalyzed coupling of secondary homoallylic halides proceeds through a freely diffusing (non-caged) radical requires: (a) the cyclization rate constant k_cyc for clock substrate 49 under reaction conditions (to convert ring-opened:ring-closed ratio into a radical lifetime); (b) a quantum yield measurement (to distinguish chain from non-chain pathway); (c) TEMPO inhibition with a measured inhibition rate constant or yield-vs-[TEMPO] profile (to confirm radical character and rule out organonickel-bound radical). The linear [Ni]-dependence of uncyclized:cyclized ratio is consistent with a free radical but is not sufficient to establish it because a partially caged organonickel species would also give a metal-loading-dependent product ratio.
* **EP**: EP-04a [Discrimination / replication pack]; EP-03a [Direct-observation / state-assignment pack]
* **Case-specific implementation**: Use the well-characterized radical cyclization rate constant for the hex-5-en-1-yl radical (k_cyc ≈ 2.3 × 10⁸ s⁻¹ at 20 °C) as a starting point; measure k_cyc for substrate 49's homoallylic radical in DMF at −20 °C by laser flash photolysis or calibrated radical clock comparison. For quantum yield: compare the product yield obtained under identical conditions with 1.0 equiv and 0.1 equiv Ni loading (a chain process will show turnover greater than stoichiometric Ni; a non-chain process will not). For TEMPO: add 0, 0.1, 0.5, 2.0 equiv TEMPO relative to alkyl halide and plot yield vs. [TEMPO]; a radical pathway shows yield suppression at sub-stoichiometric TEMPO.
* **Notes**: SRG-4 encompasses U-4 (high severity: radical cyclization rate constant absence) and U-7 (medium severity: quantum yield/TEMPO absence). The RI-04 pattern here is the "incomplete negative evidence" subtype (v0.2a codebook note): the radical clock result is used as positive mechanistic evidence but lacks mass-balance closure (TEMPO trapping) and kinetic-window evaluation (k_cyc). Position in TEMPERATURE_SUMMARY: high_convergence_low_gap (step distance=0 for SRG-4 items).

---

**SRG-5 [Cu/L101 functional group tolerance]**

* **Primary RI**: RI-07 [Unsupported boundary]
* **Secondary RI**: RI-08 [Unquantified reliability]
* **ER**: The claim of "excellent chemo- and regioselectivity" for Cu/L101-catalyzed allylic alkylation with 9-BBN reagents (p. 9630) requires demonstration of tolerance for at least a representative set of functional groups (ester, free alcohol, amine, ketone, heteroaromatic, acid-sensitive groups) beyond the single aryl bromide competition experiment reported. A single chemoselectivity datapoint (aryl bromide tolerance) does not constitute a functional group tolerance profile and does not support the "excellent" qualifier across the broader functional group space.
* **EP**: EP-07a [Boundary-test pack]; EP-08a [Replication / uncertainty pack]
* **Case-specific implementation**: Prepare a competition substrate or substrate panel in which one of the following functional groups is present as a bystander: (a) ester (ethyl ester, lactone), (b) free alcohol, (c) N-protected amine (Boc, Cbz), (d) ketone, (e) pyridine ring. Run the Cu/L101 9-BBN allylic alkylation for each panel member and report yield, ee, and chemoselectivity ratio. A 5-functional-group panel would define the practical scope of the "excellent chemoselectivity" claim.
* **Notes**: SRG-5 encompasses B-11 (convergence 2/3, temperature_gap=none). The RI-07 "negative boundary claim" subtype (v0.2a codebook note) applies: "excellent chemo- and regioselectivity" is a positive boundary claim asserted without the failure examples or range of functional group tests that would support the boundary. RI-08 secondary applies because the single competition experiment is a single data point with no replicate yield/ee data.

---

**SRG-6 [Acyclic vs. cyclic allylic electrophile selectivity gap]**

* **Primary RI**: RI-05 [Qualitative overread]
* **Secondary RI**: RI-03 [Unobserved explanatory]
* **ER**: The systematic observation that acyclic allylic electrophiles give lower ee than cyclic ones in Ni-catalyzed AAS (section 4.1.1) is presented as a scope limitation without mechanistic analysis. Extracting design guidance from this observation requires at least one structural or kinetic measurement that discriminates among the three leading explanations: (a) faster σ→π allyl isomerization in cyclic substrates (due to ring rigidity) giving a more tightly controlled allylic geometry, (b) different S_N2 vs. S_N2′ product ratios for acyclic vs. cyclic allyl-Ni intermediates indicating different allyl complex geometry, (c) different Ni–allyl C–C bond rotation barriers.
* **EP**: EP-05a [Quantitative-ranking substantiation pack]; EP-03a [Direct-observation / state-assignment pack]
* **Case-specific implementation**: Compare the σ→π isomerization half-life of the Ni-allyl complex derived from cyclohex-2-en-1-yl acetate (cyclic, high ee) and pent-2-en-1-yl acetate (acyclic, low ee) under stoichiometric Ni/L conditions (no Grignard) by ¹H NMR line-shape analysis or ¹³C HMBC. Alternatively, report the S_N2 vs. S_N2′ ratio for the corresponding (unlabeled) cross-coupling with MeMgBr under the same conditions as a qualitative proxy: a high S_N2/S_N2′ ratio for the cyclic substrate would indicate allyl geometry lock, while equal ratios would point to geometry-independent factors.
* **Notes**: SRG-6 encompasses B-10 (convergence 2/3, temperature_gap=none; V1=medium, V2=medium). RI-05 is primary because the selectivity gap is reported as a qualitative observation (low ee for acyclic) and attributed implicitly to substrate geometry without numerical support for the geometric assignment. RI-03 secondary applies because the species proposed to explain the gap (a specific allyl-Ni geometry that differs between cyclic and acyclic substrates) is neither observed directly nor kinetically constrained.

---

**Outside the SRGs: CLAs**

**CLA-1 [Computational-mechanism-without-experimental-validation systemic pattern (SRG-8)]**

* **Primary RI**: RI-06 [Imported model]
* **Secondary RI**: RI-04 [Unreplicated discriminator]
* **ER**: Across at least three independent reaction types (Ni¹/Ni³ via Lin et al., DET for Cu/L32 via unnamed computational study, ester-directed carbometallation for Pd/phenanthroline γ-arylation), the review presents DFT-derived mechanistic assignments as operative mechanistic descriptions without reporting experimental predictions derived from those models. For each imported computational mechanism, the claim that it is the operative mechanism requires at least one experimental test of a prediction unique to that mechanism and not shared by the competing mechanism.
* **EP**: EP-06a [Analogy-validation pack]; EP-04a [Discrimination / replication pack]
* **Case-specific implementation**: For the DET mechanism for Cu/L32-catalyzed coupling of racemic cyclic electrophile 313 (C-9, U-8): run (R)-313 and (S)-313 separately under identical Cu/L32 conditions; if DET is operative, both should give the same product ee and configuration, and the rate should be identical from both enantiomers. This is a direct, single-experiment test of the DET prediction that discriminates DET from kinetic resolution.
* **Notes**: CLA-1 corresponds to SRG-8 (systemic pattern documented in S1 META). Grounded in U-8 (DET mechanism, medium severity), C-8 (Sawamura γ-arylation unreported mechanism), C-9 (DET computational study without experimental confirmation). The D-4 Candidate 6 (systemic DFT-without-experimental-validation pattern) maps directly to this CLA. The pattern is not captured in any existing SRG (SRG-1 through SRG-7 address individual mechanistic absences; CLA-1 addresses the field-level norm). The Labeling mismatch pattern (§6 detection criterion) is present here: computational studies are labeled [REDACTED: verbatim source quotation; see the source paper via its DOI]) without modal qualifier.

**CLA-2 [Review's prioritization logic unsupported by biological demand inventory (SRG-7 partial)]**

* **Primary RI**: RI-07 [Unsupported boundary]
* **Secondary RI**: RI-05 [Qualitative overread]
* **ER**: The Conclusion's claim that tert-alkyl coupling, two-sec-alkyl coupling, and related underdeveloped reactions [REDACTED: substantial verbatim quotation; see Tier 9] uses the biological prevalence claim as a priority-setting argument for the five deferred areas (A-1 through A-5). This argument requires either: (a) a systematic survey of natural products and pharmaceuticals containing these motifs and lacking viable enantiocontrolled cross-coupling routes, or (b) a comparison with alternative methods (enzymatic resolution, chiral auxiliary, organocatalysis) for the same structural targets showing the existing alternative routes are inadequate.
* **EP**: EP-07a [Boundary-test pack]; EP-05a [Quantitative-ranking substantiation pack]
* **Case-specific implementation**: Compile a table of 10–20 natural products or approved pharmaceuticals bearing all-carbon quaternary centers or vicinal tertiary centers, noting for each whether a current enantiocontrolled cross-coupling route exists and what the best current alternative route provides in terms of step count and ee. This table would convert the "present in many" qualitative claim into a quantitative unmet-need argument and would make the frontier prioritization evidence-based.
* **Notes**: Grounded in U-5 (medium severity: self-contradictory absence — prioritization logic depends on unvalidated biological need claim), C-7 (Tang natural product synthesis unnamed), C-10 (Breit α-tocopherol not benchmarked). CLA-2 is distinct from A-1 through A-5 (which are deferred research questions) because the CLA addresses the missing premise for the paper's own prioritization logic. RI-07 applies via the "negative boundary claim" subtype (v0.2a): "remain at the forefront" and "a largely undeveloped area of great synthetic promise" are positive scope boundary claims asserted without the failure-example inventory or comparative method survey that would establish the boundary.

---

### §3 Current VQ assessment

**Current judgment: VQ-2 (Method) — partial / fails at specific RI-07 claims; qualified for RI-05**

---

**VQ-1 [Observation] — PASS (non-fatal caveats)**

VQ-1 requires resolution of RI-02 (object identification: product/catalyst structure/purity established). The review covers literature from primary papers where structures are typically confirmed by NMR, HPLC-chiral, X-ray, and optical rotation. As a review, Cherney 2015 does not itself characterize products, but it cites primary literature where characterization was performed. The review cannot be held to RI-02 for results it did not generate. One non-fatal caveat: C-3 (1973–74 Consiglio-Kumada benchmark) — early ee values from the prototypical system are introduced but the primary papers' purity/characterization methods are not discussed and some of those early reports used methods (optical rotation only, not HPLC-chiral) now considered insufficient for stereocentre assignment. This is documented as non-fatal (era-norm tolerated, see §4).

VQ-1 holds, with the non-fatal caveats noted above regarding pre-HPLC era characterization standards for the 1973–74 benchmark papers (C-3).

---

**VQ-2 [Method] — CONDITIONAL PASS (RI-01 non-fatal; RI-07 fails for specific boundary claims)**

VQ-2 requires resolution of RI-01 (reporting integrity: consistent measurement frames enabling cross-comparison) and RI-07 (boundary claims with failure examples), and inherits VQ-1.

RI-01 assessment: B-2 explicitly documents that Figure 5's ligand survey ee values are [REDACTED: substantial verbatim quotation; see Tier 9] This is an acknowledged reporting incoherence (varying temperature, solvent, Ni precursor, loading across the >20 ligands), and no corrective systematic comparison is provided. However, the caution statement is explicit, and the affected section (Figure 5 ligand survey) is clearly delimited. Given that Chemical Reviews format inherently aggregates data from different primary papers with different conditions, this RI-01 instance is judged non-fatal: the caveat is disclosed, and the reader is warned not to draw quantitative cross-study comparisons. If this review is used as a quantitative ligand comparison database, RI-01 becomes fatal; as a qualitative survey, it is non-fatal.

RI-07 assessment: Two specific boundary claims fail RI-07.

First, [REDACTED: substantial verbatim quotation; see Tier 9] (Cu/L101 allylic alkylation with 9-BBN, SRG-5/CLA-2) is a positive boundary claim backed by a single aryl bromide competition experiment. No failure examples for other functional groups are reported; the "excellent" qualifier for a broader functional group space is unsupported. This RI-07 instance is fatal for the chemoselectivity boundary claim itself, though not for the reported yields and ee values from the tested substrates.

Second, the five frontier areas (A-1 through A-5) are defined as "underdeveloped" or "yet to be realized" without an inventory of specific structures that remain inaccessible, making these negative boundary claims unsupported by failure-example surveys (CLA-2).

VQ-2 holds conditionally: RI-01 is non-fatal; RI-07 fails for the Cu/L101 chemoselectivity claim and the frontier prioritization claims, rendering those specific claims below VQ-2 certification, though the remainder of the review's outcome data (yield, ee, substrate scope tables) are not affected by these RI-07 failures.

---

**VQ-3 [Mechanism] — FAILS**

VQ-3 requires resolution of RI-03, RI-04, and RI-06, inheriting VQ-1 and VQ-2.

RI-03 assessment: SRG-1 (Ni–heteroatom precoordination) and SRG-2 (Ni¹/Ni³ manifold) both fail RI-03. The precoordination complex is unobserved; neither NMR, EXAFS, nor kinetic evidence for precoordination has been cited. The Ni¹ and Ni³ intermediates are unobserved directly; no EPR or CV characterization under catalytic conditions is cited. The "available-but-unutilized characterization" RI-03 subtype (v0.2a) does not apply because these characterizations were not performed at the time of the cited primary papers, not merely unreported in the review. These are genuine "not observed" absences, not "observed but not discussed" absences.

RI-04 assessment: SRG-2's radical clock interpretation fails RI-04. The linear [Ni]-dependence for substrate 49's radical clock is a single high-discriminatory data point interpreted as conclusive evidence for a freely diffusing radical, without the rate constant conversion required to establish the intermediate lifetime. The "incomplete negative evidence" RI-04 subtype applies: radical clock results are used as positive mechanistic evidence without mass-balance closure (TEMPO) or kinetic-window evaluation (k_cyc).

RI-06 assessment: SRG-1 (precoordination model imported from organometallic coordination chemistry without kinetic isomorphism demonstration in the catalytic context) and CLA-1 (DFT-derived mechanisms from other systems — Lin et al. Ni¹/Ni³ DFT from gas-phase/implicit-solvent models — imported as operative mechanisms for catalytic conditions in DMF/THF without experimental isomorphism confirmation) both fail RI-06.

VQ-3 [Mechanism] FAILS. Unresolved: RI-03 (SRG-1 and SRG-2), RI-04 (SRG-2, SRG-4), RI-06 (SRG-1 and CLA-1).

*Layered VQ asymmetry:* However, **Layer 1 (comprehensive cartographic coverage) on its own** reaches VQ-2 comfortably: the outcome data (yield, ee, substrate scope) in the survey sections are drawn from primary papers that did characterize their products and did report their methods consistently within each paper. The VQ-3 failure is localized to the mechanistic interpretation sections (2.2.1–2.2.3, 3.1.2, 4.1.1) where the precoordination, Ni¹/Ni³, DKR/KR, and DET frameworks are invoked. The cartographic claim of the review is VQ-2 certified; the embedded mechanistic claims fail VQ-3.

---

**VQ-4 [Benchmark] — NOT REACHED**

VQ-4 requires resolution of RI-08 and RI-09, inheriting VQ-3. Since VQ-3 fails, VQ-4 certification is not evaluated. Noting for record: even if VQ-3 were resolved, RI-08 failures (SRG-3, SRG-5: no replicate rate measurements or uncertainty descriptors for regime assignments or chemoselectivity claims) and RI-09 patterns (C-1: "paradigm shift" claim relative to Nobel-winning achiral methods without direct comparison) would require resolution for VQ-4.

---

### §4 Era-Norm Annotation

**communication-era tolerated:**

- **B-2** (Figure 5 ligand survey: "comparisons should be drawn with caution" — conditions vary across >20 ligands). In 2015, Chemical Reviews reviews aggregating multi-decade literature routinely compiled results from papers using different Ni precursors, solvents, and temperatures; systematic head-to-head ligand screening within a review was not standard practice. The caution disclaimer was the accepted substitute for standardized conditions at this format scale.

- **C-3** (Consiglio-Kumada 1973–74 benchmark: early ee values from the prototypical Ni/DIOP system reported by optical rotation without chiral HPLC). In 1973–74, chiral HPLC for ee determination had not yet been established as standard practice; optical rotation-based ee reporting was the field norm. The review reproduces the 1973–74 data as historical context, and the era-norm relaxation of the primary papers' characterization standards is appropriate.

- **B-6** (irreversibility of oxidative addition stated without citing the specific experiment). In a 66-page review covering 427 papers, compression of mechanistic conclusions to single sentences without citing every supporting experiment was tolerated by Chemical Reviews editorial standards. The "Further studies confirmed" phrasing is a genre convention of this review format.

- **B-13** (rate-determining step assignment for meso-anhydride desymmetrization — method for assignment not described, absolute rate constants absent). The mechanistic study referenced is a kinetic report from the primary literature; the review format permits reporting the conclusion without reproducing the methodology.

**modern-era deficient:**

- **U-1 / SRG-2** (Ni¹/Ni³ mechanism presented as established without EPR, CV, or stoichiometric organometallic evidence). By 2015, EPR characterization of Ni¹ and Ni³ complexes in the context of Ni-catalyzed cross-coupling was an achievable experiment (several groups had characterized Ni¹ alkyl complexes by EPR; freeze-quench EPR of catalytic mixtures was technically feasible). Presenting the Ni¹/Ni³ mechanism as established without citing EPR confirmation is not defensible by 2015 standards. By contemporary standards (2026), with multiple EPR and electrochemical studies of Ni-catalyzed cross-coupling now published, the absence is a clear modern-era deficiency.

- **U-2 / SRG-1** (precoordination mechanism validated solely by SAR). By 2015, saturation kinetics and amine inhibition experiments were standard mechanistic tools in organometallic catalysis. The absence of these experiments for a mechanism presented as the dominant design principle across an entire subsection of the field is a modern-era deficiency.

- **B-4 / U-3 / SRG-3** (KR/DKR/DYKAT assignments without measured rate constants). By 2015, quench-labeling methods for measuring Grignard racemization rates were established. A review that introduces the DKR/KR/DYKAT framework as the organizing kinetic principle should benchmark at least one assignment with measured rate constants. The exclusive reliance on reagent-ratio dependence of ee is a modern-era deficiency in a mechanistically organized review.

- **B-15** (s-factor for atropisomer kinetic resolution stated as "approximately 5" without the Kagan–Duplomb conversion-dependent ee analysis that establishes s-factors). By 2015, reporting a selectivity factor without the analytical method for its determination was not accepted in primary mechanistic papers; importing an unverified s-factor into a review is a modern-era deficiency.

- **CLA-1 / SRG-8** (DFT-derived mechanisms presented as operative without experimental predictions). By 2015, the field had established the norm (reinforced by the Houk group and others) that computational mechanisms should be accompanied by experimental predictions and tests. The uniform presentation of DFT proposals as mechanistic conclusions is a modern-era deficiency across all three systems (Ni¹/Ni³, DET Cu/L32, Sawamura γ-arylation).

**Dual classification (tolerated then, deficient now):**

- **B-2** (Figure 5 ligand survey inconsistency): tolerated in 2015 by Chemical Reviews format convention; deficient by modern standards because quantitative ligand comparison databases are now routinely expected in reviews (see e.g., 2020+ Acc. Chem. Res. standards), and a 2025 review of this scope would be expected to standardize at least one representative comparison series.

---

### §5 Shortest-reinforcement route

**Objective function 1: Advance the embedded mechanistic claims from VQ-2 to VQ-3**
(Required: resolve RI-03 for SRG-1 and SRG-2; resolve RI-04 for SRG-2 and SRG-4; resolve RI-06 for SRG-1 and CLA-1.)

**Shortest route to VQ-3:**

1. **EP-03a** [Direct-observation / state-assignment pack] — Freeze-quench EPR characterization of the Ni/L38 system under catalytic α-bromo amide Negishi coupling conditions to detect Ni¹ and Ni³ intermediates directly; simultaneously resolves RI-03 for SRG-2 (Ni¹/Ni³) and provides the kinetic detection required for RI-06 isomorphism confirmation. Single experiment, highest information gain across SRG-2 and CLA-1.
   Advances RI-03 (SRG-2), RI-06 (CLA-1, partial).

2. **EP-03a** [Direct-observation / state-assignment pack] — Saturation kinetics of coupling rate vs. [sec-BuMgX] for the Ni/PPFA system in PhBr at reaction temperature; if hyperbolic, confirms Ni–N precoordination (resolves RI-03 for SRG-1); if linear, refutes it. Exogenous amine inhibition experiment provides orthogonal confirmation.
   Advances RI-03 (SRG-1), RI-06 (SRG-1 import validation).

3. **EP-04a** [Discrimination / replication pack] — Measure the radical cyclization rate constant k_cyc for clock substrate 49's homoallylic radical in DMF at −20 °C, and run TEMPO inhibition yield vs. [TEMPO] profile under catalytic conditions; these two measurements together resolve RI-04 for SRG-2 and SRG-4 simultaneously.
   Advances RI-04 (SRG-2, SRG-4), RI-03 (SRG-4).

4. **EP-06a** [Analogy-validation pack] — For the DET mechanism (Cu/L32, CLA-1/U-8), run (R)-313 and (S)-313 separately under identical conditions and compare ee and rate; this is a single definitive experiment that tests the isomorphism between the DFT-derived DET model and the catalytic system.
   Advances RI-06 (CLA-1).

5. **EP-05a** [Quantitative-ranking substantiation pack] — Measure k_rac and k_coup for Grignard 13 at the reaction temperature (quench-labeling for k_rac; initial-rate GC monitoring for k_coup); resolves RI-05 for SRG-3 by replacing the qualitative "might suggest" regime assignment with a quantitative ratio.
   Advances RI-05 (SRG-3), RI-08 (SRG-3 partial).

Certification-gate note: The experimental investment order above follows information gain (EP-03a twice because it simultaneously advances the two highest-priority SRGs), but the final certification follows the gate order VQ-1 → VQ-2 → VQ-3 → VQ-4 regardless of the order in which individual RI deficiencies are resolved.

---

**Objective function 2: Advance from VQ-3 to VQ-4** (prerequisite: VQ-3 achieved)

**Shortest route to VQ-4:**

1. **EP-08a** [Replication / uncertainty pack] — For the Cu/L101 allylic alkylation 9-BBN system (SRG-5), prepare a 5-functional-group competition substrate panel and report yield/ee/chemoselectivity for each; replaces the single aryl bromide competition experiment with a systematic tolerance profile, resolving RI-08 and RI-07 for SRG-5.
   Advances RI-08 (SRG-5), RI-07 (SRG-5).

2. **EP-09a** [Internal benchmark pack] — For the "paradigm shift[REDACTED: substantial verbatim quotation; see Tier 9]paradigm shift" framing.
   Advances RI-09 (C-1).

3. **EP-07a** [Boundary-test pack] — Compile an inventory of 10–20 natural products bearing all-carbon quaternary centers or vicinal tertiary centers with no viable enantiocontrolled cross-coupling route, and show that current alternative methods (enzymatic resolution, organocatalysis) fail on ≥5 of these targets; resolves RI-07 for CLA-2 (frontier prioritization).
   Advances RI-07 (CLA-2).

Certification-gate note: The experimental investment order above follows information gain, but the final certification is fixed by the gate order VQ-1 → VQ-2 → VQ-3 → VQ-4.

---

### §6 Contribution to institutional design

**New representative cases for existing RI codes:**

- **RI-03 (Unobserved explanatory) — largest-scale review-context instance recorded.** Cherney 2015 provides the first RI-03 instance in a review article rather than a primary paper, and the scale is qualitatively different: the unobserved species (Ni¹ and Ni³ intermediates) underpin the mechanistic rationale for an entire subsection of a 66-page review covering >200 reactions. The institutional design implication: RI-03 applies to reviews when a mechanistic model is presented as the organizing framework for a large body of experimental data, not only when individual papers propose a specific intermediate.

- **RI-06 (Imported model) — cycle-level review-format import.** The precoordination model (SRG-1) and the DFT-derived Ni¹/Ni³ model (CLA-1) both demonstrate RI-06 at the cycle-level (v0.2a scope note confirmed). The review imports entire mechanistic cycles from organometallic coordination chemistry (PPFA precoordination from stoichiometric Ni–amine chemistry) and from gas-phase/implicit-solvent DFT (Lin et al. Ni¹/Ni³ energetics) into the catalytic context without demonstrating kinetic isomorphism. This is a confirmed new case for the cycle-level RI-06 scope note.

- **RI-07 (Unsupported boundary) — "qualitative superiority claim in a review's Conclusion" subtype.** The frontier prioritization (A-1 through A-5, CLA-2) represents a systematic use of RI-07 negative boundary claims ("underdeveloped," "yet to be realized," "great synthetic promise") without the failure-example inventory that would establish the boundary. This is a new subtype for the institutional design: review Conclusions that define a research frontier by assertion rather than by systematic failure-mode inventory.

**Labeling mismatch pattern detected:**

CLA-1 exhibits the labeling mismatch pattern. The DET mechanism for Cu/L32 is introduced as [REDACTED: substantial verbatim quotation; see Tier 9] (hypothesis label: "proposed") but the surrounding narrative uses factual verbs ([REDACTED: verbatim source quotation; see the source paper via its DOI] (first sentence uses "proposed[REDACTED: substantial verbatim quotation; see Tier 9]proposed[REDACTED: substantial verbatim quotation; see Tier 9]often co-occurs with RI-06").

**RI co-occurrence pattern:**

SRG-2 exhibits a three-RI co-occurrence: RI-03 (Ni¹/Ni³ unobserved) + RI-04 (radical clock single-experiment overinterpretation) + RI-06 (Lin DFT model imported). Resolving only RI-03 (EPR detection of Ni¹/Ni³) would not suffice for VQ-3 certification if RI-04 (radical clock kinetics) remains unresolved, because the radical clock result is presented as independent evidence for the Ni¹/Ni³ radical chain pathway — the two arguments are co-dependent. Resolving RI-03 and RI-04 together would, however, also advance RI-06 (by confirming experimental isomorphism of the DFT-derived cycle). This is the first three-RI co-occurrence case in the dataset; prior cases were typically two-RI.

**Incomplete negative evidence pattern (confirmed for SRG-4):**

The radical clock experiment for substrate 49 (SRG-4) is a confirmed instance of the "incomplete negative evidence" RI-04 subtype (v0.2a codebook note): radical clock results (linear [Ni]-dependence of uncyclized:cyclized ratio) are used as positive mechanistic evidence for a freely diffusing radical without mass-balance closure (TEMPO trapping yield) or kinetic-window evaluation (k_cyc). This is the third confirmed instance in the dataset (after Monnereau 2009 and Breitenfeld 2014 for TEMPO/radical clock patterns), strengthening the case for codifying the "incomplete negative evidence" RI-04 subtype as a formal note in the codebook v0.3.

**PRI promotion considerations:**

- **PRI-11 (Mechanism–kinetics decoupling):** The DKR/KR/DYKAT regime assignments (SRG-3) are mechanistically supported but algebraically unverified — k_rac and k_coup are not derived from the proposed kinetic scheme. However, PRI-11 as currently defined requires that [REDACTED: substantial verbatim quotation; see Tier 9] SRG-3 is a different pattern: the kinetic framework (DKR/KR) implies specific rate constant inequalities that are never measured, rather than the mechanism implying a specific rate law that is never derived. This is a conceptually related but structurally distinct pattern from PRI-11. No promotion action is warranted; the SRG-3 pattern is best accommodated within RI-05 (Qualitative overread) with a new implementation note: [REDACTED: substantial verbatim quotation; see Tier 9]

- **New PRI candidate — PRI-12 candidate: Computational mechanism without experimental validation (review-scale pattern).** The systemic pattern in CLA-1 (SRG-8) — DFT-derived mechanisms presented as operative across three independent reaction types in a single review, without experimental predictions or tests — constitutes a structural pattern not fully captured by existing RI codes. RI-06 (Imported model) captures individual instances; what CLA-1 adds is the systemic, field-level dimension: when this pattern appears across multiple reaction types in a review, it creates a false consensus about the field's mechanistic understanding. Proposal: **PRI-12 candidate: [REDACTED: substantial verbatim quotation; see Tier 9]** One additional case from a different review or multi-system primary paper would be needed for promotion.

**New EP dictionary implementation:**

For review-article contexts, EP-03a (Direct-observation / state-assignment pack) requires a modified implementation note: [REDACTED: substantial verbatim quotation; see Tier 9]

---

> **Tier 8 redaction notice**: This file is a redacted copy of the corresponding Tier 3 / Tier 9 output. Verbatim source-paper quotations have been replaced by `[REDACTED: see source paper §<loc>; full text retained in Tier 9 reviewer-only deposit]` markers, preserving location references and our own analytical content. Bibliographic fields (title, authors, journal, year, DOI), analytical labels (`evidence_chain:` with B-/U-/A-/C- internal IDs), short technical terms, and our own analytical text are not redacted. The redaction was applied by `scripts/redact_for_tier8.py` and, for this version, by `scripts/build_paperA_R1_public.py` with `scripts/redact_source_ngram_runs.py` (scripts of the project repository; they are not deposited).
