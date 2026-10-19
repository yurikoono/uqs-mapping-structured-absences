```
prompt_version: stage3-v2-en-20260419
model_info: claude-sonnet-4-6

# Re-certification Assessment Sheet for Scientific Knowledge

## Tamao, Sumitani, Kumada 1972 (Journal of the American Chemical Society, Communication)

---

### §1 Claim Architecture

**Core claim summary:**

The paper reports a catalytic method for selective cross-coupling of Grignard reagents with vinyl or aryl halides using a nickel-phosphine complex, specifically [NiCl₂(dpe)] as the representative catalyst.

*Novelty pillar:* A transition metal catalyst — rather than a stoichiometric organometallic reagent — achieves selective C–C bond formation (cross over homo) with sp² organic halides, including reactive chlorides that prior art could not exploit; and does so even with Grignard reagents bearing β-hydrogen atoms.

*Utility pillar:* Practical one-step access to "hardly accessible" normal alkyl arenes (e.g., m-di-n-butylbenzene) and vinyl compounds via high-yield Grignard cross-coupling under mild conditions (ether, 0° to reflux, catalytic Ni).

**Layered structure:** Four independent claim layers are present; independent layers exist and no single refutation collapses all simultaneously.

- *Layer 1 (Synthetic utility):* Yields and substrate scope (11 Table I entries, β-H compatibility). Can be evaluated by yield data alone; does not depend on mechanistic correctness.
- *Layer 2 (Chloride reactivity):* "High reactivity of chlorides" claimed as "most remarkable." Depends on comparison with prior bromide/iodide art (asserted, not verified within paper).
- *Layer 3 (Ligand design + mechanism):* Bidentate diphosphine activity order with cis-geometry hypothesis. Depends on the proposed Ni(0)/Ni(II) catalytic cycle being operative.
- *Layer 4 (Solvent selectivity):* "Ether definitely superior to THF." Independent single-variable claim with no within-paper comparison data.

Inter-layer dependency: Layer 3 supplies the mechanistic rationale that is claimed to explain Layers 1 and 2 — but Layer 1's empirical yields stand regardless of whether Layer 3's mechanism is correct. Layer 4 is fully independent.

---

### §2 SRG / CLA → RI / ER / EP Crosswalk

---

**SRG-1 [Mechanistic cycle without experimental evidence in the dpe-Ni system]**

* **Primary RI**: RI-06 [Imported model] — the Ni(0)/Ni(II) cycle in eqs 2–4 is constructed from two precedents in different Ni systems: reductive elimination from dipy-Ni (refs 11–12) and halogen-Ni transmetalation (ref 13). The RI-06 codebook note (v0.2a) on cycle-level import is directly applicable: the entire catalytic cycle is imported, not individual steps.
* **Secondary RI**: RI-03 [Unobserved explanatory] — intermediates 1, 2, and 3 are neither isolated nor spectroscopically observed in the actual [NiCl₂(dpe)] system; all are presented as required participants in the operative cycle without kinetic constraint.
* **ER**: To claim that eqs 2–4 describe the operative mechanism in the [NiCl₂(dpe)] system, at least one elementary step (preferably transmetalation: NiCl₂(dpe) + RMgX → NiR₂(dpe)) must be demonstrated stoichiometrically in the actual dpe-Ni system, and at least one intermediate (1, 2, or 3) must be spectroscopically characterized.
* **EP**: EP-06a (Analogy-validation pack); EP-03a (Direct-observation / state-assignment pack)
* **Case-specific implementation**: Synthesize NiR₂(dpe) (intermediate 1) by treating NiCl₂(dpe) with 2 equiv RMgBr and characterize by ³¹P and ¹H NMR; confirm stoichiometric coupling upon addition of R'X (eq 3 test). For the black-precipitate issue (U-2): conduct a mercury-drop poisoning test under standard Table I conditions to discriminate homogeneous from heterogeneous catalysis.
* **Notes**: Members: B-2, B-14, U-1, U-2, U-4. B-2 carries V2=critical (only critical rating in TEMPERATURE_SUMMARY). RI-06 and RI-03 co-occur — resolving RI-06 (isomorphism demonstration via stoichiometric step) advances but does not fully resolve RI-03 (direct observation of intermediates in the catalytic system required independently). Labeling mismatch detected: "working hypothesis[REDACTED: substantial verbatim quotation; see Tier 9]reacts with," "is subsequently converted to," "forms," "is released"). Co-occurs with RI-06.

---

**SRG-2 [Selectivity claim without byproduct data]**

* **Primary RI**: RI-07 [Unsupported boundary] — "selective cross-coupling" in the title and opening sentence constitutes a negative boundary claim of the form "homo-coupling does not occur to a significant extent" without any byproduct yield data. The RI-07 extended use (v0.2a: negative boundary claims) applies. Self-contradictory absence: the paper's own eq 3 explicitly predicts R–R homo-coupling as a product of each catalytic turnover, yet no R–R yield is reported for any Table I entry.
* **Secondary RI**: RI-08 [Unquantified reliability] — the selectivity comparison against Tamura-Kochi (C-1) is made without replicate measurements or uncertainty values on either side.
* **ER**: To quantify the selectivity claim, R–R homo-coupling yield must be reported for each Table I entry (or a statistically representative subset), enabling a cross/homo selectivity ratio to replace the qualitative "selective" descriptor.
* **EP**: EP-07a (Boundary-test pack)
* **Case-specific implementation**: For each Table I entry, isolate and quantify by glpc the predicted R–R byproduct (e.g., Ph–Ph for PhMgBr entries, n-Bu–n-Bu for n-BuMgBr entries) against an authentic reference sample under the same glpc conditions used for the cross-coupled product.
* **Notes**: Members: B-1, U-1, C-1. B-1: convergence=3/3, gap=none (highest-priority item in TEMPERATURE_SUMMARY). RI-07 is doubly applicable here (positive claim: "selective") and in SRG-4 (negative claim: "only Csp² halides can be used").

---

**SRG-3 [Analytical quality of Table I yield data]**

* **Primary RI**: RI-01 [Reporting integrity] — cross-comparison among the 11 Table I entries is impossible: (i) glpc-based and isolated yields coexist without per-entry specification; (ii) yield basis differs between Examples 1 (organic halide) and 2 (Grignard reagent) with no per-entry basis stated; (iii) glpc conditions (column, stationary phase, internal standard identity/concentration) are absent; (iv) reaction times are given for only 2 of 11 entries; (v) the Table I footnote disclaims non-optimized conditions globally without per-entry differentiation.
* **Secondary RI**: RI-08 [Unquantified reliability] — no replicate measurements and no uncertainty estimates accompany any yield.
* **ER**: A uniform measurement framework is required: single yield basis (organic halide) applied consistently across all 11 entries, with glpc conditions fully stated (column type, stationary phase, internal standard, calibration curve), per-entry reaction times, and at least duplicate runs for each entry.
* **EP**: EP-01a (Reporting-coherence pack)
* **Case-specific implementation**: Rerun Table I under standardized conditions (fixed [NiCl₂(dpe)] loading, fixed reaction time, uniform ether solvent, organic-halide yield basis throughout), report glpc conditions with the identity and concentration of the internal standard, and include duplicate runs for at least three representative entries spanning the yield range.
* **Notes**: Members: B-4, B-8, B-9, B-12, B-13. B-4 and B-8 each: convergence=2/3, gap=none (TEMPERATURE_SUMMARY). RI-08 subtype (internal inconsistency) also applies: the mixed yield-basis reporting (organic halide vs. Grignard reagent) produces an internal inconsistency where the same concept (yield of one reaction) is defined relative to two different starting materials with no reconciliation stated.

---

**SRG-4 [Scope restriction to Csp² halides without experimental boundary testing]**

* **Primary RI**: RI-07 [Unsupported boundary] — [REDACTED: substantial verbatim quotation; see Tier 9] is asserted without a single failed sp³ case. No sp³ halide entry appears in Table I and the paper does not state whether sp³ halides were tested. RI-07 extended use (v0.2a) applies.
* **Secondary RI**: (none — the scope claim stands or falls on the missing failure data alone)
* **ER**: At least one sp³ halide entry (e.g., n-BuCl, EtBr) attempted under Table I conditions must be reported — either as a failed case establishing the boundary or as a successful case revising it.
* **EP**: EP-07a (Boundary-test pack)
* **Case-specific implementation**: Test n-BuCl and n-BuBr with PhMgBr under Condition A; report product yield (including any homo-coupling) to establish whether the sp²/sp³ boundary is mechanistically intrinsic (zero cross-coupled product with sp³ halides) or a consequence of non-optimized conditions.
* **Notes**: Members: B-5, B-6, A-2. SRG-4 and SRG-2 share RI-07 as primary RI (positive "selective" in SRG-2; negative "only sp²" in SRG-4). A-2 defers scope extension, which is aligned with the RI-07 non-fatal classification — the authors acknowledge the limitation but do not provide failure data.

---

**SRG-5 [Solvent and condition effects without within-paper comparison]**

* **Primary RI**: RI-09 [External superiority] — [REDACTED: substantial verbatim quotation; see Tier 9] is asserted against an external system (Tamura-Kochi THF-based catalysts) without a direct within-paper comparison of ether vs. THF under the same NiCl₂(dpe) conditions. No Table I entry uses THF; no yield in THF is reported anywhere.
* **Secondary RI**: RI-01 [Reporting integrity] — the solvent claim cannot be cross-compared without a matched-pair experiment.
* **ER**: At least one matched-pair experiment (same substrate, same [NiCl₂(dpe)] loading, same temperature/time, ether vs. THF) must be reported to substantiate the "definitely superior" solvent claim.
* **EP**: EP-09a (Internal benchmark pack)
* **Case-specific implementation**: Run m-dichlorobenzene + n-BuMgBr with [NiCl₂(dpe)] in THF under otherwise identical conditions to Example 1 (Condition A); compare isolated yield and homo-coupling byproduct yield with the ether result.
* **Notes**: Members: B-7, B-9. B-9 is shared with SRG-3 (non-optimized condition disclaimer). SRG-5 addresses the solvent-superiority assertion specifically; SRG-3 addresses the broader data-quality issue.

---

**SRG-6 [Cis/trans stilbene selectivity without analytical specification or kinetic/thermodynamic frame]**

* **Primary RI**: RI-04 [Unreplicated discriminator] — the cis/trans stilbene ratios (80:20 from cis-DCE; 43:57 from trans-DCE) are reported as single time-point measurements with neither analytical method stated nor kinetic or thermodynamic context provided. These single data points carry claimed mechanistic implications ("some interesting mechanistic implications") while remaining analytically uncharacterized.
* **Secondary RI**: RI-01 [Reporting integrity] — the method used to determine the cis/trans ratio (glpc area ratio, NMR integration, or separate isolation) is not stated, precluding reproduction.
* **ER**: The cis/trans selectivity observation requires: (i) stated analytical method for ratio determination; (ii) time-course data to distinguish kinetic vs. thermodynamic product distribution; (iii) a blank experiment confirming the [NiCl₂(dpe)] catalyst does not promote stilbene E/Z isomerization under the 20-hour reflux conditions.
* **EP**: EP-04a (Discrimination / replication pack)
* **Case-specific implementation**: Run the cis-DCE + PhMgBr reaction under Condition A at multiple time points (1, 5, 10, 20 hr); determine cis/trans stilbene ratio by ¹H NMR at each time point; separately expose stilbene to [NiCl₂(dpe)] in ether at reflux for 20 hr to test for catalyst-promoted isomerization.
* **Notes**: Members: A-1, B-11, U-3. A-1: V1=medium, V2=high; convergence=2/3, temperature_gap=low (TEMPERATURE_SUMMARY). The observation that footnote 23 frames the cis enrichment as "a facile route to cis-stilbene" — a positive reframe of an unexplained mechanistic anomaly — is a T2 inference suggesting the anomaly is treated as a utility rather than a problem.

---

**Outside the SRGs: CLAs**

---

**CLA-1: Ligand activity order attributed to cis geometry without independent mechanistic support**

* **Primary RI**: RI-05 [Qualitative overread] — the six-member ligand activity order (stated without per-catalyst yields or rates; established for one substrate combination only) is interpreted as positive evidence that [REDACTED: substantial verbatim quotation; see Tier 9] At least four structural parameters co-vary across the six Ni complexes (chelate ring size, phosphine electronics, steric bulk, denticity); the attribution to cis geometry alone is derived from a qualitative ranking without numerical support.
* **Secondary RI**: RI-04 [Unreplicated discriminator] — the order was established for one substrate combination only (n-BuMgBr + PhCl, footnote 21); generality across substrate scope is unstated.
* **ER**: Quantitative activity data (yield or TON per catalyst under identical conditions for at least 3 substrate combinations) are required; and a matched-pair experiment — one complex known to enforce cis geometry vs. one that does not — must be conducted independently to establish causation.
* **EP**: EP-05a (Quantitative-ranking substantiation pack); EP-04a (Discrimination / replication pack)
* **Case-specific implementation**: For each of the six Ni complexes, measure yield of n-BuPh cross-coupling product under identical conditions (fixed substrate loadings, time, temperature, solvent); additionally, synthesize a model trans-diorganonickel complex and determine whether it undergoes reductive elimination under the same conditions.
* **Notes**: B-3 (not in any SRG member list) + U-4 (partially overlapping SRG-1 via the mechanistic attribution but not listed as SRG-1 member). B-3: V1=medium, V2=medium/high; convergence=2/3, temperature_gap=low (TEMPERATURE_SUMMARY). RI-05 is serious here: the causal attribution of an activity ordering to a single geometric variable, when four variables co-vary, constitutes a qualitative overread. If serious, VQ-3 is at minimum "qualified."

---

**CLA-2: Concurrent Corriu-Masse communication acknowledged but not compared**

* **Primary RI**: RI-09 [External superiority] — the necessity of the bidentate phosphine ligand (and, by extension, the cis-geometry mechanistic hypothesis) cannot be established relative to the concurrent Ni(acac)₂ system (Corriu-Masse) without a direct comparison on at least one common substrate pair. The paper acknowledges "similar cross-coupling reactions" but draws no experimental distinction.
* **Secondary RI**: (none — the missing data do not yet exist at submission time)
* **ER**: A direct yield and selectivity comparison between [NiCl₂(dpe)] and Ni(acac)₂ on at least three common substrate pairs (one aryl-aryl, one alkyl-aryl, one vinyl-aryl) under matched conditions is required to establish any unique advantage of chelating phosphine coordination.
* **EP**: EP-09a (Internal benchmark pack)
* **Case-specific implementation**: Run PhMgBr + PhCl, n-BuMgBr + PhCl, and PhMgBr + CH₂=CHCl in parallel with [NiCl₂(dpe)] and Ni(acac)₂ under otherwise identical conditions; compare cross-coupling yields and homo-coupling byproduct yields.
* **Notes**: C-3 (not in any SRG). RI-09 here is of a different character than SRG-5: the comparison partner (Ni(acac)₂) was not available in the paper's primary data because the Corriu-Masse work arrived post-submission. The RI-09 therefore arises from an epistemic gap created by simultaneous discovery, not from a deliberate omission.

---

### §3 Current VQ assessment

**Current judgment: VQ-1 (Observation)**

---

**VQ-1 [Observation]: PASSES** (non-fatal)

RI-02 (Object identification): The products in Table I are structurally simple, known compounds (stilbene, di-n-butylbenzenes, vinylnaphthalene, Ph-Et) whose identities are established by comparison of physical properties with literature values and by multi-technique characterization ("glpc, nmr, ir, and/or mass spectra"). The "and/or" qualifier (B-13) is non-fatal: for known compounds with literature physical data reported, glpc retention time + at least one spectroscopic confirmation is sufficient for identity assignment at VQ-1, given 1972 era norms. The catalyst [NiCl₂(dpe)] is a known compound with cited synthesis (ref 14). VQ-1 holds with B-13 noted as non-fatal.

---

**VQ-2 [Method]: FAILS**

On the premise that RI-02 is non-fatal (VQ-1 holds), VQ-2 requires RI-01 and RI-07 to be resolved.

RI-01 (SRG-3) is unresolved: the yield measurement framework is internally inconsistent — four Table I entries report glpc-based yields while seven report isolated yields, the yield basis differs between the two detailed examples, and glpc conditions are absent. Cross-comparison among entries to assess substrate scope trends is impossible without a uniform framework.

RI-07 (SRG-2 and SRG-4) is doubly unresolved: (i) the "selective" claim (SRG-2) carries no byproduct yield data for any Table I entry — the paper's own eq 3 predicts R–R formation per turnover, yet no R–R yield is reported; (ii) the sp²-only scope restriction (SRG-4) is asserted without a single failed sp³ halide entry.

VQ-2 fails: RI-01 (SRG-3) and RI-07 (SRG-2, SRG-4) are all unresolved.

---

**VQ-3 [Mechanism]: FAILS** (inherits VQ-2 failure)

On the premise that VQ-2 were achieved, VQ-3 requires RI-03, RI-04, and RI-06 to be resolved.

RI-06 (SRG-1) is unresolved: the catalytic cycle in eqs 2–4 is imported from dipy-Ni systems (refs 11–12) and general transmetalation precedents (ref 13) without any stoichiometric step demonstrated in the actual [NiCl₂(dpe)] system.

RI-03 (SRG-1) is unresolved: intermediates 1, 2, and 3 are presented as operative but are neither isolated, spectroscopically observed, nor kinetically constrained in the [NiCl₂(dpe)] system.

RI-04 (SRG-6 and CLA-1) is unresolved: the cis/trans stilbene ratios are single time-point measurements without analytical or kinetic context; the ligand activity order is from one substrate combination only.

Additionally, RI-05 (CLA-1) is serious: the causal attribution of the activity order to cis geometry, with four co-varying structural parameters, constitutes a qualitative overread. VQ-3 would be **qualified** even if RI-03, RI-04, and RI-06 were resolved, unless RI-05 is also addressed.

VQ-3 fails (inherits VQ-2 failure; additionally RI-06, RI-03, RI-04 unresolved; VQ-3 would be qualified due to RI-05).

---

**VQ-4 [Benchmark]: FAILS** (inherits VQ-3 failure)

On the premise that VQ-3 were achieved, VQ-4 requires RI-08 and RI-09 to be resolved.

RI-08 (SRG-3) is unresolved: no replicate measurements appear for any Table I entry.

RI-09 (SRG-5 and CLA-2) is doubly unresolved: the ether-superiority claim (SRG-5) lacks a within-paper matched-pair comparison; the advantage of [NiCl₂(dpe)] over Ni(acac)₂ (CLA-2) cannot be assessed without a direct comparison experiment.

VQ-4 fails (inherits VQ-3 failure; additionally RI-08 and RI-09 unresolved).

---

**Layered VQ asymmetry:**

- **Layer 1 (Synthetic utility)** on its own: reaches VQ-1 (product identities established; yields reported). Fails VQ-2 due to RI-01 (inconsistent yield framework, SRG-3) and RI-07 (selectivity unquantified, SRG-2). This is the most advanced layer.
- **Layer 2 (Chloride reactivity)** on its own: fails VQ-2 due to RI-09 (no within-paper bromide/iodide comparison for any substrate; SRG-5 analog).
- **Layer 3 (Ligand design + mechanism)** on its own: fails VQ-2 due to RI-05 (qualitative overread, CLA-1) and fails VQ-3 due to RI-06 + RI-03 (SRG-1). This is the most fragile layer — the cis-geometry hypothesis is the farthest from experimental validation.
- **Layer 4 (Solvent selectivity)** on its own: fails VQ-2 due to RI-09 (no within-paper ether vs. THF data; SRG-5). This is the weakest independent claim.

Layer 1 is the most robust: it reaches VQ-1 with non-fatal qualifications and requires only quantitative improvements (RI-01, RI-07) to reach VQ-2. Layers 3 and 4 fail VQ-2 on the basis of missing comparison data and missing mechanistic validation, respectively.

---

### §4 Era-Norm Annotation

**communication-era tolerated:**

- **B-1** (no byproduct quantification for "selective[REDACTED: substantial verbatim quotation; see Tier 9]selective" in synthetic chemistry was primarily yield-based rather than byproduct-ratio-based.
- **B-4** (absent glpc conditions): glpc was a routine identification and yield-measurement tool in 1972 synthetic chemistry whose specific conditions (column, stationary phase) were often considered proprietary or reportable only in full papers, not communications.
- **B-8** (reaction times for only 2 of 11 entries): abbreviated experimental sections that provided full detail for only representative examples and omitted reaction times for the remaining scope entries were standard practice for JACS Communications.
- **B-13** (generic "and/or" characterization disclaimer): characterization by one or more of glpc, NMR, IR, MS without full per-compound data tables was within the reporting norm for 1972 JACS Communications, where the primary function was to establish product identity rather than provide complete spectral assignments.
- **A-1** (deferred mechanistic explanation): explicitly deferring stereochemical and mechanistic understanding to future work was and remains standard practice for initial synthetic communications reporting newly discovered reactions.
- **A-2** (deferred scope extension): stating "investigations are continuing" as a prospective notice was a standard genre convention for initial reports, not a reportable omission.

**modern-era deficient:**

- **B-1** (no byproduct quantification): modern reporting standards for a paper claiming "selective[REDACTED: substantial verbatim quotation; see Tier 9]selective" an operational definition; the 1972 non-reporting would fail peer review today.
- **B-2 + B-14** (catalytic cycle without NiCl₂(dpe)-system validation): presenting eqs 2–4 as the operative mechanism — rather than as a speculative model — without any stoichiometric step validated in the actual [NiCl₂(dpe)] system would not survive modern mechanistic review.
- **B-3** (qualitative activity order without per-catalyst yield/rate data): modern structure–activity reporting requires numerical yield or TON values for each catalyst in a comparative series; a verbal ordering without data is insufficient. [Also dual-classified.]
- **B-7** (no THF comparison data for "definitely superior" solvent claim): "definitely superior" is a comparative claim that modern reporting requires to be supported by at least one matched-pair experiment (same substrate, same catalyst loading, ether vs. THF).
- **B-10** (black precipitate uncharacterized): in the modern context of Ni-catalysis mechanism debates, the observation of a black precipitate during a "homogeneous" catalytic reaction requires characterization (TEM for nanoparticle size/morphology, Hg-drop poisoning test, filtration experiment) to rule out heterogeneous catalysis or catalyst decomposition.

**Dual classification (tolerated then but deficient now):**

- **B-1**: Communication-era tolerated (selectivity established by yield, not byproduct ratio) but modern-era deficient (selectivity ratio against homo-coupling is now required when "selective" appears in the title).
- **B-3**: Communication-era tolerated (qualitative catalyst ranking in a single footnote was acceptable for a 1972 communication) but modern-era deficient (quantitative TON or yield per catalyst is now required to support a structure–activity conclusion about the "first requisite" of catalyst design).
- **B-13**: Communication-era tolerated (per-compound spectral data tables were not required in 1972 JACS Communications) but modern-era deficient (full NMR/MS data with assignments are now required for each new compound in a communication or article).

---

### §5 Shortest-reinforcement route

**Current VQ: VQ-1. First objective: VQ-2.**

**Shortest route to VQ-2:**

1. **EP-07a** (Boundary-test pack) — quantify R–R homo-coupling product (R–R byproduct yield by glpc with authentic R–R reference) for each Table I entry under the reported conditions; add at least one sp³ halide trial (e.g., n-BuCl + PhMgBr) to establish or revise the sp²-only scope boundary.
   Advances RI-07 (SRG-2: "selective" claim operationalized; SRG-4: sp²-only restriction tested with failure data). Highest information gain — resolves two RI-07 instances simultaneously and provides data predicted by the paper's own eq 3.

2. **EP-01a** (Reporting-coherence pack) — standardize all Table I yields to a single basis (organic halide), report full glpc conditions (column, stationary phase, internal standard identity and concentration), and add per-entry reaction times for the remaining 9 Table I entries.
   Advances RI-01 (SRG-3: reporting-framework inconsistency resolved; cross-entry comparison enabled). Secondary advance: RI-08 partial (replicate data for at least 3 entries recommended alongside standardization).

Certification-gate note: The experimental investment order follows information gain (EP-07a first to address the central "selective" claim, EP-01a second to standardize the yield framework), but final VQ-2 certification requires both RI-01 and RI-07 to be resolved — neither alone is sufficient, and the gate order VQ-1 → VQ-2 → VQ-3 → VQ-4 is fixed by the inheritance principle.

---

**Second objective: VQ-3 (prerequisite: VQ-2 achieved)**

**Shortest route to VQ-3:**

1. **EP-06a** (Analogy-validation pack) — demonstrate at least one stoichiometric elementary step of eqs 2–4 in the actual [NiCl₂(dpe)] system: treat NiCl₂(dpe) with 2 equiv n-BuMgBr and characterize the resulting complex by ³¹P and ¹H NMR to confirm or refute formation of intermediate 1 (NiR₂(dpe)).
   Advances RI-06 (SRG-1: isomorphism between imported dipy-Ni model and target dpe-Ni system tested) and simultaneously advances RI-03 (SRG-1: intermediate 1 observed or excluded). Highest information gain — a single stoichiometric experiment addresses the root of both RI-06 and RI-03 for the most important intermediate.

2. **EP-05a** (Quantitative-ranking substantiation pack) — measure cross-coupling yield and R–R homo-coupling yield for each of the six Ni complexes in the activity order under identical, standardized conditions (same substrate, same loading, same temperature and time).
   Advances RI-05 (CLA-1: replaces qualitative ranking with quantitative activity data; necessary to remove the VQ-3 "qualified" status arising from the cis-geometry qualitative overread).

3. **EP-04a** (Discrimination / replication pack) — run the cis-DCE + PhMgBr reaction at 1, 5, 10, and 20 hours and measure the cis/trans stilbene ratio at each time point by ¹H NMR; separately test whether [NiCl₂(dpe)] promotes stilbene E/Z isomerization under reflux conditions.
   Advances RI-04 (SRG-6: kinetic vs. thermodynamic character of the isomer distribution determined; stilbene isomerization pathway excluded or quantified).

Certification-gate note: The experimental investment order follows information gain (EP-06a → EP-05a → EP-04a), but final VQ-3 certification follows the inheritance principle: VQ-2 must be fully certified before VQ-3 assessment can proceed, and VQ-3 is "qualified" until RI-05 (CLA-1) is resolved — EP-05a cannot be deferred if VQ-3 (non-qualified) is the target.

---

### §6 Contribution to institutional design

**1. RI-06 cycle-level import: new representative case confirmed.**
SRG-1 provides a clear example of full catalytic cycle import: the entire Ni(0)/Ni(II) cycle (eqs 2–4) is assembled from two separate non-dpe-Ni precedents (refs 11–12 for reductive elimination; ref 13 for transmetalation) and presented as the operative mechanism of the [NiCl₂(dpe)] system without any stoichiometric step validated in the target system. This confirms and extends the RI-06 codebook note (v0.2a) on "cycle-level import.[REDACTED: substantial verbatim quotation; see Tier 9]two precedents from different Ni complexes assembled into one cycle for a third Ni complex."

**2. Labeling mismatch pattern confirmed.**
The paper labels its mechanistic proposal as "working hypothesis[REDACTED: substantial verbatim quotation; see Tier 9]reacts with," "is subsequently converted to," [REDACTED: substantial verbatim quotation; see Tier 9] The hypothesis label is concentrated in one sentence; the narrative body asserts the mechanism as fact. This exactly matches the "Labeling mismatch" detection criterion. Co-occurrence with RI-06 is confirmed. Recommended institutional note: labeling mismatch tends to occur when a cycle is imported from another system (RI-06) — the authors use declarative language consistent with the known behavior of the source system, then hedge only at the end.

**3. Automatic-resolution pattern via Communication→Full Paper: applicable.**
RI-01 items (B-4 absent glpc conditions, B-8 absent reaction times, B-13 generic characterization) and RI-07 items that arise from page constraints (B-1 no byproduct data) are highly likely to be resolved in the Kumada group's anticipated follow-up full paper(s). These represent the "Automatic-resolution pattern via Communication→Full Paper transition" — RI-01 and RI-07 arise from page-limit constraints and can be expected to disappear when the full paper is published. Cross-reference with §4 era-norm annotation: these items are dual-classified (communication-era tolerated, automatic-resolution expected). Recommended for tracking: when full papers are available for this reaction series, verify whether B-1 (selectivity quantification), B-3 (per-catalyst yield data), and B-7 (ether vs. THF comparison) were resolved.

**4. PRI-11 boundary case identified — "kinetics absent" vs. "kinetics decoupled."**
PRI-11 is defined as [REDACTED: substantial verbatim quotation; see Tier 9] In the Kumada 1972 paper, no kinetic data are reported at all — the mechanism is supported purely by analogy from another system (RI-06), not by any agreement with rate orders (because no rate orders were measured). This represents a more primitive case than PRI-11's definition: not "mechanism decoupled from kinetics" but "mechanism proposed with kinetics entirely absent." Recommended institutional note: PRI-11's definition should be accompanied by a note distinguishing (a) mechanism supported only by observed rate orders (PRI-11 as defined) from (b) mechanism proposed without any kinetic data whatsoever — the latter is better described as RI-06 + RI-03, not PRI-11. The Kumada 1972 case is Category (b).

**5. RI-09 dual-character identified: deliberate omission vs. epistemic gap.**
CLA-2 (Corriu-Masse not compared) represents a form of RI-09 where the comparison partner did not exist in the primary data at submission time (concurrent independent discovery). This is structurally different from the typical RI-09 case where the comparison is available but not conducted (e.g., SRG-5's ether vs. THF). Recommended codebook annotation: RI-09 should distinguish (a) external superiority asserted without available comparison data (SRG-5 type) from (b) external superiority unresolvable at time of submission due to concurrent discovery (CLA-2 type). Both are RI-09, but their remediation timelines differ (immediate vs. post-concurrent publication).

inference_time_sec: not available — inject externally
```

---

> **Tier 8 redaction notice**: This file is a redacted copy of the corresponding Tier 3 / Tier 9 output. Verbatim source-paper quotations have been replaced by `[REDACTED: see source paper §<loc>; full text retained in Tier 9 reviewer-only deposit]` markers, preserving location references and our own analytical content. Bibliographic fields (title, authors, journal, year, DOI), analytical labels (`evidence_chain:` with B-/U-/A-/C- internal IDs), short technical terms, and our own analytical text are not redacted. The redaction was applied by `scripts/redact_for_tier8.py` and, for this version, by `scripts/build_paperA_R1_public.py` with `scripts/redact_source_ngram_runs.py` (scripts of the project repository; they are not deposited).
