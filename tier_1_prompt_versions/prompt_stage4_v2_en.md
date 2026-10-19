# Stage 4: Identification of EP-Filling Papers and Generation of the Selection Map — English-only track
<!-- prompt_version: stage4-v2-en-20260419 -->
**Language: English throughout (English-only evaluation variant of stage4-v2-20260416). RI/EP/VQ codes, technical terms, and paper citations remain in English as in the original.**

Report the prompt version at the start of your output:
```
prompt_version: stage4-v2-en-20260419
```

---

## Input

Paste the following before this prompt:
1. **Stage 0 output** (BIB-1 through BIB-8b, S0-1 through S0-7)
2. **Stage 1 Turn 4 output** (A, B, C, U, META, TEMPERATURE_SUMMARY, GAP)
3. **Stage 2 output** (D-1 through E, confirmed_english)
4. **Stage 3 output** (§1 through §6)

Primary reference sections:
- **§2 SRG / CLA → RI / ER / EP Crosswalk** (EP inventory and
  case-specific implementations)
- **§5 Shortest-reinforcement route** (EP investment order and VQ
  objective functions)
- **§3 Current VQ assessment** (pass/fail for each VQ level)
- **§4 Era-Norm Annotation** (what was tolerated then and what is
  deficient now)

---

## Purpose

For each EP listed in Stage 3 §5 (Shortest-reinforcement route), identify
the papers that historically filled (or partially filled) that EP, and
structure the result as a recommended selection list. This allows
empirical verification of how the "unasked questions" extracted by UQS
have been addressed by subsequent scientific development.

---

## Output discipline

Follow the §A through §E structure below and output only the structured
selection map. Do not add explanatory prose, follow-up questions,
next-step suggestions, or text outside the specified fields.

**Basic stance:** identification of filling papers should make maximum
use of the model's domain knowledge (awareness of the literature,
researchers, and research groups). When knowledge is uncertain, state so
explicitly (via the confidence level) and avoid hallucination.

---

## Reference system

Use the systems introduced in Stage 3 as-is:
- **EP code system:** EP-01a through EP-10a (assigned in Stage 3 §2)
- **RI code system:** RI-01 through RI-09, PRI-10 (Root-Issue Codebook
  v0.2)
- **VQ decision matrix:** VQ-1 through VQ-4 (including the inheritance
  principle)

---

## Selection-map generation procedure

### Step 1: §A Three-tier classification of EP filling difficulty

**Input:** Stage 3 §2 (case-specific implementation of each EP) + §5 (EP
investment order)

Classify every EP listed in Stage 3 §5 into one of the following three
tiers based on how readily a filling paper can be detected.

**Classification criteria:**

| Tier | Label | Criterion |
|:-----|:------|:----------|
| **Tier 1** | Clearly trackable in the literature | The experiment that the EP demands is likely to exist as the main subject of an independent paper. The experimental method, substrate system, and measurement are concrete enough to be hit directly by a literature search. |
| **Tier 2** | Indirectly trackable | The information the EP demands is included within review articles, textbooks, or methodology papers but is not the main subject of an independent paper. Alternatively, demonstration exists for similar systems but demonstration in the target system itself is limited. |
| **Tier 3** | Filling may not be found | The EP arises from the paper-specific reporting-format issue (RI-01) or from replication convention (RI-08) and is not a property likely to be filled by an independent paper. Or, the field has systematically avoided this question. |

**Classification procedure:**
1. For each EP, consult the case-specific implementation (§2) and assess
   the plausibility of the required experiment existing as an independent
   paper.
2. Take the RI codes assigned to the EP into account:
   - RI-03, RI-06, RI-07 → Tier 1 candidates (experimental verification
     of mechanism, boundary, or analogy is often published as
     independent research)
   - RI-05, RI-09 → Tier 2 candidates (quantitative substantiation and
     benchmark comparison are more often included in reviews)
   - RI-01, RI-08 → Tier 3 candidates (reporting format and replication
     are usually resolved automatically in a Full Paper, or remain
     unresolved as field convention)
3. The above are default tendencies; make individual judgments based on
   the concreteness of the case-specific implementation (e.g., an RI-01
   case may be Tier 1 if the Full Paper expansion exists as an
   independent paper).

**Output format:**
```
**Tier 1 (clearly trackable in the literature):** EP-XXa, EP-YYa, ...
  — [one-sentence justification for each EP assigned to Tier 1]

**Tier 2 (indirectly trackable):** EP-XXa, EP-YYa, ...
  — [one-sentence justification for each EP assigned to Tier 2]

**Tier 3 (filling may not be found):** EP-XXa, EP-YYa, ...
  — [one-sentence justification for each EP assigned to Tier 3]
```

---

### Step 2: §B Identification of filling-paper candidates for each EP

**Input:** §A three-tier classification + Stage 3 §2 (case-specific
implementation) + §5 + model's domain knowledge

**Search methodology:**
Filling-paper identification is performed not by citation count or
surface similarity to the original paper, but by **back-deriving search
terms from the EP's case-specific implementation**.

Procedure:
1. From the case-specific implementation (§2) of each EP, extract the
   concrete content of the experiment to be performed (substrate,
   analytical method, measurement target).
2. Convert that experimental content into search terms. Example: EP-03a
   "spectroscopic identification of intermediates in the NiCl₂(dpe)
   system" → "nickel diphosphine intermediate characterization
   spectroscopic."
3. Use the model's domain knowledge to identify papers matching the
   search terms.
4. Note that highly cited papers are more likely to be *application*
   papers that used the original method, not filling candidates. A
   filling paper is one that performed the experiment corresponding to
   the EP; it may not cite the original paper at all.

For each EP in Tier 1 and Tier 2, identify filling-paper candidates
using the following template. For Tier 3, also record partial fillings
or related developments if any exist.

**Identification principles:**
- **Filling Onset:** the paper that first provided the experiment or
  data corresponding to the EP. Partial filling is allowed.
- **Filling Establishment:** the paper at which filling became decisive.
  It provides substantially the experimental evidence the EP demands.
- When both are the same paper, combine into a single entry.
- **Self-filling by the original author group:** carefully watch for
  patterns in which the original paper's author group fills the EP in a
  later paper (Full Paper, sequel). Include the automatic-resolution
  pattern of communication→Full Paper transitions.

**Per-EP candidate template:**
```
**EP-XXa [common label] (Tier N)**

* **RI to be filled**: RI-XX [Label]
* **Filling Onset**: [Author et al., journal year] — [one-sentence
  description of the filling]
* **Filling Establishment**: [Author et al., journal year] —
  [one-sentence description of the filling]
  (If identical to Filling Onset, write "same as above.")
* **Nature of filling**: [select one of the following]
  - Complete: substantially satisfies the EP's requirements
  - Partial: satisfies part of the EP's requirements; some unfilled
    elements remain
  - Indirect: filled in an analogous system rather than the target
    system itself
  - Attempted: moved in the direction of the EP, but the filling paper's
    own data reliability (VQ level) is insufficient, so it does not
    function as a filling
  - Paradigm-shift: the original paper's framework itself is replaced by
    a new paradigm, changing the premise of the EP (the EP is not
    resolved but the framing of the question changes)
* **Confidence**: [High / Medium / Low]
  - High: confident of the paper's existence and content
  - Medium: confident of the paper's existence but inference is involved
    in mapping to EP filling
  - Low: knowledge is uncertain and actual literature confirmation is
    needed
* **Notes**: [additional information, e.g., cross-references when one
  paper fills multiple EPs, time to filling, context of the filling
  (why the research was conducted), etc.]
```

**Identification guidelines:**
1. Target the literature from the original paper's year (BIB-4) onward.
2. When multiple filling candidates exist for the same EP, restrict to
   the one or two most decisive.
3. When one paper fills multiple EPs (bundle filling), cross-reference
   among the per-EP entries.
4. When no filling paper is found, write "**unidentified**" and give
   1–2 sentences stating the reason.
5. **Review articles do not fill EPs.** Reviews systematize existing
   data but do not supply new experimental evidence. Reviews are not
   filling papers but secondary information sources used to identify
   filling papers. Exception: if the review contains meta-analysis or
   an original quantitative re-evaluation that directly addresses the
   EP's requirements, record it with a note.
6. **Filling papers do not declare themselves "filling."** A paper
   that fills an EP was not written for the purpose of filling the
   original paper's absences. What is required is an operation (the
   detection of evidential complementarity) that judges whether the
   experimental content of a paper written in a different context and
   for a different purpose structurally satisfies the EP's
   requirements. Judge filling by correspondence to the case-specific
   implementation of the EP, not by superficial similarity of subject
   matter.

---

### Step 3: §C Recommended selection list

**Input:** §B filling-paper candidates

From the filling-paper candidates identified in §B, construct a
recommended selection list of 5–7 papers optimal for EP-filling
verification.

**Selection criteria (in priority order):**
1. **EP coverage of filling**: prefer papers that fill more EPs.
2. **Decisiveness of filling**: Complete > Partial > Indirect.
3. **Step-wise coverage of the VQ hierarchy**: include at least one
   paper each from the VQ-2, VQ-3, and VQ-4 layers.
4. **Temporal diversity**: to verify the temporal unfolding of filling,
   select papers from different eras as far as possible.
5. **Confidence**: High > Medium. Low papers are not included in the
   selection list as a rule (they may appear in §B's candidate column).

**Output format:**
```
| Order | Paper | EPs filled | VQ level | Year | Confidence |
|-------|-------|------------|----------|------|------------|
| 1 | [Author et al., Journal Year] | EP-XXa, EP-YYa | VQ-N | YYYY | High/Med |
| ... | ... | ... | ... | ... | ... |
```

After the table, describe the selection rationale in 1–2 paragraphs. If
bundle fillings (one paper covering multiple EPs) exist, note the
efficiency.

---

### Step 4: §D Correspondence between VQ hierarchy and filling time order

**Input:** §C recommended selection list + Stage 3 §3 (VQ assessment)

Arrange the papers in the recommended selection list by publication year
and analyze the correspondence with the VQ hierarchy.

**Analysis framework:**

1. **Temporal mapping**: associate each filling paper's publication year
   with the VQ level it fills, constructing a time axis of the form
   "the VQ-N requirement was filled in year Y."
2. **Hierarchy–time hypothesis test**: test the following hypothesis:
   > "The higher the VQ level, the longer the time required to fill it.
   > This is because the VQ hierarchy reflects the difficulty structure
   > of scientific development."
   - If supporting evidence exists, record it.
   - If counterexamples exist, record those as well.
3. **Classification of filling patterns**: record any of the following
   that apply:
   - **Self-filling**: resolution by a later paper from the original
     author group
   - **Technology-driven filling**: resolution via emergence of new
     analytical techniques or computational methods
   - **Cross-field filling**: resolution through approaches from a
     different research field
   - **Paradigm-shift filling**: a change in the framework that
     underpins the EP redefines the question itself (succession rather
     than filling)
   - **Long-delay filling**: filling more than 20 years after the
     original paper
   - **Unfilled**: still unfilled (handled in §E)
4. **Comparison with author retrospective (when applicable)**: compare
   the list of "characteristics" or "achievements" the original author
   later mentioned in a retrospective (review, retrospective article,
   Nobel lecture, etc.) against the Stage 3 EP list. The gap between
   EPs the author recognized and those not recognized can be recorded
   as direct evidence of "structural absences invisible to field
   insiders."

**Output format:**
```
**Filling time axis:**
- VQ-N requirement: EP-XXa → [year] [author] [filling pattern]
- VQ-N requirement: EP-YYa → [year] [author] [filling pattern]
...

**Evaluation of hierarchy–time correspondence:**
[2–3 sentences on whether the hypothesis is supported or not]

**Notable patterns:**
[long-delay filling, bundle filling, self-filling, and other
 noteworthy items]
```

---

### Step 5: §E Heuristic significance of unfilled EPs

**Input:** §B (unidentified EPs) + §D (unfilled patterns)

For EPs whose filling paper was not identified in §B or which were
judged unfilled in §D, describe their scientific-historical significance.

**Analytical lenses:**
1. **Reason for non-filling:** estimate why the EP was not filled:
   - Technical difficulty (experimentally impossible or extremely hard)
   - Field convention (experiments of this kind are not customarily
     performed)
   - Reporting-format issue (partially resolved by communication→Full
     Paper transition but not completely)
   - Lack of interest (the scientific community did not care about the
     question)
   - **Misaligned incentive structure** (filling is technically
     feasible, but incentives for publishing that experiment as an
     independent paper do not exist. Examples: replication of
     established systems, replicate measurements, substrate-matched
     benchmark comparisons — these are hard to paperize under
     publication conventions that demand novelty.)
2. **Value as a UQS finding:** judge whether the item can be recorded
   as "a question the field has systematically avoided for N years." If
   so, describe its heuristic significance in 1–2 sentences.
3. **Future filling feasibility:** assess whether the EP can be filled
   by present-day technology and methodology.
4. **VQ-hierarchy inversion diagnosis:** if unfilled EPs cluster at
   low-VQ requirements (RI-01, RI-08, RI-09) and filled EPs cluster at
   high-VQ requirements (RI-03, RI-06, RI-07), record this as an
   inversion between "the EP-filling order dictated by scientific logic
   (low-VQ → high-VQ)" and "the actual filling order dictated by
   publication incentives (high-VQ → low-VQ)." This inversion pattern
   is evidence that the field's incentive structure maintains part of
   the UQS-visible structural absences.

**Output format:**
```
**List of unfilled EPs:**

EP-XXa [common label]:
* **Reason for non-filling**: [choose from categories above +
  1–2 sentences of explanation]
* **Heuristic significance**: [yes / no. If yes, 1–2 sentences.]
* **Future filling feasibility**: [high / medium / low + one-sentence
  rationale]
```

If no unfilled EPs exist, write: "All EPs have an identified filling
paper."

---

## Output format

```
prompt_version: stage4-v2-en-20260419
model_info: <model name and version>

# EP-Filling Selection Map

## [Paper authors] [year] ([BIB-3] [BIB-7])

### §A Three-tier classification of EP filling difficulty
[three-tier classification output]

### §B Filling-paper candidates for each EP
[per-EP templates]

### §C Recommended selection list
[5–7-paper selection table and selection rationale]

### §D Correspondence between VQ hierarchy and filling time order
[time axis, hierarchy–time correspondence, notable patterns]

### §E Heuristic significance of unfilled EPs
[list of unfilled EPs, or "All EPs have an identified filling paper"]
```
