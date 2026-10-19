# Tier 2 — Input Metadata

**Spec (SI-11.11)**: Corpus paper list with DOIs, retrieval dates, PDF sources, and per-paper execution dates for the 21-paper Paper A corpus.

## Files

- **`paperA_21_paper_corpus_manifest.csv`** — the 21-paper Paper A corpus (revised 2026-09-28 in response to review):
  - 2 development-set papers (Kumada 1972, Murai 1993)
  - 10 Heck **refinement-set** papers (hom1/2, het1/2, comp1/2, app1/2, scr1/2). They were used to refine the prompts from v15 to v17 and are not a held-out test set; their DOIs are listed, consistent with SI-11.17
  - 1 Layer-1 historical anchor (Tamao 1976 BCSJ "Full Paper I")
  - 7 Layer-2 papers (Monnereau 2009, Breitenfeld 2014, Cherney 2015 [review], Tellis–Molander 2016, Eno–Morken 2016, Poisson–Mazet 2021, Li 2024)
  - 1 Tamao 2002 retrospective mini-review (Stage 2F integration anchor)
- Columns: `folder` (the paper's folder name in the project repository, including two legacy spellings: `molken2016` = Morken, `pengfei2024` = Li; six of these names differ from the deposited directories), `deposit_path` (added 2026-10-17: the directory of the paper's records in Tier 3 of the reviewer version), `public_path` (the redacted copy of those records in Tier 8 of this cut, or "reviewer version only"), `canonical_id` (first-author-year), bibliographic fields and `title_crossref` taken from Crossref on 2026-09-28, `bib_key` (key in the manuscript's BibTeX file; stable across renumbering).
- Corrections relative to the version deposited with the submission: two placeholder DOIs (`10.1021/jacs.6bXXXXX`, `10.1021/jacs.1bXXXXX`), one empty DOI (Li 2024) and one DOI that does not resolve (Tamao 2002, `…02)01209-4` → `…02)01159-2`) were replaced; the reference-number column, which did not match the submitted manuscript, was replaced by `bib_key` (a column `md_reference_number`, whose numbers followed an earlier draft, was removed in version v4 of this record); the test-set papers are no longer anonymised.

## Excluded from this tier (cleaned 2026-06-25)

- **`corpus/corpus_paper_list.csv`** — Parent ~1,113-paper Heck-reaction corpus from which the 10-paper refinement set was sampled. The 10 refinement-set papers in `paperA_21_paper_corpus_manifest.csv` are the relevant subset; the parent corpus is not separately deposited because the 21-paper manifest above already documents the actual evaluation set.
- **`uqs_new_corpus_roster.csv`** — the phys_chem / spectroscopy roster. The submitted manuscript cited a 98-paper pilot drawn from this corpus; in the revision that pilot is no longer used as evidence (author decision, 2026-09-28), and the roster is not part of this deposit.

## Per-paper execution dates

Per-paper Stage 0–Stage 4 execution dates are encoded in the individual output filenames under `tier_3_stage_outputs/` *(reviewer version only; redacted Markdown copies under `tier_8_redacted_public_raw_outputs/`)*. Aggregate execution-date ranges per phase are summarised in `../zenodo_manifest.md` §3.
