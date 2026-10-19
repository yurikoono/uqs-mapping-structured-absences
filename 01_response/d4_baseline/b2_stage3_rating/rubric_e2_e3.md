---
title: B2 → Stage 3 — rating rubric for endpoints 2 and 3 (frozen before rating)
created: 2026-09-29
status: active
audience: paperA
open_questions: false
---

# Rating rubric: endpoints 2 and 3 (pre-registration `../preregistration_B2_stage3.md`)

Ten Stage 3 outputs, each identified only by a 6-digit ID. They are in `papers/dev/kumada/b2_stage3_R1_2026-09/in_{id}/`:
`s3.md` is the Stage 3 output, and `record.md` is the input record it was given. The source paper is the middle
communication in `papers/dev/kumada/Kumada_1972.pdf`. **Do not open `_key.json`.**

## Endpoint 2 — quotations (`e2_quote_packets.json`)

Each row is a quoted string from an s3 output that failed or weakly matched the mechanical gate. Check it against the PDF,
reading page images where the text layer is scrambled, and classify it as one of:

- **M** — does not faithfully report the source. Wording is altered in a way that changes meaning; a value or relation is
  wrong; the attribution is wrong; or the string cannot be found and is presented as a quotation of the paper.
- **B** — borderline: a word is inserted or dropped inside quotation marks and the meaning is preserved, or a drawn
  formula has been transcribed with something lost.
- **S** — present in the source: table or scheme text, OCR or ligature artefacts, or an ellipsis joining genuine segments.
- **C** — meaning-preserving compression or paraphrase inside quotation marks.
- **A** — model-authored text in quotation marks that is not presented as a quotation of the paper (for example a
  proposed question, a field label, or an example of language the paper does not use), or text the gate harvested from
  between two quoted terms.

Output per row: `{"q": id, "class": "M|B|S|C|A", "source_text": "≤30 words from the PDF, or 'not found'", "note": "…"}`.

## Endpoint 3 — support by the input record (one judgement set per output)

For each s3 output, read its §2 (SRG/CLA crosswalk), §3 (VQ assessment) and §5, and compare them with its `record.md`.
List every **unsupported fill**: a statement that presents, as though it were in the input, content that the record does
not contain, and that neither the record nor the PDF supports, without the output saying it is missing or inferred.
Examples:
- convergence or temperature values when the record has none;
- member items or IDs that the record does not contain;
- a D-4-derived claim when the record has no D-4;
- a paper fact that is neither in the record nor in the PDF.

Do not list:
- content the output explicitly marks as absent from the record, or as inferred ("not available", "inferred from …");
- ordinary Stage 3 analysis derived from the record or the PDF.

Output per s3: `{"output": id, "unsupported_fills": [{"quote": "≤30 words from s3", "why": "…"}], "flagged_inferences": n, "notes": "…"}`.
Here `flagged_inferences` counts the places where the output supplies something **and** labels it as inferred.

Read everything yourself. Scripts may only split or assemble files; they must not decide anything.
