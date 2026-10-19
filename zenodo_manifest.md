# Zenodo Deposit Manifest — Paper A

**Generated**: 2026-05-22
**Manuscript**: *Mapping Structured Absences in Scientific Papers: An Auditable LLM-Assisted Workflow Demonstrated on Cross-Coupling Chemistry* (Digital Discovery, DD-ART-06-2026-000428)
**Revised**: 2026-09-28 (first-round revision; see §6)
**Manifest scope**: Model identifiers, release dates, knowledge cutoffs, training-data cutoffs, and per-run execution-date summary for all analyses referenced in the manuscript Data Availability section.

This file is the physical artifact referenced in the Data Availability Tier 8 paragraph as "a manifest file" recording per-model and per-run metadata.

---

## 1. Model identifiers and cutoff dates

| Model | Identifier as recorded in `model_info` of the deposited outputs | Release date | Reliable-knowledge cutoff | Training-data cutoff | Role in this paper |
|---|---|---|---|---|---|
| **Claude Sonnet 4.6** | `claude-sonnet-4-6` | 2026-02-17 ¹ | August 2025 ² | January 2026 ² | **Primary model**: v18.4 S0–S2 with Stage 3 v2 EN / Stage 4 v2 EN on the development set (N = 6 per language cell) and single runs on the nine EP-context papers; Stage 3 v4 / Stage 4 v6 for four context analyses (Uchino 1970, Terao–Kambe 2002, Jones–Vicic 2005, Martin–Buchwald 2007). |
| **Claude Opus 4.7** | `claude-opus-4-7` | 2026-04-16 ³ | January 2026 ² | January 2026 ² | Stage 2F integrative analysis under v18.4 (G1 / G2 / G3 / all-papers × s2f v6 / v7 / v7.1). |
| **Claude Opus 4.6** | `claude-opus-4-6` | 2026-02-05 ⁴ | May 2025 ² | August 2025 ² | Stage 2F baseline runs under the v17 configuration; cited in the SI-6 historical comparison only. |
| **Claude Haiku 4.5** | `claude-haiku-4-5-20251001` | 2025-10-15 ⁵ | February 2025 ² | July 2025 ² | SI-6 four-model cross-comparison on Kumada 1972 (v17). |
| **GPT-5.4 Thinking** | `gpt-5.4-thinking` (three files); "GPT-5.4 Thinking" elsewhere | 2026-03-05 ⁶ | August 2025 ⁷ | August 2025 ⁷ ‡ | Cross-vendor arm of SI-6 on Kumada 1972 (v17). |

**Models whose outputs are in this deposit but that support no claim in the paper.** These outputs are kept as the raw record of work performed. Their exact snapshots were not recorded, so no release date or cutoff is given.

| Model (as recorded) | Where | Status |
|---|---|---|
| GPT-5.5 Thinking | EP-10a provenance check (SI-3.7) and ad-hoc Stage 4 cross-check (SI-11.1 model-use ledger) | Cross-check only; not part of the SI-6 four-model set |
| GPT-5.5 (as recorded: `GPT-5` / `GPT-5.5`) | `papers/dev/kumada/decon_2026-07/gpt55_run1–5/` (30 files) and `gpt55_prompts/` | A cross-vendor replication of the decontamination control, run alongside the Sonnet 4.6 arm reported in Methods 6; not reported in the paper and supports no claim |
| Gemini 1.5 Pro | v17 trial mentioned in SI-6 | Not run under the model-pinned v17 protocol; internal methodology record only (SI-6) |
| Claude Opus 4.8 | `tier_8_…/dev_set/murai/multirun/` (Murai retrieval-depth study) | Raw record only; the study's summary values are withdrawn (§5) |
| "Claude Sonnet" (snapshot not recorded) | Murai retrieval-depth outputs | Raw record only |
| Claude 3.5 Haiku | `devset_kumada_v15_haiku.md` (v15 era) | Historical v15 record |

`tier_3_stage_outputs/context_analyses/uchino1970/` *(reviewer version only; redacted Markdown copies under `tier_8_redacted_public_raw_outputs/`)* holds the merged Stage 1 output only (no per-turn files), as produced in May 2026; the other three context analyses carry per-turn files. Two further provenance caveats: `test_set/app2/app2_v17_sonnet_s3.md` and `_s4.md` self-report `claude-sonnet-4-5`, and three Kumada v18.4 files dated 2026-06-01 self-report `claude-sonnet-4-6-20251101`, which predates the model's release. Both are the model's own report of its identity inside the output text and are known to be unreliable; the execution configuration for these runs was Sonnet 4.6.

**Source URLs (accessed 2026-06-28)**:
- ¹ Sonnet 4.6 announcement: [`https://www.anthropic.com/news/claude-sonnet-4-6`](https://www.anthropic.com/news/claude-sonnet-4-6)
- ² Anthropic cutoff data — official models overview page (Sonnet 4.6 / Haiku 4.5 in "Latest models", Opus 4.7 / Opus 4.6 in "Legacy models" Accordion): [`https://docs.anthropic.com/en/docs/about-claude/models/overview`](https://docs.anthropic.com/en/docs/about-claude/models/overview)
- ³ Opus 4.7 announcement: [`https://www.anthropic.com/news/claude-opus-4-7`](https://www.anthropic.com/news/claude-opus-4-7)
- ⁴ Opus 4.6 announcement: [`https://www.anthropic.com/news/claude-opus-4-6`](https://www.anthropic.com/news/claude-opus-4-6)
- ⁵ Haiku 4.5 announcement: [`https://www.anthropic.com/news/claude-haiku-4-5`](https://www.anthropic.com/news/claude-haiku-4-5). (Note: API ID `claude-haiku-4-5-20251001` reflects the model snapshot date 2025-10-01; the public release / general-availability date is 2025-10-15.)
- ⁶ GPT-5.4 (Thinking variant) announcement: [`https://openai.com/index/introducing-gpt-5-4/`](https://openai.com/index/introducing-gpt-5-4/)
- ⁷ GPT-5.4 Thinking system card: [`https://deploymentsafety.openai.com/gpt-5-4-thinking`](https://deploymentsafety.openai.com/gpt-5-4-thinking); the GPT-5.4 family knowledge cutoff is August 31, 2025 (per OpenAI release-notes corpus).

**‡** OpenAI does not publish a separate "training data cutoff" distinct from the "knowledge cutoff" in the GPT-5.4 Thinking system card; the August 2025 entry above is the unified knowledge cutoff per OpenAI documentation. This contrasts with Anthropic's two-field convention (reliable-knowledge cutoff + training-data cutoff). Reviewers should interpret the GPT-5.4 Thinking entries accordingly.

**Note**: Per-run execution dates are recorded in the individual `.md` output files (filename includes execution date or batch ID); aggregate execution-date ranges are summarised in §3 below.

### Reconciliation note (2026-06-28)

The 2026-05-22 initial draft of this manifest reported "Claude Sonnet 4.6 (2025-09 release)" and "Claude Opus 4.6 (2025-09 release)". Both were incorrect: September 2025 was the release date of **Claude Sonnet 4.5** (`claude-sonnet-4-5-20250929`), not Sonnet 4.6 or Opus 4.6. The corrected dates above (Sonnet 4.6: 2026-02-17; Opus 4.6: 2026-02-05) are consistent with the aggregate execution-date ranges in §3 (all phases run April–May 2026, i.e. after both models' release).

---

## 2. Prompt-version × Model × Stage matrix

The cells indicate which prompt × model combinations were executed for which stages. Production-run cells are bolded.

| Prompt | Sonnet 4.6 | Opus 4.7 | Opus 4.6 | Haiku 4.5 | GPT-5.4 Thinking |
|---|---|---|---|---|---|
| v15 | S0–S2 dev set | — | — | — | — |
| v16 | S0–S2 dev set | — | — | — | — |
| v16.1 | S0–S2 dev set + 10 test | — | — | — | — |
| v17 | S0–S4 dev + test + EP filling | S0–S4 dev (cross-model SI-6) | Stage 2F G1/G2/G3/all × s2f/v7/v7.1 (cited historically) | S0–S4 dev (cross-model SI-6) | S0–S4 dev (cross-model SI-6, cross-vendor) |
| v18 | S0–S2 dev (refinement) | — | — | — | — |
| v18.1 | S0–S2 dev (refinement) | Stage 2F integrative | — | — | — |
| v18.2 | S0–S2 dev (refinement) | — | — | — | — |
| v18.3 | S0–S2 dev (cross-model protocol formalisation) | — | — | — | — |
| **v18.4** | **S0–S2 + Stage 3 v2 EN + Stage 4 v2 EN: development set (N = 6 per language cell) and the nine EP-context papers (single runs). The ten refinement-set papers were not re-run at v18.4 (their outputs are v15–v17).** | **Stage 2F G1/G2/G3/all × s2f/v7/v7.1 (production)** | — | — | — |

---

### Stage 2F version-stamp note (recorded 2026-06-13)

The matrix above lists Stage 2F **v7** and **v7.1 (s2fv71)** as distinct prompt versions. Reviewers should be aware: all v7.1 (`s2fv71`) output files carry the internal header `prompt_version: stage2f-v7-20260417` — a header carry-over from v7 (the prompt file `prompt_stage2f_v71.md` itself declares this string at the top). This is a known metadata-stamp bug and does **not** affect output content.

The v7.1 configuration is identified unambiguously by (i) the filename suffix `s2fv71` and (ii) `tier_1_prompt_versions/…/prompt_stage2f_v71.md`. v6 / v7 / v7.1 are three distinct prompt versions; the internal stamp will be corrected in a future prompt version (v19) — see `improvements/_prompts/v19_prompt_improvement_backlog_20260613.md` (F10 / Spec-4). The frozen deposit retains the original stamp for run-provenance fidelity.

---

## 3. Aggregate execution-date ranges

| Phase | Date range | Scope |
|---|---|---|
| Phase 1 (initial refinement) | 2026-04-12 — 2026-04-15 | v15 → v17 cycle on dev set + 10 test |
| Phase 1.5 (post-v17 cycle) | 2026-04-19 — 2026-04-22 | 4-model cross-validation (SI-6); EP-10a addition; ChemOntology Layer A draft |
| Phase 2 (v18 refinement) | 2026-04-23 — 2026-05-02 | v17 → v18.4 cycle, cross-model verification protocol formalisation |
| Phase 3 (English-only conversion) | 2026-05-03 — 2026-05-12 | v18.4 EN baseline on dev set + 8 EP filling + Tamao 2002 (the 10 refinement-set papers were not re-run); Stage 2F EN under Opus 4.7 |
| Phase 4 (multi-run aggregation) | 2026-05-10 | N=6 multi-run on Kumada + Murai × {JA, EN} × {S2, S3, S4} |
| Phase 5 (audit + retrieval) | 2026-05-13 — 2026-05-22 | EP-03a/07a/08a/09a structured-database audit; pre-submission integrity audits; editorial passes; rhetoric prompt validation |

---

## 4. Files referenced by manuscript

### Top-level files included via tier structure

- **Paper A UQS prompts**: `tier_1_prompt_versions/` holds 86 prompt files: the Stage 0–2 prompts of the 9 versions v15, v16, v16.1, v17, v18, v18.1, v18.2, v18.3, v18.4 (67 files, one folder per version: the v15→v17 refinement cycle of Results Part 4 and the v18.4 production configuration, with the English Stage 2 prompts and, for v18.4, the Stage 1 Turn 4 textbook-pilot variants); at the top level, Stage 3 v1 / v2 / v2 EN / v3 / v4 (5 files), Stage 4 v1 / v2 / v2 EN / v3 / v6 (5 files) and Stage 2F v6 / v7 / v7.1 (3 files); and the v19 Stage 0–2 prompts of the reproducibility control's successor-version arm (`v19_successor_arm/`, 6 files; Methods 6, SI-7 rows 24–29). SI-7 lists the SHA-256 of 29 of these files (the prompts it tabulates), and those 29 match; `MANIFEST.csv` gives the SHA-256 of all 86. v0–v14 are exploratory / superseded prompts not used by the published analyses and are excluded; later prompt versions are not deposited.
- **21-paper corpus manifest**: see `tier_2_input_metadata/paperA_21_paper_corpus_manifest.csv`.
- **21-paper Stage 0–4 + Stage 2F outputs**: see `tier_3_stage_outputs/` *(reviewer version only; redacted Markdown copies under `tier_8_redacted_public_raw_outputs/`)* organised as `dev_set/` (2 papers), `test_set/` (10 Heck papers), `ep_historical_case_study/` (8 historical + 1 Tamao 2002 mini-review), `stage2f_integration_outputs/` (24 Stage 2F output files for the G1 / G2 / G3 / all-papers × s2f v6 / v7 / v7.1 cells under both v17 Opus 4.6 and v18.4 Opus 4.7, plus the Kumada 1972 Stage 3 anchor file).
- **Methodology-evolution record**: see `tier_7_aggregation_scripts_and_methodology_evolution/` (regression_log; changelogs v17–v184; session handovers v15→v16 + v16.1).
- **Cross-model verification**: see `tier_7` (cross_model_verification_protocol.md + cross_model_kumada_vs_murai_meta.md).
- **v17 twelve-paper aggregate metrics**: see `tier_7` (v17_twelve_paper_metrics.csv + extract_v17_metrics.sh + README).

### Application-direction artifact (scope-limited)

- **ChemOntology Layer A** (Paper A Kumada-1972 scope): `application_direction_chemontology_layer_a/ep_to_chemontology_mapping.md` + `mapping_verification_log.md`.
- Layer B / Layer C / Phase 2 NiCl₂(dpe) execution: **deferred to Paper B Zenodo deposit** (in preparation, Yoshioka et al.).
- A second Layer A mapping (Pd amidocarbonylation system) belongs to later work of the project and is not deposited here.

### Per-reference verification catalogue

- 29 chemistry / empirical references with BIB caches and per-reference analysis records (source PDFs are not deposited): `per_reference_catalogue/refs_catalogue_29_of_31/` *(reviewer version only)* (= `papers/refs/`).
- Refs 2 (Althusser & Balibar 1965) and 3 (Macherey 1966): not digitally available; cited as historical acknowledgments in the "symptomatic reading" lineage (SI-0.2).
- Four cross-coupling references added during revision (Murahashi 1975, Martin & Buchwald 2007, Terao & Kambe 2002, Jones & Vicic 2005 — refs 19, 20, 35, 36) are cited for context only and are not part of the verification catalogue.

---

## 5. Reproducibility notes

### Sonnet stochasticity

Sonnet 4.6 outputs are stochastic; single-run rank order within the Top-3 reinforcement EP SET varies from run to run. In the revision the SET was re-counted mechanically from the 24 per-run Stage 3 records under three extraction rules stated before counting (`tier_4_classification_tables/reaggregation_R1/`, SI-3). For Kumada 1972 each EP of {EP-03a, EP-04a, EP-06a} appears in the top three of 67–100% of runs per language cell; for Murai 1993 the SET is stable in the English cell but not in the Japanese cell (EP-04a 33–50%). The earlier statement that the SET met a ≥75% inclusion frequency for both papers is withdrawn.

### Model-version reproducibility

The exact model snapshots may not be available indefinitely. Reproducibility is therefore conditional on the model identifier table above; re-execution under newer model versions may produce different point outputs. The deposited records support audit of the published outputs without re-execution.

### Per-run execution dates

Per-run execution dates are encoded in the `.md` output files. A summary CSV mapping (paper × stage × model × prompt × run) → execution date can be generated on request; this CSV is not auto-generated for the staging folder but will be added before public deposit if reviewers request a single-file index.

### Superseded summary values — Murai multi-run study (recorded 2026-08-31)

`tier_8_redacted_public_raw_outputs/dev_set/murai/multirun/` contains an eighteen-run Stage 4
retrieval-depth study on Murai 1993 (three models × two prompt versions × three fresh runs),
together with the contemporaneous summary memo `murai_multirun_summary_20260612.md`.

A pre-submission audit on 2026-08-29 found that the study's candidate ledger is keyed at
author–year granularity rather than at paper identity: one run can list the same paper as
several rows under different Evidence Packs, and verification verdicts attach to author–year
bins rather than to paper identities. The memo's derived statistics are therefore
author–year-bin statistics and are not valid at the paper level. The affected headline values
are the Kakiuchi 1995 BCSJ recurrence (`15 / 18 runs`), the verified-candidate count
(`101 / 125`), the per-arm failure rates (`32 % / 14 % / 13 %`), and the within-cell Jaccard
range (`0.08–0.55`). These values are **superseded and must not be reused**. The withdrawal is
not repaired by recounting, because the derived statistics share the key defect. The raw
per-run output files are unaffected and are unchanged.

Four files in that directory carry the correction, all byte-identical (SHA-256) to the
working-repository originals:

| File | Role |
|---|---|
| `RECOUNT_NOTE_20260829.md` | The finding, a deterministic strict-identity recount, and the registered repair path. Supersedes the memo's headline values. |
| `murai_multirun_summary_20260612.md` | The memo itself, now carrying its `⚠️ SUPERSEDED` banner. The copy staged on 2026-06-29 predated the banner and was refreshed on 2026-08-31; the pre-banner copy remains in this repository's version history. | (R1, 2026-10-05: the copies under `tier_3_stage_outputs/dev_set/murai/multirun/` *(reviewer version only; redacted Markdown copies under `tier_8_redacted_public_raw_outputs/`)* and `per_reference_catalogue/.../ref03_murai1993/existing_uqs_dir/multirun/` *(reviewer version only)* had not been refreshed and still held the pre-banner version. Both now hold the bannered version, with the recount note and the two ledger TSVs beside them, byte-identical to the working-repository originals.)
| `murai_multirun_candidates.tsv` | The primary candidate ledger (125 rows). Deposited so that the strict-identity recount, which is derived from this file alone, can be reproduced by a reader. |
| `murai_multirun_verifications.tsv` | The verification ledger (45 rows), whose author–year keying is the defect itself. |

Tier 8 redaction status of the two ledgers: they contain no `quote:` / `key_quote:` /
`target_*` fields and no verbatim source-paper excerpts. Their only quoted strings are article
titles, which the Tier 8 policy classes as public bibliographic information and does not
redact. They are therefore deposited unmodified.

**Scope for this deposit.** No claim in Paper A is derived from these values; the four
superseded quantities appear nowhere in the manuscript or its Supporting Information. Paper A's
multi-run evidence is the N = 6 Stage 3 and Stage 4 aggregation on the development set, re-counted
in the revision from the per-run records (SI-3); it is not affected by the ledger-keying defect. (The
statement in the 2026-08-31 version of this paragraph that a "24-run Kumada Stage 4 pilot" was
reported "as 24/24 and 23/24 in the main text" was itself wrong: the 24/24 value counted runs whose text
mentioned an inversion, and the 23/24 value could not be traced to any record of this paper; both are withdrawn
in the revision.) The Murai multi-run study is deposited as a raw
record of work performed, not as evidence for any statement in the paper. The correction is
mirrored here so that this deposit and the companion UQS 2.0 deposit, which withdraws the same
values, carry the identical correction record.

---

## 6. Manifest update history

| Date | Update |
|---|---|
| 2026-05-22 | Initial manifest created at staging-folder construction. |
| 2026-06-13 | Stage 2F v7.1 version-stamp note added (§2 supplement) recording the known internal-header carry-over in `s2fv71` outputs. |
| 2026-06-25 | Tier 1 narrowed to Paper A-used prompts only (removed v0–v14 and non-Paper-A stage2f3 prompts); Tier 2 narrowed to the 21-paper manifest CSV (removed parent Heck corpus + the corpus roster of later work of the project); Tier 3 reorganised into 4 subdirs (dev_set / test_set / ep_historical_case_study / stage2f_integration_outputs); Tier 6 narrowed to Paper A audit material (removed project-wide inventory.tsv); ChemOntology narrowed to Layer A core files (removed the mapping of later work of the project and stale Discussion 2 insertion draft). Manifest §4 updated to reflect the new file-level structure. |
| 2026-06-28 | Tier 4 split into `figures_data/` + `figures_output_pdf_png_svg/` (CSV source data + rendered figure outputs as separate concerns). Tier 7 rendering scripts narrowed from the whole `figures/scripts/` folder to the six data-driven scripts (fig2 / fig3 / fig4 / fig5 / figS1 / render_tables) per SI-11.11 Tier 7 spec ("Figs. 2–5, SI Fig. S1") and chemistry-community convention; the three presentation-artifact scripts (`fig1_uqs_pipeline.py` schematic, `scheme1_kumada_reaction.py` chemistry scheme, `graphical_abstract.py` editorial artwork) are not deposited (rendered PDF/PNG/SVG outputs remain available under Tier 4 for reviewer reference). |
| 2026-06-28 | Manifest §1 release-date and cutoff placeholders fully resolved via direct fetch of the Anthropic models overview page, the four Anthropic news announcements, and the OpenAI GPT-5.4 / GPT-5.4 Thinking pages. Source URLs added as footnotes 1–7. The 2026-05-22 initial draft's "Sonnet 4.6 / Opus 4.6 (2025-09 release)" entries were corrected to 2026-02-17 / 2026-02-05 (the September 2025 date belonged to Sonnet 4.5, not Sonnet 4.6 or Opus 4.6); the corrected dates are consistent with the §3 aggregate execution-date ranges. |
| 2026-08-31 | §5 correction record added for the Murai multi-run study: the four superseded headline values of `murai_multirun_summary_20260612.md` are identified; `RECOUNT_NOTE_20260829.md` and the two ledger TSVs are deposited into `tier_8_.../dev_set/murai/multirun/`; and the memo itself is refreshed to the banner-carrying version (the 2026-06-29 staged copy predated the 2026-08-29 banner). All four files are SHA-256 identical to the working-repository originals. The TSVs carry no verbatim source-paper excerpts and are deposited unredacted per the Tier 8 bibliographic-information exemption. No Paper A claim is affected. |
| 2026-09-28 | First-round revision (Digital Discovery). Title corrected (the 2026-05-22 draft title had been left in place). §1: identifier column added from the `model_info` lines of the deposited outputs; models whose outputs are deposited but support no claim are listed separately; two self-report caveats recorded. §2 / §3: the v18.4 scope is corrected (the refinement set was not re-run at v18.4; Stage 3 v2 EN / Stage 4 v2 EN named). §5: the ≥75% Top-3 statement and the 24/24 inversion statement are replaced by the revision's re-count; the 2026-08-31 scope paragraph is corrected. |

### Models used in the revision studies (added 2026-10-05)

- Held-out set, single-prompt baselines and B2 -> Stage 3: Claude Sonnet 4.6 (`claude-sonnet-4-6`, from the CLI usage records deposited next to each run).
- Haiku 4.5 replication (2026-09): `claude-haiku-4-5` / `claude-haiku-4-5-20251001` as recorded in each output's `model_info`.
- LLM raters (benchmark cells, SRG-root mapping, Stage 3 fill passages): two Claude subagents run from the authors' Claude Code session. Their model version was not recorded. Every rating was checked by an author (SI-6.10, SI-11.20).
