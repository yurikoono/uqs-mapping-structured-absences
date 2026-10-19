# Web of Science raw exports — status (R1, 2026-09-28; re-export added 2026-10-05)

In the submitted package, seven files named `wos_variant_*.txt` under `ep07a_wos_llm/`, `ep08a_wos_llm/`
and `ep09a_wos_llm/` were byte-identical (SHA-256 of the redacted copy `a37ca338e295c096…`). Only
`ep08a_wos_llm/wos_variant_a.txt` is genuine: its records match the DOIs in
`ep08a_wos_llm/wos_variant_a_analysis.md`. The other six were copies of it saved under the wrong names, so the
raw exports behind those six query variants were missing. The six copies are removed in this version:

- `ep07a_wos_llm/wos_variant_a.txt`
- `ep08a_wos_llm/wos_variant_b.txt`
- `ep08a_wos_llm/wos_variant_c.txt`
- `ep09a_wos_llm/wos_variant_a.txt`
- `ep09a_wos_llm/wos_variant_b.txt`
- `ep09a_wos_llm/wos_variant_c.txt`

The per-variant analyses (`wos_variant_*_analysis.md`) and hit-count tables (`hit_counts.md`) are those of
the original searches of 2026-05-20; a dated re-run note is appended to each `hit_counts.md`.

**Re-export (2026-10-05).** All twelve EP-07a / EP-08a / EP-09a queries were re-run verbatim and the six missing
exports re-generated; they are in `wos_reexport_20261005/` (plus a re-run of EP-08a A for comparison with its genuine May export).
Eleven hit counts are unchanged and every returned record is one already classified in the May analyses; no new
record appeared. EP-08a Variant A returned 2 records instead of 3 (Zhou et al. 2020, 10.1039/d0qo00901f,
classified Not applicable in May, is no longer returned). No classification changes. Details:
`wos_reexport_20261005/README.md`; SI-9.8.6.

The EP-03a exports (`ep03a_wos_llm/wos_variant_{a,b,c,d}.txt`, `wos_raw_49hits.txt`) are distinct files and are
not affected. All exports carry facts only (abstract, Keywords Plus and funding fields removed).
