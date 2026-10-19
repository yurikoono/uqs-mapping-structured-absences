```
prompt_version: stage1-v16.1-20260414

target_title:   Regiocontrol in the oxidative Heck reaction of indole by ligand-enabled switch of the regioselectivity-determining step
target_authors: Yu-Jie Wang, Chen-Hui Yuan, De-Zhao Chu and Lei Jiao
target_start:   page 1: [REDACTED: paper boundary quote; see Tier 9]
target_end:     end of document

[Turn 1: Agent V1]
field: Synthetic organic chemistry / Pd(II)-catalyzed C–H functionalization
field_rationale: BIB-3 (Chemical Science) and BIB-1 identify the paper as synthetic organometallic chemistry; S0-4 specifies Pd(II)-catalyzed aerobic oxidative Heck reaction with ligand design, placing the subfield squarely in Pd(II) C–H functionalization.

V1-Q1 | P6 (Table 2 footnote)* | [REDACTED: substantial verbatim quotation; see Tier 9] | What are the isolated yields and selectivity ratios (C2:C3) for each substrate entry under C2-alkenylation conditions? The table footnote states only C2-products were isolated, so the minor C3 co-product yield and the actual C2:C3 ratio are not quantified for individual entries. | high | T1

V1-Q2 | P5 (Table 1)* | [REDACTED: substantial verbatim quotation; see Tier 9] | Why are GC conversion and NMR yield used in Table 1 (optimization) while isolated yields are used in Table 2 (scope)? The relationship between these different metrics is never stated, and no correlation between NMR yield and isolated yield is provided. | medium | T1

V1-Q3 | P4 (Scheme 3)* | [REDACTED: substantial verbatim quotation; see Tier 9] | What is the yield or proportion of the Michael addition byproduct 3c, and does it form under the SOHP-ligand conditions? The text mentions it for MPAA/DAF conditions but does not report its formation or absence under optimal SOHP conditions. | medium | T1

V1-Q4 | P4 (Scheme 3)* | [REDACTED: substantial verbatim quotation; see Tier 9] | What is the yield of bisalkenylation product 3d under the final optimized conditions (entry 16, Table 1)? Table 1 shows 3d yields during optimization (6–15%), but the scope table (Table 2) does not report 3d for each entry. | medium | T1

V1-Q5 | P7 (Section 2.4)* | [REDACTED: substantial verbatim quotation; see Tier 9] | What yields were actually obtained with disubstituted olefins, and was any C2-selectivity observed at all? The paper describes "rather low reactivity" without reporting numbers. | low | T1

V1-Q6 | P7 (Section 2.4)* | [REDACTED: substantial verbatim quotation; see Tier 9] | What oxidation products are formed from NH-indoles, and was any characterization performed? The nature of the competing oxidation pathway is unstated. | medium | T1

V1-Q7 | P5 (Section 2.3)* | [REDACTED: substantial verbatim quotation; see Tier 9] | If PdCl₂·L17 is only implied to be a precatalyst, what is the actual resting-state Pd species during catalysis? The paper does not characterize the in-situ active catalyst. | high | T1

V1-Q8 | P6 (Scheme 5b)* | [REDACTED: substantial verbatim quotation; see Tier 9] | What is the time scale over which the C2 and C3 deuteration levels equilibrate, and at what conversion does the catalytic reaction typically occur? Without this, it is unclear whether the equilibration is relevant to catalytic turnover conditions. | medium | T1

V1-Q9 | P6 (Scheme 6)* | [REDACTED: substantial verbatim quotation; see Tier 9] | What is the C2:C3 selectivity ratio in the KIE experiment with C2-deuterated substrate vs. the non-deuterated control? Only yield is mentioned as diminished; the numerical selectivity shift is not reported. | medium | T1

V1-Q10 | P3 (Section 2.1)* | [REDACTED: substantial verbatim quotation; see Tier 9] | Which functional, basis set, and dispersion correction were used for the DFT calculations of the ligand-free system (Scheme 2)? The paper refers to ESI for "computational details" without stating them in the main text. | medium | T2

V1-Q11 | P8 (Scheme 8)* | [REDACTED: substantial verbatim quotation; see Tier 9] | The paper rules out thermodynamic control by showing the C3-insertion intermediate cannot convert to the C2-counterpart at 70 °C. Was the reverse experiment also tested — i.e., does the C2-insertion intermediate convert to the C3-counterpart? | high | T2

V1-Q12 | P7 (Table 2, entries 3 and 11)* | "N-tosylindole still preferred C3-product formation (entry 3)" | What is the observed C2:C3 ratio for N-tosylindole under SOHP conditions? Entry 3 is noted as an exception to C2-selectivity but no ratio is given. | medium | T1

V1-Q13 | P5 (Section 2.2, Table 1, entry 12)* | [REDACTED: substantial verbatim quotation; see Tier 9] | What specific C2:C3 ratio results from DMSO interference, and does DMSO coordinate competitively to Pd displacing the SOHP ligand? Only yield and selectivity are described qualitatively; no mechanistic investigation of the DMSO inhibition is provided. | medium | T1

V1-Q14 | P7 (Scheme 9)* | [REDACTED: substantial verbatim quotation; see Tier 9] | What are the isolated yields of products 23 and 24, and what is the 24a:24b ratio? The term "good yields" is not quantified here. | medium | T1
```

---

> **Tier 8 redaction notice**: This file is a redacted copy of the corresponding Tier 3 / Tier 9 output. Verbatim source-paper quotations have been replaced by `[REDACTED: see source paper §<loc>; full text retained in Tier 9 reviewer-only deposit]` markers, preserving location references and our own analytical content. Bibliographic fields (title, authors, journal, year, DOI), analytical labels (`evidence_chain:` with B-/U-/A-/C- internal IDs), short technical terms, and our own analytical text are not redacted. The redaction was applied by `scripts/redact_for_tier8.py` and, for this version, by `scripts/build_paperA_R1_public.py` with `scripts/redact_source_ngram_runs.py` (scripts of the project repository; they are not deposited).
