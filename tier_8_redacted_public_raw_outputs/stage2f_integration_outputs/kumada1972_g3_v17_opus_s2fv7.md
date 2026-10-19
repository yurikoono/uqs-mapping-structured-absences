prompt_version: stage2f-v7-20260417

---

**[F. Within-Group Comparison]**

**Group composition:** G3 — Methodological Expansion (ligand, substrate, condition axes, 1972–2016)
- Kumada 1972 (JACS Communication): foundational Ni-diphosphine cross-coupling method
- Monnereau 2009 (Adv. Synth. Catal. Full Paper): calixarene-diphosphine Ni catalyst for high-TOF Kumada coupling
- Molander 2016 (Acc. Chem. Res. Account): photoredox/Ni dual catalysis paradigm for sp³–sp² cross-coupling
- Morken 2016 (JACS Communication): Ni-catalyzed asymmetric Kumada cross-coupling of prochiral cyclic sulfates

---

**Repeated patterns**

**RP-1: Catalytic cycle proposed without experimental validation of elementary steps**

All four papers propose Ni catalytic cycles whose elementary steps lack direct experimental verification within the operating system.

evidence_chain: [Kumada_1972 : B-2, B-14, U-1, U-4 | Monnereau_2009 : B-6, B-8, U-2, U-3, U-4 | Molander_2016 : B-1, U-1, U-2, U-3 | Morken_2016 : B-3, U-4, B-18, B-19]

- Kumada 1972: Ni(0)/Ni(II) cycle (eqs 2–4) assembled from dipy-Ni analogy; no intermediate observed (B-2, B-14).
- Monnereau 2009: 41.8 ppm activated species has no assigned Ni oxidation state (U-2); RDS assignment (OA for ArCl) from electronic trend only, no kinetics (B-8, U-3); homogeneous catalysis untested (U-4).
- Molander 2016: NiI/NiIII intermediates in photoredox cycle spectroscopically unobserved (U-2); no Stern-Volmer quenching for SET step (U-1); no radical probe (U-3); control experiments asserted without data (B-1).
- Morken 2016: pyboxNi(Ar) proposed as reacting species from er-variation across ArMgBr only (B-19); Ni oxidation states unspecified (B-3); no intermediate trapped or characterized (U-4).

---

**RP-2: Quantitative analytical basis for primary data underreported**

All four papers ground their quantitative claims in measurements whose reliability cannot be independently assessed.

evidence_chain: [Kumada_1972 : B-4, B-8, B-12, B-13 | Monnereau_2009 : B-1, B-2, B-3 | Molander_2016 : B-3, B-9, B-10, B-11 | Morken_2016 : B-6, B-7]

- Kumada 1972: glpc conditions absent, yield basis mixing, reaction times missing (SRG-3).
- Monnereau 2009: GC response factors unverified for 17 diverse biaryls (B-1); no replicate measurements (B-2); TOF from single time-point with no kinetic verification (B-3).
- Molander 2016: HPLC conditions for ee absent (B-9); CV conditions absent (B-10); all scope yields single-experiment without replicates (B-11); mass balance for low-yield substrates absent (B-3).
- Morken 2016: SFC column/conditions absent for 17 er values (B-6); "average of two experiments" without individual values or SD (B-7).

---

**RP-3: Self-contradictory absence — models generating untested predictions**

All four papers contain self-contradictory absences where the paper's own model predicts testable observables that are not tested.

evidence_chain: [Kumada_1972 : U-1, U-2 | Monnereau_2009 : U-1, U-2, U-3 | Molander_2016 : U-1, U-2, U-3, U-4 | Morken_2016 : U-1, U-3, U-4]

- Kumada 1972: Catalytic cycle predicts R–R (untested); black mixture vs homogeneous mechanism (untested).
- Monnereau 2009: TOF denominator contradicted by incomplete activation (U-1); Ni(0)/Ni(II) cycle predicted by unknown 41.8 ppm species (U-2); RE acceleration for ArBr vs OA-limited ArCl (U-3).
- Molander 2016: PC* quencher identity (U-1); NiI/NiIII oxidation states (U-2); free radical intermediate lifetime (U-3); DKR khomolysis >> kRE requirement (U-4).
- Morken 2016: 44% mass balance in radical clock (U-1); RE retention assumption (U-3); intermediate existence (U-4).

---

**RP-4: Benchmark comparisons asserted rather than experimentally verified**

All four papers claim superiority or advancement over prior methods without complete quantitative comparison.

evidence_chain: [Kumada_1972 : C-1, C-2 | Monnereau_2009 : B-5, C-1, C-2 | Molander_2016 : C-1, C-2 | Morken_2016 : C-1, C-2]

- Kumada 1972: Tamura-Kochi Fe catalysts and Corey/Whitesides stoichiometric reagents cited but not numerically compared (C-1, C-2).
- Monnereau 2009: "Outperforms fastest diphosphines" based on single-substrate single-run comparison with dppp only; dppb, dppf, DPEphos named but not tested (B-5, C-1, C-2).
- Molander 2016: Prior Pd-catalyzed secondary alkyl Suzuki methods cited with conditions but no yield comparison on shared substrates (C-1); Labadie/Stille rate hierarchy cited without rate data (C-2).
- Morken 2016: Fu, Zhong/Bian, Nakamura enantioconvergent methods cited in introduction but no er/yield comparison in results (C-1, C-2).

---

**RP-5: Scope failures reported qualitatively without mechanistic attribution**

Multiple papers identify substrate classes that fail or underperform but provide no data or mechanistic explanation for the failure.

evidence_chain: [Kumada_1972 : B-5 (sp³ exclusion unexplained) | Monnereau_2009 : B-12 (bromomesitylene 15.6% unattributed) | Molander_2016 : B-4 (amine-silicate failure unattributed) | Morken_2016 : B-4, B-5 (ortho-ArMgBr, quaternary, tertiary alcohol failures — no data)]

---

**Cross-field temperature patterns**

temperature_pattern: RP-1 (mechanism validation) | papers: [Kumada_1972, Monnereau_2009, Molander_2016, Morken_2016] | profile_consistency: consistent | note: Mechanistic validation gaps consistently receive high severity from V2 across all papers: Kumada 1972 B-2 V2=critical; Monnereau 2009 B-6 V2=critical; Molander 2016 U-2 V2=high; Morken 2016 B-3 V2=high. The gap is recognized by mechanistic specialists in every case but not by other viewpoints, indicating that the mechanistic community sees the gap more acutely than synthetic chemists evaluating practical value.

temperature_pattern: RP-2 (analytical underreporting) | papers: [Kumada_1972, Monnereau_2009, Morken_2016] | profile_consistency: consistent | note: Analytical agents (V3) rate measurement quality gaps at high-to-critical severity across all experimental papers: Kumada 1972 B-4 V3=medium; Monnereau 2009 B-7 V3=critical; Morken 2016 B-7 V3=medium. The strongest convergence item is Monnereau 2009's B-7 (TOF denominator: 3/3 convergence), where all three viewpoints independently flagged the same measurement validity problem.

temperature_pattern: RP-3 (self-contradictory absence) | papers: [all four] | profile_consistency: consistent | note: Self-contradictory absence receives high severity across all papers whenever it is flagged. The consistency is remarkable — each paper independently generates the same pattern (model predicts → prediction untested), suggesting this is field-wide rather than individually chosen.

---

**Same-root group patterns**

recurring_root: Catalytic cycle proposed without elementary step validation | papers: [Kumada_1972, Monnereau_2009, Molander_2016, Morken_2016] | member_items: [Kumada_1972: SRG-1, Monnereau_2009: SRG-5, Molander_2016: SRG-1, Morken_2016: SRG-3] | note: This is a structural gap that persists across all four papers regardless of reaction type (thermal KTC, photoredox/Ni, asymmetric desymmetrization) or publication era (1972–2016). Genre convention — mechanism sections in cross-coupling papers serve narrative contextualization rather than hypothesis testing.

recurring_root: Quantitative measurement basis underreported | papers: [Kumada_1972, Monnereau_2009, Molander_2016, Morken_2016] | member_items: [Kumada_1972: SRG-3, Monnereau_2009: SRG-4, Molander_2016: SRG-5+SRG-6, Morken_2016: SRG-5] | note: Genre convention across journals (JACS, Adv. Synth. Catal., Acc. Chem. Res.) and formats (communication, full paper, Account). Not individually chosen.

recurring_root: Benchmark superiority asserted without matched-pair comparison | papers: [all four] | member_items: [Kumada_1972: C-1+C-2, Monnereau_2009: SRG-2, Molander_2016: SRG-4, Morken_2016: C-1+C-2] | note: Every paper positions against named prior art without performing common-substrate yield comparison. This is a field-wide convention — introductions frame advancement qualitatively while results sections present only the new method's data.

---

**Temporal trajectory of recurring patterns**

temporal_trajectory: RP-1 (mechanism validation) | classification: shifting | transition_point: ~2014 (photoredox/radical mechanisms) | note: 1972: 2-electron Ni(0)/Ni(II) cycle proposed by analogy (structurally suppressed — no NMR, no radical probes). 2009: same paradigm with even less mechanistic evidence (41.8 ppm species unidentified). 2016 (Molander): radically different mechanism proposed (NiI/NiIII/photoredox) but still without elementary step validation. 2016 (Morken): back to 2-electron-like mechanism but with SN2-like OA and untested RE assumption. The gap persists but shifts in character from "no tools" to "tools available, paradigm changed, validation still absent."

temporal_trajectory: RP-2 (analytical underreporting) | classification: time-invariant | transition_point: n/a | note: 1972: glpc conditions absent. 2009: GC response factors absent, no replicates. 2016 (Molander): scope yields without replicates. 2016 (Morken): SFC conditions absent, "average of two" without SD. The character of analytical underreporting is unchanged across 44 years.

temporal_trajectory: RP-3 (self-contradictory absence) | classification: time-invariant | transition_point: n/a | note: The specific untested predictions change (R–R in 1972; TOF denominator in 2009; NiIII intermediates in 2016; RE retention in 2016) but the structural pattern is invariant.

temporal_trajectory: RP-4 (benchmark superiority asserted) | classification: time-invariant | transition_point: n/a | note: Every paper claims improvement over prior art without matched comparison. This is a stable feature of methodology papers across all eras.

temporal_trajectory: RP-5 (scope failures undiagnosed) | classification: time-invariant | transition_point: n/a | note: Kumada 1972 does not explain the sp² restriction; Monnereau 2009 does not explain bromomesitylene failure; Morken 2016 does not explain ortho-ArMgBr failure. Undiagnosed scope failures persist as a stable feature.

---

**Structural suppression vs. individual choice**

RP-1 (mechanism validation):
- *Era-dependent*: structurally suppressed (1972, 2009: limited in situ tools for Ni) → individually chosen (2016: tools available — in situ NMR, EPR, radical clocks, DFT — but not deployed for key mechanistic claims in either Molander or Morken).

RP-2 (analytical underreporting):
- *Incentive-suppressed*: No journal among JACS (1972), Adv. Synth. Catal. (2009), Acc. Chem. Res. (2016), or JACS (2016) requires replicate data, response factor calibration, or uncertainty quantification for yield/conversion/er. Publishing this information would not constitute an independent contribution.

RP-3 (self-contradictory absence):
- *Individually chosen*: Every untested prediction is testable with the paper's own infrastructure. Testing R–R (1972) requires glpc. Testing activation yield (2009) requires quantitative NMR integration. Testing NiIII intermediates (Molander 2016) requires EPR. Testing RE retention (Morken 2016) requires a single stoichiometric experiment.

RP-4 (benchmark superiority asserted):
- *Incentive-suppressed*: Performing a matched-pair comparison (identical substrate, identical conditions) against a competitor's method risks showing the new method is not superior for that specific case, even if it offers advantages in other dimensions (scope breadth, conditions mildness). The incentive structure of methodology papers rewards demonstration of scope over head-to-head comparison.

RP-5 (scope failures undiagnosed):
- *Individually chosen* (partially): Diagnosing failure modes requires additional experiments (Hammett analysis, steric mapping, alternative ligand screening) that are within each paper's capability but were not pursued. However, the communication format (1972, Morken 2016) structurally compresses failure analysis, making it partially *format-suppressed* as well.

---

**Paradigm competition**

This group reveals three methodological paradigms coexisting rather than competing:

**Paradigm 1: Ligand design for 2-electron Ni(0)/Ni(II) catalysis (1972, 2009)**
Kumada 1972 and Monnereau 2009 both operate within the same catalytic manifold (Ni(0)/Ni(II) oxidative addition → transmetalation → reductive elimination) with Grignard nucleophiles and aryl halide electrophiles. The expansion axis is ligand architecture: dppp (1972) → calixarene-diphosphine (2009).

Systematically unanswered question:
- What structural and electronic features of the diphosphine ligand quantitatively determine the rate-limiting step and overall TOF?
  evidence_chain: [Kumada_1972 : B-3 → ligand order from 1 substrate, cis-geometry hypothesis; Monnereau_2009 : U-3 → RE-vs-OA tension unresolved, B-10 → dynamics/catalysis rate comparison conditions incompatible]

**Paradigm 2: Single-electron activation via photoredox/Ni dual catalysis (2016, Molander)**
Fundamentally different activation mode: organotrifluoroborates or alkylsilicates undergo SET to generate carbon radicals that enter a NiI/NiIII manifold. No Grignard reagent; no 2-electron transmetalation.

Systematically unanswered question:
- What is the dominant quencher of the excited photocatalyst, and are NiI/NiIII intermediates spectroscopically detectable?
  evidence_chain: [Molander_2016 : U-1 → Stern-Volmer absent; U-2 → NiI/NiIII undetected; "no textual basis in Kumada_1972 or Monnereau_2009" — the question does not arise in the 2-electron paradigm]

**Paradigm 3: Enantioselective desymmetrization via Ni/chiral ligand (2016, Morken)**
Combines 2-electron SN2-like oxidative addition with a chiral PyBox ligand to achieve enantioselective coupling of prochiral substrates — a new selectivity axis (enantiocontrol) rather than a new activation mode.

Systematically unanswered question:
- Is the enantioselectivity kinetically or thermodynamically controlled, and at which elementary step is stereochemical information set?
  evidence_chain: [Morken_2016 : U-2 → kinetic/thermodynamic control untested; B-18 → selectivity-determining step assumed from er variation, not proven]

**Coexistence, not succession:** Unlike G1 and G2, the three paradigms in G3 are not sequential replacements — they coexist as independent methodological expansions from the same 1972 origin. However, all three share the same blind spot: catalytic cycle validation (RP-1). This shared gap persists regardless of the paradigm, suggesting it is a field-wide structural convention rather than a paradigm-specific limitation.

---

**Divergences**

**DV-1: Nucleophile type defines the paradigm**
Kumada 1972 and Monnereau 2009 use Grignard reagents (2-electron nucleophile). Molander 2016 uses organotrifluoroborates and alkylsilicates (1-electron radical progenitors). Morken 2016 uses Grignard reagents but with prochiral electrophiles. The nucleophile choice determines the entire mechanistic manifold.

evidence_chain: [Kumada_1972 : S0-4 → PhMgBr | Monnereau_2009 : S0-4 → PhMgBr | Molander_2016 : S0-4 → organotrifluoroborates/silicates | Morken_2016 : S0-4 → ArMgBr]

**DV-2: Metric of success diverges**
Kumada 1972: yield and substrate breadth. Monnereau 2009: TOF (kinetic metric). Molander 2016: conceptual paradigm + scope breadth. Morken 2016: enantioselectivity (er). Each paper defines success differently, making cross-paper comparison structurally difficult.

evidence_chain: [Kumada_1972 : D-1 success_criteria → yield, selectivity | Monnereau_2009 : D-1 success_criteria → TOF | Molander_2016 : D-1 success_criteria → paradigm + scope | Morken_2016 : D-1 success_criteria → er]

**DV-3: Format constrains evidentiary depth**
Communication (1972, 2016-Morken) vs full paper (2009) vs Account (2016-Molander). The Account format (Molander) is uniquely permissive of data absence because it is retrospective; the communication format (Morken) compresses mechanistic evidence to two experiments; the full paper (Monnereau) has space but still omits replication and response factor data.

evidence_chain: [Kumada_1972 : D-3 → JACS Communication 3pp | Monnereau_2009 : D-3 → Adv. Synth. Catal. full paper 7pp | Molander_2016 : D-3 → Acc. Chem. Res. Account 11pp | Morken_2016 : D-3 → JACS Communication 4pp]

---

**U-item patterns**

recurring_U: Self-contradictory absence involving catalytic cycle predictions | papers: [all four] | item_ids: [Kumada_1972: U-1, U-2; Monnereau_2009: U-1, U-2, U-3; Molander_2016: U-1, U-2, U-3, U-4; Morken_2016: U-1, U-3, U-4] | note: U-items constitute the single largest category of recurring gaps across all four papers. Their accumulation across papers, paradigms, and formats suggests that the A/B/C classification framework captures individual paper omissions well but does not naturally capture the recursive pattern of "model predicts observable → observable not tested" that is endemic to cross-coupling mechanism sections.

---

**Self-contradictory absence patterns**

self_contradictory: [Kumada_1972] : catalytic cycle eq 3 → R–R predicted → unreported | item_id: U-1
self_contradictory: [Kumada_1972] : homogeneous cycle → black mixture → unanalyzed | item_id: U-2
self_contradictory: [Monnereau_2009] : TOF uses mol(precatalyst) as denominator → paper reports incomplete activation → TOF denominator incorrect by paper's own data | item_id: U-1
self_contradictory: [Monnereau_2009] : Ni(0)/Ni(II) cycle proposed → 41.8 ppm species Ni oxidation state unknown → cycle identity unverified | item_id: U-2
self_contradictory: [Monnereau_2009] : bite-angle dynamics accelerates RE (ArBr hypothesis) → ArCl: OA is RDS → RE acceleration irrelevant when OA limits → tension unacknowledged | item_id: U-3
self_contradictory: [Molander_2016] : SET cycle predicts PC* quenched by organotrifluoroborate → Stern-Volmer absent → quencher identity unknown | item_id: U-1
self_contradictory: [Molander_2016] : cycle predicts NiI and NiIII intermediates → neither observed by EPR/UV-Vis → stated as established | item_id: U-2
self_contradictory: [Molander_2016] : DKR model predicts khomolysis >> kRE → no kinetic validation → model used for stereochemical predictions | item_id: U-4
self_contradictory: [Morken_2016] : non-radical mechanism predicts no ring-opened product → 44% mass balance unaccounted → "only detected" claim depends on unstated detection limit | item_id: U-1
self_contradictory: [Morken_2016] : SN2-like OA deduced → RE retention assumed → assumption untested → stereochemical assignment indeterminate | item_id: U-3
self_contradictory: [Morken_2016] : cycle predicts pyboxNi(Ar) and Ni-sulfate intermediates → none observed → proposed as "plausible" | item_id: U-4

**Recurring pattern assessment:** Self-contradictory absence is the most densely recurring pattern across this group, appearing in every paper regardless of mechanism type, publication era, or format. The pattern reflects a **narrative function of mechanism diagrams**: catalytic cycles in cross-coupling papers serve to organize synthetic results rather than to generate and test predictions. This is simultaneously a **genre convention** (expected by editors and reviewers) and a **genuine analytical gap** (each prediction is individually testable). The convention persists because testing predictions would either confirm them (unpublishable) or falsify them (requiring a different paper), creating an incentive structure that preserves the gap.

---

**Group-level unasked question**

[REDACTED: substantial verbatim quotation; see Tier 9]

evidence_chain: [Kumada_1972 : B-2 (cycle from analogy), U-2 (heterogeneous untested) | Monnereau_2009 : U-2 (Ni oxidation state unknown), U-4 (heterogeneous untested) | Molander_2016 : U-1 (quencher unknown), U-2 (NiI/NiIII unobserved) | Morken_2016 : B-3 (Ni oxidation state unspecified), U-4 (intermediates unobserved)]

TEMPERATURE_SUMMARY correspondence: The group-level question maps to the strongest convergence items across papers. In Kumada 1972, B-2 (mechanism without evidence) has V2=critical. In Monnereau 2009, B-7/U-1 (TOF denominator) has 3/3 convergence (V1=high, V2=high, V3=critical). In Molander 2016, U-7 (DFT model extrapolation) has 3/3 convergence (all high). In Morken 2016, B-1 and U-1 (radical clock mass balance) have 3/3 convergence (all high). The strongest convergence items in each paper all concern the gap between mechanistic claims and their experimental evidence base — the group-level unasked question is exactly this gap at the field level.

recurring_root correspondence: The group-level question subsumes all three recurring roots (cycle validation, analytical underreporting, benchmark superiority) as facets of a single problem: the field has no agreed standard for what constitutes sufficient mechanistic evidence in Ni-catalyzed cross-coupling. Each paper proposes a mechanism at a different level of certainty, from "working hypothesis" (1972) to "established" (Molander 2016), but the evidentiary standard for each level is nowhere defined or enforced.

---

*End of G3 output.*

---

> **Tier 8 redaction notice**: This file is a redacted copy of the corresponding Tier 3 / Tier 9 output. Verbatim source-paper quotations have been replaced by `[REDACTED: see source paper §<loc>; full text retained in Tier 9 reviewer-only deposit]` markers, preserving location references and our own analytical content. Bibliographic fields (title, authors, journal, year, DOI), analytical labels (`evidence_chain:` with B-/U-/A-/C- internal IDs), short technical terms, and our own analytical text are not redacted. The redaction was applied by `scripts/redact_for_tier8.py` and, for this version, by `scripts/build_paperA_R1_public.py` with `scripts/redact_source_ngram_runs.py` (scripts of the project repository; they are not deposited).
