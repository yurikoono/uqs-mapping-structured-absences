---
title: Mapping Verification Log
created: 2026-04-19
layer: A (companion to ep_to_chemontology_mapping.md)
legend: ✓ verified in source | ⚠ inferred/hypothetical | ✗ uncertain/requires co-author
---

# Per-Parameter Source Citations for the EP-to-ChemOntology Mapping

Each parameter choice in `ep_to_chemontology_mapping.md` is cited
here against its source. Abbreviations:

- **Main** = Nath et al. (2026) *ACS Catal.* **16**, 2105–2118 main text
- **SI** = same paper, Supporting Information (S-numbered pages)
- **S3v2** = `papers/dev/kumada/kumada_v17_sonnet_s3v2.md`
- **Disc2** = `manuscript/sections/discussion_en.md`, Discussion 2

---

## Structural Unit (SU) assignments for the NiCl₂(dpe) system

| SU | Assignment | Source | Status |
|---|---|---|---|
| M | Ni | Main p. 2106 Figure 1; Main p. 2107 (M_k B_{0/1} L_n S_m schema) | ✓ Verified |
| L | dpe (1,2-bis(diphenylphosphino)ethane), bidentate | Main p. 2107 (L class); Main p. 2111 Versatility section names Kumada coupling as applicable | ✓ Verified concept; ⚠ bidentate encoding (two RCs on dpe) requires co-author confirmation that a single bidentate ligand is represented as one L unit with two coordination sites (per Main p. 2107 "denticity/hapticity" attribute) |
| B | none (no explicit base in Kumada 1972; Grignard acts as both alkyl source and in-situ halide-abstracting agent) | S3v2 §1 Claim Architecture, §2 SRG-1; Main p. 2107 "at most one base" (m=0 allowed) | ⚠ Inferred — the Grignard plays an unusual dual role; co-author review requested |
| S(R1) | Aryl halide (e.g., chlorobenzene), FG = –Cl | Main p. 2107 Figure 2 ("substrate type R1: –X, –OTf, –CHO...") | ✓ Verified |
| S(R3) | R-MgBr (e.g., n-BuMgBr), FG = MgBr | Main p. 2107 Figure 2 ("substrate type R3: RMgX, RSnR'₃...") | ✓ Verified |
| S(R2) | Vinyl halide (for stilbene-producing EP-04a), FG = alkene + –Cl | Main p. 2107 Figure 2 ("substrate type R2: alkene, alkyne") | ✓ Verified; ⚠ vinyl chloride has both R1 (halide) and R2 (alkene) character — Main p. 2107 notes that a substrate carrying more than one FG may be assigned to more than one substrate type |

## ERPO availability

| ERPO | Published source | Status |
|---|---|---|
| CoordinationComplex | Main Table 2 (p. 2108, 2nd row) | ✓ Verified |
| AssociationOfCoordinationComplexWithaSubstrateType(m,n) | Main Table 2 (3rd row); SI Table S2 | ✓ Verified |
| AssociationOfCoordinationComplexWithaComponentOfaSubstrateType(m,n,o) for o∈{1,2} | Main Table 2 (4th row); SI Table S2 | ✓ Verified |
| DissociationOfaSubstrateType(m,n) | Main Table 2 (5th row); SI Table S2 | ✓ Verified |
| OxidativeAddition | Main Table 2 (6th row, composite of 4 sub-ERPOs); SI Fig S1 XML | ✓ Verified |
| OlefinInsertion | SI Fig S2 XML | ✓ Verified |
| β-Hydride Elimination | SI Fig S3 XML | ✓ Verified |
| Transmetalation | **SI Fig S4 XML** | ✓ Verified — this is the key finding that unlocks direct Kumada mapping |
| BaseElimination | Main p. 2112 Table 4 (ERPO₅); Main p. 2113 Figure 6 legend ("BE"); Main p. 2114 Figure 8(g→h) | ✓ Verified concept, ⚠ XML definition not shown in SI Figures S1–S4 |
| AssociationOfTwoComponents | SI Table S2 (e.g., Association_of_C1R1_C1R2) | ✓ Verified — critical for cross-coupling branch |
| MigratoryInsertion | Main p. 2114 Figure 8 caption; SI Fig S6 (MigratoryInsertion1, MigratoryInsertion2) | ✓ Verified concept |
| **ReductiveElimination** | — | ✗ **NOT DEFINED in Nath et al. (2026) main text, SI Figures S1–S4, or SI Table S2.** The Heck cycle achieves product release via BHE + BE; the Kumada cycle requires C–C bond formation from a Ni(II) diorganyl without β-elim. **Requires new ERPO definition or decomposition via AssociationOfTwoComponents.** See `ep_to_chemontology_mapping.md` §"Open methodological questions" item 1. |

## `allowed_changes` per-SU values

| SU | Value | Source | Status |
|---|---|---|---|
| S (substrate) = 3 | Substrate S = 3 in Heck example | Main Table 4 entry 6 ("L = 0, B = 1, S = 3"); SI Fig S5 (styrene: "allowed_changes": 3; iodobenzene: "allowed_changes": 3) | ✓ Verified for substrate SUs |
| M (metal) = 1 | Metal = 1 (Pd in Heck) | SI Fig S5 (Palladium: "allowed_changes": 1, "chemical_role": "M") | ✓ Verified for Pd; ⚠ Ni hybridization behaviour at the metal during OA/RE may warrant M = 2; co-author review requested |
| L (ligand) = 0 | Ligand = 0 (PPh₃ in Heck) | Main Table 4 entry 6; SI Fig S5 (triphenylphosphane: "allowed_changes": 0, "chemical_role": "L") | ✓ Verified for rigid monodentate phosphine; ⚠ dpe is bidentate and can be fluxional — L = 0 is a starting assumption |
| B (base) = 1 | Base = 1 (NEt₃ in Heck) | Main Table 4 entry 6 | ✓ Verified for Heck; in Kumada no explicit base — item marked as "B = — " in the mapping table |

**Note on the Discussion 2 claim that "`allowed_changes = S = 3` is
considered appropriate"**: the claim is consistent with Main Table 4
entry 6, but it omits the M and L per-SU values. The insertion draft
expands the claim to the full per-SU setting.

## Geometric / collision / stopping parameters

| Parameter | Value | Source | Status |
|---|---|---|---|
| SU radius r | 2.2 Å | Main Table 4 entry 7 ("a default value") | ✓ Verified |
| Proximity threshold δ | 3.0 Å | Main Table 4 entry 8 ("a default value") | ✓ Verified; ⚠ Main p. 2115 notes that for Figure 8 the authors used tighter bond-specific thresholds (2.9 Å for Pd–I, 2.5 Å for Pd–C, 1.9 Å for each of C–C, Pd–H and C–H, and 2.0 Å for I–H) — equivalent tighter thresholds for Ni–Cl, Ni–C(aryl), Ni–C(alkyl), Ni–H would need to be chosen by a chemistry co-author |
| AFIR model collision γ | 500 kJ/mol | Main p. 2112 ("Why is γ = 500 kJ/mol?"); SI Table S4 ("Gamma=500.0 set 5.0") | ✓ Verified |
| STOPPATH | 2000 | Main p. 2112 (SC-AFIR runs stopped at STOPPATH = 2000); SI Table S4 | ✓ Verified as default; EP-driven termination (Bi-directional framing) would override this |
| Temperature for RCMC kinetic navigation | 200 / 300 / 400 K | SI Table S4 ("Siml_temperature=200.0 300.0 400.0") | ✓ Verified |
| TimeScale | 86400 s (1 day) | Main p. 2112; SI Table S4 | ✓ Verified |

## Calculation-level parameters

| Item | Value | Source | Status |
|---|---|---|---|
| Initial search method | GFN2-xTB | Main p. 2107 Methodology; Main p. 2112 (the semiempirical method is described as much faster and as already validated for palladium systems) | ✓ Verified; ⚠ the reliability statement concerns palladium systems — extension to Ni is not empirically demonstrated in Nath et al. (2026) |
| DFT refinement requirement for Ni | Mandatory (inferred) | Disc2 paragraph 4 ("computational accuracy for a system involving a Ni oxidation-state change (d¹⁰→d⁸) is not necessarily equivalent to that for the Pd systems primarily validated in the ChemOntology paper") | ⚠ Inferred from Disc2; not stated in Nath et al. (2026). Consistent with general knowledge of Ni d-orbital accuracy requirements, but specific functional / basis-set recommendations are not prescribed. |
| SCF package | ORCA (via GRRM23 interface) | Main p. 2112 (ORCA, gas phase, GFN2-xTB level); SI Table S4 (OrcaProc=1, OrcaMem=200) | ✓ Verified |

## Cross-reference to the Stage 3 v2 EP definitions

| EP ID | Source reference in `kumada_v17_sonnet_s3v2.md` |
|---|---|
| EP-01a | SRG-2 (RI-05 + RI-01), SRG-3 (RI-01 + RI-08), SRG-5 (RI-01 + RI-05) |
| EP-02a | §5 auxiliary route — "Identity/purity substantiation pack — Table Iのすべてのエントリについて..." |
| EP-03a | SRG-1 (RI-03 + RI-06), Case-specific implementation (i)(ii)(iii) |
| EP-04a | SRG-6 (RI-04 + RI-08), cis/trans-stilbene content |
| EP-05a | SRG-2 (selectivity, mass balance), SRG-4 (boundary), SRG-5 (solvent effect), CLA-1 |
| EP-06a | SRG-1 (analogy validation from dipy-Ni to dpe-Ni), Case-specific implementation |
| EP-07a | SRG-4 (boundary test — sp³ halide, PhCl/PhBr/PhI comparison) |
| EP-08a | SRG-6, SRG-3 (replication / uncertainty) |
| EP-09a | CLA-1 (NiCl₂(dpe) vs Ni(acac)₂ benchmark) |

## Items flagged as inferred or uncertain (recap)

- dpe denticity encoding (one L with two coordination sites) — Main p. 2107
  supports this via the "denticity/hapticity" attribute, but no
  explicit Kumada / bidentate worked example is given. **⚠ inferred**
- B (base) = absent in the Kumada system — the Grignard serves dual
  role. **⚠ inferred**
- M (metal) = 1 is inherited from the Pd Heck example; Ni may warrant
  M = 2 given d¹⁰/d⁸ redox. **⚠ inferred, co-author review requested**
- DFT refinement is **mandatory** for Ni-containing EPs — Nath et al.
  does not state this explicitly but only validates GFN2-xTB on Pd.
  **⚠ inferred**
- ReductiveElimination ERPO gap — **✗ uncertain; open question**
- Kumada cross-coupling product labeling (C1R1-C1R3 → Ar-R) — SI
  Table S3 leaves these combinations "Not labeled yet". **✗ uncertain**
- Bond-specific δ thresholds for Ni (Ni–Cl, Ni–C, Ni–H) — not provided
  by Nath et al. (the Heck-specific values are Pd-only).
  **✗ uncertain; chemistry co-author judgment**
