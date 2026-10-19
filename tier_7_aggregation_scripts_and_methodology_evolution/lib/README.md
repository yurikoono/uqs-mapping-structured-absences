# Implementations used by the scoring scripts of the revision (`lib/`)

Copies of files of the project folder `scripts/`, byte for byte (checked when this package is built). The scoring scripts in `01_response/` and the two wrappers in `papers/dev/kumada/repro_2026-07/` use the project path when they run in the project repository and this folder when they run in this package. README §0 item 15 says how to re-run them.

- `repro_extract.py` — counts of A / B / C / U items, D-4 candidates and the canonical findings (two instruments, strict and loose) per run (`repro_metrics.csv`); also imported by `01_response/d3_heldout/check_heldout.py` and `01_response/d4_baseline/extract_cells*.py`.
- `repro_aggregate.py` — aggregates `repro_metrics.csv` into `repro_summary.md`.
- `verbatim_quote_gate.py` — the quote-provenance gate (fuzzy matching of each quoted string against the text layer of the source PDF, extracted with `pdftotext`; needs `rapidfuzz`); used by `01_response/d4_baseline/aggregate_d4.py`, `score_b2_stage3.py` and for the held-out gate files `01_response/d3_heldout/gate_*.json`.
- `verbatim_gate_corpus_scan.py` — runs the gate over several folders (`papers/_audits/paperA_quote_gate_R1_2026-09/`).
- `verbatim_quote_gate_20260720.py` — the gate as it was on 2026-07-20 (project commit `18a7325`), which wrote `papers/dev/kumada/repro_2026-07/verbatim_gate_20260720.json`; the later version gives different counts on the same runs.

The source PDFs are not deposited: the gate needs the reader's own copy of each paper (README §0 item 15).
