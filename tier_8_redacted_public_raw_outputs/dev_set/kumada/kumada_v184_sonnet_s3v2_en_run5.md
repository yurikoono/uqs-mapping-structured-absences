```
prompt_version: stage3-v2-en-20260419
model_info: claude-sonnet-4-6
```

# Re-certification Assessment Sheet for Scientific Knowledge

## Tamao, Sumitani, Kumada 1972 (JACS Communication)

---

### §1 Claim Architecture

**Core claim summary:**

The paper asserts two co-equal pillars. The Novelty pillar is that [NiCl₂(dpe)] and related dihalodiphosphinenickel complexes constitute a new class of catalysts enabling selective cross-coupling of Grignard reagents with sp²-carbon organic halides — a reaction previously inaccessible with the yields, selectivity, and substrate breadth demonstrated here. Within this novelty, the paper offers three independently evaluable sub-contributions: (a) the synthetic utility result (Table I yields of 76–98% across ten substrate combinations), (b) the catalyst design principle (bidentate diphosphine ligand required; ranked activity order [NiCl₂(dpp)] > [NiCl₂(dpe)] > [NiCl₂(dmpe)] ≈ [NiCl₂(PPh₃)₂] ≫ monodentate), and (c) the proposed three-step homogeneous Ni(II)/Ni(II) catalytic cycle (eqs 2–4). The Utility pillar is that the method enables "hardly accessible" targets — specifically the series of di-n-butylbenzene isomers — in a single step, and is applicable to Grignard reagents bearing β-hydrogen atoms that had been problematic in prior transition-metal catalysis.

**Layered structure judgment:**

Independent layers exist. A challenge to layer (c) — the mechanistic cycle — does not collapse the yield data of layer (a); a challenge to the yield data quality (absence of replicates) does not collapse the ligand design claim of layer (b). However, inter-layer dependencies are present: the mechanistic inference of layer (c) (cis-geometry of diorganonickel intermediate as "first requisite") is derived from the unquantified ligand activity order of layer (b), creating a propagation path in which quantitative uncertainty in (b) undermines the mechanistic inference in (c). Layer (a) is the most autonomous; it is grounded in isolated or glpc-determined yields requiring no mechanistic interpretation. Layer (c) is the most fragile, resting entirely on analogy with stoichiometric (dipy)Ni chemistry (refs 11–12) with no direct observation of any proposed intermediate under catalytic conditions. No single refutation collapses all three layers simultaneously; the paper's architecture distributes epistemic risk across layers.

---

### §2 SRG / CLA → RI / ER / EP Crosswalk

**SRG-1 [Catalytic mechanism evidence gap]**
Members: A-2, U-1, U-2, B-12

* **Primary RI**: RI-06 [Imported model] — The entire three-step Ni(II)/Ni(II) catalytic cycle (eqs 2–4) is constructed by analogy with stoichiometric (dipy)Ni reactions (refs 11–12), without demonstrating isomorphism between the (dipy)Ni stoichiometric system and the [NiCl₂(dpe)] catalytic system. The ligand environment differs (bipyridyl vs. diphosphine), the reaction mode differs (stoichiometric vs. catalytic), and no elementary step under actual catalytic conditions has been directly verified.
* **Secondary RI**: RI-03 [Unobserved explanatory] — Intermediates 1, 2, and 3 (the diorganonickel, haloorganonickel, and new diorganonickel species of the proposed cycle) are neither directly observed spectroscopically nor kinetically constrained under [NiCl₂(dpe)] catalytic conditions.
* **ER**: For the proposed cycle to function as a mechanistic contribution rather than a rationalization, at least one elementary step (oxidative addition of R'X'' to L₂NiR₂, or transmetalation of L₂Ni(R')(X'') with RMgX') must be demonstrably operative under the reported catalytic conditions; and the catalyst identity throughout the reaction must be established as the proposed Ni(II) complex rather than an alternative species (e.g., Ni⁰ nanoparticles suggested by the observed black mixture in Example 1).
* **EP**: EP-03a [Direct-observation / state-assignment pack]; EP-06a [Analogy-validation pack]
* **Case-specific implementation**: EP-03a: independently synthesize [NiR₂(dpe)] (intermediate 1) and [NiR(Cl)(dpe)] (intermediate 2) and characterize them by ³¹P NMR and X-ray crystallography; confirm that [NiR₂(dpe)] reacts with PhCl to produce Ph-R and [NiPh(Cl)(dpe)] (stoichiometric mimic of eq 3 under [NiCl₂(dpe)] conditions). EP-06a: explicitly compare the (dipy)Ni stoichiometric analogy (refs 11–12) with the [NiCl₂(dpe)] system by attempting the eq 1 reaction type with [NiCl₂(dpe)] in place of (dipy)Ni; characterize the reaction mixture (including the black precipitate of Example 1) for Ni⁰ nanoparticles by TEM or XRD.
* **Notes**: A-2 (high-severity deferred, V1=high, V2=high; high_convergence_low_gap); U-2 (medium-severity self-contradictory absence: "black mixture" consistent with Ni⁰, recorded but uncharacterized); B-12 (black mixture reporting omission, V1=low). The RI-06 scope note applies here at the cycle-level: the entire catalytic architecture is imported, not just individual steps. A-2 ↔ B-12 (pivot): the mechanistic deferral (A-2) provides structural cover for leaving the black-mixture observation (B-12) uncharacterized.

---

**SRG-2 [Cross/homo-coupling selectivity quantification]**
Members: B-6, U-1, C-1

* **Primary RI**: RI-04 [Unreplicated discriminator] — The paper's central selectivity claim (cross-coupling over homo-coupling, overcoming the "substantial amounts" of homo-coupling products in prior art) is supported by a single analytical determination per substrate with no reported cross:homo product ratio, no identification of homo-coupling byproduct (e.g., Et-Et from EtMgBr/PhCl), and no direct head-to-head comparison on a shared substrate with the Tamura-Kochi system. U-1 elevates this beyond a reporting omission: the paper's own proposed catalytic cycle (eq 3) explicitly predicts R–R homo-coupling product as a stoichiometric byproduct, yet R–R is neither reported, quantified, nor acknowledged as undetectable.
* **Secondary RI**: RI-09 [External superiority] — The claimed superiority over prior art (Tamura-Kochi, refs 5–6) rests solely on external literature characterization of prior-art limitations, with no direct comparison on a shared substrate.
* **ER**: For the selectivity claim to hold, at minimum one substrate combination must report both the cross-coupling product yield and the homo-coupling byproduct yield (or an unambiguous detection limit), and at least one direct comparison of the Ni-dpe system with the Tamura-Kochi system on a common substrate must be provided.
* **EP**: EP-04a [Discrimination / replication pack]; EP-09a [Internal benchmark pack]
* **Case-specific implementation**: EP-04a: for the EtMgBr/PhCl entry (the highest-yield entry at 98%), analyze the crude reaction mixture by quantitative GC with calibrated internal standard to determine the Et-Et and Ph-Ph homo-coupling yields in addition to the Ph-Et cross-coupling yield; repeat for at least one alkyl Grignard entry where the eq 3 homo-coupling product would be most volatile and thus easiest to quantify. EP-09a: run EtMgBr/vinyl chloride or n-BuMgBr/PhCl under Tamura-Kochi conditions (Fe catalyst in THF) alongside the [NiCl₂(dpe)] conditions and report cross:homo yields for both systems from the same substrate set.
* **Notes**: U-1 (high-severity self-contradictory absence, V2=high, V3=high; high_convergence_low_gap); B-6 (reporting omission, V2=high, V3=high); C-1 (severed Tamura-Kochi citation, affects_claims=yes). This SRG constitutes the deepest structural tension in the paper: the selectivity claim is supported by the absence of homo-coupling data, while the mechanism predicts homo-coupling product must exist.

---

**SRG-3 [Scope restriction without negative-result evidence]**
Members: B-4, A-3

* **Primary RI**: RI-07 [Unsupported boundary] — The paper asserts [REDACTED: substantial verbatim quotation; see Tier 9] (Feature 2) without reporting a single failed reaction with an sp³ halide. The restriction is rationalized mechanistically (footnote 19: sp² C–Cl undergoes oxidative addition to low-valent nickel), but no direct experimental demonstration — not even a 0% yield or "trace product" entry — establishes the sp² boundary empirically.
* **Secondary RI**: (none — the boundary claim is the primary gap; A-3 records the deferral of extension, which is not independently a different RI category)
* **ER**: For the "only sp² halides" boundary to be experimentally established rather than mechanistically inferred, at least one sp³ alkyl or allyl halide (e.g., n-BuCl, BnCl) must be subjected to the standard [NiCl₂(dpe)] conditions and the result reported — whether it is a failed reaction with recovered starting material, formation of a different product, or catalyst decomposition.
* **EP**: EP-07a [Boundary-test pack]
* **Case-specific implementation**: EP-07a: run n-BuCl and BnCl (sp³ and borderline sp³/sp² cases, respectively) with EtMgBr and [NiCl₂(dpe)] under Condition A; report isolated or glpc yield of cross-coupling product, homo-coupling product (Et-Et, Bu-Bu), and recovery of the halide. The benzyl case is particularly informative because allyl/benzyl halides have partial sp² character at the reactive carbon and their outcome would experimentally resolve whether the boundary is truly sp² or more nuanced.
* **Notes**: B-4 (mixed classification — intentional narrowing + reporting omission; convergence=3/3, the only full-convergence item in Stage 1; high_convergence_low_gap); A-3 (scope extension deferred, V1=medium, V3=medium). B-4 ↔ A-3 (pivot): the scope restriction is simultaneously claimed as a positive feature and deferred for extension, exploiting both the restriction and the prospect of overcoming it without empirical grounding for either.

---

**SRG-4 [Stereochemical outcome and its mechanistic basis]**
Members: A-1, B-11

* **Primary RI**: RI-04 [Unreplicated discriminator] — The cis:trans stilbene ratios (80:20 from cis-DCE; 43:57 from trans-DCE) are reported as single determinations without stating the analytical method (¹H NMR, glpc, or other) or measurement uncertainty. The mechanistic interpretation ("rather nonstereospecifically," "anomalously enriched with the cis isomer") is applied to data of unknown analytical precision: a ±5–10% uncertainty in the 43:57 ratio would shift the interpretation between "partial retention of configuration" and "essentially random," which have different mechanistic implications for which step of the catalytic cycle loses stereochemical memory.
* **Secondary RI**: RI-03 [Unobserved explanatory] — No mechanistic assignment of the stereochemical outcome to a specific step (oxidative addition, transmetalation, or reductive elimination) is made; the entire mechanistic question is deferred to A-1.
* **ER**: For the stereochemical data to support mechanistic inference, the analytical method and its uncertainty must be stated; and the anomalous cis enrichment from both cis- and trans-DCE must be assigned to a specific step in the catalytic cycle, at minimum by kinetic or control experiments distinguishing whether the loss of stereochemical memory occurs at oxidative addition or at a downstream step.
* **EP**: EP-04a [Discrimination / replication pack]; EP-03a [Direct-observation / state-assignment pack]
* **Case-specific implementation**: EP-04a: determine the cis:trans stilbene ratios by both ¹H NMR integration and GC with calibrated response factors, reporting the uncertainty from both methods; run the cis-DCE and trans-DCE reactions in parallel with replicates (n ≥ 2) to confirm reproducibility of the 80:20 and 43:57 ratios. EP-03a: run the reaction of (cis-DCE) with PhMgBr under [NiCl₂(dpe)] conditions at low conversion (≤30%) to test whether the cis:trans ratio is conversion-dependent (thermodynamic equilibration) or conversion-independent (kinetic selectivity arising from the mechanism).
* **Notes**: A-1 (deferred, V1=medium, V2=medium; high_convergence_low_gap); B-11 (reporting omission, V3=medium; convergence=1/3). A-1 ↔ B-11: the stereochemical mechanistic deferral (A-1) is compounded by the analytical uncertainty of the ratio data (B-11); if the ratios are imprecise, the "nonstereospecific" conclusion is doubly uncertain.

---

**SRG-5 [Yield data analytical quality]**
Members: B-2, B-7, B-9, B-11

* **Primary RI**: RI-01 [Reporting integrity] — The Table I yield column mixes isolated yields and glpc-based yields without systematic explanation of which method was used per entry, the internal standard identity and response factors for glpc quantification are not disclosed, no replicates or standard deviations are reported for any of the ten substrate combinations, and the characterization footnote ("by glpc, nmr, ir, and/or mass spectra") allows identity assignment by a single technique per entry without specifying which technique was applied to which product.
* **Secondary RI**: RI-08 [Unquantified reliability] — The absence of replicates means that yield differences between entries (e.g., 98% vs. 76% for EtMgBr vs. n-BuMgBr with PhCl) cannot be assessed as statistically significant. The subtype RI-08 internal inconsistency note applies: the "and/or mass spectra" formulation allows characterization quality to vary systematically across entries in a way that is not disclosed.
* **ER**: For the Table I yield data to be independently reproducible and cross-comparable, the analytical method (isolated vs. glpc) must be consistently disclosed per entry, the glpc internal standard identity and response factors must be stated, and at minimum one representative entry must include replicate yield data with standard deviation.
* **EP**: EP-01a [Reporting-coherence pack]; EP-08a [Replication / uncertainty pack]
* **Case-specific implementation**: EP-01a: add a footnote to each Table I entry specifying the analytical method used to determine the yield; for glpc-only entries, identify the internal standard (e.g., n-decane) and report the response factor relative to each product class (alkylbenzene, stilbene, α-vinylnaphthalene). EP-08a: report n ≥ 2 independent runs for the EtMgBr/PhCl entry (the benchmark highest-yield case) and the n-BuMgBr/PhCl entry (the lowest isolated yield, 76%) to establish the run-to-run reproducibility envelope. These two entries span the yield range and provide the most information for calibrating the reliability of all other single-determination entries.
* **Notes**: B-2 (yield basis mixing, V1=medium, V3=medium; high_convergence_low_gap); B-7 (characterization "and/or" formulation, V3=medium; convergence=1/3); B-9 (no replicates, V3=medium; convergence=1/3); B-11 (cis:trans ratio method not stated; shared with SRG-4). All four items share the root that multiple quantitative claims lack the analytical metadata needed to evaluate their reliability.

---

**SRG-6 [Prior work numerical comparison gap]**
Members: C-1, C-2, A-4

* **Primary RI**: RI-09 [External superiority] — The paper's competitive positioning against Tamura-Kochi (refs 5–6), against π-allylnickel and cuprate reagents (refs 7–10), and against the concurrent Corriu-Masse system (footnote 3a) rests entirely on external literature descriptions without any direct head-to-head yield, selectivity, or substrate-scope comparison on a shared substrate. Feature (5) ([REDACTED: substantial verbatim quotation; see Tier 9]) is the most egregious case: the word "definitely" implies comparative data that is completely absent.
* **Secondary RI**: (none — the missing comparisons are all external reference type)
* **ER**: For the superiority claims over prior art to be substantiated, at least one shared substrate comparison must be run under the Ni-dpe conditions and under a representative prior-art condition (e.g., Fe catalyst/THF for Tamura-Kochi; Ni(acac)₂ for Corriu-Masse) with yields reported for both; and the Corriu-Masse system must be explicitly distinguished from the Ni-dpe system at the level of catalyst structure and substrate scope rather than noted without comment.
* **EP**: EP-09a [Internal benchmark pack]
* **Case-specific implementation**: EP-09a: run n-BuMgBr/PhCl under [NiCl₂(dpe)]/Et₂O conditions (as in Table I) and under Fe(acac)₂/THF conditions (Tamura-Kochi), reporting isolated cross-coupling yield and homo-coupling byproduct yield for both; run EtMgBr/PhCl under [NiCl₂(dpe)]/Et₂O and [NiCl₂(dpe)]/THF to substantiate the solvent superiority claim with the paper's own catalyst rather than by contrast with Tamura-Kochi.
* **Notes**: C-1 (severed Tamura-Kochi citation, affects_claims=yes); C-2 (cuprate/allylnickel cited and set aside without numerical comparison, affects_claims=medium); A-4 (Corriu-Masse concurrent submission noted without scope or yield comparison). B-5 (solvent claim without data, V1=low, V2=low; low convergence) is the most direct representative of RI-09 in the B items and feeds directly into EP-09a.

---

**Outside the SRGs: CLAs**

**CLA-1: Self-contradictory absence — homo-coupling byproduct of eq 3**

This CLA captures U-1 in its standalone form as a self-contradictory absence that is not fully resolved within any of the six SRGs above. SRG-2 addresses the selectivity quantification gap from the reporting and benchmark perspective; CLA-1 addresses it from the model-consistency perspective.

* **Primary RI**: RI-03 [Unobserved explanatory] — The proposed catalytic cycle explicitly generates R–R as a stoichiometric byproduct of eq 3 (L₂NiR₂ + R'X'' → L₂Ni(R')(X'') + R–R). R–R is therefore an "observable that the paper's proposed model predicts" but is neither observed nor reported in any Table I entry or experimental procedure. The absence of R–R is not acknowledged as a detection limit — it is simply not mentioned.
* **ER**: For the proposed cycle to be internally consistent with the reported selectivity, the paper must either (a) report R–R quantification (confirming it is present but minor) or (b) report that R–R was not detected above a stated detection limit and provide a mechanistic explanation for why eq 3, as written, does not produce detectable R–R.
* **EP**: EP-03a [Direct-observation / state-assignment pack]
* **Case-specific implementation**: EP-03a: in the crude reaction mixture of EtMgBr/PhCl (or n-BuMgBr/m-DCB), analyze by quantitative GC with Et-Et, n-Bu-n-Bu, and m-dibutylbenzene authentic standards to determine homo-coupling yields; the detection limit of the GC method should be stated so that a "not detected" result can be interpreted as an upper bound on the homo-coupling selectivity.
* **Notes**: U-1 (high-severity self-contradictory absence; V2=high, V3=high; high_convergence_low_gap). This CLA represents the deepest internal logical tension in the paper: the central selectivity claim is self-contradicted by the paper's own mechanism at the level of a predicted but unreported obligate byproduct.

---

**CLA-2: Quantitative basis of ligand activity order — D-4 Candidate 5 (B-3)**

* **Primary RI**: RI-05 [Qualitative overread] — The paper derives a mechanistic conclusion ([REDACTED: substantial verbatim quotation; see Tier 9]) from a qualitative activity ranking (footnote 21: [REDACTED: substantial verbatim quotation; see Tier 9]) for which no numerical yield or conversion values are disclosed. A mechanistic conclusion of this specificity — that cis-geometry of the diorganonickel intermediate is a "requisite" — requires quantitative differentiation of the ligand activities, not merely a rank order.
* **ER**: For the mechanistic conclusion to follow from the ligand activity data, the yield or conversion for each of the six ligand complexes ([NiCl₂(dpp)], [NiCl₂(dpe)], [NiCl₂(dmpe)], [NiCl₂(PPh₃)₂], [NiCl₂(PEt₃)₂], [NiCl₂(PPh₂Me)₂]) under identical conditions must be reported numerically; the mechanistic inference about cis-geometry as "first requisite" requires that the bidentate vs. monodentate gap be quantitatively larger than the bidentate intra-group variation.
* **EP**: EP-05a [Quantitative-ranking substantiation pack]
* **Case-specific implementation**: EP-05a: report glpc or isolated yields for the coupling of n-BuMgBr with PhCl catalyzed by each of the six complexes under identical conditions (e.g., 1 mol% catalyst, Et₂O, reflux, 3 h); if the ranking holds, provide bite-angle or P–Ni–P angle data from crystal structures or calculations for the bidentate ligands to support the geometric mechanistic inference.
* **Notes**: B-3 (V1=medium, V2=medium; convergence=2/3; high_convergence_low_gap). The RI-05 overread note applies: the mechanistic inference about cis-geometry is derived from an unverifiable ranking; if [NiCl₂(dpp)] and [NiCl₂(dpe)] differ by only a few percent yield, the "first requisite" conclusion becomes unsupported by the data that generated it.

---

### §3 Current VQ assessment

**Current judgment: VQ-2 (Method) — fails to reach VQ-3**

**VQ-1 [Observation] — PASS (with non-fatal qualification)**

RI-02 [Object identification]: The paper characterizes products by "glpc, nmr, ir, and/or mass spectra" (footnote c). For major isolated products in Examples 1 and 2, physical constants (bp, refractive index) are reported and compared with literature values. The product identity claims are credible at the VQ-1 level: the synthetic products (di-n-butylbenzenes, α-vinylnaphthalene, stilbene isomers) are known compounds with established physical constants. The "and/or" formulation (B-7) allows single-technique identification for some entries, which is non-fatal at VQ-1 given the identity claims rest on matching to known compounds with literature bp values, but constitutes a non-fatal RI-02 concern.

Non-fatal note: B-7 and B-8 (purity unsubstantiated for "pure" m-di-n-butylbenzene; bp deviation from literature not explained) reduce confidence in the identity/purity assignments for minor products but do not prevent VQ-1 from being satisfied for the named main products.

**VQ-2 [Method] — PASS (qualified)**

On the premise that RI-02 is non-fatal (VQ-1 holds), VQ-2 requires resolution of RI-01 and RI-07.

RI-01 [Reporting integrity]: non-fatal at VQ-2 by era-norm context (see §4). The mixed isolated/glpc yield reporting (B-2) and the absence of replicates (B-9) are structurally enabled by the JACS Communication format. The yield range 76–98% is internally consistent: no entry is arithmetically contradictory. The reporting incoherence does not prevent VQ-2 from being formally satisfied, but the qualification is substantial.

RI-07 [Unsupported boundary]: the "only sp² halides" restriction (B-4) is asserted without failure examples. This is non-fatal at VQ-2 because the mechanistic rationalization in footnote 19 (sp² C–Cl oxidative addition to low-valent Ni) provides a theoretical basis, even without experimental confirmation. VQ-2 holds on this basis but only as a qualified pass.

**VQ-2 (qualified)** because: RI-05 remains in a serious form in CLA-2 (ligand activity order mechanistic overread), and RI-01 in SRG-5 is structurally significant though era-norm tolerated. The qualification reflects that method claims are not independently reproducible from the data as presented.

**VQ-3 [Mechanism] — FAIL**

VQ-3 requires resolution of RI-03, RI-04, and RI-06 (inheriting VQ-2).

RI-06 [Imported model] in SRG-1: fatal at VQ-3. The entire catalytic cycle (eqs 2–4) is imported from stoichiometric (dipy)Ni chemistry without any experimental verification that the individual steps operate under [NiCl₂(dpe)] catalytic conditions. No elementary step is directly demonstrated. The model import is cycle-level (entire architecture), not just step-level, making this a maximal RI-06 violation.

RI-03 [Unobserved explanatory] in SRG-1 and CLA-1: fatal at VQ-3. Intermediates 1, 2, and 3 are unobserved under catalytic conditions; the key byproduct R–R predicted by eq 3 is not reported, detected, or bounded by a detection limit. CLA-1 demonstrates that the cycle's own predictions are inconsistent with the reported selectivity (or the selectivity is unverified).

RI-04 [Unreplicated discriminator] in SRG-2 and SRG-4: non-fatal individually but collectively fatal at VQ-3. The cross:homo selectivity claim (SRG-2) rests on single unreplicated determinations without homo-coupling product quantification; the stereochemical data (SRG-4) lack stated analytical method and uncertainty.

**Unresolved RIs preventing VQ-3**: RI-06 (SRG-1), RI-03 (SRG-1, CLA-1), RI-04 (SRG-2, SRG-4).

**VQ-4 [Benchmark] — FAIL** (inherits VQ-3 failure; additionally, RI-08 in SRG-5 and RI-09 in SRG-6 are unresolved)

**Layered VQ asymmetry:**

However, **Layer (a) — synthetic utility result (Table I yields)** on its own reaches approximately VQ-2 (qualified), because the identity claims for the named products are credible, the yield ranges are internally consistent, and the era-norm context permits the reporting omissions. The yields as a synthetic-utility claim (not a mechanistic claim) do not require VQ-3 resolution.

**Layer (b) — catalyst design principle (ligand activity order)** does not surpass VQ-2 (qualified) because CLA-2's RI-05 prevents independent quantitative evaluation.

**Layer (c) — proposed Ni(II)/Ni(II) catalytic cycle** does not reach VQ-2 independently: RI-06 and RI-03 are fatal at VQ-3 and the mechanistic claims cannot be separated from the model import and unobserved intermediates.

---

### §4 Era-Norm Annotation

**Communication-era tolerated:**

- **B-9 (no replicates)**: Single-determination yields per substrate entry were the norm in JACS Communications in 1972; statistical reporting was not expected in priority communications focused on scope establishment. Era context: the paper's explicit qualifier "The experimental conditions are not necessarily optimum" (Table I footnote a) signals awareness that these are preliminary results — the field expectation was that full paper replication would follow.

- **B-7 ("and/or mass spectra[REDACTED: substantial verbatim quotation; see Tier 9]glpc, nmr, ir, and/or mass spectra") represented thorough practice for 1972; the specific technique per product was not required disclosure.

- **B-1 (TON and catalyst loading optimization absent)**: Communication format did not require catalytic efficiency metrics (TON, TOF) in 1972; Table I footnote a's qualifier "not necessarily optimum" was a recognized device to pre-empt optimization-completeness expectations. Full optimization data were expected in a follow-up full paper.

- **B-3 (ligand activity order without numerical values)**: Qualitative rankings with a brief footnote specifying conditions were tolerated in 1972 communications; the expectation that quantitative yield values for each ligand would appear in a subsequent full paper was standard practice.

- **B-5 (solvent claim without comparative data)**: Comparative claims based on laboratory experience rather than systematic data were more common in 1972 communications. The distinction from Tamura-Kochi was a qualitative positioning claim, not a quantitative benchmark requirement.

- **B-8 (bp deviation from literature not explained)**: Boiling point discrepancies across different pressure conditions were common in pre-NIST-database literature and correction of bp to standard conditions was not required disclosure. The comparison to "lit. bp 75–76° (0.4 mm)" vs. the reported "bp 84° (5 mm)" is pressure-scale consistent and was read as such by contemporary chemists.

**Modern-era deficient:**

- **B-2 (mixed isolated/glpc yield reporting without calibration disclosure)**: By contemporary standards, glpc-based yields require disclosure of the internal standard identity, response factors relative to each product class, and GC purity of calibration standards. The dual-footnote system (footnotes d and e) without per-entry disclosure creates a yield-basis ambiguity that would not be accepted in a modern full paper or supplementary information. Directly conflicts with VQ-2 (Method) requirements.

- **B-6 + U-1 (homo-coupling byproduct absent from Table I)**: Contemporary standards require reporting of major byproducts (≥1–5%) in catalytic reactions as a matter of selectivity characterization, particularly when the paper's central claim is selectivity for cross-coupling over homo-coupling. The absence of homo-coupling product data — combined with the cycle's explicit prediction of R–R in eq 3 — would be flagged in modern peer review as a fatal inconsistency. Directly prevents VQ-3 certification.

- **A-2 + U-2 (mechanism proposed without any elementary step verification, black mixture uncharacterized)**: Contemporary standards require at least one piece of direct evidence for each proposed elementary step in a catalytic mechanism (e.g., stoichiometric reactions of independently synthesized intermediates, KIE, crossover experiments). The observation of a "black mixture" would trigger a requirement to characterize the catalyst resting state (Ni⁰ vs. Ni(II)) by in situ NMR or XPS. These are modern VQ-3 requirements.

- **B-4 (sp² restriction without any failure example)**: Modern synthetic scope papers routinely include a "substrate limitations" table or section reporting failed or low-yield substrates, particularly when the scope restriction is a named feature of the method. Asserting "only sp² halides can be used" without any negative result would not pass modern peer review without at least one representative sp³ halide failure example. Era-norm dual classification: tolerated in 1972 (scope communications focused on positively demonstrated examples), deficient by modern standards (reproducibility and boundary falsification requirements).

- **B-9 (no replicates)**: Dual classification. While tolerated in 1972 communication format (see above), modern supplementary information requirements (≥n=2 for benchmark substrates; standard deviation reported for isolated yields) make this deficient for contemporary re-certification.

---

### §5 Shortest-reinforcement route

**First objective function: VQ-3 [Mechanism]**

Current state: VQ-2 (qualified). Blocking RIs: RI-06 (SRG-1, cycle-level model import), RI-03 (SRG-1, unobserved intermediates; CLA-1, unreported byproduct R–R).

```
Shortest route to VQ-3:

1. EP-04a [Discrimination / replication pack] for CLA-1 — In the
   EtMgBr/PhCl crude mixture, quantify Et-Et and Ph-Ph homo-coupling
   products by calibrated GC with authentic standards; report the
   cross:homo product ratio and the detection limit for homo-coupling
   products. Advances RI-04 (SRG-2) and partially advances RI-03
   (CLA-1: establishes whether R–R is present at a detectable level,
   constraining the mechanistic cycle).

2. EP-06a [Analogy-validation pack] for SRG-1 — Isolate or
   independently synthesize [NiEt₂(dpe)] (intermediate 1) and confirm
   that it reacts with PhCl to produce Ph-Et and [NiPh(Cl)(dpe)]
   (stoichiometric verification of eq 3 under the paper's specific
   ligand system). Advances RI-06 (replaces the (dipy)Ni analogy with
   a direct [NiCl₂(dpe)]-system experiment).

3. EP-03a [Direct-observation / state-assignment pack] for SRG-1 —
   Characterize the black precipitate from Example 1 by XRD, TEM, or
   ICP to determine whether it is Ni⁰ metal or a Ni(II) salt; if Ni⁰,
   determine whether it is catalytically active in a separate
   experiment (e.g., Ni⁰ + PhCl + n-BuMgBr under Condition A
   conditions). Advances RI-03 (U-2 partial resolution: establishes
   whether the proposed homogeneous Ni(II) cycle is consistent with
   the reaction mixture).

4. EP-05a [Quantitative-ranking substantiation pack] for CLA-2 —
   Report glpc yields for each of the six ligand complexes in the
   n-BuMgBr/PhCl benchmark reaction. Advances RI-05 (allows
   independent evaluation of the "cis-geometry as first requisite"
   mechanistic inference).

Certification-gate note: EP-04a (CLA-1) and EP-06a (SRG-1) together
address RI-03 and RI-06 at the level required for VQ-3; EP-03a
resolves the residual RI-03 gap from U-2. These three investments are
necessary but not individually sufficient — all three must be
completed for VQ-3 gate to open, following the inheritance principle
VQ-1 → VQ-2 → VQ-3.
```

**Second objective function: VQ-4 [Benchmark]**

Prerequisite: VQ-3. Additional blocking RIs: RI-08 (SRG-5), RI-09 (SRG-6).

```
Shortest route to VQ-4 (after VQ-3 achieved):

1. EP-09a [Internal benchmark pack] for SRG-6 — Run n-BuMgBr/PhCl
   under [NiCl₂(dpe)]/Et₂O and Fe(acac)₂/THF (Tamura-Kochi) in
   parallel; run [NiCl₂(dpe)] with Et₂O and THF as solvents in
   parallel. Advances RI-09 (establishes internal comparison with
   prior art on a shared substrate and with the paper's own catalyst
   under both solvents).

2. EP-08a [Replication / uncertainty pack] for SRG-5 — Report n ≥ 2
   independent runs for EtMgBr/PhCl (highest yield) and n-BuMgBr/PhCl
   (lowest isolated yield) with standard deviations; disclose glpc
   internal standard identity and response factors. Advances RI-08
   (establishes run-to-run reproducibility and measurement consistency
   across the yield range).

Certification-gate note: The final certification follows the
inheritance principle; VQ-4 cannot be achieved before VQ-3 is
verified. The experimental investment order here prioritizes EP-09a
(highest information gain for benchmark positioning) over EP-08a
(analytical completeness), but both are required for VQ-4 gate.
```

---

### §6 Contribution to institutional design

**New representative cases for existing RI codes:**

- **RI-06 cycle-level import (scope note confirmed and extended)**: This paper provides the clearest case to date of cycle-level model import. The entire Ni(II)/Ni(II) catalytic cycle (eqs 2–4) is constructed from a single stoichiometric (dipy)Ni precedent (refs 11–12) without any elementary-step verification in the target ([NiCl₂(dpe)]) system. The RI-06 scope note ([REDACTED: substantial verbatim quotation; see Tier 9]) is fully instantiated here. This case should be recorded as a canonical RI-06 cycle-level example alongside any future Codebook revision.

- **RI-03 self-contradictory absence subtype**: CLA-1 provides a particularly clean instance of RI-03 operating through a self-contradictory absence: the proposed catalytic cycle (eq 3) explicitly generates R–R as a product, yet R–R appears nowhere in the experimental data. This is distinct from the "available-but-unutilized characterization" subtype (where data were acquired but not analyzed) — here the predicted observable was never sought in the reported experiments. The Codebook could benefit from a third RI-03 subtype label: **"predicted-but-unsought observable"** to distinguish it from both the "unobserved" base case and the "available-but-unutilized" subtype.

**Labeling mismatch pattern detected:**

The paper explicitly labels the mechanistic cycle as a "working hypothesis" (A-2: "apart from the working hypothesis described above"). However, the surrounding narrative uses factual verbs throughout: [REDACTED: substantial verbatim quotation; see Tier 9] (emphasis added). The hypothesis label is confined to a single parenthetical phrase in the penultimate sentence of the mechanistic discussion; the body of the mechanistic section reads as factual. This labeling mismatch pattern co-occurs with RI-06 as expected per the Codebook note. Position of hypothesis label: penultimate sentence of the mechanistic discussion section, concentrated at the end in the form of a deferral phrase.

**Automatic-resolution pattern via Communication → Full Paper transition:**

The following RI instances are consistent with automatic resolution upon full-paper publication: B-9 (no replicates; RI-08), B-3 (ligand order without numerical values; RI-05), B-1 (TON absent; RI-10 provisional), B-7 (characterization "and/or"; RI-02), and B-5 (solvent claim without data; RI-09). The follow-up full paper by Tamao et al. (J. Organometal. Chem., 1977) would be expected to resolve these automatically. This confirms the pattern noted for other 1972-era communications: RI-07 (boundary without failure examples) and RI-01 (reporting integrity) arising from page-limit constraints are not automatically resolved in the full paper — they require specific experimental design decisions rather than merely expanded reporting.

**RI co-occurrence pattern:**

SRG-1 exhibits a RI-06 + RI-03 co-occurrence. The mechanistic cycle is both imported without isomorphism verification (RI-06) and requires unobserved intermediates (RI-03). Resolving RI-06 alone (e.g., by verifying isomorphism between (dipy)Ni and (dpe)Ni at one step) is insufficient: RI-03 requires direct observation of the intermediates independently of whether the (dipy)Ni analogy holds. Conversely, resolving RI-03 alone (observing one intermediate) does not resolve RI-06 (the entire cycle could still be an invalid import). Both RIs must be resolved simultaneously for VQ-3. This co-occurrence structure means that EP-06a (analogy-validation) and EP-03a (direct observation) are complementary, not substitutable — a pattern worth recording in the Codebook as a co-occurrence design note for Ni-catalyzed mechanistic papers.

**PRI candidate: no new PRI proposed.** PRI-10 (Kinetic overclaim) could apply to the "definitely superior" solvent claim (B-5) and the "remarkable" chloride reactivity claim, but neither reaches the level of an absolute rate enhancement claim — they are qualitative superiority claims that fit RI-09 (external superiority) and RI-05 (qualitative overread) better than PRI-10. PRI-11 (Mechanism–kinetics decoupling) does not apply in its strict form because no rate law is proposed at all (the absence is more fundamental than a mechanism-kinetics decoupling). Both PRI-10 and PRI-11 remain on their current provisional promotion track without new evidence from this case.

**New EP case-specific implementation note for Ni systems:**

EP-07a (Boundary-test pack) for sp²-only scope claims should specify benzyl halides (BnCl, BnBr) as mandatory boundary-test substrates in Ni-catalyzed cross-coupling papers, because BnCl occupies the boundary between sp³ and sp² character (the benzylic carbon is tetrahedral but adjacent to a π-system that could enable oxidative addition by a different mechanism). This implementation note — [REDACTED: substantial verbatim quotation; see Tier 9] — generalizes beyond this paper and should be added to the EP-07a entry.

---

> **Tier 8 redaction notice**: This file is a redacted copy of the corresponding Tier 3 / Tier 9 output. Verbatim source-paper quotations have been replaced by `[REDACTED: see source paper §<loc>; full text retained in Tier 9 reviewer-only deposit]` markers, preserving location references and our own analytical content. Bibliographic fields (title, authors, journal, year, DOI), analytical labels (`evidence_chain:` with B-/U-/A-/C- internal IDs), short technical terms, and our own analytical text are not redacted. The redaction was applied by `scripts/redact_for_tier8.py` and, for this version, by `scripts/build_paperA_R1_public.py` with `scripts/redact_source_ngram_runs.py` (scripts of the project repository; they are not deposited).
