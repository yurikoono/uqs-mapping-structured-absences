```
prompt_version: stage1-v16.1-20260414
model_info: claude-sonnet-4-6

target_title:   Regiocontrol in the oxidative Heck reaction of indole by ligand-enabled switch of the regioselectivity-determining step
target_authors: Yu-Jie Wang, Chen-Hui Yuan, De-Zhao Chu and Lei Jiao
target_start:   page 1: [REDACTED: paper boundary quote; see Tier 9]
target_end:     end of document

[Agent fields]
V1: Synthetic organic chemistry / Pd(II)-catalyzed C–H functionalization — generates questions about yield reporting, selectivity ratios, scope limitations, and byproduct accounting.
V2: Mechanistic / physical organic chemistry — generates questions about kinetic validity of quasi-reversibility claim, KIE interpretation, and evidentiary basis for step assignments.
V3: Computational chemistry / theoretical methods — generates questions about DFT methodology (functional, dispersion, solvation, conformational sampling) absent from main text.

[A] A-1 | P6 (Scheme 5b)* | [REDACTED: substantial verbatim quotation; see Tier 9] | deferred | mixed_detail: deferred/forgotten — the faster C2-deuteration in the catalytic reaction vs. the independent labeling is noted but explicitly unresolved; the paper proposes a tentative hypothesis (ref 24) but closes without returning to it | T1 | linked_to: B-4 | cross_field_temperature: n/a

[A] A-2 | P7 (Conclusion)* | [REDACTED: substantial verbatim quotation; see Tier 9] | deferred | mixed_detail: n/a | T1 | linked_to: B-5 | cross_field_temperature: n/a

[A] A-3 | P7 (Section 2.3, kinetics)* | [REDACTED: substantial verbatim quotation; see Tier 9] | deferred | mixed_detail: n/a | T1 | linked_to: B-6, B-7 | cross_field_temperature: n/a

[B] B-1 | P6 (Table 2 footnote)* | [REDACTED: substantial verbatim quotation; see Tier 9] | reporting_omission | rhetorical_function: Footnote specifying which products were isolated, presented as a procedural clarification. | note: C2:C3 selectivity ratios are not reported for any individual substrate entry in the scope table; the minor C3 co-product yield is not quantified; this prevents evaluation of selectivity consistency across the substrate series. Flag: metric incompleteness (GC vs isolated yield across tables). | cross_field_temperature: V1=high; convergence=1/3

[B] B-2 | P5 (Table 1 footnote a)* | [REDACTED: substantial verbatim quotation; see Tier 9] | reporting_omission | rhetorical_function: Standard table footnote describing analytical methods used for yield determination. | note: No correlation between NMR yield and isolated yield is provided; the two tables (optimization Table 1 vs. scope Table 2) use different metrics without explanation. Flag: metric incompleteness. | cross_field_temperature: V1=medium; convergence=1/3

[B] B-3 | P3 (Section 2.1, Scheme 2b)* | [REDACTED: substantial verbatim quotation; see Tier 9] | reporting_omission | rhetorical_function: Statement of DFT-computed activation energy barriers presented as evidence for C3-selectivity. | note: DFT methodology (functional, basis set, dispersion, solvation) is entirely absent from the main text. The barrier difference of 4.9 kcal mol⁻¹ predicts a selectivity ratio of ~4000:1 at 70 °C, which is inconsistent with typical experimental C3-selectivities; this discrepancy is unacknowledged. SRG-1, SRG-2. | cross_field_temperature: V1=medium(Q10), V3=critical(OV1); convergence=2/3; temperature_gap=medium

[B] B-4 | P6 (Scheme 5b)* | [REDACTED: substantial verbatim quotation; see Tier 9] | mixed | rhetorical_function: Observation framed as evidence consistent with the proposed reaction mechanism. | note: The anomalous faster C2-deuteration under catalytic vs. labeling conditions is noted but not explained. The paper moves away from this tension via a tentative hypothesis (footnote 24) without returning to it. intentional_narrowing: the observation is reframed as "consistent with" mechanism without testing the hypothesis. methodological_limitation: the independent labeling experiment uses different conditions from the catalytic reaction (absence of acrylate). linked_to: A-1. | cross_field_temperature: V1=medium(Q8), V2=high(OV3); convergence=2/3; temperature_gap=low

[B] B-5 | P7 (Section 2.4)* | [REDACTED: substantial verbatim quotation; see Tier 9] | methodological_limitation | rhetorical_function: Scope limitation stated as a factual constraint on the reaction. | note: No yields are given for disubstituted olefins; "rather low reactivity" is not quantified. No C2-selectivity data under these conditions is reported. Flag: negative result as evidence. linked_to: A-2. | cross_field_temperature: V1=low; convergence=1/3

[B] B-6 | P6 (Scheme 8)* | [REDACTED: substantial verbatim quotation; see Tier 9] | mixed | rhetorical_function: Stoichiometric trapping experiment presented as direct evidence for C2-insertion under SOHP conditions. | note: The C2:C3 ratio in the norbornene trapping (3:1) is substantially lower than the C2-selectivity in the catalytic reaction. intentional_narrowing: the paper describes this as "direct evidence" without acknowledging the selectivity discrepancy. methodological_limitation: norbornene insertion reversibility is acknowledged but thermodynamic control is ruled out by only a one-directional experiment (C3→C2 not observed; C2→C3 not tested). SRG-4. linked_to: A-3. | cross_field_temperature: V1=high(Q11), V2=high(OV2); convergence=2/3; temperature_gap=none

[B] B-7 | P7 (Section 2.3, kinetics)* | [REDACTED: substantial verbatim quotation; see Tier 9] | reporting_omission | rhetorical_function: Conclusion from kinetic data presented as mechanistic finding. | note: No rate constants are reported; no quantitative kinetic model is fitted to the saturation-kinetics data; the assertion that "neither step is rate-limiting" is not supported by a quantitative criterion. Flag: negative result as evidence. SRG-2. | cross_field_temperature: V2=high(Q2); convergence=1/3

[B] B-8 | P7 (Section 2.4, NH-indoles)* | [REDACTED: substantial verbatim quotation; see Tier 9] | methodological_limitation | rhetorical_function: Limitation on substrate scope framed as an acknowledged constraint. | note: The oxidation products are not characterized; yields are not given for the oxidation pathway. | cross_field_temperature: V1=medium(Q6); convergence=1/3

[B] B-9 | P8 (Fig. 2 description)* | [REDACTED: substantial verbatim quotation; see Tier 9] | reporting_omission | rhetorical_function: Clarification that the figure displays only part of the full energy surface for presentation purposes. | note: The C3-pathway energy values under SOHP conditions are not given in the main text; the quantitative basis for the C3-palladation barrier under SOHP (15.3 kcal mol⁻¹) is stated but the full C3-SOHP surface (TS-2a, C3-insertion, β-hydride elimination) energies are absent. SRG-1. | cross_field_temperature: V3=high(Q2); convergence=1/3

[B] B-10 | P5 (Section 2.3)* | [REDACTED: substantial verbatim quotation; see Tier 9] | reporting_omission | rhetorical_function: Comparison of pre-formed vs. in-situ complex framed as indirect evidence about the precatalyst identity. | note: The resting-state Pd species under catalytic conditions is not characterized; the DFT calculations start from PdCl₂·L13 which may not reflect the actual resting state. | cross_field_temperature: V1=high(Q7), V2=critical(OV1); convergence=2/3; temperature_gap=low

[C] C-1 | P3 (Introduction)* | ref 6a (Campbell, Meyer, Stahl, Chem. Commun. 2011) | Cited as prior example of ligand-dictated C3-/C2-selectivity switch in indole arylation using DAF ligand | reason_severed: DAF (L3) is tested in the present paper and gives C3-selectivity, but no comparison to ref 6a's arylation system is drawn; "first time" claim for alkenylation depends on this distinction | affects_claims: yes — the novelty claim requires distinguishing alkenylation from arylation but no explicit comparison is made | symmetric_pattern: no

[C] C-2 | P3 (Introduction)* | refs 9a, 9b (Sanhueza et al. 2013; Jackson and Montgomery 2015) | Cited as prior rare examples of regiocontrol by switch of regioselectivity-determining step | reason_severed: Cited only to establish rarity; no mechanistic comparison to the present system | affects_claims: medium — novelty rests partly on rarity claim | symmetric_pattern: yes

[C] C-3 | P3 (Section 2.1)* | ref 18 (Zhang et al., Org. Biomol. Chem. 2016) | Prior DFT study of the same ligand-free reaction | reason_severed: No numerical comparison of barrier values between ref 18 and the present paper's Scheme 2 | affects_claims: medium — the claim that present study discloses new mechanistic information is asserted without quantitative comparison | symmetric_pattern: no

[C] C-4 | P3 (Introduction)* | ref 13e (Grimster et al. 2005) | Source of "established ligandless conditions" and mechanistic picture for C3-selective oxidative Heck reaction | reason_severed: The mechanistic picture from ref 13e is accepted without independent verification | affects_claims: yes — baseline mechanistic claim depends on ref 13e's picture | symmetric_pattern: no

[C] C-5 | P3 (Introduction)* | refs 2, 3, 4 (DG, template, intrinsic regiocontrol) | Background citations for three classical regiocontrol modes | reason_severed: No experimental comparison showing these strategies fail on present substrates | affects_claims: yes/medium — the alternative mode claim implies classical strategies are insufficient here | symmetric_pattern: yes

[C] C-6 | P8 (Section 2.3)* | ref 25 (Wang and Carrow, ACS Catal. 2019) | Only cited precedent for quasi-reversible KIE scenario | reason_severed: No quantitative comparison of KIE values or kinetic profiles between thiophene and indole systems | affects_claims: yes — this is the only cited analogy for the quasi-reversible interpretation; non-comparison leaves it unsupported | symmetric_pattern: no

[U] U-1 | P6 (Scheme 5a)* | [REDACTED: substantial verbatim quotation; see Tier 9] | Why does the C2-alkenylation product 3b show deuterium incorporation at C3? | V2 | high | note: self-contradictory absence — the paper's proposed C2-palladation/C2-insertion pathway predicts no deuterium at C3 of product 3b; the observation is recorded without explanation or acknowledgment as potential counter-evidence.

[U] U-2 | P6 (Scheme 6)* | [REDACTED: substantial verbatim quotation; see Tier 9] | What is the quantitative kinetic framework that makes KIE ≈ 3.5 compatible with reversible C–H activation? | V2/V3 | critical | note: self-contradictory absence — the paper's proposed quasi-reversible mechanism predicts a partial/attenuated KIE; a KIE of 3.5 is quantitatively inconsistent with reversibility unless the partitioning between forward and back reaction is specified. The paper acknowledges the contradiction but provides no model to resolve it.

[U] U-3 | P5 (Table 1 general)* | [REDACTED: substantial verbatim quotation; see Tier 9] | What is the complete mass balance of the reaction accounting for all identified and unidentified byproducts? | V1 | high | note: Total of reported yields in Table 1 entries leaves ~20–25% unaccounted under optimal conditions; aerobic conditions and multiple byproduct pathways (3c, 3d, oxidation) make mass balance non-trivial; absence is not acknowledged.

[META]
  linked_items: [A-1↔B-4, A-2↔B-5, A-3↔B-6, A-3↔B-7, B-10↔B-3]
  same_root_groups:
    SRG-1 (DFT methodology absent from main text): B-3, B-9 — shared root: all DFT computational parameters deferred to ESI; energy values cannot be independently evaluated
    SRG-2 (Quasi-reversibility without quantitative kinetic framework): U-2, B-7, A-3 — shared root: the paper's central mechanistic claim (quasi-reversible palladation) lacks a quantitative kinetic model
    SRG-3 (Selectivity metric asymmetry): B-1, B-2 — shared root: C2:C3 selectivity ratios systematically absent across optimization and scope tables
    SRG-4 (Norbornene stoichiometric vs. catalytic selectivity discrepancy): B-6 — shared root: stoichiometric trapping gives lower selectivity than catalytic system without explanation
    SRG-5 (Mass balance / byproduct accounting): B-1, U-3 — shared root: quantitative byproduct accounting absent
  symmetric_citations: [C-2 (refs 9a, 9b), C-5 (refs 2, 3, 4)]
  unreported_data: [C2:C3 ratios for Table 2 entries; ΔG‡ values for C3-pathway under SOHP from Fig. 2; rate constants from kinetic experiments; yields of 3c and 3d in scope table; isolated yields for Scheme 9 products 23 and 24; complete mass balance]
  series_signal: no

[TEMPERATURE_SUMMARY]
  high_convergence_high_gap: [B-3 (V1=medium, V3=critical; convergence=2/3; temperature_gap=medium)]
  high_convergence_low_gap: [B-4 (V1=medium, V2=high; convergence=2/3; gap=low), B-6 (V1=high, V2=high; convergence=2/3; gap=none), B-10 (V1=high, V2=critical; convergence=2/3; gap=low), U-2 (V2=critical, V3=critical; convergence=2/3; gap=none)]
  low_convergence_high_gap: [U-2 (V2=critical; also V3-OV2=critical — both independently critical before overlap counted)]

[GAP] GAP-1 | type 2 | high | DFT study of the same ligand-free reaction (ref 18: Zhang et al. Org. Biomol. Chem. 2016) — numerical barrier comparison needed to validate present paper's Scheme 2 model | Zhang et al., Org. Biomol. Chem. 2016, 14, 4146 | T1 | pending

[GAP] GAP-2 | type 3 | high | Quantitative kinetic partitioning model for quasi-reversible C–H activation with significant apparent KIE (ref 25: Wang and Carrow, ACS Catal. 2019) — needed to evaluate U-2 | Wang and Carrow, ACS Catal. 2019, 9, 6821 | T1 | pending

[GAP] GAP-3 | type 1 | medium | Ref 13e (Grimster et al. 2005) — "established ligandless conditions" baseline whose mechanistic picture underpins Scheme 2 | Grimster et al., Angew. Chem. Int. Ed. 2005, 44, 3125 | T1 | pending

inference_time_sec: not available — inject externally
```

---

> **Tier 8 redaction notice**: This file is a redacted copy of the corresponding Tier 3 / Tier 9 output. Verbatim source-paper quotations have been replaced by `[REDACTED: see source paper §<loc>; full text retained in Tier 9 reviewer-only deposit]` markers, preserving location references and our own analytical content. Bibliographic fields (title, authors, journal, year, DOI), analytical labels (`evidence_chain:` with B-/U-/A-/C- internal IDs), short technical terms, and our own analytical text are not redacted. The redaction was applied by `scripts/redact_for_tier8.py` and, for this version, by `scripts/build_paperA_R1_public.py` with `scripts/redact_source_ngram_runs.py` (scripts of the project repository; they are not deposited).
