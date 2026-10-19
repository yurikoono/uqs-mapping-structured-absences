# Future Work — Deferred Items and Phase 2 Planning

**Created**: 2026-04-20
**Purpose**: Archive of items deliberately deferred beyond the current Digital Discovery submission scope, organized as a working registry for Phase 2 and later work.

---

## How this folder relates to other registries

This project maintains three registries for different time horizons, and they should **not duplicate** each other:

| Registry | Location | Horizon | Content |
|---|---|---|---|
| **Open issues** | [`improvements/open_issues.md`](../improvements/open_issues.md) | Within current iteration (v15→v17 cycle) | OI-001 through OI-023: prompt-level or analysis-level issues identified during development |
| **SI preparation issues** | [`manuscript/si/output/si_issues_log.md`](../manuscript/si/output/si_issues_log.md) | Pre-submission for current paper | Issues #1–#6 plus Items #1–#11: inconsistencies and author-decision items discovered during SI preparation |
| **Future work (this folder)** | `future_work/` | **Beyond current submission** | Work explicitly acknowledged as out-of-scope for the Digital Discovery paper; intended for Phase 2 paper, separate methods paper, or later revisions |

When a deferred item from `si_issues_log.md` turns into a future-work item (e.g., "the full systematic pilot is explicitly Phase 2 work"), it should be cross-referenced here rather than duplicated. This folder is the authoritative record of Phase 2 scope.

---

## Files in this folder

- [`README.md`](README.md) — this index.
- [`pilot_evaluation_issues.md`](pilot_evaluation_issues.md) — comprehensive registry of design, operational, analytical, and external-validity issues for the Tier 1 advisor-evaluation pilot, generated from a 2026-04-20 scoping discussion. Used as the detailed scope definition for the Phase 2 evaluation-validation paper.
- [`deferred_items_registry.md`](deferred_items_registry.md) — aggregate registry of ALL deferred items across the project (methodology refinement, scope expansion, cross-model extensions, language study, ChemOntology pilot execution, open issues from `improvements/open_issues.md`, figure/table updates, references). Cross-references the authoritative source for each item.

---

## Status of Phase 2 commitment

The main-manuscript `Methods 6` and `SI-8` adopt **Option γ** for the pilot evaluation:

1. The current Digital Discovery submission uses `SI-8.5` as a placeholder stating that "pilot-application data will be reported in a separate publication."
2. `Methods 6` / `SI-8.1`–`SI-8.4` operationally define the protocol in enough detail to make Phase 2 executable.
3. This `future_work/` folder documents what Phase 2 needs to address, including the issues catalogued in `pilot_evaluation_issues.md`.

The explicit Phase 2 commitment allows the current submission to claim the protocol is "operational by design" while avoiding the n=1 pilot-data risk discussed in `pilot_evaluation_issues.md` §C.

---

## Roadmap for filling this folder

As new items are deferred from the current iteration, they should be added to `deferred_items_registry.md` with:

1. A short description.
2. Link to the authoritative source (e.g., `improvements/open_issues.md` OI-number, `si_issues_log.md` Issue number, specific manuscript/SI paragraph).
3. Assessment of which Phase 2 (or later) deliverable would resolve the item.
4. Any dependencies on external events (e.g., "requires Gemini 3 Flash model-pinning to become available via Antigravity API").

New focused documents (e.g., `phase2_paper_outline.md`, `bilingual_study_protocol.md`, `chemontology_pilot_execution_plan.md`) should be added here as they are developed, and indexed above.
