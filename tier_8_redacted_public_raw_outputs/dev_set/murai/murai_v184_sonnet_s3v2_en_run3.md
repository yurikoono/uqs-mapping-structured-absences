prompt_version: stage3-v2-en-20260419
model_info: claude-sonnet-4-6

# Re-certification Assessment Sheet for Scientific Knowledge

## Murai et al. 1993 (Nature, Article)

---

### §1 Claim Architecture

**Core claim summary:**

The paper makes a compound claim structured around three pillars: *Novelty* — the ruthenium complex RuH₂(CO)(PPh₃)₃ is the first catalyst to achieve all three of efficiency, selectivity, and generality simultaneously in the catalytic coupling of aromatic C–H bonds with olefins; and *Utility* — the reaction is directly applicable to practical organic synthesis as demonstrated by quantitative bilateral yields (runs 8–13), high turnover frequency (runs 1, 9, 10), and broad substrate scope across acylbenzenes, acylheteroaromatics, and a variety of mono- and di-substituted terminal olefins. The enabling mechanism is stated as chelation assistance: the carbonyl directing group coordinates Ru, positioning it for selective ortho C–H cleavage. The paper simultaneously acknowledges that [REDACTED: substantial verbatim quotation; see Tier 9] placing the mechanistic claim in a formally speculative frame while presenting it in factual-verb form throughout the "Possible mechanisms" section.

**Layered structure judgment:**

The claims form three independently falsifiable layers:

- **Layer 1 — Efficiency/yield layer**: Bilateral quantitative yield from equimolar reactants (runs 8–13); TOF "among the highest reported for this type of reaction." Falsifiable by a mass-balance or time-resolved kinetics experiment showing lower-than-claimed yields or lower TOF than prior art.
- **Layer 2 — Scope/generality layer**: Applicability beyond one or two reactant combinations; demonstrated across acylbenzene + acylheteroaromatic substrates and multiple olefin classes. Falsifiable by showing that the scope is confined to the aromatic ketone directing-group class (narrower than the abstract claim "a variety of aromatic systems").
- **Layer 3 — Mechanistic/chelation layer**: Chelation-assisted ortho C–H cleavage via a postulated cyclometallated Ru intermediate. Falsifiable in principle by isolating the intermediate or demonstrating that selectivity arises by a different mechanism (e.g., thermodynamic product distribution).

**Independence:** A yield counter-example (Layer 1 failure) would not collapse the scope claim (Layer 2) or the mechanism (Layer 3). A scope counter-example (Layer 2 failure, e.g., evidence that ketone is the only effective directing group) would not collapse Layer 1 yields. A mechanism refutation (Layer 3) would not by itself eliminate the synthetic utility of Layer 1 or Layer 2. The three layers are structurally independent; no single refutation simultaneously dismantles all claims.

**Inter-layer dependencies:** The mechanism (Layer 3) is invoked to *explain* the efficiency and selectivity of Layers 1 and 2, but neither Layer 1 nor Layer 2 depends on the correctness of Layer 3 for its empirical validity (the yields and scope data exist independent of the mechanistic interpretation). This asymmetry means that the empirical layers (1, 2) are more robust than the mechanistic layer (3), and that Layer 3 gains support from Layers 1 and 2 only if the proposed mechanism uniquely predicts the observed product distribution — which it cannot, given that the mechanism is presented only as one possible account.

---

### §2 SRG / CLA → RI / ER / EP Crosswalk

---

**SRG-1 [Quantitative evidence base]**
Member items: B-1, B-2, B-3, B-4

* **Primary RI**: RI-01 [Reporting integrity]
* **Secondary RI**: RI-09 [External superiority]
* **ER**: For the efficiency and TOF superiority claims to hold, yields must be reported with a fully specified GC calibration (internal standard, response factors, calibration curve), isolated yields must be available for all runs or a justified subset, and TOF values must appear numerically in Table 1 alongside the numerical TOF values for refs 11 and 12 on a common or comparable substrate.
* **EP**: EP-01a [Reporting-coherence pack]; EP-09a [Internal benchmark pack]
* **Case-specific implementation**: (i) Report the GC internal standard identity (e.g., dodecane), the response factor for each Si-containing product relative to the standard, and the calibration range used; (ii) Provide isolated yields for all 13 runs or provide an explicit justification for selective isolation reporting; (iii) Insert a TOF column into Table 1 with numerical values calculated at defined time points (e.g., TOF at 50% conversion) for runs 1, 9, 10; (iv) Tabulate the TON and TOF values from refs 11 (Jordan & Taylor) and 12 (Moore et al.) on the most comparable substrate, enabling direct numerical comparison. The first three items are achievable within the existing three-page format as table column additions; the fourth requires one sentence of text or a supplementary note.
* **Notes**: B-1 (GC yield without calibration, TEMPERATURE_SUMMARY high_convergence_low_gap, V1=high, V3=high, convergence 2/3, gap: none); B-2 (TOF claimed without numerical values, TEMPERATURE_SUMMARY high_convergence_low_gap, V1=high, V3=high, convergence 2/3, gap: none); B-3 (catalyst SAR without any yield data, TEMPERATURE_SUMMARY high_convergence_low_gap, V1=medium, V2=medium, V3=medium, convergence 3/3, gap: none); B-4 ("standard methods" certification for 13 novel products without method specification). RI-09 is secondary because the superiority over refs 11/12 (C-1) is asserted through qualitative limitation statements rather than a common-substrate numerical comparison.

---

**SRG-2 [Catalytic cycle evidence absent]**
Member items: A-1, U-1, U-2

* **Primary RI**: RI-03 [Unobserved explanatory]
* **Secondary RI**: RI-06 [Imported model]
* **ER**: For the chelation-assistance mechanism to function as the paper's stated "key to our success," the cyclometallated intermediate shown in Fig. 1 must be independently demonstrated (isolation, ³¹P{¹H} NMR observation, or stoichiometric trapping), the active Ru(0) species must be confirmed by activation data (induction period, H₂ evolution, or spectroscopic identification), and at least one elementary step in the proposed catalytic cycle must be supported by direct experimental evidence rather than precedent analogy from mechanistically distinct systems.
* **EP**: EP-03a [Direct-observation / state-assignment pack]; EP-06a [Analogy-validation pack]
* **Case-specific implementation**: (i) Perform a stoichiometric reaction of RuH₂(CO)(PPh₃)₃ with acetophenone in the absence of olefin at 135 °C and characterise the product by ³¹P{¹H} NMR and X-ray crystallography to verify or refute the proposed ruthenacyclic intermediate; (ii) Monitor H₂ evolution during an early-stage catalytic run (GC headspace analysis) to confirm reductive elimination of H₂ from the Ru(II) pre-catalyst as the activation step; (iii) Perform a crossover experiment: mix Ru-catalyst with a mixture of two isotopically labelled aromatic ketones (deuterated at the ortho position in one, unlabelled in the other) and test for H/D scrambling in the product, which would confirm or rule out reversible C–H oxidative addition. The cyclometallated intermediate characterisation (item i) is the single most information-dense experiment: it would simultaneously address U-1, A-1, and B-11/C-2.
* **Notes**: A-1 (formally deferred: [REDACTED: substantial verbatim quotation; see Tier 9]; TEMPERATURE_SUMMARY low_convergence_high_gap via V2-Q2 → critical); U-1 (self-contradictory absence: intermediate shown in Fig. 1 has no experimental characterisation; V2=critical, V3=critical, convergence 2/3, gap: none); U-2 (pre-catalyst Ru(II) vs. proposed Ru(0) discrepancy unacknowledged; V2=high, single-agent sourcing). RI-06 is secondary because refs 14 and 15 (stoichiometric cyclometallation of acetophenone with Mn(I) and Ru(II)-carboxylate complexes, respectively) are mechanistically distinct from the proposed Ru(0) oxidative addition cycle; the analogy is imported without isomorphism validation (B-11, C-2).

---

**SRG-3 [Selectivity basis absent]**
Member items: B-8, B-9, B-10, U-4

* **Primary RI**: RI-04 [Unreplicated discriminator]
* **Secondary RI**: RI-05 [Qualitative overread]
* **ER**: For the selectivity claims (ortho C–H selectivity, anti-Markovnikov olefin selectivity, ring-strain rate control) to be mechanistically grounded, rate constants or relative rates must be measured under defined initial conditions for at least two structurally differentiated substrate pairs, the three non-observed regioisomers must be sought by GC/NMR at a defined detection limit, and the 1-indanone negative result must be accompanied by the detection limit of the assay and the reaction conditions applied.
* **EP**: EP-04a [Discrimination / replication pack]; EP-05a [Quantitative-ranking substantiation pack]
* **Case-specific implementation**: (i) Measure the kinetic isotope effect kH/kD using ortho-deuterated acetophenone with triethoxyvinylsilane under standard conditions (run 9 conditions); this single experiment tests whether C–H cleavage is the rate-determining step and provides direct kinetic evidence for the proposed chelation-assisted mechanism; (ii) Report rate constants (or half-lives at defined substrate concentrations) for runs 10 and 11, enabling the ring-strain hypothesis to be tested quantitatively rather than by endpoint comparison; (iii) Add a GC-search for the three non-observed regioisomers in runs 8 and 13 with a stated detection limit (e.g., < 0.5% by GC with internal standard); (iv) Report the conditions (substrate, catalyst loading, time) for the 1-indanone experiment and its GC detection limit, converting the binary "did not react at all" to a quantitative bound (e.g., < 1% product at 24 h, 2 mol% catalyst).
* **Notes**: B-8 (rate attribution between runs 10 and 11 without kinetic data; TEMPERATURE_SUMMARY high_convergence_low_gap, V1=medium, V2=high, convergence 2/3, gap: low); B-9 (1-indanone negative result as positive mechanistic evidence, "not shown[REDACTED: substantial verbatim quotation; see Tier 9]virtually 100%" without detection limit for non-observed isomers); U-4 (self-contradictory absence: "virtually" qualifier acknowledges possible trace formation without quantifying). RI-05 is secondary: the ring-strain argument (faster run 10 vs. slower run 11) derives a structural causal inference from a two-endpoint yield-and-time comparison without numerical kinetic support.

---

**SRG-4 [Scope claims exceed data]**
Member items: B-5, U-3, B-7

* **Primary RI**: RI-07 [Unsupported boundary]
* **Secondary RI**: RI-08 [Unquantified reliability]
* **ER**: For the scope claim "a variety of aromatic systems" to be accurate, either the abstract must qualify the scope as "aromatic ketone systems" or the paper must demonstrate C–H functionalization with at least one non-ketone directing group (aldehyde, ester, amide, imine). Additionally, the bilateral quantitative yield claim requires olefin fate monitoring (olefin conversion, mass balance from olefin side) for the runs claiming quantitative yield from both starting materials.
* **EP**: EP-07a [Boundary-test pack]; EP-08a [Replication / uncertainty pack]
* **Case-specific implementation**: (i) Test at least one non-ketone directing group under standard run-9 conditions (e.g., methyl benzoate, benzaldehyde, acetanilide, 2-acetylpyridine) and report whether coupling occurs; a single negative result with conditions reported would sharpen the boundary of the chelation-assistance claim; (ii) Report olefin conversion (by GC or ¹H NMR) for runs 8–13 that claim quantitative bilateral yield, specifically monitoring vinyltrimethylsilane and triethoxyvinylsilane consumption and checking for olefin oligomerization or isomerization products; (iii) Revise the abstract to qualify the scope as "aromatic ketone systems" until broader directing-group scope is demonstrated.
* **Notes**: B-5 (scope claim mixed: "a variety of aromatic systems" vs. all 13 runs using aromatic ketones); U-3 (self-contradictory absence: abstract scope claim unsupported by the paper's own data); B-7 ("based on both starting materials" yield claim without olefin fate monitoring). RI-08 is secondary because the bilateral quantitative yield claims (runs 8–13) are not accompanied by replicate measurements or uncertainty ranges.

---

**SRG-5 [Prior art not engaged numerically]**
Member items: C-1, B-2

* **Primary RI**: RI-09 [External superiority]
* **ER**: For the efficiency superiority claim over refs 11 and 12 to hold, TON and TOF values from refs 11 (Jordan & Taylor 1989) and 12 (Moore et al. 1992) must be reproduced from those papers and directly compared with the numerical TOF values for runs 1, 9, and 10 on a structurally analogous substrate, or a footnote must qualify the comparative claim as based on the characterisation of limitations in those papers.
* **EP**: EP-09a [Internal benchmark pack]
* **Case-specific implementation**: Retrieve refs 11 and 12, extract TON/TOF for the highest-performing substrate in each, and compare with the calculated TOF for runs 1, 9, 10 (calculated as mol product / [mol Ru × time(h)]). If a common substrate comparison is not possible due to substrate-class difference, report the comparison in a table with a footnote on the comparison basis. This is achievable as a supplementary note or as a Table 1 footnote within the existing format.
* **Notes**: C-1 (severed quantitative benchmark: refs 11/12 cited with qualitative limitation characterisation only, no numerical comparison); B-2 (TOF values stated as "among the highest" for runs 1, 9, 10 without any numerical TOF values in the paper). TEMPERATURE_SUMMARY: B-2 high_convergence_low_gap, V1=high, V3=high, convergence 2/3, gap: none.

---

**Outside the SRGs: CLAs**

---

**CLA-1: Catalyst fate and recyclability**

Grounded_in: B-2, B-7 (D-4-6; not captured in any SRG)

* **Primary RI**: RI-08 [Unquantified reliability]
* **ER**: For the claim of "practical organic synthesis" utility to be validated at the catalyst-sustainability level, the paper must report whether the Ru catalyst is recoverable after reaction, what its activity is in a second run (if recyclable), and whether the TOF calculation is based on total Ru loading or active Ru — because an insoluble precipitate or deactivated complex would make the TOF calculation an understatement of the initial active-species efficiency.
* **EP**: EP-08a [Replication / uncertainty pack]
* **Case-specific implementation**: Perform a catalyst-reuse experiment: after run 9 (0.5 h, 100% yield), analyse the reaction mixture by ³¹P{¹H} NMR and ICP-MS (or AAS) to determine Ru speciation and recovery; charge fresh substrate and olefin and measure yield after 0.5 h to determine if the catalyst retains activity. Alternatively, report a time-resolved yield profile for run 9 (at 0.1, 0.25, 0.5 h) that would allow calculation of an initial TOF independent of endpoint yield.
* **Notes**: This CLA captures the catalyst lifetime dimension of the practical-utility claim. It is distinct from SRG-1 (which addresses calibration of the yield measurement) and SRG-5 (which addresses prior-art comparison). No B/A item in any SRG covers catalyst recyclability directly.

---

**CLA-2: Anomalous catalyst loading in runs 5 and 6**

Grounded_in: B-6 (D-4-7; not captured in any SRG)

* **Primary RI**: RI-01 [Reporting integrity]
* **Secondary RI**: RI-04 [Unreplicated discriminator]
* **ER**: For the substrate-scope table to be internally consistent and comparative, the rationale for the 3× catalyst loading in runs 5 and 6 (0.12 mmol vs. 0.04 mmol standard) must be stated, and the yield at standard loading (0.04 mmol) for the same substrates must be reported to enable a direct comparison with the rest of the scope table.
* **EP**: EP-01a [Reporting-coherence pack]; EP-04a [Discrimination / replication pack]
* **Case-specific implementation**: Report runs 5 and 6 at the standard 2 mol% loading (0.04 mmol) under otherwise identical conditions to determine whether elevated loading is a catalyst deactivation threshold (substrate-inhibition effect) or a practical convenience; if the standard-loading yield differs substantially, add a footnote explaining the substrate-specific loading requirement and its mechanistic implication for Si-containing olefin substrates (vinyltrimethylsilane).
* **Notes**: B-6 (Table 1: runs 5 and 6 at 0.12 mmol vs. all others at 0.04 mmol, no rationale stated; 33 h reaction time of run 6 vs. 4 h of run 5 at identical loading with identical olefin, not discussed). This is a condition-reporting coherence violation within Table 1, not captured by SRG-1 (which covers the calibration dimension) or SRG-3 (which covers the selectivity dimension). RI-04 is secondary because the long reaction time of run 6 constitutes a single-data-point observation interpreted (implicitly) as substrate-specific reactivity without a second replicate or a mechanism.

---

**CLA-3: Mechanistic basis for 1:1 vs. 1:2 selectivity control**

Grounded_in: [T2: A-1, B-8] (D-4-9; not captured in any SRG)

* **Primary RI**: RI-05 [Qualitative overread]
* **ER**: For the steric-congestion attribution of 1:1 vs. 1:2 selectivity (runs 1 and 2 vs. run 9) to be mechanistically grounded, the paper must demonstrate that the 1:1 adduct's geometry prevents carbonyl chelation (e.g., by space-filling model or DFT geometry optimisation) or provide a competition experiment that distinguishes steric from electronic and concentration-dependent (mass-action) explanations for the selectivity switch.
* **EP**: EP-05a [Quantitative-ranking substantiation pack]
* **Case-specific implementation**: Perform a competition experiment: add the isolated 1:1 adduct of run 1 to a fresh solution of triethoxyvinylsilane (2 equiv.) under run 9 conditions and monitor whether the 1:2 product forms; if it does not, the 1:1 product is genuinely resistant to a second coupling, supporting steric inhibition; if it does, the selectivity in run 1 is kinetically controlled by olefin concentration rather than by steric blocking of chelation. This single experiment distinguishes the two explanations without requiring structural data.
* **Notes**: The steric-congestion attribution appears in the paper without exclusion of the alternative (mass-action kinetics): the use of 6 equiv. olefin in run 2 to drive the 1:2 product is equally consistent with a concentration-dependent equilibrium as with steric deblocking. The claim is a T2 inference (one step from the text: A-1 + B-8 together indicate that mechanistic attributions in this paper lack quantitative grounding).

---

**CLA-4: Absence of concrete synthetic target connection**

Grounded_in: [T2: B-5, U-3] (D-4-8; not captured in any SRG)

* **Primary RI**: RI-07 [Unsupported boundary]
* **ER**: For the practical-utility claim ("required for practical organic synthesis," "extremely valuable in organic synthesis") to be grounded, the paper must identify at least one named synthetic target (natural product, pharmaceutical intermediate, industrial chemical) for which the present reaction provides a shorter or otherwise superior route compared to existing methods.
* **EP**: EP-07a [Boundary-test pack]
* **Case-specific implementation**: Add one target-molecule sentence to the Applications section: e.g., identify one known natural product or pharmaceutical building block that contains the ortho-alkylated aryl ketone motif and is currently synthesised by a longer route; use the product of one of the 13 runs as a retrosynthetic disconnection entry point for that target. This does not require new experimental data — it is an analytical extension of the existing scope demonstration.
* **Notes**: This CLA captures the "practical organic synthesis" utility claim at the level of named synthetic problems. It is not captured by SRG-4 (which addresses the scope overstatement) or SRG-1 (which addresses yield quantification). The claim is classified as RI-07 (unsupported boundary) because the paper asserts a positive limit — "required for practical organic synthesis" — without a single concrete synthetic problem that crosses that boundary.

---

### §3 Current VQ assessment

**Current judgment: VQ-2 (Method) — holds at the method level, but only on the premise that RI-02 is non-fatal**

---

**VQ-1 [Observation] — Pass (with non-fatal qualification)**

RI-02 [Object identification]: The paper certifies that [REDACTED: substantial verbatim quotation; see Tier 9] (B-4). For a Nature communication of 1993, this certification functions as the era-standard object-identification claim. RI-02 is assessed as **non-fatal** on era-norm grounds (see §4): in 1993, full spectroscopic data were typically deposited or available on request, and "standard methods" was accepted as a certification of identity. The 13 products are all structurally defined by their substrate structures plus the regioselectivity of the C–H/olefin coupling, leaving little structural ambiguity. VQ-1 holds on the premise that RI-02 is non-fatal.

---

**VQ-2 [Method] — Pass (with non-fatal RI-01 qualification for era; modern-era deficient for TOF claim)**

VQ-2 inherits the VQ-1 premise (RI-02 non-fatal).

RI-01 [Reporting integrity] (primary RI of SRG-1): The yield measurement method is internally inconsistent across runs — GC yields without calibration for 10 of 13 runs, isolated yields for 3 of 13, and no internal standard or response factor stated. This is a **non-fatal** RI-01 violation on era-norm grounds for the scope demonstration (GC yield without calibration was acceptable in 1993 Nature communications for substrate-scope tables), but it is **fatal to the TOF superlative claim** ("among the highest reported") because TOF cannot be evaluated without knowing whether the GC yields are numerically accurate. The paper's method-level claim is therefore conditionally coherent for the scope data but incoherent for the efficiency (TOF) claim.

The resolution: the scope demonstration (Layer 2) reaches VQ-2 in a qualified form; the TOF superiority claim (part of Layer 1) does not reach VQ-2 because RI-01 is fatal for that specific sub-claim. VQ-2 overall holds for the observational scope data with a RI-01 non-fatal qualification, but the TOF-superiority sub-claim remains at sub-VQ-2.

RI-07 [Unsupported boundary] (primary RI of SRG-4/CLA-4): The scope claim "a variety of aromatic systems" fails VQ-2 because the stated boundary is not supported by failure examples for non-ketone directing groups. However, this is assessed as **non-fatal for VQ-2 gate passage** because the experimental data for the demonstrated substrate class (aromatic ketones) are internally coherent. The abstract-level boundary overstatement is a scope-framing problem (Layer 2 boundary) that does not invalidate the observations within the demonstrated scope.

**VQ-2 judgment:** Holds for the empirical scope observations, with the TOF superiority sub-claim below VQ-2 (RI-01 fatal for that sub-claim) and the abstract-level scope boundary failing RI-07.

---

**VQ-3 [Mechanism] — Fail**

VQ-3 is assessed on the premise that VQ-2 holds for the empirical scope observations.

RI-03 [Unobserved explanatory] (primary RI of SRG-2): The cyclometallated intermediate shown in Fig. 1 is not isolated, spectroscopically observed, or kinetically constrained. The proposed Ru(0) active species is not confirmed despite the pre-catalyst being formally Ru(II). No elementary step in the proposed catalytic cycle has direct experimental support. VQ-3 **fails** because RI-03 is unresolved and is assessed as **fatal to the mechanistic layer (Layer 3)**: the paper's "Possible mechanisms" section cannot reach VQ-3 status until the intermediate is at least constrained by stoichiometric experiment.

RI-06 [Imported model] (secondary RI of SRG-2): The cyclometallated intermediate is supported only by analogy to stoichiometric reactions of Mn(I) and Ru(II)-carboxylate complexes (refs 14, 15), which are mechanistically distinct from the proposed Ru(0) oxidative addition. The model is imported without isomorphism validation. This is assessed as **fatal in combination with RI-03**: importing an analogy from a different mechanism while the proposed intermediate is unobserved leaves Layer 3 mechanistically unsupported.

RI-04 [Unreplicated discriminator] (primary RI of SRG-3): The selectivity claims (ring-strain rate control, regioselectivity "virtually 100%") rest on single-data-point endpoint comparisons (runs 10 vs. 11) and unquantified detection limits. RI-04 is **non-fatal for VQ-3 gate passage** from the scope perspective — the regioselectivity claim is supported by the consistent product structures across 13 runs — but remains as a deficiency for the mechanistic interpretation of selectivity.

RI-05 [Qualitative overread] (secondary RI of SRG-3 and CLA-3): The steric-congestion attribution of 1:1/1:2 selectivity and the ring-strain attribution of run 10/11 rate difference both constitute qualitative overread. **Non-fatal** for VQ-3 gate passage: RI-05 items create a "VQ-3 qualified" status for Layer 3, but VQ-3 already fails on RI-03 grounds, making the RI-05 qualification moot at this gate.

**VQ-3 judgment:** Fails. Unresolved fatal RIs: RI-03, RI-06. Layer 3 (mechanistic) cannot reach VQ-3. Layers 1 and 2 on their own do not require VQ-3 (mechanism) to hold; their empirical claims are at VQ-2.

---

**VQ-4 [Benchmark] — Not reachable from current evidence base**

VQ-4 inherits the VQ-3 failure. Additionally:

RI-08 [Unquantified reliability] (primary RI of SRG-4, CLA-1, CLA-2): Comparative data lack replicate measurements and uncertainty descriptions; no two runs are exact replicates; no error bars appear in Table 1. **Fatal for VQ-4**: benchmark claims cannot be certified without replication.

RI-09 [External superiority] (primary RI of SRG-5): Superiority over refs 11 and 12 is asserted without direct numerical comparison on a common substrate. **Fatal for VQ-4**: the benchmark claim ("among the highest reported") is unverifiable from the paper's data.

**VQ-4 judgment:** Not reachable. Unresolved fatal RIs: RI-08, RI-09 (in addition to inherited VQ-3 failure from RI-03, RI-06).

---

**Per-layer VQ asymmetry:**

- **Layer 1 (Efficiency/yield)** on its own: Reaches VQ-2 (qualified) — the yield data are observationally coherent for the scope demonstrations, but the TOF superiority sub-claim is below VQ-2 (RI-01 fatal for that sub-claim, RI-09 unresolved).
- **Layer 2 (Scope/generality)** on its own: Reaches VQ-2 (qualified) — the substrate-scope data are observationally coherent within the aromatic ketone class, but the abstract-level scope boundary ("a variety of aromatic systems") fails RI-07.
- **Layer 3 (Mechanism/chelation)** on its own: Below VQ-3 — RI-03 (unobserved intermediate) is fatal; RI-06 (imported model) is fatal in combination with RI-03.

The most robust part of the paper's claim is the empirical substrate scope (Layer 2, VQ-2 qualified); the most fragile is the mechanistic layer (Layer 3, VQ-3 failure). The utility claim (Layer 1) sits between: the yield data are observationally sound, but the TOF superiority and practical-utility framing require VQ-4-level evidence that is absent.

---

### §4 Era-Norm Annotation

**communication-era tolerated:**

- **B-1** (GC yield without internal standard or response factor specification): In 1993 Nature communications, substrate-scope GC yield reporting without calibration details was standard practice for short communications. The three-page format did not require — and rarely permitted — full analytical method reporting. The era norm accepted GC yield as a reliable metric for scope demonstration without calibration documentation. The B-1 omission is tolerated for the substrate-scope function of the yield data, though not for the TOF superiority claim (see modern-era deficient).

- **B-4** ("standard methods[REDACTED: substantial verbatim quotation; see Tier 9]established unequivocally by standard methods" as a pro forma object-identification certification; full spectroscopic data were expected to be available on request rather than in-print. This era norm rendered B-4 communication-era tolerated.

- **B-3** (catalyst SAR reported qualitatively — "equally effective," "modestly effective," "not effective"): In 1993 Nature communications, comparative catalyst screening was routinely reported in qualitative terms without tabulating the screening yields, especially where the screening function was to justify the selected catalyst rather than to characterise SAR. Communication-era tolerated as a scope-justification statement.

- **C-3** (refs 1–7 cited as a block for 30 years of C–H activation history without individual engagement): Citation of a background block en masse was standard in 1993 short communications, which lacked the space for individuated prior art discussion. Communication-era tolerated.

- **A-1** (mechanism formally deferred: "not yet clear"): In 1993, a Nature communication reporting a synthetically significant catalytic result was not expected to resolve the mechanism prior to publication; mechanism was a second publication's business. The formal deferral in A-1 is communication-era tolerated.

---

**modern-era deficient:**

- **B-2** (TOF claimed as "among the highest reported" without numerical TOF values): Modern reporting standards require that any comparative performance superlative be accompanied by numerical values for both the present system and the systems being compared. The TOF superlative is unverifiable from Table 1 (which contains no TOF column) and therefore fails modern reproducibility standards. Modern-era deficient.

- **B-6** (anomalous 3× catalyst loading in runs 5 and 6 with no stated rationale): Modern substrate-scope reporting requires that condition deviations from the standard protocol be flagged explicitly in the table and explained mechanistically or practically. The silent 3× loading increase in runs 5 and 6 would not be acceptable in a modern Joule, Nature Chemistry, or JACS communication without footnoted justification. Modern-era deficient.

- **U-2** (Ru(II) pre-catalyst vs. Ru(0) active species discrepancy unacknowledged): In 2025, any paper proposing a catalytic cycle that requires a Ru(0) active species would be expected to either characterise the activation step or explicitly acknowledge the Ru(II)/Ru(0) gap with a reference to activation literature. The complete absence of any acknowledgment of this discrepancy is modern-era deficient.

- **B-9** (1-indanone negative result as mechanistic evidence without detection limit): Modern standards for using negative results as positive mechanistic evidence require specifying the conditions (substrate loading, catalyst loading, reaction time, GC detection limit). "Did not react at all" without these conditions is modern-era deficient as a mechanistic argument.

- **B-10 / U-4** (regioselectivity "virtually 100%[REDACTED: substantial verbatim quotation; see Tier 9]Virtually 100%" with "virtually" unquantified is modern-era deficient.

**Items in both categories:**

- **B-1** is communication-era tolerated for the substrate-scope yield data but modern-era deficient for the TOF superiority sub-claim: the TOF claim cannot be independently verified without GC calibration data, and this deficiency is independent of the era norm for scope reporting.

---

### §5 Shortest-reinforcement route

**Objective function 1: Advance from current VQ-2 (qualified) to VQ-3**

VQ-3 requires resolution of RI-03 (primary, fatal for Layer 3) and RI-06 (secondary, fatal in combination with RI-03). RI-04 (SRG-3) is a non-fatal qualification for VQ-3 but should be addressed to remove the "qualified" flag.

**Shortest route to VQ-3:**

1. **EP-03a [Direct-observation / state-assignment pack]** — Perform a stoichiometric reaction of RuH₂(CO)(PPh₃)₃ with acetophenone (2 equiv.) in toluene at 135 °C under N₂ (no olefin) and characterise the product by ³¹P{¹H} NMR and X-ray crystallography; if the ruthenacyclic intermediate is obtained, this simultaneously resolves RI-03 (intermediate directly observed) and partially resolves RI-06 (the intermediate's characterised structure can then be compared with refs 14/15 to assess mechanistic analogy validity). Advances RI-03 (primary); partially advances RI-06 (secondary). *Single highest-information-gain experiment in the paper.*

2. **EP-03a [Direct-observation / state-assignment pack]** (second implementation) — Monitor H₂ evolution by GC headspace analysis in the first 10 minutes of a standard run (run 9 conditions), confirming that the Ru(II) pre-catalyst undergoes reductive elimination of H₂ to generate an active Ru(0) species. Advances RI-03 (U-2: Ru(II)/Ru(0) activation step confirmed). Advances RI-06 indirectly (a confirmed Ru(0) active species validates the mechanistic assumption that the cycle begins at Ru(0)).

3. **EP-06a [Analogy-validation pack]** — Compare the characterised stoichiometric cyclometallation product (from step 1) structurally with the products described in refs 14 and 15, and explicitly assess whether the Mn(I)/Ru(II)-carboxylate pathway from those references is isomorphic to the proposed Ru(0) oxidative addition. Record the structural and mechanistic differences explicitly. Advances RI-06 (imported model fully evaluated). Requires step 1 output.

4. **EP-04a [Discrimination / replication pack]** — Measure the kinetic isotope effect kH/kD using ortho-deuterated acetophenone under run 9 conditions; report the observed kH/kD value. Advances RI-04 (rate-determining step identified; the selectivity claims gain kinetic grounding). Removes the "qualified" flag from VQ-3.

*Certification-gate note: The experimental investment order follows information gain (EP-03a first, as it advances the most RIs simultaneously), but final VQ-3 certification follows the inheritance gate order VQ-1 → VQ-2 → VQ-3, with VQ-2 confirmed as the current level before VQ-3 is assessed.*

---

**Objective function 2: Advance from VQ-3 to VQ-4 (after VQ-3 is satisfied)**

VQ-4 additionally requires resolution of RI-08 (SRG-4, CLA-1) and RI-09 (SRG-5). RI-01 for the TOF sub-claim and RI-07 for the scope boundary also require attention.

**Shortest route to VQ-4 (after VQ-3):**

1. **EP-09a [Internal benchmark pack]** — Retrieve the TON/TOF data from refs 11 (Jordan & Taylor, JACS 1989) and 12 (Moore et al., JACS 1992); calculate TOF for runs 1, 9, 10 using a time-resolved yield profile (at defined conversion, e.g., 50% or initial rate); tabulate all values on a common basis. Advances RI-09 (external superiority claim now internally benchmarked). Also partially advances RI-01 (TOF calculation requires a defined GC calibration basis for the present runs).

2. **EP-01a [Reporting-coherence pack]** — Specify the GC internal standard and response factors for the Si-containing products in runs 1–13; provide isolated yields for the remaining 10 runs or justify the selective isolation reporting; add TOF column to Table 1. Advances RI-01 (reporting integrity for yield and TOF data fully specified). Prerequisite for RI-09 numerical comparison.

3. **EP-08a [Replication / uncertainty pack]** — Report replicate runs (n ≥ 2) for at least runs 1, 9, and 10 (the runs cited for the TOF superiority claim), with standard deviations on yield and time; report a catalyst-reuse experiment for run 9. Advances RI-08 (unquantified reliability). Prerequisite for VQ-4 gate passage.

4. **EP-07a [Boundary-test pack]** — Test at least one non-ketone directing group (e.g., methyl benzoate, acetanilide, benzaldehyde) under run 9 conditions and report the result (positive or negative with detection limit). Advances RI-07 (unsupported boundary for "a variety of aromatic systems"). Removes or reframes the abstract-level scope claim.

*Certification-gate note: Final VQ-4 certification requires all RI-08, RI-09 to be resolved in addition to the inherited VQ-3 requirements (RI-03, RI-06, RI-04). The gate order VQ-1 → VQ-2 → VQ-3 → VQ-4 is fixed regardless of the experimental investment order.*

---

### §6 Contribution to institutional design

**New representative cases for existing RI codes:**

- **RI-03 (Unobserved explanatory) — "Labeling mismatch[REDACTED: substantial verbatim quotation; see Tier 9]postulated" appears once (in the context of refs 14/15 — [REDACTED: verbatim source quotation; see the source paper via its DOI] or "postulated" qualifier. The "Possible mechanisms" section thereafter uses factual-verb form throughout: "the reaction may begin with the coordination" (modal hedge), [REDACTED: substantial verbatim quotation; see Tier 9] (factual verb "results in"; "to give[REDACTED: substantial verbatim quotation; see Tier 9]labeling mismatch + RI-06 co-occurrence" as a standard combined detection rule.

- **RI-06 (Imported model) — cycle-level import confirmed:** The entire proposed catalytic cycle is assembled from analogies drawn from mechanistically distinct systems (Mn(I) electrophilic cyclometallation, Ru(II)-carboxylate cyclometallation, olefin oxidative addition to Ru), none of which individually supports the proposed Ru(0) oxidative addition of an arene C–H bond. This is a cycle-level import (not merely a single-step analogy), confirming the RI-06 scope-note added in v0.2a. The Murai case is a cleaner cycle-level import than prior cases because the pre-catalyst oxidation state (Ru(II)) does not match the proposed active-species oxidation state (Ru(0)) — a discrepancy that is both unacknowledged and detectable from the paper's own text. This case should be added to the RI-06 case library as the reference instance of "cycle-level model import with pre-catalyst/active-species oxidation-state mismatch."

**PRI promotion evidence:**

- **PRI-11 (Mechanism–kinetics decoupling) — additional confirmation case:** The Murai 1993 paper provides a third independent case for PRI-11. The paper proposes a four-step catalytic cycle (coordination → C–H oxidative addition → olefin insertion → reductive elimination) but derives no rate law from this cycle, does not compare the cycle's rate-law predictions with the observed yield/time data, and supports the cycle only by agreement with product structure (ortho selectivity, anti-Markovnikov) rather than by rate orders. The paper's own text acknowledges the situation: [REDACTED: substantial verbatim quotation; see Tier 9] This is an exact instance of PRI-11's definition: [REDACTED: substantial verbatim quotation; see Tier 9] Given that PRI-11 had two-paper independent confirmation (Breitenfeld 2014 + Pengfei 2024) and the Murai case provides a third, historically earlier, and chemically distinct case, this case is suitable as an anchor for PRI-11 promotion from provisional to confirmed status. The promotion criterion is satisfied: isomorphic pattern confirmed across three independent papers.

**New VQ boundary insight — VQ-3 failure mode with era-norm interaction:**

The Murai case establishes a specific failure mode at the VQ-3 gate that has not been recorded in prior cases: **era-norm tolerated A-item + unresolved fatal RI-03 + cycle-level RI-06 co-occurrence.** The pattern is: a paper formally acknowledges mechanistic uncertainty (A-1: "not yet clear[REDACTED: substantial verbatim quotation; see Tier 9]not yet clear"). The institutional design implication: an A-item (formal deferral) does not convert RI-03 from fatal to non-fatal at VQ-3; VQ-3 failure is not mitigated by the presence of an A-item acknowledging the same gap. This boundary clarification should be added to the VQ decision matrix notes.

**New EP case-specific implementation — EP-04a with incomplete negative evidence:**

The 1-indanone "did not react at all" result (B-9, SRG-3) is a representative case of "incomplete negative evidence" as specified in the Stage 3 v2 institutional design template. The pattern: a negative result (zero yield) is used as positive mechanistic evidence (ring-strain confirmation) without specifying the conditions applied to the negative substrate or the detection limit of the assay. This case adds a chemistry-specific implementation to EP-04a: in future Murai-type C–H activation papers, EP-04a should include the requirement that any "substrate did not react" claim be accompanied by (a) a stated detection limit for the GC assay, (b) the reaction conditions applied to the unreactive substrate (time, temperature, catalyst loading, olefin), and (c) confirmation that at least one standard positive-control substrate gave the expected yield under identical conditions in the same experimental run. This implementation should be added to the EP-04a entry in the EP dictionary.

**Automatic-resolution pattern via communication → Full Paper transition:**

B-1 (GC calibration) and B-4 ("standard methods[REDACTED: substantial verbatim quotation; see Tier 9]automatic-resolution candidates — verify in the Full Paper series" rather than as permanent VQ-2 failures.

**RI co-occurrence pattern — RI-03 + RI-06 requiring joint resolution:**

The co-occurrence of RI-03 (unobserved intermediate) and RI-06 (imported cycle-level model) in SRG-2 creates a resolution dependency that does not exist when either appears alone. When RI-03 is the only unresolved item, EP-03a (direct observation) alone resolves both. When RI-06 co-occurs, resolving RI-03 by isolation of the intermediate is necessary but not sufficient: the isolated intermediate must also be compared structurally with the refs-14/15 analogues to confirm or reject the mechanistic analogy (EP-06a). This means that RI-03 + RI-06 co-occurrence requires at minimum a two-step resolution (EP-03a then EP-06a) and that resolving EP-03a first provides the structural data needed for EP-06a. The co-occurrence pattern in the Murai case should be recorded as the reference instance of "RI-03 + RI-06 joint resolution requiring sequenced EP investment."

---

> **Tier 8 redaction notice**: This file is a redacted copy of the corresponding Tier 3 / Tier 9 output. Verbatim source-paper quotations have been replaced by `[REDACTED: see source paper §<loc>; full text retained in Tier 9 reviewer-only deposit]` markers, preserving location references and our own analytical content. Bibliographic fields (title, authors, journal, year, DOI), analytical labels (`evidence_chain:` with B-/U-/A-/C- internal IDs), short technical terms, and our own analytical text are not redacted. The redaction was applied by `scripts/redact_for_tier8.py` and, for this version, by `scripts/build_paperA_R1_public.py` with `scripts/redact_source_ngram_runs.py` (scripts of the project repository; they are not deposited).
