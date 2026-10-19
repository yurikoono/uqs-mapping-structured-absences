```
prompt_version: stage3-v2-en-20260419
model_info: claude-sonnet-4-6
```

# Re-certification Assessment Sheet for Scientific Knowledge

## Li et al. 2024 (Nature Catalysis, full_paper)

---

### §1 Claim Architecture

**Core claim:** Two pillars. **Novelty:** first general eXEC of fully unactivated alkyl halides (no activation substituents, no stoichiometric reductants) via a Ni(I/II/III) radical catalytic cycle. **Utility:** broad scope across four substrate classes (1°–2°, 1°–1°, 2°–2°, 1°–3°), 63 products, late-stage bio-relevant modification, gram-scale scalability.

**Layered structure — independent layers exist.** Layer 1 (Scope): supported by isolated yields alone; survives mechanistic refutation. Layer 2 (Selectivity): "highly selective" claim rests on cross:homo ratio; partially independent of Layer 1. Layer 3 (Mechanistic): Ni(I/II/III) cycle, Ni(III)-preferred RE (ΔG‡ = 13.4 vs. 16.2 kcal mol⁻¹); load-bearing for Novelty pillar only. Layer 2 is mechanistically grounded in Layer 3's rate-determining-step assignment; if Layer 3 fails, the kinetic selectivity interpretation is undermined while Layer 1 utility stands.

---

### §2 SRG / CLA → RI / ER / EP Crosswalk

**SRG-1 [DFT methodology absent]**
* **Primary RI:** RI-01 Reporting integrity
* **Secondary RI:** RI-06 Imported model
* **ER:** DFT functional, basis set, solvation model, reference electrode calibration, and spin-state assignments for Ni(I/III) must be stated so computed values are verifiable and the 2.8 kcal mol⁻¹ barrier difference can be assessed against method error.
* **EP:** EP-01a Reporting-coherence pack; EP-06a Analogy-validation pack
* **Case-specific implementation:** Disclose functional (e.g., B3LYP or M06-L), basis set (def2-TZVP/Ni), SMD-DMF, and spin multiplicity per Fig. 5c intermediate. Apply DLPNO-CCSD(T) single-point on both RE TSs.
* **Notes:** Members: V1-Q7, V2-OV1, V3-Q1, V3-Q4, V3-OV1, V3-OV4 (6 members). high_convergence_low_gap (3/3, all high, gap=none). U-6 (critical, prerequisite-absence).

**SRG-2 [2.8 kcal mol⁻¹ barrier reliability]**
* **Primary RI:** RI-04 Unreplicated discriminator; **Secondary RI:** RI-08 Unquantified reliability
* **ER:** Typical DFT error for open-shell Ni (±2–5 kcal mol⁻¹) can encompass the 2.8 kcal mol⁻¹ difference; stated uncertainty bounds or high-level benchmark required.
* **EP:** EP-04a Discrimination / replication pack; EP-08a Replication / uncertainty pack
* **Case-specific implementation:** D3BJ dispersion sensitivity check + DLPNO-CCSD(T) on both RE TSs; report ΔΔG‡ with sensitivity range.
* **Notes:** Members: V1-Q8, V2-OV2, V3-Q2, V3-OV2 (4 members). high_convergence_low_gap (3/3, gap=low). Subordinate to SRG-1.

**SRG-3 [Radical probes do not isolate Ni oxidation-state steps]**
* **Primary RI:** RI-04 Unreplicated discriminator; **Secondary RI:** RI-03 Unobserved explanatory (Ni(I) species A not directly observed)
* **ER:** Radical-clock experiment must report rearranged and unrearranged product yields (ratio constrains τ via kring ≈ 1×10⁸ s⁻¹); one experiment must directly probe Ni(I) under electrolysis conditions.
* **EP:** EP-04a Discrimination / replication pack; EP-03a Direct-observation / state-assignment pack
* **Case-specific implementation:** Report unrearranged yield alongside ring-opened 94 (53%); EPR of Ni/L2 under electrolysis to detect Ni(I) (d⁹, S=½) directly.
* **Notes:** Members: V2-Q1, V2-Q2, V2-Q3, V2-Q8. Convergence 1/3 (V2). U-7 + B-9. RI-03: "Available-but-unutilized characterization."

**SRG-4 [Selectivity mechanism uncharacterised]**
* **Primary RI:** RI-05 Qualitative overread; **Secondary RI:** RI-07 Unsupported boundary
* **ER:** The selectivity model must be validated against the observed by-product distribution (17% secondary + 13% primary homocoupling at Entry 1) by deriving predicted yields from proposed rate constants.
* **EP:** EP-05a Quantitative-ranking substantiation pack; EP-07a Boundary-test pack
* **Case-specific implementation:** Extract k₁ and k₂ from Fig. 4b slopes; calculate predicted cross:homo at 3:1 stoichiometry; compare to 85:17:13. Model must account for 13% primary homocoupling under primary halide deficiency.
* **Notes:** Members: V1-Q9, V2-Q5, V2-OV5 (3 members). high_convergence_low_gap (2/3, both=medium, gap=none). U-1 (self-contradictory absence).

**SRG-5 [Reference electrode inconsistency — CV vs. DFT/SWV]**
* **Primary RI:** RI-01 Reporting integrity; **Secondary RI:** RI-06 Imported model
* **ER:** CV potentials (Fig. 4a, Ag/AgCl) and DFT/SWV potentials (Figs. 4c–d, Ag/AgNO₃) must be harmonized; the ~0.1–0.2 V offset is on the same scale as the 0.24 V primary vs. secondary bromide potential difference.
* **EP:** EP-01a Reporting-coherence pack; EP-06a Analogy-validation pack
* **Case-specific implementation:** State Ag/AgCl → Ag/AgNO₃ conversion via ferrocene in DMF; re-plot Fig. 4a alongside Figs. 4c–d on a common scale.
* **Notes:** Members: V1-Q5, V2-Q6, V3-Q7. Convergence 2/3; V3=high. U-2 + B-7. low_convergence_high_gap.

**SRG-6 [Kinetic analysis — mechanism–kinetics decoupling]**
* **Primary RI:** RI-05 Qualitative overread
* **Secondary RI:** PRI-11 Mechanism–kinetics decoupling (provisional; confirmed here — see §6)
* **ER:** A rate law must be derived algebraically from the proposed Ni(I/II/III) cycle and compared to Fig. 4b; the apparent contradiction that primary bromide is harder to reduce by CV (−2.72 V vs. −2.48 V) yet shows greater concentration sensitivity in rate, and the fact that the DFT initiation barrier (ΔG‡≈20 kcal mol⁻¹) is the highest in the profile, must both be reconciled.
* **EP:** EP-05a Quantitative-ranking substantiation pack; EP-03a Direct-observation / state-assignment pack
* **Case-specific implementation:** Derive d[3]/dt under steady-state approximation from Fig. 5c. Identify which step is turnover-limiting vs. selectivity-determining. If kSET (20 kcal mol⁻¹) is overall rate-limiting, the radical addition selectivity interpretation of Fig. 4b requires revision.
* **Notes:** Members: V1-Q6, V2-OV3, V2-Q7, V3-Q3, V3-OV3 (5 members). high_convergence_low_gap (2/3, gap=none). PRI-11 confirmation (see §6).

**SRG-7 [Scope generality vs. divergent catalyst system]**
* **Primary RI:** RI-07 Unsupported boundary; **Secondary RI:** RI-05 Qualitative overread
* **ER:** "General strategy" claim requires mechanistic rationale for why 2°–2° and 1°–3° coupling requires L11/DMA, with CV or DFT evidence that the Ni(I/II/III) cycle operates under L11.
* **EP:** EP-07a Boundary-test pack; EP-05a Quantitative-ranking substantiation pack
* **Case-specific implementation:** CV of Ni(II)/L11 in DMA vs. Ni(II)/L2 in DMF; DFT RE barriers under L11 ligation; test whether L2 gives any yield for 2°–2° coupling.
* **Notes:** Members: V1-Q3, V1-Q4. Convergence 1/3 (V1, high). low_convergence_high_gap.

**SRG-8 [Mass balance and by-product accounting]**
* **Primary RI:** RI-08 Unquantified reliability; **Secondary RI:** RI-01 Reporting integrity
* **ER:** Mass balance at standard and 1.5 equiv. conditions must account for cross-coupling product, homocoupling by-products, protodehalogenation, and recovered SM.
* **EP:** EP-08a Replication / uncertainty pack; EP-01a Reporting-coherence pack
* **Case-specific implementation:** GC yield (internal standard) of products 3, 4, 5, protodebromination, and recovered SM at Entry 1 and 1.5 equiv.; closure ≥90%.
* **Notes:** Members: V1-Q1, V1-Q11. Convergence 1/3. B-1 + B-6.

**Outside the SRGs: CLAs**

**CLA-1: Anodic half-reaction absent from the proposed mechanism**
* **Primary RI:** RI-03 Unobserved explanatory
* **Secondary RI:** RI-07 Unsupported boundary
* **ER:** The decisive anode-material dependence (Fe: 85%; Zn: 30%; Mg: 17%) requires identification of the anodic process; the cathodic Ni(I/II/III) cycle cannot constitute a complete electrochemical mechanism without it.
* **EP:** EP-03a Direct-observation / state-assignment pack; EP-07a Boundary-test pack
* **Case-specific implementation:** ICP-OES for Fe²⁺/Fe³⁺ post-reaction; UV-Vis for I₃⁻; Faradaic efficiency (moles product per Faraday) to close the electrical balance.
* **Notes:** Grounded_in: U-3 (high severity, prerequisite-absence), B-5. Not in any SRG. Directly bears on D-1 Claim 3. low_convergence_high_gap (V1-Q13, severity=high).

---

### §3 Current VQ assessment

**Current judgment: VQ-2 (Method), qualified**

**VQ-1 [Observation] — Pass.** RI-02: No high-severity product identity failure; standard NMR/MS characterization implied. Non-fatal caveat: B-2 (methyl iodide for compound 56). **VQ-1 holds.**

**VQ-2 [Method] — Qualified (inherits VQ-1).** RI-01 *Unresolved*: (a) DFT parameters absent (SRG-1); (b) CV vs. DFT/SWV reference electrode mismatch (SRG-5); (c) spin multiplicities not stated. RI-07 *Unresolved*: "general strategy" without L2/L11 rationale (SRG-7); "highly selective" without quantitative model (SRG-4). **VQ-2 qualified** — partially era-norm-dependent (§4).

**VQ-3 [Mechanism] — Fails (inherits qualified VQ-2).** RI-03 *Unresolved*: Ni(I) species A not directly observed; anodic half-reaction (CLA-1) absent. RI-04 *Unresolved — fatal at VQ-3*: (a) 2.8 kcal mol⁻¹ within ±2–5 kcal mol⁻¹ DFT error is sole pathway discriminator (SRG-2); (b) radical-clock qualitative only (SRG-3); (c) kinetic data not connected to derived rate law (SRG-6). RI-06 *Unresolved*: Ni(I/II/III) cycle imported from organometallic precedent without isomorphism demonstration in this electrochemical environment. **VQ-3 fails** on RI-04 (fatal), RI-03, RI-06.

**Layered VQ asymmetry:** Layer 1 (Scope) approaches VQ-4-equivalent for practical utility; limited externally by absent head-to-head comparison with Lin (ref 60) and Gong (refs 29–30). The paper's synthetic scope substantially outpaces its mechanistic layer.

**VQ-4 [Benchmark] — Not reached** (contingent on VQ-3; RI-08/RI-09 present, deferred).

---

### §4 Era-Norm Annotation

**communication-era tolerated:**
- SRG-1: DFT details in supplementary accepted in 2024 Nature Catalysis. B-3: divergent catalyst in caption footnote is standard. B-1/SRG-8: no formal mass balance table required by this journal format.

**modern-era deficient:**
- SRG-5: CV (Ag/AgCl) vs. DFT/SWV (Ag/AgNO₃) without conversion not acceptable in 2024 mechanistic electrochemistry; ~0.1–0.2 V offset on same scale as 0.24 V primary vs. secondary bromide difference. U-2 / B-7.
- SRG-2: DFT barrier difference for open-shell Ni without uncertainty estimation insufficient by 2024 standards. U-6.
- CLA-1: 2024 electrosynthesis community expects anodic contribution identified when anode material critically governs reactivity (Fe >> Zn >> Mg by 55+ pp). U-3.
- SRG-3: Reporting only rearranged product in radical-clock experiment is qualitatively incomplete by 2024. U-7 / B-9.
- SRG-7: "General strategy" while requiring unexplained catalyst switching. *Dual classification:* caption-footnote format era-tolerated; underlying mechanistic gap modern-era deficient.

---

### §5 Shortest-reinforcement route

**Shortest route to VQ-3:**
1. **EP-03a** — EPR of Ni/L2 under standard electrolysis (DMF/NaI, 5 mA, Fe/Ni foam) to detect Ni(I) (d⁹, S=½); in-situ UV-Vis to track Ni(II)→Ni(I). Advances RI-03 + RI-06.
2. **EP-04a** — Report unrearranged product yield alongside ring-opened 94; DLPNO-CCSD(T) on both RE TSs (target: uncertainty < 1 kcal mol⁻¹). Advances RI-04.
3. **EP-01a** — State DFT functional/basis set/solvation/spin multiplicities; convert Fig. 4a to Ag/AgNO₃ via ferrocene. Advances RI-01.
4. **EP-06a** — Measure steady-state cathode potential in preparative cell; ICP-OES/UV-Vis for anodic products (CLA-1). Advances RI-06.

*Investment priority:* EP-03a first (resolves RI-03 + RI-06 simultaneously). EP-04a second (3/3 agents; computationally accessible). EP-01a third (no new experiments). EP-06a fourth.

*Certification-gate note:* Investment order follows information gain, but final VQ certification is fixed by gate order VQ-1 → VQ-2 → VQ-3 → VQ-4.

**Shortest route to VQ-4** [contingent on VQ-3]:
1. **EP-08a** — Complete mass balance at Entry 1 + 1.5 equiv. (closure ≥90%). Advances RI-08.
2. **EP-09a** — Head-to-head comparison table on ≥3 substrates from Lin (ref 60) + ≥3 from Gong (refs 29–30). Advances RI-09.
3. **EP-05a** — Derive predicted selectivity from k₁/k₂ (Fig. 4b); compare to 85:17:13. Advances RI-05, RI-07.

*Certification-gate note:* Investment order follows information gain, but final certification is fixed by gate order VQ-1 → VQ-2 → VQ-3 → VQ-4.

---

### §6 Contribution to institutional design

**PRI-11 promotion: two-paper confirmation satisfied.**
Pengfei 2024 independently confirms PRI-11, isomorphic with Breitenfeld 2014. The Ni(I/II/III) cycle is proposed (Fig. 5c); kinetic data (Fig. 4b) collected; no algebraic rate law derived; kinetic conclusion rests only on slope comparison. **PRI-11 is a promotion candidate.** Refined definition: [REDACTED: substantial verbatim quotation; see Tier 9]

**New representative case for RI-06 (cycle-level import):**
The entire Ni(I/II/III) cycle assembled from Ni organometallic precedent (Anderson & Vicic ref 65 for Ni(I)→Ni(III)) without demonstrated isomorphism under the paper's specific electrochemical conditions. CV/SWV from a three-electrode cell applied to the preparative two-electrode system without isomorphism verification. Clearest corpus case to date for the RI-06 scope note "cycle-level import."

**Labeling mismatch pattern detected:**
"Plausible" and "Path II cannot be ruled out" in the conclusion paragraph; preceding three paragraphs use assertive factual verbs throughout ("electroreduction of Ni(II) provided…"; "reductive elimination via dialkyl–Ni(III) complexes is preferred"). Hypothesis qualification concentrated in final two sentences. Co-occurrence with RI-06 confirmed.

**RI co-occurrence pattern: RI-04 + RI-06 in SRG-2.**
Resolving only RI-04 (uncertainty bounds) insufficient while RI-06 remains; resolving only RI-06 (stating functional) insufficient while the difference may lie within DFT error. Both must be resolved simultaneously.

**Incomplete negative evidence (RI-04 case-specific):**
TEMPO-trapping (product 95, 41%) provides qualitative evidence for radical involvement but no mass balance and no relative trapping efficiency of primary vs. secondary radical; negative control used as positive evidence without kinetic-window evaluation.

**New EP corpus implementations:**
- EP-03a in Ni electrochemical systems: in-situ EPR + UV-Vis spectroelectrochemistry at controlled cathode potential; distinct from X-ray of isolated intermediates in thermal Pd/Ni systems.
- EP-04a for radical-clock experiments: rearranged AND unrearranged yields required; ratio constrains cage vs. free radical for inner- vs. outer-sphere SET discrimination.
- EP-01a for multi-reference-electrode papers: unified reference scale via ferrocene required when CV (Ag/AgCl), SWV (Ag/AgNO₃), and DFT potentials are compared in the same paper. Proposed as standing requirement for electrochemical synthesis subfield.

---

> **Tier 8 redaction notice**: This file is a redacted copy of the corresponding Tier 3 / Tier 9 output. Verbatim source-paper quotations have been replaced by `[REDACTED: see source paper §<loc>; full text retained in Tier 9 reviewer-only deposit]` markers, preserving location references and our own analytical content. Bibliographic fields (title, authors, journal, year, DOI), analytical labels (`evidence_chain:` with B-/U-/A-/C- internal IDs), short technical terms, and our own analytical text are not redacted. The redaction was applied by `scripts/redact_for_tier8.py` and, for this version, by `scripts/build_paperA_R1_public.py` with `scripts/redact_source_ngram_runs.py` (scripts of the project repository; they are not deposited).
