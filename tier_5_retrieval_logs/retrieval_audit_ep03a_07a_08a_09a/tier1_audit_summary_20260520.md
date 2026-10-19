---
title: Paper A — Tier 1 #1 retrieval audit cumulative summary
created: 2026-05-20
status: active
audience: paperA
open_questions: false
---

# Paper A — Tier 1 #1 retrieval audit cumulative summary (2026-05-20)

## Overview

Structured Web of Science Core Collection retrieval audit for four Evidence Packs targeting the Digital Discovery DD reviewer-defense vulnerabilities identified by GPT-3/4/5: the negative claim that EP-08a (replicate measurement) and EP-09a (substrate-matched head-to-head benchmark) remain unfilled in the published academic record after 54 years.

Audit performed against criteria locked **before** retrieval in `improvements/paperA_ep_audit_criteria_20260520.md` (Phase 0 0B).

## Module structure

| Module | EP | Type | Variants run | Cumulative hits | Audit method |
|---|---|---|---|---|---|
| 1 | EP-03a | Positive control (mechanistic) | n=1 WoS pilot (2026-04-20) | ≈49 hits, 0 LLM-overlap | Pre-existing SI-9 pilot (5 query variants); not re-run |
| 2 | EP-08a | Negative claim (replicates) | 4 strict + 2 syntax-relaxed = 6 formulations | **11** | This audit |
| 3 | EP-09a | Negative claim (benchmark) | 4 variants | **11** | This audit |
| 4 | EP-07a | Positive control (scope) | 2 variants | **9** | This audit |
| **Total (Modules 2+3+4)** | — | — | 14 query formulations | **31** | — |

## Cumulative classification (Modules 2+3+4)

| EP | Hits | Complete | Partial | Minimal | Not applicable | Verdict |
|---|---|---|---|---|---|---|
| EP-08a (negative) | 11 | 0 | 0 | 0 | 11 | **Negative claim survives structured retrieval** |
| EP-09a (negative) | 11 | 0 | 0 | 2 | 9 | **Negative claim survives structured retrieval** (2 Minimal at weakest inclusion criteria) |
| EP-07a (positive control) | 9 | 0 | 2 | 0 | 7 | **Positive control returns Partial fillers** → audit methodology calibrated |

## Key findings

### 1. Negative claims (EP-08a + EP-09a) — strongly supported

**Across 22 cumulative candidate papers from 10 orthogonal WoS query formulations, zero provide Complete or Partial filler conditions** per 0B §4 / §5 criteria.

EP-08a (replicate measurement):
- 4 strict variants: A (general Ni-Kumada-reproducibility) / B (Ni-specific catalyst + replicate methodology) / C (cis/trans + kinetic + Ni/Grignard) / D (named-reaction control)
- 2 syntax-relaxed formulations (Variant D′ AND co-occurrence; Variant D″ NEAR/3 proximity) — both 0 hits, **ruling out hyphen-syntax artifact** in original Variant D

EP-09a (head-to-head benchmark):
- 4 variants: A (strict named-benchmark) / B (head-to-head Ni-Grignard vocabulary) / C (comparison language + predecessor terms) / D (Fe-Kumada vs Ni-Kumada matched-conditions)
- 2 Minimal candidates at weakest inclusion criteria: Quesnelle-Snieckus 2018 (cross-reaction-class qualitative); Berding 2009 (verbal "highest activity reported to date")

### 2. Positive control (EP-07a) — audit methodology calibrated ✓

**2 Partial fillers identified** under identical retrieval methodology:

- **Breitenfeld et al. 2013** (*J. Am. Chem. Soc.*) — N2N-Ni pincer alkyl-alkyl Kumada paradigm-shift; mechanism study revealing bimetallic radical OA
- **Garcia et al. 2016** (*ACS Catal.*) — PNNN-Pyr-Ni pincer cross-coupling of nonactivated secondary alkyl halides

Both papers from the Hu group at EPFL using Ni-pincer ligands (structurally distinct from original 1972 dppe-Ni). Consistent with the **paradigm-shift filling layer (2009-2024)** narrative in Results Part 2.

The positive control finding **directly calibrates the EP-08a / EP-09a 0-Partial results as genuine structural absences**, not retrieval-methodology artifacts.

### 3. Three convergent diagnostic patterns (EP-09a Module)

Across EP-09a Variants A-D, three structural patterns emerged in keyword matches:

1. **Catalyst-design papers dominate** keyword matches (NHC-Ni / pincer-Ni / dinuclear-Ni / Co-Zr) — predecessor terms appear as historical context, not as benchmark targets
2. **Within-family comparisons dominate** when comparison language IS used (Zhou 2014 Co/Zr Xyl vs Mes ligand variants) — internal optimisation, not external predecessor benchmark
3. **Explicit benchmark vocabulary co-occurs with cross-coupling-Grignard effectively never** (Variant B: 1 off-target hit; Variant D: 0 hits)

These three patterns provide **empirical direct support** for the publication-incentive interpretation developed in Discussion 1: substrate-matched, condition-matched head-to-head benchmarking against named predecessors is structurally underwritten in modern chemistry publishing.

### 4. Soler-Yanes 2014 boundary observation (key diagnostic)

Soler-Yanes et al. 2014 (*Eur. J. Org. Chem.*) was found in EP-09a Variant A. The paper uses **Ni(acac)₂-TMEDA** (the Corriu/Masse predecessor catalyst class) as their **chosen** catalyst for new substrate scope (benzyl/allyl chlorides), but does **NOT benchmark dppe-Ni against Ni(acac)₂ at matched conditions**.

This is a clean empirical illustration of the publication-incentive interpretation:

- Using existing catalyst for new substrate scope = **publishable novelty** ✓ (Soler-Yanes 2014)
- Benchmarking existing catalyst against another existing catalyst at matched conditions = **no novelty, rarely published** ✗ (EP-09a target, structurally absent)

### 5. Triangulation across retrieval modalities

Both negative claims (EP-08a, EP-09a) are now supported by **three independent retrieval modalities**:

| Modality | EP-08a | EP-09a |
|---|---|---|
| LLM-parametric (Sonnet + GPT-5.4 cross-vendor convergence) | 0 filler | 0 filler |
| Open-web preliminary (Google Scholar + Crossref) | 0 filler (PMC8036247 / Joshi-Pangu 2011 / 50kg PRD all not applicable) | 0 filler (Kambe 2002 Minimal; Hazari 2017 Minimal; NiCl₂(dppe) Suzuki paper not applicable) |
| **WoS structured retrieval** | **0 filler across 11 hits / 6 formulations** | **0 filler across 11 hits / 4 variants** |

## Methodology implications for the DD submission

The Tier 1 #1 audit results enable the following DD reviewer-defense narrative for the EP-08a / EP-09a negative claims:

> **Claim**: EP-08a (replicate-measurement data with reported standard deviations for the dppe-Ni Kumada Table I substrate set) and EP-09a (substrate-matched, condition-matched numerical head-to-head benchmark of dppe-Ni vs Corriu/Masse Ni(acac)₂ / Tamura-Kochi Fe / Corey-Whitesides stoichiometric) did not surface in the published academic record over the 54-year window.
>
> **Audit methods**: LLM-parametric retrieval (Sonnet 4.6 + GPT-5.4 Thinking cross-vendor convergence); Web of Science Core Collection structured retrieval across 4 variants per EP (EP-08a additionally tested with 2 syntax-relaxed formulations); per-candidate human classification against criteria locked pre-retrieval (Phase 0 0B). Positive-control parallel audit for EP-07a (substrate-scope extension) returned 2 Partial fillers under identical methodology, calibrating that the audit pipeline successfully identifies filling literature when it exists.
>
> **Caveat**: This is an absence-of-evidence observation in the searched academic record (WoS Core Collection + LLM-parametric retrieval + open-web preliminary check), not evidence of absence in global chemical knowledge. For reaction systems with substantial industrial deployment such as Kumada cross-coupling, evidence relevant to EP-08a / EP-09a plausibly exists in patent literature and proprietary process records that fall outside this observable space (Methods §3 *Note on academic corpus boundedness*).

## Cross-checks remaining (optional)

- **Scopus 4 variants per EP**: orthogonal database; 0-Partial / 0-Complete result expected based on WoS convergence; user-side execution optional for thoroughness (not gating for submission)
- **Crossref API DOI verification**: all 31 candidates have DOIs verified at WoS-export level; full DOI-level Crossref check is optional secondary verification

## Manuscript integration phase (next)

The audit data above feeds into manuscript at:

| Section | Update |
|---|---|
| Methods §3 (Note on academic corpus boundedness) | Add WoS structured-retrieval-audit paragraph (≈ 150 words) |
| Methods §X (new sub-section "Structured bibliographic retrieval audit") | New 200-300 word sub-section describing the audit methodology |
| Results Part 2 | Update EP-08a / EP-09a non-detection claim with WoS audit triangulation reference |
| Discussion 1 | Reference the audit findings + Soler-Yanes 2014 boundary observation |
| Limitations L1 | Reference the audit as a partial mitigation of the corpus-boundedness limitation |
| **SI table (new)** | Per-EP candidate table with 0B classification; published in supplementary information |
| SI-9 extension | Extend the existing EP-03a pilot section to cover Modules 2/3/4; update 5-failure-mode taxonomy with new findings |
| Data Availability Tier 5 | Already includes `validation/ep{03a,07a,08a,09a}_wos_llm/` directories per Phase 0 0A §6 |

## File locations

- Per-EP validation directories:
  - `validation/ep03a_wos_llm/` (pre-existing pilot, 2026-04-20)
  - `validation/ep07a_wos_llm/` (this audit)
  - `validation/ep08a_wos_llm/` (this audit)
  - `validation/ep09a_wos_llm/` (this audit)
- Master execution plan: `improvements/paperA_tier1_retrieval_audit_execution_20260520.md`
- 0B audit criteria (locked pre-retrieval): `improvements/paperA_ep_audit_criteria_20260520.md`
- Phase 0 0A claim lock: `improvements/paperA_dd_target_narrative_20260520.md`
- Query strings: `improvements/paperA_tier1_wos_scopus_queries_ready_20260520.md`
- This summary: `validation/tier1_audit_summary_20260520.md`
