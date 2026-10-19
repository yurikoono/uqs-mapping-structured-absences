prompt_version: stage3-v2-en-20260419
model_info: claude-sonnet-4-6

# Re-certification Assessment Sheet for Scientific Knowledge

## Murai et al. 1993 (Nature, communication)

---

### §1 Claim Architecture

**Core claim summary:**

The paper's core claim has two pillars. The **Novelty pillar** is that RuH₂(CO)(PPh₃)₃ catalyzes the addition of aromatic C–H bonds (ortho to a ketone directing group) to olefins with efficiency, selectivity, and substrate generality never previously demonstrated in catalytic C–H functionalization. The **Utility pillar** is that this reaction meets the threshold required for "practical organic synthesis," as operationalized through three independently stated performance criteria: bilateral quantitative yield (N-2), TOF "among the highest reported" (N-3), and "virtually 100%" regioselectivity (N-5). The mechanistic principle—chelation assistance positioning low-valent Ru for ortho-selective C–H cleavage (N-6)—is claimed both as the explanation for the observed performance and as a transferable strategy for broader selective organometallic catalysis (N-7).

**Layered structure judgment:**

Yes, independent layers exist. The paper organizes its novelty across four structurally separable axes: (i) efficiency (N-1, N-2, N-3), (ii) substrate generality (N-4), (iii) regioselectivity (N-5), and (iv) the chelation-assistance mechanistic principle (N-6, N-7). A refutation of any single layer does not collapse the others: for instance, if the TOF values were shown to be uncompetitive with refs 11–12 (challenging efficiency), the scope and selectivity claims would remain independently standing. The mechanistic principle layer (N-6/N-7) is the most expansive claim and the one with the thinnest evidentiary support; its collapse would weaken the interpretive framing of all other layers but would not falsify the empirical yield or selectivity data. The dependency structure runs: empirical claims (layers i–iii) are mutually independent; the mechanistic layer (iv) is dependent on all three empirical layers for its warrant but does not logically underpin them. A single refutation does not collapse all claims. However, the mechanistic and empirical layers are jointly undergrounded: the efficiency claims (layer i) lack quantitative verification, and the mechanism (layer iv) lacks any direct experimental support, such that both poles of the paper's argument are simultaneously fragile.

---

### §2 SRG / CLA → RI / ER / EP Crosswalk

**SRG-1 [Quantitative evidence base]** (members: B-1, B-2, B-3, B-4)

* **Primary RI**: RI-01 [Reporting integrity]
* **Secondary RI**: RI-08 [Unquantified reliability]
* **ER**: For the efficiency and TOF claims to be independently verifiable, the paper must report: GC calibration method (internal standard and response factors), actual TOF values for runs 1, 9, 10 alongside literature comparators, quantitative yield data for the alternative catalyst experiments (B-3), and the specific characterization data ("standard methods") for all 13 novel products.
* **EP**: EP-01a [Reporting-coherence pack]; EP-08a [Replication / uncertainty pack]
* **Case-specific implementation**: (EP-01a) For the Ru-catalyzed aromatic C–H/olefin coupling system, reporting coherence requires: (a) stating the GC internal standard (e.g., dodecane or hexadecane) and response factors used to convert GC peak areas to molar yields for all 13 runs; (b) reporting actual TOF values (mol product mol⁻¹ Ru h⁻¹) for runs 1, 9, and 10 at defined time points; (c) specifying what "standard methods" means for the novel silylated alkylbenzene products (minimum: ¹H NMR, ¹³C NMR, and HRMS or elemental analysis). (EP-08a) For runs 5 and 6 (elevated catalyst loading, 0.12 mmol vs. standard 0.04 mmol), duplicate runs at standard and elevated loading are needed to establish whether the threefold loading difference is required for these allylsilane/vinylsilane substrates, and whether the isolated yield for runs 5 and 6 (GC yield only: 100% and 96%) can be reproduced.
* **Notes**: B-1 (V1=high, V3=high; high_convergence_low_gap; gap: none). B-2 (V1=high, V3=high; high_convergence_low_gap; gap: none). B-3 (V1=medium, V2=medium, V3=medium; highest convergence 3/3; high_convergence_low_gap; gap: none). B-4 not in TEMPERATURE_SUMMARY but directly linked to B-1/B-2 via SRG-1. The convergence of B-1, B-2, B-3 across all three agents (synthetic, mechanistic, analytical) with no inter-agent gap signals that the evidence-base deficiency is field-uniformly recognized rather than perspective-dependent.

---

**SRG-2 [Catalytic cycle evidence absent]** (members: A-1, U-1, U-2)

* **Primary RI**: RI-03 [Unobserved explanatory]
* **Secondary RI**: RI-06 [Imported model]
* **ER**: For the mechanistic claim to hold—that chelation-assisted coordination of Ru(0) to the carbonyl followed by oxidative addition to the ortho C–H bond is the operative pathway—the paper must provide direct evidence for at least one elementary step in the proposed cycle: either (a) stoichiometric isolation or spectroscopic observation (³¹P{¹H} NMR, X-ray) of the cyclometallated intermediate, or (b) evidence that the formally Ru(II) pre-catalyst generates a Ru(0) active species under reaction conditions (e.g., H₂ evolution, induction period, ³¹P NMR monitoring during reaction initiation).
* **EP**: EP-03a [Direct-observation / state-assignment pack]; EP-06a [Analogy-validation pack]
* **Case-specific implementation**: (EP-03a) For the Ru/aromatic ketone system: treat a stoichiometric mixture of RuH₂(CO)(PPh₃)₃ with acetophenone (1:1) in toluene at 135 °C under inert atmosphere; monitor by ³¹P{¹H} NMR for formation of a new Ru complex; if the cyclometallated intermediate forms, confirm by ¹H NMR (ortho H disappearance, Ru–H signal) and, if crystalline, by X-ray diffraction. If Ru(0) formation is the rate-limiting activation step, monitor H₂ evolution by head-space GC or by manometry during the induction period. (EP-06a) For the mechanistic analogy citations (refs 14, 15, 17): explicitly compare the oxidation state and ligand set of the Mn(I) and Ru(II) stoichiometric cyclometallation products (refs 14, 15) with the proposed Ru(0) OA intermediate; if the analogy is oxidation-state-level, obtain or cite a Ru(0) cyclometallation precedent with an aryl ketone directing group to replace the mechanistically distinct Mn(I)/Ru(II) systems.
* **Notes**: U-1 (V2=critical, V3=critical; high_convergence_low_gap; gap: none) — classified as self-contradictory absence: the proposed cycle mandates the intermediate as the selectivity-determining species, yet no direct experimental evidence for it is provided. U-2 (high, V2 only; low_convergence_high_gap) — internally self-contradictory: the cycle requires Ru(0), the pre-catalyst is Ru(II), and the genuine Ru(0) source (Ru₃(CO)₁₂) is stated to be "not effective[REDACTED: substantial verbatim quotation; see Tier 9]not yet clear") is the single explicit acknowledgment of the mechanistic gap. The RI-06 secondary assignment arises because refs 14–15 are mechanistically distinct systems (Mn(I) electrophilic and Ru(II) carboxylate) imported to support a Ru(0) OA claim without demonstrating isomorphism (C-2, B-11).

---

**SRG-3 [Selectivity basis absent]** (members: B-8, B-9, B-10, U-4)

* **Primary RI**: RI-04 [Unreplicated discriminator]
* **Secondary RI**: RI-05 [Qualitative overread]
* **ER**: For the chelation-based mechanistic account of ortho-selectivity and the ring-strain hypothesis to be analytically supported, the paper must provide: (a) rate constants or activation parameters (or at minimum time-resolved yield profiles) for runs 10 and 11 at the same catalyst loading, allowing numerical quantification of the rate difference; (b) a detection-limit basis for the claim that 1-indanone "did not react at all"; (c) quantitative specification of the detection limit for non-observed regioisomers in runs 8 and 13 (the "virtually 100%" claim).
* **EP**: EP-04a [Discrimination / replication pack]; EP-05a [Quantitative-ranking substantiation pack]
* **Case-specific implementation**: (EP-04a) For the run 10 / run 11 rate comparison: perform time-resolved GC aliquot experiments for both runs under identical conditions (same catalyst loading; compare with 0.04 mmol for both, not the mixed-loading dataset in Table 1); obtain pseudo-first-order rate constants k_obs for the two substrates; compute the rate ratio with uncertainty. For the 1-indanone negative result: run a parallel experiment with 1-indanone under standard conditions for 24 h; determine the GC detection limit for the expected product (estimated by spiking a synthetic standard or by analogy with run 11 product); report as "< X% yield at 24 h." (EP-05a) For the "virtually 100%" regioselectivity claim: spike the crude reaction mixture with authentic regioisomeric standards (or with a model compound expected to co-elute with any minor regioisomer); establish GC resolution and detection limits at ≥ 0.5% level; report the quantitative lower bound on regioselectivity.
* **Notes**: B-8 (V1=medium, V2=high; high_convergence_low_gap; gap: low). B-9 (V1=medium, V2=high; high_convergence_low_gap; gap: low). The gap:low annotation indicates that V1 and V2 assess the severity differently (medium vs. high), but both flag the same mechanistic attribution problem. The "not shown" qualifier in B-9 is structurally notable: data exist but are withheld, yet the negative result is used as the strongest kinetic evidence in the Possible Mechanisms section. RI-05 secondary assignment: the rate ordering (run 10 faster than run 11; 1-indanone unreactive) is derived from a qualitative ranking without numerical rate support.

---

**SRG-4 [Scope claims exceed data]** (members: B-5, U-3, B-7)

* **Primary RI**: RI-07 [Unsupported boundary]
* **Secondary RI**: RI-05 [Qualitative overread]
* **ER**: For the abstract claim "a variety of aromatic systems" to be supported by the data, the paper must either qualify the claim to "aromatic ketone systems" or provide at least one demonstration run with a non-ketone directing group (aldehyde, ester, amide, imine, or N-heterocycle). For the "almost quantitative yields based on both starting materials" claim (runs 8–13), the paper must report olefin mass balance (fate of excess olefin as isomerization, oligomerization, or hydrosilylation products) to confirm that the olefin is consumed stoichiometrically in the desired reaction.
* **EP**: EP-07a [Boundary-test pack]; EP-05a [Quantitative-ranking substantiation pack]
* **Case-specific implementation**: (EP-07a) Boundary test for directing-group scope: run the reaction with benzaldehyde (aldehyde directing group) and with N,N-dimethylbenzamide (amide directing group) under the standard conditions (2 mmol substrate, 2–10 mmol vinyltriethoxysilane, 0.04 mmol RuH₂(CO)(PPh₃)₃, toluene, 135 °C); report yield and regioselectivity, or explicitly state that these substrates gave ≤X% yield under the stated detection limits, thereby bounding the scope claim to aromatic ketones. (EP-05a) For the bilateral quantitative yield claim: for representative runs 8–13, quantify the olefin consumption by GC with the same internal standard used for the product, and report the olefin mass balance. For vinyltriethoxysilane-based runs specifically (runs 1–2, 8–13), report whether oligomeric or hydrosilylated by-products are detected.
* **Notes**: U-3 is a self-contradictory absence: the abstract-level scope language ("variety of aromatic systems") is not qualified as "aromatic ketone systems" despite all 13 runs being ketone-only. B-5 records the same observation as a mixed B-item (intentional narrowing + methodological limitation), indicating the authors made a deliberate framing choice that outpaces the demonstrated data. B-7 is the olefin-fate component: bilateral quantitative yield implies olefin quantitative consumption, which is not reported. These three items share the root that the scope and efficiency framing language systematically exceeds what the experimental data demonstrates.

---

**SRG-5 [Prior art not engaged numerically]** (members: C-1, B-2)

* **Primary RI**: RI-09 [External superiority]
* **Secondary RI**: RI-01 [Reporting integrity]
* **ER**: For the comparative efficiency claim ("TOF among the highest reported," "this has never been attained before") to be independently verifiable, the paper must report the actual TOF values for runs 1, 9, and 10 alongside the corresponding values from refs 11–12 under comparable conditions, or on a common substrate with a side-by-side experiment.
* **EP**: EP-09a [Internal benchmark pack]; EP-01a [Reporting-coherence pack]
* **Case-specific implementation**: (EP-09a) Report the TOF (mol product mol⁻¹ Ru h⁻¹) for runs 1, 9, and 10 calculated from the stated reaction times and molar quantities (2 mmol ketone, 0.04 mmol Ru); e.g., run 9: 2 mmol product / 0.04 mmol Ru / 0.5 h = 100 h⁻¹ as an apparent TOF (assuming complete conversion). For the comparative claim, extract TOF from refs 11 and 12 under their stated conditions and tabulate alongside. If the reactions use incompatible substrates (α-picoline/propene vs. aromatic ketone/vinylsilane), state the substrate class boundary explicitly and limit the comparative claim to "for aromatic ketone C–H functionalization" rather than "for this type of reaction" (which implies a broader comparison class). (EP-01a) Report the denominator used to define the molar ratio in the TOF: total Ru or estimated fraction of Ru active at the given temperature.
* **Notes**: B-2 (V1=high, V3=high; high_convergence_low_gap; gap: none). C-1 records the Dropped Quantitative Benchmark as the missing side of the comparison: neither the paper's own TOF values nor the reference-side values are tabulated. The two items are structurally complementary: B-2 is the absence of the paper's own metric; C-1 is the absence of the comparator metric. Together they make the efficiency comparison unverifiable from within the paper.

---

**Outside the SRGs: CLAs**

**CLA-1: Mechanistic analogy validity (B-11, C-2, C-5)**

* **Primary RI**: RI-06 [Imported model]
* **Secondary RI**: RI-03 [Unobserved explanatory]
* **ER**: For the mechanistic citations (refs 14, 15, 17) to support the proposed Ru(0) OA → cyclometallation → olefin insertion → reductive elimination cycle, the paper must demonstrate (or cite) isomorphism between the imported systems and the proposed mechanism: specifically, that Mn(I) electrophilic cyclometallation (ref. 14) and Ru(II) carboxylate cyclometallation (ref. 15) give structurally and electronically equivalent intermediates to those expected from Ru(0) OA, and that acrylic ester OA to Ru (ref. 17) is mechanistically analogous to aromatic C–H OA.
* **EP**: EP-06a [Analogy-validation pack]; EP-03a [Direct-observation / state-assignment pack]
* **Case-specific implementation**: (EP-06a) Explicit oxidation-state and electron-count analysis of the cited precedent intermediates (refs 14, 15) vs. the proposed Ru intermediate: refs 14–15 produce Ru(II) and Mn(I) metallacyclic species respectively, while the proposed cycle requires Ru(II) from Ru(0) OA. If the product stoichiometry is the same but the oxidation pathway differs, this must be acknowledged. A Ru(0) cyclometallation precedent with an aryl ketone (e.g., from Ru₃(CO)₁₂ + ketone under UV) or an explicit DFT energy profile for the OA step would replace the mechanistically distinct analogies. (EP-03a) RI-03 subtype "available-but-unutilized characterization" applies here in the reverse: the paper cites existing stoichiometric products that could be compared crystallographically with the proposed intermediate, but does not perform this comparison.
* **Notes**: This CLA is not captured in any existing SRG. It bridges SRG-2 (catalytic cycle evidence absent) at the mechanistic level and adds a structurally specific RI-06 claim: the import of Mn(I)/Ru(II) cycle-level analogies to support a Ru(0) OA claim is an instance of cycle-level model import without isomorphism demonstration (per RI-06 scope note, cycle-level import applies). The co-occurrence of RI-06 and RI-03 in this CLA means resolving only one is insufficient (see §6 for RI co-occurrence pattern).

**CLA-2: Catalyst activation pathway — Ru(II) to Ru(0) (U-2, B-3, A-1) [Self-contradictory-absence check]**

* **Primary RI**: RI-03 [Unobserved explanatory]
* **ER**: The paper's proposed catalytic cycle mandates a Ru(0) active species. The pre-catalyst is formally Ru(II). The observation that genuine Ru(0) source Ru₃(CO)₁₂ is "not effective" is reported without explanation. This constitutes a self-contradictory absence: the cycle predicts Ru(0) must form and be active, yet the paper provides no activation evidence and reports that an alternative Ru(0) source is inactive.
* **EP**: EP-03a [Direct-observation / state-assignment pack]
* **Case-specific implementation**: Monitor H₂ evolution during the pre-catalyst activation period (RuH₂(CO)(PPh₃)₃ + ketone in toluene at 135 °C, no olefin) using a gas-tight setup with GC head-space analysis; if H₂ is not detected, this would argue against reductive elimination as the activation pathway and would require a revised mechanistic proposal. Alternatively, test whether the independently synthesized Ru(0) complex [Ru(CO)₂(PPh₃)₃] under identical conditions gives the same yield and rate as RuH₂(CO)(PPh₃)₃ (note: the paper states Ru(CO)₂(PPh₃)₃ was "equally effective," providing a partial answer to this question but without quantitative yield comparison or mechanistic analysis of its activation pathway).
* **Notes**: Partially overlaps with SRG-2 (U-2 is a member) but the self-contradictory-absence check (prompt §2b) identifies this as a CLA because the specific Ru(0)/Ru(II) activation discrepancy is not explicitly the subject of any single SRG member; SRG-2 captures the broader "catalytic cycle evidence absent" pattern. The CLA here isolates the internal logical contradiction at the pre-catalyst level. The observation that Ru(CO)₂(PPh₃)₃ is "equally effective" (B-3) is the strongest piece of evidence for a Ru(0) active species (since Ru(CO)₂(PPh₃)₃ can be formally Ru(0)); however, this point is not developed in the paper.

---

### §3 Current VQ assessment

**Current judgment: VQ-2 (Method) — fails at VQ-3**

**VQ-1 [Observation] — Pass (non-fatal reservation)**

RI-02 [Object identification] status: non-fatal at the current VQ-1 level. The paper certifies product structures as "established unequivocally by standard methods" (B-4), which, within the 1993 Nature communication genre, is taken as a reasonable proxy for NMR + elemental analysis or HRMS characterization of novel compounds. The 13 products are structurally distinct and well-defined by synthesis context (ortho-alkylated aromatic ketones with defined Si-containing substituents). The non-fatal reservation is that B-4's "standard methods[REDACTED: substantial verbatim quotation; see Tier 9]standard methods" refers to a minimum of ¹H NMR and elemental analysis for isolated products (runs 1, 3, 13 in parentheses), with GC characterization for the remaining runs.

**VQ-2 [Method] — Qualified pass (RI-01 non-fatal, RI-07 unresolved)**

On the premise that RI-02 is non-fatal (VQ-1 holds). RI-01 [Reporting integrity] is partially resolved within the communication format: the paper reports GC yields for most runs and isolated yields for 3 runs, establishing the measurement frame at a minimal level. The absence of calibration curve details (B-1) and the absence of actual TOF values (B-2) constitute non-fatal RI-01 items that prevent quantitative cross-comparison but do not invalidate the yield order-of-magnitude results. However, RI-07 [Unsupported boundary] is unresolved in a serious form: the scope boundary "variety of aromatic systems" is stated without failure examples (SRG-4, U-3, B-5), and the catalyst loading discontinuity (runs 5–6, elevated loading with no stated rationale) creates an unacknowledged boundary within the demonstrated substrate set. VQ-2 is therefore a qualified pass: the method-level reporting is minimally adequate for demonstrating the existence of the reaction, but not adequate for establishing the scope boundaries or the claimed comparative superiority. The qualification arises from RI-07 remaining unresolved in a form that directly affects the generality and efficiency claims.

**VQ-3 [Mechanism] — Fails (RI-03, RI-04, RI-06 unresolved)**

On the premise that VQ-2 is qualified. VQ-3 fails because RI-03, RI-04, and RI-06 are all unresolved at a fatal or near-fatal level:

- RI-03 [Unobserved explanatory] (SRG-2, CLA-2): The cyclometallated intermediate central to the selectivity-determining step is never directly observed or trapped. The Ru(0) active species is postulated but its formation from Ru(II) pre-catalyst is not demonstrated. Both are central to the proposed mechanism; without them, the mechanistic account is entirely product-structure inference.
- RI-04 [Unreplicated discriminator] (SRG-3): The rate comparison between runs 10 and 11 is presented as the key evidence for chelation-induced ring strain. No rate constants, activation parameters, or time-resolved yield data are provided. The single data point (run 10: 0.5 h, 100%; run 11: 20 h, 88%) is interpreted at a mechanistic level (ring strain) without excluding steric, electronic, or solubility alternatives.
- RI-06 [Imported model] (CLA-1): The mechanistic analogies invoked to support the Ru(0) OA/cyclometallation cycle (refs 14, 15, 17) are from mechanistically distinct systems (Mn(I) electrophilic, Ru(II) carboxylate, olefin OA vs. aromatic C–H OA) without demonstration of isomorphism. VQ-3 cannot hold when the proposed mechanism's key steps are supported only by structurally analogous but mechanistically different precedents.

**However, the empirical layer (efficiency + generality + selectivity claims) on its own reaches a higher level than the mechanism layer.** Specifically, the observation that this class of reaction proceeds in high yield across 13 substrate combinations (layer i–iii) would stand at VQ-2 even if the mechanism is entirely incorrect. The per-layer asymmetry is: empirical layers (i–iii) → VQ-2 qualified; mechanistic layer (iv) → VQ-1 at best (product structures are established, mechanism is entirely postulated).

**VQ-4 [Benchmark] — Fails (RI-08, RI-09 unresolved; inherited from VQ-3)**

VQ-4 fails both on inheritance (VQ-3 fails) and on its own terms. RI-08 [Unquantified reliability] is unresolved: isolated yields are provided for only 3 of 13 runs; GC calibration methodology is unstated; no replicate measurements or uncertainty estimates are reported for any run. RI-09 [External superiority] is unresolved: the TOF superlative ("among the highest reported") and the bilateral quantitative yield claim ("never been attained before") are asserted against prior art (refs 11–12) without numerical comparison on a common substrate or reporting of actual TOF values.

---

### §4 Era-Norm Annotation

**Communication-era tolerated:**

- **B-1** (GC yield without calibration methodology, isolated yields for 3 of 13 runs): Nature Articles of this era routinely certified yields by GC without specifying the internal standard or response factors; the expectation was that full analytical details would appear in the subsequent Full Paper. Tolerated in 1993 because the communication format explicitly deferred supporting data to the Full Paper format.

- **B-4** ("standard methods" for product characterization): In 1993 Nature communications, "standard spectroscopic methods" was accepted terminology for NMR (¹H, ¹³C) + elemental analysis (or combustion analysis) for isolated compounds, without detailed spectra or tables. The interpretation was convention-dependent and expected to be fully expanded in follow-up publications.

- **B-3** (qualitative catalyst SAR without yield values): The brief paragraph describing relative catalyst effectiveness ("equally effective," "modestly effective," "not effective") without numerical yields is consistent with the Nature Articles convention of providing a qualitative overview and reserving tabulated SAR data for the Full Paper. The convention was norm-compliant in 1993.

- **A-1** (mechanism deferred as "not yet clear"): Complete mechanism deferral is a recognized convention in synthetic discovery communications of this era, particularly in Nature, where a major practical discovery was considered worth reporting without a complete mechanistic account. This convention is less acceptable in contemporary high-impact communications, which typically require at least preliminary kinetic or spectroscopic mechanistic evidence.

- **B-2** (TOF superlative without numerical values): Asserting comparative superlatives without tabulating the supporting values was more tolerated in 1993 Nature communications than in current standards; the expectation was that the Full Paper would provide numerical TOF comparisons. Dual classification: also modern-era deficient (see below).

**Modern-era deficient:**

- **B-2** (TOF superlative without numerical values): By contemporary standards, any comparative superlative ("among the highest reported") must be supported by explicit tabulation of the claimed values alongside the comparators. The absence of actual TOF numbers for runs 1, 9, 10 in 2025 would be a direct reason for rejection at most high-impact journals. Dual classification: tolerated in 1993 but deficient by modern standards.

- **U-1** (cyclometallated intermediate entirely postulated, no spectroscopic evidence): In 2025, proposing a catalytic mechanism with a central selectivity-determining intermediate and providing no isolation, NMR, or computational evidence for that intermediate would be considered a fatal deficiency in any mechanistic communication. ³¹P{¹H} NMR monitoring of stoichiometric reactions is now a standard entry-level mechanistic experiment.

- **U-2** (Ru(II) pre-catalyst → Ru(0) active species, no activation evidence): The oxidation-state discrepancy between the pre-catalyst and the proposed active species, combined with the observation that the genuine Ru(0) source (Ru₃(CO)₁₂) is ineffective, would require explicit address in any modern submission. Induction period studies, H₂ evolution monitoring, or in-situ ³¹P NMR are now standard tools for this type of characterization.

- **B-5 / U-3** (scope claim "variety of aromatic systems" overstates demonstrated data): Modern practice requires that abstract-level scope language be bounded by the demonstrated data; "aromatic ketone systems" rather than "aromatic systems" would be the required phrasing. Reviewers would flag this as overclaiming in any current submission.

- **C-1** (comparative benchmark: qualitative limitations of refs 11–12 without numerical comparison): Modern high-impact publications require side-by-side quantitative comparison on a common substrate (or explicit statement of why a common substrate comparison is not feasible) when the novelty claim is comparative efficiency.

---

### §5 Shortest-reinforcement route

**First objective function: reach VQ-3 (Mechanism)**

Current VQ-2 (qualified). Required: resolve RI-03, RI-04, RI-06.

**Shortest route to VQ-3:**

1. **EP-03a** [Direct-observation / state-assignment pack] — Under stoichiometric conditions, mix RuH₂(CO)(PPh₃)₃ (1 equiv) with acetophenone (1 equiv) in d₈-toluene at 100–135 °C; monitor by ³¹P{¹H} NMR and ¹H NMR for the cyclometallated Ru intermediate; confirm identity by COSY/HMQC or X-ray if crystalline. Advances RI-03 (unobserved cyclometallated intermediate) — highest single-experiment information gain, because it simultaneously addresses U-1 (intermediate identity) and U-2 (Ru(0) vs. Ru(II) activation pathway: if a Ru(II) cyclometallate forms from a Ru(II) pre-catalyst without Ru(0) formation, the mechanistic proposal requires revision).

2. **EP-04a** [Discrimination / replication pack] — Obtain time-resolved yield profiles for runs 10 and 11 using aliquot-GC at defined time points (e.g., 0, 5, 15, 30, 60 min for run 10; 0, 1, 4, 10, 20 h for run 11) at identical catalyst loading (0.04 mmol); compute k_obs from initial-rate kinetics; perform the equivalent time-course for 1-indanone to establish a quantitative rate upper bound ("< X% yield at 24 h detection limit"). Advances RI-04 (unreplicated discriminator) and partially addresses RI-03 by establishing whether ring strain is kinetically operative.

3. **EP-06a** [Analogy-validation pack] — Provide an explicit mechanistic comparison between refs 14–15 (Mn(I)/Ru(II) electrophilic cyclometallation) and the proposed Ru(0) OA/cyclometallation; either cite a Ru(0) ketone-directed C–H OA precedent, or perform a DFT calculation of the OA energy barrier for the Ru(0)/acetophenone system as a minimal computational anchor. Advances RI-06 (imported model) and removes the mechanistic analogy gap identified in CLA-1.

Certification-gate note: EP-03a information gain is highest (advances RI-03 for both U-1 and U-2 simultaneously), but final VQ-3 certification requires all three RIs (RI-03, RI-04, RI-06) to be resolved; the experimental investment order follows information gain, but the final certification is fixed by the gate order VQ-1 → VQ-2 → VQ-3 → VQ-4.

---

**Second objective function: reach VQ-4 (Benchmark)** [prerequisite: VQ-3]

**Shortest route to VQ-4:**

1. **EP-01a** [Reporting-coherence pack] — Report actual TOF values (mol product mol⁻¹ Ru h⁻¹) for runs 1, 9, 10 alongside TOF values extracted from refs 11 and 12 under their stated conditions; tabulate GC internal standard (identity, purity standard, response factor relative to product) for all 13 runs; specify characterization data (¹H NMR, ¹³C NMR, HRMS, or elemental analysis) for each of the 13 isolated or GC-quantified products. Advances RI-01 (reporting integrity) and RI-09 (external superiority).

2. **EP-08a** [Replication / uncertainty pack] — Provide duplicate or triplicate runs for at least representative high-yield examples (runs 9, 10, 12) and for runs 5–6 (elevated loading); report mean ± SD for GC yield; provide isolated yield with purity data (GC purity or ¹H NMR integration) for all runs where isolated yield is currently absent. Advances RI-08 (unquantified reliability).

3. **EP-09a** [Internal benchmark pack] — On a common substrate (e.g., acetophenone + vinyltriethoxysilane, run conditions of this paper), compare with refs 11 and 12 systems either by direct side-by-side experiment (if feasible with the same substrate class) or by explicit acknowledgment that substrate classes differ (α-picoline vs. aromatic ketone) and restriction of the TOF comparison to "aromatic ketone C–H functionalization catalysis." Advances RI-09.

4. **EP-07a** [Boundary-test pack] — Test at least one non-ketone directing group (benzaldehyde or dimethylbenzamide); report result (positive yield with scope extension, or negative result with detection limit, explicitly bounding the scope to aromatic ketones). Advances RI-07 (unsupported boundary) for the scope claim.

Certification-gate note: EP-01a has the highest information gain for VQ-4 because it resolves both RI-01 (which is formally a VQ-2 item carried unresolved) and RI-09 (the primary VQ-4 requirement); the final certification is fixed by the gate order VQ-1 → VQ-2 → VQ-3 → VQ-4, meaning VQ-3 must be achieved before VQ-4 can be certified.

---

### §6 Contribution to institutional design

**1. New representative case for RI-03 — "self-contradictory absence" subtype with internal logical contradiction:**

The Murai 1993 case provides a particularly clean representative example of RI-03 in a form that includes an internal logical contradiction: the proposed cycle mandates Ru(0) as the active species, but (a) the pre-catalyst is formally Ru(II) and (b) the genuine Ru(0) source (Ru₃(CO)₁₂) is reported as "not effective[REDACTED: substantial verbatim quotation; see Tier 9]unobserved intermediate": it is "unobserved intermediate in the presence of contradictory experimental evidence." This pattern should be added to the RI-03 case library as: **RI-03 subtype — internally contradicted active species**: a species central to the proposed mechanism is both unobserved and contradicted by a control experiment whose result is reported without mechanistic discussion.

**2. Labeling mismatch — concentrated in final sentence of Possible Mechanisms:**

The labeling mismatch pattern is present and well-localized. The section header is "Possible Mechanisms" and the opening sentence is [REDACTED: verbatim source quotation; see the source paper via its DOI] However, the subsequent sentences shift from conditional language ("The reaction may begin with...") to factual verbs: [REDACTED: verbatim source quotation; see the source paper via its DOI] The word "postulated" appears only in the specific context "the intermediate postulated in Fig. 1," while the surrounding language treats the cyclometallation, olefin insertion, and reductive elimination as observed events. This labeling mismatch — hypothesis label in the section header, factual verbs in the body — is concentrated in the middle of the Possible Mechanisms section and is structurally consistent with the RI-06 co-occurrence (imported mechanistic model presented in factual verb form). The pattern is documented as a co-occurrence of labeling mismatch + RI-06.

**3. Automatic-resolution pattern via communication → Full Paper transition:**

Multiple RI items in this paper are of the type that would automatically resolve in the Full Paper format: B-1 (GC calibration), B-2 (actual TOF values), B-4 ("standard methods[REDACTED: substantial verbatim quotation; see Tier 9]communication-era tolerated." The correspondence between these items and the Full Paper resolution is confirmed by the existence of the subsequent Kakiuchi/Chatani mechanistic publications (GAP-3) that provided KIE, intermediate trapping, and Ru oxidation-state evidence in the period 1994–2000. This is a clear example of the automatic-resolution pattern: RI-01, RI-07, and RI-08 items arise from the communication format constraints and are resolved in the Full Paper trajectory.

**4. RI co-occurrence pattern — RI-03 and RI-06 co-occur in CLA-1:**

In CLA-1 (mechanistic analogy validity), RI-06 [Imported model] and RI-03 [Unobserved explanatory] co-occur structurally: the analogy citations (refs 14, 15) are from mechanistically non-isomorphic systems (RI-06), and the intermediate that the analogy is meant to support is also directly unobserved (RI-03). Resolving only RI-06 (by finding a genuine Ru(0) aryl ketone OA precedent) would still leave RI-03 unresolved (the intermediate is still unobserved in this paper's system). Resolving only RI-03 (by isolating the cyclometallated intermediate) would make RI-06 moot (the analogy would no longer be needed as structural support). The most efficient resolution strategy is therefore EP-03a (direct observation), which resolves RI-03 and makes RI-06 a secondary concern. This RI-03 + RI-06 co-occurrence is a new documented case of the co-occurrence pattern in which resolving the primary RI (RI-03) renders the secondary RI (RI-06) non-fatal, rather than requiring both to be resolved independently.

**5. Incomplete negative evidence — "not shown" pattern:**

B-9 (1-indanone "did not react at all" — "not shown[REDACTED: substantial verbatim quotation; see Tier 9](not shown)[REDACTED: substantial verbatim quotation; see Tier 9]did not react at all[REDACTED: substantial verbatim quotation; see Tier 9]absence of reaction in one substrate" is used to confirm a mechanistic hypothesis without establishing the detection boundary for the claimed absence.

**6. No new PRI candidate detected:**

All patterns observed in this paper map onto existing RI codes (RI-01 through RI-09) or the provisional PRI-10/PRI-11. No pattern requiring a new PRI candidate was detected in isolation. However, the internally contradicted active species subtype of RI-03 (point 1 above) is a noteworthy elaboration of RI-03 that could contribute to the v0.3 Codebook annotation notes if confirmed in additional cases.

**7. VQ boundary insight — per-layer asymmetry and communication-format compression:**

This case provides evidence that the VQ assessment of a communication-format paper requires explicit per-layer analysis. The empirical layers (efficiency + generality + selectivity) of Murai 1993 reach VQ-2 (qualified) as a stable achievement — the existence and approximate yield of the reaction is established. The mechanistic layer (proposed cycle, chelation assistance, ring-strain hypothesis) does not reach VQ-3. This asymmetry is structurally characteristic of synthetic discovery communications: the empirical discovery (VQ-2+) precedes mechanistic understanding (VQ-3) by years or decades. The institutional design implication is that communication-format papers should be assessed with an explicit two-register VQ judgment: (a) VQ level for the empirical discovery claim, and (b) VQ level for the mechanistic interpretation claim. For Murai 1993: empirical = VQ-2 qualified; mechanistic = VQ-1 (product identity established, mechanism entirely postulated). The gap between the two registers is the primary driver of the subsequent Full Paper and mechanistic study literature (GAP-3).

---

> **Tier 8 redaction notice**: This file is a redacted copy of the corresponding Tier 3 / Tier 9 output. Verbatim source-paper quotations have been replaced by `[REDACTED: see source paper §<loc>; full text retained in Tier 9 reviewer-only deposit]` markers, preserving location references and our own analytical content. Bibliographic fields (title, authors, journal, year, DOI), analytical labels (`evidence_chain:` with B-/U-/A-/C- internal IDs), short technical terms, and our own analytical text are not redacted. The redaction was applied by `scripts/redact_for_tier8.py` and, for this version, by `scripts/build_paperA_R1_public.py` with `scripts/redact_source_ngram_runs.py` (scripts of the project repository; they are not deposited).
