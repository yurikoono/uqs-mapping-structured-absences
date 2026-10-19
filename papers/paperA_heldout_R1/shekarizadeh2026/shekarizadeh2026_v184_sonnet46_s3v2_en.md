prompt_version: stage3-v2-en-20260419
model_info: claude-sonnet-4-6

# Re-certification Assessment Sheet for Scientific Knowledge

## Shekarizadeh, Azadi, Sohrabifard, Mirzajani 2026 (Journal of Saudi Chemical Society, full paper)

### §1 Claim Architecture

**Core claim:** This paper claims that a nitrogen-rich triazine tridentate linker in a graphene oxide framework (GOF2) provides more N-donor coordination sites than a benzene-amide linker (GOF1), yielding a 60× higher Pd loading (31.92 vs 0.532 wt%), and that this differential N-Pd coordination — not merely loading volume or particle size — is the mechanistic origin of GOF2's superior Heck-Mizoroki activity (TOF = 39.2 vs 9.5 h⁻¹ for bromobenzene/styrene at 80 °C). The **Novelty pillar** is the deliberate linker-heteroatom-density comparison as a design principle for supported Pd nanoreactors; the **Utility pillar** is eco-friendly (H₂O/EtOH) recyclable (5 cycles) C-C coupling with TOF superior to prior literature systems.

**Layered structure:** Four independent layers exist (see Stage 2 D-1): Layer 1 — synthesis and structural characterization of GOF1/GOF2; Layer 2 — Pd immobilization and compositional characterization; Layer 3 — catalytic performance comparison (yield, TOF, substrate scope); Layer 4 — stability/reusability. These layers have an inter-layer dependency pattern: Layer 3's causal attribution (N-coordination → enhanced TOF) requires Layer 2 data (N-Pd coordination confirmed, equal-loading comparison), which is where the fatal gap lies. Refutation of Layer 3's causal claim does not collapse Layers 1, 2, or 4 independently. The paper does NOT collapse to a single refutation point: the synthesis of two linker-distinct GOF platforms (Layer 1) and the 5-cycle recyclability demonstration (Layer 4) are independent contributions that survive the TOF attribution failure.

---

### §2 SRG / CLA → RI / ER / EP Crosswalk

**SRG-1 [Pd active-site quantification and cross-system comparability]** (B-8, U-2, C-2, B-15)

* **Primary RI**: RI-01 [Reporting integrity]
* **Secondary RI**: RI-09 [External superiority]
* **ER**: The GOF1 vs GOF2 activity comparison requires that both systems be evaluated at equal Pd mol% (or, if mol% differs, that a loading-response curve be established for each), and that TOF be normalized by active-site count (surface Pd, from CO chemisorption or equivalent). The Table 8 external comparison additionally requires direct measurement under identical conditions rather than literature-harvested values at different temperatures and loadings.
* **EP**: EP-01a (Reporting-coherence pack); EP-09a (Internal benchmark pack)
* **Case-specific implementation**: (a) Run GOF1 and GOF2 at matched Pd mol% (e.g., 0.05 mol% for both) in the standard H₂O/EtOH/K₂CO₃/80 °C system for bromobenzene + styrene; measure yield and TOF at identical time points. (b) Perform CO pulse chemisorption on both catalysts to determine surface-Pd dispersion and re-calculate TOF on a per-surface-Pd-atom basis. (c) Add ref [12] bipyridine-GOF to Table 8 at matched mol%.
* **Notes**: B-8 (3/3 convergence, gap=none; rated high by all three agents); U-2 (high severity, 3/3 convergence — comparability prerequisite-absence). Appears in TEMPERATURE_SUMMARY high_convergence_low_gap. C-2 and B-15 extend the RI-09 dimension. SRG-7 (B-13, U-2) overlaps on U-2, reflecting that N-Pd coordination is both the unverified causal agent (SRG-7/RI-03) and the confounded variable in the performance comparison (SRG-1/RI-01).

---

**SRG-2 [Textural characterization of actual catalysts]** (B-2, B-7)

* **Primary RI**: RI-01 [Reporting integrity]
* **Secondary RI**: RI-05 [Qualitative overread]
* **ER**: The mesopore diffusion argument — invoked to explain substrate accessibility in GOF2 despite its smaller pore diameter — requires BET surface area, pore volume, and BJH pore size data for Pd@GOF2 (not only for GOF2 before Pd loading), and requires explicit statement of the pore geometry model used in BJH analysis.
* **EP**: EP-01a (Reporting-coherence pack); EP-05a (Quantitative-ranking substantiation pack)
* **Case-specific implementation**: Measure N₂ physisorption isotherms (77 K) on the actual Pd@GOF1 and Pd@GOF2 catalysts; fit BET to the linear range (P/P₀ = 0.05–0.30); apply BJH to the adsorption branch with cylindrical pore geometry; report BET area, total pore volume, and mean BJH pore diameter before and after Pd loading.
* **Notes**: B-2 (2/3 convergence, gap=none; V1=high, V3=high). B-7 secondary (medium, V3-Q4). The "completely overrides pore dimensions" assertion (B-14) is an RI-05 instance (qualitative overread) co-occurring with this SRG.

---

**SRG-3 [AAS methodology and detection limit]** (B-3)

* **Primary RI**: RI-04 [Unreplicated discriminator]
* **Secondary RI**: RI-01 [Reporting integrity]
* **ER**: The hot filtration test conclusion ("no detectable amounts of palladium had leached") constitutes a single negative measurement interpreted as positive mechanistic evidence for heterogeneous catalysis; this requires reporting the AAS instrument detection limit, the calibration range used for the complex GOF-matrix digest, and the calculated upper bound on leached Pd compatible with the reported sensitivity.
* **EP**: EP-04a (Discrimination / replication pack); EP-01a (Reporting-coherence pack)
* **Case-specific implementation**: For the hot filtration AAS: report (a) calibration curve range (ppb) for Pd in the H₂O/EtOH matrix with GOF digest background, (b) instrument detection limit (IDL) and method detection limit (MDL), (c) dilution factor applied to the 31.92 wt%-Pd sample digest, and (d) the maximum homogeneous Pd concentration compatible with the IDL that would sustain the observed catalytic rate under the Heck conditions (back-calculate from known homogeneous Pd activity data for the same substrate).
* **Notes**: B-3 (3/3 convergence, gap=low; V1=high, V2=high, V3=medium — highest convergence among all SRGs). The gap=low reflects disciplinary asymmetry: analytical chemists (V3) rate the method reporting deficit as medium (standard practice in many subfields) while catalysis experts (V1, V2) rate AAS detection limit as essential for the mechanistic conclusion (high).

---

**SRG-4 [Statistical validity of quantitative claims]** (B-1, B-9)

* **Primary RI**: RI-08 [Unquantified reliability]
* **Secondary RI**: none
* **ER**: The yield and TOF values in Tables 3–7 require at minimum triplicate measurements with standard deviation, and quantitative reaction monitoring (GC-FID conversion at the TLC endpoint) to establish whether isolated yields reflect conversion efficiency or workup/chromatography losses.
* **EP**: EP-08a (Replication / uncertainty pack)
* **Case-specific implementation**: For the model substrate (bromobenzene + styrene, Table 3 optimized conditions), run three independent reactions for each catalyst and report mean yield ± SD. For a representative scope entry (one activated and one deactivated aryl bromide per catalyst), report GC conversion alongside isolated yield to close the mass balance.
* **Notes**: B-1 (2/3 convergence, gap=low; V1=high, V3=critical — the gap=low reflects genuine disciplinary disagreement: heterogeneous catalysis subfield practice routinely accepts single-point scope yields [V1], while analytical methodology requires replicates for quantitative comparison claims [V3]). B-9 (2/3 convergence, gap=none).

---

**SRG-5 [Particle size characterization methodology]** (B-4, B-5)

* **Primary RI**: RI-01 [Reporting integrity]
* **Secondary RI**: RI-05 [Qualitative overread]
* **ER**: The Scherrer equation application requires disclosure of: peak(s) used, instrument broadening correction (standard reference material), Scherrer K constant, and whether lattice strain was separated (Williamson-Hall). TEM particle size requires particle count, SD, and histogram. Without these, the XRD vs TEM comparison (described as "good agreement" despite ~1.2 nm discrepancy for GOF2) cannot be evaluated.
* **EP**: EP-01a (Reporting-coherence pack); EP-05a (Quantitative-ranking substantiation pack)
* **Case-specific implementation**: For XRD: report the Pd(111) peak (2θ ≈ 40°) FWHM, the LaB₆ standard instrumental broadening, K = 0.94 (standard for spherical particles), and either Williamson-Hall or single-peak analysis; for TEM: report particle count (≥150 particles) and SD for both fresh and recycled catalysts.
* **Notes**: B-4 (Scherrer, 2/3 convergence, gap=none — V1-Q8/V3-Q1). B-5 (TEM count absent, 2/3 convergence). The XRD vs TEM "good agreement" claim (RI-05) is non-fatal for the performance claims but undermines confidence in the particle size sintering interpretation (B-5 → Layer 4).

---

**SRG-6 [Mechanistic cycle evidence absent]** (U-1, U-3, B-11)

* **Primary RI**: RI-06 [Imported model]
* **Secondary RI**: RI-03 [Unobserved explanatory]; PRI-11 candidate [Mechanism–kinetics decoupling]
* **ER**: The Pd(0)/Pd(II) catalytic cycle proposed for the GOF-Pd/H₂O-EtOH system requires at minimum one line of experimental evidence in this system — such as a Hammett correlation across the substituent series, a radical probe experiment, or homo-coupling quantification — to demonstrate isomorphism with the imported literature mechanism.
* **EP**: EP-06a (Analogy-validation pack); EP-03a (Direct-observation / state-assignment pack)
* **Case-specific implementation**: (a) Plot ln(TOF) vs Hammett σ for the 8 electronically distinct aryl bromides in Table 5; a linear correlation with positive slope would support OA rate-determining step in Pd(0)/Pd(II) cycle. (b) Add TEMPO (2 equiv) to the optimized GOF2 reaction; persistence of activity would argue against radical chain mechanism. (c) Quantify homo-coupling (bibenzyl or 4-substituted biphenyls) by GC in the reaction mixture at 50% conversion.
* **Notes**: U-1 (medium, Pd-H not characterized), U-3 (medium, homo-coupling not measured — self-contradictory absence: the Pd(0)/Pd(II) cycle predicts homo-coupling as a competing pathway, but its absence is not reported). B-11 (2/3 convergence, gap=none). PRI-11 applies: the paper's mechanistic evidence (halide reactivity order I >> Br >> Cl) is qualitative agreement with rate trends, not an algebraically derived rate law. This paper provides an additional case for PRI-11 in a heterogeneous Pd nanoparticle system.

---

**SRG-7 [N-Pd coordination characterization gap]** (B-13, U-2)

* **Primary RI**: RI-03 [Unobserved explanatory]
* **Secondary RI**: RI-05 [Qualitative overread]
* **ER**: The mechanistic claim that N-Pd electronic donation is the operative driving force requires direct characterization of the Pd coordination environment in Pd@GOF1 and Pd@GOF2 — specifically a Pd 3d XPS binding energy shift between the two systems, or an EXAFS Pd–N coordination number and bond length — rather than inference from a single FT-IR band at ~530 cm⁻¹ with no intensity calibration.
* **EP**: EP-03a (Direct-observation / state-assignment pack); EP-05a (Quantitative-ranking substantiation pack)
* **Case-specific implementation**: Collect Pd 3d₅/₂ XPS spectra for Pd@GOF1 and Pd@GOF2 under identical conditions; report binding energy (eV) for both and Pd(0)/Pd(II) surface ratio by peak deconvolution. A lower Pd 3d₅/₂ BE in Pd@GOF2 relative to Pd@GOF1 would provide direct evidence for greater N→Pd electron donation. Alternatively, Pd K-edge EXAFS could provide Pd–N coordination number and bond length.
* **Notes**: B-13 (N-Pd FT-IR claim, 2/3 convergence, gap=none). U-2 here is its secondary role: the N-Pd coordination characterization gap (SRG-7) and the loading/particle-size confound (SRG-1) share U-2 as a common node because the absence of active-site quantification and the absence of N-Pd direct characterization are two sides of the same missing experiment (a matched-loading comparison with XPS/EXAFS).

---

Outside the SRGs: CLAs

**CLA-1 [EDS vs AAS Pd content discrepancy]** (B-6)

* **Primary RI**: RI-01 [Reporting integrity]
* **ER**: The 7× EDS/AAS discrepancy for Pd@GOF1 (3.65 vs 0.532 wt%) and the 1.3× discrepancy for Pd@GOF2 (41.72 vs 31.92 wt%) require reconciliation before the quantitative Pd loading claims can be accepted; the discrepancy reflects the EDS/AAS surface vs bulk sampling depth difference and matrix correction effects that are standard knowledge but unaddressed in the paper.
* **EP**: EP-01a (Reporting-coherence pack)
* **Case-specific implementation**: Provide ZAF correction parameters for the EDS Pd Lα line in the C/N/O-rich GOF matrix; state the probed depth (keV beam energy → interaction volume); explain that AAS (bulk digest) is the definitive loading value and that EDS surface enrichment of Pd in the 5–10 nm surface layer accounts for the over-reading.
* **Notes**: B-6 is not in any SRG. Directly bears on the core D-1 novelty claim (GOF2 achieves 31.92 wt% Pd vs GOF1's 0.532 wt%). Non-fatal at VQ-1 (AAS is used as the operative loading value for all calculations), but the unaddressed discrepancy weakens analytical credibility.

---

**CLA-2 [Homo-coupling byproducts absent — self-contradictory absence]** (B-10)

* **Primary RI**: RI-03 subtype [Unobserved explanatory — self-contradictory absence]
* **ER**: The Pd(0)/Pd(II) cycle (as drawn) generates aryl-Pd(II)-X intermediates that can undergo bimolecular reductive elimination to form homo-coupled biaryls; the absence of any homo-coupling quantification means that the paper's mass balance is incomplete and that one of the predicted pathway products is systematically unaccounted for.
* **EP**: EP-03a (Direct-observation / state-assignment pack)
* **Case-specific implementation**: For each aryl halide substrate in Tables 5 and 6, measure homo-coupling product (biaryl) yield by GC-FID; report in a supplementary mass-balance table; confirm that total carbon recovery (Heck product + homo-coupling + recovered starting material) ≥ 95%.
* **Notes**: B-10 corresponds to V2-Q6 (homo-coupling not reported). The catalytic cycle proposed explicitly predicts aryl-Pd(II)-X as an intermediate; the absence of homo-coupling data constitutes a self-contradictory absence exactly fitting the Stage 3 prompt §2 pattern check. Not captured by SRG-6 (which focused on the Pd-H intermediate and base mechanistic assignments) but extends the SRG-6/RI-06 domain.

---

### §3 Current VQ assessment

**Current judgment: VQ-1 (Observation)**

**VQ-1 [Observation] — holds (non-fatal RI-02 noted)**
The catalyst objects (Pd@GOF1, Pd@GOF2) are identified by complementary FT-IR (amide vs ester carbonyl), XRD (Pd fcc reflections), TEM (nanoparticle imaging), EDS, and AAS. The identity of the Heck products as E-stilbene derivatives is established for representative substrates by NMR and FT-IR in the SI. CLA-1 (EDS vs AAS discrepancy) introduces a non-fatal RI-02 note: quantitative Pd composition is uncertain at the EDS/AAS level, but the AAS value is used consistently for all catalytic calculations and the qualitative identity of the catalyst objects is not in doubt. VQ-1 holds.

**VQ-2 [Method] — fails (fatal RI-01 from SRG-1)**
On the premise that VQ-1 holds, VQ-2 requires RI-01 and RI-07 to be non-fatal. RI-01 from SRG-1 is fatal: the paper's core performance comparison (GOF1 TOF = 9.5 h⁻¹ vs GOF2 TOF = 39.2 h⁻¹) is conducted at non-equivalent Pd mol% (0.05 vs 0.3 mol%), making the direct cross-system TOF comparison non-isomolar. Without a matched-loading experiment, the TOF difference cannot be attributed to linker heteroatom density — it may reflect that 6× more total Pd simply converts more substrate in the same time window, not that per-site activity is higher. This is fatal for the paper's comparison method, which is the primary claim vehicle. RI-07 from SRG-3 (the hot filtration negative claim without detection limit) is non-fatal for VQ-2 — the hot filtration test provides a useful lower bound on leaching even without the quantified detection limit, and the recyclability data independently support catalyst retention.

**VQ-3 [Mechanism] — not reached (VQ-2 fails)**
Unresolved: RI-06 (SRG-6: Pd(0)/Pd(II) cycle imported without system validation), RI-03 (SRG-7: N-Pd coordination unobserved, CLA-2: homo-coupling not measured). These would remain independently unresolved even if VQ-2 were fixed.

**VQ-4 [Benchmark] — not reached (VQ-3 fails)**
Unresolved: RI-08 (SRG-4: no replicates for TOF comparison), RI-09 (SRG-1/B-15, C-2: Table 8 comparison at non-equivalent conditions; ref [12] bipyridine-GOF excluded from comparison table).

**Per-layer asymmetry (§1 layered structure):**
However, **Layer 1 (materials design and characterization of GOF1 vs GOF2 as linker-composition-distinct platforms)** on its own reaches VQ-2: the synthesis routes, FT-IR, XRD, TEM, BET, and TGA data for the GOF frameworks and their Pd-loaded derivatives are consistently reported with complementary techniques, and the qualitative claim (triazine linker accommodates more Pd than benzene linker) is supported at VQ-2 without requiring the equal-loading comparison.

However, **Layer 4 (5-cycle recyclability)** on its own reaches VQ-2: recyclability is demonstrated by independent yield measurements across 5 cycles plus post-cycle-5 AAS and TEM, with a self-consistent picture of low leaching and moderate sintering.

The paper as a whole is blocked at VQ-1 due to the fatal RI-01 in the cross-system comparison (Layer 3).

---

### §4 Era-Norm Annotation

**communication-era tolerated:**
- **B-1** (no replicates in scope tables): Single-point isolated yield reporting without standard deviation is near-universal in heterogeneous catalysis scope tables as of 2026 in mid-tier journals; the Journal of Saudi Chemical Society does not explicitly require replicate data in scope tables, and this omission is genre-norm consistent.
- **B-4** (Scherrer equation parameter undisclosed): In materials chemistry papers, applying the Scherrer equation without reporting the K constant, instrumental broadening correction, or strain separation is common practice in this journal class and across the subfield; reviewers rarely require full Williamson-Hall documentation.
- **B-7** (BJH pore geometry model not stated): The convention of reporting BJH pore diameters without specifying adsorption vs desorption branch or pore shape assumption is widespread in materials catalysis journals and not specifically addressed in the journal's author guidelines.
- **B-9** (TLC monitoring qualitative; mass balance absent): The use of TLC as the sole reaction monitoring tool with no GC conversion quantification is common in synthetic scope tables in the heterogeneous catalysis subfield; mass balance closure is not typically required.

**modern-era deficient:**
- **B-8** (non-equivalent mol% for the GOF1 vs GOF2 TOF comparison): As of 2026, high-impact heterogeneous catalysis journals require isomolar comparison conditions or loading-response curves before an intrinsic activity claim (per-site TOF) can be made; using 6× different Pd mol% and calling the result a "normalized intrinsic activity" is not defensible at VQ-2.
- **B-3** (AAS detection limit absent for the hot filtration negative evidence): Reporting "no detectable palladium" without the instrument detection limit in quantitative Pd loading studies is flagged in modern analytical chemistry guidelines (IUPAC) and in the heterogeneous catalysis literature as an incomplete negative result claim.
- **B-13** (N-Pd coordination claimed from a single IR band without calibration or complementary XPS/EXAFS): In 2026, mechanistic claims attributing rate enhancement to a specific metal-support electronic interaction require XPS or EXAFS characterization; IR band assignment alone no longer meets the standard for "direct evidence" in the heterogeneous catalysis community.
- **B-2** (BET of actual catalysts absent when Pd loading is 31.92 wt%): For catalysts with >30 wt% metal loading, post-loading textural characterization is expected in full papers that invoke pore diffusion arguments for activity rationalization.

**Dual classification (tolerated then, deficient now):**
- **B-8** straddles this boundary: non-equivalent loading comparisons were tolerably common in GOF-Pd literature before circa 2022–2023, when the subfield began demanding iso-molar TOF comparisons following broader adoption of CO chemisorption for Pd dispersion. By 2026, it is modern-era deficient.

---

### §5 Shortest-reinforcement route

**Shortest route to VQ-2:**

1. EP-01a [Reporting-coherence pack] — Conduct a matched-loading experiment: measure yield and TOF for both Pd@GOF1 and Pd@GOF2 at an equal Pd mol% (0.05 mol% each, using the GOF2 loading standard as the low reference) for bromobenzene + styrene under the optimized conditions, and report yield vs time profiles at ≥3 time points.
   Advances RI-01 (SRG-1, fatal blocker).

2. EP-07a [Boundary-test pack] — Report the AAS instrument detection limit and method detection limit for Pd in the H₂O/EtOH matrix, calculate the maximum leached Pd concentration compatible with the IDL, and compare this to a published homogeneous Pd catalyst activity reference at equivalent concentration to establish the upper bound on any homogeneous contribution.
   Advances RI-07 (SRG-3/B-3).

Certification-gate note: The experimental investment order follows information gain (matched-loading experiment first, since it advances the fatal RI-01 and simultaneously enables a fair RI-09 evaluation), but the final certification is fixed by the gate order VQ-1 → VQ-2 → VQ-3 → VQ-4.

---

**Shortest route to VQ-3 (prerequisite: VQ-2):**

3. EP-06a [Analogy-validation pack] — Validate the Pd(0)/Pd(II) mechanistic cycle in the GOF-Pd/H₂O-EtOH system by constructing a Hammett plot (ln(TOF) vs σ) across the 8 electronically diverse aryl bromides in Table 5; add a radical probe experiment (TEMPO, 2 equiv, under GOF2 optimized conditions) to distinguish radical chain from ionic mechanism; quantify homo-coupling (biaryl) by GC.
   Advances RI-06 (SRG-6) and RI-03 (CLA-2).

4. EP-03a [Direct-observation / state-assignment pack] — Collect Pd 3d XPS spectra on fresh Pd@GOF1 and Pd@GOF2; report Pd 3d₅/₂ binding energies and Pd(0)/Pd(II) surface ratios to directly characterize N→Pd electron donation as a function of linker N density.
   Advances RI-03 (SRG-7).

5. EP-08a [Replication / uncertainty pack] — Report triplicate measurements for the benchmark substrate (bromobenzene + styrene) for both GOF1 and GOF2 under the optimized conditions; establish whether the TOF difference survives statistical testing (mean ± SD, non-overlapping confidence intervals).
   Advances RI-08 (SRG-4).

---

**Shortest route to VQ-4 (prerequisite: VQ-3):**

6. EP-09a [Internal benchmark pack] — Construct an internal benchmark table that includes (a) GOF1 and GOF2 at matched mol% with CO chemisorption-derived surface-Pd counts for TON/TOF normalization, (b) the bipyridine-GOF from the authors' own ref [12] at the same mol% under identical conditions, and (c) the best-performing prior system (entry with highest reported TOF) directly re-run under the GOF1/GOF2 optimized conditions for a head-to-head measurement.
   Advances RI-09 (SRG-1/B-15, C-2).

7. EP-08a [Replication / uncertainty pack] — Extend replication to ≥3 runs per substrate for all scope entries; report mean ± SD and GC-FID conversion for each entry to enable statistical comparison between GOF1 and GOF2 substrate scope performance.
   Advances RI-08 (SRG-4) at VQ-4 level.

Certification-gate note: VQ-4 requires RI-08 and RI-09 in addition to all lower-level requirements; the matched-loading experiment (step 1) is a prerequisite for RI-09 resolution, establishing that the same-conditions direct comparison is methodologically valid before the external benchmark table is extended.

---

### §6 Contribution to institutional design

**1. RI-01 + RI-09 co-occurrence in the same SRG — new structural pattern:**
SRG-1 shows simultaneous RI-01 (non-equivalent mol% denominator for internal GOF1 vs GOF2 TOF comparison) and RI-09 (Table 8 external benchmark without direct comparison). This co-occurrence has structural significance: resolving only RI-09 (by adding a direct comparison experiment against prior literature) without first resolving RI-01 (equal-loading internal comparison) would construct an internally inconsistent claim — the new paper's "best value" for the RI-09 comparison would itself remain methodologically compromised. The RI-01 + RI-09 co-occurrence means both must be addressed in sequence, not in parallel. This is a new case for the codebook's RI co-occurrence pattern library: **denominator mismatch (RI-01) blocks external benchmark validity (RI-09) when the internal comparison is itself the primary claim vehicle**.

**2. PRI-11 additional case in heterogeneous Pd nanoparticle system:**
SRG-6 shows mechanism–kinetics decoupling (PRI-11): the Pd(0)/Pd(II) cycle is supported only by qualitative agreement with halide reactivity order (I >> Br >> Cl) and substrate electronic effects, without an algebraically derived rate law from the proposed cycle. Prior PRI-11 cases (Breitenfeld 2014 and Pengfei 2024 per v0.2a notes) were in homogeneous Pd systems; this paper provides a case in a heterogeneous Pd nanoparticle / porous framework system. The PRI-11 pattern is thus not mechanistically specific to homogeneous catalysis — it generalizes to any catalysis paper where the mechanistic model is post-hoc mapped to observed trends without kinetic derivation. This constitutes a third independent case, supporting formal PRI-11 promotion as a full RI code, with the heterogeneous catalysis domain as a confirmed extension.

**3. Incomplete negative evidence pattern (RI-04, CLA-2):**
The hot filtration test is presented as mechanistically conclusive for heterogeneous catalysis, yet (a) the AAS detection limit is unstated (SRG-3) and (b) the predicted mechanistic byproduct (homo-coupling from aryl-Pd(II)-X intermediate) is not measured (CLA-2). This matches the Stage 3 prompt's explicit "Incomplete negative evidence" pattern: negative experimental results (no Pd detected, no continued reaction after catalyst removal) are used as positive mechanistic evidence without mass-balance closure or kinetic-window evaluation. The case-specific implementation for EP-04a in heterogeneous Pd/H₂O-EtOH systems: the kinetic window is the TOF × catalyst mass calculation for the upper-bound leached Pd concentration vs known homogeneous Pd activity; this calculation is absent from the paper and should be added to the EP dictionary as a heterogeneous Pd hot-filtration implementation note.

**4. New RI-01 implementation — "Two-level denominator mismatch in TOF comparison":**
This paper presents a previously unrecorded RI-01 variant: the TOF denominator (total Pd mol) is invalid at two independent levels simultaneously — (level a) total vs surface-accessible Pd (CO chemisorption needed), and (level b) different total Pd mol% used in GOF1 and GOF2 experiments. Prior RI-01 cases in the corpus typically involved one type of measurement-frame inconsistency (different conditions, different units, or missing normalization). The two-level denominator mismatch deserves a note in the RI-01 implementation catalog as "when the TOF denominator is simultaneously analytically unverified AND operationally non-equivalent across the comparison, both defects must be resolved before the cross-system comparison is valid."

**5. Labeling mismatch co-occurring with RI-06 (§6 explicit pattern):**
The phrase [REDACTED: verbatim source quotation; see the source paper via its DOI] uses factual assertive verbs ("clearly proves," "actively alters") for a claim that is structurally a mechanistic hypothesis — the N-Pd coordination → enhanced TOF causal chain requires the XPS/EXAFS evidence that is absent (SRG-7/RI-03). This labeling mismatch co-occurs with RI-06 (the Pd(0)/Pd(II) cycle and N-Pd coordination effect are imported from the general N-heterocycle coordination chemistry literature without demonstrating isomorphism in the GOF system). The labeling mismatch is concentrated in the "Discussion" and "Conclusion" sections, not in the "Results," consistent with the pattern observed in other corpus papers where the assertion drift between Results and Discussion is the locus of labeling mismatches.

**6. No new PRI candidate required:**
All detected patterns are adequately captured by RI-01, RI-03, RI-04, RI-05, RI-06, RI-08, RI-09, and PRI-11. No pattern was observed that fails to fit existing codes.

---

> **Public-cut redaction notice**: verbatim quotations from the analysed papers in this file have been replaced by `[REDACTED: …]` markers (rules in the repository README). The unredacted file is in the reviewer version of the deposit.
