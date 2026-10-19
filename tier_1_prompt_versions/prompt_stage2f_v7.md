# Stage 2F: Within-Group Comparison
<!-- prompt_version: stage2f-v7-20260417 -->
**Language: English**

Report the prompt version at the start of your output:
```
prompt_version: stage2f-v7-20260417
```

*Paste the Stage 0, Stage 1, and Stage 2 (D-1 through E) outputs of ALL papers in the group before running this prompt.*

**Integration mode:** If the input consists of Stage 2F outputs from
multiple sub-groups (rather than raw Stage 0/1/2 outputs), this prompt
operates in integration mode. In integration mode:
- Identify patterns that emerged **independently** in multiple sub-groups
  without being seeded by the shared reference paper
- Cross-reference recurring_roots across sub-groups to detect field-wide
  (rather than sub-group-specific) structural patterns
- Synthesize sub-group-level group_unasked_questions into a single
  integrated question, noting whether the sub-group questions are
  independent or facets of a single underlying problem
- If Stage 3 outputs are available for the reference paper, cross-reference
  the EP filling landscape with the 2F patterns to assess whether the
  VQ hierarchy corresponds to the observed filling order

---

## Output discipline

Produce only the structured fields listed in the Output format section below.
Do not add explanatory prose, offer follow-up questions, suggest next steps,
or append any text outside the specified fields.

---

**[F. Within-Group Comparison]**

**Repeated patterns**
Which types of bypassed questions recur across papers in this group? List them with the paper IDs where each pattern appears.
For each pattern, provide:
```
evidence_chain: [paper_id : item_id for each paper, e.g., "Kumada_1972 : B-6, Murai_1993 : B-3"]
```

**Cross-field temperature patterns**
If Stage 1 outputs include cross_field_temperature data, compare the
temperature profiles of repeated patterns across papers:
- Do the same gaps receive the same severity distribution across papers?
  (e.g., is "mass balance absence" rated V1=low, V3=high in both papers?)
- Where temperature profiles differ across papers, note the difference and
  hypothesize what accounts for it (format, era, subfield norms).
- Identify any gap whose temperature_gap **increases** across later papers —
  this may indicate a field norm that is becoming more contested.

```
temperature_pattern: [pattern_id] | papers: [list] | profile_consistency: [consistent/divergent] | note: [one sentence]
```

**Same-root group patterns**
If Stage 1 outputs include same_root_groups in META, compare whether the
same root (e.g., "quantitative experimental validation absent") recurs
across papers. Record:
```
recurring_root: [root description] | papers: [list] | member_items: [paper_id:item_ids for each] | note: [is this a genre convention or a structural gap?]
```

**Temporal trajectory of recurring patterns**
If the group spans multiple years, assess how each recurring pattern
changes over time. Classify each pattern into one of the following:
- *Time-invariant*: the gap persists with essentially the same character
  across all years in the corpus, regardless of available technology or
  changing field norms. This is the strongest evidence for a field-wide
  structural convention rather than an individual or era-specific choice.
- *Narrowing*: the gap is progressively addressed but never fully closed.
  The evidential basis improves over time but no paper achieves complete
  resolution.
- *Shifting*: the character of the gap changes over time (e.g., from
  "structurally suppressed" because tools were unavailable, to
  "individually chosen" because tools are now available but not applied).
  Record the transition point (year/paper) where the shift occurs.
- *Emergent*: the gap appears only in later papers and is absent in earlier
  ones (e.g., DFT-related gaps that cannot exist pre-DFT).

```
temporal_trajectory: [pattern_id] | classification: [time-invariant/narrowing/shifting/emergent] | transition_point: [year/paper if applicable] | note: [one sentence]
```

**Structural suppression vs. individual choice**
For each repeated pattern, apply the following diagnostic criterion:
- *Individually chosen*: would be answerable with the paper's own
  experimental infrastructure but is absent
- *Structurally suppressed*: answering would require a different genre of
  paper, a different institutional collaboration, or a different timescale
  of research
- *Incentive-suppressed*: answering is technically feasible but the
  resulting work would not constitute a publishable contribution under
  current publication norms (e.g., replication studies, benchmark
  comparisons of existing systems, mass balance audits). Distinguish from
  "individually chosen" by asking: would ANY group in the field be
  incentivized to do this work? If not, it is incentive-suppressed.
- *Era-dependent*: the diagnostic changes over time. Record the
  transition: e.g., "structurally suppressed (1972: tools unavailable)
  → individually chosen (2021: tools available, not applied)"

**Paradigm competition**
Does the group reveal competing paradigms for solving the same problem? If so:
- Name the competing paradigms explicitly
- Identify which questions each paradigm systematically leaves unanswered
- For each "systematically unanswered question," state the evidence_chain:
  ```
  evidence_chain: [paper_id : item_id → key quote, OR "no textual basis in [paper_id]" if the gap is visible only retrospectively]
  ```
  Gaps with "no textual basis" are retrospective — they become visible only through comparison with later work, not from the paper's own text. This distinction is analytically significant.
- Note whether the gap left by one paradigm is precisely the space that another paradigm later occupies. If the relationship is sequential (one paradigm's blind spot becomes the next paradigm's founding problem) rather than competitive, state this explicitly — the distinction between paradigm competition and paradigm succession is analytically significant.

**Divergences**
Where the gaps differ across papers: what accounts for the difference? Consider subfield, year, journal format, and competitive landscape.
For each divergence, provide:
```
evidence_chain: [paper_id : item_id for each paper supporting the divergence claim]
```

**U-item patterns**
If any U items (unclassified questions) from Stage 1 recur across papers,
record them as a separate pattern category. Recurring U items may indicate
a systematic gap in the A/B/C classification framework itself.
```
recurring_U: [description] | papers: [list] | item_ids: [list] | note: [implication for classification framework]
```

**Self-contradictory absence patterns**
Specifically check whether the following pattern recurs across papers:
a paper proposes a model (catalytic cycle, reaction mechanism, selectivity
model, etc.) that predicts specific observables, but those observables are
not tested within the paper itself. This "self-contradictory absence" is
distinct from ordinary B-items (scope limitations) because the gap is
generated by the paper's own logic rather than by external norms.

For each instance, record:
```
self_contradictory: [paper_id] : [model/cycle proposed] → [prediction generated] → [prediction untested] | item_id: [U-item or B-item reference]
```

If this pattern recurs across multiple papers, assess whether it reflects:
- A **narrative function** of mechanism diagrams in methodology papers
  (cycle diagrams serve to contextualize scope data rather than to generate
  testable predictions)
- A **genre convention** (methodology papers are not expected to validate
  their own mechanistic proposals)
- A **genuine analytical gap** (the predictions could and should be tested)

**Group-level unasked question**
State in one English sentence the question this group of papers most systematically failed to ask.
Provide:
```
evidence_chain: [paper_id : item_id pairs that collectively support this conclusion]
```
If TEMPERATURE_SUMMARY data is available, note whether the group-level
unasked question corresponds to any high_convergence_high_gap items.
If same_root_groups recur across papers, note whether the group-level
unasked question corresponds to a recurring root.

**Integration mode additional requirement:** If sub-group-level
group_unasked_questions are available, assess whether they are:
- **Independent**: genuinely different questions arising from different
  aspects of the field
- **Facets of a single problem**: different manifestations of one
  underlying unsolved problem
If the latter, state the unified question and explain how the sub-group
questions relate to it as facets.

---

**Output format**

```
prompt_version: stage2f-v7-20260417

[F]   repeated_patterns: each with evidence_chain
      | temperature_patterns: each with profile_consistency (if cross_field_temperature data available)
      | recurring_roots: (if same_root_groups recur across papers)
      | temporal_trajectories: each with classification (if group spans multiple years)
      | suppression_diagnostic: (individually_chosen / structurally_suppressed / incentive_suppressed / era_dependent)
      | paradigm_competition: each unanswered question with evidence_chain
        (use "no textual basis in [paper_id]" for retrospective gaps)
      | divergences: each with evidence_chain
      | recurring_U: (if applicable)
      | self_contradictory: (if applicable)
      | group_unasked_question: "[英語一文]" with evidence_chain
```
