# Stage 1 — Turn 2: Agent V2 (Adjacent field)
<!-- prompt_version: stage1-v184-20260502 / turn2 -->

<!-- v17 C8: PDF direct reading -->
## PDF reading note

Read the paper PDF directly using the Read tool (multimodal reading).
If the PDF is 20 pages or fewer, read the entire file in one call.
If the PDF exceeds 20 pages, split into page ranges (e.g., "1-20", "21-40")
with a maximum of 20 pages per call. Do not use pdftotext or other
text-extraction tools. Figures, schemes, structural formulas, and energy
diagrams are available for analysis through direct PDF reading.

---

# Turn 2: Agent V2 (Adjacent field — self-determined)

## Field determination

Review V1's output. Identify the most important **adjacent disciplinary
perspective** that V1's questions did not cover. State the field you are
adopting and why V1's perspective left this gap.

**Field differentiation rule (mandatory):**
V2 must adopt a field that generates **questions of a fundamentally
different kind** from V1's. Apply this test: would V2's questions be
different in kind (e.g., mechanistic vs. synthetic, thermodynamic vs.
procedural, theoretical vs. experimental, statistical vs. mechanistic),
or merely additional instances of the same type of question V1 already
asked? If the latter, the field choice is too close to V1.

<!-- v18 C1: cross-subfield V2 differentiation examples -->
- V2 **must not** select a field that is a direct subdiscipline of V1's
  field or that merely narrows V1's scope. Examples by paper type:
  - **Synthesis paper** (V1 = "synthetic organometallic chemistry"):
    selecting "reaction mechanism in organometallic synthesis" is
    acceptable (different question type: mechanistic vs. synthetic);
    selecting "analytical aspects of organometallic synthesis" is
    prohibited if it only adds data-quality questions of the same type
    V1 raised.
  - **Computational methodology paper** (V1 = "DFT methodology /
    computational reaction-path analysis"): selecting "experimental
    physical organic chemistry" or "kinetic measurement / spectroscopy"
    is acceptable (computational predictions vs. experimental
    verification); selecting "alternative DFT functional benchmarking"
    is prohibited as it merely adds parallel computational questions.
  - **Theoretical / formal paper** (V1 = "quantum-chemical theory /
    formal derivation"): selecting "experimental verification of
    theoretical predictions" or "numerical analysis / convergence
    properties" is acceptable; selecting "alternative theoretical
    formulation in the same family" is prohibited.
- The `field_rationale` must state **which type of question V1 cannot
  generate** and why V2's field fills that gap.

**V2 pre-emption declaration:** At the end of the `field:` line in your
output, append `[preempts_turn3_default: yes]` if the field you have
selected is the same field that Turn 3's guidance table would recommend
for V3 (e.g., you select computational chemistry when DFT is present in
the paper). This flag tells V3 to choose an alternative field.

**Absence-based field triggers:**
The paper's missing content — not only its present content — should inform
V2's field choice. In particular:

- If the paper **proposes a catalytic cycle, reaction mechanism, or
  mechanistic hypothesis** but reports **no kinetic data, no intermediate
  characterization, and no mechanistic probes** (radical clocks, crossover
  experiments, isotope labeling, linear free-energy relationships), V2
  should strongly consider **mechanistic / physical organic chemistry**.
  This perspective would interrogate: rate-determining step identification,
  oxidation-state assignments, radical vs. ionic pathway discrimination,
  and the evidentiary basis for elementary steps.

<!-- v18 C1: theoretical / methodology paper triggers -->
- If the paper **proposes a new theoretical framework, computational
  method, or descriptor** without **independent experimental verification,
  systematic benchmarking, or sensitivity analysis**, V2 should consider
  **experimental verification / numerical analysis / statistical methodology**.
  This perspective would interrogate: whether the theoretical predictions
  have been tested against independent measurement; whether benchmark
  performance is statistically significant or reflects overfitting; whether
  the convergence behavior of the algorithm is characterized; whether the
  range of validity (chemical systems, parameter regimes) is empirically
  established rather than assumed.

- If the paper **derives selection rules, conservation principles, or
  symmetry-based predictions** from formal arguments without specifying
  the operational conditions for falsification, V2 should consider
  **experimental physical chemistry / spectroscopy** to interrogate which
  observations would constitute disconfirmation, whether the predictions
  have been tested in cases not pre-selected by the authors, and whether
  edge cases (boundaries of applicability) have been probed empirically.

- If the paper reports **selectivity claims** (regio-, stereo-, or
  chemo-selectivity) or **yield/condition variations** without
  thermodynamic or kinetic analysis, V2 must generate questions about
  whether observed selectivity or reactivity patterns reflect kinetic or
  thermodynamic control. This trigger applies **independently** of the
  mechanistic trigger above — even if V2 adopts a mechanistic perspective
  under the first trigger, these questions must still be generated because
  they are answerable without resolving the full catalytic mechanism.

  **Primary selectivity** (the paper's central claim) must be addressed
  first. Examples:
  - Cross-coupling vs. homo-coupling: is the preference for cross-coupled
    product governed by relative rates of competing reductive eliminations
    (kinetic control) or by thermodynamic product stability?
  - Regioselectivity: is the observed regiochemistry determined by the
    relative rates of oxidative addition at different positions, or by
    equilibration of intermediates?

  **Secondary selectivity** (subsidiary observations) should also be
  addressed if data permit. Examples:
  - Stereochemical outcomes (cis/trans ratios): kinetic vs. thermodynamic
    product distribution; does extended reaction time alter the ratio?
  - Solvent or temperature effects on yield: rate-driven or
    equilibrium-driven?

  These questions are **independent of** whether the catalytic cycle
  mechanism is correct, and must not be subsumed under mechanistic
  hypothesis questions.

  **Independence from field choice:** The selectivity trigger applies
  regardless of which field V2 adopts. Even when V2 selects a computational
  methodology field, V2 must still check: "Does the paper report selectivity
  data (yield ratios, er, dr, regio- or chemoselectivity)?" If yes, generate
  at least one question asking whether the observed selectivity is kinetically
  or thermodynamically controlled — as a separate, explicitly labeled
  question independent of the DFT methodology questions.

- If the paper reports **DFT calculations, transition state analysis, or
  computational mechanistic evidence**, V2 may adopt a **computational
  chemistry** perspective. When doing so, apply the following checklist.

  **DFT reporting checklist (mandatory when V2 adopts computational
  chemistry):** For each item below that is absent from the paper's DFT
  methodology description, generate one question:
  1. Energy type: Is ΔE (electronic energy), ΔH (enthalpy), or ΔG (Gibbs
     free energy) reported? Were thermochemical corrections (ZPE, thermal,
     entropy) applied?
  2. Dispersion correction: Was D3BJ or equivalent applied? (Relevant for
     transition-metal complexes, π-systems, bulky substituents, or any
     non-covalent contact controlling the reported energetics.)
  3. Solvation model: Was implicit solvation (PCM / SMD / COSMO) applied?
     Relevant if any intermediate is ionic/charged or if the experimental
     solvent is polar (DMF, MeCN, MeOH, etc.).
  4. Conformational sampling: How were the lowest-energy TS structures
     identified? (Grid search, CREST, systematic dihedral scan, assertion?)
  5. Reference state: In energy profiles, is the zero-energy reference
     clearly defined, and is it the genuine resting state or an artificial
     intermediate?
  6. Temperature consistency: Are thermochemical corrections computed at
     the actual reaction temperature, or at default 298.15 K?
  <!-- v18 C1: extended checklist items for non-DFT computational papers -->
  7. Spin contamination ⟨S²⟩ (open-shell systems): Is ⟨S²⟩ reported, and
     is its deviation from the ideal value characterized?
  8. Active-space justification (multireference methods): Is the choice
     of active space (CASSCF, CASPT2, MRCI, NEVPT2) justified by an
     orbital-occupation analysis or by sensitivity to active-space size?
  9. Basis-set convergence: Is the basis-set dependence of the reported
     observables characterized, or is a single basis set used without
     extrapolation or convergence test?
  10. Numerical convergence (analytical gradients, second derivatives):
      Are convergence thresholds for forces / Hessian elements reported,
      or only for energy?
  Generate a question for each absent item that is relevant to the paper's
  mechanistic, selectivity, or methodological conclusions. Do not generate
  questions for items that are irrelevant to the paper's claims.

<!-- v17 C2: OI-010 — catalytic cycle mechanistic evaluation independent of DFT checklist -->
  **Catalytic cycle mechanistic evaluation (mandatory when DFT is present):**
  When applying the DFT reporting checklist above, maintain a **separate**
  evaluation of the paper's proposed catalytic cycle or reaction mechanism
  with respect to experimental verification. Specifically:
  - Check whether each elementary step in the proposed catalytic cycle
    has experimental support (kinetic data, isotope effects, intermediate
    trapping, crossover experiments, stoichiometric step validation)
  - Record mechanistic steps that rely solely on DFT evidence without
    experimental corroboration as B-item or U-item candidates
  - The DFT checklist evaluates computational methodology quality; the
    catalytic cycle evaluation assesses whether the proposed mechanism
    is experimentally grounded. These are independent assessments — do
    not let DFT methodology questions subsume or replace mechanistic
    evidence questions.

- If the paper describes **material properties** without structural
  characterization, V2 should consider **structural chemistry /
  crystallography / solid-state characterization**.

These triggers are illustrative, not exhaustive. The principle is: **a
major claim unsupported by data from an adjacent field is the strongest
signal for V2's field choice.**

## Instructions

You are a specialist in **[self-determined field]**. You have read V1's
questions. Your task is twofold:

**Part A — New questions (8–12):**
Generate questions that V1's perspective did not cover. Each with quote,
loc, question, severity, inference tier.

**Part B — Overlap re-evaluation (important):**
Review V1's questions. For any question that is **also important from your
field's perspective**, record it as an overlap entry with your own severity
rating and a one-sentence note explaining why your field views it
differently. **Do not skip overlaps** — they are analytically valuable.

## Turn 2 output format

```
[Turn 2: Agent V2]
field: [field name] [preempts_turn3_default: yes/no]
field_rationale: [why this perspective is needed, referencing gaps in V1's coverage]

--- New questions ---
V2-Q1 | loc | quote | question | severity | inference_tier
V2-Q2 | loc | quote | question | severity | inference_tier
...

--- Overlaps with V1 ---
V2-OV1 | overlaps_with: V1-QN | severity_V2: [rating] | note: [one sentence: why this field views it differently]
V2-OV2 | overlaps_with: V1-QN | severity_V2: [rating] | note: ...
...
```
