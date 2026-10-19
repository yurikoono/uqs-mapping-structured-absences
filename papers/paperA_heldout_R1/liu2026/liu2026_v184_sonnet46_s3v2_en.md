```
prompt_version: stage3-v2-en-20260419
model_info: claude-sonnet-4-6
```

# Re-certification Assessment Sheet for Scientific Knowledge

## Liu et al. 2026 (Organic Letters, Letter)

---

### §1 Claim Architecture

**Core claim summary:**

The paper claims that DABCO and aryl iodides form a photoactive EDA complex that, under 365 nm irradiation, initiates a tandem radical Heck-type arylation of trans-cinnamate followed by [4+2] electrocyclization to afford 9,10-dihydronaphthalene products. The reaction requires no discrete photocatalyst, no transition metal, and no strong oxidant, and proceeds from readily available feedstock substrates at room temperature.

*Novelty pillar*: First photocatalyst-free EDA-mediated tandem Heck-type arylation/[4+2] electrocyclization that operates on unactivated trans-cinnamates (overcoming the 4-hydroxycinnamate requirement of the closest prior art, Xia et al. 2020, ref 10).

*Utility pillar*: 28 substrate combinations in 30–75% isolated yield; demonstrated scalability to 2 mmol (71% yield); direct derivatization of the products (compound 31, 79% yield).

**Layered structure — three independent layers:**

- **Layer 1 (Synthetic utility)**: The 28 substrate combinations yield isolable 9,10-dihydronaphthalene products in 30–75% yield under photocatalyst-free conditions. This layer can be refuted only by demonstrating that the reported products are misidentified or that all yields reflect selective purification of minor components. It cannot be refuted by mechanistic reassignment.
- **Layer 2 (EDA photomechanistic claim)**: The DABCO/ArI EDA complex is the photoactive species responsible for SET and subsequent radical cascade. This layer can be partially refuted if an alternative mechanism (e.g., direct ArI excitation, DABCO serving as stoichiometric reductant without EDA complex formation) were shown to operate, without collapsing Layer 1.
- **Layer 3 (Novelty over Xia ref 10)**: The new method overcomes the 4-hydroxycinnamate substrate limitation of ref 10. This is the most fragile layer: it depends on a claimed difference in substrate scope that has not been verified by direct experimental comparison. Layer 3 is asserted (not demonstrated) and thus structurally dependent on an unverified external benchmark (C-1).

*Inter-layer dependency*: Refuting Layer 2 weakens but does not eliminate Layer 1 (the chemistry works regardless of the exact mechanism). Refuting Layer 3 does not affect Layers 1 or 2. A full mechanistic reassignment (e.g., showing the reaction is not EDA-mediated) would demote Layer 2 and remove Layer 3's comparative basis, but leave Layer 1 intact.

---

### §2 SRG / CLA → RI / ER / EP Crosswalk

---

**SRG-1 [Mechanistic elementary steps unsupported]** (B-5, B-6, U-1, U-2, U-3)

* **Primary RI**: RI-03 Unobserved explanatory — all four proposed elementary steps (SET, radical addition → III, HAT → IV, [4+2] → V, aromatization → 3) are inferred from product structure and qualitative inhibition experiments; none of the proposed intermediates (II, III, IV, V) is directly observed or kinetically constrained.
* **Secondary RI**: RI-04 Unreplicated discriminator — the TEMPO/BHT inhibition experiment and the light-on/off experiment are each single experiments interpreted as evidence for specific mechanistic steps (radical pathway; non-chain mechanism) without mass-balance closure or kinetic-window quantification.
* **Secondary RI**: RI-06 Imported model — the [4+2] electrocyclization assignment is imported from pericyclic chemistry theory (Woodward-Hoffmann) without demonstration of isomorphism in this specific EDA-initiated radical system where the diene intermediate (IV) is proposed to be a radical species rather than a closed-shell diene.
* **ER**: All elementary steps in the proposed mechanism must be either directly detected (e.g., transient absorption spectroscopy for EDA excitation, EPR/NMR for radical intermediates II–IV) or kinetically bounded by at least one mechanistic probe experiment (KIE, radical clock, quantum yield, or stoichiometric oxidant identification) that excludes the principal alternative pathway at each step.
* **EP**: EP-03a (Direct-observation / state-assignment pack); EP-04a (Discrimination / replication pack); EP-06a (Analogy-validation pack)
* **Case-specific implementation**: (a) Primary kinetic isotope effect using d5-ethyl trans-cinnamate (kH/kD > 2 would confirm HAT; kH/kD ≈ 1 would redirect to oxidative mechanism); (b) Stoichiometric DABCO consumption measurement per mole of product 3 (by NMR quantitation of DABCO remaining after a stopped-time reaction) to identify the terminal oxidant in the V → 3 aromatization step; (c) DFT calculation of the concerted [4+2] transition state vs. stepwise radical closure activation energies for the vinyl-radical-diene intermediate IV, with orbital symmetry analysis.
* **Notes**: B-5 (3/3 convergence, high_convergence_low_gap: highest-convergence item), U-2 (critical severity, low_convergence_high_gap: V2 only — strongest single-agent signal), U-1 (high severity), B-6 (2/3 convergence), U-3 (high severity). This is the largest SRG (5 items) and dominates the mechanistic gap.

---

**SRG-2 [DABCO role and fate unexplained]** (B-1, B-2, U-1)

* **Primary RI**: RI-03 Unobserved explanatory — DABCO radical cation (I), generated as the primary oxidation product of SET, is proposed in Scheme 3f but its subsequent fate (re-reduction, dimerization, or decomposition) is not observed, constrained, or reported.
* **Secondary RI**: RI-05 Qualitative overread — the conclusion that "DABCO plays a crucial role" and that it is uniquely effective compared to NEt3 and KOH is derived from two qualitative yield comparisons (entries 5–6: NEt3 → nd, KOH → nd) without measurement of ionization potentials, EDA complex formation constants, or HAT acceptor ability for the compared reagents.
* **ER**: DABCO stoichiometry per catalytic turnover must be quantified: if DABCO is consumed as a stoichiometric reductant (forming DABCO•+ irreversibly), the yield of the DABCO-derived oxidation product must be measured and the distinction between "photocatalytic" (DABCO regenerated) and "stoichiometric reductant" (DABCO consumed) must be resolved. The uniqueness of DABCO must be grounded in at least one measured physicochemical property (Kd for EDA complex, or ionization potential comparison with NEt3).
* **EP**: EP-03a (Direct-observation / state-assignment pack); EP-05a (Quantitative-ranking substantiation pack)
* **Case-specific implementation**: (a) 1H NMR titration of a stopped reaction to quantify DABCO remaining vs. product yield (mass balance on DABCO per mole of product 3); (b) UV-vis or electrochemical measurement of DABCO/NEt3 EDA complex formation constants with 4-iodobenzaldehyde (2a) to establish the physicochemical basis for DABCO's unique effectiveness.
* **Notes**: B-1 (2/3, V1=high, V2=critical; stoichiometry), B-2 (2/3, V1=high, V2=critical; uniqueness), U-1 (high; DABCO•+ fate; shared with SRG-1). The B-1/B-2/U-1 cluster is physically unified: DABCO's stoichiometric requirement (B-1) and unique effectiveness (B-2) both flow from the absence of DABCO•+ characterization (U-1).

---

**SRG-3 [EDA complex evidence qualitative only]** (B-7, B-8)

* **Primary RI**: RI-04 Unreplicated discriminator — the UV-vis color change (B-7) and the "tentative" TEMPO-radical adduct HRMS detection (B-8) are each single-experiment qualitative observations interpreted as "strong evidence" for (a) EDA complex formation and (b) radical intermediate presence, respectively, without replicate measurements, mass-balance, or alternative-pathway exclusion.
* **Secondary RI**: RI-01 Reporting integrity — the UV-vis experiment lacks quantitative parameters (λmax, ε, Kd, stoichiometry by Job's plot) that would allow cross-comparison of this EDA complex with others in the literature.
* **ER**: EDA complex characterization must include quantitative UV-vis titration (Job's method or continuous variation) that establishes stoichiometry and Kd under the reaction conditions, and the TEMPO-radical adduct detection must be supported by the observed m/z, mass accuracy (ppm error), and comparison with theoretical m/z for the proposed adduct.
* **EP**: EP-04a (Discrimination / replication pack); EP-01a (Reporting-coherence pack)
* **Case-specific implementation**: (a) UV-vis Job's plot using DABCO (0.4 mmol) and 4-iodobenzaldehyde (2a, 0.2 mmol) in MeCN at room temperature to determine stoichiometry; spectrophotometric titration to determine Kd; (b) HRMS report in the main text or Table 1 footnote: observed [M+H]+ m/z, calculated m/z, ppm error, and the proposed adduct molecular formula for the TEMPO-trapped radical intermediate.
* **Notes**: B-7 (2/3, V2=medium, V3=high), B-8 (2/3, V2=high, V3=high). This SRG is the evidential bridge for the EDA mechanism claim; its resolution would advance Layer 2 independently of the elementary-step mechanism (SRG-1).

---

**SRG-4 [Stereochemical outcome reporting incomplete]** (B-3, B-4)

* **Primary RI**: RI-08 Unquantified reliability — isolated yields for all 28 compounds are single-determination values with no replicate measurements, no standard deviations, and no dr data for 27 of 28 compounds.
* **Secondary RI**: RI-01 Reporting integrity — mass balance is not reported for any substrate; the fate of unconsumed starting material and the nature of byproducts are unspecified.
* **ER**: Representative replicate yields (n ≥ 3, at minimum for the model reaction compound 3 and for one substrate at each extreme of the yield range) and dr data for all products bearing new stereocenters must be reported. The relative configuration of the major diastereomer for compound 15 (1.2:1 rr) and all other dr-relevant products must be assigned by NMR or X-ray.
* **EP**: EP-08a (Replication / uncertainty pack); EP-01a (Reporting-coherence pack)
* **Case-specific implementation**: (a) Triplicate synthesis of compound 3 under standard conditions, reporting mean yield ± SD; (b) 1H NMR NOESY analysis or X-ray for compound 15 to assign the structure of each diastereomer and confirm whether "rr" designates regioisomers or diastereomers.
* **Notes**: B-3 (2/3, V1=medium, V3=high; mass balance), B-4 (2/3, V1=medium, V3=medium; dr). SRG-4 is shared with SRG-5 (B-3 appears in both).

---

**SRG-5 [Photochemical conditions insufficiently specified]** (B-3, B-10)

* **Primary RI**: RI-01 Reporting integrity — the irradiation source is described as "365 nm LEDs" with no specification of power (watts), irradiance (mW/cm²), lamp-to-vessel distance, or vessel geometry; cross-comparison with other photoredox protocols and inter-lab reproduction are compromised by this omission.
* **Secondary RI**: RI-08 Unquantified reliability — without photon flux specification, the effective quantum yield of the reaction is unmeasurable and the yield data are not fully reproducible.
* **ER**: Lamp power (W), measured or estimated irradiance at the vessel surface (mW/cm²), and lamp-to-vessel distance must be reported. If irradiance measurement is not available, the lamp model and batch number should be specified.
* **EP**: EP-01a (Reporting-coherence pack); EP-08a (Replication / uncertainty pack)
* **Case-specific implementation**: Report irradiation geometry in the Supporting Information: e.g., "365 nm LED (Kessil PR160L, 30 W nominal, irradiance measured at 10 cm from source = X mW/cm²)" and vessel position in the irradiation setup.
* **Notes**: B-3 (shared with SRG-4; 2/3), B-10 (V3=medium, single agent). SRG-5 is the least mechanistically significant SRG but is non-trivially blocking for VQ-2.

---

**Outside the SRGs: CLAs**

---

**CLA-1 [Dropped quantitative benchmark — Xia ref 10]**

* **Derived from**: D-4 Candidate 6; grounded in C-1 (Ref 10, Xia/Liang et al. Chem. Sci. 2020; affects_claims = yes).
* **CLA trigger**: C-1 directly bears on Layer 3 (novelty over Xia); B/A items in grounded_in are not included in any SRG; C-1 is the only C item where affects_claims = yes.
* **Primary RI**: RI-09 External superiority — the claim that the new EDA method "significantly overcomes the limitation of 4-hydroxycinnamates" rests entirely on the characterization of ref 10's substrate requirement from the external literature, without a direct experimental comparison (no substrate from Xia's scope is tested under the new conditions; no head-to-head yield table is presented).
* **ER**: At least one substrate from Xia's scope (e.g., ethyl 4-hydroxycinnamate) must be tested under the new EDA conditions, and at least one substrate from the new scope (e.g., ethyl trans-cinnamate without 4-OH) must be tested under Xia's conditions, with a head-to-head yield comparison in a two-column table.
* **EP**: EP-09a (Internal benchmark pack)
* **Case-specific implementation**: Prepare ethyl 4-hydroxy-trans-cinnamate and test it under the new standard conditions (DABCO 3.0 equiv, MeCN, 365 nm, 24 h, Ar, rt) with 4-iodobenzaldehyde (2a); compare the yield of the tandem product against the Xia protocol yield from the same substrate pair. Test ethyl trans-cinnamate (1a) under the Xia protocol (if applicable) to confirm no product is obtained, establishing that the new method's substrate scope truly extends beyond Xia's.
* **Notes**: C-1 (symmetric cite-and-dismiss; affects_claims = yes). Layer 3 cannot be certified to VQ-4 without this CLA resolved.

---

**CLA-2 [Entry 10 kinetic efficiency gap]**

* **Derived from**: D-4 Candidate 8; grounded in B-12.
* **CLA trigger**: B-12 directly bears on the claimed kinetic advantage of the in-situ tandem architecture over sequential addition; B-12 is not in any SRG; it is used as mechanistic "evidence" (not merely a reporting omission).
* **Primary RI**: RI-04 Unreplicated discriminator — the single comparison of independently submitted 3a (21% yield) vs. in-situ tandem (75% yield) is a single data point interpreted at a high mechanistic level ("evidence for the role of 3a as an intermediate") without an additional experiment that explains the 54-pp efficiency gap.
* **Secondary RI**: RI-05 Qualitative overread — the 3.6-fold efficiency gap is treated as binary evidence (3a is an intermediate) rather than as a quantitative kinetic constraint that would distinguish obligate coupling from thermodynamic escape.
* **ER**: A time-resolved yield experiment must be performed for both the tandem (1a + 2a, standard conditions) and the sequential (pre-formed 3a, standard conditions) pathways, measuring conversion of starting material and yield of product at 1h, 3h, 6h, 12h, and 24h. The relative rate constants (k3a_in-situ vs. k3a_external) extracted from this profile would constrain the kinetic architecture of the cascade.
* **EP**: EP-04a (Discrimination / replication pack); EP-05a (Quantitative-ranking substantiation pack)
* **Case-specific implementation**: Monitor conversion of 3a (externally added, 0.2 mmol) under standard conditions at 1h intervals by GC-FID (internal standard), to generate a time-yield profile comparable to Scheme 3c's tandem profile. Overlay the two profiles to determine whether in-situ 3a cyclizes faster at early time points (kinetic coupling) or whether the gap is exclusively due to 3a decomposition at late time points.
* **Notes**: B-12 (2/3, V1=high, V2=high). Layer 1's claim of a tandem kinetic advantage is directly testable by this CLA.

---

### §3 Current VQ assessment

**Current judgment: VQ-1 (Observation)**

---

**VQ-1 (Observation) — HOLDS**

RI-02 is resolved: the structure of the representative product (compound 3, 9,10-dihydronaphthalene) is established by X-ray crystallography (CCDC 2577250). The remaining 27 compounds are characterized by 1H/13C NMR and HRMS (per SI), with structural assignments consistent with the established skeleton of compound 3. RI-02 is non-fatal: the product identity is established at sufficient granularity for VQ-1, though X-ray for additional compounds would strengthen assignments of compounds with unassigned stereochemistry.

---

**VQ-2 (Method) — FAILS**

On the premise that VQ-1 (RI-02) holds (above), VQ-2 requires resolution of RI-01 and RI-07.

*RI-01 (SRG-5, SRG-3) unresolved*: LED irradiance is not specified (B-10), and UV-vis EDA complex characterization lacks quantitative parameters (B-7). The absence of photon flux specification means the primary photochemical input to the reaction is unknown; inter-lab comparison of this photochemical protocol is not possible without it.

*RI-07 (SRG-2, B-2) unresolved*: The claim that DABCO is uniquely effective is based on two failure examples (NEt3, KOH — entries 5–6), both of which differ from DABCO in multiple physicochemical parameters simultaneously (pKa, ionization potential, geometry, EDA complex formation capacity). The boundary "only DABCO is effective" is an unsupported boundary without failure examples among structurally analogous cage or bridged amines.

Both RI-01 and RI-07 are non-fatal to the core synthetic claim individually, but together they prevent VQ-2 certification. RI-01 is the more consequential barrier (photon flux specification is a method reproducibility requirement).

---

**VQ-3 (Mechanism) — FAILS**

(Would require VQ-2 to hold first.)

*RI-03 (SRG-1) unresolved*: All four proposed elementary steps (SET → II, radical addition → III, HAT → IV, [4+2] → V, aromatization → 3) involve unobserved intermediates or unobserved stoichiometric processes. No transient-state intermediate has been detected; the terminal oxidant for the aromatization step (U-2, critical) is unidentified; the HAT agent is unspecified (B-5, 3/3 convergence). RI-03 failures here are fatal to VQ-3 as stated: the mechanistic claim cannot hold without at least one elementary step being kinetically constrained.

*RI-04 (SRG-3, CLA-2) unresolved*: Qualitative radical trapping (TEMPO/BHT inhibition) and light-on/off experiments are used as positive mechanistic discriminators without mass-balance closure (SRG-3, B-8) and without kinetic quantitation of the efficiency gap (CLA-2, B-12).

*RI-06 (SRG-1, B-6) unresolved*: The [4+2] electrocyclization assignment is imported from pericyclic chemistry theory without demonstration of isomorphism in the EDA-initiated radical system. Specifically, the diene intermediate IV in this system is formed via HAT from a radical species, not via a thermal or photochemical activation of a pre-existing diene; whether Woodward-Hoffmann orbital symmetry rules apply to the ring-closing step of a radical intermediate is not addressed.

**However, Layer 1 (synthetic utility) on its own reaches approximately VQ-1.5**: The structural assignment by X-ray (compound 3) and NMR/HRMS (all others) satisfies VQ-1, and the 28-substrate scope with consistency of product class provides method-level evidence that falls short of VQ-2 only due to RI-01 (LED specification) and RI-08 (no replicates). Layer 1 is the most robust layer; its VQ ceiling is VQ-2 pending LED specification and replication data.

---

**VQ-4 (Benchmark) — FAILS**

(Would require VQ-3 to hold first.)

*RI-08 (SRG-4) unresolved*: No replicate yields are reported for any substrate; standard deviations are absent for all 28 yield determinations. Comparative data lack uncertainty quantification.

*RI-09 (CLA-1) unresolved*: Superiority over the Xia method (ref 10) is asserted on the basis of the external literature characterization of Xia's scope, without any direct experimental comparison. Layer 3 (novelty over Xia) cannot reach VQ-4 without CLA-1 resolved.

---

### §4 Era-Norm Annotation

---

**communication-era tolerated** (2026, Organic Letters letter format):

- *B-3 (no mass balance)*: Isolated-yield-only reporting is the standard for scope tables in Org. Lett. letters in 2026. Mass balance is expected in mechanism-focused full papers but not required for preparative scope surveys at this venue/format combination.
- *B-4 (no dr for 27/28 compounds)*: When only one substrate shows a mixture of stereoisomers, reporting dr only for that substrate (compound 15) and implying single diastereomer formation for others by NMR analysis is within current Org. Lett. norms for synthetic letters. This is conditionally tolerated: it would not be tolerated if the paper claimed stereoselectivity as a feature.
- *B-7 (UV-vis without Kd/ε)*: Qualitative UV-vis EDA complex characterization (color change + spectral shift) is current-era standard for establishing EDA complex formation in photocatalysis letters at this venue; quantitative Kd/ε are expected in photophysics journals but not routinely required by Org. Lett. as of 2026.
- *B-9 (ortho/meta byproducts uncharacterized)*: Brief mention of "complicated reaction system" without byproduct characterization is tolerated in letters where the paper's scope does not include those substrates as claimed products.
- *C-2, C-3 (symmetric cite-and-dismiss for refs 6–7)*: Clustering prior methods as "limitation-bearing" without individual evaluation is a common rhetoric pattern in synthetic method letters and is tolerated at current genre norms.

**modern-era deficient** (items insufficient for present-day re-certification):

- *B-5 (HAT mechanistically unsubstantiated)*: By 2026, photocatalysis letters in Org. Lett. that propose a specific elementary step as the key mechanistic event (here: HAT as the dehydrogenation step) are expected to support it with at least one diagnostic experiment (KIE, radical clock, or isotope labeling). HAT assignment without evidence is modern-era deficient for a mechanism-proposing letter.
- *B-10 (LED power/irradiance not specified)*: By 2026, photon flux specification is expected in photocatalysis papers following the guidelines of photochemistry professional societies and is explicitly listed in current best-practice reporting checklists for photocatalysis manuscripts. The absence of irradiance data is modern-era deficient.
- *U-2 (aromatization terminal oxidant unidentified)*: The aromatization step (V → 3) is mechanistically incomplete — no terminal oxidant is identified, no reduced byproduct is measured, and the mechanism is atom-imbalanced as drawn. By 2026 mechanistic standards, an incomplete mechanism at a key bond-forming step is modern-era deficient.
- *B-8 (HRMS radical adduct "tentative")*: Reporting a key piece of mechanistic evidence as "tentative" without providing mass accuracy (ppm error) or the observed/theoretical m/z ratio in the main text is modern-era deficient. HRMS data sufficient to confirm a proposed radical adduct requires explicit ppm error in the text (not just SI).
- *C-1 (no direct comparison with Xia ref 10)*: The novelty claim rests on an unverified substrate scope superiority. By 2026 standards, a novelty claim asserting improvement over a specific prior method requires at least a minimal head-to-head comparison. This is modern-era deficient independent of venue format.

**dual classification** (tolerated then, deficient now):

- *B-10 (LED specification)*: Pre-2023 photocatalysis letters routinely omitted irradiance; the practice shifted with field-specific reporting guidelines adopted ~2023–2024. A 2026 paper that follows pre-2023 practice is era-norm-crossing: tolerated at the pre-2023 era norm, deficient by 2026 standards.

---

### §5 Shortest-reinforcement route

---

**Shortest route to VQ-2:**

1. **EP-01a** (Reporting-coherence pack) — Report lamp model, power (W), irradiance at the reaction vessel surface (mW/cm²), and lamp-to-vessel distance in the Supporting Information; add a cross-reference in the main text Conditions footnote. Advances RI-01 (SRG-5, B-10).
2. **EP-07a** (Boundary-test pack) — Test at least two structurally analogous cage amines (e.g., ABCO [2-azabicyclo[2.2.2]octane], TEDA, DABCO-Me) and one additional non-cage tertiary amine (e.g., 1,4-diazabicyclo[5.4.0]undec-7-ene [DBU]) under standard conditions to establish that DABCO's cage geometry or specific ionization potential is the determinant of effectiveness, rather than basicity alone. Advances RI-07 (SRG-2, B-2).

*Certification-gate note: resolution of RI-01 (EP-01a) and RI-07 (EP-07a) are the two required gates for VQ-2 certification; both must be resolved before VQ-3 assessment begins.*

---

**Shortest route to VQ-3** (requires VQ-2 first):

1. **EP-03a** (Direct-observation / state-assignment pack) — Primary kinetic isotope effect using d5-ethyl trans-cinnamate (or d1-cinnamate at the aliphatic C–H position) under standard conditions with 4-iodobenzaldehyde (2a): compare kH/kD at the HAT step. A primary KIE (kH/kD ≥ 2) confirms C–H abstraction as the mechanistic event; kH/kD ≈ 1 would redirect the investigation to oxidative alternatives. This is the highest-information-gain single experiment for SRG-1. Advances RI-03 (B-5, SRG-1).
2. **EP-04a** (Discrimination / replication pack) — Quantify DABCO stoichiometric consumption: perform a stopped-time reaction at t = 6h and t = 24h, measure residual DABCO by 1H NMR with internal standard (mesitylene), and compute moles of DABCO consumed per mole of product 3 formed. A ratio approaching 1 would confirm stoichiometric consumption; a ratio approaching 0 would indicate regeneration. Simultaneously: identify the DABCO-derived byproduct(s) by LC-HRMS. Advances RI-03 (U-2, SRG-1; U-1, SRG-2).
3. **EP-06a** (Analogy-validation pack) — DFT calculation at a consistent level of theory (e.g., ωB97X-D/6-311+G(d,p)/MeCN implicit solvent) of the activation barriers for (a) concerted [4+2] thermal electrocyclization of the putative diene intermediate IV and (b) stepwise radical closure of the same system; compare with the activation barrier for the competing radical elimination. If the concerted [4+2] barrier is lower than the radical closure barrier, the orbital symmetry assignment is computationally validated. Advances RI-06 (B-6, SRG-1).
4. **EP-03a** (Direct-observation pack, photophysical) — UV-vis Job's plot and spectrophotometric titration of DABCO vs. 4-iodobenzaldehyde (2a) in MeCN to determine stoichiometry and Kd of the EDA complex. Report λmax, ε, Kd, and stoichiometry in the main text. Advances RI-03 (SRG-3, B-7; SRG-2, U-1).
5. **EP-04a** (Discrimination pack, CLA-2) — Time-resolved yield experiment for externally added 3a (0.2 mmol, standard conditions) at 1h, 3h, 6h, 12h, 24h intervals by GC-FID or NMR with internal standard, compared to the in-situ tandem time profile. Advancing RI-04 (CLA-2, B-12) determines whether the kinetic advantage of the tandem architecture is a coupled step or an artifact of 3a decomposition.

*Certification-gate note: VQ-3 certification requires resolving RI-03 (EP-03a steps 1, 2, 4 above), RI-04 (EP-04a steps 2, 5), and RI-06 (EP-06a step 3); the experimental investment order (KIE first for highest gain) differs from the formal gate order (RI-03 → RI-04 → RI-06 each required); the final certification follows the inheritance principle VQ-1 → VQ-2 → VQ-3.*

---

**Route to VQ-4** (requires VQ-3 first):

1. **EP-09a** (Internal benchmark pack) — Direct head-to-head yield comparison with Xia ref 10: test ethyl 4-hydroxy-trans-cinnamate under the new EDA conditions; test ethyl trans-cinnamate under Xia's conditions; tabulate yields side-by-side for ≥3 substrate pairs. Advances RI-09 (CLA-1, C-1).
2. **EP-08a** (Replication / uncertainty pack) — Report triplicate isolated yields with SD for compound 3 (model reaction) and for 3–4 representative substrates at the low (30–35%), mid (50–55%), and high (70–75%) yield ranges. Advances RI-08 (SRG-4, B-3).

*Certification-gate note: VQ-4 requires resolving RI-08 (EP-08a) and RI-09 (EP-09a) in addition to inheriting VQ-3 requirements.*

---

### §6 Contribution to institutional design

**Labeling mismatch (confirmed, co-occurs with RI-06)**

The proposed mechanism in Scheme 3f employs exclusively factual verbs throughout its description: "is excited," "gives DABCO radical cation I and intermediate II," "generates radical intermediate III," "is then converted into intermediate IV," "is obtained via a [4+2] electrocyclization process," "can be generated via an aromatization process." The hypothesis label ("proposed mechanism") appears only in the scheme title; within the main text narrative describing each step, all verbs are in the indicative mood. This labeling mismatch — where the scheme is called "proposed" but described as factual throughout — co-occurs with RI-06 (the [4+2] assignment imported from pericyclic chemistry theory without isomorphism verification). This confirms the labeling mismatch pattern as an RI-06-associated signature in synthetic photocatalysis letters.

**Incomplete negative evidence (case-specific implementation of RI-04 confirmed)**

Two mechanistic control experiments are used as positive mechanistic evidence without mass-balance closure or kinetic-window evaluation:
1. TEMPO/BHT inhibition ("significantly suppressed" reaction): used to confirm radical pathway, without quantifying what fraction of the TEMPO/BHT was consumed per mole of starting material, or whether the inhibition rate constant is consistent with the proposed radical intermediate lifetime.
2. Light-on/off experiment: used to "exclude a radical chain pathway," without characterizing the dark decay rate of any photoproduced radical species, which would be required to distinguish "no chain" from "chain with short chain length."
This pattern — radical trapping and light-on/off experiments used as positive mechanistic evidence without kinetic-window quantification — is a case-specific implementation of RI-04 (unreplicated discriminator used for high-level mechanistic conclusion). This pattern has appeared in prior UQS analyses of visible-light photocatalysis papers and represents a recurring methodological signature in this subfield.

**RI co-occurrence pattern (RI-03 + RI-04 + RI-06 in SRG-1)**

The mechanistic elementary steps SRG-1 exhibits a three-way RI co-occurrence: RI-03 (unobserved intermediates), RI-04 (qualitative controls used as positive evidence), and RI-06 (pericyclic mechanism imported without isomorphism check). Resolving RI-04 alone (improving the quality of radical trapping experiments) leaves RI-03 and RI-06 unresolved; resolving RI-03 alone (detecting intermediates) leaves the orbital symmetry question (RI-06) unresolved. All three must be addressed for VQ-3 certification. This three-way co-occurrence pattern in EDA-initiated radical cascade papers with a pericyclic terminal step may be worth tracking across additional papers in this subfield.

**Self-contradictory absence pattern (U-2, aromatization oxidant) — new representative case for RI-03**

U-2 (aromatization oxidant unidentified) is the most analytically significant self-contradictory absence in this paper: the proposed mechanism explicitly draws a V → 3 conversion that is formally a two-electron oxidation (loss of two H atoms or equivalent), yet no oxidant is identified and the mechanism as drawn is atom-imbalanced. This is a clear RI-03 subtype — "available-but-unutilized mechanistic analysis": the paper could have identified the aromatization oxidant from the stoichiometry of the already-used reagents (DABCO, ArI, solvent) but did not do so. This provides a new representative case for the RI-03 subtype catalog.

**PRI candidate assessment**

No new PRI code is required for this paper. The RI-03 + RI-06 co-occurrence in EDA/pericyclic systems is a subtype of existing codes. If this co-occurrence is confirmed across 2+ independent EDA-initiated cascade papers, it could constitute a PRI candidate; for now, it is recorded as a recurring observation at the SRG level. This case confirms existing institutional design with the addition of a new RI-03 (self-contradictory-absence) representative case and a new RI-04 (incomplete negative evidence) representative case specific to visible-light photocatalysis.
