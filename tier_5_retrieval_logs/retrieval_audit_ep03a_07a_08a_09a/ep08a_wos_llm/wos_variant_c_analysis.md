# EP-08a — WoS Variant C Analysis (2026-05-20)

## Query

```
TS=("cis-stilbene" OR "trans-stilbene" OR "1,2-dichloroethylene" OR "1,2-dichloroethene") AND TS=("time-course" OR "time course" OR "kinetic" OR "thermodynamic" OR "isomerization") AND TS=("Ni" OR "nickel" OR "Grignard") AND DT=(Article)
```

- Database: WoS Core Collection
- Filter: Document Type = Article
- Date executed: 2026-05-20
- Executor: User (Hokkaido U subscription)
- **Hit count: 7**

This variant directly targets EP-08a case-specific implementation (iii): "time-course (1 h, 5 h, 20 h) to distinguish kinetic vs thermodynamic product" on cis/trans-1,2-dichloroethylene substrates.

## Candidates and 0B classification

### Candidate 1: Wicht et al. 1998 (*Organometallics*)

| Field | Value |
|---|---|
| Title | Platinum(0) complexes of chiral diphosphines: Enantioface-selective binding of trans-stilbene |
| DOI | [10.1021/om971000j](https://doi.org/10.1021/om971000j) |
| Topic | Pt(0)(diphos)(trans-stilbene) complexes; enantioface-selective binding by chiral diphosphines |
| trans-stilbene role | **Ligand of Pt(0) organometallic complex** (not coupling product) |
| Ni / cross-coupling relevance | None (Pt not Ni; no coupling reaction) |
| **0B §4 classification** | **Not applicable** — Pt complex chemistry; trans-stilbene used as ligand, not as Kumada substrate or product |

### Candidate 2: Nattmann-Cornella 2020 (*Organometallics*)

| Field | Value |
|---|---|
| Title | Ni(4-tBustb)₃: A Robust 16-Electron Ni(0) Olefin Complex for Catalysis |
| DOI | [10.1021/acs.organomet.0c00485](https://doi.org/10.1021/acs.organomet.0c00485) |
| Topic | Ni(0) tris-stilbene precatalyst design and stability characterisation |
| Stilbene role | **Ligand of Ni(0) precatalyst** (4-tBu-stilbene as supporting ligand) |
| "Kinetic" mention context | "Faster kinetic profiles" of the precatalyst in Ni-catalysed transformations |
| Replicate / SD / time-course on Kumada Table I | None |
| **0B §4 classification** | **Not applicable** — precatalyst design paper; stilbene used as ligand for Ni(0), not as Kumada coupling target |

### Candidate 3: Solans-Monfort et al. 2011 (*Dalton Trans.*)

| Field | Value |
|---|---|
| Title | O-O Bond activation in H₂O₂ and (CH₃)₃C-OOH mediated by [Ni(cyclam)(CH₃CN)₂](ClO₄)₂ |
| DOI | [10.1039/c0dt01605e](https://doi.org/10.1039/c0dt01605e) |
| Topic | Ni-cyclam oxidation chemistry; peroxide O-O bond activation |
| cis-stilbene role | **Oxidisable substrate for Ni(III) quenching** (not coupling target) |
| Ni-Kumada relevance | None (Ni-cyclam oxidation, not cross-coupling) |
| **0B §4 classification** | **Not applicable** — oxidation chemistry; cis-stilbene as oxidisable substrate |

### Candidate 4: Iwamoto-Tanaka 2001 (*Catal. Surv. Jpn.*)

| Field | Value |
|---|---|
| Title | Preparation of metal ion-planted mesoporous silica by template ion-exchange method and its catalytic activity for asymmetric oxidation of sulfide |
| DOI | [10.1023/A:1012257731538](https://doi.org/10.1023/A:1012257731538) |
| Topic | Heterogeneous catalysis on mesoporous MCM-41; metal ion-planted catalysts |
| trans-stilbene role | **Epoxidation substrate** for Mn-MCM-41 catalyst test (trans-stilbene oxide product) |
| "Time course" mention context | Time course of template ion-exchange process (catalyst preparation), not stilbene reaction kinetics |
| Ni-Kumada relevance | None |
| **0B §4 classification** | **Not applicable** — heterogeneous oxidation chemistry; trans-stilbene as epoxidation substrate |

### Candidate 5: Iwamoto 2004 (*J. Synth. Org. Chem. Jpn.*)

| Field | Value |
|---|---|
| Title | What can we expect from mesoporous materials in the field of heterogeneous catalysis? |
| DOI | [10.5059/yukigoseikyokaishi.62.411](https://doi.org/10.5059/yukigoseikyokaishi.62.411) |
| Topic | Review of mesoporous catalysts |
| Document type | Review article |
| Ni mention | Ni ion combined with M41 for ethene → propene metathesis (not Kumada) |
| **0B §4 classification** | **Not applicable** — review of heterogeneous mesoporous catalysis; Ni reactions are metathesis-type, not Kumada |

### Candidate 6: El-Agamey-Fukuzumi 2012 (*Chem. Eur. J.*)

| Field | Value |
|---|---|
| Title | The Remarkable Effect of the Manganese Ion with Dioxygen on the Stability of π-Conjugated Radical Cations |
| DOI | [10.1002/chem.201201328](https://doi.org/10.1002/chem.201201328) |
| Topic | Carotenoid radical cation kinetics by nanosecond laser flash photolysis |
| trans-stilbene role | **Electron donor in radical cation studies** (1,4-dicyanonaphthalene photosensitized ET); Ni(ClO₄)₂ tested as metal ion |
| Ni-Kumada relevance | None (Ni(ClO₄)₂ as radical-cation-stabiliser, not catalyst) |
| **0B §4 classification** | **Not applicable** — photochemistry of radical cations; trans-stilbene as electron donor; Ni as metal ion test, not catalyst |

### Candidate 7: Dange et al. 2019 (*Chem. Sci.*)

| Field | Value |
|---|---|
| Title | Acyclic 1,2-dimagnesioethanes/-ethene derived from magnesium(i) compounds: multipurpose reagents for organometallic synthesis |
| DOI | [10.1039/c9sc00200f](https://doi.org/10.1039/c9sc00200f) |
| Topic | Mg(I) dimer 1,2-addition reactions; 1,2-di-Grignard reagent chemistry |
| trans-stilbene role | **Substrate for Mg(I) bond 1,2-addition** (not Kumada coupling product) |
| Ni / cross-coupling relevance | None (Mg(I) main-group chemistry; some di-Grignard reagent applications mentioned but not Kumada) |
| **0B §4 classification** | **Not applicable** — Mg(I) main-group chemistry; trans-stilbene as substrate for Mg-Mg bond addition |

## Summary — Variant C

| Classification | Count |
|---|---|
| Complete filler | **0** |
| Partial filler | **0** |
| Minimal filler | **0** |
| Not applicable | **7** |

## Interpretation

Variant C targeted the most chemistry-specific aspect of EP-08a — time-course discrimination of kinetic vs thermodynamic products for cis/trans-stilbene or 1,2-dichloroethylene substrates with Ni / Grignard chemistry. All 7 hits surface "trans-stilbene" or "cis-stilbene" + "kinetic / time course" + "Ni / Grignard" co-occurrences, but **none are in the Kumada cross-coupling context**.

The 7 hits reveal a useful taxonomy of how stilbene appears in the published literature:

1. **As ligand of organometallic complex** (Wicht 1998 Pt, Nattmann 2020 Ni(0))
2. **As oxidisable substrate** (Solans-Monfort 2011 Ni-cyclam, Iwamoto 2001 Mn-MCM-41)
3. **As mesoporous-catalysis epoxidation product** (Iwamoto 2001, 2004)
4. **As electron donor in photochemistry** (El-Agamey 2012)
5. **As substrate for Mg(I) bond addition** (Dange 2019)

None of these are the Kumada-coupling-product cis/trans-1,2-dichloroethylene with n ≥ 3 replicate measurement on per-Table-I-entry yields. The negative claim is consistent across all 7 candidates.

## Diagnostic note (Variant C-specific)

The high stilbene-mention diversity across non-Kumada chemistry domains illustrates an important retrieval property: **broadly-used model substrates appear in many unrelated contexts**, but their use in the specific Kumada-coupling-product role required by EP-08a is rare. Structured keyword retrieval cannot distinguish substrate role (ligand vs product vs electron donor vs oxidisable target) at the query level — this requires per-candidate content reading. The 0B §4 rule "filling must be in the dppe-Ni Kumada system OR explicitly mapped back" handles this cleanly by requiring application-context match.

## Combined Variant A + B + C running total (EP-08a)

| Variant | Hits | Complete | Partial | Minimal | Not applicable |
|---|---|---|---|---|---|
| A (strict Ni + reproducibility) | 3 | 0 | 0 | 0 | 3 |
| B (Ni-specific + replicate methodology) | 1 | 0 | 0 | 0 | 1 |
| C (cis/trans + kinetic + Ni/Grignard) | 7 | 0 | 0 | 0 | 7 |
| **Total (A + B + C)** | **11** | **0** | **0** | **0** | **11** |

## Next steps

- Variant D (Kumada-named control: Kumada-Tamao / Kumada-Corriu + replicate variability terms) — pending execution
- Scopus variants A-D — pending execution
- Crossref API verification of all candidates' DOIs — Claude TODO after Module 2 fully complete

## File locations

- Raw export: `validation/ep08a_wos_llm/wos_variant_c.txt`
- Hit count summary: `validation/ep08a_wos_llm/hit_counts.md`
- Sibling Variant A / B analyses: `validation/ep08a_wos_llm/wos_variant_{a,b}_analysis.md`
