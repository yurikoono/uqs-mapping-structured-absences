prompt_version: stage3-v2-en-20260419
model_info: claude-sonnet-4-6

# Re-certification Assessment Sheet for Scientific Knowledge

## Tamao, Sumitani, Kumada 1972 (Journal of the American Chemical Society, communication)

---

### §1 Claim Architecture

**Core claim summary:**

The paper reports a selective catalytic cross-coupling of Grignard reagents with sp²-carbon organic halides (vinyl or aryl), using [NiCl₂(dpe)] as a catalytic complex in diethyl ether. The Novelty pillar has three components: (a) selectivity — cross-coupling predominates over homo-coupling, which plagued all prior transition-metal-catalyzed Grignard coupling methods; (b) catalyst design — the bidentate diphosphine [NiCl₂(dpe)] is presented as the enabling structure, with activity orders among Ni-phosphine complexes documented; (c) mechanistic framework — a three-step catalytic cycle (diorganonickel formation → oxidative-addition/transmetalation → reductive elimination) is proposed as a "working hypothesis.[REDACTED: substantial verbatim quotation; see Tier 9]hardly accessible by conventional methods."

**Layered structure judgment:**

Independent layers are present. Three layers can be identified: (a) **Synthetic utility layer** — the method gives high isolated and glpc yields across ten substrate combinations; a refutation of analytical precision would not collapse this layer because the yield range (76–98%) is sufficiently high that even ±10% systematic calibration error would not alter the synthetic utility conclusion. (b) **Catalyst design layer** — the bidentate phosphine activity order and the ligand-requirement claim (feature 3) rest on data in footnote 21 that are not disclosed; this layer is internally fragile but does not depend on the synthetic utility layer. (c) **Mechanistic layer** — the proposed three-step catalytic cycle is explicitly a "working hypothesis" derived by analogy with stoichiometric (dipy)Ni reactions; a demonstration that the actual catalyst is heterogeneous Ni⁰ rather than homogeneous Ni(II) would collapse this layer but would not collapse the synthetic utility layer.

The critical asymmetry: the paper's central selectivity claim ("cross over homo coupling") spans all three layers simultaneously — it is invoked as a utility criterion (Table I: no homo-coupling products reported), as a catalyst design argument (bidentate phosphine prevents R–R homo-coupling), and as a mechanistic prediction (eq 3 predicts R–R as a byproduct of the initiation step). A refutation of the selectivity claim at any layer would create pressure on all others. This is the single point of structural vulnerability across an otherwise layered architecture.

---

### §2 SRG / CLA → RI / ER / EP Crosswalk

---

**SRG-1 [Catalytic mechanism evidence gap]**

* **Primary RI**: RI-06 [Imported model]
* **Secondary RI**: RI-03 [Unobserved explanatory]
* **ER**: For the proposed Ni(0)/Ni(II) catalytic cycle (eqs 2–4) to be accepted as the operative mechanism, the diorganonickel intermediate 1 (L₂NiR₂) and haloorganonickel intermediate 2 (L₂Ni(R')(X'')) must be independently identifiable as kinetically relevant species under actual [NiCl₂(dpe)] catalytic conditions in diethyl ether, not merely by analogy with stoichiometric (dipy)Ni chemistry (refs 11–12). The proposed cycle is the paper's entire mechanistic account; if the analogy with (dipy)Ni is not valid in the (dpe)Ni system, the cycle provides no explanatory support for any of the five "significant features."
* **EP**: EP-06a [Analogy-validation pack]; EP-03a [Direct-observation / state-assignment pack]
* **Case-specific implementation**: (EP-06a) Synthesize authentic [NiCl₂(dpe)]-derived diorganonickel intermediate 1 (L₂Ni(n-Bu)₂ or L₂Ni(Et)₂) by independent stoichiometric route; verify that it undergoes the reaction sequence in eq 3 with PhCl at the rate required to account for catalytic turnover. This tests whether the (dpe)Ni system is genuinely isomorphic with the (dipy)Ni analogy. (EP-03a) Monitor the [NiCl₂(dpe)] + n-BuMgBr + PhCl reaction in diethyl ether by in situ ³¹P NMR to identify which Ni-phosphine species are present during catalytic turnover and whether the black precipitate observed in Example 1 is formed before or after product formation.
* **Notes**: Members A-2 (primary explicit deferral — "working hypothesis[REDACTED: substantial verbatim quotation; see Tier 9]unobserved explanatory" species under catalytic conditions. The co-occurrence of RI-06 and RI-03 in this SRG means that resolving only the analogy question (EP-06a) is insufficient — even if the (dpe)Ni system is isomorphic with (dipy)Ni, intermediate 1 must still be directly observed under catalytic conditions (EP-03a) to achieve VQ-3.

---

**SRG-2 [Cross/homo-coupling selectivity quantification]**

* **Primary RI**: RI-08 [Unquantified reliability]
* **Secondary RI**: RI-09 [External superiority]
* **ER**: For the selectivity claim ("selective cross-coupling") to hold as the paper's central contribution, the cross:homo product ratio must be reported for at least one representative Table I entry, and the Ni-dpe system must be compared numerically with the Tamura-Kochi benchmark on a shared substrate (e.g., n-BuMgBr + vinyl chloride) to establish that "substantial amounts" of homo-coupling characterizing prior methods is improved by a definable margin in this system.
* **EP**: EP-08a [Replication / uncertainty pack]; EP-09a [Internal benchmark pack]
* **Case-specific implementation**: (EP-08a) For the entry n-BuMgBr/PhCl (76% isolated yield), run the reaction in triplicate under identical conditions and quantify R-R homo-coupling product (n-Bu-n-Bu, bp ~144°C, distinguishable by glpc) in each replicate to establish cross:homo ratio and reproducibility. (EP-09a) Prepare a direct comparison experiment: run n-BuMgBr + CH₂=CHCl (Table I entry, 95% glpc yield) under [NiCl₂(dpe)] conditions and under Tamura-Kochi Fe catalyst conditions in the same solvent system, reporting cross-coupling product yield and homo-coupling (n-Bu-n-Bu) yield for both, on the same glpc calibration.
* **Notes**: Members B-6 (homo-coupling product not reported or quantified, "negative result as evidence" flag), C-1 (Tamura-Kochi cited as benchmark but no shared-substrate comparison on common metric), U-1 (eq 3 predicts R–R as stoichiometric byproduct of initiation step, yet R–R is absent from all product analyses). Position in TEMPERATURE_SUMMARY: high_convergence_low_gap (B-6: V2=high, V3=high, convergence=2/3; U-1: V2=high, V3=high, convergence=2/3). RI-08 is Primary because the selectivity claim rests entirely on the absence of homo-coupling products from Table I without any measurement or detection-limit statement — an internal consistency check (yield + homo-coupling = 100% - unreacted starting material) cannot be performed. RI-09 is Secondary because the superiority claim over Tamura-Kochi rests entirely on the characterization in refs 5–6 without a direct experimental comparison.

---

**SRG-3 [Scope restriction without negative-result evidence]**

* **Primary RI**: RI-07 [Unsupported boundary]
* **Secondary RI**: RI-05 [Qualitative overread]
* **ER**: For the sp² electrophile restriction to be established as the operational scope boundary (feature 2), at least one representative failed reaction with an sp³ alkyl or allyl halide must be reported — either as a 0% yield Table I entry or as a footnote stating [REDACTED: substantial verbatim quotation; see Tier 9] — to distinguish a fundamental mechanistic barrier from a practical preference.
* **EP**: EP-07a [Boundary-test pack]
* **Case-specific implementation**: Run n-BuMgBr with n-BuBr, n-BuCl, and allyl chloride each under standard conditions A ([NiCl₂(dpe)], diethyl ether, 0°C to reflux), and report yields of n-Bu-n-Bu (cross-coupling product, i.e., 1-butene dimerization product would be the homo-coupling product) and any other products by glpc; if product formation is zero, state the detection limit and whether starting material is recovered. This directly tests whether the sp² restriction is mechanistically grounded (β-hydride elimination from the alkyl-Ni intermediate would produce 1-butene rather than cross-coupled product) or is a kinetic preference.
* **Notes**: Members B-4 (sp² restriction announced as feature 2 without any failed reaction data, "substrate selection bias" flag, convergence=3/3 — highest in dataset), A-3 (scope extension explicitly deferred to future work). SRG-3 position in TEMPERATURE_SUMMARY: B-4 is the dataset's maximum-convergence item (V1=medium, V2=medium, V3=medium, convergence=3/3, gap=none). RI-07 is Primary because the sp² boundary is asserted without a single failure example — this is the canonical RI-07 case ("only X is possible" asserted without failure examples). RI-05 is Secondary because the qualitative ranking of sp² over sp³ reactivity is presented as a feature without numerical reactivity comparison.

---

**SRG-4 [Stereochemical outcome without analytical or mechanistic basis]**

* **Primary RI**: RI-04 [Unreplicated discriminator]
* **Secondary RI**: RI-01 [Reporting integrity]
* **ER**: For the non-stereospecific cis-stilbene-enriched product ratio (cis:trans = 80:20 from cis-1,2-DCE; cis:trans = 43:57 from trans-1,2-DCE) to carry the evidentiary weight of a "significant feature[REDACTED: substantial verbatim quotation; see Tier 9]partial stereochemical retention" from "near-random scrambling" (a ±5% band on the 43:57 result would span the full range from partial retention to statistical scrambling).
* **EP**: EP-04a [Discrimination / replication pack]; EP-01a [Reporting-coherence pack]
* **Case-specific implementation**: (EP-04a) Replicate the cis-1,2-DCE + PhMgBr and trans-1,2-DCE + PhMgBr reactions in triplicate under condition A; measure the cis:trans stilbene ratio in each replicate by ¹H NMR (coupling constants: J_cis ≈ 12 Hz, J_trans ≈ 16 Hz — directly accessible in 1972) with integration to ±2% and report the mean ± SD for each. (EP-01a) Specify whether Table I's reported ratios were measured by ¹H NMR, glpc on an achiral column, or another method, and disclose the calibration basis for glpc ratios if applicable.
* **Notes**: Members A-1 (explicit deferral of stereochemical and mechanistic details, T1), B-11 (analytical method for cis:trans ratio not stated, uncertainty estimate absent). Position in TEMPERATURE_SUMMARY: high_convergence_low_gap (A-1: V1=medium, V2=medium, convergence=2/3). RI-04 is Primary because the stereochemical ratios are single-determination data points with strong discriminatory power (feature 4 of the paper) that are interpreted mechanistically ("non-stereospecific") without analytical precision. RI-01 is Secondary because cross-comparison of the two DCE entries and comparison with subsequent mechanistic papers requires knowing the measurement method, which is not disclosed.

---

**SRG-5 [Yield data analytical quality]**

* **Primary RI**: RI-08 [Unquantified reliability]
* **Secondary RI**: RI-01 [Reporting integrity]
* **ER**: For the ten Table I yield values (76–98%) to support the claim "generally very high yields," each yield value must be accompanied by the analytical method used (glpc vs. isolated), the basis for glpc quantification (internal standard identity, response factor), and at least one replicate measurement demonstrating reproducibility within a defined error band.
* **EP**: EP-08a [Replication / uncertainty pack]; EP-01a [Reporting-coherence pack]
* **Case-specific implementation**: (EP-08a) For the highest-yield glpc entry (EtMgBr/PhCl, 98%) and the lowest-yield isolated entry (n-BuMgBr/PhCl, 76%), run each in triplicate and report mean ± SD for both glpc and isolated yields in the same experiment to determine whether glpc and isolation efficiencies diverge systematically for this substrate class. (EP-01a) Specify the internal standard (e.g., n-decane or dodecane commonly used in 1972 glpc quantification) and the response factor used for the five glpc-only entries.
* **Notes**: Members B-2 (mixed glpc/isolated yield basis without disclosure criteria, five glpc-only entries), B-7 ("and/or" characterization allowing single-method identity assignment), B-9 (no replication or standard deviations for any of the ten entries), B-11 (analytical method for cis:trans ratio unstated, absorbed here as measurement coherence failure). Position in TEMPERATURE_SUMMARY: high_convergence_low_gap (B-2: V1=medium, V3=medium, convergence=2/3). RI-08 is Primary because the absence of replication data means the precision of every yield value in Table I is undefined; RI-01 is Secondary because the mixed yield-reporting basis makes cross-entry comparison impossible without additional metadata.

---

**SRG-6 [Prior work numerical comparison gap]**

* **Primary RI**: RI-09 [External superiority]
* **Secondary RI**: RI-04 [Unreplicated discriminator]
* **ER**: For the superiority claim over prior cross-coupling methods to be established, at least one direct experimental comparison on a shared substrate must be performed — either a side-by-side yield comparison between [NiCl₂(dpe)] and the Tamura-Kochi Fe catalyst on n-BuMgBr + CH₂=CHCl, or a distinguishing experimental criterion between [NiCl₂(dpe)] and Ni(acac)₂ (the Corriu-Masse system) on any substrate in Table I.
* **EP**: EP-09a [Internal benchmark pack]
* **Case-specific implementation**: Run n-BuMgBr + CH₂=CHCl (Table I entry, Condition B, 95% glpc) under Tamura-Kochi Fe catalyst conditions (FeCl₃ or Fe(acac)₃ with appropriate Grignard stoichiometry from refs 5–6) in diethyl ether and in THF simultaneously with the [NiCl₂(dpe)] run, reporting product identity and glpc yield for both. For the Corriu-Masse comparison, run n-BuMgBr + PhCl under [NiCl₂(dpe)] and under Ni(acac)₂ conditions and report cross:homo yield ratio for each.
* **Notes**: Members C-1 (Tamura-Kochi cited without shared-substrate comparison, severed citation), C-2 (cuprate/allylnickel cited and set aside without numerical comparison), A-4 (Corriu-Masse Ni(acac)₂ acknowledged as [REDACTED: verbatim source quotation; see the source paper via its DOI] is the sole discriminator against the prior art without a measurement.

---

**Outside the SRGs: CLAs**

---

**CLA-1 [Catalyst turnover and catalytic efficiency claim]**

* **Primary RI**: RI-08 [Unquantified reliability]
* **ER**: For the paper's claim of "catalytic" character to be distinguished from near-stoichiometric reactivity, the turnover number (TON) must be reported, and the minimum catalyst loading at which full conversion is maintained must be determined.
* **EP**: EP-08a [Replication / uncertainty pack]
* **Case-specific implementation**: Run n-BuMgBr + m-DCB (Example 1 conditions) at [NiCl₂(dpe)]/organic-halide ratios of 10⁻¹, 10⁻², and 10⁻³ and report isolated yield and TON at each loading; this directly establishes whether the 10⁻²–10⁻³ mol% range in the paper represents genuine catalytic efficiency or a practical minimum.
* **Notes**: This CLA is grounded in B-1 (TON absent, "standard practice in catalytic chemistry") and B-3 (ligand activity ranking with no yield values — data exist but are not disclosed). The D-4 Candidate 8 analysis notes that a minimum TON of ~47 per Ni atom is calculable from the Example 1 data but is never stated. D-4 marks this as "not applicable[REDACTED: substantial verbatim quotation; see Tier 9]catalytic" vs. stoichiometric positioning) is not captured in any SRG's member_items. Position in TEMPERATURE_SUMMARY: high_convergence_low_gap (B-1: V1=medium, V3=low, convergence=2/3, gap=low).

---

**CLA-2 [Self-contradictory absence of homo-coupling byproduct — mechanistic dimension]**

* **Primary RI**: RI-03 [Unobserved explanatory]
* **Secondary RI**: RI-04 [Unreplicated discriminator]
* **ER**: For the proposed catalytic cycle to be internally consistent, the R–R homo-coupling product explicitly predicted by equation 3 (L₂NiR₂ + R'X'' → L₂Ni(R')(X'') + R–R) must either be detected and quantified in Table I reactions, or its absence must be explained by a kinetically grounded argument (e.g., R–R is formed transiently in the initiation step but is consumed faster than it accumulates, with a calculation or measurement supporting this claim).
* **EP**: EP-03a [Direct-observation / state-assignment pack]; EP-04a [Discrimination / replication pack]
* **Case-specific implementation**: For the EtMgBr + PhCl reaction (Table I, 98% glpc yield, cross-coupling product Ph-Et), perform a glpc scan of the crude reaction mixture for Et-Et (bp −89°C, volatile but identifiable if captured) and Ph-Ph (bp 255°C, distinguishable from Ph-Et by retention time); report the detection limit for each homo-coupling product. If Et-Et is below the detection limit (as expected given volatility), spike a known amount and confirm recovery to establish the analytical bound.
* **Notes**: U-1 is the primary item (self-contradictory absence — eq 3 predicts R–R as stoichiometric byproduct, yet no Table I entry or procedure mentions it). B-6 (reporting omission of cross:homo ratio) is the complementary reporting-perspective angle. SRG-2 develops the selectivity dimension; this CLA develops the mechanistic self-contradiction dimension separately. U-1 is the highest-severity U item (V2=high, V3=high, convergence=2/3). The self-contradictory-absence CLA check procedure in the Stage 3 prompt identifies this as the canonical case: [REDACTED: substantial verbatim quotation; see Tier 9] CLA-2 is not absorbed into SRG-1 (mechanism) or SRG-2 (selectivity) because it straddles both — it is mechanistically a RI-03 (unobserved species that the paper's cycle predicts) and comparatively a RI-04 (single interpretive claim — "selective" — without a discrimination experiment for the predicted byproduct).

---

### §3 Current VQ assessment

**Current judgment: VQ-2 (Method)**

---

**VQ-1 [Observation] — Assessment: Holds (non-fatal)**

Requirement: RI-02 (product or catalyst structure/purity established at a granularity excluding alternative candidates).

Product identity is established at a minimal but non-fatal level: two of the ten substrates receive full experimental procedures with bp, refractive index, and multi-technique characterization (glpc, nmr, ir, mass spectra per footnote c). For the remaining eight Table I entries, the "and/or[REDACTED: substantial verbatim quotation; see Tier 9]pure" designation in Example 1 (B-8) lacks a GC purity percentage, but the bp (84°/5 mm) is consistent with the literature. RI-02 is non-fatal: product identity is confirmable from the characterization provided, even if incomplete by modern standards. **VQ-1 holds**, with the non-fatal RI-02 residual in B-7 and B-8 noted.

---

**VQ-2 [Method] — Assessment: Holds (conditional)**

Requirements: RI-01 (cross-comparison requires consistent measurement frames) + RI-07 (boundary claims supported by failure examples). Inherits VQ-1.

RI-01: The mixed glpc/isolated yield-reporting basis (SRG-5, B-2) creates a non-standard measurement frame within Table I. However, the mixed-basis issue is non-fatal for VQ-2 because the qualitative claim "generally very high yields" is substantiated by both methods independently — even the lowest isolated yield (76%) and the lowest glpc-method yield (80%) are consistent with "high yield." RI-01 is therefore non-fatal at VQ-2: the inconsistency prevents precise cross-entry comparison but does not invalidate the method's principal yield claim.

RI-07: The sp² electrophile restriction (SRG-3, feature 2) is asserted without a single failure example (B-4, convergence=3/3). This is an unresolved RI-07. However, the scope boundary is presented with a mechanistic rationale (footnote 19 references the mechanism of sp² C–halogen bond activation) and the paper explicitly labels it as a current limitation. For VQ-2, the scope boundary claim is accepted as a method-level boundary statement, but it carries the qualifier that it is asserted rather than demonstrated. By the VQ decision matrix rules, RI-07 is required for VQ-2; its unresolved status means VQ-2 holds only conditionally — the method's scope claim is not definitively established.

On the premise that RI-02 is non-fatal (as established under VQ-1) and RI-01 is non-fatal at the method level, and accepting the RI-07 qualification: **VQ-2 holds (conditional on RI-07).**

**However, the solvent superiority layer (feature 5, "definitely superior[REDACTED: substantial verbatim quotation; see Tier 9]RI-07 extended use — negative boundary claims": "X is the most serious limitation" without data). This is also non-fatal at VQ-2 for the same reason: the method works in diethyl ether regardless of whether THF comparison data exist.

---

**VQ-3 [Mechanism] — Assessment: Fails**

Requirements: RI-03, RI-04, RI-06 (+ inherits VQ-2). RI-05 if in serious form → VQ-3 qualified.

RI-06: Unresolved. The three-step catalytic cycle (eqs 2–4) is wholly imported from stoichiometric (dipy)Ni chemistry (refs 11–12). No experiment under [NiCl₂(dpe)] catalytic conditions verifies the isomorphism. This is RI-06 at the cycle-level import scope (per the codebook scope note). **Fatal at VQ-3**: without cycle-level isomorphism verification, the mechanistic account cannot be accepted. (SRG-1, CLA-2)

RI-03: Unresolved. Intermediates 1 (L₂NiR₂) and 2 (L₂Ni(R')(X'')) are not characterized under catalytic conditions; the observation of a black precipitate (B-12, U-2) raises the additional possibility that the operative species is heterogeneous Ni⁰, an alternative explanatory entity that is neither observed nor ruled out. **Fatal at VQ-3.**

RI-04: Partially unresolved. The stereochemical ratios (cis:trans = 80:20 and 43:57, SRG-4, A-1, B-11) are single-determination data presented as a mechanistically significant "feature" without analytical uncertainty or replication. The selectivity claim (cross:homo ratio) is similarly a single-determination claim for each Table I entry with no discrimination experiment for the predicted R–R byproduct (CLA-2, U-1). **Non-fatal** individually, but in combination with RI-06 and RI-03 the mechanistic claim cannot be supported.

VQ-3 fails on RI-06 and RI-03. RI-04 is non-fatal in isolation but cannot rescue VQ-3 when the primary mechanistic framework is unvalidated.

**Note: However, the Synthetic utility layer on its own reaches VQ-2** without requiring VQ-3. The paper's three-layer architecture (§1) means that a refutation of VQ-3 does not collapse the synthetic utility layer. The utility layer — demonstrating that [NiCl₂(dpe)] in diethyl ether gives high yields of cross-coupled products from Grignard reagents and sp² halides — is supported by VQ-2 evidence independent of the mechanistic hypothesis.

---

**VQ-4 [Benchmark] — Assessment: Fails (prerequisite VQ-3 fails)**

Requirements: RI-08, RI-09 (+ inherits VQ-3). Not evaluable while VQ-3 fails. For the record: RI-08 (quantitative reliability) is unresolved across both Table I and the selectivity data (SRG-2, SRG-5); RI-09 (external superiority) is unresolved — no direct comparison with Tamura-Kochi on a shared substrate (SRG-6, C-1). Both would require resolution before VQ-4 could be assessed.

---

### §4 Era-Norm Annotation

**Communication-era tolerated:**

- **B-1 (TON absent):** JACS Communications in 1972 did not require turnover number reporting for catalytic cross-coupling methods; the field of cross-coupling catalysis was emergent and TON standards were not yet established. The disclaimer "The experimental conditions are not necessarily optimum" signals this is a preliminary report, accepted under communications norms.

- **B-2 (mixed glpc/isolated yield basis without disclosure criteria):** Mixed yield-reporting basis across a scope table was standard in 1972 synthetic chemistry communications; glpc quantification using internal standards was accepted as equivalent to isolated yield for volatile substrates. The internal standard identity and response factors were not required fields in JACS Communications of this era.

- **B-3 (ligand activity order without yield values):** Qualitative catalyst activity rankings without numerical supporting data in a communication were tolerated in 1972 organometallic chemistry; the expectation of a full numerical comparison across ligand series was a norm of full papers, not communications.

- **B-5 (THF "definitely superior[REDACTED: substantial verbatim quotation; see Tier 9]definitely") were accepted in communications in 1972 when the comparison was well-established by the authors' direct experience but not yet systematically documented; comparative yield data were reserved for the follow-up full paper.

- **B-7 ("and/or" characterization):** Footnote-compressed multi-technique characterization disclosure with "and/or" was standard JACS Communications practice in 1972; elemental analysis was the universal identity criterion for novel compounds in full papers but was routinely abbreviated in communications.

- **B-9 (no replication or standard deviations):** No JACS communication in this era required replicate experiments for yield reporting; the concept of statistical significance applied to synthetic yield data became a formal expectation only in the 1990s–2000s.

- **B-14 (reaction time without kinetic profile):** Reporting a fixed endpoint reaction time (20 hours) without a time-conversion profile was universal practice in synthetic communications of this era; kinetic profiling was reserved for mechanistic studies.

- **A-1, A-2 (mechanistic deferrals):** Explicit deferral of mechanistic and stereochemical characterization in a priority communication was not only tolerated but expected; the communication format was understood as a placeholder for mechanistic follow-up in the full paper.

---

**Modern-era deficient:**

- **B-2 (mixed yield basis) [dual classification]:** By modern analytical standards, mixed reporting of glpc and isolated yields within a single Table column without disclosure of the selection criterion and without internal standard specification is not acceptable in any journal; modern editors require uniform yield basis or explicit cross-validated comparison.

- **B-6 (homo-coupling product not reported or quantified):** By modern standards, a paper claiming selective cross-coupling must report the cross:homo ratio for at least the highest-yield and lowest-yield entries; the absence of homo-coupling product quantification is not acceptable in any 2024 submission claiming selectivity as a central criterion.

- **B-7 ("and/or[REDACTED: substantial verbatim quotation; see Tier 9]and/or" multi-technique footnote without specification of which method was applied to which compound would be rejected by modern reviewers.

- **B-11 (analytical method for cis:trans ratio unstated):** Reporting stereochemical ratios without specifying the measurement method (NMR vs. GC) and without uncertainty estimation is not acceptable in modern organic or organometallic chemistry; this is a RI-01 deficiency by present-day standards.

- **U-2 (black precipitate uncharacterized):** Modern mechanistic papers are required to address changes in catalyst appearance (particularly metal precipitation in homogeneous catalysis) with at least one characterization experiment (TEM, XRD, or SEM); the observation of a black mixture without any characterization would require explanation in a modern submission.

- **CLA-1 / B-1 (TON absent) [dual classification]:** Modern catalysis papers reporting a "catalytic" method are required to specify TON and turnover frequency (TOF); the absence of TON is a standard reviewer flag in modern submissions and would require resolution before publication in any current catalysis journal.

---

### §5 Shortest-reinforcement route

**First objective function: VQ-2 → VQ-3**

The three unresolved RIs for VQ-3 are RI-06 (imported model, cycle-level), RI-03 (unobserved intermediates), and RI-04 (unreplicated discriminator for stereo/selectivity data). The EP investment ordering by information gain and experimental feasibility:

```
**Shortest route to VQ-3:**

1. EP-06a [Analogy-validation pack] — Synthesize [NiCl₂(dpe)]-derived diorganonickel 
   intermediate 1 (L₂Ni(n-Bu)₂) by independent stoichiometric route and confirm it 
   reacts with PhCl to give Ph-n-Bu + n-Bu-n-Bu at the rate required for catalytic 
   turnover; this validates the (dipy)Ni → (dpe)Ni analogy (RI-06) and simultaneously 
   establishes the first direct evidence for a catalytic intermediate under conditions 
   relevant to Table I. Advances RI-06. (SRG-1, CLA-2)

2. EP-03a [Direct-observation / state-assignment pack] — Monitor [NiCl₂(dpe)] + 
   n-BuMgBr + PhCl by in situ ³¹P NMR in Et₂O; if intermediate 1 or 2 is detectable, 
   assign its structure; if the black precipitate appears before product formation, 
   characterize it by XRD or TEM as Ni⁰ metal. Advances RI-03. (SRG-1, U-2)

3. EP-04a [Discrimination / replication pack] — Replicate the cis-1,2-DCE + PhMgBr 
   and trans-1,2-DCE + PhMgBr reactions in triplicate; measure cis:trans ratios by 
   ¹H NMR (coupling constants directly accessible); report mean ± SD. Advances RI-04. 
   (SRG-4)

Certification-gate note: The experimental investment order above prioritizes 
information gain (EP-06a resolves the structurally heaviest RI and simultaneously 
advances two SRGs) and experimental feasibility (EP-03a in situ NMR is accessible 
with standard 1970s-era equipment), but the final VQ-3 certification is fixed by the 
gate order VQ-1 → VQ-2 → VQ-3 → VQ-4: VQ-2 must be confirmed first (including 
resolution of the RI-07 sp² boundary qualification), before VQ-3 certification is 
assessed.
```

**Second objective function: VQ-3 → VQ-4 (prerequisite: VQ-3 achieved)**

```
**Shortest route to VQ-4 (after VQ-3 achieved):**

1. EP-09a [Internal benchmark pack] — Run n-BuMgBr + CH₂=CHCl (Table I Condition B, 
   95% glpc yield) simultaneously under [NiCl₂(dpe)] and Tamura-Kochi Fe conditions 
   in identical solvent and stoichiometry; report cross-coupling yield and homo-coupling 
   yield (n-Bu-n-Bu) for both. Advances RI-09. (SRG-6)

2. EP-08a [Replication / uncertainty pack] — Run all ten Table I entries in triplicate 
   under standardized glpc quantification (disclosed internal standard, response 
   factors, detection limits for homo-coupling products); report mean ± SD for each. 
   Advances RI-08 across SRG-2 and SRG-5.

3. EP-07a [Boundary-test pack] — Run n-BuMgBr with n-BuBr, n-BuCl, and allyl 
   chloride under standard conditions; report yields and identify all products including 
   n-Bu-n-Bu and 1-butene. Advances RI-07. (SRG-3)

Certification-gate note: VQ-4 requires resolution of all VQ-3 prerequisites plus 
RI-08 and RI-09; gate order remains VQ-1 → VQ-2 → VQ-3 → VQ-4.
```

---

### §6 Contribution to institutional design

**New representative case for existing RI codes:**

- **RI-06 at cycle-level import (codebook scope note confirmed):** SRG-1 provides a clean representative case of cycle-level RI-06 import: the entire three-step Ni(0)/Ni(II) catalytic cycle is transposed from stoichiometric (dipy)Ni chemistry without testing isomorphism in the (dpe)Ni system. This confirms the codebook scope note: [REDACTED: substantial verbatim quotation; see Tier 9] The Kumada 1972 case is the canonical instance of this scope note.

- **RI-07 extended use (negative boundary claims confirmed):** The sp² electrophile restriction (SRG-3) is the canonical case of RI-07 in its "only X is possible" form combined with the "negative boundary claims" extension. Feature 2 of the paper asserts both: "only C_{sp²} halides can be used" (positive boundary) and implicitly "sp³ halides cannot be used" (negative boundary) without failure data for either direction. This confirms the codebook's extended use note for RI-07.

**Labeling mismatch pattern detected:**

The catalytic cycle (eqs 2–4) is explicitly labeled "a working hypothesis" in the penultimate paragraph, yet throughout the surrounding text the cycle is narrated with factual verbs: [REDACTED: substantial verbatim quotation; see Tier 9] The phrase "well-established fact" appears adjacent to the hypothesis label, applying factual language to a step (the Grignard transmetalation) whose operation in the [NiCl₂(dpe)] catalytic system has not been directly verified. The hypothesis label is concentrated in a single sentence near the end of the mechanistic discussion — precisely the pattern noted in §6 of the Stage 3 prompt ("hypothesis label concentrated in the final sentence"). This is the canonical labeling mismatch: the hypothesis label is present but functionally local, while factual-verb narration pervades the mechanism section.

**RI co-occurrence pattern — RI-06 + RI-03 in SRG-1:**

SRG-1 exhibits structural RI co-occurrence: RI-06 (imported cycle) and RI-03 (unobserved intermediates) both apply to the mechanistic layer, and resolving only RI-06 (by stoichiometric synthesis of intermediate 1 via EP-06a) would not resolve RI-03 (intermediates must additionally be observed under catalytic, not just stoichiometric, conditions). Conversely, in situ detection of intermediates (EP-03a) would resolve RI-03 but would not by itself validate the cycle-level analogy with (dipy)Ni (RI-06). Both EPs are required. This co-occurrence pattern is structurally analogous to the RI-04 + RI-06 co-occurrence noted in the codebook, but the specific form here (cycle-import + unobserved-catalytic-intermediate) is new and warrants a case-specific note in the EP dictionary.

**Incomplete negative evidence pattern (CLA-2):**

CLA-2 identifies a specific instance of the incomplete-negative-evidence pattern applicable to RI-04: the absence of R–R homo-coupling product in Table I is used implicitly as positive evidence for selectivity, but no mass-balance closure or detection-limit evaluation is reported. The "absence as evidence[REDACTED: substantial verbatim quotation; see Tier 9]negative experimental results are used as positive mechanistic evidence without mass-balance closure or kinetic-window evaluation." The Kumada 1972 case is distinctive in that the predicted byproduct (R–R) is volatile (Et-Et bp −89°C; n-Bu-n-Bu bp ~144°C) and could easily have been lost during workup, making the analytical silence doubly ambiguous. This case-specific implementation (volatility-driven absence ambiguity) should be added to the EP-04a dictionary.

**Automatic-resolution pattern via communication → Full Paper transition:**

The codebook notes the automatic-resolution pattern for RI-07 and RI-01 in the communication → full paper transition. For Kumada 1972, this pattern applies partially: B-2 (mixed yield basis), B-3 (ligand ranking without values), B-5 (THF comparison without data), and B-9 (no replication) are all format-constrained omissions that would be resolved automatically in a full paper. However, B-6 (homo-coupling product absence) and U-1 (self-contradictory byproduct prediction) are not format-constrained — they reflect a structural gap in the paper's experimental design that would require additional experiments, not just disclosure of existing data. The era-norm annotation in §4 confirms: B-6 and U-1 are in the "modern-era deficient" category, not the "communication-era tolerated" category, which means they would not be automatically resolved even in a full paper that retained the same experimental scope.

**PRI candidate proposal:**

No new pattern requiring a new PRI candidate was detected. The mechanism-selectivity self-contradiction (CLA-2, U-1) is structurally covered by the existing RI-03 / RI-04 co-occurrence framework. PRI-10 (kinetic overclaim) is not triggered: the paper makes no absolute rate enhancement claim. PRI-11 (mechanism–kinetics decoupling) is not fully triggered because the paper does not derive a rate law even informally, but this is a distinction of scope rather than a new pattern — PRI-11's definition [REDACTED: substantial verbatim quotation; see Tier 9] requires at least an observed rate order, which the paper does not provide. The Kumada 1972 case falls below the PRI-11 floor: it is a mechanism supported entirely by analogy, not even by rate-order matching.

**No Stage 2F input present — single-paper mode confirmed.**

---

> **Tier 8 redaction notice**: This file is a redacted copy of the corresponding Tier 3 / Tier 9 output. Verbatim source-paper quotations have been replaced by `[REDACTED: see source paper §<loc>; full text retained in Tier 9 reviewer-only deposit]` markers, preserving location references and our own analytical content. Bibliographic fields (title, authors, journal, year, DOI), analytical labels (`evidence_chain:` with B-/U-/A-/C- internal IDs), short technical terms, and our own analytical text are not redacted. The redaction was applied by `scripts/redact_for_tier8.py` and, for this version, by `scripts/build_paperA_R1_public.py` with `scripts/redact_source_ngram_runs.py` (scripts of the project repository; they are not deposited).
