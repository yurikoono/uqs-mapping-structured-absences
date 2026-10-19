# Control experiments of the revision (`papers/`) — *Mapping Structured Absences in Scientific Papers* (Ono, Yoshioka, Taketsugu)

**Purpose.** The materials for the **four control experiments reported in Methods 6 of the revised manuscript** (measured in SI-11.18). They postdate the deposit shared with the submitted manuscript (2026-06-30; an unpublished Zenodo record) and are part of this revised deposit (concept DOI 10.5281/zenodo.23437447; see README). Paths below are the `papers/...` paths cited in the manuscript, relative to the package root, so a reader following a citation lands on the file.

**Prepared.** 2026-09-07 from the repository state at commit `eba0f89`; included in the revised deposit as built on 2026-10-16 (the files are unchanged since their experiment dates; see the per-directory READMEs / evaluation notes). The file counts were taken when this package was built.

| Path | Control experiment (Methods 6 paragraph) | Contents | Files |
|---|---|---|---|
| `papers/dev/kumada/decon_2026-07/` | Prompt-exemplar contamination and decontamination control (Stages 0–2, N = 5, Sonnet 4.6; plus a GPT-5.5 replication of the same decontaminated prompts) | `prompts_decon/` (the two replaced passages), `run1`–`run5` (Sonnet 4.6 outputs), `gpt55_run1`–`5` + `gpt55_prompts/` (GPT-5.5 arm; the `PASTE_run*.txt` files are the author-written session prompts), `decon_evaluation_2026-07.md` (adjudication) | 78 |
| `papers/dev/kumada/repro_2026-07/` | Run-to-run variability of absolute counts (Stages 0–2, N = 5 per prompt version) | per-run S0/S1/S2 outputs, `repro_metrics.csv`, extraction / aggregation scripts, `canon.json` (seven benchmark findings), `verbatim_gate_20260720.json` | 40 |
| `papers/_audits/paperA_quote_gate_R1_2026-09/` | Paper A-scoped model-identity check and quote-provenance gate (R1 re-run) | `README.md` (audit report), gate result JSON for the two tranches (`quote` fields are the ≤ 240-character key-quote anchors already present in the deposited outputs; no source full text; redacted in the public cut), the model-identity audit log and the two gate scan logs | 6 |
| `papers/dev/kumada/s4_exemplar_control_2026-08/` | Stage 4 exemplar control (v6 vs v6-decontaminated, N = 5 per arm, alternating) | ten run outputs, `candidates.json`, `crossref_adjudication.json` | 13 |

**Copyright hygiene.** No source-paper PDFs, OCR full texts, page scans or WoS export prose. The 5 `.txt` files in these folders (`decon_2026-07/gpt55_prompts/PASTE_run*.txt`) are author-written session prompts, not source text. In this cut the `quote` fields of the `_audits` gate JSON (the short key-quote anchors that the analyses in the reviewer version quote) are redacted like every other quote field.

**Integrity.** The SHA-256 of every file is listed in `CHECKSUMS.sha256` at the package root; verify with `shasum -a 256 -c CHECKSUMS.sha256` run from the package root.

**Related correction record.** The superseded Murai multi-run summary and its recount note (`RECOUNT_NOTE_20260829.md`) are in `tier_3_stage_outputs/dev_set/murai/multirun/` *(reviewer version only; redacted Markdown copies under `tier_8_redacted_public_raw_outputs/`)*.

**Input-ablation control.** The pre-registered input-ablation control (`papers/ablation_provenance/`, SI-11.19) is included in this package; see `README_input_ablation.md`.
