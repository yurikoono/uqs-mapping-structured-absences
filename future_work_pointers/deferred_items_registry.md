# Deferred Items Registry — Phase 2 and Beyond

**Created**: 2026-04-20
**Purpose**: Comprehensive registry of all items explicitly deferred beyond the current Digital Discovery submission. Each item links to its authoritative source; this registry does not duplicate content from `improvements/open_issues.md` or `si_issues_log.md`.

**Reading order**: §1 methodology validation → §2 scope expansion → §3 cross-vendor / cross-model → §4 language study → §5 ChemOntology pilot execution → §6 open prompt-level issues from the v15→v17 cycle → §7 figure/table updates → §8 references and data availability.

---

## §1. Methodology validation

### §1.1 Tier 1 advisor-evaluation pilot (full systematic)
- **Scope**: n ≥ 5 advisors × 2–3 papers (see `pilot_evaluation_issues.md` §G pre-flight checklist)
- **Target deliverable**: dedicated Phase 2 methods paper OR substantial SI-8.5 update in a follow-on submission
- **Authoritative source for issues**: [`pilot_evaluation_issues.md`](pilot_evaluation_issues.md) (this folder)
- **Connected submission note**: SI-8.5 is a placeholder pending this work
- **Dependencies**: advisor recruitment network, rewriter-script development (§1.2), response-form template (§1.3)
- **Blockers resolved before Phase 2 start**: see pre-flight checklist in `pilot_evaluation_issues.md` §G

### §1.1C Tier 1C — UQS-as-review-scaffold bias-reduction study (added 2026-05-08)

- **Context**: User observation (2026-05-08) — human reviewers default to specialty-confined perspective; this bias is structurally hard to overcome via individual reviewer effort. UQS, deployed as a peer-review scaffold, structurally reduces five identifiable reviewer biases (specialty-confined questioning blindness, single-perspective dependency, implicit defect-bias, impressionistic critique, era-norm anachronism). This study empirically tests whether the structural reduction is observable. Until the study runs, the bias-reduction claim is a *hypothesis* in Paper C and grant proposals; this study upgrades it to *empirical*.
- **Hypothesis (pre-registered, refined 2026-05-09 v2 to incorporate refined Metric 7 = constructive conversion rate)**: reviewers using UQS scaffold produce reviews with simultaneously (a) higher anchor rate of absence claims (rigor), (b) higher defect-vs-opportunity separation rate (meta-cognitive surfacing), (c) higher cross-specialty coverage of comments (specialty-confined-questioning-bias reduction), (d) **lower unnecessary-revision-demand rate** (bounded-scaffold validation — comments that are next-research-project disguised as defect should *decrease*), (e) higher comment transparency / explainability, (f) lower era-anachronism rate, (g) **higher constructive conversion rate** (third-axis validation — among comments that identify a deficiency / absence / limitation, the fraction that come accompanied by a specific direction in which the author can strengthen the scientific contribution; UQS scaffold should structurally support reviewers who choose to convert criticism into direction-of-growth). The simultaneous *increase* in coverage AND *decrease* in unnecessary demands AND *increase* in constructive conversion rate is the signature of a bounded constructive-elevation review scaffold; if UQS only increases coverage without decreasing unnecessary demands, it re-positions as a critique-amplification tool; if UQS increases coverage and decreases unnecessary demands but does not shift the constructive conversion rate, the bias-reduction claim survives but the constructive-elevation claim is unsupported (still a positive but weaker outcome).
- **Critical caveat for Metric (g) — refined 2026-05-09 v2**:
  - **Why constructive conversion rate (and not constructive-vs-gatekeeping ratio)**: the earlier-draft metric "constructive-vs-gatekeeping ratio" was vulnerable to *lenient review* gaming — a reviewer who writes only soft, constructive comments without valid criticism would score artificially high. The refined metric uses *valid criticism comments as the denominator*, so lenient reviews have small denominators and cannot inflate the metric. The metric measures **conversion skill** (criticism → direction-of-growth), which directly tests the editorial-intelligence framing of Axis 3.
  - **Correlation, not causation**: the metric measures correlation only — UQS scaffold may attract constructive-disposition reviewers (selection bias) rather than transforming gatekeeping reviewers into constructive ones. Tier 1C analysis must distinguish "scaffold supports the disposition" (operational claim, defensible) from "scaffold creates the disposition" (over-claim, indefensible). Reviewer randomization across A/B groups partially controls for selection; full causal inference requires within-reviewer crossover design (reviewer reviews 2 papers, one with scaffold and one without) which may not be feasible at pilot scale.
  - **Direction quality must be assessed separately**: a high constructive conversion rate does not mean the directions are good — they can be wrong, premature, or off-target. Tier 1C should pair this metric with a separate **substantive accuracy** assessment (directions rated post-hoc by independent domain experts on a 1-5 scale for technical correctness and value), so that "high conversion rate + low direction quality" is detectable as a different failure mode (UQS scaffold makes reviewers more talkative without necessarily wiser).
- **Design**: A/B comparison study. 5–10 reviewers per group, 2–3 papers selected to cross specialty boundaries (e.g., synthesis paper assigned to polymer-chemistry reviewers and to mechanistic-chemistry reviewers; reviewers reviewing in their non-primary specialty). Group A receives paper + UQS scaffold (EP dictionary, key_quote anchoring template, dual-layer VQ guide, defect/opportunity deferral note, **explicit bounded-scaffold instruction that not every mapped absence is a revision demand**, **constructive-elevation framing reference** that absences may be articulated as direction-of-growth rather than absence-as-failure); Group B receives paper only. Both groups submit reviews using the same response form. Compare across groups on the seven hypothesis metrics.
- **Output**: empirical demonstration of bias reduction (or refutation, which would refine the value proposition). Basis for Paper C empirical support and for grant submissions to research-integrity / meta-science funding streams (see `project_uqs_reviewer_bias_reduction.md` for funding angle).
- **Sequencing**: should follow §1.1 Tier 1 advisor pilot (pilot validates UQS output quality first; bias-reduction study tests deployment as scaffold). Earliest realistic execution: post-Paper-A publication, post-Tier-1-pilot.
- **Dependencies**: reviewer recruitment via co-authors' networks (cross-specialty); access to 2–3 papers with sufficient cross-specialty interest; statistical-comparison expertise for the A/B analysis (basic R / Python suffices); ethical clearance similar to Tier 1 (anonymization, consent, withdrawal rights).
- **Distinct from Tier 1A/1B**: Tier 1A (existing §1.1) evaluates UQS output quality with experts as evaluators (UQS as object). Tier 1B (mentioned in `project_paperB_system_selection_logic.md`) measures computational-chemist alignment on system selection for a given EP gap (UQS as design constraint). Tier 1C (this entry) measures bias reduction when UQS is deployed as scaffold for reviewers (UQS as scaffold). Three distinct study designs; do not conflate.
- **Authoritative source**: `memory/project_uqs_reviewer_bias_reduction.md` for full mechanism articulation, hypotheses, and deployment guidance.

### §1.1D Tier 1D — Adjacent-field selection criteria validation study (added 2026-05-09)

- **Context**: User observation (2026-05-09) — UQS Stage 1/2 currently delegates adjacent-field selection (which neighboring fields' perspectives drive U-item generation) entirely to LLM internal judgment, without explicit criteria. Qualitative cross-vendor differences observed (n=1: Claude relatively reasonable, Gemini sloppier). This unarticulated layer in the methodology weakens three UQS claims: (i) cross-vendor convergence (vendor-noise channel from differing field-set choices), (ii) reproducibility / specification framing (specification cannot include a layer that is not specified), (iii) specialty-confined-questioning-bias reduction (LLM training-distribution bias in field choice). Phase 3 cross-genre expansion (registry §2.5) compounds the problem because LLM "adjacent fields" judgment is strongest in chemistry and weakens in legal / medical / policy / historical genres. Tier 1D empirically validates that explicit selection criteria reduce vendor divergence.
- **Hypothesis structure (pre-registered, refined 2026-05-09 v2 with Core/Exploratory distinction)**: applying the proposed 4-layer adjacent-field selection framework (Layer 1 citation-graph / Layer 2 methodological proximity / Layer 3 conceptual overlap with **explicit anchoring constraint** to named concept/mechanism/variable/representation/explanatory-gap / Layer 4 stakeholder proximity), with required **5-tuple selection record** (layer + evidence_basis + question_lens + core_or_exploratory + confidence) per selected field, produces three simultaneous outcomes:
  - **H1 (core convergence)**: substantially higher cross-vendor Jaccard overlap for *Core adjacent fields* under Condition B vs. A. Headline test of criteria effectiveness.
  - **H2 (exploratory divergence preservation)**: vendor divergence is *not* suppressed for *Exploratory adjacent fields* under Condition B. Vendor-specific creative selection is preserved as research-program-design asset. Headline test that criteria do not over-restrict.
  - **H3 (mainstream-bias reduction)**: substantially lower mainstream-bias index under Condition B — explicit Layer 1-4 criteria force inclusion of less-mainstream fields when warranted, counteracting LLM training-distribution bias.
  - **Joint signature**: H1 + H2 + H3 simultaneously is the signature of *"criteria ensure reproducibility without sacrificing creativity"*. Failure of H2 alone would refute the Core/Exploratory distinction's value; failure of H1 would refute the entire framework; failure of H3 would refute the bias-reduction claim of Axis 1.
- **Design**: 2 × N factorial. Two conditions:
  - **Condition A (current state)**: no explicit selection criteria; LLM picks adjacent fields freely as in current UQS prompts.
  - **Condition B (proposed criteria)**: prompt explicitly applies the 4-layer framework and requires selection-record format (yaml schema with Layer ID + criterion + evidence per field).
  
  Each condition is run on 3-5 Kumada-lineage papers (and 2-3 Phase 3 cross-genre papers if Tier 1 cross-genre pilot is underway by Tier 1D start) across 4-5 vendors (Sonnet / Opus / GPT / Gemini / DeepSeek if available).
- **Metrics (refined 2026-05-09 v3 with 3-level overlap measurement, GPT review v5)**:
  1. **3-level overlap measurement (replaces single-Jaccard metric)**: field-name Jaccard alone undercounts agreement (different field names can share lens) and overcounts agreement (same field names can have different lenses). Measure overlap at three levels per vendor pair, separately for Core and Exploratory tiers:
     - **Field-level overlap (Jaccard on field names)** — coarsest measure; baseline comparable to earlier draft
     - **Lens-level overlap (Jaccard on `question_lens` content)** — measures whether vendors agree on *what to look for*, regardless of field-name surface form
     - **Absence-type overlap (Jaccard on absence categories surfaced via the selected lenses)** — measures whether vendors arrive at the same kinds of absences end-to-end
     For Core tier, all three should rise under Condition B (H1). For Exploratory tier, all three should remain divergent (H2).
  2. **Layer-distribution profile** — which Layer (1-4) of fields each vendor over/under-selects per condition. B should show more uniform distribution across Layers 1-4; A typically shows concentration in Layers 1-2 (citation / methodological — easier for LLM) with under-representation of Layers 3-4 (conceptual / stakeholder — harder).
  3. **5-tuple completeness rate** — fraction of selected fields with all 5 tuple elements (layer + evidence_basis + question_lens + core_or_exploratory + confidence) populated. B ≈ 100% by prompt construction; A ≈ low.
  4. **Mainstream-bias index** — fraction of selected fields that are LLM-popular (field publication-count proxy > median). H3: B substantially lower than A.
  5. **Layer 3 anchor compliance rate** — fraction of Layer 3 selections that cite one of the five permitted anchors (named concept / mechanism / variable / representation / explanatory gap), explicitly present OR latent-with-reconstruction-source-cited per the v3 refinement. B ≈ 100% by prompt; A typically zero. This is a sub-metric capturing Layer 3 specifically, the highest-risk layer.
  6. **Exclusion-record completeness rate (added v3, GPT review v5; bounded v4 GPT review v6)** — fraction of analyses that include `excluded_candidate_fields` records with `reason_for_exclusion` and `status` populated, capped at the 3-5 per-run boundary. B ≈ 100% by prompt; A typically zero. Tests whether the specification's bounded completeness-record requirement is actually satisfied.
  7. **Sampling-budget compliance rate (added v4, GPT review v6)** — fraction of analyses that fall within the prescribed lens_sampling_budget ranges (Core 3-5 / Exploratory 1-3 / excluded 3-5). B ≈ 100% by prompt construction; A varies (LLM in Condition A may select any number of fields without budget awareness). Tests whether the stopping rule is actually applied. Sub-metrics: Core-budget compliance / Exploratory-budget compliance / Excluded-budget compliance separately.
  8. **U-item provenance completeness rate (added v4, GPT review v6)** — fraction of generated U-items that contain `originating_lens` field with at minimum `question_lens` content and `core_or_exploratory` status, AND whose `originating_lens` content matches one of the lenses recorded in the analysis's lens-selection block. B ≈ 100% by prompt construction; A typically zero (Condition A does not request provenance). Tests whether the evidential chain from selection criteria → selected lens → generated U-item is auditable. This metric is the **most important specification-compliance test** because it validates that the entire upstream specification pipeline is actually traceable from output back to selection criteria.
  9. **Layer 3 anchor_status completeness rate (added v4, GPT review v6)** — for Layer 3 selections specifically, fraction that contain mandatory `anchor_status` field with one of the two permitted values (`explicit_in_target_paper` / `reconstructably_latent_not_explicit`). For latent selections, additionally verify reconstruction_basis cites one of the four permitted reconstruction sources. B ≈ 100% by prompt; A typically zero. Sub-metric of Metric 5 (Layer 3 anchor compliance) capturing the explicit/latent distinction.

- **Why 3-level overlap matters (v3 articulation)**:
  - Field-only Jaccard would misclassify cases where Claude says "organometallic chemistry" with lens "Ni cycle mechanism" and GPT says "catalytic mechanism" with lens "Ni cycle mechanism" — same intent, different label, marked as disagreement at field level.
  - Field-only Jaccard would also misclassify cases where two vendors both say "computational chemistry" but one's lens is "spin-state ordering" and the other's is "solvation models" — same field name, different intent, marked as agreement at field level.
  - Lens-level Jaccard captures *true methodological convergence*; absence-type Jaccard captures *end-to-end output convergence*. Field-level remains useful as the most easily computable comparison and as baseline for cross-checking the more sophisticated metrics.
- **Output**: empirical demonstration that explicit selection criteria reduce vendor noise; basis for upgrading the UQS specification (registry §9.1) to mandate the 4-layer framework as a required compliance component. Also: empirical anchoring for the Paper A limitation acknowledgment text (see `memory/project_uqs_adjacent_field_selection.md`).
- **Sequencing**: can run independently of Tier 1A (advisor pilot) and Tier 1C (reviewer-bias-reduction); does not require Paper A publication. Could be executed as a methodology-internal study during Paper C drafting, with results feeding Paper C specification framing.
- **Distinct from Tier 1A/1B/1C**:
  - Tier 1A (§1.1) — UQS output quality with experts as evaluators (UQS as object)
  - Tier 1B (`project_paperB_system_selection_logic.md`) — computational-chemist alignment on system selection (UQS as design constraint)
  - Tier 1C (§1.1C) — bias reduction when UQS deployed as scaffold for reviewers (UQS as scaffold)
  - **Tier 1D (this entry)** — adjacent-field selection criteria validation (UQS as methodology with currently-implicit layer made explicit). Methodology-internal study; does not require external evaluators beyond multi-vendor LLM access.
- **Dependencies**: multi-vendor LLM API access (already required for cross-model verification protocol); citation-graph data access (WoS / Scopus / Semantic Scholar) for Layer 1 operationalization; field-publication-count proxy for mainstream-bias index calculation.
- **Authoritative source**: `memory/project_uqs_adjacent_field_selection.md` for full framework articulation, layer definitions, cross-genre extension protocol, and Paper A / Paper C deployment guidance.
- **Specification freeze status (added v5 GPT review v7, 2026-05-09)**: The expert-lens sampling specification has reached v0.1 freeze with 6+1 structural components (4-layer + 5-tuple + excluded fields + Core/Exploratory + Layer 3 anchoring + sampling budget + U-item provenance). **No further specification components are to be added without empirical trigger** — Tier 1D execution results, Paper C drafting feedback, or cross-genre demonstration findings (registry §2.5) are required to promote any new component from "Future-version candidate" to "active v0.2 specification". This freeze prevents specification bloat from continued conceptual articulation in successive sessions. The next phase of work in this area is **empirical (Tier 1D execution)**, not conceptual (further memory edits). Future-version candidates registered in `memory/project_uqs_adjacent_field_selection.md` Future-version candidates section: (1) three-tier Core/Peripheral/Exploratory layering; (2) full lens-centric design replacing field-centric; (3) confidence-calibration method standardization; (4) multi-vendor compulsory cross-check at lens-selection level; (5) per-genre EP dictionary fork governance. Each requires explicit empirical trigger before promotion.

### §1.2 Rewriter script (Stage 1 / D-4 → student-question form)
- **Target file**: `scripts/convert_to_student_questions.py` (not yet written)
- **Dependency**: LLM API access + prompt design for rewrite task
- **Quality-assurance checklist**: preserve (a) specific object, (b) anchor in paper, (c) absence being pointed at; cross-validate via second model or human
- **Estimated effort**: 3–5 days

### §1.3 Response-recording form template
- **Target file**: `scripts/pilot_form_template.md` (Google Forms / Qualtrics specification)
- **Fields required**: item ID, category selection (vi-alternative list), confidence, time-per-item, free-text comment, meta-evaluation prompt at session end
- **Estimated effort**: 2–3 days

### §1.4 Consent form and advisor-instruction cover sheet
- **Target files**: `docs/pilot_consent_form.md`, `docs/pilot_advisor_instructions.md`
- **Content**: data-use statement, anonymization policy, right to withdraw, verbatim advisor prompt from Methods 6
- **Estimated effort**: 1–2 days
- **Institutional dependency**: IRB exemption / minimal-review determination from the author-group's institution

### §1.5 Tier 2 collective-pattern-use record infrastructure
- **Scope**: how recurring_roots, group_unasked_question, and temporal_trajectory Stage 2F outputs are presented to researchers, how use cases are recorded, what fields the use-case log captures
- **Target deliverable**: protocol specification + template; deferred to Phase 2 or later
- **Authoritative source**: SI-8.3 (present draft is sufficient for submission but not operationalized)

### §1.6 Limited expert verification
- **Scope**: 1–2 experts × 2–3 papers, verification of positional accuracy and inference-tier accuracy on Stage 1 output
- **Status**: protocol defined in SI-8.4 but not yet executed
- **Target deliverable**: pre-submission OR Phase 2; depends on pilot timing decisions

### §1.7 Codebook v0.3 (PRI → RI promotion, EP-10a formalization)
- **Context**: PRI-11 (Mechanism-kinetics decoupling) was re-derived in five sources in 2026-04-19 cross-model validation; should be promoted from paper-specific PRI to RI-11 in the next Codebook revision. EP-10a is now in the SI-3 dictionary (see SI-3 preamble update 2026-04-19).
- **Updated evidence for PRI-11 promotion (2026-04-21)**: The UQS self-analysis of Yamamoto-Hayashi-Yamamoto 1978 *BCSJ* (see §1.14 completion) surfaced PRI-11 as a **third independent confirmation case** (after Breitenfeld 2014 and Pengfei 2024). Fig. 3 time-course kinetic data is used in Yamamoto 1978 to support Scheme 1 mechanism without algebraic rate-law derivation from the proposed cycle — matching PRI-11's definition exactly. Yamamoto 1978's S3v2 output §6 documents this explicitly as a PRI-11 confirmation. **The 3-paper independent confirmation threshold is now met**; PRI-11 → RI-11 promotion is recommended for the v0.3 revision.
- **Updated evidence for EP-10a formalization (2026-04-21)**: The same analysis also demonstrated the **first independent application of EP-10a outside Kumada 1972** (Yamamoto 1978's SRG-3 binds rate-law absence to EP-10a as the Kinetic verification pack target). This cross-paper applicability supports EP-10a's generality and reduces the concern that EP-10a was a single-case artifact. Codebook v0.3 should record this second-case confirmation.
- **Target**: Codebook v0.3 specification document
- **Authoritative source**: SI-3 preamble, `improvements/stage4_literature_update_20260419.md`, and now `papers/ep/kumada1972/yamamoto1978/yamamoto1978_v17_sonnet_s3v2.md` §2 (SRG-3), §3 (VQ judgment), §6 (Codebook contribution).

### §1.8 v18 prompt revision — **first-priority scope (2026-04-22 upgrade)**

- **Context — two layers**:
  - **Layer A (original, from SI-6.6)**: VQ judgment divergence across four models reflects implicit era-norm choice, not capability difference. Opus 4.7's dual-layer reporting resolves this; the v18 prompt should require all models to report both era-norm VQ and modern-era VQ explicitly.
  - **Layer B (added 2026-04-22)**: the Stage 4 filling-type label "Paradigm-shift" shows cross-model instability that the VQ dual-layer fix does not address. Per the SI-6.6 end-of-section analysis, only 2 of 4 models used Paradigm-shift at all; Sonnet JA / GPT-5.4 used Partial where Opus 4.7 / Sonnet EN used Paradigm-shift; Haiku substituted non-five-type vocabulary. The instability originates not in era-norm choice but in the **absence of an operational criterion** in the current Stage 4 v2 prompt for the concept-level judgment "is the source paper's question answered in the source's framework, or in a replacement framework?" — the definitional heart of the Paradigm-shift category.
- **v18 proposal — two items**:
  1. Require dual-layer VQ reporting (Layer A, unchanged).
  2. **Articulate an operational criterion for the Paradigm-shift filling-type label** (Layer B, new). Specifically, the Stage 4 prompt should provide: (i) a definitional frame distinguishing "question answered in source framework" (→ Complete / Partial / Indirect) from "question reformulated in replacement framework" (→ Paradigm-shift); (ii) 2–3 diagnostic questions the model should answer before assigning the label (e.g., *"Does the candidate paper treat the source paper's mechanistic entities as obsolete?"*, *"Does the candidate paper claim its finding implies the source paper's framework cannot handle the case?"*, *"Does the candidate paper cite the source paper as historical context rather than as a shared framework?"*); (iii) concrete examples paired with counter-examples at the level of specific Kumada-1972-family candidates (e.g., Vicic 2004 Ni(I)/Ni(III) = Paradigm-shift because it replaces Ni(0)/Ni(II); Tamao 1976 BCSJ Full Paper = Partial not Paradigm-shift because it stays within the Ni(0)/Ni(II) framework).
- **Methodological significance — watershed argument (2026-04-22)**: articulation of the Paradigm-shift criterion is the boundary between a methodology that remains LLM-assisted (where the concept-level call is an implicit judgment internal to the model) and one that is transferable to human analysts (where the criterion is articulated enough to be reproducibly applied by non-LLM readers). This is why Layer B is first-priority rather than a polish item. Recorded as a core v18 scope expansion, not an optional extension.
- **Target**: `prompts/v18/` directory, Stage 3 v3 prompt revision (Layer A), Stage 4 v3 prompt revision (Layer B).
- **Dependencies**: draft proposals benefit from the empirical base registered in §1.15 (cross-model agreement study with dimensional-adequacy test) once executed, but v18 Layer B draft can begin before §1.15 runs, with post-empirical refinement.
- **Authoritative source**: [`SI-6.md`](../manuscript/si/output/SI-6.md) §SI-6.6 (both the original VQ divergence analysis and the 2026-04-22 Stage-4 filling-type divergence addendum); Discussion 3 end-paragraph (section file `discussion_en.md` and `discussion_ja.md`, propagated to integrated manuscripts).

### §1.9 Table 4 / Layer A EP-10a mapping update
- **Context**: The EP-to-ChemOntology-AFIR parameter mapping (`chemontology_pilot/layer_A_parameter_mapping/ep_to_chemontology_mapping.md`), which underlies manuscript Table 4 and Discussion 2, was constructed before EP-10a (Kinetic verification pack) was added to the Kumada 1972 dictionary on 2026-04-19. The current Table 4 covers nine EPs (EP-01a through EP-09a). A preliminary mapping sketch for EP-10a is noted in the Layer A document's "Scope of mapping" section: target parameters = RCMC kinetic-navigation output + rate-law extraction; required ERPOs = same as EP-06a with time-resolved population flux; expected output = Arrhenius-like rate expressions per elementary step.
- **Target**: revised Layer A mapping document (10 EPs), revised manuscript Table 4, minor Discussion 2 prose update removing the Phase 2 deferral.
- **Authoritative source**: [Discussion 2 of `discussion_en.md`](../manuscript/sections/discussion_en.md) and `chemontology_pilot/layer_A_parameter_mapping/ep_to_chemontology_mapping.md` "Pending Phase 2 update" note.
- **Dependencies**: does not block submission; is not on the critical path for the present manuscript. Co-author review required before finalizing EP-10a mapping cells (bidentate Ni-P phosphine + kinetic model).

### §1.10 Methods 6 preliminary expert verification — systematic Phase 2 study
- **Context**: Methods 6 "Limited expert verification" is repositioned in the current manuscript as preliminary and qualitative; inter-rater-reliability (IRR) statistics are not reportable from n = 2–3. The Phase 2 systematic study is specified in [`pilot_evaluation_issues.md`](./pilot_evaluation_issues.md) §A-3.
- **Target**: expert panel with n ≥ 5 advisors, per-item {positional, inference-tier} accuracy assessment, Cohen's κ per pair and Fleiss's κ across panel, as per `pilot_evaluation_issues.md` A-3 target.
- **Authoritative source**: [Methods 6 of `methods_en.md`](../manuscript/sections/methods_en.md), [`SI-8.md` §SI-8.4](../manuscript/si/output/SI-8.md), [`pilot_evaluation_issues.md` §A-3](./pilot_evaluation_issues.md).

### §1.11 Reference 30 citation verification (Chen et al. 2019)
- **Context**: References 26–31 were added to the main manuscript References list on 2026-04-21 to support Vancouver-style citation of Layer-1 papers and cross-model-identified filling papers (Results Part 3). Reference 30 (Chen et al. *J. Am. Chem. Soc.* 2019, Kumada-system mechanism-kinetics unification) has a placeholder bibliographic stub; the full citation (page range, exact author list order) is pending co-author confirmation. References 26–29 and 31 are complete.
- **Related**: Handoff §5.2 M5 listed refs 8, 9, 10, 11, 18 as uncertain at the 2026-04-17 handoff; refs 26–29 and 31 are now added based on SI-4.9 cross-model validation; ref 30 joins the "to-verify" list.
- **Target**: confirm ref 30 full citation with co-authors; if Chen 2019 is not an appropriate reference, identify the intended paper.
- **Authoritative source**: [References list in `manuscript_en.md`](../manuscript/sections/manuscript_en.md), [SI-4.9 cross-model filling-paper update](../manuscript/si/output/SI-4.md), [`improvements/stage4_literature_update_20260419.md`](../improvements/stage4_literature_update_20260419.md).

### §1.12 Principal validation programme — multi-layer LLM-judgment dependency resolution

- **Context**: Discussion 4 explicitly acknowledges that UQS delegates judgment to a language model at multiple successive layers (Stage 3 EP definition; Stage 4 retrieval-term reverse-engineering, candidate evaluation, filling-type classification, three-tier detectability, per-candidate confidence). No external ground-truth filling-paper set exists, so precision and recall cannot be directly measured. Cross-model convergence provides *consistency* evidence but cannot establish independence because frontier models share substantial training-corpus overlap. The narrative scaffold (two-layer chronology, "49-year" interval, consolidating-Account exception) is analyst-imposed interpretation on top of the LLM candidate list.
- **Target validation programme (Phase 2, combined)**:
  1. **Independent human-expert annotation** of Stage 3 EPs and Stage 4 filling-paper classifications for at least Kumada 1972 and two additional anchor papers. Inter-rater reliability per §A-3 of `pilot_evaluation_issues.md`.
  2. **Citation-network analysis**: retrieve the full citation graph of papers citing Kumada 1972 (via WoS / Scopus / Semantic Scholar APIs; ≥ several thousand records); LLM-score each for EP-filling against the Kumada 1972 EP dictionary; compare distribution against the Stage 4 hand-identified candidate set.
  3. **Controlled repeated runs under temperature perturbation**: for a fixed EP, repeat Stage 4 retrieval at multiple sampling temperatures (e.g., T = 0.0, 0.3, 0.7) across at least 10 independent runs; report candidate-set stability and confidence-level calibration.
  4. **Citation-content hallucination audit**: systematic DOI resolution of every Stage 4 citation across all papers in the present study; identify all citation-content mismatches of the Yamamoto 1978 type; report the base rate.
  5. **Heck corpus benchmark**: run the restricted-scope LLM-vs-WoS comparison (SI-10 type) against the existing ~1,000-paper Heck corpus as a bounded ground-truth surrogate; report recall.
- **Authoritative sources**: [Discussion 4 "Multi-layer LLM-judgment dependency" in `discussion_en.md`](../manuscript/sections/discussion_en.md), [`SI-10.md` §10.6](../manuscript/si/output/SI-10.md), [`pilot_evaluation_issues.md`](./pilot_evaluation_issues.md).
- **Dependencies**: requires co-author recruitment of 5+ human annotators; requires WoS / Scopus API access; requires budget for repeated LLM runs. Not on the critical path for the present submission but is the principal follow-up programme.

### §1.13 Optional defect-vs-opportunity annotation pass

- **Context**: Discussion 4 "The defect / research-opportunity interpretation is external to UQS" establishes that the categorical output of UQS is structural, not normative. Whether a given absence is read as a reporting-hygiene defect or as an open research opportunity is deferred to the researcher, via Methods 6's Tier 1 advisor-evaluation protocol. This is a deliberate design choice (it preserves informational richness and avoids imposing a fixed evaluative frame on the reader), but it leaves a practical gap: researchers using UQS output for research planning or graduate supervision must perform this evaluation manually for each item. A machine-assistance layer for this judgment is an optional Phase 2 extension that could be useful without compromising the core design.
- **Proposed form**: An *annotation pass* — not a classification step — that, for each absence item, offers the researcher a side-by-side reading of two interpretations (defect framing vs opportunity framing) with relevant field-norm context (era-norm, comparable-paper coverage, cross-paper recurrence). The annotation pass is *presentational* rather than *decisional*: it structures the information the researcher uses to make the judgment, but does not substitute for the judgment itself.
- **Target inputs for the pass**: Stage 3 CLAs and A/B items where the two readings diverge most sharply (e.g., Kumada 1972 CLA-2 bidentate necessity); Stage 2F recurring_roots that appear in both reporting-hygiene and substantive research clusters; VQ-2 items with Tier 1 detectability and VQ-3 items with Tier 3 detectability (the cross-diagonal of the detectability × VQ matrix).
- **Rationale**: preserves the "categorical output × researcher judgment" separation established in Discussion 4, while acknowledging that the researcher-side judgment currently has no tooling support within UQS.
- **Authoritative source**: [Discussion 4 "The defect / research-opportunity interpretation is external to UQS" in `discussion_en.md`](../manuscript/sections/discussion_en.md); Methods 6 pointer in [`methods_en.md`](../manuscript/sections/methods_en.md).
- **Dependencies**: does not block submission; is a Phase 2 research direction on UQS tooling. Would require co-author consensus on whether to introduce any machine-assisted step into the reader-side reading, given the design principle that the reading is properly the reader's.

### §1.14 UQS self-analysis of Yamamoto-Hayashi-Yamamoto 1978 *BCSJ* 51, 2091 (hallucination-victim paper) — **COMPLETED 2026-04-21**

- **Status**: ✅ Completed the same day as registration. Executed via Sonnet agent in a single coherent session; 8 output files archived at `papers/ep/kumada1972/yamamoto1978/`. See that folder's `STATUS.md` for the full summary.
- **Original context**: The Opus 4.7 Stage 4 output on Kumada 1972 included a "Yamamoto-Kohara-Yamamoto 1978 *BCSJ* 51, 2091" citation that library-hardcopy verification (2026-04-21) revealed to be a **triple-mismatch citation-content separation hallucination** — see SI-10.3 (iv). The paper itself is the hallucination-victim record, not an EP-03a filler for Kumada 1972.
- **Key findings from the completed analysis**:
  - **8 EPs** in Yamamoto 1978's own dictionary (EP-01a, EP-03a, EP-04a, EP-05a, EP-06a, EP-08a, EP-09a, **EP-10a**) — the first independent application of EP-10a outside Kumada 1972, supporting EP-10a's generality.
  - **PRI-11 (Mechanism-kinetics decoupling) — third independent confirmation.** Fig. 3 kinetic profile used as mechanism support without algebraic rate-law derivation from Scheme 1. After Breitenfeld 2014 (proposal) and Pengfei 2024 (second case), Yamamoto 1978 clears the "3 independent confirmations" threshold for PRI → RI promotion. Directly feeds §1.7 below.
  - **"Second-generation non-filler" chain** established as a methodological observation: Kumada 1972 proposes intermediates without isolation → Yamamoto 1978 inherits the cycle and extends it to polycondensation (still without isolation) → Yamamoto 1981 provides first partial self-filling at the alkyl-analog level. Yamamoto 1978 is therefore **not a filler** for Kumada 1972's EP-03a; it is a paper that *inherits* that gap and rebinds it to a polymer-scale system.
  - **Scheme-labeling mismatch pattern** detected: "seems to proceed" hedge followed by factual-verb step descriptions. Candidate for inclusion in Phase 2 Codebook revision notes as a recurring rhetorical mode.
- **Authoritative source**: `papers/ep/kumada1972/yamamoto1978/STATUS.md` (full EP-inheritance summary and UQS-methodological findings).
- **Downstream impact**: §1.7 (Codebook v0.3) PRI-11 elevation now has 3-paper confirmation; consider moving PRI-11 → RI-11 in the next revision cycle.

### §1.15 Cross-model agreement on Stage 4 filling-type assignment (two-axis study)

- **Context**: An ad-hoc review of the four-model v17 Stage 4 outputs on Kumada 1972 (recorded at the end of SI-6.6, 2026-04-22) surfaced a divergence that the quantitative SI-6 table did not track: the **filling-type label** ("Complete / Partial / Indirect / Attempted / Paradigm-shift") assigned to specific candidate papers is unstable across models in ways not attributable to era-norm context choice. The divergence has three observed forms: (i) Paradigm-shift label used by Opus 4.7 and Sonnet English, not used by Sonnet Japanese or GPT-5.4; (ii) Haiku 4.5 substituting non-five-type vocabulary ("Attempted but Insufficient," "Communication-era tolerated," "Era-norm dependent") that may be read as structural dissatisfaction with the five-type vocabulary's implicit one-dimensionality; (iii) Sonnet 4.6 Japanese–English asymmetry under the same v17 prompt, consistent with a corpus-level hedging bias in Japanese academic prose.
- **Scope — all five filling types, not Paradigm-shift alone**: the 2026-04-22 observation focused on Paradigm-shift because the label's cross-model rarity made it visually salient. However, the agreement-quantification gap applies equally to the remaining four types (Complete / Partial / Indirect / Attempted). The SI-6.3 quantitative table did not report per-type agreement rates for any of the five. The study scope below is therefore uniformly applied to all five types; Partial-vs-Complete boundary cases in particular may exhibit quieter divergence that the ad-hoc review was not sensitive to. This scope alignment is noted in SI-6.6's final bullet (2026-04-24 addition following external Opus review feedback) and in the Conclusions null-finding hedge.
- **Scope — two-axis study**:
  - **Axis 1: quantitative agreement on filling-type assignment.** Multi-paper, multi-model matrix (ideally 4 models × ≥ 10 candidate papers × 4–10 source papers) with explicit per-paper per-model per-EP filling-type labels. Inter-rater agreement measured as Cohen's κ (pairwise) or Fleiss's κ (multi-model). Expected finding (pre-registered hypothesis): Paradigm-shift agreement ≪ Partial agreement, with the gap attributable to the absence of an operational criterion for Paradigm-shift in the current Stage 4 v2 prompt.
  - **Axis 2: dimensional-adequacy test of the five-type vocabulary.** Empirical test of whether the five types are best read as a one-dimensional spectrum (Complete → Partial → Indirect → Attempted, with Paradigm-shift as a discontinuity) or as a two-dimensional structure (e.g., **conceptual-judgment axis** × **data-completeness axis**, where Paradigm-shift occupies a distinct region on the conceptual axis and Haiku's invented labels like "Era-norm dependent" occupy a distinct region on a third era-norm axis). Procedure: (a) collect all filling-type labels used across the model × paper × EP matrix in Axis 1; (b) project labels into candidate 1-D / 2-D / 3-D representations; (c) evaluate which representation best explains the variance in cross-model assignment. Consequence for Codebook v0.3: if the 2-D or 3-D hypothesis is supported, the five-type vocabulary should be replaced by an explicit multi-dimensional label schema in v18's Stage 4 prompt revision.
- **Methodological significance**: this study is the empirical complement to §1.8 Layer B. Whereas §1.8 aims to articulate the Paradigm-shift criterion prescriptively (what operationalisation should look like), §1.15 measures descriptively how much cross-model agreement exists at baseline and whether the five-type vocabulary is dimensionally adequate. A draft Paradigm-shift criterion from §1.8 can be tested in a subsequent round of this study (criterion-driven multi-model re-run, comparing agreement before and after criterion articulation — the empirical test of whether the articulation achieves its transferability goal).
- **Scale and dependencies**: requires ≥ 4 models, ≥ 10 candidate papers per source, ≥ 4 source papers. Not executable within a single Claude Code session; requires multi-session matrix execution and separate agreement analysis. Dependencies include: cross-vendor API access (OpenAI for GPT family, Anthropic for Claude family, Google for Gemini family); budget for repeated runs; agreement-metric tooling (Python scikit-learn / R irr package suffice). Aligned with §1.12 principal validation programme's hallucination-audit and multi-paper-matrix axes.
- **Authoritative source**: SI-6.6 end-of-section analysis (2026-04-22); Discussion 3 watershed paragraph (section files `discussion_en.md` / `discussion_ja.md`, propagated to integrated manuscripts).

---

## §2. Empirical scope expansion

### §2.1 Additional chemistry sub-fields
- **Context**: UQS has been demonstrated on Ni-catalyzed cross-coupling (Kumada 1972 lineage). Other chemistry sub-fields for future evaluation include organic synthesis, computational chemistry, materials science, biochemistry.
- **Authoritative source**: Discussion 4 §"Applicability" lists directions (i)–(iv) of extension.
- **Scope note**: each sub-field requires redesign of Layer 2 and Layer 3 (per Discussion 4); not a simple prompt reuse.

### §2.2 Non-chemistry domains (biology, physics)
- **Scope**: evaluate whether UQS transfers to domains with different evidence architectures
- **Authoritative source**: Discussion 4 §"Applicability" (ii)
- **Known unknowns**: how A/B/C/U categories, VQ hierarchy, and EP dictionary concepts map to biology (e.g., experimental reproducibility conventions differ) and to physics (e.g., theoretical-claim vs experimental-claim distinction is different)

### §2.3 Larger N of papers per domain
- **Current scope**: 12 papers in Heck chemistry (test set + dev set); 8 filling papers in Kumada lineage (plus 5 in the newly-documented Layer 1). 
- **Phase 2 target**: N ≥ 30 papers per domain for distributional claims.

### §2.4 Temporal cross-section expansion
- **Current scope**: 1972–2024 (54-year span) focused on Kumada lineage.
- **Phase 2 target**: add papers from different decades in other sub-fields to test temporal-bias claims made in Discussion 1.

### §2.5 Cross-genre demonstration (non-scientific text corpora) — Phase 3 scope

- **Context (added 2026-05-08)**: The portability comparison with Synthegy (Bran et al., *Matter* 2026, 102812) — LLM-as-evaluator architecture in chemistry, locked to SMILES + retrosynthesis engine + cheminformatics verifier infrastructure — surfaced an asymmetry in domain-portability that is structurally favourable to UQS. Whereas Synthegy's architecture is portable in principle but its *instantiation* requires domain-by-domain rebuilding of the symbolic representation, search engine, action space, and verifier stack, the UQS pipeline keeps both processing and validation entirely within textual discourse. Genre substitution requires only domain-vocabulary adjustment in prompts and replacement of the chemistry-specific Stage 4 *Computational* (AFIR) modality with a genre-appropriate verification analog. The cross-disciplinary scope claims of Paper C's UQS 2.0 chapter — currently supported by within-science n > 1 (chemistry + biology + noble-gas chemistry, see [`project_rothlisberger2008_opus47_baseline.md`](memory) and Paper C Methods) — would be substantially strengthened by a small-N demonstration in at least one non-scientific text corpus.
- **Scope — three concentric tiers**:
  - **Tier 1 (proof-of-concept, 1 corpus × 2–3 documents)**: legal corpus pilot. Candidate sources: 2–3 widely-cited US Supreme Court opinions or comparable judgments where the text is publicly available, the discursive structure is rich enough to host A/B/C/U items, and at least one expert reader can validate the absences. Target deliverable: small-N pilot report demonstrating that S0 → S2 pipeline produces non-trivial structured-absence catalog without architectural change.
  - **Tier 2 (3 corpora × 5+ documents each, structured comparison)**: legal + clinical-guideline + policy. Compare absence-catalog density, key_quote anchoring quality, and cross-model convergence rates across genres. Target deliverable: separate methods paper on cross-genre UQS as a second-order text-corpus methodology.
  - **Tier 3 (historical archive integration)**: apply UQS to documents from a different epistemic era (e.g., 19th-century scientific or political writing) to test whether structured-absence detection itself is era-relative. This is the most ambitious tier and would substantiate UQS as a tool for historiography of science / historical sociology in addition to contemporary science.
- **Architectural changes required (Tier 1 baseline)**:
  - Stage 1 prompts: domain-vocabulary substitution (replace "reaction" / "yield" / "catalyst" with genre vocabulary).
  - Stage 4 *Computational* (AFIR): replace with genre-appropriate verification modality. For legal: precedent-search / statutory-cross-reference. For clinical guidelines: cohort-data / RCT-database lookup. For policy: outcome-statistics / impact-evaluation database.
  - Codebook (RI / EP dictionary): each genre requires a parallel dictionary of recurring discursive patterns — analogous to how Kumada lineage produced 10 EPs.
  - **Adjacent-field selection criteria (added 2026-05-09 v11)**: each target genre requires domain-specific operational definitions for the 4-layer adjacent-field selection framework — Layer 1 citation-graph (case-citation graph for legal, PubMed for medical, policy-document references for policy), Layer 2 methodological (doctrinal / RCT / quantitative as appropriate), Layer 3 conceptual (legal / clinical / policy concept ontologies), Layer 4 stakeholder (parties / patients / citizens). This is a **prerequisite for Tier 1 cross-genre demonstration** — without operational definitions per layer, adjacent-field selection in the new genre will be more vendor-dependent than in chemistry (where LLM training depth is greatest). See `memory/project_uqs_adjacent_field_selection.md` Cross-disciplinary expansion section for the full mapping.
  - Output naming convention: extend `papers/` to non-scientific genres or fork into `corpora/legal/`, `corpora/policy/`, etc.
  - **No change required** to: A/B/C/U classification, D-4 / E abstraction, SRG / CLA structure, Stage 2F group integration, cross-model verification protocol, key_quote anchoring.
- **Methodological significance**: a successful Tier 1 demonstration would constitute the empirical complement to the architectural portability claim. Without it, the claim is theoretical-only; with it, UQS positioning shifts from "chemistry-validated, architecturally portable" to "validated as a second-order text-corpus methodology beyond science". This is a step-change in the contribution scope of Paper C and any subsequent UQS 2.0 follow-on.
- **Dependencies**: domain-expert collaborator per target genre (legal scholar, clinician, policy analyst, historian); access to publicly-available text corpora; budget for cross-model UQS runs in the new genre; institutional ethics review depending on the corpus (e.g., clinical guidelines may not require review but patient-level data would).
- **Relation to other registry items**: distinct from §2.1 (chemistry sub-fields, intra-discipline) and §2.2 (biology / physics, non-chemistry but still science). §2.5 is the *beyond-science* extension. §1.12 principal validation programme remains unchanged in scope; cross-genre demonstration is a methodology-extension axis, not a methodology-validation axis.
- **Authoritative source**: this registry entry; supporting positioning analysis in `memory/project_uqs_text_portability.md` (independent positioning axis), `memory/project_llm_evaluator_paradigm.md` (paradigm convergence + root divergence framing), `memory/reference_synthegy_bran2026.md` (Synthegy comparison source).
- **Sequencing note**: Tier 1 should not be attempted before Paper A is submitted. Paper A's empirical scope must remain chemistry-only to keep the lead-use-case argument tight. Tier 1 is most naturally executed as part of the Paper C drafting cycle, where the cross-disciplinary chapter provides the natural home for the demonstration. Tier 2 / Tier 3 are Phase 3 (post-Paper C) work.

---

## §3. Cross-vendor / cross-model extensions

### §3.1 Gemini 3 Flash model-pinned run
- **Status**: Gemini 1.5 Pro trial run (2026-04-18) was auto-reassigned by Antigravity and excluded from publication scope; retained as internal methodology record at `papers/dev/kumada/gemini3flash/`.
- **Phase 2 target**: execute a model-pinned Gemini 3 Flash run via API to complete the three-vendor matrix (Anthropic + OpenAI + Google).
- **Dependency**: reliable model-pinning route via Antigravity / Google AI Studio / direct API.
- **Authoritative source**: [`si_issues_log.md`](../manuscript/si/output/si_issues_log.md) Issue #1 scope-decision paragraph.

### §3.2 Matched-prompt Claude re-run for GPT-5.4 comparison
- **Context**: current SI-6 documents Claude Haiku 4.5 / Sonnet 4.6 / Opus 4.7 runs on v17, and GPT-5.4 Thinking on v17 — prompt-version matching is already complete. However, a fair comparison of GPT-5.4's Stage 3 and Stage 4 against Claude should also include GPT-5.4 runs on the 10 test-set papers (currently only Kumada 1972 for GPT-5.4).
- **Phase 2 target**: GPT-5.4 Thinking on remaining 11 papers (dev + test) for a 4-model × 12-paper matrix.
- **Estimated cost / effort**: substantial — requires ~12 × 4 stages × GPT-5.4 run time + cross-model analysis.

### §3.3 N papers × M models matrix analysis
- **Scope**: systematic comparison of output quality across models and papers
- **Target deliverable**: dedicated model-capability paper (Phase 3?) — possibly separate from UQS-proper
- **Authoritative source**: Discussion 3 §"Causal claims remain unavailable with n = 1" paragraph lists verification paths (a)(b)(c)

### §3.4 UQS-specific benchmark design
- **Scope**: design of benchmarks mapped to UQS's capability requirements (structural prompt compliance, external-regulation parallel retention, multi-step inference stability, T1/T2/T3 discipline)
- **Target deliverable**: separate methods paper on LLM benchmark design for structured-absence detection
- **Authoritative source**: Discussion 3 §"Causal claims" verification path (c)

---

## §4. Bilingual / language study

### §4.1 Systematic bilingual comparison (Sonnet + Opus 4.7 × Japanese + English × N papers)
- **Current state**: English-track prompt variants exist for Stage 2/3/4 (`prompts/v17/prompt_stage2_v17_en.md`, `prompts/stage2f3/prompt_stage3_v{N}_en.md`, `prompts/stage2f3/prompt_stage4_v{N}_en.md`); Kumada 1972 pilot runs archived at `papers/dev/kumada/kumada_v17_sonnet_{s2,s3v2,s4v2}_en.md`.
- **Phase 2 target**: N papers × 2 models × 2 languages; report D-4 count, SRG granularity, EP identification, scope_type correctness per cell; systematic bilingual comparison report per `{paper}_bilingual_comparison.md` template.
- **Authoritative source**: [`si_issues_log.md`](../manuscript/si/output/si_issues_log.md) Item #9 (scoping decision 2026-04-19).

### §4.2 Cross-language extension (e.g., agglutinative, head-final languages beyond Japanese)
- **Scope**: test whether the Japanese syntactic-structure hypothesis (predicate deferral accommodates suspended-conclusion reasoning) generalizes to other languages with similar syntactic properties (Korean, Turkish) or differs in head-initial languages (Spanish, Indonesian).
- **Target deliverable**: separate methods paper (Phase 3+)
- **Authoritative source**: [`discussion_en.md`](../manuscript/sections/discussion_en.md) Discussion 3 §"Linguistic structure and the detection of absence" — acknowledges this as open empirical question. [SI-9](../manuscript/si/output/SI-9.md) §SI-9.3 Layer 1 articulates the layered-hypothesis structure and §SI-9.9 Phase 2 obligation 6 specifies the cross-language extension target.

### §4.3 Stage-level language optimization (added 2026-04-20 via SI-9)
- **Scope**: per-stage systematic comparison of Japanese vs English execution. Test whether specific stages (Stage 3 VQ judgment, Stage 4 EP-filling literature search) benefit from English execution while other stages retain Japanese. The current uniform post-D-4-Japanese convention may be sub-optimal; findings feed v18 prompt revision.
- **Target deliverable**: v18 prompt specification + empirical validation in the Phase 2 bilingual study.
- **Authoritative source**: [SI-9](../manuscript/si/output/SI-9.md) §SI-9.4 (per-stage rationale), §SI-9.9 Phase 2 obligation 4.

### §4.4 Paper-language × analysis-language 4-quadrant design (added 2026-04-20 via SI-9)
- **Scope**: include at least one Japanese-language source paper in the Phase 2 pilot. Compare 4 quadrants (Eng-paper × Eng-analysis, Eng-paper × Jp-analysis, Jp-paper × Eng-analysis, Jp-paper × Jp-analysis) to isolate the "external metalinguistic reading" effect versus the "native-reading" effect.
- **Target deliverable**: 4-quadrant experimental design as an integral part of the Phase 2 bilingual-comparison paper.
- **Authoritative source**: [SI-9](../manuscript/si/output/SI-9.md) §SI-9.9 Phase 2 obligation 3.

### §4.5 Category × language interaction profile validation (added 2026-04-20 via SI-9)
- **Scope**: populate the §SI-9.6 hypothesis table (A / B / C / U / D-4 / E / VQ across Japanese vs English) with measured yield, grounding quality, and cross-language overlap per category. This is a falsifiable version of the triangulation framing.
- **Target deliverable**: per-category language-advantage map as the primary output of the Phase 2 empirical study.
- **Authoritative source**: [SI-9](../manuscript/si/output/SI-9.md) §SI-9.6, §SI-9.9 Phase 2 obligation 2.

### §4.6 Family × language interaction (added 2026-04-20 via SI-9)
- **Scope**: combine §SI-9.3 Layer 4 with SI-6's family-specific analytical-depth residuals. Do Claude and GPT-5.4 respond differently to language switches? Does a given family retain its analytical-depth signature under the alternate language?
- **Target deliverable**: integrated with §4.1 Phase 2 bilingual-comparison study.
- **Authoritative source**: [SI-9](../manuscript/si/output/SI-9.md) §SI-9.3 Layer 4, §SI-9.9 Phase 2 obligation 5.

### §4.7 Japanese-language companion to SI-9 (added 2026-04-20 via SI-9.10)
- **Scope**: produce a Japanese-language parallel articulation of the SI-9 argument — not a translation, but a parallel document designed to make the language-conditional features of the rationale accessible to Japanese-reading readers, and to surface which aspects of the argument shift between the two framings.
- **Target deliverable**: separate document `manuscript/si/output/SI-9_ja.md` as a Phase 2 artifact.
- **Authoritative source**: [SI-9](../manuscript/si/output/SI-9.md) §SI-9.10.

### §4.8 Status of English-only prompt variants (updated 2026-04-20)
- **Status**: the English-only variants for Stage 2 v17, Stage 3 v2, and Stage 4 v2 are now **archived verbatim in SI-7.8** (2026-04-20 SI-7 full expansion). Stage 3 v1 en and Stage 4 v1 en do not exist; Stage 2F English variants are not yet prepared.
- **Phase 2 follow-ups**:
  - Produce Stage 2F English variants (v6, v7, v7.1 _en) when the Phase 2 bilingual study scope is finalised.
  - Produce Stage 3 v1 en retrospectively if the Phase 2 study needs to compare v1-era bilingual execution; otherwise skip.
- **Cross-reference**: [SI-7](../manuscript/si/output/SI-7.md) §SI-7.8 holds the variants actually archived. Registry §4.1 specifies the systematic comparison scope.

---

## §5. ChemOntology-AFIR pilot execution

### §5.1 Execute NiCl₂(dpe) GRRM/AFIR pilot per Layer C plan
- **Status**: companion deliverable produced — Layer A (parameter mapping, Table 4), Layer B (YAML input specifications + 3 variants), Layer C (execution plan) — all drafted 2026-04-19/20 and archived in `chemontology_pilot/`.
- **Execution status**: **planned, not run**; the pilot computation has not been performed.
- **Phase 2 target**: run the pilot per Layer C; evaluate whether EP-03a / EP-06a / EP-04a (and possibly EP-05a) are computationally filled by ChemOntology-AFIR output for the NiCl₂(dpe) system.
- **Dependencies**: computational-chemistry collaborator access; access to AFIR software; compute resources.
- **Authoritative source**: [`SI-3.md`](../manuscript/si/output/SI-3.md) preamble "second update 2026-04-19" paragraph; `chemontology_pilot/` directory.
- **Pre-execution deliverable — 3-part partition spec format (added 2026-05-08)**: before the pilot is run, the existing system specification (`chemontology_pilot/layer_B_input_specification/pilot_input_NiCl2_dpe.yaml` and `.json`) must be revised to the **3-part partition format** prescribed by the gap-driven system-selection logic for Paper B (see `memory/project_paperB_system_selection_logic.md`). The revised spec must explicitly partition system scope into three named blocks: (a) `unfilled_EP` — EP IDs the pilot is computing as filling-targets, with source-paper attribution and gap-description; (b) `reference_EPs` — EP IDs already established in the source paper or downstream literature, with their established_value and the role they play in the pilot (initial state, validation anchor, branching ratio cross-check, etc.); (c) `chemical_context` — substrate / catalyst / solvent choices with explicit `simplifications_made` list and `rationale` for each simplification. This format is operationally tied to Paper B's central methodological commitment ("gap-driven system selection") and must be in place before pilot execution so that the pilot produces a Paper-B-grade EP-Computational filling record rather than a generic AFIR computation. Estimated effort to revise the spec: 1-2 days; see `memory/project_paperB_system_selection_logic.md` for the canonical template and the NiCl₂(dpe) worked example.
- **Pre-execution deliverable — Synthegy-style counterfactual spec (added 2026-05-08)**: alongside the 3-part partition spec, prepare a deliberately-contrasting Synthegy-style counterfactual specification for the *same chemical scope* — i.e., what input a utility-driven framework would propose if asked to perform an AFIR computation on a Kumada-family system. This counterfactual is rhetorical material for Paper B Discussion (not actually run), and serves to make the gap-driven vs. utility-driven contrast concrete. Document it as `chemontology_pilot/layer_B_input_specification/counterfactual_synthegy_style.md` so that Paper B Methods/Discussion can reference both specs side-by-side. Mark explicitly that the counterfactual is *constructed by extrapolation*, since Synthegy as published does not propose AFIR-style computational systems.

### §5.2 Stage 4 Computational classification extension
- **Context**: if the ChemOntology pilot succeeds, a sixth filling type — *Computational* — should be added to Stage 4 (current five types: Complete / Partial / Indirect / Attempted / Paradigm-shift).
- **Proposed sub-classifications**: Computational-Complete (multiple theory levels, robustness confirmed) / Computational-Partial (single theory level) / Computational-Indirect (analog system only).
- **Authoritative source**: [`manuscript_en.md`](../manuscript/sections/manuscript_en.md) Discussion 2 §"Stage 4 extension: the Computational classification as future work."

### §5.3 UQS-ChemOntology bidirectional connection paper
- **Scope**: a dedicated paper on the UQS ↔ ChemOntology bridge — structuring of objective functions in one direction, reaction-network-as-evidence in the other direction.
- **Target deliverable**: Phase 3 paper, likely separate from UQS-proper.
- **Authoritative source**: Discussion 2 §"Bidirectional intellectual contributions."

---

## §6. Open issues carried from the v15→v17 development cycle

The following are tracked in [`improvements/open_issues.md`](../improvements/open_issues.md) and are NOT resolved by the v17 prompt. They are recorded here for Phase 2 visibility; the authoritative source for each remains `improvements/open_issues.md`.

### §6.1 OI-001 β-H elimination pattern detection
- **Status**: open (continued monitoring); detected in Kumada dev-set Entry 001 R4
- **Why not resolved**: detection requires chemistry-domain sensitivity that does not yield to prompt-level instruction additions
- **Phase 2 direction**: possible addressing via Codebook v0.3 RI redefinition or via improved training-data coverage in later model generations

### §6.2 OI-004 bilateral-yield-mismatch propagation
- **Status**: partially addressed by v17 C7 (yield basis mixing exception); residual propagation not fully suppressed
- **Phase 2 direction**: refinement of C-item consolidation rules in v18

### §6.3 OI-005 catalyst-loading anomaly loss
- **Status**: out of v17 scope; Murai run-5 3× catalyst anomaly remains unsurfaced
- **Phase 2 direction**: domain-specific C-item subtype for "unexplained parameter anomaly"

### §6.4 OI-015 silyl hidden-requirement absence
- **Status**: open; Murai case where silyl group may be hidden substrate requirement
- **Phase 2 direction**: chemistry-domain sensitivity pattern; may require domain-knowledge-informed prompt additions

(Other open issues — OI-002, OI-003, OI-006, OI-014, OI-016, OI-017, OI-018, OI-019, OI-020, OI-021, OI-022, OI-023 — are documented in the authoritative file.)

---

## §7. Figure and table updates

### §7.1 Fig. 2 EP-filling matrix — add EP-10a column and two-layer row structure
- **Current state**: Fig. 2 is implemented (per `manuscript/design/figures_tables_design.md` status line) with 8 EPs and single-layer row structure (Kumada 1972 origin + 8 filling papers).
- **Update needed**: add EP-10a column (VQ-3 group); add Layer 1 rows (Tamao-Kiso 1973, Kiso-Tamao 1973, Morrell-Kochi 1975, Tamao 1976 already present, Tamao 1982); visual separator between Layer 1 and Layer 2; explicit ≈35-year gap annotation.
- **Authoritative source**: `manuscript/design/figures_tables_design.md` warning at top; `SI-4.9` and `improvements/stage4_literature_update_20260419.md` for the data.
- **Decision pending**: authors decide at submission time whether to update Fig. 2 pre-submission OR include Fig. 2 as-is and note the EP-10a addition as a subsequent update in the Discussion.

### §7.2 Table 3 historical case-study papers — add Layer 1 papers
- **Current state**: Table 3 contains the 8 Layer-2 papers.
- **Update needed**: add a separate Layer-1 sub-table OR footnote referencing `SI-4.9` for the 5 Layer-1 papers.
- **Authoritative source**: same as §7.1.

### §7.3 SI Fig. S1
- **Status**: managed separately via `manuscript/design/claude_code_figures_guide.md`; not in UQS-proper submission scope but may need updating to reflect v18 prompt revision if that occurs.

---

## §8. References and data availability

### §8.1 Four flagged references — RESOLVED 2026-04-19

All four previously-flagged references in `manuscript/sections/references_en.md` were verified on 2026-04-19 by cross-check against the BIB-1 field of each paper's Stage 0 output:

| Ref # | Citation (verified) | Source |
|---|---|---|
| **Ref 8 (Molander 2016)** | Tellis, Kelly, Primer, Jouffroy, Patel, Molander, *Acc. Chem. Res.* **49**, 1429–1439 (DOI 10.1021/acs.accounts.6b00214) | `papers/ep/kumada1972/molander2016/molander2016_v17_sonnet_s0.md` BIB-1 |
| **Ref 9 (Morken 2016)** | Eno, Lu, Morken, *J. Am. Chem. Soc.* **138**, 7824–7827 (DOI 10.1021/jacs.6b03384) | `papers/ep/kumada1972/molken2016/molken2016_v17_sonnet_s0.md` BIB-1 |
| **Ref 10 (Mazet 2021)** | Poisson, Tran, Besnard, Mazet, *ACS Catal.* **11**, 15041–15050 (DOI 10.1021/acscatal.1c04800) | `papers/ep/kumada1972/mazet2021/mazet2021_v17_sonnet_s0.md` BIB-1 |
| **Ref 11 (Li 2024)** | Li, Zhu, Guo, Kou, Wang, Xie, Ma, Feng, Wang, Qiu, *Nat. Catal.* **7**, 412–421 (DOI 10.1038/s41929-024-01118-3) | `papers/ep/kumada1972/pengfei2024/pengfei2024_v17_sonnet_s0.md` BIB-1 |

**Status**: all four are confirmed and documented in the verification log at `manuscript/sections/references_en.md` (lines 75-78 table; lines 166-169 detailed entries). No further pre-submission action required.

**Not carried to Phase 2.**

### §8.2 Zwart work selection — RESOLVED 2026-04-19

**Ref 18 (Zwart)** is finalized as a composite citation of two Zwart papers in *Life Sci. Soc. Policy*:

- **(a)** H. Zwart, "The oblique perspective: philosophical diagnostics of contemporary life sciences research," *Life Sci. Soc. Policy* **13**, 4 (2017) — DOI 10.1186/s40504-017-0047-9
- **(b)** H. Zwart, "Scientific iconoclasm and active imagination: synthetic cells as techno-scientific mandalas," *Life Sci. Soc. Policy* **14**, 10 (2018) — DOI 10.1186/s40504-018-0075-0

**Rationale for selection** (per `references_en.md` line 173):
- (a) provides the core Lacanian "philosophical diagnostics of life sciences research" matching the SI-0.2 characterization directly.
- (b) extends the oblique-reading practice to synthetic-biology visual culture ("mandala" analysis) and is the closest single match for the 2018 citation date.
- Both are open-access publications in *Life Sciences, Society and Policy* (Springer); Zwart is Editor-in-Chief of the journal.

**Status**: confirmed and accepted as final (2026-04-20). Alternative works (e.g., Zwart's 2022 *Continental Philosophy of Technoscience* monograph) were considered but not preferred — the 2017+2018 composite is the most focused match for SI-0.2's symptomatic-reading characterization.

**Optional minor future refinement**: SI-0.2's current phrasing attributes "Lacanian + Hegelian dialectics" to Zwart. Paper (a) matches the Lacanian attribution cleanly; paper (b) additionally draws on Jungian and Bachelardian registers. If a future revision tightens the philosophical specifics, generalizing to "continental-philosophical" would improve accuracy across both cited works. This is a non-blocking copy-editing refinement, not a Phase 2 research item.

**Not carried to Phase 2.**

### §8.3 GitHub / OSF public release of raw data and scripts
- **Scope**: all reconciliation tables, Stage 0-4 outputs per paper, Stage 3 v1 and v2 prompts, rewriter scripts (when written for Phase 2), pilot response forms (Phase 2), ChemOntology pilot YAML/JSON (already drafted in `chemontology_pilot/`).
- **Target**: pre-submission — minimal public release of SI inputs (reconciliation CSVs, critical Stage 3 / Stage 4 records). Post-submission — full release with pilot data once Phase 2 completes.

### §8.4 CLAUDE.md / MANIFEST.md project documentation refresh — RESOLVED 2026-04-20

- **Scope**: update `CLAUDE.md` and `MANIFEST.md` to reflect folder structure as of 2026-04-20 (including `future_work/`, `chemontology_pilot/`, `manuscript/`, nine-EP dictionary, four-model v17 comparison, Phase 2 scope).
- **Resolution applied**:
  - `MANIFEST.md`: full rewrite. Version bumped from v15 (2026-04-12 baseline) to v17 (2026-04-20). New sections added for §1 folder structure, §2 prompt inventory (S0–S2, Stage 2F/3/4, English-only variants), §3 paper sets (dev + test + EP-filling + conventional-layer references), §4 key deliverables (`manuscript/`, cross-model validation, ChemOntology pilot, Phase 2 registry), §5 naming conventions with all model identifiers, §6 summary of 9-EP dictionary + two-layer filling + four-model findings, §7 version management and open issues, §8 current status and Phase 2 roadmap.
  - `CLAUDE.md`: folder-structure section (lines 9–20) replaced with a three-category structured listing: "分析実行関連" (original analysis folders), "文書・改善サイクル関連" (docs + improvements), "投稿成果物関連（2026 年追加）" (manuscript/, chemontology_pilot/, future_work/), and "補助" (scripts/). The analysis-execution operational workflow (§ Stage 0 → Stage 4 の実行手順, § 短縮記法, § 英語単独トラック, § Stage 2F モデル版切替 Opus 4.7 対応) — which occupies the bulk of `CLAUDE.md` — is unchanged because it is still accurate.
- **Not carried to Phase 2.**

---

## §9. Long-term vision and LLM-evolution scenarios — Phase 3+ scope

### §9.1 UQS specification standardization (community-maintained methodology standard)

- **Context (added 2026-05-08)**: As LLMs continue evolving, both UQS-style and Synthegy-style approaches will be increasingly subsumed into native LLM capabilities (5-10 year horizon). The asymmetry: Synthegy will be **subsumed as implementation** (its function gets absorbed into LLMs, the framework becomes redundant — "Synthegy" disappears, capability remains), while UQS must **survive as specification** (the methodology requires externalization as a community-maintained standard so that judgments like "what counts as an EP" or "how to validate cross-model convergence" remain reproducible regardless of which LLM executes them). This is analogous to how HTTP, IUPAC nomenclature, or SMILES-line-notation persist as specifications independent of any specific implementation.
- **Phase 3+ target**: package UQS as a community-maintained specification document, separate from the prompt-set implementation. Components:
  - **EP dictionary**: governance for ongoing addition / refinement of EPs (currently 10 EPs in Kumada lineage; Codebook v0.3+ expected to extend across chemistry sub-fields).
  - **Classification taxonomy**: A/B/C/U / D-4 / E / VQ / scope_type definitions formally articulated as standalone specification document.
  - **Anchoring conventions**: key_quote format, source_paper attribution rules, cross-model convergence reporting format.
  - **Adjacent-field selection criteria (added 2026-05-09 v11)**: 4-layer framework (Layer 1 citation-graph / Layer 2 methodological / Layer 3 conceptual via EP dictionary / Layer 4 stakeholder) with required {Layer ID, criterion, evidence} triple per selected field. This is a **mandatory specification component** — without it, adjacent-field selection remains an unspecified layer in implicit LLM judgment, and the specification framing has a structural hole (cf. `memory/project_uqs_adjacent_field_selection.md`). Cross-genre extension (Phase 3, registry §2.5) requires domain-specific operational definitions for each layer.
  - **Compliance criteria**: what does a "UQS-conformant analysis output" require? (per-item key_quote, source attribution, scope_type tag, cross-model convergence report, **adjacent-field selection record with rationale triples**, at minimum).
  - **Version governance**: how the specification is updated over time (Codebook revisions, RI promotion criteria, EP addition criteria, **layer-framework revisions when new genres are added**).
- **Target deliverable**: separate "UQS Specification v1.0" document, possibly as an open standard hosted independently of the per-paper repositories. Candidate hosting: GitHub specification repository, RSC / IUPAC affiliated home, or community methodology platform.
- **Strategic significance**: positions UQS to remain referenceable beyond the lifecycle of any specific prompt-set implementation. Without specification standardization, UQS as currently packaged (markdown prompts, manual stage execution) becomes obsolete the moment LLMs natively support absence-detection workflows. With specification standardization, the methodology persists as community resource regardless of LLM evolution, and the foundational publications (Paper A / Paper C) remain the canonical reference for the standard.
- **Authoritative source**: `memory/project_uqs_long_term_vision.md` for full rationale; this registry entry for the operational task.
- **Dependencies**: requires community uptake — at minimum, a small set of external groups must adopt or cite the specification for it to function as standard. Paper A / Paper C publication is necessary precondition; sufficient external adoption is target outcome of subsequent dissemination.

### §9.2 Paper C re-positioning as specification-foundational publication

- **Context**: Paper C is currently positioned as "UQS 2.0 methodology evolution" — implying a successor implementation rather than a foundational specification. The long-term-vision analysis (memory: `project_uqs_long_term_vision.md`) identifies that this framing has 5-10 year referenceability half-life, whereas a specification-foundational positioning has decade-stable referenceability comparable to canonical methodology papers (e.g., RFC 2616 for HTTP/1.1, IUPAC nomenclature publications).
- **Phase 2-Paper-C target**: re-frame Paper C drafting around specification framing. Concrete changes:
  - **Title / subtitle**: include "specification" or "methodology standard" in title-level visibility (e.g., subtitle *"a specification for second-order analysis of scientific discourse"*).
  - **Abstract**: lead with the specification claim, not the prompt-evolution narrative.
  - **Methods**: present EP dictionary / taxonomy / anchoring conventions as components of the specification, not as features of one project's implementation.
  - **Discussion**: explicitly anticipate LLM native subsumption as success criterion (the specification survives the implementation shift); invite community participation in maintaining the standard.
- **Authoritative source**: `memory/project_uqs_long_term_vision.md` "Paper C deployment" section.
- **Dependencies**: depends on co-author consensus regarding specification-vs-tool framing. Coordinate with `project_paperABC_journal_strategy.md` for venue selection (Patterns / Cell Reports Methods are appropriate; specification framing strengthens these venue fits).

### §9.3 LLM-evolution-triggered strategy re-evaluation protocol

- **Context**: Major LLM capability shifts (frontier model that natively supports absence-detection; chemistry-vertical LLM product that bundles Synthegy-equivalent features; specification-following LLM that auto-conforms to community methodology standards) will require strategy re-evaluation within 6 months of release. Without a re-evaluation protocol, the long-term vision (this section) drifts from current state without explicit revisit.
- **Trigger conditions**:
  - Any frontier LLM release that demonstrates >70% performance on a UQS-style absence-detection benchmark without explicit prompt protocol.
  - Any commercial chemistry-LLM product bundling Synthegy-equivalent capability (retrosynthesis search + LLM evaluation) at non-enterprise pricing.
  - Any independent group publishing a competing specification for second-order analysis of scientific discourse.
  - Any IUPAC / RSC / ACS initiative to standardize LLM-augmented chemistry methodology.
- **Re-evaluation scope**: revisit `memory/project_uqs_long_term_vision.md`, `memory/project_paperABC_journal_strategy.md`, and registry §9.1 / §9.2. Update the 5-10 year prediction; revise Paper C / future-paper positioning if needed; re-validate the specification framing.
- **Cadence**: at minimum annual review independent of trigger conditions; trigger-driven re-evaluation within 6 months of qualifying event.
- **Authoritative source**: `memory/project_uqs_long_term_vision.md` "Caveats / what to watch" section for the latest trigger-condition list.

---

## §10. Phase 4+ research program — domains outside UQS specification scope

### Context (added 2026-05-09 v15)

After UQS expert-lens sampling specification reached v0.1 freeze with 6+1 components (registry §1.1D revision 15), the comparison with Synthegy (Bran et al. 2026) surfaced **five domains structurally outside both UQS and Synthegy methodologies** that are nonetheless valuable enough to register as next-frontier research candidates. These are NOT specification extensions of UQS — by design, they require methodologies complementary to UQS, not refinements of it. Authoritative articulation: `memory/project_uqs_synthegy_shared_limitations.md`.

The 5 domains share a common structural reason for being outside UQS / Synthegy reach: both methodologies depend on (a) existing text corpora, (b) existing conceptual vocabulary, (c) retrospective or near-term-prospective time horizons, (d) within-paradigm anchoring. Domains where any of these constraints fails are intentional outside-scope.

### §10.1 Unpublished knowledge corpus extension (Tier 2A: Lab-tradition cartography) — **Paper G candidate (long-horizon, 3-5 y)**

- **Scope**: extend UQS architecture to corpora not currently in scope — lab notebooks (digitized at scale), oral histories (transcribed PI-student dialogues), conference recordings, personal scientific archives. Estimated dark-matter knowledge volume: 5-10× published knowledge per publication-bias literature.
- **Why valuable**: addresses replication crisis, negative-results recovery, prevention of repeated lab failures across labs. Directly relevant to research integrity / open science funding streams.
- **Why outside current UQS scope**: UQS corpus is published papers; new corpus types require corpus-construction methodology that UQS does not provide.
- **Phase 4 target**: small-N pilot on a single research lab's notebook archive (with consent), demonstrating that UQS architecture (4-layer + 5-tuple + provenance) works on non-published corpus with domain-vocabulary substitution.
- **Dependencies**: corpus access (consent-bound), corpus digitization tooling, ethics review for personal archive material.
- **Authoritative source**: `memory/project_uqs_synthegy_shared_limitations.md` Domain 1.

### §10.2 Cross-paradigm vocabulary translation (Layer 5) — **Paper D ACTIVE (near-term, committed 2026-05-09)**

- **Scope**: cross-paradigm question generation — invoking concepts from paradigms whose vocabulary is not present in the target paper. Currently forbidden by UQS Layer 3 anchoring constraint (`memory/project_uqs_adjacent_field_selection.md`).
- **Why valuable**: scientific breakthroughs frequently arise from paradigm-vocabulary translation (information theory → molecular biology; quantum mechanics → biology; statistical mechanics → economics → biology).
- **Why outside current UQS scope**: Layer 3 anchoring requirement specifically excludes cross-paradigm vocabulary that has no anchor in target paper text. Latent-reconstructable exception is bounded to within-paper reconstruction.
- **Phase 4 target**: develop a candidate 5th sampling Layer with explicit cross-paradigm anchoring criteria that retain auditability while permitting controlled paradigm crossing. If validated, promote from Future-version candidate 6 (currently registered as out-of-v0.1) to active specification v0.2.
- **Empirical trigger for promotion**: documented cases of UQS analyses where a within-paradigm Layer 1-4 selection systematically misses a cross-paradigm question that an interdisciplinary expert would have raised.
- **Authoritative source**: `memory/project_uqs_synthegy_shared_limitations.md` Domain 2 + `memory/project_uqs_adjacent_field_selection.md` Future-version candidates section.

### §10.3 Priority overlay methodology — **Paper F candidate (medium-horizon, 2-3 y)**

- **Scope**: combine UQS cartography with priority signals (citation impact, funding-history, community-survey output, strategic-statement analysis) to produce ranked candidate research directions. Operates downstream of UQS, not as UQS extension.
- **Why valuable**: research-program design, funding allocation, graduate-student advising, peer-review judgment all require prioritization. Cartography alone yields no action guidance.
- **Why outside current UQS scope**: UQS deliberately defers priority labeling to the reader (bounded scaffold defensive line, `memory/project_uqs_reviewer_bias_reduction.md` Mechanism 3). Priority overlay is a separate methodology layer that consumes UQS output, not modifies it.
- **Phase 4 target**: prototype priority-overlay methodology applied to a Kumada-lineage UQS cartography, demonstrating actionable priority output that could guide research-program selection.
- **Methodology dependencies**: scientometric tools (citation-network metrics), funding-database access, community-survey design.
- **Authoritative source**: `memory/project_uqs_synthegy_shared_limitations.md` Domain 3.

### §10.4 Longitudinal trajectory inference — **Paper E candidate (medium-term, 12-18 mo; promote-on-trigger when Paper D Phase C validates Layer 5)**

- **Scope**: cross-temporal aggregation of UQS cartographies across decades to infer field-trajectory signals (which absences persisted, which were filled, on what timescale, with what intervening developments). Meta-methodology applied to UQS-output corpus.
- **Why valuable**: funding agencies, national science policy, learned societies need long-horizon trajectory predictions for strategic planning. Both UQS and Synthegy are silent on this.
- **Why outside current UQS scope**: UQS is fundamentally retrospective per single-paper analysis. Trajectory inference requires aggregation across analyses + projection methodology that UQS does not contain.
- **Phase 4 target**: multi-paper longitudinal study using Kumada lineage 1972-2026 cartography (already produced by Paper A) as proof-of-concept; extract trajectory signals (which EPs filled when, which remained unfilled, what historical events correlated with filling).
- **Distinct from `project_uqs_long_term_vision.md` §9.3**: that registers LLM-evolution forecasting (10-year horizon for methodology evolution); §10.4 here registers science-trajectory forecasting (decade-to-century horizon for chemistry-as-a-field evolution). Different objects of forecast.
- **Authoritative source**: `memory/project_uqs_synthegy_shared_limitations.md` Domain 4.

### §10.5 Paradigm-shift acknowledgment (specification limitation, not extension) — **Paper C limitations chapter (NOT separate paper)**

- **Scope**: not a methodology extension, but explicit articulation of UQS specification's outer bound. UQS detects paradigm-shifts *between articulable paradigms* (registry §1.8 Layer B v18 prompt proposal); it does not generate *new* paradigms or recognize concepts outside current vocabulary.
- **Why valuable**: scientific revolutions involve concepts that did not exist in prior vocabulary (Kuhn). Honest articulation that UQS cannot reach this is itself a contribution — establishes the limit of what specification-bounded methodology can do.
- **Why outside current UQS scope**: LLM-as-evaluator paradigm itself presupposes articulable vocabulary. Genuinely novel concepts emerge outside the constraint protocol; a constrained evaluator cannot recognize them.
- **Phase 4 target**: not a project but an articulation in Paper C limitations chapter. Reference candidate text in `memory/project_uqs_synthegy_shared_limitations.md` Domain 5.
- **No "promotion to active specification" path**: this is a permanent specification limitation, not a candidate for v0.2. Articulating it as such is the contribution.

### §10.6 Potential UQS × Synthegy collaboration territory

- **Scope**: three of the five Phase 4 domains have collaboration potential where UQS and Synthegy together attack what neither can alone:
  - Domain 1 (unpublished knowledge): UQS cartographs absence in lab notebooks + Synthegy feasibility-scores failed routes
  - Domain 3 (priority ranking): UQS surfaces absences + Synthegy evaluates candidate solutions → "absence × feasibility" matrix
  - Domain 5 within-paradigm subset: UQS paradigm-shift filling type + Synthegy elementary-step formalism reform
- **Why valuable**: extends contribution beyond either methodology alone; potential "Paper B+" or post-Synthegy collaboration paper.
- **Status**: speculative. None of the three combinations attempted. Forward-looking research direction, not committed plan.
- **Dependencies**: contact with Schwaller lab (or Synthegy successors) for collaboration discussion; co-author alignment on cross-methodology research direction.
- **Authoritative source**: `memory/project_uqs_synthegy_shared_limitations.md` "Potential UQS × Synthegy collaboration territory" section.

---

## Registry update log

- **2026-04-20 (initial)**: registry created with §1–§8 scoping based on state of project at this date.
- **2026-04-20 (revision 1)**: §8.1 and §8.2 marked RESOLVED after verification that the references were already confirmed on 2026-04-19. §8 is now restricted to §8.3 (GitHub / OSF release) and §8.4 (CLAUDE.md / MANIFEST.md refresh). Sections §8.1 and §8.2 are retained as historical-resolution records and do not carry to Phase 2.
- **2026-04-20 (revision 2)**: §8.4 marked RESOLVED after refresh of both `CLAUDE.md` (folder-structure section) and `MANIFEST.md` (full rewrite from v15 baseline to v17 + 4-model + 9-EP + two-layer + Phase 2 scope). §8 is now restricted to §8.3 (GitHub / OSF public release) as the only active Phase-2-direction item.
- **2026-04-20 (revision 3, late evening)**: SI-9 "Rationale for the Bilingual Design of the UQS Analytical Pipeline" commissioned and written. §4 expanded with five new sub-sections (§4.3 Stage-level language optimization; §4.4 Paper-language × analysis-language 4-quadrant design; §4.5 Category × language interaction profile validation; §4.6 Family × language interaction; §4.7 Japanese-language companion to SI-9). §4 is now the most detailed Phase 2 sub-section of the registry, reflecting that bilingual / language study is now a systematic research programme with multiple axes of experimentation rather than a single comparison.
- **2026-05-08 (revision 4)**: §2.5 Cross-genre demonstration (non-scientific text corpora) added as Phase 3 scope. Triggered by portability-axis comparison with Synthegy (Bran et al., *Matter* 2026, 102812) which surfaced UQS's structural text-portability against Synthegy's chemistry-locked instantiation. Tier 1 (legal pilot) → Tier 2 (legal + clinical + policy) → Tier 3 (historical archive). Distinct from §2.1 (intra-chemistry sub-fields) and §2.2 (non-chemistry science). Sequencing: not before Paper A submission; most naturally executed as part of Paper C drafting. Supporting memory: `project_uqs_text_portability.md`.
- **2026-05-08 (revision 5)**: §5.1 expanded with two pre-execution deliverables — (1) revision of the NiCl₂(dpe) system spec to the **3-part partition format** (`unfilled_EP` / `reference_EPs` / `chemical_context`) operationalising the gap-driven system-selection logic for Paper B; (2) preparation of a **Synthegy-style counterfactual spec** as rhetorical material for the gap-driven-vs-utility-driven contrast in Paper B Discussion. Triggered by the 8-axis comparison developed for Paper B's methodological commitment. Supporting memory: `project_paperB_system_selection_logic.md`.
- **2026-05-08 (revision 6)**: §9 Long-term vision and LLM-evolution scenarios added as Phase 3+ scope. Three sub-sections — §9.1 UQS specification standardization (community-maintained methodology standard, analogous to HTTP / IUPAC / SMILES); §9.2 Paper C re-positioning as specification-foundational publication (title/abstract/Methods/Discussion changes); §9.3 LLM-evolution-triggered strategy re-evaluation protocol with explicit trigger conditions and cadence. Triggered by analysis of democratization-speed asymmetry (UQS leads infrastructure-wise, Synthegy leads end-user-utility-wise) and LLM-design-subsumption asymmetry (Synthegy → implementation subsumed; UQS → must survive as specification). Supporting memory: `project_uqs_long_term_vision.md`.
- **2026-05-08 (revision 7)**: §1.1C Tier 1C UQS-as-review-scaffold bias-reduction study added as Phase 2 work. Triggered by user observation that human reviewers default to specialty-confined perspective and UQS scaffold structurally reduces five identifiable reviewer biases. A/B comparison study design (5-10 reviewers per group, cross-specialty paper assignment). Distinct from §1.1 Tier 1 (UQS-output-quality evaluation) and from Tier 1B (computational-chemist system-selection alignment). Sequencing: post-Paper-A, post-Tier-1. Supporting memory: `project_uqs_reviewer_bias_reduction.md`.
- **2026-05-08 (revision 8)**: §1.1C metrics refined to incorporate bounded-scaffold validation (GPT review v2). Six headline metrics replace prior four: anchor rate / defect-vs-opportunity separation / cross-specialty coverage / **unnecessary-revision-demand rate** / comment transparency / era-anachronism rate. Critical hypothesis is that UQS scaffold *simultaneously* increases coverage AND decreases unnecessary demands — this signature distinguishes bounded review scaffold from critique-amplification tool. Group A instruction set explicitly includes the bounded-scaffold defensive line ("not every mapped absence is a revision demand"). Supporting memory: `project_uqs_reviewer_bias_reduction.md` Bounded review scaffold section.
- **2026-05-09 (revision 9)**: §1.1C metrics extended with seventh metric — **constructive-vs-gatekeeping ratio** — operationalising the third value axis (constructive review elevation, Kuchitsu lineage). User input cited Kozo Kuchitsu (1927-2021, University of Tokyo, former editor of Chemical Physics Letters; biographical anchor: Springer Structural Chemistry obituary) as articulator of the editorial philosophy that peer review should elevate flawed papers into first-rate field-building contributions rather than gatekeep. Critical caveat: Metric 7 measures correlation not causation; "scaffold supports constructive disposition" defensible, "scaffold creates constructive disposition" over-claim. Group A instruction set extended with constructive-elevation framing reference. Supporting memory: `project_uqs_reviewer_bias_reduction.md` Constructive review elevation section.
- **2026-05-09 (revision 10)**: §1.1C Metric 7 refined from **constructive-vs-gatekeeping ratio** to **constructive conversion rate** (GPT v3 review). The earlier-draft ratio was vulnerable to lenient-review gaming (soft comments without valid criticism inflate the metric). Refined definition: among comments identifying a deficiency / absence / limitation, the fraction accompanied by a specific direction for strengthening the contribution. Denominator is valid criticism only; lenient reviews cannot inflate. Direct measure of **conversion skill** (criticism → direction-of-growth), the editorial-intelligence capacity tested by Axis 3. Companion metric added: substantive accuracy of suggested directions (post-hoc independent expert rating) to detect "high conversion rate + low direction quality" failure mode. Kuchitsu attribution clarified: bibliographic facts are documented in published Springer / IUPAC obituaries; the specific philosophy quote is recalled by colleagues / user testimony, not directly verifiable in those obituaries — deploy as "associated with" / "recalled by colleagues" not "as documented by" until primary sources confirmed. Supporting memory: `project_uqs_reviewer_bias_reduction.md` (Sourcing of the editorial philosophy section + Constructive conversion rate refinement).
- **2026-05-09 (revision 11)**: §1.1D Tier 1D — Adjacent-field selection criteria validation study added as Phase 2 work (methodology-internal). Triggered by user observation (2026-05-09) that adjacent-field selection in UQS Stage 1/2 is currently delegated entirely to LLM judgment without explicit criteria, with qualitative cross-vendor variation visible (Claude relatively reasonable, Gemini sloppier; n=1). 2 × N factorial study (Condition A no-criteria / Condition B 4-layer-framework with required {Layer ID, criterion, evidence} triple) across 4-5 vendors × 3-5 Kumada-lineage papers. 4 metrics: Jaccard overlap / layer distribution / rationale articulation rate / mainstream-bias index. Methodology-internal — does not require external evaluators or Paper A publication; can run during Paper C drafting. Distinct from Tier 1A/1B/1C. Cross-genre expansion (§2.5) requires domain-specific Layer 1-4 operationalization, registered as prerequisite. Supporting memory: `project_uqs_adjacent_field_selection.md`.
- **2026-05-09 (revision 12)**: §1.1D refined with Core/Exploratory distinction (GPT review v4) — adjacent-field selection schema upgraded from {Layer, criterion, evidence} **triple** to **5-tuple** (layer + evidence_basis + question_lens + core_or_exploratory + confidence). Layer 3 (conceptual overlap) gains mandatory **explicit anchoring constraint** to one of five permitted anchor types (named concept / mechanism / variable / representation / explanatory-gap explicitly present in target paper) — blocks LLM free-association as the source of vendor variance. Hypothesis structure expanded from single hypothesis to **3-hypothesis joint signature** (H1 core convergence + H2 exploratory divergence preservation + H3 mainstream-bias reduction) — joint success demonstrates "criteria ensure reproducibility without sacrificing creativity"; failure of H2 alone refutes the Core/Exploratory distinction's value. Metrics extended from 4 to 5 (added Layer 3 anchor compliance rate as sub-metric for highest-risk layer); Jaccard split by Core vs. Exploratory tier. Adjacent-field selection reframed as **upstream gate that defines UQS's output space**, not preprocessing layer — must become central UQS specification component on par with EP dictionary. Supporting memory: `project_uqs_adjacent_field_selection.md` (Reframing as upstream gate + Layer 3 explicit constraint + 5-tuple schema + Core vs Exploratory distinction + Paper C canonical deployment text).
- **2026-05-09 (revision 13)**: §1.1D extended with sampling-design framing + 3-level overlap measurement + Layer 3 latent-reconstructable exception + excluded-fields completeness record (GPT review v5). Adjacent-field selection re-framed from "upstream gate" (metaphor) to "**sampling design**" (methodological vocabulary, social-science / statistics / qualitative-research lineage) — strengthens specification framing for Paper C. Layer 3 anchor constraint refined to "explicitly present **or reconstructably latent**" with 4 reconstruction sources (experimental operation / observed product / mechanistic language / cited literature) — historical-paper (pre-1980s) compatibility while suppressing free-association. **5-tuple schema extended with `excluded_candidate_fields` completeness record** (name + reason_for_exclusion + status + consideration_layer) — required for compliance, ensures re-execution reproducibility. **Vendor-specialization operational principle** added (Claude conservative for Core / Gemini associative for Exploratory) — converts vendor difference from noise to designed division of labor, generalizes "protocol design as primary value" framing. **Metrics extended to 6 with 3-level overlap measurement** replacing single-Jaccard: field-level / lens-level / absence-type — captures cases where field name and intent diverge in either direction. Two **future-version candidates** (Core/Peripheral/Exploratory three-tier, lens-centric design) registered but not adopted in v3; deferred to UQS spec v2 with explicit empirical triggers. Paper A limitation text refined to GPT v5 compressed canonical version. Supporting memory: `project_uqs_adjacent_field_selection.md` (sampling-design reframing + Layer 3 latent exception + excluded-fields schema + vendor-specialization principle + 3-level overlap rationale + future-version candidates).
- **2026-05-09 (revision 14)**: §1.1D extended with **sampling budget / stopping rule + U-item provenance** as the closing structural pieces of the adjacent-field selection specification (GPT review v6). **Sampling budget**: lens_sampling_budget schema (Core 3-5 / Exploratory 1-3 / excluded 3-5) closes the previously-unspecified "how many selections is enough" boundary; Paper A uses fixed budget, Paper C uses variable budget. **U-item provenance**: each U-item record extended with `originating_lens` field (question_lens content + core_or_exploratory status, matched to lens-selection block) — closes the evidential chain from selection criteria → selected lens → generated U-item, enabling Tier 1A/1C/1D measurement at lens granularity. **Vendor-specialization deployment text refined to vendor-neutral** (conservative-mode / associative-mode language replacing Claude / Gemini names) for specification longevity. **Excluded-fields recording bounded at top 3-5 per run** to prevent specification weight inflation. **Layer 3 anchor `anchor_status` field mandatory** (explicit_in_target_paper / reconstructably_latent_not_explicit) preventing explicit/latent distinction loss. **Naming refinement**: "expert-lens sampling" adopted as Paper C primary term (with "adjacent-field selection" parenthetical), preserving Paper A continuity. **Metrics extended to 9** adding sampling-budget compliance + U-item provenance completeness + Layer 3 anchor_status completeness. Most-compressed canonical sentence (GPT v6 headline) saved verbatim — enumerates all six structural components in one sentence. Supporting memory: `project_uqs_adjacent_field_selection.md` (Sampling budget section + U-item provenance section + vendor-neutral deployment text + bounded exclusion rule + anchor_status field + expert-lens sampling naming + GPT v6 canonical headline).
- **2026-05-09 (revision 15)**: §1.1D updated with **specification freeze v0.1 declaration + minimum viable specification (MVS) + compliance checklist + closing refinements** (GPT review v7). The expert-lens sampling specification declared **frozen at v0.1** with 6+1 structural components — no further additions without empirical trigger; future refinements register as v0.2 candidates. **MVS articulated**: subset of v0.1 strictly required for UQS-conformance (bounded lens budget + explicit inclusion/exclusion records + provenance links per U-item) — permits lighter conformance levels while preserving the principle. **Compliance checklist** (15 items, MVS subset marked) added as deployment-ready Paper C SI deliverable, supporting analyst self-check / reviewer audit / Tier 1D Condition B prompt / specification document. **Intentional asymmetry of Core/Exploratory strictness** articulated as designed feature (Core constrained for reproducibility, Exploratory bounded but permissive for hypothesis generation) — prevents specification from becoming bureaucratic checklist. **Sampling budget guardrail framing**: numeric ranges (3-5 / 1-3 / 3-5) re-positioned as guardrails not universal constants — pre-empts "why 5 not 6" reviewer challenges. **`defect_or_opportunity_status` field** added to U-item provenance schema, structurally connecting expert-lens sampling specification to reviewer-bias-reduction specification. **Final canonical definition** (GPT v7 definition form, distinct from claim-form headlines) saved verbatim. **Paper C transition deployment text** for "expert-lens sampling" naming refinement saved verbatim. **Specification freeze rule**: future refinement proposals default to Future-version candidates registration; promotion requires explicit empirical trigger. The next phase of work in this area is **Tier 1D empirical execution**, not further conceptual articulation. Supporting memory: `project_uqs_adjacent_field_selection.md` (v0.1 freeze section + MVS articulation + compliance checklist + intentional-asymmetry articulation + guardrail framing + defect_or_opportunity_status schema + GPT v7 final canonical definition + Paper C transition deployment text).
- **2026-05-09 (revision 16)**: §10 Phase 4+ research program added — five domains structurally outside both UQS and Synthegy methodologies but valuable enough to register as next-frontier research candidates. Triggered by post-v0.1-freeze synthesis of UQS-Synthegy correspondence: shared design constraints (LLM-as-evaluator + dependence on existing text + dependence on existing vocabulary + retrospective time-horizon + within-paradigm anchoring) imply five intentional outside-scope domains. **§10.1 Unpublished knowledge corpus** (lab tradition / oral history / personal archives — dark matter ~5-10× published volume); **§10.2 Cross-paradigm vocabulary translation** (Future Layer 5 candidate; currently forbidden by Layer 3 anchoring); **§10.3 Priority overlay methodology** (downstream of UQS cartography, combines with priority signals); **§10.4 Longitudinal trajectory inference** (cross-temporal aggregation, distinct from §9.3 LLM-evolution forecasting); **§10.5 Paradigm-shift acknowledgment** (specification limitation articulation, not extension — permanent outer bound). **§10.6 Collaboration territory** with Synthegy on three of five domains (Paper B+ candidate). None of §10 violate v0.1 freeze rule because they are outside specification scope, not extensions. Supporting memory: `project_uqs_synthegy_shared_limitations.md` (5-domain articulation + updated UQS-Synthegy correspondence after v0.1 freeze + Paper C limitations-chapter framing + UQS × Synthegy collaboration territory).
- **2026-05-09 (revision 17)**: §10 sub-sections updated with **paper assignments** following 5-domain → paper assignment analysis. Domain → Paper mapping: §10.1 Domain 1 → **Paper G candidate (long-horizon 3-5y)**; §10.2 Domain 2 → **Paper D ACTIVE near-term committed** (Layer 5 cross-paradigm extension; Phase A pilot in Paper A peer-review window); §10.3 Domain 3 → **Paper F candidate (medium-horizon 2-3y)**; §10.4 Domain 4 → **Paper E candidate (medium-term 12-18mo; promote-on-trigger when Paper D Phase C validates Layer 5)**; §10.5 Domain 5 → **Paper C limitations chapter (NOT separate paper)**. 4-paper near-term portfolio (A/B/C/D) committed. Paper E/F/G are aspirational long-horizon candidates with explicit drop-without-prejudice / merge-possibility / promote-on-trigger rules. Sequencing: Paper A peer review concurrent with Paper B drafting + Paper D Phase A pilot → Paper A published + Paper D Phase B → Paper C drafting + Paper D Phase C → Paper C published → Paper D drafting → Paper D published. Total time-to-Paper-D ~18-24 months. New supporting memory: `project_paperD_layer5_cross_paradigm.md` (Paper D design memory with Layer 5 8-tuple schema + 6 candidate approaches + Phase A/B/C pilot design + 4 promotion criteria + Paper D narrative structure). Updated supporting memory: `project_uqs_synthegy_shared_limitations.md` (Domain → Paper assignment table + sequencing implications) + `project_paperABC_journal_strategy.md` (4-paper hybrid + Paper E/F/G long-horizon candidates).
- Subsequent updates should append entries or revise specific §subsection status; overall structure should remain stable to preserve cross-references.
