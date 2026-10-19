# EP-09a — WoS Variant B Analysis (2026-05-20)

## Query

```
TS=(nickel AND "cross-coupling") AND TS=("head-to-head" OR "side-by-side" OR "parallel reaction" OR "benchmark" OR "internal standard comparison") AND TS=(Grignard OR "RMgX") AND DT=(Article)
```

- Database: WoS Core Collection
- Filter: Document Type = Article
- Date executed: 2026-05-20
- Executor: User (Hokkaido U subscription)
- **Hit count: 1**

This variant targets direct benchmark vocabulary (`head-to-head` / `side-by-side` / `parallel reaction` / `benchmark` / `internal standard comparison`) combined with Ni cross-coupling + Grignard.

## Candidate and 0B §5 classification

### Candidate 1: Kosar et al. 2020 (*Int. J. Quantum Chem.*)

| Field | Value |
|---|---|
| Title | Benchmark approach to search of cost-effective and accurate density functional for homolytic cleavage of C-Mg bond of Grignard reagent |
| Authors | Naveen Kosar, Khurshid Ayub, Mazhar A. Gilani, Faheem Shah, Tariq Mahmood |
| Journal / Year / DOI | *Int. J. Quantum Chem.* 2020, 120, e26106 / [10.1002/qua.26106](https://doi.org/10.1002/qua.26106) |
| Subject area | **Computational / quantum chemistry — DFT methods benchmarking** |
| "Benchmark" usage | **Density functional theory method benchmark** (comparing 29 DFs × 3 basis sets for C-Mg bond dissociation energy calculation), NOT catalyst benchmark |
| "Grignard" usage | C-Mg bond of Grignard reagent as test substrate for DFT method comparison |
| Cross-coupling / nickel relevance | "Cross-coupling reactions" + "Nickel pincer complex" appear in Keywords Plus (auto-generated keywords), not in main paper focus |
| Subject classification (WoS Categories) | Chemistry-Physical, Mathematics-Interdisciplinary, Quantum Science & Technology, Physics-Atomic Molecular & Chemical |
| **0B §5 classification** | **Not applicable** — DFT methods benchmarking paper (comparing 29 density functionals for accuracy in C-Mg bond dissociation energy); not an experimental Ni-catalyst benchmark. The keyword combination of "benchmark" + "Grignard" + (via Keywords Plus) "cross-coupling" triggered the match but the paper's subject is computational methodology comparison, not Ni cross-coupling catalysis comparison |

## Summary — Variant B

| Classification | Count |
|---|---|
| Complete filler | **0** |
| Partial filler | **0** |
| Minimal filler | **0** |
| Not applicable | **1** |
| **Total** | **1** |

## Interpretation

Variant B applied a **direct benchmark-vocabulary** filter (`head-to-head` / `side-by-side` / `parallel reaction` / `benchmark` / `internal standard comparison`) combined with Ni cross-coupling + Grignard. Despite the explicit benchmark-language target, only **1 paper** matched — and it is a **DFT methods benchmarking paper** (theoretical chemistry) entirely unrelated to experimental Ni-catalyst comparison.

This is a **very strong signal for the EP-09a negative claim**. The vocabulary that EP-09a explicitly targets (head-to-head benchmark of dppe-Ni vs named predecessors) does not co-occur with Ni-cross-coupling-Grignard in WoS Core Collection. The only paper that does combine these keywords is using "benchmark" in a different sense entirely (computational methodology comparison).

## Diagnostic note — vocabulary gap as direct empirical support

The Variant B result quantifies the publication-incentive interpretation at the **vocabulary level**:

- Papers performing benchmark studies of cross-coupling catalysts presumably exist somewhere in the literature
- But papers using the explicit vocabulary of "head-to-head" / "side-by-side" / "parallel reaction" / "benchmark" in combination with Ni cross-coupling + Grignard appear to be effectively absent from WoS Core Collection
- This is consistent with the framing that **substrate-matched, condition-matched head-to-head benchmarking is structurally underwritten** in modern chemistry publishing — the methodology language itself does not surface

## EP-09a WoS Module — running cumulative (A + B)

| Variant | Hits | Complete | Partial | Minimal | Not applicable |
|---|---|---|---|---|---|
| A (strict named-benchmark) | 9 | 0 | 0 | 2 | 7 |
| B (head-to-head Ni-Grignard vocabulary) | 1 | 0 | 0 | 0 | 1 |
| **Cumulative (A + B)** | **10** | **0** | **0** | **2** | **8** |

## Next steps

- Variant C (predecessor catalyst comparison language): pending execution
- Variant D (Fe-Kumada vs Ni-Kumada same-substrate): pending execution

## File locations

- Raw export: `validation/ep09a_wos_llm/wos_variant_b.txt`
- Hit count summary: `validation/ep09a_wos_llm/hit_counts.md`
- Sibling Variant A analysis: `validation/ep09a_wos_llm/wos_variant_a_analysis.md`
