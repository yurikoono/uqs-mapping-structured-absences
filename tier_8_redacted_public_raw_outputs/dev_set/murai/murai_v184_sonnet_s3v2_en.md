prompt_version: stage3-v2-en-20260419
model_info: claude-sonnet-4-6

# Re-certification Assessment Sheet for Scientific Knowledge

## Murai et al. 1993 (Nature, Article)

---

### §1 Claim Architecture

**Core claim summary:**

The paper advances a single integrated claim: that RuH2(CO)(PPh3)3 catalyses the
coupling of aromatic C–H bonds with olefins through a chelation-assisted mechanism,
achieving simultaneously (a) near-quantitative yields from both starting materials without
using either in stoichiometric excess as solvent (Efficiency / N-1, SC-1), (b) virtually
100% regioselectivity at the ortho aromatic position and anti-Markovnikov olefin
terminus (Selectivity / N-2, SC-3), and (c) broad substrate scope across acylbenzenes,
acylheteroaromatics, and a range of terminal olefins (Generality / N-3). A mechanistic
attribution — chelation assistance via a five-membered cyclometallated Ru intermediate
— is advanced as both explanation and design principle (N-4), with a programmatic
extrapolation that the approach "should be applicable more widely for selective
organometallic catalysis" (N-5).

**Novelty pillar:** The paper claims an absolute historical first: "[REDACTED: verbatim source text; see the source paper via its DOI]" (efficiency
qualifier on N-1). The novelty axis is simultaneously quantitative (yield parity from both
components) and scope-based (generality across substrate classes previously beyond the
state-of-the-art).

**Utility pillar:** The paper frames the reaction as meeting "efficiency, selectivity and
generality required for practical organic synthesis" — invoking synthetic practicability,
not merely chemical curiosity. The Applications section positions chelation assistance
as a transferable design principle, extending utility beyond the demonstrated chemistry.

**Layered structure judgment:**

The claim architecture has three functionally independent layers that cannot be mutually
refuted by a single experimental attack:

- **Layer A — Efficiency and yield data:** The quantitative yield claims (runs 8–13,
  GC and isolated yields) are anchored in experimental outcomes. A refutation of the
  mechanism does not collapse Layer A; a GC recalibration challenge does not collapse
  the isolated-yield entries. This layer is the most empirically robust.

- **Layer B — Selectivity claim:** The virtual 100% regioselectivity assertion rests
  on the observation that only one of four possible regioisomers is detected. A refutation
  of the chelation model as the mechanistic explanation for selectivity would not
  automatically refute the selectivity data, only the explanation for it. Layer B is
  empirically observable but analytically underspecified.

- **Layer C — Mechanistic and programmatic claims:** The chelation-assistance
  mechanism (N-4) and the broader-applicability extrapolation (N-5) form an
  independent layer that could be challenged without touching the yield or selectivity
  data. The explicit deferral ("[REDACTED: verbatim source text; see the source paper via its DOI]" A-1) partially insulates this layer from falsification while retaining its
  rhetorical function.

**Inter-layer dependencies:** Layer C is narratively required to explain Layer B
(ortho selectivity is attributed to the chelate geometry), but empirically decoupled from
it. Layer B's selectivity data could in principle be confirmed while the chelation model
is refuted and replaced. Layer A is essentially independent of both B and C. This means
that a finding disproving the cyclometallated intermediate (U-1) would damage Layer C
and undermine the explanation for Layer B, but would not touch the yield data in Layer A.

---

### §2 SRG / CLA → RI / ER / EP Crosswalk

**SRG-1 [Quantitative evidence base]**
Member items: B-1, B-2, B-3, B-4

* **Primary RI**: RI-01 [Reporting integrity] — Cross-comparison is impossible due to
  inconsistent measurement frames: GC yields without calibration method for 10 of 13
  runs, no numerical TOF values, qualitative-only catalyst comparison, and undefined
  "standard methods" for structure determination.
* **Secondary RI**: RI-09 [External superiority] — the TOF superiority claim ("among
  the highest reported") asserts superiority over refs 11/12 without a common numerical
  comparison.
* **ER**: For the efficiency and TOF claims to be independently verifiable, every
  yield must be traceable to a calibrated analytical method (GC internal standard,
  response factors), all TOF values must be tabulated numerically alongside the literature
  comparators being surpassed, and the catalyst comparison must report yield data under
  uniform conditions.
* **EP**: EP-01a [Reporting-coherence pack]; EP-09a [Internal benchmark pack]
* **Case-specific implementation:**
  - EP-01a: Report GC yields for all 13 runs with a common internal standard (e.g.,
    mesitylene or dodecane), validated response factors for each product class (silane-
    containing products, non-silane products), and isolated yields for all runs currently
    reporting only GC values (runs 2, 4, 5, 7, 9, 10, 11, 12).
  - EP-09a: Tabulate numerical TOF values (mol product mol⁻¹ Ru h⁻¹) for runs 1, 9,
    and 10 alongside the TOF values from refs 11 (Jordan & Taylor) and 12 (Moore et al.)
    under the conditions reported in those papers, using a defined denominator (total Ru
    loaded or independently determined concentration of active catalyst).
* **Notes:** B-1 and B-2 are high_convergence_low_gap (V1=high, V3=high, convergence
  2/3, gap=none). B-3 is the sole B-item with three-field convergence (V1=medium,
  V2=medium, V3=medium, convergence 3/3, gap=none). SRG-1 is the quantitative
  infrastructure on which all three performance axes rest; none of the three performance
  claims (efficiency, TOF, scope) can be independently verified without resolving RI-01.
  B-2 ↔ C-1 forms a closed loop: the TOF superiority claim is asserted but never
  numerically grounded.

---

**SRG-2 [Catalytic cycle evidence absent]**
Member items: A-1, U-1, U-2

* **Primary RI**: RI-03 [Unobserved explanatory] — the cyclometallated Ru intermediate
  shown in Fig. 1, which is the paper's sole mechanistic warrant for ortho selectivity,
  is neither isolated, spectroscopically observed under catalytic conditions, nor
  kinetically constrained.
* **Secondary RI**: RI-06 [Imported model] — the mechanistic analogies in refs 14
  and 15 (stoichiometric Mn(I)/Ru(II) cyclometallation) are imported without
  demonstrating isomorphism with a catalytic Ru(0) oxidative-addition mechanism.
* **ER**: For the catalytic mechanism to be considered established at VQ-3, at
  minimum: (a) the proposed five-membered Ru metallacycle must be directly observed
  (isolation, ³¹P{¹H} NMR under catalytic conditions, or trapping) or kinetically
  constrained (rate data consistent with it as the resting state); (b) the conversion of
  the Ru(II) pre-catalyst to the proposed Ru(0) active form must be demonstrated
  (e.g., by a control reaction using a Ru(0) source, or by detecting H2 evolution during
  the induction period).
* **EP**: EP-03a [Direct-observation / state-assignment pack]; EP-06a [Analogy-
  validation pack]
* **Case-specific implementation:**
  - EP-03a: Attempt stoichiometric cyclometallation of acetophenone with
    RuH2(CO)(PPh3)3 under dilute toluene conditions (without added olefin) and
    characterise the product by ³¹P{¹H} NMR and, if crystals are obtained, single-
    crystal X-ray diffraction; alternatively, conduct in-situ IR monitoring under
    catalytic conditions to detect characteristic Ru–H and Ru–C stretching modes
    expected for the metallacycle. For the active-species question (U-2), use a Ru(0)
    complex (e.g., Ru(CO)2(PPh3)3 or a known Ru(0) source) as a direct pre-catalyst
    comparison, and monitor H2 evolution (mass spectrometer headspace or GC) during
    the early phase of the reaction with RuH2(CO)(PPh3)3.
  - EP-06a: Assess the mechanistic equivalence of the refs 14/15 Mn(I)/Ru(II)
    carboxylate cyclometallation precedents to the proposed Ru(0) oxidative-addition
    pathway by constructing a reaction coordinate comparison; quantify the oxidation-
    state discrepancy and specify what additional evidence would be required to bridge
    electrophilic cyclometallation (refs 14/15) and oxidative addition (proposed).
* **Notes:** U-1 is classified high_convergence_low_gap (V2=critical, V3=critical,
  convergence 2/3, gap=none) and also low_convergence_high_gap (V2 critical, V2-Q4).
  U-2 connects to B-3 (chloride vs. hydride inactivity) as diagnostic datum unexploited.
  A-1 is the paper-explicit deferral that creates the protective umbrella for both U-1
  and U-2. RI-06 applies at cycle level: the entire proposed catalytic cycle is
  constructed from mechanistically distinct precedents without demonstrated isomorphism.

---

**SRG-3 [Selectivity basis absent]**
Member items: B-8, B-9, B-10, U-4

* **Primary RI**: RI-04 [Unreplicated discriminator] — the run 10 vs. run 11 rate
  comparison and the 1-indanone negative result are each single data points with high
  discriminatory interpretive weight (ring-strain hypothesis), evaluated without kinetic
  parameters, and the regioselectivity claim ("virtually 100%") is asserted without
  confirmed detection limits for non-observed isomers.
* **Secondary RI**: RI-05 [Qualitative overread] — the mechanistic significance of
  the run 10/11 rate difference (attributed solely to ring strain) and the 1-indanone
  unreactivity are derived from qualitative rankings (fast/slow/no reaction) without
  quantitative rate constants or activation parameters.
* **ER**: For the selectivity claims to be established beyond a single-point observation,
  kinetic data (rate constants or at minimum initial-rate ratios) are required for the
  run 10/11 comparison, the conditions and detection threshold for the 1-indanone
  experiment must be specified, and the three non-observed regioisomers for at least
  one representative run must be confirmed absent at a defined GC or NMR detection
  limit.
* **EP**: EP-04a [Discrimination / replication pack]; EP-05a [Quantitative-ranking
  substantiation pack]
* **Case-specific implementation:**
  - EP-04a: For the run 10/11 comparison, measure initial rates (GC aliquots at defined
    time intervals) under identical conditions for tetralone ketone (run 10) and the ring-
    expanded analogue (run 11); report rate constants and, if possible, Eyring parameters.
    For 1-indanone: run the standard conditions (2/2/0.04 mmol, toluene reflux, 135 °C,
    20 h) and report the GC yield of any ortho-alkylated product at a defined detection
    limit (≤1% recommended given the 88% yield for the structural congener, run 11).
  - EP-05a: For one representative run (e.g., run 9 or 10 with vinyl triethoxysilane),
    prepare the three alternative regioisomers (meta-alkylated, para-alkylated,
    Markovnikov-addition product) synthetically or by an independent route, add as
    internal standards, and quantify their yield from the standard reaction by co-injection
    GC at a defined detection limit.
* **Notes:** B-8 and B-9 are high_convergence_low_gap (V1=medium, V2=high,
  convergence 2/3, gap=low). U-4 is classified "self-contradictory absence": the paper
  claims "virtually 100%" while never confirming isomer absence analytically. RI-05
  is secondary here; it does not reach the threshold for VQ-3 qualification on its own,
  but co-occurs structurally with RI-04 (see §6).

---

**SRG-4 [Scope claims exceed data]**
Member items: B-5, U-3, B-7

* **Primary RI**: RI-07 [Unsupported boundary] — the claim that the reaction applies
  to "a variety of aromatic systems" is a positive scope boundary stated without failure
  examples for non-ketone directing substrates, and the broader applicability assertion
  in the Applications section is a positive boundary claim without any non-ketone
  directed experiment.
* **Secondary RI**: RI-01 [Reporting integrity] — B-7 (bilateral quantitative yield
  claim without olefin mass balance) means the "quantitative from both" framing is
  internally inconsistent: runs using olefin excess (4–10 mmol olefin vs. 2 mmol
  ketone) cannot support a claim that both starting materials are consumed quantitatively
  in the product.
* **ER**: For the scope claim to be internally consistent, the abstract-level framing
  ("a variety of aromatic systems") must be qualified to "aromatic ketone systems" or
  supplemented with at least one non-ketone directed substrate, and all bilateral-
  quantitative-yield claims must be accompanied by olefin consumption data (GC of
  remaining olefin or identified olefin-derived by-products).
* **EP**: EP-07a [Boundary-test pack]; EP-01a [Reporting-coherence pack]
* **Case-specific implementation:**
  - EP-07a: Test at least one non-carbonyl directing substrate — an aryl imine, an
    N-aryl amine, or an arylphosphine oxide — under the standard catalytic conditions
    to determine whether the directing requirement is strictly limited to ketone carbonyls
    or extends to other heteroatom donors. Report the yield (even if zero) with GC
    detection limits.
  - EP-01a: For runs 8–13 reporting bilateral quantitative yield, monitor olefin
    consumption by GC (internal standard, aliquots at defined time points) and report
    the fate of any excess olefin (isomerisation, oligomerisation, recovered starting
    material). For runs with excess olefin (4–10 mmol olefin vs. 2 mmol ketone), revise
    the efficiency description to specify the yield basis (ketone-based, not bilateral).
* **Notes:** B-5 is classified "mixed" (intentional narrowing + methodological
  limitation). U-3 is "self-contradictory absence": the abstract's scope claim is not
  supported by the table contents. B-7 introduces a RI-08 subtype (internal
  inconsistency: "quantitative from both" is formally incompatible with >1:1 olefin
  loading); secondary RI-01 captures this. SRG-4 is the scope-architecture counterpart
  to SRG-1's analytical architecture.

---

**SRG-5 [Prior art not engaged numerically]**
Member items: C-1, B-2

* **Primary RI**: RI-09 [External superiority] — the paper's superiority claim over
  refs 11 and 12 (Jordan & Taylor 1989; Moore et al. 1992) is asserted in qualitative
  language (by-products, isomer mixtures, limited substrate scope) without a direct
  numerical comparison of yield, TON, or TOF on a common substrate or reaction class.
* **Secondary RI**: RI-01 [Reporting integrity] — the absence of numerical TOF values
  in the current paper (B-2) makes the comparison with refs 11/12 structurally
  impossible even in principle, compounding the RI-09 pattern.
* **ER**: For the competitive-positioning claim to stand, at least one direct numerical
  comparison — the paper's TOF/TON for a reaction type representable by refs 11/12,
  or a common substrate run side by side — must be reported, or the limitations of refs
  11/12 must be reproduced under the present conditions as a control.
* **EP**: EP-09a [Internal benchmark pack]
* **Case-specific implementation:** For runs 1, 9, and 10, report the actual TOF value
  (mol product mol⁻¹ Ru h⁻¹ at a defined time point) and cite the corresponding TOF
  from the Jordan & Taylor (ref 11) and Moore et al. (ref 12) papers, with the denominator
  and time basis stated for each, to allow a common-unit comparison.
* **Notes:** SRG-5 is a secondary SRG closely coupled to SRG-1 (the TOF claim in B-2
  is common to both). B-2 ↔ C-1 is the clearest closed-loop instance in the paper:
  the superiority claim (B-2) depends on a tabulated numerical comparison (C-1) that
  is asserted but never provided.

---

**Outside the SRGs: CLAs**

**CLA-1: Candidate 5 — Kinetic/thermodynamic basis for dual regioselectivity**

Candidate 5 addresses the selectivity question at a level above what SRG-3 fully captures:
SRG-3 treats the detection-limit issue and the single-comparator rate argument; Candidate
5 extends to the unasked question of whether the selectivity is kinetically or
thermodynamically controlled, and what the transition-state structure of the rate-
determining C–H cleavage step is.

* **Primary RI**: PRI-11 candidate [Mechanism–kinetics decoupling] — the proposed
  catalytic cycle (chelation → C–H oxidative addition → migratory insertion → reductive
  elimination) is not used to derive a rate law algebraically, and the observed selectivity
  is attributed to the chelate geometry without a kinetic equation linking chelation
  geometry to selectivity.
* **Secondary RI**: RI-03 [Unobserved explanatory] — the C–H cleavage transition
  state, which would directly determine the ortho/meta/para competition, is neither
  computed nor experimentally characterised.
* **ER**: For the selectivity to be mechanistically grounded, a kinetic isotope effect
  measurement (kH/kD with ortho-deuterated aromatic ketone) must confirm that C–H
  cleavage is rate-determining, and a rate law derived from the proposed cycle must
  account for the observed dependence on Ru, ketone, and olefin concentrations.
* **EP**: EP-10a [Kinetic verification pack (provisional)]; EP-04a [Discrimination /
  replication pack]
* **Case-specific implementation:**
  - EP-10a: Measure kH/kD using acetophenone-d0 vs. acetophenone-d4 (ortho positions
    fully deuterated) under the standard catalytic conditions; a primary KIE (kH/kD > 2)
    would confirm C–H cleavage as the rate-determining step, which is the mechanistic
    prerequisite for chelation geometry as the selectivity determinant.
  - EP-04a: Measure initial rate (GC aliquots at ≤5 min intervals in a 30-minute
    window) as a function of [Ru], [ketone], and [olefin] separately to extract partial
    orders; compare the order in Ru to the coordination equilibrium predicted by the
    proposed chelation-first cycle.
* **Notes:** PRI-11 pattern: the proposed cycle predicts a rate law that is never
  derived algebraically; the mechanism is supported only by the qualitative agreement
  between the observed chemoselectivity and the predicted chelation geometry, without
  a quantitative bridge. This is structurally isomorphic to the PRI-11 pattern
  confirmed in Breitenfeld 2014 / Pengfei 2024. If confirmed across a third paper, this
  strengthens the case for promotion. Grounded in B-8, B-9, B-10, U-4.

---

**CLA-2: Candidate 8 — Catalyst structure–activity relationship**

Candidate 8's grounded_in items (B-3, B-6) are members of SRG-1 at the B-3 level,
but the deeper question — what structural feature determines activity — is not fully
captured by SRG-1's RI-01 framing.

* **Primary RI**: RI-05 [Qualitative overread] — the six-complex catalyst comparison
  ("equally effective," "modestly effective," "not effective") derives structural and
  electronic implications from qualitative rankings without any quantitative yield, rate,
  or spectroscopic data under comparable conditions.
* **Secondary RI**: RI-03 [Unobserved explanatory] — the mechanistic reason why
  RuHCl(CO)(PPh3)3 is inactive while RuH2(CO)(PPh3)3 is active is unobserved; the
  implied Ru(II)→Ru(0) activation via H2 reductive elimination is the explanatory species
  that is neither proposed nor tested.
* **ER**: For the catalyst structure–activity relationship to be characterized, quantitative
  yield data (GC yield at a defined time point under uniform conditions) must be reported
  for all compared complexes, and the mechanistic implication of the hydride-vs-chloride
  activity difference must be tested (e.g., by monitoring H2 evolution during pre-catalyst
  activation or by direct Ru(0) complex comparison).
* **EP**: EP-05a [Quantitative-ranking substantiation pack]; EP-03a [Direct-
  observation / state-assignment pack]
* **Case-specific implementation:**
  - EP-05a: Run each of the five alternative Ru complexes under identical standard
    conditions (acetophenone + vinyl triethoxysilane, 2/2/X mmol, reflux toluene, 4 h)
    and report GC yield with a common internal standard; normalise loading to 2 mol%
    Ru for all.
  - EP-03a: Monitor the early-phase reaction (first 30 min) of RuH2(CO)(PPh3)3 under
    the standard conditions by in-situ IR or ³¹P{¹H} NMR in refluxing toluene-d8 to
    detect H2 loss (induction period) and identify the activated Ru species.
* **Notes:** B-3 has three-field convergence (V1=medium, V2=medium, V3=medium;
  convergence 3/3, gap=none). The structural implication of the RuHCl/RuH2 distinction
  is the most mechanistically informative datum in the paper that goes unexploited.

---

### §3 Current VQ assessment

**Current judgment: VQ-2 (qualified)**

---

**VQ-1 [Observation]: holds (non-fatal)**

The core synthetic observation — that mixing RuH2(CO)(PPh3)3 with an aromatic ketone
and a terminal olefin in refluxing toluene produces an ortho-alkylated aromatic ketone —
is supported by isolated product characterisation via "standard methods" (B-4). For three
runs, isolated yields are reported (runs 3, 6, 13 in parentheses). The paper's product
identities are established at a level consistent with 1993 Nature communication
conventions (NMR, elemental analysis or HRMS, implied by "standard methods"). RI-02
is judged **non-fatal**: the statement "standard methods" is under-descriptive
(B-4), but the consistency of the 13 runs' reported products across the substrate scope
table provides collective structural plausibility sufficient for observation-level
certification.

Qualification note: B-4 is formally deficient (RI-02 partially active), but the
non-fatal judgment rests on the 1993 communication-era norm (§4) and the
collective internal consistency of Table 1.

---

**VQ-2 [Method]: holds (qualified) — on the premise that VQ-1 is non-fatal**

VQ-2 inherits VQ-1 (non-fatal).

The GC-yield method is described at a minimum level (yields determined by GC, isolated
yields in parentheses), and a subset of runs has isolated yields confirming the GC results.
RI-01 is partially resolved for those runs. However, RI-01 remains **partially active**:
GC calibration (internal standard, response factors) is absent for all 13 runs, isolated
yields are missing for 10 runs, olefin mass balance is not reported (B-7), and the
measurement frame for the TOF claim is undefined (B-2). The judgment is **qualified**
rather than full because RI-01's active residual means the quantitative precision of the
efficiency claims cannot be independently verified. RI-07 (unsupported scope boundary,
SRG-4) is also partially active: the abstract-level scope claim ("a variety of aromatic
systems") is broader than the method actually demonstrates.

Qualification grounds: RI-01 (SRG-1) and RI-07 (SRG-4) remain partially active;
VQ-2 holds in qualified form because the analytical basis is present in principle (GC
yields, isolated yields for a subset) but incompletely documented.

**However, Layer A (yield data) on its own:** The isolated-yield entries (runs 3, 6, 13)
and the GC yields for equimolar runs 8–13 collectively support VQ-2 for the specific
claim that "some reactions achieve near-quantitative yields." This sub-layer reaches VQ-2
in unqualified form. The broader quantitative-comparison and TOF claims (SRG-1 + SRG-5)
remain at qualified VQ-2.

---

**VQ-3 [Mechanism]: fails**

VQ-3 inherits VQ-1 (non-fatal) and VQ-2 (qualified).

VQ-3 requires resolution of RI-03, RI-04, and RI-06. All three remain seriously active:

- **RI-03 (SRG-2):** The cyclometallated Ru intermediate (U-1) is neither isolated,
  spectroscopically observed, nor kinetically constrained. The Ru(0) active species (U-2)
  is not confirmed. The mechanistic edifice rests entirely on a proposed species that has
  no direct experimental support in this paper.
- **RI-04 (SRG-3):** The run 10/11 rate comparison and the 1-indanone unreactivity
  (B-8, B-9) are each single data points interpreted at mechanistic weight without
  kinetic parameters. The regioselectivity claim (B-10, U-4) lacks confirmed detection
  limits for non-observed isomers.
- **RI-06 (SRG-2):** The Mn(I)/Ru(II) carboxylate cyclometallation precedents (refs
  14/15, C-2) are mechanistically distinct from the proposed Ru(0) oxidative addition,
  and the analogy is imported without isomorphism demonstration. Ref 17 (olefin OA to
  Ru) is similarly distinct from aromatic C–H OA. RI-06 applies at cycle level.
- **RI-05 (CLA-2):** The qualitative catalyst ranking (B-3) is a qualified co-occurrence
  with RI-04 and RI-06; RI-05 is not lethally active on its own but reinforces the
  mechanism-level failure.

Lethality: RI-03 is **fatal** at VQ-3 for the mechanistic claim (N-4): the paper's
central selectivity rationale depends on the cyclometallated intermediate, which is
experimentally absent. RI-04 is **non-fatal** for the selectivity data themselves
(Layer B holds at VQ-2) but is **fatal** for the ring-strain mechanistic interpretation
of the data. RI-06 is **fatal** for the mechanistic model as stated.

---

**VQ-4 [Benchmark]: fails**

VQ-4 requires resolution of RI-08 and RI-09 (inheriting VQ-3, which fails).

RI-09 (SRG-5) is directly active: the TOF superiority claim over refs 11/12 is asserted
without tabulated numerical comparison. RI-08 (partially active via B-7 internal
inconsistency and B-1 absence of replication data) means comparison across catalyst
variants is not reproducibly characterised. VQ-4 cannot be assessed until VQ-3 is first
resolved.

---

### §4 Era-Norm Annotation

**Communication-era tolerated:**

The following omissions were structurally normal for a three-page Nature Article in
December 1993 and are not deficiencies relative to the genre convention of that period:

- **B-4 ("standard methods"):** In 1993, Nature communications for synthetic papers
  routinely cited "standard spectroscopic methods" without listing each spectrum
  individually; ¹H NMR, ¹³C NMR, and microanalysis (or HRMS) were implied and were
  provided to editors on request.

- **B-2 (TOF values not tabulated):** The comparative TOF claim ("among the highest
  reported") was a normal rhetorical device in 1993 short communications; numerical
  TOF tables comparing the current result with literature values were the norm for full-
  paper kinetics studies, not for three-page scope-and-yield papers.

- **B-3 (qualitative catalyst comparison):** Qualitative description of catalyst-
  screening results ("equally effective," "modestly effective") without yield values was
  standard practice in high-impact communications of this era; full quantitative catalyst
  screening belonged to the subsequent full paper.

- **A-1 (mechanism deferred):** Explicit acknowledgment that the mechanism is "not
  yet clear" was a legitimate scientific statement in 1993 and was the normal form for
  reporting a new catalytic transformation prior to dedicated mechanistic studies.

- **B-1 (GC calibration absent):** In 1993 Nature communications, GC calibration
  protocols (internal standard, response factors) were not routinely reported in the
  main text; they were embedded in the experimental section of the associated full paper.
  Since no supplementary section was available in 1993 Nature, the omission is
  format-constrained, not a scientific choice.

---

**Modern-era deficient:**

The following omissions would not be accepted in a present-day resubmission or re-
certification of the same claims:

- **B-1 (GC calibration absent):** Current standards (2020s) require internal-standard
  identity and response-factor calibration for all GC-yield claims, including in short
  communications; the absence of this information makes the ten GC-only yields
  (runs 1, 2, 4, 5, 7, 9, 10, 11, 12) formally unverifiable.

- **B-2 (TOF values not tabulated):** A superlative claim ("among the highest
  reported") in a modern submission requires numerical substantiation of both the
  current paper's TOF and the comparators, regardless of communication format.

- **U-1 (cyclometallated intermediate not observed):** By current mechanistic
  organometallic chemistry standards, a catalytic mechanism citing a five-membered
  metallacycle as the selectivity-determining species requires at minimum a
  stoichiometric observation or an in-situ spectroscopic characterisation (³¹P{¹H} NMR,
  IR); the 1993 "not yet clear" deferral is unacceptable for a modern VQ-3
  certification claim.

- **U-2 (Ru(II) → Ru(0) activation not demonstrated):** The invocation of "low-
  valent ruthenium" as the active species while the pre-catalyst is RuH2(CO)(PPh3)3
  (formally Ru(II)) requires, in modern submissions, at least a control experiment
  demonstrating catalytic activity from a defined Ru(0) source or spectroscopic evidence
  of activation.

- **B-7 (olefin mass balance absent):** A modern efficiency claim stating "quantitative
  yields from both starting materials" requires that both components are monitored
  analytically; the fate of excess olefin (oligomerisation, isomerisation, recovered
  material) is now a mandatory disclosure in atom-economy efficiency claims.

- **U-3 / B-5 (scope claim exceeds abstract framing):** Current submission standards
  require that abstract-level scope claims are tightly coordinated with the data table;
  "a variety of aromatic systems" when all 13 examples are aromatic ketones would be
  flagged by a modern editor as abstract overclaiming, requiring either qualification
  or additional scope data.

- **B-9 (negative evidence "not shown"):** Reporting a mechanistically decisive
  negative result (1-indanone "did not react at all") with the parenthetical "not shown"
  is not acceptable in current practice; the full conditions, reaction time, and GC
  detection limit must be reported.

---

**Dual-classification items (tolerated then, deficient now):**

- **B-1:** Both — tolerated in 1993 as format-constrained; deficient by modern
  analytical reporting standards.
- **B-2:** Both — tolerated in 1993 as rhetorical comparative claim; deficient by
  modern quantitative-comparison standards.
- **A-1 / U-1 / U-2:** A-1 itself was tolerated (honest mechanistic humility); however,
  A-1 is now inseparable from U-1 and U-2 as a bundle: the "not yet clear" deferral
  in 1993 appropriately suspended the mechanism; a modern re-certification of the
  same mechanism as established requires resolving U-1 and U-2.

---

### §5 Shortest-reinforcement route

**Current VQ: VQ-2 (qualified)**
**First objective function: VQ-3 [Mechanism]**
**Second objective function: VQ-4 [Benchmark]**

---

**Shortest route to VQ-3:**

1. **EP-03a [Direct-observation / state-assignment pack]** — Attempt stoichiometric
   cyclometallation of acetophenone with RuH2(CO)(PPh3)3 in toluene-d8 at 135 °C
   (without olefin) and characterise by ³¹P{¹H} NMR; separately, run the standard
   reaction in the presence of a known alkyne trap or CO gas to intercept the proposed
   metallacycle, and monitor H2 evolution during the pre-catalyst induction period.
   **Advances RI-03 (primary SRG-2 failure); also advances RI-06 (by establishing
   whether the observed species has the structure predicted by the imported Ru(0)-OA
   model).**
   *Information gain: resolves the most fatal RI at VQ-3, addressing both the
   intermediate question (U-1) and the active-species question (U-2) in a single
   experimental package.*

2. **EP-04a [Discrimination / replication pack]** — Measure initial rates for run 10
   vs. run 11 substrates at three time points (5, 15, 30 min, GC aliquots), report the
   1-indanone experiment with full conditions and GC detection limit, and for run 9
   confirm absence of the three non-observed regioisomers at ≤1% detection limit.
   **Advances RI-04 (SRG-3 primary failure); partially advances RI-05 (CLA-2) by
   converting qualitative rate ranking to quantitative rate ratio.**
   *Information gain: quantifies the selectivity claims and converts the ring-strain
   mechanistic argument from qualitative assertion to discriminated comparison.*

3. **EP-06a [Analogy-validation pack]** — Assess the mechanistic equivalence of refs
   14 and 15 (Mn(I)/Ru(II) carboxylate cyclometallation) to the proposed Ru(0) OA
   pathway by identifying the oxidation-state discrepancy explicitly and specifying the
   electronic structural conditions under which electrophilic cyclometallation and OA
   converge.
   **Advances RI-06 (SRG-2 secondary failure); reduces the mechanistic import gap
   between the cited analogy and the proposed catalytic step.**
   *Information gain: lower than EP-03a (does not generate new experimental data)
   but necessary to bring the mechanistic model to VQ-3 coherence.*

4. **EP-10a [Kinetic verification pack (provisional)]** — Measure kH/kD using
   acetophenone-d0 vs. acetophenone-d4 under standard conditions to confirm whether
   C–H cleavage is rate-determining (PRI-11 candidate / CLA-1; also addresses RI-03
   for the kinetic-constraint route).
   **Advances PRI-11 candidate (CLA-1); provides the mechanistic anchor for
   attributing selectivity to the chelation-directed C–H activation step.**
   *Information gain: confirms (or refutes) rate-determining-step assignment, which
   is required for the chelation model to constitute a mechanistic explanation rather
   than a structural analogy.*

**Certification-gate note:** The experimental investment order follows information gain
(EP-03a → EP-04a → EP-06a → EP-10a), but the final VQ-3 certification is gated by
the inheritance principle: RI-02 must remain non-fatal (VQ-1), RI-01 must be at worst
qualified (VQ-2), and all of RI-03, RI-04, and RI-06 must be resolved before VQ-3
holds.

---

**Shortest route to VQ-4 (prerequisite: VQ-3 attained):**

1. **EP-09a [Internal benchmark pack]** — Tabulate numerical TOF values (mol product
   mol⁻¹ Ru h⁻¹) for runs 1, 9, and 10 alongside the corresponding values from refs 11
   and 12, using a defined denominator and common time basis; present as a side-by-side
   table.
   **Advances RI-09 (SRG-5 primary); resolves the core external-superiority gap.**

2. **EP-08a [Replication / uncertainty pack]** — Report at minimum triplicate GC
   yields with standard deviations for two representative runs (one equimolar, one with
   olefin excess) and the internal-standard calibration method; extend isolated yields to
   all 13 runs.
   **Advances RI-08 (partially active via B-7 internal inconsistency and B-1 absence
   of replication); upgrades the yield infrastructure from internally consistent to
   statistically validated.**

3. **EP-07a [Boundary-test pack]** — Test at least one non-carbonyl directed substrate
   and report the result (yield or confirmed unreactivity with conditions and detection
   limit).
   **Advances RI-07 (SRG-4); constrains the scope boundary from "variety of aromatic
   systems" to a defined directing-group requirement.**

**Certification-gate note:** VQ-4 certification requires VQ-3 first; EP-09a and EP-08a
can be executed in parallel with VQ-3 experiments but certify only after VQ-3 is
confirmed.

---

### §6 Contribution to institutional design

**1. New representative case for RI-03:**

The Murai 1993 paper provides a high-salience case for the **RI-03 (Unobserved
explanatory)** code in the context of a proposed organometallic catalytic intermediate.
The specific pattern here is that the proposed species (the five-membered Ru metallacycle)
is used as the paper's primary selectivity warrant, is structurally depicted in a figure
(Fig. 1), and is discussed using factual verbs ("[REDACTED: verbatim source text; see the source paper via its DOI]"), yet is simultaneously acknowledged as part of a
mechanism that "is not yet clear." This constitutes the **Labeling mismatch** pattern
flagged in the Stage 3 prompt: the authors explicitly label the mechanism as unresolved
(A-1), but the narrative of the key mechanistic subsection uses factual verbs that assert
the intermediate's existence as a fact. The mismatch is concentrated at the junction of
the "Possible mechanisms" subsection and Fig. 1. This case strengthens the institutional
documentation of RI-03's most practically consequential subtype: a proposed catalytic
intermediate that is structurally defined in a figure, referenced by factual language in
the text, yet experimentally absent.

**2. RI-06 at cycle level — new case:**

SRG-2 provides a clean instance of the **RI-06 (Imported model) cycle-level** pattern.
The paper imports three distinct mechanistic precedents (Mn(I) electrophilic
cyclometallation, ref 14; Ru(II) carboxylate cyclometallation, ref 15; olefin oxidative
addition to Ru, ref 17) and assembles them into a proposed cycle without demonstrating
that any of the three is isomorphic to the corresponding step in the Ru(0) aromatic-C–H-
activation cycle. This is not a single-step import but a **cycle-level import** in which
each individual step's precedent is mechanistically distinct from the target cycle. The
RI-06 scope note (v0.2a) states that cycle-level import is included; Murai 1993 is the
first case in the current collection to provide this pattern in an explicit, citable form.
Recommended addition to RI-06 casebook: "Murai 1993 — three distinct stoichiometric/
heterometallic precedents assembled into a proposed homogeneous catalytic cycle without
isomorphism demonstration at any step level."

**3. PRI-11 candidate (Mechanism–kinetics decoupling) — new supporting case:**

CLA-1 presents a clean instance of the **PRI-11 candidate** pattern: the proposed
catalytic cycle (chelation → C–H OA → migratory insertion → reductive elimination) is
not used to derive a rate law algebraically; the mechanism is supported only by the
qualitative agreement between observed chemoselectivity and the chelation geometry
predicted by the proposed cycle, without a quantitative kinetic bridge. This is
structurally isomorphic to the PRI-11 pattern confirmed in Breitenfeld 2014 and Pengfei
2024. Murai 1993 provides a third independent case from a different chemical system
(Ru-catalysed C–H activation vs. the prior confirmed cases), which meets the
two-paper isomorphism criterion for PRI-11 promotion and adds a third case from a
distinct reaction class. **Institutional recommendation:** PRI-11 should be considered
for formal promotion from provisional to full RI status, with Murai 1993 as a third
confirming case alongside Breitenfeld 2014 and Pengfei 2024.

**4. Incomplete negative evidence pattern (RI-04 implementation):**

B-9 (1-indanone "did not react at all," data "not shown") provides a citable case of
the **Incomplete negative evidence** pattern identified in the Stage 3 institutional
design framework. The pattern here is: a negative result is cited as positive mechanistic
evidence for a causal hypothesis (ring strain prevents cyclometallation), but neither the
mass-balance closure (what is the product/starting-material distribution?) nor the kinetic
window (was the reaction time sufficient to detect a slow reaction?) is established. This
is an application of RI-04 to a negative-result datum rather than a positive one: the
"unreplicated discriminator" is an absent outcome reported as a definitive mechanistic
constraint. The case-specific implementation of EP-04a for this paper (report 1-indanone
yield at ≥20 h with ≤1% GC detection limit) should be added to the EP-04a casebook as
a concrete implementation of RI-04 for negative-result mechanistic evidence.

**5. Automatic-resolution pattern (communication → full paper):**

As noted in §4, B-1 (GC calibration), B-2 (TOF values), and B-3 (catalyst comparison
quantification) are all structurally consistent with the **automatic-resolution pattern**:
omissions arising from the three-page Nature Article format that would have been resolved
automatically in the corresponding full paper (which the Murai group published
subsequently in JACS and other venues through 1994–2000). RI-01 (SRG-1) and the
scope-boundary RI-07 (SRG-4) in this paper are the clearest instances of this pattern in
the current collection. The institutional design insight is that format-induced RI-01 and
RI-07 instances should be classified as **communication-era tolerated** in §4 but
simultaneously tracked as **requiring explicit resolution** in the subsequent full
paper for VQ-2 certification to be upgraded from "qualified" to "full."

**6. SRG-3 RI-04/RI-05 co-occurrence:**

SRG-3 presents the pattern of RI-04 and RI-05 co-occurring in the same SRG. The ring-
strain hypothesis (B-8, B-9) is simultaneously an unreplicated discriminator (RI-04: two
single data points with high interpretive weight) and a qualitative overread (RI-05: causal
attribution to ring strain derived from a fast/slow/no-reaction ranking). The institutional
design note (§6 prompt) states that co-occurring RIs require resolving both. In this case,
resolving RI-04 (by reporting quantitative rates) would automatically constrain RI-05
(by providing the numerical basis that qualitative overread requires). The co-occurrence
is therefore **serially resolvable**: RI-04 resolution subsumes RI-05 resolution for
SRG-3. This is a case-specific pattern worth documenting: **"co-occurring RI-04/RI-05
with serial resolution: RI-04 investment subsumes RI-05."**

**Summary sentence:** This case provides new representative instances for RI-03
(cycle-intermediate labeling mismatch), RI-06 (cycle-level import), RI-04 (incomplete
negative evidence), supports PRI-11 promotion as a third confirming case, and documents
the automatic-resolution pattern for format-constrained RI-01/RI-07 in the
communication-to-full-paper transition.
