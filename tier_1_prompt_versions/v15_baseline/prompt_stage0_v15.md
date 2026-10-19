# Stage 0: Paper Summary
<!-- prompt_version: stage0-v15-20260331 -->

Report the prompt version at the start of your output:
```
prompt_version: stage0-v15-20260331
```

---

## Pre-processing note

If the PDF contains multiple papers printed on the same pages (e.g., JACS
Communications), the calling environment should extract the target paper's
text in advance using a "Sir:"-based splitter and pass only that text here.
If pre-splitting was not performed, apply the identification procedure below.

---

## Output discipline

Produce only the structured fields listed in the Output format section below.
Do not add explanatory prose, offer follow-up questions, suggest next steps,
or append any text outside the specified fields. The output ends with the
`inference_time_sec` field. Internal reasoning about ambiguous loc values or
classification decisions must not appear in output.

---

## Multi-paper PDFs

If the PDF contains more than one independent paper (e.g., back-to-back
communications in a journal issue), analyze only the paper whose
bibliographic information matches the first complete title, author list,
and institutional address found in the document. Do not import data,
claims, or citations from adjacent papers printed on the same pages.

**Identification procedure (mandatory before answering any S0 field):**

Step 1. Scan the entire document for paper boundaries. A boundary is any of:
a bold title line, a new author block with institutional address, or a
"Sir:" salutation that opens a new communication. List every boundary found.

Step 2. Identify which boundary marks the **start** of the target paper —
the first line of its title (not "Sir:", which may follow the title).
Record this as BIB-8a.

Step 3. Identify which boundary marks the **end** of the target paper —
the first line of the *next* paper's title (or "end of document" if none).
Record this as BIB-8b.

Step 4. All S0 fields must draw **only** from text between BIB-8a and
BIB-8b. Text before BIB-8a belongs to a preceding paper; text at or after
BIB-8b belongs to a following paper. This rule applies to every quoted
sentence, every cited reference number, and every observation in S0.

---

Read the attached paper and answer the following sections concisely.
Each answer should be one to three sentences unless otherwise specified.

**Anchoring rule (applies to all fields below):**
Report only what the paper explicitly states. Do not infer, paraphrase beyond
the text, or import background chemical knowledge to fill gaps. If a field
cannot be filled from the paper's text, write "not stated."

Note: The paper text below may include [PAGE N] and L-number markers for line
tracking. These are for downstream use; you may ignore them when reading.

---

[BIB. Bibliographic information]
Extract the following from the paper's header, footer, and first page. Use
exactly what is printed; do not infer or guess missing fields.

[BIB-1] title: <full title as printed>
[BIB-2] authors: <all authors, comma-separated, as printed>
[BIB-3] journal: <journal name as printed>
[BIB-4] year: <publication year>
[BIB-5] volume_pages: <volume, page range or article number>
[BIB-6] doi: <DOI as printed in the document. If no DOI appears in the
              printed text of the document, write "not found". Do NOT
              infer, look up, or reconstruct a DOI from the journal name,
              year, or volume; write only what is visibly printed.>
[BIB-7] format: <full_paper / communication / note / review / letter>
[BIB-8a] target_paper_start: <"page X: first line of target paper's title">
[BIB-8b] target_paper_end: <"page X: first line of next paper's title" or "end of document">

---

[S0-1. Core claim]
What is the single most important finding or contribution this paper claims?
Use the paper's own language where possible.

[S0-2. Evidence type]
What kind of evidence is the claim based on? (e.g., substrate scope table,
kinetic data, spectroscopic characterization, computational results) Report
only evidence types that appear in the paper.

[S0-3. Position against prior work]
How does the paper describe its relationship to prior work? What does it claim
to improve upon or go beyond? Report the paper's own framing; do not assess
whether that framing is accurate.

[S0-4. Methodology]
What is the primary experimental or analytical method used? Describe only
what the paper itself describes.

[S0-5. Reach of conclusions]
What scope does the paper claim for its conclusions? Use the paper's own
qualifications (e.g., "not necessarily optimum," "promising," "limited to")
rather than smoothing them away.

[S0-6. Stated next question]
What does the paper itself identify as the next question or future direction?
Quote directly if brief enough.
**Boundary check (mandatory):** Before including any quote, confirm it falls
between BIB-8a and BIB-8b. If uncertain, append [?boundary] to the quote.

[S0-7. Note Added in Proof]
Does the paper contain a "Note Added in Proof," addendum, or equivalent
late addition? If yes, state in one sentence what it references (e.g.,
a concurrent submission, an erratum, additional data). If no such note
exists, write "none." This field is metadata only — do not analyze
implications.

---

Output format (use exactly):
```
prompt_version: stage0-v15-20260331
model_info: <model name and version as reported by the system, or "not available">
[BIB-1] title: ...
[BIB-2] authors: ...
[BIB-3] journal: ...
[BIB-4] year: ...
[BIB-5] volume_pages: ...
[BIB-6] doi: ...
[BIB-7] format: ...
[BIB-8a] target_paper_start: ...
[BIB-8b] target_paper_end: ...
[S0-1] core_claim: ...
[S0-2] evidence_type: ...
[S0-3] prior_work_position: ...
[S0-4] methodology: ...
[S0-5] conclusion_reach: ...
[S0-6] next_question_stated: ...
[S0-7] note_added_in_proof: ...
inference_time_sec: <wall-clock seconds if injected by the calling environment;
                     otherwise "not available — inject externally">
```
