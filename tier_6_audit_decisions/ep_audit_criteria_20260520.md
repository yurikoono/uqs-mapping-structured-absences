---
title: Paper A — EP filling criteria (locked before retrieval audit)
created: 2026-05-20
status: active
audience: paperA
open_questions: true
---

# Paper A — EP filling criteria (locked before retrieval audit)

## Purpose

This document is the **Phase 0 0B artifact** of the Paper A Digital Discovery (DD) revision project. It fixes the **Complete / Partial / Minimal / Non-filler** judgement criteria for each Tier 1 #1 audit-target EP **before** the WoS / Scopus / Google Scholar / Crossref structured retrieval begins.

This pre-retrieval lock is the **post-hoc adjustment defense** against the reviewer concern "the authors adjusted the criteria after seeing the data." All Tier 1 #1 audit results must be classified against the §2–§5 criteria below, and any criterion modification during audit must be (a) documented with rationale, (b) preceded by an attempt to apply the original criterion, and (c) reported transparently in SI.

The four EPs audited (EP-03a + EP-07a as positive controls; EP-08a + EP-09a as negative claims) are sampled from the ten-EP Kumada 1972 dictionary (`manuscript_A/SI/output/SI-3.md` §SI-3.7). Source EP definitions are reproduced verbatim from SI-3 to keep this criteria document anchored.

## 1. Common rubric

For each EP, audit candidate papers are classified into one of four levels:

| Level | Rule of thumb | Manuscript treatment |
|---|---|---|
| **Complete filler** | Closes the EP requirement at its source-paper scope without important residual gaps | Cited as decisive filling; appears in EP filling map (Results Part 2) |
| **Partial filler** | Closes part of the EP requirement (subset of substrates / single dimension / different system) | Cited with explicit hedge ("partial filling at X dimension"); enters EP filling map with note |
| **Minimal filler** | Mentions the topic but does not deliver the required evidence form | Optional reference; not counted toward EP closure |
| **Non-filler** | No paper at this level within retrieval | Negative claim recorded with corpus-boundedness caveat |

**Cross-cutting rules** (apply to all four EPs):

- **System identity**: Filling must be in the dppe-Ni Kumada system, OR in a system whose explicit mapping back to dppe-Ni is provided by the authors. Filling in clearly distinct systems (Fe-Kumada / Pd cross-coupling / different ligand class without bridge) is at most Minimal unless the original authors map back.
- **Same-conditions principle**: For "head-to-head" claims (EP-09a-style), conditions matching means substrate identity + solvent class + temperature window + comparable workup. Conditions modified to favour one system are not same-conditions.
- **Ambiguous case handling**: When a candidate paper sits between Partial and Minimal, the auditor records the candidate, the deciding factor, and the chosen level. The decision is not re-litigated after Tier 1 #1 results are reviewed for narrative effect.
- **Multi-paper aggregation**: If two papers together meet Complete-filler conditions (e.g., one supplies mechanism observation, another supplies cross-validation), the EP is recorded as Complete-by-aggregation with both papers cited; this is distinguished from single-paper Complete in the EP filling map.

## 2. EP-03a — Direct-observation / state-assignment pack (VQ-3, positive control)

### Source EP definition (verbatim, SI-3.7)

> **EP-03a Direct-observation / state-assignment pack** — VQ-3. Source RI / SRG: RI-03 via SRG-1. Case-specific implementation: (i) follow the stoichiometric reaction of NiCl₂(dpe) with PhMgBr (eq 2 analog) by low-temperature NMR or ESI-MS to observe the putative intermediate Ph₂Ni(dpe) (1); (ii) verify that the isolated intermediate or a model complex (e.g., Me₂Ni(dpe)) reacts with PhCl to give eq 3 coupling; (iii) exclude Ni(I)/Ni(III) radical pathways with a radical-clock substrate or EPR measurements.

### Audit criteria

**Complete filler** — both required:

1. Direct spectroscopic observation (low-T NMR / ESI-MS / EPR / X-ray) of at least **two** of the three proposed intermediates (1, 2, 3) of Kumada eqs 2–4 under stoichiometric or catalytic conditions matching the dppe-Ni system (or a system explicitly mapped back to dppe-Ni); OR a unified computational study whose intermediate identities are cross-validated with experimental observation (e.g., Chen 2019 *J. Am. Chem. Soc.*, 141, 5835).
2. Treatment of the radical-pathway question (Ni(I)/Ni(III)) via radical clock or EPR, OR a chemically reasoned exclusion against radical participation.

**Partial filler** — any one:

- Observation of **one** intermediate (e.g., Ph₂Ni(dpe) only) without the chain to eq 3 verification
- Observation in a related but not strictly dppe-Ni system (different bidentate phosphine, different aryl-alkyl pair) with no explicit mapping to dppe-Ni
- Computational study without experimental cross-validation
- Observation in a precursor / model complex (e.g., dipy-Ni) referenced as an analogy

**Minimal filler** — any one:

- Mention of intermediates as "putative" or "presumed" without direct observation
- Observation in a clearly distinct system (Fe-Kumada / Pd / Ru analog) without mapping back
- Inference from product distribution alone

**Non-filler**:

- No paper within retrieval discusses intermediate observation or computational identity in a way that connects to Kumada eqs 2–4

### Why suitable as positive control

EP-03a is expected to have **clear positive filling** in the literature (Chen 2019, Dawson 2020 mark the 49-year decisive milestone reported in Results Part 2). It therefore tests whether UQS-guided retrieval can recover **known filling** — a true positive baseline against which the negative EP-08a / EP-09a claims gain credibility.

### Pre-known anchors (do not double-count as audit findings)

- Morrell–Kochi 1975 *J. Am. Chem. Soc.* (aryl-alkyl Ni intermediates) — Partial
- Chen 2019 *J. Am. Chem. Soc.* 141, 5835 (mechanism-kinetics unification, benzylic-ether Kumada) — Complete-by-aggregation
- Dawson 2020 (spectroscopic resting-state assignment for the Kumada system) — Complete-by-aggregation

The structured retrieval audit must **also** check whether papers between 1975–2018 fill EP-03a at Partial / Minimal level. False negatives in the LLM-parametric retrieval at this band are the most informative finding for DD reviewers.

## 3. EP-07a — Boundary-test pack (VQ-2, positive control, scope-extension)

### Source EP definition (verbatim, SI-3.7)

> **EP-07a Boundary-test pack** — VQ-2 (for scope boundary). Source RI / SRG: RI-07 via SRG-4. Case-specific implementation: (i) test n-BuCl, sec-BuCl, PhCH₂Cl (Csp³ halides) under the same conditions (NiCl₂(dpe) / Et₂O) with PhMgBr and present inactive / poorly selective results as a "failed scope" row of Table I; (ii) test PhBr and PhI with the reference substrate (n-BuMgBr) under the same conditions as PhCl for direct yield comparison.

### Audit criteria

**Complete filler** — both required:

1. Same-conditions test of at least **three** Csp³ halide substrates (e.g., n-BuCl, sec-BuCl, PhCH₂Cl, c-hex-Cl) in the dppe-Ni Kumada system, with documented yield / selectivity outcomes (including "failed" outcomes).
2. Same-conditions PhCl / PhBr / PhI direct yield comparison under matched dppe-Ni conditions.

**Partial filler** — any one:

- Either the Csp³ scope-extension OR the Cl/Br/I comparison reported, not both
- Scope explored across substrates but conditions not matched between substrates
- Comparable scope explored in a related but not strict dppe-Ni system

**Minimal filler** — any one:

- Scope tested under modified catalyst / ligand (e.g., dppp, dppf) without strict dppe-Ni replication
- Single Csp³ substrate tested
- Cl/Br/I comparison reported qualitatively only

**Non-filler**:

- No scope-extension paper within retrieval addresses Csp³ halides or Cl/Br/I comparison in the Kumada system

### Why suitable as positive control

EP-07a tests **publication-incentive-aligned** filling — substrate-scope extension is broadly considered the most rewarded follow-up activity. We therefore expect dense literature filling, providing a second positive baseline orthogonal to EP-03a (which tests mechanism-extension). If UQS-guided retrieval misses substantial scope-extension filling here, that is a calibration finding for the retrieval methodology.

### Pre-known anchors (do not double-count as audit findings)

- Tamao et al. *Bull. Chem. Soc. Jpn.* 1976 (Full Paper I; scope extension) — Partial / Complete depending on Csp³ scope completeness
- Subsequent Kumada-system substrate-scope papers in the 1976–1985 window — expected Partial

## 4. EP-08a — Replication / uncertainty pack (VQ-4, negative claim)

### Source EP definition (verbatim, SI-3.7)

> **EP-08a Replication / uncertainty pack** — VQ-4. Source RI / SRG: RI-08 via SRG-2, SRG-6, SRG-3. Case-specific implementation: (i) for all 11 Table I entries, perform n ≥ 3 replicates with standard deviations on yield; (ii) for cis/trans-dichloroethylene substrates, n ≥ 3 replicates with glpc and ¹H NMR cross-method determination; (iii) time-course (1 h, 5 h, 20 h) to distinguish kinetic vs thermodynamic product.

### Audit criteria

**Complete filler** — all three required:

1. For all 11 (or a clearly identified core subset n ≥ 8) Table I-type entries, **n ≥ 3 replicates with reported standard deviations or 95% CI**
2. **Cross-method verification** (GC + NMR, or equivalent) on at least the cis/trans-dichloroethylene substrate class
3. **Time-course** at 3+ time points to distinguish kinetic from thermodynamic product on at least one substrate where it matters

**Partial filler** — any one:

- Replicate data with n ≥ 3 + SD reported for **a subset** of entries (not all 11)
- Cross-method verification on one substrate without replicates
- Time-course alone, without per-entry replicate SDs

**Minimal filler** — any one:

- Anecdotal mention of "replicated" without n or SD
- Replicate study performed but only summary statistic (mean ± unspecified) without distribution
- A single replicate measurement at a non-Table-I substrate

**Non-filler**:

- No replicate measurement with reported uncertainty found in the published academic literature within retrieval window for the dppe-Ni Kumada system at substrate-matched conditions

### Why suitable as negative-claim test

EP-08a is the central **negative claim** of Paper A (Results Part 2 / EP-08a non-filling). Cross-model convergence (Sonnet + GPT-5.4 Thinking both find no filling) has been documented in SI-3.7 — but this is by definition LLM-parametric retrieval. The Tier 1 #1 structured retrieval audit tests whether the negative claim survives WoS + Scopus + Google Scholar + Crossref structured search. **This is the highest-stakes audit item for DD reviewers** and must be paired with the §4 non-claim from `paperA_dd_target_narrative_20260520.md`.

### Search terms locked

Per SI-3.7 EP-08a search term derivation:
- "Kumada cross-coupling standard deviation replicate measurement"
- "cis/trans stilbene kinetic thermodynamic product"
- Auxiliary: "Ni(II) phosphine Grignard replicate uncertainty"
- Auxiliary: "NiCl₂(dpe) cross-coupling kinetics time-course"

### Boundary case handling (must be decided pre-retrieval)

- **Process-chemistry / scale-up papers in academic journals**: These often report yield variance under industrial-style replication. If found, classified as Partial (different scale, but quantitative replication).
- **Methodology papers reporting "all yields are average of N runs"**: Without per-entry SD, classified as Minimal even if N is stated.
- **Recent process-intensification or flow-chemistry papers**: If they replicate the original 11 Table I-type substrates with SDs, classified as Partial (system identity may differ slightly).

## 5. EP-09a — Internal benchmark pack (VQ-4, negative claim)

### Source EP definition (verbatim, SI-3.7)

> **EP-09a Internal benchmark pack** — VQ-4. Source RI / SRG: RI-09 via SRG-2, SRG-4, CLA-1, CLA-2. Case-specific implementation: parallel reactions with Tamura-Kochi (Fe) and Corriu/Masse (Ni(acac)₂) and Corey/Whitesides stoichiometric reagents on the same substrate, yielding direct numerical yield, selectivity, and operability comparisons.

### Audit criteria

**Complete filler** — both required:

1. **Parallel reaction with at least 2 of the 3 named benchmarks** (Corriu/Masse Ni(acac)₂; Tamura-Kochi Fe; Corey/Whitesides stoichiometric) at **substrate-matched + condition-matched** setup
2. **Numerical comparison** of yield AND selectivity AND operability (workup convenience / catalyst loading / reaction time)

**Partial filler** — any one:

- 1 benchmark comparison with same substrate + matched conditions
- All 3 benchmarks but with different substrates or different conditions
- 2 benchmarks with same substrate but conditions not strictly matched (e.g., different solvent class)

**Minimal filler** — any one:

- Mention of "predecessor catalysts" or "earlier Ni systems" without numerical comparison
- Benchmark to non-named (non-Corriu/Tamura/Corey) systems with no return to dppe-Ni context
- Verbal claim of superiority without head-to-head data

**Non-filler**:

- No same-axis head-to-head benchmark with **named predecessor catalysts** (Corriu/Masse Ni(acac)₂; Tamura-Kochi Fe; Corey/Whitesides) in retrieval

### Why suitable as negative-claim test

EP-09a is the **second central negative claim** of Paper A (alongside EP-08a). The publication-incentive-misalignment argument (Discussion 1) hinges on this: benchmarking against predecessors is rarely rewarded with novelty, so it tends to remain unwritten. The Tier 1 #1 structured retrieval audit tests whether this absence survives WoS + Scopus + Google Scholar + Crossref.

### Search terms locked

Per SI-3.7 EP-09a search term derivation:
- "Kumada coupling benchmark vs Corriu Masse"
- "Ni(acac)₂ vs NiCl₂(dpe) Grignard coupling comparison"
- Auxiliary: "Ni Fe Grignard cross-coupling head-to-head"
- Auxiliary: "Kumada Tamura-Kochi benchmark substrate-matched"

### Boundary case handling (must be decided pre-retrieval)

- **Review articles citing both Corriu and Kumada**: Citation alone is Minimal, not Partial. Only numerical comparison data counts.
- **Pd cross-coupling era papers (post-1980) comparing to Ni-Kumada systems**: System distance is significant; classified as Minimal unless the comparison is presented as a fair head-to-head with conditions strictly matched.
- **Mechanistic-comparison papers (e.g., Fe-Kumada vs Ni-Kumada)**: If numerical yield + selectivity data are reported at matched conditions, classified as Partial; the "same family" caveat is recorded.

## 6. Inter-rater reliability handling

Tier 1 #1 retrieval audit is performed by Claude (Sonnet) + one human reviewer (author or co-author). For each candidate paper:

1. Claude proposes a level based on the §2–§5 criteria
2. Human reviewer accepts / modifies / rejects
3. Disagreements are documented with rationale
4. Final level is the human reviewer's decision; Claude's proposal is recorded as a separate column

This is **separate from** the Tier 1 #5 Internal Mini-Audit (which evaluates UQS workflow outputs against the protocol). The Tier 1 #1 audit is performed against the criteria locked in this document; the Mini-Audit is performed against the Mini-Audit Protocol v0.1.

## 7. Retrieval scope (locked pre-audit)

Per `paperA_dd_target_narrative_20260520.md` §4 non-claim:

| Database | Mandatory | Note |
|---|---|---|
| Web of Science (WoS) | Yes | Hokkaido U subscription assumed |
| Scopus | Yes | Hokkaido U subscription assumed |
| Google Scholar | Yes (sanity check) | Public access |
| Crossref | Yes (DOI / bibliographic verification) | Public access |
| SciFinder | Optional | If accessible; otherwise note "bibliographic, not reaction-database exhaustive" |
| Reaxys | Optional | If accessible; otherwise note as above |
| Semantic Scholar | Optional auxiliary | Public access |

Retrieval window: **1972–2026** (publication years; full 54-year span per Paper A baseline). Date of search will be recorded in SI table.

## 8. Audit output format

For each EP (03a / 07a / 08a / 09a), the SI audit table contains:

- Search executed (database / query / date)
- Candidate paper list (DOI, first author, year, journal, title)
- Per-paper level (Complete / Partial / Minimal / not-filling / not-applicable)
- Claude proposal vs human reviewer final decision (transparency column)
- Brief rationale (1-3 sentences per paper)
- False positive / false negative discussion at the EP summary level

## 9. Document status

Phase 0 0B artifact. **Criteria here are the locked operational baseline** for Tier 1 #1 retrieval audit.

- §1–§5: 凍結 (any modification requires explicit revision-cycle decision and is logged in SI as a deviation)
- §6–§8: Tier 1 work 進行と共に refine 可
- §9: open questions: WoS / Scopus subscription confirmation, human reviewer assignment

## Related documents

- Phase 0 0A claim lock: `improvements/paperA_dd_target_narrative_20260520.md`
- v11 snapshot: `improvements/paperA_v11_snapshot_20260520.md`
- Locked revision plan: `improvements/paperA_dd_revision_plan_20260520.md`
- Source EP definitions: `manuscript_A/SI/output/SI-3.md` §SI-3.7
- Internal Mini-Audit Protocol: `improvements/paperA_Internal_Mini-Audit_Protocol_for_UQS_Outputs.md`
