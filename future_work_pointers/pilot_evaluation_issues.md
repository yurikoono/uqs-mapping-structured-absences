# Pilot Evaluation (Tier 1 Advisor-Evaluation Protocol) — Implementation Issues

**Created**: 2026-04-20
**Status**: deferred to Phase 2 per Option γ decision (see `README.md`).
**Primary reference**: [Methods 6](../manuscript/sections/methods_en.md) and [SI-8](../manuscript/si/output/SI-8.md) of the Digital Discovery submission define the protocol; this document catalogs the unresolved operational specifications and risks that a Phase 2 systematic pilot must address.

---

## Context and decision

The Digital Discovery submission declares that the Tier 1 advisor-evaluation protocol is "operational by design" (Methods 6, SI-8.1–SI-8.4) but treats actual pilot-application data as Phase 2 work (SI-8.5 is a placeholder; see [`si_issues_log.md` Issue #4](../manuscript/si/output/si_issues_log.md)). The decision to defer the pilot rather than run a minimal n = 1 pilot ("Option β") or a fully systematic pilot ("Option δ" — several advisors × several papers) was made on 2026-04-20 because:

- **n = 1 pile-up risk**: the paper already rests on n = 1 empirical observations in SI-6 (four-model comparison on one paper) and SI-3 (Kumada 1972 deep analysis). A third n = 1 observation in SI-8.5 would make the paper feel anecdotal.
- **Pre-submission timeline**: running even a minimal pilot requires ~10–14 days for recruitment, LLM-rewrite script development, execution, analysis, and writeup.
- **Pre-registration criteria absence**: without predefined success / failure thresholds, post-hoc analysis risks cherry-picking.
- **Self-referential concern**: the advisor population is part of the same publication system whose implicit motivations UQS analyzes (see §C-4 below), complicating interpretation of any single pilot outcome.

This document catalogs the issues a Phase 2 systematic pilot must confront, organized by type. Each item is tagged as **blocker** (must be resolved before the Phase 2 pilot starts) or **open question** (acceptable to resolve during pilot execution, but documented).

---

## A. Protocol design — operational precisions not yet specified

### A-1. Definition of "thesis advisor" — blocker

Methods 6 / SI-8.1 refer to "thesis advisor" as the evaluator, but the operational definition is not specified:

- Limited to faculty with active PhD students, or do postdocs / associate professors / senior industrial researchers qualify?
- What sub-field expertise is required — organometallic chemistry in general, or specifically cross-coupling reactions?
- What minimum experience threshold (years as an independent researcher)?

**Resolution for Phase 2**: define inclusion criteria before advisor recruitment; document in the pilot pre-registration.

### A-2. Evaluation-unit size — blocker

For Kumada 1972, Stage 1 produces ~25 A/B/C/U items plus ~8 D-4 candidates — ~33 items total per paper. Methods 6 does not specify how many items one advisor evaluates:

- **All items**: ~2–4 hours of advisor time; fatigue bias risk.
- **Random subset**: sampling bias unless combined with multiple advisors.
- **Category-stratified subset**: more defensible design but requires more advisors to cover all strata.

**Resolution for Phase 2**: target a fixed number (e.g., 15 items per advisor per session) with category stratification across advisors.

### A-3. Inter-rater reliability (IRR) — blocker

The 6-category response (SI-8.2) is inherently subjective. Required number of advisors:

- **n = 1**: anecdotal; insufficient for any population-level claim.
- **n = 2–3**: minimum for Cohen's κ IRR calculation (still marginal).
- **n ≥ 5**: meaningful distributional description.

**Resolution for Phase 2**: target n ≥ 5 advisors per paper; report Cohen's κ across pairs and Fleiss's κ across the full panel.

### A-4. Blind vs transparent presentation — blocker

Methods 6 states the advisor framing "structurally suppresses biased reaction to AI-generated output," but:

- **Fully blind** (advisor not told items are LLM-generated): creates a consent issue — the advisor may feel deceived when the SI reports this.
- **Transparent** (advisor told the experimental purpose): contradicts the claim that bias is suppressed.

**Resolution for Phase 2**: two-step design. (i) advisor first receives items without any LLM context and evaluates them; (ii) after submission, advisor is debriefed and given the option to revise any evaluation. Both rounds are reported separately in the Phase 2 paper.

### A-5. Paper selection for pilot — open question

- **Kumada 1972**: already extensively analyzed in SI-3; advisors may know the paper too well to be neutral.
- **Murai 1993**: same issue.
- **One of the test-set 10 papers**: less well-known to typical advisors, but requires matching sub-field expertise.

**Resolution for Phase 2**: select 2–3 papers covering different sub-fields (e.g., one homogeneous, one heterogeneous, one synthetic application) and randomize advisor-paper assignment to prevent advisor-paper correlation bias.

---

## B. Practical logistics

### B-1. Advisor recruitment — blocker

Finding chemistry-PhD advisors willing to spend 2–4 hours on a pilot is non-trivial. Recruitment strategies:

- **Co-author network**: fast (1–2 weeks) but introduces selection bias toward LLM-sympathetic respondents.
- **Random sampling from corresponding authors of recent Heck papers**: slower (2–4 weeks) but more representative.
- **Professional society mailing list**: widest reach but lowest response rate.

**Resolution for Phase 2**: two-tier recruitment — 2–3 advisors from the co-author network (fast pilot), 3–5 from random sampling (validation).

### B-2. Student-question rewrite pipeline — blocker

SI-8.1 Step 1–2 specifies an LLM pass to rewrite Stage 1 / D-4 items into student-question form. This rewriter does not yet exist:

- Script: `scripts/convert_to_student_questions.py` (or equivalent) not yet written.
- Quality-assurance checklist for preserving (a) specific object, (b) anchor in paper, (c) absence being pointed at — not yet formalized.
- Verification that the rewrite does not introduce content the original item did not have — method not specified.

**Resolution for Phase 2**: develop the rewriter as an LLM prompt + verification script; require cross-check by a second model or human before the pilot presentation.

### B-3. Response-recording form — blocker

No template exists for:

- Paper form, Google Forms, Qualtrics, spreadsheet, or dedicated tool — method not specified.
- Metadata fields: timestamp, advisor confidence, time-per-item, free-text comment — partially mentioned in SI-8.1 Step 5 as "inferred from protocol structure" but not formally required.

**Resolution for Phase 2**: build a structured form (e.g., Google Forms) with mandatory and optional fields; pilot-test with one advisor before full deployment.

### B-4. Timeline — blocker

Minimum pre-submission execution window for a systematic pilot:

| Phase | Duration |
|---|---|
| Advisor recruitment | 2–4 weeks |
| Rewriter script development + validation | 3–5 days |
| Form and instruction-sheet design | 2–3 days |
| Pilot execution (n advisors × 1–2 sessions each) | 1–2 weeks |
| Data analysis and writeup | 1 week |
| **Total** | **6–10 weeks** |

For the Digital Discovery submission, this timeline is incompatible with the planned deadline; Phase 2 is therefore a separate effort.

### B-5. IRB / consent — open question

The pilot may qualify as "ordinary peer collaboration" and therefore fall outside formal IRB oversight at most institutions. However, because the resulting data will be reported in a publication (Phase 2 paper), a short informed-consent document is prudent:

- Data-use statement.
- Anonymization policy (advisor identity disclosed or anonymized in publication).
- Right to withdraw.

**Resolution for Phase 2**: draft `docs/pilot_consent_form.md` before advisor contact; consult the author group's institutional IRB contact for explicit exemption or minimal-review determination.

### B-6. Compensation and acknowledgements — open question

- Standard peer-evaluation: no monetary compensation, Acknowledgements section citation.
- Anonymous vs named advisor disclosure — advisor's preference at consent time.

**Resolution for Phase 2**: offer both options at consent; default to anonymized aggregation unless the advisor explicitly consents to named attribution.

---

## C. Analytical and reporting risks

### C-1. n = 1 limitation pile-up — blocker (for Option β, avoided by Option γ)

The current Digital Discovery submission already rests on n = 1 empirical foundations:

- SI-3 / SI-4 / SI-5: one paper's Stage 3 deep analysis, eight filling papers, one Stage 2F integrative analysis.
- SI-6: four-model comparison on one paper.

Adding an n = 1 pilot in SI-8.5 would make the paper's empirical foundation "three-times n = 1," inviting reviewer pushback that the paper's conclusions are anecdotal. Option γ (defer to Phase 2) avoids this by keeping the n = 1 pile-up from growing.

**Resolution for Phase 2**: systematic pilot must target n ≥ 5 advisors × 2–3 papers to support meaningful distributional claims.

### C-2. Missing pre-registered success / failure criteria — blocker

SI-8.2 defines six response categories but does not specify:

- What percentage of items falling in category (ii) "Already studied but demonstrates mature insight" constitutes success?
- What percentage in category (vi) "Unable to evaluate" invalidates the pilot?
- What distributional skew across categories indicates a specific failure mode (e.g., too many (iv) "basic, already-established knowledge" suggests UQS output is too shallow)?

**Resolution for Phase 2**: pre-register success / failure thresholds on OSF or similar before pilot execution; report all results regardless of direction.

### C-3. Category (vi) "Unable to evaluate" threshold — blocker

If advisors mark too many items as (vi), the pilot produces effectively empty data. Causes of elevated (vi):

- Item too specialized for the advisor's sub-field.
- Item poorly rewritten (too abstract, too technical).
- Item is a true UQS discovery that the advisor genuinely cannot evaluate.

**Resolution for Phase 2**: define (vi) upper bound (e.g., ≤ 30% of items) as a quality-control threshold; re-recruit advisors or re-rewrite items if exceeded.

### C-4. Self-referential problem — open question

UQS's D-4 items are "unquestioned motivations" — absences invisible from inside the field. The advisor evaluating them is also inside the field. If the advisor dismisses a structurally valid D-4 item because the item is invisible to them, the pilot cannot distinguish:

- "UQS generated a useless item."
- "UQS generated a genuinely useful item that the advisor cannot see because of their internal position."

This is a **fundamental interpretive difficulty** rather than a fixable design flaw; the Phase 2 paper should discuss it explicitly as a methodology-of-evaluation concern.

**Resolution for Phase 2**: include a "meta-evaluation" question — ask each advisor at the end of their session: "Did any of the items, on reflection, feel 'structurally correct but invisible' to you?" Record these separately as a signal of UQS-specific insight.

### C-5. Re-entry of field biases — open question

Methods 6 claims the advisor framing suppresses publication-incentive-structure bias, but the advisor is still evaluated under that same incentive structure in their ordinary career. The advisor's evaluations may implicitly reflect biases that UQS is designed to bypass.

**Resolution for Phase 2**: treat advisor evaluations as descriptive, not normative. The Phase 2 paper should frame Tier 1 as "useful complementary evidence" rather than "ground truth."

---

## D. External validity concerns

### D-1. Single-reaction-system generalization — open question

Kumada-1972-based pilot results do not generalize to organic synthesis broadly, much less to computational chemistry or non-chemistry fields.

**Resolution for Phase 2**: pilot should cover ≥ 2 sub-fields of chemistry; domain generalization (biology, physics) remains Phase 3+ work.

### D-2. Temporal bias of 1972 paper — open question

An advisor in 2026 evaluating absences in a 1972 paper evaluates across a ≥ 50-year shift in field conventions. Results on a 1972 paper may not generalize to evaluations on recent (e.g., 2024) papers.

**Resolution for Phase 2**: include at least one paper from each of three decades (1972–1980, 2000–2010, 2020–2025) in the pilot set.

### D-3. Self-selected advisor bias — open question

Advisors who agree to participate are likely more LLM-sympathetic and more open to methodology-innovation research. They do not represent the "ordinary" advisor population.

**Resolution for Phase 2**: document this bias explicitly in Phase 2 paper Limitations; consider a follow-up study with blinded recruitment from a larger advisor pool.

---

## E. Connection to Discussion 3 / SI-6 four-model comparison

### E-1. Multi-model item inclusion — open question

SI-6 showed that four-model v17 runs produce family-specific residuals in analytical depth. The Phase 2 pilot could:

- **Use only Sonnet output** (consistent with production recommendation): simpler but only evaluates Sonnet's output quality.
- **Mix items from multiple models**: more robust evaluation of UQS-in-general, but introduces a confound between "the item's UQS quality" and "the source model."

**Resolution for Phase 2**: multi-model mixing with model-source logging; report per-model sub-distributions in addition to pooled results.

### E-2. What does the pilot actually validate? — open question

Clarify in advance: the Phase 2 pilot validates "UQS-generated items appear useful / insightful to domain experts" — not "reasoning-oriented post-training is the causal source of UQS capability" (that causal question remains out of scope per Discussion 3). The two are separately evaluable.

---

## F. Infrastructure and documentation gaps

### F-1. Unwritten artifacts — blockers (for Phase 2 start)

- `scripts/convert_to_student_questions.py` — LLM-driven rewriter for Stage 1 / D-4 → student-question form.
- `scripts/analyze_pilot_responses.py` — tabulation, IRR calculation, distributional reporting.
- `docs/pilot_advisor_instructions.md` — cover sheet explaining the protocol, with the verbatim advisor prompt ("The following is a list of questions and observations ...").
- `docs/pilot_consent_form.md` — data-use consent, anonymization policy, right to withdraw.
- `scripts/pilot_form_template.md` — Google Forms / Qualtrics question specification.

### F-2. SI-8.5 formatting for Phase 2 — open question

When pilot data is eventually available, SI-8.5 format should cover:

- Per-advisor per-paper category distribution (stacked bar).
- Item-level category assignment (table with item ID × category).
- IRR statistics (Cohen's κ per pair; Fleiss's κ across panel).
- Free-text comments aggregated by theme.
- Meta-evaluation "structurally correct but invisible" item counts.

Target length: 1,500–3,000 words (currently ~200 words for the placeholder).

---

## G. Summary — Phase 2 pilot pre-flight checklist

Before starting the Phase 2 pilot, the following must be resolved:

- [ ] A-1: Inclusion criteria for "thesis advisor" documented.
- [ ] A-2: Fixed evaluation-unit size (items per advisor per session).
- [ ] A-3: Advisor count targeting n ≥ 5 with IRR reporting plan.
- [ ] A-4: Two-step blind-then-debrief design implemented.
- [ ] B-1: Two-tier recruitment strategy executed.
- [ ] B-2: Rewriter script and QA checklist published.
- [ ] B-3: Response-recording form designed and pilot-tested.
- [ ] C-2: Pre-registered success / failure thresholds posted to OSF or equivalent.
- [ ] C-3: Category (vi) upper bound set and documented.
- [ ] F-1: All unwritten artifacts completed.

The following can be resolved during pilot execution:

- A-5: Final paper selection (to be finalized at recruitment stage).
- B-5 / B-6: IRB / consent / compensation (per-institution variation acceptable).
- C-4 / C-5: Self-referential and field-bias issues (discussed in Phase 2 paper, not resolved operationally).
- D-1 / D-2 / D-3: External validity limitations (documented as Phase 2 paper Limitations).
- E-1 / E-2: Multi-model scope and separation-of-claims clarification.

---

## References

- **Methods 6**: [`manuscript/sections/methods_en.md`](../manuscript/sections/methods_en.md) lines 41–58.
- **SI-8.1–SI-8.5**: [`manuscript/si/output/SI-8.md`](../manuscript/si/output/SI-8.md).
- **Issue #4**: [`manuscript/si/output/si_issues_log.md`](../manuscript/si/output/si_issues_log.md).
- **Discussion 3 context for Phase 2 scope**: [`manuscript/sections/discussion_en.md`](../manuscript/sections/discussion_en.md) Discussion 3 §"Methodological implication."
- **CLAUDE.md Phase 2 note**: "systematic study is Phase 2 work" — quoted in the bilingual comparison report instructions.
