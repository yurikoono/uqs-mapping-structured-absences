prompt_version: stage1-v184-20260528_v4pilot_v6
model_info: claude-sonnet-4-6
executed_date: 2026-05-28
paper: Kumada / Tamao / Sumitani 1972, JACS — Ni-catalyzed cross-coupling of Grignard reagents
year: 1972
delta_t: ~54y
status: PILOT — V6 anchor-genesis schema cross-paper operability test (second paper after boyer1973); schema retrofit on existing v4 baseline (kumada_v184_sonnet_s1_v4pilot_v3_20260527.md)

================================================================================
== V7-SUPERSESSION HEADER (2026-05-28) ==
================================================================================
CITATION-LAYER STATUS: This pilot's textbook-citation layer is SUPERSEDED by
v7 actual-access discipline. The CONCEPTUAL gap-detection layer (the 12 V4-Q
questions) is RETAINED. The 4 user-verified items (Q1/Q5/Q7/Q12) are
re-classified in the "V7 RE-CLASSIFICATION APPENDIX" at the END of this file.
SCOPE LIMIT (GPT correction #2/#4, 2026-05-28): The "no fully faithful
  direct-textbook anchor" finding applies to THESE FOUR Crabtree-checked Kumada
  items ONLY — NOT generalized to the n=11 baseline or V4 in general. The
  unreliability is specific to **memory_based_anchor mode**; it does NOT negate
  V4 under actual_text_read.
PROMOTION JUDGMENT (convergent design diagnosis, NOT independent validation):
  schema operability PASS; factual anchoring reliability under memory-based
  mode FAIL; production HOLD.
See: V7 RE-CLASSIFICATION APPENDIX (end of file) + prompts/v184/prompt_stage1_turn4_canonical_textbook_v184_pilot_v7.md
================================================================================

scope_declaration (user constraint, 2026-05-28):
  This is a SCHEMA OPERABILITY TEST across paper types — boyer1973 (biochemistry, peripheral foundational, G7=1, Δt=48y) vs kumada1972 (organometallic, paradigm-initiating, G7=4, Δt=54y). The test asks: does the v6 R7 schema (stance + trigger_relation + anachronism_status + textbook_access_mode + paper_inference_tier + textbook_verification_status) populate naturally on a structurally distinct paper, or does it require paper-specific refactoring?

  Same constraints as boyer1973 v6 pilot:
  - All `textbook_access_mode` = `memory_based_anchor` (no Crabtree/Hartwig PDF read in session; no user-supplied excerpt)
  - All `textbook_quote_status` ∈ {`anchor_only_no_quote`, `paraphrased`}. `verified_short_quote` count = 0 by construction
  - This pilot evaluates v6 promotion criteria (a)–(d) cross-paper. Criterion (e) factual accuracy is deferred to post-pilot spot-check (per user policy)
  - No new spot-check executed on kumada1972 V4-Q items this session (would require additional WebSearch on organometallic primary literature). All `textbook_verification_status` = `memory_based_unverified`

baseline_references:
  - v4 baseline (v3 prompt, identical body to v4): papers/dev/kumada/kumada_v184_sonnet_s1_v4pilot_v3_20260527.md
    - 12 V4-Q items established
    - 5 V4-OV overlaps
    - gap_type distribution: G1=3 / G2=2 / G4=1 / G5=1 / G7=4 (strict 3, inclusive 4)
    - anticipates_canonical=3 → "paradigm-initiating paper signal"
  - v6 baseline (boyer1973): papers/sandbox/38_boyer1973/boyer1973_v184_sonnet_s1_v4pilot_v6_20260528.md
    - 9 V4-Q items
    - 4 V4-OV overlaps
    - gap_type distribution: G1=2 / G2=2 / G4=3 / G5=1 / G7=1
    - anticipates_canonical=3 (peripheral foundational vs paradigm-initiating distinction below)

cross_paper_design_note:
  This pilot preserves kumada1972's 12 V4-Q items + 5 V4-OV from the v4 baseline (no re-analysis of paper content). The v6 schema (stance / trigger_relation / anachronism_status / textbook_access_mode / paper_inference_tier / textbook_verification_status) is added as a retrofit layer. The test is whether all 12 items naturally populate the new fields without forcing — if any item resists natural mapping, that is a schema-operability failure that v7 would need to address.

---

[V4 (PILOT v6): Canonical-textbook reader (textbook-equipped reader)]
field: V4_canonical_textbook_reader — Crabtree "The Organometallic Chemistry of the Transition Metals" (7th ed., 2022) + Hartwig "Organotransition Metal Chemistry" (2010), cross-coupling catalysis chapters
field_rationale: V1 (synthetic/analytical), V2 (mechanistic/kinetic), and V3 (analytical chemistry/chromatography) all operate with field-internal licenses — they know that a 1972 communication is not expected to report oxidative addition rate constants. V4 uniquely asks what the textbook presents as established canonical knowledge that the paper omits, mis-describes, or leaves as an open question — a question a reader equipped only with textbook knowledge would find jarring. Per-item rationale appears in `stance.rationale` for each V4-Q below.

textbook_corpus_used:
  - Crabtree, "The Organometallic Chemistry of the Transition Metals," 7th ed. (2022), Chs. 4 / 6 / 9
  - Hartwig, "Organotransition Metal Chemistry" (2010), Chs. 7 / 18
  Note: this pilot's `textbook_access_mode` is `memory_based_anchor` for ALL items.

---

--- New questions (v6 schema retrofit on v4 baseline) ---

V4-Q1:
  loc: P2:Lcol:18* (equations 2–4)
  quote: [REDACTED: see `loc:` above; full text in Tier 9]
  paper_anchor_role: figure_reference

  stance:
    frame: V4_canonical_textbook_reader
    rationale: V1 and V2 know that the 1972 paper's catalytic cycle was an early proposal and that the field has since clarified the active oxidation state — they read past the precatalyst-vs-active-catalyst distinction. The textbook-equipped reader, holding the Ni(0)/Ni(II) canonical cycle as a single defined object, registers the missing reduction step immediately as a gap.

  textbook_reference: Crabtree Ch. 9, "Kumada Coupling" section; Hartwig Ch. 18 §18.1
  textbook_quote_status: paraphrased
  textbook_canonical_claim: [REDACTED: substantial verbatim quotation; see Tier 9]
  textbook_access_mode: memory_based_anchor

  trigger_relation:
    primary_type: omission
    secondary_type: later-resolution
    subtype: null
    explanation: Paper's equation 2 starts the cycle at Ni(II)R₂ formation but does not show the prior Ni(II)→Ni(0) reduction step. The textbook canonical cycle inserts this reduction step between precatalyst (Ni(II)Cl₂) and active catalyst (Ni(0)). The primary relation is omission (paper does not state the reduction); secondary is later-resolution (the Ni(0) active species was characterized only after 1972).

  gap_type: G1 (Mid-step gap)
  question: The textbook presents a canonical Ni(0)/Ni(II) catalytic cycle beginning with Ni(0) performing oxidative addition. Equation 2 in the paper describes the precatalyst NiCl₂L₂ reacting directly with two equivalents of Grignard reagent to form Ni(II)R₂ — skipping the reduction step. Where in the paper's mechanism does the Ni(0) active catalyst appear, and is the paper proposing a Ni(II)/Ni(II) or a Ni(0)/Ni(II) cycle?

  anachronism_status:
    value: uncertain
    rationale: The Ni(0) active catalyst hypothesis was emerging in 1972 but not yet canonical — early studies (Wilke 1966, Tolman late 1960s–early 1970s) had observed Ni(0) species, but the connection to catalytic cross-coupling specifically came in subsequent years (Kumada follow-up 1974, others 1976+). A 1972 textbook-equipped reader could plausibly ask "where is the Ni(0) species?" if equipped with Wilke-era organometallic knowledge, but might not insist on it as canonical.

  differentiation: V1 and V2 note mechanistic uncertainty but neither asks the textbook-grounded question of which oxidation state is the active catalyst — V4 asks this from the canonical textbook presentation where Ni(0) is unambiguously the active species, a presentation that postdates the 1972 paper.
  severity: high
  paper_inference_tier: T1_paper_explicit
  textbook_verification_status: memory_based_unverified

V4-Q2:
  loc: P2:Lcol:5* (equation 1 and surrounding text)
  quote: [REDACTED: see `loc:` above; full text in Tier 9]
  paper_anchor_role: observed_statement

  stance:
    frame: V4_canonical_textbook_reader
    rationale: V2 reads the paper's "released by halide" phrasing through mechanistic-skeptic lens and asks about the mechanistic detail. The textbook-equipped reader holds canonical reductive elimination as a spontaneous concerted process requiring no co-reagent — the paper's framing immediately reads as inconsistent with the canonical definition.

  textbook_reference: Crabtree Ch. 6 §6.2, "Reductive elimination"
  textbook_quote_status: paraphrased
  textbook_canonical_claim: [REDACTED: substantial verbatim quotation; see Tier 9]
  textbook_access_mode: memory_based_anchor

  trigger_relation:
    primary_type: mismatch
    secondary_type: later-resolution
    subtype: null
    explanation: Paper describes the coupling step as occurring "by the action of an organic halide" — implying the halide actively triggers R–R release. The textbook canonical mechanism describes reductive elimination as spontaneous (halide is the OA substrate downstream, not a trigger for R–R release). The two formulations are mechanistically inconsistent. Secondary later-resolution because the canonical mechanism became firm post-1972.

  gap_type: G1 (Mid-step gap)
  question: The textbook presents reductive elimination as a spontaneous concerted process from cis-NiR₂L₂. The paper's "released by the action of an organic halide" is not standard reductive elimination. Does the paper describe (a) oxidative addition of R'X'' to Ni(II)R₂ to give Ni(IV), then reductive elimination; (b) an associative substitution; or (c) something else?

  anachronism_status:
    value: contemporary-plausible
    rationale: Canonical reductive elimination definitions (concerted, cis, spontaneous) were established in organometallic literature by 1972 (Halpern late 1960s, Collman around 1968–1972). A 1972 reader of organometallic textbooks would have flagged the "released by halide" phrasing as non-standard. This question is askable at the paper's date.

  differentiation: V2-Q3 addresses this mechanistic ambiguity from an expert mechanistic viewpoint; V4 asks it from the textbook-reader perspective where reductive elimination is defined as spontaneous (no halide required).
  severity: high
  paper_inference_tier: T1_paper_explicit
  textbook_verification_status: memory_based_unverified

V4-Q3:
  loc: P3:Lcol:8* (feature 3, ligand activity order)
  quote: [REDACTED: see `loc:` above; full text in Tier 9]
  paper_anchor_role: observed_statement

  stance:
    frame: V4_canonical_textbook_reader
    rationale: V2 sees the cis-geometry conclusion as one mechanistic factor and asks for additional electronic factors. The textbook-equipped reader, who knows that the canonical analysis separates cis-requirement (necessary condition) from bite-angle quantification (rate-tuning factor), registers that the paper conflates these two distinct canonical knobs into a single "first requisite" framing.

  textbook_reference: Crabtree Ch. 6 §6.3 (reductive elimination cis requirement) + Crabtree Ch. 9 §9.4 (bite angle effects)
  textbook_quote_status: paraphrased
  textbook_canonical_claim: [REDACTED: substantial verbatim quotation; see Tier 9]
  textbook_access_mode: memory_based_anchor

  trigger_relation:
    primary_type: under-specification
    secondary_type: later-resolution
    subtype: null
    explanation: Paper presents cis-geometry as the "first requisite" sufficient to explain the activity order. Textbook canonical analysis adds bite angle as an independent quantitative parameter that further tunes the rate. The paper under-specifies the multi-factor canonical analysis. Secondary later-resolution because bite-angle quantification was developed post-1972.

  gap_type: G2 (Unconditional generalization)
  question: The textbook separates two canonical factors — cis-requirement and bite-angle optimization — that together explain bidentate phosphine effects in cross-coupling. The paper's "cis configuration is the first requisite" explains part of the dpp > dpe > dmpe ordering but does not address the bite angle / σ-donor / backbone rigidity dimension. Does the observed order reflect bite angle, electronic effects, or backbone rigidity, conditions the textbook treats as independent?

  anachronism_status:
    value: retrospective-only
    rationale: The bite angle concept as a quantitative design parameter was formalized in the 1980s–2000s (Casey, van Leeuwen). In 1972, the concept did not exist in this form. The paper's qualitative "cis = first requisite" was the available canonical framing.

  differentiation: V2-Q8 asks about cis geometry vs. electronic factors from expert mechanistic perspective; V4 asks from the textbook presentation that separates cis-requirement and bite-angle effects into distinct canonical factors.
  severity: medium
  paper_inference_tier: T1_paper_explicit
  textbook_verification_status: memory_based_unverified

V4-Q4:
  loc: P1:Rcol:13* (introduction, prior cross-coupling context)
  quote: [REDACTED: see `loc:` above; full text in Tier 9]
  paper_anchor_role: observed_statement

  stance:
    frame: V4_canonical_textbook_reader
    rationale: V1 and V2 read the paper's homo-coupling discussion within the practitioner frame ("prior methods had selectivity problems"). The textbook-equipped reader holds two specifically distinct mechanistic origins of homo-coupling (radical-chain in Fe/Cu/Ag salts; bis-alkyl M(II) reductive elimination) as separate canonical entries, and registers that the paper collapses both into one undifferentiated narrative.

  textbook_reference: Hartwig Ch. 18 §18.1 (cross-coupling mechanism distinctions)
  textbook_quote_status: paraphrased
  textbook_canonical_claim: [REDACTED: substantial verbatim quotation; see Tier 9]
  textbook_access_mode: memory_based_anchor

  trigger_relation:
    primary_type: mechanism-gap
    secondary_type: under-specification
    subtype: null
    explanation: Paper attributes prior poor selectivity to "nonspecific nature" of earlier catalysts — a single undifferentiated reason. Textbook canonical analysis distinguishes radical-chain pathways from bis-alkyl reductive elimination as separate mechanisms requiring different design responses. The paper's account omits this mechanistic differentiation (mechanism-gap); the explanation is also under-specified about which pathway dpe suppresses.

  gap_type: G4 (Multiple-mechanism collapse, Many→One direction)
  question: The textbook presents two mechanistically distinct reasons why earlier transition-metal-catalyzed Grignard couplings gave homo-coupling: (a) radical-chain mechanisms with Fe/Cu/Ag, and (b) facile reductive elimination from bis-alkyl M(II) species. The paper collapses both into "nonspecific catalysts." Does dpe suppress homo-coupling by preventing radical pathways, by controlling the Ni(II)R₂ reductive elimination kinetics, or both?

  anachronism_status:
    value: uncertain
    rationale: Radical-chain mechanisms for Fe/Cu/Ag-catalyzed Grignard reactions were being identified by Kochi (1971+) and Tamura around 1972. The reductive elimination origin of homo-coupling from M(II)R₂ was being mechanistically clarified around the same time. A well-read 1972 organometallic chemist could plausibly distinguish these mechanisms, but their canonical separation into the textbook two-pathway form was a later consolidation.

  differentiation: V1-Q14 and V2-Q6 address selectivity from synthetic and mechanistic angles; V4 asks from the textbook canonical presentation that delineates two distinct mechanistic origins of homo-coupling.
  severity: medium
  paper_inference_tier: T1_paper_explicit
  textbook_verification_status: memory_based_unverified

V4-Q5:
  loc: P2:Lcol:1* (equation 3)
  quote: [REDACTED: see `loc:` above; full text in Tier 9]
  paper_anchor_role: figure_reference

  stance:
    frame: V4_canonical_textbook_reader
    rationale: V1/V2/V3 engage equation 3 within the paper's own oxidation-state framework. The textbook-equipped reader, holding the resolved Ni(0)/Ni(II) cycle as canonical, registers equation 3 as a description in pre-canonical oxidation-state terms — historically appropriate vagueness that the field subsequently resolved.

  textbook_reference: Hartwig Ch. 18 §18.1; Crabtree Ch. 9 (canonical Ni(0)/Ni(II) OA-TM-RE cycle)
  textbook_quote_status: paraphrased
  textbook_canonical_claim: [REDACTED: substantial verbatim quotation; see Tier 9]
  textbook_access_mode: memory_based_anchor

  trigger_relation:
    primary_type: later-resolution
    secondary_type: null
    subtype: null
    explanation: Paper's equation 3 describes the R–R-releasing step in pre-canonical oxidation-state terms (Ni(II)R₂ + R'X'' → Ni(II)(R')(X'') + R–R, implying Ni(II)/Ni(IV) or Ni(II)/Ni(II) cycle). Textbook canonical mechanism is Ni(0)/Ni(II) with OA of R'X'' to Ni(0). The relation is paradigmatic later-resolution at Δt ≈ 54y. The paper's framing is historically appropriate for T₀.

  gap_type: G7 (Resolved-to-black-box, Δt ≈ 54y)
  question: The textbook canonical cycle is Ni(0)/Ni(II) with OA-TM-RE sequence. The paper's equation 3 describes the R–R-releasing step in terms of Ni(II)R₂ being converted by R'X'' — leaving the oxidation-state pathway as a black box. The textbook now presents this step as oxidative addition of R'X'' to Ni(0) (the resolved mechanism). The 1972 description is contemporaneously appropriate vagueness; the textbook has since resolved it.

  anachronism_status:
    value: retrospective-only
    rationale: The Ni(0)/Ni(II) canonical resolution required mechanistic studies in the late 1970s and 1980s (Kumada follow-ups, Negishi, Stille). In 1972, the oxidation-state pathway was genuinely unresolved. Strict G7 = strict retrospective-only.

  differentiation: V1/V2/V3 none flag this as historically necessary vagueness that the field subsequently resolved; V4 uniquely identifies this as a G7 gap anchored to the textbook's resolved mechanism vs. the paper's contemporaneously appropriate black-box description.
  severity: high
  paper_inference_tier: T2_paper_grounded_inference
  textbook_verification_status: memory_based_unverified
  note: textbook_anchor_relation_to_paper: anticipates_canonical — paper introduces the catalytic cycle concept that the field subsequently resolved as Ni(0)/Ni(II).

V4-Q6:
  loc: P3:Lcol:18* (feature 4)
  quote: [REDACTED: see `loc:` above; full text in Tier 9]
  paper_anchor_role: observed_statement

  stance:
    frame: V4_canonical_textbook_reader
    rationale: V1/V2/V3 engage the stereochemical scrambling from synthetic/mechanistic expertise. The textbook-equipped reader holds vinyl-OA stereochemical retention as canonical AND the loss-of-fidelity as a diagnostic of radical/π-allyl pathways — so the paper's "anomalous" label is recognized as a pre-canonical black-box term whose textbook resolution did not yet exist.

  textbook_reference: Crabtree Ch. 6 §6.2 and Ch. 9 (vinyl OA stereochemistry; retention as canonical, scrambling as diagnostic)
  textbook_quote_status: paraphrased
  textbook_canonical_claim: [REDACTED: substantial verbatim quotation; see Tier 9]
  textbook_access_mode: memory_based_anchor

  trigger_relation:
    primary_type: later-resolution
    secondary_type: null
    subtype: null
    explanation: Paper labels the cis/trans scrambling as "anomalous[REDACTED: substantial verbatim quotation; see Tier 9]anomalous" label is later-resolution to a specific canonical diagnostic.

  gap_type: G7 (Resolved-to-black-box, Δt ≈ 54y)
  question: The textbook presents vinyl-halide cross-coupling as proceeding with stereochemical retention via concerted OA to Ni(0), with loss of fidelity diagnosing radical or π-allyl pathways. The paper labels the scrambling "anomalous" without resolution. The textbook now provides the diagnostic interpretation. What mechanistic pathway accounts for the scrambling — radical, π-allyl Ni, or σ-vinyl Ni interconversion?

  anachronism_status:
    value: retrospective-only
    rationale: The diagnostic interpretation of vinyl stereochemical scrambling (radical vs concerted OA vs π-allyl) was clarified through the 1970s–80s. In 1972, "anomalous" was the available descriptor without a canonical diagnostic framework.

  differentiation: V1-Q7 and V2-Q4/Q5 address the stereochemical question from synthetic/mechanistic expertise; V4 uniquely identifies the "anomalous" label as a G7 black-box term.
  severity: high
  paper_inference_tier: T2_paper_grounded_inference
  textbook_verification_status: memory_based_unverified

V4-Q7:
  loc: P3:Lcol:12* (feature 3, ligand identity: dpe)
  quote: [REDACTED: see `loc:` above; full text in Tier 9]
  paper_anchor_role: terminology

  stance:
    frame: V4_canonical_textbook_reader
    rationale: V2 asks about bite angle vs cone angle from mechanistic expertise. The textbook-equipped reader notes that the very concept of bite angle as a quantitative design parameter did not exist in 1972 — the paper appropriately uses qualitative cis-geometry language. The textbook resolution introduces a concept that postdates the paper.

  textbook_reference: Crabtree Ch. 9 §9.4 (bite angle effects in Ni cross-coupling)
  textbook_quote_status: paraphrased
  textbook_canonical_claim: [REDACTED: substantial verbatim quotation; see Tier 9]
  textbook_access_mode: memory_based_anchor

  trigger_relation:
    primary_type: later-resolution
    secondary_type: terminology-shift
    subtype: null
    explanation: Paper introduces dpe as the most useful bidentate ligand and uses cis-geometry vocabulary. Textbook resolves the ligand effect using the bite angle concept (a vocabulary that did not exist quantitatively in 1972). Primary later-resolution (the concept postdates the paper); secondary terminology-shift (the textbook vocabulary refines the paper's qualitative description).

  gap_type: G7 (Resolved-to-black-box, Δt ≈ 54y)
  question: The textbook presents bite angle as a quantitative parameter controlling reductive elimination rate, independent of the cis-geometry effect. The paper uses qualitative cis-geometry language — appropriate for 1972 since the bite angle concept did not yet exist quantitatively. The textbook resolution introduces a refined descriptor (bite angle) that anticipates and supersedes the paper's qualitative discussion.

  anachronism_status:
    value: retrospective-only
    rationale: Bite angle as a quantitative cross-coupling design parameter was developed 1990s–2000s. In 1972 the concept did not exist in this form. The question is strict retrospective-only.

  differentiation: V2-Q8 asks about bite angle vs cone angle from expert mechanistic perspective; V4 identifies the absence of bite angle as a concept in the 1972 paper as a G7 gap.
  severity: medium
  paper_inference_tier: T2_paper_grounded_inference
  textbook_verification_status: memory_based_unverified
  note: textbook_anchor_relation_to_paper: anticipates_canonical — paper introduces dpe as superior bidentate ligand, field subsequently quantified as bite-angle effect.

V4-Q8:
  loc: P1:Rcol:1* (introduction)
  quote: [REDACTED: see `loc:` above; full text in Tier 9]
  paper_anchor_role: sentence_silence

  stance:
    frame: V4_canonical_textbook_reader
    rationale: V1/V2/V3 read the paper with knowledge of its retrospective significance — they implicitly know that Kumada coupling founded the OA-TM-RE cycle paradigm. The textbook-equipped reader notices that the paper itself frames its scope narrowly ("two independent facts") and does not claim paradigmatic generality — a framing gap visible only when comparing the paper's self-positioning to the textbook's retrospective canonization.

  textbook_reference: Hartwig Ch. 18 §18.1 (Kumada-Tamao as founding example of OA-TM-RE paradigm)
  textbook_quote_status: paraphrased
  textbook_canonical_claim: [REDACTED: substantial verbatim quotation; see Tier 9]
  textbook_access_mode: memory_based_anchor

  trigger_relation:
    primary_type: later-resolution
    secondary_type: null
    subtype: paradigm-omission
    explanation: Paper presents the work as an isolated synthetic method ("two independent facts"), not as the founding example of a cross-coupling paradigm. Textbook resolves the paper as paradigmatic (the OA-TM-RE prototype). The relation is later-resolution at the paradigm-recognition level; subtype "paradigm-omission" because what is missing is paradigm framing rather than a specific fact.

  gap_type: G7 (Resolved-to-black-box, Δt ≈ 54y)
  question: The paper frames the Ni-catalyzed Grignard coupling as a method motivated by "two independent facts concerning σ-organonickel complexes," not as the founding example of a cross-coupling paradigm. The textbook presents Kumada coupling as the prototype OA-TM-RE cycle that underlies Suzuki/Negishi/Stille/etc. Why is the paradigmatic significance absent from the paper's self-framing?

  anachronism_status:
    value: retrospective-only
    rationale: In 1972, the OA-TM-RE paradigm did not exist as a unified framework (Pd-catalyzed Heck just emerging; Suzuki/Negishi not yet discovered). The paradigm recognition was a retrospective consolidation through the 1980s–90s. Strict retrospective-only.

  differentiation: No V1/V2/V3 question addresses this framing gap, because all three operate from field-internal knowledge that already knows the retrospective significance; V4 uniquely asks why the textbook's "first example of OA-TM-RE" canonization is absent from the paper.
  severity: medium
  paper_inference_tier: T2_paper_grounded_inference
  textbook_verification_status: memory_based_unverified
  note: textbook_anchor_relation_to_paper: anticipates_canonical — paper introduces the catalytic cycle that the field subsequently generalized as OA-TM-RE paradigm.

V4-Q9:
  loc: P3:Lcol:1* (feature 1)
  quote: [REDACTED: see `loc:` above; full text in Tier 9]
  paper_anchor_role: observed_statement

  stance:
    frame: V4_canonical_textbook_reader
    rationale: V1 asks about quantification of β-hydride elimination byproducts from synthetic perspective. The textbook-equipped reader, who knows that β-H suppression is canonically a kinetic competition (transmetalation must outpace β-H elimination), registers the paper's unconditional "high yields are obtained" as missing the kinetic-condition specification.

  textbook_reference: Hartwig Ch. 18 §18.3 (β-hydride elimination as kinetic competitor)
  textbook_quote_status: paraphrased
  textbook_canonical_claim: [REDACTED: substantial verbatim quotation; see Tier 9]
  textbook_access_mode: memory_based_anchor

  trigger_relation:
    primary_type: under-specification
    secondary_type: null
    subtype: null
    explanation: Paper states "high yields are obtained" as unconditional. Textbook frames the same outcome as kinetically conditional (transmetalation must outcompete β-H elimination). The paper under-specifies the kinetic conditions under which the unconditional-sounding claim holds (temperature, Grignard concentration, ligand, etc.).

  gap_type: G2 (Unconditional generalization)
  question: The textbook frames β-H suppression in Kumada coupling as a kinetic competition: transmetalation must outpace β-H elimination. The paper's "high yields" claim is presented unconditionally. Under what conditions (temperature, Grignard concentration, ligand) does transmetalation kinetically outcompete β-H elimination? Are these the Table I conditions, and does the unconditional-sounding feature hold across the parameter space?

  anachronism_status:
    value: contemporary-plausible
    rationale: β-hydride elimination as a competing pathway and the kinetic-competition framework were established in 1970s organometallic literature (Schrock, Whitesides, Halpern). A 1972 textbook-equipped reader could ask the kinetic-condition question.

  differentiation: V1-Q9 asks about quantification of β-hydride elimination byproducts; V4 asks from the textbook canonical picture that frames β-H suppression as a kinetic competition requiring specification of operating conditions.
  severity: medium
  paper_inference_tier: T1_paper_explicit
  textbook_verification_status: memory_based_unverified

V4-Q10:
  loc: P3:Lcol:6* (feature 2)
  quote: [REDACTED: see `loc:` above; full text in Tier 9]
  paper_anchor_role: observed_statement

  stance:
    frame: V4_canonical_textbook_reader
    rationale: V1 asks about experimental validation of sp³ exclusion. The textbook-equipped reader, who knows the canonical OA reactivity order (aryl > vinyl > allyl ≫ alkyl) and its mechanistic basis (π-system stabilization of OA transition state), notes that the paper states the conclusion without the mechanistic explanation that the textbook provides.

  textbook_reference: Crabtree Ch. 6 §6.1 (OA reactivity order and mechanistic basis)
  textbook_quote_status: paraphrased
  textbook_canonical_claim: [REDACTED: substantial verbatim quotation; see Tier 9]
  textbook_access_mode: memory_based_anchor

  trigger_relation:
    primary_type: omission
    secondary_type: null
    subtype: null
    explanation: Paper states "only sp² halides can be used" as a feature without mechanistic explanation. Textbook provides the canonical mechanistic basis (OA-barrier difference, π-stabilization). The relation is omission: the paper omits the textbook's explanatory step (mechanism A → conclusion B is missing A).

  gap_type: G1 (Mid-step gap)
  question: The textbook explains sp² selectivity in Ni cross-coupling via OA-barrier differences (π-stabilization of aryl/vinyl OA transition state, absent for alkyl). The paper states the selectivity rule without the mechanistic basis. Why are sp³ halides inactive — high OA barrier, β-H elimination capture, or something else?

  anachronism_status:
    value: contemporary-plausible
    rationale: OA reactivity differences across hybridization were appreciated in 1970s organometallic literature. A 1972 textbook-equipped reader could reasonably expect the mechanistic explanation. Contemporary-plausible.

  differentiation: V1-Q4 asks about experimental validation of sp³ exclusion; V4 asks from the textbook reader's perspective why the mechanistic explanation for sp² selectivity is absent.
  severity: low
  paper_inference_tier: T1_paper_explicit
  textbook_verification_status: memory_based_unverified

V4-Q11:
  loc: P2:Lcol:18* (equations 2–4, transmetalation step eq 4)
  quote: [REDACTED: see `loc:` above; full text in Tier 9]
  paper_anchor_role: figure_reference

  stance:
    frame: V4_canonical_textbook_reader
    rationale: V2 asks about rate-determining step from kinetic-mechanistic expert perspective. The textbook-equipped reader, who has internalized the specific 4-membered cyclic TS for Grignard transmetalation to Ni(II), notes that the paper's equation 4 represents transmetalation as bare ligand exchange without the canonical mechanistic detail.

  textbook_reference: Hartwig Ch. 18 §18.2 (Grignard transmetalation mechanism)
  textbook_quote_status: paraphrased
  textbook_canonical_claim: [REDACTED: substantial verbatim quotation; see Tier 9]
  textbook_access_mode: memory_based_anchor

  trigger_relation:
    primary_type: omission
    secondary_type: null
    subtype: null
    explanation: Paper's equation 4 represents transmetalation as ligand exchange without specifying the cyclic TS, the driving force, or the mechanistic distinction from other transmetalating reagents. Textbook canonical mechanism (4-membered TS, MgX₂ driving force) is omitted from the paper.

  gap_type: G1 (Mid-step gap)
  question: The textbook presents transmetalation in Kumada coupling via a 4-membered cyclic TS with MgX₂ formation as the driving force. The paper's equation 4 represents transmetalation as simple ligand exchange with no mechanistic detail. Why are Grignard reagents particularly effective transmetalating agents for Ni(II), and what is the mechanistic basis?

  anachronism_status:
    value: uncertain
    rationale: The specific 4-membered cyclic TS for Grignard transmetalation was elucidated through later mechanistic studies (Hartwig review 2010 represents the consolidated picture). In 1972 the existence of "transmetalation" as a step was understood, but the specific TS mechanism was not yet established. Mixed plausibility.

  differentiation: V2-Q1 asks about rate-determining step from kinetic/mechanistic expert perspective; V4 asks why the textbook-canonical mechanistic explanation for Grignard transmetalation is absent.
  severity: low
  paper_inference_tier: T2_paper_grounded_inference
  textbook_verification_status: memory_based_unverified

V4-Q12:
  loc: P2:Rcol:1* (Table I header)
  quote: [REDACTED: see `loc:` above; full text in Tier 9]
  paper_anchor_role: numerical_value

  stance:
    frame: V4_canonical_textbook_reader
    rationale: V1 asks about missing TON data from synthetic expert perspective. The textbook-equipped reader, who knows the canonical reporting standard for catalyst loading (mol% with TON/TOF for comparison), notes that the paper's "ratio range 10⁻²–10⁻³" is not the textbook-standard format and prevents calculating TON.

  textbook_reference: Crabtree Ch. 9; Hartwig Ch. 18 (standard catalyst loading and TON reporting conventions)
  textbook_quote_status: paraphrased
  textbook_canonical_claim: [REDACTED: substantial verbatim quotation; see Tier 9]
  textbook_access_mode: memory_based_anchor

  trigger_relation:
    primary_type: under-specification
    secondary_type: null
    subtype: null
    explanation: Paper reports catalyst loading as a ratio range (10⁻²–10⁻³, spanning a factor of 10) without specifying which entry uses which loading. Textbook standard is mol% per entry with TON calculable. The paper's format is under-specified relative to the textbook's standardized reporting framework.

  gap_type: G5 (Loose definition)
  question: The textbook standard for cross-coupling catalyst loading is mol% per entry with TON/TOF calculable. The paper reports a ratio range "10⁻²–10⁻³" without per-entry specification. What is the catalyst loading for each Table I entry, and what TON does each represent?

  anachronism_status:
    value: contemporary-plausible
    rationale: Standardized mol% reporting was a 1970s norm, although the rigor of TON/TOF reporting varied. The paper's range-format reporting was acceptable but already non-canonical by 1972 standards.

  differentiation: V1-Q1 asks about missing TON data from synthetic expert perspective; V4 asks from the textbook-reader perspective that the ratio-range format is not the canonical way to report catalyst loading.
  severity: low
  paper_inference_tier: T1_paper_explicit
  textbook_verification_status: memory_based_unverified

---

--- Overlaps with V1/V2/V3 (v6 R5 schema: genesis metadata) ---

V4-OV1:
  overlaps_with: V1-Q3, V2-OV1
  gap_type: G7 (partial)
  severity_V4: high
  textbook_reference: Crabtree Ch. 9, Hartwig Ch. 18 (Ni intermediate spectroscopic characterization)
  textbook_access_mode: memory_based_anchor
  trigger_relation:
    primary_type: later-resolution
    explanation: V1/V2 note the absence of intermediate characterization from data-completeness perspective. V4 anchors to textbook's canonical Ni(II)(Ar)(X) intermediate evidence base (crystal structures, IR/UV spectra) that was developed post-1972. The 1972 reliance on (dipy)Ni model compounds is historically appropriate; textbook resolution provides post-paper characterization.
  anachronism_status:
    value: retrospective-only
    rationale: Spectroscopic/structural characterization of Ni cross-coupling intermediates required techniques developed after 1972.
  stance_rationale: V1 (synthetic) and V2 (mechanistic) demand contemporary in-situ characterization; V4 anchors to retrospective canonical evidence that did not exist in 1972. Same gap, different epistemic anchors.
  textbook_verification_status: memory_based_unverified
  note: Cross-frame convergence on the intermediate-characterization gap; V4 adds the historical-positioning dimension.

V4-OV2:
  overlaps_with: V1-Q7, V2-Q4, V2-Q5
  gap_type: G7 (partial)
  severity_V4: high
  textbook_reference: Crabtree Ch. 6/9 (vinyl OA stereochemical retention)
  textbook_access_mode: memory_based_anchor
  trigger_relation:
    primary_type: later-resolution
    explanation: V1/V2 address vinyl stereochemistry from synthetic/mechanistic expertise. V4 identifies the "anomalous" label as a G7 black-box term whose textbook resolution (retention from concerted OA; scrambling as radical/π-allyl diagnostic) is absent in 1972 but canonical now. Same observation reached via expert reasoning (V1/V2) vs textbook canonical diagnostic (V4).
  anachronism_status:
    value: retrospective-only
    rationale: The canonical diagnostic interpretation of stereochemical scrambling was 1970s–80s development.
  stance_rationale: V1/V2 ask what happened experimentally; V4 asks why the canonical diagnostic interpretation is absent. Same observation, different frame.
  textbook_verification_status: memory_based_unverified
  note: V4 supplies retrospective canonical diagnostic vs V1/V2 contemporary mechanistic probing.

V4-OV3:
  overlaps_with: V2-Q2
  gap_type: G4 (Many→One)
  severity_V4: high
  textbook_reference: Crabtree Ch. 9 (canonical Ni(0)/Ni(II) cycle)
  textbook_access_mode: memory_based_anchor
  trigger_relation:
    primary_type: mismatch
    explanation: V2-Q2 asks Ni(0)/Ni(II) vs Ni(I)/Ni(III) vs radical chain from mechanistic expertise. V4-Q1 asks from the textbook canonical Ni(0)/Ni(II) presentation that makes the paper's Ni(II)/Ni(II) initiation step inconsistent with canonical active-catalyst statement. Same gap surfaced by expert speculation (V2) vs textbook canonical mismatch (V4).
  anachronism_status:
    value: uncertain
    rationale: Ni(0) active catalyst hypothesis available in 1972 but not yet canonical.
  stance_rationale: V2 (mechanistic skeptic) speculates among mechanisms; V4 (textbook) reaches the same gap by canonical mismatch. Convergence indicates a structurally robust gap.
  textbook_verification_status: memory_based_unverified
  note: Cross-frame convergence on the active-oxidation-state question.

V4-OV4:
  overlaps_with: V1-Q6, V2-Q7, V2-Q8
  gap_type: G7 (partial)
  severity_V4: medium
  textbook_reference: Crabtree Ch. 9 (bite angle effects)
  textbook_access_mode: memory_based_anchor
  trigger_relation:
    primary_type: later-resolution
    explanation: V1/V2 address ligand effects from synthetic/mechanistic perspectives. V4 identifies the absence of the bite-angle concept as a G7 gap (the concept did not exist in 1972). Same observation reached from expert mechanism (V1/V2) vs textbook conceptual evolution (V4).
  anachronism_status:
    value: retrospective-only
    rationale: Bite angle as a quantitative parameter was 1990s–2000s development.
  stance_rationale: V1/V2 explore mechanistic ligand factors; V4 identifies the conceptual vocabulary gap (bite angle).
  textbook_verification_status: memory_based_unverified
  note: V4 unique contribution is the conceptual-evolution dimension.

V4-OV5:
  overlaps_with: V2-Q6, V3-OV3
  gap_type: G4 (Many→One)
  severity_V4: medium
  textbook_reference: Hartwig Ch. 18 (homo-coupling mechanism distinctions)
  textbook_access_mode: memory_based_anchor
  trigger_relation:
    primary_type: mechanism-gap
    explanation: V2-Q6 asks about selectivity from mechanistic perspective. V4-Q4 identifies the textbook's two-pathway delineation (radical-chain vs bis-alkyl reductive elimination) that the paper collapses into one narrative. Same gap reached by expert critique (V2) vs textbook canonical differentiation (V4).
  anachronism_status:
    value: uncertain
    rationale: Both pathways were being clarified around 1972; their canonical separation was a later consolidation.
  stance_rationale: V2 (mechanistic) probes for kinetic distinction; V4 (textbook) supplies the canonical two-pathway framework. Different frames, same gap.
  textbook_verification_status: memory_based_unverified
  note: V4 frames the gap as mechanism collapse, V2 as kinetic discrimination question.

---

--- 「綻び」 typology distribution (self-report) ---
G1 (Mid-step gap): 3 (V4-Q1, V4-Q10, V4-Q11)
G2 (Unconditional generalization): 2 (V4-Q3, V4-Q9)
G3 (Exception normalization): 0
G4 (Multiple-mechanism collapse): 1 (V4-Q4)
G5 (Loose definition): 1 (V4-Q12)
G6 (Convention-stripped reference): 0
G7 (Resolved-to-black-box, Δt ≈ 54y): 4 (V4-Q5, V4-Q6, V4-Q7, V4-Q8)
G7-boundary: 0
G_novel: 0

Total Part A questions: 12
Regression check vs v4 baseline (2026-05-27): gap_type distribution IDENTICAL — G1=3 / G2=2 / G4=1 / G5=1 / G7=4. v5/v6 promotion criterion (c) "No regression on v4 typology" SATISFIED.

---

--- V4 PILOT v6 self-evaluation ---

unique_kind_compliance_estimate: 85% (unchanged from v4 baseline)

textbook_anchor_specificity_rate: 100% (all 12 V4-Q items cite specific Crabtree or Hartwig chapter)

novel_subtype_flagged: 0

textbook_anchor_pending_count: 0

textbook_quote_status_distribution (v5 introduced, v6 R2 refined):
  anchor_only_no_quote_count: 0
  paraphrased_count: 12
  verified_short_quote_count: 0
  — All 12 V4-Q items use paraphrased canonical claims. No anchor-only items in this paper (vs boyer1973 which had 1 anchor_only). The denser textbook claim content reflects kumada1972's mechanistic specificity (canonical Ni-cycle is well-defined; each gap maps to a specific canonical knob).

textbook_access_mode_distribution (v6 R6 NEW):
  actual_text_read_count: 0
  user_supplied_excerpt_count: 0
  memory_based_anchor_count: 12
  bibliographic_anchor_only_count: 0
  Consistency check: verified_short_quote_count (0) = actual_text_read_count (0) + user_supplied_excerpt_count (0) ✅

page_level_anchor_count (v5 NEW): 0
  No page numbers; no figure-number guesses included in this retrofit (kept consistent with v6 prompt's honest under-anchoring discipline).

hallucination_risk_self_assessment (v5 introduced, v6 R2 refined): medium
  12 of 12 V4-Q items carry paraphrased textbook_canonical_claim entries. No verified_short_quote items. Verification burden is per-item; spot-check execution for kumada1972 (Crabtree/Hartwig direct lookup or WebSearch triangulation on organometallic primary literature) is queued as separate work.

paper_inference_tier_distribution (v6 R7 NEW):
  T1_paper_explicit_count: 7 (V4-Q1, V4-Q2, V4-Q3, V4-Q4, V4-Q9, V4-Q10, V4-Q12)
  T2_paper_grounded_inference_count: 5 (V4-Q5, V4-Q6, V4-Q7, V4-Q8, V4-Q11)
  T3_paper_external_inference_count: 0
  — Compare to boyer1973: T1=3, T2=6, T3=0. kumada1972 has higher T1 share (7/12=58% vs 3/9=33%), reflecting the paper's specific quantitative claims (equations, ligand orders, Table I) that allow direct paper-side anchoring vs boyer1973's more interpretive content.

textbook_verification_status_distribution (v6 R7 NEW):
  textbook_directly_verified_count: 0
  primary_literature_corroborated_count: 0
  memory_based_unverified_count: 12
  bibliographic_anchor_only_count: 0
  — Compare to boyer1973: 0 / 3 / 6 / 0. Boyer1973 has 3 spot-checked items (V4-Q4/Q8/Q9 via WebSearch); kumada1972 has 0 spot-checked this session. This is a known difference reflecting the scope decision to defer kumada1972 factual verification.

cross_axis_independence_check (v6 R7 NEW):
  — Combinations populated in this paper:
    - T1_paper_explicit + memory_based_unverified: 7 items (V4-Q1, Q2, Q3, Q4, Q9, Q10, Q12)
    - T2_paper_grounded_inference + memory_based_unverified: 5 items (V4-Q5, Q6, Q7, Q8, Q11)
  — Note: only 2 of the 4 possible R7 combinations are populated here, because no items have textbook_directly_verified or primary_literature_corroborated status. This is a consequence of the scope constraint (no spot-check), not a schema-operability failure. The 4-combination independence was already demonstrated at boyer1973; kumada1972 confirms that the schema accepts items at the T1+unverified and T2+unverified positions without conflict.

trigger_relation_distribution (v6 NEW):
  omission_count: 3 (V4-Q1 primary, V4-Q10 primary, V4-Q11 primary)
  mismatch_count: 1 (V4-Q2 primary)
  under_specification_count: 3 (V4-Q3 primary, V4-Q9 primary, V4-Q12 primary)
  later_resolution_count: 4 (V4-Q5, V4-Q6, V4-Q7, V4-Q8 — all primary)
  terminology_shift_count: 0 primary (V4-Q7 secondary)
  mechanism_gap_count: 1 (V4-Q4 primary)
  other_count: 0
  total_primary: 12 (all natural primary_type, no "other") — promotion criterion (a) PASSES at 12/12 (100%, exceeds ≥ceil(0.8·12) = 10 threshold)
  — Compare to boyer1973: omission ×2, under-spec ×4, later-res ×3 = 9 total. kumada1972 distribution is more spread (5 different primary types used vs boyer1973's 3). This is consistent with kumada1972's richer mechanistic content (12 V4-Q items spanning catalytic cycle, ligand effects, stereochemistry, transmetalation).

secondary_trigger_count (v6 NEW): 4 items with secondary_type (V4-Q1, V4-Q2, V4-Q3, V4-Q4, V4-Q7). Boyer1973 had 5; kumada1972 has 4 — comparable rate.

trigger_subtype_inventory (v6 NEW):
  - "paradigm-omission" (V4-Q8): paper omits paradigm framing (OA-TM-RE cycle as cross-coupling prototype)
  Total subtype entries: 1. Same single subtype as boyer1973's V4-Q4 (PMF paradigm-omission). The "paradigm-omission" subtype reappears in a different domain (organometallic vs biochemistry), suggesting it may be a generalizable subtype across domains.

anachronism_status_distribution (v6 NEW):
  contemporary_plausible_count: 4 (V4-Q2, V4-Q9, V4-Q10, V4-Q12)
  retrospective_only_count: 5 (V4-Q3, V4-Q5, V4-Q6, V4-Q7, V4-Q8)
  uncertain_count: 3 (V4-Q1, V4-Q4, V4-Q11)
  — Compare to boyer1973: 1 / 6 / 2. kumada1972 has more contemporary-plausible items (4 vs 1), reflecting that some questions (canonical reductive elimination, β-H kinetics, OA reactivity order) were canonical in 1972 organometallic literature even though the textbook resolution of the full Kumada cycle came later.

anachronism_typology_independence_check (v6 NEW):
  — Looking for cases where gap_type ↔ anachronism_status pairing contradicts the heuristic:
    - V4-Q3 (G2, retrospective-only): G2 typically contemporary-plausible per heuristic; this is retrospective-only because bite angle concept postdates 1972. EMPIRICAL: G2 can be retrospective-only when the "condition" being unspecified is itself a post-paper concept.
    - V4-Q4 (G4, uncertain): G4 typically polymorphic per boyer1973 confirmation; this kumada1972 G4 is "uncertain" (radical-chain and bis-alkyl pathways both contested in 1972).
    - V4-Q9 (G2, contemporary-plausible): aligns with heuristic.
    - V4-Q11 (G1, uncertain): G1 typically contemporary-plausible per heuristic; this is uncertain (transmetalation TS mechanism not fully resolved in 1972). Same finding as boyer1973's anachronism × gap_type independence.
    - V4-Q5 through V4-Q8 (G7, retrospective-only): all 4 G7 items align with heuristic G7=retrospective-only.
  — Conclusion: anachronism × gap_type independence STRONGLY CONFIRMED at kumada1972 (n=12). Multiple cases where G2 / G1 / G4 → retrospective-only or uncertain rather than the heuristic contemporary-plausible. v6 design principle (anachronism = item-level, not type-level) is empirically validated cross-paper.

rationale_quality_self_check (v6 NEW):
  stance.rationale: 12 substantive, 0 templated, 0 boilerplate (each rationale cites specific V1/V2/V3 contrast for THIS item)
  trigger_relation.explanation: 12 substantive, 0 templated, 0 boilerplate (each explanation cites paper-specific quote and textbook-specific position)
  anachronism_status.rationale: 12 substantive, 0 templated, 0 boilerplate (each rationale cites specific historical knowledge state)
  — Promotion criterion (d) PASSES at 12/12 across all three rationale fields (well above ≥ceil(0.8·12) = 10 threshold). Self-assessed; human review recommended.

gap_type_vs_trigger_relation_independence (v6 NEW):
  (a) Same gap_type with DIFFERENT trigger_relation primary_types:
    - G7 appears with later-resolution (V4-Q5, Q6, Q7, Q8) — 1 trigger type, but 4 instances at different mechanistic depth
    - G1 appears with omission (V4-Q1, Q10, Q11) — 1 trigger type, but with varied secondary_type (Q1 later-resolution secondary; Q10/Q11 no secondary)
    - G2 appears with under-specification only (V4-Q3, V4-Q9) — 1 trigger type
    — Note: kumada1972 shows LESS within-gap-type primary trigger variation than boyer1973 (where G4 spanned 3 trigger types). This is consistent with kumada1972's tighter gap_type ↔ trigger_relation mapping.
  (b) Same trigger_relation with DIFFERENT gap_types:
    - under-specification appears with G2 (V4-Q3, Q9), G5 (V4-Q12) — 2 different gap_types ✅
    - later-resolution appears with G7 (V4-Q5, Q6, Q7, Q8) only
    - omission appears with G1 (V4-Q1, Q10, Q11) only
    — Limited cross-axis variation on this paper; only under-specification spans multiple gap_types.
  — Conclusion: Cross-axis multi-valence is OBSERVED but LESS PRONOUNCED at kumada1972 than at boyer1973. The schema still satisfies promotion criterion (c) at n=2 (≥1 cross-axis multi-valence case). The paper-level variation in cross-axis density is itself an interesting empirical observation: paradigm-initiating papers (kumada1972, G7-heavy) may have tighter gap_type ↔ trigger_relation correlation than peripheral foundational papers (boyer1973, more polysemous G4).

anticipates_canonical_count: 3 (V4-Q5, V4-Q7, V4-Q8 — paradigm-initiating paper signal)

g7_count: 4 (strict 3 = V4-Q5/Q6/Q7; inclusive 4 includes V4-Q8 paradigm-omission)
g7_boundary_count: 0

---

--- V6 cross-paper outcome summary ---

Promotion criterion (a) trigger_relation applicability:
  Required: ≥ceil(0.8·12) = 10 V4-Q items with natural primary_type, substantive explanation.
  Observed: 12/12 natural primary_type, 12/12 substantive explanation (self-assessed).
  **PASS at kumada1972** (also PASS at boyer1973). Cross-paper consistency confirmed.

Promotion criterion (b) anachronism_status natural distribution:
  Required: natural mix across 3 values; item-level rationale, not auto-inferred from gap_type.
  Observed: 4 contemporary-plausible / 5 retrospective-only / 3 uncertain. All values populated, item-specific rationale.
  Cross-paper comparison: boyer1973 (1/6/2), kumada1972 (4/5/3). The distributions differ — kumada1972 has more contemporary-plausible items, reflecting that some organometallic concepts (canonical reductive elimination, β-H elimination kinetics) were textbook-canonical in 1972 while corresponding biochemistry concepts (chemiosmotic theory acceptance) were still contested.
  **PASS at kumada1972, with cross-paper distribution variation observed as feature, not bug.**

Promotion criterion (c) gap_type vs trigger_relation independence:
  Required: ≥1 cross-axis multi-valence case.
  Observed: under-specification spans G2 + G5 (2 gap_types). Less rich than boyer1973 (G4 spanned 3 trigger types), but ≥1 threshold met.
  **PASS at kumada1972** (also PASS at boyer1973). Cross-paper finding: paradigm-initiating papers (G7-heavy) may have tighter gap_type ↔ trigger_relation correlation than peripheral foundational papers — an empirical observation worth recording but not a schema operability problem.

Promotion criterion (d) rationale quality:
  Required: ≥ceil(0.8·12) = 10 items rated substantive across all three rationale fields.
  Observed (self-assessed): 12/12 substantive, 0/12 boilerplate per field.
  **PASS at kumada1972** (also PASS at boyer1973).

Promotion criterion (e) textbook-canonical accuracy:
  At kumada1972: **NOT SPOT-CHECKED** this session. All 12 items remain textbook_verification_status=memory_based_unverified. Spot-check execution for organometallic claims (Ni(0)/Ni(II) cycle, bite angle, OA reactivity order, transmetalation TS) is queued as separate work — analogous to boyer1973's spot-check that elevated 3 items to primary_literature_corroborated.
  **PARTIAL across the two-paper corpus**: 3/9 spot-checked at boyer1973 (PASS) + 0/12 at kumada1972 (deferred). Cross-paper criterion (e) requires either user-side Lehninger+Crabtree direct lookup OR additional WebSearch triangulation rounds.

---

--- Cross-paper v6 schema operability conclusion ---

The v6 R7 schema (stance + trigger_relation + anachronism_status + textbook_access_mode + paper_inference_tier + textbook_verification_status) populates naturally on kumada1972's 12 V4-Q items and 5 V4-OV overlaps WITHOUT requiring paper-specific refactoring. All 12 items naturally accept primary_type assignment (0 "other" branch usage); all 12 anachronism_status values have item-level rationale; all 12 paper_inference_tier values map from the legacy unified inference_tier; all 12 textbook_verification_status values are honestly reported as memory_based_unverified.

Cross-paper differences observed:
- gap_type distribution: boyer1973 G4-dominant (3/9) vs kumada1972 G7-dominant (4/12)
- trigger_relation primary distribution: boyer1973 under-specification dominant (4/9) vs kumada1972 later-resolution dominant (4/12)
- anachronism distribution: boyer1973 6/9 retrospective-only vs kumada1972 5/12 retrospective-only (kumada1972 has more contemporary-plausible items)
- paper_inference_tier: boyer1973 T1=3/9 vs kumada1972 T1=7/12

These differences are paper-property differences, not schema differences. The schema is the same; the schema reports the differences faithfully.

Conclusion: **v6 R7 schema is cross-paper operable at n=2** (boyer1973 + kumada1972). Combined with the boyer1973 spot-check (criterion (e) PASS for 3 items), this supports the cautious framing that **v6 has passed cross-paper schema operability test** while **production confirmation requires (i) cross-paper spot-check completion AND (ii) optional Lehninger+Crabtree direct lookup as final layer**.

Cross-references:
  prompts/v184/prompt_stage1_turn4_canonical_textbook_v184_pilot_v6.md (1048 lines)
  papers/sandbox/38_boyer1973/boyer1973_v184_sonnet_s1_v4pilot_v6_20260528.md (671 lines)
  papers/dev/kumada/kumada_v184_sonnet_s1_v4pilot_v3_20260527.md (v4 baseline)
  improvements/v4_pilot_spotcheck_boyer1973_v6_20260528.md (criterion (e) memo)
  memory/project_uqs_textbook_corpus_aspirational.md (memory update 2026-05-28)

================================================================================
== V7 RE-CLASSIFICATION APPENDIX (2026-05-28, post user-side Crabtree PDF verification) ==
================================================================================

STATUS: This v6 pilot's textbook-citation layer is SUPERSEDED by v7
discipline. The conceptual gap-detection layer (the 12 V4-Q questions
themselves) is retained, but the textbook anchors are re-classified below
using the v7 schema (external_anchor_relation + anchor_existence incl
wrong_context + claim_fidelity) and GPT's 4-category verification framework
(verified_present/partial/wrong_context/absent). Source of verification:
USER direct examination of the actual Crabtree 7th ed. Ch.9 PDF (term/section
search), 2026-05-28.

PROMOTION JUDGMENT (GPT-aligned): v6 schema operability PASS; v6 factual
anchoring reliability under memory-based mode FAIL; v6 production HOLD.

--- Verified items (n=4; user-supplied actual-text verification) ---

V4-Q1 (Ni active catalyst missing step):
  original textbook_reference (v6): "Crabtree Ch.9 'Kumada Coupling' section"
  textbook_access_mode (v7): actual_text_read (user-verified against Crabtree Ch.9 PDF)
  verification verdict (GPT 4-cat): verified_absent
  v7 anchor_existence: disconfirmed
    — Crabtree Ch.9 is titled "Homogeneous Catalysis"; no "Kumada Coupling"
      section exists; search for Kumada/Grignard/RMgX/Ni(0)/Ni(II) = 0 hits
  v7 external_anchor_relation: field_synthesis (the Ni(0)/Ni(II) canonical
    cycle is modern field canon synthesized across sources; NOT a Crabtree
    Ch.9 statement) — possibly generic_textbook_template if extrapolated from
    the §9.7 Pd cycle
  v7 claim_fidelity: not_applicable (anchor disconfirmed)
  V4 frame (v7 CHANGE 10): V5 (retrospective field-canon reader), NOT strict V4a
  diction correction (v7 CHANGE 7): "the textbook presents Ni(0)/Ni(II) as
    canonical" → "Modern field canon treats Ni(0)/Ni(II) as the resolved cycle;
    this is NOT directly stated in Crabtree Ch.9 (which presents the Pd cycle).
    Requires verification against Hartwig Ch.18 for a direct Ni statement."
  rescue path: if Hartwig Ch.18 directly states the Ni(0)/Ni(II) Kumada cycle,
    Q1 becomes direct_textbook_statement (V4a) anchored on Hartwig, with Crabtree
    dropped from textbook_reference.

V4-Q5 (Ni canonical OA-TM-RE cycle):
  original textbook_reference (v6): "Hartwig Ch.18 §18.1; Crabtree Ch.9 (canonical Ni(0)/Ni(II) OA-TM-RE cycle)"
  textbook_access_mode (v7): actual_text_read (Crabtree portion user-verified; Hartwig portion still unverified)
  verification verdict (GPT 4-cat): verified_wrong_context (Crabtree portion)
  v7 anchor_existence: wrong_context
    — Crabtree §9.7 presents the Pd(0)/Pd(II) cross-coupling cycle (right
      concept: cross-coupling cycle; wrong system: Pd not Ni); "transmetalation"
      term never appears; Ni cycle is reader extrapolation from the Pd template
  v7 external_anchor_relation: generic_textbook_template (Pd cross-coupling
    cycle → Ni Kumada extrapolation)
  v7 claim_fidelity: not_applicable (Ni-specific claim not in the cited text)
  V4 frame: V4b (textbook-enabled analogical reader)
  diction correction: "Crabtree Ch.9 presents the canonical Ni(0)/Ni(II) cycle"
    → "Crabtree §9.7 presents the canonical Pd(0)/Pd(II) cross-coupling cycle;
    a reader may extrapolate the same OA-(replacement)-RE template to Ni Kumada.
    The Ni-specific cycle requires verification against Hartwig Ch.18."
  textbook_reference refactor (Option α): drop Crabtree, keep "Hartwig Ch.18
    §18.1" only, mark Hartwig unverified pending separate check.

V4-Q7 (bite angle for Ni Kumada):
  original textbook_reference (v6): "Crabtree Ch.9 §9.4 (bite angle effects in Ni cross-coupling)"
  textbook_access_mode (v7): actual_text_read (user-verified)
  verification verdict (GPT 4-cat): verified_wrong_context
  v7 anchor_existence: wrong_context
    — Crabtree §9.4 IS "Alkene Hydroformylation"; bite-angle→RE principle IS
      stated BUT for Rh hydroformylation with BISBI ligand (right concept:
      bite-angle→RE; wrong system: Rh hydroformylation not Ni coupling); "dpe"
      appears at p.11 in a Rh Schrock-Osborn asymmetric-hydrogenation context
  v7 external_anchor_relation: cross_system_extrapolation (Rh hydroformylation
    bite-angle principle → Ni coupling transfer)
  v7 claim_fidelity: not_applicable (Ni-coupling bite-angle claim not in cited text);
    the GENERAL bite-angle→RE principle is present (could be cited as a
    general-principle anchor at partial level)
  V4 frame: V4b (textbook-enabled analogical reader)
  diction correction: "Crabtree §9.4 treats bite angle in Ni cross-coupling"
    → "Crabtree §9.4 (Alkene Hydroformylation) states the general principle that
    larger bite angle facilitates reductive elimination, for Rh/BISBI. A reader
    may transfer this principle to Ni coupling; the Ni-specific bite-angle
    application and the '~85° benchmark Ni ligand' claim are NOT in Crabtree."

V4-Q12 (catalyst-loading reporting format):
  original textbook_reference (v6): "Crabtree Ch.9 + Hartwig Ch.18 (TON/TOF reporting norm)"
  textbook_access_mode (v7): actual_text_read (Crabtree portion user-verified)
  verification verdict (GPT 4-cat): verified_partial
  v7 anchor_existence: partial (GPT correction #3, 2026-05-28: NOT `confirmed`)
    — the TON/TOF framework + condition-statement norm ARE in Crabtree §9.1
      Kinetics, p.4-5 ("The TON and TOF depend on the conditions, which must
      therefore be stated"), BUT the V4-Q12 claim slides beyond what the text
      supports. `partial` (not `confirmed`) is used deliberately: `confirmed`
      would risk the reader misreading "the textbook claim was correct" when
      in fact the original claim over-slides. The framework is present; the
      specific normative claim is not.
  v7 external_anchor_relation: direct_textbook_statement (for the TON/TOF
    framework) — the only one of the 4 items with a genuine direct anchor
  v7 claim_fidelity: over_slides
    — over-claim 1: "mol% per-entry is textbook standard" — Crabtree mixes
      ppm/%/ratio, does not mandate mol%
    — over-claim 2: "range notation is non-standard" — Crabtree itself uses
      "1 ppm to 1%" range
    — over-claim 3: "prevents TON calculation" — should be "permits only
      order-of-magnitude TON estimate"
  V4 frame: V4a_with_correction (strict / direct textbook reader, but claim
    requires weakening per claim_fidelity=over_slides)
  claim correction: "non-standard format prevents TON calculation" →
    "the range format permits only an order-of-magnitude TON estimate, not
    entry-specific TON comparison"

--- Summary: v7 re-classification of kumada1972 verified items ---

| Item | GPT 4-cat verdict | v7 anchor_existence | v7 external_anchor_relation | v7 claim_fidelity | V4 frame |
|------|-------------------|---------------------|------------------------------|-------------------|----------|
| Q1 | verified_absent | disconfirmed | field_synthesis | n/a | V5 |
| Q5 | verified_wrong_context | wrong_context | generic_textbook_template | n/a | V4b |
| Q7 | verified_wrong_context | wrong_context | cross_system_extrapolation | n/a | V4b |
| Q12 | verified_partial | partial | direct_textbook_statement | over_slides | V4a_with_correction |

Key finding (SCOPE-LIMITED per GPT correction #2, 2026-05-28): **In the four
Crabtree-checked Kumada items, no item survives as a fully faithful
direct-textbook anchor without qualification.** Q12 is the closest to
strict-V4a (the TON/TOF framework is a genuine direct anchor) but its claim
over_slides; Q5/Q7 are V4b (analogical: Pd→Ni, Rh→Ni); Q1 is V5 (field
synthesis). This is the empirical basis for the v7 access-discipline + the
V4a/V4b/V5 frame split.
  IMPORTANT SCOPE LIMITS:
  - This "0 faithful" finding applies to THESE FOUR Crabtree-checked Kumada
    items ONLY. It is NOT generalized to the n=11 baseline or to V4 in general.
  - The unreliability is specific to the **memory_based_anchor** generation
    mode. It does NOT negate V4 under actual_text_read conditions, which v7 is
    designed to enable (and which has not yet been piloted).
The remaining 8 V4-Q items (Q2/Q3/Q4/Q6/Q8/Q9/Q10/Q11) are NOT yet verified
and carry access_mode=concept_level_no_citation pending user Crabtree/Hartwig
verification (triage checklist queued).

---

> **Tier 8 redaction notice**: This file is a redacted copy of the corresponding Tier 3 / Tier 9 output. Verbatim source-paper quotations have been replaced by `[REDACTED: see source paper §<loc>; full text retained in Tier 9 reviewer-only deposit]` markers, preserving location references and our own analytical content. Bibliographic fields (title, authors, journal, year, DOI), analytical labels (`evidence_chain:` with B-/U-/A-/C- internal IDs), short technical terms, and our own analytical text are not redacted. The redaction was applied by `scripts/redact_for_tier8.py` and, for this version, by `scripts/build_paperA_R1_public.py` with `scripts/redact_source_ngram_runs.py` (scripts of the project repository; they are not deposited).
