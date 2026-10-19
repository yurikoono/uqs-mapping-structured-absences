---
title: Paper A — Digital Discovery target narrative (claim lock)
created: 2026-05-20
status: active
audience: paperA
open_questions: true
---

# Paper A — Digital Discovery target narrative (claim lock)

## Purpose

This document is the **Phase 0 0A artifact** of the Paper A Digital Discovery (DD) revision project. It locks the claim boundaries that the submitted manuscript must defend, *before* Tier 1 audit work (retrieval / Data Availability / Mini-Audit / framing rewrite) begins.

The locks here serve as the **post-hoc adjustment defense** against reviewer concerns about "the authors moved the goalposts after seeing the data." All Tier 1 + 2 + 3 work must remain consistent with §1–§4 below; changes to those four claims require explicit revision-cycle decision.

## 1. Main claim (1 sentence, workflow-led)

**UQS is an auditable LLM-assisted workflow for converting structured evidential absences in chemical literature into experimentally actionable research questions.**

Key features locked:

- **"workflow"** (not "method", not "tool"): emphasises the pipelined character with explicit governance checks at each Stage
- **"auditable"**: positions the paper for Digital Discovery's data-first / reproducibility audience
- **"LLM-assisted"** (not "LLM-driven"): human verification + retrieval audit are integral, not optional
- **"structured evidential absences"**: the technical object — not "missing information" / "open problems" / "unsolved questions"
- **"experimentally actionable research questions"**: the deliverable — concrete, lab-runnable, not abstract

## 2. Demonstrated claim (what this paper shows)

**In the Kumada 1972 case, UQS yields ten Evidence Packs (EP-01a–EP-10a) and seven Subgroup-Specific Propositions (SSP-1–SSP-7) that can be traced to source-paper evidence and subsequent literature.**

Expansions (each is a sub-claim the paper must support):

- The EPs are reproducibly derived from Stage 3 across model families (Sonnet / Opus / GPT-5 / Haiku)
- The SSPs are anchored to specific source-paper observations across multiple corpus papers
- Filling-status assignments (Complete / Partial / Minimal / Non-filler) for each EP are made against **locked criteria** (Phase 0 0B: `paperA_ep_audit_criteria_20260520.md`)
- Negative claims (EP-08a + EP-09a) are stress-tested by **structured bibliographic retrieval** (WoS + Scopus + Google Scholar + Crossref) — Tier 1 #1
- Sampled outputs survive **internal expert mini-audit** (12-item set per Mini-Audit Protocol v0.1) — Tier 1 #5

## 3. Stability claim (NOT validation)

**Cross-model agreement (Sonnet / Opus / GPT-5 / Haiku) and multi-run aggregation (N=6 per cell) support the stability and robustness of UQS outputs against single-vendor and single-run idiosyncrasy. They do NOT, in themselves, establish that outputs are objectively true or exhaustive.**

This is the central terminological calibration the manuscript must hold:

| Claim type | Permitted wording | Forbidden wording |
|---|---|---|
| Chemistry-internal | "mechanistic validation" / "experimental validation" / "catalytic-cycle validation" | (none — chemistry usage is natural) |
| LLM-output | "stability check" / "convergence check" / "robustness screen" / "cross-model robustness evidence" | "primary validation" / "model-independent validation" / "captures structural properties" |
| Output property | "is consistent with outputs reflecting source-paper structure" | "reflects source-paper structure" (drops the calibration) |
| Independence | "partial cross-vendor independence" / "shared-training-data caveat acknowledged" | "model-independent" / "fully independent" |

Cross-model independence is **acknowledged as partial** (limited by shared training data); this is non-negotiable per the cross-vendor convergence limitation.

## 4. Non-claim (explicit boundary)

**UQS does not prove that no relevant evidence exists outside the searched academic record. The 54-year non-detection of EP-08a (replicate measurement) and EP-09a (substrate-matched benchmarking) is an absence-of-evidence observation in the published academic literature within our UQS-guided + structured-bibliographic retrieval, not evidence-of-absence in global chemical knowledge (which includes patent literature, industrial process records, and unpublished know-how).**

This non-claim is **structurally load-bearing**:

- It is the post-hoc adjustment defense for the negative EP-08a/09a finding
- It must appear in **Abstract** (already present, 2026-05-09 addition) + **Introduction** (already present, §29 Fourth claim) + **Methods §3** (corpus boundedness note) + **Results Part 2** (already present) + **Discussion 1** + **Limitations**
- Audit trail (Phase 0 0B EP criteria + Tier 1 #1 retrieval audit) must operationally enforce this boundary
- Bibliographic-not-reaction-database-exhaustive caveat: if SciFinder / Reaxys are not accessible, this is recorded explicitly in SI

## 5. What is future work (NOT this paper)

These belong to companion papers. Forward references in main text are **minimised**; one consolidated "Future work" paragraph in Discussion 3 / Outlook.

| Companion | Status | Treatment in Paper A |
|---|---|---|
| **Paper B** (Yoshioka et al., in preparation) — UQS × ChemOntology-AFIR | Skeleton stage, empirical pilot pending | Discussion 3 / Outlook 1 mention; reframe as "**application direction, not a dependency of the present workflow**" (1 sentence) |
| **Paper C** (in preparation) — UQS 2.0 methodology evolution | Drafting, v6 archive | Reference only where Paper A's prompt-evolution claim (Results Part 4) needs the trajectory anchor; otherwise consolidated in Future work |
| **Paper D** (folder 未作成) — Layer 5 cross-paradigm | Not started | NOT referenced in Paper A |
| **Paper E** (skeleton, 2026-05-18) — Reflection-as-oracle | Skeleton stage | NOT referenced in Paper A |
| **Paper H** (long-horizon candidate) — UQS-grounded systematic review | Concept stage | NOT referenced in Paper A |

Companion-reference policy (Tier 1 #3 enforcement):

- Max 1 mention of Paper B in body (Discussion 3 / Outlook)
- Paper C consolidated to Future work paragraph (no inline forward refs)
- Paper D / E / H: **zero mention** in Paper A
- No forward references to companion papers in **Abstract / Introduction / Results / Methods main flow**

## 6. DD-specific required evidence (auditability story)

The manuscript must include or reference the following at submission. Priorities (9-tier) are derived from GPT-5 recommendation:

| Priority | Item | Status target | Storage |
|---|---|---|---|
| 1 | Prompt versions (v15–v17 + Stage 2F + Stage 3 + Stage 4 in `prompts/`) | Public release | Zenodo + GitHub |
| 2 | Input metadata (corpus papers list, DOIs, dates analysed) | Public | SI + Zenodo |
| 3 | Stage-wise output summaries (Stage 0 / 1 / 2 / 3 / 4 per paper) | Public | SI + Zenodo |
| 4 | Classification tables (EP audit, SSP table, filling-status matrix) | Public | SI + Zenodo |
| 5 | Retrieval logs (date, database, query, candidate set, decisions) | Public | SI + Zenodo |
| 6 | Inclusion / exclusion decisions (with rationale) | Public | SI + Zenodo |
| 7 | Aggregation scripts / pseudocode | Public | GitHub |
| 8 | Redacted raw LLM outputs (copyrighted source-text fragments removed) | Public | Zenodo |
| 9 | Full raw LLM outputs | Reviewer-only access (private link at submission, evaluated for legal release before publication) | Zenodo (private/embargoed) |

DOI policy:

- **DOI reserved before submission if feasible**; otherwise reviewer-accessible repository at submission with **DOI assigned before acceptance / publication** (RSC author guidelines compatible)

Raw output legal caveat:

- All raw outputs must be **checked for copyrighted source-paper text fragments** before public release
- Where Stage 0/1/2 outputs quote PDF text directly, redacted public version excludes the quotes; reviewer-only full version retains them
- This split is documented in Data Availability section

## 7. Operational constraints derived from this lock

1. **All Tier 1 #1 retrieval audit results must be checked against the non-claim (§4) before main-text incorporation.** No claim like "the field does not know X" — only "the published academic record within our retrieval does not surface X."
2. **All Stability claims (§3) must be checked against the cross-vendor independence limitation.** No claim of "model-independent validation" — only "cross-model robustness evidence under partial-independence conditions."
3. **All SSP framing must respect the demonstrated/non-claim distinction.** SSPs are decomposable next-step propositions, not "proof that the field's open problems are exactly these seven."
4. **Pre-submission Mini-Audit results determine final main-text inclusion.** Items failing A4 (invalid anchor), B3-B4 (over-extended inference), or C4 (unreasonable classification) per Mini-Audit Protocol §4 are demoted to SI or removed.
5. **Figure 1 must surface the auditability story.** Per GPT-5: input / each Stage / Stage output / LLM 投入 / human verification / retrieval audit / final EPs+SSPs / **explicit boundary "not a proof of global absence"**.
6. **SSP-1 illustration in Introduction (inserted 2026-05-20) must carry "output not input" disclaimer** (Tier 2 #8): a 1-sentence note that the example is an illustrative output of the completed workflow, not a target around which the workflow was designed.

## 8. Open questions

- Q1: WoS / Scopus 両アクセス可否 (Hokkaido U subscription 確認要)
- Q2: Mini-Audit auditor 依頼先 (内部 co-author n=1-2 vs 外部 organometallic chemist) → user 経由で 2026-05-20 に依頼予定
- Q3: Pre-submission placeholders 6 件 (improvements/paperA_pre_submission_placeholders_20260516.md) と本 revision との parallel 化可否
- Q4: Mini-Audit Protocol §7 wording template と本 manuscript Methods text の最終 wording 整合

## 9. Document status

Phase 0 0A artifact. **Locks here are the operational baseline for Tier 1 audit design** (0B EP criteria + Tier 1 #1 retrieval audit).

- §1–§4: 凍結。変更には revision-cycle decision 必要
- §5–§7: Tier 1 work 進行と共に refine 可
- §8: open questions resolved 時に update

## Related documents

- Locked revision plan: `improvements/paperA_dd_revision_plan_20260520.md`
- v11 snapshot: `improvements/paperA_v11_snapshot_20260520.md`
- Phase 0 0B EP audit criteria: `improvements/paperA_ep_audit_criteria_20260520.md` (作成予定)
- Internal Mini-Audit Protocol: `improvements/paperA_Internal_Mini-Audit_Protocol_for_UQS_Outputs.md`
- Pre-submission placeholders: `improvements/paperA_pre_submission_placeholders_20260516.md`
