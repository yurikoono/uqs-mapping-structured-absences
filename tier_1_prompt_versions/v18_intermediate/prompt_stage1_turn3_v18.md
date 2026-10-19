# Stage 1 — Turn 3: Agent V3 (Methodology / statistics)
<!-- prompt_version: stage1-v18-20260425 / turn3 -->

<!-- v17 C8: PDF direct reading -->
## PDF reading note

Read the paper PDF directly using the Read tool (multimodal reading).
If the PDF is 20 pages or fewer, read the entire file in one call.
If the PDF exceeds 20 pages, split into page ranges (e.g., "1-20", "21-40")
with a maximum of 20 pages per call. Do not use pdftotext or other
text-extraction tools. Figures, schemes, structural formulas, and energy
diagrams are available for analysis through direct PDF reading.

---

# Turn 3: Agent V3 (Methodology / statistics — self-determined)

## Field determination

Review V1's and V2's outputs. Identify the most important **methodological
or analytical perspective** not yet covered. This should focus on data
quality, analytical methods, statistical validity, or experimental design
rather than domain-specific content.

**Determination guidance based on S0-2 and S0-4:**

<!-- v18 C1: expanded V3 guidance for computational/theoretical/historical papers -->
| Signal in S0-2 / S0-4 | Recommended V3 field |
|---|---|
| Yield tables, GC/HPLC data as primary evidence | Analytical chemistry / chromatography |
| Spectroscopic characterization (NMR, IR, MS, UV-Vis) as primary evidence | Spectroscopy / structural analysis |
| Statistical tests, regression, p-values present | Biostatistics / experimental design |
| DFT, transition state calculations, MD simulations | **Computational chemistry / theoretical methods** |
| Multireference / wavefunction methods (CASSCF, CASPT2, CCSD(T), MRCI) | **Multireference electronic structure / numerical convergence** |
| New computational descriptor / orbital-based index (NRO, NPO, IBO, AFIR-γ, reactivity indices) | **Construct validity / measurement theory** (interrogates whether the descriptor is operationally well-defined and externally validated) |
| Selection rules / symmetry arguments / formal proofs | **Philosophy of science / falsifiability analysis** (interrogates operational conditions of falsification) |
| Kinetic data, rate constants, Arrhenius analysis | Chemical kinetics / physical chemistry |
| Benchmark training-set optimization | **Statistical learning / overfitting diagnostics** |
| None clearly dominant | General scientific methodology |

**Computational chemistry conditional:** If S0-2 or S0-4 contains
terms such as "DFT," "density functional," "transition state calculation,"
"computational," "molecular dynamics," or "ab initio," V3 should adopt a
computational chemistry perspective. This is the primary trigger. If such
terms are absent (e.g., a 1972 communication with no computational content),
do not force a computational perspective — select from the other options above.

**Pre-emption check (mandatory first step):** Before selecting a field,
read V2's output header. If V2 declared `[preempts_turn3_default: yes]`,
the field this table recommends is unavailable to V3. In that case:
1. State which field V2 took and why it is pre-empted.
2. Select the next most important methodological perspective not covered
   by V1 or V2. Guidance by paper type:
   - DFT paper already taken by V2 → prioritize:
     * NMR spectroscopy / quantitative analytical chemistry (if ³¹P/¹H
       NMR monitoring or NMR-derived equilibrium constants are primary
       evidence)
     * Chemical kinetics / physical chemistry (if rate constants or
       activation parameters are primary evidence)
     * Analytical chemistry / chromatography (if HPLC/GC-MS product
       quantification is primary evidence)
   - State the alternative choice and the pre-emption reason explicitly
     in the `field_rationale` field.

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
