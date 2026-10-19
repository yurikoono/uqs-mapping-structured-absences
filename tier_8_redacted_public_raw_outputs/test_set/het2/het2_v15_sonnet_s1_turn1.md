```
prompt_version: stage1-v15-20260331
```

```
target_title:   Deconvoluting Substrates, Support, and Temperature Effects on Leaching and Deactivation of Pd Catalysts: An In Situ Study in Flow
target_authors: Oliver J. Newton, Matthew J. Takle, Jeffery Richardson, Klaus Hellgardt, and King Kuok Mimi Hii
target_start:   page 1: [REDACTED: paper boundary quote; see Tier 9]
target_end:     end of document
```

```
[Turn 1: Agent V1]
field: Heterogeneous catalysis / continuous-flow Pd cross-coupling chemistry
field_rationale: The journal (ACS Catalysis) and methodology (tandem flow reactor with packed-bed and plug-flow stages, ICP–MS leaching quantification) place the paper squarely in supported-metal heterogeneous catalysis studied in flow.

V1-Q1
loc: P2:Lcol:1-5* (Results, "Nature of Support")
quote: [REDACTED: see `loc:` above; full text in Tier 9]
question: What are the actual Pd loadings (wt%) and total surface areas of the three commercial catalysts? Normalizing leached Pd to total Pd by mass (4 mg) without knowing loading % or dispersion means the comparison is on absolute mass rather than on per-surface-Pd or per-active-site bases, making cross-catalyst comparisons potentially misleading.
severity: high
inference_tier: T2 [paper-grounded inference]

V1-Q2
loc: P2:Lcol:1-5* (Results, "Nature of Support")
quote: [REDACTED: see `loc:` above; full text in Tier 9]
question: What was the bed volume (void fraction, packing density) and residence time in the PBR for each of the three catalysts? Different catalysts may have very different bulk densities and packing characteristics, meaning equivalent Pd mass does not imply equivalent contact time with the mobile phase.
severity: high
inference_tier: T2 [paper-grounded inference]

V1-Q3
loc: P3:Lcol:30-40* (Results, "Assessment of Individual Reaction Components")
quote: [REDACTED: see `loc:` above; full text in Tier 9]
question: For the iodobenzene experiment with PdEnCat 30 (Fig. 7C), what is the conversion at S1 (bed outlet) versus S2 (PFR outlet) at 90 °C? The modified reactor (configuration 2) only collects samples at the outlet; it is not stated whether the conversion observed is attributable entirely to leached Pd in the PFR or includes any heterogeneous contribution from the PBR itself.
severity: high
inference_tier: T2 [paper-grounded inference]

V1-Q4
loc: P4:Lcol:1-10* (Results, "Assessment of Individual Reaction Components", NEt3 experiment)
quote: [REDACTED: see `loc:` above; full text in Tier 9]
question: Figure 4B used DMF as solvent containing all three reaction components (PhI, acrylate, NEt3) at T1 = 30 °C, while the NEt3 experiment (Fig. 7D) uses DMF as the mobile phase with NEt3 at F1 and only PhI + acrylate at F2. Are the flow rates, Pd loading, and total experiment duration strictly identical between these two experiments such that the 182 vs. 194 ppm comparison is valid?
severity: high
inference_tier: T2 [paper-grounded inference]

V1-Q5
loc: P1:Rcol:15-25* (Introduction)
quote: [REDACTED: see `loc:` above; full text in Tier 9]
question: No carbon balance or mass balance for the Heck reaction is provided in the main text. What are the yields of methyl cinnamate relative to iodobenzene consumed, and are any side products (e.g., biphenyl from homocoupling, stilbene from double bond isomerization) observed? Absence of mass balance makes it impossible to assess whether leached Pd catalyses the same reaction pathway as the heterogeneous catalyst.
severity: medium
inference_tier: T2 [paper-grounded inference]

V1-Q6
loc: P2:Rcol:20-35* (Results, "Solvent Effects", flow reactor section)
quote: [REDACTED: see `loc:` above; full text in Tier 9]
question: The ICP–MS measurement reports total Pd in the collected mobile-phase fractions. What is the speciation of the leached Pd (Pd(0) clusters, Pd(II) complexes, colloidal Pd)? Without speciation data, the paper's mechanistic interpretation (e.g., that DMF stabilizes nanoclusters) remains speculative.
severity: medium
inference_tier: T2 [paper-grounded inference]

V1-Q7
loc: P3:Rcol:1-15* (Results, "Nature of Support", Pd/Al2O3 section)
quote: [REDACTED: see `loc:` above; full text in Tier 9]
question: For Pd/Al2O3 at 90 °C in DMF (Fig. 5C), what happens beyond 90 min? The experiment appears to end at 90 min; whether the pseudosteady state is sustained or whether further deactivation occurs is not shown.
severity: medium
inference_tier: T2 [paper-grounded inference]

V1-Q8
loc: P2:Lcol:15-25* (Results, "Solvent Effects", batch section)
quote: [REDACTED: see `loc:` above; full text in Tier 9]
question: No ICP–MS data for leached Pd in the batch experiments are reported; only color observation is used as a proxy for leaching. Why were the batch reaction aliquots not subjected to ICP–MS analysis, and how does the batch leaching extent compare quantitatively to the flow reactor data?
severity: medium
inference_tier: T2 [paper-grounded inference]

V1-Q9
loc: P4:Rcol:5-15* (Results, Pd/Al2O3, triethylamine section)
quote: [REDACTED: see `loc:` above; full text in Tier 9]
question: The 6 ppm background leaching in the NEt3 experiment with Pd/Al2O3 — is this within the ICP–MS blank/detection limit for this experimental setup? The paper does not report a control experiment (catalyst-free) to establish the background Pd level in the mobile phase.
severity: medium
inference_tier: T2 [paper-grounded inference]

V1-Q10
loc: P4:Rcol:20-30* (Results, Pd/Al2O3, iodobenzene section)
quote: [REDACTED: see `loc:` above; full text in Tier 9]
question: For Pd/Al2O3 exposed to iodobenzene at 90 °C (Fig. 9A), conversion data appear to be available only for 60 min before the experiment ends. Is the pseudosteady-state conversion sustained beyond this point, or is the experiment terminated prematurely? This limits confidence in the claim of no deactivation.
severity: medium
inference_tier: T2 [paper-grounded inference]

V1-Q11
loc: P5:Lcol:1-10* (Conclusions)
quote: [REDACTED: see `loc:` above; full text in Tier 9]
question: What is the actual residence time in the PBR, and how does it compare to the timescale for Pd re-deposition measured in prior studies? The dismissal of boomerang catalysis is stated as an inference from short residence time but no quantitative support is given.
severity: medium
inference_tier: T2 [paper-grounded inference]

V1-Q12
loc: P2:Lcol:30-40* (Results, "Nature of Support", FC-1001 section)
quote: [REDACTED: see `loc:` above; full text in Tier 9]
question: Is the difference between 735 ppm (FC-1001) and 455 ppm (PdEnCat 30) statistically significant? No replicate experiments or error estimates are reported for any of the ICP–MS measurements in the paper.
severity: high
inference_tier: T2 [paper-grounded inference]

V1-Q13
loc: P3:Lcol:20-30* (Results, "Assessment of Individual Reaction Components", introduction to config 2)
quote: [REDACTED: see `loc:` above; full text in Tier 9]
question: In configuration 2, the component used at F1 flows through the PBR and then mixes at F2 with the remaining components. Does the F1 stream (containing leached Pd) enter the PFR already at reaction temperature, or is there a temperature transition zone? Mixing geometry and thermal equilibration details are not reported, yet they affect the conversion observed at the PFR outlet.
severity: medium
inference_tier: T2 [paper-grounded inference]

V1-Q14
loc: P2:Rcol:35-45* (Results, "Solvent Effects", toluene and dioxane)
quote: [REDACTED: see `loc:` above; full text in Tier 9]
question: In dioxane and toluene with PdEnCat 30, S1 and S2 profiles are identical and attributed entirely to heterogeneous catalysis. However, 10 and 140 ppm Pd were still detected in the mobile phase. What is the conversion in the PFR if 140 ppm of Pd (toluene case) is present but produces no detectable S2 > S1 increase? Is the PFR conversion measurement sensitive enough to detect activity from sub-200 ppm dissolved Pd?
severity: medium
inference_tier: T2 [paper-grounded inference]
```

---

> **Tier 8 redaction notice**: This file is a redacted copy of the corresponding Tier 3 / Tier 9 output. Verbatim source-paper quotations have been replaced by `[REDACTED: see source paper §<loc>; full text retained in Tier 9 reviewer-only deposit]` markers, preserving location references and our own analytical content. Bibliographic fields (title, authors, journal, year, DOI), analytical labels (`evidence_chain:` with B-/U-/A-/C- internal IDs), short technical terms, and our own analytical text are not redacted. The redaction was applied by `scripts/redact_for_tier8.py` and, for this version, by `scripts/build_paperA_R1_public.py` with `scripts/redact_source_ngram_runs.py` (scripts of the project repository; they are not deposited).
