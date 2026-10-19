# EP-08a — WoS Variant A Analysis (2026-05-20)

## Query

```
TS=("Kumada" OR "Ni-catalyz*" OR "nickel-catalyz*") AND TS=("cross-coupling" OR "Grignard coupling") AND TS=("standard deviation" OR "replicate" OR "uncertainty" OR "error bar" OR "reproducibility") AND DT=(Article)
```

- Database: WoS Core Collection
- Filter: Document Type = Article
- Date range: not explicitly limited at search; results span 2020-2026
- Date executed: 2026-05-20
- Executor: User (Hokkaido U subscription)
- **Hit count: 3**

## Candidates and 0B classification

### Candidate 1: Zhou-Xu-Zhang-Kong 2020 (*Org. Chem. Front.*)

| Field | Value |
|---|---|
| Title | Nickel-catalyzed enantioselective electroreductive cross-couplings |
| Authors | Zhijun Zhou, Sheng Xu, Jing Zhang, Wangqing Kong |
| Journal / Year / DOI | *Org. Chem. Front.* 2020, 7, 3262–3265 / [10.1039/d0qo00901f](https://doi.org/10.1039/d0qo00901f) |
| Document type per abstract | **Highlight / review** ("In this highlight, we summarize the recent progress…") |
| Substrate class | Reductive cross-coupling of two electrophiles (NOT original Kumada Table I substrates) |
| Catalyst | Ni-catalyzed enantioselective (no dppe-Ni Kumada system) |
| Replicate / SD / time-course | NOT reported (highlight format) |
| "Reproducibility" mention context | Notes that excessive Zn powder reductant "poses severe challenges with respect to reproducibility" — this is the source of the keyword match, but the paper does not itself provide replicate measurements for Kumada Table I |
| **0B §4 classification** | **Not applicable** — reaction class (reductive electrophile-electrophile coupling) ≠ Grignard cross-coupling; document type (highlight) ≠ primary research with replicate data; system identity does not map back to dppe-Ni Kumada Table I |

### Candidate 2: Kurig-Cagan-Harper-Kawamata-Blackmond-Baran 2026 (*Angew. Chem. Int. Ed.*)

| Field | Value |
|---|---|
| Title | Arylhydrazines: Convenient Homogeneous Reductants for Scalable Cross-Coupling |
| Authors | Nils Kurig, David A. Cagan, Kaid C. Harper, Yu Kawamata, Donna G. Blackmond, Phil S. Baran |
| Journal / Year / DOI | *Angew. Chem. Int. Ed.* 2026, 65, 12 / [10.1002/anie.9252206](https://doi.org/10.1002/anie.9252206) |
| Substrate class | Reductive sp²-sp³ cross-coupling of aryl halides with secondary alkyl iodides (NOT original Kumada Table I Grignard substrates) |
| Catalyst | NiII precursor + bipyridine ligand + hindered amine base (NOT dppe-Ni) |
| Replicate / SD reporting | Calorimetry-guided safety + decagram-scale demonstrations mentioned (positive direction), but specifics not in abstract — would require full paper read |
| Head-to-head benchmark | "Direct comparisons reveal superior yields and selectivity relative to Zn-based methods" — comparison is to **Zn reductant**, NOT to Corriu/Masse Ni(acac)₂ / Tamura-Kochi Fe / Corey-Whitesides as required by 0B §5 for EP-09a |
| "Reproducibility" mention context | Reductive cross-couplings "often suffer from limitations associated with heterogeneous reductants like Zn (e.g., poor reproducibility and scalability)" — keyword match origin |
| **0B §4 classification** | **Not applicable** for EP-08a — different substrate class + different catalyst class (NiII / bipyridine ≠ dppe-Ni) + reductive cross-coupling paradigm ≠ Grignard cross-coupling; even if substrate were aligned, no per-Kumada-Table-I replicate SDs reported |
| **0B §5 classification** | **Minimal (cross-referenced for EP-09a)** — qualitative head-to-head superiority claim vs Zn baseline, not vs named Kumada-era predecessors |

### Candidate 3: Takahashi-Hu-Gao-Gao-Pang-Seo-Jiang-Maeda-Takaya-Kubota-Ito 2021 (*Nat. Commun.*)

| Field | Value |
|---|---|
| Title | Mechanochemical synthesis of magnesium-based carbon nucleophiles in air and their use in organic synthesis |
| Authors | Rina Takahashi, Anqi Hu, Pan Gao, Yunpeng Gao, Yadong Pang, Tamae Seo, Julong Jiang, Satoshi Maeda, Hikaru Takaya, Koji Kubota, Hajime Ito |
| Journal / Year / DOI | *Nat. Commun.* 2021, 12, 6691 / [10.1038/s41467-021-26962-w](https://doi.org/10.1038/s41467-021-26962-w) |
| Research focus | Mechanochemical synthesis of Grignard reagents via ball milling (in air); demonstrates downstream use in nucleophilic addition + nickel-catalyzed cross-coupling under solvent-free conditions |
| Catalyst | Ni-catalyzed cross-coupling demonstrated, specific catalyst (presumably bipy or phosphine class) not named in abstract |
| Replicate / SD reporting | NOT explicitly reported in abstract; paper focuses on the mechanochemical method as a methodological advance |
| "Reproducibility" mention context | "Often cause reproducibility problems" refers to conventional Grignard preparation method (the **problem** the paper addresses), not to systematic replicate measurement of dppe-Ni Kumada yields with reported SDs |
| **0B §4 classification** | **Not applicable** — research focus (mechanochemical Grignard synthesis in air) is methodologically tangential to EP-08a's target (n ≥ 3 replicates with SDs for dppe-Ni Kumada Table I). The Ni-cross-coupling demonstrated uses unspecified catalyst class and unspecified substrates; no per-substrate replicate data. **Boundary candidate** — if full paper read shows substrate matching + replicate reporting for the Kumada Table I substrates, could elevate to Minimal |

## Summary — Variant A

| Classification | Count | Notes |
|---|---|---|
| Complete filler | **0** | — |
| Partial filler | **0** | — |
| Minimal filler | **0** (1 boundary — Takahashi 2021 pending full-text read) | — |
| Not applicable | **3** | All 3 papers are off-target: 2 reductive cross-couplings (different paradigm), 1 mechanochemical Grignard synthesis (different focus) |

## Interpretation — preliminary

WoS Variant A (the strictest Kumada + cross-coupling + replicate/SD/uncertainty keyword combination) returns **3 papers, none of which provide systematic replicate measurements (n ≥ 3, with SDs) for the dppe-Ni Kumada Table I substrate set**. The 3 papers' "reproducibility" keyword matches arise from **mentioning reproducibility as a problem** (Zn powder reductant in cases 1 + 2; conventional Grignard synthesis in case 3), not from **providing replicate data**.

This is a **strong supporting signal for the EP-08a negative claim**. The structured WoS retrieval has independently failed to recover any Complete or Partial filler under 0B §4 criteria — consistent with the cross-model LLM-parametric retrieval finding (Sonnet + GPT-5.4 both report no filling).

The complementarity framing (per SI-9 EP-03a pilot diagnostic) holds: LLM retrieval and structured DB retrieval have **different but parallel** non-detection results for EP-08a.

## Next steps for this Module

- Variants B (relaxed methodology terms), C (cis/trans time-course), D (Kumada-named control) — pending user execution
- Scopus variants A-D — pending user execution
- Crossref API verification of candidates' DOIs — Claude TODO once full variant set is in
- Variant A interpretation conclusion: **negative claim strengthened**; if Variants B-D and Scopus also return ≤ 5 candidates with 0 Complete / 0 Partial, the EP-08a non-detection claim is well-defended for DD submission

## File locations

- Raw export (this Variant A): `validation/ep08a_wos_llm/wos_variant_a.txt`
- Hit count summary: `validation/ep08a_wos_llm/hit_counts.md` (to be created on next variant)
- 0B criteria reference: `improvements/paperA_ep_audit_criteria_20260520.md` §4
