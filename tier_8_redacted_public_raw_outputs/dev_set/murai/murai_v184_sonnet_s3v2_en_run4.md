prompt_version: stage3-v2-en-20260419
model_info: claude-sonnet-4-6 (run #4, independent EN track)

# Re-certification Assessment Sheet for Scientific Knowledge

## Murai et al. 1993 (Nature, communication)

---

### §1 Claim Architecture

**Core claim summary:**

The paper claims that RuH2(CO)(PPh3)3 catalyses the addition of aromatic C–H bonds ortho to ketone directing groups across a range of aromatic ketones and terminal olefins, achieving [REDACTED: substantial verbatim quotation; see Tier 9] The **Novelty pillar** rests on three interlocking sub-claims: (NC-2) bilateral quantitative yields "never attained before" in catalytic C–H functionalization; (NC-4) virtually 100% regioselectivity at both the aromatic and olefinic positions; and (NC-3) generality spanning acylbenzenes, acylheteroaromatics, and diverse terminal olefins — exceeding the two-reactant-combination limitation of prior art. The **Utility pillar** is anchored in the phrase "required for practical organic synthesis" and the forward-looking claim (NC-6) that chelation assistance "should be applicable more widely for selective organometallic catalysis." An auxiliary mechanistic sub-claim (NC-5) identifies chelation assistance — Ru coordination to the carbonyl directing group driving ortho C–H cleavage via a cyclometallated intermediate — as the enabling mechanistic principle.

**Layered structure judgment:**

The claim architecture is layered, and a single refutation does not collapse all claims simultaneously. Specifically: (i) Refutation of the bilateral quantitative yield claim (NC-2) on analytical grounds would not defeat the regioselectivity claim (NC-4) or the substrate generality claim (NC-3). (ii) Refutation of the mechanistic rationale (NC-5 — chelation-directed cyclometallated intermediate) would not defeat the empirical yield and scope data, since the paper itself acknowledges "the mechanism is not yet clear" (A-1) even while proposing the mechanistic model. (iii) Refutation of the "variety of aromatic systems" scope framing (NC-3, U-3) on the grounds that all 13 runs use aromatic ketones would weaken but not eliminate the intra-class generality claim. (iv) The forward-looking generalizability claim (NC-6) is the least falsifiable layer from the paper alone.

However, the layers are not fully independent: the Novelty pillar as a whole depends structurally on the analytical evidence base (SRG-1). All three sub-claims — efficiency, selectivity, generality — rest on GC yield data whose calibration methodology is undocumented, and on structural characterisation compressed to "standard methods." If the analytical foundation (SRG-1) is found inadequate, all three sub-claims lose their evidentiary grounding simultaneously. In this sense, SRG-1 is the shared structural core whose failure would partially collapse the entire Novelty pillar.

The Mechanistic sub-claim (NC-5) occupies an anomalous position: it is simultaneously disclaimed ("not yet clear," A-1) and deployed as an explanatory apparatus (Fig. 1, ring-strain arguments for runs 10/11 rate difference, 1-indanone non-reactivity). This creates an internal tension in which mechanistic reasoning is invoked to explain selectivity outcomes (SRG-3) while the mechanism is formally held open. Refutation of NC-5 would therefore also undermine the selectivity-attribution arguments within NC-4 — a dependency the layered structure does not make explicit.

---

### §2 SRG / CLA → RI / ER / EP Crosswalk

**SRG-1 [Quantitative evidence base]** (member items: B-1, B-2, B-3, B-4)

* **Primary RI**: RI-01 [Reporting integrity]
* **Secondary RI**: RI-08 [Unquantified reliability]
* **ER**: For the efficiency, selectivity, and generality claims to be independently evaluable, the analytical methodology underlying all yield data must be specified with sufficient detail for external reproduction: internal standard identity, response factors or calibration curves for GC quantification, isolated yield confirmation for all runs presented as definitive, and explicit statement of characterisation methods for all novel products.
* **EP**: EP-01a [Reporting-coherence pack]; EP-08a [Replication / uncertainty pack]
* **Case-specific implementation**: (EP-01a) Provide calibrated GC yield data for all 13 runs using a specified internal standard (e.g., decane or dodecane) with stated response factors for each aromatic ketone–olefin product class; report isolated yields for all runs rather than the three currently provided; tabulate actual TOF values (mol product / mol Ru / h) for runs 1, 9, 10 alongside the conditions (substrate, time, temperature) used for their calculation. (EP-08a) Report replicate yields (n ≥ 3) for at least one representative run per substrate class (acylbenzene, acylheteroaromatic, TMS-olefin) with standard deviation; for the "highest reported TOF" claim, tabulate the literature TOF values from refs 11–12 alongside the paper's own TOF values on a common comparison basis.
* **Notes**: B-1 (GC calibration absent, isolated yields absent for 10/13 runs; high_convergence_low_gap, V1=high, V3=high, convergence 2/3); B-2 (TOF claim without numerical values; high_convergence_low_gap, V1=high, V3=high, convergence 2/3); B-3 (catalyst SAR comparison with no yield/condition data; high_convergence_low_gap, V1=medium, V2=medium, V3=medium, convergence 3/3 — the only 3/3 convergence item in the paper); B-4 ("standard methods[REDACTED: substantial verbatim quotation; see Tier 9]never attained before," "highest reported") but no replicate data or uncertainty descriptions are provided for any run. The shared root is that all four items involve quantitative performance claims whose evidentiary basis cannot be externally evaluated.

---

**SRG-2 [Catalytic cycle evidence absent]** (member items: A-1, U-1, U-2)

* **Primary RI**: RI-03 [Unobserved explanatory]
* **Secondary RI**: RI-06 [Imported model]
* **ER**: For the chelation-directed catalytic cycle to be mechanistically supported, at least one central species or elementary step must be directly observed or kinetically constrained: either the cyclometallated Ru intermediate (Fig. 1) must be isolated, spectroscopically characterized (³¹P{¹H} NMR, X-ray), or trapped under stoichiometric conditions; or the conversion of the Ru(II) pre-catalyst to the proposed Ru(0) active species must be demonstrated by an activation experiment (induction period, spectroscopic monitoring, Ru(0) control).
* **EP**: EP-03a [Direct-observation / state-assignment pack]; EP-06a [Analogy-validation pack]
* **Case-specific implementation**: (EP-03a) React RuH2(CO)(PPh3)3 with acetophenone under stoichiometric conditions in toluene-d8; monitor by ³¹P{¹H} NMR for formation of the proposed five-membered ruthenacyclic intermediate; attempt crystallization for X-ray structure confirmation. Additionally, monitor the pre-catalyst under catalytic turnover conditions by ³¹P{¹H} NMR to detect whether Ru(II) is converted to a distinct Ru species (Ru(0) candidate) during the induction period. (EP-06a) Provide a mechanistic justification for why the Mn(I) and Ru(II) cyclometallation products (refs 14–15) are structurally isomorphic with the proposed Ru(0) oxidative addition intermediate despite the oxidation-state difference; alternatively, cite a Ru(0)-specific aromatic C–H oxidative addition precedent that directly maps onto the proposed catalytic cycle entry step.
* **Notes**: A-1 (mechanism deferred: "not yet clear[REDACTED: substantial verbatim quotation; see Tier 9]not effective[REDACTED: substantial verbatim quotation; see Tier 9]applies not only to individual elementary steps but also to large-scale model import in which an entire catalytic cycle is constructed from another system").

---

**SRG-3 [Selectivity basis absent]** (member items: B-8, B-9, B-10, U-4)

* **Primary RI**: RI-04 [Unreplicated discriminator]
* **Secondary RI**: RI-05 [Qualitative overread]
* **ER**: For the selectivity claims to have a causal basis, the mechanistic attribution of rate differences and regioselectivity to chelation-directed ring strain must be supported by kinetic measurements that exclude alternative explanations: rate constants or relative rate data with controlled variables, a defined detection limit for the "did not react[REDACTED: substantial verbatim quotation; see Tier 9]virtually 100%" regioselectivity.
* **EP**: EP-04a [Discrimination / replication pack]; EP-05a [Quantitative-ranking substantiation pack]
* **Case-specific implementation**: (EP-04a) Measure a kinetic isotope effect (kH/kD) using deuterium-labelled acetophenone-d5 or β-tetralone-d6 to determine whether C–H cleavage is rate-determining; provide time-resolved yield profiles (GC analysis at multiple time points) for runs 10 and 11 to extract pseudo-first-order rate constants; report the 1-indanone experiment (B-9, "not shown[REDACTED: substantial verbatim quotation; see Tier 9]did not react" is quantitatively defined rather than qualitatively asserted. (EP-05a) Replace "virtually 100%" regioselectivity with a quantified ratio of the observed product to the sum of all detectable regioisomers, using GC analysis with stated detection limits; for the aromatic regioselectivity (runs 8 and 13), report whether ortho, meta, and para isomers were detected at defined thresholds.
* **Notes**: B-8 (run 10 vs. 11 rate difference attributed to ring strain without kinetic data; high_convergence_low_gap, V1=medium, V2=high, convergence 2/3, gap: low); B-9 (1-indanone negative result cited as mechanistic evidence, "not shown,[REDACTED: substantial verbatim quotation; see Tier 9]virtually 100%[REDACTED: substantial verbatim quotation; see Tier 9]did not react") without numerical rate support. Linked to SRG-2: the ring-strain argument depends on the cyclometallated intermediate (U-1) being the selectivity-determining species — but that intermediate is unobserved, creating a cascade where RI-04/RI-05 in SRG-3 are contingent on RI-03 in SRG-2.

---

**SRG-4 [Scope claims exceed data]** (member items: B-5, U-3, B-7)

* **Primary RI**: RI-07 [Unsupported boundary]
* **Secondary RI**: RI-05 [Qualitative overread]
* **ER**: For the scope claim ("a variety of aromatic systems") to be accurate, the demonstrated substrate scope must match the abstract's framing; any boundary not demonstrated experimentally must be explicitly qualified; and the "bilateral quantitative yield" claim must be supported by a mass balance that accounts for the fate of both starting materials.
* **EP**: EP-07a [Boundary-test pack]; EP-05a [Quantitative-ranking substantiation pack]
* **Case-specific implementation**: (EP-07a) Explicitly delimit the scope claim in the abstract to "aromatic ketone systems" or "carbonyl-directed aromatic systems" reflecting the actual substrate space tested; alternatively, report one or more non-ketone directing group substrates (aldehyde, ester, amide, imine) to provide empirical grounding for "a variety of aromatic systems"; for runs 8–13 (bilateral quantitative yield claim), report olefin conversion by GC analysis alongside product yield so that "based on both starting materials" can be independently verified. (EP-05a) Quantify the olefin mass balance for runs 1–7 and 8–13 to establish what fraction of the olefin is incorporated into product versus isomerized, oligomerized, or hydrosilylated, since the claim of "almost quantitative yields based on both the starting materials" depends on this.
* **Notes**: B-5 (mixed-classification: abstract scope claim "a variety of aromatic systems" overstates the demonstrated aromatic ketone scope); U-3 (self-contradictory absence: all 13 runs are aromatic ketones, yet the abstract implies non-ketone aromatic scope; V1=high); B-7 (bilateral quantitative yield claim without olefin mass balance). RI-07 extended use applies (Codebook note on negative boundary claims): "a variety of aromatic systems" implies the boundary of the reaction includes non-ketone aromatics, but no failure examples for non-ketone substrates are reported to justify this boundary by demonstration. RI-05 applies as secondary because the scope ranking ("variety") is a qualitative label derived from 13 runs within a single substrate class.

---

**SRG-5 [Prior art not engaged numerically]** (member items: C-1, B-2)

* **Primary RI**: RI-09 [External superiority]
* **Secondary RI**: RI-01 [Reporting integrity]
* **ER**: For the efficiency-superiority claim over refs 11–12 to be verifiable, the paper's own TOF values for runs 1, 9, and 10 must be stated, and those values must be compared with the TOF values from refs 11 and 12 on a common measurement basis (same time unit, same definition of active catalyst).
* **EP**: EP-09a [Internal benchmark pack]; EP-01a [Reporting-coherence pack]
* **Case-specific implementation**: (EP-09a) Tabulate TOF values (mol product / mol Ru / h) for runs 1, 9, and 10 alongside the TOF values extracted from refs 11 (Jordan & Taylor 1989) and 12 (Moore et al. 1992) using the same definition; if the reaction types are not directly comparable (pyridine/Zr vs. aromatic ketone/Ru), acknowledge the comparison limitation explicitly rather than asserting superiority without qualification. (EP-01a) Report the denominator of the TOF calculation (total Ru or kinetically active Ru fraction), the time at which TOF is measured (initial rate or average over the run), and whether partial conversion data are used for runs shorter than full conversion.
* **Notes**: C-1 (dropped quantitative benchmark: refs 11–12 compared on qualitative limitations, not on numerical TOF/TON/yield on a common substrate); B-2 (TOF claim without numerical values; high_convergence_low_gap, V1=high, V3=high, convergence 2/3). RI-09 is Primary: superiority is asserted on the basis of external qualitative limitation statements about refs 11–12 rather than a direct comparison run under the paper's own conditions. RI-01 is secondary because the absence of a defined TOF calculation methodology (denominator, time window, active catalyst fraction) means even the paper's own TOF comparison with prior art cannot be reproduced.

---

**Outside the SRGs: CLAs**

**CLA-1: Mechanistic analogy validity — imported cycle from oxidation-state-discrepant systems**

* **Primary RI**: RI-06 [Imported model]
* **Secondary RI**: RI-03 [Unobserved explanatory]
* **ER**: For the proposed catalytic cycle (Fig. 1) to constitute a mechanistic model rather than a schematic, the elementary step analogies invoked from refs 14, 15, 17, and 18 must be shown to be isomorphic with the proposed Ru(0) oxidative addition cycle; the oxidation-state discrepancy between Mn(I)/Ru(II) precedents and the proposed Ru(0) mechanism must be explicitly acknowledged and bridged.
* **EP**: EP-06a [Analogy-validation pack]; EP-03a [Direct-observation / state-assignment pack]
* **Case-specific implementation**: (EP-06a) For each elementary step in Fig. 1, identify a precedent in which the same metal oxidation state and ligand environment is used as in the proposed cycle; specifically, identify a Ru(0) aromatic C–H oxidative addition precedent distinct from the olefin OA described in ref. 17 (Komiya & Yamamoto); address whether M–H or M–C insertion (the two options given parenthetically with ref. 18) produces different product regiochemistry, since this distinction affects the interpretation of anti-Markovnikov selectivity.
* **Self-contradictory-absence check**: The catalytic cycle (Fig. 1) predicts that the Ru(0) active species must exist under turnover conditions — yet Ru3(CO)12 (a Ru(0) source) is listed as "not effective," creating a puzzle the paper does not address. This is a self-contradictory-absence pattern: the proposed mechanism requires Ru(0) but the paper's own data show one Ru(0) source is inactive, without discussion of why.
* **Notes**: Grounded in B-11, C-2, C-4, C-5, C-6. Not captured in a single SRG; closest affinity to SRG-2 (mechanistic evidence gap). The CLA is independently motivated by the Ru3(CO)12 inactive result (B-3), which, combined with the Ru(0) requirement, creates a self-contradictory-absence pattern beyond SRG-2's scope.

---

**CLA-2: Discontinuous catalyst loading in runs 5–6**

* **Primary RI**: RI-01 [Reporting integrity]
* **Secondary RI**: RI-07 [Unsupported boundary]
* **ER**: For the generality claim to extend uniformly to TMS-substituted terminal olefins, runs 5 and 6 (6 mol% catalyst, 3× standard loading) must either perform at standard loading (2 mol%) or the elevated loading must be acknowledged as a substrate-specific limitation with the standard-loading result reported.
* **EP**: EP-01a [Reporting-coherence pack]; EP-07a [Boundary-test pack]
* **Case-specific implementation**: (EP-01a) Add a footnote or separate entry for runs 5 and 6 stating the rationale for elevated catalyst loading; report the result at standard 2 mol% loading (even as a failure-mode data point) to allow assessment of TMS-olefin substrate reactivity relative to the Si(OEt)3-olefin substrates (runs 9–11). (EP-07a) If TMS-olefins require 6 mol% loading to achieve >90% yield within a practical time frame, qualify the generality claim for this substrate class explicitly, since the 33-h reaction time of run 6 already signals a reactivity boundary.
* **Notes**: Grounded in B-6. Related to SRG-4 (scope exceeds data) and SRG-1 (quantitative evidence base). The loading discontinuity is embedded silently in Table 1 and confounds the cross-run efficiency comparison — runs 5 and 6 cannot be compared directly with runs 9–11 for the "highest TOF" discussion.

---

### §3 Current VQ assessment

**Current judgment: VQ-2 (Method) — qualified**

---

**VQ-1 [Observation]: fails**

Grounds: RI-02 [Object identification] is unresolved. The paper certifies product structures for all 13 novel products as "established unequivocally by standard methods" (B-4) without specifying what those methods are. For a 1993 Nature communication, ¹H NMR and elemental analysis were minimum standards for novel compounds; for Si-containing products (runs 1–13 involving triethoxyvinylsilane or trimethylvinylsilane), ²⁹Si NMR, high-resolution mass spectrometry, or X-ray data would have been expected at the full-paper level. The characterization basis for product identity — which is the foundation for all subsequent claims about selectivity, yield, and scope — is not independently evaluable from the paper's text. The "unequivocally" qualifier heightens rather than resolves this gap, because it implies a high confidence level that the omitted data would need to justify.

Non-fatal assessment: In the context of a Nature communication with a 3-page limit in 1993, the "standard methods" compression was a recognized format convention and would not have caused the paper's core claims to be retracted or disputed by contemporaneous referees. VQ-1 failure is therefore **era-norm dependent** (non-fatal at time of publication, deficient by modern reporting standards). However, the failure at VQ-1 propagates: all higher-level VQ judgments are conditional on this characterisation gap being tolerated.

---

**VQ-2 [Method]: qualified**

On the premise that RI-02 is era-norm-dependent non-fatal (VQ-1 tolerated), VQ-2 is assessed as **qualified** rather than a pass.

Grounds for qualified status: RI-01 [Reporting integrity] is unresolved in a structurally serious form. The GC yield reporting for 13 runs provides no internal standard, no response factor specification, and no calibration curve; isolated yields are provided for only 3 runs (runs 1, 3, 13) and absent for 10 runs. The TOF claim ("highest reported") is asserted without a numerical value. The catalyst structure–activity comparison uses four undefined qualitative labels. CLA-2 (discontinuous catalyst loading in runs 5–6) is not disclosed in the text. RI-07 [Unsupported boundary] is unresolved for the scope claim (SRG-4). Together, RI-01 and RI-07 mean that the methodological framework underlying the paper's three central claims cannot be externally audited.

RI-05 [Qualitative overread] remains in SRG-3 and SRG-4, and the "virtually 100%" regioselectivity and "variety of aromatic systems[REDACTED: substantial verbatim quotation; see Tier 9]qualified" status.

Note: VQ-2 qualified does not mean the results are incorrect — the substrate-scope table presents 13 reactions with yields that are internally plausible and consistent with the mechanistic rationale. It means the analytical basis for independent verification is missing.

---

**VQ-3 [Mechanism]: fails**

On the premise that VQ-2 (qualified) is provisionally accepted, VQ-3 fails.

Grounds: RI-03 [Unobserved explanatory] is fatal at this level. The cyclometallated intermediate (U-1) is the mechanism's selectivity-determining species and is both central and entirely experimentally uncharacterised — it is depicted in Fig. 1 as a defined organometallic species but has not been isolated, observed by NMR, or trapped. Additionally, RI-06 [Imported model] is unresolved: the cycle-level mechanistic model is constructed from Mn(I)/Ru(II) stoichiometric systems (refs 14–15) that are mechanistically distinct from the proposed Ru(0) oxidative addition pathway without a bridging argument. U-2 (Ru(II) → Ru(0) activation mechanism absent) is a second RI-03 gap. RI-04 [Unreplicated discriminator] is unresolved in SRG-3: the run 10/11 rate comparison and the 1-indanone negative result are single data points interpreted at a mechanistic level without kinetic analysis or controlled-variable exclusion.

Layered VQ asymmetry: The **empirical substrate-scope layer** (runs 1–13 as an observational dataset, independently of mechanistic interpretation) has reached VQ-1 with era-norm tolerance and is approaching VQ-2. The yield data, even without calibration documentation, provide a consistent empirical picture of reactivity across 13 substrate combinations. However, the **mechanistic interpretation layer** does not approach VQ-3 in any form, because the central intermediate is experimentally invisible. This asymmetry is structurally significant: the paper's long-term impact rested on the empirical layer, while the mechanism was subsequently established by the Kakiuchi/Chatani group in follow-up publications (GAP-3).

---

**VQ-4 [Benchmark]: fails**

VQ-4 fails because VQ-3 has not been passed, and additionally RI-08 [Unquantified reliability] and RI-09 [External superiority] are unresolved. No replicate measurements or uncertainty estimates are provided for any yield. The "highest reported TOF" claim lacks the numerical TOF values needed to evaluate it against refs 11–12.

---

### §4 Era-Norm Annotation

**communication-era tolerated:**

- **B-4** ("standard methods[REDACTED: substantial verbatim quotation; see Tier 9]established unequivocally by standard methods" was standard practice. The journal format did not require spectral data tables in the main text; supporting information systems were not yet formalized at Nature in this period. Contemporaneous communications in Nature, JACS Communications, and Angewandte Chemie used equivalent compression. Non-fatal at the time.

- **B-1** (GC yield without internal standard or calibration specification): In 1993 synthetic organometallic communications, GC yield reporting without explicit internal standard identification was common in short-format papers, where readers were expected to accept GC yield as a recognized but operationally variable quantity. The absence of calibration specification would not have been flagged by contemporaneous referees of a Nature communication.

- **B-3** (catalyst SAR as qualitative labels without supporting data): A short-format paper in 1993 was not expected to provide full condition tables for exploratory catalyst screening. The qualitative designations ("equally effective," "modestly effective," "not effective") were a recognized way to communicate screening results within the page constraint.

- **A-1** ("mechanism is not yet clear"): Explicit mechanism deferral was both common and respected in high-impact 1993 communications, where the empirical demonstration was understood to precede mechanistic elaboration. The "Possible mechanisms" section heading itself signals that the mechanistic content is hypothetical, and referees of that era would not have required mechanistic evidence as a condition of publication for a substrate-scope result of this quality.

- **B-2** (TOF claim without numerical values): Comparative superlative claims ("among the highest") without tabulation were acceptable in 1993 Nature communications, where the primary criterion was scope and novelty of the chemical transformation rather than precise kinetic characterization.

**modern-era deficient:**

- **B-1** (GC yield without calibration): Under current reporting standards — including ACS guidelines, Nature Chemistry, and JACS full paper standards — GC yield data require specification of internal standard, response factor, or calibration procedure. Without this, yields cannot be independently reproduced. Modern re-certification would require calibrated GC or a complete set of isolated yields.

- **B-4** ("standard methods[REDACTED: substantial verbatim quotation; see Tier 9]Standard methods" without specification fails contemporary reporting standards for novel compound characterization.

- **B-2** (TOF claim without values): A comparative "highest reported" claim without numerical values is not acceptable in contemporary papers. TOF must be defined (initial turnover frequency vs. average), calculated from a stated denominator, and compared with literature values numerically.

- **U-1** (cyclometallated intermediate: depicted in Fig. 1 as a defined structure, experimentally uncharacterised): At the time of publication this was tolerated under "Possible mechanisms[REDACTED: substantial verbatim quotation; see Tier 9]proposed" or "postulated" consistently throughout the text and figure, or a brief stoichiometric experiment providing at least indirect support.

- **B-6** (elevated catalyst loading in runs 5–6 not disclosed in text): Modern reporting standards require disclosure and discussion of non-standard conditions within the scope table. An unexplained 3× increase in catalyst loading embedded silently in a data table would be flagged by contemporary reviewers.

- **B-9** ("not shown[REDACTED: substantial verbatim quotation; see Tier 9]not shown." A "did not react" result invoked as mechanistic evidence must specify what "did not react" means quantitatively.

**Items in both categories (tolerated then, deficient now):**

- **B-1, B-4, B-2**: All three were tolerated within the 1993 Nature communication format but are deficient by modern standards. This dual classification applies directly: the format_exploitation documented in D-2 of Stage 2 created the structural opportunity for these omissions, and the automatic-resolution pattern (§6 below) explains why they were expected to be addressed in follow-up full papers.

---

### §5 Shortest-reinforcement route

**Objective function 1: VQ-3 [Mechanism] (current VQ-2 qualified → target VQ-3)**

For VQ-3, the required resolutions are RI-03 (unobserved explanatory) and RI-04 (unreplicated discriminator), inheriting VQ-2's requirements (RI-01, RI-07).

```
Shortest route to VQ-3:

1. EP-03a [Direct-observation / state-assignment pack] — React RuH2(CO)(PPh3)3
   stoichiometrically with acetophenone in toluene-d8; monitor by ³¹P{¹H} NMR
   for formation of the five-membered ruthenacyclic intermediate shown in Fig. 1;
   confirm Ru oxidation state via X-ray or ¹³C NMR of carbonyl region.
   Advances RI-03 (U-1, primary gap; addresses both the intermediate identity
   and the Ru(II) → Ru(0) pre-catalyst activation question, U-2).

2. EP-04a [Discrimination / replication pack] — Measure kH/kD isotope effect with
   deuterium-labelled aromatic substrate (e.g., acetophenone-d5) under catalytic
   conditions; provide time-resolved yield profile for runs 10 and 11 to extract
   comparative rate constants; report the 1-indanone control experiment (B-9) with
   explicit conditions and GC detection limit.
   Advances RI-04 (SRG-3: run 10/11 selectivity attribution, B-8, B-9).

3. EP-06a [Analogy-validation pack] — Identify a Ru(0)-specific aromatic C–H
   oxidative addition precedent isomorphic with the proposed cycle; address the
   mechanistic discrepancy between Mn(I)/Ru(II) stoichiometric precedents (refs
   14–15) and the proposed Ru(0) OA mechanism; address why Ru3(CO)12 (a Ru(0)
   source) is inactive if Ru(0) is required.
   Advances RI-06 (CLA-1: imported cycle from oxidation-state-discrepant systems).

4. EP-01a [Reporting-coherence pack] — Report calibrated GC yields with internal
   standard for all 13 runs; provide isolated yields for all runs; tabulate TOF values
   for runs 1, 9, 10 with stated calculation basis; disclose and explain the elevated
   catalyst loading in runs 5–6.
   Advances RI-01 (SRG-1, SRG-5: quantitative evidence base and prior-art
   comparison; also resolves CLA-2).

5. EP-05a [Quantitative-ranking substantiation pack] — Replace "virtually 100%"
   regioselectivity with quantified ratio and stated detection limits; report olefin
   mass balance for runs 8–13 to substantiate the bilateral quantitative yield claim.
   Advances RI-05 (SRG-3, SRG-4: qualitative overread in selectivity and scope claims).
```

Information-gain ordering rationale: EP-03a is ranked first because confirming the cyclometallated intermediate (RI-03, U-1) simultaneously advances the two largest gaps in the paper — intermediate identity and active species identity — and provides the foundational mechanistic support that the entire "Possible mechanisms" section requires. EP-04a is ranked second because it directly tests the selectivity attribution (SRG-3) without requiring the intermediate to be first isolated; KIE data can be obtained in parallel with EP-03a stoichiometric experiments. EP-06a is ranked third because it requires the outcome of EP-03a to be meaningful — only once the intermediate is characterized can the analogy with refs 14–15 be properly evaluated. EP-01a is ranked fourth because GC methodology improvement and isolated yield expansion are independent of the mechanistic work and can be addressed in a concurrent analytical effort. EP-05a is ranked fifth because quantification of regioselectivity thresholds, while important for VQ-2 passage, is technically straightforward once the product identity (EP-01a) is confirmed.

```
Certification-gate note: The experimental investment order follows information
gain, but the final certification is fixed by the gate order VQ-1 → VQ-2 → VQ-3
→ VQ-4; EP-02a (product identity confirmation, VQ-1) must be confirmed before
VQ-2 certification proceeds, and VQ-2 must hold before VQ-3 certification can be
awarded, regardless of the order in which the above experiments are performed.
```

---

**Objective function 2: VQ-4 [Benchmark] (VQ-3 as prerequisite → target VQ-4)**

```
Shortest route to VQ-4 (after VQ-3 achieved):

1. EP-08a [Replication / uncertainty pack] — Report replicate yields (n ≥ 3) for
   at least one representative run per substrate class with standard deviation;
   report the uncertainty on all TOF values calculated from kinetic profiles
   obtained in EP-04a.
   Advances RI-08 (SRG-1: unquantified reliability of yield and TOF data).

2. EP-09a [Internal benchmark pack] — Tabulate the paper's own TOF values for
   runs 1, 9, 10 alongside extracted literature TOF values from refs 11 (Jordan &
   Taylor 1989) and 12 (Moore et al. 1992) on a common measurement basis (same
   time unit, denominator definition, substrate class).
   Advances RI-09 (SRG-5: external superiority claim).

Certification-gate note (VQ-4): EP-08a and EP-09a can be executed in parallel
after VQ-3 is certified; however, RI-08 and RI-09 are both required for VQ-4
passage, and neither can substitute for the other.
```

---

### §6 Contribution to institutional design

**1. Representative case for RI-03 — "Available-but-unutilized characterization" subtype (Codebook application note, v0.2a):**

The Murai 1993 paper provides a clear case for the RI-03 subtype "Available-but-unutilized characterization." The paper's experimental setup — refluxing toluene with RuH2(CO)(PPh3)3 and acetophenone — is a stoichiometric experiment that the authors could have run alongside the catalytic reactions. The proposed intermediate is drawn as a structurally defined five-membered ruthenacycle (Fig. 1). The characterisation data needed to confirm it (³¹P{¹H} NMR in toluene-d8, or X-ray from a stoichiometric reaction) were within the technical capability of the Osaka University organometallic chemistry group in 1993. This is therefore not a case where the observation was technically impossible, but a case where a characterization that could have been performed was not performed and reported. The case strengthens the RI-03 "available-but-unutilized" subtype as a recurring pattern in high-impact communications that prioritize scope demonstration over mechanistic grounding.

**2. RI-06 cycle-level import — new representative case:**

The mechanistic citations in the "Possible mechanisms[REDACTED: substantial verbatim quotation; see Tier 9]distributed RI-06" or "mosaic import."

**3. Labeling mismatch detected:**

The paper exhibits a labeling mismatch of the type flagged in the §6 template. The [REDACTED: verbatim source quotation; see the source paper via its DOI] (not "may give"); [REDACTED: substantial verbatim quotation; see Tier 9] (not "is postulated to involve"). The factual-verb mode is concentrated in the mechanistic-explanation sentences that support the selectivity-attribution claims, while the hypothetical label ("not yet clear") is concentrated in the opening sentence. This asymmetric deployment allows the paper to disclaim mechanistic certainty in the abstract while using the mechanism as an explanation in the Results — a pattern that co-occurs with RI-06 (the imported mechanism makes its factual-verb deployment feel more natural, because the precedents cited are presented as if they directly support the proposed intermediate).

**4. Automatic-resolution pattern (communication → Full Paper):**

The Murai 1993 paper is an exemplary case of the automatic-resolution pattern in which RI-01 and RI-07 gaps arising from the communication format were resolved in subsequent full papers. The GC calibration gap (B-1), isolated yield gaps (B-1), and characterization compression (B-4) were addressed in the Kakiuchi/Chatani group's follow-up JACS and JACS Communications papers over 1994–2000, which also provided the mechanistic data (intermediate trapping, KIE, Ru oxidation state assignments) that resolve RI-03 and RI-04 (GAP-3). This confirms that the A items in §4's Era-Norm Annotation (B-1, B-4, B-2) are indeed automatic-resolution candidates in the communication → Full Paper transition. The Codebook should note that for landmark communications (high citation count, paradigm-setting results), the automatic-resolution pattern is frequently confirmed by the research group's own follow-up literature — and Stage 3 analysis should therefore cross-reference GAP-3-type entries to anticipate where RI gaps are likely to have been resolved externally.

**5. Ru3(CO)12 inactive result as self-contradictory-absence within CLA-1:**

The paper notes that Ru3(CO)12 is "not effective[REDACTED: substantial verbatim quotation; see Tier 9]in-text-negative-result–as–silent–contradiction" variant should be added to the Codebook as a sub-pattern of RI-03 or flagged as a PRI candidate.

**6. PRI-11 inapplicability confirmed:**

PRI-11 (Mechanism–kinetics decoupling: [REDACTED: substantial verbatim quotation; see Tier 9]) does not apply to Murai 1993, because the paper does not report any rate orders at all. The decoupling presupposes a rate law comparison that this paper has not performed. This case therefore refines PRI-11's applicability boundary: PRI-11 requires that rate-law data exist but be used only qualitatively, whereas Murai 1993 represents the more fundamental RI-03/RI-04 case where kinetic data are entirely absent. The Murai case and PRI-11 cases (Breitenfeld 2014, Pengfei 2024) occupy different positions on the kinetic-evidence spectrum, and their distinction is analytically informative for future classification.

**7. PRI-10 (Kinetic overclaim) — one additional case:**

PRI-10 applies in a specific form to Murai 1993: the "highest reported TOF" claim (B-2) asserts an absolute rate enhancement without kinetic data. This is isomorphic with the Monnereau 2009 case that established PRI-10 provisionally. Murai 1993 therefore provides a second independent paper in which a comparative rate claim ("highest reported[REDACTED: substantial verbatim quotation; see Tier 9]isomorphism confirmed across two independent papers[REDACTED: substantial verbatim quotation; see Tier 9]Murai 1993 provides a second PRI-10 case (B-2: 'highest reported TOF' without TOF value or rate measurement). Promotion candidate confirmed pending cross-case isomorphism review."

**Summary of institutional contributions:**

- New representative case for RI-03 "available-but-unutilized characterization" subtype
- New representative case for RI-06 "distributed / mosaic import" at the cycle level (proposed as Codebook v0.3 note)
- Labeling mismatch detected: factual verbs in mechanistic attribution despite "Possible mechanisms" heading — co-occurring with RI-06
- Automatic-resolution pattern confirmed for B-1, B-4, B-2 (communication → Full Paper, Kakiuchi/Chatani group)
- New self-contradictory-absence sub-pattern: "in-text-negative-result-as-silent-contradiction" (Ru3(CO)12 inactive vs. Ru(0) requirement)
- PRI-11 inapplicability boundary clarified (no rate orders reported; PRI-11 requires rate-law data to exist before decoupling applies)
- Second independent case supporting PRI-10 promotion (B-2: "highest reported TOF" without kinetic measurement)

---

> **Tier 8 redaction notice**: This file is a redacted copy of the corresponding Tier 3 / Tier 9 output. Verbatim source-paper quotations have been replaced by `[REDACTED: see source paper §<loc>; full text retained in Tier 9 reviewer-only deposit]` markers, preserving location references and our own analytical content. Bibliographic fields (title, authors, journal, year, DOI), analytical labels (`evidence_chain:` with B-/U-/A-/C- internal IDs), short technical terms, and our own analytical text are not redacted. The redaction was applied by `scripts/redact_for_tier8.py` and, for this version, by `scripts/build_paperA_R1_public.py` with `scripts/redact_source_ngram_runs.py` (scripts of the project repository; they are not deposited).
