# EP-08a — Google Scholar / open-web preliminary candidates (2026-05-20)

**Status:** Preliminary discovery via WebSearch + WebFetch verification. Pending user-side WoS / Scopus structured execution.

## Candidate 1: Joshi-Pangu et al. (2011)

| Field | Value |
|---|---|
| Title | Nickel-Catalyzed Kumada Cross-Coupling Reactions of Tertiary Alkylmagnesium Halides and Aryl Bromides/Triflates |
| Source | [PMC8036247](https://pmc.ncbi.nlm.nih.gov/articles/PMC8036247/) |
| Substrates | **tert-BuMgCl + aryl bromides / triflates** (NOT Kumada 1972 11 Table I substrates) |
| Catalyst | NiCl₂·(H₂O)₁.₅ + **NHC ligand** (NOT dppe / NiCl₂(dpe)) |
| Replicates | "Average isolated yields of two runs" footnote; **no SDs reported** |
| Time-course | **None reported** |
| Head-to-head benchmark | **None** with Corriu/Masse Ni(acac)₂ or Tamura-Kochi Fe or Corey-Whitesides |
| **0B §4 classification** | **Not applicable** (system distance: NHC catalyst ≠ dppe-Ni; substrate class ≠ Kumada 1972 Table I; no SD reporting even if substrates aligned) |
| Notable secondary finding | The paper documents that NiCl₂ hydration state affects reproducibility — a useful methodological note but not systematic replicate data |

**Audit decision rationale**: Per 0B §4 cross-cutting rule "System identity — filling must be in the dppe-Ni Kumada system OR explicitly mapped back". This paper is NHC-catalysed on tertiary alkyl-Mg + aryl Br/triflate — neither catalyst class nor substrate class matches Kumada 1972. Not counted as EP-08a filler.

## Candidate 2: Large-scale Kumada process-chemistry (50 kg scale)

| Field | Value |
|---|---|
| Source | Academia preprint surfaced in WebSearch |
| Title (fragment) | "Investigation of a Kumada Cross Coupling Reaction for Large-Scale Production of (2R,7R,E)-2-Isopropyl..." |
| Substrate | Specific pharmaceutical intermediate (not 1972 Table I) |
| Replicates | Process-scale demonstrated at 50 kg batch |
| **0B §4 classification** | **Pending content read** — boundary case per 0B §4 "Process / flow chemistry replication on Kumada substrates → Partial". Need substrate identity check + condition matching check |

**Action**: Locate the formal PRD (process R&D) publication of this work; verify substrate match and condition matching.

## Open-web search summary

WebSearch query: `"Kumada coupling" replicate measurement "standard deviation" Ni Grignard reproducibility` (2026-05-20)

**Top 10 results scanned**:

1. wikidoc (encyclopedia — not relevant)
2. Joshi-Pangu 2011 PMC8036247 (above, not applicable)
3. organic-chemistry.org (educational — not relevant)
4. ScienceDirect Topics overview (review-style — not relevant)
5. Alfa Chemistry resource (vendor — not relevant)
6. Wikipedia (encyclopedia — not relevant)
7. KCIL industrial insights (industrial — not relevant)
8. Process-chemistry 50 kg paper (above, pending)
9. Ni-Catalyzed Enantioconvergent Kumada-Corriu cross-coupling (ACS Catalysis — to check)
10. (additional results)

**Preliminary finding**: No surface-level paper reports systematic n ≥ 3 replicates + SD on the original 1972 Kumada Table I 11-substrate set. The negative claim from cross-model convergence (Sonnet + GPT-5.4) survives open-web sanity check. WoS / Scopus structured search will provide the bibliographic depth needed for the publication-strength claim.

## Pending actions

- Locate PRD publication for the 50 kg process-chemistry candidate; verify substrate / condition matching for 0B §4 Partial / Minimal decision
- WebFetch the ACS Catalysis enantioconvergent Kumada-Corriu paper (result #9) to check whether it reports per-substrate replicates with SDs
- User to execute WoS / Scopus Variants A-D queries per master execution plan
