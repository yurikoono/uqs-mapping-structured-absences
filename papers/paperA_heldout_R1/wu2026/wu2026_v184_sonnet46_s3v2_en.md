```
prompt_version: stage3-v2-en-20260419
model_info: claude-sonnet-4-6
```

# Re-certification Assessment Sheet for Scientific Knowledge

## Wu, Wang, Wang, Koh, Shi 2026 (CCS Chemistry, full_paper)

---

### §1 Claim Architecture

**Core claim summary:**
The paper reports a Ni/NHC-catalyzed protocol that achieves, for the first time, enantioselective intermolecular reductive Heck and Heck coupling of internal cyclic alkenes (2,5-dihydrofuran, dihydropyrrole, styrene derivatives) with aryl or alkenyl triflates, using bulky yet flexible chiral NHC ligands (L4, L5). The Novelty pillar rests on two interconnected claims: (i) intermolecular asymmetric Heck-type coupling of non-directed internal alkenes was previously inaccessible ("remains scarce," "challenging"), and (ii) the ANIPE/IPE-type NHC ligand design — large steric bulk combined with conformational flexibility — is the enabling structural feature. The Utility pillar claims broad synthetic value: [REDACTED: verbatim source text; see the source paper via its DOI], pharmaceutically relevant heterocycle substrates, gram-scale applicability, and mild conditions. A subsidiary Mechanistic claim — carbometallation (rather than hydrometallation) is the dominant pathway — is supported by deuterium labeling, radical capture, and kinetic studies.

**Layered structure:**
Three partially independent layers exist; a single refutation does not collapse all claims simultaneously.

- **Layer 1 (Synthetic scope and efficiency):** Most robust. The 60 examples with tabulated yields, ee, and rr constitute evidence that the transformation is feasible and reproducible at lab scale. This layer would survive even if Layers 2 and 3 were refuted.
- **Layer 2 (Ligand design principle):** Intermediate robustness. The empirical ligand screening (Table 1: L1 > L3 > L4, L5; L2 inactive) supports the structural importance of NHC bulk, but the paper does not show that NHC flexibility (as opposed to bulk alone) is necessary, so the specific design principle is only partially supported.
- **Layer 3 (Mechanistic assignment — carbometallation):** Most fragile. Rests on three control experiments each containing internal ambiguity (77% D incorporation, U-1; 85% yield with BHT, U-2; kinetic rate orders without stated precision, U-3). If any of these is reinterpreted, the mechanistic assignment weakens without affecting Layers 1 or 2.

Inter-layer dependency: Layer 3 supports Layer 2's design rationale (NHC suppresses β-H elimination from alkyl-Ni by proximity control during carbometallation). If Layer 3 falls, Layer 2's mechanistic basis weakens; the empirical ligand screening data (Layer 1 component) still stands.

---

### §2 SRG / CLA → RI / ER / EP Crosswalk

**SRG-1 [Mechanistic validation incompleteness]**

Member items: A-2, B-9, C-3, U-1, U-2, U-3

* **Primary RI:** RI-04 (Unreplicated discriminator) — Each of the three mechanistic control experiments (D-labeling, BHT radical capture, kinetics) constitutes a single measurement with strong discriminatory power (mechanistic assignment) interpreted at a high level without internal validation: 77% D incorporation is not 100% (U-1); 85% yield with BHT does not establish detection limit (U-2); kinetic rate orders lack stated precision (U-3).
* **Secondary RI:** RI-06 (Imported model) — The four-step catalytic cycle (Figure 3) is explicitly called "plausible" and is imported from related Ni/NHC systems (refs 57–61, C-3) without demonstrating isomorphism via stoichiometric experiments, intermediate characterization, or key observable validation in this specific Ni/L5/ArOTf/cyclic-alkene system.
* **ER:** For the carbometallation assignment to be established, the three mechanistic probes must individually yield unambiguous results (D-incorporation ≈ 100%; BHT titration establishing the radical detection window; rate orders with ± uncertainty stated); and at least one elementary step (oxidative addition, carbometallation) must be independently validated by a stoichiometric experiment or intermediate characterization.
* **EP:** EP-04a (Discrimination/replication pack); EP-06a (Analogy-validation pack)
* **Case-specific implementation:** (1) KIE study using kH/kD with iPrOH vs iPrOD at standard conditions to quantify the H-transfer step; (2) Repeat D-labeling with varied equivalents of iPrOD-d8 (0.5, 1.0, 5 equiv added to iPrOH solvent) to determine whether 77% incorporation reaches a saturation plateau that accounts for H/D scrambling; (3) BHT titration (0.1–10 equiv) to establish the radical flux detection limit; (4) Stoichiometric reaction of Ni(cod)₂/L5/HCl with 4-NMe₂-C₆H₄OTf to characterize intermediate I; (5) Stoichiometric alkene insertion of characterized intermediate I with 2,5-dihydrofuran to confirm carbometallation step II.
* **Notes:** U-1 and U-1/U-2 are in high_convergence_low_gap (convergence 2/3, gap=none). RI-04 + RI-06 co-occurrence: resolving RI-06 (cycle isomorphism) is insufficient if RI-04 ambiguities (U-1, U-2) remain; both must be resolved for VQ-3.

---

**SRG-2 [Quantitative measurement and reporting completeness]**

Member items: B-3, B-4, B-7, U-3

* **Primary RI:** RI-08 (Unquantified reliability) — No replicate measurements or uncertainty estimates are provided for any of the 60 scope entries (yield, ee, rr); the kinetic rate orders are reported without stated precision (U-3 is double-listed here and in SRG-1 for its measurement aspect); GC rr values are determined on crude mixtures without calibration (B-7).
* **Secondary RI:** RI-01 (Reporting integrity) — Yield reporting basis is inconsistent: optimization tables (Tables 1, 3) use NMR yield while scope tables (Tables 2, 4) use isolated yield without a cross-calibration control.
* **ER:** For the quantitative claims (up to 99% ee, up to >99:1 rr) to be credible and reproducible, at minimum the standard substrate (entry 1, Table 1) should be reported in triplicate with SD; GC calibration factors or retention-time standards for representative regioisomer pairs should be provided; and the absolute configuration assignment method for non-X-ray products should be stated.
* **EP:** EP-08a (Replication/uncertainty pack); EP-01a (Reporting-coherence pack)
* **Case-specific implementation:** (1) Report entry 1 (1a + 2a, L5/NaOiPr/iPrOH/40°C) in triplicate; state SD for isolated yield, ee, and rr; (2) Provide GC response factor correction factors or authentic standard retention times for the α- and β-regioisomers for at least one representative substrate pair; (3) State explicitly in the main text or SI how absolute configuration is assigned for the 58 products without X-ray confirmation (e.g., "HPLC elution order relative to X-ray-confirmed 3c/4k; same-sense NHC configuration expected to give same-sense product").
* **Notes:** B-3 is in high_convergence_low_gap (V1=medium, V3=high; convergence 2/3; gap=low). B-7 is in high_convergence_low_gap (V1=medium, V3=medium; convergence 2/3; gap=none).

---

**SRG-3 [Scope boundary and failure disclosure]**

Member items: A-1, B-2, B-5, B-8

* **Primary RI:** RI-07 (Unsupported boundary) — The paper claims "broad functional group tolerance" and "excellent regio- and enantioselectivity" as scope-wide properties without reporting any systematically attempted substrate classes that failed or gave lower performance.
* **Secondary RI:** RI-05 (Qualitative overread) — The qualitative descriptor "excellent functional group tolerance, including heterocycles" implies a general claim derived from a curated substrate set, without a failure-mode analysis.
* **ER:** For the scope boundary claim to be evaluable, the paper should report representative examples of substrate classes that were attempted but gave <20% yield or <80% ee, along with the observed failure mode.
* **EP:** EP-07a (Boundary-test pack)
* **Case-specific implementation:** Test at least 3 substrate classes at the scope boundary: (a) sterically very bulky ortho,ortho-disubstituted ArOTf; (b) heteroaryl triflates other than those shown (e.g., thienyl triflate, pyridinyl triflate with N close to the triflate); (c) acyclic trisubstituted internal alkenes. Report yield and ee, including N.R. outcomes.
* **Notes:** A-1 defers scope extension to future work; RI-07 and RI-05 are therefore prospective (future work might resolve them) but descriptive of this paper's empirical boundary.

---

**SRG-4 [Dropped prior-art numerical comparison]**

Member items: C-1, C-2

* **Primary RI:** RI-09 (External superiority) — The claim [REDACTED: verbatim source quotation; see the source paper via its DOI] implies that this work surpasses prior art (refs 26-34 and 35-42), but no direct experimental comparison of yield, ee, or substrate scope is provided.
* **ER:** For the "more general" claim to be demonstrated (not merely asserted), a head-to-head comparison of this paper's performance against the most comparable prior system (minimally ref 37, Ni-catalyzed enantioselective reductive Heck of ArOTf) on shared substrate(s) is required.
* **EP:** EP-09a (Internal benchmark pack)
* **Case-specific implementation:** Select 2–3 substrates from ref 37's scope table; run them under current conditions and ref 37 conditions in parallel; report yield and ee in a comparison table. Alternatively, test one substrate from this paper's scope (1a + 2a) under ref 37's conditions (bisoxazoline Ni, Et₂O, etc.) and compare.
* **Notes:** No TEMPERATURE_SUMMARY position (C items). C-1/C-2 are symmetric (SRG-4 member items; symmetric_pattern: yes for C-2, partial for C-1).

---

Outside the SRGs: CLAs

No standalone CLAs: all D-4 candidates map into one of the four SRGs. The self-contradictory-absence CLA check finds U-1 (D-labeling) and U-2 (BHT) captured in SRG-1; B-9 (Heck by-product characterization) also in SRG-1.

---

### §3 Current VQ assessment

**Current judgment: VQ-2 (Method) — qualified**

**VQ-1 (Observation) — holds:**
RI-02 requires product identity established at a granularity that excludes alternative candidates. The paper provides NMR/MS characterization of isolated products in SI, and X-ray confirmation for two representative products (3c, CCDC 2454997; 4k, CCDC 2454994). Absolute configuration assignment for the remaining 58 products is absent from the main text (B-3, RI-01 aspect), but the product structures themselves are established by standard methods. VQ-1 holds; B-3 (absolute configuration assignment method) is a partial non-fatal deficiency at this level.

**VQ-2 (Method) — holds (qualified):**
On the premise that RI-02 is non-fatal (VQ-1 holds), VQ-2 requires RI-01 (reporting integrity) and RI-07 (unsupported boundary).

RI-01: The GC calibration absence (B-7) introduces unquantified systematic error into rr values, and the inconsistent yield basis (B-6, NMR vs isolated yield) affects benchmarking. These are non-fatal within the scope tables themselves (isolated yield is the standard reporting metric), but they undermine the cross-table comparability. RI-01 is partially non-fatal.

RI-07: The scope boundary is asserted without failure data (B-8, SRG-3). RI-07 is present but is era-norm tolerated for full synthetic papers in 2026 (scope tables without failure entries are standard practice). Classified as non-fatal by current genre convention.

VQ-2 holds (qualified): both RI-01 and RI-07 are present but non-fatal by current era norms, so the methodological framework is sufficient for the synthetic scope claim.

**VQ-3 (Mechanism) — fails:**
On the premise that VQ-2 holds, VQ-3 requires RI-03 (unobserved explanatory), RI-04 (unreplicated discriminator), RI-06 (imported model).

RI-03: Key intermediates I–IV in the proposed cycle (Figure 3) are neither isolated nor characterized. The oxidation-state assignment of Ni in each step is inferred from analogy. RI-03 is present and is fatal for establishing the mechanistic claim (carbometallation vs. hydrometallation), though non-fatal for Layer 1 (synthetic scope).

RI-04: Each of the three control experiments has an internal ambiguity: 77% D incorporation (U-1); 85% yield with BHT (U-2); kinetic rate orders without stated precision (U-3). RI-04 is present and fatal for the mechanistic claim.

RI-06: The catalytic cycle is imported from related Ni/NHC systems (refs 57-61) without stoichiometric validation in this specific system. RI-06 is present.

VQ-3 fails — RI-03, RI-04, and RI-06 are all unresolved for the mechanistic claim (Layer 3).

However, **Layer 1 (synthetic scope) on its own: VQ-2 holds.** The synthetic transformation is demonstrated with 60 examples, two X-ray confirmations, and gram-scale replication. The mechanistic failure does not retroactively invalidate the synthetic scope, which rests on observed yields and ee values rather than on the proposed mechanism.

**VQ-4 (Benchmark) — fails:**
Requires VQ-3 (fails) + RI-08 (unquantified reliability) + RI-09 (external superiority).
RI-08: No replicate data or error estimates (B-4). Present throughout.
RI-09: Superiority over refs 26-34 and 35-42 asserted but not benchmarked (SRG-4, C-1, C-2). Present.
VQ-4 fails — both RI-08 and RI-09 are unresolved, and VQ-3 does not hold.

---

### §4 Era-Norm Annotation

**communication-era tolerated:**
(Note: this is a full paper, not a communication; era-norm tolerances apply to the full-paper genre in CCS Chemistry, 2026.)

- **B-4 (no replicate data for scope table entries):** Tolerated across top synthetic journals (JACS, ACIE, Nature Chemistry) in 2026 for scope table entries, where it is standard practice to report a single run per substrate. This omission does not constitute a methodological deficiency within the current publication norm.
- **B-7 (GC rr without calibration):** Tolerated in synthetic methodology papers; GC-based rr ratios without response-factor correction are standard across comparable papers in the subfield. The rr values serve as relative qualitative guidance rather than absolute measurements.
- **B-9 (Heck by-product not characterized under standard conditions):** Tolerated in mechanistic supporting evidence for a synthetic paper; the degree of Heck contamination under standard conditions (if any) is a mechanistic question typically deferred to follow-up mechanistic studies.

**modern-era deficient:**
- **B-3 (absolute configuration assignment method not stated for 58/60 products):** Modern-era deficient — since approximately 2020, leading synthetic chemistry journals expect the main text to state explicitly how absolute configuration is assigned for non-X-ray-confirmed products (HPLC elution order relative to X-ray-confirmed standard; VCD; OR). Omission of this information prevents verification and limits the paper's utility for synthetic applications requiring a specific enantiomer.
- **RI-04 manifestations (U-1 and U-2: ambiguous D-incorporation and BHT experiment):** Modern-era deficient — post-2015 standards for mechanistic control experiments in full papers from leading groups require at least an acknowledgment of the deviation (77% D), discussion of possible explanations, and for the BHT experiment, a concentration-titration or comparison with a known radical process. The presentation of ambiguous data as conclusive evidence is increasingly inconsistent with modern mechanistic chemistry standards.
- **RI-09 (external superiority without benchmarking):** Modern-era deficient — the "more general" claim (vs. refs 35-42) without a single head-to-head experiment is increasingly viewed as insufficient in competitive method development papers; top journals in asymmetric catalysis (JACS, Angewandte) require at least a representative comparison with the closest prior work.

**Items belonging to both tags:**
- None in this paper: the era-norm tolerances apply to different items from the modern-era deficiencies.

---

### §5 Shortest-reinforcement route

**Current VQ: VQ-2 (qualified)**
**First objective function: VQ-3 (Mechanism)**
**Second objective function: VQ-4 (Benchmark)**

**Shortest route to VQ-3:**

1. **EP-04a (Discrimination/replication pack) — primary investment.**
   Run the KIE study (kH/kD) for the H-transfer step using iPrOH vs iPrOD under standard conditions; repeat the D-labeling experiment with varied iPrOD-d8 loading (0.5, 1.0, 5.0 equiv) in iPrOH to establish the D incorporation plateau; conduct BHT titration (0.1, 0.5, 1.0, 5.0 equiv) to establish the radical detection threshold.
   Advances: RI-04 (provides replication of mechanistic discriminating experiments with precision; resolves U-1 and U-2).

2. **EP-06a (Analogy-validation pack) — secondary investment.**
   Stoichiometric reaction of Ni(cod)₂/L5/HCl with 4-NMe₂-C₆H₄OTf to generate and characterize intermediate I; then test the stoichiometric reactivity of characterized intermediate I with 2,5-dihydrofuran to confirm the carbometallation step.
   Advances: RI-06 (establishes isomorphism of the imported cycle with this specific Ni/NHC/ArOTf/cyclic-alkene system); RI-03 (directly observes one key intermediate).

**Shortest route to VQ-4 (after VQ-3):**

3. **EP-09a (Internal benchmark pack).**
   Select 2–3 substrates from ref 37 (Huang et al. 2021) and test under current conditions vs. ref 37 conditions; tabulate yields and ee head-to-head.
   Advances: RI-09 (transforms the "more general" assertion into a demonstrated performance advantage).

4. **EP-08a (Replication/uncertainty pack).**
   Run entry 1 (1a + 2a, L5/NaOiPr/iPrOH/40°C, 12 h) in triplicate; report SD for isolated yield, ee, and rr.
   Advances: RI-08 (establishes the precision of the quantitative claims that underpin the entire scope table).

Certification-gate note: The experimental investment order follows information gain (EP-04a first, as it resolves the most urgent mechanistic ambiguities U-1 and U-2 in SRG-1), but the final certification is fixed by the gate order VQ-1 → VQ-2 → VQ-3 → VQ-4.

---

### §6 Contribution to institutional design

**New representative case for RI-04 — "multi-probe ambiguity" variant:**
This paper provides a new, well-documented case for RI-04 in which the unreplicated discriminator pattern arises not from a single data point but from three independent control experiments each with an internal unexplained deviation. The 77% D incorporation (U-1), 85% yield with BHT (U-2), and undisclosed kinetic precision (U-3) collectively create an impression of mechanistic convergence, but each probe individually is insufficient to rule out alternative interpretations. This "multi-probe ambiguity" variant — where each probe has an unaddressed gap — is worth adding to the RI-04 codebook note as distinct from the single-critical-experiment pattern. Proposed note: "RI-04 multi-probe variant: when N ≥ 3 probes each support the same mechanism but each has a significant unexplained deviation from the predicted value (e.g., D-labeling gives 77% not 100%; radical scavenger gives 85% not 0% yield), the collective evidence may create a false impression of convergence. Each probe must be internally resolved before convergence can be claimed."

**Confirmed RI-04 / RI-06 co-occurrence pattern:**
The co-occurrence of RI-04 (unreplicated discriminating experiments) and RI-06 (imported catalytic cycle from related Ni/NHC systems) in SRG-1 is confirmed in this paper. This co-occurrence is structurally similar to the pattern observed in Breitenfeld 2014 and other Ni-catalyzed papers where the catalytic cycle is constructed by analogy from Pd chemistry. The implication for EP design is that resolving RI-06 alone (by stoichiometric validation of the cycle) is insufficient if RI-04 ambiguities remain in the mechanistic probes — both RI-04 and RI-06 must be independently resolved.

**Labeling mismatch pattern confirmed:**
The paper uses "plausible catalytic cycle" in one sentence but employs factual verbs throughout the mechanism discussion: "carbometallation... generated alkylnickel intermediates II," "hydride transfer and reductive elimination released the product." The hypothesis label is localized to a single phrase ("plausible catalytic cycle was proposed") and does not propagate to the individual elementary step descriptions, which are stated factually. This labeling mismatch — consistent with the pattern identified in prior analyses — co-occurs with RI-06 (imported model) as expected.

**RI-07 boundary — era-norm dependency note:**
This paper provides additional support for the observation that RI-07 (unsupported boundary) is era-norm tolerated in full synthetic papers in 2026 — scope tables without failure entries are universally accepted in top synthetic chemistry journals. The era-norm distinction (tolerated in 2026 vs. what would now be expected in mechanism-focused papers) is confirmed: RI-07 is non-fatal for the synthetic scope claim (Layer 1) but becomes relevant if the paper's boundary claims extend to mechanism (Layer 3). This dual-status — tolerated for synthetic, non-tolerated for mechanistic — is worth recording in the RI-07 boundary annotation.

**No new PRI candidates detected.** All patterns are within the existing RI-01 through RI-09 framework. The "multi-probe ambiguity" is a variant of RI-04, not a new code.

---

> **Public-cut redaction notice**: verbatim quotations from the analysed papers in this file have been replaced by `[REDACTED: …]` markers (rules in the repository README). The unredacted file is in the reviewer version of the deposit.
