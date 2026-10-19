```
prompt_version: stage3-v2-en-20260419
model_info: claude-sonnet-4-6
```

# Re-certification Assessment Sheet for Scientific Knowledge

## Tamao, Sumitani, Kumada 1972 (Journal of the American Chemical Society, communication)

---

### §1 Claim Architecture

**Core claim summary:**

The paper asserts two separable pillars. The **Novelty pillar** is that nickel-phosphine complexes — specifically dihalodiphosphinenickel compounds, exemplified by [NiCl₂(dpe)] — operate as *catalysts* (not stoichiometric reagents) for selective cross-coupling of Grignard reagents with sp² organic halides (vinylic and aromatic). The novelty relative to prior art rests on three sub-claims: (a) selectivity (cross- over homo-coupling achieved without reported byproducts); (b) β-hydrogen tolerance (alkylmagnesium reagents that fail in most transition-metal coupling contexts perform well); and (c) chloride reactivity (sp² C–Cl bonds, largely unused in prior work, participate at synthetically useful yields). A subordinate mechanistic novelty claim proposes a three-step Ni(0)/Ni(II) catalytic cycle (eqs 2–4) as the rationalization, framed explicitly as a "working hypothesis.[REDACTED: substantial verbatim quotation; see Tier 9]hardly accessible" compounds — exemplified by m-di-n-butylbenzene and α-vinylnaphthalene — in high isolated or glpc-quantified yields (76–98%) across ten substrate combinations in Table I.

**Layered structure judgment:**

The paper has a genuine two-layer architecture that the authors themselves acknowledge through their "working hypothesis[REDACTED: substantial verbatim quotation; see Tier 9][REDACTED: verbatim source text; see the source paper via its DOI][REDACTED: substantial verbatim quotation; see Tier 9]selective cross-coupling catalyzed by nickel-phosphine complexes" — is therefore partially but not wholly protected against refutation; the synthetic claim (Layer 1) is robust against mechanistic refutation, while the mechanistic claim (Layer 2) is self-declared as provisional.

---

### §2 SRG / CLA → RI / ER / EP Crosswalk

#### SRG-1 [Catalytic mechanism evidence gap]

Members: A-2, U-2, B-12

**Primary RI**: RI-06 [Imported model]
**Secondary RI**: RI-03 [Unobserved explanatory]

**ER**: The paper's proposed catalytic cycle must be shown to operate via the claimed intermediates (diorganonickel complex 1, haloorganonickel complex 2) under the actual [NiCl₂(dpe)] reaction conditions, rather than via analogy with a structurally distinct stoichiometric (dipy)Ni system; minimally, the identity of the active catalyst species must be distinguishable from Ni⁰ nanoparticles formed during the reaction.

**EP**: EP-06a (Analogy-validation pack); EP-03a (Direct-observation / state-assignment pack)

**Case-specific implementation**:
- EP-06a: Conduct independent synthesis and characterization of [dpe-Ni(n-Bu)(Cl)] and [dpe-Ni(n-Bu)₂] analogous to intermediates 2 and 1; demonstrate that stoichiometric reactions of these isolated complexes with organic halides and Grignard reagents reproduce the cross-coupling selectivity observed under catalytic conditions. This tests whether the (dipy)Ni→(dpe)Ni cycle analogy is mechanistically valid.
- EP-03a: Characterize the black precipitate formed in Example 1 by mercury-drop test (to distinguish homogeneous Ni(II) from heterogeneous Ni⁰), followed by X-ray powder diffraction or ICP analysis of the filtrate and residue; conduct a hot-filtration test to determine whether catalytic activity resides in the soluble or insoluble phase.

**Notes**: A-2 is high_convergence_low_gap (V1=high, V2=high; convergence=2/3; gap=none); U-2 is severity=medium. SRG-1 is the largest single mechanistic evidence cluster; RI-06 takes priority (it applies at the cycle level — the entire catalytic mechanism is imported from a non-isomorphous system) over RI-03 (which captures the unobserved intermediates). RI-06 scope note (cycle-level import) applies directly. Labeling mismatch detected: the narrative uses factual verbs throughout eqs 2–4 ("reacts with," "forms," "is converted to," "released by," "completes the catalytic cycle") despite the authors' own "working hypothesis" label concentrated in a single terminal sentence — see §6.

---

#### SRG-2 [Cross/homo-coupling selectivity quantification]

Members: B-6, U-1, C-1

**Primary RI**: RI-04 [Unreplicated discriminator]
**Secondary RI**: RI-09 [External superiority]

**ER**: The paper's titular claim of "selective[REDACTED: substantial verbatim quotation; see Tier 9]seldom employed" characterization of all prior methods.

**EP**: EP-04a (Discrimination / replication pack); EP-09a (Internal benchmark pack)

**Case-specific implementation**:
- EP-04a: For the EtMgBr/PhCl entry (98% yield), run a parallel reaction with an explicit homo-coupling test: identify and quantify Et-Et byproduct by glpc against an authentic Et-Et standard; report as "Et-Et: X% by glpc." The mechanistic significance is compound: eq 3 predicts R–R as a stoichiometric byproduct of the initiation step; if Et-Et is absent at <1%, this simultaneously validates the selectivity claim and constrains the mechanistic cycle.
- EP-09a: Run n-BuMgBr + PhCl under Tamura-Kochi Fe conditions (or cite a published yield for the same substrate combination) to provide the single head-to-head numerical comparison required to substantiate "seldom employed in synthetic practice" for the prior-method class.

**Notes**: U-1 is severity=high (self-contradictory absence: eq 3 predicts homo-coupling byproduct R–R, which is neither detected nor acknowledged as undetectable in Table I); B-6 is high_convergence_low_gap (V2=high, V3=high; convergence=2/3; gap=none); C-1 is severed citation affecting the core comparative positioning. RI-04 takes priority: U-1 identifies a single prediction of the catalytic cycle (homo-coupling byproduct) that should have been detectable and was not reported, constituting an unreplicated discriminator with high interpretive weight. RI-09 is secondary: the superiority claim against Tamura-Kochi rests entirely on asserted scope differences rather than any direct comparison yield.

---

#### SRG-3 [Scope restriction without negative-result evidence]

Members: B-4, A-3

**Primary RI**: RI-07 [Unsupported boundary]

**ER**: The claim that "only C_sp² halides can be used" must be substantiated by at least one reported failed reaction with a C_sp³ alkyl halide (e.g., n-BuCl or EtCl) under otherwise standard conditions, with product yield reported as 0% or <detection limit.

**EP**: EP-07a (Boundary-test pack)

**Case-specific implementation**:
- EP-07a: Run n-BuMgBr + n-BuCl under the identical [NiCl₂(dpe)] conditions used for Table I Entry 1 (EtMgBr/PhCl) and report the yield of cross-coupling product (n-Bu-n-Bu or n-Bu-(n-Bu)) alongside any homo-coupling byproduct; include the result in Table I as the sp³ boundary demonstration entry.

**Notes**: B-4 is high_convergence_low_gap (V1=medium, V2=medium, V3=medium; convergence=3/3; gap=none) — the highest convergence item in the entire Stage 1 analysis. A-3 is the companion deferral. RI-07 extended use (negative boundary claim) applies: the exclusion of sp³ halides is presented as a positive feature of the method without a single negative-result datum. RI-07 is not fatal to Layer 1 but substantially weakens the boundary claim as stated.

---

#### SRG-4 [Stereochemical outcome and its mechanistic basis]

Members: A-1, B-11

**Primary RI**: RI-04 [Unreplicated discriminator]
**Secondary RI**: RI-01 [Reporting integrity]

**ER**: The cis:trans stilbene ratios (80:20 from cis-DCE; 43:57 from trans-DCE) must be measured by a stated analytical method with sufficient precision to determine whether the 43:57 ratio differs significantly from a 50:50 statistical mixture; and the elementary step at which geometric information from the vinyl halide is lost must be identified.

**EP**: EP-04a (Discrimination / replication pack); EP-01a (Reporting-coherence pack)

**Case-specific implementation**:
- EP-04a: Re-measure the cis:trans ratio for both DCE entries by ¹H NMR (coupling constants J_cis ≈ 10–12 Hz, J_trans ≈ 16 Hz) with explicit integration and reported uncertainty; at 43:57, a ±3% analytical uncertainty changes the mechanistic interpretation between "partial retention" and "near-statistical scrambling."
- EP-01a: State the analytical method (glpc or NMR) used to generate the 80:20 and 43:57 ratios in Table I footnote, and provide the same method disclosure for all five glpc-only entries.

**Notes**: A-1 is high_convergence_low_gap (V1=medium, V2=medium; convergence=2/3; gap=none); B-11 is low-convergence (V3=medium only). The 43:57 ratio is a critical discriminating datum: if within analytical uncertainty of 50:50, the observation collapses to "stereochemical information is completely lost," which is interpretively distinct from "anomalous cis enrichment." RI-04 takes priority over RI-01 because the discriminatory power of the cis:trans ratio is the primary stake.

---

#### SRG-5 [Yield data analytical quality]

Members: B-2, B-7, B-9, B-11

**Primary RI**: RI-08 [Unquantified reliability]
**Secondary RI**: RI-01 [Reporting integrity]

**ER**: The yield figures in Table I must be either replicated (n ≥ 2) with reported standard deviation, or accompanied by sufficient analytical metadata (internal standard identity, response factors, glpc purity percentages, or elemental analysis) to evaluate their reliability independently.

**EP**: EP-08a (Replication / uncertainty pack); EP-01a (Reporting-coherence pack)

**Case-specific implementation**:
- EP-08a: For the two preparative examples (Example 1: m-di-n-butylbenzene, 94%; Example 2: α-vinylnaphthalene, 80%), conduct one additional independent run and report the range; extend this to the two entries most critical to the improvement claim (highest yield: EtMgBr/PhCl, 98%; lowest: n-BuMgBr/PhCl, 76%).
- EP-01a: Provide a Table I footnote specifying (a) the identity of the glpc internal standard and the response-factor basis, (b) which products were confirmed by all four analytical methods (glpc, NMR, IR, mass spectrometry) vs. a subset, and (c) the basis for the "pure" designation in Example 1 (GC purity %, elemental analysis, or other).

**Notes**: B-2 is high_convergence_low_gap (V1=medium, V3=medium; convergence=2/3; gap=none); B-7, B-9, B-11 are low-convergence but collectively constitute the RI-08 subtype (internal inconsistency — dual yield basis without systematic justification). RI-08 subtype (internal inconsistency) applies: glpc and isolated yields are mixed in the same Table I column with footnotes d and e but without systematic cross-referencing. This SRG is non-fatal to Layer 1 but is the primary analytical quality vulnerability if an independent replication is attempted.

---

#### SRG-6 [Prior work numerical comparison gap]

Members: C-1, C-2, A-4

**Primary RI**: RI-09 [External superiority]

**ER**: The claim that prior transition-metal-catalyzed cross-coupling methods "are seldom employed in synthetic practice" due to homo-coupling formation must be substantiated by at least one direct quantitative comparison — yield, cross:homo ratio, or functional-group tolerance — between the Ni-dpe system and a prior method (Tamura-Kochi Fe or Corriu-Masse Ni(acac)₂) on at least one shared substrate.

**EP**: EP-09a (Internal benchmark pack)

**Case-specific implementation**:
- EP-09a: Run n-BuMgBr + CH₂=CHCl (vinyl chloride) under Tamura-Kochi Fe conditions as a direct comparison with Table I Entry 5 (n-C₅H₁₁MgCl + CH₂=CHCl, 95%); if a direct comparison is not feasible, cite the Corriu-Masse published yield for the most overlapping substrate combination and state the difference numerically.

**Notes**: A-4 (forgotten deferral — no prospective acknowledgment that a comparison with Corriu-Masse will be made) is the most unusual SRG-6 item: the concurrent submission is noted in proof but neither compared nor prospectively addressed. C-2 (cuprate/allylnickel dismissal) is a symmetric citation pattern. RI-09 is the primary code; no secondary RI is warranted since all three items map to the same external-comparison deficiency. SRG-6 intersects with SRG-2 through the shared stake: C-1 contributes to the homo-coupling selectivity comparison gap as well as the prior-work comparison gap.

---

#### Outside the SRGs: CLAs

**CLA-1: Quantitative catalyst operational data (TON and ligand ranking values)**

Grounded in: B-1, B-3 (D-4 Candidate 7; not members of any SRG)

**Primary RI**: RI-05 [Qualitative overread]

**ER**: The ligand activity ranking ([NiCl₂(dpp)] > [NiCl₂(dpe)] > ... ≫ [NiCl₂(PEt₃)₂]) and the catalyst loading range (10⁻² to 10⁻³) must be supported by the yield values for each catalyst on the specified substrate (n-BuMgBr + chlorobenzene) and by at least one TON determination (moles product per mole catalyst), respectively.

**EP**: EP-05a (Quantitative-ranking substantiation pack)

**Case-specific implementation**: Report yield (%) for each of the six catalyst complexes tested with n-BuMgBr + chlorobenzene in a supplementary table, and calculate TON for [NiCl₂(dpe)] at the lower loading limit (10⁻³ equiv) in Example 1 by quantifying isolated product per mole catalyst used.

**Notes**: B-1 is high_convergence_low_gap (V1=medium, V3=low; convergence=2/3; gap=low); B-3 is high_convergence_low_gap (V1=medium, V2=medium; convergence=2/3; gap=none). CLA-1 is non-fatal: the absence of numerical ligand ranking values and TON does not invalidate the synthetic utility claim but prevents evaluation of the structure-activity relationship that the authors invoke to explain the catalytic cycle (cis-geometry requirement). RI-05 is warranted because the paper draws structural-mechanistic implications (cis geometry as "first requisite") from a qualitative ranking without the numerical support that would allow the ranking to be challenged.

---

**CLA-2: Solvent superiority claim without comparative data**

Grounded in: B-5 (D-4 Candidate 8; not a member of any SRG)

**Primary RI**: RI-09 [External superiority]

**ER**: The statement [REDACTED: substantial verbatim quotation; see Tier 9] must be supported by at least one yield or conversion comparison of an identical reaction run in both solvents under otherwise identical conditions.

**EP**: EP-09a (Internal benchmark pack)

**Case-specific implementation**: Run EtMgBr + PhCl (Table I Entry 1) in THF instead of diethyl ether under the same [NiCl₂(dpe)] loading, temperature, and time, and report the yield alongside the ether result.

**Notes**: B-5 is low-convergence (V1=low, V2=low; convergence=2/3; gap=none). CLA-2 is non-fatal: the solvent claim is a secondary feature (feature 5 of five) and does not affect the validity of any Table I entry. "Definitely" is the lexical signal that comparative data exist unpublished; CLA-2 records the gap between the rhetorical strength of that word and the absence of supporting data.

---

### §3 Current VQ assessment

**Current judgment: VQ-2 (Method) — conditional pass; VQ-3 (Mechanism) — fails**

---

**VQ-1 [Observation] — PASS (non-fatal qualification noted)**

RI-02 (Object identification) is assessed as non-fatal. The products in Table I are characterized by glpc, NMR, IR, and/or mass spectra, and physical constants (bp, refractive index) are compared against literature values in the preparative examples. The "and/or[REDACTED: substantial verbatim quotation; see Tier 9]pure" designation in Example 1 lacks elemental analysis. However, the comparison of bp 84° (5 mm) with the literature value bp 75–76° (0.4 mm), while numerically consistent after pressure correction, is not annotated — a minor RI-02 issue. These are judged non-fatal: product identity at the class level (cross-coupling product class, not a single enantiomer or regioisomer) is adequately established for the synthetic utility claim. VQ-1 holds with the non-fatal RI-02 qualification that full elemental analysis or HRMS per compound was not provided.

---

**VQ-2 [Method] — CONDITIONAL PASS (on premise that RI-02 is non-fatal)**

Inheriting from VQ-1 (RI-02 non-fatal per above).

RI-01 (Reporting integrity): **Non-fatal, with qualification.** The dual yield-basis in Table I (isolated yield vs. glpc-only for five entries; B-2) and the undisclosed glpc calibration basis (B-7, B-9) constitute a reporting-coherence deficit. However, the two preparative examples provide isolated yields with full experimental procedures, establishing a concrete reference point. The glpc-only yields are not structurally critical to the paper's overall scope claim. The qualification: the analytical uncertainty of the 43:57 cis:trans ratio (B-11) is the one case where RI-01 becomes interpretively significant (see SRG-4), but this affects only the stereochemical sub-claim (feature 4), not the cross-coupling scope claim.

RI-07 (Unsupported boundary): **Non-fatal, with qualification.** The exclusion of sp³ halides (SRG-3, B-4) is asserted without a single failed example. This is the highest-convergence item (3/3 agents) in the paper. However, since the sp² restriction is consistent with the chemical logic of the proposed cycle (sp² C–Cl bonds are known to undergo oxidative addition at Ni; sp³ C–Cl bonds do not, at least not efficiently under the same conditions), the boundary claim has mechanistic plausibility even without direct negative-result data. The qualification: RI-07 remains unresolved and would require EP-07a for formal closure.

VQ-2 holds on the premise that RI-02 is non-fatal, and on the premise that RI-01 and RI-07 are non-fatal for Layer 1 (synthetic utility) but unresolved for Layer 2 (mechanism and scope definition).

---

**VQ-3 [Mechanism] — FAILS**

Inheriting from VQ-2 (RI-01, RI-07 non-fatal per above).

RI-03 (Unobserved explanatory): **Fatal for Layer 2.** None of the three key intermediates in the proposed catalytic cycle (diorganonickel complex 1, haloorganonickel complex 2, and the regenerated complex 2 via complex 3) is directly observed under actual [NiCl₂(dpe)] catalytic conditions (SRG-1, A-2). The proposed mechanism is constructed entirely by analogy with stoichiometric (dipy)Ni reactions.

RI-06 (Imported model): **Fatal for Layer 2.** The entire catalytic cycle (eqs 2–4) is imported from a structurally distinct (dipy)Ni stoichiometric system without establishing isomorphism. The (dipy)Ni complex has a non-chelating bipyridyl ligand with a different bite angle and coordination geometry from [NiCl₂(dpe)]; the mechanistic analogy is asserted in the paper's text ("These facts suggest a catalytic ability…") rather than demonstrated. The black precipitate (B-12, U-2) provides in-text evidence consistent with Ni⁰ formation — an alternative active species not captured by the (dipy)Ni→(dpe)Ni import.

RI-04 (Unreplicated discriminator): **Fatal for the selectivity sub-claim of Layer 2.** The self-contradictory absence (U-1): the proposed cycle (eq 3) predicts homo-coupling product R–R as a stoichiometric byproduct; no R–R is detected, quantified, or acknowledged as below detection limit. This single gap simultaneously (a) leaves the mechanistic cycle internally unverified and (b) makes the selectivity claim of Layer 1 vulnerable (see §1 inter-layer analysis below).

**Layered VQ asymmetry:**

The paper-wide VQ judgment is VQ-2 (conditional) / VQ-3 fails. However, **Layer 1 (Synthetic utility) on its own** reaches VQ-2 firmly: the scope (ten substrate combinations, two preparative examples) and yield data (Table I) substantiate the synthetic utility claim at the reporting level, and RI-07 (sp² boundary) and RI-01 (yield basis) are non-fatal for this layer. Layer 1 does not reach VQ-3 because RI-04 (SRG-2, U-1) creates a vulnerability in Layer 1 as well: "selective" cross-coupling is a Layer 1 claim, and the absence of any cross:homo ratio leaves this claim qualitative (supported by absence of reported byproducts, not by measured suppression).

**Layer 2 (Mechanistic rationalization) on its own** fails VQ-3 for three independently sufficient reasons: RI-03, RI-06, and the Layer 2 component of RI-04.

---

### §4 Era-Norm Annotation

**communication-era tolerated:**

- **B-1** (TON and catalyst loading optimization data absent): In 1972 JACS Communications, catalyst loading was routinely reported as a stoichiometric ratio with the disclaimer "conditions are not necessarily optimum." TON as a figure of merit was not standard reporting practice in preparative synthetic chemistry communications in this period.

- **B-2** (Dual yield-basis — isolated vs. glpc-only in the same table column): Mixing of isolated and glpc-quantified yields in a single table column was standard practice in synthetic communications of the 1970s; the disclosure of the dual basis via footnotes d and e represented the expected level of transparency for the format.

- **B-7** (Characterization "and/or" formulation without per-compound method disclosure): The "and/or" formulation as a collective characterization footnote was genre-standard in 1972 JACS Communications; per-compound analytical tables appeared in full papers, not communications.

- **B-9** (All yields are single determinations without replicates): Single-determination yield tables were standard in synthetic communications; replicate data and standard deviations in yield tables were not expected conventions in organic or organometallic chemistry publications of this era.

- **A-1, A-2** (Explicit mechanistic deferrals with "Further studies are required" language): This phrase was the standard JACS Communications formula for signaling preliminary status; the communication format was explicitly designed for priority establishment before complete characterization.

- **A-3** (Scope extension deferred): "Investigations are continuing on the extension, refinement, and application" is the conventional prospective statement in communications of this period, serving the same priority-signaling function as A-1/A-2.

- **B-13, B-14** (Substrate-dependent reaction time without kinetic data): In 1972, time-course data and induction-period characterization were not standard elements of synthetic communications; the 20-hour reflux condition was reported as a practical guideline without mechanistic contextualization.

---

**modern-era deficient:**

- **B-6** (No cross:homo product ratio for any Table I entry): By contemporary standards, a paper titled "Selective Cross-Coupling" requires at least one entry with a quantified byproduct yield; the absence of any homo-coupling quantification — even a "<1% by glpc" annotation — is insufficient for a claim with "selective" in the title. This item was *tolerated in the communication era* (see above) but is deficient by modern standards; it thus bears a dual classification.

- **U-1** (Homo-coupling byproduct predicted by eq 3 not reported): Contemporary catalysis papers are expected to address mechanistic predictions of their own catalytic cycles explicitly; a cycle that predicts a byproduct that is not reported creates a self-consistency requirement that modern reviewers would flag. Dual classification: era-tolerated (see B-6) but modern-deficient.

- **B-4** (sp² restriction asserted without a single failed sp³ halide example): Contemporary scope characterization in synthetic catalysis requires at least one reported failed substrate to substantiate an exclusion. The absence of any negative-result datum for sp³ alkyl halides does not meet modern reporting standards for a boundary claim.

- **B-12** (Black precipitate in Example 1 uncharacterized and unacknowledged as potentially mechanistically significant): By contemporary standards, in-procedure observations consistent with catalyst decomposition or alternative active-species formation must be addressed, particularly when a homogeneous mechanism is proposed. A mercury-drop test or hot-filtration test would be required in a modern submission.

- **B-3** (Ligand activity order without numerical yield values): Contemporary structure-activity relationships require numerical support; a qualitative ranking without the underlying data from which it was derived (footnote 21 specifies only "n-BuMgBr with chlorobenzene" but provides no yields) is insufficient for a modern publication in catalysis.

- **B-11** (Cis:trans ratio method undisclosed): At 43:57, the analytical method choice (glpc vs. ¹H NMR) substantially affects the precision of the claim; modern characterization standards require method disclosure for stereochemical determinations.

- **C-1** (Prior-method comparison asserted rather than measured): By contemporary standards, the claim that prior methods "are seldom employed in synthetic practice" requires at least one head-to-head yield comparison on a shared substrate, not qualitative scope differentiation.

---

### §5 Shortest-reinforcement route

**First objective function: Advance from VQ-2 (conditional) to VQ-3 (Mechanism)**

The unresolved RIs blocking VQ-3 are: RI-06 (imported model), RI-03 (unobserved explanatory), and RI-04 (unreplicated discriminator — in its selectivity application via SRG-2). These require EP-04a, EP-06a, and EP-03a. The ordering follows information gain and experimental feasibility.

---

**Shortest route to VQ-3:**

1. **EP-04a** [Discrimination / replication pack] — Quantify homo-coupling byproduct (e.g., Et-Et from EtMgBr/PhCl entry) by glpc against an authentic standard and report as a percentage of the theoretical yield; this single experiment simultaneously (a) closes U-1 (self-contradictory absence), (b) provides the discriminating datum for the selectivity claim (SRG-2), and (c) constrains the mechanistic cycle (if Et-Et is detected at the level predicted by eq 3's initiation step, the proposed cycle is consistent; if absent, eq 3 requires revision).
   Advances RI-04 (SRG-2); resolves U-1.

2. **EP-07a** [Boundary-test pack] — Run n-BuMgBr + n-BuCl under standard conditions and report the yield of cross-coupling product and any byproducts; this closes SRG-3 (RI-07) and provides the negative-result evidence required for the sp² boundary claim.
   Advances RI-07 (SRG-3); resolves B-4.

3. **EP-06a** [Analogy-validation pack] — Synthesize and characterize [dpe-Ni(n-Bu)(Cl)] and [dpe-Ni(n-Bu)₂] independently; demonstrate that their stoichiometric reactions with PhCl and n-BuMgBr, respectively, reproduce the catalytic selectivity; conduct a mercury-drop test or hot-filtration test on the Example 1 reaction mixture to determine whether catalytic activity is homogeneous or heterogeneous.
   Advances RI-06 (SRG-1) and RI-03 (SRG-1); partially resolves A-2, U-2, B-12.

4. **EP-03a** [Direct-observation / state-assignment pack] — Characterize the active catalyst by in-situ NMR or UV-Vis spectroscopy during a catalytic run; identify whether [NiCl₂(dpe)] is reduced to Ni⁰ under the reaction conditions and at what point in the induction period.
   Advances RI-03 (SRG-1); resolves U-2.

*Certification-gate note: The experimental investment order (EP-04a → EP-07a → EP-06a → EP-03a) follows information gain, but the final VQ certification follows the inheritance principle: RI-02 and RI-01/RI-07 (VQ-1 and VQ-2) must be confirmed non-fatal before VQ-3 can be certified, regardless of when the EP investments are completed.*

---

**Second objective function: Advance from VQ-3 to VQ-4 (Benchmark)**

Once VQ-3 is certified, the remaining unresolved RIs are RI-08 (SRG-5) and RI-09 (SRG-6, CLA-2).

---

**Shortest route to VQ-4:**

1. **EP-09a** [Internal benchmark pack] — Run the most representative Table I substrate combination (EtMgBr/PhCl or n-BuMgBr/PhCl) under Tamura-Kochi Fe conditions and under Corriu-Masse Ni(acac)₂ conditions; report the cross-coupling yield and the cross:homo ratio for each system in a comparative table.
   Advances RI-09 (SRG-6); closes C-1, C-2, A-4.

2. **EP-08a** [Replication / uncertainty pack] — Replicate the two preparative examples (Example 1 and Example 2) on independent runs and report yield ranges; additionally, conduct the five glpc-only Table I entries in parallel with a calibrated internal standard and disclose the standard identity and response factors.
   Advances RI-08 (SRG-5); closes B-2, B-7, B-9.

3. **EP-05a** [Quantitative-ranking substantiation pack] — Report the yield (%) for each of the six catalyst complexes tested with n-BuMgBr + chlorobenzene (footnote 21 conditions) as a supplementary table, and calculate TON for [NiCl₂(dpe)] in Example 1.
   Advances RI-05 (CLA-1); closes B-1, B-3.

*Certification-gate note: VQ-4 certification requires that all VQ-3 prerequisites (RI-06, RI-03, RI-04) be resolved first; EP-09a, EP-08a, and EP-05a can be executed in parallel, but VQ-4 is not certifiable until VQ-3 is certified.*

---

**Top-3 EP rank order (single list across both objective functions, ordered by information gain):**

1. **EP-04a** — highest information gain: simultaneously closes U-1 (self-contradictory absence, severity=high), advances RI-04 (SRG-2, the selectivity claim's central vulnerability), and constrains the mechanistic cycle via eq 3; single glpc experiment executable without new synthesis.

2. **EP-06a** — second highest: independently synthesizing intermediates 1 and 2 under dpe-Ni conditions converts the entire mechanistic proposal from an imported analogy (RI-06) to a directly tested claim; simultaneously addresses RI-03 if in-situ characterization is combined; requires the most experimental investment but provides the most mechanistic yield.

3. **EP-07a** — third highest: single negative-result experiment resolves the highest-convergence item in the analysis (B-4, convergence=3/3); requires no new reagents beyond the Table I setup.

---

### §6 Contribution to institutional design

**1. Labeling mismatch — confirmed representative case:**

The Kumada 1972 paper provides a clear representative case for the Labeling mismatch pattern specified in the Stage 3 v2 prompt. The authors explicitly label the catalytic cycle in the final substantive sentence as "the working hypothesis described above," yet throughout eqs 2–4 and their narrative framing the text uses exclusively factual verbs: "reacts with" (eq 2), "is subsequently converted to" (eq 2→3), "releases" (eq 3), "is regenerated to complete the catalytic cycle" (eq 4). The hypothesis label is concentrated in a single sentence at the end of the discussion section, while four preceding sentences and four equations use the declarative mode. This case confirms the Labeling mismatch entry in the institutional codebook and extends it to the specific context of a proposed catalytic cycle (as distinct from a single mechanistic step or a structural assignment). The co-occurrence with RI-06 is directly confirmed: the factual verb framing of an imported model is the operational signature of this pattern.

**2. RI-06 cycle-level import — confirmed and extended:**

SRG-1 confirms the RI-06 scope note (cycle-level import) for a case in which an entire catalytic cycle is constructed from a non-isomorphous stoichiometric system ((dipy)Ni → (dpe)Ni). The specific structural mismatches that make the import potentially non-isomorphous are: (a) bidentate chelation geometry (dpe enforces a specific P–Ni–P bite angle absent in dipy); (b) stoichiometric vs. catalytic conditions (concentration regime, steady-state intermediate ratios); and (c) the possibility of Ni⁰ nanoparticle formation under the actual catalytic temperature (80°C reflux) that does not arise in room-temperature stoichiometric reactions. The Kumada case thus adds an implementation criterion for RI-06: for cycle-level import, the lethality of the RI depends on whether the imported-from system is stoichiometric (and thus potentially operates under very different concentration and temperature conditions than the target catalytic system).

**3. RI-04 + RI-06 co-occurrence — new institutional note:**

In SRG-1/SRG-2, RI-04 and RI-06 co-occur in a specific structural relationship: the imported model (RI-06) generates a prediction (homo-coupling byproduct R–R via eq 3) that, if verified, would simultaneously test the validity of the imported cycle. This creates a compound investment opportunity: EP-04a (discrimination/replication to detect R–R) simultaneously tests RI-04 (unreplicated discriminator) and constrains RI-06 (whether the imported cycle's eq 3 prediction is empirically satisfied). The institutional note is: **when RI-04 and RI-06 co-occur in the same SRG, the mechanistic prediction of the imported model should be used as the discrimination test; this allows a single experiment to advance both RIs simultaneously**. This is a new case-specific implementation note for the EP dictionary.

**4. VQ asymmetry — synthetic utility layer reaches VQ-2 while mechanistic layer fails VQ-3:**

The Kumada paper provides a clear example of per-layer VQ asymmetry in a two-pillar claim structure. The synthetic utility layer (Layer 1) reaches VQ-2 and is non-fatally bounded by RI-07 and RI-01. The mechanistic layer (Layer 2) fails VQ-3 for three independently sufficient reasons (RI-03, RI-06, RI-04). This asymmetry is informative for institutional design: **a priority communication can achieve VQ-2 for its utility claim and simultaneously fail VQ-3 for its mechanistic claim; the communication format is structurally optimized to protect the utility layer while deferring the mechanistic layer**. This is consistent with the Automatic-resolution pattern (communication→Full Paper): A-1, A-2, A-3 are the canonical cases, where the deferrals are explicitly prospective and would be resolved in the expected Full Paper. The §4 era-norm annotation confirms that these deferrals were era-tolerated.

**5. Self-contradictory absence (U-item type) — confirmed institutional case:**

U-1 (homo-coupling byproduct predicted by eq 3 not reported) is a clean example of the self-contradictory-absence CLA pattern. The catalytic cycle itself is the source of the prediction; the primary data table is the location of the absence; the paper's own language ("selective") is the claim that the absence is meant to support. The Kumada case thus provides an anchor example for the self-contradictory-absence detection rule in §2's CLA check: **the U-item pattern is not merely an analytical omission but a logical gap in which the model and the data tell incompatible stories when the model's predictions are taken seriously**. The institutional note for the EP dictionary is that EP-04a (Discrimination/replication pack) is the standard remediation for this pattern: the predicted byproduct should be explicitly searched for and its yield (or upper bound) reported.

**6. PRI-11 candidate — not promoted in this case:**

The paper proposes a catalytic cycle without deriving a rate law from it algebraically (PRI-11: Mechanism–kinetics decoupling). However, in a 1972 synthetic chemistry communication, the expectation to derive and validate a rate law from a proposed mechanism was not an entry criterion; the mechanism is explicitly labeled as a working hypothesis. PRI-11 is therefore applicable in principle but era-norm tolerated (see §4). No promotion action is warranted for this paper alone; if PRI-11 is confirmed in a post-1990 synthetic organometallic paper with a comparable pattern, promotion criteria would be satisfied. The Kumada case is recorded as a historical anchor for PRI-11 with the era-norm flag.

**7. Automatic-resolution pattern — confirmed:**

A-1 (stereochemical deferral), A-2 (complete mechanistic evidence gap), and A-3 (scope extension deferral) are all automatic-resolution candidates: in the expected Full Paper(s) from the Kumada group (which followed: Tamao et al., JACS 1976; J. Organometal. Chem. series), these deferrals were in fact resolved. The Kumada 1972 communication is therefore a clean historical case of the communication-format automatic-resolution pattern: **the RI-01 (scope restriction) and RI-07 (boundary assertion) issues generated by the 3-page format were prospectively flagged by the authors themselves and resolved in subsequent full publications**. This pattern is most cleanly captured by the language "Investigations are continuing on the extension, refinement, and application" (A-3), which functions simultaneously as a deferral acknowledgment and a prospective resolution commitment.

**Summary statement:** This case confirms the existing institutional design for RI-03, RI-04, RI-06, RI-07, RI-08, and RI-09, and extends it in three directions: (a) a documented case of Labeling mismatch co-occurring with RI-06 in a full catalytic-cycle context; (b) a new compound-investment implementation note for EP-04a when RI-04 and RI-06 co-occur; and (c) a clean historical anchor for the Automatic-resolution pattern in which JACS Communications-format deferrals (A-1, A-2, A-3) map directly to the subsequent full publication program.

---

> **Tier 8 redaction notice**: This file is a redacted copy of the corresponding Tier 3 / Tier 9 output. Verbatim source-paper quotations have been replaced by `[REDACTED: see source paper §<loc>; full text retained in Tier 9 reviewer-only deposit]` markers, preserving location references and our own analytical content. Bibliographic fields (title, authors, journal, year, DOI), analytical labels (`evidence_chain:` with B-/U-/A-/C- internal IDs), short technical terms, and our own analytical text are not redacted. The redaction was applied by `scripts/redact_for_tier8.py` and, for this version, by `scripts/build_paperA_R1_public.py` with `scripts/redact_source_ngram_runs.py` (scripts of the project repository; they are not deposited).
