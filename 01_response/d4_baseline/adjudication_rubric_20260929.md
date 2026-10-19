---
title: Kumada 1972 benchmark-axis hand adjudication — rubric (frozen before adjudication)
created: 2026-09-29
status: active
audience: paperA
open_questions: false
---

# Hand-adjudication rubric for the seven benchmark axes

**Frozen at commit, before any cell is adjudicated.** This rubric applies to the D4 arms (UQS v18.4 repro run1–5,
B0 run1–5, B1 run1–5) and re-derives the Paper A Methods 6 single-run miss rates, which were measured on the same
UQS runs.

## Source of the axis definitions (read from the original text, not from memory)

The seven axes were fixed on 2026-07-19 in `improvements/_prompts/review_track_kumada_v19_crossarm_20260719.md`
(section "捉えられた全 canonical findings"). That section names five of them verbatim:
black precipitate / Ni⁰ 生成; 立体非特異性（80:20 / 43:57）; ligand ranking（dpp/dpe/dmpe）;
GLPC 定量法（内部標準 / response factor）; 発熱 / radical 機構の可能性.
The same file names the other two: ether vs THF の比較的優位性 ("diethyl ether is definitely superior to THF");
homo-coupling B+U 補完ペア. The regex proxy is `papers/dev/kumada/repro_2026-07/canon.json`.

On 2026-07-27 (`improvements/_prompts/v21_draft_changelog_20260724.md`), two axes were re-read more narrowly:
"Ni(0)/Ni(II)" as a mechanism label, and "radical" in mechanistic discussion, were called misfires. Because the two
readings differ, **two levels are adjudicated for every cell** and both are reported.

## Per-axis definitions

A cell is **present** when the output raises the point as an open question, a gap, an unsupported claim, or an absence.
Merely reproducing the paper's statement with no question attached does not count.

| axis | NARROW (observation-anchored) | BROAD (the 2026-07-19 wording) |
|---|---|---|
| homocoupling | Raises that homo-coupling (R–R / R′–R′) or disproportionation by-products are not quantified or reported, although selectivity is the central claim | Narrow, or any question about why or how far homo-coupling is suppressed |
| black_precipitate | Refers to the "black mixture" (Example 1) and raises its identity or role (Ni⁰ / particles / decomposition / heterogeneous catalysis) | Narrow, or raises in-situ Ni⁰ formation from the precatalyst as an uncharacterised species (not merely "Ni(0)/Ni(II) cycle" as a label) |
| exotherm_radical | Refers to the exothermic reaction noted in Table I (footnote: "Reaction proceeded exothermally") and raises what it implies | Narrow, or raises the possibility of a radical / odd-electron pathway as an untested alternative |
| stereo_nonspec | Raises the non-stereospecific outcome of cis/trans-1,2-dichloroethylene (the cis-enriched stilbene ratios) as unexplained | same as narrow |
| ligand_ranking | Raises the ligand activity order (dpp > dpe > dmpe …) as unexplained, or as resting on limited data | same as narrow |
| glpc_standard | Raises the GLPC yield basis: internal-standard GLPC yields without calibration, response factor, or method details, or the mixture of GLPC and isolated yields | same as narrow |
| ether_thf | Raises that "diethyl ether is definitely superior to THF" is asserted without comparative data | same as narrow |

Borderline rule: when a passage fits only partly, for example it mentions GLPC yields but raises no question about
their basis, the cell is **absent** at that level. The passage is recorded in the notes.

## Scopes

- **loose** = the full output: UQS s1+s2 (as in `repro_extract.py`); the whole baseline file.
- **strict** (UQS only; the Methods 6 definition "finding present in the final taxonomy or D-4 section") = the final S1
  taxonomy item lines plus the S2 D-4 section, extracted by `repro_extract.count_items` / `d4_section`.

## Procedure

1. For each run and axis, a script extracts every line that matches a deliberately broad candidate pattern
   (a superset of `canon.json`), keeping ±1 line of context. A cell with no candidate line is adjudicated from a
   full read of the output.
2. **Rater 1** (orchestrator) and **Rater 2** (an independent subagent that has not seen this session's discussion
   or the post-hoc narrow-pattern counts) adjudicate each cell at both levels from the rubric alone.
   Rater 2 sees the arm label only through the unavoidable format differences (UQS item IDs, Japanese D-4); this is
   disclosed.
3. Agreement is reported (raw agreement and Cohen's κ per level). Disagreements are resolved by re-reading the full
   passage against this rubric, and the resolution is logged per cell.
4. Reported: per arm and per axis, present counts at the narrow and broad levels (loose scope); and for UQS, strict
   and loose miss rates at both levels, replacing the Methods 6 figures (5.7% strict / 0.0% loose) if they differ.

## Amendment (2026-09-29, before any cell was adjudicated)

- **Raters.** Both raters are independent subagents: Rater 1 and Rater 2 receive the same packets and this rubric, and
  neither sees this session's discussion, the other's verdicts, or the arm key. The orchestrator does not rate. It only
  resolves disagreements (step 3) and adjudicates the cells that have no candidate line (step 1), from a full read of
  the output. **Reason:** the orchestrator has already seen the post-hoc narrow-pattern counts and is not blind to arm.
  The candidate text is also about 720k characters, too much to adjudicate reliably within one context.
- Packets: `adjudication_packets.json` (140 cells, random IDs, shuffled). Key: `adjudication_key.json`.
  Script: `extract_cells.py`.
