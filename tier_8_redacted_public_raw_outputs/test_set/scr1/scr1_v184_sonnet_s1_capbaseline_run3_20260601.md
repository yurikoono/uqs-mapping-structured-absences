```
prompt_version: stage1-v184-20260502
model_info: claude-sonnet-4-6
arm: cap_baseline (prompts/v184/ — V1: 10–15 questions, V2: 8–12, V3: 6–10)
run: 3
date: 2026-06-01
```

---

# Stage 1 Turn 4 Synthesis — ARM A: Cap Baseline (Run 3)

```
prompt_version: stage1-v184-20260502
model_info: claude-sonnet-4-6

target_title:   Homogeneous Pd-Catalyzed Heck Coupling in γ-Valerolactone as a Green Reaction Medium: A Catalytic, Kinetic, and Computational Study
target_authors: Dániel Fodor, Tamás Kégl, József M. Tukacs, Attila K. Horváth, László T. Mika
target_start:   page 1: [REDACTED: paper boundary quote; see Tier 9]
target_end:     end of document

[Agent fields]
V1: Physical organic chemistry / homogeneous catalysis — specialist in kinetic analysis and mechanism of Pd-catalyzed Heck coupling
V2: Computational chemistry / DFT methodology — specialist in transition-state calculations and energy surface analysis
V3: Chemical kinetics / physical chemistry — specialist in kinetic model validation, parameter estimation, and statistical reliability
```

---

## Turn 1 — Agent V1

```
[Turn 1: Agent V1]
field: Physical organic chemistry / homogeneous catalysis
field_rationale: BIB-3 (ACS Sustainable Chemistry & Engineering), BIB-1 (Heck coupling with kinetic and computational study), and S0-4 (kinetic parameter determination, Hammett LFERs, Eyring analysis) identify this as a homogeneous catalysis / physical organic chemistry paper focused on kinetics, mechanism, and catalyst evaluation.

V1-Q1 | P6:L3-8* (Table 2) | [REDACTED: substantial verbatim quotation; see Tier 9] | The K₁k₂ composite rate constants are reported with uncertainties, but the individual uncertainties on K₁ and k₂ are never separately reported. What are the propagated uncertainties on the derived activation parameters (ΔH‡_app, ΔS‡_app) calculated from these composite K₁k₂ values? | critical | T2 [paper-grounded inference]

V1-Q2 | P7:L18-22* | [REDACTED: substantial verbatim quotation; see Tier 9] | No uncertainty (±) is reported for ΔH‡_app or ΔS‡_app in either GVL or DMF. What are the standard errors or confidence intervals on these key thermodynamic parameters derived from the Eyring plot? | critical | T1

V1-Q3 | P8:L5-10* | [REDACTED: substantial verbatim quotation; see Tier 9] | The mechanistic conclusion (no medium effect) rests on the ΔS‡_app values being "very similar," yet no statistical test or uncertainty propagation is presented to assess whether the two values are distinguishable within experimental error. How similar must ΔS‡_app values be to conclude no medium effect, given the absence of reported uncertainties? | high | T2 [paper-grounded inference]

V1-Q4 | P4:L12-18* | [REDACTED: substantial verbatim quotation; see Tier 9] | The selectivity ratio 3a:4a at full conversion in GVL is not reported. Is the 3a:4a product ratio time-dependent (kinetic vs thermodynamic distribution), and what is the quantitative selectivity at complete conversion? | medium | T2 [paper-grounded inference]

V1-Q5 | P6:L32-38* | [REDACTED: substantial verbatim quotation; see Tier 9] | The orders are stated as "slightly lower than unity" but the actual fitted values are deferred to SI Figure S2 and never stated in the main text. What are the quantitative kinetic orders in iodobenzene and styrene under the fitted model, and do the deviations from unity carry physical significance? | medium | T1

V1-Q6 | P4:L38-45* | [REDACTED: substantial verbatim quotation; see Tier 9] | The Hammett analysis uses TOF at 30 min rather than initial rates. Is the reaction sufficiently early (low conversion) at 30 min under all conditions such that TOF at 30 min is equivalent to initial TOF, and if not, how does conversion-dependent catalyst evolution affect the LFER? | high | T2 [paper-grounded inference]

V1-Q7 | P4:L20-28* | [REDACTED: substantial verbatim quotation; see Tier 9] for styrene derivatives | The R² = 0.860 for the styrene Hammett correlation is described as "acceptable" without statistical qualification. Are any data points outliers by formal statistical criteria, and was the correlation tested for leverage/influence? | medium | T2 [paper-grounded inference]

V1-Q8 | P3:L22-28* | [REDACTED: substantial verbatim quotation; see Tier 9] | The base (Et₃N) is used in 1.2 equivalents — the same loading as styrene — but its concentration is never systematically varied in the kinetic study. How does variation of [Et₃N] affect the rate, and is base a kinetically significant variable in the fitted model? | high | T1

V1-Q9 | P5:L8-14* | [REDACTED: substantial verbatim quotation; see Tier 9] | The catalyst precursor screening is performed at 403 K whereas the kinetic study uses 363–393 K. Are the precatalyst comparison results transferable to kinetic conditions, and is the activation mechanism (Pd(II) → Pd(0)) the same across all precatalysts at the higher temperature? | medium | T2 [paper-grounded inference]

V1-Q10 | P7:L42-50* | [REDACTED: substantial verbatim quotation; see Tier 9] | The paper states K₁ "cannot be determined uniquely" from kinetic data alone, yet proceeds to derive ΔH‡_app and ΔS‡_app as composite quantities containing K₁-dependent terms. What additional experiment (e.g., stoichiometric oxidative addition, NMR trapping) would allow K₁ to be independently measured? | high | T1

V1-Q11 | P8:L28-35* | [REDACTED: substantial verbatim quotation; see Tier 9] | Replacement with K₂CO₃ or Cs₂CO₃ is qualitatively reported as causing "substantial drop," but no quantitative conversions, yields, or kinetic data are given. What are the quantitative conversion/yield data for the inorganic base experiments? | high | T1

V1-Q12 | P8:L14-20* | [REDACTED: substantial verbatim quotation; see Tier 9] | The computational study considers only the neutral pathway with triethylamine as ligand; the cationic pathway is acknowledged but not modeled. Was the cationic pathway computationally evaluated? | high | T1

V1-Q13 | P9:L8-14* | [REDACTED: substantial verbatim quotation; see Tier 9] | The pathway to 1,1-diphenylethylene (4a) is not modeled computationally despite being a consistently formed product. Why was the DFT pathway leading to 4a excluded? | medium | T2 [paper-grounded inference]

V1-Q14 | P3:L18-22* | [REDACTED: substantial verbatim quotation; see Tier 9] | The concentration ranges cover less than a factor of 3 for each reactant. Is the simplified kinetic model valid beyond these narrow ranges at preparative-scale conditions used in Figures 2–4? | medium | T2 [paper-grounded inference]
```

---

## Turn 2 — Agent V2

```
[Turn 2: Agent V2]
field: Computational chemistry / DFT methodology [preempts_turn3_default: yes]
field_rationale: V1 covered kinetics, mechanistic scope, and experimental data quality. The paper also reports a substantial DFT/M06/def2-TZVP computational section (Scheme 5, Figure 11) that requires evaluation for computational methodology quality — particularly energy type, basis-set choice, temperature corrections, solvation model, and conformational sampling.

--- New questions ---
V2-Q1 | P9:L1-5* | [REDACTED: substantial verbatim quotation; see Tier 9] | Are the energies in Figure 11 / Scheme 5 ΔG at 363 K (from thermochemical corrections) or ΔE_electronic? The caption says "free energies" but the computational details state frequencies at 363.15 K — is the full ΔG(363 K) plotted? | high | T1

V2-Q2 | P9:L8-12* | [REDACTED: substantial verbatim quotation; see Tier 9] | IRC confirmation is stated but not quantified. Were bidirectional IRCs computed for all five transition states (10TS, 11TS, 15TS, 17TS, 21TS)? | medium | T2 [paper-grounded inference]

V2-Q3 | P8:L42-46* | [REDACTED: substantial verbatim quotation; see Tier 9] | A single basis set is used without convergence test. Were barrier heights for 15TS (107.8 kJ/mol) and 11TS (55.6 kJ/mol) tested against a larger basis? | medium | T3 [external inference]

V2-Q4 | P8:L44-46* | "D3 empirical dispersion correction with Becke and Johnson damping" | Conformational sampling of Et₃N coordination geometries in triethylamine-ligated intermediates (complex 7, 11TS) is not described. How were the lowest-energy conformers identified? | high | T2 [paper-grounded inference]

V2-Q5 | P9:L32-38* | [REDACTED: substantial verbatim quotation; see Tier 9] | Only 2 of 7 experimental Hammett substituents are evaluated computationally. Is the two-point validation sufficient to claim computational confirmation of the Hammett trend? | high | T2 [paper-grounded inference]

V2-Q6 | P9:L14-22* | [REDACTED: substantial verbatim quotation; see Tier 9] | The agreement between DFT and kinetic data is qualitative only. What quantitative metric was used to conclude agreement — was the computed ΔG‡ compared against the experimental ΔG‡_app? | high | T2 [paper-grounded inference]

V2-Q7 | P8:L44-46* | [REDACTED: substantial verbatim quotation; see Tier 9] | Was any transition state found to have unexpected additional imaginary frequencies, and how were such cases handled? | medium | T1

V2-Q8 | P9:L5-8* | [REDACTED: substantial verbatim quotation; see Tier 9] | GVL's SMD parameters are approximated from generic ester values. Was sensitivity of the energy profile to GVL-specific SMD parameters tested? | high | T2 [paper-grounded inference]

--- Overlaps with V1 ---
V2-OV1 | overlaps_with: V1-Q12 | severity_V2: high | note: Under phosphine-free conditions, the cationic Heck pathway (halide dissociation facilitated by amines) is documented in the computational literature and may be energetically competitive with the neutral pathway.

V2-OV2 | overlaps_with: V1-Q13 | severity_V2: high | note: The 4a (1,1-diphenylethylene) minor product pathway requires 1,1-insertion; its omission means the DFT model cannot rationalize the k₃/k₄ selectivity ratio which is a key experimental output of the kinetic study.

V2-OV3 | overlaps_with: V1-Q4 | severity_V2: medium | note: The 3a:4a ratio should be predictable from relative DFT barriers for anti-Markovnikov vs. Markovnikov β-hydride elimination; its absence is a gap in the mechanistic model.
```

---

## Turn 3 — Agent V3

```
[Turn 3: Agent V3]
field: Chemical kinetics / physical chemistry — kinetic model validation and error analysis
field_rationale: V2 declared [preempts_turn3_default: yes] (computational chemistry). V1 addressed general experimental gaps, V2 DFT methodology. S0-2 and S0-4 identify kinetic data (Eyring analysis, Chemmech fitting, K₁k₂ at 5 temperatures) as the primary experimental evidence, requiring a dedicated chemical kinetics / physical chemistry perspective.

--- New questions ---
V3-Q1 | P7:L12-18* | [REDACTED: substantial verbatim quotation; see Tier 9] | The relative sum-of-squares minimization is reported without the parameter covariance matrix or confidence intervals. Are the ± values in Tables 1 and 2 standard deviations from the fit covariance matrix, propagated uncertainties from replicate experiments, or neither? | critical | T1

V3-Q2 | P7:L20-26* | [REDACTED: substantial verbatim quotation; see Tier 9] | The 5% average deviation is an aggregate criterion applied to all curves simultaneously. Were the residuals randomly distributed (white noise), or is there systematic structure that would indicate model misspecification? | high | T1

V3-Q3 | P7:L28-34* | [REDACTED: substantial verbatim quotation; see Tier 9] | The design varies one concentration at a time (OVAT). Was any cross-term experiment performed to test interaction effects and verify parameter orthogonality? | high | T2 [paper-grounded inference]

V3-Q4 | P7:L34-38* | [REDACTED: substantial verbatim quotation; see Tier 9] | The number of replicate kinetic curves at each temperature is not stated. How many independent replicate runs were performed at each of the five temperatures, and were the K₁k₂ values in Table 2 obtained from single runs or averaged from replicates? | critical | T1

V3-Q5 | P8:L55-60* | [REDACTED: substantial verbatim quotation; see Tier 9] | The aggregate average deviation masks possible systematic variation with temperature or concentration. Are residuals uniform across the full temperature range (363–393 K)? | medium | T2 [paper-grounded inference]

V3-Q6 | P7:L8-12* | [REDACTED: substantial verbatim quotation; see Tier 9] | Sub-unity orders may indicate model misspecification. Were alternative kinetic models (inhibitor term, catalyst deactivation, Pd aggregation) tested and excluded, or was the simplified 4-step model accepted without model discrimination? | high | T2 [paper-grounded inference]

V3-Q7 | P8:L1-4* | [REDACTED: substantial verbatim quotation; see Tier 9] | Whether GVL and DMF fits share any parameter constraints or are entirely independent optimizations is not stated. Are GVL and DMF fit with completely independent parameter sets? | medium | T1

--- Overlaps with V1/V2 ---
V3-OV1 | overlaps_with: V1-Q1 | severity_V3: critical | note: From a kinetics perspective, the absence of propagated uncertainties on ΔH‡_app and ΔS‡_app from the composite K₁k₂ quantities is fundamental — the Eyring analysis entangles K₁ and k₂ contributions so the true uncertainty is larger than the uncertainty on K₁k₂ alone.

V3-OV2 | overlaps_with: V1-Q2 | severity_V3: critical | note: Standard kinetic parameter estimation requires confidence intervals on Eyring parameters; their absence means the stated conclusion "no medium effect on mechanism" cannot be statistically evaluated.

V3-OV3 | overlaps_with: V1-Q8 | severity_V3: high | note: In kinetic modeling, base concentration is typically treated as a parameter; its omission from the model means the fitted K₁k₂ values absorb any implicit [base] dependence and may not be reproducible at different base loadings.
```

---

## Turn 4 — Synthesis (ARM A Output)

```
prompt_version: stage1-v184-20260502
model_info: claude-sonnet-4-6

target_title:   Homogeneous Pd-Catalyzed Heck Coupling in γ-Valerolactone as a Green Reaction Medium: A Catalytic, Kinetic, and Computational Study
target_authors: Dániel Fodor, Tamás Kégl, József M. Tukacs, Attila K. Horváth, László T. Mika
target_start:   page 1: [REDACTED: paper boundary quote; see Tier 9]
target_end:     end of document

[Agent fields]
V1: Physical organic chemistry / homogeneous catalysis — specialist in kinetic analysis and mechanism of Pd-catalyzed Heck coupling
V2: Computational chemistry / DFT methodology — specialist in transition-state calculations and energy surface analysis
V3: Chemical kinetics / physical chemistry — specialist in kinetic model validation, parameter estimation, and statistical reliability

[A]
A-1 | P7:L42-50* | [REDACTED: substantial verbatim quotation; see Tier 9] | deferred | n/a | T1 | linked_to: B-3, U-3 | V1=high (1/3)

A-2 | P9:L14-22* | [REDACTED: substantial verbatim quotation; see Tier 9] | deferred | n/a | T1 | linked_to: B-5 | V1=high, V2=high; convergence=2/3, temperature_gap=none

[B]
B-1 | P7:L18-22* | [REDACTED: substantial verbatim quotation; see Tier 9] | reporting_omission | Quantitative statement of derived thermodynamic parameters. | note: No uncertainty (± value) is reported for ΔH‡_app or ΔS‡_app in either solvent; standard practice in Eyring analysis requires uncertainty reporting. Flag: metric incompleteness. | V1=critical, V3=critical; convergence=2/3, temperature_gap=none

B-2 | P8:L28-35* | [REDACTED: substantial verbatim quotation; see Tier 9] | reporting_omission | Qualitative mechanistic inference from inorganic base substitution experiment. | note: No quantitative conversion/yield data for K₂CO₃ or Cs₂CO₃ experiments are provided; "substantial drop" is not quantified. Flag: metric incompleteness. | V1=high (1/3)

B-3 | P7:L34-38* | [REDACTED: substantial verbatim quotation; see Tier 9] | reporting_omission | Disclosure of kinetic order results via SI reference. | note: Numerical values of kinetic orders in IB and styrene deferred to SI without main-text quantification; physical significance of deviation from unity not addressed. | V1=medium (1/3)

B-4 | P9:L32-38* | [REDACTED: substantial verbatim quotation; see Tier 9] | methodological_limitation | Computational validation of Hammett substituent effects. | note: Only 2 of 7 experimental Hammett substituents computed; two-point linear validation insufficient when 7-point experimental correlation exists. | V2=high (1/3)

B-5 | P9:L8-14* | [REDACTED: substantial verbatim quotation; see Tier 9] | intentional_narrowing | Scope-limiting statement for the computational model. | note: Minor product pathway (1,1-diphenylethylene, 4a) computationally excluded without quantitative justification; cationic pathway acknowledged but not modeled. | V1=medium, V2=high; convergence=2/3, temperature_gap=low

B-6 | P7:L20-26* | [REDACTED: substantial verbatim quotation; see Tier 9] | reporting_omission | Goodness-of-fit criterion statement. | note: No residual plots, individual curve fit quality, or covariance matrix reported; 5% average is an aggregate criterion masking possible systematic deviations at specific temperatures or concentrations. Flag: metric incompleteness. | V3=high (1/3)

B-7 | P4:L38-48* | [REDACTED: substantial verbatim quotation; see Tier 9] | reporting_omission | Presentation of Hammett linear free energy correlations. | note: TOF at 30 min used rather than initial rates; no verification that 30-min TOF is a valid initial-rate proxy for all substituents given variable conversions. Flag: metric incompleteness. | V1=high (1/3)

[C]
C-1 | P2:L22-28* | Dupont (ref 27): [REDACTED: substantial verbatim quotation; see Tier 9] | Introduction — cited with specific numerical ΔH‡/ΔS‡ values as prior kinetic benchmark | Dropped Quantitative Benchmark — numerical comparison introduced but not completed; paper reports own ΔH‡_app and ΔS‡_app but never directly compares against Dupont's values. | yes/medium — different catalyst (PPh₃-ligated), but comparison is absent despite the striking difference in ΔS‡ sign. | partial

C-2 | P2:L28-32* | Jagtap (ref 28): "[REDACTED: verbatim source text; see the source paper via its DOI]" | Introduction — cited with specific numerical ΔH‡ | Dropped Quantitative Benchmark — similar ΔH‡ to present work (103.0 kJ/mol) cited without direct numerical comparison in Discussion. | yes | yes

C-3 | P2:L32-36* | Amatore (ref 29): [REDACTED: substantial verbatim quotation; see Tier 9] | Introduction — cited with specific numerical ΔH‡/ΔS‡ | Dropped Quantitative Benchmark — the remarkable ΔS‡ sign difference (+139 vs +7 J·mol⁻¹·K⁻¹) is never discussed in the Results/Discussion. | yes | yes

C-4 | P8:L13-18* | refs 74–76 (Balcells, Kozuch, Bäcktorp — DFT phosphine-ligated Heck studies) | Background framing of prior DFT work | Cited as a group without comparison of present DFT barriers against any individual reference's specific findings. | medium — prior DFT studies provide benchmarks for Pd-Heck barriers. | yes (grouped cite-and-drop)

C-5 | P5:L1-5* | Vaccaro (ref 56) — heterogeneous GVL-Heck study | Background — GVL Heck precedent | Cited to establish GVL precedent without comparing yields/selectivities against present homogeneous system. | medium | no

[U]
U-1 | P7:L18-28* | [REDACTED: substantial verbatim quotation; see Tier 9] | Does the numerical similarity of ΔS‡_app(GVL) and ΔS‡_app(DMF) constitute statistical evidence for no medium effect, given that no uncertainties are reported on either value? | V1/V3 | critical | note: self-contradictory absence — the paper's proposed mechanistic conclusion (no medium effect) requires that the GVL–DMF difference in ΔS‡_app fall within combined uncertainty; no uncertainty is reported; the paper's own analytical framework (eq 5) makes the uncertainty computable but it is not computed.

U-2 | P8:L28-35* | [REDACTED: substantial verbatim quotation; see Tier 9] | Can the drop in conversion with K₂CO₃/Cs₂CO₃ be attributed specifically to loss of NEt₃ ligand function vs. loss of Brønsted base function, and does this experiment test the dual role assigned to Et₃N in Scheme 4? | V1 | high | note: self-contradictory absence — the paper's proposed mechanism (Scheme 4) assigns Et₃N both ligand and base roles; the inorganic base experiment is designed only to probe Brønsted base function and cannot distinguish these two roles; the mechanistic interpretation of the "substantial drop" remains ambiguous relative to the paper's own mechanistic model.

U-3 | P7:L42-50* | [REDACTED: substantial verbatim quotation; see Tier 9] | Can the composite ΔH‡_app and ΔS‡_app be compared to the DFT barrier at 15TS without knowing the enthalpic and entropic contribution from K₁? | V1 | high | note: prerequisite-absence — the paper acknowledges ΔH‡_app = ΔH‡ + ΔH⊖ + ΔH₁⊖ (eq 4); the K₁ contribution (ΔH⊖) is neither measured nor estimated from DFT; the apparent agreement between experimental ΔH‡_app = 103 kJ/mol and computed 15TS barrier = 107.8 kJ/mol is therefore unverifiable without knowing the K₁ enthalpic contribution.

[META]
  linked_items: [A-1 ↔ B-3 ↔ U-3; A-2 ↔ B-5; B-1 ↔ U-1; B-2 ↔ U-2; C-1 ↔ C-2 ↔ C-3]
  same_root_groups:
    SRG-1: {B-1, U-1, V3-Q1, V3-Q2} — same root: uncertainty/statistical validation of kinetic parameters and derived thermodynamic quantities entirely absent from main text
    SRG-2: {B-5, A-2, V1-Q13, V2-OV2} — same root: computational pathway restricted to neutral/major-product channel; minor product pathway (4a) and cationic pathway absent
    SRG-3: {C-1, C-2, C-3} — same root: three prior kinetic benchmarks with numerical ΔH‡/ΔS‡ values cited in introduction but never compared against paper's results in Discussion
    SRG-4: {A-1, U-3} — same root: K₁ unresolvable from kinetic data, making composite activation parameters undeconvolutable and DFT–kinetic comparison unverifiable
    SRG-5: {B-2, U-2} — same root: NEt₃ dual role (ligand vs. base) unresolved by the inorganic base control experiment
  symmetric_citations: C-1/C-2/C-3 (three kinetic benchmark papers cited in introduction with specific numerical ΔH‡/ΔS‡ values, none compared numerically in Results/Discussion)
  unreported_data: kinetic orders in IB and styrene (SI only); individual curve residuals; ΔH‡_app and ΔS‡_app uncertainties; quantitative inorganic base conversion data; conformational sampling details for Et₃N-Pd intermediates; number of replicate kinetic runs per temperature
  series_signal: no

[TEMPERATURE_SUMMARY]
  high_convergence_high_gap: []
  high_convergence_low_gap: [B-1 (V1=critical, V3=critical, convergence=2/3, gap=none), A-2 (V1=high, V2=high, convergence=2/3, gap=none), B-5 (V1=medium, V2=high, convergence=2/3, gap=low), V1-Q8/V3-OV3 merged at B-2 level (V1=high, V3=high, convergence=2/3, gap=none)]
  low_convergence_high_gap: [U-1 (V1+V3=critical via SRG-1, but formally 2/3 convergence), V3-Q1 (critical, 1/3), V3-Q4 (critical, 1/3)]

[GAP]
GAP-1 | type 1 | high | Dupont (ref 27): retrieve for ΔH‡/ΔS‡ numerical comparison with GVL results; the opposite sign of ΔS‡ between PPh₃-ligated and phosphine-free systems is not discussed | Dupont et al., Pd/PPh₃ kinetic study (implied ref 27) | T1 | pending
GAP-2 | type 1 | high | Jagtap (ref 28): retrieve for direct ΔH‡ comparison; ΔH‡ = 98.7 kJ/mol similar to GVL value but comparison absent from Discussion | Jagtap, S. V.; Deshpande, R. M., Kinet. Catal. 2013 (implied) | T1 | pending
GAP-3 | type 3 | medium | Independent measurement of K₁ (stoichiometric oxidative addition or NMR titration) to deconvolute ΔH‡_app into elementary-step contributions | new experiment; not present in paper | T3 [external inference] | pending

inference_time_sec: not available — inject externally
```

---

## ARM A — Item Count Summary

| Category | Count |
|---|---|
| A (Deferred) | 2 |
| B (Traces of Rejection) | 7 |
| C (Uncontinued Citations) | 5 |
| U (Unclassified) | 3 |
| **TOTAL** | **17** |

## ARM A — Marker Check

| Marker | Present? | Evidence items |
|---|---|---|
| M1 (propagated/error uncertainty NOT reported for kinetic parameters K₁k₂, ΔH‡/ΔS‡) | **yes** | B-1 (reporting_omission, critical convergence 2/3), U-1 (self-contradictory absence, critical), V1-Q1, V1-Q2 |
| M2 (catalyst resting-state ambiguity / Figure 11 interpretation gap) | **yes** | A-1 (K₁ unresolvable), U-3 (prerequisite-absence: K₁ contribution to ΔH‡_app unquantified; DFT reference state complex 7 vs kinetic resting state) |
| M3 (NEt₃ / base concentration as uncontrolled kinetic variable) | **yes** | V1-Q8, B-2 (quantitative data absent for inorganic base experiment), U-2 (dual-role ambiguity), V3-OV3 |

---

> **Tier 8 redaction notice**: This file is a redacted copy of the corresponding Tier 3 / Tier 9 output. Verbatim source-paper quotations have been replaced by `[REDACTED: see source paper §<loc>; full text retained in Tier 9 reviewer-only deposit]` markers, preserving location references and our own analytical content. Bibliographic fields (title, authors, journal, year, DOI), analytical labels (`evidence_chain:` with B-/U-/A-/C- internal IDs), short technical terms, and our own analytical text are not redacted. The redaction was applied by `scripts/redact_for_tier8.py` and, for this version, by `scripts/build_paperA_R1_public.py` with `scripts/redact_source_ngram_runs.py` (scripts of the project repository; they are not deposited).
