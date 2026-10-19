prompt_version: stage3-v2-en-20260419
model_info: claude-sonnet-4-6

# Re-certification Assessment Sheet for Scientific Knowledge

## Murai et al. 1993 (Nature, Articles)

---

### §1 Claim Architecture

**Core claim summary:**

The paper's central assertion is that RuH₂(CO)(PPh₃)₃ enables catalytic, efficient, selective, and broadly applicable coupling of ortho aromatic C–H bonds with terminal olefins, using chelation assistance by an aromatic carbonyl directing group as the enabling principle. The **Novelty pillar** is the first broadly applicable catalytic C–H/olefin coupling that simultaneously achieves (a) high yields (approaching quantitative), (b) high regioselectivity ("virtually 100%[REDACTED: substantial verbatim quotation; see Tier 9]extremely valuable in organic synthesis" with a [REDACTED: substantial verbatim quotation; see Tier 9] and the chelation-assistance principle is projected as "applicable more widely for selective organometallic catalysis."

**Layered structure:**

Yes — four independent layers exist, and a single refutation does not collapse all claims:

- **Layer 1 (Synthetic demonstration):** The GC yield data in Table 1 (13 runs) constitute independently verifiable experimental observations. A refutation of the mechanism would not invalidate the yield data.
- **Layer 2 (Mechanistic design principle — chelation assistance):** The chelation-assistance framing is an interpretive layer. The paper explicitly states [REDACTED: substantial verbatim quotation; see Tier 9] This layer is immune to refutation by yield-level anomalies but is vulnerable at the mechanistic level (intermediate not confirmed, active-species identity not established).
- **Layer 3 (Comparative efficiency — superiority over refs 11/12):** This layer is asserted, not demonstrated numerically; it is structurally independent of the synthetic data but is unsupported by the paper's own quantitative record.
- **Layer 4 (Projected generality — "applicable more widely"):** A speculative extrapolation beyond the paper's data; it does not depend on the other layers being validated, and it cannot be falsified by the paper's data alone.

Inter-layer dependencies: Layers 3 and 4 depend on Layer 1 being accepted as valid. Layer 2 (mechanistic) is used rhetorically to support Layer 4 but is not experimentally linked to Layer 1; A-1 explicitly severs this connection by deferring mechanistic confirmation. This creates a situation in which the mechanistic deferral (Layer 2 declared provisional) structurally insulates the synthetic claim (Layer 1) from mechanistic attack, while simultaneously grounding the projected generality claim (Layer 4) — which it cannot evidentiary support.

---

### §2 SRG / CLA → RI / ER / EP Crosswalk

**2a. SRG acquisition (from Stage 1 Turn 4 META):**

- SRG-1 [Quantitative evidence base]: B-1, B-2, B-3, B-4
- SRG-2 [Catalytic cycle evidence absent]: A-1, U-1, U-2
- SRG-3 [Selectivity basis absent]: B-8, B-9, B-10, U-4
- SRG-4 [Scope claims exceed data]: B-5, U-3, B-7
- SRG-5 [Prior art not engaged numerically]: C-1, B-2

**2b. CLA candidate identification:**

D-4 candidates not captured in existing SRGs:

- **Candidate 7** (Mechanistic analogy validity — B-11, C-2, C-5, C-4): B-11 and C-2 are partially within SRG-2's orbit but the specific invalidity of the cited precedents (Mn(I)/Ru(II) ≠ Ru(0) OA) is not captured by any SRG member item. CLA designation warranted.
- **Candidate 8** (Catalyst loading discontinuity — B-6): B-6 is not a member of any SRG. CLA designation warranted.
- **Candidate 9** (Catalyst recovery/recyclability — B-2, B-3): grounded_in items overlap with SRG-1 (B-2, B-3); the specific catalyst fate question is not captured by SRG-1's scope. CLA designation warranted.
- **Candidate 10** (Thermodynamic vs. kinetic control — B-8, B-10, A-1): B-8 is SRG-3 member; A-1 is SRG-2 member. The thermodynamic/kinetic framing gap is a cross-SRG issue. Capture as CLA since no single SRG addresses this explicitly.

**Self-contradictory-absence CLA check:**

U-1 (cyclometallated intermediate postulated, not observed) and U-2 (Ru(II) pre-catalyst, Ru(0) cycle required, activation not characterized) are captured in SRG-2. No additional U items fall outside existing SRGs.

---

**2c. RI mapping:**

---

**SRG-1 [Quantitative evidence base]**

* **Primary RI**: RI-01 [Reporting integrity] — Cross-comparison of performance claims is impossible because measurement frames are inconsistent: GC yield without internal standard (B-1), TOF superlative without actual TOF values (B-2), catalyst screen without yield data (B-3), structure certification without method specification (B-4).
* **Secondary RI**: RI-08 [Unquantified reliability] — No replicate measurements or uncertainty estimates are reported for any run in Table 1; mass balance for olefin consumption is not monitored (B-7).
* **ER**: For the efficiency claim to hold independently evaluable, the paper must report: (a) GC calibration method (internal standard identity, response factors) enabling yield-number conversion; (b) actual TOF values for runs 1, 9, 10 permitting comparison with claimed "highest"; (c) catalyst comparison data with yield values enabling structure–activity evaluation; (d) product characterization methods enabling identity confirmation.
* **EP**: EP-01a [Reporting-coherence pack]; EP-08a [Replication / uncertainty pack]
* **Case-specific implementation**: For EP-01a: supply internal standard identity (e.g., biphenyl or n-decane) and GC response factors for each product, plus isolated yields for the 10 runs currently GC-only. For EP-08a: report TOF as (mol product)(mol Ru)⁻¹ h⁻¹ with time-resolved yield data for runs 1, 9, 10; include duplicate runs for at least two representative substrates to establish yield precision (±σ).
* **Notes**: Sub-B items B-1, B-2, B-3, B-4, B-7. Position in TEMPERATURE_SUMMARY: high_convergence_low_gap (B-1: V1=high, V3=high, convergence 2/3; B-2: V1=high, V3=high, convergence 2/3; B-3: V1=medium, V2=medium, V3=medium, convergence 3/3). B-3 is the highest-convergence item (3/3 agents). This SRG constitutes the quantitative foundation gap; its resolution is a prerequisite for Layer 1 to reach VQ-4.

---

**SRG-2 [Catalytic cycle evidence absent]**

* **Primary RI**: RI-03 [Unobserved explanatory] — The cyclometallated intermediate (Fig. 1) is the selectivity-determining species according to the paper's own argument, yet no stoichiometric synthesis, ³¹P{¹H} NMR observation, X-ray structure, or trapping experiment is reported (U-1). Similarly, the Ru(0) active species required by the proposed cycle is not observed; the activation pathway from Ru(II) pre-catalyst is not proposed or characterized (U-2).
* **Secondary RI**: RI-06 [Imported model] — The proposed cycle imports the cyclometallation intermediate via structural analogy from Mn(I) electrophilic (ref. 14) and Ru(II) carboxylate (ref. 15) precedents that operate by different mechanisms (B-11); the Ru(0) OA cycle itself is an imported mechanistic model not independently validated.
* **ER**: For the mechanistic design claim (chelation assistance) to reach VQ-3, the paper requires: (a) experimental observation of the cyclometallated intermediate by at least one direct method (stoichiometric synthesis, ³¹P NMR characterization, or X-ray crystallography); (b) identification of the Ru(0) active species by spectroscopy or independent Ru(0) source control experiment; (c) at least one kinetic discriminator (KIE, Hammett correlation, or rate-law derivation) distinguishing the proposed OA mechanism from electrophilic and radical alternatives.
* **EP**: EP-03a [Direct-observation / state-assignment pack]; EP-06a [Analogy-validation pack]
* **Case-specific implementation**: For EP-03a: stoichiometric reaction of RuH₂(CO)(PPh₃)₃ with acetophenone at 135°C to attempt isolation or ³¹P{¹H} NMR detection of the cyclometallated Ru(II) complex, combined with an independent Ru(0) source (e.g., Ru₃(CO)₁₂ + PPh₃ under H₂) as catalyst to verify active-species identity. For EP-06a: quantitative comparison of the stoichiometric cyclometallation conditions in refs 14 and 15 (Mn(I)/Ru(II), electrophilic mechanism) with the proposed Ru(0) OA conditions, specifying why the structural similarity of intermediates overrides the mechanistic differences.
* **Notes**: Sub-items A-1, U-1, U-2. Position: low_convergence_high_gap (V2-Q2 → A-1/U-1, critical, V2-only; U-2, high, V2-only). This is the highest-priority mechanistic gap. A-1's explicit deferral ("not yet clear") provides textual cover but does not reduce the analytical weight of the gap. RI-03 and RI-06 co-occur: resolving RI-03 (observing the intermediate) does not resolve RI-06 (validating the analogy with structurally non-isomorphic precedents) — both must be addressed to reach VQ-3.

---

**SRG-3 [Selectivity basis absent]**

* **Primary RI**: RI-05 [Qualitative overread] — The paper derives mechanistic causal assignments (chelation controls ortho-selectivity; ring strain controls rate differences between runs 10 and 11; 1-indanone does not react due to ring strain) from qualitative kinetic comparisons (B-8: run 10 = 0.5 h vs. run 11 = 20 h) and a negative result (B-9: 1-indanone "did not react at all") without rate constants, activation energies, or control experiments isolating the variable.
* **Secondary RI**: RI-04 [Unreplicated discriminator] — The negative result for 1-indanone (B-9) is a single data point ("did not react at all," no detection limit stated, no competing explanation excluded) used as positive evidence for the ring-strain hypothesis. The regioselectivity claim "virtually 100%" (B-10, U-4) is a single-run observation without analytical confirmation that non-observed regioisomers are absent.
* **ER**: For the selectivity claim to pass VQ-3, the paper requires: (a) rate constants or at least time-resolved yield profiles for runs 10 and 11 enabling a quantitative rate ratio; (b) a GC/NMR detection limit statement for the 1-indanone case (or a confirmed zero-conversion assay); (c) analytical confirmation (GC or NMR with defined detection limits) that non-observed regioisomers are absent, not merely undetected, in at least one representative run.
* **EP**: EP-05a [Quantitative-ranking substantiation pack]; EP-04a [Discrimination / replication pack]
* **Case-specific implementation**: For EP-05a: report GC yield at multiple time points for runs 10 and 11 (both using α-tetralone and benzocycloheptanone substrates) in the same vessel under identical conditions; compute kobs ratio to verify the rate-difference claim quantitatively. For EP-04a: re-run the 1-indanone case with GC monitoring at 1, 4, 8, and 20 h to establish a conversion limit; separately, spike a reaction mixture with authentic regioisomeric products to establish GC detection limits for the regioselectivity claim.
* **Notes**: Sub-items B-8, B-9, B-10, U-4. Position: high_convergence_low_gap (B-8: V1=medium, V2=high, convergence 2/3, gap=low; B-9: V1=medium, V2=high, convergence 2/3, gap=low). RI-05 makes VQ-3 "qualified[REDACTED: substantial verbatim quotation; see Tier 9]Incomplete negative evidence" per §6.

---

**SRG-4 [Scope claims exceed data]**

* **Primary RI**: RI-07 [Unsupported boundary] — The claim "a variety of aromatic systems" (Abstract, B-5; U-3) sets a positive boundary that exceeds the demonstrated data: all 13 runs use aromatic ketone directing groups, and no non-ketone example (aldehyde, ester, amide, imine) is provided. The paper implicitly claims "all acylbenzene/acylheteroaromatic + terminal olefin combinations" are within scope while presenting 13 selected runs with two acylheteroaromatic examples (runs 12, 13).
* **Secondary RI**: RI-01 [Reporting integrity] — B-7: the "quantitative yields based on both starting materials" claim presupposes monitored olefin consumption, but no olefin fate data (isomerization, oligomerization) are reported for any run.
* **ER**: For the scope claim to hold, the paper requires: (a) at least one non-ketone directing group example (aldehyde, ester, or imine) to justify "a variety of aromatic systems"; (b) olefin mass balance data (GC analysis of the reaction mixture for olefin isomers and oligomers) to validate "quantitative yields based on both starting materials."
* **EP**: EP-07a [Boundary-test pack]; EP-01a [Reporting-coherence pack]
* **Case-specific implementation**: For EP-07a: test benzaldehyde, methyl benzoate, and N,N-dimethylbenzamide as directing-group variants against triethoxyvinylsilane under standard conditions; report yield and selectivity, even if zero. For EP-01a: include GC monitoring of olefin consumption (using authentic triethoxyvinylsilane and its isomers as standards) in at least one run to close the bilateral yield mass balance.
* **Notes**: Sub-items B-5, U-3, B-7. U-3 is the self-contradictory absence: the abstract's claim cannot be verified by the paper's own 13 runs. RI-07 is the primary driver; the scope claim is not a "negative boundary" (RI-07 extended use) but a positive boundary with insufficient supporting experiments.

---

**SRG-5 [Prior art not engaged numerically]**

* **Primary RI**: RI-09 [External superiority] — The claim that the present system has "among the highest" turnover frequencies (B-2) for "this type of reaction" and surpasses refs 11 and 12 (C-1) is asserted by citing the limitation of prior systems without providing the comparative TOF values from those references or a matched comparison on any common substrate.
* **Secondary RI**: RI-01 [Reporting integrity] — B-2: actual TOF values for runs 1, 9, 10 are not tabulated; the comparison claim is therefore unverifiable even against the paper's own stated data.
* **ER**: For the comparative efficiency claim to hold, the paper requires: (a) tabulated TOF values for runs 1, 9, 10 in units of (mol product)(mol Ru)⁻¹ h⁻¹; (b) literature TOF values for refs 11 and 12 cited from those papers on a common basis; (c) acknowledgment of whether runs with non-standard loading (runs 5, 6) are included or excluded from the efficiency summary.
* **EP**: EP-09a [Internal benchmark pack]; EP-01a [Reporting-coherence pack]
* **Case-specific implementation**: For EP-09a: add a single row to Table 1 specifying TOF (h⁻¹) calculated from yield, time, and catalyst loading for runs 1, 9, 10; append a footnote citing the closest TOF or TON values extracted from refs 11 (Jordan & Taylor, JACS 1989) and 12 (Moore et al., JACS 1992) on their respective substrates.
* **Notes**: Sub-items C-1, B-2. Position: high_convergence_low_gap (B-2: V1=high, V3=high, convergence 2/3). SRG-5 overlaps structurally with SRG-1 (B-2 is a shared member); SRG-5 captures the external-comparative dimension, SRG-1 the internal analytical dimension. Resolution of SRG-1 (reporting actual TOF values) is a prerequisite for resolving SRG-5.

---

**Outside the SRGs: CLAs**

---

**CLA-1: Mechanistic analogy validity — Mn(I)/Ru(II) precedents cited for Ru(0) OA cycle**

* **Primary RI**: RI-06 [Imported model] — The paper imports the cyclometallated intermediate from refs 14 (Mn(I), electrophilic) and 15 (Ru(II) carboxylate) and invokes ref. 17 (olefin OA to Ru) for the olefin coordination step, without addressing the mechanistic discrepancy between these stoichiometric non-Ru(0) precedents and the proposed catalytic Ru(0) cycle.
* **Secondary RI**: RI-03 [Unobserved explanatory] — The intermediate that is being validated by analogy (B-11, C-2) is itself not observed (see SRG-2, U-1).
* **ER**: For the mechanistic analogy to be acceptable as supporting evidence, the paper requires: demonstration that the structural products of the Mn(I) and Ru(II) reactions (refs 14, 15) are electronically and structurally isomorphic with the proposed Ru(0) OA intermediate, or an explicit argument why the oxidation-state discrepancy is mechanistically irrelevant.
* **EP**: EP-06a [Analogy-validation pack]
* **Case-specific implementation**: For EP-06a: provide DFT-computed structures of (a) the proposed Ru(0) OA cyclometallated intermediate and (b) the Mn(I) and Ru(II) stoichiometric precedent products, comparing M–C, M–O bond lengths and metal d-electron count to evaluate structural isomorphism. Alternatively, prepare the proposed intermediate via the reported stoichiometric routes (refs 14, 15 conditions adapted for Ru) and compare ³¹P{¹H} and ¹H NMR to the catalytically relevant complex.
* **Notes**: Grounded in B-11, C-2, C-5, C-4. This CLA overlaps with SRG-2 in scope (both concern the mechanistic intermediate) but the specific analogy-validity issue is distinct from the observation gap (RI-03 in SRG-2). Labeling mismatch pattern (§6): the paper uses factual verb [REDACTED: substantial verbatim quotation; see Tier 9] — "similar to" is a qualification, but "has been known" is factual. The factual verb construction partially obscures the analogy gap.

---

**CLA-2: Catalyst loading discontinuity (runs 5 and 6)**

* **Primary RI**: RI-01 [Reporting integrity] — Runs 5 and 6 use 6 mol% catalyst (0.12 mmol) versus 2 mol% (0.04 mmol) for all other runs; the rationale is not stated; the efficiency generalization claims (TOF, practical synthesis criteria) apply as if all runs use the same loading.
* **Secondary RI**: RI-07 [Unsupported boundary] — The claim that [REDACTED: substantial verbatim quotation; see Tier 9] may not hold for the substrate combinations in runs 5 and 6, which require 3× the standard loading; the boundary is set without acknowledging this limitation.
* **ER**: For the efficiency claim to apply uniformly to all 13 runs, the paper requires: an explicit statement identifying the conditions under which 6 mol% loading is required and whether this represents a substrate class limitation or an experimental optimization shortfall.
* **EP**: EP-01a [Reporting-coherence pack]
* **Case-specific implementation**: For EP-01a: add a table footnote to Table 1 runs 5–6 specifying the reason for elevated loading (e.g., lower catalyst activity with allylsilane substrates); report the yield achieved at 2 mol% loading for run 5 to establish whether the elevated loading is strictly necessary.
* **Notes**: Grounded in B-6. This is a minor coherence gap, non-fatal to the overall efficiency claim, but relevant to the practical utility extrapolation. Not a member of any SRG.

---

**CLA-3: Catalyst fate, recovery, and recyclability**

* **Primary RI**: RI-01 [Reporting integrity] — The paper reports yields for 13 runs and claims high TOF for runs 1, 9, 10, but provides no information on ruthenium speciation after reaction, catalyst recovery, or recyclability; the "practical organic synthesis" utility claim implicitly requires this information.
* **ER**: For the practical utility claim to be supported, the paper requires at least a post-reaction spectroscopic analysis (ICP, ³¹P NMR of the spent reaction mixture) or a catalyst recycling run.
* **EP**: EP-01a [Reporting-coherence pack]
* **Case-specific implementation**: Filter post-reaction mixture and analyze the filtrate and solid by ³¹P{¹H} NMR and ICP-OES; report whether the Ru catalyst is recoverable and reusable for at least one additional run on run 9 conditions.
* **Notes**: Grounded in B-2, B-3. Non-fatal to the synthetic demonstration claim; relevant to the "extremely valuable in organic synthesis" assertion. Era-norm dependent: catalyst recycling data were not routinely reported in 1993 short communications; by modern standard (ACS Catalysis, Angewandte submission requirements) this is expected.

---

**CLA-4: Thermodynamic vs. kinetic control of selectivity**

* **Primary RI**: RI-05 [Qualitative overread] — The paper attributes ortho-aromatic selectivity to a kinetically controlled chelation-directed C–H cleavage step and anti-Markovnikov olefin selectivity to M–H insertion regiopreference, but does not specify whether either selectivity is thermodynamically or kinetically determined; the mechanism is "not yet clear," making these assignments speculative.
* **Secondary RI**: RI-03 [Unobserved explanatory] — The selectivity-determining transition state is neither observed nor kinetically constrained.
* **ER**: For the "applicable more widely" projected generality to have mechanistic grounding, the paper requires at least a qualitative thermodynamic analysis (e.g., whether the C–H functionalization products are thermodynamic sinks or whether the reaction could be reversible under the conditions).
* **EP**: EP-05a [Quantitative-ranking substantiation pack]; EP-03a [Direct-observation / state-assignment pack]
* **Case-specific implementation**: For EP-05a: perform a crossover experiment by running a 1:1 mixture of two aromatic ketones with one olefin and determining whether statistical or selective product distribution is observed; kinetic selectivity predicts the distribution would be substrate-controlled. For EP-03a: a temperature-dependent yield series (80°C, 100°C, 120°C, 135°C) would distinguish a kinetically controlled low-temperature-selective from a thermodynamically controlled flat-temperature-yield case.
* **Notes**: Grounded in B-8, B-10, A-1. Cross-SRG: A-1 in SRG-2, B-8 in SRG-3. RI-05 makes VQ-3 "qualified" per the matrix note. This CLA reinforces the SRG-3 finding from a different angle.

---

### §3 Current VQ assessment

**Current judgment: VQ-2 (qualified) [Method — Qualified]**

---

**VQ-1 [Observation] — PASS (non-fatal)**

RI-02 [Object identification]: Product structures are certified as "established unequivocally by standard methods" (B-4). The paper does not specify which standard methods were used, and for 13 novel products in a 1993 Nature communication this is consistent with ¹H NMR + elemental analysis/HRMS. The certification claim is vague but is applied uniformly to all 13 runs. Judgment: **non-fatal** — the absence of method specification is a reporting omission (RI-01) rather than a product identity failure; there is no internal evidence that any of the 13 reported products is misidentified. VQ-1 holds on a non-fatal basis.

Note (non-fatal): B-4's "standard methods" omission is formally RI-02, but given the 1993 Nature short-communication context and the structural simplicity of the ortho-functionalized ketone products (readily confirmed by ¹H NMR ortho-H shift and molecular ion), this does not constitute a plausible identity failure. Modern recertification would require full NMR data or HRMS for all 13 compounds.

---

**VQ-2 [Method] — PASS (qualified) — on the premise that VQ-1 holds**

RI-01 [Reporting integrity]: SRG-1 identifies systematic analytical omissions (no GC calibration, no isolated yields for 10/13 runs, no actual TOF values, no olefin fate data). These omissions make the efficiency claims non-independently evaluable. However, they are **non-fatal** to the observational core: the existence of the products and their approximate yield levels are not in dispute, only the precision of the numerical claims. The GC yield method, while uncalibrated, is standard for exploratory catalysis reports.

RI-07 [Unsupported boundary — SRG-4]: The scope boundary "a variety of aromatic systems" is unsupported. This is **non-fatal** to the demonstrated runs (which are not claimed to be impossible) but is fatal to the abstract-level scope claim taken at face value.

**Qualification of VQ-2:** RI-05 [Qualitative overread — SRG-3 and CLA-4] remains in a substantive form: the mechanistic attributions for rate differences (runs 10 vs. 11) and the negative result (1-indanone) are used as positive kinetic evidence without numerical support. Per Note 1 of the VQ decision matrix, if RI-05 remains in a serious form, VQ-3 is "qualified." The qualification propagates down: VQ-2 is thus returned as **qualified** because the method-level claims (selectivity, rate attribution) rest on qualitative readings that do not meet RI-05 standards.

---

**VQ-3 [Mechanism] — FAIL**

RI-03 [Unobserved explanatory — SRG-2]: The cyclometallated intermediate is the central explanatory species for all selectivity claims and is simultaneously (a) depicted in Fig. 1 as a defined structure, (b) qualified by the paper itself as "postulated," and (c) supported only by mechanistic analogies from non-isomorphic systems (RI-06, CLA-1). No elementary step in the proposed catalytic cycle is directly confirmed. This is **fatal** to VQ-3: a mechanism that invokes an unobserved key intermediate as its selectivity-determining species and derives all structure–activity arguments from that intermediate cannot reach the Mechanism certification level.

RI-06 [Imported model — SRG-2, CLA-1]: The proposed cycle imports mechanistic structure from Mn(I) and Ru(II) non-Ru(0) precedents without demonstrating isomorphism. Co-occurrence of RI-03 and RI-06 means resolving one is insufficient; both must be addressed.

Unresolved RIs at VQ-3: RI-03, RI-06.

**However, Layer 1 (synthetic demonstration) on its own:** The Table 1 data reach VQ-2 (qualified) as a stand-alone synthetic demonstration; they do not depend on the mechanism being confirmed. If the paper's claims were narrowed to [REDACTED: substantial verbatim quotation; see Tier 9] then a VQ-2 (qualified) recertification of Layer 1 alone would be defensible.

---

**VQ-4 [Benchmark] — FAIL (blocked by VQ-3 failure)**

RI-08 [Unquantified reliability — SRG-1]: No replicate measurements, no uncertainty estimates, no time-resolved yield data are provided. Fatal to VQ-4.

RI-09 [External superiority — SRG-5]: "Among the highest reported" TOF claim is asserted without tabulation of actual TOF values for runs 1, 9, 10 or a numerical comparison with refs 11, 12. Fatal to VQ-4.

VQ-4 blocked by unresolved VQ-3 and additional RI-08, RI-09 failures.

---

### §4 Era-Norm Annotation

**communication-era tolerated:**

- **B-1** (GC yield without isolated yields for 10/13 runs; no internal standard specified): In 1993 Nature Articles communications, GC yield reporting without a fully specified calibration curve was standard practice for exploratory catalysis scope tables; isolated yields for a 2 mmol scale run in refluxing toluene were often reported only for the "showcase" examples. Tolerated by the 1993 Nature short-communication format.

- **B-4** ("Structures of all products established unequivocally by standard methods"): In 1993, bulk ¹H NMR + elemental analysis or HRMS was considered sufficient for structure certification of new compounds in Nature communications without explicit enumeration. "Standard methods" was an accepted shorthand.

- **B-3** (qualitative-only catalyst screen: "equally effective," "modestly effective," "not effective"): Brief qualitative catalyst comparisons without yield tables were routine for scope-defining communications in organometallic catalysis in the early 1990s; full structure–activity tables were relegated to follow-up papers.

- **C-3** (refs 1–7 cited as a single block for 30-year field history): Citation of a historical background cluster without individual attribution was standard for short communications constrained to a narrow reference list.

- **CLA-3** (catalyst recovery/recyclability not reported): Catalyst recyclability was not a standard reporting requirement for new catalyst discovery papers in Nature in 1993; recycling studies were expected in subsequent process-chemistry reports.

**modern-era deficient:**

- **B-2** (TOF superlative claim "among the highest reported" with no actual TOF values): A modern recertification at ACS Catalysis, Nature Catalysis, or JACS requires tabulated TOF (h⁻¹) with time-resolved data; a superlative efficiency claim without the numerical basis would be rejected at review. Dual classification: tolerated in 1993 communication format; fatal gap by modern standards.

- **B-1** (GC yield without internal standard specification): Modern catalysis reporting requires explicit GC calibration methodology (internal standard identity, response factors, or yield calculation protocol); absence is a reviewable deficiency at any major journal. Dual classification: tolerated in 1993; deficient now.

- **B-9** (1-indanone "did not react at all" used as positive mechanistic evidence without detection limit): Modern mechanistic papers require a defined lower detection limit or an alternative zero-conversion assay; use of "did not react at all" as a mechanistic argument without analytical support is insufficient by current standards. This is also a case of "Incomplete negative evidence" (§6).

- **U-1** (cyclometallated intermediate "postulated[REDACTED: substantial verbatim quotation; see Tier 9]the mechanism is not yet clear" — would today require a disclaimer figure caption.

- **U-4** (regioselectivity "virtually 100%[REDACTED: substantial verbatim quotation; see Tier 9]virtually 100%" without analytical confirmation is insufficient.

- **CLA-1** (Mn(I)/Ru(II) precedents cited for Ru(0) OA cycle without mechanistic reconciliation): Modern organometallic mechanistic papers require at minimum a sentence acknowledging the oxidation-state difference between the cited precedents and the proposed mechanism; citing across a mechanistic class boundary without comment is now a reviewable objection.

---

### §5 Shortest-reinforcement route

**First objective function: VQ-2 (qualified) → VQ-3 [Mechanism]**

The blocking conditions for VQ-3 are unresolved RI-03 (unobserved cyclometallated intermediate) and RI-06 (imported mechanistic model from non-isomorphic precedents). Both must be resolved; resolving one is insufficient.

```
Shortest route to VQ-3:

1. EP-03a [Direct-observation / state-assignment pack] — Stoichiometric
   reaction of RuH₂(CO)(PPh₃)₃ with acetophenone at 80–135°C in toluene
   under N₂, monitored by ³¹P{¹H} NMR at defined time intervals, to
   detect or rule out the cyclometallated Ru(II) intermediate; or
   independently, synthesis of the intermediate by established routes from
   refs 14/15 adapted for Ru and spectroscopic comparison with the
   catalytically active species. Advances RI-03 (eliminates the
   unobserved-explanatory gap for U-1 and partially for U-2).

2. EP-06a [Analogy-validation pack] — DFT computation of the proposed
   Ru(0) OA cyclometallated intermediate (M06-L/def2-TZVP or comparable)
   to establish that the electronic structure is consistent with the
   structural analogy claimed from refs 14 and 15, and to provide a first-
   principles basis for the Ru(0) → Ru(II) OA step; or, an independent
   Ru(0) source (e.g., generated in situ from Ru₃(CO)₁₂) used as
   catalyst to confirm that the pre-catalyst activation step produces the
   same active species. Advances RI-06 (validates the imported mechanistic
   model) and partially RI-03 (active-species confirmation for U-2).

3. EP-04a [Discrimination / replication pack] — kH/kD kinetic isotope
   effect experiment using deuterated aromatic substrate (acetophenone-d₅)
   versus acetophenone under identical conditions (run 9 or run 10) to
   confirm that C–H cleavage is rate-determining and to provide at least
   one kinetic discriminator distinguishing the OA mechanism from
   electrophilic SE_Ar or concerted metalation-deprotonation alternatives.
   Advances RI-04 (provides a discrimination experiment for the key
   elementary step). Prerequisite for VQ-3 qualification removal.
```

*Note on ordering:* EP-03a has the highest information gain because it simultaneously addresses U-1 (intermediate identity) and partially U-2 (active species). EP-06a is ranked second because computational validation is now experimentally accessible and provides a lower-cost route to RI-06 resolution. EP-04a (KIE) is ranked third as it requires deuterated substrate synthesis but provides the only direct kinetic discriminator.

**Second objective function: VQ-3 → VQ-4 [Benchmark]**

With VQ-3 resolved, the remaining VQ-4 blockers are RI-08 (unquantified reliability) and RI-09 (external superiority claim).

```
Shortest route to VQ-4:

1. EP-08a [Replication / uncertainty pack] — Report actual TOF values
   (mol product)(mol Ru)⁻¹ h⁻¹ calculated from time-resolved yield data
   for runs 1, 9, and 10; include duplicate runs (n≥2) for at least two
   representative substrates to establish yield reproducibility (±1σ).
   Advances RI-08 (internal reliability) and contributes to RI-09 (TOF
   basis for external comparison).

2. EP-09a [Internal benchmark pack] — Extract TON/TOF values from refs 11
   (Jordan & Taylor, JACS 1989, zirconium/α-picoline/propene system) and
   12 (Moore et al., JACS 1992, ruthenium/pyridine/CO/hexene system) from
   those publications; tabulate against runs 1, 9, 10 on a common basis
   [(mol product)(mol M)⁻¹ h⁻¹]; acknowledge that different metals and
   substrates make direct comparison approximate and specify a substrate-
   normalized comparison metric. Advances RI-09 (converts asserted
   superiority to evidenced superiority).

3. EP-01a [Reporting-coherence pack] — Supply GC calibration methodology
   (internal standard identity, response factors for representative
   products, or isolated-yield validation for the 10 GC-only runs) to
   enable independent verification of Table 1 yields. Advances RI-01
   (removes the cross-comparison impossibility) and supports RI-08.
```

**Certification-gate note:** Experimental investments should be prioritized in the information-gain order above (EP-03a → EP-06a → EP-04a for VQ-3; EP-08a → EP-09a → EP-01a for VQ-4), but the final certification must follow the fixed gate order VQ-1 → VQ-2 → VQ-3 → VQ-4; VQ-4 cannot be certified before VQ-3 is resolved.

---

### §6 Contribution to institutional design

**1. New representative case for RI-03 (subtype: cycle-level, no elementary step confirmed):**

The Murai 1993 case provides an extreme instance of RI-03 in which no single elementary step of a multi-step proposed catalytic cycle is experimentally characterized. The paper proposes Ru(0) coordination → C–H OA → cyclometallation → olefin insertion → reductive elimination, but direct evidence exists for none of these steps. The RI-03 subtype "Available-but-unutilized characterization" does not apply here (there is no acquired data that could verify the mechanism); rather, this is the canonical "unobserved explanatory" subtype. This case strengthens the case for RI-03 as a standalone fatal-at-VQ-3 code in the Codebook.

**2. RI co-occurrence pattern — RI-03 + RI-06 in SRG-2:**

SRG-2 demonstrates that RI-03 and RI-06 systematically co-occur when a paper proposes a novel catalytic cycle by analogy with precedents from a different metal/oxidation-state class. Resolving RI-03 (observing the intermediate) does not resolve RI-06 (validating that the analogy is mechanistically isomorphic), because the observed intermediate in the new system might differ from what the analogical precedent predicts. Conversely, resolving RI-06 computationally (DFT validation of structural similarity) does not replace the need for direct observation (RI-03). The Murai case should be registered as the first clean documented instance of the RI-03 + RI-06 co-occurrence pattern requiring dual resolution — a note should be added to the Codebook: [REDACTED: substantial verbatim quotation; see Tier 9]

**3. Labeling mismatch pattern confirmed:**

The paper explicitly uses the hypothesis label "postulated" in the text ("the intermediate postulated in Fig. 1") while the figure caption and the mechanistic discussion use factual language ([REDACTED: substantial verbatim quotation; see Tier 9]). This is a clean instance of the "Labeling mismatch" pattern: the hypothesis qualifier is isolated to one parenthetical phrase while the rest of the mechanistic section proceeds with factual verbs. The position of the hypothesis label (concentrated in a single qualifier phrase in a seven-sentence mechanistic section) is consistent with what would be expected from a short communication that needed to assert a mechanistic framework without claiming to have established it. This pattern is consistent with prior observations and confirms it as a recurring structural feature of short communications proposing catalytic cycles without mechanistic verification.

**4. Incomplete negative evidence pattern (RI-04 case-specific instance):**

B-9 (1-indanone "did not react at all") is used as positive mechanistic evidence for the ring-strain hypothesis without a mass-balance closure or kinetic-window evaluation. Specifically: (a) no GC analysis of the 1-indanone reaction mixture is reported to confirm zero conversion vs. trace conversion below GC detection; (b) the substrate's "did not react at all" verdict is used to support a specific structural claim (ring strain in the cyclometallated intermediate) without excluding electronic (reduced electron density at the carbonyl due to ring conjugation) or steric alternatives. This is a textbook instance of "Incomplete negative evidence" per §6 of the prompt, specifically: negative result used as positive mechanistic evidence without mass-balance closure. The existing RI-04 handling in the Codebook adequately captures this; the Murai case provides a clean organic-catalysis case-specific implementation that could be added to the EP-04a dictionary entry: [REDACTED: substantial verbatim quotation; see Tier 9]

**5. Automatic-resolution pattern via communication → Full Paper transition:**

B-1 (GC calibration), B-3 (qualitative catalyst screen), B-4 (standard methods), and CLA-2 (catalyst loading rationale) are patterns consistent with the short-communication → full paper transition. The Murai group's follow-up papers (Kakiuchi et al., JACS 1993 and subsequent publications) resolved many of these omissions automatically by providing extended substrate scope tables, isolated yield data, and further catalyst structure–activity comparisons in full-length papers. This confirms the "automatic-resolution pattern" for RI-01/RI-07 items arising from format constraints. However, the mechanistic items (SRG-2: RI-03, RI-06) were not automatically resolved by format transition — they required dedicated mechanistic studies that appeared over subsequent years (KIE studies, computational work by Gorelsky et al. 2003 and others). This distinction is important: format-driven omissions (SRG-1, parts of SRG-3, CLA-2) auto-resolve; mechanism-level omissions (SRG-2) require dedicated experimental campaigns.

**6. No new PRI candidate detected:**

The patterns observed are fully captured by existing RI codes. PRI-10 (Kinetic overclaim) is a borderline candidate: B-2's "among the highest reported TOF" without actual TOF values could be construed as a kinetic overclaim, but the paper does not claim a specific rate enhancement (it claims a rank-order position), so PRI-10 does not strictly apply. PRI-11 (Mechanism–kinetics decoupling) is not instantiated here because no rate law is proposed or tested. No new PRI candidate is warranted from this case.

**Summary:** This case confirms and reinforces existing institutional design on RI-03, RI-06, RI-04 (incomplete negative evidence), and the labeling mismatch pattern. The primary contribution is the documentation of the RI-03 + RI-06 co-occurrence requiring dual resolution as a distinct pattern requiring a Codebook annotation.

---

> **Tier 8 redaction notice**: This file is a redacted copy of the corresponding Tier 3 / Tier 9 output. Verbatim source-paper quotations have been replaced by `[REDACTED: see source paper §<loc>; full text retained in Tier 9 reviewer-only deposit]` markers, preserving location references and our own analytical content. Bibliographic fields (title, authors, journal, year, DOI), analytical labels (`evidence_chain:` with B-/U-/A-/C- internal IDs), short technical terms, and our own analytical text are not redacted. The redaction was applied by `scripts/redact_for_tier8.py` and, for this version, by `scripts/build_paperA_R1_public.py` with `scripts/redact_source_ngram_runs.py` (scripts of the project repository; they are not deposited).
