# EP-09a — WoS Variant A Analysis (2026-05-20, updated with full abstracts)

## Query

```
TS=("NiCl2(dpe)" OR "NiCl2(dppe)" OR "Kumada coupling" OR "dpe-Ni" OR "dppe-Ni") AND TS=("Ni(acac)2" OR "nickel acetylacetonate" OR "Corriu" OR "Masse" OR "Tamura-Kochi" OR "Corey-Whitesides") AND DT=(Article)
```

- Database: WoS Core Collection
- Filter: Document Type = Article
- Date executed: 2026-05-20
- Executor: User (Hokkaido U subscription)
- **Hit count: 9**

This variant targets the strict named-benchmark scenario for EP-09a: Kumada-system catalyst syntax combined with named predecessor catalyst terms (Corriu/Masse Ni(acac)₂, Tamura-Kochi Fe, Corey-Whitesides stoichiometric).

## Candidates and 0B §5 classification (with abstracts)

### Candidate 1: Park-Buck-Rizzo 1998 (*Tetrahedron*)

| Field | Value |
|---|---|
| Title | A convenient synthesis of 3,6-substituted carbazoles via nickel catalyzed cross-coupling |
| DOI | [10.1016/S0040-4020(98)00786-8](https://doi.org/10.1016/S0040-4020(98)00786-8) |
| Substrates | 3,6-dibromocarbazole + alkyl/vinyl/aryl Grignard reagents |
| Catalyst | Nickel-catalysed (specific ligand not stated in abstract) |
| "Corriu-Kumada coupling" usage | Reaction-name attribution ("via nickel catalyzed coupling with Grignard reagents (Corriu-Kumada coupling)") |
| Head-to-head benchmark | None |
| **0B §5 classification** | **Not applicable** — carbazole-synthesis-focused application paper; "Corriu-Kumada coupling" used as reaction-name parenthetical; no benchmark against named predecessors at matched conditions |

### Candidate 2: Matsubara et al. 2017 (*Organometallics*)

| Field | Value |
|---|---|
| Title | Dinuclear Systems in the Efficient Nickel-Catalyzed Kumada-Tamao-Corriu Cross-Coupling of Aryl Halides |
| DOI | [10.1021/acs.organomet.6b00451](https://doi.org/10.1021/acs.organomet.6b00451) |
| Catalyst | **Dinuclear Ni(I) with bulky NHC ligands** (NOT dppe-Ni) |
| Substrates | Aryl halides |
| Research focus | Active species identification via stoichiometric + kinetic experiments; reveals monovalent and divalent dinickel species as active |
| "Kumada-Tamao-Corriu" usage | Reaction-name attribution (per 1972 IUPAC-style historic naming) |
| Head-to-head benchmark vs named predecessors | None — within-dinuclear-Ni mechanistic study, not predecessor comparison |
| **0B §5 classification** | **Not applicable** — confirmed via abstract. Dinuclear NHC-Ni(I) catalyst design (not dppe-Ni); mechanistic focus on active-species identification; no benchmark against Corriu Ni(acac)₂ / Tamura Fe / Corey-Whitesides at matched conditions |

### Candidate 3: Sun-Li-Sun 2014 (*Dalton Trans.*)

| Field | Value |
|---|---|
| Title | [CNN]-pincer nickel(II) complexes of N-heterocyclic carbene (NHC) |
| DOI | [10.1039/c4dt00461b](https://doi.org/10.1039/c4dt00461b) |
| Catalyst | [CNN]-pincer Ni(II) + NHC-amine arms (NOT dppe-Ni) |
| Substrate | Unactivated aryl chlorides or dichlorides |
| **0B §5 classification** | **Not applicable** — pincer-NHC Ni catalyst design, not dppe-Ni vs predecessor benchmark |

### Candidate 4: Soler-Yanes et al. 2014 (*Eur. J. Org. Chem.*) — KEY UPDATE FROM ABSTRACT

| Field | Value |
|---|---|
| Title | Nickel-Catalyzed Kumada Coupling of Benzyl Chlorides and Vinylogous Derivatives |
| DOI | [10.1002/ejoc.201403007](https://doi.org/10.1002/ejoc.201403007) |
| **Catalyst (abstract-confirmed)** | **Ni(acac)₂-TMEDA** (Ni(acac)₂ + N,N,N',N'-tetramethylethylenediamine) |
| Substrate | Benzyl chlorides + allyl chlorides + alkylmagnesium reagents |
| Comparison | None — paper uses Ni(acac)₂-TMEDA as the **chosen** catalyst for new substrate scope, NOT as a benchmark target |
| Mechanism note | "Reaction seems to follow a radical pathway" |
| **0B §5 classification** | **Not applicable** — paper uses Ni(acac)₂ (the named predecessor catalyst class) for a new substrate scope, but NOT as a head-to-head benchmark vs dppe-Ni at matched conditions. The keyword match arose because the paper *uses* Ni(acac)₂, not because it *benchmarks* dppe-Ni against it. |
| **Diagnostic note** | This is an informative **boundary observation** for Discussion 1: post-1972 literature continues to use Ni(acac)₂ as a chosen catalyst for new substrate scopes — but this is "predecessor catalyst still in active use" rather than "predecessor catalyst benchmarked against dppe-Ni at matched conditions". Consistent with publication-incentive interpretation: choosing an existing catalyst for new substrates yields novelty; benchmarking the existing catalyst against another existing catalyst does not. |

### Candidate 5: Quesnelle-Snieckus 2018 (*Synthesis-Stuttgart*) — Minimal

| Field | Value |
|---|---|
| Title | Directed ortho Metalation (DoM)-Linked Corriu-Kumada, Negishi, and Suzuki-Miyaura Cross-Coupling Protocols: A Comparative Study |
| DOI | [10.1055/s-0037-1611053](https://doi.org/10.1055/s-0037-1611053) |
| Comparison axis (abstract-confirmed) | **Suzuki-Miyaura vs Negishi vs Corriu-Kumada** (3 cross-coupling reaction classes, DoM-linked context) |
| Comparison granularity | **Qualitative only**: "Suzuki-Miyaura and Negishi protocols show greater scope and better yields than the Corriu-Kumada variant, although the latter qualitatively proceeds at fastest rate but has low functional group tolerance" |
| Substrate-matched + condition-matched numerical benchmark | NO |
| Comparison with named predecessor Ni-Kumada catalysts (Corriu Ni(acac)₂; Tamura Fe; Corey-Whitesides) | NO (compares between cross-coupling reaction classes, not within Ni-Kumada catalyst family) |
| **0B §5 classification** | **Minimal** — comparative paper but on a **different axis** (cross-reaction-class) than the EP-09a target (within-Ni-Kumada predecessor benchmark). Qualitative cross-protocol comparison; no numerical matched-condition data |

### Candidate 6: Wei et al. 2019 (*Angew. Chem. Int. Ed.*)

| Field | Value |
|---|---|
| Title | Visible-Light-Promoted Iron-Catalyzed C(sp²)-C(sp³) Kumada Cross-Coupling in Flow |
| DOI | [10.1002/anie.201906462](https://doi.org/10.1002/anie.201906462) |
| Catalyst | **Iron** (Fe) under photoredox / flow chemistry |
| **0B §5 classification** | **Not applicable** — Fe-catalysed Kumada (different metal); no head-to-head with dppe-Ni at matched conditions |

### Candidate 7: Matsubara et al. 2019 (*Molecules*)

| Field | Value |
|---|---|
| Title | Fluorine-Substituted Arylphosphine for an NHC-Ni(I) System |
| DOI | [10.3390/molecules24183222](https://doi.org/10.3390/molecules24183222) |
| Catalyst | NHC-Ni(I) with fluorine-substituted arylphosphine (not dppe-Ni) |
| Focus | Solid-state stability; structural characterisation |
| **0B §5 classification** | **Not applicable** — NHC-Ni(I) catalyst design, not predecessor benchmark |

### Candidate 8: Berding et al. 2009 (*Dalton Trans.*) — Minimal (verbal superiority claim)

| Field | Value |
|---|---|
| Title | N-donor functionalized N-heterocyclic carbene nickel(II) complexes in the Kumada coupling |
| DOI | [10.1039/b905036a](https://doi.org/10.1039/b905036a) |
| Catalyst | N-donor functionalised NHC-Ni(II) (cis amido, trans benzimidazolato) |
| Substrate | Phenylmagnesium chloride + 4-chloroanisole / 4-fluoroanisole |
| Activity claim | "Shows the **highest activity in this reaction reported to date**, yielding the desired product in quantitative yields within 30 min (4-chloroanisole) or 150 min (4-fluoroanisole) with only 1 mol% catalyst" |
| Head-to-head numerical comparison with named predecessors | NO — verbal superiority claim "reported to date" without numerical matched-condition table |
| **0B §5 classification** | **Minimal** — per 0B §5 Minimal criterion "Verbal claim of superiority without head-to-head data". Strong verbal claim of "highest activity reported to date" but does not provide substrate-matched + condition-matched numerical benchmark against Corriu Ni(acac)₂ / Tamura Fe / Corey-Whitesides as 0B §5 Partial requires |

### Candidate 9: Li et al. 2016 (*Tetrahedron*)

| Field | Value |
|---|---|
| Title | Newly-generated Al(OH)₃-supported Pd nanoparticles-catalyzed Stille and Kumada coupling reactions |
| DOI | [10.1016/j.tet.2015.10.069](https://doi.org/10.1016/j.tet.2015.10.069) |
| Catalyst | **Pd nanoparticles** (not Ni); heterogeneous Pd/Al(OH)₃ |
| **0B §5 classification** | **Not applicable** — Pd-catalysed (not Ni); heterogeneous nanoparticle |

## Summary — Variant A (updated)

| Classification | Count | Papers |
|---|---|---|
| Complete filler | **0** | — |
| Partial filler | **0** | — |
| **Minimal filler** | **2** | Quesnelle-Snieckus 2018 (cross-reaction-class qualitative comparison); Berding 2009 (verbal "highest activity reported to date" without head-to-head data) |
| Not applicable | **7** | Park 1998, Matsubara 2017, Sun 2014, Soler-Yanes 2014, Wei 2019, Matsubara 2019, Li 2016 |
| **Total** | **9** | — |

## Interpretation

WoS Variant A returned 9 papers. **None provide substrate-matched + condition-matched numerical benchmark of dppe-Ni Kumada vs named predecessor catalysts** (Corriu/Masse Ni(acac)₂; Tamura-Kochi Fe; Corey-Whitesides stoichiometric) per 0B §5 Complete or Partial criteria. The 2 Minimal candidates are at the weakest end of the inclusion criteria (cross-reaction-class qualitative comparison; verbal superiority claim without matched-condition data).

## Diagnostic observation — Soler-Yanes 2014 boundary case

Soler-Yanes 2014's use of Ni(acac)₂-TMEDA as the chosen catalyst for benzyl/allyl-chloride scope-extension reveals an interesting pattern: **post-1972 chemistry literature continues to use Ni(acac)₂ (the Corriu/Masse predecessor catalyst) as an active catalyst of choice for new substrate scopes**, but **does not benchmark dppe-Ni against Ni(acac)₂ at matched conditions**.

This is exactly the publication-incentive pattern Discussion 1 articulates:
- Using an existing catalyst for new substrates = publishable novelty ✓
- Benchmarking existing catalyst against another existing catalyst at matched conditions = no novelty, rarely published ✗

The structural absence of EP-09a-class benchmarks is therefore consistent with both:
1. LLM-parametric retrieval cross-model convergence (Sonnet + GPT-5.4)
2. Open-web preliminary check (Kambe 2002 / Hazari 2017)
3. **WoS Variant A structured retrieval (this analysis, 9 hits)**

The convergence of three independent retrieval modes on "0 head-to-head numerical benchmark with named predecessors" is the strongest form of the EP-09a negative finding available without exhaustive multi-database + per-paper full-text reading.

## Next steps

- Variant B (head-to-head Ni comparison terms): pending execution
- Variant C (predecessor catalyst comparison language): pending execution
- Variant D (Fe-Kumada vs Ni-Kumada same-substrate): pending execution

## File locations

- Raw export (full abstracts version): `validation/ep09a_wos_llm/wos_variant_a.txt`
- Hit count summary: `validation/ep09a_wos_llm/hit_counts.md`
- 0B criteria reference: `improvements/paperA_ep_audit_criteria_20260520.md` §5
