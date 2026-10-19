---
generated: 2026-06-01
prompt_experiment: relaxedcap_20260601 (turns 1+2+3, no turn4)
paper: scr1 — Heck coupling in GVL (Fodor et al., ACS Sus. Chem. Eng. 2020)
stage0_source: scr1_v184_sonnet_s0_capexp_20260601.md
model: claude-sonnet-4-6
note: Generation-ordered extraction with online root tracking. No Turn 4 synthesis. Items appear in V1→V2→V3 generation order.
---

# scr1 Stage 1 — Generation-Ordered Root Curve

## Root legend (assigned online in generation order)

| Root ID | Core absence / methodological gap |
|---------|-----------------------------------|
| R1  | GC-only product quantification — no isolated yields anywhere |
| R2  | No quantitative comparison between new and prior ΔH‡/ΔS‡ literature values |
| R3  | Temperature inconsistency between experimental sub-studies (catalyst screen at 403 K vs scope/kinetics at 363–393 K) |
| R4  | Scope limited to aryl iodides — no aryl bromides or chlorides tested |
| R5  | No Pd-free blank / control experiment |
| R6  | Water tolerance claim not supported by statistical test |
| R7  | K₁k₂ non-separability — individual K₁ and k₂ inaccessible from data |
| R8  | 4a (1,1-diphenylethylene) formation pathway absent from both computation and mechanistic analysis; 3a/4a selectivity mechanistically unresolved |
| R9  | No quantitative comparison between computed DFT barrier and experimental ΔH‡_app |
| R10 | GVL stability/degradation under reaction conditions (base, Pd, heat) not tested |
| R11 | Single-timepoint (30-min) measurements used as rate proxies without validation (covers: Hammett TOF at 30 min; solvent comparison at single timepoint) |
| R12 | Et₃N vs inorganic base replacement — no quantitative conversion/yield data reported |
| R13 | k₃/k₄ equated to [3a]/[4a] product ratio without independent verification |
| R14 | Geometry optimization in gas phase; SMD solvation only as single-point correction |
| R15 | Conformational sampling of TS structures not described |
| R16 | Basis set convergence not assessed (only def2-TZVP, no QZVP/CBS) |
| R17 | Cationic pathway excluded from DFT study without justification |
| R18 | Reference state for energy profile (complex 7) not established as experimental resting state |
| R19 | DFT functional (M06) not benchmarked for this Pd organometallic system |
| R20 | RDS assignment without independent experimental evidence (KIE, crossover, intermediate trapping) |
| R21 | IRC confirmation not specified per-TS |
| R22 | Base-assisted HI elimination pathway not computed despite experimental evidence of base necessity |
| R23 | Eyring analysis statistical rigor — no Eyring plot shown, no propagated uncertainties on ΔH‡_app/ΔS‡_app, heteroscedastic error bars not addressed |
| R24 | No alternative kinetic model discrimination (only one model tested) |
| R25 | Kinetic orders "slightly lower than unity" — numerical values deferred to SI only |
| R26 | "No medium effect" conclusion drawn from composite (apparent) parameters that conflate intrinsic and preequilibrium contributions |
| R27 | Kinetic fit quality assessed by average deviation only — no residual plots or chi-squared |
| R28 | Parameter identifiability of simultaneous multi-curve fit not assessed |
| R29 | No replicate kinetic runs — reported uncertainties reflect fitting error only |
| R30 | Temperature measurement/control precision not reported (critical given narrow 30 K Eyring span) |

---

## Generation-ordered item table

| idx | agent | severity | root_id | new_root | short_desc |
|-----|-------|----------|---------|----------|------------|
| 1   | V1    | high     | R1      | yes      | GC-only yields; no isolated product reported |
| 2   | V1    | high     | R2      | yes      | Prior ΔH‡/ΔS‡ values cited but never numerically compared |
| 3   | V1    | medium   | R3      | yes      | Catalyst screen at 403 K vs scope/kinetics at 378 K |
| 4   | V1    | medium   | R4      | yes      | Only aryl iodides tested; no bromides/chlorides |
| 5   | V1    | low      | R5      | yes      | No Pd-free blank reaction reported |
| 6   | V1    | medium   | R6      | yes      | Water tolerance: no statistical test on flat trend |
| 7   | V1    | medium   | R7      | yes      | K₁k₂ non-separable; no experiment to resolve individually |
| 8   | V1    | medium   | R8      | yes      | No computed or experimental pathway to minor product 4a |
| 9   | V1    | high     | R9      | yes      | No numerical DFT barrier vs experimental ΔH‡_app comparison |
| 10  | V1    | medium   | R10     | yes      | GVL degradation under reaction conditions untested |
| 11  | V1    | medium   | R11     | yes      | Hammett TOF at 30 min not validated as initial-rate proxy |
| 12  | V1    | medium   | R12     | yes      | NEt₃ vs K₂CO₃/Cs₂CO₃: substantial drop, no numbers given |
| 13  | V1    | medium   | R11     | no       | Solvent comparison at single 30-min timepoint only |
| 14  | V1    | medium   | R13     | yes      | k₃/k₄ ≈ [3a]/[4a]: no independent product ratio verification |
| 15  | V2    | high     | R14     | yes      | Gas-phase geometry + single-point SMD for ionic intermediates |
| 16  | V2    | high     | R15     | yes      | Conformational sampling of TS structures unstated |
| 17  | V2    | medium   | R16     | yes      | Basis set convergence not assessed (def2-TZVP only) |
| 18  | V2    | high     | R17     | yes      | Cationic Heck pathway not computed despite acknowledged possibility |
| 19  | V2    | high     | R18     | yes      | Complex 7 as energy reference not established as resting state |
| 20  | V2    | medium   | R19     | yes      | M06 functional not benchmarked for Pd organometallics |
| 21  | V2    | high     | R20     | yes      | RDS (C–C coupling) assigned without KIE or crossover evidence |
| 22  | V2    | low      | R21     | yes      | IRC confirmation not stated per individual transition state |
| 23  | V2    | medium   | R8      | no       | 3a vs 4a selectivity: kinetic vs thermodynamic control unaddressed |
| 24  | V2    | medium   | R22     | yes      | Base role in HI elimination omitted from computation |
| 25  | V3    | high     | R23     | yes      | Eyring plot absent; linearity of fit not verifiable |
| 26  | V3    | critical | R23     | no       | ΔH‡_app and ΔS‡_app reported without propagated uncertainties |
| 27  | V3    | high     | R24     | yes      | No alternative kinetic models tested for discrimination |
| 28  | V3    | medium   | R25     | yes      | Kinetic orders numerical values absent from main text |
| 29  | V3    | high     | R23     | no       | Eyring fit uses heteroscedastic data; weighting not described |
| 30  | V3    | high     | R26     | yes      | "No medium effect" conclusion from composite apparent parameters |
| 31  | V3    | medium   | R27     | yes      | Fit quality: average deviation only, no residuals or chi-squared |
| 32  | V3    | high     | R28     | yes      | Parameter identifiability of simultaneous fit not assessed |
| 33  | V3    | medium   | R29     | yes      | No replicate kinetic runs; uncertainties = fitting error only |
| 34  | V3    | medium   | R30     | yes      | Temperature control precision unreported (narrow 30 K Eyring span) |

---

## Summary

TOTAL_ITEMS=34  TOTAL_DISTINCT_ROOTS=30

NEW_ROOT_AT_INDEX: 1,2,3,4,5,6,7,8,9,10,11,12,14,15,16,17,18,19,20,21,22,24,25,27,28,30,31,32,33,34

HIGH_OR_CRITICAL_AT_INDEX: 1,2,9,15,16,18,19,21,25,26,27,29,30,32

---

## Root-saturation curve (cumulative distinct roots by index)

| idx | cum_new_roots |
|-----|---------------|
| 1   | 1  |
| 2   | 2  |
| 3   | 3  |
| 4   | 4  |
| 5   | 5  |
| 6   | 6  |
| 7   | 7  |
| 8   | 8  |
| 9   | 9  |
| 10  | 10 |
| 11  | 11 |
| 12  | 12 |
| 13  | 12 (R11 reuse) |
| 14  | 13 |
| 15  | 14 |
| 16  | 15 |
| 17  | 16 |
| 18  | 17 |
| 19  | 18 |
| 20  | 19 |
| 21  | 20 |
| 22  | 21 |
| 23  | 21 (R8 reuse) |
| 24  | 22 |
| 25  | 23 |
| 26  | 23 (R23 reuse) |
| 27  | 24 |
| 28  | 25 |
| 29  | 25 (R23 reuse) |
| 30  | 26 |
| 31  | 27 |
| 32  | 28 |
| 33  | 29 |
| 34  | 30 |

**Saturation observation:** V1 (idx 1–14) opened 13 new roots. V2 (idx 15–24) opened 9 new roots (1 reuse at idx 23). V3 (idx 25–34) opened 8 new roots (2 reuses at idx 26 and 29). The new-root rate did not saturate across the three agents — V3 continued to surface new roots at nearly the same rate as V2. High/critical-severity items appeared throughout all three agents, including at idx 26 (critical, V3-Q2) and idx 30 (high, V3-Q6), confirming that high-severity absences were not concentrated early.

---

## Full item detail (for downstream Stage 2 use)

### V1 items

**V1-Q1 (idx 1)**
loc: P3 (p9928), right col, General Procedure
quote: [REDACTED: see `loc:` above; full text in Tier 9]
question: All conversion and yield figures throughout the paper report GC-FID values. No isolated yield is reported for any substrate. Are GC-conversion values representative of isolated synthetic yields, and does the selectivity reflect the purified product distribution?
severity: high | inference_tier: T1 | root: R1

**V1-Q2 (idx 2)**
loc: P2 (p9927), left col, para 3
quote: [REDACTED: see `loc:` above; full text in Tier 9]
question: Three prior studies are cited with specific numerical ΔH‡/ΔS‡ values (Dupont: 69±3 / −43±8; Jagtap: 98.7; Amatore: 75±5 / 7±8), yet the paper never makes a quantitative comparison on these axes against its own results (103.0 kJ·mol⁻¹ / +139.7 J·mol⁻¹·K⁻¹). What explains the sign reversal in ΔS‡ and the large magnitude difference from phosphine-ligated systems?
severity: high | inference_tier: T1 | root: R2

**V1-Q3 (idx 3)**
loc: P4 (p9929), Figure 4 caption
quote: [REDACTED: see `loc:` above; full text in Tier 9]
question: The catalyst precursor screening (Figure 4) was conducted at 403 K, while the substrate scope and all kinetic studies use 363–393 K (with comparative experiments at 378 K). No justification is given for the temperature change. How does this affect comparability of precursor efficiencies?
severity: medium | inference_tier: T1 | root: R3

**V1-Q4 (idx 4)**
loc: P3 (p9928), Results opening / Scheme 2
quote: [REDACTED: see `loc:` above; full text in Tier 9]
question: The substrate scope is restricted exclusively to aryl iodides. No aryl bromides or chlorides are tested. The paper claims "excellent functional group tolerance" but does not address tolerance to the halide leaving group, which governs practical applicability of GVL as a Heck solvent for cheaper substrates.
severity: medium | inference_tier: T1 | root: R4

**V1-Q5 (idx 5)**
loc: P3 (p9928), General Procedure
quote: [REDACTED: see `loc:` above; full text in Tier 9]
question: No control experiment without Pd catalyst is described. Is there any background thermal or base-mediated coupling of iodobenzene and styrene in GVL at 363–393 K under the reaction conditions?
severity: low | inference_tier: T2 | root: R5

**V1-Q6 (idx 6)**
loc: P4–5 (p9929–9930), Figure 3 caption and text
quote: [REDACTED: see `loc:` above; full text in Tier 9]
question: Figure 3 shows conversion values varying between ~45% and ~52% across six water levels. No statistical test is applied to this trend. Given the visible scatter, is the "no decrease" conclusion statistically justified, and could the trend conceal a significant but small effect?
severity: medium | inference_tier: T2 | root: R6

**V1-Q7 (idx 7)**
loc: P6 (p9931), right col
quote: [REDACTED: see `loc:` above; full text in Tier 9]
question: The kinetic model yields only the product K₁k₂ and the ratio k₃/k₄. No experiment is proposed (e.g., pre-formed IBC complex, stoichiometric step validation, NMR equilibrium measurement) to separate K₁ from k₂. What additional experiment could resolve the individual contributions, and how would this change the interpretation of ΔH‡_app?
severity: medium | inference_tier: T2 | root: R7

**V1-Q8 (idx 8)**
loc: P8 (p9933), left col
quote: [REDACTED: see `loc:` above; full text in Tier 9]
question: The kinetic model explicitly determines k₃/k₄ = 9.80±0.47 (GVL), yet no computational pathway leading to 1,1-diphenylethylene (4a) is shown. Without a computed TS for 4a formation, the mechanistic basis for the k₃/k₄ ratio cannot be assessed computationally.
severity: medium | inference_tier: T1 | root: R8

**V1-Q9 (idx 9)**
loc: P8 (p9933), left col, Computational Studies
quote: [REDACTED: see `loc:` above; full text in Tier 9]
question: The highest computed free energy barrier is 15TS at 107.8 kJ·mol⁻¹ (relative to complex 7). The experimental ΔH‡_app = 103.0 kJ·mol⁻¹. No quantitative comparison between these values is made. Is the "agreement with kinetic measurements" claimed in the text based on a numerical comparison, and if so, where is it shown?
severity: high | inference_tier: T2 | root: R9

**V1-Q10 (idx 10)**
loc: P2 (p9927), right col
quote: [REDACTED: see `loc:` above; full text in Tier 9]
question: GVL is acknowledged to react with amines. No experiment tests whether GVL degrades under reaction conditions (90–120 °C, Et₃N base, Pd catalyst) over the reaction timescale, and whether degradation products affect catalysis or the kinetic model.
severity: medium | inference_tier: T2 | root: R10

**V1-Q11 (idx 11)**
loc: P4 (p9929), Figure 5 caption
quote: [REDACTED: see `loc:` above; full text in Tier 9]
question: The Hammett correlation uses TOF at 30 min as the kinetic parameter. For reactions with catalyst induction periods and time-varying concentrations, the 30-min TOF may not reflect intrinsic rate constants. No justification is given for using 30-min TOF as a linear free energy proxy, nor is a comparison to initial-rate TOF provided.
severity: medium | inference_tier: T2 | root: R11

**V1-Q12 (idx 12)**
loc: P8 (p9933), left col
quote: [REDACTED: see `loc:` above; full text in Tier 9]
question: The replacement of Et₃N by K₂CO₃ and Cs₂CO₃ "substantially" drops conversion, but no numerical data (conversion %, yield, TOF) is reported for these experiments. Without quantitative data, the conclusion that NEt₃ plays a catalytic (ligand) role — rather than acting solely as a superior Brønsted base — cannot be evaluated.
severity: medium | inference_tier: T1 | root: R12

**V1-Q13 (idx 13)**
loc: P4 (p9929), Figure 2 caption
quote: [REDACTED: see `loc:` above; full text in Tier 9]
question: The solvent comparison (DMF, Tol, 1,4-DO, NMP, DMSO, GVL) uses a single 30-min timepoint. Differences in conversion may reflect differences in initial rate, length of induction period, or final equilibrium conversion — these cannot be distinguished from a single measurement. Is GVL genuinely faster, or does it have a shorter induction period?
severity: medium | inference_tier: T2 | root: R11 (reuse)

**V1-Q14 (idx 14)**
loc: P6–7 (p9931–9932), Table 1
quote: [REDACTED: see `loc:` above; full text in Tier 9]
question: The kinetic model equates k₃/k₄ to the [3a]/[4a] product concentration ratio. This assumes both products form irreversibly and have equal GC-FID response factors. No independent measurement of the [3a]/[4a] ratio (NMR, isolated product analysis) is provided to verify this equivalence.
severity: medium | inference_tier: T2 | root: R13

---

### V2 items

**V2-Q1 (idx 15)**
loc: P3 (p9928), right col, Computational Details
quote: [REDACTED: see `loc:` above; full text in Tier 9]
question: Geometry optimizations are performed without explicit mention of solvation (SMD applied only for single-point energies). For polar intermediates in GVL (ε = 30.1), gas-phase structures may differ significantly from solution geometries. Were any geometries re-optimized with SMD to test the effect on barriers?
severity: high | inference_tier: T2 | root: R14

**V2-Q2 (idx 16)**
loc: P3 (p9928), right col
quote: [REDACTED: see `loc:` above; full text in Tier 9]
question: For TS structures involving flexible triethylamine, phenyl, and styrene groups, how were the lowest-energy conformers identified? No conformational search method (CREST, dihedral scan, etc.) is mentioned. A non-global-minimum TS would systematically overestimate the computed free energy barrier.
severity: high | inference_tier: T2 | root: R15

**V2-Q3 (idx 17)**
loc: P3 (p9928), right col
quote: [REDACTED: see `loc:` above; full text in Tier 9]
question: Only def2-TZVP is used for all calculations; no basis set convergence test (e.g., def2-QZVP single-point or CBS extrapolation) is reported. For Pd-containing transition states, 4d correlation effects can shift barriers by several kJ·mol⁻¹. Is the basis set adequacy established for the reported barriers?
severity: medium | inference_tier: T2 | root: R16

**V2-Q4 (idx 18)**
loc: P8 (p9933), left col
quote: [REDACTED: see `loc:` above; full text in Tier 9]
question: The computational study considers only the neutral pathway. The paper explicitly acknowledges that cationic pathways are possible under phosphine-free conditions. Given that Pd(OAc)₂ activation could generate ionic intermediates and that Et₃N can coordinate, what is the justification for restricting the DFT study to the neutral pathway only?
severity: high | inference_tier: T1 | root: R17

**V2-Q5 (idx 19)**
loc: Scheme 5 caption + Figure 11 caption
quote: [REDACTED: substantial verbatim quotation; see Tier 9] (both Scheme 5 and Figure 11)
question: All computed free energies are referenced to complex 7 (Pd(II)(Ph)(I)(NEt₃)), a post-oxidative-addition intermediate. The experimental kinetic model identifies IBC (the Pd–iodobenzene π-complex, formed via rapid K₁ equilibrium) as the key observable species. Is complex 7 the experimentally relevant resting state, and if not, does the energy reference undermine comparison with the experimental ΔG‡?
severity: high | inference_tier: T2 | root: R18

**V2-Q6 (idx 20)**
loc: P3 (p9928), right col
quote: [REDACTED: see `loc:` above; full text in Tier 9]
question: M06 is used for single-point energy corrections, applied to geometries optimized with a different (Grimme D3-GGA) functional. M06 was parameterized primarily for organic thermochemistry and shows known issues for organometallic systems. No validation against higher-level methods (e.g., DLPNO-CCSD(T)) or prior Pd-Heck DFT studies is provided.
severity: medium | inference_tier: T3 [external inference] | root: R19

**V2-Q7 (idx 21)**
loc: P8 (p9933), right col
quote: [REDACTED: see `loc:` above; full text in Tier 9]
question: The RDS assignment (C–C coupling via 15TS) is supported by computational barriers and the kinetic observation that k₂ is temperature-dependent (K₁k₂ measurable). However, no kinetic isotope effect, crossover experiment, or intermediate trapping provides independent experimental confirmation. Could β-hydride elimination or reductive elimination be kinetically competitive with C–C coupling under some conditions?
severity: high | inference_tier: T2 | root: R20

**V2-Q8 (idx 22)**
loc: P3 (p9928), right col
quote: [REDACTED: see `loc:` above; full text in Tier 9]
question: IRC confirmation is described globally for "the reaction pathways" but is not attributed to specific transition states. Of the five TS structures in Figure 11 (15TS, 17TS, 21TS, and those in Scheme 5: 10TS, 11TS), which were individually confirmed by IRC? A failed IRC for any TS would undermine the proposed pathway connectivity.
severity: low | inference_tier: T2 | root: R21

**V2-Q9 (idx 23)**
loc: P6 (p9931), right col / Table 1
quote: [REDACTED: see `loc:` above; full text in Tier 9]
question: The k₃/k₄ ≈ 9.8 ratio (GVL) reflects the preference for trans-stilbene over 1,1-diphenylethylene formation. Is this regioselectivity kinetically controlled (different TS energies for insertion into internal vs terminal vinyl C–H) or thermodynamically controlled? The computational study addresses only the pathway to 3a and provides no answer.
severity: medium | inference_tier: T2 | root: R8 (reuse)

**V2-Q10 (idx 24)**
loc: P8 (p9933), right col
quote: [REDACTED: see `loc:` above; full text in Tier 9]
question: The base (Et₃N) is confirmed experimentally as essential (replacement with K₂CO₃ "substantially" drops conversion) yet its role in the HI elimination step (the last step of the Heck cycle) is entirely excluded from the computed pathway. The assumption that base assistance lowers the barrier is stated without supporting computation or comparison to the uncatalyzed HI elimination barrier.
severity: medium | inference_tier: T1 | root: R22

---

### V3 items

**V3-Q1 (idx 25)**
loc: P7–8 (p9932), right col
quote: [REDACTED: see `loc:` above; full text in Tier 9]
question: The Eyring plot used to extract ΔH‡_app and ΔS‡_app from the K₁k₂ vs T data (Table 2) is not shown in the main text or listed in the SI figure inventory (SI figures cited: S1, S2, S3, S4). Without the Eyring plot, the linearity of ln(K₁k₂/T) vs 1/T cannot be assessed by the reader, and outliers or curvature would be invisible.
severity: high | inference_tier: T1 | root: R23

**V3-Q2 (idx 26)**
loc: P7–8 (p9932), right col
quote: [REDACTED: see `loc:` above; full text in Tier 9]
question: The paper reports ΔH‡_app and ΔS‡_app values without any uncertainty (e.g., ±? kJ·mol⁻¹). The parameters A and p in Table 1 carry uncertainties of ~10–13%. The uncertainties in ΔH‡_app and ΔS‡_app are never given. Is the near-identity of GVL and DMF values (103.0 vs 103.7 kJ·mol⁻¹) statistically distinguishable — or could the two values overlap within propagated error?
severity: critical | inference_tier: T1 | root: R23 (reuse)

**V3-Q3 (idx 27)**
loc: P6 (p9931), left col / Scheme 3
quote: [REDACTED: see `loc:` above; full text in Tier 9]
question: Only one kinetic model (rapid pre-equilibrium K₁ followed by bimolecular k₂) is fitted to the data. No alternative models (e.g., irreversible oxidative addition, or styrene binding first) are proposed and discriminated statistically. On what basis is Scheme 3 selected over mechanistically plausible alternatives with similar or fewer parameters?
severity: high | inference_tier: T2 | root: R24

**V3-Q4 (idx 28)**
loc: P6 (p9931), left col
quote: [REDACTED: see `loc:` above; full text in Tier 9]
question: The kinetic orders for iodobenzene, styrene, and catalyst are described only as "slightly lower than unity," with numerical values deferred to SI Figure S2. The exact values (e.g., 0.85, 0.92?) are relevant to whether the simplified bimolecular rate law of Scheme 3 adequately captures the system or whether a fractional-order mechanism is needed.
severity: medium | inference_tier: T1 | root: R25

**V3-Q5 (idx 29)**
loc: P6–7 (p9931–9932), Table 2 / Data Treatment
quote: [REDACTED: see `loc:` above; full text in Tier 9]
question: Table 2 shows K₁k₂ uncertainties that increase approximately 3-fold from 363 K to 393 K (GVL: ±0.64×10⁵ at 363 K vs ±0.85×10⁶ at 393 K). When these heteroscedastic K₁k₂ values are used to construct the Eyring plot, is the regression weighted by the reported uncertainties, or is an unweighted least-squares regression applied? Unweighted regression would give disproportionate influence to the noisiest high-temperature points and bias ΔH‡_app.
severity: high | inference_tier: T2 | root: R23 (reuse)

**V3-Q6 (idx 30)**
loc: P8–9 (p9933), left col
quote: [REDACTED: see `loc:` above; full text in Tier 9]
question: The "no medium effect on mechanism" conclusion rests on the similarity of ΔH‡_app and ΔS‡_app between GVL and DMF. However, both are apparent (composite) parameters: ΔH‡_app = ΔH‡ + ΔH⊖ + ΔH₁⊖ (eq 4). Two solvents could have identical apparent parameters with opposite-sign intrinsic components that cancel. Is the conclusion that "the medium does not play any crucial role" logically valid when based solely on composite parameters?
severity: high | inference_tier: T2 | root: R26

**V3-Q7 (idx 31)**
loc: P7 (p9932), right col
quote: [REDACTED: see `loc:` above; full text in Tier 9]
question: The fit quality criterion is "average deviation" (mean absolute relative deviation). No residual plots, chi-squared statistics, or run tests are provided. Could the 5.3% average deviation for DMF mask systematic early-time deviations (induction period) or late-time deviations (catalyst deactivation) that would indicate model inadequacy?
severity: medium | inference_tier: T2 | root: R27

**V3-Q8 (idx 32)**
loc: P3 (p9928), Data Treatment / P6 (p9931), Kinetic Studies
quote: [REDACTED: see `loc:` above; full text in Tier 9]
question: The simultaneous fit of multiple concentration–time curves (four species × multiple temperatures × multiple initial concentrations) to three parameters (A, p, k₃/k₄) may suffer from parameter correlation and non-unique solutions. No parameter correlation matrix, profile likelihood, or sensitivity analysis is presented to confirm that the reported A, p, and k₃/k₄ values correspond to a unique global minimum.
severity: high | inference_tier: T2 | root: R28

**V3-Q9 (idx 33)**
loc: P3 (p9928), Data Treatment
quote: [REDACTED: see `loc:` above; full text in Tier 9]
question: Figures 7–10 show kinetic curves at multiple initial concentrations and temperatures, but no replicate experiments (repeated runs at identical initial conditions) are described or shown. The uncertainties in K₁k₂ (Table 2) therefore reflect fitting residuals from the Chemmech program, not experimental reproducibility. What is the run-to-run reproducibility of these kinetic curves?
severity: medium | inference_tier: T2 | root: R29

**V3-Q10 (idx 34)**
loc: P3 (p9928), General Procedure
quote: [REDACTED: see `loc:` above; full text in Tier 9]
question: The Eyring analysis spans only 363–393 K (30 K range). The precision of temperature control (±? K for the thermostated oil bath) is not reported. A systematic calibration error of ±1 K in a 30 K window introduces a relative error of ~3% in 1/T, which propagates directly into the slope (ΔH‡_app/R) of the Eyring plot. Was the temperature independently calibrated, e.g., with an internal thermometer?
severity: medium | inference_tier: T2 | root: R30

---

> **Tier 8 redaction notice**: This file is a redacted copy of the corresponding Tier 3 / Tier 9 output. Verbatim source-paper quotations have been replaced by `[REDACTED: see source paper §<loc>; full text retained in Tier 9 reviewer-only deposit]` markers, preserving location references and our own analytical content. Bibliographic fields (title, authors, journal, year, DOI), analytical labels (`evidence_chain:` with B-/U-/A-/C- internal IDs), short technical terms, and our own analytical text are not redacted. The redaction was applied by `scripts/redact_for_tier8.py` and, for this version, by `scripts/build_paperA_R1_public.py` with `scripts/redact_source_ngram_runs.py` (scripts of the project repository; they are not deposited).
