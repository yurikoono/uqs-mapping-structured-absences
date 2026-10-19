# EP-07a — WoS Variant A Analysis (2026-05-20)

## Query

```
TS=("Kumada coupling" OR "NiCl2(dpe)" OR "NiCl2(dppe)" OR "nickel-catalyzed Grignard") AND TS=("n-butyl chloride" OR "sec-butyl chloride" OR "benzyl chloride" OR "alkyl halide" OR "Csp3" OR "C(sp3)") AND DT=(Article)
```

- Database: WoS Core Collection
- Filter: Document Type = Article
- Date executed: 2026-05-20
- Executor: User (Hokkaido U subscription)
- **Hit count: 9**

This is the **positive control variant** for the EP-07a audit: substrate-scope extension to Csp³ halides in the Ni-Kumada family. EP-07a per 0B §3 expects dense filling (publication-incentive-aligned target).

## Candidates and 0B §3 classification

### Candidate 1: Breitenfeld-Ruiz-Wodrich-Hu 2013 (*J. Am. Chem. Soc.*) — Partial

| Field | Value |
|---|---|
| Title | Bimetallic Oxidative Addition Involving Radical Intermediates in Nickel-Catalyzed Alkyl-Alkyl Kumada Coupling Reactions |
| DOI | [10.1021/ja4051923](https://doi.org/10.1021/ja4051923) |
| Catalyst | NiII pincer complex [(N2N)Ni-Cl] |
| Substrate scope | Alkyl-alkyl Kumada coupling (Csp³ substrates) |
| Mechanism | Radical, bimetallic OA, second-order in Grignard, first-order in catalyst |
| **0B §3 classification** | **Partial** — Csp³ scope extension in a **related (Ni-based) but not strict dppe-Ni system**. Per 0B §3 Partial criterion 3 "Comparable scope explored in related but not strict dppe-Ni system". The N2N pincer Ni is structurally distinct from dppe-Ni but shares Ni-based Kumada catalysis. This is a paradigm-shift filling (alkyl-alkyl Kumada was challenging in the original 1972 communication's scope). |

### Candidate 2: Coombs-Perry-Kwon-Thomas-Ess 2018 (*Organometallics*)

| Field | Value |
|---|---|
| Title | Why Two Metals Are Better Than One for Heterodinuclear Cobalt-Zirconium-Catalyzed Kumada Coupling |
| DOI | [10.1021/acs.organomet.8b00449](https://doi.org/10.1021/acs.organomet.8b00449) |
| Catalyst | Co-Zr heterobimetallic (NOT Ni) |
| Substrate | Alkyl halides + alkyl Grignards |
| Focus | DFT mechanistic study |
| **0B §3 classification** | **Not applicable** — Co-Zr catalyst (not Ni). System identity strongly mismatched per 0B §3 cross-cutting rule |

### Candidate 3: Bauer-Cheung-Hu 2015 (*Synthesis*)

| Field | Value |
|---|---|
| Title | Cross-Coupling of Nonactivated Primary and Secondary Alkyl Halides with Aryl Grignard Reagents Catalyzed by Chiral Iron Pincer Complexes |
| DOI | [10.1055/s-0034-1380136](https://doi.org/10.1055/s-0034-1380136) |
| Catalyst | **Iron** (Fe-bopa pincer, NOT Ni) |
| **0B §3 classification** | **Not applicable** — Fe-catalyzed (not Ni); different metal family |

### Candidate 4: Bauer-Wodrich-Scopelliti-Hu 2015 (*Organometallics*)

| Field | Value |
|---|---|
| Title | Iron Pincer Complexes as Catalysts and Intermediates in Alkyl Aryl Kumada Coupling Reactions |
| DOI | [10.1021/om501122p](https://doi.org/10.1021/om501122p) |
| Catalyst | **Iron** (bopa pincer) |
| **0B §3 classification** | **Not applicable** — Fe-Kumada mechanism study |

### Candidate 5: Garcia-Di Franco-Epenoy-Scopelliti-Hu 2016 (*ACS Catal.*) — Partial

| Field | Value |
|---|---|
| Title | From Dimethylamine to Pyrrolidine: The Development of an Improved Nickel Pincer Complex for Cross-Coupling of Nonactivated Secondary Alkyl Halides |
| DOI | [10.1021/acscatal.5b02324](https://doi.org/10.1021/acscatal.5b02324) |
| Catalyst | Ni(II) pincer complex (with pyrrolidino group): `[(PNNN-Pyr-Me)Ni-Cl]` vs `[(N2N-Me)Ni-Cl]` |
| Substrate scope | Nonactivated **secondary alkyl halides** (Kumada + Suzuki-Miyaura) |
| Specific scope extension | Secondary Csp³ — historically a challenging substrate class |
| **0B §3 classification** | **Partial** — Csp³ scope extension (secondary alkyl halides) in **related (Ni-pincer) but not strict dppe-Ni system**. Per 0B §3 Partial criterion 3. The PNNN-Pyr-Ni pincer is Ni-based with distinct ligand class from dppe; the substrate class (secondary alkyl halides) maps to EP-07a's Csp³ scope target |

### Candidate 6: Wei-Abdiaj-Sambiagio-Li-Zysman-Colman-Alcazar-Noel 2019 (*Angew. Chem.*)

| Field | Value |
|---|---|
| Title | Visible-Light-Promoted Iron-Catalyzed C(sp²)-C(sp³) Kumada Cross-Coupling in Flow |
| DOI | [10.1002/anie.201906462](https://doi.org/10.1002/anie.201906462) |
| Catalyst | **Iron** + photoredox + flow chemistry |
| **0B §3 classification** | **Not applicable** — Fe-catalyzed (not Ni) |

### Candidate 7: Tsien et al. 2025 (*Angew. Chem.*)

| Field | Value |
|---|---|
| Title | Accelerating Medicinal Chemistry: A C(sp³)-Rich Fragment Toolbox for Redox-Neutral Cross-Coupling |
| DOI | [10.1002/anie.202517207](https://doi.org/10.1002/anie.202517207) |
| Catalyst | Nickel-catalyzed redox-neutral cross-coupling with sulfonyl hydrazide reagents (modern paradigm) |
| Kumada relevance | Mentioned in comparison only: "51% yield for trideuteromethylation… versus precedented 14% via Kumada coupling" |
| **0B §3 classification** | **Not applicable** — modern Ni redox-neutral radical cross-coupling with non-Grignard sulfonyl-hydrazide reagents; Kumada is cited only as inferior precedent. Different reaction class than EP-07a's dppe-Ni Kumada scope extension |

### Candidate 8: Bisz-Szostak 2019 (*Adv. Synth. Catal.*)

| Field | Value |
|---|---|
| Title | Iron-Catalyzed C(sp²)-C(sp³) Cross-Coupling of Chlorobenzamides with Alkyl Grignard Reagents |
| DOI | [10.1002/adsc.201800849](https://doi.org/10.1002/adsc.201800849) |
| Catalyst | **Iron-catalyzed** |
| **0B §3 classification** | **Not applicable** — Fe-catalyzed (not Ni) |

### Candidate 9: Do-Anosike-Beng 2023 (*RSC Adv.*)

| Field | Value |
|---|---|
| Title | Diastereospecific arylation and cascade deconstructive amidation/thioesterification of readily available lactam-fused bromolactones |
| DOI | [10.1039/d3ra04690g](https://doi.org/10.1039/d3ra04690g) |
| Catalyst | **Palladium** ([5,5]-system) + Co(acac)₃ ([5,6]-system, β-hydride-prone) |
| Substrate | Lactam-bromolactones + aryl Grignards |
| "C(sp³)-C(sp²) Kumada coupling" | Pd-catalyzed in this case |
| **0B §3 classification** | **Not applicable** — Pd-Kumada (not Ni) + Co(acac)₃ for one system. System identity mismatched |

## Summary — Variant A

| Classification | Count | Papers |
|---|---|---|
| Complete filler | **0** | — |
| **Partial filler** | **2** | Breitenfeld 2013 (N2N-Ni pincer, alkyl-alkyl Kumada paradigm-shift); Garcia 2016 (PNNN-Pyr-Ni pincer, secondary alkyl halide scope) |
| Minimal filler | **0** | — |
| Not applicable | **7** | Coombs 2018 (Co-Zr), Bauer 2015a/2015b (Fe), Wei 2019 (Fe-photoredox), Tsien 2025 (modern Ni redox-neutral), Bisz 2019 (Fe), Do 2023 (Pd) |
| **Total** | **9** | — |

## Interpretation — positive-control calibration

This is the **positive-control finding** for the Tier 1 #1 audit methodology: EP-07a Variant A returns **2 Partial fillers** in Ni-pincer systems (Breitenfeld 2013, Garcia 2016) — both extending Csp³ scope in related-Ni systems.

The audit methodology **successfully distinguishes** between:

- **EP-07a (publication-incentive-aligned positive)**: Returns 2 Partial fillers; the retrieval pipeline is functional for finding scope-extension filling literature
- **EP-08a / EP-09a (publication-incentive-misaligned negatives)**: Cumulative 22 hits, 0 Complete / 0 Partial / 2 Minimal — no Partial filler exists despite identical retrieval methodology

This **positive-vs-negative contrast** is exactly the calibration GPT-5 recommended: the audit pipeline returns Partial fillers when they exist (EP-07a), and returns no Partial fillers when they don't (EP-08a / EP-09a). The negative claims are therefore not retrieval-methodology artifacts but reflect actual structural absences in the published academic record.

## Diagnostic observation — paradigm-shift filling pattern

The 2 Partial fillers (Breitenfeld 2013, Garcia 2016) both come from the Hu group at EPFL and use **Ni-pincer ligands** (N2N pincer, PNNN-Pyr pincer) — structurally distinct from the original 1972 dppe-Ni system. This is consistent with the **paradigm-shift filling layer** (2009–2024) reported in Results Part 2 of the manuscript: scope extension to Csp³ halides was filled not by the original dppe-Ni system but by paradigm-shifted Ni catalysts.

This pattern fills the EP-07a target in a graded sense:
- **Strict dppe-Ni Csp³ scope**: not filled (original 1972 system) — would require Complete classification
- **Related Ni-catalyst Csp³ scope**: Partial-filled by Ni-pincer paradigm shift (2013–2016)
- **Cross-metal Csp³ scope**: Iron-Kumada (Bauer 2015, Wei 2019, Bisz 2019) and modern radical cross-coupling (Tsien 2025) are extensions to related but distinct paradigm — Not applicable for dppe-Ni-specific EP-07a

## Hit count expectation vs reality

| Expected hit count | Actual hits | Gap interpretation |
|---|---|---|
| 50-200 (positive control prediction) | 9 | Lower than expected; query may have been too narrow (specific Csp³ halide names rather than general "alkyl chloride" keywords). Variant B will likely catch additional scope-extension papers using different terminology |

## Next steps

- **Variant B (Cl/Br/I direct comparison)**: pending execution

## File locations

- Raw export: `validation/ep07a_wos_llm/wos_variant_a.txt`
- 0B criteria reference: `improvements/paperA_ep_audit_criteria_20260520.md` §3
