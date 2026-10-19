```
prompt_version: stage1-v15-20260331
model_info: claude-sonnet-4-6

target_title:   Thermally accelerated Heck reaction under direct mechanocatalysis using palladium milling balls
target_authors: Johanna Templ, Suhmi Hwang, Tino Schwemin, Hakan Baltaci and Lars Borchardt
target_start:   page 1: [REDACTED: paper boundary quote; see Tier 9]
target_end:     end of document

[Agent fields]
V1: Mechanochemical organometallic catalysis / synthetic organic chemistry — the primary field of the journal and the paper's experimental approach.
V2: Mechanistic / physical organic chemistry (catalytic cycle analysis) — adjacent field covering elementary steps, kinetics, and evidentiary basis for mechanistic claims absent from V1.
V3: Analytical chemistry / experimental design and data quality — methodological field covering yield measurement validity, characterization standards, and experimental controls absent from V1 and V2.

---

### Step 0: Boundary recheck

All quotes in Turns 1–3 are drawn from within the single-paper PDF (pages 1–5, target_start to target_end). No adjacent paper exists in this document. No boundary violations detected. No items require [?boundary] marking.

---

### Step 1: Cross-field temperatures for overlapping questions

| Overlap group | Question origins | Severities | Convergence | temperature_gap |
|---|---|---|---|---|
| Internal temp / thermal–mechanical claim | V1-Q3 (high), V2-Q5 (critical), V3-OV3 (high) | min=3, max=4 | 3/3 | low |
| Pd leaching / surface vs. homogeneous | V1-Q12 (high), V2-Q4 (critical), V2-OV2 (critical), V3-OV2 (critical), V3-Q4 (high) | min=3, max=4 | 3/3 | low |
| Recyclability undemonstrated | V1-Q8 (high), V3-OV4 (high) | min=3, max=3 | 2/3 | none |
| E/Z stereoselectivity absent | V1-Q10 (medium), V2-Q8 (medium), V2-OV4 (medium) | min=2, max=2 | 2/3 | none |
| No replicates / error bars | V1-Q2 (medium), V3-OV1 (high) | min=2, max=3 | 2/3 | low |
| K₂CO₃ "boiling point" error | V1-Q11 (high), V2-OV3 (medium) | min=2, max=3 | 2/3 | low |

---

### Step 2: Same-root groups

SRG-1: {B-2, B-15} — root: internal temperature of the reaction mixture not measured; makes thermal vs. mechanical contribution unresolvable.
SRG-2: {B-3, B-6} — root: Pd milling ball surface not characterized (composition, area, pre/post state) and Pd leaching into solution not quantified; both derive from absence of heterogeneous catalyst characterization data.
SRG-3: {A-5, B-11} — root: recyclability cited as a core advantage of direct mechanocatalysis but no recycling data (cycle yields, mass loss, Pd contamination) are reported.
SRG-4: {B-4, A-3 (partial)} — root: stereochemical outcome (E/Z ratio) neither reported nor its mechanistic origin discussed.
SRG-5: {B-1, B-7} — root: absence of error quantification and yield measurement method disclosure across all datasets (optimization and scope).
SRG-6: {B-8, A-1} — root: C(sp²)-I chemoselection presented as a positive feature but its kinetic vs. thermodynamic basis is neither tested nor acknowledged as deferred.
SRG-7: {A-2, A-3} — root: mechanism of the Pd ball surface catalytic cycle is not described; reactivity patterns for specific substrate classes derive from the same mechanistic gap.

---

[A] A-1
loc: P4:Lcol (Conclusions)
quote: [REDACTED: see `loc:` above; full text in Tier 9]
deferral_type: deferred
mixed_detail: n/a
reason_inferred: T1 (paper explicitly states deferral)
linked_to: B-8
cross_field_temperature: V2-Q1=high, V2-Q11=medium; convergence=2/3; temperature_gap=low
note: This sentence is the paper's only explicit mechanistic deferral; it covers why ArI is selectively activated over ArBr/ArCl. V2-Q1 (kinetic vs. thermodynamic chemoselection) and V2-Q11 (absolute vs. relative inactivity of ArBr) are subquestions of this deferred mechanism.

---

[A] A-2
loc: P3:Lcol:L15-25* (4-hydroxybiphenyl inhibition)
quote: [REDACTED: see `loc:` above; full text in Tier 9]
deferral_type: mixed
mixed_detail: The paper asserts surface-mediated catalysis as established, but the supporting experiment does not exclude Pd nanoparticle leaching (mechanistic gap). The broader catalytic cycle (oxidative addition, migratory insertion, β-hydride elimination on the Pd surface, role of O₂, role of K₂CO₃) is nowhere described and implicitly deferred to "further mechanistic studies."
reason_inferred: T2 [paper-grounded inference] for the gap; T1 for the explicit "further mechanistic studies" deferral
linked_to: B-2, B-3
cross_field_temperature: V2-Q2=high, V2-Q3=high, V2-Q4=critical; convergence=2/3 for cycle questions, 3/3 for Pd-leaching aspect; temperature_gap=low

---

[A] A-3
loc: P3:Rcol:L1-8* (vinyl scope)
quote: [REDACTED: see `loc:` above; full text in Tier 9]
deferral_type: forgotten
mixed_detail: n/a
reason_inferred: T1 (not stated in paper — no explanation offered)
linked_to: A-2
cross_field_temperature: V1-Q6=medium, V2-Q6=medium; convergence=2/3; temperature_gap=none
note: Low yield with vinyl pyridine and yield suppression with EWG aryl iodides (V1-Q13, V2-Q7) share the same absent explanation and are grouped here; neither is acknowledged as a limitation. V2-Q7 (inverted EWG trend vs. solution-phase Heck) is absorbed into this A item.

---

[A] A-4
loc: P3:Rcol:L20-35* (one-pot Wittig/Heck, Fig. 3 inset)
quote: [REDACTED: see `loc:` above; full text in Tier 9]
deferral_type: forgotten
mixed_detail: n/a
reason_inferred: T2 [paper-grounded inference]
linked_to: B-10
cross_field_temperature: V1-Q15=medium, V2-Q9=medium; convergence=2/3; temperature_gap=none
note: The compatibility of KOtBu (Wittig base) with the Pd ball surface and K₂CO₃ (Heck base) under milling conditions is not addressed; the question of whether the Wittig step or the Heck step limits scope is left open.

---

[A] A-5
loc: P4:Lcol (Conclusions)
quote: [REDACTED: see `loc:` above; full text in Tier 9]
deferral_type: deferred
mixed_detail: n/a
reason_inferred: T1 (paper frames recyclability as an advantage inherent to the approach)
linked_to: B-11
cross_field_temperature: V1-Q8=high, V3-OV4=high; convergence=2/3; temperature_gap=none
note: Catalyst recyclability is cited as the principal advantage of direct mechanocatalysis throughout the paper, but no recycling experiment (cycles, yields, mass loss, Pd content of product) appears anywhere in the main text or is referenced in ESI. Grouped with SRG-3.

---

[B] B-1
loc: P2:Lcol:L1-5* (standard conditions)
quote: [REDACTED: see `loc:` above; full text in Tier 9]
classification: methodological_limitation
rhetorical_function: Statement of standard reaction conditions from which all yield data derive.
note: No replicates reported for any entry in the optimization table or scope; no error bars or standard deviations given. It is impossible to determine whether inter-entry yield differences (e.g., 44% vs. 35% in Fig. 2) are statistically significant. [metric incompleteness]
cross_field_temperature: V1-Q2=medium, V3-OV1=high; convergence=2/3; temperature_gap=low

---

[B] B-2
loc: P2:Rcol:L30-40* (frequency discussion)
quote: [REDACTED: see `loc:` above; full text in Tier 9]
classification: methodological_limitation
rhetorical_function: Mechanistic interpretation of frequency-dependent yield data to support the "mechanically driven" claim in the title.
note: The frequency experiment is conducted at fixed external thermostat temperature (120 °C), but internal temperature of the milling jar was not measured at any frequency. Lower frequency may generate less frictional heat and reduce actual internal temperature; without internal temperature data, the paper's mechanistic claim—that the Heck reaction requires mechanical energy input specifically—cannot be distinguished from a purely thermal explanation. The claim in the paper's title ("thermally accelerated") further depends on this uncontrolled variable. [mechanistic claim without necessary control]
cross_field_temperature: V1-Q3=high, V2-Q5=critical, V3-OV3=high; convergence=3/3; temperature_gap=low

---

[B] B-3
loc: P1:Rcol:L30-40* (Introduction, direct mechanocatalysis)
quote: [REDACTED: see `loc:` above; full text in Tier 9]
classification: methodological_limitation
rhetorical_function: Framing statement presenting separation and recyclability as defining advantages of the direct mechanocatalytic approach.
note: The paper's central claim—that the Pd ball is the surface-active catalyst rather than leached Pd nanoparticles—rests solely on the 4-hydroxybiphenyl inhibition experiment. However, 4-hydroxybiphenyl is also a known inhibitor of Pd nanoparticles in solution. A mercury-drop test or TEMPO radical trap would be required to distinguish true surface catalysis from nanoparticle catalysis (V2-Q4). Additionally, quantitative ICP-MS or ICP-OES analysis of dissolved Pd in the product mixture is absent (V1-Q12), meaning the product purity and the recyclability claim cannot be evaluated analytically. Pd ball not characterized before or after use (V3-Q4). [negative result as evidence; mechanistic claim without mechanistic probes]
cross_field_temperature: V1-Q12=high, V2-Q4=critical, V2-OV2=critical, V3-OV2=critical, V3-Q4=high; convergence=3/3; temperature_gap=low

---

[B] B-4
loc: P4:Lcol (Conclusions)
quote: [REDACTED: see `loc:` above; full text in Tier 9]
classification: methodological_limitation
rhetorical_function: Summary statement implicitly conveying that all products are formed with defined stereochemistry.
note: Products are named as trans-stilbenes throughout, and one product (3a) is explicitly called "trans-stilbene," yet E/Z ratio, isomer characterization, or conditions affecting stereoselectivity are never discussed in the paper. Whether stereoselectivity is complete (E-only), near-complete, or kinetically controlled is unreported. [metric incompleteness]
cross_field_temperature: V1-Q10=medium, V2-Q8=medium, V2-OV4=medium; convergence=2/3; temperature_gap=none

---

[B] B-5
loc: P2:Lcol (Fig. 2, optimization)
quote: [REDACTED: see `loc:` above; full text in Tier 9]
classification: methodological_limitation
rhetorical_function: Summary of identified optimal conditions following one-factor-at-a-time parameter screening.
note: No blank experiment (reaction without Pd milling ball, using a chemically inert ball such as ZrO₂ or stainless steel) appears anywhere in the optimization table or in the ESI reference. Without a zero-catalyst control, contamination-driven background catalysis cannot be ruled out. [missing control experiment]
cross_field_temperature: V3-Q6=high; convergence=1/3

---

[B] B-6
loc: P2:Lcol:L1-5* (standard conditions)
quote: [REDACTED: see `loc:` above; full text in Tier 9]
classification: methodological_limitation
rhetorical_function: Specification of catalyst and reactor components in the standard conditions.
note: The Pd milling ball is identified only by diameter; supplier, purity grade, surface oxide state, roughness, and surface area are not reported. Without surface area, effective catalyst loading (mol Pd surface-accessible) is unknown, making turnover number (TON) and turnover frequency (TOF) incalculable and comparison with other Pd catalysts impossible. No pre/post characterization (SEM, XPS) is provided to confirm the ball remains intact and is not fragmenting into particles. [metric incompleteness]
cross_field_temperature: V3-Q3=high, V3-Q4=high; convergence=2/3 (both V3); temperature_gap=none

---

[B] B-7
loc: P3 (Fig. 3 caption footnote)
quote: [REDACTED: see `loc:` above; full text in Tier 9]
classification: methodological_limitation
rhetorical_function: Footnote in the scope figure caption specifying that some yields differ from isolated values.
note: The footnote indicates some scope entries use ¹H NMR yields, but does not identify which specific substrates these are, nor does it state that an internal standard was used for quantification. Isolated and ¹H NMR yields can differ by >10 percentage points. The optimization table (Fig. 2) does not specify the yield measurement method at all. [metric incompleteness; information asymmetry in data presentation]
cross_field_temperature: V3-Q1=medium, V3-Q2=high; convergence=2/3 (V3 only); temperature_gap=low

---

[B] B-8
loc: P3:Lcol:L20-35* (chemoselectivity paragraph)
quote: [REDACTED: see `loc:` above; full text in Tier 9]
classification: mixed
rhetorical_function: Statement presenting scope restriction (ArBr/ArCl inactivity) as a positive chemoselectivity feature distinguishing this method from solution-phase analogs.
note: [intentional_narrowing] The authors frame the inability to couple ArBr and ArCl as a deliberate advantage for selective functionalization of multi-halogenated substrates. [methodological_limitation] Whether ArBr truly cannot react (zero reactivity) or reacts too slowly under these conditions (kinetic selectivity) is not established; no prolonged-reaction or competition experiment distinguishes these. The conditions for the chemoselectivity demonstration (1-bromo-4-iodobenzene) are not explicitly stated to be identical to standard conditions (V1-Q4). [categorically discontinuous conditions; negative result as evidence]
cross_field_temperature: V1-Q4=low, V2-Q1=high, V2-Q11=medium; convergence=2/3; temperature_gap=medium

---

[B] B-9
loc: P1:Rcol:L4-8* (abstract)
quote: [REDACTED: see `loc:` above; full text in Tier 9]
classification: methodological_limitation
rhetorical_function: Abstract-level summary of the paper's central contribution.
note: Mass balance is not reported for any reaction; for substrates with moderate or low yields (e.g., 3i: 48%, 3t: 18%, 3u-3w: 82–84%), it is unknown whether unreacted starting material is recovered or whether side products form. [metric incompleteness; mass balance absent]
cross_field_temperature: V1-Q1=medium; convergence=1/3

---

[B] B-10
loc: P3:Rcol:L20-35* (one-pot Wittig/Heck)
quote: [REDACTED: see `loc:` above; full text in Tier 9]
classification: mixed
rhetorical_function: Presentation of one-pot Wittig olefination / Heck cross-coupling as a demonstration of expanded synthetic utility.
note: [intentional_narrowing] Scope is limited to two examples. [substrate_selection_bias] No statement discloses whether additional substrates were attempted and failed; selective reporting of successful examples without failure disclosure is a substrate selection bias. [metric incompleteness] Yield measurement method (isolated or NMR) is not specified for these two products.
cross_field_temperature: V1-Q7=medium, V3-Q7=medium; convergence=2/3; temperature_gap=none

---

[B] B-11
loc: P1:Rcol:L30-40* (Introduction)
quote: [REDACTED: see `loc:` above; full text in Tier 9]
classification: methodological_limitation
rhetorical_function: Motivational statement identifying catalyst recyclability as a core advantage of the direct mechanocatalytic approach.
note: No catalyst recycling experiment is reported in the paper or referenced in ESI; the recyclability advantage is stated as inherent to the approach based on the ability to remove the ball from the reaction mixture, but yield maintenance over multiple cycles, Pd ball mass loss, and Pd contamination of product streams are untested. [claimed advantage without supporting data]
cross_field_temperature: V1-Q8=high, V3-OV4=high; convergence=2/3; temperature_gap=none

---

[B] B-12
loc: P3:Lcol:L15-25* (inhibition experiment)
quote: [REDACTED: see `loc:` above; full text in Tier 9]
classification: methodological_limitation
rhetorical_function: Control experiment presented as mechanistic evidence that catalytic activity originates from the Pd surface.
note: Inhibition is reported at a single dose (0.5 equiv.); no dose-response data are provided. A dose-response across multiple inhibitor loadings would be required to distinguish surface-site saturation (Langmuir-consistent with heterogeneous catalysis) from bulk-phase Pd nanoparticle inhibition. The experiment is presented as conclusive evidence without sufficient data points. [negative result as evidence; single-point data]
cross_field_temperature: V3-Q8=medium; convergence=1/3

---

[B] B-13
loc: P2:Lcol:L5-15* (time optimization)
quote: [REDACTED: see `loc:` above; full text in Tier 9]
classification: methodological_limitation
rhetorical_function: Justification for the 2-hour reaction time as the standard condition.
note: Only two time points are compared (30 min: 57%; 2 h: 82%); no kinetic profile (yield vs. time) is provided. The claim of "incomplete conversion" is not supported by measurement of remaining starting material. Without a time profile, whether 2 h represents a plateau or an intermediate point, and whether the reaction has an induction period, cannot be assessed. [metric incompleteness]
cross_field_temperature: V3-Q9=medium; convergence=1/3

---

[B] B-14
loc: P2:Lcol (Fig. 2, optimization)
quote: [REDACTED: see `loc:` above; full text in Tier 9]
classification: methodological_limitation
rhetorical_function: Definition of the standard conditions resulting from one-factor-at-a-time optimization.
note: The optimization varies one parameter at a time without factorial design; parameter interactions (e.g., temperature × frequency, base × bulking agent) are not probed, limiting confidence that the identified optimum is a global rather than local optimum. All optimization entries are apparent single experiments. [experimental design limitation]
cross_field_temperature: V1-Q14=medium; convergence=1/3

---

[B] B-15
loc: P2:Lcol:L1-5* (standard conditions)
quote: [REDACTED: see `loc:` above; full text in Tier 9]
classification: methodological_limitation
rhetorical_function: Specification of the thermal conditions used in the standard procedure.
note: The method for maintaining and measuring the external temperature (heating device, thermocouple placement, calibration) is not described. The difference between external set-point and actual internal reaction temperature is a major uncontrolled variable, particularly relevant to the paper's central "thermally accelerated" claim. Grouped in SRG-1 with B-2.
cross_field_temperature: V3-Q5=medium; convergence=1/3

---

[C] C-1
loc: P1:Rcol (Introduction, mechanochemical cross-coupling survey)
citation: Refs to mechanochemical Negishi, Buchwald-Hartwig, Suzuki-Miyaura, Tsuji-Trost, Mizoroki-Heck using Pd powder (cited collectively in Introduction)
textual_function: Cited as the state-of-the-art mechanochemical cross-coupling protocols that share the recyclability limitation of catalyst in powdered form, motivating the present direct mechanocatalytic approach.
reason_severed: The cited protocols are grouped and characterized by a shared limitation (catalyst powder, filtration required) without comparing yields, substrate scope, or conditions to the current paper's results; no quantitative comparison is made.
affects_claims: yes — the paper's claim of superiority over prior mechanochemical protocols rests on an asserted recyclability advantage, but since no quantitative yield or scope comparison is made, the relative performance of this work vs. the cited methods cannot be assessed.
symmetric_pattern: yes — all cited mechanochemical coupling papers are treated identically (grouped, characterized by the same limitation, then dismissed in favor of the direct mechanocatalytic approach).

---

[C] C-2
loc: P1:Rcol (Introduction, direct mechanocatalysis paragraph)
citation: Refs to Pd milling ball Suzuki–Miyaura and Sonogashira couplings (same group; Hwang et al. RSC Mechanochem. 2024 and related)
textual_function: Cited as the proof-of-concept for using metallic Pd milling balls as direct mechanocatalysts in other cross-coupling reactions, establishing the enabling precedent for the current Heck work.
reason_severed: Cited only as precedent; no comparison of the mechanistic conditions, TON, Pd leaching, or substrate scope between those reactions and the Heck reaction is made. Mechanistic differences between Suzuki and Heck reactions on the Pd surface (different catalytic cycles) are not discussed.
affects_claims: medium — the paper extrapolates recyclability and surface-catalysis claims from the cited precedents to the Heck system, but does not demonstrate that the mechanistic basis established for Suzuki couplings applies equally to Heck reactions.
symmetric_pattern: yes — both cited coupling-type papers are treated as equivalent enabling precedents without differentiation.

---

[U] U-1
loc: P2:Lcol (Fig. 2, temperature entries)
quote: [REDACTED: see `loc:` above; full text in Tier 9]
question: K₂CO₃ is a solid ionic salt with a melting point of ~891 °C; it has no boiling point of 119 °C. The text appears to contain a factual error — either the substance referred to is not K₂CO₃, or the property cited (119 °C boiling point) is not its boiling point. If this error is in the paper, the causal explanation for yield reduction at higher temperatures is incorrect as stated.
originating_agent: V1 (V1-Q11); confirmed by V2 (V2-OV3)
severity: high (V1); medium (V2)
note: This does not fit A (no prospective deferral), B (not a rejected approach or scope limitation), or C (not an uncontinued citation). The item is a potential factual error in the paper's causal reasoning, preserved here for Stage 2 D-4 attention.

---

[META]
  linked_items:
    - A-1 ↔ B-8 (chemoselection mechanism deferred in A-1 is the mechanistic basis for scope limitation framed as positive feature in B-8)
    - A-2 ↔ B-2 (catalytic cycle mechanism deferred; frequency experiment supports thermal claim but internal temperature is uncontrolled)
    - A-2 ↔ B-3 (catalytic cycle mechanism deferred; surface vs. homogeneous catalyst identity is part of the same mechanistic gap)
    - A-3 ↔ B-8 (substrate reactivity trends for specific substrates derive from same mechanistic gap as chemoselection)
    - A-4 ↔ B-10 (one-pot scope limitation linked to unanswered compatibility questions)
    - A-5 ↔ B-11 (recyclability deferred in A-5 is the same claim stated without data in B-11)
    - B-2 ↔ B-15 (both concern unmeasured temperature variables in the same experimental system)
    - B-3 ↔ B-12 (Pd leaching absent; inhibition experiment is the only mechanistic probe but insufficient)

  same_root_groups:
    - SRG-1: {B-2, B-15} — internal temperature of reaction not measured; thermal vs. mechanical contribution claim rests on uncontrolled variable
    - SRG-2: {B-3, B-6} — Pd ball surface characterization and Pd leaching measurement both absent; both derive from absence of heterogeneous catalyst characterization data
    - SRG-3: {A-5, B-11} — recyclability claimed as core advantage of the approach but no recycling data reported
    - SRG-4: {B-4, A-3 (partial)} — E/Z outcome unreported and mechanistic basis for stereoselectivity not discussed
    - SRG-5: {B-1, B-7} — yield measurement error and method undisclosed across optimization and scope datasets
    - SRG-6: {B-8, A-1} — C(sp²)-I chemoselectivity framed as positive but its kinetic vs. thermodynamic basis is both the deferred mechanistic question (A-1) and the unexamined premise of the scope restriction (B-8)
    - SRG-7: {A-2, A-3} — catalytic cycle on Pd surface not described; mechanistic explanation for substrate reactivity trends shares the same absent foundation

  symmetric_citations:
    - C-1 and C-2 are both cite-and-dismiss in parallel: C-1 dismisses prior art by assigning a shared limitation; C-2 cites same-group precedent to authorize the present approach without mechanistic comparison

  unreported_data:
    - ESI referenced for details of inhibition control experiment and additional substrate data but specific contents not evaluable from main text
    - Recycling cycle data (claimed capability, not shown)
    - Full substrate consumption / mass balance for all scope entries
    - Internal temperature measurements
    - Pd ball characterization (pre/post SEM, XPS, mass)
    - ICP-MS of product mixtures for Pd content

  series_signal: no

---

[TEMPERATURE_SUMMARY]
  high_convergence_high_gap: none
  high_convergence_low_gap:
    - B-2 (internal temp / thermal-mechanical; convergence=3/3, gap=low)
    - B-3 (Pd leaching / surface catalysis; convergence=3/3, gap=low)
    - B-1 (no replicates; convergence=2/3, gap=low)
    - B-7 (yield method disclosure; convergence=2/3, gap=low)
    - B-8 (chemoselectivity mixed; convergence=2/3, gap=medium)
    - A-1 (chemoselection deferred; convergence=2/3, gap=low)
    - A-3 (substrate trends; convergence=2/3, gap=none)
    - A-4 (one-pot scope; convergence=2/3, gap=none)
    - A-5 / B-11 (recyclability; convergence=2/3, gap=none)
    - B-4 (E/Z; convergence=2/3, gap=none)
    - B-10 (one-pot scope; convergence=2/3, gap=none)
  low_convergence_high_gap:
    - B-5 (no blank control; V3-Q6=high; convergence=1/3; flagged for D-4 attention)
    - B-6 (Pd ball characterization; V3-Q3/Q4=high; convergence=1 agent)
    - U-1 (K₂CO₃ error; V1=high, V2=medium; convergence=2/3, gap=low — borderline)

---

[GAP]
GAP-1 | type: 3 | priority: high | description: Mercury-drop test or analogous experiment to definitively distinguish heterogeneous Pd ball surface catalysis from homogeneous Pd nanoparticle catalysis under mechanochemical conditions | candidate_paper: Not recoverable from paper | inference_label: T2 | status: pending

GAP-2 | type: 1 | priority: medium | description: Same-group precedent papers for Pd milling ball Suzuki–Miyaura and Sonogashira couplings (cited in Introduction, Hwang et al. RSC Mechanochem. 2024 and related) — needed to compare surface area, TON, and mechanistic basis across coupling types | candidate_paper: Hwang et al. RSC Mechanochem. 2024 (ref ~40 in paper) | inference_label: T1 | status: pending

GAP-3 | type: 3 | priority: medium | description: Internal temperature measurement methodology for ball mills under operating conditions (e.g., in situ infrared or thermocouple methods) — needed to validate the thermal vs. mechanical energy claim | candidate_paper: Not recoverable from paper | inference_label: T3 | status: pending

GAP-4 | type: 2 | priority: low | description: Contemporary mechanochemical Heck papers using Pd nanoparticle dispersions (not milling balls) that may address the recyclability and chemoselectivity questions without being cited here | candidate_paper: Not recoverable from paper | inference_label: T3 | status: pending

inference_time_sec: not available — inject externally
```

---

> **Tier 8 redaction notice**: This file is a redacted copy of the corresponding Tier 3 / Tier 9 output. Verbatim source-paper quotations have been replaced by `[REDACTED: see source paper §<loc>; full text retained in Tier 9 reviewer-only deposit]` markers, preserving location references and our own analytical content. Bibliographic fields (title, authors, journal, year, DOI), analytical labels (`evidence_chain:` with B-/U-/A-/C- internal IDs), short technical terms, and our own analytical text are not redacted. The redaction was applied by `scripts/redact_for_tier8.py` and, for this version, by `scripts/build_paperA_R1_public.py` with `scripts/redact_source_ngram_runs.py` (scripts of the project repository; they are not deposited).
