```
prompt_version: stage1-v17-20260415

[Turn 1: Agent V1]
field: Transition-metal-catalyzed C–H functionalization / Pd(II) organometallic chemistry / synthetic organic chemistry
field_rationale: The paper reports a Pd(II)-catalyzed aerobic oxidative Heck C–H alkenylation of indoles with DFT mechanistic support, published in Chemical Science; V1 therefore represents the specialist in homogeneous Pd catalysis and C–H functionalization.

target_title:   Regiocontrol in the oxidative Heck reaction of indole by ligand-enabled switch of the regioselectivity-determining step
target_authors: Yu-Jie Wang, Chen-Hui Yuan, De-Zhao Chu, Lei Jiao
target_start:   page 1: [REDACTED: paper boundary quote; see Tier 9]
target_end:     end of document

---

V1-Q1
loc: P9:Lcol (Section 2.4, paragraph on electron-deficient olefins)*
quote: [REDACTED: see `loc:` above; full text in Tier 9]
question: The attribution of failure with acrylonitrile (Table 2, entry 17: only 22% C2 yield) to "difficulty in C2-palladation" is stated without experimental or computational evidence. The DFT study models only the standard tert-butyl acrylate substrate; were DFT calculations performed for acrylonitrile to distinguish whether the bottleneck is the palladation step or the insertion step?
severity: medium
inference_tier: T2

V1-Q2
loc: P3:Rcol (Table 1, entry 1, footnote)*
quote: [REDACTED: substantial verbatim quotation; see Tier 9] [Table 1, entry 1: 86% conv., 3a 76%, 3b 10%, 3d 0%, overall 10%]
question: Entry 1 (no ligand) affords 10% C2 product (3b) alongside 76% C3 product despite the paper's claim that the intrinsic selectivity is C3. Is this 10% C2 within measurement error, or does it reflect a bona fide ligand-independent C2 pathway whose origin is not discussed?
severity: medium
inference_tier: T1

V1-Q3
loc: P8:Lcol (Table 2, footnote a)*
quote: [REDACTED: see `loc:` above; full text in Tier 9]
question: For C2-alkenylation conditions in Table 2, only C2 products are isolated and reported; the fate of the remaining substrate (recovery vs. decomposition) and the co-produced C3 byproduct yield are not stated. What is the mass balance?
severity: medium
inference_tier: T1

V1-Q4
loc: P7:Lcol (Scheme 8)*
quote: [REDACTED: see `loc:` above; full text in Tier 9]
question: Norbornene is used as the alkene in stoichiometric mechanistic Scheme 8 (insertion trap), not the actual substrate tert-butyl acrylate. Norbornene cannot undergo β-hydride elimination, making it a special case. The relevance of this experiment to the acrylate pathway is not established.
severity: medium
inference_tier: T2

V1-Q5
loc: P8:Rcol (Section 2.3 DFT paragraph)*
quote: [REDACTED: see `loc:` above; full text in Tier 9]
question: The role of Cu(II) as a stoichiometric HCl scavenger rather than oxidant is assigned from DFT. Was this role validated experimentally, for example by replacing Cu(II) with an inorganic base (K₂CO₃, Et₃N) at comparable stoichiometry and measuring the effect on yield and C2/C3 ratio?
severity: medium
inference_tier: T2

V1-Q6
loc: P8:Lcol (Table 2, entry 2)*
quote: [REDACTED: see `loc:` above; full text in Tier 9]
question: N-H indole (entry 2) participates in both C2- and C3-alkenylation without any discussion of whether the NH acts as a ligand, undergoes N-palladation, or is deprotonated under the reaction conditions. No mechanistic comment on this substrate is provided despite its structural difference from N-methyl substrates.
severity: medium
inference_tier: T2

V1-Q7
loc: P8:Lcol (Table 2, entry 3)*
quote: [REDACTED: see `loc:` above; full text in Tier 9]
question: N-Ts indole gives no product under C3-alkenylation conditions (DMSO ligand), while affording 80% yield (C3/C2 = 12:1) under C2 conditions. The paper does not explain why the strongly electron-withdrawing N-Ts group prevents C3-functionalization under the DMSO system but permits it under SOHP conditions.
severity: medium
inference_tier: T1

V1-Q8
loc: P8:Rcol (Table 2, entry 11)*
quote: [REDACTED: see `loc:` above; full text in Tier 9]
question: The doubly substituted indole 1k (5-OMe, 6-CO₂Me) gives no product under C3-alkenylation conditions. No electronic or steric rationale is provided, and no scope failure attribution is offered. Is the failure due to steric clash at C3, electronic deactivation, or catalyst poisoning by the ester?
severity: medium
inference_tier: T1

V1-Q9
loc: P5:Lcol (Section 2.3, KIE paragraph)*
quote: [REDACTED: see `loc:` above; full text in Tier 9]
question: The KIE = 3.3 is reported from an intermolecular H/D competition experiment. At what conversion was the KIE determined? If measured at high conversion, competitive product inhibition or isotope-dilution effects may distort the apparent KIE. The experimental protocol for the KIE measurement is not stated in the main text (deferred to ESI).
severity: medium
inference_tier: T2

V1-Q10
loc: P7:Lcol (Section 2.3, DFT activation energy discussion)*
quote: [REDACTED: see `loc:` above; full text in Tier 9]
question: DFT-calculated activation barriers are not validated against experimental activation parameters (ΔH‡, ΔS‡) from Eyring analysis. The paper reports KIE = 3.3 as consistent with C–H activation being rate-determining, but whether the 18.5 kcal mol⁻¹ barrier is quantitatively consistent with the observed reaction rate at 70°C is not discussed.
severity: medium
inference_tier: T2

V1-Q11
loc: P5:Rcol (Table 1, entries 12–16)*
quote: [REDACTED: see `loc:` above; full text in Tier 9]
question: Entry 16 uses 5 mol% Pd (vs 10 mol% elsewhere) and 50°C/12 h conditions (vs 70°C/3 h); these are not the same conditions as entries 8 and 15. The paper selects entry 16 as optimal but the individual contributions of reduced Pd loading, lower temperature, and extended time to the improved C2-selectivity are not deconvoluted.
severity: medium
inference_tier: T1

V1-Q12
loc: P10:Lcol (Scheme 9)*
quote: [REDACTED: see `loc:` above; full text in Tier 9]
question: The C2-alkenylation of tryptophan and tryptophol derivatives (Scheme 9) gives only 24% and 39% yields—substantially below the 44–80% range for unnatural indoles in Table 2. The paper presents these as successful applications but provides no explanation for the reduced efficiency or discussion of whether the amino acid/alcohol side-chain interferes with the catalytic cycle.
severity: medium
inference_tier: T1

V1-Q13 [Dropped Quantitative Benchmark]
loc: P1:Rcol (Introduction, Scheme 1a)*
quote: [REDACTED: see `loc:` above; full text in Tier 9]
question: The introduction cites the prior C3-selective method with a specific 75% yield (Scheme 1a, ref 13e) as the benchmark. The current C3-conditions (Table 1/Table 2) give comparable or slightly higher C3 yields, but no explicit comparison of isolated yield or selectivity against that numerical benchmark is made in the results section.
severity: low
inference_tier: T1

V1-Q14
loc: P4:Rcol (Section 2.2, paragraph on ligand optimization)*
quote: [REDACTED: see `loc:` above; full text in Tier 9]
question: Ligands L5 (bipyridine) and L6 (1,10-phenanthroline) afford trace C2 products but are not further optimized. The paper does not explain whether bidentate N,N-donor ligands were systematically excluded due to catalyst inhibition, and why the sulfooxide-pyridine bidentate motif (κ²-S,N) works whereas κ²-N,N does not.
severity: medium
inference_tier: T2

V1-Q15 [ESI delegation check]
loc: P5:Lcol (Section 2.3, stoichiometry paragraph)*
quote: [REDACTED: see `loc:` above; full text in Tier 9]
question: The quasi-reversibility of C2-palladation in the SOHP system is a central mechanistic claim. The primary evidence (time-course of D-incorporation at C2 vs C3 in the SOHP system, Scheme 5 right plot) is stated qualitatively in the main text; the paper notes "see ESI†" for further details. The quantitative D% values for both positions at multiple time points are deferred to ESI, meaning the central mechanistic evidence is not fully presented in the main text. Does the ESI data rule out that D-incorporation at C3 in the SOHP system arises from a secondary pathway (re-protonation of a C2-Pd species at C3 by solvent exchange) rather than genuine reversibility?
severity: high
inference_tier: T2
```

---

> **Tier 8 redaction notice**: This file is a redacted copy of the corresponding Tier 3 / Tier 9 output. Verbatim source-paper quotations have been replaced by `[REDACTED: see source paper §<loc>; full text retained in Tier 9 reviewer-only deposit]` markers, preserving location references and our own analytical content. Bibliographic fields (title, authors, journal, year, DOI), analytical labels (`evidence_chain:` with B-/U-/A-/C- internal IDs), short technical terms, and our own analytical text are not redacted. The redaction was applied by `scripts/redact_for_tier8.py` and, for this version, by `scripts/build_paperA_R1_public.py` with `scripts/redact_source_ngram_runs.py` (scripts of the project repository; they are not deposited).
