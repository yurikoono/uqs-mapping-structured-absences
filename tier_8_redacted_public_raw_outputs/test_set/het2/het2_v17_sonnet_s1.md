```
prompt_version: stage1-v17-20260415
model_info: claude-sonnet-4-6

target_title:   Deconvoluting Substrates, Support, and Temperature Effects on Leaching and Deactivation of Pd Catalysts: An In Situ Study in Flow
target_authors: Oliver J. Newton, Matthew J. Takle, Jeffery Richardson, Klaus Hellgardt, King Kuok Mimi Hii
target_start:   page 1: [REDACTED: paper boundary quote; see Tier 9]
target_end:     end of document

[Agent fields]
V1: Heterogeneous catalysis / flow chemistry — generates questions about experimental design, catalyst characterization, and data validity in the context of Pd leaching studies.
V2: Organometallic reaction mechanisms / physical inorganic chemistry — generates questions about whether mechanistic claims (α-hydride elimination, oxidative addition, Pd(0) stabilization) are experimentally grounded.
V3: Analytical chemistry / flow reactor measurement design — generates questions about measurement validity, replication, reactor characterization, and data normalization.

--- Step 0: Boundary recheck ---
All quotes from V1, V2, V3 were verified to fall within the target paper (pages 1–9 of a single-paper PDF). No boundary violations detected. No [?boundary] flags required.

---

[A] A-1 | P6:Rcol:20-35* | [REDACTED: substantial verbatim quotation; see Tier 9] | deferral_type: deferred | mixed_detail: n/a | reason_inferred: T1 (paper explicitly labels the claim as speculation) | linked_to: B-13, B-16, U-2 | cross_field_temperature: V1=medium, V2=high; convergence=2/3; temperature_gap=low

[A] A-2 | P6:Lcol:1-20* | [REDACTED: substantial verbatim quotation; see Tier 9] [followed by report of leaching at 30°C labeled "rather unexpected[REDACTED: substantial verbatim quotation; see Tier 9]rather unexpected"), (2) invoke the established Scheme 2 mechanism without modification, and (3) do not return to explain the 70°C discrepancy. All three suppression criteria met. | reason_inferred: T1 | linked_to: B-12, U-4 | cross_field_temperature: V2=high; convergence=1/3; temperature_gap: n/a (single agent)

[A] A-3 | P6:Lcol:25-35* | [REDACTED: substantial verbatim quotation; see Tier 9] | deferral_type: deferred | mixed_detail: n/a | reason_inferred: T1 (paper explicitly frames the contrast as "interesting" but takes no further experimental action) | linked_to: C-5 | cross_field_temperature: V2=medium; convergence=1/3; temperature_gap: n/a

[A] A-4 | P7:Lcol:20-30* | [REDACTED: substantial verbatim quotation; see Tier 9] | deferral_type: deferred | mixed_detail: n/a | reason_inferred: T1 (explicit future-work statement) | linked_to: A-1, B-8 | cross_field_temperature: n/a

---

[B] B-1 | P4:Lcol:1-8* | [REDACTED: substantial verbatim quotation; see Tier 9] | classification: reporting_omission | rhetorical_function: Positive framing of cross-catalyst comparability based on equal Pd mass normalization. | note: The three catalysts have different Pd weight loadings, particle sizes, dispersions, and surface areas; normalizing by total Pd mass does not equate the number of exposed (leachable) surface Pd sites. No batch-specific characterization data (BET, TEM, CO chemisorption, XPS) are reported. Standard practice in heterogeneous catalysis would require reporting Pd dispersion or surface area for cross-catalyst comparisons. | cross_field_temperature: V1=high; convergence=1/3

[B] B-2 | P5:Rcol:1-12* | [REDACTED: substantial verbatim quotation; see Tier 9] | classification: methodological_limitation | rhetorical_function: Description of the experimental temperature-ramp protocol used in all configuration 2 experiments. | note: Sequential 30→90°C protocol within a single run means the catalyst surface state (Pd oxidation state, loading, coordination environment) at the start of the 90°C phase is not equivalent to a freshly loaded catalyst at 90°C. The 30°C phase — particularly when NEt3 is in F1 — would reduce Pd(OAc)2 to Pd(0) via Scheme 2, fundamentally changing the surface Pd speciation before the 90°C phase begins. The paper presents each temperature phase as an independent measurement without acknowledging this carryover. [sequential protocol confounding check triggered] | cross_field_temperature: V1=high, V2=medium; convergence=2/3; temperature_gap=low

[B] B-3 | P5:Rcol:1-7* | [REDACTED: substantial verbatim quotation; see Tier 9] | classification: reporting_omission | rhetorical_function: Introduction of the four component-leaching experiments for PdEnCat 30. | note: The paper does not state whether a fresh catalyst bed was packed for each of the four component experiments (A: DMF; B: acrylate; C: PhI; D: NEt3). If the same bed was used sequentially, cumulative leaching and surface modification from earlier runs would confound results from later runs — particularly the NEt3 experiment (D), which shows the highest leaching. This is a critical reporting omission because the paper's central component-attribution claim depends on the independence of the four experiments. See also U-1. | cross_field_temperature: V1=critical, V3=critical; convergence=2/3; temperature_gap=none

[B] B-4 | P5:Lcol:5-15* | [REDACTED: substantial verbatim quotation; see Tier 9] | classification: reporting_omission | rhetorical_function: Description of the component-isolation protocol used in configuration 2. | note: The concentrations of each component in F1 and F2 streams are not reported in the main text; it is unclear whether the component concentration at the catalyst surface in F1 reproduces the concentration in the full reaction mixture. If F1 delivers a diluted or concentrated solution, the component-specific leaching attribution may not translate to actual reaction conditions. | cross_field_temperature: V1=high, V3=high; convergence=2/3; temperature_gap=none

[B] B-5 | P6:Rcol:1-10* + Figure 9B caption | [REDACTED: substantial verbatim quotation; see Tier 9] [Pd/Al2O3 + NEt3] | classification: reporting_omission | rhetorical_function: Quantitative evidence supporting the claim that Pd/Al2O3 is completely stable toward triethylamine. | note: No ICP–MS detection limit, analytical uncertainty (±ppm), or blank/baseline Pd value is reported in the main text. The claim of "complete stability" is based on a 6 ppm reading that may be at or near the detection limit of the method. Standard analytical reporting requires detection limit and measurement uncertainty alongside quantitative claims. | cross_field_temperature: V1=medium, V3=high; convergence=2/3; temperature_gap=low

[B] B-6 | P4:Lcol:1-8* | [REDACTED: substantial verbatim quotation; see Tier 9] | classification: reporting_omission | rhetorical_function: Justification for cross-catalyst ICP comparison based on equal initial Pd loading. | note: Total Pd mass balance is not reported: the paper does not account for Pd remaining on the catalyst after each experiment, Pd deposited in reactor tubing or PFR walls, or Pd in wash fractions. The reported ppm values represent only the Pd in collected liquid fractions; without mass balance, the ICP values underestimate total leaching and cannot be used for quantitative cross-catalyst comparison. [metric incompleteness flag] | cross_field_temperature: V1=medium, V3=high; convergence=2/3; temperature_gap=low

[B] B-7 | P5:Rcol:15-25* | [REDACTED: substantial verbatim quotation; see Tier 9] | classification: reporting_omission | rhetorical_function: Conclusion isolating DMF and methyl acrylate as non-leaching agents, used as baseline for subsequent component attributions. | note: All configuration 2 experiments use DMF as solvent carrier in F1. Experiment A (DMF alone) yields 30 ppm baseline leaching. This DMF-background contribution is not subtracted from the PhI (65 ppm) or NEt3 (182 ppm) values. Without background correction, the component-specific values are slightly inflated; more importantly, the paper presents these as if the 30 ppm baseline is negligible, but this assumption is not stated or justified.

[B] B-8 | P2:Lcol:1-15* | [REDACTED: substantial verbatim quotation; see Tier 9] | classification: intentional_narrowing | rhetorical_function: Summary of the quantitative capability demonstrated in the authors' earlier paper (ref 28) for PdEnCat 30. | note: The multiscale modeling framework from ref 28 is not applied to FC-1001 or Pd/Al2O3 in this paper. For both new catalysts, the hetero/homogeneous TOF partition remains qualitative (S1 vs. S2 conversion profiles). The paper does not acknowledge this as a narrowing; the model could in principle be applied to the new data. | linked_to: A-4

[B] B-9 | P7:Lcol:10-25* | [REDACTED: substantial verbatim quotation; see Tier 9] | classification: methodological_limitation | rhetorical_function: Affirmative claim that boomerang catalysis and halide-induced leaching are not operative under the flow conditions used. | note: The assertion that Pd cannot redeposit under single-pass flow is a logical inference, not a tested proposition. No residence-time data or spiking experiment is cited. The claim is necessary to validate the quantitative use of ICP data as a proxy for irreversible leaching, but its evidentiary basis is "not stated in paper." | cross_field_temperature: V1=medium, V2=medium; convergence=2/3; temperature_gap=none

[B] B-10 | P3:Rcol:1-15* | [REDACTED: substantial verbatim quotation; see Tier 9] | classification: intentional_narrowing | rhetorical_function: Observation that FC-1001 shows anomalously higher activity in dioxane/toluene compared to the other two catalysts, noted during preliminary batch screening. | note: The paper does not follow up with flow-reactor leaching experiments for FC-1001 in non-polar solvents. Whether this activity proceeds via heterogeneous or leached species is not investigated. The paper implicitly narrowed detailed flow studies to DMF without explicitly acknowledging that this leaves FC-1001's non-polar solvent behavior unexplained.

[B] B-11 | P4:Rcol:20-35* | [REDACTED: substantial verbatim quotation; see Tier 9] | classification: reporting_omission | rhetorical_function: Description of the Pd surface state in Pd/Al2O3 used to contextualize its leaching behavior. | note: The paper states Pd/Al2O3 has a "thin layer of PdO" but provides no characterization data for the specific batch used (XPS, XANES, or TEM). The PdO surface description is likely adopted from general literature about commercial Pd/Al2O3 rather than verified for this batch. This characterization gap directly bears on the mechanistic speculations invoking ArI oxidative addition to surface Pd atoms. See also U-2. | cross_field_temperature: V2=high; convergence=1/3

[B] B-12 | P2:Rcol:10-20* | [REDACTED: substantial verbatim quotation; see Tier 9] | classification: reporting_omission | rhetorical_function: Structural description of the FC-1001 catalyst introduced for comparison. | note: The paper applies Scheme 2 (α-hydride elimination mechanism for bare Pd(OAc)2) to explain FC-1001 leaching, without addressing how the phosphine ligand on FC-1001 modifies the Pd(II) center and whether the mechanism remains operative with a coordinated phosphine. The mechanistic equivalence between PdEnCat and FC-1001 is assumed without justification. | linked_to: A-2

[B] B-13 | P6:Rcol:1-10* | [REDACTED: substantial verbatim quotation; see Tier 9] | classification: reporting_omission | rhetorical_function: Mechanistic inference about the chemical identity of leached Pd species from FC-1001 based on deactivation kinetics. | note: Two distinct reporting omissions: (1) the inference of chemically different species from different deactivation kinetic profiles is confounded by the large difference in initial Pd concentrations (176 vs. 555 ppm at 30°C; ~307 vs. ~380 ppm at 90°C) — concentration-dependent agglomeration rate alone could explain the kinetic difference without invoking chemical distinction; (2) the Pd(0)·NEt3 stabilization inference lacks spectroscopic or stoichiometric evidence. [negative result as evidence flag — different deactivation rate used to infer different species identity] | linked_to: A-1, B-15, B-16

[B] B-14 | P3:Rcol:20-30* | [REDACTED: substantial verbatim quotation; see Tier 9] | classification: mixed | rhetorical_function: Mechanistic interpretation of DMF's role, supported by literature analogy. | note: mixed — intentional_narrowing (the paper chooses the DMF-as-passive-stabilizer interpretation without testing the alternative that DMF participates in a cooperative redox step with NEt3 or PhI) AND reporting_omission (refs 45–48 demonstrate DMF-stabilized Pd clusters in DMF-only or stoichiometric systems; no experiment in the current system directly tests DMF stabilization under leaching conditions). | linked_to: C-2

[B] B-15 | P6:Lcol:30-40* | [REDACTED: substantial verbatim quotation; see Tier 9] | classification: reporting_omission | rhetorical_function: Kinetic comparison between PhI- and NEt3-induced leached species from FC-1001 used as evidence for chemically distinct species. | note: The deactivation kinetics comparison (steeper vs. gentler decline) is not normalized for initial Pd concentration, which differs substantially between the two experiments. Without concentration normalization or kinetic modeling, the observed difference in deactivation rate does not unambiguously indicate chemically distinct species. | linked_to: B-13

[B] B-16 | P7:Lcol:1-12* | [REDACTED: substantial verbatim quotation; see Tier 9] | classification: reporting_omission | rhetorical_function: Summary conclusion statement asserting NEt3 as primary leaching agent for polymer-supported catalysts with no PBR-level catalytic turnover. | note: The phrase "in the absence of catalytic turnover" is ambiguous: it likely refers specifically to the PBR at T1=30°C (no PBR-level conversion), not to the entire system. Figures 7D and 8B (blue curves, 30°C phase) show non-zero conversion at the PFR outlet (T2=110°C), indicating that NEt3-leached Pd IS catalytically active when it reaches 110°C. The conclusions text does not clarify this distinction, creating an apparent contradiction with the figure data.

[B] B-17 | P3:Lcol:1-10* | [REDACTED: substantial verbatim quotation; see Tier 9] | classification: reporting_omission | rhetorical_function: Description of the analytical monitoring protocol, characterizing the overall experimental methodology. | note: No replicate experiments are reported for any experiment in the paper (batch or flow). All conversion profiles (Figures 3–9) and all ICP–MS values appear to be single-run data. Run-to-run reproducibility is not stated or characterized. Quantitative comparisons between catalysts and between components cannot be statistically evaluated without replicate data or stated uncertainty. Systematic reporting omission across the entire dataset. | cross_field_temperature: V3=high; convergence=1/3

[B] B-18 | P7:Lcol:30-35* | "breakthrough curves (PDF)" [ESI reference] | classification: reporting_omission | rhetorical_function: Reference to ESI content containing reactor characterization data. | note: Breakthrough curves are relegated to ESI (experiment performed, data exist) without any main-text discussion. These curves are essential for confirming steady-state conditions before sampling, plug-flow behavior in the PFR, and completion of the 30→90°C temperature transition before 90°C-phase samples were collected. The absence of main-text discussion means these foundational reactor characterization data are effectively invisible to readers evaluating the claims. [ESI delegation — data exist but not discussed in main text]

[B] B-19 | P2:Lcol:1-8* | [REDACTED: substantial verbatim quotation; see Tier 9] | classification: reporting_omission | rhetorical_function: Conceptual introduction of the tandem reactor measurement principle. | note: Flow rates, PBR volume, PFR volume, and resulting residence times are not stated in the main text. These parameters govern both the S1 vs. S2 conversion comparison (space velocity determines whether S1 conversion includes leached-Pd contributions) and the absolute ICP values (different residence times yield different total eluent volumes per unit time). Likely deferred to ESI but not acknowledged in main text.

[B] B-20 | P5:Lcol:5-15* | [REDACTED: substantial verbatim quotation; see Tier 9] | classification: reporting_omission | rhetorical_function: Description of the F2 mixing junction in configuration 2. | note: Mixing volume, geometry, and effectiveness at the F2 junction are not described. Incomplete mixing at F2 would yield non-homogeneous reagent concentrations entering the PFR, producing conversion data that underestimates catalytic activity of the leached Pd. Standard flow reactor design reporting should include mixing characterization.

[B] B-21 | P5:Rcol:1-12* | [REDACTED: substantial verbatim quotation; see Tier 9] | classification: reporting_omission | rhetorical_function: Statement of the ICP–MS analysis procedure for collected fractions in configuration 2 experiments. | note: Total collection volume, collection time window, and normalization basis (per mL, per hour, per mmol reagent) are not stated. The ppm values from configuration 2 experiments are directly compared with ppm values from configuration 1 experiments (B-3, U-3) without normalization; different reactor configurations likely produce different total eluent volumes per unit time. ESI Table S1 mentioned but normalization basis not clarified.

[B] B-22 | P3:Rcol:15-28* | [REDACTED: substantial verbatim quotation; see Tier 9] | classification: reporting_omission | rhetorical_function: Observation linking colored solution to colloidal Pd/Pd black formation as evidence of leaching and deactivation. | note: The paper uses HPLC to determine conversion in the same DMF runs that show visible colloidal Pd and Pd black. Colloidal Pd can absorb UV light and adsorb organics, potentially affecting HPLC peak areas and detector response. No HPLC method validation data (calibration curves, recovery experiments with Pd-containing mixtures) are reported to confirm accuracy of conversion values in the presence of heterogeneous Pd particles.

---

[C] C-1 | P2:Lcol:15-25* | ref 29 (Bourouina, Meille, de Bellefon, J. Flow Chem. 2018, 8, 117) | textual_function: Cited as contemporaneous split-flow work concluding Suzuki reactions via [REDACTED: verbatim source text; see the source paper via its DOI]." | reason_severed: The current paper's findings (catalytic turnover closely associated with leached species) align qualitatively with ref 29 but no quantitative comparison (leached Pd fraction, TOF ratio, catalyst loading) is made; different reaction type, substrate, and support are not acknowledged as barriers to direct comparison. | affects_claims: medium — the paper's claim that leached species dominate catalysis is supported by ref 29's analogous conclusion, but without quantitative comparison the support remains anecdotal. | symmetric_pattern: no

[C] C-2 | P3:Rcol:20-30* | refs 45–48 (Yano et al. 2013; Ishida et al. 2020; Nagata et al. 2019; Onishi et al. 2018 — DMF-stabilized Pd nanoclusters) | textual_function: Cited as group to support the claim that DMF stabilizes Pd nanoclusters active in cross-coupling; invoked as mechanistic explanation for why DMF amplifies leached-Pd catalytic activity. | reason_severed: All four refs demonstrate DMF-stabilized Pd clusters in DMF-only or stoichiometric systems; none involve packed-bed flow leaching conditions with NEt3 or ArI. No experiment in the current paper directly tests whether leached Pd forms nanoclusters stabilized by DMF. | affects_claims: yes — the mechanistic explanation for DMF's role depends entirely on analogy to refs 45–48 without in-system verification. | symmetric_pattern: yes (all four refs serve identical rhetorical function: analogy support for DMF stabilization)

[C] C-3 | P1:Rcol:15-30* | refs 18–19 (Thathagar et al. Angew. Chem. 2006; Gaikwad et al. Chem.–Eur. J. 2007 — Rothenberg nanofiltration) | textual_function: Cited as early examples of in situ leaching detection using nanofiltration membranes; noted as "effective in detecting leached Pd" but limited because catalytic activity of leached species cannot be determined. | reason_severed: Cited as methodological background to contrast with the tandem-flow approach; no data from refs 18–19 is quantitatively compared against current findings. | affects_claims: medium — the contrast motivates the paper's design but the comparison is qualitative and self-serving. | symmetric_pattern: yes (both refs cited together as alternative detection approach)

[C] C-4 | P2:Rcol:10-20* | ref 12 (Greco, Goessler, Cantillo, Kappe, ACS Catal. 2015, 5, 1303) | textual_function: Cited to introduce FC-1001 in a flow Heck reaction context; reports leaching "detected at 100°C in acetonitrile" and notes the authors [REDACTED: substantial verbatim quotation; see Tier 9] | reason_severed: The current paper uses FC-1001 under different conditions (NEt3 base, DMF solvent, iodobenzene) and finds leaching at 30°C, directly contradicting ref 12's implicit assumption. No direct comparison of leaching onset temperatures, amounts, or reaction outcomes is made. [Dropped Quantitative Benchmark — specific temperature of leaching detection cited in introduction but not compared against current FC-1001 results in Discussion] | affects_claims: medium — direct comparison would strengthen the paper's claim that NEt3 dramatically lowers the leaching onset temperature for FC-1001. | symmetric_pattern: no

[C] C-5 | P6:Lcol:25-35* | ref 23 (Newton, Ferri, et al. Catal. Sci. Technol. 2020, 10, 466) | textual_function: Cited as prior work showing K2CO3/ethanol causes leaching from Pd/Al2O3 under mild conditions via attack on the alumina support, contrasted with current finding that NEt3 does NOT cause leaching from Pd/Al2O3. | reason_severed: The contrast is noted as "interesting" but not experimentally probed: no experiment varies base type (organic vs. inorganic) at fixed solvent, or solvent (ethanol vs. DMF) at fixed base, to identify which variable is responsible. | affects_claims: medium — the mechanistic conclusion that base identity (organic vs. inorganic) determines Pd/Al2O3 leaching depends on an unverified variable substitution. | linked_to: A-3 | symmetric_pattern: no

---

[U] U-1 | P5:Rcol:1-7* | [REDACTED: substantial verbatim quotation; see Tier 9] | question: Was a fresh catalyst bed used for each of the four component experiments? If not, cumulative leaching from earlier experiments would confound the component attribution that is the paper's central contribution. | originating_agent: V1 (critical), V3 (critical) | severity: critical | note: self-contradictory absence — the paper's central claim (component-by-component attribution of leaching) requires the four experiments to be independent. If the same catalyst bed was reused in sequence, the claim cannot be evaluated. The paper's narrative describes 4 "experiments" but does not state independence. This is not merely a reporting omission (B-3) — it is a potential internal contradiction where the paper's evidence structure would collapse if beds were not refreshed.

[U] U-2 | P4:Rcol:20-35* | [REDACTED: substantial verbatim quotation; see Tier 9] | question: If the Pd/Al2O3 surface consists of PdO (Pd(II)), how does ArI cause leaching via oxidative addition, which requires Pd(0)? | originating_agent: V2 (high) | severity: high | note: self-contradictory absence — the paper's own catalyst description (PdO surface layer) is inconsistent with the invoked leaching mechanism (oxidative addition of ArI to Pd(0)). Computational refs 54–55 model Pd(0) nanoparticle leaching but do not address PdO-terminated surfaces. The mechanism predicts that a prior reduction step (PdO → Pd(0)) must occur before ArI oxidative addition, but this step is neither mentioned nor evidenced in the paper. This absence is not acknowledged.

[U] U-3 | P6:Lcol:1-12* | [REDACTED: substantial verbatim quotation; see Tier 9] | question: Are the ICP–MS ppm values from configuration 2 (Figure 7D) and configuration 1 (Figure 4B) normalized on the same basis (same collection volume, same total eluent, same reactor geometry)? | originating_agent: V3 (high) | severity: high | note: self-contradictory absence — the paper's strongest quantitative conclusion ("NEt3 is the biggest culprit") rests on a direct numerical comparison (182 vs. 194 ppm) between experiments run on different reactor configurations (config 1 has no F2 inlet; config 2 has two feed pumps and different total flow). The paper's own experimental description predicts that total eluent volume and flow profile may differ between configurations, yet the ppm comparison is made without any normalization statement or acknowledgment of this potential inconsistency.

[U] U-4 | P6:Lcol:1-20* | [REDACTED: substantial verbatim quotation; see Tier 9] | question: What mechanistic modification to the α-hydride elimination pathway would be necessary to explain leaching at 30°C from PdEnCat, when the same pathway is documented only at ≥100°C for comparable Pd(II) systems? | originating_agent: V2 (high) | severity: high | note: self-contradictory absence — the paper's proposed mechanism (Scheme 2, α-hydride elimination) predicts that leaching at 30°C should be minimal or absent (mechanism known to require ~100°C). The paper reports 182 ppm leaching at 30°C and labels this "rather unexpected" but does not resolve the contradiction. The absence of mechanistic explanation for the 70°C temperature discrepancy means the paper's mechanistic account is internally incomplete. This is not merely an A (deferred) item because the paper both invokes the mechanism AND notes it is inconsistent with the observation.

---

[META]
  linked_items:
    - A-1 ↔ B-13 (leached species speculation explicitly acknowledged; B-13 notes missing evidence for inference)
    - A-1 ↔ B-15 (deactivation kinetics used as sole evidence for species identity)
    - A-1 ↔ U-2 (PdO/Pd(0) contradiction bears on species identity speculation)
    - A-2 ↔ U-4 (A-2 is the suppressed deferral of the temperature paradox; U-4 is the self-contradictory mechanistic absence)
    - A-2 ↔ B-12 (phosphine effect on Scheme 2 is the within-mechanism extension of the temperature paradox)
    - A-3 ↔ C-5 (A-3 defers the NEt3 vs. K2CO3 comparison; C-5 notes ref 23 was not experimentally interrogated)
    - A-4 ↔ B-8 (future design statement not backed by quantitative TOF analysis for new catalysts)
    - B-3 ↔ U-1 (same underlying absent datum: fresh catalyst bed question)
    - B-11 ↔ U-2 (catalyst surface characterization gap feeds into mechanism contradiction)
    - B-14 ↔ C-2 (B-14 flags DMF mechanism as mixed omission; C-2 identifies the uncontinued citation basis for that claim)
    - B-13 ↔ B-15 ↔ B-16 (three B items derive from the same kinetic-inference-without-normalization problem for FC-1001)
    - U-3 ↔ B-21 (ICP normalization omission enables the invalid cross-configuration comparison)
    - B-2 ↔ U-4 (sequential protocol confounding is compounded by the mechanistic prediction that 30°C phase changes Pd surface speciation before 90°C phase)

  same_root_groups:
    - SRG-1 [Component attribution experimental independence]: B-3, U-1, B-2, B-7
      shared root: All derive from the absence of data confirming that the four component-leaching experiments are mutually independent (fresh catalyst beds, no sequential carryover, no DMF background subtraction).
    - SRG-2 [Quantitative Pd leaching data validity]: B-5, B-6, B-17, B-21, U-3
      shared root: All derive from the absence of standard analytical validation data (replicates, detection limits, mass balance, collection normalization) required to evaluate the quantitative ICP claims.
    - SRG-3 [Reactor characterization absent from main text]: B-18, B-19, B-20, B-4
      shared root: All derive from the absence of key reactor design and operating parameters (flow rates, residence times, F2 mixing, component concentrations) that are prerequisites for interpreting the conversion and ICP data.
    - SRG-4 [Leached species identity — mechanism vs. evidence]: A-1, B-11, B-13, B-15, U-2
      shared root: All derive from the absence of spectroscopic or structural characterization of leached Pd species; the paper's mechanistic inferences about species identity rest entirely on kinetic/conversion profiles.
    - SRG-5 [α-hydride elimination mechanism — applicability and temperature paradox]: A-2, B-12, U-4
      shared root: All derive from the paper invoking Scheme 2 without verifying its applicability to (a) 30°C conditions and (b) phosphine-coordinated FC-1001.

  symmetric_citations:
    - C-2 (refs 45–48, DMF nanocluster stabilization — all serve identical rhetorical function as analogy support)
    - C-3 (refs 18–19, Rothenberg nanofiltration — both cited as contrasting background methodology)

  unreported_data:
    - Breakthrough curves: exist in ESI, not discussed in main text (B-18)
    - Flow rates, PBR/PFR volumes, residence times: likely in ESI, not in main text (B-19)
    - ICP–MS Table S1 with precise values: mentioned, deferred to ESI (B-21)
    - Figure S3 (colored solution photographs): deferred to ESI (B-22)
    - Batch aliquot quenching protocol: deferred to ESI experimental methods

  series_signal: yes [T1] — The paper explicitly builds on ref 28 (own prior paper, same reactor system, same reaction) and states findings will "guide future catalyst design and optimization"; this is the second paper in an ongoing research program on in-flow Pd leaching (A-4).

---

[TEMPERATURE_SUMMARY]
  high_convergence_high_gap: [] (empty — as expected; no convergent items show temperature_gap > low)

  high_convergence_low_gap:
    - B-3/U-1 (V1=critical, V3=critical; convergence=2/3; gap=none)
    - B-4 (V1=high, V3=high; convergence=2/3; gap=none)
    - B-9 (V1=medium, V2=medium; convergence=2/3; gap=none)
    - B-2 (V1=high, V2=medium; convergence=2/3; gap=low)
    - A-1 (V1=medium, V2=high; convergence=2/3; gap=low)
    - B-5 (V1=medium, V3=high; convergence=2/3; gap=low)
    - B-6 (V1=medium, V3=high; convergence=2/3; gap=low)

  low_convergence_high_gap:
    - A-2/U-4 (V2=high, single agent — unexplained temperature paradox in central mechanism)
    - U-2 (V2=high, single agent — PdO/Pd(0) self-contradiction in Pd/Al2O3 mechanism)
    - U-3 (V3=high, single agent — cross-configuration ICP comparison without normalization underpins key conclusion)
    - B-17 (V3=high, single agent — no replicates across entire dataset)

---

[GAP]
GAP-1 | type 1 | priority: high | description: Ref 28 (Barreiro et al., Catal. Today 2018) — the authors' multiscale model for deconvoluting hetero/homogeneous TOF was applied only to PdEnCat 30; retrieving ref 28 would clarify whether the model parameters could be extended to FC-1001 and Pd/Al2O3, and what quantitative TOF ratios those catalysts would yield. | candidate_paper: Barreiro E.M. et al., Catal. Today 2018, 308, 64–70 | inference_label: T1 | status: pending

GAP-2 | type 3 | priority: high | description: Papers spectroscopically characterizing leached Pd species from heterogeneous Pd catalysts under flow Heck conditions. The paper defers species identification as speculation (A-1, U-2); operando EXAFS or ESI-MS studies of collected fractions would resolve both the cluster vs. molecular species question and the PdO/Pd(0) surface mechanism question. | candidate_paper: Reimann et al., J. Am. Chem. Soc. 2011, 133, 3921 (in-situ quick-scanning EXAFS of leached Pd, ref 20) | inference_label: T2 | status: pending

GAP-3 | type 3 | priority: medium | description: Papers investigating α-hydride elimination kinetics from Pd(OAc)2 with trialkyl amines at sub-50°C temperatures, or from encapsulated/immobilized Pd(II) systems. Would resolve A-2/U-4 regarding unexpected 30°C leaching from PdEnCat via Scheme 2 pathway. | candidate_paper: Muzart J., J. Mol. Catal. A 2009, 308, 15 (ref 52, review of amine–Pd(0/II) interactions) | inference_label: T2 | status: pending

GAP-4 | type 2 | priority: medium | description: Köhler group studies (refs 13–17) on leaching mechanisms for Pd nanoparticles in Heck reactions, cited in introduction for context but never directly compared against the current component-isolation findings. Systematic engagement with these studies would place the component-attribution findings in quantitative context with prior Pd/C and Pd/support leaching data. | candidate_paper: Gnad et al., ACS Catal. 2020, 10, 6030 (ref 15 — leaching mechanism for aryl bromides/chlorides) | inference_label: T2 | status: pending

inference_time_sec: not available — inject externally
```

---

> **Tier 8 redaction notice**: This file is a redacted copy of the corresponding Tier 3 / Tier 9 output. Verbatim source-paper quotations have been replaced by `[REDACTED: see source paper §<loc>; full text retained in Tier 9 reviewer-only deposit]` markers, preserving location references and our own analytical content. Bibliographic fields (title, authors, journal, year, DOI), analytical labels (`evidence_chain:` with B-/U-/A-/C- internal IDs), short technical terms, and our own analytical text are not redacted. The redaction was applied by `scripts/redact_for_tier8.py` and, for this version, by `scripts/build_paperA_R1_public.py` with `scripts/redact_source_ngram_runs.py` (scripts of the project repository; they are not deposited).
