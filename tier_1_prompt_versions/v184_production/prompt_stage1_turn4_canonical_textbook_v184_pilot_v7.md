# Stage 1 — V4 (PILOT v7): Agent V4 (Canonical-textbook reader / textbook-equipped reader) — ACTUAL-ACCESS textbook anchoring
<!-- prompt_version: stage1-v184-20260528_v4pilot_v7 -->
<!-- File lineage: prompt_stage1_turn4_naive_textbook_v184_pilot_v[1..5].md → _canonical_textbook_v184_pilot_v6.md → _v7.md -->
<!-- Status: PILOT v7 — ACTUAL-ACCESS textbook anchoring discipline. Paradigm shift from v6: memory-based specific textbook citation is PROHIBITED. Specific textbook citations (chapter title / section name / page / named content) are permitted ONLY when the textbook content was actually accessed this session (actual_text_read via Read tool OR user_supplied_excerpt). Without access, V4 stays at concept level and names NO specific textbook location. -->
<!-- FREEZE STATE (2026-05-28, session arc close): schema conceptually closed. NO further fields should be added before an actual-access pilot. Conclusion: memory-based textbook anchoring is unsuitable for production citation claims; V4 must use generation/verification separation with a specified accessible textbook corpus. Conceptual question generation remains valuable; citation/provenance layer remains HOLD until actual-access validation. NEXT: actual-access 1-paper pilot using a Crabtree-Ch9-covered topic (hydrogenation / hydroformylation / Pd coupling / etc.) + supplied Crabtree partial PDF as Stage-B corpus — NOT kumada (Ni Kumada absent from Crabtree Ch.9). Hartwig (library) needed for kumada Q1/Q5 rescue. -->
<!-- Core design principle (v6, RETAINED): A question is "ある読者立場が、ある論文箇所を、ある外部規範と照合したときに発生する、再検証可能な認識イベント." v6 preserves the GENESIS (paper_anchor × stance × external_anchor × trigger_relation → question). -->
<!-- Core design principle (v7, NEW): The textbook anchor must be REAL, not recalled. Memory-based textbook citation produces systematically confabulated anchors (empirically confirmed: see v6→v7 rationale). A "textbook-equipped reader" who has NOT actually read the cited textbook location is not equipped — it is guessing. v7 enforces that the textbook anchor's specificity never exceeds the access actually obtained. -->
<!-- v6→v7 changes (2026-05-28, ACTUAL-ACCESS discipline; user Option 1 decision after kumada1972 verification sweep):
     RATIONALE: User-side direct verification of the kumada1972 v6 pilot against the actual Crabtree textbook PDF (n=4 items: V4-Q1 / V4-Q5 / V4-Q7 / V4-Q12) revealed systematic memory-based citation confabulation reaching the TABLE-OF-CONTENTS level:
       - V4-Q1: cited "Crabtree Ch.9 'Kumada Coupling' section" — no such section exists; Ch.9 is titled "Homogeneous Catalysis"; §9.7 "Coupling Reactions" covers Pd reactions only, never names Kumada
       - V4-Q5: cited "Crabtree Ch.9 canonical Ni(0)/Ni(II) OA-TM-RE cycle" — Ch.9 presents the Pd(0)/Pd(II) cycle only; "transmetalation" term never appears; Ni cycle is reader extrapolation from the Pd template
       - V4-Q7: cited "Crabtree §9.4 bite angle in Ni cross-coupling" — §9.4 is "Alkene Hydroformylation" (Rh/BISBI); the Ni-Kumada bite-angle application is absent; "dpe" appears only in a Rh Schrock-Osborn asymmetric-hydrogenation context (p.11)
       - V4-Q12: cited "Crabtree Ch.9 TON/TOF reporting norm" — partially correct (TON/TOF framework IS in §9.1 Kinetics p.4-5) BUT the claim over-slides (textbook mixes ppm/%/ratio, does not mandate mol%; TON defined as cycles-before-deactivation, not moles-product/moles-cat; range notation is used by the textbook itself)
     PATTERN: 3 of 4 (Q1/Q5/Q7) were citation hallucinations confabulated at chapter-title / section-name / section-content levels; 1 of 4 (Q12) had a real anchor but a claim that over-slides the textbook. NOT A SINGLE verified item had claim_fidelity=faithful. The memory-based anchor mode is systematically unreliable for specific citation.
     CHANGE (1): textbook_access_mode value `memory_based_anchor` is RENAMED/RECONCEIVED as `concept_level_no_citation`. Under this mode, NO specific textbook location (chapter title, section name/number, page, figure, named content) may be cited. The canonical knowledge may be referenced only at concept level, explicitly framed as "the model's representation of canonical knowledge as generally taught", NOT as a textbook citation.
     CHANGE (2): Specific textbook citation (chapter/section/page/named content + paraphrased or verbatim canonical_claim attributable to a location) is PERMITTED ONLY when textbook_access_mode ∈ {actual_text_read, user_supplied_excerpt}. The Read tool must have read the textbook PDF/excerpt this session, OR the user must have supplied the excerpt in the conversation.
     CHANGE (3): `bibliographic_anchor_only` retained — a bare bibliographic citation ("Crabtree, The Organometallic Chemistry of the Transition Metals, 7th ed.") with NO chapter/section/content claim is permitted without access, because it makes no verifiable content claim beyond the book's existence.
     CHANGE (4): Verification fields consolidated into a 3-part `textbook_verification` block, applicable ONLY when access_mode ∈ {actual_text_read, user_supplied_excerpt}: anchor_existence {confirmed | partial | disconfirmed} × claim_fidelity {faithful | over_slides | under_states} × inference_tier {T1_textbook_explicit | T2_textbook_grounded_extrapolation | T3_textbook_external_extrapolation}. This absorbs the v6-R7/R8 proposals and the kumada1972 + boyer1973 empirical outcome categories (disconfirmed anchor / partial anchor + over-slide / confirmed anchor + over-slide / confirmed + faithful).
     CHANGE (5): textbook_access_mode value `primary_literature_triangulation` ADDED — when the canonical claim is corroborated via WebSearch on the textbook's underlying primary literature (e.g., Mitchell 1961 for PMF, Noji 1997 for γ-rotation) but the textbook itself was not read. This is an intermediate tier: stronger than concept_level_no_citation, weaker than actual_text_read. It permits a citation to the PRIMARY LITERATURE (not the textbook section), with the canonical claim framed as "corroborated by the textbook's cited primary source".
     CHANGE (6): The n=11 v3 baseline pilots and the v5/v6 boyer1973 + kumada1972 pilots were all generated under the memory-based-allowed paradigm. Their CONCEPTUAL gap-detection layer (the 「綻び」 typology questions themselves) may survive, but their TEXTBOOK-CITATION layer is now considered unreliable and requires regeneration under v7 discipline (actual access) before any specific textbook citation from those pilots is used in a manuscript.
     --- GPT review fold-in (2026-05-28, second-opinion review of the kumada1972 verification sweep; folded into v7 same-day, pre-pilot) ---
     CHANGE (7) [DICTION RULE — GPT fix #1, "最重要"]: Under access_mode = concept_level_no_citation, verified-assertion DICTION is PROHIBITED, not only specific citation. The access gate (CHANGE 1-2) blocks naming a section; CHANGE 7 additionally blocks the verified-sounding PHRASING that made the kumada1972 outputs read as established textbook claims despite the memory_based flag. PROHIBITED phrasings under concept_level: "The textbook presents X", "Crabtree Ch.9 states", "The textbook resolves this as", "the canonical textbook description is". PERMITTED phrasings: "A possible textbook-side expectation is...", "A reader may extrapolate from the textbook's [related-system] template to [paper's system]...", "This canonical-knowledge claim requires verification against [named source]...". Rationale: even without a specific section number, "the textbook presents Ni(0)/Ni(II) as canonical" asserts a verified textbook claim. The diction must mark the epistemic status (expectation / extrapolation / requires-verification), not assert.
     CHANGE (8) [external_anchor_relation — GPT fix #2]: NEW field replacing the under-resolved inference_tier (T1/T2/T3) with a relation-KIND taxonomy that is more diagnostic of the failure mode:
         external_anchor_relation:
           value: direct_textbook_statement | generic_textbook_template | cross_system_extrapolation | field_synthesis | unsupported
             # direct_textbook_statement   = the textbook directly states this for the paper's specific system (requires actual access to assert)
             # generic_textbook_template   = the textbook states a GENERAL template (e.g., Pd cross-coupling cycle) that the reader applies to the paper's system (e.g., Ni Kumada); the template is real, the specific application is reader-supplied
             # cross_system_extrapolation  = the textbook states the principle for a DIFFERENT system/context (e.g., Rh hydroformylation bite-angle) that the reader transfers to the paper's system (e.g., Ni coupling); transfer is reader-supplied
             # field_synthesis             = the claim combines textbook + reviews + primary literature into a modern field-canon not stated verbatim in any single textbook location
             # unsupported                 = no textbook basis identified (neither direct, template, cross-system, nor synthesis)
           rationale: MANDATORY free text — which of the three sources (textbook-text / field-canon / reader-extrapolation) the claim draws on, and how they were (or were not) separated.
         This field forces the separation of (1) what the textbook literally says, (2) modern field canon, (3) reader extrapolation — the three things the kumada1972 failure compressed into one textbook_canonical_claim.
     CHANGE (9) [verification states — GPT fix #3]: anchor_existence value set EXTENDED with `verified_wrong_context`. Full set: confirmed | partial | wrong_context | disconfirmed | not_applicable.
         # verified_wrong_context = the cited location EXISTS and discusses the relevant CONCEPT, but in a different system/context than claimed (e.g., Crabtree §9.4 discusses bite-angle→RE but for Rh hydroformylation/BISBI, NOT Ni cross-coupling/dpe). Distinct from `partial` (general principle, right domain) and `disconfirmed` (absent entirely).
         claim_fidelity (over_slides / faithful / under_states) RETAINED as the orthogonal second axis (V4-Q12 case: anchor confirmed/partial BUT claim over_slides). GPT's single-enum {verified_present/partial/wrong_context/absent} maps onto anchor_existence; claim_fidelity is kept separate to preserve the over_slides dimension.
         Empirical mapping (kumada1972 sweep): Q1/Q5 → disconfirmed (or wrong_context: Pd-cycle present, Ni-claim absent) ; Q7 → wrong_context (Rh-hydroformylation bite-angle present, Ni-coupling claim absent) ; Q12 → confirmed + over_slides (TON/TOF present, mol%-mandate claim over-states).
     CHANGE (10) [V4 frame split — GPT fix #4; DESIGN DIRECTION, not yet hard-coded]: The kumada1972 failure shows that "textbook-equipped reader" conflates three distinct reader frames that should be separated in Paper E2 design:
         - V4a (strict / direct textbook reader): gaps between paper and knowledge DIRECTLY stated in textbook text (external_anchor_relation = direct_textbook_statement only). The only frame whose textbook anchors are verifiable as textbook citations.
         - V4b (textbook-enabled analogical reader): gaps surfaced by extrapolating textbook templates/principles to the paper's system (external_anchor_relation = generic_textbook_template | cross_system_extrapolation). Kumada Q5/Q7 belong here, NOT in strict V4.
         - V5 (retrospective field-canon reader): gaps against modern field canon synthesized from textbook + reviews + primary literature (external_anchor_relation = field_synthesis). Kumada Q1 (Ni(0)/Ni(II) as modern canon) may belong here.
         v7 does NOT yet hard-split the prompt into V4a/V4b/V5; it ADDS external_anchor_relation so that each question is TAGGED with its frame, enabling the split to be drawn analytically downstream (and in Paper E2).
     CHANGE (11) [PROMOTION JUDGMENT — GPT]: v6/v7 production promotion is HOLD, not "supported-pending-spot-check". Honest status:
         - schema operability: PASS (cross-paper boyer1973 + kumada1972)
         - factual anchoring reliability under memory-based/concept-level mode: FAIL (in the 4 Crabtree-checked Kumada items: 3 citation hallucinations + 1 over-slide; no fully faithful direct-textbook anchor without qualification — finding scope-limited to these 4 items, NOT generalized to n=11 baseline or V4 in general)
         - production promotion: HOLD until v7 actual-access discipline demonstrates ≥1 confirmed+faithful anchor on a paper with real textbook access
       Design motto (GPT): "V4 should not merely cite textbooks; it must preserve the epistemic path from textbook text to question."
     CHANGE (12) [CATEGORY-ERROR REFRAMING + GENERATION/VERIFICATION SEPARATION — GPT deep diagnosis, 2026-05-28]: The deepest design correction. Asking the model "where in the textbook you were TRAINED ON is the basis for this question?" is a CATEGORY ERROR — the model has no source-attributable memory of its training documents. Under that framing the model does NOT retrieve a source; it performs PLAUSIBLE SOURCE RECONSTRUCTION (post-hoc confabulation of a citation that would justify the question). The kumada1972 "Crabtree Ch.9 Kumada Coupling section" was not a faulty memory — it was a confabulated justification.
         CORRECTED FRAMING: V4 must NOT ask the model to attribute its question to "the textbook it was trained on". Instead, V4 separates two distinct objects that v6 conflated:
           (i) the model's INTERNAL canonical knowledge — used to GENERATE the question; unauditable; introspective source attribution is impossible; expressed only at concept level (access_mode = concept_level_no_citation), with epistemic-status-marking diction (CHANGE 7).
           (ii) an EXTERNAL, PRE-SPECIFIED, ACTUALLY-ACCESSIBLE textbook corpus — used to VERIFY the question; auditable; the ONLY thing a specific textbook citation may be anchored to (access_mode = actual_text_read / user_supplied_excerpt).
         GENERATION/VERIFICATION SEPARATION (V4 as a 2-stage pipeline):
           Stage A (generation): textbook-equipped reader generates questions + concept-level canonical-knowledge claims; NO specific textbook citation; access_mode = concept_level_no_citation.
           Stage B (verification): each canonical-knowledge claim is checked against the specified accessible corpus → anchor_existence {confirmed | partial | wrong_context | disconfirmed} + claim_fidelity. A specific textbook citation is emitted ONLY for claims that pass Stage B under actual access.
         This formalizes what the kumada1972 manual verification did. The "specified accessible corpus" is NOT "what the model was trained on" — it is what the project has DECIDED is the canonical reference AND can actually open and check.
     CHANGE (13) [claim_fidelity ENRICHED — GPT]: claim_fidelity value set extended from {faithful | over_slides | under_states} to {faithful | over_slides | over_generalizes | wrong_system | under_states | unsupported}:
         # faithful        = claim accurately represents the verified textbook statement
         # over_slides     = claim asserts somewhat MORE than the text (stronger/more specific), same system
         # over_generalizes = claim generalizes the textbook statement beyond its stated scope/conditions
         # wrong_system    = claim transfers a statement true for system X to the paper's system Y (claim-level analogue of anchor_existence=wrong_context)
         # under_states    = claim asserts LESS than the textbook
         # unsupported     = no textbook support for the claim (typically paired with anchor_existence=disconfirmed)
       kumada mapping: Q12 = over_slides (mol% mandate, prevents-calculation overstate) ; Q5/Q7 = wrong_system (Pd→Ni, Rh→Ni transfer) at the claim level, complementing anchor_existence=wrong_context ; Q1 = unsupported (no Crabtree basis).
-->
<!-- v5→v6 changes (2026-05-28, anchor-genesis schema; user-confirmed via "問いの発生条件を保存する" core principle + 6-condition design constraints):
<!-- v5→v6 changes (2026-05-28, anchor-genesis schema; user-confirmed via "問いの発生条件を保存する" core principle + 6-condition design constraints):
     (1) NEW mandatory field stance (per V4-Q item): {frame: V4_canonical_textbook_reader (fixed for this prompt), rationale: one-sentence justification of why THIS frame, not V1/V2/V3, surfaces THIS question}. v5's global field_rationale (single header-level statement) is decomposed into item-level rationale to preserve per-question genesis.
     (2) NEW mandatory field trigger_relation (per V4-Q item):
         - primary_type: OPEN ENUM. Initial candidates: omission | mismatch | under-specification | later-resolution | terminology-shift | mechanism-gap | other. "other" branch MUST be paired with explicit subtype in free text.
         - secondary_type: OPTIONAL (single value or null). Used when a question is co-triggered by a second relation (e.g., omission + later-resolution on PMF for boyer1973-Q4-equivalent).
         - subtype: OPTIONAL free-text refinement. Used to capture paper-specific or frame-specific relation types not anticipated by the initial enum (e.g., "stoichiometry-mismatch", "direction-mismatch", "scale-mismatch", "assay-to-mechanism jump", "model-to-measurement mismatch").
         - explanation: MANDATORY free text, 1–3 sentences. Pattern: "Paper reports/omits X; external norm (named in external_anchor) would lead reader to expect Y; the relation between X and Y is Z." DO NOT use boilerplate; explanation must be paper-and-anchor-specific.
     (3) "naive textbook reader" / "naive outsider" / "first-principles reader" wording FULLY DEPRECATED across the prompt. New canonical phrasings:
         - Schema label: V4_canonical_textbook_reader
         - Body / discussion: textbook-equipped reader
         Rationale: "naive" wrongly implies shallow understanding; the canonical-textbook reader is a sophisticated reader equipped with explicit, codified, externally-auditable knowledge — NOT a beginner. Renaming aligns the schema with the actual epistemic operation.
     (4) NEW mandatory field anachronism_status (per V4-Q item):
         - value: contemporary-plausible | retrospective-only | uncertain
         - rationale: MANDATORY free text, 1–2 sentences. NOT auto-inferred from gap_type (e.g., G7 ≠ automatic retrospective-only; G1–G6 ≠ automatic contemporary-plausible). Each item must articulate WHY this question's plausibility hinges on post-paper knowledge stabilization (or does not).
     (5) Mapping table between gap_type (G1–G7) and trigger_relation is RETAINED but RELABELED as "diagnostic heuristic guide" — NOT a validation constraint. Schema validation MUST NOT enforce 1-to-1 mapping. The same G4 can manifest as mechanism-gap (boyer1973-Q4 PMF), terminology-shift (vocabulary evolved), or later-resolution (Noji 1997 settled it), and these are analytically distinct genesis paths even though they share the gap_type label.
     (6) Scope clarification: v6 modifies V4 (Turn 4 textbook-equipped reader) INTERNAL schema only. V1 (own-field expert) / V2 (adjacent-field) / V3 (methodology) prompts in prompts/v184/prompt_stage1_turn[1|2|3]_v184.md are UNCHANGED. V1–V3 unification into a parallel anchor-genesis schema is deferred to (a) v7 prompt revision OR (b) Stage 2 adapter schema that post-processes V1–V3 outputs into the v6 anchor-genesis structure. v6 does not break compatibility with v184 baseline V1–V3 production outputs.
     (7) v5 page-level anchor machinery (textbook_quote_status / textbook_canonical_claim / page_level_anchor) is FULLY RETAINED unchanged. v6 = additive extension on v5, not a replacement.
     (8) v6 promotion criteria (must demonstrate before v6 → production):
         - (a) trigger_relation applicability: ≥ceil(0.8·N) V4-Q items in pilot have natural primary_type (not "other"), AND explanation field contains paper-and-anchor-specific content (not boilerplate), where N = total V4-Q count in this pilot (typically 8–15)
         - (b) anachronism_status distribution: natural mix across contemporary-plausible / retrospective-only / uncertain (not collapsed to a single value); rationale field populated with substantive item-specific justification
         - (c) gap_type vs trigger_relation independence demonstrated: ≥1 G_i with multiple trigger_relation realizations OR ≥1 trigger_relation type with multiple G_i realizations (cross-axis multi-valence)
         - (d) v5 criteria (anchor granularity gain, hallucination surface, no v4 typology regression) preserved
-->
<!-- v6 in-place refinements (2026-05-28, pre-pilot; user-requested 6-item review fix):
     (R1) Body 「素人」 (Japanese for "naive / amateur") wording deleted from §"Pilot context (V4 design)". The structural-redefinition subsection is rewritten as "Textbook-equipped reader: structural definition" without using 「素人」. Rationale: v6 already renames "naive textbook reader" → "canonical-textbook reader (textbook-equipped reader)"; retaining 「素人」 in the body contradicts the rename. The structural content (knowledge type, not knowledge quantity; field-internal license vs no field-internal license; etc.) is preserved verbatim.
     (R2) textbook_quote_status enum value `from_memory_verbatim` is REPLACED by `verified_short_quote`. The new value is gated: usable ONLY when the user has supplied the textbook excerpt, OR the model has directly read a legally accessible textbook excerpt in the session. LLM-memory-based verbatim quotation is now PROHIBITED — it carries both confabulation risk and copyright risk, and v6's core focus is anchor + trigger_relation, not verbatim quotation. Header changelog mentions of `from_memory_verbatim` are retained as deprecation markers; all schema/output/self-eval mentions are updated to `verified_short_quote`.
     (R3) Section titles "V4 PILOT v3 self-evaluation" and "V4 PILOT v3 execution constraints" updated to "V4 PILOT v6 self-evaluation" and "V4 PILOT v6 execution constraints". These were v3-era residuals that survived v4/v5 updates; v6 cleans them up.
     (R4) Promotion criteria thresholds rewritten from `≥7/9` to `≥ceil(0.8·N)` (where N = total V4-Q count in this pilot). The previous fixed-9 baseline was inconsistent with the documented quantity target of 8–15 questions. The proportional threshold accommodates any N in [8, 15] uniformly.
     (R5) Overlap entries (V4-OV[N]) schema extended from `overlaps_with | gap_type | severity_V4 | note` to include the minimum v6 genesis metadata: `trigger_relation` (primary_type + explanation), `anachronism_status` (value + brief rationale), `textbook_reference`, and `stance_rationale` (one sentence on why textbook-equipped reader views the same question differently from the overlapping V1/V2/V3 question). Rationale: overlaps are the most important locus for frame-convergence analysis; reducing overlap entries to minimal metadata defeats the v6 design goal of preserving genesis.
     (R6) NEW mandatory field `textbook_access_mode` (per V4-Q item, and per V4-OV item where textbook anchor is invoked): one of {actual_text_read, user_supplied_excerpt, memory_based_anchor, bibliographic_anchor_only}. This is orthogonal to textbook_quote_status (which describes WHAT is rendered) — access_mode describes HOW the model accessed the textbook content. For the boyer1973 pilot starting state (no textbook PDF supplied, no excerpt provided), default is `memory_based_anchor` for all items; if the user later supplies a Lehninger excerpt or the model reads a textbook chapter via the Read tool, access_mode for affected items becomes `actual_text_read` or `user_supplied_excerpt` accordingly.
     (R7) Split `inference_tier` field into TWO separate fields (post-boyer1973 spot-check finding 2026-05-28): the prior unified `inference_tier` conflated two orthogonal epistemic axes — paper-side explicitness AND textbook-side verification status. Spot-check empirically confirmed that V4-Q items can have `T1_paper_explicit` paper-side (well-verified by direct paper read) AND `memory_based_unverified` textbook-side (LLM memory anchor not yet externally verified). The two axes are now separated:
         - `paper_inference_tier`: how directly the paper supports this question
           * `T1_paper_explicit`: paper directly states the relevant text
           * `T2_paper_grounded_inference`: follows from paper text in one inference step
           * `T3_paper_external_inference`: requires external knowledge beyond paper
         - `textbook_verification_status`: how verified the textbook canonical claim is at session time
           * `textbook_directly_verified`: textbook_access_mode = actual_text_read OR user_supplied_excerpt; the canonical claim has been directly checked against textbook
           * `primary_literature_corroborated`: textbook claim triangulated via WebSearch / open-access primary literature (the textbook references); weaker than direct textbook read but stronger than pure memory
           * `memory_based_unverified`: only LLM training-memory anchor; no external verification this session
           * `bibliographic_anchor_only`: chapter/section pointer only; no specific content claim made beyond the bibliographic level
         The two axes are independent. A V4-Q can be T1_paper_explicit + memory_based_unverified (paper text well-known, textbook claim unverified). A V4-Q can be T2_paper_grounded_inference + textbook_directly_verified (inference step needed from paper, but textbook claim verified). All four combinations are valid and each conveys distinct trust-calibration information.
-->
<!-- v4→v5 changes (2026-05-28, page-level anchor extension; user-requested via 「どの教科書の何の記述をもとに」 anchor granularity question):
     (1) textbook_reference field extended: chapter/section anchor REMAINS mandatory + page number / equation / scheme / figure number added as OPTIONAL granularity layer (LLM may omit when not confidently recalled — see textbook_quote_status field)
     (2) NEW field textbook_quote_status (mandatory, 3 enum values):
         - "anchor_only_no_quote": chapter/section pointer only; no LLM-side textbook claim text generated (v3/v4 default behavior; lowest hallucination risk)
         - "paraphrased": LLM paraphrases the canonical knowledge in 1-2 sentences in textbook_canonical_claim field; explicitly flagged as LLM rendering, NOT verbatim; medium hallucination risk; reader MUST verify against original textbook
         - "from_memory_verbatim": LLM attempts verbatim recall of a short textbook sentence; HIGHEST hallucination risk; MUST be enclosed in textbook_canonical_claim with explicit ⚠ "VERIFY AGAINST ORIGINAL" warning
     (3) NEW field textbook_canonical_claim (conditional, populated iff textbook_quote_status ∈ {paraphrased, from_memory_verbatim}): the LLM's rendering of what the textbook says at the anchored location
     (4) Anchor-fabrication discipline tightened: if a specific page/equation cannot be confidently recalled, MUST fall back to chapter/section-only with textbook_quote_status=anchor_only_no_quote — do NOT fabricate page numbers to reach finer granularity
     (5) Self-evaluation section extended: textbook_quote_status distribution (3 counts) + paraphrased_count + verbatim_count exposed for downstream audit
     (6) Boundary clarification: this is a PILOT extension. n=11 production v4 corpus (kumada1972 / wakamatsu1971 / boyer1973 / hayaishi1957 / slater1950 / beinert1983 / weber1993 / demeis1984 / murai1993 / hoque2022 / kuninobu2015) was run under v3/v4 (anchor_only_no_quote default). v5 promotion requires n≥1 re-run comparison demonstrating (a) anchor granularity gain measurable and (b) hallucination-risk surface acceptable.
-->
<!-- v3→v4 changes (2026-05-27, n=10 pilot complete — production promotion):
     (1) Three-zone G2 gradient formally added: modern(44-46%) > Δt≈31y(23%) > foundational(0-17%);
         confirmed cross-domain (murai1993 organometallic G2=23% = weber1993 biochemistry G2=23%)
     (2) G7-boundary cross-domain CONFIRMED: murai1993 (organometallic, Δt≈31-33y) G7-boundary=2
         matches weber1993 (biochemistry, Δt≈31y) G7-boundary=2 exactly; domain-independent threshold
     (3) "Resolution-imminent discovery paper" new sub-category added (anticipates_canonical=2,
         G7-boundary=2, G7=0 formal): murai1993 as canonical case. Distinct from "canonical formation
         paper" (=4, beinert1983) and "paradigm-initiating paper" (=3, kumada1972).
     (4) Co-location structural pattern added: G7-boundary instances = anticipates_canonical instances
         in resolution-imminent papers (by construction — paper is resolution-imminent at precisely
         the knowledge nodes it anticipates)
     (5) Combined classification rule extended to 3-category (foundational / resolution-imminent /
         modern); n=10, 10/10 accuracy
     (6) G7 cross-domain CONFIRMED: kumada1972 (organometallic, Δt≈54y) G7=3 strict;
         G7 density=3 ("direct mechanism paper") cross-domain consistent
     (7) G2 elevation hypothesis CONFIRMED at n=2 modern controls: hoque2022=46%, kuninobu2015=44%
     (8) G_novel-GE sub-type candidate registered: hoque2022 "geometric/electronic attribution
         indeterminacy" — paper attributes selectivity to geometric mechanism when textbook electronic
         mechanism provides equally sufficient explanation
     (9) Production promotion status updated: all 3 remaining validation criteria CONFIRMED (n=10)
         → prompt now suitable for all disciplines in V4 pilot deployment
-->
<!-- Position: inserted between Turn 3 and Turn 4 (synthesis), per Turn 1 §"Agent count guidance" -->
<!-- v1→v2 changes:
     (1) G7 added as formal 7th type in 「綻び」 typology (n=2 pilot confirmed: boyer1973 + hayaishi1957)
     (2) G4 direction variants note: "Many→One" vs "One→Many"
     (3) anticipates_canonical ≥2 pattern guidance added
     (4) G1 example: name-encodes-specificity type (enzyme/catalyst name)
     (5) Structural ceiling ~86% note added in pilot notes
     (6) Textbook corpus reference changed to general template (adapt per discipline)
-->
<!-- v2→v3 changes (2026-05-27, n=7 pilot complete):
     (1) G7-boundary subtype formally added to G7 typology entry (weber1993 Δt≈31y as canonical case)
     (2) anticipates_canonical=4 "canonical formation paper" sub-category added (beinert1983 as canonical case)
     (3) G7 density interpretation guide added as new section (density=3 "direct mechanism paper" vs density=1 "peripheral")
     (4) g7_boundary_count added to output format self-evaluation section
     (5) Pilot status updated to n=7 complete; all hypotheses confirmed; combined classification rule added
     (6) G4+G5 NOT foundational-specific CONFIRMED (n=7 correction to v2 expectation)
     (7) Textbook corpus reference expanded (2026-05-27): organometallic now 4 refs with [baseline type] labels
         (Hegedus & Söderberg "Methodology-proximal" added; Elschenbroich removed); biochemistry expanded to 3
         refs (Voet & Voet added); physical chemistry/spectroscopy expanded to 3 refs (Hollas added);
         general organic chemistry section added as new discipline (Carey & Sundberg + March's added)
-->

Report the prompt version at the start of your output:
```
prompt_version: stage1-v184-20260528_v4pilot_v7
```

---

## PDF reading note

Read the paper PDF directly using the Read tool (multimodal reading). If
the PDF is 20 pages or fewer, read the entire file in one call. If the
PDF exceeds 20 pages, split into page ranges (e.g., "1-20", "21-40")
with a maximum of 20 pages per call. Do not use pdftotext or other
text-extraction tools.

---

## Pilot context (V4 design)

V4 = "**textbook reader**" — a hypothetical reader who has internalized
the canonical knowledge currently presented in standard textbooks of the
paper's discipline, but holds **NO field-internal licenses**.

**Textbook-equipped reader: structural definition**:

The textbook-equipped reader (V4 frame) is NOT defined by knowledge
*deficit*. It is defined by knowledge *type*: only externally-codified,
textbook-canonical knowledge — no internalized field-internal licenses
(no tacit "conventional exceptions", no "workaround acceptance", no
"this-is-understood-by-experts omissions"). The textbook-equipped reader
functions as an **externally auditable canonical-knowledge oracle**.

| | Own-field expert (V1) | Textbook-equipped reader (V4) |
|---|---|---|
| Textbook canonical knowledge | Holds | **Holds** |
| Field-internal license (tacit exceptions, workarounds, accepted omissions) | **Internalized** | **NOT held** |
| "This-is-too-long-to-elaborate, just flag it" style omissions | Recognizes and accepts | **Does not pass over** |
| Jump from textbook description to paper description | "That's how it is" — passes through | **"Wait — why?" — stops** |

V4 questions are anchored to **inconsistencies between textbook canonical
knowledge and paper description**. This is kind-distinct from V1
(own-field expert), V2 (adjacent-field), and V3 (methodology) frames,
each of which surfaces a different category of question.

---

## V4 frame sub-split (v7 CHANGE 10 — DESIGN DIRECTION, tagged not hard-split)

The kumada1972 verification sweep revealed that "textbook-equipped reader"
silently conflates THREE distinct reader frames. v7 does not hard-split the
prompt; instead each V4-Q is TAGGED via `external_anchor_relation` so the
split can be drawn analytically downstream (and in Paper E2). The three
frames and their distinguishing `external_anchor_relation` values:

| Frame | Definition | external_anchor_relation | Anchor verifiable as textbook citation? |
|-------|-----------|--------------------------|------------------------------------------|
| **V4a — strict / direct textbook reader** | Gap between paper and knowledge DIRECTLY stated in textbook text | `direct_textbook_statement` | YES (requires actual access) |
| **V4b — textbook-enabled analogical reader** | Gap surfaced by extrapolating a textbook template/principle to the paper's system | `generic_textbook_template` \| `cross_system_extrapolation` | NO — it is reader extrapolation, not a textbook citation |
| **V5 — retrospective field-canon reader** | Gap against modern field canon synthesized from textbook + reviews + primary literature | `field_synthesis` | NO — no single textbook location states it |

Empirical placement from kumada1972: Q5/Q7 are V4b (Pd→Ni template; Rh→Ni
cross-system), NOT strict V4a. Q1 may be V5 (Ni(0)/Ni(II) as modern field
canon). Only `direct_textbook_statement` items (none confirmed in kumada1972
under memory-based mode) are strict V4a. **The strictest, most defensible
textbook anchor is V4a + actual_text_read; everything else must be marked as
extrapolation or synthesis, not asserted as a textbook citation.**

---

## Textbook corpus reference (TEMPLATE — adapt per paper)

**Use the textbook corpus appropriate to the paper's discipline.**
Specify the actual textbook editions used in the `textbook_corpus_used`
field of the output. The following are canonical defaults by discipline:

**Organometallic / homogeneous catalysis & organic synthesis**:
- Crabtree, "The Organometallic Chemistry of the Transition Metals"
  (7th ed., 2022), particularly: C–H activation, σ-bond metathesis,
  oxidative addition/reductive elimination, metal–ligand interactions
  [Mechanism-proximal baseline]
- Hegedus & Söderberg, "Transition Metals in the Synthesis of Complex
  Organic Molecules" (3rd/4th ed.), particularly: functional group
  compatibility, regioselectivity, and named catalytic transformations
  in organic synthesis [Methodology-proximal baseline]
- Hartwig, "Organotransition Metal Chemistry" (2010), particularly:
  ligand effects, C–H functionalization, boron chemistry, selectivity
  concepts
- Clayden, Greeves & Warren, "Organic Chemistry" (2nd ed., 2012) /
  Kürti & Czakó, "Strategic Applications of Named Reactions"

**Biochemistry / enzymology**:
- Nelson & Cox, "Lehninger Principles of Biochemistry" (8th/9th ed.),
  particularly relevant metabolic pathway (respiratory chain, ATP
  synthesis) and enzyme mechanism chapters [Mechanism-proximal baseline;
  canonical reference for G7 density and black-box resolution verification]
- Berg, Tymoczko, Gatto & Stryer, "Biochemistry" (9th/10th ed.),
  particularly structural bioenergetics and regulatory mechanism chapters
  [Complementary canonical reference]
- Voet & Voet, "Biochemistry" (5th ed.), for rigorous chemical structures
  and thermodynamic foundations

**General physical chemistry / spectroscopy**:
- Atkins, de Paula & Keeler, "Atkins' Physical Chemistry" (11th/12th ed.),
  particularly: Chemical Thermodynamics, Statistical Thermodynamics, and
  Molecular Spectroscopy chapters [Core normative baseline for molecular
  properties and kinetics]
- McQuarrie & Simon, "Physical Chemistry: A Molecular Approach",
  particularly: Quantum Mechanics and Spectroscopy chapters [Rigorous
  reference for quantum chemical foundations and structural assignments]
- Hollas, "Modern Spectroscopy" (4th ed.), for precise verification of
  selection rules, electronic/vibrational/rotational transitions, and
  experimental resolution limits [Spectroscopy-specific baseline]

**General organic chemistry / physical organic & synthetic methodology**:
- Clayden, Greeves & Warren, "Organic Chemistry" (2nd ed., 2012),
  particularly: regioselectivity, stereochemistry, orbital mechanisms
  (pericyclic reactions), and retrosynthetic analysis [The ultimate
  normative baseline for modern organic logic]
- Carey & Sundberg, "Advanced Organic Chemistry: Part A: Structure and
  Mechanisms / Part B: Reactions and Synthesis" (5th ed.), particularly:
  quantitative physical organic parameters, reactive intermediates, and
  transition state models [Rigorous reference for physical-organic gaps]
- Smith, "March's Advanced Organic Chemistry: Reactions, Mechanisms, and
  Structure" (8th ed.), as the comprehensive encyclopedic reference for
  functional group transformations and mechanistic scope boundary
  verification

**Time gap caveat (feature, not bug)**:
The paper may predate the current textbook editions. The textbook canonical
coverage may have been formed largely through post-paper research programs.
This time gap is a **primary mechanism by which 「綻び」 surface**:

- The paper proposes / observes / assumes a concept; the textbook presents
  the field's refined understanding after subsequent resolution.
- Inconsistencies between paper (at T₀) and textbook (at T₀+Δt) are NOT
  defects of either — they record how the field evolved.
- V4's task is to surface those points of inconsistency that, **read from
  the textbook side**, become visible as canonical gaps in the paper.

---

## 「綻び」 7-type typology (internal probe checklist, NOT output classification)

教科書 reader が surface する「綻び」は以下の 7 subtype に分類できる (G7 は
v2 で正式追加、G7-boundary subtype は v3 で正式追加)。本 checklist は V4 の
**systematic internal probe** として deploy する。出力での明示分類は不要だが、
各 question に対して該当 type を 1 つ assign する。

| ID | Type | 定義 | 検出パターン |
|---|---|---|---|
| **G1** | **Mid-step gap** | 教科書 A → B → C、論文 A → C | 教科書が B を明示する steps を論文が省略。**注 (v2 NEW)**: enzyme/catalyst NAME が specific step や regiochemistry を encode している (例: "tryptophan **2,3**-dioxygenase" → 2,3-regiochemistry が paper で verify されていない) 場合も G1 に該当する |
| **G2** | **Unconditional generalization** | 教科書「条件 K のとき X」、論文「X」 | 教科書が要求する operating condition を論文が明示せず |
| **G3** | **Exception normalization** | 教科書「例外として Y」、論文「Y (typical case として)」 | 例外を typical 扱い、または逆に typical を例外として扱う |
| **G4** | **Multiple-mechanism collapse** | 教科書「M1 / M2 / M3」、論文「M1 のみ」 | 教科書が並置する複数機構の一部しか論文が扱わず、他を排除する根拠も提示せず。**注 (v2 NEW — direction variants)**: G4 には 2 方向がある。**"Many→One" direction**: paper が textbook より narrow (textbook は M1/M2/M3 を提示するが paper は M1 のみを考慮)。**"One→Many" direction**: textbook が 1 つの resolved mechanism を提示するが paper は複数の candidates を同等に扱い resolution を達成していない。どちらも G4 として flag する。 |
| **G5** | **Loose definition** | 教科書「term T は厳密に X」、論文「T」(loose 使用) | 教科書が厳密定義する term を論文が文脈依存で loose 使用 |
| **G6** | **Convention-stripped reference** | 教科書「Z は慣習的に W と書く」、論文「W」(慣習 unstated) | 教科書が明示する convention を論文が前提として省略 |
| **G7** | **Resolved-to-black-box gap** *(FORMALLY ADOPTED v2; n=2 confirmed: boyer1973 Δt=48y, hayaishi1957 Δt=64y; n=5 foundational Δt≥40y all confirmed v3)* | 論文が T₀ に適切に vague / open-ended な表現（"mechanism not clear", "conformational change"）で記述した概念を、textbook が T₀+Δt に specific な resolved form（例: γ-subunit rotation; Fe²⁺ ferryl mechanism）として提示している場合に surface する gap | **Activation condition: Δt ≥ ~40 years** (大きな時間差がある場合に consistently 出現)。**G7-boundary subtype (v3 NEW — canonical case: weber1993 Δt≈31y)**: Δt ≈ 30-39y の resolution-imminent papers（resolution が 1-5 年後に来る papers）では、full G7 ではなく **G7-boundary** cases が出現する。G7-boundary = paper は resolution の直前に位置しており、vague な記述と approaching-resolution の兆候が共存している状態。Flag as `G7-boundary` (NOT G7-absent AND NOT full G7); use note: "G7-boundary case (Δt = Xy; textbook canonical form established ≈Y-Z years post-paper)". **G7-boundary cases は `g7_boundary_count` フィールドで集計し、`g7_count` (full G7 only) とは分離する。G7 activation は binary ではなく 30-40y range の gradient である。** **Critical design note**: G7 は **paper の欠陥ではなく歴史的必然**（paper 投稿時点では genuinely unknown → 適切な vague 表現）を記録する。これは G1-G6（paper が T₀ に knowable だった内容の省略）と質的に異なる。Modern papers (Δt small) では **G7 は absent が expected** — G7 の absence は modern paper の defining feature となりうる。 |

**Novel subtype handling (重要)**:
candidate gap が 7 type のいずれにも fit しない場合、強制 classify せず
`G_novel` として flag し、**short subtype description** を付加する。これに
より「綻び」 typology の expansion candidate が surface する。

---

## G7 density interpretation guide (v3 NEW)

G7 count per paper (「G7 density」) correlates with the paper's
**mechanism-proximity** — how directly the paper was working on the
subsequently-resolved central problem:

| G7 density | Interpretation | Canonical case (n=10 pilot) |
|---|---|---|
| 0 (modern) | Modern paper (Δt small); G7 absent = defining feature | kuninobu2015 (Δt≈11y), hoque2022 (Δt≈2y) |
| 0 + G7-boundary ≥1 | **Resolution-imminent discovery paper** (Δt ≈ 30-39y); approaching but not yet resolved. **Sub-category (v4 NEW)**: anticipates_canonical typically=2, G7-boundary=2; **Co-location pattern**: G7-boundary instances = anticipates_canonical instances (by construction — paper is resolution-imminent at precisely the knowledge nodes it anticipates). **Cross-domain CONFIRMED**: weber1993 biochemistry (Δt≈31y) + murai1993 organometallic (Δt≈31-33y), both G7-boundary=2, both G2=23% | weber1993 (Δt≈31y, 2 G7-boundary), **murai1993 (Δt≈31-33y, 2 G7-boundary, cross-domain confirmed v4)** |
| 1 | Foundational, **peripheral contribution** — paper addressed adjacent questions that fed into the central resolution | boyer1973 (oxygenase, Δt=48y), hayaishi1957 (oxygenase, Δt=64y) |
| 2 | Foundational, **proximal contribution** | — |
| 3 | **Direct mechanism paper** — paper was working on the precisely-resolved central problem. Cross-domain confirmed: holds in organometallic chemistry as well as biochemistry | slater1950 (respiratory chain, Δt≈74y), beinert1983 ([3Fe-4S] canonical, Δt≈41y), demeis1984 (Boyer mechanism thermodynamics, Δt≈40y), **kumada1972 (Ni cross-coupling, Δt≈54y, organometallic, cross-domain confirmed v4)** |

**Three-zone G2 gradient (v4 NEW — confirmed cross-domain)**:
G2 (Unconditional generalization) rate is a **Δt-dependent, domain-independent metric**:
- Modern papers (Δt < 20y): G2 ≈ 44–46% (n=2: kuninobu2015=44%, hoque2022=46%)
- Resolution-imminent zone (Δt ≈ 31y): G2 ≈ 23% (n=2 cross-domain: weber1993=23%, murai1993=23% — numerical identity)
- Foundational papers (Δt ≥ 40y): G2 = 0–17% (n=6, range 0–23%)

Use this gradient as a **temporal placement check**: if G2 rate falls in a given zone but G7 activation pattern suggests another zone, investigate the discrepancy rather than assuming error.

**Design note**: G7 density is a post-hoc computed metric. Do NOT
artificially inflate G7 count to match a target density. Report honestly;
the density emerges naturally from the paper's scope. Use this guide
only for **retrospective interpretation**, not as a generation target.

---

## Field determination

Review V1's, V2's, V3's outputs in this session. Confirm that V4's
textbook-reader perspective is **different in kind** from each of the
three. State V4's field as:

```
V4 (PILOT v6): Canonical-textbook reader (textbook-equipped reader) —
               [discipline-appropriate textbook corpus] without
               field-internal licenses
```

with a one-sentence rationale identifying which kind of question V1/V2/V3
cannot generate that V4 will fill.

---

## Anchoring discipline (modified for V4)

Every V4 question must be **doubly anchored**:

1. **Paper anchor (mandatory)**: verbatim `quote` from the paper, with
   `loc` reference (per Turn 1 §"Location markers" rules)
2. **Textbook anchor (mandatory)**: specific chapter / section / concept
   that establishes the canonical knowledge against which the gap is
   measured (e.g., "Crabtree Ch.8, C–H activation oxidative addition
   mechanisms")
3. **Textbook quote-status (mandatory; v5 introduced, v6 R2 refined)**:
   one of three labels declaring how the textbook canonical knowledge is
   rendered in the output:
   - `anchor_only_no_quote` — chapter / section pointer only; the LLM
     does NOT render textbook content text. This is the lowest-hallucination-
     risk option and matches v3/v4 behavior. Use when chapter-level anchor
     is sufficient and the reader will verify by opening the textbook.
   - `paraphrased` — the LLM paraphrases the canonical knowledge in 1–2
     sentences in the `textbook_canonical_claim` field. This is an LLM
     rendering, NOT verbatim. Hallucination risk medium. The reader MUST
     verify against the original textbook before treating the claim as
     authoritative.
   - `verified_short_quote` (v6 R2 NEW; replaces deprecated
     `from_memory_verbatim`) — a short verbatim quote from the textbook,
     GATED by access. **MUST NOT be generated from LLM memory alone.**
     Permitted only when `textbook_access_mode` (Field 4 below) is
     `actual_text_read` OR `user_supplied_excerpt`. In both cases, the
     `textbook_canonical_claim` field contains the verbatim sentence in
     quotation marks plus the access provenance (e.g., "[user-supplied
     excerpt, supplied YYYY-MM-DD]" or "[directly read via Read tool
     from URL/path]"). LLM-memory-based verbatim quotation is
     **PROHIBITED** because it combines confabulation risk with copyright
     risk and v6's analytical value lies in anchor + trigger_relation,
     not in verbatim quotation.
4. **Textbook access mode (mandatory; v6 R6 introduced, v7 ACCESS GATE)**:
   one of five labels declaring how the model accessed the textbook
   content for this V4-Q. **In v7 this field is the ACCESS GATE that
   governs whether a specific textbook citation is permitted at all.**
   - `actual_text_read` — the model has, within this session, read the
     textbook chapter / section via the Read tool from a legally
     accessible source (user-provided PDF, open-access excerpt). **Permits
     specific citation** (chapter title / section / page / named content)
     and `textbook_quote_status = verified_short_quote`.
   - `user_supplied_excerpt` — the user has provided the textbook excerpt
     in the conversation. **Permits specific citation** of the supplied
     content and `verified_short_quote`.
   - `primary_literature_triangulation` (v7 NEW) — the textbook was NOT
     read, but the canonical claim has been corroborated via WebSearch on
     the textbook's underlying primary literature (e.g., Mitchell 1961 for
     PMF; Noji 1997 for γ-rotation; Walker c-ring papers for H⁺/ATP).
     **Permits citation of the PRIMARY LITERATURE (not the textbook
     section)**; the canonical claim must be framed as "corroborated by
     the primary source the textbook cites", and `textbook_reference` must
     name the primary literature, NOT a guessed textbook chapter/section.
   - `concept_level_no_citation` (v7; REPLACES `memory_based_anchor`) — the
     model has NOT read the textbook and has NO user excerpt and NO primary-
     literature corroboration. **NO specific textbook location may be cited.**
     The canonical knowledge is referenced ONLY at concept level, explicitly
     framed as "the model's representation of canonical knowledge as
     generally taught", NOT as a textbook citation. `textbook_reference`
     MUST NOT name a chapter title, section name/number, page, or figure.
     This is the v7 DEFAULT in the absence of access. Compatible with
     `textbook_quote_status = anchor_only_no_quote` ONLY (no paraphrased
     location-attributed claim, no verbatim).

     **DICTION RULE (v7 CHANGE 7 — the most important phrasing constraint)**:
     Under `concept_level_no_citation`, verified-assertion diction is
     PROHIBITED. The access gate blocks naming a section; the diction rule
     additionally blocks verified-SOUNDING phrasing that would make an
     unverified memory claim read as an established textbook fact.
     - PROHIBITED (asserts a verified textbook claim):
       · "The textbook presents X"
       · "Crabtree Ch.9 states ..."
       · "The textbook resolves this as ..."
       · "the canonical textbook description is ..."
     - REQUIRED (marks epistemic status as expectation / extrapolation /
       requires-verification):
       · "A possible textbook-side expectation is ..."
       · "A reader may extrapolate from the textbook's [related-system]
         template to [the paper's system] ..."
       · "This canonical-knowledge claim requires verification against
         [named source] before it can be cited as a textbook statement."
     Rationale: even without a specific section number, "the textbook
     presents Ni(0)/Ni(II) as canonical" asserts a verified claim. The
     diction must mark the epistemic path (expectation / extrapolation /
     pending-verification), not assert. This is what the kumada1972 v6
     outputs failed: they carried the memory_based flag yet wrote
     "the textbook presents ..." in verified-assertion voice.
   - `bibliographic_anchor_only` — only a bare bibliographic citation
     (book title + edition, e.g., "Crabtree, The Organometallic Chemistry
     of the Transition Metals, 7th ed.") with NO chapter/section/content
     claim. Permitted without access because it makes no verifiable content
     claim beyond the book's existence.

   **v7 ACCESS GATE rule (the core v7 constraint)**:
   - Specific textbook citation (naming a chapter title, section
     name/number, page, figure, or attributing specific content to a
     location) is PERMITTED ONLY when access_mode ∈ {actual_text_read,
     user_supplied_excerpt}.
   - `primary_literature_triangulation` permits citing the PRIMARY SOURCE,
     not the textbook location.
   - `concept_level_no_citation` and `bibliographic_anchor_only` permit NO
     specific textbook-location claim.
   - **Rationale**: memory-based specific citation is systematically
     confabulated (empirically confirmed at TOC level — see v6→v7
     changelog). A reader who has not read the cited location is guessing,
     not citing. v7 forbids the specificity of the anchor from exceeding
     the access actually obtained.

5. **Textbook canonical claim (v5 introduced; v7 access-gated)**: populated
   iff `textbook_quote_status ∈ {paraphrased, verified_short_quote}` AND
   access_mode permits the corresponding specificity. Under
   `concept_level_no_citation`, the canonical knowledge may be stated as a
   concept-level paraphrase ONLY with explicit framing ("model's
   representation of canonical knowledge, not a textbook citation") and
   `textbook_quote_status = anchor_only_no_quote`.

**Page-level granularity (v5 introduced; v7 access-gated)**:
Specific page / equation / scheme / figure numbers may be cited ONLY under
access_mode ∈ {actual_text_read, user_supplied_excerpt}, where they can be
read off the actual text. Under `concept_level_no_citation`, NO page /
figure / section number may be named — not even "approximately". (This
closes the v5 ⚠-flagged-figure-pointer path, which the kumada1972 sweep
showed to be a confabulation vector at the section-mapping level.)

**Anchor-fabrication discipline (v5 strengthened)**:
- DO NOT fabricate page numbers, equation numbers, or figure numbers to
  reach finer granularity. If unsure, fall back to chapter/section.
- DO NOT generate a `textbook_canonical_claim` if you are not confident
  the textbook makes that claim. Fall back to
  `textbook_quote_status = anchor_only_no_quote` instead.
- The reader will calibrate trust based on `textbook_quote_status` —
  honest under-anchoring is more valuable than over-confident
  granularity.

---

## Anchor-genesis schema (v6 NEW — three additional mandatory fields per V4-Q)

v6 introduces three fields that preserve not just WHERE a question comes
from (paper anchor, textbook anchor) but HOW it was generated — which
reader stance read the paper passage, what specific relation between
paper-side and textbook-side content triggered the question, and whether
the question is plausible at the paper's contemporary time-point or only
in retrospect.

**Core principle**: A question is "ある読者立場が、ある論文箇所を、ある外部規範と照合したときに発生する、再検証可能な認識イベント." The v6 schema preserves the genesis of each
question, not only its textual destination.

### Field 5: `stance` (MANDATORY per V4-Q)

```yaml
stance:
  frame: V4_canonical_textbook_reader
  rationale: "one sentence: why THIS frame, not V1 (own-field expert),
              not V2 (adjacent-field), not V3 (methodology), surfaces
              THIS specific question"
```

- `frame` is fixed for this prompt (always `V4_canonical_textbook_reader`)
- `rationale` is the item-level genesis statement. It MUST be specific to
  this question, not boilerplate. It should answer: what is it about
  textbook-equipped reading that makes this gap visible, where V1/V2/V3
  would not have surfaced it?
- The header-level `field_rationale` (global stance summary) is retained,
  but per-item `stance.rationale` is now where per-question genesis lives.

### Field 6: `trigger_relation` (MANDATORY per V4-Q)

```yaml
trigger_relation:
  primary_type: "omission | mismatch | under-specification |
                 later-resolution | terminology-shift | mechanism-gap |
                 other"
  secondary_type: "optional second type (or null) when the question is
                   co-triggered by two relations"
  subtype: "optional free-text refinement (e.g., 'stoichiometry-mismatch',
            'direction-mismatch', 'scale-mismatch', 'assay-to-mechanism
            jump', 'model-to-measurement mismatch'); use to capture
            paper-specific or frame-specific relation types not
            anticipated by the initial enum"
  explanation: "MANDATORY free text, 1–3 sentences. Pattern: 'Paper
                reports/omits X; external norm (named in external_anchor)
                would lead reader to expect Y; the relation between X and
                Y is Z.' Must be paper-and-anchor-specific — NOT
                boilerplate."
```

**Initial enum candidates** (open set — add via `subtype` if none fit):
- `omission`: paper does not state X that textbook treats as required
- `mismatch`: paper states X variant; textbook states X canonical (the two are inconsistent)
- `under-specification`: paper uses term/concept loosely; textbook defines it precisely
- `later-resolution`: paper's open framing was later resolved into a specific canonical form (anticipates_canonical territory; G7 territory at large Δt)
- `terminology-shift`: paper's term has been canonically replaced or refined
- `mechanism-gap`: paper omits a mechanistic step textbook includes
- `other`: none of the above fit; MUST be paired with explicit `subtype`

**CRITICAL design constraint (heuristic, not validation)**:
The mapping between `gap_type` (G1–G7) and `trigger_relation.primary_type`
is a **diagnostic heuristic guide**, NOT a validation constraint. The
same `gap_type` can manifest through multiple trigger relations, and the
same trigger relation can produce questions of multiple gap types. This
is by design — `gap_type` captures the SHAPE of the resulting gap
(taxonomic), while `trigger_relation` captures the GENESIS mechanism
(mechanistic). Both are analytically distinct and must be preserved
independently.

Diagnostic mapping (heuristic only — do NOT enforce):

| gap_type | typical trigger_relation candidates |
|---|---|
| G1 (Mid-step gap) | omission, mechanism-gap |
| G2 (Unconditional generalization) | under-specification, mismatch |
| G3 (Exception normalization) | mismatch, terminology-shift |
| G4 (Multiple-mechanism collapse) | mechanism-gap, later-resolution, mismatch |
| G5 (Loose definition) | under-specification, terminology-shift |
| G6 (Convention-stripped reference) | terminology-shift, omission |
| G7 (Resolved-to-black-box) | later-resolution (typical at Δt≥40y) |

Use this table to think with, not to validate against. If a question's
genesis does not fit the typical mapping, that is an EMPIRICAL FINDING —
record the gap_type and trigger_relation faithfully and flag the
mismatch in `stance.rationale`.

### Field 7: `anachronism_status` (MANDATORY per V4-Q)

```yaml
anachronism_status:
  value: "contemporary-plausible | retrospective-only | uncertain"
  rationale: "MANDATORY free text, 1–2 sentences. NOT auto-inferred
              from gap_type. Articulate WHY this question's plausibility
              hinges on post-paper knowledge stabilization (or does not).
              Pattern: 'This question would/would not have been askable
              at the paper's publication date because [specific
              historical knowledge state].'"
```

**Definitions**:
- `contemporary-plausible`: A reader equipped with the canonical
  knowledge available at the paper's publication date could have asked
  this question. The textbook-equipped reader's question matches what a
  paper-date textbook-equipped reader would also have surfaced.
- `retrospective-only`: This question depends specifically on knowledge
  that was codified into textbooks AFTER the paper's publication. Asking
  it of the paper is anachronistic in the strict sense — fair as
  retrospective audit, but unfair as contemporary critique.
- `uncertain`: Insufficient evidence to judge which side of the line this
  question falls on. Default to this when in doubt rather than
  forcing a contemporary-plausible / retrospective-only choice.

**CRITICAL design constraint (item-level judgment, not type-level
inference)**:
DO NOT auto-derive `anachronism_status` from `gap_type`. Specifically:
- G7 (resolved-to-black-box) is TYPICALLY but NOT NECESSARILY retrospective-only
- G1–G6 are TYPICALLY but NOT NECESSARILY contemporary-plausible
- Each item requires explicit, paper-specific rationale. The rationale
  is what makes anachronism status auditable. Default-by-typology hides
  the very thing the field is meant to expose.

**Purpose**: V4's intrinsic risk is anachronism — imposing post-paper
canonical knowledge on a paper that predates the canonicalization.
`anachronism_status` is the defense against this risk: it makes each
question's temporal positioning explicit and auditable. Without it, the
textbook-equipped reader's questions become silently retrospective by
default. With it, the textbook-equipped reader's questions become
explicitly time-stamped against the canonical knowledge that grounds
them.

---

**Inference tier — v6 R7 SPLIT (post-spot-check refinement, 2026-05-28)**:

The prior unified `inference_tier` (T1/T2/T3 in V1/V2/V3) conflated two
orthogonal epistemic axes. The boyer1973 spot-check empirically confirmed
that V4-Q items can be T1 paper-side (paper explicitly states) AND
unverified textbook-side (LLM memory anchor only). v6 R7 splits the
unified field into two independent fields, both MANDATORY per V4-Q.

### Field 8: `paper_inference_tier` (v6 R7 NEW, mandatory per V4-Q)

How directly the paper supports the existence and wording of this question
on the paper side:

| Tier | Label | Meaning |
|------|-------|---------|
| T1_paper_explicit | *(no label)* | Paper directly states the relevant text or directly shows the relevant figure/data |
| T2_paper_grounded_inference | `[paper-grounded inference]` | Follows from quoted paper text in one inference step |
| T3_paper_external_inference | `[external inference]` | Requires external knowledge beyond paper text |

### Field 9: `textbook_verification` (v7 CONSOLIDATED — 3-part block; supersedes v6 R7 single-enum textbook_verification_status)

How the textbook canonical claim relates to the actually-accessed
textbook content. **This applies ONLY when access_mode ∈
{actual_text_read, user_supplied_excerpt}** (the only modes that permit a
specific textbook-location claim). Under `concept_level_no_citation`,
`bibliographic_anchor_only`, or `primary_literature_triangulation`, the
textbook_verification block is omitted or marked `not_applicable`
(because there is no read textbook location to verify against).

The block has three independent sub-axes (consolidating the v6-R7/R8
proposals and absorbing the kumada1972 + boyer1973 empirical outcome
categories):

```yaml
textbook_verification:
  anchor_existence: confirmed | partial | wrong_context | disconfirmed
    # confirmed   = the cited location exists AND discusses the relevant topic
    #               in the right system/context
    # partial     = the cited location exists and states a GENERAL principle in
    #               the right domain, but NOT the specific application claimed
    # wrong_context (v7 CHANGE 9 — GPT fix #3) = the cited location EXISTS and
    #               discusses the relevant CONCEPT, but in a DIFFERENT
    #               system/context than claimed (e.g., Crabtree §9.4 states
    #               bite-angle→RE but for Rh hydroformylation/BISBI, NOT Ni
    #               cross-coupling/dpe). Distinct from `partial` (right domain,
    #               general principle) and `disconfirmed` (absent entirely).
    # disconfirmed = the cited location does not exist OR does not discuss the
    #               topic at all (e.g., "Crabtree Ch.9 Kumada Coupling section"
    #               — no such section; Ch.9 is "Homogeneous Catalysis")
  claim_fidelity: faithful | over_slides | over_generalizes | wrong_system | under_states | unsupported | not_applicable
    # faithful        = canonical_claim accurately represents the verified textbook statement
    # over_slides     = claim asserts somewhat MORE than the text (stronger/more specific), same system
    # over_generalizes (v7 CHANGE 13) = claim generalizes the textbook statement beyond its stated scope/conditions
    # wrong_system (v7 CHANGE 13) = claim transfers a statement true for system X to the paper's system Y (claim-level analogue of anchor_existence=wrong_context)
    # under_states    = claim asserts LESS than the textbook
    # unsupported (v7 CHANGE 13) = no textbook support for the claim (typically paired with anchor_existence=disconfirmed)
    # not_applicable  = no verification performed (access_mode not in {actual_text_read, user_supplied_excerpt})
    # EMPIRICAL NOTE (scope-limited): in the 4 Crabtree-checked Kumada items,
    #   no item was a fully faithful direct-textbook anchor without qualification
    #   (Q12 over_slides; Q5/Q7 wrong_system; Q1 unsupported). NOT generalized
    #   to n=11 baseline or V4 in general. Specific to memory_based mode.
  inference_tier: T1_textbook_explicit | T2_textbook_grounded_extrapolation | T3_textbook_external_extrapolation
    # T1 = textbook directly states this for the paper's specific system/topic
    # T2 = textbook states the general principle OR states it for a RELATED
    #      system (e.g., Pd cycle → Ni Kumada; Rh bite-angle → Ni); the reader
    #      extrapolates. Symmetric to paper_inference_tier T2.
    # T3 = canonical claim requires extrapolation beyond textbook content
```

**Two independent axes (paper-side and textbook-side)**: `paper_inference_tier`
(Field 8) describes how directly the PAPER supports the question;
`textbook_verification` (Field 9) describes how the TEXTBOOK content
relates to the canonical claim. A V4-Q can be `T1_paper_explicit` (paper
directly states X) while textbook_verification shows
`anchor_existence=disconfirmed` (the claimed textbook location does not
exist). These are orthogonal and both are reported.

**v7 empirical grounding**: The 3-axis structure was derived from the
kumada1972 + boyer1973 verification sweep (n=7 items). Observed
combinations:
- disconfirmed + not_applicable (kumada Q1, Q5): citation hallucination
- partial + over_slides (kumada Q7): general principle present, specific
  application extrapolated
- confirmed + over_slides (kumada Q12, boyer Q4/Q8/Q9): real anchor, claim
  overstates the text
- confirmed + faithful: NOT YET OBSERVED (0 of 7) — a target state that
  v7 actual-access discipline is designed to make achievable

**Compatibility note**: V1, V2, V3 prompts (Stage 1 Turn 1/2/3) still use
the legacy unified `inference_tier`. V1-V3 unification into this v7
structure is deferred to a future Stage 1 revision OR a Stage 2 adapter.

**Critical: avoid field-internal expert reasoning**:
- DO NOT use reasoning like "well, in this field it's understood that..."
- DO NOT use reasoning that requires field-internal license
- IF a gap candidate requires expert workaround knowledge to even
  perceive, it does NOT belong in V4 — it belongs in V1

**Anchor-unavailable handling**:
- If a paper passage seems to fit a 「綻び」 type but you cannot identify
  a specific textbook reference, flag as `textbook_anchor: pending`
  rather than fabricate
- If the paper precedes textbook coverage (paper anticipates / introduces
  what later became canonical knowledge), explicitly note
  `textbook_anchor: anticipates_canonical` — this is itself a valuable
  observation about how the paper relates to the eventual canonical form

**anticipates_canonical pattern note (v2 NEW; v3 enhanced; v4 sub-category extended)**:
- If `anticipates_canonical` appears **≥2 times** in a single V4 analysis,
  note explicitly in the self-evaluation section: "anticipates_canonical
  count ≥2 is a **strong foundational paper signal** — this paper
  introduced or motivated concepts that the field later formalized."
- **If count = 2 AND G7-boundary ≥ 1 AND G7 = 0 (v4 NEW)**: add note: "**Resolution-imminent
  discovery paper signal** — this paper introduced canonical concepts whose mechanistic
  resolution arrived 5–15 years post-publication; G7-boundary instances co-locate with
  anticipates_canonical instances by construction (the paper is resolution-imminent at
  precisely the knowledge nodes it anticipates). Δt ≈ 30–39y signature."
  (Canonical cases: weber1993 [biochemistry, Δt≈31y] + murai1993 [organometallic,
  Δt≈31-33y], both G7-boundary=2 and anticipates_canonical=2; cross-domain confirmed.)
- **If count = 3 AND full G7 ≥ 3**: add note: "**Paradigm-initiating paper signal** —
  this paper proposed the founding framework; canonical elaboration required subsequent
  decades." (Canonical case: kumada1972, Δt≈54y, G7=3 strict.)
- **If count = 4 (v3 NEW)**: add note: "**Canonical formation paper signal**
  — this paper was not applying an existing textbook framework but
  constructing the evidence base that became the textbook entry itself.
  Four dimensions of canonical knowledge anticipated." (Canonical case:
  beinert1983, where the paper established the [3Fe-4S] cluster evidence
  base that became the textbook entry for iron-sulfur cluster structural
  assignment.)
- This pattern is expected in early foundational papers (1950s–1970s era)
  and should be absent or rare in modern papers (2010s+).

---

## Severity scale (same as V1-V3)

| Severity | Meaning |
|----------|---------|
| **low** | The 「綻び」 is minor; textbook coverage is sparse on this point or paper's framing is acceptable variation |
| **medium** | Noteworthy 「綻び」; a textbook reader would pause and ask the question |
| **high** | Significant 「綻び」; the inconsistency is hard to read past without explanation |
| **critical** | The paper's central premise contradicts canonical textbook knowledge on a load-bearing point |

Severity is computed **from the textbook reader's perspective**, not from
any field-internal expert standpoint.

---

## Instructions

You are the **textbook-equipped reader** as defined above (schema label
`V4_canonical_textbook_reader`). You hold the canonical knowledge that
standard discipline-appropriate textbooks codify, but you do NOT hold
field-internal licenses (no internalized "conventional exceptions",
no "workaround acceptance", no "this-is-understood-by-experts
omissions"). You are NOT a beginner; you are a reader whose knowledge
is externally auditable because it lives in textbooks rather than in
tacit field practice. You have read V1, V2, V3 outputs. Your task is
twofold:

### Part A — New questions (8–15)

Generate questions that V1, V2, V3 did not cover, anchored to BOTH paper
quotes AND specific textbook references. Each question must:

1. Quote the relevant paper passage (`quote` — required)
2. Provide location reference (`loc`)
3. Provide specific textbook reference (`textbook_reference` — required)
4. Assign one 「綻び」 type from {G1, G2, G3, G4, G5, G6, **G7**, **G7-boundary**} OR `G_novel`
   with short description; for G7-boundary, add note on Δt and resolution timing
5. State the question concisely
6. Note differentiation from V1/V2/V3 (`differentiation`: 1-sentence
   why this question is different in kind from what V1/V2/V3 generated)
7. Assign severity (low/medium/high/critical)
8. Label inference tier (T1/T2/T3)

**Different-in-kind mandate**: V4 must generate questions of a
fundamentally different kind from V1/V2/V3. Apply this test for each
candidate question: would V1 (own-field expert), V2 (adjacent field), or
V3 (methodology/stats) naturally produce this question from their
respective stances? If YES for any of the three, the question is too
close to their kind — discard or reformulate from the textbook-reader
stance.

Acceptable V4 question kinds (illustrative, not exhaustive):
- "The textbook describes step B between A and C; the paper skips from
  A to C — where is B in the paper's account?" (G1 mid-step gap)
- "The textbook says X holds only under condition K; the paper asserts
  X without stating K — does K hold here?" (G2 unconditional generalization)
- "The textbook treats Y as an established exception; the paper uses Y
  as a typical case — is the paper's case actually typical?" (G3 exception normalization)
- "The textbook lists M1, M2, M3 as candidate mechanisms; the paper
  considers M1 only — why are M2 / M3 not addressed?" (G4 many→one direction)
- "The textbook presents the resolved form Z of mechanism M; the paper
  (written before Z was established) uses the earlier black-box
  term — this is historically appropriate but records a knowledge gap
  that was later resolved." (G7 resolved-to-black-box, only for Δt ≥ ~40y)
- "The paper is written shortly before the resolution of mechanism M;
  it approaches the resolved form but uses pre-resolution vocabulary —
  this is a G7-boundary case." (G7-boundary, Δt ≈ 30-39y)
- "The term T is strictly defined in textbooks as X; the paper uses T
  loosely — which sense applies here?" (G5 loose definition)
- "The textbook notes convention W is always written assuming Z; the
  paper writes W without Z — does the convention apply?" (G6 convention-stripped reference)

### Part B — Overlap re-evaluation (important)

Review V1, V2, V3 outputs. For any question that is **also visible from
a textbook reader's perspective**, record it as an overlap entry with V4
severity, the 「綻び」 type it would match, and a one-sentence note on
why the textbook reader would view it differently.

**Do not skip overlaps** — they are analytically valuable for confirming
or refuting V4's contribution boundary.

---

## V4 output format

```
[V4 (PILOT v7): Canonical-textbook reader (textbook-equipped reader) — ACTUAL-ACCESS anchoring]
field: V4_canonical_textbook_reader — [discipline-specific textbook
       corpus] without field-internal licenses
field_rationale: [one sentence: which kind of question V1/V2/V3 cannot
                  generate that V4 will fill — note: per-item rationale
                  appears in `stance.rationale` for each V4-Q below;
                  this header-level field_rationale is the global stance
                  summary]

textbook_corpus_used:
  - [specific textbook, edition, relevant chapters]
  - [...]

--- New questions ---

Each V4-Q is emitted as a multi-line YAML-like block (v6 schema is too
wide for a single pipe-delimited row). Schema:

```
V4-Q[N]:
  loc: "P:col:L"
  quote: "verbatim paper passage"
  paper_anchor_role: "observed_statement | missing_control | numerical_value | figure_reference | terminology | sentence_silence"

  stance:
    frame: "V4_canonical_textbook_reader"
    rationale: "one sentence: why THIS frame surfaces THIS question (item-specific, NOT boilerplate)"

  textbook_access_mode: "actual_text_read | user_supplied_excerpt | primary_literature_triangulation | concept_level_no_citation | bibliographic_anchor_only"   # v7 ACCESS GATE — determines whether specific citation is permitted
  textbook_reference: "
    - if access_mode ∈ {actual_text_read, user_supplied_excerpt}: specific chapter title / section / page / named content (read off the actual text)
    - if access_mode = primary_literature_triangulation: cite the PRIMARY LITERATURE (e.g., 'Mitchell 1961 Nature 191:144'), NOT a textbook section
    - if access_mode = concept_level_no_citation: NO specific location — concept-level reference only (e.g., 'canonical organometallic catalytic-cycle concept, as generally taught'); MUST NOT name chapter title / section / page / figure
    - if access_mode = bibliographic_anchor_only: book title + edition only, no chapter/section/content claim"
  textbook_quote_status: "anchor_only_no_quote | paraphrased | verified_short_quote"
    # verified_short_quote permitted ONLY under access_mode ∈ {actual_text_read, user_supplied_excerpt}
    # paraphrased with location attribution permitted ONLY under access_mode ∈ {actual_text_read, user_supplied_excerpt, primary_literature_triangulation}
    # under concept_level_no_citation / bibliographic_anchor_only: anchor_only_no_quote ONLY
  textbook_canonical_claim: "
    - if quote_status=anchor_only_no_quote: '—' (empty)
    - if quote_status=paraphrased AND access permits: '[paraphrased] <1-2 sentence rendering of accessed content>'
    - if quote_status=paraphrased AND access_mode=concept_level_no_citation: '[concept-level, model's representation, NOT a textbook citation] <1-2 sentence>'
    - if quote_status=verified_short_quote: '<verbatim quote> [provenance: actual_text_read from <path> | user_supplied_excerpt supplied <date>]'"
  external_anchor_source_type: "textbook_canonical | primary_literature | concept_level"  # v7: reflects access_mode
  external_anchor_relation:   # v7 CHANGE 8 — separates textbook-text / field-canon / reader-extrapolation
    value: "direct_textbook_statement | generic_textbook_template | cross_system_extrapolation | field_synthesis | unsupported"
      # direct_textbook_statement  = textbook directly states this for the paper's specific system (requires actual access)
      # generic_textbook_template  = textbook states a general template (e.g., Pd cross-coupling cycle); reader applies it to the paper's system (e.g., Ni)
      # cross_system_extrapolation = textbook states the principle for a DIFFERENT system/context (e.g., Rh hydroformylation bite-angle); reader transfers to the paper's system
      # field_synthesis            = claim synthesizes textbook + reviews + primary literature into modern field canon, not verbatim in any single textbook location
      # unsupported                = no textbook basis identified
    rationale: "MANDATORY free text — which of {textbook-text, field-canon, reader-extrapolation} the claim draws on, and how they are separated. This prevents compressing the three into one canonical_claim (the kumada1972 failure mode)."

  trigger_relation:
    primary_type: "omission | mismatch | under-specification | later-resolution | terminology-shift | mechanism-gap | other"
    secondary_type: "<second type if co-triggered, else null>"
    subtype: "<optional free-text refinement; required if primary_type=other>"
    explanation: "MANDATORY free text, 1-3 sentences. Paper reports/omits X; external norm would lead reader to expect Y; relation between X and Y is Z. (Paper-and-anchor-specific, NOT boilerplate.)"

  gap_type: "G1 | G2 | G3 | G4 | G5 | G6 | G7 | G7-boundary | G_novel"
  question: "the textbook-equipped reader's question, in English"

  anachronism_status:
    value: "contemporary-plausible | retrospective-only | uncertain"
    rationale: "MANDATORY free text, 1-2 sentences. Item-level judgment, NOT auto-inferred from gap_type."

  differentiation: "explicit comparison to nearest V1/V2/V3 questions; what makes this kind-different"
  severity: "low | medium | high | critical"
  paper_inference_tier: "T1_paper_explicit | T2_paper_grounded_inference | T3_paper_external_inference"
  textbook_verification:   # v7 CONSOLIDATED block; populate ONLY if access_mode ∈ {actual_text_read, user_supplied_excerpt}; else 'not_applicable'
    anchor_existence: "confirmed | partial | wrong_context | disconfirmed | not_applicable"
    claim_fidelity: "faithful | over_slides | over_generalizes | wrong_system | under_states | unsupported | not_applicable"
    inference_tier: "T1_textbook_explicit | T2_textbook_grounded_extrapolation | T3_textbook_external_extrapolation | not_applicable"
```

Generate V4-Q1, V4-Q2, ... V4-Q[N] (8-15 items) following this schema.

**v7 ACCESS-GATE reminder**: If you have NOT actually read the textbook
and have NO user excerpt and NO primary-literature corroboration, set
`access_mode = concept_level_no_citation` and DO NOT name any specific
chapter title / section / page / figure. State the canonical knowledge
at concept level only. This is the single most important v7 discipline:
**never let the anchor's specificity exceed the access actually obtained.**

--- Overlaps with V1/V2/V3 (v6 R5 schema: genesis metadata mandatory) ---

Overlap entries are the locus for FRAME CONVERGENCE analysis: when the same
question (or near-same question) is surfaced from both V4 (textbook-equipped
reader) and one of V1/V2/V3, this is evidence that the question is
multiply-supported across reader stances. Reducing overlap entries to
minimal metadata would defeat the v6 design goal of preserving genesis.
Therefore overlap entries carry a reduced but still substantive subset of
the V4-Q schema. Format:

```
V4-OV[N]:
  overlaps_with: "V1-Q[M] | V2-Q[M] | V3-Q[M]"  # the converging V1/V2/V3 item
  gap_type: "G1 | G2 | ... | G7 | G7-boundary | G_novel"
  severity_V4: "low | medium | high | critical"
  textbook_access_mode: "actual_text_read | user_supplied_excerpt | primary_literature_triangulation | concept_level_no_citation | bibliographic_anchor_only"   # v7 ACCESS GATE (same as V4-Q schema)
  textbook_reference: "specific location ONLY if access_mode ∈ {actual_text_read, user_supplied_excerpt}; primary literature if primary_literature_triangulation; concept-level only otherwise (no chapter/section/page)"
  trigger_relation:
    primary_type: "omission | mismatch | ... | other"
    explanation: "1-2 sentences: why textbook-equipped reading produces
                  the SAME question as the V1/V2/V3 frame did, OR what
                  the textbook frame adds that V1/V2/V3 does not. The
                  presence of cross-frame convergence is the key
                  observation; the trigger_relation captures WHY both
                  frames converge."
  anachronism_status:
    value: "contemporary-plausible | retrospective-only | uncertain"
    rationale: "1 sentence: time-stamp of the convergent question.
                Note that contemporary-plausible overlaps (V4 question
                askable at paper date AND V1/V2/V3 question askable at
                paper date) are stronger evidence of structural gap
                than retrospective-only V4 overlaps."
  stance_rationale: "1 sentence: how the textbook-equipped reader's
                     anchoring (canonical-knowledge inconsistency)
                     differs from or aligns with the V1/V2/V3 frame's
                     anchoring (field-internal expert / adjacent field /
                     methodology). DIFFERENT anchoring + SAME question =
                     strongest evidence of frame-independent gap."
  textbook_verification:   # v7 CONSOLIDATED block (same as V4-Q); populate ONLY if access_mode ∈ {actual_text_read, user_supplied_excerpt}, else not_applicable
    anchor_existence: "confirmed | partial | wrong_context | disconfirmed | not_applicable"
    claim_fidelity: "faithful | over_slides | over_generalizes | wrong_system | under_states | unsupported | not_applicable"
    inference_tier: "T1_textbook_explicit | T2_textbook_grounded_extrapolation | T3_textbook_external_extrapolation | not_applicable"
  note: "optional: any additional observation specific to this convergence"
```

Generate V4-OV1, V4-OV2, ... (3–7 entries; not all V1/V2/V3 questions need
re-evaluation — only those genuinely visible from textbook-equipped stance).

--- 「綻び」 typology distribution (self-report) ---
G1 (Mid-step gap): [count of V4-Q items]
G2 (Unconditional generalization): [count]
G3 (Exception normalization): [count]
G4 (Multiple-mechanism collapse): [count; note direction if relevant: "N Many→One, M One→Many"]
G5 (Loose definition): [count]
G6 (Convention-stripped reference): [count]
G7 (Resolved-to-black-box): [count; if non-zero, note Δt for each instance]
G7-boundary: [count; if non-zero, note Δt and resolution timing for each instance]
G_novel: [count, with subtype descriptions]

--- V4 PILOT v6 self-evaluation ---
unique_kind_compliance_estimate: [percentage of V4-Q items that V4 judges
  to be genuinely different-in-kind from V1/V2/V3 outputs; honest self-
  estimate]
textbook_anchor_specificity_rate: [percentage of V4-Q items with specific
  chapter / section cited vs vague reference]
novel_subtype_flagged: [count of G_novel items; if non-zero, list subtype
  descriptions for typology expansion consideration]
textbook_anchor_pending_count: [count of V4-Q items where specific
  textbook reference could not be identified]
textbook_quote_status_distribution (v5 introduced, v6 R2 refined):
  anchor_only_no_quote_count: [count]
  paraphrased_count: [count]
  verified_short_quote_count: [count]
  # Note: from_memory_verbatim is deprecated in v6 R2 and MUST be zero.
  # If you would have used it in v5, use either paraphrased
  # (with textbook_access_mode=memory_based_anchor) or
  # anchor_only_no_quote.

textbook_access_mode_distribution (v6 R6 introduced, v7 5-value):
  actual_text_read_count: [count]
  user_supplied_excerpt_count: [count]
  primary_literature_triangulation_count: [count]   # v7 NEW
  concept_level_no_citation_count: [count]           # v7 (replaces memory_based_anchor)
  bibliographic_anchor_only_count: [count]
  # v7 ACCESS-GATE consistency rules:
  # (a) any V4-Q with a specific textbook-location citation (chapter title /
  #     section / page / named content) MUST have access_mode ∈
  #     {actual_text_read, user_supplied_excerpt}. Report any violation as a
  #     v7 gate breach (the most important schema error to catch).
  # (b) verified_short_quote_count must equal actual_text_read_count +
  #     user_supplied_excerpt_count.
  # (c) concept_level_no_citation items MUST have textbook_reference with NO
  #     chapter/section/page/figure named.

paper_inference_tier_distribution (v6 R7 NEW):
  T1_paper_explicit_count: [count]
  T2_paper_grounded_inference_count: [count]
  T3_paper_external_inference_count: [count]

textbook_verification_distribution (v7 CONSOLIDATED; only items with access_mode ∈ {actual_text_read, user_supplied_excerpt} are counted here):
  anchor_existence:
    confirmed_count: [count]
    partial_count: [count]
    wrong_context_count: [count]   # v7 CHANGE 9
    disconfirmed_count: [count]
  claim_fidelity:
    faithful_count: [count]
    over_slides_count: [count]
    over_generalizes_count: [count]   # v7 CHANGE 13
    wrong_system_count: [count]        # v7 CHANGE 13
    under_states_count: [count]
    unsupported_count: [count]         # v7 CHANGE 13
external_anchor_relation_distribution (v7 CHANGE 8 NEW):
  direct_textbook_statement_count: [count]
  generic_textbook_template_count: [count]
  cross_system_extrapolation_count: [count]
  field_synthesis_count: [count]
  unsupported_count: [count]
  # v7 frame-split signal: direct_textbook_statement → strict V4a;
  # generic_textbook_template / cross_system_extrapolation → V4b (analogical);
  # field_synthesis → V5 (retrospective field-canon). Track the distribution
  # to see which frame each pilot paper predominantly exercises.
  inference_tier:
    T1_textbook_explicit_count: [count]
    T2_textbook_grounded_extrapolation_count: [count]
    T3_textbook_external_extrapolation_count: [count]
  not_applicable_count: [count of items with access_mode NOT in {actual_text_read, user_supplied_excerpt}, hence no verification block]
  # v7 empirical watch: claim_fidelity=faithful was 0 of 7 in the
  # boyer1973+kumada1972 sweep. Track whether actual-access items (v7
  # discipline) achieve faithful, which the memory-based items could not.

cross_axis_independence_check (v6 R7 introduced, v7 updated):
  # Verify that paper_inference_tier (paper-side) and textbook_verification
  # (textbook-side) carry orthogonal information. Report combinations like:
  #   T1_paper_explicit + anchor_existence=disconfirmed (paper directly
  #     supports the question, but the claimed textbook location does not
  #     exist) — the prototypical case justifying the paper/textbook split
  #   T2_paper_grounded_inference + anchor_existence=confirmed+faithful
  #     (paper needs an inference step, but textbook claim is verified faithful)
  # Presence of divergent combinations confirms the two sides are independent.

page_level_anchor_count (v5 NEW): [count of V4-Q items whose
  textbook_reference includes a specific page / equation / scheme / figure
  number beyond chapter/section level]

hallucination_risk_self_assessment (v5 introduced, v6 R2 refined):
  [one of "low" (all anchor_only_no_quote), "medium" (some paraphrased,
  no verified_short_quote), "verified" (≥1 verified_short_quote with
  documented access provenance); brief note on which V4-Q items carry
  highest verification burden. Note: under v6 R2, there is no "high"
  risk category equivalent to v5's from_memory_verbatim — that pathway
  is prohibited.]

trigger_relation_distribution (v6 NEW):
  omission_count: [count]
  mismatch_count: [count]
  under_specification_count: [count]
  later_resolution_count: [count]
  terminology_shift_count: [count]
  mechanism_gap_count: [count]
  other_count: [count; if non-zero, list subtype labels for typology expansion consideration]
secondary_trigger_count (v6 NEW): [count of V4-Q items with non-null secondary_type]
trigger_subtype_inventory (v6 NEW): [list of subtype free-text labels used
  in this pilot; cumulative across items; used to surface emerging
  paper-specific or domain-specific relations beyond the initial enum]

anachronism_status_distribution (v6 NEW):
  contemporary_plausible_count: [count]
  retrospective_only_count: [count]
  uncertain_count: [count]
anachronism_typology_independence_check (v6 NEW): [examine whether any
  V4-Q item shows gap_type ↔ anachronism_status pairing that contradicts
  the "typical" mapping (e.g., G7 + contemporary-plausible, or G1 +
  retrospective-only). Report any such cases as empirical findings; these
  are evidence that the v6 design constraint "anachronism is NOT
  auto-inferred from gap_type" is doing real work.]

rationale_quality_self_check (v6 NEW): [for each of the three mandatory
  free-text rationale fields (stance.rationale, trigger_relation.explanation,
  anachronism_status.rationale), self-assess on a 3-level scale:
    - "substantive" — paper-and-anchor-specific content unique to this item
    - "templated" — partially specific but with formulaic phrasing
    - "boilerplate" — generic statement that could apply to any item
  Report counts per field. Target: ≥ceil(0.8·N) V4-Q items "substantive"
  across all three fields, where N = total V4-Q count. "Boilerplate"
  populations indicate v6 schema is being filled by rote rather than
  capturing genuine genesis.]

gap_type_vs_trigger_relation_independence (v6 NEW): [identify cases where:
  (a) the same gap_type appears with DIFFERENT trigger_relation primary_types
      across V4-Q items, OR
  (b) the same trigger_relation primary_type appears with DIFFERENT gap_types
      across V4-Q items.
  Report instances. Presence of such cross-axis multi-valence is empirical
  confirmation that gap_type and trigger_relation are analytically orthogonal
  (not redundant labels for the same phenomenon).]

anticipates_canonical_count: [count of V4-Q items where the paper
  anticipates what later became canonical knowledge]
anticipates_canonical_pattern_note: [if count ≥ 2, write: "Count ≥2:
  strong foundational paper signal — [brief description]"; if count = 4,
  add: "Canonical formation paper signal — [brief description]"; if
  count 0–1, write "Count [N]: [brief note or 'no pattern detected']"]
g7_count: [count of full G7 items only (Δt ≥ ~40y); if present, note Δt
  for each instance; if absent, write "G7 absent — consistent with modern
  paper hypothesis (Δt < ~40y)" or applicable note]
g7_boundary_count: [count of G7-boundary items (Δt ≈ 30-39y, resolution-
  imminent); if non-zero, note Δt and resolution timing for each instance;
  if absent, write "G7-boundary absent"; tabulated separately from g7_count]
```

---

## V4 PILOT v6 execution constraints

- **Quantity target**: 8–15 questions (Part A new questions)
- **Overlap target**: 3–7 entries (Part B; not all V1-V3 questions need
  re-evaluation — only those genuinely visible from textbook-reader stance)
- **Boundary discipline**: Do not generate questions about content
  outside the paper's stated scope (Turn 1 §"Universal boundary rule"
  applies)
- **No new chemistry knowledge import**: All claims must anchor to the
  paper text + named textbook chapter; do not introduce chemistry
  knowledge that is not in either source

---

## Notes on pilot status (v7 update — ACTUAL-ACCESS discipline PILOT, 2026-05-28)

**V4 v7 status**: **PILOT** — actual-access textbook anchoring discipline. Paradigm shift from v6:
memory-based specific textbook citation is PROHIBITED. v6 anchor-genesis schema (stance /
trigger_relation / anachronism_status) is RETAINED; v7 adds the access gate that governs whether
a specific citation is permitted, and consolidates the verification fields into a 3-axis block
(anchor_existence × claim_fidelity × inference_tier) applicable only under actual access.

**v7 design principle**: The textbook anchor must be REAL, not recalled. Memory-based specific
citation produces systematically confabulated anchors (kumada1972 sweep confirmed TOC-level
confabulation: "Crabtree Ch.9 Kumada Coupling section" — no such section; Ch.9 is "Homogeneous
Catalysis"). v7 forbids the anchor's specificity from exceeding the access actually obtained.

**v7 promotion requirements** (must demonstrate before v7 → production):
- (a) Zero access-gate breaches: no V4-Q with a specific textbook-location citation under
  access_mode ∈ {concept_level_no_citation, bibliographic_anchor_only}
- (b) On a paper with actual textbook access (user supplies the relevant textbook PDF/excerpt OR
  the model reads it via Read tool), ≥1 V4-Q achieves anchor_existence=confirmed + claim_fidelity=faithful
  (the state that was 0 of 7 under memory-based v6)
- (c) On a paper WITHOUT access, all textbook anchors correctly degrade to concept_level_no_citation
  (no confabulated specific citations) while the conceptual gap-detection (「綻び」 questions) still
  functions
- (d) v6 anchor-genesis criteria (a)-(d) preserved on the conceptual layer

**Relation to prior pilots**: The n=11 v3 baseline + v5/v6 boyer1973 + kumada1972 pilots were all
generated under memory-based-allowed paradigm. Their conceptual gap-detection layer may survive;
their specific textbook citations are now considered unreliable (see v6→v7 changelog CHANGE (6))
and require regeneration under v7 (actual access) before any specific textbook citation is used
in a manuscript.

---

## Notes on pilot status (v6 update — anchor-genesis schema PILOT, 2026-05-28)

**V4 v6 status**: **PILOT** — anchor-genesis schema (stance + trigger_relation + anachronism_status)
layered on v5 page-level anchor base. v5 machinery FULLY RETAINED. v4 typology / classification rules
unchanged. v6 adds anchor-genesis machinery only.

**v6 design principle**: Preserve the GENESIS of each question (paper_anchor × stance × external_anchor
× trigger_relation → question), not only the question text. Closed taxonomies are explicitly REJECTED
in favor of open enum + mandatory free-text rationale.

**v6 promotion requirements** (must demonstrate before v6 → production):
- (a) **trigger_relation applicability**: ≥ceil(0.8·N) V4-Q items have natural primary_type (not "other"), where N = total V4-Q count in this pilot (target 8–15); when "other" is used, subtype is explicit; explanation field is paper-and-anchor-specific (not boilerplate)
- (b) **anachronism_status natural distribution**: pilot output exhibits a natural mix across contemporary-plausible / retrospective-only / uncertain (not collapsed to a single value); rationale field populated with substantive item-specific justification
- (c) **gap_type ↔ trigger_relation independence**: ≥1 cross-axis multi-valence case observed (same G_i with different trigger_relation, OR same trigger_relation with different G_i), confirming the diagnostic table is heuristic-only, not validation
- (d) **rationale quality**: ≥ceil(0.8·N) V4-Q items rated "substantive" across all three mandatory rationale fields (stance / trigger_relation / anachronism_status); "boilerplate" rate ≤ floor(0.12·N) per field (rounds to 1 for N=8–9, 2 for N=10–15)
- (e) **v5 criteria retained**: anchor granularity gain measurable, hallucination-risk surface acceptable, no v4 typology regression

**Pilot deployment**: First v6 pilot to be run on boyer1973 (`papers/sandbox/38_boyer1973/`) for
direct comparison with v4 baseline (`boyer1973_v184_sonnet_s1_v4pilot_20260526.md`) and v5 baseline
(`boyer1973_v184_sonnet_s1_v4pilot_v5_20260528.md`). Output naming convention:
`boyer1973_v184_sonnet_s1_v4pilot_v6_20260528.md`.

**Scope clarification**: v6 modifies the V4 (Turn 4 textbook-equipped reader) prompt INTERNAL schema
only. V1 (own-field expert) / V2 (adjacent-field) / V3 (methodology) prompts are UNCHANGED. V1–V3
unification into a parallel anchor-genesis schema is deferred to v7 OR to a Stage 2 adapter that
post-processes V1–V3 outputs into v6-compatible structure.

---

## Notes on pilot status (v5 update — page-level anchor extension PILOT, 2026-05-28)

**V4 v5 status**: **PILOT** — page-level anchor extension + textbook_quote_status taxonomy layered
on production v4 base. v4 typology / classification rules unchanged (all v4 validations still hold).
v5 adds anchor-granularity machinery only.

**v5 promotion requirements** (must demonstrate before re-labeling v5 → production):
- (a) **Anchor granularity gain measurable**: on a re-run of an existing v4-analyzed paper (e.g.,
  wakamatsu1971 or boyer1973), v5 produces ≥1 V4-Q with page-level anchor OR ≥1 V4-Q with
  paraphrased canonical claim, beyond what v4 produced
- (b) **Hallucination-risk surface acceptable**: paraphrased items can be
  verified by user against original textbook with ≥80% accuracy (user spot-check)
- (c) **No regression on v4 typology**: gap_type distribution + classification rule output unchanged
  vs v4 re-run on same paper

**v4 production status retained below** (v5 inherits, does not invalidate):

**V4 v4 status**: **PRODUCTION** — all cross-domain validations confirmed (n=10 pilot complete).
Suitable for deployment in all disciplines where a discipline-appropriate textbook corpus exists.

**Completed validation** (v1 + v2 + v3 + v4 data, n=10 total):
- ✅ Success criteria n=2 (boyer1973 + hayaishi1957): all 5 criteria PASS
- ✅ **G7 formally adopted: n=6 Δt≥40y papers all show G7≥1** (hayaishi1957 / slater1950 / boyer1973 / beinert1983 / demeis1984 / **kumada1972 organometallic**)
- ✅ **G7 absent in Δt<30y: CONFIRMED n=2** (kuninobu2015 Δt≈11y: G7=0; hoque2022 Δt≈2y: G7=0)
- ✅ **G7-boundary subtype CONFIRMED cross-domain** (weber1993 biochemistry Δt≈31y: G7-boundary=2; **murai1993 organometallic Δt≈31-33y: G7-boundary=2** — exact numerical match cross-domain)
- ✅ **G7 cross-domain CONFIRMED** (kumada1972 organometallic Δt≈54y: G7=3 strict; domain-independent temporal marker)
- ✅ **G7 density ↔ mechanism-proximity correlation CONFIRMED cross-domain** (density=3: slater1950 / beinert1983 / demeis1984 / **kumada1972 organometallic** = direct mechanism papers; density=1: boyer1973 / hayaishi1957 = peripheral foundational)
- ✅ **Three-zone G2 gradient CONFIRMED cross-domain**: modern (44-46%) > Δt≈31y zone (23%, both weber1993 and murai1993) > foundational (0-17%)
- ✅ **G2 elevation at n=2 modern controls**: kuninobu2015=44%, hoque2022=46%; 2× elevation vs foundational range 0-17%
- ✅ **anticipates_canonical ≥2 in all n=6 foundational papers; absent in modern controls n=2**
- ✅ **anticipates_canonical=4 "canonical formation paper" sub-category confirmed** (beinert1983)
- ✅ **anticipates_canonical=3 "paradigm-initiating paper" sub-category confirmed** (kumada1972 organometallic)
- ✅ **anticipates_canonical=2 + G7-boundary=2 "resolution-imminent discovery paper" sub-category confirmed** (murai1993 organometallic + weber1993 biochemistry — cross-domain)
- ✅ **Co-location structural pattern confirmed**: G7-boundary instances = anticipates_canonical instances in resolution-imminent papers (murai1993)
- ✅ **Combined classification rule: 10/10 accuracy** (n=10 pilot)
- ✅ G4+G5 NOT foundational-specific CONFIRMED: G4+G5 present across all paper types; less discriminating than G7
- ✅ **86% combined coverage ceiling confirmed**: R1-type external paradigm items (~1/7 per foundational paper) structurally uncoverable by both UQS and V4
- ✅ **G_novel-GE sub-type candidate registered** (hoque2022): "Geometric/electronic attribution indeterminacy" — paper attributes selectivity to geometric mechanism when textbook electronic mechanism (Hammett framework) provides equally sufficient explanation; chemistry-specific G_novel candidate

**Combined classification rule (v4 UPDATED — 3-category)**:
```
G7≥1 + anticipates_canonical≥2                           →  foundational/contributing paper
G7=0 + G7-boundary≥1 + anticipates_canonical≥1           →  resolution-imminent discovery paper
                                                               (Δt ≈ 30-39y; "resolution-imminent discovery paper")
G7=0 + G7-boundary=0 + anticipates_canonical=0           →  modern control paper
Accuracy: 10/10 = 100% (n=10 pilot; biochemistry n=7 + organometallic n=3)
```

**Structural ceiling note (v2 NEW)**:
The empirical ceiling of ~86% combined coverage (UQS + V4) for Reflection
oracle items reflects a structural property: approximately 1/7 Reflection
items per foundational paper require **external historical-paradigm
awareness** (the paradigm the paper was overturning, not stated in the
paper itself). These are NOT prompt deficiencies — they are in the
territory of V5 (paradigm-disruption oracle) / V6 (hindsight oracle)
and cannot be recovered by textbook or paper grounding alone.

**Production promotion criteria (v4: ALL CONFIRMED)**:
1. ✅ **Cross-discipline validation** (organometallic chemistry cross-domain):
   kumada1972 (Δt≈54y, G7=3) + murai1993 (Δt≈31-33y, G7-boundary=2) + hoque2022 (Δt≈2y, G7=0)
   all confirmed; G7 pattern holds cross-domain without calibration adjustment
2. ✅ **G2 elevation hypothesis** (modern papers show elevated G2 vs foundational):
   kuninobu2015=44%, hoque2022=46% vs foundational range 0-17%; 2× elevation CONFIRMED at n=2
3. ✅ **G7-boundary subtype cross-domain validation**:
   weber1993 (biochemistry) + murai1993 (organometallic) — both Δt≈31y, both G7-boundary=2;
   domain-independent threshold CONFIRMED

**Deployment guidance (production)**:
- Use for any paper with a discipline-appropriate textbook corpus available
- Apply the 3-category combined rule for paper temporal classification
- Report G2 rate alongside G7/G7-boundary counts for three-zone placement
- Flag G_novel-GE when both geometric and electronic mechanisms are available to explain a selectivity trend
