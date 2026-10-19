---
title: R3-3 (b) — Stage 4 candidates retained / retracted after verification (re-derived tally)
created: 2026-10-05
status: active
audience: paperA
open_questions: true
---

# R3-3 (b): retained and retracted Stage 4 candidates

Files in this folder:

- `candidates.csv` — one row per candidate (764 rows below the header; 763 counted + 1 annotation row).
- `tally_counts.json` — every count in this memo, per analysis and per record set.
- `build_tally.py` — regenerates both from the primary records. Run `python3 build_tally.py`.
  For each verdict copied from a prose record, the script checks that the cited record line still
  contains a fixed token. If a record is edited or moved, the build fails instead of
  mis-assigning the verdict.

Every count below was recounted from the Stage 4 output files and the verification records. None
was copied from SI or manuscript text. Section 5 lists where the recount differs from numbers already
in the paper.

---

## 1. The verification rule, quoted from the original text

**Methods 2** (`manuscript_A/sections/9_manuscript_en.md` l.98; the submitted version
`submissions/paperA_2026-06-30_Digital_Discovery_v1/.../9_manuscript_en.md` l.98 has the same wording):

> "Hallucinated references are a structural risk, so candidates are retained only after a four-step chain: confidence-tagged generation → Crossref resolution → content check → cross-model divergence detection. Candidates failing any step are retracted. Filling status is assigned against pre-locked Complete/Partial/Minimal/Non-filler criteria. The five-pattern hallucination taxonomy and defence protocol are in SI-11.2."

An earlier, longer version of the same rule survives in a pre-submission draft
(`submissions/.../sections/9_manuscript_en.md.boldbak2` l.641). It is the only text that defines each step:

> "(2) the candidate's bibliographic shell (authors + year + journal + volume + page) is resolved against Crossref; if Crossref returns no record, the candidate is flagged as a probable mode (v) full-citation fabrication and retracted; (3) when Crossref returns a record, the LLM's content description is checked against the actual paper's content … (4) for papers exhibiting high-prior fabrication risk … cross-model parallel retrieval … is used as a structural divergence detector. Candidates surviving all four checks are reported as filling papers; candidates failing any step are either retracted (fabrication) or reported as "not retrieved under the present protocol" …"

**Main text, Results Part 2** (l.200): "The retrieval logs, the four-step verification chain, the WoS query strings and candidate tables, and the locked-criteria document are deposited in SI-4, SI-9, and SI-9.8."

**SI-9.3b** (`SI/output/SI-9.md` l.98): "The four-step verification chain is analyst-supervised …"

**SI-11.1** (`SI/output/SI-11.md` l.20, Stage 4 row): "Four-step verification: (1) LLM candidate generation, (2) Crossref DOI resolution, (3) abstract / full-text content match, (4) cross-vendor parallel retrieval for high-prior-fabrication-risk cases".

**SI-11.2** (heading l.66: "Hallucination patterns (A–E) and the seven-step defence"; l.68; l.80):

> "The four-step retention chain of Methods 2 (confidence-tagged generation, Crossref resolution, content check, cross-model divergence detection) governs whether a Stage 4 candidate is kept; the seven-step defence below is the wider set of pipeline measures in which that chain is embedded (steps 2–4 correspond to it)."
>
> "Seven-step defence applied across the pipeline. Each LLM-suggested specific-paper identification proceeds through a layered verification chain rather than being retained on the basis of LLM output alone: 1. Key-quote anchoring … 2. DOI verification against Crossref … 3. Author verification protocol … 4. Cross-vendor convergence … 5. Multi-run aggregation at the SET level … 6. anchor_status field … 7. Hallucination-rate × model-size empirical heuristic …"

**SI-11.5, step 6** (l.125): "No separate retained/retracted log was kept".

The submitted SI-11.2 (l.66) began "This section expands the hallucination-control summary in Methods §2.X" and had no bridging sentence. The working-tree sentence "steps 2–4 correspond to it" was added later, and it is not accurate (see §6).

---

## 2. Aggregation rule used for this tally

**Unit.** A *candidate* is one publication that a Stage 4 run proposes for an Evidence Pack (EP).

- Part A: one "Filling Onset" or "Filling Establishment" slot in §B (JA: 充填開始点 / 充填確立点) that names a publication. Slots reading "unidentified / 未同定" (89), "same as above / 同上" (51) or a bare label heading (2) are not candidates. A slot that names alternatives counts once, under its first citation.
- Part B: the unit used by the record itself. Named candidates for B1–B4. Candidate identity per run for B5 (the record's §13.3 / §15.3 matrices). Ledger rows for B6. §C recommended-list rows for B7.

**Two checks recorded per candidate.** These come from the verification records only.

- `bib_check`:
  - `resolved`
  - `corrected` (the record names a single real paper, and only authors, pages or DOI needed fixing)
  - `not_resolved` (no such paper)
  - `mismatch` (the tuple points to a different real paper, or the journal, volume and pages are wrong)
  - `insufficient` (the citation is too vague to resolve)
  - `not_checked`
- `content_check`:
  - `fills` (the record judges that the paper's content supports the claimed role)
  - `does_not_fill` (the paper does not contain what the model said it contains)
  - `not_checked`

**Status (strict; this is the Methods 2 rule):**

- **retracted** if `bib_check` ∈ {not_resolved, mismatch} or `content_check` = does_not_fill
- **retained** if `bib_check` ∈ {resolved, corrected} and `content_check` = fills
- **unclassifiable** otherwise. Reasons:
  - no record exists
  - the record checked the bibliography only
  - the citation is too vague to resolve
  - the verdict is keyed to an author–year bin
  - the candidate named in the record is absent from the deposited output

The strict rule requires the content check because Methods 2 retains a candidate "only after" all checks. Cross-model divergence (step 4) is not required: by the draft definition and SI-11.1 it is a trigger applied only to high-risk candidates, not a gate every candidate must pass.

**Bibliographic-only status (lenient, reported alongside):** retained if `bib_check` ∈ {resolved, corrected}, otherwise as above. This is the reading under which a Crossref hit alone counts as "kept".

**Retraction reason classes:**

| Class | Assigned when |
|---|---|
| DOI does not resolve | `not_resolved` |
| metadata mismatch | `mismatch` |
| content does not fill | `does_not_fill` |
| duplicate | never assigned; one duplicate row in B7 is recorded under "unclassifiable" with a note |
| other | never assigned |

---

## 3. Denominators

### Part A — the 37 Stage 4 analyses reported in the paper

Methods 6 (l.137) says "Stage 4 v2, which produced 33 of the 37 Stage 4 analyses reported here … the remaining four analyses … used Stage 3 v4 and Stage 4 v6". The paper never lists the 37. Reconstructed list (it reproduces 33 + 4):

| Group | Analyses | Stage 4 version (header) | Model | Candidates |
|---|---|---|---|---|
| Kumada 1972 multi-run, JA | 6 | stage4-v2-20260416 | Sonnet 4.6 | 84 |
| Kumada 1972 multi-run, EN | 6 | stage4-v2-en-20260419 | Sonnet 4.6 | 87 |
| Murai 1993 multi-run, JA | 6 | stage4-v2-20260416 | Sonnet 4.6 | 67 |
| Murai 1993 multi-run, EN | 6 | stage4-v2-en-20260419 | Sonnet 4.6 | 73 |
| Case studies (Breitenfeld, Cherney, Kumada 1976, Mazet, Molander, Monnereau, Morken, Li, Tamao 2002) | 9 | stage4-v2-en-20260419 | Sonnet 4.6 | 116 |
| Context analyses (Uchino 1970, Terao 2002, Jones 2005, Martin 2007) | 4 | stage4-v6-20260504 | Sonnet 4.6 | 41 |
| **Total** | **37** | | | **468** |

- All 37 files match, by SHA-256, files in the R1 reviewer deposit (`tier_3_stage_outputs/`).
- S0–S2 is v18.4 for all 37.
- Of the 468 candidates, 361 name an author, year and journal, 82 are partial, and 25 are generic, such as "Kochi group EPR studies, 1975–1985".
- Only 3 candidates carry a DOI. All 3 are in the v6 context analyses, and each is marked "推定; 要確認" (estimated; needs checking).

### Part B — every candidate that a verification record covers

| Set | Record (verdicts) | Analyses (S0–S2 / Stage 4 / model) | Unit |
|---|---|---|---|
| B1 | `papers/dev/kumada/cross_model_v182_comparison.md` §5 | Kumada; v18.2 / S4 v3; Sonnet 4.6 (1 run) and GPT-5.5 Thinking with web search (1 run) | named candidates (6 + 9) |
| B2 | `papers/dev/murai/cross_model_v182_comparison.md` §3 | Murai; same design | named candidates (7 + 8) |
| B3 | deposit `tier_5_…/ep03a_wos_llm/verification_log.md` (+ `candidate_check_*.txt`) | Kumada; v17 / S4 v2; Opus 4.7 and GPT-5.4 Thinking | EP-03a candidates (7) |
| B4 | `records/stage4_literature_update_20260419.md` (literature-update memo of 2026-04-19) | Kumada; v17 / S4 v2; GPT-5.4 Thinking | DOI-corrected candidates (2) |
| B5 | `records/kumada_retrieval_depth_verification_extract.md` §10–§16 (retrieval-depth verification record, line-preserving extract) | Kumada; v17 / S4 v2 and v6; Sonnet 4.6 (6 runs + the v2 baseline), "GPT-5.4" (6 runs), Haiku 4.5 (v2 run 1) | candidate identity per run |
| B6 | `papers/dev/murai/multirun/murai_multirun_{candidates,verifications}.tsv` | Murai; v17 / S4 v2 and v6; Sonnet, "Opus 4.8", Haiku 4.5 × 3 runs | ledger rows (125) |
| B7 | `papers/dev/kumada/s4_exemplar_control_2026-08/crossref_adjudication.json` | Kumada; a fixed S0–S3 record (version not stated in the run files) / S4 v6 (arm A) and decontaminated v6 (arm B); Sonnet 4.6 × 5 + 5 | §C list rows (51) |

In total, Part B covers 48 analyses and 295 candidates. None of the 48 is among the 37 Part A analyses.

The B4 and B5 records are prose memos; they are deposited under `records/` (B4 as a copy, B5 as a line-preserving extract of its verification sections, built by `records/make_extracts.py`), so the line numbers below and in `candidates.csv` can be followed.

---

## 4. Tally

### Part A (the 37 analyses)

| | Retained | Retracted | Unclassifiable | Total |
|---|---|---|---|---|
| All 37 analyses | 0 | 0 | **468** | 468 |

Reason for every row: no candidate-level verification record exists for any of the 37 analyses.

- A search of `improvements/`, `papers/` and the response folder found no Crossref or content log that names these files.
- The v6 context analyses record their own status: 25 `Bibliographic verification status: pending` lines.
- This agrees with SI-11.5 step 6: "No separate retained/retracted log was kept."
- 179 of the 468 rows share a first author and year with a candidate that some Part B record resolved. This is shown in the `hint_same_author_year_resolved_in` column as a possible shortcut for re-verification. It is not counted as verification.

### Part B (supporting verification studies)

| Set | Analyses | Retained | Retracted | Unclassifiable | Total | Retained, bibliographic check only |
|---|---|---|---|---|---|---|
| B1 Kumada v18.2, Sonnet | 1 | 0 | 2 | 4 | 6 | 1 |
| B1 Kumada v18.2, GPT-5.5 | 1 | 9 | 0 | 0 | 9 | 9 |
| B2 Murai v18.2, Sonnet | 1 | 0 | 1 | 6 | 7 | 6 |
| B2 Murai v18.2, GPT-5.5 | 1 | 0 | 0 | 8 | 8 | 8 |
| B3 EP-03a audit (Opus 4.7, GPT-5.4) | 2 | 2 | 1 | 4 | 7 | 6 |
| B4 literature update (GPT-5.4) | (same GPT-5.4 analysis as B3) | 2 | 0 | 0 | 2 | 2 |
| B5 retrieval depth, Sonnet | 7 | 1 | 8 | 23 | 32 | 20 |
| B5 retrieval depth, "GPT-5.4" | 6 | 3 | 0 | 39 | 42 | 29 |
| B5 retrieval depth, Haiku | 1 | 0 | 1 | 5 | 6 | 0 |
| B6 Murai multi-run | 18 | 0 | 10 | 115 | 125 | 29 |
| B7 exemplar control | 10 | 0 | 2 | 49 | 51 | 45 |
| **Part B total** | **48** | **17** | **25** | **253** | **295** | **155** |

- **Bibliographic-only reading** of Part B: 155 retained, 25 retracted, 115 unclassifiable.
- **Retraction reasons** (25): 18 DOI does not resolve; 4 content does not fill; 3 metadata mismatch.
- **Retracted, by model:**

  | Model | Retracted |
  |---|---|
  | Sonnet 4.6 | 13 |
  | Haiku 4.5 | 8 |
  | "Opus 4.8" (self-reported) | 2 |
  | Opus 4.7 | 1 |
  | Sonnet (no version stated) | 1 |

- **Retained after a metadata correction**: 2 (Tamao–Zembayashi–Kiso–Kumada 1973; Chen et al. 2019).
- **Unclassifiable reasons** (253):

  | Reason | Rows |
  |---|---|
  | Bibliographic check only | 138 |
  | Murai verdict keyed to an author–year bin that holds several citation shells | 75 |
  | Named in the record but no verdict | 22 |
  | Candidate in the record or ledger but absent from the deposited output | 11 |
  | Citation too vague | 7 |

**The 25 retracted candidates** (row ids refer to `candidates.csv`):

| Row | Analysis | Model | Candidate as proposed | Reason | Record |
|---|---|---|---|---|---|
| 469 | Kumada v18.2 S4 v3 | Sonnet 4.6 | Tamao, Sumitani, Hayashi, Kumada, JACS 1976 | does not resolve | cross_model (Kumada) l.110 |
| 471 | Kumada v18.2 S4 v3 | Sonnet 4.6 | Nagase, Hayashi, Kumada, Tetrahedron Lett. 1973/74 | does not resolve | l.112 |
| 487 | Murai v18.2 S4 v3 | Sonnet 4.6 | Chatani, Fukuyama, Kakiuchi, Murai, JACS 1998, 120, 11522 ("Rh-catalysed") | content does not fill (the paper is Ru₃(CO)₁₂) | cross_model (Murai) l.46 |
| 500 | Kumada v17 S4 v2 | Opus 4.7 | Yamamoto, Kohara, Yamamoto, BCSJ 1978, 51, 2091 | metadata mismatch (triple mismatch) | verification_log l.49 |
| 525–527 | Kumada v17 S4 v6 (pilot 1) | Sonnet 4.6 | Komiya 1983 (dmpe ≠ dppe); Tamao 1972 JACS 94, 9268 (wrong topic); Smith–Kochi 1976 (Fe, not Ni) | content does not fill | B5 record l.634–636 |
| 529–532 | Kumada v17 S4 v2/v6 (4 runs) | Sonnet 4.6 | "Corriu/Masse J. Organomet. Chem. 1973–75 continuation" | does not resolve | B5 record l.638 |
| 533 | Kumada v17 S4 v6 (pilot 1) | Sonnet 4.6 | Yamamoto, Yamamoto, Ikeda, BCSJ 1971, 44, 1505 | does not resolve | B5 record l.274 |
| 587 | Kumada v17 S4 v2 run 1 | Haiku 4.5 | Tamao et al., JACS 1976, 98, 4173 | metadata mismatch | B5 record l.1127 |
| 628, 664–665, 698, 706, 709, 711, 713, and two Haiku v2 run 2/3 rows | Murai v17 S4 v2/v6 | Sonnet, "Opus 4.8", Haiku 4.5 | (see CSV) | does not resolve | murai_multirun_verifications.tsv |
| 721 | Kumada S4 v6, arm A run 3 | Sonnet 4.6 | Zembayashi, Tamao, Hayashi, Kumada, Tetrahedron Lett. 1977, 18, 4097 | metadata mismatch (page) | crossref_adjudication.json l.79 |
| 741 | Kumada S4 v6 decontaminated, arm B run 10 | Sonnet 4.6 | Tamao, Zembayashi et al., J. Organomet. Chem. 1976, 117, 361 | does not resolve | crossref_adjudication.json l.105 |

**The 17 strictly retained candidates:**

- 9 GPT-5.5 candidates on Kumada (B1).
- Parshall 1974 and Anderson–Jones–Vicic 2004, both checked against the PDF (B3).
- Tamao–Zembayashi 1973 and Chen 2019 (B4).
- Knochel 1995 (B5, Sonnet).
- Tamao–Kiso–Sumitani–Kumada 1972 in 3 GPT runs (B5).

The B1 content checks were made from titles and metadata, not from full text. Only Parshall 1974 and Anderson 2004 were checked against the paper itself.

### Overall

| | Retained | Retracted | Unclassifiable | Total |
|---|---|---|---|---|
| Part A (37 analyses) | 0 | 0 | 468 | 468 |
| Part B (48 analyses) | 17 | 25 | 253 | 295 |
| **All 85 analyses** | **17** | **25** | **721** | **763** |

The overall row adds two different populations. It should not be read as a retraction rate. A rate needs a population in which every candidate was checked, and no such population exists. The closest is B7: all 51 candidates were checked against Crossref (bibliography only). In B7, 2 candidates failed and 4 could not be resolved.

---

## 5. Mismatches with numbers and statements already in the paper or in the records

1. **Methods 2 vs the records.** Methods 2 says candidates "are retained only after a four-step chain". For the 37 analyses the paper reports, no candidate-level record exists (468 candidates, 0 checked). The chain was applied only in side studies (Part B), and there mostly at the bibliographic step. SI-11.5 step 6 ("No separate retained/retracted log was kept") agrees with the records. Methods 2 does not.

2. **SI-9 (v) and SI-9 l.124: Kumada Sonnet "2/3 (67%)".** The recount matches the record: 2 not resolved out of the 3 checkable predictions. The 3 checkable predictions come from 6 examined, and the output has 13 proposal slots. The SI does not state this denominator.
   - **Murai "0/7 full, 1/7 partial".** The recount matches. Under the Methods 2 rule, however, the "partial" case (Chatani 1998, described as Rh-catalysed; the paper is Ru₃(CO)₁₂) fails the content check and should be counted as **retracted**. The SI calls it a partial hallucination and does not say whether it was kept.
   - **GPT-5.5 "9/9, 8/8".** The recount matches at the bibliographic level. The Murai record has no content judgement.

3. **Methods 6, exemplar control** ("one page-number error in the exemplar-carrying arm (25 candidates) and one unresolvable … coordinate in the decontaminated arm (26 candidates)"). The recount matches: 25 and 26 §C rows, each matched to its adjudication key. The text "Every candidate from all ten runs was then adjudicated" omits that 4 candidates (2 per arm) could not be resolved either way (INCOMPLETE/UNVERIFIABLE). One of them is a duplicate row ("上記と同一"). Also, arm B outputs carry the same header tag as arm A (`stage4-v6-20260504`), so the arm can be identified only from the file name.

4. **SI-6.7 composite list: 14 papers kept, 1 retracted (Yamamoto 1978).** The records support 4 of the 14 as retained under the strict rule: Parshall 1974, Anderson–Jones–Vicic 2004, Tamao–Zembayashi 1973 and Chen 2019.
   - Bibliography only: Morrell–Kochi 1975, Dawson 2020, Jones–Vicic 2006. These are marked "Pending" in verification_log l.38–40.
   - No record for these analyses: Kiso–Tamao–Kumada 1973, Tamao 1976 BCSJ (resolved only in other records), the Kochi textbook / Whitesides, Tamao 1982 *Tetrahedron*, Terao–Kambe 2002, Phapale 2009.
   - Yamamoto–Kohara–Yamamoto 1981 was not proposed by any Stage 4 run. It was added by the analyst after the retrieval check, and SI-6.7 says so.

5. **SI-9.3b reference numbers.** "Refs 23, 34 (middle-author substitution)" and "Ref 33 (full author-list replacement)" use the submitted numbering: 23 = Tamao–Zembayashi 1973, 33 = Chen 2019, 34 = Dawson 2020. In the revised reference list these are refs 31, 41 and 42.
   - No record documents a middle-author error for Dawson 2020. The only Dawson discrepancy on record is a page number (8002), and that error was introduced by the analyst.
   - Other records number the same corrections differently: the literature memo l.116 has "Refs 26/31"; the pre-submission draft has "Refs 26, 30, 31 corrected"; `paperA_pre_submission_qa_audit_response_20260511.md` l.75 has "4 Pattern E corrections (Refs 26, 30, 31)".

6. **Errors attributed to GPT-5.4 that are not in the deposited GPT-5.4 output.** The literature memo says GPT-5.4 named "Sumitani" as third author of the 1973 *J. Organomet. Chem.* paper and gave Chen 2019 a fabricated author list and "141, 18". The deposited `kumada_v17_gpt54thinking_s4.md` names only "Tamao et al." (l.57) and "Chen et al." (l.103), with correct links. The corrected errors cannot be traced to that file.

7. **Analyst transcription errors inside the B3 verification record.** `llm_candidates_ep03a.md` and `candidate_direct_queries.md` carry three wrong values. The model's output contains none of them, and the WoS exports deposited alongside show the correct values:

   | Paper | Value in the record | Problem | Correct value |
   |---|---|---|---|
   | Parshall 1974 | DOI 10.1021/ja00815a017 | resolves to Gleicher et al. (`candidate_check_1`) | ja00815a009 |
   | Anderson 2004 | DOI 10.1021/ja0488380 | resolves to Hong/Grubbs (`candidate_check_4`) | ja0483903 |
   | Dawson 2020 | p. 8002 | wrong page | p. 3044 (`candidate_check_6`) |

8. **B5 record vs files.**
   - ~~The §15.3 matrix places Morrell–Kochi 1975 in GPT runs v2 R3 and v6 R3. Neither file contains it.~~ **Corrected 2026-10-05:** both files contain it, spelled "Morell" (one r; v6 R3 l.67 gives the correct bibliography and DOI 10.1021/ja00858a011). The search pattern was too narrow (`Morrell`); it is now `Mor{1,2}ell`. The record's 5/6 is correct. Strict counts are unchanged; the lenient count moves from 153/25/117 to 155/25/115. Pattern-based searches for author names should allow for spelling variants that the models themselves produce.
   - The same memo reports Hayashi–Tajika 1976 (JACS 98, 3718) as unconfirmed (§11.6, l.520) and later as confirmed (§13.2, l.617).

9. **B6 Murai ledger vs files.**
   - The summary's 101 real / 24 fabricated is reproduced only by joining verdicts on author–year bins. 18 bins hold more than one citation shell. Once verdicts are tied to a single shell, 10 retractions and 29 bibliographic passes can be attributed; 75 rows cannot. The repository's `RECOUNT_NOTE_20260829.md` already withdraws these values. Paper A does not cite them.
   - In addition, 8 of the 14 ledger candidates for Sonnet v2 run 1 (for example Satoh 2011 *Chem. Rev.*, marked fabricated) do not appear in the deposited run file. 3 more ledger rows in other runs are also absent.

10. **Model identities.**
    - 3 of the 6 "GPT-5.4 Thinking" retrieval-depth runs record `model_info: gpt-5.5-thinking` or `GPT-5.5 Thinking` in their headers: v2 run 2, v6 run 1 and v6 run 3. SI-6, SI-11.2 and the B5 record call all six GPT-5.4.
    - The Murai multi-run "opus48" files self-report "Claude Opus 4.8".
    - Five of the six Murai Sonnet files give no version ("Claude Sonnet (current snapshot)").

11. **"37 analyses."** The reconstructed list reproduces 33 + 4. The paper should list them; see the proposed SI table below.

12. **Methods 2 says no external database or API is queried.** The two GPT-5.5 verification arms (B1/B2) used chat web search. So did the GPT runs whose output carries ChatGPT `utm_source` links. Their 0% fabrication rate is therefore not a parametric-recall result. SI-9 l.94 says this; Methods 2 does not.

---

## 6. Step-count discrepancy: main text "four steps", SI "seven steps"

Texts: quoted in §1. What does not match:

- The four steps in Methods 2 are generation, Crossref resolution, content check and cross-model divergence. Steps 2–4 of the SI-11.2 list are DOI verification, author verification and cross-vendor convergence. So "steps 2–4 correspond to it" (SI-11.2 l.68) is not correct:
  - the content check has no counterpart in the seven-step list;
  - author verification is a sub-check of Crossref resolution;
  - confidence-tagged generation is not in the list.
- Seven-step items 1, 5 and 6 (key-quote anchoring, multi-run SET aggregation, anchor_status) apply to Stage 0–3 outputs, not to Stage 4 candidates.
- Item 7 is a model-choice heuristic, not a check.
- SI-11.1 l.20 makes step (4) conditional ("for high-prior-fabrication-risk cases"). Methods 2 lists it as a step every candidate passes.

**Proposed unified wording.** Use one number, four, and stop calling the SI list "steps".

- *Methods 2, replace the two sentences from "Hallucinated references …" to "… are retracted.":*
  > "Hallucinated references are a structural risk. A candidate is kept only if it passes three checks: (1) its bibliographic record (all authors, year, journal, volume, page) resolves to one paper in Crossref; (2) that paper's abstract or full text contains what the model said it contains; and (3) its filling status meets the pre-locked Complete/Partial/Minimal/Non-filler criteria. For candidates with high fabrication risk (older papers, dense author networks), a second model's independent retrieval is used to flag citations that only one model produces. A candidate that fails check (1) or (2) is retracted. These checks were applied in the verification studies listed in SI-9.10; the per-EP filling labels in the 37 Stage 4 analyses themselves were not checked candidate by candidate and are reported as exploratory (Results Part 2)."

  This changes "four-step chain" to "three checks plus one trigger". If the authors prefer to keep "four", the minimal edit is to keep the Methods sentence and define the steps as above, with step 4 described as a trigger.
- *SI-11.2:* retitle to "Hallucination patterns (A–E) and pipeline safeguards". Replace "seven-step defence" (l.66, l.80, l.92, and the main-text SI list at l.655) with "safeguards". Split the list into:
  - **Stage 4 candidate checks**: the Methods 2 checks, with the author-list check folded into Crossref resolution.
  - **Upstream safeguards on Stage 0–3 outputs**: key-quote anchoring, multi-run SET aggregation, anchor_status.
  - **Model choice**: the model-size heuristic.

  Delete "steps 2–4 correspond to it".
- *SI-11.1 l.20, SI-9.3b l.98, Results l.200:* change "Four-step verification" / "four-step verification chain" to "the Stage 4 candidate checks (Methods 2)".

---

## 7. Proposed SI-9 text (new SI-9.10)

> **SI-9.10 Retained and retracted Stage 4 candidates**
>
> *Rule.* A Stage 4 candidate is *retained* when its bibliographic record resolves to a single paper in Crossref (after correcting author or page errors where the record identifies the intended paper) **and** the paper's content was checked and found to support the claimed role. It is *retracted* when no such paper exists, when the citation points to a different paper, or when the paper does not contain what the model attributed to it. All other candidates are *unclassifiable*. Every candidate is listed, with the Stage 4 file and line that proposed it and the record and line that holds the verdict, in `tier_4_classification_tables/stage4_candidates_R1/candidates.csv`; the counts are regenerated by `build_tally.py`.
>
> *The 37 Stage 4 analyses reported in the paper* (24 Kumada/Murai multi-run analyses and 9 case-study analyses under Stage 4 v2; 4 context analyses under Stage 4 v6; all Sonnet 4.6 with S0–S2 v18.4) propose 468 candidates. None of them was verified individually: 0 retained, 0 retracted, 468 unclassifiable. The per-EP filling labels drawn from these analyses are therefore exploratory; the claims of non-detection in the main text rest on the locked Web of Science audit (SI-9.8, SI-9.9), not on this layer.
>
> *Verification studies.* Candidate-level verdicts exist for 295 candidates from 48 other Stage 4 runs on Kumada 1972 and Murai 1993 (S0–S2 v17 or v18.2, and the fixed S0–S3 record of the exemplar control; Stage 4 v2, v3 or v6; Sonnet 4.6, Opus 4.7, Haiku 4.5, a self-reported "Opus 4.8", GPT-5.4 Thinking and GPT-5.5 Thinking). Of these, 17 are retained and 25 retracted (18 non-existent papers, 4 papers whose content does not match the model's description, 3 citations pointing to the wrong paper). 253 are unclassifiable, mostly because only the bibliographic record was checked (136) or because the verdict could not be tied to a single citation (75). Counting a Crossref match alone as retention gives 153 retained, 25 retracted and 117 unclassifiable. The retracted candidates come from Sonnet 4.6 (13), Haiku 4.5 (8), Opus (3) and Sonnet without a stated version (1); none comes from the two GPT-5.5 runs with web search. Two retained candidates (Tamao–Zembayashi–Kiso–Kumada 1973; Chen *et al.* 2019) needed author or volume corrections.
>
> These counts describe the checks that were made, not a fabrication rate. Only one study checked every candidate it produced: the exemplar-control runs, 51 candidates checked against Crossref, with 2 failures and 4 that could not be resolved.

(Before using this text, the authors should decide whether to re-run the content check on the 138 bibliography-only candidates, or on the 179 Part A candidates that share an author and year with a resolved paper. Either would change the numbers above.)

---

## 8. Proposed response-letter sentence (R3-3, "Retracted candidates")

> *Retracted candidates.* The referee is right that the paper gave a rule but no list. We have now listed every Stage 4 candidate and its status (SI-9.10; `stage4_candidates_R1/candidates.csv`, regenerated by a deposited script). This showed that the verification chain had not been applied to the 37 Stage 4 analyses the paper reports: their 468 candidates were never checked one by one, and Methods 2 now says so and calls the per-EP filling labels from these analyses exploratory. Candidate-level checks exist for 295 candidates from 48 supporting runs: 17 were retained, 25 retracted (18 non-existent, 4 content mismatches, 3 wrong citations), and 253 could not be classified, mostly because only the bibliographic record was checked. We also unified the description of the checks: the main text said "four steps" and SI-11.2 "seven"; Methods 2 now defines the Stage 4 checks once, and SI-11.2 describes the remaining items as pipeline safeguards rather than further steps.

Short version, if space is tight:

> We now list all Stage 4 candidates with their status (SI-9.10, deposited CSV). The 468 candidates of the 37 reported analyses were never checked individually, and Methods 2 now says so. In 48 supporting runs, 17 candidates were retained, 25 retracted and 253 could not be classified. The main text and SI now describe the same set of checks.

---

## 9. Ambiguities and limits of this recount

- **Choosing a strict or lenient status.** The strict rule follows Methods 2 literally. Most records checked bibliography only. If the authors decide that a Crossref match is enough, use the lenient column. Either way, the paper should state which rule it uses.
- **"Content does not fill" for Chatani 1998 (B2).** The paper exists, but the model misdescribed it (Rh vs Ru). The record calls it a "partial hallucination" and records no decision. It is counted here as retracted, following the content-check definition in the draft Methods.
- **Self-flagged uncertain citations counted as retracted.** The "Corriu continuation" rows (B5, 4 runs) are counted as retracted under the record's group-level verdict "不在" (does not exist). The model had itself flagged the citation as uncertain ("書誌未確定").
- **Haiku v2 run 1 (B5).** Five candidates are recorded only as "likely fabricated", with no resolution check. They are counted as unclassifiable, not retracted.
- **Part A parsing is heuristic** (regular expressions over §B). Spot checks of 25 random rows found correct slot and author extraction. Some "generic" rows describe a group of papers rather than one. A slot that names alternatives counts once.
- **B5 counting.** Candidate presence per run in B5 is taken from the record's own matrices. The script checks that each named candidate occurs in the run file and lists the 2 that do not.
- **B4 and B5 records.** Deposited under `records/` (2026-10-16), so the `verification_record` column can be followed for all 82 rows. The B5 extract is taken from the memo version the tally was built against; a note added to the memo later on 2026-10-05 is not included (it concerns the Hayashi–Tajika entry, whose confirmation §13.2 already records).
- **No new checks were run.** No Crossref lookup or content check was performed for this recount. Every verdict comes from an existing record.
