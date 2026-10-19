# Stage 1 — Turn 4: Synthesis
<!-- prompt_version: stage1-v183-20260427 / turn4 -->

<!-- v17 C8: PDF direct reading -->
## PDF reading note

Read the paper PDF directly using the Read tool (multimodal reading).
If the PDF is 20 pages or fewer, read the entire file in one call.
If the PDF exceeds 20 pages, split into page ranges (e.g., "1-20", "21-40")
with a maximum of 20 pages per call. Do not use pdftotext or other
text-extraction tools. Figures, schemes, structural formulas, and energy
diagrams are available for analysis through direct PDF reading.

---

# Turn 4: Synthesis

## Instructions

You now have the complete question sets from V1, V2, and V3, plus all overlap
re-evaluations. Perform the following synthesis.

### Step 0 (mandatory): Boundary recheck

Before any classification, re-examine every `quote` field from Turns 1–3.
For each quote, verify that the quoted text falls between `target_start`
and `target_end`. Pay particular attention to:
- Quotes that mention metals, ligands, or reactions not discussed in the
  target paper (may originate from an adjacent paper in the same PDF)
- Quotes near page boundaries

If a quote fails the boundary check:
- Append `[?boundary]` to the item
- Classify the item as **U** with note: "boundary violation suspected —
  exclude from downstream analysis"
- Do **not** include it in any same_root_group or TEMPERATURE_SUMMARY

### Step 1: Compute cross_field_temperature for overlapping questions

For each question that received overlap re-evaluations, compute:
- `convergence`: how many agents flagged this question (2/3 or 3/3)
- `temperature_gap`: difference between max and min severity across agents,
  using the following scale based on severity step distance:

**Severity ordering:** low (1) < medium (2) < high (3) < critical (4)

| Step distance | temperature_gap |
|---|---|
| 0 (same severity) | none |
| 1 (e.g., low↔medium, high↔critical) | low |
| 2 (e.g., low↔high, medium↔critical) | medium |
| 3 (e.g., low↔critical) | high |

Example: V1=medium, V2=critical, V3=high → max=critical(4), min=medium(2),
distance=2 → temperature_gap=medium.

**Counting overlaps toward convergence:**
Overlap entries (V2-OVn, V3-OVn) count as agent flags for convergence
purposes:
- V1 raises Q as a new question → convergence contribution: 1
- V2 records Q as V2-OVn (overlap re-evaluation) → contribution: 2
  (convergence = 2/3 between V1 and V2)
- V3 also records Q as V3-OVn → contribution: 3 (convergence = 3/3)
The temperature_gap is computed from all three severity values (V1, V2,
V3) regardless of whether they appear as new questions or overlap
re-evaluations. The severity_V2 value comes from the V2-OVn entry;
the severity_V3 value comes from the V3-OVn entry.

### Step 2: Identify same-root question groups

Before classifying individual questions, scan for questions from different
agents that address **different facets of the same underlying data absence
or methodological gap**. Group them and record the connection in META
linked_items as a `same_root_group`.

**Rules:**
- This is factual connection-listing, not interpretation. State only
  "these questions derive from the same absent data" or similar.
- Do not merge the questions — each retains its own item_id after
  classification. The group membership is metadata.
- Example: V1-Q1 (TON not reported), V1-Q8 (mass balance absent),
  V3-Q4 (no replication data) → same_root_group: "quantitative
  experimental validation absent"

### Step 3: Classify all questions

Classify each question (including overlapping ones — classify once with
all agents' perspectives noted) into one of four categories:

**A (Deferred Questions):**
The paper explicitly sends the issue to future work, or closes without
resolving a question it has raised. The incompleteness is prospective.

Apply the **A vs B boundary rule:**
- **A** = prospective (would disappear if a follow-up paper resolved it)
- **B** = descriptive of this experiment's boundary (regardless of follow-up)
- Both → classify as **B** with prospective character noted

Apply the **suppressed classification checklist** (all three required):
1. Textual indicator the authors were aware of the tension
2. Textual move *away* from the tension
3. Paper does not return to address it
If any absent → classify as deferred or mixed, not suppressed.

Deferral types: deferred / suppressed / mixed / forgotten

<!-- v18.2 C14: methodological-failure diagnostic question rule -->
**Methodological-failure diagnostic rule (v18.2 added, mandatory for
A items involving computational / spectroscopic / methodological failure):**

When an A item records that the paper itself acknowledges a **methodological
failure** of its own primary method — examples include:
- "Root-tracking failed for state X" (computational chemistry)
- "MRCI did not converge for system Y; CASPT2 was used instead"
- "The Sternheimer formalism gave a value 3× experiment"
- "The single-reference method is inadequate for this region"
- "The basis set proved insufficient for property Z"

— record an **additional A-item child** (or a tightly-linked U item) that
asks the **diagnostic question**: "Why does this method fail here, and what
does the failure imply about the method's domain of validity?" Mark this
child item with the note "diagnostic_question_for: A-N (parent failure
record)".

The diagnostic question must:
1. Be distinct from the failure observation itself (which records that
   the failure occurred)
2. Ask for an attribution of cause (e.g., multireference character,
   spin contamination, basis incompleteness, geometric pathology)
3. Be flagged for downstream D-4 promotion in Stage 2 (the diagnostic
   question is an independent D-4 candidate — its grounding is the parent
   A item plus any related B/U items)

This rule was identified in the NobleGas References cross-paper analysis
(analysis_summary_v181_sonnet.md §P2) where multiple computational chemistry
papers acknowledged method failure but did not pursue a diagnostic question
about why the method failed. The diagnostic question is essential for
methodology papers because it bears on the method's domain of validity —
which is the central claim of methodology papers.

**B (Traces of Rejection):**
Approaches, conditions, substrates, or interpretations that the authors
explicitly negated, limited, or set aside within this work.

Classifications: methodological_limitation / intentional_narrowing /
reporting_omission / mixed

reporting_omission: A standard methodological datum that the field
conventionally requires in reporting (e.g., thermochemical correction
type for DFT results, NMR acquisition parameters for quantitative NMR,
HPLC calibration details for selectivity claims) that is entirely absent
from the paper — with no acknowledgment of the omission and no limiting
statement. Unlike methodological_limitation (which involves an explicitly
acknowledged constraint), reporting_omission involves no textual
acknowledgment at all. The rhetorical_function field should read 'not
stated in paper.'
Use this classification when: (a) the paper presents a quantitative
claim, and (b) a standard datum required to evaluate that claim is
absent. Note: when the self-contradictory absence rule (see U below)
also applies, the item receives BOTH a B classification (for the
reporting omission) and a separate U item (for the self-contradictory
absence). The B and U items are complementary, not mutually exclusive.

**Multi-aspect classification rule:** When a single passage shows features
of **both** `intentional_narrowing` and `methodological_limitation` (e.g.,
a scope claim stated as a positive feature but without supporting evidence,
or a condition restriction that is both a deliberate choice and an
unacknowledged constraint), classify as `mixed` and note both components
in the `note` field. Do not default to one classification when both apply.

**B-item consolidation rule:** Before finalizing B items, check for items
that share the **same primary quote**. If two or more B items quote the
same passage (or overlapping passages from the same sentence), consolidate
them into a single B item. The consolidated item should:
- Use the most complete version of the quote
- Apply `mixed` classification if the original items had different
  classifications
- Merge the `note` fields, preserving all flags from both items
- Record all contributing agents' severity ratings in
  `cross_field_temperature`
Do not create separate B items for different analytical angles on the same
quoted passage — those angles belong in the consolidated item's `note`.

<!-- v17 C7: OI-004 — yield basis mixing exception to consolidation rule -->
**B-item consolidation exception — yield basis mixing:**
When the paper uses different yield calculation bases within the same
work (e.g., yield based on starting material vs. yield based on product,
single-substrate yield vs. bilateral yield from both coupling partners,
isolated yield vs. GC yield applied inconsistently across entries), and
this inconsistency constitutes an internal contradiction, do **not**
consolidate these into a general reporting_omission item. Retain them as
independent B items, because the contradiction arises from the
juxtaposition of different metrics, not from a single omission.

**rhetorical_function constraint:** The `rhetorical_function` field must
be a single sentence describing the textual function of the passage (e.g.,
"Disclaimer qualifying yield data," "Scope restriction framed as positive
feature"). Do not include interpretation, analysis, or assessment of
implications — those belong in the `note` field. If the paper does not
provide an identifiable rhetorical function, write "not stated in paper."

Flag when present:
- Metric incompleteness (GC vs isolated yield, missing mass balance)
- Negative result as evidence
- Categorically discontinuous conditions
- Substrate selection bias

**C (Uncontinued Citations):**
Prior works cited but never substantively engaged. State function, reason
severed, affects_claims, symmetric_pattern.

**Exhaustive extraction rule:** Scan ALL references cited in the paper
(footnotes, endnotes, in-text citations). For each cited reference,
determine whether it was substantively engaged — i.e., the paper
discusses the reference's specific findings, reproduces or compares its
data, or designs experiments in response to it. If the reference is
cited but substantive engagement is absent (e.g., cited only as
background, grouped in a list citation, acknowledged without comparison,
or invoked as analogy without validation), classify it as a C item.
Do not limit C items to the most prominent citations — minor footnote
references that are cited-and-dropped are equally valid C items if the
severed engagement affects the paper's claims.

<!-- v17 C4: OI-013 — Dropped Quantitative Benchmark as explicit C sub-type -->
**Dropped Quantitative Benchmark (explicit C sub-type):**
When a prior study is cited in the introduction or related-work section
with specific numerical values (rate constants, activation parameters
such as ΔH‡ or ΔS‡, selectivity values, yields, TON/TOF) and the
results/discussion section does not make a direct comparison on the same
numerical axis, classify it as a C item with `reason_severed` noting
"Dropped Quantitative Benchmark — numerical comparison introduced but
not completed." This pattern is particularly important when the paper's
own results are reported on the same metric (e.g., both papers report
ΔS‡ values) but no direct comparison is presented.

**Antagonist reference exclusion (check before classifying C items):**
A reference that was the direct experimental target of the paper — i.e.,
the paper designed specific experiments to refute or confirm it — is
FULLY ENGAGED and must NOT be classified as C, even if no side-by-side
comparison table exists. Indicator phrases in the paper: "to rule out,"
"against the mechanism proposed by [ref]," "in contrast to [ref],"
"to test the hypothesis of [ref]," "refuting [ref]."
If you initially flag such a reference as a C candidate, reclassify it
immediately and note "fully engaged antagonist — excluded from C" in
your working notes.

**symmetric_pattern values:**
- `yes`: the same rhetorical function (cite-and-dismiss or cite-and-defer)
  applies uniformly to all grouped references
- `partial`: grouped references are cited together but represent
  qualitatively different chemistry or different levels of relevance.
  Note the internal differentiation in the `affects_claims` field.
- `no`: no symmetric pattern

**U (Unclassified):**
Questions that do not fit A/B/C but are analytically important. These may
indicate gaps in the A/B/C classification system itself. Preserve for
direct input to D-4.

**Self-contradictory absence rule:** A question that could be classified
as B (reporting_omission) must ADDITIONALLY be classified as U when the
following condition holds: the paper's own proposed model, mechanism, or
catalytic cycle **predicts** the generation of specific data (e.g.,
byproducts, intermediates, stoichiometric quantities) that are not
reported anywhere in the paper. In such cases, the absence is not merely
an omission of a standard datum (→ B), but a failure to test the paper's
own hypothesis against its own predictions (→ U). Record both: the B
item for the reporting omission, and a separate U item for the
self-contradictory absence. The U item's `note` field must state:
"self-contradictory absence — the paper's proposed [model/mechanism/cycle]
predicts [specific datum] but this is neither reported nor acknowledged
as untested." This rule also applies when an observation noted in the
paper (e.g., anomalous color change, unexpected exothermicity) is
consistent with a scenario that would undermine the paper's claims
(e.g., catalyst decomposition vs. intact catalyst turnover) but is
recorded without characterization or analysis.

<!-- v18.1 C11: multi-critical U-item independent recording protection -->
**Multi-critical U-item independent recording rule (v18.1):**
When a paper contains MULTIPLE self-contradictory absences or
prerequisite-absence patterns, all U items at critical or high severity
must be recorded INDEPENDENTLY. Do not absorb a high-severity U item into
a B item even if a more severe U item is also present. The presence of
one critical U item (e.g., "predicts X but does not test X") does NOT
justify demoting other high-severity U items to B status.

In particular, the following two U-item types are protected from
absorption into B (reporting_omission) and must be recorded as
independent U items when applicable:

(1) **Threshold reliability (閾値信頼性)**: A numerical descriptor or
    score function with a binary classification threshold (e.g., "X > c
    → category A") has internal evidence (boundary cases, outliers, or
    edge data points reported in the paper itself) showing that the
    threshold lacks sharp discriminative power. This is a self-contradictory
    absence: the paper's own data internally undermines the operational
    reliability of its proposed classification rule.

(2) **Inter-system / inter-molecular comparability (分子間比較可能性)**:
    A scalar quantity computed for multiple systems is compared as
    absolute values across systems whose mathematical preconditions for
    such comparison (electron count, orbital count, normalization,
    dimensionality) differ, without justification of the comparison's
    validity. This is a prerequisite-absence: the operational basis for
    cross-system comparison is asserted rather than established.

Both (1) and (2) must be recorded as U items with explicit notes:
- (1): "threshold reliability — the paper's own data ([cite specific
  boundary cases]) shows that the proposed threshold lacks discriminative
  sharpness; this is a self-contradictory absence regarding the
  classification rule."
- (2): "comparability prerequisite — the paper compares [scalar quantity]
  across [systems] without establishing that absolute-value comparison is
  mathematically warranted; this is a prerequisite-absence regarding the
  operational basis."

These U items must be carried forward to Stage 2 D-4 as independent
candidates and not absorbed into other D-4 candidates derived from more
severe U items.

### Step 4: Record META

After classification, record structural connections:
- **linked_items**: A↔B, A↔C connections (use assigned item_ids only)
- **same_root_groups**: Groups of questions from different agents
  that derive from the same underlying data absence. State the shared root
  factually. Do not interpret — interpretation belongs in Stage 2 D-4.
- **symmetric_citations**: C-item pairs abandoned in parallel
- **unreported_data**: data described as existing but not shown
- **series_signal**: evidence of planned publication series (target paper only)

### Step 5: Record GAP

Based on A, B, C analysis, identify papers important for context:
- Type 1: Severed citations to retrieve
- Type 2: Unacknowledged contemporaries
- Type 3: Papers that would answer deferred questions

---

## Turn 4 output format (this is the output passed to Stage 2)

```
prompt_version: stage1-v183-20260427
model_info: <model name and version>

target_title:   [copied from BIB-1]
target_authors: [copied from BIB-2]
target_start:   [copied from BIB-8a]
target_end:     [copied from BIB-8b]

[Agent fields]
V1: [field] — [one-sentence rationale]
V2: [field] — [one-sentence rationale]
V3: [field] — [one-sentence rationale]

[A] item_id | loc | quote | deferral_type | mixed_detail (if mixed; else "n/a") | reason_inferred (T1/T2/T3) | linked_to | cross_field_temperature (if applicable: agent=severity for each, convergence, temperature_gap)

[B] item_id | loc | quote | classification | rhetorical_function (one sentence, function only — no interpretation) | note (REQUIRED — use flags; if none: "note: none") | cross_field_temperature (if applicable)

[C] item_id | loc | citation | textual_function | reason_severed (or "not stated in paper") | affects_claims (yes/no/medium + one sentence) | symmetric_pattern (yes/no/partial)

[U] item_id | loc | quote | question | originating_agent | severity | note: [why A/B/C classification does not apply]

[META]
  linked_items: [list — use only item_ids defined above]
  same_root_groups: [list of groups, each with member item_ids and shared root description — factual only, no interpretation]
  symmetric_citations: [list]
  unreported_data: [list]
  series_signal: [yes/no + inference label + which A-items]

[TEMPERATURE_SUMMARY]
  high_convergence_high_gap: [list of item_ids where convergence ≥ 2/3 AND temperature_gap = medium or high]
  high_convergence_low_gap: [list of item_ids where convergence ≥ 2/3 AND temperature_gap = none or low]
  low_convergence_high_gap: [list of item_ids where convergence = 1/3 AND severity = critical from the flagging agent]

Note on expected frequency: In practice, high_convergence_high_gap is
frequently empty because agents in adjacent fields rarely disagree on
severity by more than one step (distance > 1). An empty
high_convergence_high_gap list is the normal case, not an exception.
The fallback rule is the standard D-4 selection path when this list
is empty — apply it without qualification.

[GAP] request_id | type (1/2/3) | priority | description | candidate_paper | inference_label (T1/T2/T3) | status (pending)

inference_time_sec: <wall-clock seconds if injected by the calling environment;
                     otherwise "not available — inject externally">
```
