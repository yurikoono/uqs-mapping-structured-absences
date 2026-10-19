```
prompt_version: stage3-v2-en-20260419
model_info: claude-sonnet-4-6
```

# Re-certification Assessment Sheet for Scientific Knowledge

## Tamao, Sumitani, and Kumada 1972 (Journal of the American Chemical Society, communication)

---

### §1 Claim Architecture

**Core claim summary:**

The paper reports that a class of nickel–bidentate diphosphine complexes — represented by [NiCl₂(dpe)] — catalyzes the selective cross-coupling of Grignard reagents with vinyl or aryl halides to give high isolated or glpc yields of the cross-coupling products. The Novelty pillar has two components: (i) catalytic (rather than stoichiometric) use of nickel in a cross-coupling reaction, and (ii) the practical differentiator — tolerance for Grignard reagents bearing β-hydrogen atoms without β-hydride elimination, enabling access to alkyl-substituted arenes that are "not readily accessible by conventional methods." The Utility pillar is synthetic: multi-gram-scale one-step preparation of otherwise-difficult targets (e.g., m-di-n-butylbenzene, α-vinylnaphthalene) in 76–98% yield with sp² halide electrophiles and especially with the economically advantaged chloride substrates.

A mechanistic "working hypothesis" — a three-step Ni(II)/Ni(II) catalytic cycle (eqs 2–4) — is offered as a provisional interpretive frame, explicitly not as an independently validated claim. Five distinctive features (β-H tolerance, sp² selectivity, bidentate diphosphine requirement, non-stereospecific coupling, ether solvent preference) are enumerated.

**Layered structure judgment:**

The claim architecture is genuinely layered and asymmetric. NC-1 (new catalytic method) is the outer container; NC-2 (β-H tolerance), NC-3 (cross/homo selectivity), NC-4 (chloride reactivity), and NC-5 (mechanistic working hypothesis) are progressively more specific layers. Independent layers exist: refuting the yield data for any single substrate would not collapse NC-4 (chloride reactivity) or NC-2 (β-H tolerance). Refuting NC-3 — demonstrating that homo-coupling products are present at a significant level — would collapse the practical utility claim (NC-1) and the comparison with prior methods. NC-5 is explicitly labeled provisional, making it structurally insulated from refutation within the paper. Critically, NC-3 and NC-5 are not mutually independent: if the actual active catalyst is heterogeneous Ni⁰ (as the black precipitate might indicate), both the mechanistic working hypothesis and the selectivity narrative require revision. The most fragile layer is NC-3 (selectivity without quantified cross:homo ratios), and the most robust individual layer is NC-4 (chloride reactivity has direct support in multiple Table I entries).

---

### §2 SRG / CLA → RI / ER / EP Crosswalk

**SRG-1 [Catalytic mechanism evidence gap]**
(members: A-2, U-1, U-2, B-12)

* **Primary RI**: RI-06 [Imported model] — The entire three-step catalytic cycle (eqs 2–4) is constructed by direct analogy with stoichiometric (dipy)Ni reactions (refs 11–12), without demonstrating isomorphism between the (dipy)Ni stoichiometric system and the [NiCl₂(dpe)] catalytic system under the actual reaction conditions.
* **Secondary RI**: RI-03 [Unobserved explanatory] — Intermediates 1, 2, and 3 of the proposed catalytic cycle are neither directly observed under [NiCl₂(dpe)] catalytic conditions nor kinetically constrained; specifically, the potential decomposition of the precatalyst to Ni⁰ (U-2, B-12) is observed but left uncharacterized, generating an alternative mechanistic hypothesis that is never excluded.
* **ER**: For the proposed Ni(II)/Ni(II) catalytic cycle to hold, the active species must be an intact L₂Ni complex throughout the reaction, and the elementary steps (oxidative addition of R'X, transmetalation with RMgX, reductive elimination) must be demonstrated under actual [NiCl₂(dpe)] catalytic conditions — not merely inferred by analogy with stoichiometric (dipy)Ni chemistry reported by Uchino et al. and Miller et al.
* **EP**: EP-03a [Direct-observation / state-assignment pack]; EP-06a [Analogy-validation pack]
* **Case-specific implementation**: (EP-03a) Independently synthesize the proposed [dpe-Ni(R)(X)] and [dpe-Ni(R)(R')] intermediates (compounds 2 and 3 in the catalytic cycle) and characterize them by ³¹P NMR, ¹H NMR, and X-ray crystallography; then verify that these isolated intermediates are catalytically competent for cross-coupling under the standard conditions (ether, 0°–reflux). (EP-06a) Demonstrate the mechanistic isomorphism between (dipy)Ni and [NiCl₂(dpe)] by running the stoichiometric reaction of eq 1 with [NiCl₂(dpe)] as the nickel source and confirming that the same intermediate structure and reactivity are obtained; characterize the black precipitate from Example 1 by powder XRD, elemental analysis, or TEM to determine whether it is Ni⁰ metal, NiI, or an intact Ni-phosphine species.
* **Notes**: Sub-items A-2 (highest priority — high_convergence_low_gap, V1=high, V2=high), U-1 (high_convergence_low_gap, V2=high, V3=high), U-2 (self-contradictory absence — black color consistent with Ni⁰, severity=medium), B-12 (reporting omission of black precipitate, severity=low). The RI-06/RI-03 co-occurrence is structurally important: resolving only RI-06 (showing the analogy is valid) would be insufficient if RI-03 is left open — the black precipitate evidence of Ni⁰ formation would still undermine the mechanistic claim. Both RIs must be addressed simultaneously to reach VQ-3 for the mechanism layer. This is an RI co-occurrence pattern (see §6).

---

**SRG-2 [Cross/homo-coupling selectivity quantification]**
(members: B-6, U-1, C-1)

* **Primary RI**: RI-04 [Unreplicated discriminator] — The cross-coupling selectivity claim — the paper's central competitive differentiator — rests entirely on the absence of homo-coupling products from the product descriptions, a single interpretation of negative evidence without any direct measurement (no cross:homo ratio, no homo-coupling product identified or quantified) and without a stated glpc detection limit for the relevant homo-coupling byproducts (e.g., Et-Et, n-Bu-n-Bu).
* **Secondary RI**: RI-09 [External superiority] — The superiority of the Ni-dpe system over prior methods (Tamura-Kochi Cu/Fe catalysts) is asserted by describing prior methods' failure modes, without a direct head-to-head comparison on any shared substrate.
* **ER**: For the selectivity claim to hold quantitatively, the paper must report cross:homo product ratios (or an analytically justified detection limit for homo-coupling products) for at least a representative set of Table I entries, and must compare the cross-coupling yield with an appropriate prior method on at least one shared substrate.
* **EP**: EP-04a [Discrimination / replication pack]; EP-09a [Internal benchmark pack]
* **Case-specific implementation**: (EP-04a) For the most favorable entries in Table I (e.g., EtMgBr/PhCl, n-BuMgBr/PhCl), explicitly report the glpc yield of the predicted homo-coupling product (Et-Et or n-Bu-n-Bu) alongside the cross-coupling product yield, establishing the selectivity as a ratio with an identified and quantified denominator; state the glpc detection limit for these byproducts. (EP-09a) Run at least one Table I substrate combination under both [NiCl₂(dpe)] and the Tamura-Kochi Fe catalyst conditions and report yields side by side; run the same substrate under Ni(acac)₂ conditions to address the Corriu-Masse concurrent claim.
* **Notes**: U-1 is shared between SRG-1 and SRG-2 because it has both a mechanistic dimension (the cycle predicts R–R) and a selectivity dimension (R–R is absent from product descriptions). C-1 (dropped quantitative benchmark — Tamura-Kochi) is in high_convergence (affects_claims: yes). The incomplete negative evidence pattern applies here: the absence of homo-coupling products is used as positive evidence for selectivity without mass-balance closure or detection-limit evaluation. This is a case-specific implementation of RI-04 (see §6).

---

**SRG-3 [Scope restriction without negative-result evidence]**
(members: B-4, A-3)

* **Primary RI**: RI-07 [Unsupported boundary] — The scope restriction to sp² carbon halides is asserted as a positive feature ([REDACTED: substantial verbatim quotation; see Tier 9]) without any reported failed reaction with sp³ alkyl, allyl, or benzyl halides that would demonstrate the boundary experimentally.
* **Secondary RI**: RI-06 [Imported model] — Footnote 19 invokes literature on oxidative additions to "low valent nickel complexes" (Ugo; Fahey; Gerlach et al.) to rationalize the sp² selectivity, but the paper's proposed catalytic cycle uses Ni(II) intermediates (not Ni⁰), so the mechanistic basis for sp³ exclusion is not established within the paper's own framework.
* **ER**: For the scope boundary to be definitively established, at least one sp³ halide (e.g., n-BuCl, n-BuBr, or cyclohexyl chloride) must be reported as a substrate that gave exclusively homo-coupling, no reaction, or unacceptably low cross-coupling yield under the standard [NiCl₂(dpe)] conditions.
* **EP**: EP-07a [Boundary-test pack]
* **Case-specific implementation**: Report the outcome (yield, product identity) when n-butyl chloride or cyclohexyl bromide is used as the electrophile in place of PhCl under Condition A; include glpc traces showing the product distribution (cross-coupling product, homo-coupling product, recovered starting material) to establish the boundary empirically rather than by assertion.
* **Notes**: B-4 is the sole convergence=3/3 item in the entire paper (V1=medium, V2=medium, V3=medium), making this the strongest cross-field signal. A-3 is linked (high_convergence_low_gap, convergence=2/3). The RI-07 extended use applies here: the boundary claim "only sp² halides can be used" is a scope assertion made without failure examples, which qualifies as a negative boundary claim under the RI-07 definition.

---

**SRG-4 [Stereochemical outcome and its mechanistic basis]**
(members: A-1, B-11)

* **Primary RI**: RI-05 [Qualitative overread] — The paper reports anomalous cis-enrichment (cis:trans = 80:20 from cis-DCE; cis:trans = 43:57 from trans-DCE) and draws structural implications ("feature 4" — non-stereospecific coupling), but the analytical method used to determine these ratios is not stated (¹H NMR integration? glpc? other?), and the paper's own catalytic cycle (eqs 2–4) provides no mechanistic basis for predicting the direction or magnitude of the stereochemical outcome.
* **Secondary RI**: RI-03 [Unobserved explanatory] — The step at which geometric information is lost or inverted (oxidative addition of cis- vs. trans-DCE? transmetalation? reductive elimination?) is not identified; an intermediate with defined geometry (e.g., a cis- or trans-[dpe-Ni(Ph)(vinyl)] complex) that could carry or invert stereochemical information is neither observed nor proposed with a rationale.
* **ER**: For the stereochemical observation to be mechanistically interpretable, the analytical method and its precision for the cis:trans ratio determination must be stated, the ratios must carry defined analytical uncertainty (±N%), and at minimum a proposal — grounded in the paper's own catalytic cycle — must be offered for which step controls the geometric outcome.
* **EP**: EP-05a [Quantitative-ranking substantiation pack]; EP-03a [Direct-observation / state-assignment pack]
* **Case-specific implementation**: (EP-05a) Re-determine the cis:trans ratios by ¹H NMR integration with stated precision (e.g., cis:trans = 80±3:20±3 from cis-DCE) and verify independently by glpc with stated calibration. (EP-03a) Run the stoichiometric version of the coupling step (eq 4, from isolated intermediate 3) with cis- vs. trans-[dpe-Ni(Ph)(vinyl)] intermediates to determine whether the cis-enrichment originates at the reductive elimination step or is inherited from the transmetalation step.
* **Notes**: A-1 is in high_convergence_low_gap (V1=medium, V2=medium, convergence=2/3). B-11 is directly linked to A-1 (the ratios whose mechanistic implications are deferred are also the ratios whose analytical basis is not reported). This SRG has a lower VQ impact than SRG-1 and SRG-2 — it is relevant to VQ-3 qualification but does not independently block VQ-3 unless RI-05 remains in a serious form.

---

**SRG-5 [Yield data analytical quality]**
(members: B-2, B-7, B-9, B-11)

* **Primary RI**: RI-08 [Unquantified reliability] — The paper reports yields from 76% to 98% across ten substrate combinations without replicate measurements, without stated uncertainty bounds, and with a mixed yield-reporting basis (isolated yield vs. glpc yield with undisclosed internal standard and calibration) that makes cross-entry comparison unreliable.
* **Secondary RI**: RI-01 [Reporting integrity] — The use of two distinct measurement bases (isolated yield and glpc yield with an internal standard) across the same Table I column, without systematic disclosure of which products were characterized by which methods and why isolation was not performed for five entries, renders cross-comparison between entries impossible.
* **ER**: For the yield data to be analytically reliable, at minimum the internal standard identity and glpc response factors must be disclosed, the characterization method(s) applied to each product must be stated explicitly (not via an "and/or" footnote), and at least one representative entry must be reported in duplicate or triplicate with a stated standard deviation.
* **EP**: EP-01a [Reporting-coherence pack]; EP-08a [Replication / uncertainty pack]
* **Case-specific implementation**: (EP-01a) Revise Table I footnotes to specify, for each entry: which yield basis was used (isolation or glpc), the identity of the internal standard used for glpc quantification, and the response factor correction applied; disclose which characterization methods were used for each product. (EP-08a) Report at least one Table I entry (e.g., n-BuMgBr/PhCl, 76%) with ≥2 independent replicate determinations and state the standard deviation or range.
* **Notes**: B-2 and B-9 are both in high_convergence_low_gap. B-7 and B-11 are single-agent items but are structurally linked through the same shared root (SRG-5). This SRG is a non-fatal deficiency cluster — the data omissions do not overturn the core claim but prevent quantitative evaluation of yield differences between entries. Era-norm considerations apply (see §4).

---

**SRG-6 [Prior work numerical comparison gap]**
(members: C-1, C-2, A-4)

* **Primary RI**: RI-09 [External superiority] — The paper's claim of superiority over prior methods (Tamura-Kochi; π-allylnickel; cuprates) and its implicit indifference to the concurrent Corriu-Masse Ni(acac)₂ system are all asserted on the basis of external literature descriptions, without any direct head-to-head comparison on a shared substrate.
* **ER**: For the positioning claim to be externally validated, at least one shared substrate must be run under both the Ni-dpe conditions and the best-performing prior method (likely Tamura-Kochi Fe for alkenyl halides, or Ni(acac)₂ for the Corriu-Masse comparison) with yields reported side by side.
* **EP**: EP-09a [Internal benchmark pack]
* **Case-specific implementation**: Include at least one Table I entry where the identical substrate combination (e.g., n-BuMgBr + vinyl chloride, which is covered in Table I as n-C₅H₁₁MgCl/CH₂=CHCl giving 95% glpc yield) is run under both Ni-dpe conditions and Tamura-Kochi Fe conditions, reporting both yields under the same analytical basis; separately, run PhMgBr/vinyl chloride under Ni(acac)₂ conditions (replicating the Corriu-Masse approach) to establish whether the bidentate diphosphine ligand is required for high selectivity or whether the Ni center alone suffices.
* **Notes**: C-1 (affects_claims: yes), A-4 (forgotten deferral — Corriu-Masse Note Added in Proof), C-2 (symmetric citation — allylnickel/cuprate cited and dismissed). This SRG primarily impairs the relative novelty claims; it does not affect the absolute performance claims within the paper's own Table I.

---

**Outside the SRGs: CLAs**

**CLA-1 [Self-contradictory absence of homo-coupling byproduct — mechanistic model vs. reported data]**

* **Primary RI**: RI-04 [Unreplicated discriminator]
* **ER**: Equation 3 of the proposed catalytic cycle predicts that every turnover's initiation step produces R–R as a stoichiometric byproduct; the paper must either report the quantity of R–R formed or provide a mechanism-based argument for why R–R is produced at sub-detection levels (e.g., the initiation step occurs only once per catalyst molecule, making the R–R yield equal to the catalyst loading × substrate ratio, i.e., 1–10 mmol% relative to substrate).
* **EP**: EP-04a [Discrimination / replication pack]
* **Case-specific implementation**: For the EtMgBr/PhCl reaction at the standard [NiCl₂(dpe)] loading of 10⁻²–10⁻³ mol/mol, calculate the expected maximum R–R (Et-Et) yield from eq 3 and confirm by glpc whether it is detectable; if it is present at <1% and below the detection threshold, state this explicitly with the detection limit value.
* **Notes**: This CLA is recorded independently from SRG-1 (which addresses the broader mechanistic evidence gap) and SRG-2 (which addresses the selectivity quantification gap). The self-contradictory nature — the paper's own equation 3 predicts a byproduct that is not reported — makes this the highest-severity single item in the paper (U-1 at severity=high). The self-contradictory-absence CLA check is triggered: the catalytic cycle predicts R–R homocoupling formation, but R–R yield is not reported. Not included in existing SRGs as a standalone CLA because SRG-1 focuses on the mechanistic cycle's analogy basis and SRG-2 focuses on comparative selectivity; this CLA specifically addresses the internal logical contradiction between the proposed mechanism and the product data.

---

**CLA-2 [Catalyst identity — homogeneous vs. heterogeneous active species]**

* **Primary RI**: RI-03 [Unobserved explanatory]
* **ER**: The paper's proposed Ni(II)/Ni(II) catalytic cycle requires the active catalyst to be an intact [NiCl₂(dpe)]-derived homogeneous complex throughout the reaction; the black precipitate observed in Example 1 ([REDACTED: substantial verbatim quotation; see Tier 9]) is neither characterized nor acknowledged as inconsistent or consistent with the homogeneous mechanism.
* **EP**: EP-03a [Direct-observation / state-assignment pack]
* **Case-specific implementation**: Characterize the black material from Example 1 by at minimum a qualitative test (does it dissolve on workup? is it magnetically susceptible? does it reform a phosphine-nickel complex on re-exposure to dpe ligand?) and ideally by elemental analysis or powder XRD; a control experiment heating [NiCl₂(dpe)] under the standard conditions without substrate would establish the catalyst's thermal stability.
* **Notes**: This CLA is partially addressed in SRG-1 (RI-03 secondary) but is raised here as a standalone CLA because the black precipitate issue could affect the interpretation of all Table I data — not only the mechanism section — if the active catalyst is Ni⁰. Originating item: U-2 (severity=medium), B-12 (severity=low). The Available-but-unutilized characterization RI-03 subtype applies: the black mixture was observed (color and salt formation recorded) but the observational data were not used to evaluate the mechanistic claim.

---

### §3 Current VQ assessment

**Current judgment: VQ-2 (Method) — fails at VQ-3 threshold**

---

**VQ-1 [Observation] — Pass (non-fatal)**

RI-02 (Object identification) is non-fatal. Product structures are assigned by glpc, NMR, IR, and/or mass spectra; physical constants (bp, refractive index) are compared with literature values for the two showcase products. The "and/or[REDACTED: substantial verbatim quotation; see Tier 9]pure m-di-n-butylbenzene") without GC% or elemental analysis (B-8) is a non-fatal deficiency at the communication format level — the physical constant agreement with literature is sufficient for VQ-1 in a 1972 communication. VQ-1 holds, with the non-fatal qualifier that product purity is asserted rather than analytically quantified.

---

**VQ-2 [Method] — Pass (qualified, on the premise that VQ-1 holds)**

On the premise that RI-02 is non-fatal, VQ-2 is assessed. RI-01 (Reporting integrity — SRG-5): the mixed yield-reporting basis (isolated vs. glpc with undisclosed calibration) constitutes a non-fatal RI-01 for this paper's era and format. The yields are internally self-consistent (the two detailed examples with isolated yields are corroborated by glpc checks where stated), and the range of reported yields (76–98%) is broad enough that the mixed basis does not obscure the overall performance pattern. RI-07 (Unsupported boundary — SRG-3): the sp² electrophile restriction is asserted without negative-result evidence (B-4). However, the footnote 19 citation to literature on sp²-C–Cl bond reactivity in oxidative additions to low-valent Ni complexes provides a basis for the boundary, even if the mechanistic basis within the paper's own Ni(II) cycle is not fully established. The RI-07 deficiency is therefore non-fatal at VQ-2. VQ-2 holds (qualified), on the premise that RI-02 is non-fatal, with the non-fatal qualifiers that RI-01 and RI-07 remain incompletely resolved.

---

**VQ-3 [Mechanism] — Fail**

Unresolved RIs blocking VQ-3: **RI-06** (primary, SRG-1) and **RI-03** (secondary, SRG-1 and CLA-2).

The proposed three-step Ni(II)/Ni(II) catalytic cycle (eqs 2–4) is imported wholesale from stoichiometric (dipy)Ni chemistry without demonstrating isomorphism with the [NiCl₂(dpe)] catalytic system (RI-06). Intermediates 1, 2, and 3 are not directly characterized under catalytic conditions (RI-03). Critically, the black precipitate observed in Example 1 (B-12, U-2) is consistent with Ni⁰ formation — a heterogeneous catalyst for which the proposed ionic cycle would not apply — and is neither characterized nor excluded (RI-03, CLA-2). The paper's own labeling of the cycle as a "working hypothesis[REDACTED: substantial verbatim quotation; see Tier 9]only C_sp² halides can be used," "a bidentate diphosphine exhibits remarkable catalytic activity") that goes beyond the hypothesis label. Additionally, the selectivity claim (NC-3) rests on the absence of reported homo-coupling products, which are predicted by eq 3 as stoichiometric byproducts of the initiation step — the self-contradictory absence constitutes an unresolved RI-04 (CLA-1) that interacts with the mechanistic claim. RI-05 (SRG-4) remains in a potentially qualified form: the cis-enrichment observation has no mechanistic explanation within the proposed cycle. VQ-3 fails.

**Layered VQ asymmetry:** The synthetic utility claims (NC-1, NC-2, NC-4) on their own reach a level closer to VQ-2 solidly: the yield data are sufficient for the method to be reproducible in practice (as demonstrated by subsequent adoption of the reaction in the literature). However, the mechanism layer (NC-5) and the selectivity claim (NC-3) do not reach VQ-3. The sp² selectivity assertion (SRG-3, RI-07) remains undemonstrated for the sp³ case specifically.

---

**VQ-4 [Benchmark] — Fail (inherits VQ-3 failure)**

RI-08 (Unquantified reliability — SRG-5): no replicate yield data or standard deviations are provided for any Table I entry. RI-09 (External superiority — SRG-2 secondary, SRG-6): the superiority over Tamura-Kochi and equivalence/superiority over concurrent Ni(acac)₂ are asserted without a head-to-head comparison on any shared substrate. VQ-4 fails, both on its own requirements and by inheritance from VQ-3.

---

### §4 Era-Norm Annotation

**communication-era tolerated:**

- **B-1 (no catalyst loading optimization or TON):** In 1972 JACS Communications, catalytic efficiency reporting did not yet require turnover number data; the demonstration that a sub-stoichiometric amount of [NiCl₂(dpe)] (10⁻²–10⁻³ mol/mol) gave high yields was sufficient. The communication format explicitly allowed the qualifier "experimental conditions are not necessarily optimum" as a placeholder for future optimization.

- **B-2 (mixed yield-reporting basis — isolated vs. glpc):** Dual yield-reporting in the same table was standard practice in 1972 synthetic communications; the distinction between isolation-based and glpc-based yields was understood to reflect practical considerations (volatile products isolated by glpc; stable products isolated directly), and the absence of unified calibration disclosure was convention-consistent.

- **B-3 (ligand activity order without yield values):** The practice of stating a qualitative rank order for catalyst performance without publishing the underlying numerical data was common in short synthetic communications in this period, especially when the order was stated as a footnoted observation rather than a primary result.

- **B-7 (characterization by "and/or" formulation):** In 1972, a communication in JACS did not require full analytical characterization for every product; glpc retention time comparison with an authentic sample, combined with one or two spectroscopic measurements, was commonly accepted. Elemental analysis was required only for full articles in this journal.

- **B-9 (no replicate yield data or standard deviations):** Single-determination yield reporting was the norm in 1972 synthetic communications; replicate measurements and statistical reporting of variance became standard requirements for full articles and later extended to communications after the 1990s.

- **B-5 (solvent superiority claim without comparative data):** Qualitative solvent preference statements ("definitely superior") were accepted in 1972 communications as practical guidance from expert practitioners, without the requirement to provide a tabulated comparison.

- **B-12 (black precipitate recorded without characterization):** In-procedure observations of color changes and precipitate formation were routinely recorded as procedural details in 1972; formal catalyst characterization under operating conditions was not yet a standard expectation for communications.

- **A-2 (full mechanistic evidence deferred to future work):** In 1972, a communication presenting a new synthetic method was not expected to provide complete mechanistic validation; the "working hypothesis" framing was accepted as an appropriate interim mechanistic proposal in the communication format.

---

**modern-era deficient:**

- **B-2 (mixed yield-reporting basis — isolated vs. glpc):** By contemporary standards, all yields in a single table column must be reported on a consistent basis with disclosed calibration, or clearly flagged with footnote-level disclosure of the internal standard identity, response factors, and calibration range. The absence of these disclosures renders cross-entry comparison unreliable.

- **B-6 / U-1 (selectivity claimed without cross:homo ratio):** Modern synthetic catalysis papers are expected to report selectivity as a quantitative ratio (cross:homo) with a stated analytical method and detection limit for the minor product, rather than by asserting selectivity through the absence of reported byproducts. The IUCr/ACS guidelines now require mass balance closure or explicit acknowledgment of unreported byproducts.

- **B-4 (scope boundary without negative-result evidence):** Contemporary scope characterization requires at least one failed substrate to be reported and analyzed, in order to distinguish a mechanistically principled scope restriction from an empirically convenient one.

- **B-9 (no replicate yield data):** Replicate measurements with stated precision (e.g., 94 ± 2%, n=3) are now required for any yield reported as a primary result in a synthetic paper; single-determination values are acceptable only as preliminary screening data.

- **U-2 / B-12 (black precipitate uncharacterized):** Contemporary organometallic catalysis requires that any in-situ observation consistent with catalyst decomposition (color change, precipitate, loss of homogeneity) be addressed either by characterization of the observation or by a control experiment demonstrating that catalyst integrity is maintained under the reaction conditions. Failing to characterize the black precipitate while proposing a homogeneous mechanism would not pass peer review by modern standards.

- **A-2 (mechanistic cycle as working hypothesis without kinetic or intermediate-level support):** A three-step catalytic cycle proposed without at least one piece of direct experimental evidence (observed intermediate, rate-law consistency, kinetic isotope effect, or crossover experiment) would not satisfy the minimum mechanistic evidence threshold required by modern JACS for a new catalytic method paper.

**Dual classification (communication-era tolerated AND modern-era deficient):**

- B-2 (yield basis mixing): tolerated in 1972 by communication convention; deficient now because contemporary data reporting standards require explicit calibration disclosure and basis consistency.
- B-4 (scope boundary assertion): tolerated in 1972 as a positive-framing practice; deficient now because contemporary scope-characterization norms require negative-result reporting to establish exclusions empirically.
- A-2 (mechanistic deferral): tolerated in 1972 as the norm for communication-format synthetic papers; deficient now because a new catalytic method paper in 2026 is expected to provide at minimum one intermediate characterization or one kinetic measurement supporting the proposed cycle.

---

### §5 Shortest-reinforcement route

**Objective function 1: Advance from VQ-2 to VQ-3**

The blocking RIs at VQ-3 are RI-06 (imported model — analogy not validated) and RI-03 (active species not observed or constrained). These two RIs must be resolved simultaneously, because confirming the analogy (RI-06) would still leave RI-03 open if the active catalyst is heterogeneous. The CLA-1 RI-04 deficiency (self-contradictory absence of R–R) also interacts with VQ-3 certification for the selectivity sub-claim.

```
Shortest route to VQ-3:

1. EP-03a [Direct-observation / state-assignment pack] — Independently synthesize
   [dpe-Ni(n-Bu)(Cl)] (compound 2) and [dpe-Ni(Ph)(n-Bu)] (compound 3) and confirm
   that isolated compound 3 undergoes reductive elimination to give the cross-coupling
   product (Ph-n-Bu) under the standard conditions, establishing that the proposed
   intermediates are catalytically competent.
   Advances RI-03 (primary), RI-06 (secondary — confirms the analogy is
   mechanistically operative for the dpe system, not only for dipy).

2. EP-06a [Analogy-validation pack] — Characterize the black precipitate from
   Example 1 (powder XRD, elemental analysis, or quantitative dissolution test) to
   determine whether it is Ni⁰ metal or an intact nickel-phosphine species; run a
   control experiment heating [NiCl₂(dpe)] under standard conditions without substrate
   to isolate the precatalyst decomposition pathway.
   Advances RI-06 (confirms the homogeneous cycle is operative, not a Ni⁰ surface
   pathway), RI-03 (characterizes the unobserved species).

3. EP-04a [Discrimination / replication pack] — For the EtMgBr/PhCl entry, report
   the glpc yield of Et-Et (homo-coupling product) with a stated detection limit;
   calculate the expected maximum Et-Et yield from eq 3 based on catalyst loading and
   verify whether the observed Et-Et level is consistent with the proposed initiation
   mechanism.
   Advances RI-04 (CLA-1 — resolves the self-contradictory absence of R–R byproduct).

4. EP-05a [Quantitative-ranking substantiation pack] — Re-determine the cis:trans
   stilbene ratio from cis- and trans-DCE by ¹H NMR with stated analytical precision
   (±N%) to establish whether the anomalous cis-enrichment is analytically robust.
   Advances RI-05 (SRG-4 — elevates qualitative stereochemical observation to
   quantitatively evaluable data; resolves the qualified VQ-3 component if RI-05
   can be shown non-fatal).

Certification-gate note: The experimental investment order (EP-03a → EP-06a →
EP-04a → EP-05a) follows information gain — EP-03a and EP-06a together resolve
the two primary blocking RIs simultaneously. However, the final VQ-3 certification
follows the gate order VQ-1 → VQ-2 → VQ-3, and VQ-3 cannot be granted until both
RI-03 and RI-06 are resolved, regardless of the order in which the experiments are
performed.
```

**Objective function 2: Advance from VQ-3 to VQ-4 (prerequisite: VQ-3 achieved)**

```
Shortest route to VQ-4:

1. EP-08a [Replication / uncertainty pack] — Report at least two representative
   Table I entries (e.g., n-BuMgBr/PhCl and PhMgBr/vinyl chloride) in triplicate with
   stated standard deviations, under a unified yield-reporting basis (isolated yield
   with disclosed calibration or glpc yield with disclosed internal standard and
   response factors).
   Advances RI-08 (primary RI for VQ-4 in SRG-5).

2. EP-09a [Internal benchmark pack] — Run n-C₅H₁₁MgCl/vinyl chloride (95% glpc
   yield under Ni-dpe conditions, Table I) under Tamura-Kochi Fe catalyst conditions
   and under Ni(acac)₂ conditions, reporting yields under the same analytical basis,
   to establish the comparative performance advantage directly.
   Advances RI-09 (primary in SRG-6) and addresses C-1 (dropped quantitative
   benchmark).

Certification-gate note: VQ-4 certification requires that RI-08 and RI-09 be resolved
and that VQ-3 requirements be satisfied. The gate order is fixed: VQ-1 → VQ-2 →
VQ-3 → VQ-4, and investing in EP-08a and EP-09a before VQ-3 is certified advances
the data quality but does not accelerate the VQ-4 gate.
```

---

### §6 Contribution to institutional design

**1. New representative case for existing RI codes:**

- **RI-06 (cycle-level import):** This paper provides a clean case of RI-06 at cycle-level scope: the entire three-step Ni(II)/Ni(II) catalytic cycle (eqs 2–4) is imported from stoichiometric (dipy)Ni chemistry into the [NiCl₂(dpe)] catalytic context. The RI-06 scope note in v0.2a — [REDACTED: substantial verbatim quotation; see Tier 9] — is directly instantiated here. This case strengthens the RI-06 codebook entry by providing a historically significant example where the imported cycle later proved substantially correct (subsequent literature validated Ni(0)/Ni(II) cycle variants), but the original communication provided no mechanism-level evidence for the isomorphism.

- **RI-07 (extended use — negative boundary claims):** The sp² selectivity claim ([REDACTED: substantial verbatim quotation; see Tier 9]) is a negative boundary claim — an assertion that sp³ halides cannot be used — made without any reported failed experiment with sp³ substrates. This confirms the RI-07 extended use note: RI-07 applies to [REDACTED: substantial verbatim quotation; see Tier 9] The Kumada 1972 case provides a canonical example of scope boundary asserted positively ("Only X is possible") without a single failure case.

**2. Labeling mismatch pattern detected:**

A **labeling mismatch** is present and concentrated in a specific textual structure. The paper labels the catalytic cycle explicitly as a "working hypothesis" in the closing sentences ([REDACTED: verbatim source quotation; see the source paper via its DOI]). However, the five [REDACTED: verbatim source quotation; see the source paper via its DOI] (feature 1), "Only C_sp² halides… can be used" (feature 2), [REDACTED: substantial verbatim quotation; see Tier 9] (feature 3), [REDACTED: substantial verbatim quotation; see Tier 9] (feature 4), [REDACTED: substantial verbatim quotation; see Tier 9] (feature 5). The hypothesis label is concentrated in the final two sentences of the paper; the preceding features section contains no epistemic hedging. This creates a structural mismatch: the hypothesis disclaimer applies retroactively to claims stated in factual form. This pattern co-occurs with RI-06, consistent with the codebook note.

**3. Incomplete negative evidence pattern:**

The selectivity claim (NC-3, SRG-2) relies on a specific form of incomplete negative evidence: the absence of reported homo-coupling products is used as positive evidence for cross-coupling selectivity, without mass-balance closure and without a stated detection limit for the absent byproducts. This is the case-specific implementation of RI-04 noted in the codebook: [REDACTED: substantial verbatim quotation; see Tier 9] The Kumada 1972 case instantiates this pattern in the following specific form: the absence of reported byproducts is the only evidence for selectivity, and the proposed catalytic cycle's own equation 3 predicts that the absent byproduct (R–R) should be present at a level proportional to catalyst loading — creating the self-contradictory absence (U-1/CLA-1). This is a compound of RI-04 and the self-contradictory-absence CLA check, and the combination is distinctive enough to propose as a named sub-pattern.

**4. RI co-occurrence pattern:**

A structurally important RI co-occurrence is present in SRG-1: RI-06 (imported model) and RI-03 (unobserved explanatory) co-occur in the same SRG and cannot be resolved independently. Resolving only RI-06 — demonstrating that the (dipy)Ni → [dpe-Ni] analogy is mechanistically valid — would be insufficient if RI-03 remains open: the black precipitate (potential Ni⁰ formation) would still undermine the homogeneous mechanism claim, making the now-confirmed analogy moot. Conversely, showing that the black precipitate is not Ni⁰ (resolving RI-03 partially) would not by itself validate the proposed cycle — the intermediates 1, 2, and 3 would still need direct characterization to reach VQ-3. The Kumada 1972 case thus provides a representative example of the RI-06 + RI-03 co-occurrence structure requiring simultaneous resolution, which should be recorded in the codebook as a common pairing in early transition-metal catalysis papers.

**5. Automatic-resolution pattern via communication → Full Paper transition:**

This paper shows the expected automatic-resolution pattern for a JACS communication that led to a full paper (the Tamao–Sumitani–Kumada 1977 paper in JACS). Several RI-07 and RI-01 items arising from the page-limit constraints of the communication format (B-3 — ligand activity order without yield values; B-1 — no TON data; B-2 — yield basis mixing) would be automatically resolved in a full paper with complete experimental sections and systematic scope tables. The §4 Era-Norm Annotation dual-classification items (B-2, B-4, A-2) are precisely the categories that show this pattern. This is consistent with the codebook note that [REDACTED: substantial verbatim quotation; see Tier 9]

**6. Institutional design additions:**

No new PRI candidate is proposed for this paper. The PRI-10 (kinetic overclaim) pattern is not present: the paper does not assert a rate enhancement without kinetic data — it simply does not report kinetic data and labels the mechanism a working hypothesis. The PRI-11 (mechanism–kinetics decoupling) pattern is a precursor match: the proposed catalytic cycle is not used to derive a rate law algebraically, and the mechanism is not even supported by agreement with observed rate orders (as in the PRI-11 definition), since no kinetic data are reported at all. This case falls short of the PRI-11 threshold (which requires rate order data that support the mechanism by agreement) — it is a simpler case of RI-06 + RI-03 without any kinetic dimension. No promotion candidate is generated.

EP dictionary case-specific implementation additions:

- EP-03a in a Ni-phosphine catalytic system: [REDACTED: substantial verbatim quotation; see Tier 9] This implementation is specific to early Ni-catalyzed cross-coupling papers where catalyst decomposition is a recurring ambiguity.
- EP-04a applied to self-contradictory absence: [REDACTED: substantial verbatim quotation; see Tier 9] This implementation is specific to papers where the proposed catalytic cycle explicitly predicts a byproduct that is not reported.

---

> **Tier 8 redaction notice**: This file is a redacted copy of the corresponding Tier 3 / Tier 9 output. Verbatim source-paper quotations have been replaced by `[REDACTED: see source paper §<loc>; full text retained in Tier 9 reviewer-only deposit]` markers, preserving location references and our own analytical content. Bibliographic fields (title, authors, journal, year, DOI), analytical labels (`evidence_chain:` with B-/U-/A-/C- internal IDs), short technical terms, and our own analytical text are not redacted. The redaction was applied by `scripts/redact_for_tier8.py` and, for this version, by `scripts/build_paperA_R1_public.py` with `scripts/redact_source_ngram_runs.py` (scripts of the project repository; they are not deposited).
