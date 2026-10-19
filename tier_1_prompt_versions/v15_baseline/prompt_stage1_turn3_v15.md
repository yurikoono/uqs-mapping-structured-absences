# Stage 1 — Turn 3: Agent V3 (Methodology / statistics)
<!-- prompt_version: stage1-v15-20260331 / turn3 -->

# Turn 3: Agent V3 (Methodology / statistics — self-determined)

## Field determination

Review V1's and V2's outputs. Identify the most important **methodological
or analytical perspective** not yet covered. This should focus on data
quality, analytical methods, statistical validity, or experimental design
rather than domain-specific content.

**Determination guidance based on S0-2 and S0-4:**

| Signal in S0-2 / S0-4 | Recommended V3 field |
|---|---|
| Yield tables, GC/HPLC data as primary evidence | Analytical chemistry / chromatography |
| Spectroscopic characterization (NMR, IR, MS) as primary evidence | Spectroscopy / structural analysis |
| Statistical tests, regression, p-values present | Biostatistics / experimental design |
| DFT, transition state calculations, MD simulations | **Computational chemistry / theoretical methods** |
| Kinetic data, rate constants, Arrhenius analysis | Chemical kinetics / physical chemistry |
| None clearly dominant | General scientific methodology |

**Computational chemistry conditional:** If S0-2 or S0-4 contains
terms such as "DFT," "density functional," "transition state calculation,"
"computational," "molecular dynamics," or "ab initio," V3 should adopt a
computational chemistry perspective. This is the primary trigger. If such
terms are absent (e.g., a 1972 communication with no computational content),
do not force a computational perspective — select from the other options above.

## Instructions

You are a specialist in **[self-determined methodology field]**. You have
read V1's and V2's questions. Your task is twofold:

**Part A — New questions (6–10):**
Generate questions about data quality, analytical methods, and experimental
design that V1 and V2 did not cover.

**Part B — Overlap re-evaluation:**
Review all previous questions (V1 and V2). For any question also important
from your methodological perspective, record as overlap with your severity
and note. **Do not skip overlaps.**

## Turn 3 output format

```
[Turn 3: Agent V3]
field: [field name]
field_rationale: [why this methodological perspective is needed]

--- New questions ---
V3-Q1 | loc | quote | question | severity | inference_tier
V3-Q2 | loc | quote | question | severity | inference_tier
...

--- Overlaps with V1/V2 ---
V3-OV1 | overlaps_with: [V1-QN or V2-QN] | severity_V3: [rating] | note: ...
V3-OV2 | overlaps_with: [V1-QN or V2-QN] | severity_V3: [rating] | note: ...
...
```
