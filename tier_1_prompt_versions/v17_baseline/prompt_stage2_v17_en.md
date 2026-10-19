# Stage 2: Interpretation (D-1 through E) — English-only track
<!-- prompt_version: stage2-v17-en-20260419 -->
**Language: English throughout (English-only evaluation variant of stage2-v17-20260415)**

Report the prompt version at the start of your output:
```
prompt_version: stage2-v17-en-20260419
```

*Paste the full Stage 1 output (A, B, C, U, META, GAP, TEMPERATURE_SUMMARY)
before running this prompt.*

*If prior papers' Stage 2 analyses are available, paste them after the Stage
1 output. D-4 may reference patterns observed in prior papers. If no prior
analyses are available, proceed with this paper's Stage 1 output alone.*

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

## Output discipline

Produce only the structured fields listed in the Output format section below.
Do not add explanatory prose, offer follow-up questions, suggest next steps,
or append any text outside the specified fields. The output ends with the
`inference_time_sec` field.

---

## Anchoring discipline (carried forward from Stage 1)

The same three-tier distinction applies here:

| Tier | Label | Meaning |
|------|-------|---------|
| **T1** | *(no label)* | Directly stated in the paper text |
| **T2** | `[paper-grounded inference]` | Follows directly from the text; one step only |
| **T3** | `[external inference]` | Draws on knowledge outside the paper |

**Additional rules for Stage 2:**

- **Novelty claims (D-1):** Report what the paper claims as novel. Do not
  independently assess whether the claim is accurate against the literature
  — that requires external verification. If the paper's novelty claim
  depends on a literature comparison not supported by the paper's own cited
  evidence, flag it with
  `[paper-grounded inference: comparison asserted, not experimentally verified]`.

- **Catalyst identity precision:** When the paper names a specific complex
  as a representative catalyst within a class (e.g., one bidentate
  diphosphine complex among several tested), describe it as representative
  of the class, not as uniquely enabling. Privileging one complex above its
  reported class requires explicit textual support.

- **Scope of the propositional form (E):** The `confirmed_english_propositional`
  must encode the paper's stated substrate scope and nothing else. Apply
  these rules in order before writing the proposition:
  1. Use the paper's exact conjunction (or / and) as printed.
  2. Do not add any modifiers, result clauses, or feature phrases. The
     proposition ends after naming the substrate scope — no "to yield X",
     no "suppressing Y", no "with high Z".
  3. Check: could the proposition be falsified by a substrate-scope
     counterexample alone (not by a yield or selectivity measurement)?
     If no, remove the offending phrase and recheck.
  - **Bad examples** — do not produce any of these:
    - "...high-yield cross-coupling..." → "high-yield" is a feature, not scope
    - "...aryl and vinyl halides" → use "or" if the paper prints "or"
    - "...suppressing homocoupling products" → result phrase, not scope
    - "...to yield coupled products" → result clause, not scope
  - **Good example:** "Nickel-phosphine complexes catalyze selective
    cross-coupling of Grignard reagents with vinyl or aryl halides."

  **Mechanism papers:** For papers whose S0-1 core_claim describes a
  mechanistic finding (a pathway re-assignment, rate-determining step
  identification, or mechanistic distinction) rather than a new synthetic
  transformation, the confirmed_english_propositional describes the
  transformation studied — not the mechanistic finding itself. The
  proposition must still end after naming the substrate scope (no mechanism
  clause). Example:
    Correct:   "Palladium complexes catalyze copper-free Heck-Cassar-
                Sonogashira cross-coupling of terminal alkynes with aryl
                halides or triflates."
    Incorrect: "...via direct alkyne coordination rather than Pd(II)-Pd(II)
                transmetalation." [mechanism clause — prohibited]
  The mechanistic finding belongs in confirmed_english_question only.

- **Scope anchor rule:** The substrate scope terms in
  `confirmed_english_propositional` must be anchored to the **paper's own
  stated scope** (BIB-1 title and S0-1 core_claim), NOT to the actual
  coverage detected by Stage 1 agents. Stage 1 agents may correctly observe
  that the paper's data covers only chlorides, but if the paper's title says
  "organic halides" and S0-1 says "vinyl or aryl halides," the propositional
  must use "halides" (or "vinyl or aryl halides"), not "chlorides."
  The narrower actual scope is properly recorded as a D-4 candidate
  (the gap between stated and demonstrated scope), not in the propositional.
  - **Example of the error this rule prevents:**
    Title says "organic halides" → V3 notes "only chlorides tested" →
    propositional incorrectly narrows to "chlorides" → WRONG.
    Correct: propositional uses "halides" per title; D-4 records the
    gap between stated and demonstrated scope.

- **scope_type determination (E):** Assign scope_type based on the
  `confirmed_english_question` alone. Ask: does this specific question, as
  written, require stepping outside chemistry to answer? If yes →
  beyond_chemistry. Does it ask for a general principle or framework within
  chemistry? If yes → framework_question. Does it ask for a specific tool,
  reagent, or condition? If yes → tool_question. Do not let the broadest
  transformation explored in the scope-abstraction step of E inflate the
  scope_type of the confirmed question.

  **Disambiguation criteria for tool_question vs. framework_question:**
  Before assigning `tool_question`, check: does the
  `confirmed_english_question` ask *whether a specific tool, catalyst,
  or reagent enables a particular reaction* (→ tool_question), or does it
  ask *what boundary conditions, design principles, or governing factors
  determine reactivity or selectivity* (→ framework_question)? A question
  about catalyst design is `tool_question` only if the answer would be a
  specific reagent, condition, or protocol — not a general design
  principle or structure-activity relationship.

- **holy_grail_narrative (D-3):** Classify as "yes" only if the paper itself
  uses mythologising or quest-framing language (e.g., "long-sought",
  "elusive goal", "dream reaction", "holy grail"). Framing a known
  problem as unsolved and then presenting a solution is **not** sufficient
  for a "yes" classification — that is normal scientific rhetoric. Require
  direct textual evidence of aspirational/quest language.

- **Suppressed-reading guard (D-2, D-3, D-4):** Identifying a footnote or
  syntactic move as evidence of *suppression* requires that the paper shows
  (a) awareness of the tension and (b) a textual move away from it. The
  co-occurrence of an anomalous result and a utility reframe is suggestive
  but not conclusive. When the paper also acknowledges the anomaly directly
  elsewhere (e.g., in a "further studies are required" sentence), classify
  as T2 reframing rather than suppression.

- **Competitive and institutional narratives (D-2, D-3):** Statements about
  field dynamics, institutional motives, or publication culture that go
  beyond the paper's own text must be labeled `[external inference]` and
  kept to one sentence maximum. Do not construct narratives about group
  prestige, national standing, or competitive urgency that are not supported
  by the paper itself. The existence of a concurrent submission (Note Added
  in Proof) establishes priority-sensitive context; the strength or urgency
  of competition cannot be further characterized from the paper alone.

- **T3 elaboration limit:** A T3 claim must be stated in one sentence and
  must not be elaborated into a narrative, even if labeled. If more than one
  sentence is needed to make a T3 point, that is a signal the claim exceeds
  what the paper supports.

- **D-4 grounded_in — item_id rule:** Each candidate must carry a
  `grounded_in` field listing specific Stage 1 item_ids that actually
  appear in the Stage 1 output. **Use only the final A/B/C/U item_ids
  assigned in Turn 4** (e.g., A-1, B-3, C-2, U-1). **Do not reference
  turn-level question IDs** (V1-Qx, V2-Qx, V3-Qx) — these are
  intermediate labels that are superseded by Turn 4's classification.
  If a D-4 candidate draws on a question that was not classified into
  A/B/C/U (e.g., it was subsumed into another item's note), reference
  the A/B/C/U item that absorbed it.
  Candidates with no textual anchor
  (`grounded_in: none (retrospective)`) should be rare and clearly separated
  under the heading "questions_that_cannot_be_asked."

---

**[D-1. Declared motivation]** *(English)*

What does the paper explicitly state as its purpose and contribution?
Identify:
- The specific claims of novelty, using the paper's own language
- The performance criteria by which the authors measure success — report
  only criteria the paper itself invokes
- Whether the novelty claims are structured in layers such that no single
  refutation can collapse all claims simultaneously

For each claim, note whether it is **directly stated (T1)** or requires one
reasoning step from the text **(T2)**. Do not import external chemical
knowledge to strengthen or qualify claims.

---

**[D-2. Inferred motivation]** *(English)*

What motivations can be read from the paper's tone, emphasis, and citation
patterns — beyond what is explicitly stated? Address each of the following.
**Label each claim T2 or T3 as appropriate. T3 claims must be one sentence
maximum and must not be elaborated.**

- *Competitive positioning*: How does the paper position itself against named
  prior work? State whether the comparison is experimentally verified within
  the paper or asserted.
- *Concurrent submissions*: If the paper contains a "Note Added in Proof"
  or equivalent acknowledgment of a concurrent or competing submission,
  address the following as a mandatory sub-item: (a) does the paper
  establish any experimental or conceptual distinction between its system
  and the concurrent work? (b) If no distinction is drawn, note this as a
  gap in competitive positioning and assess whether it affects the paper's
  novelty claims (`affects_novelty_claims: yes/no/indeterminate + one
  sentence`). If no Note Added in Proof exists, write "not applicable."
- *Timing pressure*: Does the pattern of deferrals in A suggest urgency?
  Anchor to specific A-items; do not assert the degree of urgency beyond
  what the text supports.
- *Format exploitation*: Does the paper appear to use its publication format
  to compress weaknesses out of view? Anchor to specific B-items.
- *Audience targeting*: What does the paper's vocabulary and example
  selection suggest about its intended audience? Anchor to the text.
- *Institutional visibility*: `[external inference — one sentence maximum]`

---

**[D-3. Institutional motivation]** *(English)*

What competitive pressures, field trends, or publication conventions appear
to have shaped the paper's design and framing? Consider:
- Journal format and its constraints on reporting completeness — anchor to
  specific B-items
- State of the subfield at the time of publication — `[external inference]`
  if not derivable from the paper's own citations
- What the paper's own framing implies about what needed to be demonstrated
  to be taken seriously
- Whether the paper's framing invokes a "holy grail" narrative — requires
  direct textual evidence of aspirational or quest language in the paper
  itself (see anchoring rule above); classify as "no" if the paper uses
  only standard problem-solution framing

**Do not describe the paper as "entering a race" or characterize competitive
urgency with intensity modifiers (e.g., "intense," "high") unless the paper
itself uses such language.** Describe only what the paper's citation pattern
and framing imply.

**Commercialization potential:**
If the paper explicitly mentions commercial, practical, or industrial
context (cost, scale, availability, waste, regulatory), record these as
T1 or T2 entries under `commercialization_potential`. If the paper does not
mention any commercial context, write "not stated in paper." Do not import
external market, patent, or regulatory analysis — such information belongs
outside the paper-anchored analysis.

---

**[D-4. Unquestioned motivations]** *(English)*

Using the observations recorded in Stage 1's A, B, C, U, and META as
material, describe the motivations and questions that should have been
asked but which the paper does not attempt to answer.

**Exploiting cross_field_temperature:**
Refer to Stage 1's TEMPERATURE_SUMMARY and explore candidates in the
following priority order.
1. **high_convergence_high_gap items** come first. These are items that all
   agents flagged but whose severity assessments diverged, and therefore
   constitute the strongest signal that the field's tacit consensus is
   structurally hiding something.
2. **low_convergence_high_gap items** are also considered. Items that
   received a critical rating from a discipline-specific baseline indicate
   a structural blind spot that is visible only from that discipline.
3. **U items** (questions that could not be classified into A/B/C but were
   judged important) are included in the D-4 search space. In particular,
   items flagged as "self-contradictory absence" indicate a missing datum
   predicted by the paper's own model and frequently form the core of D-4
   candidates. For each U item, judge explicitly whether it constitutes an
   independent D-4 candidate or should be recorded as a sub-element of an
   existing candidate.

**Fallback rule:** If high_convergence_high_gap is empty (all
high-convergence items have gap=none/low), choose priority candidates in
the following order:
(a) low_convergence_high_gap items with a critical rating first
(b) high_convergence_low_gap items with convergence=3/3 next
(c) same_root_groups that contain the largest number of A/B items across
    the group
In that case, record at the top of the D-4 output:
"high_convergence_high_gap: none — fallback rule applied."

**Exploiting same_root_groups:**
Refer to Stage 1 META's same_root_groups. If a group of questions sharing
a common root exists, describe **the entire group as a single D-4
candidate** rather than as separate candidates. Record the shared root
(e.g., "systematic absence of quantitative experimental verification") as
the core of the candidate, and enumerate the individual questions (e.g.,
absence of TON, absence of mass balance, absence of replication) as
sub-elements.

**Textual-basis requirements:**
Each candidate must carry the following fields. Each field must appear on
an **independent line** (do not concatenate onto one line):
```
grounded_in: [list of A/B/C/U item_ids assigned in Turn 4. Turn-level IDs
              such as V1-Qx or V2-Qx are prohibited. Only A/B/C/U ids
              actually present in the Stage 1 output may be used. U-item
              ids are allowed.]
key_quote: [a one-sentence quote from the paper's main text that supplies
            the grounding. Supporting Information (ESI/SI) text may not be
            used. If no direct grounding exists in the main text, use the
            main-text sentence that provides the closest context and label
            the candidate T2 or T3.]
temperature_note: [if applicable: which TEMPERATURE_SUMMARY entry the
                   candidate derives from]
same_root_group: [if applicable: which META same_root_group the candidate
                  belongs to]
```
**Output-format discipline:** the four fields above must always be
separated by line breaks. A single-line concatenation such as
`grounded_in: B-1, B-2 key_quote: "..."` is prohibited because it breaks
downstream parsing.
If no direct textual grounding exists, distinguish the two sub-cases as
follows:
- `grounded_in: [T2: item_id]` — reachable from a Stage 1 item by a single
  step of inference
- `grounded_in: none (retrospective)` — cannot in principle be derived
  from the paper's text (a retrospective observation)

`grounded_in: none (retrospective)` candidates should be kept to a
minimum and aggregated into a separate block of "questions that cannot be
asked."

**Deduplication (mandatory):**
Before finalizing each candidate, perform the following duplication check.
- Candidates that reference the same key_quote must be merged into one.
- Questions that are substantively identical must be collapsed into the
  single candidate whose key_quote is clearest, with the other facets
  added as a one-sentence note.
- If more than eight candidates remain after collapsing, keep only the top
  eight whose key_quote and grounded_in are clearest.

**Starting perspectives (other observations are also welcome):**
- What the catalyst or reagent is "consuming" during the reaction (issues
  of deactivation, recovery, and reuse)
- The counterpart to "high selectivity" — the potential existence of
  species that were not detected
- Systematic absence of non-reactive substrates or conditions
- Absence of a connection to a concrete synthetic target
- The principled rationale behind the choice of metal, ligand, and solvent
- Teleological questions about what end this reaction serves as a means
- Absence of a thermodynamic frame: whether selectivity, yield, and
  conditions are presented independently of the question "kinetic control
  or thermodynamic drive." Record this as a question separate from the
  mechanism discussion (A-class items).
- Analytical basis for negative evidence: when the paper uses results such
  as "not detected" or "not observed" as positive mechanistic evidence,
  always verify whether the detection limit and detection conditions are
  stated in the main text. If the experimental basis needed to distinguish
  "not detected = absent" from "not detected = below detection threshold"
  is missing, record the item as a D-4 candidate. (Pay particular
  attention to B items flagged with "negative result as evidence.")

<!-- v17 C3: OI-007+008 — additional D-4 candidate selection checks -->
**Additional checks (always verify when selecting D-4 candidates):**

(a) **Detection limits for negative evidence:** when the paper uses
negative statements such as "not detected," "never observed," or "not
formed" as the basis for a mechanistic claim, confirm whether the
detection limit of that observation (sensitivity of the method, measuring
conditions) is recorded in the main text. If negative evidence is used as
positive mechanistic evidence without such information, record the item
as a D-4 candidate. If the check is linked to a B-item flagged "negative
result as evidence," include that B-item's item_id in grounded_in.

(b) **Extrapolation to practical conditions:** when any of the
experimental conditions recorded in the paper diverges substantially from
ordinary synthetic use (catalyst loading ≥ 5× the usual level, substrate
concentration ≥ 10× the usual level, reaction temperature outside the
practical range, etc.), record the question of extrapolability to
practical conditions as a D-4 candidate. This is especially important
when the paper itself claims practical utility.

(c) **Matched-pair control:** when the paper presents an experimental
pair as a control (comparison of A vs. B) but the substrate, reagent, and
conditions used in A differ from those used in B (i.e., the pair is not
matched), record the asymmetry as a D-4 candidate. When multiple
variables are changing simultaneously under the "control experiment"
label, causal attribution becomes uncertain.

**Always list the following as an independent item:**
- **Unaskable questions**: questions that cannot in principle be answered
  from the paper's text (institutional conditions, funding sources, the
  authors' interior states, incidental knowledge backgrounds, etc.).
  Record these explicitly as `grounded_in: none (retrospective)` and
  distinguish them as the kind of question that is "unaskable" rather than
  "should be asked."

Finality is not required. Phrasing such as "may be the case" or "could
also be read as" is acceptable. However, when speculation moves away from
the paper's text, mark the claim with `[T3]` and keep it concise (one
sentence).

**Record last (the priority-ordering structure):**
Across these candidates, if a structure emerges in which "something else
was deferred in order to establish something," describe that structure.
Avoid asserting intentionality; maintain the form "the structure can be
read as..." Indicate explicitly which A/B items provide the grounds for
the structure.
In particular, look for the following **pivot structure**:
- When an experimental explanation that would be required to establish
  the paper's central claim has been placed "outside" as future work (an
  A item that avoids shouldering the explanation demanded by a B item),
  make that A/B pair explicit as a pivot item.
- When the quantitative basis for multiple B items has been omitted in a
  shared manner (same_root_group) and, without that omission, the
  quantitative reliability of the claim would not hold, make that SRG
  explicit as the core of the structure.
Mark pivot items in the form "A-n ↔ B-m (pivot)".

---

**[E. Questions of scope]** *(English throughout)*

First, abstract the form of the question that this paper answered in its
chemical context.

**Attach:**
```
derived_from: [the D-4 candidate number or A/B/C/U item_id that supplies
               the basis]
anchoring_note: [one sentence indicating which of T1/T2/T3 this
                 abstraction belongs to]
```

Next, enumerate multiple transformations of that form into questions in
other contexts. The target contexts are free. For each transformation:
- Describe the transformed question
- Indicate naturally whether it is "the same structure in a different
  guise" or "a figurative similarity"

Explain why you selected the transformation with the broadest reach, and
then produce the following two forms.

**Constraints on confirmed_english_propositional (restated + scope anchor
rule):**
- Single sentence, at most 20 words, no subordinate clauses
- Must include chemically meaningful tokens (used for embedding comparison)
- Must describe only what the paper actually demonstrated (do not
  retrospectively historicize)
- **Must reflect the *stated* substrate scope, and must not add features.
  Scope terms must follow BIB-1 (title) and S0-1 (core claim). A narrower
  *demonstrated* coverage that Stage 1 agents identified (e.g., "only
  chlorides in fact") must be recorded as a D-4 candidate, not reflected
  in the E propositional.**
- Use the paper's own conjunctions (or / and) as printed
- Do not add result clauses such as "to yield X"
- **Prohibited examples (do not produce):**
  - "...high-yield cross-coupling..." — feature inserted
  - "...aryl and vinyl halides" — "and" is impermissible if the paper
    prints "or"
  - "...to yield coupled products" — result clause attached
  - "...suppressing homocoupling..." — feature attached
  - "...vinyl or aryl chlorides" — narrowed to agent-detected effective
    scope

**Constraints on confirmed_english_question:**
- An English interrogative form of the question the paper actually
  addressed
- Not the "broadest transformation" selected in the scope abstraction, but
  the question faithful to the paper's actual research problem
- scope_type is determined independently on the basis of this question
  alone (do not be pulled by the breadth of the scope-abstraction
  transformation candidates)

```
confirmed_english_propositional: "..."
confirmed_english_question: "..."
scope_type: "beyond_chemistry / tool_question / framework_question"
```

**REQUIRED OUTPUT — do not omit:**

```confirmed_english
confirmed_english_propositional: "..."
confirmed_english_question: "..."
scope_type: "..."
```

---

**Output format**

```
prompt_version: stage2-v17-en-20260419
model_info: <model name and version as reported by the system, or "not available">

[D-1] declared_motivation | novelty_claims (T1/T2 labeled) | success_criteria | layered_structure (yes/no + brief explanation)

[D-2] competitive_positioning (verified/asserted) | concurrent_submissions (distinction drawn? affects_novelty_claims?) | timing_pressure (anchored to A-items) | format_exploitation (anchored to B-items) | audience_targeting | institutional_visibility ([external inference], one sentence max)

[D-3] journal_constraint (anchored to B-items) | field_competition_state ([external inference] if not from paper's citations) | entry_criteria (paper-implied only) | holy_grail_narrative (yes/no + direct textual evidence required for "yes") | commercialization_potential (T1/T2 from paper text only, or "not stated in paper")

[D-4] (English text)
      candidates: [each candidate with grounded_in (A/B/C/U item_ids only,
                   V-Q numbers prohibited) + key_quote + temperature_note +
                   same_root_group, deduplicated, upper bound 8]
      questions_that_cannot_be_asked: [aggregate of items with
                   grounded_in: none (retrospective)]
      priority_structure: [structural description, avoid asserting
                   intentionality, indicate the grounding A/B items,
                   and mark pivot items in the form "A-n ↔ B-m (pivot)"]

[E]   derived_from: [item_ids]
      anchoring_note: [which of T1/T2/T3]
      (English: description of the transformations + reason for the
       selected broadest transformation)

confirmed_english
confirmed_english_propositional: "..."
confirmed_english_question: "..."
scope_type: "..."

inference_time_sec: <wall-clock seconds if injected by the calling environment;
                     otherwise "not available — inject externally">
```
