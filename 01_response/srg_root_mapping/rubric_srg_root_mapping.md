---
title: Paper A R1 — SRG root mapping across models (rubric, frozen before rating)
created: 2026-09-29
status: active
audience: paperA
open_questions: false
---

# Rubric: which of the six Kumada 1972 SRG roots does each block address?

**Purpose.** Results Part 4 states that "four models from two vendor families (SI-6) agreed on the same six SRGs for Kumada
1972". SI-6 itself reports 5 (Haiku 4.5), 6 (Sonnet 4.6), 10 (Opus 4.7) and 6 (GPT-5.4 Thinking) SRGs, so the statement has
to be re-derived from the primary outputs. The same mapping serves as endpoint 3 of the Haiku 4.5 replication
(`haiku45_replication/preregistration_haiku45_R1.md`).

**Frozen at commit, before any rating.**

## The six roots (SI-3.4, the Sonnet 4.6 v17 Stage 3 record)

Each root is identified by its central data absence, as stated in its evidential requirement (ER).

| root | central data absence |
|---|---|
| R1 | Proposed catalytic cycle (eq 2–4) has no experimental evidence in the NiCl₂(dpe) system: intermediates not isolated or observed; the cycle rests on analogy with other Ni systems. |
| R2 | The "selective" cross-coupling claim has no by-product data: homo-coupled, protodemetalated or β-eliminated products are not quantified, and the mass balance is not closed. |
| R3 | Analytical quality of the Table I yields: glpc conditions, internal-standard identity, the yield basis, or the mixture of glpc and isolated yields are not reported uniformly. |
| R4 | Scope restriction: "Only Csp² halides can be used" is untested on Csp³ halides, and/or the chloride-reactivity claim lacks comparison against Br and I. |
| R5 | Solvent and condition effects: "diethyl ether is definitely superior to THF" (or other condition claims) has no quantitative basis. |
| R6 | Cis/trans (stereochemical) observation: the ratios for 1,2-dichloroethylene (80:20, 43:57) are reported without replication or uncertainty, or the stereochemical outcome is left unexplained. |

## Decision per block

For each block, list every root whose central data absence the block **addresses as one of its own central absences**,
judged from the block's name, its ER and its case-specific implementation. A block may address several roots, for example
when it merges two of them. A root that is mentioned only in passing, for example among the notes, does not count.

If the block addresses none of the six, record `none` and give a short label for what it does address, for example
"catalyst end state / black mixture" or "β-H tolerance".

Blocks that are only section headers with no content of their own get `header`.

Output per block: `{"block": id, "roots": ["R1", …] or [], "none_label": "…" or "", "header": true|false, "evidence": "≤25-word quote"}`.

## Aggregation (fixed now)

For each output, a root is **present** if at least one block addresses it. The results are reported as follows:
- a root × output table;
- per root, the number of outputs in which it is present;
- the Haiku 2026-09 replicate runs set against the Haiku 2026-04 run.

The Sonnet reference output is included as a check: its SRG-1…6 should map to R1…R6.
