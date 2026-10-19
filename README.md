> **Public cut (R1, 2026-10-17).** This repository is the public, quotation-redacted cut of the Paper A deposit.
> Verbatim quotations from the analysed papers are replaced by `[REDACTED: …]` markers that point to the source paper.
> Redacted are: (1) in the analysis outputs, every quoted span inside a `quote:` / `key_quote:` / `source_text` field,
> whatever its length — including the second and later quotations of a field and quotations inside a bracketed note —
> and every paper-boundary quote; also inside JSON run logs; in JSON files and tables, the whole value of a `quote` /
> `key_quote` / `source_text` key, whatever its length. Text in a quote field that is not between quotation marks (the
> model's own description, e.g. `quote: [no statement of replication appears in the main text]`) is not a quotation and
> falls under rules (2) and (3) only; template placeholders such as `"<exact text from the paper>"` are kept.
> (2) Any other quoted span of ten or more words whose words mostly come from the text of an analysed paper, also compared
> character by character in reading order, so that OCR word breaks, interleaved columns and dropped fi/fl ligatures do not
> hide a quotation, and a span that is not an E-proposition is also redacted when at least 80% of its letters and digits
> lie, in order, in one passage of such a text (shortened or retyped quotations; symbols written out as words, such as
> "approximately" for "≈", are also compared without those words); a span that these comparisons find in our own prompts
> is kept; (3) any run
> of ten or more consecutive words shared with the text of an analysed paper, compared after normalising ligatures,
> hyphenation, every dash variant and case, also inside the string literals and comments of scripts (`.py`, `.sh`; the
> code itself is unchanged); a run must also span ten written (whitespace-separated) words, and a dash between two digits
> separates them, as in the text layers. Runs of numbers and punctuation (fewer than six words that contain a letter) are not
> matched; in CSV / TSV files the rules apply cell by cell, so every row keeps its columns. "Analysed paper" means the
> text layers of the PDFs (with SI files) of the development set, the refinement set, the historical case study, the
> context analyses and the held-out set, and of the ChemOntology paper (Nath et al. 2026) that the application-direction
> notes cite; the PDFs themselves, full texts and page scans are not included. In those notes, the passages quoted from
> Nath et al. 2026 are replaced by paraphrases that keep their page / figure locators. Quotations of
> other papers are redacted only where rule (1) applies.
> **Kept by design**: shorter quotations (fewer than ten words) outside the quote fields, which serve as location
> anchors; model-written paraphrases of a paper's title or claims — the quoted E-propositions (the
> `confirmed_english_propositional` statements of Stage 2 and tables that list them) with fewer than ten contiguous words of
> the paper's text are not source quotations; bibliographic facts (titles of eight or more words — Web of
> Science titles from four — author lists, journals, years, DOIs, and citation cells of bibliographic table
> columns such as `cand_text`) — a run that also holds prose of the paper is redacted even if a citation sits inside it;
> and our own text, including quotations of our own manuscript and the raters' judgements. Our own prompts (Tier 1,
> 86 files; SI-7 lists the SHA-256 of 29 of them, and those match), the SI and the bibliographic tables are copied
> unchanged, as is every file in which nothing was redacted. Chat-service conversation links are removed. **Tier 8**: the
> 764 files that the reviewer version's Tier 8 already held are its earlier redaction with these rules applied on top;
> that redaction (`redact_for_tier8.py`) had replaced every quoted span of ten or more words, whoever wrote it, and those
> markers are kept. The 48 Tier 8 files added by this build (redacted copies of Tier 3 Markdown outputs that had no
> Tier 8 copy) are redacted under the rules above only, so model-written quoted spans are kept there. Since 2026-10-17 the
> reviewer version holds the same Tier 8 files.
> Single-quoted spans and quotations cut off inside a table cell are examined like other quoted spans, a span's length is
> counted in written words (a Greek letter such as β counts as a word), and in quote-adjudication tables the quoted string
> of every row not classed as the model's own words (class A) is redacted when it has ten or more words.
> **Web of Science records** (the tagged `.txt` exports in Tier 5): only the bibliographic identification fields are kept
> (PT, TI, SO, PY, VL, IS, BP, EP, DI, UT and the record separators FN, VR, ER, EF); all other fields (authors' full names,
> addresses, researcher identifiers, ORCIDs, e-mail addresses, ISSNs, dates, PubMed IDs, etc.) are removed. The reviewer
> version keeps the full records. `parse_wos.py` and `analyze_variants.py` read the author field, so their author-based
> output is complete only on the reviewer version.
> **Scripts that depend on quoted text** give their published results only on the reviewer version: the SI-6.10
> recomputation (`tier_7_…/classification_concordance/si6_10_datum_jaccard.py`, which compares the quoted passages of the
> deposited runs, now redacted here) and the built-in self-test of `classification_concordance.py`; and the scoring scripts
> of the revision studies (§0 item 15), which read redacted run records or the Tier 3 outputs: in this cut only the
> aggregation of the raters' verdicts (`aggregate_adjudication*.py`, `aggregate_srg_mapping.py`) and the rating keys reproduce.
> Not included: the full stage outputs (Tier 3), the reviewer-only raw logs (Tier 9) and the per-reference catalogue.
> The reviewer version, with the full outputs, is the Zenodo record with concept DOI 10.5281/zenodo.23437447, cited in the paper; its
> files are restricted to the editor and reviewers until acceptance. Build:
> `scripts/build_paperA_R1_public.py` (with `scripts/redact_source_ngram_runs.py`) in the project repository.
> The documentation files below still refer to Tier 3, Tier 9 and the per-reference catalogue; each such reference is
> marked *(reviewer version only)*. `CHECKSUMS.sha256` covers the files of this cut; `MANIFEST.csv` lists every file of
> the reviewer version with its `public_cut` status (here, unchanged = byte-identical; here, redacted; here, WoS export
> reduced; here, public-cut notes added; or reviewer version only) and, for files present here, their `public_sha256`.
> The status is derived from the bytes: "unchanged" only where the SHA-256 equals that of the reviewer version.

# Zenodo Deposit — *Mapping Structured Absences in Scientific Papers* (UQS Methodology)

> **Internal note**: Folder `zenodo_deposit_paperA/` retains the portfolio-internal codename "Paper A" for repository-organisation purposes. External references (Zenodo title, GitHub repo, citation strings) use the manuscript title directly without the "Paper A" label.

**Paper**: *Mapping Structured Absences in Scientific Papers: An Auditable LLM-Assisted Workflow Demonstrated on Cross-Coupling Chemistry* (Ono, Yoshioka, Taketsugu — under revision at *Digital Discovery*, RSC; first-round revision, R1)

**Corresponding authors**:
- Yuriko Ono — yono@sci.hokudai.ac.jp
- Tetsuya Taketsugu — take@sci.hokudai.ac.jp

**Zenodo record**: concept DOI 10.5281/zenodo.23437447, cited in the paper's Data Availability statement; it resolves to the latest version of the record. Versions of this record: v1 (10.5281/zenodo.23437448) and v2 (10.5281/zenodo.23446545; it corrected the DOI statements of v1) hold the package as built on 2026-10-16; v3 (10.5281/zenodo.23466681) adds the corrections listed in `REVISION_R1.md` (item of 2026-10-19); v4 (10.5281/zenodo.23469269) corrects the reference numbers of the revised paper and the corpus manifest (second item of 2026-10-19); v5 (this version) corrects one reference number that v4 missed (third item of 2026-10-19). It is the Zenodo record of the reviewer version of this cut (first-round revision, R1), published with its files restricted to the editor and reviewers until acceptance; this public cut is released on GitHub. The deposit shared with the submitted manuscript was a different Zenodo record (21026938), which was never published: it was shared through a preview link, and its reserved DOI 10.5281/zenodo.21026938 was never registered. **Licence**: CC BY 4.0 (`LICENSE`).

**Versions**: submitted version packaged 2026-06-29 (manuscript submitted 2026-06-30); correction record added 2026-08-31; first-round revision (R1) packaged 2026-09-28; **final R1 version packaged 2026-10-17** — see `REVISION_R1.md` for every change relative to the submitted version.

---

## §0 How to audit this paper

1. **Integrity.** From the archive root run `shasum -a 256 -c CHECKSUMS.sha256`. `MANIFEST.csv` lists every file with its SHA-256, size and top-level folder (`top_level`, i.e. the tier or supplementary directory).
2. **Prompts.** `tier_1_prompt_versions/` holds the prompts of the deposited outputs (86 files), except the Unpack prompts behind the two plain-language explanations of Kumada 1972 (`kumada_v184_sonnet_unpack_v1.md`, `_v3.md` in Tier 3; no claim of the paper uses them) and the overwritten v3 text of the Turn 4 textbook pilot (see Scope hygiene). SI-7 lists the SHA-256 of 29 of them (the prompts it tabulates), and those 29 files match it; `MANIFEST.csv` gives the SHA-256 of every Tier 1 file. The analysis configuration is S0–S2 = v18.4 (Stage 2 EN), Stage 3 = v2 EN, Stage 4 = v2 EN, Stage 2F = v6 / v7 / v7.1; the Japanese-language multi-run cells used the JA versions of Stages 2–4, the four context analyses and the R1 control runs on Kumada 1972 used the JA Stage 2 (`prompt_stage2_v184.md`, SI-7 row 23), the context analyses with Stage 3 v4 / Stage 4 v6, and the refinement set used v17 (see `RUNNING.md`).
3. **Corpus.** `tier_2_input_metadata/paperA_21_paper_corpus_manifest.csv` lists the 21 papers with Crossref-verified DOIs; `public_path` gives the redacted copy of each paper's records in this cut (Tier 8), `deposit_path` the directory of the unredacted records in Tier 3 of the reviewer version, and `folder` the folder name of the project repository (six differ, e.g. `kumada1972` → `dev_set/kumada/`).
4. **Per-paper outputs.** `tier_3_stage_outputs/` *(reviewer version only; redacted Markdown copies under `tier_8_redacted_public_raw_outputs/`)* (full, with verbatim key-quote excerpts; reviewer access) and `tier_8_redacted_public_raw_outputs/` (verbatim source-paper quotations replaced by `[REDACTED: …]` markers that point to the source paper or to the unredacted copy; see Raw-output redaction policy).
5. **Numbers in the paper.** The multi-run values (Top-3 EP SET inclusion frequency, VQ-hierarchy inversion counts, 11-paper counts) are re-derivable from `tier_4_classification_tables/reaggregation_R1/`: the scripts read the per-run records and write the CSVs cited in SI-3. *(Reviewer version only: the `reaggregate_*.py` scripts read the per-run records in Tier 3, which this cut does not hold, so they do not run here; the CSVs they wrote are included.)*
6. **Bounded non-detections.** `tier_5_retrieval_logs/` holds the locked criteria, query strings and candidate tables of the Web of Science audit; see `WOS_EXPORT_STATUS.md` there for the state of the raw exports.
7. **Models.** `zenodo_manifest.md` §1 lists every model whose outputs are deposited, with the identifier recorded in the outputs and the role in the paper.
8. **Control experiments of the revision.** `papers/` at the archive root carries the four control experiments reported in Methods 6 of the revised manuscript, at the `papers/...` paths the manuscript cites.
9. **Revision studies after 2026-09-28.** `01_response/` carries the pre-registrations, scripts, rating records and results of the studies added in the revision (expert rating, SI-8.7; held-out set and single-prompt baselines, SI-11.20; SRG-root mapping and Haiku 4.5 replication, SI-6.10; candidate tallies, SI-9.10), at the `01_response/...` paths the SI cites; their run outputs are under `papers/`. `REVISION_R1.md` lists every addition.
10. **Supporting Information.** `supporting_information/SI_R1.pdf` is the revised SI as submitted (the manuscript states that the full texts of SI-2 to SI-6 are also archived here).
11. **Project paths in the SI.** The SI cites files by their path in the project repository. In this package the run records of the 21 corpus papers are under Tier 3, and the revision studies keep their paths:

    | Project path (as cited) | In this package |
    |---|---|
    | `papers/dev/kumada/…` (Stage 0–4 outputs, `gpt54thinking/`, `gpt55thinking/`, `gemini3flash/`, `pilot_retrieval_depth/`, `cross_model_v182_comparison.md`) | `tier_3_stage_outputs/dev_set/kumada/…` *(reviewer version only; redacted Markdown copies under `tier_8_redacted_public_raw_outputs/`)* |
    | `papers/dev/murai/…` (Stage 0–4 outputs, `gpt55thinking/`, `multirun/`, `cross_model_v182_comparison.md`) | `tier_3_stage_outputs/dev_set/murai/…` *(reviewer version only; redacted Markdown copies under `tier_8_redacted_public_raw_outputs/`)* |
    | `papers/dev/kumada/{baseline_R1_2026-09, b2_stage3_R1_2026-09, haiku45_*, decon_2026-07, repro_2026-07, s4_exemplar_control_2026-08}/` | same path under `papers/` |
    | `papers/dev/{uchino,terao2002,jones2005,martin2007}/` | `tier_3_stage_outputs/context_analyses/{uchino1970,terao2002,jones2005,martin2007}/` *(reviewer version only; redacted Markdown copies under `tier_8_redacted_public_raw_outputs/`)* |
    | `papers/test/{id}/` | `tier_3_stage_outputs/test_set/{id}/` *(reviewer version only; redacted Markdown copies under `tier_8_redacted_public_raw_outputs/`)* |
    | `papers/ep/kumada1972/{paper}/` | `tier_3_stage_outputs/ep_historical_case_study/{paper}/` *(reviewer version only; redacted Markdown copies under `tier_8_redacted_public_raw_outputs/`)* (`molken2016` → `morken2016`, `pengfei2024` → `li2024`, `kumada1976b` → `kumada1976b_tamao_bcsj_layer1_anchor`) |
    | `papers/ep/kumada1972/kumada1972_*_s2f*.md`, `kumada1972_v17_sonnet_s3.md` | `tier_3_stage_outputs/stage2f_integration_outputs/` *(reviewer version only; redacted Markdown copies under `tier_8_redacted_public_raw_outputs/`)* |
    | `papers/ep/kumada1972/{yamamoto1978,yamamoto1981}/` | `tier_3_stage_outputs/citation_integrity_cases/` *(reviewer version only; redacted Markdown copies under `tier_8_redacted_public_raw_outputs/`)* |
    | `papers/ep/discussion/tamao2002/` | `tier_3_stage_outputs/ep_historical_case_study/tamao2002_minireview/` *(reviewer version only; redacted Markdown copies under `tier_8_redacted_public_raw_outputs/`)* |
    | `papers/refs/` | `per_reference_catalogue/refs_catalogue_29_of_31/` *(reviewer version only)* |
    | `papers/paperA_heldout_R1/`, `papers/_audits/`, `papers/ablation_provenance/` | same path under `papers/` |
    | `manuscript_A/DigitalDiscovery_R1/01_response/…` (e.g. in `verification_record` of the SI-9.10 tally) | `01_response/…` |
    | `zenodo_deposit_paperA_reviewer_R1_20260928/…` (the package this version was built from) | the same path without that prefix, e.g. `tier_5_retrieval_logs/…` |
    | `scripts/classification_concordance.py` (SI-6.10) | `tier_7_aggregation_scripts_and_methodology_evolution/classification_concordance/` |
    | `scripts/anchor_matcher.py`, `scripts/specifics_matcher.py` (SI-11.19) | `papers/ablation_provenance/_scoring/anchor_matcher.py`, `papers/ablation_provenance/_scoring/specifics_matcher.py` |
    | `improvements/_prompts/regression_log.md` (also cited as `improvements/regression_log.md`), `improvements/{changelog_v17,changelog_v18,changelog_v181,changelog_v182,changelog_v183,changelog_v184}.md` (in the project under `improvements/_prompts/`), `improvements/{cross_model_kumada_vs_murai_meta,cross_model_verification_protocol}.md` | `tier_7_aggregation_scripts_and_methodology_evolution/regression_log.md`, `tier_7_aggregation_scripts_and_methodology_evolution/{changelog_v17,changelog_v18,changelog_v181,changelog_v182,changelog_v183,changelog_v184,cross_model_kumada_vs_murai_meta,cross_model_verification_protocol}.md` (same file names) |
    | `improvements/paperA_ep_audit_criteria_20260520.md` (cited in the Tier 5 audit READMEs) | `tier_6_audit_decisions/ep_audit_criteria_20260520.md` (identical file; the `paperA_` prefix is dropped) |
    | the two verification records of the SI-9.10 tally (B4, B5) | `01_response/r33b_candidates/records/stage4_literature_update_20260419.md`, `01_response/r33b_candidates/records/kumada_retrieval_depth_verification_extract.md` (the SI-9.10 tally no longer cites `improvements/` paths) |
    | `future_work/…` (`deferred_items_registry.md`, `pilot_evaluation_issues.md`; SI-6, SI-8) | `future_work_pointers/` (same file names; the project's `future_work/README.md` is `future_work_pointers/project_future_work_README.md`) |
    | `docs/…` (`docs/version_history.md`, SI-1; `docs/uqs_introduction_v13.md`, source column of the SI-8 reconciliation table) | not deposited (project documentation; the SI reproduces what it uses from them) |
    | `manuscript_A/sections/…` (source column of the SI-4 and SI-8 reconciliation tables, e.g. `3_results_ja.md`, `2_methods_en.md`) | not deposited (draft section files of the manuscript; the submitted article and SI are the reference) |
    | other `improvements/…` memos (e.g. `open_issues.md`, the Phase 1.5 and Phase 2 reports, `_methodology/ablation_results_paperA_20260810.md`) | not deposited; the SI marks them "project record, not deposited" |

    Paths the SI names as not deposited (the sandbox analyses of SI-10) are not here.
12. **Reading notes.** Outputs of the Japanese-language prompt cells, and some audit notes, are in Japanese. Two driver logs (`papers/dev/kumada/baseline_R1_2026-09/logs/driver{,_bl2}.out`) are empty because the runs wrote nothing to standard output, and the files in `failed_argv_20260929/` hold the error messages of failed launches, not JSON. In a few run inputs, absolute paths of the authors' machine are shown as `<project-root>` and chat links are removed (`REVISION_R1.md`).
13. **Recomputing SI-6.10.** `python3 tier_7_aggregation_scripts_and_methodology_evolution/classification_concordance/si6_10_datum_jaccard.py`, run from the package root, prints the SI-6.10 table from the deposited runs (needs `rapidfuzz`). *(Reviewer version only: the datums it compares are quoted passages, which are redacted in this cut, so here it prints different numbers; see `tier_7_aggregation_scripts_and_methodology_evolution/classification_concordance/README.md`.)*
14. **Re-running the figure and table scripts.** `python3 tier_7_aggregation_scripts_and_methodology_evolution/fig2_ep_filling_matrix.py` (likewise `fig3_vq_trajectory.py`, `fig4_recurring_roots.py`, `fig5_vq_inversion.py`, `figS1_refinement_improvements.py` and `render_tables.py`), from any directory, needs matplotlib and pandas (`render_tables.py` also tabulate). The scripts read `tier_4_classification_tables/figures_data/` and write to `rerun_output/` at the package root, which they create; in the project repository they read and write `manuscript_A/figures/{data,output}/`. Compared with the renderings in `tier_4_classification_tables/figures_output_pdf_png_svg/` (checked 2026-10-17): Figs. 2–5 give byte-identical PNG files and PDF / SVG files that differ only in the embedded creation date and generated pattern identifiers; Tables 3–4 are byte-identical; Tables 1–2 have the same cells with different column padding; the rendering of the withdrawn SI Fig. S1 was made with an earlier version of its script and differs.
15. **Re-running the scoring scripts of the revision.** The implementations they use are in `tier_7_aggregation_scripts_and_methodology_evolution/lib/` (copies of the project's `scripts/`, see its README). Each script below runs from any directory, reads the deposited inputs and writes to `rerun_output/` at the package root (the deposited results are not overwritten), so each output can be compared with the deposited one; they need Python 3.9+, and the quote gate needs `rapidfuzz` and `pdftotext` (poppler). **Source PDFs are not deposited**: a script marked *(PDF)* needs the reader's own copy of the source paper(s), placed as stated, and stops with a message if it is missing.
    | Command | What it recomputes | Reviewer version (checked 2026-10-17) | Public cut |
    |---|---|---|---|
    | `python3 01_response/d3_heldout/check_heldout.py` | held-out structural endpoints (SI-11.20) → `check_results.json` | byte-identical | no: its inputs are redacted run records, so the numbers differ |
    | `python3 tier_7_aggregation_scripts_and_methodology_evolution/lib/verbatim_quote_gate.py papers/paperA_heldout_R1/<id> --stages s0,s1,s2_en --json <out>` and `--stages s3v2_en`, run from the package root *(PDF: `papers/paperA_heldout_R1/<id>/<id>.pdf` and `<id>_si.pdf`)* | held-out quote gate → `01_response/d3_heldout/gate_<id>_{s0-s2,s3}.json` | byte-identical (all eight files) | no: its inputs are redacted run records, so the numbers differ |
    | `python3 01_response/d4_baseline/aggregate_d4.py` *(PDF: `papers/dev/kumada/Kumada_1972.pdf`)* | single-prompt baseline endpoints (SI-11.20) → `d4_metrics.csv`, `d4_quotes.csv` | byte-identical | no: its inputs are redacted run records, so the numbers differ |
    | `python3 01_response/d4_baseline/extract_cells.py`, `extract_cells_v2.py` | blinded rating packets and keys → `adjudication{,_v2}_packets.json`, `adjudication{,_v2}_key.json` | byte-identical, except `adjudication_v2_packets.json`: the deposited packets carry two hand edits made before the rating (2026-09-29): the full text of the run added to the 12 cells without a candidate line (`fulltext`), and a header line that named the arm removed from the snippets of 2 cells; the key is identical | keys byte-identical; packets differ (redacted run records) |
    | `python3 01_response/d4_baseline/aggregate_adjudication.py`, `aggregate_adjudication_v2.py` | the two raters' verdicts combined → `adjudication{,_v2}_final.csv` | byte-identical | byte-identical |
    | `python3 01_response/d4_baseline/score_b2_stage3.py` *(PDF: `papers/dev/kumada/Kumada_1972.pdf`)* | B2 → Stage 3 endpoints → `b2_stage3_mechanical.csv`, `b2_stage3_quotes.csv` | byte-identical | no: its inputs are redacted run records, so the numbers differ |
    | `python3 01_response/srg_root_mapping/extract_srg_blocks.py`; `aggregate_srg_mapping.py` | SRG-root mapping (SI-6.10): blinded blocks → `srg_blocks_packets.json`, `srg_blocks_key.json`; the aggregation prints the mapping table | byte-identical; the printed table equals the project run | extraction: no (it reads the Stage 3 outputs in Tier 3); aggregation: same printed table |
    | `python3 01_response/r34_recount/recount.py` | R3-4 EP / SRG re-count of the refinement set → `recount.csv` | byte-identical | no (it reads the Stage 3 outputs in Tier 3) |
    | `python3 tier_7_aggregation_scripts_and_methodology_evolution/lib/repro_extract.py <copy>` then `repro_aggregate.py <copy>`, where `<copy>` is a copy of `papers/dev/kumada/repro_2026-07/` (the wrappers in that folder do the same but write into the folder itself) | reproducibility control → `repro_metrics.csv`, `repro_summary.md` | byte-identical (also the wrappers, in place) | no: its inputs are redacted run records, so the numbers differ |
    | `python3 tier_7_aggregation_scripts_and_methodology_evolution/lib/verbatim_quote_gate_20260720.py papers/dev/kumada/repro_2026-07 --json <out>`, run from the package root *(PDF: `papers/dev/kumada/Kumada_1972.pdf`)* | quote gate of the reproducibility runs → `verbatim_gate_20260720.json` | byte-identical | no: its inputs are redacted run records, so the numbers differ |
    | `python3 tier_7_aggregation_scripts_and_methodology_evolution/lib/verbatim_gate_corpus_scan.py --version v17 --json <out>` over `tier_3_stage_outputs/test_set/<id>/` *(reviewer version only; redacted Markdown copies under `tier_8_redacted_public_raw_outputs/`)* of the ten refinement-set papers, and `--version v184` over the Tier 3 folders of Kumada 1972, Murai 1993 and the nine EP-context papers, run from the package root *(PDF: each paper's article PDF and SI PDF in its folder; an SI file name must contain `_si`, `_s<n>`, `moesm`, `_esm` or `supp`)* | quote gate of the analyses Paper A cites → `papers/_audits/paperA_quote_gate_R1_2026-09/gate_*.json` | identical apart from the folder and PDF file names recorded in the JSON | no (it reads the outputs in Tier 3) |

---

## Purpose

This deposit makes every analytical decision in the paper inspectable in a **nine-tier audit-trail organisation**, from the most reusable methodology specification (Tier 1) to full raw outputs (Tier 9). Three supplementary directories cover the per-reference verification catalogue, application-direction artifacts (ChemOntology Layer A only), and non-dependency future-work pointers.

The deposit organisation mirrors the *Data Availability* section of the manuscript and the full Tier 1–9 specifications in **SI-11.11**.

---

## Folder structure

### Nine-tier audit-trail organisation

| Tier | Folder | Content |
|---|---|---|
| **1** | `tier_1_prompt_versions/` | UQS prompts v15 → v18.4 covering the v15→v17 refinement cycle (Results Part 4) and the v18.4 analysis configuration, plus the Stage 2F / 3 / 4 prompts used: `prompt_stage3_v1.md`, `prompt_stage3_v2.md` (JA), `prompt_stage3_v2_en.md`, `prompt_stage3_v4.md`, `prompt_stage4_v1.md`, `prompt_stage4_v2.md` (JA), `prompt_stage4_v2_en.md`, `prompt_stage4_v6.md`, `prompt_stage2f_v6.md`, `prompt_stage2f_v7.md`, `prompt_stage2f_v71.md`. v0–v14 are exploratory / superseded prompts not used by Paper A and are excluded. |
| **2** | `tier_2_input_metadata/` | `paperA_21_paper_corpus_manifest.csv` — the authoritative 21-paper Paper A corpus manifest (2 development + 10 refinement-set + 8 historical + 1 Tamao 2002 mini-review) with Crossref-verified DOIs, roles, and BibTeX-key cross-links (the ten Heck papers are the refinement set, not a held-out test set). |
| **3** | `tier_3_stage_outputs/` *(reviewer version only; redacted Markdown copies under `tier_8_redacted_public_raw_outputs/`)* | Complete Stage 0–Stage 4 analysis records for all 21 corpus papers, organised as `dev_set/` (2), `test_set/` (10; the folder name is kept for path stability, the set is the refinement set), `context_analyses/` (4 context papers whose Stage 3 v4 / Stage 4 v6 analyses are counted in Methods 6), `ep_historical_case_study/` (9), and `stage2f_integration_outputs/` (24 Stage 2F + 1 Stage 3 anchor files for the G1 / G2 / G3 / all-papers integration × s2f v6 / v7 / v7.1 cells under both v17 Opus 4.6 and v18.4 Opus 4.7). |
| **4** | `tier_4_classification_tables/` | EP audit table (10 EPs × per-paper filling-status matrix), SSP table (7 SSPs), Stage 1 A/B/C/U classifications, Stage 3 SRG/CLA codebook, four-model cross-comparison matrices (SI-6). `reaggregation_R1/` holds the revision's mechanical re-counts of the multi-run values (scripts + CSVs, SI-3). Two subfolders: `figures_data/` (CSV source data for Figs. 2–5, SI Fig. S1, and Tables 1–4) and `figures_output_pdf_png_svg/` (rendered figure outputs). Rendering scripts are in Tier 7 (data-driven figures only). |
| **5** | `tier_5_retrieval_logs/` | Stage 4 filling-paper retrieval logs + structured Web of Science Core Collection audit for EP-03a (pilot), EP-07a (positive-control comparator), EP-08a, EP-09a — under pre-locked criteria. |
| **6** | `tier_6_audit_decisions/` | `ep_audit_criteria_20260520.md` (criteria locked before retrieval) + `internal_mini_audit_v1/` (eleven-item expert-comment forms in EN + JA; planned protocol, not relied upon as current evidence). |
| **7** | `tier_7_aggregation_scripts_and_methodology_evolution/` | Python figure / table rendering scripts for the **data-driven figures only** (`fig2_ep_filling_matrix.py`, `fig3_vq_trajectory.py`, `fig4_recurring_roots.py`, `fig5_vq_inversion.py`, `figS1_refinement_improvements.py`, `render_tables.py` — per the SI-11.11 Tier 7 spec "Figs. 2–5, SI Fig. S1"); per-version regression log + changelogs v17 → v184; session-handover memos v15 → v16 + v16.1; v17 twelve-paper metrics CSV + extraction script; cross-model verification protocol + n=2 meta-observation. The rendering scripts run inside this package and write to `rerun_output/` (§0 item 14). `lib/`: the implementations used by the scoring scripts of the revision (§0 item 15). |
| **8** | `tier_8_redacted_public_raw_outputs/` | Redacted Stage 0/1/2/3/4/2F outputs: verbatim source-paper quotations replaced by `[REDACTED: …]` markers that point to the source paper (DOI or the item's `loc:` field) or to the unredacted copy. |
| **9** | `tier_9_full_raw_logs_reviewer_only/` | **(Reviewer-only access)** Full raw outputs with verbatim source-paper quotations. In this package the unredacted outputs are the Tier 3 copies; this tier holds only its README. Access: restricted to the editor and reviewers until acceptance (see Access policy). |

### Supplementary directories

| Folder | Content |
|---|---|
| `per_reference_catalogue/` *(reviewer version only)* | BIB caches and per-reference analysis records (source PDFs are not deposited) for the 29 chemistry / empirical references covered by the Paper A verification catalogue (`papers/refs/`). The catalogue uses the reference numbers of the April 2026 draft (31 references): its refs 15 (Althusser & Balibar 1965) and 16 (Macherey 1966; Refs 18 and 19 of the revised paper) are not digitally available, so their folders hold a status card only, and the other 29 (refs 1–14 and 17–31) have records. Four cross-coupling references added during revision as acknowledged precedents (Murahashi 1975, Martin & Buchwald 2007, Terao & Kambe 2002, Jones & Vicic 2005 — Refs 28, 29, 44 and 45 of the revised paper) are cited for context only and are not part of the verification catalogue. The folders ref32–ref36 hold status cards only: refs 32–35 are background references added in May 2026 (Refs 46–49 of the revised paper); ref 36 is not cited in the paper. Besides their Stage 0 caches, the folders of refs 1, 4–14 and 17–31 hold a complete run made on 2026-04-28/29 with the v18.3 prompts (Stage 0–2 v18.3, Stage 3 v3, Stage 4 v3; all in Tier 1); no claim of the paper uses these runs. |
| `application_direction_chemontology_layer_a/` | **ChemOntology Layer A only** (Paper A Kumada-1972 scope): `ep_to_chemontology_mapping.md` (the EP-to-ChemOntology-AFIR parameter mapping that underlies SI-3.11 / Table 4) + `mapping_verification_log.md` (per-parameter source-citation verification log). Layer B (YAML/JSON input specs), Layer C (pilot-package plan), Phase 2 NiCl₂(dpe) execution, and a mapping for a Pd amidocarbonylation system (later work of the project) are deferred to later deposits (Paper B and later work of the project). |
| `future_work_pointers/` | Registered future-work items (inter-rater-reliability pilot, Codebook v0.3, v18 prompt with dual-layer VQ output, Layer A EP-10a mapping revision). **The conclusions of Paper A do not depend on any of these items.** |

### Top-level orientation files

- `README.md` (this file)
- `zenodo_manifest.md` — manifest of model identifiers, release dates, reliable-knowledge cutoffs, training-data cutoffs, prompt × model × stage matrix, and aggregate per-phase execution-date ranges referenced in the manuscript Data Availability section.

---

## Access policy

- **Public cut (this repository).** The quotation-redacted cut of the reviewer version, released on GitHub (https://github.com/yurikoono/uqs-mapping-structured-absences) at resubmission. It holds no Tier 3 or Tier 9 files and no per-reference catalogue; Tier 8 holds the redacted outputs. It is built from the reviewer version by `scripts/build_paperA_R1_public.py` in the project repository; the notice at the top of this README states the redaction rules. The complete Supporting Information is included as `supporting_information/SI_R1.pdf`.
- **Reviewer version.** Published on Zenodo as its own record, concept DOI 10.5281/zenodo.23437447 (cited in the paper's Data Availability statement; versions are listed at the top of this README); its files are restricted to the editor and reviewers until acceptance. The deposit shared with the submitted manuscript was a different Zenodo record (21026938), which was never published: it was shared through a preview link, and its reserved DOI 10.5281/zenodo.21026938 was never registered. It includes the full stage outputs with verbatim audit excerpts (Tier 3).
- **After acceptance.** The corresponding author decides which restricted files of the reviewer version are opened; outputs containing verbatim source-paper quotations are released only where that is legally safe.

## Raw-output redaction policy

Stage 0 / 1 / 2 outputs occasionally quote source-paper text directly to anchor absence judgments. To respect publisher copyright:

- **Tier 8 (redacted public)**: verbatim source-paper quotations replaced by `[REDACTED: …]` markers. Each marker states what was removed and where the full text is: the source paper (via its DOI, or at the location given in the item's own `loc:` field, which is kept) or the unredacted copy (Tier 9; in this package, the Tier 3 copies), e.g. ``[REDACTED: verbatim source text; see the source paper via its DOI]``, ``[REDACTED: see `loc:` above; full text in Tier 9]``, ``[REDACTED: paper boundary quote; see Tier 9]``. The markers themselves carry no page, figure or scheme numbers; UQS classifications and reasoning preserved verbatim. Model-written paraphrases of a paper's title or claims (the quoted E-propositions, i.e. the `confirmed_english_propositional` statements of Stage 2 and tables that list them, with fewer than ten contiguous words of the paper's text) are not source quotations and are kept.
- **Tier 9 (full version, reviewer-only)**: source-paper quotations preserved verbatim (in this package, the Tier 3 copies); access restricted to the editor and reviewers until acceptance (see Access policy).

The redaction supports independent reproduction of UQS classifications without copyright concern (Tier 8) and content-level verification of source-anchor validity (Tier 9).

---

## Model labels in file and folder names (2026-10-19)

The model token of a file or folder name is the model planned for the run; the model that ran is the one recorded in the file's `model_info` line (for the Stage 4 candidates, also in `tier_4_classification_tables/stage4_candidates_R1/candidates.csv`, column `model_info_verbatim`). Where they differ: `dev_set/kumada/gemini3flash/GPT1.5/kumada_v17_gemini3_*` were run by Gemini 1.5 Pro (automatic model selection; not part of SI-6); in `dev_set/kumada/gpt54thinking/`, three of the six retrieval-depth files (`s4v2_retrieval_depth_run2`, `s4v6_retrieval_depth_run1`, `s4v6_retrieval_depth_run3`) record GPT-5.5 Thinking; `test_set/app2/app2_v17_sonnet_s3.md` and `_s4.md` record `claude-sonnet-4-5` (see `zenodo_manifest.md` and `papers/_audits/paperA_quote_gate_R1_2026-09/model_identity_audit.log`). `model_info` is the model's own report. Version suffixes follow the project convention (no suffix = v1), except `kumada_v17_gpt54thinking_s3/s4` and `kumada_v17_gemini3_s3/s4`, whose headers record Stage 3 / Stage 4 v2 (as SI-6 states for the GPT-5.4 run), and `murai_v182_sonnet_s3.md` (Stage 3 v3).

## Scope hygiene (2026-06-25 audit)

Some records in `01_response/` cite internal review notes of the project that are not deposited (`fable51_review_D3D4_20260929.md`, `fable51_review_20260928.md`, `D3_D4_design_proposal_20260929.md`, `ja_sync/` files); the deposited records state the results that rest on them. `01_response/d1_expert/ratings/README.md` points to `../_private/`, which is not deposited (rater anonymity). `tier_1_prompt_versions/v184_production/prompt_stage1_turn4_naive_textbook_v184_pilot_v3.md` is byte-identical to `_pilot_v4.md` (tag `stage1-v184-20260527_v4pilot_v4`): the v3 text recorded by the two `*_s1_v4pilot_v3_20260527.md` outputs was overwritten before the project's version control began (2026-06-10) and is not preserved. No claim of the paper uses the Turn 4 textbook pilot (SI-7 does not list it).

This deposit has been audited against the **21-paper Paper A corpus** specified in SI-11.11. The following items existed in the project source but have been **excluded from this deposit** as out of scope for the present paper:

### Excluded prompts (Tier 1)

- `prompts/v0/` through `prompts/v14/` — early exploratory prompts not used by Paper A's published analyses.
- `prompts/v19/` — the v19 prompts used by the reproducibility control's successor-version arm (Methods 6; SI-7 rows 24–29) are deposited in `tier_1_prompt_versions/v19_successor_arm/`; other later prompt versions are not deposited.
- `prompts/stage2f3/` non-Paper-A files: `prompt_rhetoric_v1.md` through `v12.md` (later work of the project, not used by Paper A); `prompt_unpack_v1.md` through `v3.md` + `prompt_unpack_claude_v1.md` (later work of the project, not used by Paper A); `prompt_stage4_v4.md` (not used by any deposited output); `prompt_editorial_v1.md, v2.md` (general editorial tools). (Before the revision, `prompt_stage3_v1.md`, `v4.md` and `prompt_stage4_v1.md`, `v6.md` were also excluded here, although deposited outputs had used them; they are now in Tier 1. Until 2026-10-19 `prompt_stage3_v3.md` and `prompt_stage4_v3.md` were listed here as unused, although deposited outputs carry their tags (`stage3-v3-20260425`, `stage4-v3-20260425`): the Stage 3 / Stage 4 files of the Kumada v18 / v18.1 / v18.2 and Murai v18.2 runs in Tier 3 (including `murai_v182_sonnet_s3.md`, whose name has no version suffix), the two GPT-5.5 Thinking runs of SI-11.1 row 15 (`gpt55thinking/`), and the v18.3 runs of the per-reference catalogue. They are in Tier 1 since version v3 of this record. The project's version control begins on 2026-06-10, so the deposited files are the prompts as they stood then; their tags match those recorded in the outputs.)

### Excluded corpus metadata (Tier 2)

- `corpus/corpus_paper_list.csv` — parent ~1,113-paper Heck-reaction corpus from which the 10-paper refinement set was sampled. The 10 test papers themselves are documented in `paperA_21_paper_corpus_manifest.csv`.
- `papers/uqs_new_corpus_roster.csv` — corpus roster of later work of the project, not used by Paper A.

### Excluded paper analyses (Tier 3)

- `papers/dev/{jones2005, martin2007, terao2002, uchino}/` — excluded from the submitted version. **Included from R1** under `tier_3_stage_outputs/context_analyses/` *(reviewer version only; redacted Markdown copies under `tier_8_redacted_public_raw_outputs/`)* (Stage 0–4 only), because the revised Methods 6 counts their four Stage 4 analyses among the 37 reported.
- `papers/dev/uqs_self/` — UQS self-application meta-analysis. Reflexive analysis archived at `papers/meta/ono2026/` (canonical location); not part of Paper A's 21-paper empirical corpus.
- `papers/ep/kumada1972/{yamamoto1978, yamamoto1981}/` — deposited under `tier_3_stage_outputs/citation_integrity_cases/` *(reviewer version only; redacted Markdown copies under `tier_8_redacted_public_raw_outputs/`)*: citation-integrity audit cases (SI-9.3 (iv) triple-mismatch + SI-3.7 cross-paper confirmation). Audit material, not historical case-study fillers.
- `papers/ep/etc/kumada1976/` — Hayashi-Tajika-Tamao-Kumada 1976 JACS asymmetric Grignard cross-coupling (a different 1976 Tamao paper from the Layer-1 anchor `kumada1976b` = Tamao 1976 BCSJ Full Paper I).

### Excluded ChemOntology artifacts (application-direction)

- `chemontology_pilot/layer_B_input_specification/` (Layer B), `chemontology_pilot/layer_C_pilot_package_plan/` (Layer C), and Phase 2 NiCl₂(dpe) execution — to be deposited with Paper B (in preparation).
- A second Layer A mapping, for a Pd amidocarbonylation system — later work of the project, a different chemical system; not used by Paper A.
- `chemontology_pilot/layer_A_parameter_mapping/discussion2_insertion_draft.md` — stale 2026-04-19 insertion draft for a Discussion 2 paragraph that predates the manuscript's 3-Discussion restructure. Superseded by current Discussion 3 and SI-3.11.

### Excluded audit artifacts (Tier 6)

- `audit/inventory_20260610.tsv` — project-wide file-size inventory (CLAUDE.md, scripts/, etc.). General housekeeping, not Paper A audit decisions.

### Excluded rendering scripts (Tier 7)

The following rendering scripts are **intentionally not deposited** because they produce presentation artifacts rather than data-driven scientific results, and their deposit goes beyond the SI-11.11 Tier 7 spec ("Figs. 2–5, SI Fig. S1"):

- `manuscript_A/figures/scripts/fig1_uqs_pipeline.py` — UQS workflow schematic. Schematic diagrams are conventionally drawn in vector-graphics editors (Illustrator / Inkscape); the Python implementation is for the authors' workflow only.
- `manuscript_A/figures/scripts/scheme1_kumada_reaction.py` — Kumada 1972 chemistry scheme. Chemistry schemes are conventionally drawn in ChemDraw; the Python implementation is non-standard.
- `manuscript_A/figures/scripts/graphical_abstract.py` — Digital Discovery graphical abstract artwork. Editorial publication artifact with no underlying scientific data.

The rendered outputs (PDF / PNG / SVG) of these figures are nonetheless included in `tier_4_classification_tables/figures_output_pdf_png_svg/` for reviewer convenience; only the source scripts are excluded. The scripts remain in the project source for the authors' future reuse.

All excluded items remain in the project source for history; only the Paper A-scope subset is exposed in this deposit.

---

## Packaging

`zenodo_deposit_paperA/` in the project repository is the staging organisation (symbolic links to project source). The reviewer package is a self-contained copy: `scripts/make_reviewer_package.sh` resolves the links and removes wholesale source-paper reproductions (source PDFs, OCR full texts, page scans, WoS abstract / keyword / funding fields). The R1 package was built from the 2026-08-31 package plus the changes listed in `REVISION_R1.md`, **not** re-cut from the staging links, because the linked project folders now also contain analyses run after submission that are outside this paper's scope.

## Citation

If this deposit is cited independently of the paper, please cite:

> Ono, Y., Yoshioka, M., Taketsugu, T. (2026). *Zenodo deposit accompanying "Mapping Structured Absences in Scientific Papers: An Auditable LLM-Assisted Workflow Demonstrated on Cross-Coupling Chemistry" (UQS Methodology, 9-tier audit-trail organisation)*. Zenodo. https://doi.org/10.5281/zenodo.23437447

This DOI identifies the reviewer version of this cut (first-round revision, R1), from which this public cut is built. It is the concept DOI 10.5281/zenodo.23437447, which resolves to the latest version; v1 is 10.5281/zenodo.23437448, v2 is 10.5281/zenodo.23446545, v3 is 10.5281/zenodo.23466681 and v4 is 10.5281/zenodo.23469269. The record shared with the submitted manuscript was never published and has no DOI to cite.

## Contact

Corresponding authors:
- Yuriko Ono — `yono@sci.hokudai.ac.jp`
- Tetsuya Taketsugu — `take@sci.hokudai.ac.jp`

For technical questions about deposit contents or access, please contact either corresponding author.

---

## Audit log

| Date | Action |
|---|---|
| 2026-05-22 | Initial staging folder created with 9 tiers + 3 supplementary directories. |
| 2026-06-25 | Scope audit applied: removed v0–v14, parent corpus CSV, the corpus roster of later work, dev-set reference analyses, yamamoto audit cases, Hayashi 1976 asymmetric paper, the ChemOntology mapping of later work of the project, stale Discussion 2 insertion draft, project-wide file-size inventory, and non-Paper-A stage2f3 prompts. Reorganised Tier 3 into 4 subdirs (dev_set / test_set / ep_historical_case_study / stage2f_integration_outputs) for clarity. Created `paperA_21_paper_corpus_manifest.csv` as the authoritative input-metadata manifest. |
| 2026-06-28 | Figure rendering scripts narrowed to the data-driven subset per SI-11.11 Tier 7 spec ("Figs. 2–5, SI Fig. S1") and chemistry-community convention. Tier 4 split into `figures_data/` (CSV source data) and `figures_output_pdf_png_svg/` (rendered figure outputs). Tier 7 figure scripts changed from a folder symlink (all 9 scripts) to individual symlinks for the 6 data-driven scripts (fig2/fig3/fig4/fig5/figS1 + render_tables); schematic / chemistry-scheme / graphical-abstract scripts (`fig1_uqs_pipeline.py`, `scheme1_kumada_reaction.py`, `graphical_abstract.py`) excluded as publication artifacts. |
| 2026-09-28 | First-round revision (R1): §0 audit guide added; Tier 1 prompt set completed; corpus manifest corrected against Crossref; context analyses added; re-count scripts and CSVs added; WoS raw-export status recorded; control experiments of the revision added under `papers/`. Details in `REVISION_R1.md`. |
| 2026-10-16 | Final R1 version: revision studies, SI, licence and final figures added; project-path table (§0 item 11); access policy and DOI wording (corrected 2026-10-18); regression-log entries about other manuscripts removed; three independent audits of the build applied. Details in `REVISION_R1.md`. |
| 2026-10-17 | Sixth independent audit of the deposit: Fig. 3 data corrected (EP-05a Partial plotted at 2.5; `figures_data/fig3_vq_trajectory.csv` and the rendered Fig. 3); Tier 8 of this package replaced by the Tier 8 of the public cut (stricter redaction; identical files in both cuts); in the public cut, quotations left in table cells of three adjudication / verification records redacted and the pointers to Tier 3 marked as reviewer-version only. Details in `REVISION_R1.md`. |
| 2026-10-17 | Seventh independent audit of the deposit: in the public cut, verbatim runs that a title filter had split are redacted (title masking only from eight words) and the build requires the redaction script's own check to pass; README and LICENSE describe the redaction markers as they are and state that model-written paraphrases are kept; the v19 prompts of the successor-version arm listed as deposited; file counts corrected; file modes 644 / 755 and no extended attributes. Details in `REVISION_R1.md`. |
| 2026-10-17 | Final figures and SI, and eighth independent audit of the deposit: Fig. 1 and Fig. 5 re-rendered (with the Fig. 5 script) and the corrected SI (SI-3, 5, 6, 11); every rendered figure / table and figure-data file refreshed from the current sources and checked at build time (stale Table 3 rendering replaced); in the public cut and the shared Tier 8, near-verbatim quotations (shortened or retyped, ≥ 80% character similarity to a source passage) redacted; Tier 1, Tier 3 and redaction-scope statements in README, `zenodo_manifest.md` and the public notice corrected. Details in `REVISION_R1.md`. |
| 2026-10-17 | Corrections after a further audit: another paper of the project no longer named in the documentation; Tier 7 figure and table scripts run inside the package (§0 item 14); corpus manifest gains `deposit_path`; in the public cut, verbatim passages of the ChemOntology paper replaced by paraphrases and the R1 removal notes shortened. Details in `REVISION_R1.md`. |
| 2026-10-17 | Scoring scripts of the revision runnable inside the package: implementations deposited in Tier 7 `lib/`, callers resolve their inputs in the package and write to `rerun_output/` (§0 item 15); re-run in both cuts and compared with the deposited results; no deposited script names a missing project path (checked at build time); §0 item 14 corrected (Table 2). Details in `REVISION_R1.md`. |
| 2026-10-18 | Deposit DOI: this revised deposit is the Zenodo record 10.5281/zenodo.23437448 (files restricted to the editor and reviewers until acceptance); the record shared with the submitted manuscript was never published, and the earlier statements about its DOI and about this package being a version of it are corrected. Details in `REVISION_R1.md`. |
| 2026-10-19 | Version v3: Stage 3 v3 / Stage 4 v3 prompts added to Tier 1; DOI statements name the concept DOI 10.5281/zenodo.23437447; per-reference catalogue numbering, model labels, dated notes on superseded records, ref 36 status card, Tier 6 / Tier 8 / Tier 9 wording. Details in `REVISION_R1.md`. |
| 2026-10-19 | Version v4: reference numbers of the revised paper corrected to the typeset numbering (README, `zenodo_manifest.md`); corpus-manifest column `md_reference_number` removed; v3 DOI added to the version list. Details in `REVISION_R1.md`. |
| 2026-10-19 | Version v5: the two books are Refs 18 and 19 of the revised paper also in `zenodo_manifest.md` (v4 had missed this line); §0 item 2 states which prompts are not in Tier 1; v4 DOI added to the version list. Details in `REVISION_R1.md`. |
