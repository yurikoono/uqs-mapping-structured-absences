# D3 held-out selection record (prereg `preregistration_D3_D4_R1.md`, commit 88e7cc3)

- `fetch_candidates.py` → `candidate_pool.csv` (2026-09-29): Crossref `query.bibliographic=Heck`,
  `from-online-pub-date:2026-02-01`, `type:journal-article`, with the title or abstract containing "Heck", plus the
  Heck rows of `corpus/corpus_paper_list.csv`. Each DOI was re-queried to obtain its date
  (`published-online`, falling back to `published-print`). 273 candidates, of which 76 are dated on or after 2026-02-01.
- `screen_and_draw.py` → `screening.csv`: criteria 1–4 were applied using the title and abstract only. 23 papers were
  excluded, each with its reason listed in the script. 53 were eligible and numbered 1–53 in DOI order.
  `random.Random(20260929).sample` gives the full replacement order (`draw_rank`).
- **Draw (ranks 1–4)**:

| rank | n | DOI | online | journal | OA |
|---|---|---|---|---|---|
| 1 | 25 | 10.1021/acs.joc.6c01425 | 2026-09-07 | J. Org. Chem. | closed |
| 2 | 34 | 10.1021/acs.orglett.6c03536 | 2026-09-12 | Org. Lett. | closed |
| 3 | 48 | 10.31635/ccschem.026.202607864 | 2026-07-10 | CCS Chem. | gold CC BY-NC |
| 4 | 19 | 10.1007/s44442-026-00106-5 | 2026-07-13 | J. Saudi Chem. Soc. | gold CC BY-NC-ND |

  Replacements, in order, if a PDF cannot be obtained: rank 5 = 10.1038/s41929-026-01579-8, rank 6 = 10.1021/acs.orglett.6c02415,
  rank 7 = 10.1002/ejoc.70790, rank 8 = 10.1021/acs.orglett.6c01921.
- Composition as drawn (not re-drawn, per §2.2): three homogeneous-catalysis synthetic-methodology papers (1–3)
  and one heterogeneous-catalyst paper (4). None is computational.
- Known limitation of the pool: Crossref abstracts are sparse, so papers that mention Heck only in the abstract are
  under-represented.
- Source PDFs are analysed locally only. They are never deposited (copyright hygiene).
