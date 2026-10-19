# D4 — quote adjudication across arms (FAIL + WARN < partial 85, all quote kinds)

> **Note (2026-10-19).** This record gives the state of 2026-09-29. The author check of 2026-10-05 is in `01_response/verification/human_verification_D3D4_20260929.md` (the author's marks and notes) and is reported in SI-6.10 and SI-11.20; statements below that no human has verified the ratings or the adjudication describe the state before it.

Adjudicator: the orchestrator (Claude). Decisive cases were checked on rendered page images of `Kumada_1972.pdf`: p. 4375 Table I and eq 1,
and p. 4376 for the activity order. **No human has verified these yet.** Candidate rows (`d4_quotes.csv`): UQS 53, B0 3, B1 2, B2 70.

Every candidate row was read. Most are Table I rows reconstructed from a scrambled text layer (present in the source), ellipsis or
compression inside quotation marks, or model-authored text (rhetorical_function descriptions, `framework_question`, lists of language
absent from the paper). The rows below are the ones judged to misreport the source, or to be borderline.

| arm | run | string | source | class |
|---|---|---|---|---|
| UQS v18.4 | 5 | "the following processes may be involved" (S1 V2-Q2, cited as the Kumada catalytic cycle, p. 4374–4375) | The phrase belongs to the **preceding hydrosilylation communication** on the same PDF page (Kiso et al.); it is not in the Kumada paper | **misreport (cross-paper)** |
| UQS v18.4 | 1 | "L₂Ni(X″) + RMgX′ → [L₂Ni(R)(R′)] + MgX′X″" (eq 4) | eq 4 is drawn: L₂Ni(X″)(R′) + RMgX′ → L₂Ni(R)(R′) + MgX′X″; R′ is dropped from the reactant | borderline (lossy transcription of a drawn scheme) |
| B2 | 1 | "[NiCl₂(dpp)] > [NiCl₂(dpe)] > [NiCl₂(dmpe)] << [NiCl₂(PPh₃)₂]" | p. 4376: "[NiCl₂(dmpe)] ≈ [NiCl₂(PPh₃)₂] ≫ …" | **misreport (relation inverted)** |
| B2 | 2 | "n-C₈H₁₇MgCl / CH₂=CHCl / Condition B / n-C₈H₁₇CH=CH₂ / 95%. Reaction proceeded exothermally." | Table I: that entry carries footnote e (glpc yield). Footnote f ("Reaction proceeded exothermally") is on the PhMgBr/CH₂=CHCl, ClCH=CHCl and Cl₂C=CH₂ halides | **misreport (footnote attached to the wrong entry)** |
| B2 | 5 | "n-C₆H₁₃MgCl / CH₂=CHCl / B / n-C₈H₁₇CH=CH₂ / 95" | Table I: n-C₈H₁₇MgCl | **misreport (reagent misread)** |
| B2 | 4 | "(dipy)Ni + PhCl → (dipy)Ni · 0.5PhCl + Et–Et" (eq 1) | eq 1 is drawn with Et₂ on the left and Ph and Cl on the right; the ligands are dropped | borderline (lossy transcription of a drawn scheme) |

Summary:

| arm | runs with ≥ 1 misreport | misreports | borderline |
|---|---|---|---|
| UQS v18.4 | 1/5 | 1 | 1 |
| B0 | 0/5 | 0 | 0 |
| B1 | 0/5 | 0 | 0 |
| B2 | 3/5 | 3 | 1 |

Note on the UQS arm: Methods 6 states that "all 33 key_quote anchors matched" in the v18.4 development-set analyses. That audit covered
the analyses cited in the paper and key_quote fields only. The UQS misreport found here is in the repro N = 5 runs, in a `quote:` field
of S1 (not in a key_quote), so it does not contradict the Methods 6 count, but it shows the same failure class (cross-paper import
on a multi-communication page) that the Stage 0 boundary procedure is meant to prevent.
