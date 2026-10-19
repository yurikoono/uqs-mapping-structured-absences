prompt_version: stage3-v2-en-20260419
model_info: claude-sonnet-4-6

# Re-certification Assessment Sheet for Scientific Knowledge

## Murai et al. 1993 (Nature, Articles)

---

### §1 Claim Architecture

**Core claim summary:**

The paper's core claim is that a single commercially accessible ruthenium complex, RuH₂(CO)(PPh₃)₃, catalyses the addition of aromatic ortho C–H bonds to terminal olefins via chelation-directed activation, simultaneously achieving efficiency (almost quantitative yields from both reactants, among the highest TOF reported), generality (13 substrate combinations spanning acylbenzenes and acylheteroaromatics with a variety of terminal olefins), and regioselectivity (virtually 100%, yielding only one of four possible regioisomers). The Novelty pillar is the co-occurrence of all three performance criteria in a single catalytic system — prior systems (refs 11/12) achieved high efficiency or generality but not simultaneously. The Utility pillar is the practical consequence: aromatic ketones can now be alkylated without sacrificing stoichiometric amounts of one reactant as solvent, directly opening "a new range of alkylated aromatic compounds."

The mechanistic rationale — chelation assistance by the carbonyl directing group, Ru(0) oxidative addition to the ortho C–H bond, insertion of the olefin into the Ru–H bond, and reductive elimination — is presented as the explanatory framework for all three performance pillars, but is explicitly deferred: [REDACTED: substantial verbatim quotation; see Tier 9]

**Layered structure judgment:**

Independent layers exist. Three performance claims (efficiency, generality, regioselectivity) are independently anchored to distinct subsections of Table 1:
- Efficiency (NC-1, NC-2, SC-1, SC-2): runs 8–13, bilateral quantitative yield
- Generality (NC-4, SC-4): runs 1–13 spanning heterocyclic and carbocyclic ketones, multiple olefin classes
- Regioselectivity (NC-5, SC-3): runs 8 and 13 (aromatic regiochemistry); all runs (anti-Markovnikov olefin regiochemistry)

A single refutation of the mechanistic rationale (NC-3, chelation) does not collapse the synthetic utility claims, because the catalytic outcome is documented independently of any mechanistic assignment. However, a refutation of the yield data quality (RI-01, RI-08; D-4-3) would simultaneously undermine all three claims, since all three rest on GC yields obtained by the same unspecified analytical method. The efficiency and generality claims thus share a common analytical foundation (SRG-1) whose failure would be multi-claim catastrophic. The regioselectivity and selectivity kinetics claims (SRG-3) share a common evidentiary structure — selectivity asserted without characterisation of non-observed isomers — and are somewhat independent of the efficiency layer. The mechanistic layer (SRG-2) is separable: its failure would damage plausibility but not directly invalidate the synthetic claims.

Inter-layer dependencies: the mechanistic layer (SRG-2) underpins the scope extrapolation claim (SRG-4): "chelation assistance should be applicable more widely" is a mechanistic prediction whose scope boundary (D-4-4, U-3) cannot be evaluated without knowing what directing groups satisfy the chelation requirement.

---

### §2 SRG / CLA → RI / ER / EP Crosswalk

**SRG-1 [Quantitative evidence base]**
Member items: B-1, B-2, B-3, B-4, B-7, C-1

* **Primary RI**: RI-01 [Reporting integrity] — cross-comparison between the paper's own runs and prior-art systems is impossible because GC calibration, internal standard, and TOF numerical values are all absent, and isolated yields are reported for only 3 of 13 runs.
* **Secondary RI**: RI-09 [External superiority] — the paper's central efficiency superiority over refs 11/12 (Jordan & Taylor 1989; Moore et al. 1992) is asserted qualitatively ("exceptionally high yields") without a direct numerical comparison on a common substrate or under matched conditions.
* **ER**: For the efficiency and generality claims to hold at VQ-2, GC yields must be traceable to a calibrated measurement system (internal standard and response factors specified), actual TOF values for runs 1/9/10 must be reported in units comparable to the literature, and an olefin mass balance must confirm "based on both starting materials."
* **EP**: EP-01a [Reporting-coherence pack]; EP-09a [Internal benchmark pack]
* **Case-specific implementation**: (a) EP-01a: re-run Table 1 runs with a specified GC internal standard (e.g., decane or mesitylene) and report response factors and mass balances for all 13 runs; provide isolated yields for runs currently reporting GC yields only. (b) EP-09a: report actual TOF values (mol product per mol Ru per hour) for runs 1, 9, 10 under the reported conditions, and compile the corresponding TOF values from refs 11 and 12 under their original conditions, acknowledging substrate-class differences.
* **Notes**: B-1 and B-2 appear in TEMPERATURE_SUMMARY as high_convergence_low_gap (V1=high, V3=high for both; B-3 has convergence 3/3 at medium). B-7 is a flag on bilateral quantitative yield claim without olefin mass balance — the efficiency claim's most direct empirical anchor is unverifiable as stated. C-1 is a severed quantitative comparison (GAP-1 pending). RI-09 co-occurrence is structurally necessary: resolving RI-01 alone (providing calibrated GC) would not automatically provide the cross-system numerical comparison that RI-09 requires.

---

**SRG-2 [Catalytic cycle evidence absent]**
Member items: A-1, U-1, U-2

* **Primary RI**: RI-03 [Unobserved explanatory] — the cyclometallated intermediate (Fig. 1) is the central explanatory species for site-selectivity, substrate reactivity differences (runs 10 vs. 11), and the mechanism's plausibility, yet no direct observation (isolation, ³¹P{¹H} NMR, trapping) is reported.
* **Secondary RI**: RI-06 [Imported model] — the mechanistic cycle is supported by analogy with stoichiometric cyclometallation from Mn(I) electrophilic (ref 14) and Ru(II) carboxylate (ref 15) systems, which are mechanistically distinct from the proposed Ru(0) oxidative addition pathway; the isomorphism between these precedents and the paper's Ru(0) cycle is not demonstrated.
* **ER**: For the mechanistic rationale to reach VQ-3, the five-membered Ru metalacycle intermediate must be directly observed (stoichiometric synthesis, low-temperature ³¹P{¹H} NMR, or isotope-labelling consistent with its formation), and the Ru(II) pre-catalyst activation to the Ru(0) active species must be characterised (induction period, H₂ detection, or stoichiometric control experiment with a confirmed Ru(0) source).
* **EP**: EP-03a [Direct-observation / state-assignment pack]; EP-06a [Analogy-validation pack]
* **Case-specific implementation**: (a) EP-03a: synthesise the proposed five-membered Ru–C metalacycle stoichiometrically from acetophenone and RuH₂(CO)(PPh₃)₃ or from a confirmed Ru(0) source (e.g., Ru(cod)(cod)); characterise by ³¹P{¹H} NMR, ¹H NMR, and if crystalline, X-ray diffraction. (b) EP-03a (second application): measure induction periods and H₂ evolution upon mixing RuH₂(CO)(PPh₃)₃ with toluene at 135°C; test whether pre-formed Ru(0) sources (Ru₃(CO)₁₂ at higher temperature, or Ru(CO)₃(PPh₃)₂ under CO-free conditions) replicate the catalytic results of RuH₂(CO)(PPh₃)₃. (c) EP-06a: explicitly evaluate whether the Mn(I)/Ru(II) carboxylate cyclometallation precedents (refs 14, 15) establish isomorphism with Ru(0) OA, or whether they represent mechanistically distinct pathways that support only structural analogy, not mechanistic identity.
* **Notes**: U-1 (V2=critical, V3=critical, convergence 2/3) is the highest-severity item in Stage 1. U-2 (V2=high, V2-primary only) constitutes an independent mechanistic gap logically prior to U-1 in the proposed cycle. A-1 (the single mechanistic deferral sentence) simultaneously defers U-1 and U-2, concentrating the mechanistic uncertainty into one textual pivot. RI-06 co-occurrence with RI-03: resolving RI-06 (analogy validation) does not resolve RI-03 (direct observation); both must be addressed to reach VQ-3. GAP-3 (post-1993 mechanistic follow-up by Kakiuchi/Chatani group) is a type-3 external-inference gap that would retroactively address SRG-2 without the paper's own effort.

---

**SRG-3 [Selectivity basis absent]**
Member items: B-8, B-9, B-10, U-4

* **Primary RI**: RI-04 [Unreplicated discriminator] — the rate difference between run 10 (0.5 h, 100%) and run 11 (20 h, 88%) is used as the sole quantitative evidence for the ring-strain hypothesis, without rate constants, activation parameters, or time-resolved yield profiles; 1-indanone non-reactivity is invoked as corroborating evidence without characterising the conditions under which non-reactivity was established.
* **Secondary RI**: RI-05 [Qualitative overread] — "virtually 100%" regioselectivity is asserted for aromatics and all olefin runs on the basis of GC analysis without specifying the detection limit at which the three non-observed regioisomers are declared absent.
* **ER**: For the selectivity and kinetic claims to reach VQ-3 (qualified at minimum), rate-limiting step assignments for runs 10/11/1-indanone must be supported by initial-rate measurements or kinetic isotope effects (kH/kD with deuterated aromatic) under matched conditions, and "virtually 100%" regioselectivity must be reported with a stated GC detection limit against authentic standards of the non-observed regioisomers.
* **EP**: EP-04a [Discrimination / replication pack]; EP-05a [Quantitative-ranking substantiation pack]
* **Case-specific implementation**: (a) EP-04a: measure initial rates (yield vs. time at <20% conversion) for runs 10, 11, and 1-indanone under identical catalyst loading, temperature, and solvent; report rate constants k_obs and derive activation free energy ΔG‡ for each; test kH/kD for acetophenone-d₅ to confirm or exclude C–H cleavage as rate-determining step. (b) EP-05a: synthesise authentic samples of the three expected regioisomers (meta, para aromatic addition; Markovnikov olefin addition) and establish GC and ¹H NMR detection limits; re-run representative reactions (runs 8, 9, 13) with analytical confirmation of the absence of non-primary regioisomers at a stated threshold (e.g., ≤1%).
* **Notes**: B-8 and B-9 appear in TEMPERATURE_SUMMARY as high_convergence_low_gap (V1=medium, V2=high, convergence 2/3, gap=low). RI-04 applies to B-9 (1-indanone negative result) as an "incomplete negative evidence" pattern: non-reactivity is used as positive mechanistic evidence without specifying conditions for the test or mass balance. RI-05 for B-10/U-4 is non-fatal for the utility claim but fatal for the mechanistic claim that selectivity has a predictable structural origin. The co-occurrence of RI-04 and RI-05 means resolving only RI-04 (adding rate constants) would not resolve RI-05 (detection limit for minor regioisomers) — both must be addressed for VQ-3 (qualified).

---

**SRG-4 [Scope claims exceed data]**
Member items: B-5, U-3, B-7

* **Primary RI**: RI-07 [Unsupported boundary] — the abstract states "a variety of aromatic systems" can undergo C–H cleavage and the conclusion proposes chelation assistance "should be applicable more widely for selective organometallic catalysis," while the demonstrated substrate boundary (exclusively aromatic ketones, 13 runs, no non-ketone carbonyl, no amine/imine/pyridyl directing group tested) does not support the generalisation.
* **Secondary RI**: RI-08 [Unquantified reliability] — B-7's bilateral quantitative yield claim ("based on both starting materials") is not independently verified for olefin consumption; the excess olefin in runs 1–7 (4–6 equiv) is not accounted for, so the claim that olefin is quantitatively consumed is unverified.
* **ER**: For the scope claim to hold, Table 1 must include entries with at least one non-ketone directing group (aldehyde, ester, amide, or N-chelating group) and must demonstrate which substitution patterns are required for chelation competence, or must explicitly delimit the demonstrated scope as "aromatic ketones only" in the abstract-level claim.
* **EP**: EP-07a [Boundary-test pack]; EP-08a [Replication / uncertainty pack]
* **Case-specific implementation**: (a) EP-07a: test at minimum aryl aldehyde (ArCHO, no α-methyl block), aryl ester (ArCO₂R), aryl amide (ArCONR₂), and 2-arylpyridine as directing-group variants under the standard conditions (2 mol% Ru, toluene, 135°C) with triethoxyvinylsilane as the olefin; report yields or non-reactivity with characterisation of recovered starting materials. (b) EP-08a: for bilateral quantitative yield claims (runs 8–13), independently monitor olefin conversion by ¹H NMR aliquots or GC headspace analysis; report olefin mass balance accounting for potential isomerization, hydrosilylation, or oligomerization products.
* **Notes**: U-3 and B-5 are complementary Stage 1 classifications of the same structural gap — U-3 at the abstract-level self-contradictory absence (high severity), B-5 as a mixed (intentional-narrowing + methodological-limitation) flagged item. B-7 connects SRG-4 to SRG-1 (common root: efficiency claim without mass balance) but is placed in SRG-4 because the specific unverified claim is "based on both starting materials," which is a scope statement about olefin consumption, not a calibration issue. RI-07 here applies to a positive generalisation boundary ("applicable more widely"), not a negative boundary claim — consistent with the extended use note in v0.2a.

---

**SRG-5 [Prior art not engaged numerically]**
Member items: C-1, B-2

* **Primary RI**: RI-09 [External superiority] — superiority over refs 11 (Jordan & Taylor) and 12 (Moore et al.) is asserted by qualitative limitation statements only; no direct yield, TON, or TOF comparison on shared or analogous substrates appears in the paper, and the paper's own TOF claim for runs 1/9/10 is stated without numerical values.
* **ER**: For the "highest reported TOF" claim to be independently verifiable, the paper must report its own TOF values (mol product per mol Ru per h) alongside the reported values from refs 11 and 12 under the original conditions, explicitly noting substrate-class differences that prevent direct comparison.
* **EP**: EP-09a [Internal benchmark pack]
* **Case-specific implementation**: Compile TOF values from refs 11 and 12 from the original papers using the same unit system; report TOF for runs 1, 9, 10 from time and conversion data under the Table 1 conditions; present in a summary table acknowledging that the substrate classes differ (α-picoline/propene for ref 11; pyridine/CO/1-hexene for ref 12; aromatic ketones/vinylsilane for this work) and that direct comparison is therefore partially substrate-class-dependent.
* **Notes**: SRG-5 partially overlaps SRG-1 (B-2 is member of SRG-1 in Stage 1 META). Both SRGs are anchored to the same absence (TOF values not reported), but SRG-5 is specifically about the cross-system comparison whereas SRG-1 covers the broader quantitative evidence base including GC calibration and mass balance. GAP-1 (retrieve refs 11/12 for numerical comparison) is the Stage 1 type-1 retrieval gap that directly addresses SRG-5. Placed as a separate SRG because it has its own RI-09 primary code distinct from SRG-1's primary RI-01.

---

**Outside the SRGs: CLAs**

**CLA-1: Ru(II) → Ru(0) activation mechanism (self-contradictory absence)**

* **Primary RI**: RI-03 [Unobserved explanatory] — The proposed catalytic cycle begins with Ru(0) oxidative addition, but the pre-catalyst is formally Ru(II) (RuH₂(CO)(PPh₃)₃, d⁶); the species the paper's own cycle predicts must exist (the Ru(0) active form) is neither detected nor characterised. The paper's only indirect evidence is that Ru₃(CO)₁₂ — which is already Ru(0) — "was not effective," which could be explained by ligand-sphere differences rather than by a uniform role of Ru(0) as the active state.
* **ER**: The paper's catalytic cycle requires Ru(0) as the entry point for OA; for this to be mechanistically consistent, the activation of RuH₂(CO)(PPh₃)₃ to a Ru(0) species must be demonstrated (H₂ reductive elimination, induction period characterisation, or equivalence test with a confirmed Ru(0) source).
* **EP**: EP-03a [Direct-observation / state-assignment pack]
* **Case-specific implementation**: Monitor the reaction of RuH₂(CO)(PPh₃)₃ with toluene at 135°C by ³¹P{¹H} NMR and measure any H₂ evolution; test Ru(CO)₂(PPh₃)₂ (a confirmed Ru(0) tetrakis-CO species) and authentic Ru(0) complexes as catalysts to determine whether Ru(0) entry into the cycle is uniquely required; measure induction periods for run 1 and run 9 conditions.
* **Notes**: U-2 in Stage 1 carries high severity (V2=high; V2-primary). Classified as CLA because U-2's grounded_in items (U-2, A-1) are already members of SRG-2; however, the Ru(II)→Ru(0) activation question is a logically distinct sub-question from U-1 (intermediate identity), warranting explicit CLA designation so the EP-03a investment is separately tracked. This is a self-contradictory absence: the cycle predicts a Ru(0) active species must be generated, but its generation is neither demonstrated nor modelled.

**CLA-2: Catalyst lifecycle and olefin selectivity**

* **Primary RI**: RI-07 [Unsupported boundary] — the paper claims "practical organic synthesis" utility and "among the highest TOF" but provides no catalyst recovery, reuse, or deactivation data; the claim that the catalyst is reusable (implied by "synthetic reaction" framing) is unsupported by boundary-testing experiments.
* **Secondary RI**: RI-08 [Unquantified reliability] — no reaction profiles (yield vs. time) are provided for any run, and the fate of excess olefin in runs 1–7 is uncharacterised; both limitations make it impossible to assess whether the catalyst deactivates during the reaction and whether the efficiency claim rests on genuine TOF or on a single-turnover burst.
* **ER**: For "practical synthetic utility" to hold independently of the substrate scope claim, at minimum one run must demonstrate catalyst recovery and a second addition of substrates with retained activity (or acceptable deactivation) and one run must confirm that excess olefin does not generate more than trace by-products.
* **EP**: EP-07a [Boundary-test pack]; EP-08a [Replication / uncertainty pack]
* **Case-specific implementation**: After run 9 (0.5 h, 100%), filter and concentrate the catalyst residue; add a second batch of substrate and repeat under the same conditions; report yield of the second batch. Independently: collect GC aliquots from run 1 at 0.05 h, 0.1 h, 0.2 h to construct a time-profile; check for trimethylsilylethylene isomerization and hydrosilylation by-products.
* **Notes**: D-4-7 in Stage 2 is the grounded candidate; its grounded_in items (B-2, B-7, B-6) are not uniquely captured in any single SRG. B-6 (discontinuous 6 mol% loading for runs 5–6) is an additional sub-item: its unexplained divergence from the standard 2 mol% loading for runs 5 and 6 is consistent with the catalyst lifecycle question — if the TOF were lower for allylsilane substrates, a higher loading would be needed to reach acceptable yield in acceptable time.

---

### §3 Current VQ assessment

**Current judgment: VQ-2 (qualified)**

**VQ-1 [Observation] — Pass (non-fatal)**

RI-02 (object identification): the 13 product structures are certified by "standard methods,[REDACTED: substantial verbatim quotation; see Tier 9]standard methods" certification would have been accepted within the 1993 Nature Articles genre. VQ-1 holds on a non-fatal reading of RI-02.

**VQ-2 [Method] — Qualified**

Inheriting VQ-1 (non-fatal RI-02). RI-01 (reporting integrity): SRG-1 and SRG-5 together constitute an unresolved RI-01 / RI-09 pair. The GC yield measurement system is not specified (no internal standard, no response factors, no calibration curve), isolated yields are absent for 10 of 13 runs, and actual TOF values are not reported. The bilateral quantitative yield claim (B-7) cannot be independently verified. RI-07 in SRG-4 contributes an additional VQ-2 failure: the abstract scope claim ("a variety of aromatic systems") extends beyond the demonstrated substrate boundary without boundary-test data, making the method's applicable domain formally undefined.

VQ-2 is qualified rather than failed outright because: (a) GC quantification of well-precedented aromatic coupling products in toluene is unlikely to be systematically unreliable at the ~10% level in the 1993 era; (b) the bilateral yield claim is mechanistically plausible (both C–H and olefin are consumed in the coupling); (c) a VQ-2 pass would require EP-01a implementation and EP-09a for the TOF comparison.

**VQ-3 [Mechanism] — Fail**

Inheriting VQ-2 (qualified). RI-03: neither the cyclometallated intermediate (U-1) nor the Ru(0) active species (CLA-1/U-2) is directly observed. RI-06: the mechanistic analogies invoked (refs 14/15, Mn(I)/Ru(II) carboxylate cyclometallation; ref 17, acrylic ester OA) are from distinct oxidation-state and substrate contexts, and the isomorphism is not demonstrated. RI-04: the rate difference between runs 10 and 11 is interpreted as ring-strain evidence without rate constants, and the 1-indanone negative result is deployed as mechanistic evidence without specifying detection conditions (B-9). RI-05 (SRG-3): regioselectivity "virtually 100%" lacks a stated detection limit.

VQ-3 fails on RI-03 (fatal: the paper's own cycle predicts the intermediate must exist but neither observes nor constrains it), RI-06 (fatal: the only mechanistic support is imported from distinct systems), RI-04/RI-05 (non-fatal for the utility claim, fatal for the mechanistic claim). The mechanistic layer is entirely analogy-supported speculation, consistent with the paper's own declaration ([REDACTED: substantial verbatim quotation; see Tier 9]).

**VQ-4 [Benchmark] — Fail**

Inheriting VQ-3. RI-08 (SRG-3 and CLA-2): no replicate measurements are reported for any run; all data are single-point GC yields. RI-09 (SRG-5): external superiority over refs 11/12 is asserted qualitatively without numerical cross-system comparison. Both RI-08 and RI-09 remain unresolved.

**Layered VQ asymmetry:**

However, the **synthetic utility layer** (NC-1/NC-2, runs 8–13, bilateral quantitative yield claims) on its own reaches approximately VQ-2 (qualified): if EP-01a were applied (calibrated GC, mass balance), these runs would provide a method-level record of practical efficiency independently of the mechanism. The utility layer does not require VQ-3 mechanistic resolution to stand.

The **mechanistic layer** (SRG-2, NC-3) currently rests at below VQ-1 in isolation: neither the intermediate nor the active species is directly observed, so even the observation-level claim for the mechanism cannot be established from the paper's data alone.

The **scope-claim layer** (SRG-4, NC-4, U-3) is the most fragile: if EP-07a revealed that non-ketone directing groups do not support the reaction, the abstract-level generalisation would be false, not merely unconfirmed.

---

### §4 Era-Norm Annotation

**communication-era tolerated:**

- **B-1** (GC yield without internal standard; isolated yields absent for 10/13 runs): 1993 Nature Articles accepted GC yield as the primary analytical record in synthetic communications of this scale; isolated yields for all runs were a later expectation. Tolerated within 3-page format and field norm.
- **B-2** (TOF claim without numerical TOF values): comparative TOF claims stated as qualitative assessments in short communications were standard; authors routinely deferred quantitative TOF tables to full-paper follow-ups. Tolerated within 3-page format.
- **B-3** (catalyst structure–activity comparison without quantitative data): brief qualitative catalyst comparisons were acceptable in Nature Articles short communications; individual catalyst optimisation data were expected in full papers. Tolerated within format.
- **B-4** ("standard methods[REDACTED: substantial verbatim quotation; see Tier 9]standard methods" was an accepted certification formula covering ¹H NMR and elemental analysis (or HRMS). Tolerated by 1993 journal norm.
- **A-1** (explicit mechanistic deferral): the acknowledgment that "the mechanism is not yet clear" is itself a communication-era norm — Nature Articles from this period routinely reported synthetic discoveries before mechanistic understanding was complete, with mechanistic papers following separately. Tolerated.
- **B-6** (anomalous 6 mol% catalyst loading for runs 5–6 without rationale): in short communications, condition variations without explanatory discussion were tolerated when the reaction outcomes (yield, time) were reported; the rationale was expected in a full paper. Tolerated within format.

**modern-era deficient:**

- **B-1** (GC yield without internal standard): modern synthetic communications require an internal standard (e.g., hexamethyldisiloxane, decane), explicit response factors, or isolated yields for all scope entries; absence of any calibration basis for GC yields is now insufficient for a yield claim of "almost quantitative."
- **B-2 / C-1** (TOF without numerical values; no numerical cross-system comparison): modern catalysis papers require numerical TOF values with defined time, conversion, and catalyst speciation; qualitative "highest reported" claims without supporting data in the same paper are no longer acceptable as a primary claim.
- **B-7** (bilateral quantitative yield without olefin mass balance): modern standards require mass balance closure, including the fate of excess olefin; a claim of "based on both starting materials" requires documented olefin conversion, particularly given the potential for competing isomerization and hydrosilylation reactions with Ru hydride catalysts.
- **U-1 / B-11** (cyclometallated intermediate postulated but unobserved): while era-tolerated in 1993 communication format, modern mechanistic standards require at minimum a DFT-computed energy profile for the proposed cycle, or a trapping/labelling experiment consistent with intermediate formation; an uncharacterised proposed intermediate is not acceptable as the primary mechanistic explanation in a re-submission context.
- **U-3 / B-5** (abstract scope claim broader than demonstrated data): modern journals require that abstract scope claims match the substrate boundary demonstrated in the data; "a variety of aromatic systems" would now require boundary examples or explicit qualification as "aromatic ketone systems."
- **B-9** (1-indanone non-reactivity as mechanistic evidence without conditions): modern reporting requires that negative results used as positive mechanistic evidence include the specific conditions (substrate concentration, catalyst loading, reaction time, analytical detection limit) under which non-reactivity was established.

**Dual classification (tolerated then, deficient now):**

- **B-1, B-2, B-4, A-1**: each was tolerated within the 3-page Nature Articles communication format of 1993 and the prevailing field norm (priority-of-observation reporting) but would be deficient in a modern re-certification context (e.g., a contemporary re-examination or republication of the result).

---

### §5 Shortest-reinforcement route

**Objective function 1: VQ-2 (Method) — full pass (remove "qualified" status)**

Current status: VQ-2 qualified due to RI-01 (GC calibration absent) and RI-07 (abstract scope claim not bounded by data).

**Shortest route to VQ-2 (full pass):**

1. **EP-01a [Reporting-coherence pack]** — Re-run Table 1 with a specified GC internal standard (mesitylene or decane at defined concentration); report response factors for the product class; provide isolated yields for all 13 runs; report olefin mass balance for runs 8–13 (the bilateral quantitative yield runs). Advances RI-01 directly, removing the calibration gap from B-1 and B-7.

2. **EP-09a [Internal benchmark pack]** — Report actual TOF values (mol product per mol Ru per hour) for runs 1, 9, 10 at the conditions stated in Table 1; extract corresponding values from refs 11 and 12 and present in a comparative table with an explicit note on substrate-class non-comparability. Advances RI-09 (SRG-5), removing the external superiority assertion.

3. **EP-07a [Boundary-test pack] — scope qualification only** — Qualify the abstract claim as "aromatic ketone systems" and test at minimum one non-ketone carbonyl directing group (aryl aldehyde, aryl ester) under standard conditions; report outcome (reactive or unreactive). This removes the RI-07 "unsupported boundary" status for the scope generalisation. Advances SRG-4.

Certification-gate note: The experimental investment order follows information gain (EP-01a addresses the largest number of affected items simultaneously: B-1, B-7, C-1 partially), but the final VQ-2 certification requires all three gates — RI-01, RI-09, and RI-07 — to be resolved according to the inheritance principle VQ-1 → VQ-2.

---

**Objective function 2: VQ-3 (Mechanism) — requires VQ-2 as prerequisite**

**Shortest route to VQ-3:**

1. **EP-03a [Direct-observation / state-assignment pack] — intermediate characterisation** — Stoichiometrically synthesise the proposed five-membered Ru–C metalacycle from acetophenone and a confirmed Ru(0) complex; characterise by ³¹P{¹H} NMR and ¹H NMR (and X-ray if crystalline); confirm it competently re-enters the catalytic cycle. Advances RI-03 (SRG-2, U-1). This is the highest-priority step because U-1 is the highest-severity item (V2=critical, V3=critical).

2. **EP-03a [Direct-observation / state-assignment pack] — Ru(0) activation** — Characterise the induction period and H₂ evolution for RuH₂(CO)(PPh₃)₃ activation under the catalytic conditions; test Ru(0)-source alternatives (Ru(CO)₂(PPh₃)₂, Ru(CO)₃(PPh₃)₂ at elevated temperature) as pre-catalysts. Advances RI-03 (CLA-1/U-2), resolving the Ru(II)→Ru(0) activation question independently of intermediate characterisation.

3. **EP-06a [Analogy-validation pack]** — Explicitly test the mechanistic isomorphism of the Mn(I)/Ru(II) cyclometallation precedents (refs 14/15) with the proposed Ru(0) OA cycle by attempting to form the proposed intermediate from the Mn and Ru(II) conditions and comparing spectral signatures; or explicitly derive a rate law from the proposed cycle and compare with observed concentration dependences. Advances RI-06 (SRG-2, C-2/B-11).

4. **EP-04a [Discrimination / replication pack]** — Measure initial rates for runs 10, 11, and 1-indanone under matched conditions; report k_obs and ΔG‡; measure kH/kD (deuterated aromatic) to determine whether C–H cleavage is rate-limiting. Advances RI-04 (SRG-3/B-8/B-9), converting the rate attribution to a data-supported assignment.

5. **EP-05a [Quantitative-ranking substantiation pack]** — Synthesise authentic samples of three non-observed regioisomers; establish GC detection limit; confirm "virtually 100%" selectivity with a stated threshold (≤1%). Advances RI-05 (SRG-3/B-10/U-4), converting a qualified selectivity claim to a quantified one.

Certification-gate note: The experimental investment order follows information gain (EP-03a addresses the largest number of mechanistic RIs and the highest-severity items), but the final VQ-3 certification is fixed by the gate order VQ-1 → VQ-2 → VQ-3 under the inheritance principle, and VQ-3 additionally requires RI-04 and RI-05 to be resolved at non-fatal level for the (qualified) designation.

---

### §6 Contribution to institutional design

**1. New representative case for RI-03 — Labeling mismatch pattern:**

This paper provides a textbook case of the [REDACTED: verbatim source quotation; see the source paper via its DOI] [REDACTED: substantial verbatim quotation; see Tier 9] and [REDACTED: substantial verbatim quotation; see Tier 9] The hypothesis label is concentrated in the first sentence of the Possible Mechanisms section; all subsequent sentences use indicative mood and active voice as if describing confirmed steps. This creates a labeling mismatch: the single hedging sentence permits the remainder of the mechanism to be presented factually. This pattern co-occurs with RI-06 (imported model from Mn/Ru carboxylate precedents used as if confirming Ru(0) OA) and should be recorded as a characteristic co-occurrence: labeling mismatch + RI-06 import + RI-03 unobserved intermediate.

**2. Automatic-resolution pattern via Communication → Full Paper transition:**

Several VQ-2 deficiencies in this paper (B-1, B-2, B-3, B-4) are characteristic of the automatic-resolution pattern: they arise directly from the 3-page Nature Articles page limit and would be expected to resolve in a full-paper follow-up (full analytical data, reaction profiles, TOF values). This is consistent with §4's communication-era tolerated classification for the same items. The pattern is not novel (confirmed in prior cases), but the density of auto-resolvable items here is exceptionally high — 4 of 11 B items are of this type — providing a new high-density example for the Codebook.

**3. Incomplete negative evidence (RI-04 application):**

B-9 provides a clean case of the "incomplete negative evidence" pattern flagged in v0.2a: the non-reactivity of 1-indanone is explicitly deployed as positive mechanistic evidence ("the importance of chelation is further demonstrated by...") without specifying the conditions (substrate concentration, catalyst amount, time, detection limit) under which non-reactivity was established. The phrase "did not react at all" implies a conclusive test, but "not shown[REDACTED: substantial verbatim quotation; see Tier 9]negative experimental results used as positive mechanistic evidence without mass-balance closure or kinetic-window evaluation.[REDACTED: substantial verbatim quotation; see Tier 9]negative result cited as structural evidence without detection-limit specification" example.

**4. RI co-occurrence: RI-03 + RI-06 structural coupling in SRG-2:**

In SRG-2, RI-03 (unobserved intermediate) and RI-06 (imported model) are structurally coupled: the reason the intermediate is not characterised is precisely that the authors rely on the imported model (refs 14/15) as surrogate evidence for its existence. Resolving RI-06 alone (showing the imported model is isomorphic) would not resolve RI-03 (the intermediate is still unobserved in the target system); resolving RI-03 alone (characterising the intermediate) would make RI-06 evidence redundant. This coupling means the EP-06a investment (analogy validation) should be sequenced only after EP-03a (direct observation) — if EP-03a succeeds, EP-06a becomes a corroborating rather than primary investment. This sequencing insight should be added to the EP dictionary as a co-occurrence handling note for RI-03+RI-06 pairs.

**5. PRI-10 provisional confirmation (Kinetic overclaim):**

The TOF superlative claim in B-2 ("among the highest reported for this type of reaction") without actual TOF values is structurally identical to the PRI-10 definition (provisional): "an absolute rate enhancement is claimed without kinetic data." This paper provides a second independent case in which an absolute TOF ranking is asserted without reported TOF values or rate measurements (the first confirmation was Monnereau 2009). If the Murai 1993 case is accepted as an independent isomorphic instance, PRI-10 satisfies the two-paper promotion criterion and should be promoted from provisional to established RI status. Recommended: formally note Murai 1993 as PRI-10 confirmation case #2 in the next Codebook update.

**6. No new PRI candidate identified:**

No pattern was detected in this case that requires a new provisional RI code beyond those already in the Codebook or under provisional status.

---

> **Tier 8 redaction notice**: This file is a redacted copy of the corresponding Tier 3 / Tier 9 output. Verbatim source-paper quotations have been replaced by `[REDACTED: see source paper §<loc>; full text retained in Tier 9 reviewer-only deposit]` markers, preserving location references and our own analytical content. Bibliographic fields (title, authors, journal, year, DOI), analytical labels (`evidence_chain:` with B-/U-/A-/C- internal IDs), short technical terms, and our own analytical text are not redacted. The redaction was applied by `scripts/redact_for_tier8.py` and, for this version, by `scripts/build_paperA_R1_public.py` with `scripts/redact_source_ngram_runs.py` (scripts of the project repository; they are not deposited).
