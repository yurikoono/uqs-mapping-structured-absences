# Stage 2F: Within-Group Comparison
<!-- prompt_version: stage2f-v6-20260329 -->
**Language: English**

Report the prompt version at the start of your output:
```
prompt_version: stage2f-v6-20260329
```

*Paste the Stage 0, Stage 1, and Stage 2 (D-1 through E) outputs of ALL papers in the group before running this prompt.*

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

**Structural suppression vs. individual choice**
For each repeated pattern, apply the following diagnostic criterion:
- *Individually chosen*: would be answerable with the paper's own experimental infrastructure but is absent
- *Structurally suppressed*: answering would require a different genre of paper, a different institutional collaboration, or a different timescale of research

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

---

**Output format**

```
prompt_version: stage2f-v6-20260329

[F]   repeated_patterns: each with evidence_chain
      | temperature_patterns: each with profile_consistency (if cross_field_temperature data available)
      | recurring_roots: (if same_root_groups recur across papers)
      | suppression_diagnostic
      | paradigm_competition: each unanswered question with evidence_chain
        (use "no textual basis in [paper_id]" for retrospective gaps)
      | divergences: each with evidence_chain
      | recurring_U: (if applicable)
      | group_unasked_question: "[英語一文]" with evidence_chain
```
