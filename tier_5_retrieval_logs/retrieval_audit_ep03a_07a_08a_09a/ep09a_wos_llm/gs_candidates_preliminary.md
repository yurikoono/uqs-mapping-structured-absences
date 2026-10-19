# EP-09a — Google Scholar / open-web preliminary candidates (2026-05-20)

**Status:** Preliminary discovery via WebSearch + WebFetch verification. Pending user-side WoS / Scopus structured execution.

## Candidate 1: Kambe et al. (2002)

| Field | Value |
|---|---|
| Title | Nickel-catalyzed cross-coupling reaction of Grignard reagents with alkyl halides and tosylates: remarkable effect of 1,3-butadienes |
| Authors | Jun Terao, Hideyuki Watanabe, Aki Ikumi, Hitoshi Kuniyasu, Nobuaki Kambe |
| Journal / Year / DOI | *J. Am. Chem. Soc.* 2002 / [10.1021/ja025828v](https://doi.org/10.1021/ja025828v) / PMID 11960446 |
| Substrates | Primary + secondary alkyl + aryl Grignard reagents × alkyl chlorides / bromides / tosylates |
| Catalyst comparison | Qualitative: "Nickel complexes bearing no phosphine ligands (NiCl₂, Ni(acac)₂, Ni(COD)₂) afford coupling products in good yields, whereas NiCl₂(PPh₃)₂ and NiCl₂(dppp) were less effective" |
| Matched-conditions numerical table | **None** — no formal quantitative yield/selectivity comparison table at matched conditions |
| Named predecessor comparison (Corriu/Masse Ni(acac)₂ / Tamura-Kochi Fe / Corey-Whitesides stoichiometric) | **None** |
| Main contribution | 1,3-Butadiene additive effect (NOT catalyst benchmark) |
| **0B §5 classification** | **Minimal** — qualitative catalyst-class comparison exists but no head-to-head matched-conditions numerical benchmark; benchmark is not the paper's focus |

**Audit decision rationale**: Per 0B §5 Minimal criterion "mention of 'predecessor catalysts' without numerical comparison" — Kambe 2002's catalyst-class observation is qualitative and methodological aside. It does not meet 0B §5 Partial conditions (which require 1 benchmark with same substrate + matched conditions OR all 3 with different substrates / conditions). Classified Minimal.

## Candidate 2: Hazari-Melvin-Beromi (2017) Nature Reviews Chemistry

| Field | Value |
|---|---|
| Title | Well-defined nickel and palladium precatalysts for cross-coupling |
| Authors | Nilay Hazari, Patrick R. Melvin, Megan Mohadjer Beromi |
| Journal / Year / DOI | *Nat. Rev. Chem.* 2017 / [10.1038/s41570-017-0025](https://doi.org/10.1038/s41570-017-0025) / PMC5637737 |
| Scope | Review article — well-defined Ni and Pd precatalysts for cross-coupling |
| Head-to-head benchmark with named predecessors | **None** — no substrate-matched, condition-matched numerical benchmark between dppe-Ni Kumada and Corriu/Masse Ni(acac)₂ / Tamura-Kochi Fe / Corey-Whitesides |
| Quantitative comparison tables | **No** tables comparing Ni-Kumada predecessor catalysts at matched substrates with reported yield + selectivity + operability |
| Content focus | Modern precatalyst architectures; historical discussion only |
| **0B §5 classification** | **Minimal** — historical discussion of dppe-Ni development without numerical benchmark tables. Review article boundary case per 0B §5: "Review articles citing both Corriu and Kumada → Citation alone is Minimal, not Partial. Only numerical comparison data counts." |

**Audit decision rationale**: As a review of modern precatalysts (post-2010 era), the paper acknowledges Kumada-1972 era predecessors historically but does not perform the substrate-matched, condition-matched numerical benchmark that 0B §5 Complete or Partial conditions require. Classified Minimal.

## Candidate 3: NiCl₂(dppe)-Catalyzed Suzuki-class cross-coupling (out of scope)

| Field | Value |
|---|---|
| Title | NiCl₂(dppe)-Catalyzed Cross-Coupling of Aryl Mesylates, Arenesulfonates, and Halides with Arylboronic Acids |
| Source | [J. Org. Chem.](https://pubs.acs.org/doi/abs/10.1021/jo049940i) |
| Reaction class | Suzuki-class (Ni + arylboronic acid) |
| **0B §5 classification** | **Not applicable** — reaction class is Suzuki, not Kumada Grignard cross-coupling. Out of EP-09a scope. |

**Audit decision rationale**: Per 0B §5 the EP target is the dppe-Ni Kumada Grignard system. Suzuki-class Ni reactions are outside EP-09a scope regardless of catalyst overlap.

## Open-web search summary

WebSearch query: `"NiCl2(dpe)" OR "NiCl2(dppe)" "Ni(acac)2" head-to-head benchmark comparison Grignard coupling` (2026-05-20)

**Top 8 results scanned**:

1. NiCl₂(dppe) Suzuki cross-coupling (Candidate 3, out of scope)
2. Kambe 2002 (Candidate 1, Minimal)
3. Stereospecific Ni cross-coupling with benzylic ethers (different reaction system)
4. Hazari-Melvin-Beromi 2017 review (Candidate 2, Minimal)
5. Other tangential results

**Preliminary finding**: Multiple qualitative catalyst-class observations exist in the Ni cross-coupling literature, but **no same-substrate, same-condition head-to-head numerical benchmark with named predecessors** (Corriu/Masse Ni(acac)₂; Tamura-Kochi Fe; Corey-Whitesides) surfaces in open-web check. This is preliminary support for the EP-09a negative claim; structured WoS / Scopus will refine.

## Pending actions

- User to execute WoS / Scopus Variants A-D queries per master execution plan
- WebFetch the Stereospecific Ni-Kumada (result #3) to confirm out-of-scope or boundary
- Crossref API verification of all candidates (DOI-level checks)
