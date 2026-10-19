# Tier 4 — Classification Tables

**Contents (listed when this package was built, 2026-10-16).**

- **`figures_data/`** — source data of the figures and tables:
  - `fig2_ep_filling_matrix.csv` — 10 EPs × per-paper filling-status matrix (the EP audit table; Fig. 2)
  - `fig3_vq_trajectory.csv` — VQ hierarchy trajectory data (Fig. 3)
  - `fig4_recurring_roots.csv` — Stage 2F recurring_roots taxonomy (Fig. 4)
  - `figS1_refinement_improvements.csv` — v15→v17 refinement-cycle progression (SI Fig. S1, withdrawn in R1; see below)
  - `table1_test_set.csv` — the 10-paper refinement set (Table 1; the file name keeps the earlier term "test set")
  - `table2_kumada_eps.csv` — Kumada 1972 EP dictionary (Table 2)
  - `table3_case_studies.csv` — the historical case-study papers (Table 3)
  - `table4_ep_chemontology_mapping.csv` — EP-to-ChemOntology mapping (Table 4; SI-3.11)
  - `v17_twelve_paper_metrics.csv` — per-paper U / B / D-4 counts of the twelve v17 analyses
  - `v17_twelve_paper_metrics_README.md` — documentation of the metrics CSV
- **`figures_output_pdf_png_svg/`** — rendered figures and tables (R1 versions; the authoritative renderings are those of the published article):
  - `fig1_uqs_pipeline` (.pdf, .png, .svg)
  - `fig2_ep_filling_matrix` (.pdf, .png, .svg)
  - `fig3_vq_trajectory` (.pdf, .png, .svg)
  - `fig4_recurring_roots` (.pdf, .png, .svg)
  - `fig5_vq_inversion` (.pdf, .png, .svg)
  - `figS1_refinement_improvements` (.pdf, .png, .svg)
  - `graphical_abstract_R1B` (.pdf, .png, .svg)
  - `graphical_abstract_text` (.md)
  - `scheme1_kumada_reaction` (.pdf, .png, .svg)
  - `table1_test_set` (.md)
  - `table2_kumada_eps` (.md)
  - `table3_case_studies` (.md)
  - `table4_ep_chemontology_mapping` (.md)
- **`reaggregation_R1/`** — the R3-3 re-aggregation of the revision (Top-3 inclusion frequency and Stage 4 filling levels; README in Japanese): `README.md`, `corpus11_inversion_per_paper.csv`, `corpus11_labels_per_ep.csv`, `definitions_fixed_before_counting.md`, `extraction_trace.md`, `inclusion_frequency_per_cell.csv`, `multirun_top3_per_run.csv`, `reaggregate_11papers.py`, `reaggregate_stage4.py`, `reaggregate_top3.py`, `stage4_inversion_per_run.csv`, `stage4_labels_per_ep.csv`
- **`stage4_candidates_R1/`** — the SI-9.10 tally of Stage 4 candidates (the same files as `01_response/r33b_candidates/`): `README.md`, `build_tally.py`, `candidates.csv`, `records/kumada_retrieval_depth_verification_extract.md`, `records/make_extracts.py`, `records/stage4_literature_update_20260419.md`, `tally.md`, `tally_counts.json`

**Items of the SI-11.11 Tier 4 specification that are not separate files in this tier.**

- SSP table (the seven SSPs with source-paper anchors): Table 5 of the paper; its source records are the Stage 2F outputs in `tier_3_stage_outputs/stage2f_integration_outputs/` *(reviewer version only; redacted Markdown copies under `tier_8_redacted_public_raw_outputs/`)*.
- Stage 1 absence classification per paper (A / B / C / U): the Stage 1 outputs (`*_s1.md`) of each paper in Tier 3 *(reviewer version only; redacted copies at the same sub-paths of `tier_8_redacted_public_raw_outputs/`)*.
- Stage 3 SRG / CLA codebook: defined in the Stage 3 prompts (`tier_1_prompt_versions/`, `prompt_stage3_*.md`); the per-paper SRG / CLA records are the Stage 3 outputs (`*_s3*.md`) in Tier 3 *(reviewer version only; redacted copies at the same sub-paths of `tier_8_redacted_public_raw_outputs/`)*.
- Four-model cross-comparison (SI-6): tabulated in SI-6; the underlying v17 runs on Kumada 1972 are `tier_3_stage_outputs/dev_set/kumada/kumada_v17_{haiku,sonnet,opus47}_s*.md` *(reviewer version only; redacted Markdown copies under `tier_8_redacted_public_raw_outputs/`)* and `tier_3_stage_outputs/dev_set/kumada/gpt54thinking/kumada_v17_gpt54thinking_s*.md` *(reviewer version only; redacted Markdown copies under `tier_8_redacted_public_raw_outputs/`)*; the later v18.2 cross-model notes are `tier_3_stage_outputs/dev_set/{kumada,murai}/cross_model_v182_comparison.md` *(reviewer version only; redacted Markdown copies under `tier_8_redacted_public_raw_outputs/`)* and `tier_7_aggregation_scripts_and_methodology_evolution/cross_model_kumada_vs_murai_meta.md`.
- Multi-run data: the per-run outputs in Tier 3 (`dev_set/kumada/*_run*.md`, `dev_set/murai/multirun/`) *(reviewer version only; redacted copies at the same sub-paths of `tier_8_redacted_public_raw_outputs/`)* and `papers/dev/kumada/repro_2026-07/`; their R1 re-aggregation is `reaggregation_R1/`.

## Note on rendering scripts

The Python rendering scripts for the **data-driven** figures (Figs. 2–5, SI Fig. S1) and the table-rendering script are in **Tier 7** (`tier_7_aggregation_scripts_and_methodology_evolution/`) per the SI-11.11 Tier 7 spec ("Python scripts for figure / table rendering (Figs. 2–5, SI Fig. S1)").

The schematic and publication-artifact rendering scripts — `fig1_uqs_pipeline.py` (UQS workflow schematic), `scheme1_kumada_reaction.py` (chemistry scheme), and `graphical_abstract.py` (Digital Discovery graphical-abstract artwork) — are intentionally **not deposited**. These figures are presentation artifacts rather than data-driven scientific outputs; their reproducibility value is limited (schematic diagrams and chemistry schemes are conventionally drawn in Illustrator / ChemDraw, and the graphical abstract is an editorial publication artifact). The rendered outputs (PDF / PNG / SVG) are available under `figures_output_pdf_png_svg/`; the source scripts remain in the project repository for the authors' future reuse.

**R1 (2026-10-07).** The rendered figures are the revised versions: every figure drawn at its printed width (15 cm) with text of at least 7.5 pt, Fig. 3 as ten panels, and the table-of-contents graphic at 8 × 4 cm (`graphical_abstract_R1B.*`, chosen 2026-10-16; its submission-form text is in `graphical_abstract_text.md`); Scheme 1 is drawn for a single column (8.15 cm); the data in `figures_data/` are unchanged. Renderings of the submitted version that the R1 figures replace (the submitted graphical abstract and its dense draft, the colour-vision checks of the submitted Figs. 2–4) are not repeated here; they remain in the deposit shared with the submitted manuscript (an unpublished Zenodo record). **SI Fig. S1 is withdrawn in R1**: its per-version aggregates could not be reproduced from the regression log (SI-2.B, Entry 003). `figS1_refinement_improvements.*` and its CSV and script are kept as a record of the submitted version only.
