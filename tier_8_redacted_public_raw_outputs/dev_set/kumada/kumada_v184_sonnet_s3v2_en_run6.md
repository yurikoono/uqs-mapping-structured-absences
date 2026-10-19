```
prompt_version: stage3-v2-en-20260419
model_info: claude-sonnet-4-6 (run #6, EN track, independent)
```

---

# Re-certification Assessment Sheet for Scientific Knowledge

## Tamao, Sumitani, Kumada 1972 (JACS, communication)

---

### §1 Claim Architecture

**Core claim summary:**

The paper introduces a preparative method for selective cross-coupling of Grignard reagents with vinyl or aryl (sp²) organic halides, catalyzed by a nickel-diphosphine complex — primarily [NiCl₂(dpe)]. The Novelty pillar rests on two linked sub-claims: (a) that the Ni-diphosphine system is *selective* for cross-coupling product over homo-coupling byproducts, in contrast to prior transition-metal-halide systems which produce homo-coupling in substantial amounts; and (b) that the mechanism operates through a proposed three-step catalytic cycle (eqs 2–4) — a genuine catalytic mode, not stoichiometric reagent consumption — made plausible by analogy with stoichiometric (dipy)Ni chemistry. The Utility pillar rests on the claim that "generally very high yields" are achievable even with alkyl Grignard reagents bearing β-hydrogen atoms, with a demonstration of one-step access to m-di-n-butylbenzene ("hardly accessible by conventional methods").

**Layered structure judgment:**

Three largely independent layers are identifiable:
- **Layer 1 — Selectivity claim**: "selective cross-coupling" over homo-coupling (Claim 1). Evidence: Table I yields without cross:homo ratio data.
- **Layer 2 — Mechanistic proposal**: three-step catalytic cycle (eqs 2–4), explicitly labeled "a working hypothesis."
- **Layer 3 — Practical utility**: "useful preparative method" with "generally very high yields" across ten substrate combinations.

Independent layers exist: refuting the mechanistic working hypothesis (Layer 2) would not collapse the synthetic yield data (Layer 3), and challenging the yield quality (Layer 3) does not undermine the mechanistic analogy (Layer 2). However, Layer 1 (selectivity) depends on both: without a verified mechanism, the *reason* for selectivity is hypothetical; without a cross:homo product ratio, the *fact* of selectivity is undemonstrated. Layer 1 is therefore the pivot layer — most exposed, most under-evidenced — while Layers 2 and 3 each have partial independent standing. The "working hypothesis" hedge in Layer 2 insulates it from refutation by Table I data alone, which is the characteristic structure of communication-format layering.

---

### §2 SRG / CLA → RI / ER / EP Crosswalk

#### SRG-1: Catalytic mechanism evidence gap

**SRG members:** A-2, U-1, U-2, B-12

**Primary RI:** RI-06 [Imported model]
**Secondary RI:** RI-03 [Unobserved explanatory]

**ER:** For the proposed catalytic cycle (eqs 2–4) to be accepted as a mechanistic account rather than an analogy, at minimum one elementary step under actual [NiCl₂(dpe)] catalytic conditions must be directly verified — either by observation of an intermediate (1, 2, or 3) or by a kinetic signature consistent with the proposed cycle. The import of the stoichiometric (dipy)Ni mechanism (eq 1, refs 11–12) to the catalytic [NiCl₂(dpe)] system constitutes RI-06 (cycle-level import). The un-characterized black precipitate in Example 1 — consistent with Ni⁰ nanoparticle formation — means that the proposed homogeneous Ni(II) active species (intermediates 1–3) is neither observed nor excluded, constituting RI-03.

**EP:** EP-06a (Analogy-validation pack); EP-03a (Direct-observation / state-assignment pack)

**Case-specific implementation:**
- EP-06a: Synthesize [NiCl₂(dpe)] analogs of intermediates 1 (L₂NiR₂) and 3 (L₂Ni(R')(R)) independently; verify that they exhibit the predicted reactivity with organic halides and Grignard reagents respectively under catalytic conditions. Confirm that the bidentate dpe ligand remains coordinated throughout the catalytic cycle (vs. dissociation to a Ni⁰ species).
- EP-03a: Characterize the black precipitate from Example 1 by magnetometry or elemental analysis to distinguish Ni⁰ metal from intact [NiCl₂(dpe)] or other Ni(II) species. If Ni⁰ is confirmed, revise the proposed catalytic cycle or establish a Ni⁰/Ni(II) redox cycle.

**Notes:** A-2 in high_convergence_low_gap (V1=high, V2=high; convergence=2/3, gap=none) — mechanistic evidence gap, highest combined weight in TEMPERATURE_SUMMARY. B-12 is the observational anchor for U-2 (self-contradictory absence: black mixture consistent with Ni⁰ decomposition, uncharacterized). RI-06 scope note (cycle-level import) applies: the entire proposed Ni(II) cycle is constructed by analogy from a single stoichiometric (dipy)Ni precedent (eq 1), without demonstrating isomorphism under the actual [NiCl₂(dpe)] catalytic conditions.

---

#### SRG-2: Cross/homo-coupling selectivity quantification

**SRG members:** B-6, U-1, C-1

**Primary RI:** RI-04 [Unreplicated discriminator]
**Secondary RI:** RI-09 [External superiority]

**ER:** The paper's central Novelty pillar ("selective cross-coupling") requires a demonstrated cross:homo product ratio for at least one Table I entry, enabling a quantitative comparison with the prior art (Tamura-Kochi, refs 5–6) that the paper asserts is inferior due to "homo coupling products in substantial amounts." Without this, both the absolute selectivity of the new system and its relative advantage over prior methods are undemonstrated numerically.

**EP:** EP-04a (Discrimination / replication pack); EP-09a (Internal benchmark pack)

**Case-specific implementation:**
- EP-04a: For the n-BuMgBr + PhCl entry (Table I, isolated yield 76%), report the glpc-determined cross:homo product ratio (Ph-n-Bu : n-Bu-n-Bu) in the crude reaction mixture prior to workup. Repeat for at least one vinyl halide entry (e.g., n-C₅H₁₁MgCl + CH₂=CHCl, glpc yield 95%) to establish a substrate-type comparison.
- EP-09a: Run n-BuMgBr + PhCl under Tamura-Kochi Fe-catalyst conditions (ref 5) in a head-to-head experiment, report cross:homo ratio alongside the Ni-dpe result to substantiate the "seldom employed in synthetic practice" positioning.

**Notes:** U-1 (high severity, self-contradictory absence) — the paper's own eq 3 predicts R–R as a byproduct; its complete absence from Table I is neither explained nor acknowledged. B-6 in high_convergence_low_gap (V2=high, V3=high; convergence=2/3, gap=none). C-1 records the dropped quantitative benchmark specifically for the Tamura-Kochi comparison. RI-09 is secondary: superiority over prior methods is asserted through citation contrast alone ("seldom employed in synthetic practice"), not through any parallel measurement on a shared substrate.

---

#### SRG-3: Scope restriction without negative-result evidence

**SRG members:** B-4, A-3

**Primary RI:** RI-07 [Unsupported boundary]

**ER:** The claim [REDACTED: substantial verbatim quotation; see Tier 9] defines an exclusive scope boundary. Standard scope characterization requires at least one reported failed substrate (showing zero or trace yield) to demonstrate, rather than merely assert, the exclusion. Without negative-result data for any sp³ or allyl halide, the boundary is mechanistically inferred but experimentally undemonstrated.

**EP:** EP-07a (Boundary-test pack)

**Case-specific implementation:**
- EP-07a: Report the results of [NiCl₂(dpe)]-catalyzed reactions of n-BuMgBr with at least one sp³ alkyl chloride (e.g., n-BuCl) and one allyl chloride (allyl-Cl) under Condition A, providing yield or conversion data — even if zero or trace — to establish the scope boundary empirically rather than by assertion.

**Notes:** B-4 is the only three-agent convergence item in the entire TEMPERATURE_SUMMARY (V1=medium, V2=medium, V3=medium; convergence=3/3, gap=none), making it the highest-priority item under the fallback rule. A-3 contributes the companion observation: the scope-extension deferral ("Investigations are continuing on the extension, refinement, and application…") and the scope restriction without negative evidence are complementary faces of the same gap (SRG-3's shared root).

---

#### SRG-4: Stereochemical outcome and its mechanistic basis

**SRG members:** A-1, B-11

**Primary RI:** RI-04 [Unreplicated discriminator]
**Secondary RI:** RI-01 [Reporting integrity]

**ER:** The cis:trans stilbene ratios (80:20 from cis-DCE; 43:57 from trans-DCE) are presented as a mechanistically significant observation ("anomalously enriched with the cis isomer"), yet the analytical method used to determine these ratios is not disclosed, and no mechanistic hypothesis — even at a working-hypothesis level — is offered for the anomaly. The uncertainty associated with the 43:57 ratio (plausible ±5% for undisclosed glpc) would substantially alter the interpretation (from "partial retention" to "near-random"), making this a single high-discriminatory-power observation interpreted at a mechanistically significant level without adequate analytical precision.

**EP:** EP-04a (Discrimination / replication pack); EP-01a (Reporting-coherence pack)

**Case-specific implementation:**
- EP-04a: Repeat the cis-DCE and trans-DCE coupling experiments in triplicate; report the mean cis:trans stilbene ratio ± standard deviation with the analytical method stated explicitly (¹H NMR coupling constants vs. glpc with calibrated standards). Determine whether the 43:57 ratio from trans-DCE is statistically distinct from 50:50 (random).
- EP-01a: Disclose the analytical method (¹H NMR or glpc) and the identity of any reference standards used to assign cis vs. trans stilbene configurations.

**Notes:** A-1 in high_convergence_low_gap (V1=medium, V2=medium; convergence=2/3, gap=none). The asymmetry is notable: the overall catalytic cycle receives a four-equation working hypothesis; the anomalous stereochemical outcome (the most mechanistically interesting observation in the paper) receives only a synthetic application footnote ("This reaction may offer a facile route to cis-stilbene"). RI-01 applies as secondary: two yield-reporting bases (glpc and isolation) are applied without a method-assignment principle across the Table I column, also affecting the cis:trans reporting.

---

#### SRG-5: Yield data analytical quality

**SRG members:** B-2, B-7, B-9, B-11

**Primary RI:** RI-01 [Reporting integrity]
**Secondary RI:** RI-08 [Unquantified reliability]

**ER:** The "yields are generally very high" claim requires that the yield measurements share a common evaluable basis. Currently, five entries report isolated yields and five report glpc-based yields (with undisclosed internal standard, response factors, and calibration protocol), applied across the same "Yield, %[REDACTED: substantial verbatim quotation; see Tier 9]and/or[REDACTED: substantial verbatim quotation; see Tier 9]very high yield" designation is reproducible.

**EP:** EP-01a (Reporting-coherence pack); EP-08a (Replication / uncertainty pack)

**Case-specific implementation:**
- EP-01a: Assign each Table I entry explicitly to either isolated or glpc yield basis; for glpc entries, disclose the internal standard identity and the response factor used for the cross-coupled product. Provide mass balance for at least three glpc entries.
- EP-08a: Repeat at least three representative Table I entries (one aryl-aryl, one alkyl-aryl, one vinyl) in duplicate; report yield ± range or standard deviation.

**Notes:** SRG-5's shared root: [REDACTED: substantial verbatim quotation; see Tier 9] B-2 (yield-basis mixing) in high_convergence_low_gap (V1=medium, V3=medium; convergence=2/3, gap=none). B-9 (no replication) addressed by RI-08 as secondary. B-11 (analytical method for cis:trans ratio absent) overlaps with SRG-4; it is included in SRG-5 because the same systemic absence of analytical metadata applies.

---

#### SRG-6: Prior work numerical comparison gap

**SRG members:** C-1, C-2, A-4

**Primary RI:** RI-09 [External superiority]

**ER:** The paper positions itself against Tamura-Kochi (refs 5–6), against π-allylnickel and lithium cuprate systems (refs 7–10), and — in the Note Added in Proof — implicitly against the concurrent Corriu-Masse Ni(acac)₂ system. In each case, the superior performance of [NiCl₂(dpe)] is asserted through qualitative contrast language ("seldom employed in synthetic practice," "our interest centers on a transition metal catalyst," no comment in the Note Added in Proof) without any shared-substrate numerical comparison for any prior system.

**EP:** EP-09a (Internal benchmark pack)

**Case-specific implementation:**
- EP-09a: Run n-BuMgBr + PhCl under the Tamura-Kochi Fe-catalyst conditions (THF, ref 5) and under [NiCl₂(dpe)] conditions in the same laboratory, reporting isolated yield and glpc-determined cross:homo ratio for both. Separately, obtain the Corriu-Masse Chem. Commun. 1972 paper and perform an entry-by-entry substrate overlap comparison with Table I.

**Notes:** C-1 records dropped benchmark for Tamura-Kochi; C-2 records cite-and-dismiss for cuprate/allylnickel; A-4 records the concurrent Corriu-Masse communication as a forgotten deferral. The Note Added in Proof (footnote 3a) confirms a concurrent independent discovery, yet no conceptual or experimental distinction between [NiCl₂(dpe)] and Ni(acac)₂ is drawn anywhere in the paper. This undermines the implicit claim that the bidentate phosphine architecture is the essential enabling element.

---

#### Outside the SRGs: CLAs

---

**CLA-1: The paper's proposed mechanism predicts R–R homo-coupling as a stoichiometric byproduct of eq 3, yet R–R is absent from all ten Table I entries without acknowledgment (self-contradictory absence)**

*Note: U-1 is captured as a member of SRG-2 (via B-6). However, its self-contradictory-absence character warrants an independent CLA record per the self-contradictory-absence CLA check.*

**Primary RI:** RI-03 [Unobserved explanatory] (the predicted byproduct is an observable that the paper's own proposed model generates, yet is never reported)
**Secondary RI:** RI-06 [Imported model] (the mechanistic cycle in which R–R is generated is itself imported by analogy from stoichiometric (dipy)Ni chemistry)

**ER:** Equation 3 states: L₂NiR₂ + R'X'' → L₂Ni(R')(X'') + R–R. For the mechanistic proposal to be self-consistent, R–R must either appear in the product mixture (establishing stoichiometric byproduct formation at the predicted level), be absent at quantified detection limits (establishing genuine selectivity at the mechanism level), or the mechanism must be revised to remove R–R from eq 3. None of these three resolutions is present in the paper.

**EP:** EP-03a (Direct-observation / state-assignment pack)

**Case-specific implementation:**
- EP-03a: For the n-BuMgBr + PhCl Table I entry, analyze the crude reaction mixture by glpc for n-butane, n-octane (n-Bu–n-Bu), and biphenyl (Ph–Ph) alongside the Ph-n-Bu cross-coupling product. Report the glpc detection limits for each potential homo-coupling byproduct. The complete absence of n-Bu–n-Bu is the expected result if eq 3 does not represent the actual pathway; its presence in amounts predicted by the mechanism would confirm the mechanistic proposal but challenge the selectivity claim.

**Notes:** Severity classified as high in Stage 1. The self-contradictory absence touches two independent aspects: (i) the mechanistic proposal's internal consistency (SRG-1 / CLA-1 overlap), and (ii) the unquantified selectivity claim (SRG-2 overlap). The CLA is recorded independently because its RI pattern (RI-03, observable predicted by paper's own model but unreported) is distinct from the RI-09 and RI-04 of SRG-2.

---

**CLA-2: Ligand structure–activity ranking used to derive a mechanistic conclusion without the numerical yield data on which the ranking must rest**

*Grounded in: B-3, A-2. B-3's supporting items not captured in any SRG.*

**Primary RI:** RI-05 [Qualitative overread]
**Secondary RI:** RI-03 [Unobserved explanatory]

**ER:** The claim [REDACTED: substantial verbatim quotation; see Tier 9] is derived solely from the qualitative activity ranking (footnote 21: n-BuMgBr + PhCl, six catalysts ranked by undefined criteria). The numerical yield values for each of the six catalysts in this benchmark reaction are not reported; the magnitude of ">" vs. "≫" is not disclosed. A mechanistic conclusion about intermediate geometry derived from a ranking of unstated magnitude constitutes qualitative overread (RI-05).

**EP:** EP-05a (Quantitative-ranking substantiation pack)

**Case-specific implementation:**
- EP-05a: Report isolated or glpc yield for each of the six catalyst entries ([NiCl₂(dpp)], [NiCl₂(dpe)], [NiCl₂(dmpe)], [NiCl₂(PPh₃)₂], [NiCl₂(PEt₃)₂], [NiCl₂(PPh₂Me)₂]) in the n-BuMgBr + PhCl benchmark reaction (footnote 21 conditions). Correlate the yield with a tabulated bite angle or P–Ni–P chelate angle to establish the quantitative basis for the cis-geometry inference.

**Notes:** B-3 in high_convergence_low_gap (V1=medium, V2=medium; convergence=2/3, gap=none). The structural logic of the paper's mechanistic section — ligand activity order → cis geometry requirement → proposed intermediate 3 → catalytic cycle — makes CLA-2 the one place in the paper where an experimental observation is used to ground a mechanistic claim, yet the observation is presented in qualitative form only. RI-05 Codebook application note: qualitative overread applies here not as a secondary inference problem but as the primary structural issue, since the ranking is the paper's only within-paper experimental evidence for the proposed intermediate geometry.

---

**CLA-3: "Useful preparative method" claim unsupported by TON or catalyst recyclability data**

*Grounded in: B-1, A-3. These items not included in any SRG as primary members.*

**Primary RI:** RI-08 [Unquantified reliability]

**ER:** The label "useful preparative method" implies that the catalyst is both genuinely catalytic (multiple turnovers without deactivation) and synthetically practical (reproducible yield at stated scale). Neither turnover number, turnover frequency, catalyst loading optimization data, nor any replicate experiment at the stated scale is provided. The disclaimer "The experimental conditions are not necessarily optimum" simultaneously acknowledges the preliminary status and labels the method "useful" in the same paper.

**EP:** EP-08a (Replication / uncertainty pack)

**Case-specific implementation:**
- EP-08a: Report a TON determination for [NiCl₂(dpe)] in the n-BuMgBr + PhCl or m-BuMgBr + m-DCB reaction (Example 1) by varying catalyst loading from 10⁻¹ to 10⁻⁴ mol fraction and recording yield vs. mol% [NiCl₂(dpe)]. A single TON curve would establish whether the system is genuinely catalytic (TON >> 1) or slowly consumed (TON ≈ 1–10).

**Notes:** B-1 in high_convergence_low_gap (V1=medium, V3=low; convergence=2/3, gap=low). The connection to U-2 is operative: if the black precipitate in Example 1 represents Ni⁰ decomposition, the TON may be severely limited by catalyst deactivation mid-reaction, making the "preparative" label doubly provisional.

---

### §3 Current VQ assessment

**Current judgment: VQ-2 (Method) — qualified**

---

**VQ-1 [Observation]: PASS (non-fatal)**

Product identity across all ten Table I entries is established at a minimum level — each product is characterized by at least one of glpc, nmr, ir, or mass spectra (footnote c). The "and/or[REDACTED: substantial verbatim quotation; see Tier 9]and/or[REDACTED: substantial verbatim quotation; see Tier 9]and/or" characterization is non-fatal for a 1972 JACS communication.

---

**VQ-2 [Method]: PASS (qualified)**

VQ-2 holds on the premise that RI-02 is non-fatal (see VQ-1).

**Unresolved at VQ-2:** RI-01 (SRG-5: two yield-reporting bases without calibration disclosure; B-2, B-7, B-9 collectively make cross-entry comparison unreliable), RI-07 (SRG-3: sp² scope restriction asserted without any negative-result data for sp³ or allyl halides; B-4, three-agent convergence).

Both RI-01 and RI-07 remain unresolved. RI-07 is non-fatal in the sense that the sp² restriction is mechanistically plausible (oxidative addition at sp³ C–Cl is disfavored); however, without at least one failed substrate, the restriction is boundary-level asserted rather than demonstrated. RI-01 is non-fatal at the observation level but means that the "yields are generally very high" claim across Table I cannot be evaluated quantitatively.

Qualified designation rationale: RI-01 and RI-07 are unresolved but do not individually overturn the core yield claim; together they sufficiently weaken the methodological evidentiary basis that VQ-2 is "qualified" rather than a clean pass. The qualification is recorded per the VQ decision matrix note on RI-05 analogy: when RI-01 remains in a form that prevents cross-entry comparison, VQ-2 cannot be awarded as a clean pass.

---

**VQ-3 [Mechanism]: FAIL**

Inherited premise: VQ-2 qualified.

**Unresolved at VQ-3:** RI-03 (SRG-1, CLA-1: the proposed catalytic cycle intermediates 1–3 are unobserved under actual [NiCl₂(dpe)] conditions; the black precipitate is uncharacterized), RI-04 (SRG-2, SRG-4: the selectivity claim rests on a single-determination yield series without cross:homo ratios; the cis:trans ratio determination method is undisclosed), RI-06 (SRG-1: entire Ni(II) catalytic cycle imported by analogy from stoichiometric (dipy)Ni chemistry without demonstration of isomorphism).

RI-03 is Fatal at VQ-3: the paper's proposed mechanism requires that a homogeneous Ni(II) complex is the active catalyst, but the uncharacterized black precipitate raises a formally unaddressed alternative (Ni⁰ heterogeneous catalysis). If Ni⁰ is the active species, the proposed Ni(II)/Ni(II) cycle (eqs 2–4) does not apply, and the structural inference about intermediate 3 geometry (feature 3) collapses.

RI-06 is Fatal at VQ-3: the entire mechanistic model is a cycle-level import from a different system (stoichiometric (dipy)Ni vs. catalytic [NiCl₂(dpe)]), and isomorphism is not demonstrated.

**However, Layer 3 (practical utility) on its own: VQ-2 (qualified).** The yield and scope data in Table I represent a methodological advance (sp² halides, high yields, β-hydrogen-bearing alkyl Grignard reagents) that does not depend on the mechanistic proposal. If the three-step cycle (Layer 2) were entirely withdrawn, Table I would still support the synthetic utility claim at VQ-2 (qualified, due to RI-01 unresolved). This per-layer asymmetry means the synthetic contribution of the paper is more robust than the mechanistic contribution.

---

**VQ-4 [Benchmark]: FAIL**

Inherited premise: VQ-3 fails.

**Unresolved at VQ-4 (in addition to VQ-3 failures):** RI-08 (SRG-5, CLA-3: no replication data for any Table I entry; no TON determination; "useful preparative method" not substantiated by catalyst efficiency data), RI-09 (SRG-6: superiority over all prior systems — Tamura-Kochi, cuprate, Ni(acac)₂ — asserted without any shared-substrate numerical comparison).

RI-09 is the VQ-4-specific failure: the paper's competitive claim structure is entirely qualitative. No direct comparative experiment appears anywhere in the paper.

---

### §4 Era-Norm Annotation

**Communication-era tolerated (1972 JACS communication, 3 pages):**

- **B-1** (no TON or catalyst loading optimization data): JACS communications in 1972 routinely reported catalytic results as yield tables without TON; catalyst efficiency quantification was not yet a standard reporting requirement in synthetic organometallic communications.
- **B-2** (two yield-reporting bases without internal standard identity): mixed yield reporting bases (glpc vs. isolation) were acceptable in 1972 communications because glpc was still an emerging quantitative technique and reporting conventions had not yet been standardized.
- **B-3** (ligand activity ranking without numerical values): qualitative ligand activity rankings without tabulated yield values were standard presentation in communications of this era; quantitative SAR tables were a full-paper norm.
- **B-5** (solvent superiority asserted without data): the "definitely superior" designation for diethyl ether without supporting data was accepted in 1972 communications as a directional finding without requiring the quantitative comparison required in full papers.
- **B-6** (no cross:homo product ratio in Table I): reporting only cross-coupling product yield without homo-coupling byproduct quantification was common in synthetic communications of this era; the absence of byproduct quantification was not yet treated as a standard reporting requirement.
- **B-7** ("and/or" characterization): the "and/or" formulation for product characterization was standard in 1972 JACS communications; multi-technique characterization requirements (including HRMS or elemental analysis for all products) became more stringent in later decades.
- **B-9** (no replication data for any entry): single-determination yield tables were accepted for priority-establishing communications in 1972; replicate measurements were expected in full papers.
- **A-2** (mechanistic deferral: no intermediate characterization, no kinetic data): explicitly labeling the mechanistic proposal as "a working hypothesis" while deferring experimental verification to future work was a recognized communication-format convention for establishing priority on a synthetic method.

**Modern-era deficient:**

- **B-2** (mixed yield-reporting bases without calibration disclosure) [dual]: modern submission standards require explicit statement of which method is used per entry, identification of the internal standard, and calibration protocol or response factors for glpc-based yields. A mixed-method Table I column without these disclosures would not pass peer review at JACS in 2026. *Also in communication-era tolerated — dual classification.*
- **B-6** (no cross:homo product ratio) [dual]: the paper's central claim is "selective cross-coupling." Modern peer review would require at minimum one cross:homo determination in the crude mixture to give quantitative content to the selectivity claim, regardless of format. The absence is now methodologically fatal to the novelty pillar. *Also in communication-era tolerated — dual classification.*
- **RI-07 / B-4** (sp² scope restriction without negative-result evidence): modern standards require at least one reported failed substrate to substantiate a scope exclusion ("only C_{sp²} halides can be used"). A boundary claim without negative-result evidence would trigger revision requests at most contemporary journals.
- **U-2 / B-12** (uncharacterized black precipitate): modern submissions require characterization of any unexpected physical observation in the reaction mixture that bears on the proposed catalytic species. The black precipitate in Example 1 would require at minimum ICP-MS or elemental analysis to exclude Ni⁰ nanoparticle formation.
- **U-1** (self-contradictory absence of R–R homo-coupling byproduct): modern reviewers would flag the internal inconsistency between eq 3 (predicting R–R) and Table I (reporting no R–R) as requiring resolution — either by detecting R–R at predicted levels or by revising the mechanism.
- **B-3 / CLA-2** (ligand ranking without numerical values, mechanistic conclusion): modern standards would require the numerical yield values for the six catalysts in footnote 21, at minimum in a Supporting Information table, before accepting a mechanistic conclusion ("cis configuration is the first requisite") derived from the ranking.
- **A-1 / B-11** (stereochemical outcome without analytical method or mechanistic hypothesis): the cis:trans stilbene ratios are the most mechanistically significant data in the paper; modern standards would require disclosure of the analytical method, an uncertainty estimate, and at minimum a preliminary mechanistic discussion, not merely a synthetic application footnote.

---

### §5 Shortest-reinforcement route

**Current VQ: VQ-2 (qualified)**

**First objective function: VQ-3 (Mechanism)**

The unresolved RIs blocking VQ-3 are: RI-03 (intermediates unobserved, black precipitate uncharacterized), RI-04 (selectivity claim single-determination, cis:trans ratio method undisclosed), RI-06 (entire cycle imported by analogy from stoichiometric (dipy)Ni system). VQ-3 also inherits the VQ-2 qualifications (RI-01 and RI-07 unresolved).

EP investment order for VQ-3 (information gain × feasibility):

```
Shortest route to VQ-3:

1. EP-03a (Direct-observation / state-assignment pack) — Characterize the
   black precipitate from Example 1 by ICP-MS and magnetometry to
   distinguish intact [NiCl₂(dpe)] from Ni⁰ nanoparticles; if intact
   Ni(II) is confirmed, the RI-03 (active species identity) component of
   SRG-1 is resolved and the homogeneous Ni(II) cycle becomes defensible.
   Advances RI-03 (SRG-1, CLA-1).

2. EP-06a (Analogy-validation pack) — Independently synthesize L₂NiR₂
   (intermediate 1, L = dpe, R = n-Bu) and confirm its reaction with PhCl
   to give Ph-n-Bu cross-coupling product + n-Bu–n-Bu, establishing that
   eq 3 applies under [NiCl₂(dpe)] conditions and directly addressing the
   cycle-level import.
   Advances RI-06 (SRG-1) and simultaneously resolves CLA-1 (R–R byproduct
   prediction: if n-Bu–n-Bu is detected at stoichiometric levels in the
   intermediate-1 + PhCl reaction, U-1 is explained; if n-Bu–n-Bu is
   absent, eq 3 must be revised).

3. EP-04a (Discrimination / replication pack) — For the n-BuMgBr + PhCl
   Table I entry, determine the cross:homo product ratio (Ph-n-Bu : n-Bu–
   n-Bu) by glpc in the crude reaction mixture, in triplicate; separately,
   repeat the cis-DCE and trans-DCE entries in triplicate with ¹H NMR
   confirmation of cis:trans stilbene ratios.
   Advances RI-04 (SRG-2 and SRG-4 simultaneously) — highest information
   gain per experiment because it resolves both the selectivity claim gap
   and the stereochemical measurement gap in a single experimental series.

4. EP-07a (Boundary-test pack) — Run [NiCl₂(dpe)]-catalyzed reactions of
   n-BuMgBr with n-BuCl (sp³) and allyl-Cl under Condition A; report yield
   or conversion data even if zero.
   Advances RI-07 (SRG-3) — resolves VQ-2 qualification on RI-07 and
   contributes to VQ-3 scope grounding.

5. EP-05a (Quantitative-ranking substantiation pack) — Report isolated
   yield for each of the six catalysts in the footnote-21 benchmark
   (n-BuMgBr + PhCl) to convert the qualitative ligand activity ranking
   into a semi-quantitative SAR.
   Advances RI-05 (CLA-2) — resolves the qualitative-overread component of
   the mechanistic inference about intermediate 3 geometry.
```

**Second objective function: VQ-4 (Benchmark)**

VQ-4 additionally requires resolving RI-08 and RI-09:

```
Shortest route to VQ-4 (after VQ-3 is satisfied):

6. EP-08a (Replication / uncertainty pack) — Determine TON for [NiCl₂(dpe)]
   in the n-BuMgBr + m-DCB system (Example 1) by varying catalyst loading
   from 10⁻¹ to 10⁻⁴ mol fraction; confirm that TON >> 10 to substantiate
   the "useful preparative method" designation.
   Advances RI-08 (CLA-3, SRG-5).

7. EP-09a (Internal benchmark pack) — Run n-BuMgBr + PhCl under Tamura-
   Kochi Fe-catalyst conditions in the same laboratory; report isolated yield
   and cross:homo ratio alongside the [NiCl₂(dpe)] result on the same
   substrate to provide a direct quantitative comparison.
   Advances RI-09 (SRG-6) — converts the qualitative superiority assertion
   into a demonstrated numerical comparison.
```

**Certification-gate note:** The experimental investment order above follows information gain and feasibility (EP-03a and EP-06a first because they address the fatal RI-03/RI-06 at VQ-3); however, the final certification follows the fixed gate order VQ-1 → VQ-2 → VQ-3 → VQ-4, meaning that RI-01 and RI-07 (VQ-2 qualifications) must be resolved before VQ-3 certification is awarded, regardless of whether EP-03a and EP-06a (VQ-3-targeted) are completed first.

---

### §6 Contribution to institutional design

**1. RI-06 scope note confirmed and extended (cycle-level import):**

This case provides a clean representative instance of the RI-06 scope note — [REDACTED: substantial verbatim quotation; see Tier 9] The Kumada 1972 paper imports the entire Ni(II)/Ni(II) three-step cycle from a single stoichiometric (dipy)Ni precedent (eq 1) to a catalytic [NiCl₂(dpe)] system — this is a textbook cycle-level import. No isomorphism test (same metal oxidation state trajectory, same ligand coordination behavior, same elementary step rates) is performed between the stoichiometric (dipy)Ni system and the catalytic [NiCl₂(dpe)] system. RI-06 is the primary RI for SRG-1. This case should be added to the RI-06 canonical examples in the Codebook.

**2. Labeling-mismatch pattern confirmed:**

The labeling-mismatch pattern is present and well-formed. The mechanistic section explicitly labels the three-step cycle "a working hypothesis" (final two paragraphs of the results section), yet equations 2–4 use factual chemical notation ("L₂NiX₂ + 2RMgX' → L₂NiR₂ + 2MgXX'"), and the subsequent five-features section uses factual-verb derivatives derived from the hypothetical cycle: [REDACTED: substantial verbatim quotation; see Tier 9] (feature 3). The hypothesis label is concentrated in the final two sentences of the mechanistic discussion, while the factual-verb usage of the hypothetical intermediates (particularly intermediate 3) appears in the five-features enumeration that follows. This is consistent with the labeling-mismatch pattern description in the prompt and co-occurs with RI-06 as expected.

**3. Automatic-resolution pattern confirmed for RI-07 and RI-01:**

The RI-07 (unsupported scope boundary: "Only C_{sp²} halides can be used," no negative-result evidence) and RI-01 (mixed yield-reporting bases) follow the automatic-resolution pattern via the communication→Full Paper transition. The Kumada group's subsequent full papers (Tamao et al., JACS 1976 and related; by inference from the A-3 deferral "Investigations are continuing") would be expected to (a) test sp³ halides and report the failures, and (b) provide calibrated glpc yield data for a larger substrate scope. This is exactly the pattern where page-limit constraints of the communication format generate RI-07 and RI-01 that are automatically resolved in the corresponding full paper. The correspondence with A-3 (scope-extension deferral) and the era-norm annotation (communication-era tolerated) is confirmed.

**4. RI co-occurrence pattern — RI-06 + RI-03 in SRG-1:**

SRG-1 exhibits the RI co-occurrence pattern: RI-06 (imported model) and RI-03 (unobserved explanatory) co-occur and are structurally coupled. Resolving only RI-03 (characterizing the black precipitate to confirm Ni(II) identity) is insufficient if RI-06 remains, because even confirmed Ni(II) identity does not demonstrate that the stoichiometric (dipy)Ni analogy is kinetically valid for the catalytic [NiCl₂(dpe)] system. Conversely, resolving only RI-06 (validating the analogy by synthesizing intermediate 1) does not characterize the actual species present during catalysis (RI-03). Both must be resolved sequentially: EP-03a (RI-03) → EP-06a (RI-06) in that order, because the result of EP-03a determines which version of intermediate characterization EP-06a needs to target. This co-occurrence structure — resolving only one is insufficient — should be added to the Codebook as a representative RI-06 + RI-03 co-occurrence case.

**5. Self-contradictory-absence CLA check — CLA-1 confirmed as a distinct pattern:**

CLA-1 (R–R homo-coupling byproduct predicted by eq 3, absent from all Table I entries without acknowledgment) is confirmed as a distinct self-contradictory-absence pattern. The structure: (a) the paper proposes a mechanistic cycle that *generates* an observable byproduct (R–R) at a specific mechanistic step (eq 3); (b) the paper's own product table *never reports* that byproduct; (c) the paper *never acknowledges* the absence. This is distinct from a simple reporting omission (B-6, which records the selectivity data gap from a reporting-standards perspective) because the internal inconsistency is generated *by the paper's own model*, not by an external reporting standard. CLA-1 represents the self-contradictory-absence detection check in its purest form. The Codebook should note this as: [REDACTED: substantial verbatim quotation; see Tier 9]

**6. PRI-11 (Mechanism–kinetics decoupling) — promotion candidate status not triggered:**

PRI-11 (provisional: mechanism supported only by agreement with observed rate orders, without an algebraic derivation of the rate law) is not triggered in this case because the Kumada 1972 paper provides *no kinetic data* at all — neither rate orders nor a rate law. The pattern in which PRI-11 applies ("mechanism supported only by agreement with observed rate orders") requires at least rate order data to be present; when no kinetic data exist at all, the applicable RI is RI-03 (unobserved explanatory) and RI-06 (imported model). PRI-11 is confirmed as inapplicable to the Kumada 1972 case. However, this negative case is itself useful: it marks the boundary condition for PRI-11 application as "kinetic data present but algebraic rate-law derivation absent" rather than "no kinetic data at all." This boundary should be noted in PRI-11's application notes in the Codebook.

**7. No new PRI candidate detected:**

The patterns in this paper are fully captured by existing RI-01, RI-03, RI-04, RI-05, RI-06, RI-07, RI-08, RI-09. No new structural pattern requiring a PRI candidate was detected. CLA-1's self-contradictory-absence structure is a variant of RI-03 (unobserved explanatory) rather than a new independent pattern.

---

> **Tier 8 redaction notice**: This file is a redacted copy of the corresponding Tier 3 / Tier 9 output. Verbatim source-paper quotations have been replaced by `[REDACTED: see source paper §<loc>; full text retained in Tier 9 reviewer-only deposit]` markers, preserving location references and our own analytical content. Bibliographic fields (title, authors, journal, year, DOI), analytical labels (`evidence_chain:` with B-/U-/A-/C- internal IDs), short technical terms, and our own analytical text are not redacted. The redaction was applied by `scripts/redact_for_tier8.py` and, for this version, by `scripts/build_paperA_R1_public.py` with `scripts/redact_source_ngram_runs.py` (scripts of the project repository; they are not deposited).
