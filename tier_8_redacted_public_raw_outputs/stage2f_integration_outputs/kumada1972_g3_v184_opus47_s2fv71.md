prompt_version: stage2f-v7-20260417

---

**[F. Within-Group Comparison]**

**Group composition:** G3 — Methodological Expansion (ligand, substrate, condition axes; 1972–2016; v18.4 Sonnet trajectory)
- Kumada 1972 (JACS Communication): foundational [NiCl₂(dpe)] cross-coupling of Grignard reagents with sp² halides
- Monnereau 2009 (Adv. Synth. Catal. full paper): cationic NiCp/calix[4]arene-diphosphine catalyst with dynamic bite-angle hypothesis (TOF up to 21,250 h⁻¹)
- Molander 2016 (Acc. Chem. Res. Account): photoredox/Ni dual catalysis paradigm for sp³–sp² cross-coupling via SET
- Morken 2016 (JACS Communication, "molken2016"): Ni-catalyzed asymmetric Kumada desymmetrization of prochiral cyclic sulfates with PyBox

---

**Repeated patterns**

**RP-1: Catalytic cycle / mechanistic intermediates proposed without direct experimental validation**

All four papers advance a Ni catalytic cycle (or mechanistic framework) whose elementary steps and named intermediates are neither observed nor independently kinetically constrained under operative conditions.

evidence_chain: [Kumada_1972 : A-2, B-2 (Stage2 SRG-1), B-12, U-1, U-2 | Monnereau_2009 : U-1, U-2, U-3, A-1, A-2 (Stage2 SRG-1, SRG-3) | Molander_2016 : B-5, U-1, U-2, U-7 (Stage2 SRG-1+SRG-3+SRG-10) | Morken_2016 : B-5, B-6, B-13, U-1 (Stage2 SRG-1, SRG-2)]

- Kumada 1972: cycle drawn from analogy to stoichiometric (dipy)Ni reactions (refs 11–12); none of the three intermediates (1, 2, 3) characterized; black mixture (B-12) consistent with Ni⁰ nanoparticles uncharacterized.
- Monnereau 2009: thermal activation product (δ ³¹P = 41.8 ppm) characterized only by a single chemical shift; oxidation state unassigned; bite-angle-dynamics hypothesis lacks rate-law / Hammett / control experiment.
- Molander 2016: Figure 9 PES reproduced from Gutierrez 2015 with no ⟨S²⟩ values, ZPE provenance, or solvation sensitivity; NiI/NiIII intermediates spectroscopically unobserved; no Stern–Volmer or radical-clock probe.
- Morken 2016: PyBoxNi(Ar) complex C, Ni(II)(alkyl)(aryl) D, Ni(II) sulfate E, and TS proposed in Scheme 4 with no spectroscopic, electrochemical, or kinetic data for any.

---

**RP-2: Quantitative measurement basis for primary data underreported**

All four papers ground their headline quantitative claims in measurements whose analytical reliability cannot be independently assessed from the published text.

evidence_chain: [Kumada_1972 : B-2, B-7, B-9, B-11 (Stage2 SRG-5) | Monnereau_2009 : B-1, B-2, B-7 (Stage2 SRG-6, SRG-8) | Molander_2016 : B-1, B-9 (Stage2 SRG-7, SRG-8) | Morken_2016 : U-3, B-8 (Stage2 SRG-5)]

- Kumada 1972: glpc internal standard / response factors absent; isolated and glpc yields mixed in the same column without justification; no replicates; cis:trans ratio analytical method missing.
- Monnereau 2009: GC-conversion-only across 24 entries; no isolated yields; global <3% homocoupling claim with no per-substrate breakdown; crystallographic GoF = 0.882 / wR2 = 17.48% below threshold.
- Molander 2016: yield type (isolated vs. GC) unspecified across all scope tables; mass balance for compound 11 (61% yield, "no polymerization") unsupported; outlier compounds (43, 64, 83/84) without attribution.
- Morken 2016: SFC chiral stationary phase identity, mobile phase, resolution factors absent for all 17 Table 2 entries; "average of two experiments" with no SD/range; Table 1 confounded by 6 h vs. 24 h deprotection.

---

**RP-3: Self-contradictory absence — model generates testable predictions left untested**

In every paper, the proposed mechanism or model predicts specific observables that the paper does not test, despite the predictions being addressable with the paper's own infrastructure.

evidence_chain: [Kumada_1972 : U-1, U-2 | Monnereau_2009 : U-1, U-2, U-3, U-5 | Molander_2016 : U-1, U-2, U-3, U-4, U-5, U-6 | Morken_2016 : U-1, U-2, U-4, CLA-2]

- Kumada 1972: eq 3 predicts homo-coupling byproduct R–R → not detected, quantified, or acknowledged below LOD; cycle predicts homogeneous Ni(II) → black mixture inconsistent with this is not characterized.
- Monnereau 2009: bite-angle-dynamics model predicts rigid-analogue should be slower → control not performed (acknowledged as deferred); cycle predicts Ni(0) entry → activation product oxidation state not confirmed; abstract claims "high activities with congested bromoarenes" → bromomesitylene gives lowest TOF (780 h⁻¹).
- Molander 2016: PES predicts ~6 kcal/mol B1 preference → not solvation-validated; DKR predicts ee from ΔΔG‡ → founding eq 2 datum (75:25 er, L1) never computed within DKR; mechanism predicts NiI/NiIII intermediates → never observed; HAT mechanism predicts rate competition → never measured.
- Morken 2016: cycle predicts ArMgBr as transmetalating species → aging protocol shifts speciation toward Ar₂Mg, not tested (CLA-2); design feature (b) predicts bis-coupling suppression → never quantified; reductive-elimination retention assumption → never independently established.

---

**RP-4: Benchmark superiority asserted without matched-pair experimental comparison**

Each paper positions itself against named prior art via citation but fails to provide direct numerical comparison on shared substrates under matched conditions at the headline performance regime.

evidence_chain: [Kumada_1972 : C-1, C-2, A-4 (Stage2 SRG-6) | Monnereau_2009 : B-3, B-4, C-10 (Stage2 SRG-7) | Molander_2016 : C-1, C-2, C-3 | Morken_2016 : C-1, C-2, C-3, C-4, C-5, C-6, C-7 (Stage2 RI-09)]

- Kumada 1972: Tamura-Kochi Fe and cuprate/π-allylnickel chemistry cited but no shared-substrate comparison; concurrent Corriu-Masse Ni(acac)₂ (footnote 3a) noted without comparison.
- Monnereau 2009: dppp comparison restricted to one substrate (4-bromoanisole) at one loading (5,000:1); not tested at the headline ultra-low loading (50,000:1) where complex 2 achieves 21,250 h⁻¹; prior NiBr₂/propyl-calixarene system [19] not numerically compared.
- Molander 2016: Figure 2 depicts six prior Pd Suzuki protocols' conditions but no head-to-head yield comparison on matched substrates; Labadie/Stille rate hierarchy invoked without rate constants.
- Morken 2016: Fu (ref 3), Zhong-Bian (refs 4a/4b), Nakamura (ref 5) enantioconvergent precedents and Breit/Carretero/Jarvo enantiospecific C–O precedents (refs 7–9) cited symmetrically with no er/yield comparison; Jarvo (closest structural analog) given identical cite-and-contrast treatment.

---

**RP-5: Imported model — mechanistic framework adopted from non-isomorphous source system**

Each paper imports its mechanistic narrative from an external source (analogous metal/system, prior PES, or organic SN2 logic) without demonstrating isomorphism for the actual catalytic system.

evidence_chain: [Kumada_1972 : A-2, B-12 → (dipy)Ni stoichiometric analogy (Stage3 RI-06) | Monnereau_2009 : C-14, U-4 → Pd diphosphine precedents (Stage3 RI-06 secondary) | Molander_2016 : B-5, U-1 → Gutierrez 2015 SMD-water PES (Stage3 RI-06 primary) | Morken_2016 : U-1, U-2 → Ni(0)/Ni(II) general manifold + organic SN2 attack geometry (Stage3 RI-06 secondary)]

- Kumada 1972: cycle imported from stoichiometric (dipy)Ni reactions; bite-angle/coordination mismatch with [NiCl₂(dpe)]; concentration regime mismatch.
- Monnereau 2009: Pd(0)/Pd(II) reductive-elimination bite-angle results from refs [27]/[28] applied to Ni without addressing Ni(I)/Ni(III) accessibility.
- Molander 2016: PES computed in SMD-water (ε≈80) for benzylic/PhBr applied to reactions in dioxane/acetone/EtOAc/DMF (ε = 2.2–38) and to nine substrate classes spanning benzylic to α-CF₃ to alkylsilicate to azaborine.
- Morken 2016: two-electron Ni(0)/Ni(II) manifold imported from general cross-coupling literature; SN2 in-line attack geometry imported from organic substitution chemistry without DFT validation for PyBox–Ni coordination geometry.

---

**RP-6: Scope failures reported qualitatively without mechanistic attribution or negative-result data**

Multiple papers identify substrate classes that fail or underperform but provide no quantitative data and no mechanistic explanation.

evidence_chain: [Kumada_1972 : B-4 → sp³ exclusion asserted, no failed sp³ halide reported | Monnereau_2009 : A-3 → bromomesitylene 15.6% / 780 h⁻¹ outlier suppressed in "congested bromoarenes" claim | Molander_2016 : B-4, B-8 → "amine-containing alkylsilicates performed poorly" with no yields | Morken_2016 : A-1, B-3, B-4 → "ineffective[REDACTED: substantial verbatim quotation; see Tier 9]lower yield, nearly racemic" with no values]

---

**Cross-field temperature patterns**

temperature_pattern: RP-1 (mechanism validation) | papers: [Kumada_1972, Monnereau_2009, Molander_2016, Morken_2016] | profile_consistency: consistent | note: Mechanism-evaluating viewpoints (V2 mechanistic + V3 computational/analytical) consistently rate mechanistic-validation gaps high. Convergence of V1+V2+V3 is observed for the central mechanistic claim in three of four papers (Monnereau U-1, U-2 = 3/3; Molander B-5/U-1 cluster = 3/3; Morken B-6 = 3/3, V1=high/V2=high/V3=high). Kumada's older era yields lower individual severity assignments (V1=high/V2=high, convergence 2/3) but the same pattern character. The convergence increases over time as analytical and computational tools mature (1972: 2/3 high; 2009: 3/3 high; 2016 Molander: 3/3 high; 2016 Morken: 3/3 high) — gap recognition narrows from mechanistic specialists alone to all viewpoints simultaneously.

temperature_pattern: RP-2 (analytical underreporting) | papers: [all four] | profile_consistency: consistent | note: V3 (analytical) consistently flags measurement-quality gaps at high severity once the gap involves chiral/stereochemical or structural data (Monnereau B-7 V3=high; Morken B-8 V3=high, U-3 V3=high). For yield-only datasets the V3 severity remains medium (Kumada B-2 V3=medium; Molander B-1 V1=medium). The asymmetry — V3 escalates from medium to high when chiral / structural primary data are at stake — is a stable feature across the corpus.

temperature_pattern: RP-3 (self-contradictory absence) | papers: [all four] | profile_consistency: consistent | note: Self-contradictory absence receives high severity wherever it is detected. Each paper independently generates the pattern across different mechanism types (2-electron, photoredox, asymmetric); the consistency across paradigms argues for field-wide convention rather than paper-specific oversight.

---

**Same-root group patterns**

recurring_root: Catalytic cycle proposed without elementary-step validation | papers: [Kumada_1972, Monnereau_2009, Molander_2016, Morken_2016] | member_items: [Kumada_1972 SRG-1 (A-2, U-1, U-2, B-12) | Monnereau_2009 SRG-1 (U-2, U-3, A-1, A-2) + SRG-3 (U-1, B-6) | Molander_2016 SRG-1+3 cluster (V1-Q4/V2-OV1/V3-OV1 → B-5/U-1) | Morken_2016 SRG-1 (B-5, B-6, U-1) + SRG-2 (U-1, B-13)] | note: Genre convention persisting across all four papers regardless of reaction type (thermal Kumada, calixarene-modulated Kumada, photoredox/Ni, asymmetric Kumada), publication era (1972–2016), format (Communication, full paper, Account), or target audience (synthetic, mechanistic, pharmaceutical). Mechanism sections in Ni-catalyzed cross-coupling papers serve narrative contextualization rather than hypothesis testing.

recurring_root: Quantitative measurement basis underreported | papers: [Kumada_1972, Monnereau_2009, Molander_2016, Morken_2016] | member_items: [Kumada_1972 SRG-5 (B-2, B-7, B-9, B-11) | Monnereau_2009 SRG-6 (B-1, B-2) + SRG-8 (B-7, B-8, C-13) | Molander_2016 SRG-7 (B-2, B-3, B-4) + SRG-8 (B-1, B-9) | Morken_2016 SRG-5 (U-3, B-8) + SRG-6 (B-7)] | note: Genre convention spanning JACS Communications, JACS full paper, Adv. Synth. Catal. full paper, and Acc. Chem. Res. Account formats. Not eliminable by format expansion: the 11-page Account (Molander) shows the same compression as the 4-page Communication (Morken). The convention is neither format-specific nor era-specific.

recurring_root: Benchmark superiority asserted without matched-pair comparison | papers: [Kumada_1972, Monnereau_2009, Molander_2016, Morken_2016] | member_items: [Kumada_1972 SRG-6 (C-1, C-2, A-4) | Monnereau_2009 SRG-7 (B-3, B-4, C-10) | Molander_2016 (C-1, C-2) | Morken_2016 (C-1 through C-7)] | note: Every paper positions against named prior art without matched-substrate, matched-condition numerical comparison. The closest structural analog to the new method consistently receives the same cite-and-contrast treatment as more distant references (Monnereau ↔ ref [19]; Morken ↔ Jarvo refs 9a–9d). Field-wide convention.

recurring_root: Imported mechanism without isomorphism demonstration | papers: [all four] | member_items: see RP-5 evidence chain | note: Each paper imports its mechanistic framework from a non-isomorphous source — stoichiometric → catalytic (Kumada), Pd → Ni (Monnereau), one solvent / one substrate → nine solvents / nine substrate classes (Molander), generic Ni manifold + organic SN2 → PyBox-Ni cyclic-sulfate (Morken). The pattern is not specific to any one mechanism type.

---

**Temporal trajectory of recurring patterns**

temporal_trajectory: RP-1 (mechanism validation) | classification: shifting | transition_point: ~2014–2016 (radical/photoredox era + computational availability) | note: 1972: 2-electron Ni(0)/Ni(II) cycle by analogy to stoichiometric (dipy)Ni — structurally suppressed (no in situ NMR, no EPR, no DFT). 2009: same paradigm, even less mechanistic evidence (single ³¹P shift for "active species[REDACTED: substantial verbatim quotation; see Tier 9]no tools" → [REDACTED: substantial verbatim quotation; see Tier 9]

temporal_trajectory: RP-2 (analytical underreporting) | classification: time-invariant | transition_point: n/a | note: Persistent across 1972 (no glpc conditions; mixed yield basis), 2009 (no isolated yields; below-threshold crystallographic GoF unmentioned), 2016 Molander (no yield type, no mass balance, outliers unattributed), 2016 Morken (no SFC column identity; no SD on duplicates). The pattern is invariant in character despite radical changes in measurement technology. Stage 4 implication: Tier 1 evaluators consistently flag this in modern era while authors continue to follow communication-era norms.

temporal_trajectory: RP-3 (self-contradictory absence) | classification: time-invariant | transition_point: n/a | note: Specific predictions vary (R–R in 1972; activation-product Ni state in 2009; B1/A1 ΔΔG‡ in 2016 Molander; reductive-elimination stereochemistry assumption in 2016 Morken). Structural pattern — model predicts → prediction not tested — is invariant.

temporal_trajectory: RP-4 (benchmark superiority asserted) | classification: time-invariant | transition_point: n/a | note: Tamura-Kochi citation pattern (1972) is structurally identical to Jarvo citation pattern (2016) — closest analog dismissed without matched comparison. Field-wide stable feature.

temporal_trajectory: RP-5 (imported model) | classification: shifting | transition_point: ~2009 (computational chemistry as transferable mechanism source) | note: 1972: imported from stoichiometric organometallic literature. 2009: imported from Pd diphosphine literature. 2016: imported from prior DFT computation on different substrate / different solvent (Molander) or from organic substitution chemistry without metal-context DFT (Morken). The "source" of imported mechanism shifts from precedent-experimental to precedent-computational, but the absent isomorphism demonstration is invariant.

temporal_trajectory: RP-6 (scope failures undiagnosed) | classification: time-invariant | transition_point: n/a | note: 1972 sp³ exclusion → 2009 bromomesitylene outlier → 2016 amine-silicate alkenylation "performed poorly" → 2016 quaternary-center "ineffective." Persistent feature across all eras.

---

**Structural suppression vs. individual choice**

RP-1 (mechanism validation):
- *Era-dependent*: structurally suppressed (1972, 2009: limited in situ/computational tools) → individually chosen (2016: tools available — initial-rate measurements, Hammett, EPR, radical clocks at multiple rates, DFT solvation testing, stoichiometric intermediate isolation — but not deployed to the depth required by the load-bearing mechanistic claim in either Molander or Morken). The 2016 Molander DFT case is particularly clear: ⟨S²⟩ values, ZPE, solvation sensitivity tests are computationally trivial additions if the mechanism is the central claim.

RP-2 (analytical underreporting):
- *Incentive-suppressed*: No journal among JACS Communications (1972, 2016 Morken), Adv. Synth. Catal. (2009), or Acc. Chem. Res. (2016 Molander) requires replicate data, response-factor calibration, SFC column identity in main text, or mass balance for radical-process scope tables. Adding this information would not constitute an independent contribution; reviewers do not reject for its absence in scope tables.

RP-3 (self-contradictory absence):
- *Individually chosen*: Every untested prediction is testable with the paper's own infrastructure. R–R quantification (1972) requires only one glpc run with an authentic standard. Activation-product oxidation state (2009) requires UV-vis + ³¹P integration. ΔΔG‡ for L1 system (Molander 2016) requires one additional DFT computation. Reductive-elimination retention (Morken 2016) requires one stoichiometric experiment. The cost is small; the choice is to not do the experiment.

RP-4 (benchmark superiority asserted):
- *Incentive-suppressed*: Matched-pair comparison risks demonstrating that the new method is not superior on the specific shared substrate, even if it offers other advantages (scope, conditions, enantiocontrol). The incentive structure of methodology-paper publishing rewards scope demonstration over head-to-head comparison.

RP-5 (imported model):
- *Era-dependent*: structurally suppressed (1972: stoichiometric analogy was the only available source) → mixed in 2009 (Pd analogies easy to invoke; quantitative DFT/Ni benchmarks emerging but not yet routine) → individually chosen (2016: solvent-corrected DFT, substrate-class-specific PES, cycle-level isomorphism tests are feasible).

RP-6 (scope failures undiagnosed):
- *Individually chosen partial / format-suppressed partial*: Diagnosing failure modes (steric vs. electronic vs. background-pathway competition) requires additional experiments within each paper's capability but absent. Communication formats (1972, Morken 2016) compress failure analysis structurally; Account (Molander) and full paper (Monnereau) formats do not have this excuse but exhibit the same pattern.

---

**Paradigm competition vs. coexistence**

This group reveals **three coexisting methodological paradigms** rather than competitive succession:

**Paradigm 1: Ligand design within the 2-electron Ni(0)/Ni(II) Kumada manifold (1972, 2009)**
Both Kumada 1972 and Monnereau 2009 use Grignard reagents + sp² halides under a Ni-phosphine catalyst; expansion axis is ligand architecture (dpe → calix[4]arene-diphosphine). The two papers share the manifold and differ in ligand sophistication.

Systematically unanswered question:
- What structural and electronic features of the diphosphine ligand quantitatively determine the rate-limiting step and overall TOF?
  evidence_chain: [Kumada_1972 : B-3 → ligand activity order n-BuMgBr/PhCl, no yields per ligand; Monnereau_2009 : U-2 → bite-angle-dynamics claim without rate law; B-3 → dppp comparison restricted to one loading]

**Paradigm 2: Single-electron / photoredox manifold (Molander 2016)**
Fundamentally different activation mode: SET oxidation of alkyl trifluoroborate or alkylsilicate generates carbon radical that enters NiI/NiIII manifold. No Grignard; no two-electron transmetalation. Substrate identity (Csp³) and selectivity hierarchy are inverted from the classical Kumada.

Systematically unanswered question:
- Which species (organoboron substrate or Ni complex) intercepts the excited photocatalyst first, and are NiI/NiIII intermediates spectroscopically detectable under turnover?
  evidence_chain: [Molander_2016 : U-1 → no Stern–Volmer; U-2 → spin-manifold consistency for cross-pathway ΔG comparison; "no textual basis in Kumada_1972 or Monnereau_2009 or Morken_2016" — the question does not arise in 2-electron paradigms]

**Paradigm 3: Enantioselective desymmetrization within 2-electron Kumada (Morken 2016)**
Combines 2-electron SN2-like oxidative addition with chiral PyBox ligand on Ni(II) to achieve enantiocontrol. New selectivity axis (er) added to the Kumada manifold rather than a new activation mode.

Systematically unanswered question:
- Is enantioselectivity kinetically or thermodynamically controlled, at which elementary step is stereochemical information set, and is the active transmetalating species ArMgBr or Ar₂Mg?
  evidence_chain: [Morken_2016 : U-2 → kinetic vs. thermodynamic control untested; B-9 → axial reactive-conformation argument non-unique; U-4 + CLA-2 → ArMgBr vs. Ar₂Mg unidentified]

**Coexistence not succession:** The three paradigms share the 1972 origin but expand along independent axes (ligand architecture, activation mode, selectivity dimension). Crucially, all three share the same blind spot — RP-1 (mechanism validation absent for the cycle and intermediates as drawn) — regardless of paradigm, format, or era. Whether the cycle is 2-electron Ni(0)/Ni(II), photoredox NiI/NiIII, or asymmetric Ni-PyBox, the elementary-step characterization gap persists. This structural invariance is the strongest evidence that RP-1 is a **field-wide convention** rather than a paradigm-specific limitation.

---

**Divergences**

**DV-1: Nucleophile / activation mode defines the paradigm**
Kumada 1972 / Monnereau 2009 / Morken 2016: 2-electron Grignard. Molander 2016: 1-electron radical from organoboron / silicate via SET. The nucleophile choice fully determines the mechanistic manifold, the controlling steric/electronic factors, and the relevant probe experiments.

evidence_chain: [Kumada_1972 : S0-4 → PhMgBr / sp² halide | Monnereau_2009 : S0-4 → PhMgBr / ArBr or ArCl | Molander_2016 : S0-4 → organotrifluoroborate or alkylsilicate / aryl bromide via SET | Morken_2016 : S0-4 → ArMgBr / cyclic sulfate]

**DV-2: Metric of success diverges**
Kumada 1972: yield + scope breadth. Monnereau 2009: TOF (kinetic). Molander 2016: paradigm framing + scope breadth across nine sections. Morken 2016: er (enantioselectivity). Each paper defines success by a different primary metric, which structurally precludes cross-paper quantitative comparison even within the group.

evidence_chain: [Kumada_1972 : D-1 success_criteria → isolated/glpc yields | Monnereau_2009 : D-1 success_criteria → TOF | Molander_2016 : D-1 success_criteria → paradigm + scope | Morken_2016 : D-1 success_criteria → er]

**DV-3: Format constrains evidentiary depth — but not the mechanism gap**
JACS Communication (1972, Morken) vs. Adv. Synth. Catal. full paper (Monnereau) vs. Acc. Chem. Res. Account (Molander). Despite a 4-fold range in page budget (3 pp → 11 pp), all four papers exhibit the same RP-1 / RP-2 / RP-3 patterns. The Account format (Molander) is uniquely permissive of data absence because it is retrospective; the Communication format compresses by truncation; the full paper format absorbs but does not eliminate. Format is necessary but not sufficient to explain the recurring patterns.

evidence_chain: [Kumada_1972 : D-3 → 3 pp Communication | Monnereau_2009 : D-3 → 7 pp full paper | Molander_2016 : D-3 → 11 pp Account | Morken_2016 : D-3 → 4 pp Communication]

**DV-4: Mechanism source divergence (subtype of RP-5)**
Kumada imports stoichiometric organometallic precedent. Monnereau imports Pd-based bite-angle precedent. Molander imports a prior DFT PES with mismatched solvation and substrate. Morken imports general Ni manifold + organic SN2 geometry. The source of imported mechanism diverges, but the absent isomorphism demonstration is invariant.

evidence_chain: [see RP-5 evidence chain]

---

**U-item patterns**

recurring_U: Self-contradictory absence involving catalytic-cycle predictions | papers: [all four] | item_ids: [Kumada_1972: U-1, U-2 | Monnereau_2009: U-1, U-2, U-3, U-5 | Molander_2016: U-1, U-2, U-3, U-4, U-5, U-6 | Morken_2016: U-1, U-2, U-4] | note: U items constitute the single largest category of recurring gaps. Their accumulation across paradigms, formats, and eras suggests the A/B/C classification framework captures individual paper omissions well but does not naturally capture the recursive pattern of "model predicts observable → observable not tested" that is endemic to Ni cross-coupling mechanism sections. The v18.4 prompt's explicit U-item rubric (as compared with earlier versions) appears to be detecting the pattern reliably across all four papers.

recurring_U: Prerequisite-absence for primary evidentiary claim | papers: [Monnereau_2009, Molander_2016, Morken_2016] | item_ids: [Monnereau_2009: U-1 (active species identity), U-2 (kinetic evidence for bite-angle dynamics) | Molander_2016: U-1 (DFT validation), U-2 (spin-manifold consistency), U-7 (PES scope generalization) | Morken_2016: U-1 (cycle elements unobserved), U-3 (SFC method undocumented)] | note: Distinct from self-contradictory absence — these record gaps where a load-bearing prerequisite for the central claim is asserted rather than established. Absent in Kumada 1972 (no comparable single load-bearing claim by 1972 standards); emergent from 2009 onward as the field's claim sophistication outpaces the evidentiary infrastructure deployed.

---

**Self-contradictory absence patterns**

self_contradictory: [Kumada_1972] : catalytic cycle eq 3 → R–R predicted → unreported | item_id: U-1
self_contradictory: [Kumada_1972] : homogeneous Ni(II) cycle → black mixture observed but not characterized | item_id: U-2
self_contradictory: [Monnereau_2009] : standard Kumada cycle → activation product (δ ³¹P 41.8 ppm) Ni oxidation state unconfirmed | item_id: U-1
self_contradictory: [Monnereau_2009] : bite-angle-dynamics model → rigid-analogue control needed (acknowledged as deferred) and not performed | item_id: U-3
self_contradictory: [Monnereau_2009] : abstract claims "high activities with congested bromoarenes" → bromomesitylene gives 780 h⁻¹ (lowest) outlier suppressed | item_id: A-3 (Stage 1)
self_contradictory: [Molander_2016] : Figure 9 PES B1>A1 by ~6 kcal/mol → no solvation sensitivity / ⟨S²⟩ / ZPE / spin-manifold consistency reported | item_id: U-1, U-2
self_contradictory: [Molander_2016] : DKR predicts ee from ΔΔG‡ → founding eq 2 datum (75:25 er, L1) never computed within DKR | item_id: U-5
self_contradictory: [Molander_2016] : cycle predicts NiI and NiIII intermediates → neither observed by EPR / UV-Vis | item_id: U-2
self_contradictory: [Molander_2016] : HAT mechanism predicts rate competition (k_HAT vs. k_add) → never measured | item_id: U-6
self_contradictory: [Molander_2016] : single-system PES (benzylic / PhBr) → applied to nine substrate classes without re-computation | item_id: U-7
self_contradictory: [Morken_2016] : non-radical SN2-like cycle → cyclopropylcarbinyl clock cannot discriminate Ni(0)/Ni(II) from Ni(I)/Ni(III) | item_id: U-1, B-5
self_contradictory: [Morken_2016] : 90% ds → reductive-elimination retention assumed → assumption never tested | item_id: U-1, B-6
self_contradictory: [Morken_2016] : cycle drawn with ArMgBr transmetalating → aging-protocol narrative implies Ar₂Mg dominant | item_id: CLA-2
self_contradictory: [Morken_2016] : design feature (b) predicts bis-coupling suppression → mass balance never reported | item_id: B-12, B-1

**Recurring pattern assessment:** Self-contradictory absence is the most densely recurring pattern across this group, appearing in every paper regardless of mechanism type, era, or format. The pattern reflects a **narrative function of mechanism diagrams**: cycles, schemes, and PES plots in Ni cross-coupling papers organize synthetic results rather than generate and test predictions. This is simultaneously a **genre convention** (expected by editors and reviewers) and a **genuine analytical gap** (each prediction is individually testable). The convention persists because testing predictions either confirms them (unpublishable) or falsifies them (requiring a different paper), preserving the gap.

---

**Group-level unasked question**

[REDACTED: substantial verbatim quotation; see Tier 9]

evidence_chain: [Kumada_1972 : A-2 (cycle from analogy, mechanism deferred), U-2 (heterogeneous Ni⁰ ambiguity uncharacterized) | Monnereau_2009 : U-1 (activation-product oxidation state unknown), U-2 (bite-angle-dynamics claim without rate law, Hammett, or rigid-analogue control), U-4 (Ni(I)/Ni(III) not excluded) | Molander_2016 : U-1+U-2 (DFT PES not solvation- or spin-validated), U-7 (PES not generalized to 9 substrate classes), U-4 (DKR not experimentally tested by VT-ee or radical clock) | Morken_2016 : U-1 (no intermediate observed; cycle elements asserted), B-5 (radical clock cannot discriminate Ni manifolds), B-6 (RE retention assumption untested)]

TEMPERATURE_SUMMARY correspondence: The group-level question maps to the strongest convergence items in three of four papers — Monnereau U-1/U-2 (3/3 high), Molander B-5/U-1 cluster (3/3 high), Morken B-5/B-6 (3/3 high). In Kumada 1972, the analogous items reach 2/3 high with V1=high/V2=high, the maximum convergence achievable in the era's evidentiary registry. In every paper, the convergence concentrates exactly on the gap between mechanistic claim and experimental support.

recurring_root correspondence: The group-level question subsumes all four recurring roots — cycle/intermediate validation, analytical underreporting, benchmark superiority, imported model isomorphism — as facets of a single problem: **the field has no agreed standard for what constitutes sufficient mechanistic evidence in Ni-catalyzed cross-coupling**. Each paper proposes a mechanism at a different level of certainty (1972: "working hypothesis"; 2009: "likely to rely on"; 2016 Molander: "established" / "predominates"; 2016 Morken: "presumably by an SN2-like reaction path"), but the evidentiary standard for each level is nowhere defined or enforced. Stage 4 implication: the v18.4 corpus reveals this as a structural convention, not a paper-by-paper failing. A successor methodology (e.g., UQS-derived mechanistic-evidence checklist by paradigm) is the natural Phase 2 deliverable from this G3 observation.

Cross-reference to Stage 3 §6 (institutional design): All four Stage 3 outputs independently nominate the same patterns for codification — Labeling mismatch (factual verbs in mechanism sections that are explicitly hypothetical), RI-06 cycle-level/geometry-level import, RI-04 + RI-06 co-occurrence, PRI-11 (mechanism-kinetics decoupling), and the new PRI-12 candidate (Self-reinforcing computational loop, Molander 2016). The convergent codification candidates across four independently analyzed papers strengthen the case for promotion.

---

*End of G3 output.*

---

> **Tier 8 redaction notice**: This file is a redacted copy of the corresponding Tier 3 / Tier 9 output. Verbatim source-paper quotations have been replaced by `[REDACTED: see source paper §<loc>; full text retained in Tier 9 reviewer-only deposit]` markers, preserving location references and our own analytical content. Bibliographic fields (title, authors, journal, year, DOI), analytical labels (`evidence_chain:` with B-/U-/A-/C- internal IDs), short technical terms, and our own analytical text are not redacted. The redaction was applied by `scripts/redact_for_tier8.py` and, for this version, by `scripts/build_paperA_R1_public.py` with `scripts/redact_source_ngram_runs.py` (scripts of the project repository; they are not deposited).
