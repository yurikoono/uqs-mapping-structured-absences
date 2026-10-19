# Stage 1: Multi-Perspective Structural Extraction — Turn 1
<!-- prompt_version: stage1-v184-20260502 / turn1 -->
**Language: English throughout**

Report the prompt version at the start of your output:
```
prompt_version: stage1-v184-20260502
```

---

<!-- v17 C8: PDF direct reading -->
## PDF reading note

Read the paper PDF directly using the Read tool (multimodal reading).
If the PDF is 20 pages or fewer, read the entire file in one call.
If the PDF exceeds 20 pages, split into page ranges (e.g., "1-20", "21-40")
with a maximum of 20 pages per call. Do not use pdftotext or other
text-extraction tools. Figures, schemes, structural formulas, and energy
diagrams are available for analysis through direct PDF reading.

---

## Procedure overview

This Stage is executed as a **4-turn sequential accumulation** within a
single chat session. Each turn adds a new disciplinary perspective. The
final turn synthesizes all questions into structured A/B/C/U categories
with cross-field temperature metadata.

**Agent naming convention:** Agents are labeled V1, V2, V3, V4 (Viewpoint 1–4).
The prefix "V" avoids collision with Greek letters used in chemistry
(e.g., α-carbon, β-hydride elimination, γ-butyrolactone, δ-bond).

```
Turn 1 (V1): Paper's own field expert — generates initial questions
Turn 2 (V2): Adjacent field expert — adds questions + re-evaluates V1 overlaps
Turn 3 (V3): Methodology/statistics expert — adds questions + re-evaluates overlaps
Turn 4 (synthesis): Classify all questions into A/B/C/U with convergence metadata
```

---

## Agent count guidance

The default is **3 agents (V1, V2, V3)**. This is calibrated for
communication-format papers (2–4 pages). Adjust as follows:

| Paper format | Recommended agents | Rationale |
|---|---|---|
| Communication / Letter (2–4 pp) | 3 (V1, V2, V3) | 3 agents already produce ~18 overlaps; more would saturate |
| Full paper (8–15 pp) | 3–4 | A 4th agent (V4) may be warranted if the paper spans multiple methodologies |
| Review / perspective (15+ pp) | 4 | Broader scope benefits from an additional perspective |

If a 4th agent (V4) is used, insert it between Turn 3 and Turn 4, following
the same format as Turn 3 (new questions + overlap re-evaluation).

---

## Output discipline

Each turn produces its own structured output. Only Turn 4's output is
passed to Stage 2. Do not add explanatory prose, follow-up questions,
or text outside the specified fields.

---

## Multi-paper PDFs — target-paper boundary (mandatory first step)

Copy the three fields below from the Stage 0 output before doing anything else:

```
target_title:   [copy BIB-1]
target_authors: [copy BIB-2]
target_start:   [copy BIB-8a — first line of target paper's title]
target_end:     [copy BIB-8b — first line of next paper's title, or [REDACTED: paper boundary quote; see Tier 9]]
```

**Universal boundary rule — applies to every turn and every section:**

Every passage, citation, observation, or inference must be grounded solely
in text that falls between `target_start` and `target_end`.

- Text before `target_start` → belongs to a preceding paper. Do not cite.
- Text at or after `target_end` → belongs to a following paper. Do not cite.
- If uncertain, append `[?boundary]` and mark
  `[UNVERIFIED — exclude from downstream analysis]`.

**Erratum / correction handling:** If S0-7 reports an erratum, correction,
or note added in proof that corrects specific content (e.g., "errors in
Scheme 2"), treat the corrected version as the authoritative source for
that content. Do not generate questions based on the uncorrected version
of the affected passage. Where the erratum does not specify what was
corrected, flag the affected content with [erratum — corrected version
unclear] and avoid strong interpretive claims about that passage.

---

## Location markers

The `loc` field requires a page-and-line reference. Apply the following rules
in order:

1. **Markers present in text**: If the paper text contains explicit `[PAGE N]`
   headers and `L1`, `L2`, … line labels, use them exactly: `P2:L14`,
   `P2:L14-L19`, `P1:L30-P2:L3`.

2. **Markers absent**: Assign your own sequential line numbers by counting
   from the first printed line of body text on each page (excluding headers,
   footers, page numbers). Mark with trailing asterisk: `P2:L14*`.

3. **Column-format**: Prefix the column: `P2:Lcol:14*` or `P2:Rcol:14*`.

4. **Not recoverable**: Write `loc: not recoverable` and ensure the `quote`
   field contains a full clause or longer.

**Under no circumstances omit the `quote` field to compensate for an
uncertain `loc` value. The quote is the primary anchor.**

---

## Anchoring discipline

Every item must be anchored to a direct quotation from the paper.

| Tier | Label | Meaning |
|------|-------|---------|
| **T1** | *(no label)* | The paper explicitly states this |
| **T2** | `[paper-grounded inference]` | Follows directly from quoted text; one step |
| **T3** | `[external inference]` | Draws on knowledge outside the paper |

**Rules:**
- T3 items must be labeled `[external inference]` every time.
- When the paper does not state a reason for a choice, write
  "not stated in paper" and stop.
- Mechanistic explanations not in the paper text are T3.

---

## Severity scale (used in Turns 1–3)

Each question generated in Turns 1–3 carries a severity rating reflecting
how serious the identified gap is **from the perspective of the generating
agent's discipline**:

| Severity | Meaning |
|----------|---------|
| **low** | Within normal genre conventions for the paper's format and era |
| **medium** | Noteworthy gap; standard practice in the agent's field would require this |
| **high** | Significant methodological gap; undermines confidence in specific claims |
| **critical** | Violates a basic premise of the agent's discipline; the claim cannot be evaluated without this information |

---

# Turn 1: Agent V1 (Paper's own field)

## Field determination

Determine V1's field from Stage 0:
- BIB-3 (journal) and BIB-1 (title) → broad field
- S0-4 (methodology) → subfield specialization

State the field and one-sentence rationale.

## Instructions

You are a specialist in **[determined field]**. Read the paper and identify
**10–15 questions** about information that is absent, incomplete, or
asymmetrically presented. For each question:

1. Quote the relevant passage from the paper (`quote` — required)
2. Provide a location reference (`loc`)
3. State the question concisely
4. Assign a `severity` rating from the perspective of your field
5. Label the inference tier (T1/T2/T3)

Focus on:
- Data that should be reported but is not (mass balance, controls, error bars,
  benchmark statistics, convergence criteria, parameter sensitivity)
- Claims whose evidence is incomplete within the paper
- Scope, applicability, or domain-of-validity limitations that are not acknowledged
- Information asymmetries in data presentation
  - *Synthetic / catalytic chemistry:* GC vs isolated yields, crude vs purified
    mass balance, selectivity reported on one axis only
  - *Computational / theoretical chemistry:* benchmark errors reported as MAE
    only without RMSD or maximum deviation; convergence criteria reported for
    energy but not for forces; basis-set or functional dependence reported
    for one observable but not others
  - *Physical chemistry / spectroscopy:* signal-to-noise reported only for the
    headline transition; band assignments asserted without calibration; spectral
    fitting parameters reported without uncertainty
- Mechanistic, theoretical, or methodological claims without sufficient evidence
- Substrate / system / parameter selections whose rationale is unstated

**Do not supply reasons the paper does not give.** If the paper does not
explain a choice, state "not stated in paper."

<!-- v18 C1: domain-agnostic perspective examples -->
**Domain coverage note:** The example list above is illustrative across
chemistry subfields. Match the examples to the paper's actual methodology:
do not force organometallic-style questions onto a quantum-theory paper,
nor force computational-style questions onto a synthesis paper.

<!-- v17 C1: OI-009 — scope failure example verification -->
**Scope failure example verification (mandatory):**
When the paper presents a scope table (substrate scope, Scheme, or
equivalent), check for substrates with 0% yield, 0% ee, trace yield,
or any result that the authors explicitly present as a failure or
limitation. For each such case:
1. Identify the reason the authors attribute for the failure (electronic,
   steric, conformational, thermodynamic, etc.)
2. Check whether experimental or computational evidence supporting (or
   contradicting) that attribution is presented in the paper
3. If the attribution is given without supporting evidence, record it as
   a question candidate (severity: medium or higher)

This check also applies to substrates described as "unreactive" or
"incompatible" in the text but not shown in a scope table.

<!-- v17 C4: OI-013 — Dropped Quantitative Benchmark -->
<!-- v18 C1: numerical-axis examples generalized across subfields -->
**Dropped Quantitative Benchmark check (mandatory for C-item detection):**
Scan the introduction and related-work sections for prior studies cited
with specific numerical values. The relevant axes depend on the paper's
subfield:
- *Synthetic / catalytic chemistry:* rate constants, activation parameters
  (ΔH‡, ΔS‡, ΔG‡), selectivity (ee, dr, regio-ratios), yields, TON / TOF
- *Computational / theoretical chemistry:* benchmark statistics (MAE, RMSD,
  R², maximum deviation), reference energies, basis-set extrapolated values,
  spin contamination ⟨S²⟩, computational cost (CPU hours, scaling exponent)
- *Physical chemistry / spectroscopy:* transition frequencies, line widths,
  oscillator strengths, decay lifetimes, equilibrium / rate constants
- *Theoretical foundations:* asymptotic limits, convergence rates, formal
  bounds, eigenvalue spectra (when prior work supplied numerical eigenvalues)

For each numerically-anchored citation, check whether the results/discussion
section makes a direct comparison on the same numerical axis. If a numerically-
cited prior study is never compared against the paper's own data on the
same metric, record it as a question candidate — this pattern will be
classified as a C item ("Dropped Quantitative Benchmark") in Turn 4.

<!-- v17 C5: OI-012 — ESI delegation vs experimental absence -->
**ESI delegation vs. experimental absence (mandatory distinction):**
When the paper references Supporting Information / ESI / SI for
experimental details (e.g., "see ESI for details," "full data in
Supporting Information"), treat the experiment as **performed** and
record any gap as partial disclosure (data exists but is not presented
in the main text), not as experimental absence. Specifically:
- If the main text states a qualitative conclusion and defers
  quantitative data to ESI, the experiment is performed — record the
  gap as "quantitative data deferred to ESI," not as "experiment not
  conducted."
- Pay attention to partial-negation qualifiers in the main text
  ("not mainly," "primarily," "largely") when ESI is referenced —
  these may indicate that ESI data modifies the main-text conclusion.
- Do not confuse ESI delegation with genuine experimental absence
  (where no experiment was conducted at all).

<!-- v17 C6: OI-011 — sequential protocol confounding check -->
**Sequential protocol confounding check:**
If the paper uses a sequential protocol — experiments conducted within
a single run where conditions (temperature, flow rate, solvent, reagent
concentration) are changed stepwise — check whether the preceding phase
could affect the subsequent phase (catalyst state change, intermediate
accumulation, surface modification, memory effects). If the paper
interprets data from each phase as if it were an independent experiment
without addressing carryover effects, record this as a question
candidate (severity: medium or higher). This check is particularly
relevant for flow reactor studies and multi-step one-pot procedures.

<!-- v18.2 C12: multi-measurement reporting symmetry check -->
**Multi-measurement reporting symmetry check (v18.2 added, mandatory
when the paper presents multiple measurements / modes / species / conditions
of the same kind):**

When the paper reports multiple measurements of the same quantity type
across different objects (e.g., multiple vibrational modes, multiple
isotopologues, multiple metal centers, multiple sub-systems, multiple
ligands), check whether the reporting is **symmetric across all members**:

1. **Mode/species reporting symmetry**: If the paper assigns one mode
   (e.g., ν(CO) coordination shift) as evidence for a model, are the
   other observable modes (e.g., ν(MCO), δ(MCO), ν(M-X)) also reported
   with the same fidelity? If only the supporting modes are foregrounded
   while contradicting or non-supporting modes are omitted from the table /
   discussion, record this as a question candidate (severity: medium or
   higher). Apply this even if the omission is presented as "not the
   focus of this work."

2. **Sub-system reporting symmetry**: If the paper presents predictions
   or measurements for multiple sub-systems (e.g., multiple metals, halides,
   noble gases, electronic states), check whether all sub-systems are
   reported with the same level of detail (binding energies, frequencies,
   spin states, characterization). If certain sub-systems are reported
   only by exception (e.g., "the heavier halides behave similarly") while
   detailed numerical data is provided only for selected sub-systems,
   record the asymmetry as a question candidate.

3. **Failure-case reporting symmetry**: If the paper reports successful
   predictions / characterizations / fits for some cases, are the
   unsuccessful cases (failed root-tracking, non-converged optimizations,
   excluded data points, anomalously deviating results) reported with
   equal explicitness? Selective foregrounding of successful cases without
   parallel reporting of failures is a question candidate.

This check is particularly relevant for systematic surveys (multi-system
grids), spectroscopy with multiple observable modes, and computational
studies with multiple methods or basis sets. The pattern was identified
in the NobleGas References cross-paper analysis (analysis_summary_v181_sonnet.md
§P1) where selective foregrounding of supporting modes/species was
systematic across matrix isolation and Ar-MX computational papers.

## Turn 1 output format

```
[Turn 1: Agent V1]
field: [field name]
field_rationale: [one sentence]

V1-Q1 | loc | quote | question | severity | inference_tier
V1-Q2 | loc | quote | question | severity | inference_tier
...
```

---

> **Public-cut redaction notice**: verbatim quotations from the analysed papers in this file have been replaced by `[REDACTED: …]` markers (rules in the repository README). The unredacted file is in the reviewer version of the deposit.
