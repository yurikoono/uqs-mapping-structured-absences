prompt_version: stage2f-v7-20260417

---

**[F. Within-Group Comparison]**

**Group composition:** G3 — Methodological Expansion (ligand, photoredox, asymmetric axes; 1972–2016)
- Kumada 1972 (JACS Communication): foundational Ni-diphosphine cross-coupling method, S0–S2 base case
- Monnereau 2009 (Adv. Synth. Catal. Full Paper): cationic Ni-calix[4]arene-diphosphine catalyst with bite-angle-dynamics hypothesis
- Molander 2016 (Acc. Chem. Res. Account): photoredox/Ni dual catalysis for sp³–sp² SET-transmetalation paradigm
- Morken (Eno/Lu/Morken) 2016 (JACS Communication): Ni/PyBox-catalyzed asymmetric Kumada desymmetrization of cyclic sulfates

---

**Repeated patterns**

**RP-1: Catalytic cycle proposed without independent characterization of any named intermediate**

All four papers present a multi-step catalytic cycle (Ni(0)/Ni(II) or NiI/NiIII manifold) whose elementary steps and on-cycle intermediates are neither isolated, observed spectroscopically, nor kinetically constrained under the actual reaction conditions.

evidence_chain: [Kumada_1972 : A-2, B-12, U-2 | Monnereau_2009 : U-1, U-2, B-6 | Molander_2016 : U-1, U-2, U-7, B-5 | Morken_2016 : U-1, B-13, B-5, B-6]

- Kumada 1972: cycle (eqs 2–4) built by analogy from stoichiometric (dipy)Ni; black mixture (B-12) consistent with Ni⁰ but uncharacterised.
- Monnereau 2009: 41.8 ppm activation product oxidation state unknown (U-1); no kinetic data for fanning-RE causal chain (U-2); 65 °C activation fraction unquantified (B-6).
- Molander 2016: NiI/NiIII intermediates spectroscopically unobserved (U-1); no Stern–Volmer for SET; A1 vs B1 PES not solvation-tested (U-7).
- Morken 2016: PyboxNi(Ar) complex C, Ni(II) alkyl-aryl D, Ni sulfate E, TS — none observed; transmetalation step (E→C) kinetically untested (B-13).

---

**RP-2: Mechanistic conclusion derived from a single discriminator without alternative-hypothesis exclusion**

Each paper rests its mechanistic claim on one or two probe experiments insufficient to exclude alternative manifolds.

evidence_chain: [Kumada_1972 : U-1 (R–R prediction untested) | Monnereau_2009 : U-2, U-3 (rigid-analogue control absent), U-4 (Ni(I)/Ni(III) not excluded) | Molander_2016 : U-1, U-2 (single PES, single solvation, no spin-state), U-4 (DKR same PES) | Morken_2016 : B-5 (cyclopropylcarbinyl clock cannot discriminate Ni(I)/Ni(III) if RE>10⁸ s⁻¹), B-6 (RE-retention assumed, untested)]

---

**RP-3: Self-contradictory absence — the paper's own model predicts an observable that the paper does not test**

evidence_chain: [Kumada_1972 : U-1 (eq 3 → R–R byproduct, not reported), U-2 (homogeneous cycle vs black mixture) | Monnereau_2009 : U-1 (Ni(0) cycle assumed → 41.8 ppm species not assigned), U-3 (dynamic claim → rigid analogue not tested), A-3 (congested ArBr scope claim vs bromomesitylene 780 h⁻¹ outlier) | Molander_2016 : U-1 (B1 ~6 kcal/mol gap → solvation/spin sensitivity unreported), U-3 (E_ox-based selectivity → CV absent for trifluoroborate series), U-5 (DKR predicts ee → eq 2 founding 50% ee not interrogated), U-6 (HAT mechanism → k_HAT/k_add unmeasured) | Morken_2016 : U-2 (axial conformer claim → equatorially-locked control absent), CLA-2 (Ar₂Mg vs ArMgBr — cycle drawn with ArMgBr but aging text implies Ar₂Mg)]

---

**RP-4: Quantitative analytical basis for the primary measurement underreported**

evidence_chain: [Kumada_1972 : B-2 (glpc/isolated mixed), B-7 ("and/or[REDACTED: substantial verbatim quotation; see Tier 9]average of two" without SD), B-1 (no GC conversion alongside isolated)]

---

**RP-5: Benchmark superiority asserted without matched-pair comparison on shared substrate**

evidence_chain: [Kumada_1972 : C-1 (Tamura-Kochi cited, no shared-substrate yield), C-2 (Corey/Whitesides set aside), A-4 (concurrent Corriu-Masse forgotten) | Monnereau_2009 : B-3 (dppp comparison single substrate, single 5000 loading, not at 50000), C-10 (prior NiBr₂/propyl [19] not numerically compared), B-4 (ArCl at 5000 only) | Molander_2016 : C-1 (refs 7a–7f Pd-Suzuki: Figure 2 conditions cited, no shared-substrate yield), C-2 (Figure 1B qualitative dot-matrix only), C-3 (Tamao 1976 / Stille 1983 rate trend invoked without numbers) | Morken_2016 : C-1/C-2/C-3 (Fu, Zhong-Bian, Nakamura enantioconvergent: cited, no er/yield comparison), C-4/C-5/C-6 (Breit, Carretero, Jarvo enantiospecific C–O: cited and contrasted without numbers)]

---

**RP-6: Scope failures reported qualitatively without mechanistic attribution**

evidence_chain: [Kumada_1972 : B-4 (sp³ exclusion asserted as feature, no failed example), B-5 (THF "definitely inferior[REDACTED: substantial verbatim quotation; see Tier 9]performed poorly", no values) | Morken_2016 : B-3 (quaternary/tertiary-alcohol substrates "ineffective[REDACTED: substantial verbatim quotation; see Tier 9]near-racemic", no values)]

---

**Cross-field temperature patterns**

temperature_pattern: RP-1 (cycle without intermediate observation) | papers: [all four] | profile_consistency: consistent | note: V2 (mechanistic) consistently rates this gap high-to-critical: Kumada A-2 V2=high; Monnereau U-2 V2=high (3/3); Molander U-1 V2=high (3/3); Morken U-1 V1=high/V2=high (2/3). The mechanistic-specialist viewpoint sees the gap acutely while V1 (synthetic-utility) accepts it as era-tolerated communication-format compression.

temperature_pattern: RP-3 (self-contradictory absence) | papers: [all four] | profile_consistency: consistent | note: Each paper independently generates the same structural pattern (model predicts → prediction untested) regardless of decade or paradigm. In Monnereau and Molander the count of self-contradictory U items (3 and 4 respectively) is large; in Kumada and Morken the count is smaller (2 each) but the structural pattern is identical. The cross-paper consistency is the dominant cross-field temperature signal of G3.

temperature_pattern: RP-4 (analytical underreporting) | papers: [all four] | profile_consistency: consistent | note: V3 (analytical) raises severity wherever a primary measurement is the load-bearing claim: Monnereau B-7 V3=high; Molander B-5 cluster V3=high (3/3); Morken U-3 V3=high. The strongest convergence item is Molander B-5 (V1=high/V2=high/V3=high, 3/3) — DFT validation data absence — paralleling Monnereau's B-7/U-1 (TOF denominator) 3/3 in G3 of the prior cycle.

temperature_pattern: RP-5 (asserted benchmark superiority) | papers: [all four] | profile_consistency: consistent | note: V1 raises severity when superiority claims rest on omitted comparisons (Monnereau B-3 V1=high; others V1=medium). No paper performs a matched-pair head-to-head comparison on a common substrate; the field-wide convention is stable across all four papers and three formats.

---

**Same-root group patterns**

recurring_root: Catalytic cycle proposed without elementary-step or intermediate validation | papers: [Kumada_1972, Monnereau_2009, Molander_2016, Morken_2016] | member_items: [Kumada_1972: SRG-1 (A-2, U-1, U-2, B-12); Monnereau_2009: SRG-1 (U-2, U-3, A-1, A-2) + SRG-3 (U-1, B-6); Molander_2016: SRG-1+SRG-2+SRG-3 (B-5, U-1, U-2) + CLA-1 (Ni(I)/Ni(III)); Morken_2016: SRG-1 (B-5, B-6, U-1) + SRG-2 (U-1, B-13)] | note: This is the structural backbone of G3 and persists across all four papers regardless of reaction type (thermal KTC, photoredox/Ni, asymmetric desymmetrization), publication era (1972–2016), or format (Communication, Full Paper, Account). Not "individually chosen": no paper meets the standard. Genre convention — mechanism sections in cross-coupling methodology papers serve narrative contextualization rather than hypothesis testing.

recurring_root: Quantitative measurement basis underreported relative to the load-bearing claim | papers: [all four] | member_items: [Kumada_1972: SRG-5 (B-2, B-7, B-9, B-11); Monnereau_2009: SRG-6 (B-1, B-2) + SRG-8 (B-7, B-8, C-13); Molander_2016: SRG-7 (B-2, B-3, B-4) + SRG-8 (B-1, B-9); Morken_2016: SRG-5 (U-3, B-8)] | note: Genre convention across JACS, Adv. Synth. Catal., Acc. Chem. Res., and JACS again; format-tolerated in the communication and Account formats but the load-bearing claim shifts from yield (Kumada) to TOF (Monnereau) to mechanism (Molander) to er (Morken) — in every case the primary metric lacks SD, calibration, or full method specification.

recurring_root: Asserted superiority over prior art without matched-pair comparison | papers: [all four] | member_items: [Kumada_1972: SRG-6 (C-1, C-2, A-4); Monnereau_2009: SRG-7 (B-3, B-4, C-10); Molander_2016: C-1, C-2, C-3, C-9; Morken_2016: SRG-7 unattributed + C-1/C-2/C-3/C-4/C-5/C-6 symmetric prior-art groups] | note: Every paper positions against named prior art without performing common-substrate, matched-condition yield/er comparison. Field-wide convention.

recurring_root: Mechanism imported from a structurally non-isomorphous system | papers: [Kumada_1972, Monnereau_2009, Molander_2016, Morken_2016] | member_items: [Kumada: A-2 (dipy-Ni → dpe-Ni stoichiometric→catalytic); Monnereau: C-14, U-4 (Pd diphosphine [27,28] → Ni); Molander: SRG-1+SRG-3+SRG-10 (SMD-water PES → acetone/dioxane, benzylic → 9 substrate classes); Morken: SRG-2+SRG-3 (organic SN2 attack-geometry → PyBox-Ni; Ni(0)/Ni(II) general manifold → cyclic sulfate)] | note: RI-06 "imported model" is a structurally recurring root. Each paper imports a cycle, manifold, or attack-geometry from a non-isomorphous source without demonstrating isomorphism; the import is operational rather than acknowledged.

---

**Temporal trajectory of recurring patterns**

temporal_trajectory: RP-1 (cycle without intermediate observation) | classification: shifting | transition_point: 2016 (Molander photoredox + Morken asymmetric) | note: 1972: 2-electron Ni(0)/Ni(II) cycle by analogy (no in situ tools — structurally suppressed). 2009: same paradigm with new ligand class, plus a 41.8 ppm species characterised only by chemical shift (tools available but not deployed). 2016 (Molander): mechanism shifts to NiI/NiIII photoredox manifold — fundamentally different paradigm, same pattern (DFT PES imported, intermediates unobserved). 2016 (Morken): back to 2-electron-like SN2 OA, same mechanistic-evidence absence under a different substrate class. The character of the gap changes (no tools → tools available; thermal → photoredox; achiral → chiral) but the structural pattern is invariant. *Shifting* rather than *time-invariant* because the paradigm itself moved while the gap migrated with it.

temporal_trajectory: RP-2 (single-discriminator mechanism) | classification: time-invariant | transition_point: n/a | note: 1972 inferred SN2-like by 5-feature heuristics + (dipy)Ni analogy; 2009 inferred fanning-RE causal chain from one PES + structural data; 2016 (Molander) inferred B1 pathway from one PES; 2016 (Morken) inferred SN2-like OA from one radical clock + one ds measurement. Each generation uses one or two probes despite their qualitative insufficiency.

temporal_trajectory: RP-3 (self-contradictory absence) | classification: time-invariant | transition_point: n/a | note: Specific predictions change (R–R byproduct → fanning-RE coupling → NiIII intermediates → axial-conformer reactive geometry) but the structural pattern (model predicts observable → observable not tested) is invariant.

temporal_trajectory: RP-4 (analytical underreporting) | classification: time-invariant | transition_point: n/a | note: 1972: glpc conditions absent. 2009: GC response factors absent, no replicates. 2016 (Molander): yield type unspecified across 40+ scope entries. 2016 (Morken): SFC column/conditions absent for 17 er values, "average of two" without SD. Unchanged across 44 years.

temporal_trajectory: RP-5 (benchmark asserted) | classification: time-invariant | transition_point: n/a | note: Stable feature of all four papers across all formats and eras.

temporal_trajectory: RP-6 (undiagnosed scope failures) | classification: time-invariant | transition_point: n/a | note: Kumada (sp³ exclusion no failed example); Monnereau (bromomesitylene outlier no comment); Molander (compound 64 32% no electronic attribution); Morken (quaternary substrates "ineffective" no data). Persists.

---

**Structural suppression vs. individual choice**

RP-1 (cycle without intermediate validation):
- *Era-dependent*: structurally suppressed (1972: limited in situ NMR/EPR for Ni) → individually chosen (2009: VT-NMR available but only deployed for ligand dynamics not Ni intermediate; 2016 Molander: EPR/Stern–Volmer/radical clock all available for Ni mechanism, not deployed for the central B1-pathway claim; 2016 Morken: stoichiometric PyboxNi(II)(alkyl)(aryl) synthesis is established but not performed). The 1972→2016 transition occurs around 1990 with the maturation of Ni in-situ tools.

RP-2 (single discriminator):
- *Individually chosen* (2009 onward): Hammett analysis, Stern–Volmer, EPR, variable-temperature ee, radical clocks of multiple rates, and DFT solvation-sensitivity tests are all routine and feasible within each paper's experimental program. Their non-deployment is a methodology choice, not a tool gap.

RP-3 (self-contradictory absence):
- *Individually chosen*: Every untested prediction is testable with the paper's own infrastructure. R–R glpc (Kumada), Ni oxidation-state assignment (Monnereau), CV for trifluoroborate E_ox (Molander), equatorially-locked sulfate (Morken) — all single experiments within each paper's capability.

RP-4 (analytical underreporting):
- *Incentive-suppressed*: No journal in 1972 (JACS), 2009 (Adv. Synth. Catal.), 2016 (Acc. Chem. Res.), or 2016 (JACS) requires replicate data, response factor calibration, full DFT validation tables, or chiral chromatography column documentation in the main text. Publishing this information alone does not constitute an independent contribution. SI culture absorbs the documentation in 2009/2016 but Acc. Chem. Res. has no SI and JACS Communication SI is not in scope here.

RP-5 (benchmark superiority asserted):
- *Incentive-suppressed*: Performing matched-pair comparisons risks demonstrating the new method is not superior on the comparator's preferred substrate. The incentive structure of methodology papers rewards scope demonstration over head-to-head benchmarking.

RP-6 (scope failures undiagnosed):
- *Format-suppressed* in part (1972 Communication, 2016 Morken Communication compress failure analysis) and *individually chosen* in part (Monnereau 2009 Full Paper has space; Molander 2016 Account has 11 pages). Genuine analytical work (Hammett of failure substrates, electronic-vs-steric discrimination experiments) is feasible in all four formats but is not pursued.

---

**Paradigm competition**

G3 reveals three coexisting paradigms — not sequential replacements:

**Paradigm 1: Ligand design for 2-electron Ni(0)/Ni(II) catalysis (Kumada 1972; Monnereau 2009)**
Both operate within the same catalytic manifold (OA → transmetalation → RE) with Grignard nucleophiles and aryl halide electrophiles. Expansion axis: ligand architecture (dppe → calixarene-diphosphine).

Systematically unanswered question:
- What structural and electronic features of the diphosphine ligand quantitatively determine the rate-limiting step and overall selectivity?
  evidence_chain: [Kumada_1972 : B-3 (ligand order from one substrate, no yields), B-5 (solvent superiority claim no data); Monnereau_2009 : U-3 (RE-vs-OA rate-limiting step inferred qualitatively), B-3 (dppp comparison restricted), "no textual basis in Molander_2016 or Morken_2016" — these papers do not report ligand-rate structure–activity studies for their own ligand class]

**Paradigm 2: Single-electron activation via photoredox/Ni dual catalysis (Molander 2016)**
Fundamentally different activation mode: organotrifluoroborates / alkylsilicates undergo SET to generate carbon radicals that enter a NiI/NiIII manifold. No Grignard reagent; no 2-electron transmetalation.

Systematically unanswered question:
- What is the dominant quencher of the excited photocatalyst, and what is the operational rate competition between SET, Ni-radical capture, and HAT under turnover conditions?
  evidence_chain: [Molander_2016 : U-1 (Stern-Volmer absent), U-2 (NiI/NiIII undetected), U-6 (HAT k vs Ni-trapping k unmeasured); "no textual basis in Kumada_1972, Monnereau_2009, or Morken_2016" — the question does not arise in the 2-electron paradigm]

**Paradigm 3: Enantioselective desymmetrization via Ni/chiral PyBox (Morken 2016)**
Combines 2-electron SN2-like OA with a chiral PyBox to achieve enantioselective coupling of prochiral bis-electrophiles — a new selectivity axis (enantiocontrol) rather than a new activation mode.

Systematically unanswered question:
- Is enantioselectivity kinetically or thermodynamically controlled, and at which elementary step is stereochemical information set?
  evidence_chain: [Morken_2016 : U-2 (axial reactive conformation non-uniquely supported), B-9 (no Eyring or DFT discrimination), B-6 (RE-retention assumed); [REDACTED: substantial verbatim quotation; see Tier 9] — the kinetic-vs-thermodynamic question maps differently across paradigms]

**Coexistence not succession; a shared blind spot:** The three paradigms in G3 are not sequential replacements — they coexist as independent methodological expansions from the 1972 Ni-Grignard origin. However, all three paradigms share the same blind spot: catalytic-cycle / mechanistic-evidence gap (RP-1, RP-2). The shared gap persists regardless of paradigm, suggesting it is a field-wide structural convention rather than a paradigm-specific limitation. Cross-paradigm gap left by paradigm 1 (no ligand-architecture quantitative SAR) is not occupied by paradigm 2 (Molander uses the same imported general Ni manifold without SAR for photoredox-Ni systems) or paradigm 3 (Morken uses imported general Ni manifold and imports SN2 attack-geometry from organic chemistry). The relationship is *parallel coexistence* not *succession*.

---

**Divergences**

**DV-1: Nucleophile/activation mode defines the paradigm**
Kumada/Monnereau use Grignard reagents (2-electron polar nucleophile). Molander uses organotrifluoroborates / alkylsilicates (1-electron radical precursors). Morken uses ArMgBr but with prochiral electrophiles. The nucleophile/activation choice determines the entire mechanistic manifold and the question space.

evidence_chain: [Kumada_1972 : S0-4 → ArMgBr/RMgX | Monnereau_2009 : S0-4 → PhMgBr | Molander_2016 : S0-4 → BnBF₃K, alkylsilicates | Morken_2016 : S0-4 → ArMgBr]

**DV-2: Metric of success diverges**
Kumada: yield + scope. Monnereau: TOF (kinetic metric). Molander: paradigm + scope breadth. Morken: er (enantioselectivity).

evidence_chain: [Kumada_1972 : D-1 → yield, β-H tolerance, sp² Cl reactivity | Monnereau_2009 : D-1 → TOF up to 21250 h⁻¹ at 10⁻³ mol% | Molander_2016 : D-1 → "mechanistic sea-change" + 8 substrate classes | Morken_2016 : D-1 → 96:4 er, asymmetric tertiary carbon centers]

**DV-3: Format dictates evidentiary depth ceiling**
Communication (1972, 2016-Morken) vs Full Paper (2009) vs Account (2016-Molander). The Account is uniquely permissive of data-absence-by-citation (Molander reproduces Figure 9 PES from ref 24). The Full Paper has space but underdocuments anyway. Communications structurally compress.

evidence_chain: [Kumada_1972 : D-3 → JACS Communication 3pp | Monnereau_2009 : D-3 → Adv. Synth. Catal. full paper 7pp | Molander_2016 : D-3 → Acc. Chem. Res. Account 11pp | Morken_2016 : D-3 → JACS Communication 4pp]

**DV-4: Era-dependent mechanistic-tool deployment expectations**
1972: tools genuinely scarce. 2009: VT-NMR deployed (for ligand dynamics) but EPR/Stern–Volmer/Hammett not deployed for Ni. 2016: full mechanistic toolkit available but selectively deployed (Molander uses CV for silicates only; Morken uses one radical clock and one deuterium label).

evidence_chain: [Kumada_1972 : §4 era-norm | Monnereau_2009 : VT-NMR for fanning, no kinetics | Molander_2016 : DFT + CV silicate only | Morken_2016 : single clock + single ds]

---

**U-item patterns**

recurring_U: Self-contradictory absence — model predicts a specific observable that the paper does not test | papers: [all four] | item_ids: [Kumada_1972: U-1, U-2; Monnereau_2009: U-1, U-2, U-3; Molander_2016: U-1, U-2, U-3, U-5, U-6, U-7, U-8; Morken_2016: U-1, U-2, U-3, U-4] | note: U-items are again the largest single recurring category. Their accumulation across papers, paradigms, formats, and decades suggests that the A/B/C classification framework captures individual paper omissions well but does not naturally capture the recursive pattern of "model predicts observable → observable not tested" that is endemic to cross-coupling methodology papers. The pattern is robust across the introduction of new paradigms (photoredox-Ni in Molander introduces new self-contradictory absences specific to SET + spin-state PES analysis, identical structural form to Kumada's R–R-byproduct gap).

recurring_U: Imported-model prerequisite-absence — operational basis of an imported analogy not established | papers: [Monnereau_2009, Molander_2016, Morken_2016] | item_ids: [Monnereau: U-4 (Pd analogy); Molander: U-2 (spin-manifold consistency for cross-pathway ΔG comparison), U-7 (single-substrate PES generalised to 9 classes); Morken: U-1 (general Ni cycle imported), CLA-2 (organic SN2 attack-geometry imported)] | note: Imported-model U items have a distinct character from observation-omission U items: they reveal that the operational basis for an analogical inference is asserted not established. This sub-pattern within recurring_U becomes salient only when the corpus includes papers that import models explicitly; in G3 it is present in three of four papers and entirely absent in Kumada 1972 (which used the dipy→dpe analogy but with explicit "working hypothesis" hedging). Suggests temporal trajectory: the imported-model U-item subtype emerges as theoretical/computational tools become routine and are deployed without isomorphism validation.

---

**Self-contradictory absence patterns**

self_contradictory: [Kumada_1972] : eq 3 catalytic cycle → R–R byproduct predicted → no R–R reported, no detection limit | item_id: U-1
self_contradictory: [Kumada_1972] : homogeneous Ni(II) cycle → black mixture (Ni⁰ candidate) observed → unanalyzed | item_id: U-2
self_contradictory: [Monnereau_2009] : Ni(0)/Ni(II) cycle assumed → 41.8 ppm activation product oxidation state not assigned → cycle entry unverified | item_id: U-1
self_contradictory: [Monnereau_2009] : dynamic-bite-angle hypothesis → rigid analogue would test it → not synthesised; deferred to future work | item_id: U-3 (linked A-1)
self_contradictory: [Monnereau_2009] : "high activities with congested bromoarenes" claim (abstract) → bromomesitylene 780 h⁻¹ in same Table 3 → not discussed | item_id: A-3
self_contradictory: [Molander_2016] : SMD-water PES with ~6 kcal/mol B1>A1 → reactions in acetone/MeOH (ε differs by ~4×), dioxane (ε differs by ~36×) → no solvation sensitivity | item_id: U-1
self_contradictory: [Molander_2016] : closed-shell singlet A1-TS vs open-shell doublet B1-TS compared on single PES → spin-manifold consistency unverified | item_id: U-2
self_contradictory: [Molander_2016] : Figure 4A E_ox-based reactivity hierarchy claim → CV reported only for alkylsilicates, not for trifluoroborates whose hierarchy is the load-bearing claim | item_id: U-3
self_contradictory: [Molander_2016] : DKR model predicts ee from ΔΔG‡ for all chiral systems → eq 2 founding 50% ee with L1 not computed within the model | item_id: U-5
self_contradictory: [Molander_2016] : HAT mechanism predicts rate competition between thiol-H abstraction and Ni-radical trapping → k_HAT/k_add unmeasured | item_id: U-6
self_contradictory: [Molander_2016] : single-substrate (benzylic) PES → mechanistic conclusions extended to 9 substrate classes with different E_ox and radical stability | item_id: U-7
self_contradictory: [Morken_2016] : four-intermediate catalytic cycle (C, D, E, TS) drawn → none observed, no kinetic constraint | item_id: U-1
self_contradictory: [Morken_2016] : er-insensitivity to C5 substituent size → axial reactive conformer claim non-uniquely supported (equatorial+backside attack equally consistent) | item_id: U-2
self_contradictory: [Morken_2016] : 17-entry SFC er dataset is the primary novelty evidence → SFC column/conditions not documented in communication | item_id: U-3
self_contradictory: [Morken_2016] : cycle drawn with ArMgBr transmetalation in step E→C → text identifies aging-induced Ar₂Mg / MgBr₂ precipitation as the active speciation | item_id: U-4 (CLA-2)

**Recurring pattern assessment:** Self-contradictory absence is the densest recurring pattern across G3, appearing in every paper regardless of mechanism type, paradigm, era, or format. The pattern reflects a **narrative function of mechanism diagrams in methodology papers** (cycle diagrams, PES schemes, and stereochemical models serve to organise synthetic results rather than to generate testable predictions), simultaneously a **genre convention** (expected by editors/reviewers; the convention persists because either confirming a prediction is unpublishable or falsifying it requires a different paper), and a **genuine analytical gap** (each prediction is individually testable within the paper's own infrastructure). The 2016 papers (Molander 7 instances; Morken 4 instances) show higher per-paper density than the 1972/2009 papers (2 and 3 respectively), suggesting that as mechanistic narratives become more sophisticated (DFT PES, DKR Curtin-Hammett, SN2-like asymmetric OA), the count of self-contradictory absences embedded in those narratives also grows.

---

**Group-level unasked question**

[REDACTED: substantial verbatim quotation; see Tier 9]

evidence_chain: [Kumada_1972 : A-2 (cycle from analogy), B-12/U-2 (heterogeneous candidate untested), U-1 (R–R byproduct prediction untested) | Monnereau_2009 : U-1 (active species identity), U-2 (fanning-RE causal chain), U-3 (rigid-analogue control deferred), U-4 (Ni(I)/Ni(III) not excluded) | Molander_2016 : U-1, U-2 (PES reliability + spin-manifold consistency), U-4 (DKR), U-5 (eq 2 ee), U-7 (PES generalisation) | Morken_2016 : U-1 (all four cycle intermediates unobserved), B-5/B-6 (single discriminating probes with unstated assumptions), U-3 (SFC undocumented), U-4/CLA-2 (Grignard speciation in cycle)]

TEMPERATURE_SUMMARY correspondence: The group-level question maps to the strongest convergence items in each paper. Kumada A-2 V1=high/V2=high (2/3); Monnereau U-1, U-2 both 3/3 high; Molander B-5/U-1/U-2 cluster 3/3 V1=high/V2=high/V3=high; Morken B-6 3/3 high. The strongest convergence items across all four papers concern the gap between mechanistic claims and their experimental evidence base — the group-level unasked question is precisely this gap at the field level.

recurring_root correspondence: The group-level question subsumes all four recurring roots (cycle without intermediate validation; analytical underreporting; asserted superiority without matched comparison; mechanism imported without isomorphism) as facets of a single problem: the field has no agreed standard for what constitutes sufficient evidence for a mechanistic claim in Ni-catalyzed cross-coupling, regardless of activation mode (2-electron / SET / asymmetric) or methodological expansion axis. Each paper proposes a mechanism at a different rhetorical level of certainty — from "working hypothesis" (Kumada 1972) through "likely to rely on" (Monnereau 2009) to "Mechanistic experiments point to ... stereoinvertive" (Morken 2016 abstract) and [REDACTED: verbatim source quotation; see the source paper via its DOI] (Molander 2016 §2.5) — but the evidentiary standard for each level is nowhere defined or enforced. The expansion axes of G3 (ligand architecture, activation mode, selectivity) compound the same gap: each new expansion is published with mechanistic narrative weight commensurate with its novelty rhetoric, not with its mechanistic evidence base.

---

*End of G3 v18.4 Opus 4.7 output.*

---

> **Tier 8 redaction notice**: This file is a redacted copy of the corresponding Tier 3 / Tier 9 output. Verbatim source-paper quotations have been replaced by `[REDACTED: see source paper §<loc>; full text retained in Tier 9 reviewer-only deposit]` markers, preserving location references and our own analytical content. Bibliographic fields (title, authors, journal, year, DOI), analytical labels (`evidence_chain:` with B-/U-/A-/C- internal IDs), short technical terms, and our own analytical text are not redacted. The redaction was applied by `scripts/redact_for_tier8.py` and, for this version, by `scripts/build_paperA_R1_public.py` with `scripts/redact_source_ngram_runs.py` (scripts of the project repository; they are not deposited).
