```
prompt_version: stage3-v2-en-20260419
model_info: claude-sonnet-4-6
```

# Re-certification Assessment Sheet for Scientific Knowledge

## Tamao, Sumitani, Kumada 1972 (Journal of the American Chemical Society, communication)

---

### §1 Claim Architecture

**Core claim summary:**

The paper advances two interlocked pillars. The **Novelty pillar** is the demonstration that [NiCl₂(dpe)], a well-defined nickel(II)-bidentate-phosphine complex, functions as a catalyst for selective carbon–carbon bond formation between Grignard reagents and sp² organic halides — a class of transformation that prior transition-metal-catalyzed couplings could not achieve without generating substantial homo-coupling and disproportionation side products. Within this novelty pillar, the paper additionally proposes a three-step catalytic cycle (eqs 2–4) in which a diorganonickel intermediate undergoes selective reductive elimination, with the bidentate ligand's enforced cis geometry claimed as the structural explanation for selectivity. The **Utility pillar** is the synthetic accessibility claim: ten substrate combinations (Table I) give "generally very high" yields, including primary alkylmagnesium reagents bearing β-hydrogen atoms and using inexpensive sp² chlorides as electrophiles — substrates and functional groups that previous methods handled poorly.

The paper's opening sentence encapsulates both pillars simultaneously: [REDACTED: substantial verbatim quotation; see Tier 9]

**Layered structure judgment:**

The paper contains three structurally independent claim layers with partially shared evidentiary foundations:

- **Layer I (Synthetic utility):** Yield values in Table I for ten substrate combinations. Falsifiable by yield-counterexample or failed replication. Does not depend logically on the mechanistic model being correct.
- **Layer II (Substrate/catalyst features):** The five "significant features" (β-H-tolerant Grignard scope, sp² restriction, bidentate phosphine activity ranking, stereochemical anomaly, solvent preference). Falsifiable by scope or ligand counterexample. Partially independent of Layer I in that some features (esp. feature 3, activity ranking) are stated without the underlying yield data.
- **Layer III (Mechanistic working hypothesis):** The three-step catalytic cycle (eqs 2–4), explicitly designated "working hypothesis." Insulated from falsification within the paper by the deferral label; depends on analogy with (dipy)Ni stoichiometric reactions.

**Independent-layer verdict:** A single refutation (e.g., demonstrating that sp³ alkyl halides do react, or that the active catalyst is heterogeneous Ni⁰) would collapse Layer III and significantly undermine Layer II, but Layer I (isolated yield values in Table I) could survive mechanistic revision. The paper does not assert that its mechanistic model must be correct for the preparative claim to hold. However, because the selectivity claim (cross-coupling over homo-coupling, the central novelty) is not independently quantified — it depends partly on the absence of homo-coupling product, which is itself what the mechanistic model should predict (but predicts as present in eq 3) — Layers I and III are linked by a self-contradictory absence (U-1). This creates a dependency: if the mechanistic cycle generates R–R at the rate predicted by eq 3, then the "very high yields" in Table I may be cross-coupling product mixed with unquantified homo-coupling, making Layer I's yield values themselves ambiguous. The layers are therefore **conditionally independent**: Layer I stands independently only if the cross:homo selectivity it implies is taken at face value, which it cannot be without quantitative selectivity data.

---

### §2 SRG / CLA → RI / ER / EP Crosswalk

**2a. SRGs from Stage 1 Turn 4 (taken as given):**

SRG-1: Catalytic mechanism evidence gap (A-2, U-1, U-2, B-12)
SRG-2: Cross/homo-coupling selectivity quantification (B-6, U-1, C-1)
SRG-3: Scope restriction without negative-result evidence (B-4, A-3)
SRG-4: Stereochemical outcome and its mechanistic basis (A-1, B-11)
SRG-5: Yield data analytical quality (B-2, B-7, B-9, B-11)
SRG-6: Prior work numerical comparison gap (C-1, C-2, A-4)

**2b. CLA candidate identification:**

Candidates from Stage 2 D-4 not captured by SRG member_items:

- **Candidate 7** (B-3, B-5): Catalyst activity ranking without numerical values + solvent superiority claim without matched-pair data. B-3 and B-5 are not member_items of any SRG. Both satisfy the CLA criteria: directly bear on whether the paper's structure-activity and solvent preference claims hold (tied to features 3 and 5, which are presented as novelty-supporting features), and their grounded_in items are not captured in existing SRG member_items. Record as **CLA-A**.

- **Candidate 8** (B-5 alone): The solvent superiority "definitely" claim is already captured under CLA-A via B-5. No separate CLA warranted.

- **Self-contradictory-absence CLA check:** U-1 (homo-coupling byproduct absent from Table I despite being predicted by eq 3) is captured by SRG-1 and SRG-2. U-2 (black precipitate consistent with Ni⁰, not characterized) is captured by SRG-1. U-3 (bis-alkylation selectivity for dichlorobenzene entries) — the absence of monoalkylation product intermediates in Table I is not captured by any SRG. B members involved: none listed in B-items directly; the observation arises from the three dichlorobenzene entries (89/94/95% yield for o-/m-/p-DCB). This constitutes a self-contradictory-absence pattern: the paper claims "selective cross-coupling" yet the reaction of n-BuMgBr with dichlorobenzene produces exclusively bis-alkylated product without reporting sequential selectivity. Record as **CLA-B** (U-3 only, no B-item overlap with existing SRGs).

---

**2c. RI mapping:**

---

**SRG-1 [Catalytic mechanism evidence gap]**
Members: A-2, U-1, U-2, B-12

* **Primary RI**: RI-06 [Imported model] — The entire three-step catalytic cycle (eqs 2–4) is constructed by analogy from stoichiometric (dipy)Ni reactions (refs 11–12); no elementary step has been verified under [NiCl₂(dpe)] catalytic conditions. This is a cycle-level import (see RI-06 scope note), not merely an analogy between individual steps.
* **Secondary RI**: RI-03 [Unobserved explanatory] — Intermediates 1, 2, and 3 are proposed as the active species in the catalytic cycle, but none is directly observed under catalytic turnover conditions. The black precipitate (B-12/U-2) is an unexplained observation consistent with collapse to a different active species (Ni⁰), which would constitute a second form of RI-03 subtype: "observed yet unutilized" — the black color is recorded but its implications for catalyst identity are not extracted.
* **ER**: The mechanistic model requires direct observation or kinetic constraint of at least one proposed intermediate (1, 2, or 3) under [NiCl₂(dpe)] catalytic conditions, and requires that the black precipitate observation be characterized to establish whether the active catalyst is homogeneous or heterogeneous.
* **EP**: EP-03a [Direct-observation / state-assignment pack]; EP-06a [Analogy-validation pack]
* **Case-specific implementation**: EP-03a: Characterize the black precipitate in Example 1 by TEM/XRD for Ni⁰ nanoparticles and/or by PXRD for NiCl₂ or other Ni(I)/Ni(II) species; isolate and characterize intermediate 1 (L₂NiR₂) under stoichiometric conditions with [NiCl₂(dpe)] + 2 RMgBr. EP-06a: Demonstrate that [NiCl₂(dpe)] and (dipy)Ni₂ give the same rate orders and intermediate distribution on at least one shared substrate to validate the cycle-level analogy, or alternatively show that the [NiCl₂(dpe)]/Ni(acac)₂ comparison (concurrent Corriu-Masse) gives the same product distribution, which would provide indirect validation of the Ni(II)/Ni(0) cycle generality.
* **Notes**: A-2 (V1=high, V2=high; convergence=2/3) is the highest combined weight item in TEMPERATURE_SUMMARY. U-1 sits in both SRG-1 and SRG-2 (shared via B-6 link). U-2/B-12 constitute the RI-03 subtype "observed yet unutilized." The co-occurrence of RI-06 and RI-03 in SRG-1 means resolving only the imported-model problem (RI-06) via RI-06 analogy validation does not resolve whether the active catalyst is the proposed Ni(II) species (RI-03). Both must be addressed independently.

---

**SRG-2 [Cross/homo-coupling selectivity quantification]**
Members: B-6, U-1, C-1

* **Primary RI**: RI-04 [Unreplicated discriminator] — The selectivity claim (cross-coupling over homo-coupling) is supported by a single pattern of evidence: the absence of homo-coupling products from Table I. This single negative-result datum carries the full discriminatory weight of the paper's central contribution, but is presented without quantification (no cross:homo ratio) and without a detection-limit statement that would allow "not detected" to be interpreted as a reliable measurement.
* **Secondary RI**: RI-09 [External superiority] — The improvement over Tamura-Kochi is claimed on the basis of the prior literature's "substantial amounts" of homo-coupling products; no direct comparison on a shared substrate under both systems is provided.
* **ER**: The selectivity claim requires either (a) a quantitative cross:homo product ratio for at least one Table I entry, with a stated glpc detection limit, or (b) a direct comparative experiment on a shared substrate (e.g., n-BuMgBr + PhCl) under both Tamura-Kochi and Ni-dpe conditions.
* **EP**: EP-04a [Discrimination / replication pack]; EP-09a [Internal benchmark pack]
* **Case-specific implementation**: EP-04a: For the EtMgBr/PhCl entry (98% glpc yield), quantify Et-Et and Ph-Ph homo-coupling byproducts by glpc against an independent standard; report the detection limit of the glpc analysis. EP-09a: Run n-BuMgBr + vinyl chloride under Tamura-Kochi Fe/THF conditions and [NiCl₂(dpe)]/Et₂O conditions in the same laboratory; report cross:homo ratio and yield for both.
* **Notes**: U-1 is the self-contradictory-absence item: eq 3 mechanistically predicts R–R homo-coupling as a byproduct, yet R–R is never reported or bounded. B-6 (V2=high, V3=high; convergence=2/3) in TEMPERATURE_SUMMARY high_convergence_low_gap. C-1 links the selectivity gap to the prior-art comparison gap. The U-1 self-contradiction elevates the lethality level of this SRG's gap: if eq 3 is operative, R–R must be present; its absence without a detection-limit statement is a potential internal inconsistency at the data level (RI-08 subtype "internal inconsistency" also applies as tertiary RI).

---

**SRG-3 [Scope restriction without negative-result evidence]**
Members: B-4, A-3

* **Primary RI**: RI-07 [Unsupported boundary] — The restriction [REDACTED: substantial verbatim quotation; see Tier 9] is stated categorically without a single reported failed experiment with an sp³ alkyl halide. The exclusion is presented as a feature (feature 2) rather than as a tested limit.
* **Secondary RI**: (none — RI-07 captures the pattern fully; A-3's scope deferral is a prospective acknowledgment, not a separate RI pattern)
* **ER**: The sp² scope boundary requires at least one reported negative result: an sp³ alkyl halide (e.g., n-hexyl chloride, cyclohexyl bromide) attempted under the standard Condition A with [NiCl₂(dpe)], with the product yield (or its absence) and the detection limit reported.
* **EP**: EP-07a [Boundary-test pack]
* **Case-specific implementation**: EP-07a: Attempt the coupling of n-BuMgBr with n-hexyl chloride under Condition A ([NiCl₂(dpe)], Et₂O, 0° to reflux, 20 h); characterize the product mixture by glpc. Report the yield of n-Bu–hexyl cross-coupling product and of n-Bu–n-Bu homo-coupling product; if no cross-coupled product is detected, report the glpc detection limit and confirm that starting material is recovered. A second substrate (cyclohexyl bromide) would establish whether the sp³ exclusion is universal or substrate-class-dependent.
* **Notes**: B-4 (V1=medium, V2=medium, V3=medium; convergence=3/3) is the single item with highest convergence in TEMPERATURE_SUMMARY. A-3 provides the explicit prospective acknowledgment. The A-3 ↔ B-4 pivot structure identified in D-4 priority_structure is the prototypical RI-07 pattern: the absence of negative-result data functions as the structural precondition for the "extension" deferral. Communication-era context: in 1972, reporting failed substrates was not a standardized requirement for scope communications; this item classifies as communication-era tolerated / modern-era deficient (see §4).

---

**SRG-4 [Stereochemical outcome and its mechanistic basis]**
Members: A-1, B-11

* **Primary RI**: RI-01 [Reporting integrity] — The cis:trans stilbene ratios (80:20 from cis-DCE; 43:57 from trans-DCE) are presented in Table I without specifying the analytical method (¹H NMR, glpc retention time differentiation, or other), preventing independent evaluation of the measurement uncertainty.
* **Secondary RI**: RI-05 [Qualitative overread] — The mechanistic interpretation of the anomalous cis-enrichment from both isomers as "rather nonstereospecifically" deriving from the same pathway is a qualitative structural inference derived from two ratio values without kinetic or isotopic evidence for the pathway responsible.
* **ER**: The stereochemical data require (a) specification of the analytical method for cis/trans ratio determination and its uncertainty, and (b) a mechanistic account of why both isomers produce cis-enriched stilbene — at minimum, a discrimination between kinetic control at reductive elimination versus post-formation isomerization.
* **EP**: EP-01a [Reporting-coherence pack]; EP-05a [Quantitative-ranking substantiation pack]
* **Case-specific implementation**: EP-01a: State for both the cis-DCE and trans-DCE entries in Table I which analytical method was used to determine the cis:trans ratio (e.g., ¹H NMR integration of vinyl protons at δ 6.5 ppm for cis vs 6.9 ppm for trans); report the ±uncertainty. EP-05a: Vary the reaction temperature for the PhMgBr/cis-DCE coupling (0°, room temperature, reflux) and report whether the cis:trans ratio changes — thermodynamic vs. kinetic control discrimination.
* **Notes**: A-1 (V1=medium, V2=medium; convergence=2/3). B-11 (V3=medium; convergence=1/3). The secondary RI-05 flag is a "qualified" marker at VQ-3 (see §3). Note [REDACTED: verbatim source text; see the source paper via its DOI]") is a positive synthetic reframe of the anomalous result — a labeling mismatch for §6 (the authors present a mechanistic anomaly as a synthetic opportunity without providing a mechanistic explanation).

---

**SRG-5 [Yield data analytical quality]**
Members: B-2, B-7, B-9, B-11

* **Primary RI**: RI-08 [Unquantified reliability] — Multiple quantitative claims (ten yield values, two cis:trans ratios) lack the analytical metadata required to evaluate reliability: no replication data for any entry, mixed yield-reporting bases without calibration information, and ambiguous product characterization method.
* **Secondary RI**: RI-01 [Reporting integrity] — The mixed isolated/glpc yield system creates an internal reporting-coherence failure: the five glpc-only entries (98%, 95%, 95%, 89%, 80%) are the highest-yield entries, but their yield basis is different from the isolated yield entries, and the internal standard, response factors, and calibration protocol are absent.
* **ER**: The analytical foundation of the yield claims requires (a) uniform yield-reporting basis or a documented justification for the dual-basis system, (b) disclosure of the glpc internal standard and response factors for the glpc-based entries, and (c) at minimum duplicate experiments for the two highest-yield entries (EtMgBr/PhCl, 98% glpc; n-BuMgBr/m-DCB, 94% isolated) to establish reproducibility.
* **EP**: EP-08a [Replication / uncertainty pack]; EP-01a [Reporting-coherence pack]
* **Case-specific implementation**: EP-08a: Repeat the EtMgBr/PhCl coupling (Condition A) in triplicate; report mean glpc yield and standard deviation; disclose the identity of the internal standard and the glpc response factor for Ph-Et. EP-01a: For the five glpc-only entries, either isolate the product and report both isolated and glpc yields to demonstrate agreement, or add a footnote explaining why isolation was not attempted and confirming that all glpc yields were determined with the same calibration protocol.
* **Notes**: B-2 (V1=medium, V3=medium; convergence=2/3). B-9 (V3=medium; convergence=1/3). B-11 is shared with SRG-4 (ratio-determination method). SRG-5 is the analytical-foundation SRG that underlies the quantitative claims in SRG-2 (selectivity) and Layer I (synthetic utility). If SRG-5 is unresolved, the yield values in Table I cannot be independently verified, making the entire synthetic-utility pillar of the paper analytically ungrounded.

---

**SRG-6 [Prior work numerical comparison gap]**
Members: C-1, C-2, A-4

* **Primary RI**: RI-09 [External superiority] — The paper's improvement claim over Tamura-Kochi, cuprate/allylnickel reagents, and the concurrent Corriu-Masse Ni(acac)₂ system is based entirely on citations and qualitative assertions, without any direct comparison on a shared substrate.
* **Secondary RI**: (none — RI-09 captures all three comparison gaps equally)
* **ER**: At least one comparison on a shared substrate is required to establish the superiority claim quantitatively: n-BuMgBr + vinyl chloride under both Tamura-Kochi Fe/THF and [NiCl₂(dpe)]/Et₂O conditions; or [NiCl₂(dpe)] vs. n-Bu₂CuLi on at least one aryl chloride substrate.
* **EP**: EP-09a [Internal benchmark pack]
* **Case-specific implementation**: EP-09a: Run n-BuMgBr + vinyl chloride under Tamura-Kochi conditions (FeCl₃, THF, 0°C) and under Ni-dpe conditions (Condition B) in the same laboratory session; report the cross:homo product ratio and the n-Bu-CH=CH₂ yield for both. For the concurrent Corriu-Masse comparison: run PhMgBr + PhCl under Ni(acac)₂ (no phosphine ligand) and under [NiCl₂(dpe)] conditions; compare Ph-Ph homo and Ph-Et cross product distributions.
* **Notes**: C-1 (V1=low; convergence=1/3). A-4 (V1=low; convergence=1/3). SRG-6 is the lowest-temperature SRG but carries structural significance for the priority claim: the Corriu-Masse Note Added in Proof (A-4) introduces an unresolved novelty question about whether the phosphine ligand is specifically enabling (Ni-dpe) or whether Ni(II) generally suffices (Ni(acac)₂) — without the EP-09a comparison, this question cannot be answered from the paper.

---

**Outside the SRGs: CLAs**

---

**CLA-A: Catalyst activity ranking and solvent superiority claim without quantitative data**
Grounded in: B-3, B-5 (Stage 2 D-4 Candidate 7)

* **Primary RI**: RI-05 [Qualitative overread] — The activity ranking ([NiCl₂(dpp)] > [NiCl₂(dpe)] > [NiCl₂(dmpe)] ≈ [NiCl₂(PPh₃)₂] ≫ ...) is stated as an ordinal list derived from a single test reaction (n-BuMgBr + PhCl, footnote 21), and the structural inference — [REDACTED: substantial verbatim quotation; see Tier 9] — is directly drawn from this ranking without the numerical yield values that would establish the magnitude of the differences. The solvent superiority "definitely" (B-5) applies the same qualitative-overread pattern: the certainty marker exceeds the strength of the underlying data (no THF-based experiment with [NiCl₂(dpe)] is reported).
* **Secondary RI**: RI-07 [Unsupported boundary] for B-5 specifically: "definitely superior" constitutes a boundary claim of the form "THF does not work" made without a reported failed experiment.
* **ER**: The activity ranking requires the numerical yield values for all six catalysts on the test reaction (n-BuMgBr + PhCl); the structural inference from the ranking requires intermediate characterization evidence (linking to SRG-1/EP-03a). The solvent superiority claim requires a matched-pair experiment: the same substrate + [NiCl₂(dpe)] in Et₂O vs. THF.
* **EP**: EP-05a [Quantitative-ranking substantiation pack]; EP-07a [Boundary-test pack]
* **Case-specific implementation**: EP-05a: Provide the glpc yield for each of the six catalysts in the n-BuMgBr/PhCl test reaction from footnote 21; the ranking without numbers cannot be verified or reproduced. EP-07a: Run n-BuMgBr + PhCl under [NiCl₂(dpe)] catalysis in THF (replacing Et₂O); report the yield and selectivity outcome to establish whether THF is "definitely" inferior or merely less optimal.
* **Notes**: B-3 (V1=medium, V2=medium; convergence=2/3). B-5 (V1=low, V2=low; convergence=2/3). CLA-A sits outside the SRGs because B-3 and B-5 are not member items of any SRG; they are cross-cutting to SRG-1 (the mechanistic interpretation of the ranking depends on the catalytic cycle of SRG-1) and to SRG-3 (the solvent exclusion of THF parallels the sp³ substrate exclusion of SRG-3 — both are negative-result-free boundary claims).

---

**CLA-B: Bis-alkylation selectivity in dichlorobenzene entries**
Grounded in: U-3

* **Primary RI**: RI-07 [Unsupported boundary] — The three dichlorobenzene entries (n-BuMgBr + o-/m-/p-DCB, 89/94/95% yield) report exclusively bis-alkylated products in Table I, but the paper does not acknowledge or explain the complete absence of mono-alkylated products. The claim of "selective cross-coupling" extends implicitly to sequential selectivity (both C–Cl bonds activated), yet this mechanistically distinct aspect is presented without data (yield of mono-alkylated intermediate, glpc trace showing intermediate, kinetic time course).
* **Secondary RI**: (none — the gap is entirely a boundary/scope assertion without negative-result evidence for the intermediate)
* **ER**: The bis-alkylation selectivity claim (both C–Cl bonds of DCB are alkylated, not one) requires either a report of the mono-alkylated intermediate yield at intermediate conversion, or a statement that the mono-alkylated product is not detected above the glpc detection limit.
* **EP**: EP-07a [Boundary-test pack]
* **Case-specific implementation**: EP-07a: Run n-BuMgBr (1.1 equiv per C–Cl bond, i.e., 1.1 equiv total) + m-DCB under Condition A and monitor by glpc at t = 1, 5, 10, and 20 h; report the ratio of mono-butylated, di-butylated, and unreacted m-DCB at each time point to establish whether the first alkylation is rate-determining or whether the second alkylation is faster than the first (consistent with the product distribution observed).
* **Notes**: U-3 (V1-Q10; convergence=1/3; severity=low). CLA-B is a low-priority item but represents a gap in the paper's "selective cross-coupling" claim that is distinct from SRG-2 (cross vs. homo selectivity): it concerns selectivity within the sequential activation of a bis-electrophile substrate, which the paper reports but does not analyze.

---

### §3 Current VQ assessment

**Current judgment: VQ-1 (Observation) — qualified pass; VQ-2 (Method) fails.**

---

**VQ-1 [Observation]: Qualified pass.**

Grounds: RI-02 (product identity / purity substantiation) is addressed at minimum level by the paper: products are characterized by "glpc, nmr, ir, and/or mass spectra" (B-7), and the two detailed examples (m-di-n-butylbenzene and α-vinylnaphthalene) are characterized with bp and refractive index. The "and/or[REDACTED: substantial verbatim quotation; see Tier 9]pure" designation without a GC purity percentage or elemental analysis (B-8) and the glpc-retention-time-based identification for the five glpc-only entries leaves the identity claim weakly established for part of the substrate scope. **Non-fatal assessment**: product identity for the two detailed examples reaches VQ-1; for the glpc-only entries, RI-02 is partially unresolved. The qualified pass reflects that the core products of the method are plausibly identified, but not all ten Table I entries are identically substantiated.

---

**VQ-2 [Method]: Fails.**

VQ-2 inherits the VQ-1 qualified pass and requires resolution of RI-01 and RI-07.

*RI-01 (Reporting integrity)*: SRG-5 shows that the yield-reporting system mixes isolated yields and glpc-based yields in a single column without calibration metadata. The two cis:trans ratios lack the analytical method specification (B-11). These are unresolved RI-01 deficiencies: a reader cannot reconstruct the measurement process from the paper's reporting. **Fatal by modern standards** (see §4).

*RI-07 (Unsupported boundary)*: SRG-3 shows that the sp² restriction is asserted without a single reported failed experiment with an sp³ halide (B-4). CLA-A shows that the THF inferiority claim (B-5) uses the certainty marker "definitely" without a single reported THF-based experiment with [NiCl₂(dpe)]. Both are RI-07 violations. **Fatal by modern standards for a scope claim** (see §4).

VQ-2 fails on two independent RI grounds (RI-01 via SRG-5, RI-07 via SRG-3 and CLA-A). Because VQ-2 fails, VQ-3 and VQ-4 cannot be certified.

---

**VQ-3 [Mechanism]: Cannot be certified (VQ-2 prerequisite not met).**

For reference: the mechanistic claim would additionally require resolution of RI-03 (SRG-1 primary: unobserved intermediates 1, 2, 3), RI-06 (SRG-1 secondary: cycle imported from (dipy)Ni without isomorphism validation), and RI-04 (SRG-2 primary: unreplicated selectivity discriminator). RI-05 remains in qualified form (CLA-A's activity ranking overread; SRG-4 secondary). If these were addressed, VQ-3 would be "qualified" due to RI-05.

**Per-layer asymmetry (Layer I):** The synthetic utility layer (Layer I, Table I yield data) on its own has a clearer path toward a higher VQ level once RI-01 (yield-reporting coherence) and RI-08 (replication) are resolved. **Layer I on its own: could reach VQ-2 → VQ-4 (Benchmark)** if yield data were replicated and an internal benchmark comparison with one prior method were provided — Layer I has no mechanistic dependency that would block VQ-4. The paper's weakest layer is Layer III (mechanism), which is blocked at VQ-3 by RI-06 and RI-03.

---

**VQ-4 [Benchmark]: Cannot be certified (VQ-2 and VQ-3 prerequisites not met).**

For reference: SRG-6 (RI-09) and SRG-2 (RI-09 secondary) would additionally require resolution for VQ-4 — quantitative comparison with Tamura-Kochi and the concurrent Ni(acac)₂ system on shared substrates.

---

### §4 Era-Norm Annotation

**Communication-era tolerated:**

- **B-9** (no replicate measurements, single-determination yields in Table I): In 1972, reporting single-determination yields for all entries in a JACS Communication was standard practice. Replication data for all substrate combinations would require a length that the communication format did not accommodate. Non-fatal in 1972 context; tolerated as preliminary data.

- **B-7** (characterization by "glpc, nmr, ir, and/or mass spectra" without per-product method disclosure): The "and/or" footnote convention was common for JACS Communications in this period. A full article would have specified individual product characterization; the communication format allowed this summary level. Tolerated.

- **B-1** (no TON values or catalyst loading optimization curve): In 1972, TON values were not a mandatory reporting element for catalytic cross-coupling communications; the concept of TON as a standard metric for assessing catalytic efficiency in organometallic chemistry was not yet institutionalized at the level it would be from the 1980s onward. Tolerated.

- **B-3** (catalyst activity ranking without numerical yield values): The qualitative ranking convention for catalyst screening in a communication was standard — the rankings were used as summary evidence in a format where full tables of screening data were assigned to full papers. Tolerated in 1972; the activity order itself (dpp > dpe > dmpe ≈ PPh₃ ≫ PEt₃ ≈ PPh₂Me) has been confirmed in subsequent literature and is no longer contested.

- **B-8** (bp/nD physical constants without GC purity or elemental analysis, "pure" designation without substantiation): In 1972, isolated yield with consistent bp and nD was a widely accepted purity indicator for liquid organics in synthetic communications. The boiling point comparison with a cited literature value functions as an indirect purity check. Tolerated.

- **C-1** / **SRG-6** (qualitative prior-work comparison without direct head-to-head experiment on shared substrate): Communication-format precedents of the era allowed implicit rather than explicit quantitative comparison with cited prior methods. The brevity constraint made matched-pair experiments impractical to report, and the novelty of the system (Ni-phosphine as a class) was assumed to be self-evident from the scope demonstration.

**Modern-era deficient:**

- **B-4 / SRG-3** (sp² restriction asserted without any reported failed sp³ substrate — RI-07): Modern scope communications in ACS journals require at least representative failed substrates to substantiate a scope exclusion. The categorical "Only C_sp² halides can be used" without a single negative datum is not acceptable in a 2024 substrate-scope table. **Lethal by modern standards** for the scope claim's precision; the sp³ exclusion would need to be established by at least two to three failed sp³ substrate examples.

- **B-2 / SRG-5** (mixed isolated/glpc yield basis in a single Table I column without calibration metadata — RI-01 + RI-08): Modern data reporting standards require uniform yield-reporting basis or explicit disclosure of both bases per entry, along with the glpc calibration data (internal standard identity, response factors). A single-column mixed-basis yield table with five entries of unexplained glpc-only reporting is not acceptable in a modern full paper or communication. **Non-fatal to the existence of the reaction, but fatal to the analytical credibility of the yield values.**

- **B-5 / CLA-A** (solvent superiority "definitely[REDACTED: substantial verbatim quotation; see Tier 9]definitely") require the data that establish the certainty. The absence of a single THF-based experiment with [NiCl₂(dpe)] makes the claim unverifiable. **Non-fatal to the synthetic utility claim, but unsupported as stated.**

- **B-6 / SRG-2** (central cross-coupling selectivity claim without a cross:homo product ratio or detection-limit statement — RI-04): By contemporary standards, the central novelty of a cross-coupling paper (selective over homo-coupling) must be quantified by a cross:homo ratio or percent yield of byproducts. The complete absence of any selectivity quantification, combined with the U-1 self-contradictory absence (eq 3 predicts R–R), constitutes a modern-era deficiency that is also doubly classified: tolerated in 1972 (the "selective" claim was accepted on the basis of visual inspection or qualitative glpc), but deficient by modern standards. **Record in both tags.**

- **B-6 (dual classification)**: The absence of a cross:homo ratio was tolerated in a 1972 communication claiming novelty in a new catalyst class, but it is deficient by modern standards because it leaves the central contribution (selectivity) without quantitative grounding. Any modern communication claiming selective cross-coupling must provide at least one selectivity data point.

- **B-11 / SRG-4** (cis:trans ratios without analytical method specification — RI-01): Modern analytical reporting of product ratios requires specification of the analytical method and its estimated uncertainty. The omission of the analytical method for the cis:trans stilbene ratio is not acceptable in a modern communication. **Non-fatal to the qualitative observation (cis enrichment is observed), but fatal to the quantitative precision of the ratio values.**

- **U-1 / SRG-2** (self-contradictory absence — eq 3 predicts R–R homo-coupling product, but none is detected or quantified): The internal inconsistency between the mechanistic model and the reported data is not era-dependent; it is a logical inconsistency that applies equally to 1972 and modern standards. **Lethal as stated**: either the mechanistic model (eq 3) is incorrect, or the homo-coupling product exists below a detection limit that must be stated. This item is modern-era deficient and was also deficient by 1972 standards, though reviewers of the era did not flag it as such.

---

### §5 Shortest-reinforcement route

**5a. Objective-function setting:**

*Current VQ level*: VQ-1 (qualified pass)
*First objective function*: VQ-2 [Method] — requires resolution of RI-01 (SRG-5, SRG-4) and RI-07 (SRG-3, CLA-A)
*Second objective function*: VQ-3 [Mechanism] — additionally requires resolution of RI-03 (SRG-1), RI-06 (SRG-1), RI-04 (SRG-2)
*Third objective function (reach)*: VQ-4 [Benchmark] — additionally requires resolution of RI-09 (SRG-6, SRG-2 secondary)

---

**Shortest route to VQ-2:**

1. **EP-07a [Boundary-test pack]** — Attempt coupling of n-BuMgBr with n-hexyl chloride under Condition A ([NiCl₂(dpe)], Et₂O, 0° to reflux, 20 h) and separately run [NiCl₂(dpe)] + n-BuMgBr + PhCl in THF instead of Et₂O; report product yields and detection limits for both experiments.
   Advances RI-07 (SRG-3: sp² restriction; CLA-A: THF inferiority). Two negative-result experiments together resolve both RI-07 violations.

2. **EP-01a [Reporting-coherence pack]** — For the five glpc-only entries, disclose the internal standard identity and glpc response factors; for the cis- and trans-DCE entries, specify the analytical method and estimated uncertainty for the cis:trans ratios.
   Advances RI-01 (SRG-5: yield-reporting coherence; SRG-4: cis:trans ratio method). This is a documentation investment requiring no new experiments.

3. **EP-08a [Replication / uncertainty pack]** — Repeat EtMgBr/PhCl (Condition A) in triplicate; report mean yield and standard deviation for the glpc-based entry.
   Advances RI-08 (SRG-5). Provides the first replicate data point for the highest-yield entry.

*Certification-gate note*: The experimental investment order (EP-07a → EP-01a → EP-08a) follows information gain (EP-07a advances two SRGs simultaneously; EP-01a requires no new experiments and advances two SRGs; EP-08a advances one SRG), but the final VQ-2 certification requires that both RI-01 and RI-07 are fully resolved regardless of order.

---

**Shortest route to VQ-3 (from VQ-2):**

1. **EP-03a [Direct-observation / state-assignment pack]** — Characterize the black precipitate from Example 1 by TEM or PXRD (Ni⁰ vs NiCl₂ vs other); attempt isolation of L₂NiR₂ intermediate 1 under stoichiometric conditions ([NiCl₂(dpe)] + 2 n-BuMgBr in Et₂O, 0°C).
   Advances RI-03 (SRG-1: unobserved intermediates; U-2 Ni⁰ question). This is the single highest-information-gain experiment: it simultaneously addresses the identity of the active catalyst and begins to validate the mechanistic cycle.

2. **EP-04a [Discrimination / replication pack]** — For EtMgBr/PhCl coupling (Condition A), quantify Et-Et homo-coupling product by glpc with a stated detection limit; run a crossover experiment (EtMgBr + PhCl + PhMgBr + EtCl simultaneously) to test whether the proposed intermediates scramble.
   Advances RI-04 (SRG-2: unreplicated selectivity discriminator) and provides the U-1 self-contradictory-absence resolution.

3. **EP-06a [Analogy-validation pack]** — Demonstrate that the rate of homo-coupling byproduct formation from [NiCl₂(dpe)] is measurably lower than from a control without the phosphine ligand (e.g., NiCl₂ alone or with monodentate PPh₃) on the same test substrate — this validates the RI-06 analogy by showing that the ligand architecture makes a measurable difference in selectivity.
   Advances RI-06 (SRG-1: cycle-level analogy). Note: RI-05 (CLA-A activity ranking qualitative overread) remains; VQ-3 would be certified as qualified unless EP-05a is also completed.

*Certification-gate note*: The experimental investment order (EP-03a → EP-04a → EP-06a) follows information gain, but the final VQ-3 certification (qualified or full) follows the inheritance principle: VQ-2 must be certified first, then RI-03 and RI-06 resolved (→ full VQ-3), with RI-05 resolution optionally required for unqualified VQ-3.

---

**Shortest route to VQ-4 (from VQ-3):**

1. **EP-09a [Internal benchmark pack]** — Run n-BuMgBr + vinyl chloride under Tamura-Kochi Fe/THF conditions and under [NiCl₂(dpe)]/Et₂O Condition B in the same laboratory; report cross:homo ratio and yield for both; run PhMgBr + PhCl under Ni(acac)₂ (no ligand) vs. [NiCl₂(dpe)] to establish the phosphine ligand's specific contribution.
   Advances RI-09 (SRG-6: external superiority; SRG-2 secondary: prior-work comparison). This single set of matched-pair experiments resolves all RI-09 gaps in SRG-6 and provides the benchmark for the selectivity claim in SRG-2.

*Certification-gate note*: VQ-4 certification requires that RI-08 (SRG-5, via EP-08a in the VQ-2 route) and RI-09 (SRG-6, via EP-09a) are both resolved, in addition to all lower-level requirements. The gate order is fixed: VQ-1 → VQ-2 → VQ-3 → VQ-4.

---

### §6 Contribution to institutional design

**1. Confirmed representative case for RI-06 (cycle-level import):**

Kumada 1972 provides a prototypical case for the RI-06 scope note "cycle-level import.[REDACTED: substantial verbatim quotation; see Tier 9]RI-06 applies not only to analogies between individual elementary steps but also to large-scale model import in which an entire catalytic cycle is constructed from another system" — is directly instantiated here. The case strengthens the cycle-level import subtype as a distinct pattern within RI-06, worthy of codebook documentation as an application note.

**2. Self-contradictory-absence CLA pattern (RI-04 + RI-06 co-occurrence):**

The U-1 item reveals a specific co-occurrence pattern worth recording institutionally: **RI-06 (imported model) generates a prediction that is simultaneously the central novelty claim's target datum (RI-04 unreplicated discriminator)**. Specifically: the imported (dipy)Ni cycle (RI-06) predicts R–R homo-coupling product formation (eq 3), and the absence of R–R from Table I is simultaneously the paper's central claim (selective cross-coupling, RI-04). This RI-06 + RI-04 co-occurrence means that resolving RI-06 (validating whether the cycle is correct) and resolving RI-04 (establishing whether homo-coupling is truly absent) are not independent: if the cycle is incorrect (RI-06 unresolved), the absence of R–R cannot be mechanistically interpreted. Record as a **RI co-occurrence pattern**: RI-06 × RI-04 co-occurrence where the model prediction and the central claim datum coincide in a self-contradictory fashion.

**3. Labeling mismatch pattern:**

The paper explicitly labels the catalytic cycle [REDACTED: verbatim source quotation; see the source paper via its DOI]) and is effectively confined there, while the five feature descriptions and the cycle equations deploy factual language. This is a textbook **labeling mismatch** pattern: the hypothesis is labeled at the end but deployed as a fact throughout the body. This pattern often co-occurs with RI-06 (the imported model is stated factually while the deferral label is isolated to the conclusion). This case should be added to the codebook as an application note for RI-06.

**4. RI-07 extended use — matched-pair absence:**

CLA-A (B-5: "definitely superior to THF") illustrates the RI-07 extended use for negative boundary claims without data. The certainty marker "definitely" constitutes a stronger boundary claim than "Only C_sp² halides can be used" (SRG-3 / B-4), because it adds the epistemic certainty modifier on top of the boundary assertion. Neither boundary claim is supported by a negative experiment. This case contributes a two-degree pattern: **boundary-without-data** (SRG-3, standard RI-07) and **boundary-with-certainty-marker-without-data** (CLA-A, RI-07 extended). The certainty-marker variant should be noted as a higher-severity instantiation of RI-07 extended use.

**5. Era-norm boundary insight — communication format as RI-07 generator:**

The §4 annotation reveals that three of the paper's RI-07 violations (sp² restriction without negative data, THF inferiority without THF experiment, bis-alkylation selectivity without intermediate data) all arise from the same source: the JACS Communication format discouraged reporting negative experiments by structural incentive (page limit, prior-art competition). This case confirms the "automatic-resolution pattern via communication → Full Paper transition" noted in §6 instructions. However, it additionally shows that **not all RI-07 violations generated by the communication format are automatically resolved in subsequent full papers**: the Kumada group's follow-up papers (1973–1975) did verify the sp² restriction mechanistically, but the THF inferiority claim was never formally established by a matched-pair experiment in the published literature (as of 1972 context). This suggests a **partial automatic-resolution** variant: format-generated RI-07 violations are resolved at unequal rates, and the resolution depends on whether the boundary claim becomes mechanistically important in follow-up work.

**6. PRI promotion evidence — PRI-11 (Mechanism–kinetics decoupling):**

The paper's catalytic cycle (eqs 2–4) is not used to derive a rate law; the mechanism is supported only by qualitative agreement with the observed yield pattern (no rate orders are reported). This is isomorphic with the PRI-11 pattern (mechanism supported only by agreement with observed rate orders, without algebraic derivation of the rate law). However, because no rate data at all are reported in this paper (not even rate orders), this is a stronger deficit than PRI-11 as currently defined — PRI-11 presupposes that rate orders have been observed but not algebraically derived; Kumada 1972 has no rate data whatsoever. This case may constitute an **upstream** variant of PRI-11: not "rate orders observed but rate law not derived" but [REDACTED: substantial verbatim quotation; see Tier 9] Consider adding as PRI-11 subtype: "Mechanism–kinetics decoupling (upstream): mechanism proposed without any kinetic data."

**7. VQ per-layer asymmetry — confirming the analytical value of layer-disaggregated VQ:**

The §3 per-layer asymmetry finding (Layer I alone could reach VQ-4 via synthetic utility pillar, while Layer III is blocked at VQ-3 by RI-06) confirms that the layered-structure judgment in §1 has practical analytical value: a paper's VQ level as a whole may understate the robustness of one of its independent claim layers. This case institutionalizes the practice of reporting VQ per layer when §1 identifies structurally independent layers, particularly when the utility pillar and the mechanistic pillar are both present in a single communication.

---

> **Tier 8 redaction notice**: This file is a redacted copy of the corresponding Tier 3 / Tier 9 output. Verbatim source-paper quotations have been replaced by `[REDACTED: see source paper §<loc>; full text retained in Tier 9 reviewer-only deposit]` markers, preserving location references and our own analytical content. Bibliographic fields (title, authors, journal, year, DOI), analytical labels (`evidence_chain:` with B-/U-/A-/C- internal IDs), short technical terms, and our own analytical text are not redacted. The redaction was applied by `scripts/redact_for_tier8.py` and, for this version, by `scripts/build_paperA_R1_public.py` with `scripts/redact_source_ngram_runs.py` (scripts of the project repository; they are not deposited).
