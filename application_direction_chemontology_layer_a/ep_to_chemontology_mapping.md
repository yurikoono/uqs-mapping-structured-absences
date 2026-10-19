---
title: EP-to-ChemOntology-AFIR Parameter Mapping (Kumada 1972)
created: 2026-04-19
updated: 2026-05-02 (EP-10a row added; Paper B Phase γ outline restructure prerequisite); 2026-05-20 PM (D-1 RE ERPO resolved via Option β Fragmentation; D-5 C-H activation developer-defined; co-author full meeting outcomes integrated); 2026-05-22 (Paper A Phase 1 Uchino-revision cascade: EP-06a row reframed from "imported-model validation" to "system-matched documentation axis 4 computational direct-constraint contribution" per Paper A v4.7 4-paper lineage analysis; ChemOntology integration claim wording aligned)
layer: A
ep_source: papers/dev/kumada/kumada_v17_sonnet_s3v2.md (Stage 3 v2, Sonnet 4.6) + Paper A SI-3 final dictionary (10 EPs)
chemontology_source: Nath et al. (2026) ACS Catal. 16, 2105–2118 + SI + developer-version extensions (2026-05-20 co-author meeting で disclosed: D-5 C-H activation 既定義)
status: co-author meeting で resolved (2026-05-20); Paper B Phase γ Methods §1.1 worked example + Methods §2.1 EP dictionary + Results Part 1 Table 1 source として deployable
---

# EP-to-ChemOntology-AFIR Parameter Mapping for the NiCl₂(dpe) Kumada System

This document maps each Evidence Pack (EP) derived from Kumada 1972
Stage 3 onto specific ChemOntology-AFIR parameters. It is intended as
a companion deliverable to the UQS paper (Paper A, Digital Discovery
submission) and as the empirical base for the EP-AFIR bridge
formalization in Paper B (companion methodology paper). It does
**not** report executed computational results — those are deferred to
the AFIR pilot study (Paper B Layer C execution).

## Scope of mapping

- **EP source (authoritative)**: Paper A final EP dictionary (10 EPs,
  SI-3 §SI-3.7 / §SI-3.10 / §SI-3.11). The original Stage 3 v2 analysis
  of Tamao, Sumitani, Kumada 1972 (*J. Am. Chem. Soc.* **94**, 4374)
  produced eight EPs (EP-01a, EP-03a–EP-09a); two further EPs were
  added in April 2026 through cross-model convergence:
  - **EP-02a (Identity / purity substantiation pack)** — added 2026-04-19,
    two-source cross-vendor (GPT-5.4 Thinking + Opus 4.7 Stage 3 v2 on
    Kumada 1972). The original Sonnet Stage 3 v1 grouped this absence
    under EP-01a; cross-vendor convergence promoted it to a separate
    identifier.
  - **EP-10a (Kinetic verification pack)** — added 2026-04-19 (initial)
    + 2026-04-27 (extended), seven-source cross-paper + cross-vendor
    derivation: Sonnet on Breitenfeld 2014 / Mazet 2021 / Pengfei 2024
    + GPT-5.4 Thinking and Opus 4.7 on Kumada 1972 + GPT-5.5 Thinking
    on Murai 1993 + cross-paper confirmation on Yamamoto 1978.
- **Coverage status**: This mapping covers **all 10 EPs** (EP-01a through
  EP-10a). EP-02a was included from the file's initial creation (2026-04-19)
  using the EXPECTED_PRODUCTS_WITH_CIDS enumeration mapping. EP-10a was
  added on 2026-05-02 as a prerequisite for Paper B Phase γ outline
  drafting, using the kinetic-navigation module of ChemOntology-AFIR
  (Siml_temperature / TimeScale parameters of Nath et al. 2026 SI Table S4).
- **ChemOntology reference**: Nath et al. (2026) main text + SI Entries
  #1–#16. ERPO categories used are limited to those formally defined
  in the published materials (see "Parameter legend" below). One ERPO
  ReductiveElimination is not a dedicated keyword ERPO in published SI Figs S1-S4, but **resolved 2026-05-20 via Option (β) Fragmentation ERPO** (`Dissociation_of_Ri` + `Association_of_Ri` from SI Table S2) — see §Open Methodological Questions §1.

## Parameter legend (from Nath et al. 2026)

- **Structural Units (SU)**: M (metal), L (ligand), B (base),
  S (substrate). Substrates are sub-classified by FG as R1 (halide /
  triflate / aldehyde), R2 (alkene / alkyne), R3 (RMgX / RSnR'₃)
  (main text Figure 2).
- **Conceptual ERPOs** (SI Table S2 and main text Table 2):
  CoordinationComplex; AssociationOfCoordinationComplexWithaSubstrateType(m,n);
  DissociationOfaSubstrateType(m,n);
  AssociationOfCoordinationComplexWithaComponentOfaSubstrateType(m,n,o) for o ∈ {1,2};
  AssociationOfTwoComponents.
- **Defined ERPOs via XML (SI Figures S1–S4)**: OxidativeAddition (Fig S1),
  OlefinInsertion (Fig S2), β-Hydride Elimination (Fig S3),
  **Transmetalation** (Fig S4). These are the explicitly XML-defined
  elementary processes; **ReductiveElimination is not among them as a dedicated keyword** but **resolved 2026-05-20 via Option (β)** = Fragmentation ERPO (`Dissociation_of_Ri` + `Association_of_Ri`, SI Table S2) — see §Open Methodological Questions §1.
- **Reaction-rule parameter `allowed_changes`**: per-SU numerical value
  specifying permissible atomic-hybridization changes during the
  reaction (Nath et al. 2026 Table 4; SI Figure S5 input snapshot).
  In the Heck example: substrates = 3, metal Pd = 1, base = 1,
  phosphine ligand = 0.
- **Geometric and collision parameters**: SU radius *r* = 2.2 Å; SU-to-SU
  proximity threshold *δ* = 3.0 Å; AFIR collision-energy *γ* = 500 kJ/mol;
  STOPPATH = 2000 (Nath et al. 2026 Table 4; SI Table S4).
- **Calculation level**: GFN2-xTB semiempirical screening for initial
  path search (Bannwarth, Ehlert, Grimme 2019, cited as ref 41;
  Koopman & Grimme 2019 for electron-ionization refinement);
  DFT refinement where the semiempirical energies are unreliable.
  Primary validation in Nath et al. (2026) was performed on a
  **Pd-catalyzed Heck reaction**; extension to Ni is claimed in the
  "Versatility of ChemOntology" paragraph ("Kumada coupling") but not
  empirically demonstrated in the paper itself.

## Mapping table (proposed Table 4 of the UQS manuscript)

| EP ID | EP content (short) | VQ level addressed | ChemOntology-AFIR parameter(s) | Required ERPO(s) | `allowed_changes` setting | Calculation level | Expected output | Notes on limitations |
|---|---|---|---|---|---|---|---|---|
| EP-01a | Reporting coherence: unified GLC conditions, unified yield basis, full mass balance for Table I | VQ-2 | — (not directly computable) | — | — | — | — | Out of scope for ChemOntology-AFIR: a reporting-hygiene issue in the experimental literature. Computed yields and branch-point energies may serve as an **independent reference** against which to compare the experimental mass balance, but cannot substitute for it. |
| EP-02a | Identity / purity substantiation: per-entry GC-MS or ¹H NMR | VQ-1 (residual RI-02) | `EXPECTED_PRODUCTS_WITH_CIDS` (Nath et al. Table 4, entry 9) | — | — | — | Enumeration of chemically allowed product species (cross-coupling + homocoupling + β-elim products) reachable on the PES | Mapping is **indirect**. ChemOntology can enumerate the set of products that the ERPO-constrained network is allowed to produce, giving a computational "identity checklist"; experimental product identity confirmation remains experimental. |
| EP-03a | Direct observation of intermediates 1, 2, 3 (dpe-Ni system) | VQ-3 | Reaction network nodes; node labels OA / Transmetalation / MI / BHE / Dissociation_of_Ri (RE pattern) | CoordinationComplex; OxidativeAddition (SI Fig S1); Transmetalation (SI Fig S4); β-Hydride Elimination (SI Fig S3); **Dissociation_of_Ri (Fragmentation ERPO, RE pattern; SI Table S2; β-i stepwise or β-ii compound sub-option pending operational validation — 2026-05-20 L-3 resolved)** | Substrate S = 3; metal M = 1; ligand (dpe) L = 0; base (absent) — | B97-3c routine (multi-tier scheme; spin/charge hot-spot refinement per §Calculation level) | Reaction network (node graph) for the NiCl₂(dpe) system with all proposed intermediates labeled; geometries and relative energies for each node (analog of Figure 6d–Figure 8 for Heck) | **Direct mapping.** The computational network provides a structurally labeled list of intermediates and transition states that can be compared against the experimentally unobserved species 1, 2, 3 of Kumada 1972 eqs 2–4. Does not substitute for spectroscopic observation; complementary. |
| EP-04a | Discrimination of cis/trans-stilbene ratios (kinetic vs thermodynamic control) | VQ-3 | Branch-point energy comparison between stereo-differentiated pathways; time-resolved population flux (kinetics module) | CoordinationComplex; OxidativeAddition; Transmetalation; **Dissociation_of_Ri (Fragmentation ERPO, RE pattern; 2026-05-20 L-3 resolved)** — with stereo-differentiated RC assignment on the vinyl substrate | S = 3 for substrate (inherits Heck convention); M = 1; L = 0 | B97-3c routine + RCMC kinetic navigation (*Siml_temperature* = 200 / 300 / 400 K; *TimeScale* = 86400 s — SI Table S4) | Pair of pathways leading to cis-stilbene vs trans-stilbene products; relative transition-state energies and kinetic branch ratios at multiple temperatures | **Partial mapping.** Stereochemistry on the vinyl substrate can be distinguished by careful RC assignment but ChemOntology's primary validation did not emphasize stereochemical discrimination. Experimental validation (EP-04a original purpose) still needed. |
| EP-05a | Quantitative mass-balance of cross-coupling vs homocoupling vs β-elim | VQ-3 | Branch-point energy comparison among competing ERPOs; `EXCLUDE_FORMATIONS_OF` for side products; product-label assignment (SI Table S3) | CoordinationComplex; OxidativeAddition; Transmetalation; β-Hydride Elimination (for the β-elim branch); `AssociationOfTwoComponents` with C1R1-C1R2 pattern (cross) vs C2R1-C2R2 analog (homo) | S = 3; M = 1; L = 0 | GFN2-xTB → DFT for branch-point TS energies | Energy profile of (cross-coupling pathway) vs (homocoupling pathway) vs (β-hydride elim pathway) with relative barrier heights; computational selectivity prediction | **Partial/indirect.** Branch energy comparison gives theoretical selectivity but not experimental mass balance. Table S3 in Nath et al. 2026 leaves cross-coupling product combinations (C1R1-C1R2 etc.) as **"Not labeled yet"**, so Kumada-specific product labeling would need to be added. |
| EP-06a | Analogy validation: stoichiometric realization of eqs 2–4 in NiCl₂(dpe) within the four-paper Kumada lineage | VQ-3 | Full ERPO sequence executed on target system; comparison against integrated cycle proposal + system-matched documentation axes (Paper A v4.7) | CoordinationComplex; OxidativeAddition (SI Fig S1); Transmetalation (SI Fig S4); **Dissociation_of_Ri (Fragmentation ERPO, RE pattern; 2026-05-20 L-3 resolved)** — optional BetaHydrideElimination (SI Fig S3) as competing branch | S = 3; M = 1; L = 0 (dpe as bidentate); B = — (Grignard acts as both substrate source and halide scavenger) | B97-3c routine (multi-tier scheme; spin hot-spot TPSSh / def2-mTZVP refine for Ni(0)/Ni(II) borderline species per §Calculation level) | Reaction network in which the Ni(0)/Ni(II) cycle proposed by Kumada 1972 (integrating antecedent organonickel observations with transmetalation chemistry) emerges as a connected subgraph; quantitative barriers for each step | **Most demanding EP.** Provides computational direct constraint contributing to **axis 4 (experimentally observed or directly constrained organonickel intermediates) of the system-matched documentation operational definition** in Paper A's four-paper lineage analysis (Uchino 1970 / Kumada 1972 / Morrell–Kochi 1975 / Chen / Dawson / Mazet 2019–2021; Paper A SI-10). Complements (a) antecedent product-level organonickel observations from Uchino et al. 1970 (parallel antecedent, dipy-Ni stoichiometric system) and (b) Chen / Dawson / Mazet 2019–2021 system-isomorphic experimental consolidation in the bisphosphine-Ni catalytic manifold. The framing is not "imported-model validation" (the Kumada cycle was not imported from dipy-Ni in isolation; it integrated antecedent step-level observations with Grignard transmetalation; per Paper A SI-10 §6 transposition-rather-than-filling clarification) but **system-matched documentation contribution at the computational direct-constraint level**. Schlenk equilibrium: MgBr₂ explicit only single-treatment (2026-05-20 L-6); PCM Et₂O solvation (2026-05-20 L-7). |
| EP-07a | Boundary test: sp³ halide failure; PhCl/PhBr/PhI reactivity ranking | VQ-2 | Barrier-height comparison across substrate variants at the OA step | OxidativeAddition (SI Fig S1), parameterized across different R1-type substrates (PhCl / PhBr / PhI / n-BuCl / cyclohexyl chloride) | S = 3 for substrate (same across variants); M = 1; L = 0 | GFN2-xTB; DFT refinement for transition state geometries | Table of OA transition-state energies across substrate variants; computational reactivity ranking | **Partial mapping.** Provides a predictive reactivity map but cannot substitute for experimental observation of reaction / no-reaction outcome. sp³ substrates may require alternative mechanistic pathways (e.g., SET) not cleanly covered by closed-shell OA ERPO. |
| EP-08a | Replicate measurements with n ≥ 3 and standard deviation | VQ-4 | Multi-level theory robustness (GFN2-xTB vs DFT functional variation vs basis-set variation) | same as EP-03a / EP-06a | same as EP-03a / EP-06a (per-level) | GFN2-xTB; multiple DFT functionals (e.g., PBE0-D3 / B3LYP-D3 / M06-2X) with ≥2 basis sets | Statistical spread of computed barrier heights and branch-point energies across theoretical levels; robustness metric | **Conceptually different.** Computational robustness (sensitivity to theoretical level) is not the same as experimental replication (sensitivity to run-to-run variation). This is the "Computational-Complete" classification proposed in Discussion 2 Stage 4 extension. |
| EP-09a | Internal benchmark: NiCl₂(dpe) vs Ni(acac)₂ head-to-head | VQ-4 | Parallel ChemOntology-AFIR runs with matched ERPO sets on both catalyst systems | same as EP-06a, applied to each catalyst | dpe case: L = 0 (bidentate phosphine); acac case: L = 0 (β-diketonate). S = 3; M = 1 | GFN2-xTB → DFT at matched level | Comparative PES / reaction-network output for the two catalyst systems; matched barrier-height and selectivity metrics | **Direct mapping.** Answers CLA-1 (Corriu/Masse comparison) by computational parallel execution. Does not substitute for experimental head-to-head comparison but provides a reproducible benchmark spec. |
| EP-10a | Kinetic verification: rate-law derivation from proposed cycle, time-course kinetic-vs-thermodynamic discrimination, Eyring analysis of cis/trans branch | VQ-3 (temporal dimension complementing EP-04a static / EP-07a endpoint) | Time-resolved population flux from RCMC kinetic-navigation module (same module as EP-04a); rate-law extraction from computed reaction-network barriers (Arrhenius preexponential + activation energy per elementary step); cycle-level rate-law derivation consistency check | Same as EP-06a (full Kumada catalytic cycle: CoordinationComplex; OxidativeAddition; Transmetalation; **Dissociation_of_Ri (Fragmentation ERPO, RE pattern; 2026-05-20 L-3 resolved)**) executed under time-resolved population-flux mode | S = 3; M = 1; L = 0 (same as EP-06a) | GFN2-xTB initial network + DFT refinement of barrier heights mandatory (Ni redox accuracy); RCMC kinetic navigation at *Siml_temperature* = {200, 250, 300, 350, 400} K; *TimeScale* = 86400 s (Nath et al. 2026 SI Table S4) | (a) Per-elementary-step Arrhenius-like rate expressions (k = A · exp(−Eₐ/RT)) extracted from computed barriers; (b) cycle-level integrated rate law derived from elementary-step flux; (c) kinetic vs thermodynamic branch identification at multiple temperatures (cis/trans-stilbene endpoint flux); (d) rate-vs-selectivity decomposition for SRG-4 (chloride reactivity claim); (e) consistency check between (b) and the experimental rate-law form expected from the proposed catalytic cycle | **Direct mapping** (parallel to EP-04a + EP-06a). Provides the temporal complement that EP-04a (static replicate-quality discrimination) and EP-07a (scope-boundary endpoints) leave open. Limitations: (i) rate-law extraction from computed barriers is meaningful only if the elementary-step network reproduces the experimentally observed steady state — pre-flight verification against Mazet 2021 (dppe-Ni Ni(0)/Ni(II) experimental rate observations) recommended; (ii) RCMC time-resolved navigation has not been validated for Ni systems in Nath et al. 2026 (Pd Heck primary validation); functional/basis-set robustness check (parallel to EP-08a's multi-level theory robustness) recommended for the rate-law output. Filling-paper anchor: Chen 2019 (combined computation + experiment, dppe-Ni system, rate-law-relevant) is the leading experimental-side EP-10a filler, supporting the bridge's reverse-flow consistency check. |

## Mapping methodology

The mapping was constructed as follows.

1. **VQ-level alignment.** Each EP's target VQ level (from Stage 3 v2 §5
   "最短補強ルート") was preserved. EPs targeting VQ-2 (reporting
   hygiene, boundary) were expected to map less cleanly to
   reaction-path computation than EPs targeting VQ-3 (mechanism);
   this expectation was borne out, with EP-01a, EP-02a, EP-07a showing
   only partial or indirect mapping.
2. **ERPO assignment under closure.** Only ERPOs formally defined in
   Nath et al. (2026)—CoordinationComplex and four basic
   sub-ERPOs (Table 2), OxidativeAddition (SI Fig S1), OlefinInsertion
   (SI Fig S2), β-Hydride Elimination (SI Fig S3),
   Transmetalation (SI Fig S4), BaseElimination, AssociationOfTwoComponents—were
   used. No ERPO categories were invented. Where the Kumada cycle
   requires a step not covered (most critically, reductive elimination
   from Ni(II) diorganyl to Ni(0) + R-R'), the gap is flagged as an
   open question rather than silently patched.
3. **`allowed_changes` closure.** The per-SU `allowed_changes` values in
   the table were constrained to Nath et al. (2026)'s Heck example:
   substrate = 3, metal = 1, ligand = 0 (SI Figure S5 input snapshot).
   The manuscript's Discussion 2 statement that "S = 3 is considered
   appropriate" is therefore **confirmed as the substrate-side setting**
   and identical to the Heck convention—but the manuscript's shorthand
   omits the required M = 1 and L = 0 settings that apply separately
   to the Ni metal and the dpe ligand. The insertion draft
   (`discussion2_insertion_draft.md`) corrects this.
4. **Calculation-level judgment.** Because Ni(0) ↔ Ni(II) redox involves
   d¹⁰ ↔ d⁸ electronic-structure changes that are not the primary
   validation domain of Nath et al. (2026) (which focused on
   Pd(0)/Pd(II) in the Heck reaction), DFT refinement is marked as
   mandatory, not optional, for any EP that touches a formal
   oxidation-state change (EP-03a, EP-04a, EP-06a, EP-08a, EP-09a).

## Directly, partially, and non-addressable EPs

- **Directly addressable** (expected clean ChemOntology-AFIR output):
  EP-03a, EP-06a, EP-09a, **EP-10a**. These are the natural "targets" of
  ChemOntology-AFIR computation—identification of intermediates,
  instantiation of a catalytic cycle in the target system, parallel
  execution for internal benchmarking, and (with EP-10a) time-resolved
  rate-law extraction from the elementary-step network.
- **Partially addressable** (ChemOntology contributes but does not
  substitute for experiment): EP-04a, EP-05a, EP-07a. Branch-point
  energy comparisons and substrate-scan barrier predictions provide
  theoretical ranking, but the experimental observables (stereochemistry
  ratios, mass balance, scope boundary) remain experimentally grounded.
- **Indirectly or not addressable**: EP-01a (reporting hygiene),
  EP-02a (experimental product identity), EP-08a (experimental
  replication). These are concerns about the experimental record and
  its statistical-reliability standards; the computational analog
  (multi-level-theory robustness as a substitute for experimental
  replication) is conceptually different and should be classified
  separately under the proposed "Computational" filling type
  (Paper B Methods §2.6 operational labels — Computational-Complete /
  Computational-Partial / Computational-Indirect; formal codification
  in Paper C).

The distribution of mappings is itself informative: the EPs that map
cleanly (EP-03a, EP-06a, EP-09a, EP-10a) are precisely those at VQ-3
(mechanism layer with EP-10a's temporal complement), which are the
hardest to fill from single experimental studies alone. This supports
the Paper A Discussion 2 / Paper B Results Part 1 argument that
ChemOntology-AFIR's natural contribution is at VQ-3-level filling
(static + temporal), complementing experimental work that typically
achieves VQ-1 and VQ-2 filling within a single paper.

## Bi-directional framing

The mapping supports the bidirectional framing already advanced in
Discussion 2 (Paper A v4.7 four-paper lineage version):

- **UQS → ChemOntology (input design)**: The EP list — sourced from
  Paper A's four-paper Kumada lineage analysis (Uchino 1970 / Kumada
  1972 / Morrell–Kochi 1975 / Chen / Dawson / Mazet 2019–2021) — gives
  ChemOntology-AFIR a principled termination criterion. Instead of
  running to the default STOPPATH = 2000 (Nath et al. 2026 Table 4),
  an EP-driven run terminates when barriers and intermediates
  addressing a specified set of EPs have been computed. Computational
  resources are thereby allocated by literature-derived evidential
  need rather than by default exhaustiveness.
- **ChemOntology → UQS (new evidence form)**: A computed reaction
  network is a new kind of `evidence_chain` trace for UQS, contributing
  specifically to **axis 4 (experimentally observed or directly
  constrained organonickel intermediates) of the system-matched
  documentation operational definition** (Paper A v4.7 Results Part 1
  §2). Propositions such as "β-agostic interactions mediate migratory
  insertion" (Nath et al. 2026 Figure 8f) or "the Ni(0)/Ni(II) cycle
  proposed in Kumada 1972 is energetically consistent in the target
  dppe-Ni system at matched experimental conditions" acquire a
  structural trace from the PES at the computational direct-constraint
  level. Some retrospective gaps—absences that the framework of the
  time could not formulate—may transfer to synchronic gaps once the
  network is computed. Taketsugu's data-structure observation (Paper A
  v4.7 Discussion §3, 2026-05-22 commit) — "experimental records
  structured at this resolution become more directly comparable with
  quantum-chemical and reaction-path-search calculations: ligand class,
  catalytic manifold, transmetalation context, intermediate constraints,
  kinetics, and benchmark axes can be mapped onto computable mechanistic
  hypotheses" — is the **operational complement** in the experiment-side
  data discipline.

## Open methodological questions (flagged for co-author review)

1. **ReductiveElimination ERPO gap — RESOLVED 2026-05-20 via Option (β) Fragmentation ERPO.** 
   
   Original gap: SI Table S2 and SI Figures S1–S4 do not contain an XML-defined ERPO for reductive elimination (Ni(II) diorganyl → Ni(0) + R–R'), which is the final step of the Kumada cycle.
   
   **Resolution (2026-05-20 PM co-author meeting; ChemOntology maintainer 回答)**: 
   - 固有 keyword としての "ReductiveElimination" ERPO は定義されていない、ただし **2 つの代替対応** が定義されている:
     - **(α) BetaHydrideElimination ERPO 内包**: Nath et al. 2026 p. 2115 (PAGE 11) で Figure 8 の caption の記述 (paraphrase: the β-hydride elimination step is described as reversible, as having reductive-elimination character, and as giving back the active Pd(0) catalyst) として β-HE の reversibility に reductive elimination 性質を内包する記述あり — **ただし Heck workflow に specific** (alkene release 経由)、Kumada-style cross-coupling RE (Ni(II) diorganyl → Ni(0) + R-R' direct C-C formation) には適合せず
     - **(β) Fragmentation ERPOs (Association_of_Ri + Dissociation_of_Ri)** — SI Table S2 既定義の Conceptual ERPOs を user-side で組み合わせ使用; M 中心から 2 配位子が C-C bond を形成しつつ dissociate するプロセスを `Dissociation_of_Ri` で明示表現可能
   - **Paper B Phase 1 採用 path**: **Option (β) Fragmentation ERPO** (新 XML authoring 不要、既 Conceptual ERPOs 流用) — Kumada / Suzuki / Negishi / Stille / Sonogashira 共通 cross-coupling RE infrastructure として generalizable
   - **Phase 1 Core 実行中に sub-decision empirical validation**: (β-i) Stepwise chain `Dissociation_of_Ri(Ph)` + `Dissociation_of_Ri(n-Bu)` + `Association_of_Two_Components(Ph, n-Bu)` の 3 ERPO chain vs (β-ii) Compound formulation (1 step で 2 dissociations + 1 association) — AFIR pathway search が concerted RE TS を direct に traverse できるか Sub-run A の TS_RE_cross_PhnBu computation で確認 (cost ~0, L-8 in-situ validation と integrated)
   - **Affected EP rows (mapping table)**: EP-03a / EP-04a / EP-05a / EP-06a / EP-10a の `Required ERPO(s)` column を "ReductiveElimination (new ERPO required)" → "Dissociation_of_Ri (Fragmentation ERPO, RE pattern; β-i or β-ii sub-option pending operational validation)" に置換 (mapping table 内で本日 reflect 済)
   - Status: ✅ **resolved** (新 XML authoring 不要); operational sub-validation は Sub-run A 実行内
2. **Product labeling gap.** SI Table S3 "ChemOntology product
   labeling" lists C2R1-C2R2 → Heck and (C1R1-C1R2)-(C2R1-C2R2) →
   Wilkinson but marks cross-coupling-relevant combinations
   (C1R1-C1R2, C1R1-C2R2, etc.) as "Not labeled yet". Kumada-specific
   labeling—C1R1 (aryl halide with FG) + C1R3 (R-MgBr with FG) →
   cross-coupling product Ar–R—needs to be added before
   ChemOntology-AFIR can classify Kumada outputs automatically.
3. **`allowed_changes` per-SU values for NiCl₂(dpe) system.** Discussion
   2 as drafted states "S = 3 is considered appropriate" without
   specifying M and L. The Heck input (SI Fig S5) uses M = 1 (Pd) and
   L = 0 (PPh₃). For NiCl₂(dpe): M = 1 is a reasonable starting
   value for Ni but the d¹⁰/d⁸ redox flexibility may warrant M = 2 to
   allow more hybridization changes at the metal during OA/RE; L = 0
   is appropriate for the bidentate dpe if it is assumed not to
   decompose. Confirmation from a computational co-author is requested.
4. **EP-04a content in Discussion 2.** The current Discussion 2 draft
   associates EP-04a with cross-vs-homo-coupling selectivity, which
   in Stage 3 v2 is the content of EP-05a. EP-04a in Stage 3 v2 is
   about cis/trans-stilbene stereo-discrimination (SRG-6). The
   insertion draft corrects this.
5. **Ni d-orbital accuracy at the GFN2-xTB level.** The ChemOntology
   paper explicitly states that GFN2-xTB was "proven reliable for
   palladium systems"; Ni is not addressed. For EP-03a, EP-04a, EP-06a,
   EP-08a, EP-09a, DFT refinement is therefore marked mandatory
   rather than optional. Functional and basis-set selection require
   chemistry-expert judgment (not decided in this Layer A work).
