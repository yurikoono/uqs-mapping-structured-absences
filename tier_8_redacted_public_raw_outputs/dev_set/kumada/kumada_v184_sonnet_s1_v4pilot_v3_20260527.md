prompt_version: stage1-v184-20260527_v4pilot_v3
model_info: claude-sonnet-4-6
executed_date: 2026-05-27
paper: Kumada / Tamao 1972, JACS — Ni-catalyzed cross-coupling of Grignard reagents
year: 1972
delta_t: ~54y
status: PILOT — Cross-corpus G7 test (organometallic vs biochemistry)

---

[V4 (PILOT v3): Naive textbook reader]
field: Naive textbook reader — Crabtree "The Organometallic Chemistry of the Transition Metals" (7th ed., 2022) + Hartwig "Organotransition Metal Chemistry" (2010), particularly cross-coupling catalysis chapters — without field-internal licenses
field_rationale: V1 (synthetic/analytical), V2 (mechanistic/kinetic), and V3 (analytical chemistry/chromatography) all operate with field-internal licenses — they know that a 1972 communication is not expected to report oxidative addition rate constants, or that "black precipitate" in Ni catalysis is a recognized phenomenon. V4 uniquely asks: what does the textbook *present as established canonical knowledge* that the paper simply omits, mis-describes, or leaves as an open question in a way that a reader equipped only with textbook knowledge would find jarring?

textbook_corpus_used:
  - Crabtree, "The Organometallic Chemistry of the Transition Metals," 7th ed. (2022), Chapter 9 (C–C coupling reactions): oxidative addition/reductive elimination canonical cycle, Ni(0)/Ni(II) catalytic mechanism, ligand bite-angle and selectivity effects, cis-requirement for reductive elimination
  - Crabtree Ch. 6 (Oxidative addition and reductive elimination): canonical Ni(0) oxidative addition of aryl/vinyl C–X bonds, concerted vs. radical pathways, steric/electronic factors in reductive elimination
  - Crabtree Ch. 4 (Ligand substitution in 16- and 18-electron complexes): square-planar Ni(II) coordination geometry, trans influence, chelation effects
  - Hartwig, "Organotransition Metal Chemistry" (2010), Chapter 18 (Cross-coupling reactions): Kumada coupling mechanism, Pd vs. Ni comparison, oxidative addition of C–Cl bonds, transmetalation with Grignard reagents, β-hydride elimination competing pathway
  - Hartwig Ch. 7 (Oxidative addition to form M(II) from M(0)): activation energy barriers, electronic effects on rate, Ni vs. Pd selectivity

---

--- New questions ---

V4-Q1
loc: P2:Lcol:18* (equations 2–4)
quote: [REDACTED: see `loc:` above; full text in Tier 9]
textbook_reference: Crabtree Ch. 9, "Kumada Coupling" section; Hartwig Ch. 18 §18.1: "The catalytic cycle for Kumada coupling begins with a Ni(0) species formed in situ by reduction of the Ni(II) precatalyst... The active catalyst is Ni(0)L₂, not Ni(II)Cl₂."
gap_type: G1 (Mid-step gap)
question: The textbook presents a canonical Ni(0)/Ni(II) catalytic cycle that begins with a Ni(0) species performing oxidative addition to the aryl/vinyl halide. Equation 2 in the paper, however, describes the *precatalyst* NiCl₂L₂ reacting directly with two equivalents of Grignard reagent to form a Ni(II)R₂ intermediate — skipping the reduction step that would convert Ni(II) to the active Ni(0) catalyst. According to the textbook, step A between "Ni(II)Cl₂ precatalyst" and "active Ni(0) catalyst" is reductive elimination of R–R from NiR₂L₂ to give Ni(0)L₂. The paper's proposed cycle begins at step B (Ni(II)R₂ formed), but the textbook canonical cycle begins with the Ni(0) state. Where in the paper's mechanism does the Ni(0) active catalyst appear, and is the paper proposing a Ni(II)/Ni(II) or a Ni(0)/Ni(II) cycle?
differentiation: V1 and V2 note the mechanistic uncertainty, but neither asks the textbook-grounded question of which oxidation state is the active catalyst — V4 asks this from the canonical textbook presentation where Ni(0) is unambiguously the active species, a presentation that postdates the 1972 paper.
severity: high
inference_tier: T1

---

V4-Q2
loc: P2:Lcol:5* (equation 1 and surrounding text)
quote: [REDACTED: see `loc:` above; full text in Tier 9]
textbook_reference: Crabtree Ch. 6 §6.2, "Reductive elimination": [REDACTED: substantial verbatim quotation; see Tier 9]
gap_type: G1 (Mid-step gap)
question: The textbook presents reductive elimination as proceeding through a concerted 3-centered transition state requiring both R groups to be cis. The paper's equation 1 and the derived catalytic cycle show [REDACTED: substantial verbatim quotation; see Tier 9] — but this is not a standard reductive elimination. In textbook terms, reductive elimination from NiR₂L₂ would give R–R + Ni(0)L₂ *spontaneously*, without needing "the action of an organic halide." The paper seems to conflate the initiation step (eq 2 → eq 3) with reductive elimination. Does the paper's "release by the action of an organic halide" (eq 3) describe (a) oxidative addition of R'X'' to Ni(II)R₂ to give Ni(IV), followed by reductive elimination, or (b) an associative substitution, or (c) something else? The textbook reader cannot tell from the paper alone.
differentiation: V2-Q3 addresses this mechanistic ambiguity from an expert mechanistic viewpoint; V4 asks it from the textbook-reader perspective where reductive elimination is defined as spontaneous (no halide required) — the paper's formulation contradicts the textbook canonical presentation.
severity: high
inference_tier: T1

---

V4-Q3
loc: P3:Lcol:8* (feature 3, ligand activity order)
quote: [REDACTED: see `loc:` above; full text in Tier 9]
textbook_reference: Crabtree Ch. 6 §6.3, "Reductive elimination": [REDACTED: substantial verbatim quotation; see Tier 9] Hartwig Ch. 7 §7.4: bite angle effects on reductive elimination rates from Ni(II) complexes.
gap_type: G2 (Unconditional generalization)
question: The textbook states that cis geometry is necessary for reductive elimination, AND that the bite angle of the bidentate phosphine controls the rate — not just whether the cis geometry is enforced, but how efficiently. The paper's ordering [NiCl₂(dpp)] > [NiCl₂(dpe)] > [NiCl₂(dmpe)] ≈ [NiCl₂(PPh₃)₂] is presented as evidence that "cis configuration is the first requisite," but the textbook shows that once cis geometry is enforced, bite angle (and σ-donor / π-acceptor properties) further tune the rate. The paper's conclusion (cis geometry = first requisite) is correct as far as it goes, but the textbook reader expects the *second* requisite — optimal bite angle — to be addressed. Does the observed dpp > dpe > dmpe order reflect bite angle optimization, backbone rigidity, or σ-donor capacity differences, conditions that the textbook treats as independently important?
differentiation: V2-Q8 asks about cis geometry vs. electronic factors from expert mechanistic perspective; V4 asks from the textbook presentation that separates cis-requirement and bite-angle effects into distinct canonical factors, neither of which the paper disentangles.
severity: medium
inference_tier: T1

---

V4-Q4
loc: P1:Rcol:13* (introduction, prior cross-coupling context)
quote: [REDACTED: see `loc:` above; full text in Tier 9]
textbook_reference: Hartwig Ch. 18 §18.1: [REDACTED: substantial verbatim quotation; see Tier 9]
gap_type: G4 (Multiple-mechanism collapse, Many→One direction)
question: The textbook presents two mechanistically distinct reasons why earlier transition-metal-catalyzed Grignard couplings gave homo-coupling: (a) radical-chain mechanisms operative with Fe/Cu/Ag "soluble catalysts,[REDACTED: substantial verbatim quotation; see Tier 9]selective cross-coupling" result without specifying whether it operates by suppressing radical chains, controlling the Ni(II)/Ni(0) cycle, or both. Does the dpe ligand suppress homo-coupling by preventing radical pathways, by accelerating the transmetalation→reductive elimination sequence over the Ni(II)R₂ homo-coupling pathway, or both?
differentiation: V1-Q14 and V2-Q6 address selectivity from synthetic and mechanistic angles; V4 asks from the textbook canonical presentation that delineates two *distinct mechanistic origins* of homo-coupling which the paper collapses into one undifferentiated narrative.
severity: medium
inference_tier: T1

---

V4-Q5
loc: P2:Lcol:1* (equation 3)
quote: [REDACTED: see `loc:` above; full text in Tier 9]
textbook_reference: Hartwig Ch. 18 §18.1; Crabtree Ch. 9: [REDACTED: substantial verbatim quotation; see Tier 9] The textbook cycle is: Ni(0) → [oxidative addition] → Ni(II)(Ar)(X) → [transmetalation] → Ni(II)(Ar)(R) → [reductive elimination] → product + Ni(0).
gap_type: G7 (Resolved-to-black-box gap; Δt ≈ 54y)
question: The textbook presents a canonical Ni(0)/Ni(II) cycle in which the active species performing oxidative addition is Ni(0)L₂. The paper's equation 3 describes a reaction in which the *diorgano-Ni(II)* complex 1 (NiR₂L₂) is converted by the organic halide R'X'' to give the haloorgano-Ni(II) complex 2 and homo-coupling product R–R. In the textbook canonical cycle, this corresponds to eq 3 being an *oxidative addition of R'X'' to Ni(II)R₂ generating Ni(IV)R₂(R')(X'')*, followed by reductive elimination of R–R from Ni(IV) — a Ni(II)/Ni(IV) step that was later resolved to be mechanistically distinct from the mainstream Ni(0)/Ni(II) cycle. In 1972, the paper describes this step with the vague label "[REDACTED: verbatim source text; see the source paper via its DOI]" without specifying the oxidation state pathway. The textbook now presents the resolved Ni(0)/Ni(II) cycle as canonical, having post-dated the clarification of whether Ni(II)/Ni(IV) or Ni(0)/Ni(II) is operative. This is a historically appropriate vague description at T₀ (1972) that the textbook has since resolved — a G7 gap.
differentiation: V1/V2/V3 none flag this as a *historically necessary vagueness* that the field subsequently resolved into the canonical Ni(0)/Ni(II) cycle; V4 uniquely identifies this as a G7 gap anchored to the textbook's resolved mechanism vs. the paper's contemporaneously appropriate black-box description.
severity: high
inference_tier: T2
note: G7 Δt = 54y (1972 paper vs. 2022 Crabtree textbook). The textbook presents the Ni(0)/Ni(II) oxidative addition–transmetalation–reductive elimination cycle as the resolved canonical mechanism. The 1972 paper's "initiation" step via eq 2 (Ni(II)Cl₂ + 2 RMgX → Ni(II)R₂) and the propagation via eq 3 (Ni(II)R₂ + R'X'' → Ni(II)(R')(X'') + R–R) are historically appropriate at T₀; the resolution to Ni(0)/Ni(II) came with subsequent mechanistic studies (Kumada group, 1974–1980; later reviews).
textbook_anchor: anticipates_canonical — the paper introduces the concept of a Ni-catalyzed cross-coupling cycle, which the field subsequently resolved and formalized as the Ni(0)/Ni(II) canonical mechanism now presented in Crabtree Ch. 9.

---

V4-Q6
loc: P3:Lcol:18* (feature 4)
quote: [REDACTED: see `loc:` above; full text in Tier 9]
textbook_reference: Crabtree Ch. 6 §6.2 and Ch. 9: [REDACTED: substantial verbatim quotation; see Tier 9]
gap_type: G7 (Resolved-to-black-box gap; Δt ≈ 54y)
question: The textbook presents vinyl-halide cross-coupling as proceeding with *stereochemical retention* via concerted oxidative addition to Ni(0), with loss of stereochemical fidelity diagnosed as either a radical mechanism or a π-allyl Ni intermediate. The paper describes the cis:trans = 80:20 and 43:57 product ratios as "anomalous[REDACTED: substantial verbatim quotation; see Tier 9]anomalous" without resolution; the textbook has since resolved the diagnostic meaning. This is a G7 gap — historically appropriate T₀ vagueness, textbook-resolved at T₀+54y.
differentiation: V1-Q7 and V2-Q4/Q5 address the stereochemical question from synthetic/mechanistic expertise; V4 uniquely identifies the "anomalous" label as a G7 black-box term whose resolution (radical vs. concerted mechanism diagnostic) appears in the textbook but not in the 1972 paper.
severity: high
inference_tier: T2
note: G7 Δt = 54y. The resolution of the stereochemical scrambling mechanism (now textbook-canonical: non-retention = diagnostic for radical or σ/π Ni interconversion pathways) postdates the paper. The paper's "anomalous" language is an appropriate T₀ placeholder.

---

V4-Q7
loc: P3:Lcol:12* (feature 3, ligand identity: dpe)
quote: [REDACTED: see `loc:` above; full text in Tier 9]
textbook_reference: Crabtree Ch. 9 §9.4: [REDACTED: substantial verbatim quotation; see Tier 9]
gap_type: G7 (Resolved-to-black-box gap; Δt ≈ 54y)
question: The paper introduces dpe [1,2-bis(diphenylphosphino)ethane] as the most useful bidentate ligand and notes the activity order (dpp > dpe > dmpe), interpreted solely as reflecting cis-geometry enforcement. The textbook now presents bite angle as a quantitatively understood parameter that controls reductive elimination rate independently of the cis-geometry effect. In 1972, the bite angle concept as a synthetic design parameter did not exist in quantitative form — the paper appropriately uses qualitative cis-geometry language as a contemporary black-box description. The textbook presents the resolved canonical understanding: dpe's ~85° bite angle optimizes the reductive elimination rate in the Ni(0)/Ni(II) cycle. This textbook entry anticipates and resolves the qualitative ligand-effect discussion in the 1972 paper — a G7 gap at Δt = 54y.
differentiation: V2-Q8 asks about bite angle vs. cone angle from expert mechanistic perspective; V4 identifies the *absence of bite angle as a concept* in the 1972 paper as a G7 gap — the paper uses a concept (cis geometry) that the textbook has since superseded with a more precise quantitative descriptor (bite angle).
severity: medium
inference_tier: T2
note: G7 Δt = 54y. The bite angle concept as a quantitative predictive tool for cross-coupling was developed in the 1980s–2000s. The 1972 paper appropriately uses qualitative cis-geometry language; the textbook presents the resolved form.
textbook_anchor: anticipates_canonical — the paper introduces dpe as the superior bidentate ligand, which the field subsequently quantified and formalized as the "bite angle effect" now presented in Crabtree Ch. 9.

---

V4-Q8
loc: P1:Rcol:1* (introduction, Grignard coupling context)
quote: [REDACTED: see `loc:` above; full text in Tier 9]
textbook_reference: Hartwig Ch. 18 §18.1: [REDACTED: substantial verbatim quotation; see Tier 9]
gap_type: G7 (Resolved-to-black-box gap; Δt ≈ 54y)
question: The paper presents the Ni-catalyzed Grignard coupling as an isolated synthetic method motivated by "two independent facts concerning σ-organonickel complexes." There is no recognition that this paper is initiating a general paradigm. The textbook presents Kumada coupling as the *founding example* of the OA–TM–RE cycle that underlies all cross-coupling chemistry. The paper's framing as "a new preparative method" without recognizing the paradigmatic generality is historically appropriate (1972: Pd-catalyzed Heck reaction was only beginning; Suzuki, Negishi not yet discovered). The textbook resolution presents the paper as foundational to a unified mechanistic framework. This is a G7 gap: the paper appropriately frames its scope narrowly at T₀; the textbook has resolved the broader paradigmatic significance at T₀+54y.
differentiation: No V1/V2/V3 question addresses this framing gap, because all three operate from field-internal knowledge that already knows the retrospective significance; V4 uniquely asks why the textbook's canonical "first example of OA–TM–RE cross-coupling" label is absent from the paper itself.
severity: medium
inference_tier: T2
note: G7 Δt = 54y. The paradigmatic significance of the Kumada reaction as the prototype OA–TM–RE cycle was recognized retrospectively, primarily in the 1980s–1990s with the development of the Suzuki, Negishi, and Stille reactions.
textbook_anchor: anticipates_canonical — the paper introduces the catalytic cycle concept (eqs 2–4) that the field subsequently generalized and formalized as the OA–TM–RE cross-coupling paradigm.

---

V4-Q9
loc: P3:Lcol:1* (feature 1)
quote: [REDACTED: see `loc:` above; full text in Tier 9]
textbook_reference: Hartwig Ch. 18 §18.3: [REDACTED: substantial verbatim quotation; see Tier 9]
gap_type: G2 (Unconditional generalization)
question: The textbook presents suppression of β-hydride elimination in Kumada coupling as requiring a *kinetic condition*: transmetalation must be faster than β-hydride elimination. The paper states that [REDACTED: substantial verbatim quotation; see Tier 9] as an unconditional feature, without specifying the kinetic conditions (temperature, Grignard concentration, substrate) under which transmetalation outcompetes β-hydride elimination. The textbook reader expects to see: (a) under what conditions does the transmetalation vs. β-hydride elimination competition favor cross-coupling? and (b) are these the conditions of Table I (Et₂O, reflux, 0.1–1.0 mol% Ni catalyst)? The claim that β-H-containing Grignard reagents give "high yields" is stated without specifying the operating conditions under which this holds.
differentiation: V1-Q9 asks about quantification of β-hydride elimination byproducts; V4 asks from the textbook canonical picture that frames β-H suppression as a kinetic competition requiring specification of which conditions favor productive coupling — an unconditional-generalization gap not visible from the synthetic perspective.
severity: medium
inference_tier: T1

---

V4-Q10
loc: P3:Lcol:6* (feature 2)
quote: [REDACTED: see `loc:` above; full text in Tier 9]
textbook_reference: Crabtree Ch. 6 §6.1: [REDACTED: substantial verbatim quotation; see Tier 9]
gap_type: G1 (Mid-step gap)
question: The textbook explains *why* sp³ C–X bonds are inactive in Ni-catalyzed cross-coupling: alkyl C–X bonds lack the π-system that stabilizes the oxidative addition transition state. The paper presents "only sp² halides can be used" as a feature, but without any explanation of why. A textbook reader equipped with the canonical oxidative addition reactivity order (aryl > vinyl > alkyl) and its mechanistic basis (π-system stabilization of OA transition state) expects the paper to provide either this explanation or a reference to it. The textbook reader sees step B missing between "sp³ C–X not reactive" (C) and "sp² C–X selective" (A): the missing step B is the mechanistic explanation (OA barrier for alkyl C–X too high under these conditions).
differentiation: V1-Q4 asks about experimental validation of the sp³ exclusion; V4 asks from the textbook reader's perspective why the mechanistic explanation for sp² selectivity (OA barrier difference) is absent — a mid-step gap in the conceptual scaffolding.
severity: low
inference_tier: T1

---

V4-Q11
loc: P2:Lcol:18* (equations 2–4, transmetalation step eq 4)
quote: [REDACTED: see `loc:` above; full text in Tier 9]
textbook_reference: Hartwig Ch. 18 §18.2: [REDACTED: substantial verbatim quotation; see Tier 9]
gap_type: G1 (Mid-step gap)
question: The textbook presents a specific mechanistic picture for transmetalation in Kumada coupling: a four-membered cyclic transition state involving the Mg–X and Ni–R' bonds. The paper's equation 4 represents transmetalation as a simple ligand exchange ("RMgX'") with no mechanistic detail. A textbook reader trained on Hartwig Ch. 18 expects to see, even briefly, the driving force for transmetalation (MgX₂ formation, hard-hard interaction) and the mechanistic difference from other cross-coupling reactions. The paper skips from precatalyst (Ni(II)Cl₂) to the transmetalation step without any mechanistic discussion of why Grignard reagents are effective transmetalating agents for Ni(II) complexes under the reported conditions.
differentiation: V2-Q1 asks about rate-determining step from a kinetic/mechanistic expert perspective; V4 asks why the textbook-canonical mechanistic explanation for Grignard transmetalation (4-membered cyclic TS, MgX₂ driving force) is absent — a mid-step gap in conceptual scaffolding that the textbook reader would notice.
severity: low
inference_tier: T2

---

V4-Q12
loc: P2:Rcol:1* (Table I header and footnotes)
quote: [REDACTED: see `loc:` above; full text in Tier 9]
textbook_reference: Crabtree Ch. 9; Hartwig Ch. 18: [REDACTED: substantial verbatim quotation; see Tier 9]
gap_type: G5 (Loose definition)
question: The textbook presents catalyst loading in cross-coupling as reported in mol% relative to substrate, a standardized unit enabling comparison across reactions. The paper reports catalyst loading as a ratio [NiCl₂(dpe)]/organic halide = 10⁻²–10⁻³ — a range spanning a factor of 10 (1 mol% to 0.1 mol%) without specifying which end of the range applies to which Table I entry. Textbook readers are trained to compare catalyst efficiency via TON (turnover number) and TOF (turnover frequency), which cannot be calculated from the reported ratio range without knowing the actual mol% for each entry. The "loose definition" gap: catalyst loading is reported in a format that is nominally quantitative but practically non-comparable to the textbook's standard mol% / TON framework.
differentiation: V1-Q1 asks about missing TON data from a synthetic expert perspective; V4 asks from the textbook-reader perspective that a 10⁻²–10⁻³ range format is not the canonical way to report catalyst loading, making comparison with the textbook's benchmarks impossible without additional information.
severity: low
inference_tier: T1

---

--- Overlaps with V1/V2/V3 ---

V4-OV1 | overlaps_with: V1-Q3, V2-OV1 | gap_type: G7 (partial) | severity_V4: high | note: The absence of intermediate characterization (V1-Q3, V2-OV1) is partially G7 in character: in 1972, the isolation and spectroscopic characterization of Ni(0) and Ni(II) organometallic intermediates was technically extremely challenging, so the paper's reliance on (dipy)Ni model compounds is a historically appropriate black-box move at T₀; the textbook now presents the characterized Ni(II)(Ar)(X) intermediates as canonical evidence for the cycle. V4's textbook-reader view: [REDACTED: substantial verbatim quotation; see Tier 9]

V4-OV2 | overlaps_with: V1-Q7, V2-Q4, V2-Q5 | gap_type: G7 (partial) | severity_V4: high | note: The stereochemical scrambling (V4-Q6) partially overlaps with V1-Q7 and V2-Q4/Q5, but V4 uniquely identifies the "anomalous" descriptor as a G7 black-box term whose textbook resolution (retention expected from concerted OA; scrambling = radical or σ-vinyl diagnostic) is absent in the 1972 paper; V1 and V2 address this from contemporary mechanistic expertise.

V4-OV3 | overlaps_with: V2-Q2 | gap_type: G4 (Many→One direction) | severity_V4: high | note: V2-Q2 asks about Ni(0)/Ni(II) vs. Ni(I)/Ni(III) vs. radical chain mechanism from expert perspective; V4-Q1 asks from the textbook canonical Ni(0)/Ni(II) presentation that makes the paper's Ni(II)/Ni(II) initiation step (eq 2) inconsistent with the textbook's canonical active-catalyst statement — a different framing of the same gap.

V4-OV4 | overlaps_with: V1-Q6, V2-Q7, V2-Q8 | gap_type: G7 (partial) | severity_V4: medium | note: The ligand activity order (V1-Q6) and cis-geometry/ligand factors (V2-Q7, V2-Q8) partially overlap with V4-Q3 and V4-Q7; V4's unique contribution is identifying the absence of the bite-angle concept as a G7 gap — the concept did not exist in 1972 — rather than as an experimental omission or mechanistic ambiguity.

V4-OV5 | overlaps_with: V2-Q6, V3-OV3 | gap_type: G4 (Many→One) | severity_V4: medium | note: The homo-coupling selectivity gap (V2-Q6) partially overlaps with V4-Q4; V4's unique contribution is identifying two distinct mechanistic origins of homo-coupling (radical-chain vs. Ni(II)R₂ reductive elimination) that the textbook delineates but the paper conflates into one undifferentiated "prior methods are poorly selective" narrative.

---

--- 「綻び」 typology distribution (self-report) ---
G1 (Mid-step gap): 3 (V4-Q1: Ni(0) active catalyst missing step; V4-Q10: sp³ exclusion mechanistic basis; V4-Q11: transmetalation mechanism)
G2 (Unconditional generalization): 2 (V4-Q3: bite angle/cis-geometry condition; V4-Q9: β-H suppression kinetic condition)
G3 (Exception normalization): 0
G4 (Multiple-mechanism collapse): 1 (V4-Q4: homo-coupling mechanism collapse, Many→One direction — paper presents one undifferentiated "selectivity" narrative where textbook presents two distinct mechanistic origins)
G5 (Loose definition): 1 (V4-Q12: catalyst loading format non-standard)
G6 (Convention-stripped reference): 0
G7 (Resolved-to-black-box): 4 (V4-Q5: Ni(0)/Ni(II) cycle resolution, Δt=54y; V4-Q6: stereochemical scrambling mechanism resolved, Δt=54y; V4-Q7: bite angle concept post-1972, Δt=54y; V4-Q8: paradigmatic OA–TM–RE significance, Δt=54y)
G7-boundary: 0
G_novel: 0

---

--- V4 PILOT v3 self-evaluation ---
unique_kind_compliance_estimate: 85% — Most V4-Q items anchor to specific textbook canonical knowledge unavailable to V1/V2/V3 (especially G7 items, which require the textbook T₀+54y perspective). V4-Q9 and V4-Q10 have partial overlap with V1/V2 in topic but differ in framing (kinetic-condition requirement vs. scope limitation). V4-Q12 (catalyst loading format) is the weakest differentiation claim (~60% genuinely unique-in-kind vs. V1-Q1).

textbook_anchor_specificity_rate: 100% — All 12 V4-Q items cite a specific Crabtree or Hartwig chapter and section.

novel_subtype_flagged: 0 — All gaps fit within G1–G7 typology without requiring G_novel.

textbook_anchor_pending_count: 0 — All V4-Q items have identified textbook anchors.

anticipates_canonical_count: 3 (V4-Q5: paper's eq 2–4 cycle anticipates canonical Ni(0)/Ni(II) OA–TM–RE cycle; V4-Q7: paper's dpe ligand introduction anticipates bite-angle concept; V4-Q8: paper's "new preparative method" framing anticipates canonical recognition as founding OA–TM–RE example)

anticipates_canonical_pattern_note: Count = 3: **strong foundational paper signal** — kumada1972 introduced the catalytic cross-coupling cycle concept, the dpe bidentate ligand design rationale, and the sp²-selectivity principles that the field subsequently formalized into canonical textbook entries. Three dimensions of canonical knowledge were anticipated, consistent with a paradigm-establishing paper. This count (3) falls between the "peripheral foundational" signal (count=1, e.g., boyer1973/hayaishi1957) and the "canonical formation paper" signal (count=4, beinert1983) — kumada1972 is more foundational than peripheral but did not single-handedly constitute the full canonical framework (which required decades of subsequent mechanistic work on Ni(0)/Ni(II), bite angle, and the OA–TM–RE generalization). A count of 3 may be characteristic of "paradigm-initiating papers" that propose a framework but leave its elaboration to subsequent work.

g7_count: 4 — **G7 cross-corpus test: CONFIRMED for organometallic chemistry at Δt ≈ 54y**
  - V4-Q5: Ni(0)/Ni(II) catalytic cycle resolution (Δt = 54y)
  - V4-Q6: stereochemical scrambling mechanism resolved (Δt = 54y)
  - V4-Q7: bite angle concept post-1972 (Δt = 54y)
  - V4-Q8: paradigmatic OA–TM–RE significance (Δt = 54y)
  Note: G7 density = 4 for kumada1972 → interpretation per G7 density guide: density=3 corresponds to "Direct mechanism paper." kumada1972 at density=4 may constitute a new data point above the density=3 category. However, honest assessment: V4-Q8 is somewhat weaker G7 evidence (paradigmatic framing gap rather than a specifically-resolved mechanistic black box), so the "real" mechanism-proximity G7 count may be 3 (V4-Q5/Q6/Q7). Both counts reported: G7_strict (mechanism-proximal) = 3; G7_inclusive (paradigm/framing) = 4.

g7_boundary_count: 0 — G7-boundary absent. kumada1972 Δt ≈ 54y is well within the full G7 activation range (≥40y); no G7-boundary cases surface.

---

> **Tier 8 redaction notice**: This file is a redacted copy of the corresponding Tier 3 / Tier 9 output. Verbatim source-paper quotations have been replaced by `[REDACTED: see source paper §<loc>; full text retained in Tier 9 reviewer-only deposit]` markers, preserving location references and our own analytical content. Bibliographic fields (title, authors, journal, year, DOI), analytical labels (`evidence_chain:` with B-/U-/A-/C- internal IDs), short technical terms, and our own analytical text are not redacted. The redaction was applied by `scripts/redact_for_tier8.py` and, for this version, by `scripts/build_paperA_R1_public.py` with `scripts/redact_source_ngram_runs.py` (scripts of the project repository; they are not deposited).
