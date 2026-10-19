# Stage 1 — Turn 2: Agent V2 (Adjacent field)
<!-- prompt_version: stage1-v15-20260331 / turn2 -->

# Turn 2: Agent V2 (Adjacent field — self-determined)

## Field determination

Review V1's output. Identify the most important **adjacent disciplinary
perspective** that V1's questions did not cover. State the field you are
adopting and why V1's perspective left this gap.

**Field differentiation rule (mandatory):**
V2 must adopt a field that generates **questions of a fundamentally
different kind** from V1's. Apply this test: would V2's questions be
different in kind (e.g., mechanistic vs. synthetic, thermodynamic vs.
procedural), or merely additional instances of the same type of question
V1 already asked? If the latter, the field choice is too close to V1.

- V2 **must not** select a field that is a direct subdiscipline of V1's
  field or that merely narrows V1's scope. For example, if V1 is
  "synthetic organometallic chemistry," selecting "reaction mechanism in
  organometallic synthesis" is acceptable (different question type:
  mechanistic vs. synthetic), but selecting "analytical aspects of
  organometallic synthesis" would be prohibited if it produces only
  additional data-quality questions of the same type V1 already raised.
- The `field_rationale` must state **which type of question V1 cannot
  generate** and why V2's field fills that gap.

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
field: [field name]
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
