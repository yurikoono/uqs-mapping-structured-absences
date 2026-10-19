```
prompt_version: stage1-v184-20260502 / turn3
```

---

```
target_title:   Nickel-Catalyzed Asymmetric Kumada Cross-Coupling of Symmetric Cyclic Sulfates
target_authors: Meredith S. Eno, Alexander Lu, and James P. Morken
target_start:   page 1: [REDACTED: paper boundary quote; see Tier 9]
target_end:     end of document
```

---

[Turn 3: Agent V3]
field: Analytical chemistry / chiral chromatography (SFC on chiral stationary phase; absolute configuration assignment; mass-balance and yield reporting)
field_rationale: The paper's entire enantioselectivity dataset rests on SFC analysis on unspecified chiral stationary phases; no column identity, mobile phase, flow rate, temperature, or retention-time data are reported in the communication. V1 treated yield/er numbers as given and interrogated their reproducibility and scope asymmetry from a synthetic perspective. V2 treated the same er values as kinetic/mechanistic readouts and interrogated their physical-organic interpretation. Neither agent addressed the analytical validity of the measurement instrument: whether the SFC method is validated for each substrate class, whether absolute configurations are assigned (and by what method), whether er and yield are determined from the same or different aliquots, and whether the mass-balance of each reaction is accounted for. In a communication reporting 17 product er values as the primary evidence for a new asymmetric reaction, the analytical integrity of the SFC method and the absolute configuration assignments are foundational — not incidental — claims that require scrutiny.

--- New questions ---

V3-Q1
loc: P2:Rcol:1-10 (Table 2 footnote a) and P2:Lcol:1-10 (Table 1 footnote a)
quote: [REDACTED: see `loc:` above; full text in Tier 9]
question: For all 17 products in Table 2 and all ligand-screen entries in Table 1, er is determined by SFC on a chiral stationary phase, but neither the column identity (e.g., Chiralpak IA/IB/IC/AD, Chiralcel OD, etc.), mobile phase composition, flow rate, column temperature, nor retention times/separation factors (α) are reported in the communication (presumably in SI). For products spanning a wide structural range — aliphatic (2–4), phenyl-bearing (5, 6), benzyloxy (7), N-heterocyclic (17, 18), and heteroatom-substituted (21) substrates — a single SFC method is unlikely to resolve all enantiomers with equal baseline separation. Is a single chiral column and solvent system used across all substrates, or substrate-specific methods? What are the resolution factors (Rs) for each substrate, and for substrates with low er (88:12), is baseline separation confirmed or are overlapping peaks averaged?
severity: high
inference_tier: T2 [paper-grounded inference]

---

V3-Q2
loc: P2:Rcol:1-10 (Table 2, footnote a) and P3:Lcol:15-25 (Scheme 2, eq 5)
quote: [REDACTED: see `loc:` above; full text in Tier 9]
question: The paper reports isolated yield (from silica gel chromatography) and er (from SFC) as the two primary data outputs for each entry, but does not specify whether the er was measured on the isolated product or on a crude reaction mixture aliquot. If er is measured on a crude aliquot before silica gel chromatography, purification could selectively remove minor enantiomers or diastereomers co-migrating with silica, leading to an artificially inflated er in the isolated product. Conversely, if er is measured only on the isolated product, any racemic by-product that elutes at a different Rf would be excluded from the er measurement but included in overall yield. Is the er reported pre- or post-silica-gel purification, and does the purification step affect the measured er for any substrate?
severity: medium
inference_tier: T2 [paper-grounded inference]

---

V3-Q3
loc: P3:Lcol:40-55 (Scheme 3, eq 7 and eq 8) and P3:Rcol (Scheme 4)
quote: [REDACTED: see `loc:` above; full text in Tier 9]
question: The 90% diastereospecificity (ds) in the deuterium-labeling experiment (eq 8) is determined "in comparison to authentic isotopically labeled compounds." The analytical method for this determination is not specified. Diastereomers bearing a deuterium label at a tertiary carbon adjacent to a primary alcohol (compound 27) may be difficult to distinguish by standard ¹H NMR (small Δδ for CHD vs. adjacent CH), and SFC on a chiral column may not resolve a pair of diastereomers unless optimized for this substrate. What analytical method was used to determine the 90% ds — ¹H NMR integration, ²H NMR, GC-MS (isotope ratio), or SFC — and how were the authentic diastereomers synthesized and characterized to establish the reference comparison?
severity: high
inference_tier: T1

---

V3-Q4
loc: P2:Rcol:1-10 (Table 2 header and footnote a)
quote: [REDACTED: see `loc:` above; full text in Tier 9]
question: The reaction uses 1.5 equivalents of Grignard reagent relative to the cyclic sulfate. The cyclic sulfate is a bis-electrophile with two C–O bonds, so one equivalent of Grignard is consumed in the desired monocoupling and a second equivalent could in principle react with the sulfate half-ester 20 (shown isolable in eq 5). The mass balance of the reaction — accounting for recovered starting material, product 2 (or related), sulfate half-ester 20, bis-coupled product, and Grignard self-coupling products — is not reported. What fraction of cyclic sulfate and Grignard reagent is recovered or consumed in productive vs. unproductive pathways, and is the 84% isolated yield of 2 accompanied by a mass-balance closure that confirms the absence of significant amounts of sulfate half-ester 20 or bis-coupling product?
severity: medium
inference_tier: T2 [paper-grounded inference]

---

V3-Q5
loc: P2:Lcol:40-55 (Table 1 text)
quote: [REDACTED: see `loc:` above; full text in Tier 9]
question: The ligand survey (Table 1) was conducted with a 6 h acid hydrolysis deprotection, whereas the substrate scope (Table 2) uses 24 h. Table 1 reports isolated yields post-hydrolysis, but the incomplete hydrolysis at 6 h means that some yield in Table 1 represents sulfate half-ester (compound 20) rather than alcohol product — yet both would appear as the same compound if the half-ester is also detectable by SFC. Was the er of the half-ester 20 measured in Table 1 entries, and are the er values in Table 1 for product alcohol 2 or for a mixture of alcohol 2 and sulfate half-ester 20? Was the ester hydrolysis efficiency quantified as a separate step?
severity: medium
inference_tier: T2 [paper-grounded inference]

---

V3-Q6
loc: P2:Rcol:40-55 (Table 2, products 5 and 6) and P2:Rcol:50-60 (footnote b)
quote: [REDACTED: see `loc:` above; full text in Tier 9]
question: Products 5 (phenyl-substituted, 61% y, 88:12 er) and 6 (phenethyl-substituted, 63% y, 88:12 er) are the lowest-er entries in Table 2, and substrate 14 (footnote b) requires 6 mol% Ni loading (vs. 3 mol% standard) with 91% y but 93:7 er. The 88:12 er entries use the same 3 mol% loading as the other entries. For two substrates independently giving 88:12 er, it is important to know whether this represents a reproducible minimum plateau of the catalyst system or whether the inter-run variance (reported only as "average of two experiments" with no range) encompasses values as low as 84:16 or as high as 92:8. Is 88:12 a reproducible er for substrates 5 and 6, or does it represent a noisy measurement near the baseline of catalyst performance? What is the run-to-run range for these lowest-er entries?
severity: medium
inference_tier: T2 [paper-grounded inference]

---

V3-Q7
loc: P3:Lcol:1-12 (Scheme 2, eq 4)
quote: [REDACTED: see `loc:` above; full text in Tier 9]
question: The chroman synthesis (eq 4) reports 53% yield and 94:6 er for chroman 19, derived from alcohol 11 (95:5 er). The claim "complete preservation of enantiomeric purity" implies no measurable erosion of er (95:5 → 94:6, which is within 1 er unit). However, the analytical method for er measurement of chroman 19 is not specified — whether the same chiral SFC column/method used for the primary alcohol products is applicable to a chroman framework is not stated. Chromans are bicyclic aromatic-aliphatic compounds with very different polarity/shape from the primary alcohols in Table 2. Was a validated chiral SFC method confirmed for chroman 19 specifically, and is the 1-er-unit apparent change (95:5 → 94:6) within the measurement precision of the SFC method?
severity: low
inference_tier: T2 [paper-grounded inference]

---

V3-Q8
loc: P1:Rcol (Introduction, eq 3, Scheme 1) and P2:Lcol (Table 1, synthesis of starting material)
quote: [REDACTED: see `loc:` above; full text in Tier 9]
question: The cyclic sulfate substrates (e.g., compound 1) are prepared from 1,3-diols via cyclic sulfate formation (typically with SOCl2 then oxidation, or directly with SO2Cl2). The enantiopurity of the product alcohols (2–18) is measured, but the diastereomeric/enantiomeric purity of the prochiral cyclic sulfate starting materials is not reported — they are symmetric and thus achiral, so this is not an issue for enantioselectivity. However, if the sulfate preparation introduces any asymmetric impurity (e.g., monosulfate monoester or partially oxidized species) into the "symmetric" bis-electrophile, this could generate a chiral contaminant that couples enantiospecifically with the Ni catalyst. Was the symmetry (and thus prochirality) of each cyclic sulfate confirmed analytically (e.g., by ¹H NMR symmetry, absence of SFC peaks for a resolved chiral species), and was the purity of each substrate determined before use in coupling?
severity: low
inference_tier: T2 [paper-grounded inference]

---

V3-Q9
loc: P3:Lcol:1-12 (Scheme 3, eq 7)
quote: [REDACTED: see `loc:` above; full text in Tier 9]
question: The radical clock experiment (eq 7) reports "only product 24 was detected" and 56% isolated yield. The detection claim — that ring-opened product 25 was not observed — requires a specified detection method and detection limit. In particular, if product 25 (ring-opened homoallylic alcohol derivative) and product 24 (ring-intact Kumada product) have similar Rf on silica, they might co-elute during purification. Alternatively, if GC-MS was used to analyze the crude mixture, the detection limit for a <5% contaminant should be stated. What method was used to confirm the absence of 25 (¹H NMR of crude, GC-MS, SFC, or TLC), at what detection limit, and were authentic 25 or a structurally analogous ring-opened standard available as a retention-time reference?
severity: medium
inference_tier: T2 [paper-grounded inference]

---

V3-Q10
loc: P2:Rcol:25-40 (Table 2, products 8–16)
quote: [REDACTED: see `loc:` above; full text in Tier 9]
question: The Grignard coupling partner scope (products 8–16) covers nine aryl Grignard reagents with diverse electronic and steric properties: alkyl-donor (8, 9, 10), alkoxy-donor (12, 13), silyl-donor (15), fluorine (14), chlorine (16), and N-heterocyclic (17, 18). For eight of these nine substrates, er ranges from 89:11 to 95:5. However, the chiral SFC method is likely substrate-specific — aryl-containing products with fluorine (14), chlorine (16), or trimethylsilyl (15) groups may have fundamentally different UV absorbance profiles or polarity than PhMgBr-derived product 2. Were substrate-specific SFC methods validated for each structural class, or was a single universal method applied? For products eluting near the stationary phase dead volume, is the reported er unaffected by potential co-elution of impurities (e.g., protodehalogenated Grignard self-coupling products)?
severity: medium
inference_tier: T2 [paper-grounded inference]

---

--- Overlaps with V1/V2 ---

V3-OV1 | overlaps_with: V1-Q3 | severity_V3: high | note: V1 noted that Table 2 reports averaged results from two experiments with no standard deviation or range for yield or er. From an analytical chemistry perspective, this is more severe than V1 framed it: the er measurement itself is subject to analytical uncertainty (SFC peak integration, baseline correction, noise) in addition to run-to-run reaction variance. The combined uncertainty — measurement error in SFC + reaction reproducibility — is reported as a single averaged value with no confidence interval. For entries near the threshold of "good selectivity" (88:12 er for substrates 5 and 6), the analytical uncertainty in SFC peak integration (typically ±0.5–1% per peak) combined with run-to-run variation could make the true er uncertain by ±2–4 units. The paper's claim that 88:12 er represents meaningful selectivity cannot be evaluated without knowing this combined uncertainty.

V3-OV2 | overlaps_with: V1-Q6 | severity_V3: medium | note: V1 raised the detection limit for ring-opened product 25 in the radical clock experiment. From an analytical chemistry perspective, this overlaps with V3-Q9: the claim "only 24 was detected" is analytically meaningful only if the detection method and detection limit are stated. V1 framed this as an evidence quality issue; V3 frames it as a missing method specification that undermines the mechanistic conclusion.

V3-OV3 | overlaps_with: V1-Q12 | severity_V3: medium | note: V1 raised whether Table 1 er values are confounded by the 6 h vs. 24 h deprotection protocol. From an analytical chemistry perspective, if the crude mixture contains both alcohol product 2 and sulfate half-ester 20 when assayed by SFC after incomplete hydrolysis, the two compounds may have different retention times on the chiral column, and an er measurement of an incompletely deprotected mixture would not correctly represent the er of either species. This could mean that the ligand-ranking in Table 1 is based on er values measured from a mixture of two different compounds, not from the target alcohol 2 alone.

V3-OV4 | overlaps_with: V2-Q4 | severity_V3: high | note: V2 raised whether the 90% ds in the deuterium-labeling experiment could be affected by incomplete stereospecificity of reductive elimination (an unstated assumption). From an analytical chemistry perspective, the determination of 90% ds "in comparison to authentic isotopically labeled compounds" requires an analytical method capable of resolving the two diastereomers of 27 — compounds differing only in the configuration of a CHD group adjacent to a primary alcohol. This is a very subtle structural difference. V3-Q3 elaborates the analytical method concern independently, but it fully overlaps with V2-Q4 in its mechanistic consequence: if the analytical method for ds determination is not validated, the 90% ds figure — and the mechanistic interpretation built on it — is not securely established.

---

> **Tier 8 redaction notice**: This file is a redacted copy of the corresponding Tier 3 / Tier 9 output. Verbatim source-paper quotations have been replaced by `[REDACTED: see source paper §<loc>; full text retained in Tier 9 reviewer-only deposit]` markers, preserving location references and our own analytical content. Bibliographic fields (title, authors, journal, year, DOI), analytical labels (`evidence_chain:` with B-/U-/A-/C- internal IDs), short technical terms, and our own analytical text are not redacted. The redaction was applied by `scripts/redact_for_tier8.py` and, for this version, by `scripts/build_paperA_R1_public.py` with `scripts/redact_source_ngram_runs.py` (scripts of the project repository; they are not deposited).
