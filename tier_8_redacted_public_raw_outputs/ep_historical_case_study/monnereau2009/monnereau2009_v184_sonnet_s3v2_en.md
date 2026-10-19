prompt_version: stage3-v2-en-20260419
model_info: claude-sonnet-4-6

# Re-certification Assessment Sheet for Scientific Knowledge

## Monnereau, Sémeril, Matt, Toupet, Mota 2009 (Adv. Synth. Catal. full_paper)

---

### §1 Claim Architecture

**Core claim:** Cationic Ni complex **2** (1,3-calix[4]arene-diphosphine ligand) catalyses Kumada–Tamao–Corriu coupling at TOFs up to 21,250 mol(ArBr)·mol(2)⁻¹·h⁻¹ at 1 × 10⁻³ mol% loading, surpassing [NiCl₂(dppp)]; elevated activity attributed to dynamic PNiP bite-angle enlargement (fanning motion) facilitating the reductive elimination step. **Novelty pillar:** (i) TOF breakthrough over dppp benchmark; (ii) mechanistic attribution to PNiP fanning dynamics. **Utility pillar:** ArBr/ArCl scope, air-stable precatalyst.

**Layered structure:** Three independent layers: (1) catalytic performance (TOF > dppp), (2) mechanistic attribution (dynamic bite angle → coupling step), (3) air-stability advantage. Layer 2 failure does not collapse layer 1; layer 1 data cannot establish layer 2. A single refutation cannot collapse all layers. Inter-layer dependency asymmetry: layers 1 and 3 survive layer 2 failure; layer 2's design-principle claim is undermined without layer 1's empirical context.

---

### §2 SRG / CLA → RI / ER / EP Crosswalk

**SRG-1 [Bite-angle-dynamics mechanistic claim — no kinetic or control evidence]**

* **Primary RI**: RI-03 Unobserved explanatory
* **Secondary RI**: RI-06 Imported model
* **ER**: Establishing that PNiP fanning facilitates reductive elimination requires (a) rate-limiting step assigned to coupling step for ArBr by kinetic measurement; (b) dynamic angle change — not time-average bite angle — demonstrated as the kinetically relevant variable. Structural data and qualitative conversion trends satisfy neither condition.
* **EP**: EP-03a Direct-observation / state-assignment pack; EP-06a Analogy-validation pack
* **Case-specific implementation**: (EP-03a) Initial-rate measurements varying [Ni], [PhMgBr], [ArBr] or Hammett plot from existing Table 3 ArBr entries to determine rate law and assign rate-limiting step at 100°C/dioxane. (EP-06a) EPR monitoring or radical clock substrate under catalytic conditions to exclude Ni(I)/Ni(III) manifold before invoking Pd(0)/Pd(II) analogies from refs [27]/[28].
* **Notes**: Members: U-2 (high, 3/3; prerequisite-absence — mechanistic conclusion stated as fact without kinetic data); U-3 (high; rigid-analogue control absent despite paper's own model predicting its necessity); A-1 (deferred: rigid analogue); A-2 (prospective: bulkier P substituents). U-2 primary 3/3 high_convergence_low_gap driver. RI-03 + RI-06 co-occur: resolving RI-03 alone is insufficient if RI-06 (Pd→Ni analogy unvalidated) persists — cross-case pattern, see §6.

---

**SRG-2 [Rate-limiting step inferred from qualitative trends; ortho/meta anomaly unaddressed]**

* **Primary RI**: RI-05 Qualitative overread
* **Secondary RI**: RI-04 Unreplicated discriminator
* **ER**: Assigning "oxidative addition rate-limiting for ArCl" and implicitly "coupling step rate-limiting for ArBr" on the basis of electronic conversion trends requires Hammett or initial-rate data. Anomalous regiochemical insensitivity (2-bromotoluene 1760 h⁻¹ ≈ 3-bromotoluene 1810 h⁻¹ despite expected ortho steric suppression) must be mechanistically interpreted.
* **EP**: EP-05a Quantitative-ranking substantiation pack; EP-04a Discrimination / replication pack
* **Case-specific implementation**: (EP-05a) Hammett σ plot using Table 3 ArBr entries (4-bromoanisole, 4-bromotoluene, bromobenzene) to obtain ρ. (EP-04a) Explicit commentary on ortho/meta-bromotoluene equality as a kinetic constraint: absence of ortho suppression argues against OA rate-limiting for ArBr and should be integrated into the rate-limiting step discussion.
* **Notes**: Members: U-2, B-3, B-5. B-3 (1/3, V1 high) low_convergence_high_gap. The ortho/meta equality (B-5) is a negative result present in the paper's own Table 3 with direct mechanistic discriminating power, unacknowledged.

---

**SRG-3 [Active species uncharacterised; activation fraction unquantified]**

* **Primary RI**: RI-02 Object identification
* **Secondary RI**: RI-08 Unquantified reliability
* **ER**: TOF values require (a) oxidation state assignment for the thermal activation product (δ ³¹P = 41.8 ppm singlet) to confirm Ni(0) entry into the catalytic cycle; (b) quantification of the activation fraction at 65°C to enable per-activated-Ni TOF computation.
* **EP**: EP-02a Identity / purity substantiation pack; EP-08a Replication / uncertainty pack
* **Case-specific implementation**: (EP-02a) UV-vis or ESI-MS of the activation product in dioxane at 100°C to distinguish Ni(0) d¹⁰ from Ni(II) d⁸. (EP-08a) ³¹P NMR integration vs. internal phosphorus standard after 1 h at 65°C to quantify activation fraction; compute activation-corrected TOF for dppp comparison.
* **Notes**: Members: U-1 (high, 3/3; self-contradictory absence — Ni(0) cycle entry predicted but not confirmed); B-6 (2/3; activation fraction unquantified at 65°C). U-1 primary 3/3 high_convergence_low_gap candidate. All Table 3 TOF values are lower bounds on per-site activity.

---

**SRG-5 [ΔG‡ unassignable to the fanning motion; internal ³¹P data inconsistency]**

* **Primary RI**: RI-01 Reporting integrity
* **Secondary RI**: RI-04 Unreplicated discriminator
* **ER**: The kinetic argument (fanning frequency >> coupling frequency at 100°C) requires ΔG‡ = 11.3 kcal·mol⁻¹ specifically assigned to motion 2 (PNiP fanning). The ³¹P NMR characterisation of complex 2 at −80°C must be consistent between main text (δ_B = 28.6 ppm, J = 41 Hz) and Experimental section (δ_B = 18.8 ppm, J = 34.8 Hz at 193 K): Δδ = 9.8 ppm, ΔJ = 6.2 Hz.
* **EP**: EP-01a Reporting-coherence pack; EP-04a Discrimination / replication pack
* **Case-specific implementation**: (EP-01a) Deposit raw ³¹P FID; re-record at 600 MHz with corrected parameters. (EP-04a) VT-¹H and VT-³¹P NMR at 600 MHz to separate the two near-coincident coalescence temperatures (both ~−30°C at 400 MHz; footnote [23]) and assign ΔG‡(motion 1) and ΔG‡(motion 2) independently.
* **Notes**: Members: U-6 (high, 2/3; barrier from indeterminate composite process); U-5 (high, 1/3; 9.8 ppm/6.2 Hz inconsistency); B-10 (reporting aspect of U-5). U-6 high_convergence_low_gap (low gap); U-5 low_convergence_high_gap. The barrier-assignment failure (U-6) is logically prior to the kinetic rate-comparison argument: if ΔG‡ cannot be assigned to motion 2, the "fanning faster than coupling" argument collapses.

---

**SRG-6 [GC-only reporting; no isolated yields; no per-substrate homocoupling data]**

* **Primary RI**: RI-08 Unquantified reliability
* **ER**: Performance claim at 10⁻³ mol% loading requires at minimum one isolated yield under optimal conditions (Table 2, entry 7: 100% GC conversion) and per-substrate homocoupling percentages for the highest-conversion entries (8, 12) where Ar–Ar formation is most significant.
* **EP**: EP-08a Replication / uncertainty pack
* **Case-specific implementation**: Isolate biaryl product from entries 1, 9, 13; report individual homocoupling GC% for entries 8 (95.6% conv.) and 12 (92.9% conv.).
* **Notes**: Members: B-1 (GC-only, 24 entries), B-2 (global <3% homocoupling, no substrate breakdown). Both 1/3, V1 medium. Resolving SRG-6 is prerequisite for verifying the synthetic utility claim (D-1 layer 3).

---

**SRG-7 [Benchmark comparison restricted; prior system not compared numerically]**

* **Primary RI**: RI-09 External superiority
* **Secondary RI**: RI-07 Unsupported boundary
* **ER**: "Outperforms the fastest diphosphine-based catalysts" requires dppp tested at ArBr/2 = 50,000 (the loading where complex 2's highest TOFs occur), or a principled justification for why the ArBr/2 = 5000 single-point comparison suffices.
* **EP**: EP-09a Internal benchmark pack; EP-07a Boundary-test pack
* **Case-specific implementation**: (EP-09a) One additional GC run of [NiCl₂(dppp)] at ArBr/2 = 50,000, 100°C, dioxane, 4-bromoanisole; reproduce ref [19] NiBr₂/propyl-calixarene TOF numerically as a Table 3 comparison entry. (EP-07a) Test [NiCl₂(dppp)] with bromomesitylene to determine whether the claimed advantage is substrate-class-specific.
* **Notes**: Members: B-3 (1/3, V1 high; low_convergence_high_gap); B-4 (ArCl at 5000 only, not at 50,000); C-10 (prior [19] system not compared numerically). RI-07 applies as negative-boundary variant: "outperforms all diphosphine catalysts" asserted without testing the most favourable loading for potential competitors.

---

**SRG-8 [Crystallographic evidence insufficient for P–Ni–P = 102.84°]**

* **Primary RI**: RI-01 Reporting integrity
* **Secondary RI**: RI-05 Qualitative overread
* **ER**: For 102.84° to serve as the structural anchor of the bite-angle-dynamics argument, the refinement must meet standard thresholds (GoF ≈ 1.0, wR2 < 15%, residual < ±0.5 e·Å⁻³); disordered solvent must be modelled; and the [22] bite angle range must be reproduced numerically.
* **EP**: EP-01a Reporting-coherence pack; EP-05a Quantitative-ranking substantiation pack
* **Case-specific implementation**: (EP-01a) Re-refinement with SQUEEZE for ½C₆H₁₄ + CH₂Cl₂; expand Table 1 to include Ni–Cp centroid distance and C–P–C angles. (EP-05a) Reproduce the P–Ni–P range from ref [22] numerically in Table 1 footnote to verify that 102.84° is "normal" for [NiCp(PPh₃)₂]⁺ complexes.
* **Notes**: Members: B-7 (1/3, V3 high; GoF 0.882, wR2 17.48%, residual ±1.4 e·Å⁻³); B-8 (Table 1 incomplete); C-13 (bite angles from [22] not reproduced). B-7 low_convergence_high_gap. RI-05 co-occurs: "compares with other [NiCp(PPh₃)₂]⁺ complexes" is a qualitative structural assertion without numerical comparator.

---

**Outside the SRGs: CLAs**

**CLA-1: Ni(I)/Ni(III) radical pathway not excluded; Pd→Ni analogy unvalidated**

* **Primary RI**: RI-06 Imported model
* **Secondary RI**: RI-03 Unobserved explanatory
* **ER**: Before the Pd(0)/Pd(II) mechanistic analogy ([27]/[28]) can be applied, Ni(I)/Ni(III) radical participation must be excluded by a mechanistic probe appropriate for organometallic Ni catalysis.
* **EP**: EP-06a Analogy-validation pack; EP-03a Direct-observation / state-assignment pack
* **Case-specific implementation**: EPR during catalysis in dioxane at 100°C to detect Ni(I) signals; and/or ring-opening radical clock ArBr substrate to discriminate ionic from radical elementary steps.
* **Notes**: Grounded in U-4 (1/3, V2 high; low_convergence_high_gap); C-14 (Pd analogies [27]/[28] cited without quantitative mapping). Self-contradictory absence: paper proposes Ni(0)/Ni(II) cycle (Schemes 4–5) but performs no mechanistic probe to distinguish it from Ni(I)/Ni(III). Not in formal SRG; linked to SRG-1 via U-2.

---

**CLA-2: Bromomesitylene outlier suppressed in "congested bromoarenes" scope claim**

* **Primary RI**: RI-05 Qualitative overread
* **Secondary RI**: RI-07 Unsupported boundary
* **ER**: The abstract claim "high activities with … congested bromoarenes" requires either including bromomesitylene (TOF = 780 h⁻¹; 16-fold below highest ArBr at same loading) within the "high activity" frame with justification, or bounding the scope claim to exclude fully ortho-blocked trisubstituted ArBr.
* **EP**: EP-05a Quantitative-ranking substantiation pack; EP-07a Boundary-test pack
* **Case-specific implementation**: (EP-05a) Quantify steric sensitivity gradient: bromomesitylene (780) vs. 2-bromotoluene (1760) vs. bromobenzene (2220 h⁻¹); interpret whether the rate-limiting step for 2,4,6-trisubstituted ArBr is oxidative addition. (EP-07a) Test 2,6-dimethylbromobenzene to locate the steric tolerance limit.
* **Notes**: Grounded in A-3 (suppressed; all three suppression criteria met). The bromomesitylene result internally contradicts the mechanistic hypothesis: dynamic bite-angle enlargement is proposed to facilitate congested substrates, yet the most congested ArBr tested gives the lowest TOF. Not in formal SRG.

---

### §3 Current VQ assessment

**Current judgment: VQ-2 (Method), qualified**

**VQ-1 [Observation] — holds (qualified)**
RI-02 (SRG-3): Activation product identity uncharacterised; ³¹P NMR internally inconsistent (U-5/B-10). **Non-fatal** to the observation layer: GC detection of biaryl product is independent of these deficiencies. VQ-1 holds — qualified — on the premise that RI-02 is non-fatal to the cross-coupling observation itself.

**VQ-2 [Method] — holds (qualified), on premise that RI-02 is non-fatal**
RI-01 (SRG-5): ³¹P NMR inconsistency (9.8 ppm, 6.2 Hz) is non-fatal to catalytic GC data but fatal to the NMR-based barrier argument. RI-09 (SRG-7): single-loading dppp comparison provides partial experimental grounding; headline ultra-low-loading superiority remains asserted. Both non-fatal to VQ-2 overall. VQ-2 holds (qualified): catalytic performance claim is GC-grounded with restricted direct comparison; mechanistic support at NMR level collapses.

**VQ-3 [Mechanism] — fails**
RI-03 (SRG-1): [Ni(Ar)(Ar')·1] intermediate neither observed nor kinetically constrained. **Fatal.** RI-06 (CLA-1): Ni(I)/Ni(III) not excluded; Pd→Ni analogy unvalidated. **Fatal.** RI-04 (SRG-5): ΔG‡ = 11.3 kcal·mol⁻¹ cannot be assigned to fanning motion specifically. **Fatal.** VQ-3 fails; unresolved: RI-03, RI-06, RI-04.

**VQ-4 [Benchmark] — fails (inherits VQ-3 failure)**
Additionally unresolved: RI-08 (activation-fraction correction and isolated yields absent; non-fatal individually); RI-09 (ultra-low-loading dppp comparison absent). VQ-4 fails because VQ-3 is a prerequisite.

**Layered VQ asymmetry:** **Performance layer (layer 1)** independently reaches VQ-2 (qualified): GC conversion data and the ArBr/2 = 5000 dppp comparison are methodologically coherent. **Mechanistic attribution layer (layer 2)** does not reach VQ-1 as a standalone claim: active species unidentified, mechanistic intermediate unobserved.

---

### §4 Era-Norm Annotation

**communication-era tolerated:**
- **B-1** (GC-only, no isolated yields): Adv. Synth. Catal. 2009 normalised GC-conversion-only scope tables for multi-entry catalytic surveys; no ESI section existed for supplementary isolation data.
- **B-2** (global <3% homocoupling): Single global selectivity threshold was accepted practice in 2009 catalytic scope papers in this venue.
- **B-3** (single-point dppp comparison): Single-point benchmark comparison under matched conditions was acceptable in 2009 full papers demonstrating catalytic superiority.
- **B-7/B-8** (below-threshold crystallographic statistics, abbreviated Table 1): CheckCIF enforcement was not universal in 2009; below-threshold GoF and abbreviated bond tables were tolerated in catalytic papers where the structure was supportive rather than primary.
- **B-10** (³¹P NMR discrepancy unreported): Editorial cross-checking between main text and Experimental NMR was not automated; inconsistencies were more likely to pass undetected in 2009.

**modern-era deficient:**
- **B-1** (GC-only): Current ACS Catalysis/JACS standards require at minimum one representative isolated yield for the headline optimised entry at 10⁻³ mol% loading.
- **U-1/B-6** (active species uncharacterised, activation fraction unquantified): Modern mechanistic catalysis papers require spectroscopic oxidation-state assignment of the active Ni species and precatalyst activation quantification before TOF values are interpreted as per-site rates.
- **U-4** (Ni(I)/Ni(III) not excluded): Post-2015 Ni radical mechanism literature has established Ni(I)/Ni(III) as a required alternative to discuss or exclude in any paper proposing a Ni(0)/Ni(II) ionic cycle.
- **B-7** (below-threshold crystallographic statistics without acknowledgment): Current CheckCIF-enforced standards require explicit acknowledgment of GoF < 0.9 and wR2 > 15% with documentation of disordered-solvent treatment.
- **U-5/B-10** (internal ³¹P NMR inconsistency): A 9.8 ppm discrepancy between nominally equivalent datasets would not pass modern editorial review; automated or reviewer cross-checking would require resolution before publication.

---

### §5 Shortest-reinforcement route

**Objective function 1: VQ-3 (Mechanism)**

**Shortest route to VQ-3:**
1. **EP-02a** [Identity / purity substantiation pack] — UV-vis characterisation of activation product (δ ³¹P = 41.8 ppm) to assign Ni oxidation state; ³¹P NMR integration vs. internal standard to quantify activation fraction at 65°C. Advances RI-02 (SRG-3).
2. **EP-01a** [Reporting-coherence pack] — Resolve ³¹P NMR discrepancy; re-record VT-¹H/³¹P at 600 MHz to separate two near-coincident coalescence temperatures and assign ΔG‡(motion 1) and ΔG‡(motion 2) independently. Advances RI-01 (SRG-5) and RI-04 (U-6 barrier assignment).
3. **EP-06a** [Analogy-validation pack] — EPR monitoring or radical clock substrate to exclude Ni(I)/Ni(III); validates or refutes the Pd→Ni mechanistic analogy. Advances RI-06 (CLA-1), prerequisite for RI-03.
4. **EP-03a** [Direct-observation / state-assignment pack] — Initial-rate measurements or Hammett plot from Table 3 ArBr data to determine rate law and rate-limiting step. Advances RI-03 (SRG-1), pivotal for VQ-3.

Certification-gate note: investment order (EP-02a → EP-01a → EP-06a → EP-03a) follows information gain and logical precedence, but the final certification follows the fixed gate order VQ-1 → VQ-2 → VQ-3 → VQ-4.

---

**Objective function 2: VQ-4 (Benchmark) — prerequisite: VQ-3 achieved**

**Shortest route to VQ-4:**
1. **EP-09a** [Internal benchmark pack] — Single GC run of [NiCl₂(dppp)] at ArBr/2 = 50,000, 100°C, dioxane; report activation-fraction-corrected per-site TOF from EP-02a outcome. Advances RI-09 (SRG-7) and RI-08 (SRG-3).
2. **EP-08a** [Replication / uncertainty pack] — Isolated yields for entries 1, 9, 13; per-substrate homocoupling % for entries 8 and 12. Advances RI-08 (SRG-6).
3. **EP-07a** [Boundary-test pack] — Test [NiCl₂(dppp)] with bromomesitylene; test 2,6-dimethylbromobenzene to bound the "congested ArBr" scope claim. Advances RI-07 (SRG-7/CLA-2).

Certification-gate note: the experimental investment order follows information gain, but the final certification is fixed by the gate order VQ-1 → VQ-2 → VQ-3 → VQ-4.

---

### §6 Contribution to institutional design

**1. PRI-10 (Kinetic overclaim) — primary representative case confirmed:**
Monnereau 2009 is the primary case for PRI-10. The headline TOF claim (21,250 h⁻¹; "outperforms the fastest diphosphine-based catalysts reported") rests solely on GC conversion at a fixed time point — no initial rates, no activation parameters, no rate law. One additional paper confirming this pattern satisfies the two-paper criterion for PRI-10 promotion to full RI status.

**2. RI-03 + RI-06 co-occurrence pattern in Ni-catalysis mechanistic papers:**
SRG-1 exhibits structural co-occurrence of RI-03 (unobserved [Ni(Ar)(Ar')·1] intermediate) and RI-06 (Pd(0)/Pd(II) cycle imported for Ni without isomorphism demonstration). Resolving only RI-03 is insufficient: the experiment designed to observe or constrain the Ni(II) intermediate changes categorically depending on whether Ni(I)/Ni(III) is operative. Both RIs must be resolved simultaneously. This pattern is recorded as a case-specific extension of the RI-06 "cycle-level import" scope note: for Ni-catalysed cross-coupling papers importing Pd mechanistic frameworks, RI-03 + RI-06 co-occurrence is structurally predictable and should be flagged together in SRG construction.

**3. Labeling mismatch — moderate form detected:**
The mechanistic hypothesis appears once with an explicit hedge ("If one assumes…"); abstract and conclusions use modal factual verbs ("likely to rely on," "possibly facilitates"). The hypothesis label is concentrated at one location; the conclusions adopt a softer factual register that still signals a concluded mechanism. This is a moderate labeling mismatch (weaker than pure factual-verb use) co-occurring with RI-06 import. Added to the labeling mismatch case library.

**4. EP-04a case-specific implementation — negative regiochemical result as implicit kinetic discriminator:**
B-5 (2-bromotoluene 1760 h⁻¹ ≈ 3-bromotoluene 1810 h⁻¹; ortho steric suppression absent) provides an EP-04a case-specific implementation: [REDACTED: substantial verbatim quotation; see Tier 9] Added to the EP dictionary.

**5. EP-10a inaugural case-specific entry for dynamic-ligand Ni systems:**
Monnereau 2009 provides the first EP-10a (Kinetic verification pack, provisional) implementation for conformationally dynamic organometallic catalysts: [REDACTED: substantial verbatim quotation; see Tier 9] Recorded as the representative calixarene/Ni case for EP-10a.

---

> **Tier 8 redaction notice**: This file is a redacted copy of the corresponding Tier 3 / Tier 9 output. Verbatim source-paper quotations have been replaced by `[REDACTED: see source paper §<loc>; full text retained in Tier 9 reviewer-only deposit]` markers, preserving location references and our own analytical content. Bibliographic fields (title, authors, journal, year, DOI), analytical labels (`evidence_chain:` with B-/U-/A-/C- internal IDs), short technical terms, and our own analytical text are not redacted. The redaction was applied by `scripts/redact_for_tier8.py` and, for this version, by `scripts/build_paperA_R1_public.py` with `scripts/redact_source_ngram_runs.py` (scripts of the project repository; they are not deposited).
