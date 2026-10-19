# EP-08a — WoS + Scopus hit counts

| Database | Variant | Hit count | Date executed | Notes |
|---|---|---|---|---|
| WoS Core Collection | A (strict) | **3** | 2026-05-20 | All 3 not applicable per 0B §4. Negative claim strengthened. See `wos_variant_a_analysis.md`. |
| WoS Core Collection | B (relaxed methodology) | **1** | 2026-05-20 | 1 hit = Pd-Kumada paper (Cornacchio 2009 PdCl₂(dppf)); catalyst class mismatch. Not applicable per 0B §4. See `wos_variant_b_analysis.md`. |
| WoS Core Collection | C (cis/trans time-course) | **7** | 2026-05-20 | 7 hits, all in non-Kumada contexts (Pt-stilbene, Ni-cyclam, mesoporous oxidation, photochemistry, Mg(I) chemistry). All not applicable per 0B §4. See `wos_variant_c_analysis.md`. |
| WoS Core Collection | D (strict phrase) | **0** | 2026-05-20 | "Kumada-Tamao OR Kumada-Corriu" hyphenated phrase + replicate variability terms returned zero papers. See `wos_variant_d_analysis.md`. |
| WoS Core Collection | D′ (AND co-occurrence) | **0** | 2026-05-20 | (Kumada AND Tamao) OR (Kumada AND Corriu) + replicate variability terms returned zero papers. Rules out hyphen-syntax artifact. |
| WoS Core Collection | D″ (NEAR/3 proximity) | **0** | 2026-05-20 | Kumada NEAR/3 Tamao OR Corriu + replicate variability terms returned zero papers. Three orthogonal formulations all return zero — robust negative diagnostic. |
| Scopus | A | — | pending | — |
| Scopus | B | — | pending | — |
| Scopus | C | — | pending | — |
| Scopus | D | — | pending | — |


**Re-run 2026-10-05** (same query strings): A **2** (Zhou 2020 no longer returned; the other 2 records identical), B 1, C 7, D/D′/D″ 0 — see `wos_reexport_20261005/README.md` (deposit) / `manuscript_A/DigitalDiscovery_R1/01_response/wos_reexport_20261005/` (repo). The table above is the 2026-05-20 record and is left unchanged.
