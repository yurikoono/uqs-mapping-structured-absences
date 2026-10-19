# Quote-provenance gate over the analyses cited by Paper A (R1, 2026-09-28)

Replaces, for Paper A, the July 2026 corpus-wide audit `papers/_audits/sonnet46_retro_2026-07/`, which the submitted
Methods 6 cited. That audit covered about a thousand papers outside Paper A and its own report records that its raw
rates were overstated by a reference-loading bug (fixed in `scripts/verbatim_gate_corpus_scan.py`).

## Scope and procedure

- Script: `scripts/verbatim_gate_corpus_scan.py` (fixed version; two counting sites also updated on 2026-09-28 to
  accept the gate's later `PASS_SPLICED` status), calling `scripts/verbatim_quote_gate.py`. Non-model, mechanical
  fuzzy matching of every quoted string against the source PDF and, where present, its Supporting Information.
- Stages 0–2 outputs (`*_s0.md`, `*_s1.md`, `*_s2.md`) of the analyses the manuscript cites:
  - development set and EP-context papers, v18.4 (as submitted; run from the submission snapshot):
    Kumada 1972, Murai 1993, kumada1976b, monnereau2009, breitenfeld2014, cherney2015, molander2016, molken2016,
    mazet2021, pengfei2024, tamao2002 → `gate_v184_devset_epcontext.{json,log}`
  - refinement set, v17 (the ten Heck papers; outputs unchanged since April 2026, run from the repository folders so
    that the Supporting Information PDFs obtained in August 2026 are available) → `gate_v17_refinement_set.{json,log}`
- Primary metric: `key_quote` fields (anchors that claim to be lifted from the paper).

## Results

| Set | key_quotes | PASS | PASS_FUZZY | WARN | FAIL |
|---|---|---|---|---|---|
| v18.4 (development set; the EP-context outputs carry no key_quote fields) | 33 | 27 | 6 | 0 | 0 |
| v17 refinement set | 78 | 32 | 22 | 23 | 1 |

## Manual adjudication (v17 refinement set)

The one FAIL and the seven WARN with partial-match score below 70 were checked by hand against the PDF, the Supporting
Information and, where needed, the rendered figure images:

| Paper | Output | Quote (abridged) | Score | Finding |
|---|---|---|---|---|
| HET-1 | s2 | "Alternative neutral mechanism with L' = anionic ligand (e.g., OAc⁻) is possible but unlikely." | 52.4 (FAIL) | **Genuine** — text inside Figure 8 (not in the text layer) |
| HOM-1 | s2 | "Geometry optimization: B3LYP/6-31G(d) (LANL2DZ for Pd) / Single point energy …" | 57.1 | **Genuine** — SI computational details, joined across lines |
| COMP-2 | s2 | "V_MAX B°_NO₂ = 5.20 E-05 … V_MAX M = 3.01 E-05 …" | 57.7 | **Genuine values** — SI Figure S55 (two panels joined and relabelled) |
| HET-1 | s1 | [REDACTED: verbatim source quotation; see the source paper via its DOI] | 68.9 | **Genuine caption**; the bracketed annotation is the model's own and does not match the reaction studied (4-iodobenzonitrile and tert-butyl acrylate, Figure 8) |
| APP-2 | s1 turn 2 | "Phosphoric acid and acetonitrile were found to be unsuitable; Pd(OAc)₂ and nBu₂N were found to be a suitable catalyst and base combination" | 62.0 | **Misreports the source** — the paper states that Pd(OAc)₂, acetonitrile and nBu₃N were suitable |
| APP-2 | s1 turn 1 | "On gram scale, product 6 was obtained in 31% yield, 94% ee" | 64.8 | **Misreports the source** — Scheme 3 gives the gram-scale result for compound 5 (81%, 94% ee) |
| APP-2 | s1 | "19, 33%, 43% ee" | 68.0 | **Misreports the source** — Scheme 3 gives 33%, 83% ee |
| HOM-1 | s1 | "Entry 1 (no ligand): 86% conv., 3a 76%, 3b 10%, 3d 0%, overall 10%" | 67.9 | **Not located** — Table 1 entry 1 is ligand L7 (86%, 12%, 41%, 10%, 63%); no matching row in the paper or SI |

The 16 WARN with score 73–91 are near-verbatim (typography, sub/superscripts, line joins) and were not adjudicated
individually.

## Reading

In the v18.4 analyses on which the paper's findings rest, every key_quote anchor matches the source. In the v17
refinement-set analyses, at least four key_quote anchors (three in APP-2, one in HOM-1) do not faithfully report the
source; three of the four involve values read from scheme or table images. These analyses are cited only for
the structural-coherence statement in Results Part 4.

## Model-identity check

`model_identity_audit.log`: `python3 scripts/registry_helper.py audit-provenance --scan-fs <dir>` over the submitted
`papers/dev/kumada`, `papers/dev/murai`, `papers/test` and `papers/ep` folders, comparing each output's filename model
tag with the verbatim `model_info` line it records. Kumada 112 files, Murai 86, EP 133: 0 mismatches. Refinement set
153 files: 2 mismatches, both in APP-2 (`app2_v17_sonnet_s3.md`, `_s4.md` record `claude-sonnet-4-5`); this is the
model's self-report inside the output and is noted in `zenodo_manifest.md` §1.

---

> **Public-cut redaction notice**: verbatim quotations from the analysed papers in this file have been replaced by `[REDACTED: …]` markers (rules in the repository README). The unredacted file is in the reviewer version of the deposit.
