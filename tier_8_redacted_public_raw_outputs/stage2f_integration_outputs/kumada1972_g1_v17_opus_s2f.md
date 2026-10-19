prompt_version: stage2f-v6-20260329

group: G1 — 直系継承 (Direct Lineage)
papers: Kumada 1972 (JACS Communication), Kumada 1976b (BCSJ Full Paper), Mazet 2021 (ACS Catalysis)
model_info: claude-opus-4-6

---

[F] Within-Group Comparison

---

## repeated_patterns

**RP-1: Catalytic cycle proposed without stoichiometric step validation in the actual catalytic system**

All three papers propose Ni(0)/Ni(II) catalytic cycles for diphosphine-Ni catalyzed cross-coupling, but none validates every elementary step under catalytic conditions in the system actually used for synthesis.

- Kumada 1972: Catalytic cycle (eqs 2–4) constructed from stoichiometric reactions on dipy-Ni and non-dpe-Ni systems (refs 11–13); no intermediate isolated or observed in the NiCl₂(dpe) system (B-2, B-14).
- Kumada 1976b: Scheme 1 explicitly acknowledged as not fully clarified ([REDACTED: substantial verbatim quotation; see Tier 9]); based on same external analogy (refs 30–32, C3); Morrell/Kochi (ref 46, C4) cited as "essentially consistent" without reproducing specific results.
- Mazet 2021: Several intermediates independently synthesized and characterized (6c/6d, 7c/7d, 9c), but the transmetalation product IV is never observed (B11), the dmpe resting state is unidentified (B8), and the key bimolecular transmetalation hypothesis rests on indirect kinetic evidence with acknowledged reliability limitations (B1, U3).

```
evidence_chain: Kumada_1972 : B-2, B-14 ; Kumada_1976b : A2, C3, C4 ; Mazet_2021 : B8, B11, U3
```

**RP-2: Quantitative analytical basis for yield data undercharacterized or internally inconsistent**

All three papers report yield data whose analytical foundations are incompletely specified or internally problematic.

- Kumada 1972: glpc conditions absent (B-4); yield basis inconsistent between Examples 1 and 2 (B-12); "and/or" characterization qualifier (B-13).
- Kumada 1976b: GLPC instrument conditions partially stated but temperature/carrier gas/detector absent (B4); calibration method unstated for novel products (B5); internal standard identity inconsistent (B9); yield > conversion mathematical impossibility in Table 3 (U3).
- Mazet 2021: NMR yields without uncertainty estimates across scope table (B17); "excellent mass balance" stated qualitatively without numerical value (B14); no replicate runs cited for any scope entry (B17).

```
evidence_chain: Kumada_1972 : B-4, B-12, B-13 ; Kumada_1976b : B4, B5, B9, U3 ; Mazet_2021 : B14, B17
```

**RP-3: Homo-coupling / mass balance data systematically absent**

The selectivity claim central to all three papers is never quantitatively benchmarked against the principal competing pathway.

- Kumada 1972: "Selective" is the title keyword, yet no homo-coupling product (R–R) is reported despite the proposed mechanism (eq 3) predicting its formation (B-1, U-1).
- Kumada 1976b: Benzene formation (homo-coupling index) reported selectively — quantified for some Table 3 entries but "not determined" for others (B7); dihaloethylene reactions described as giving "homo coupling product of the Grignard reagent predominating" but without product identities or yields (B2).
- Mazet 2021: No homo-coupling product quantification or mass balance reported for catalytic reactions; mass balance claimed as "excellent" for stoichiometric NMR experiments only (B14), but without numerical values.

```
evidence_chain: Kumada_1972 : B-1, U-1 ; Kumada_1976b : B2, B7 ; Mazet_2021 : B14
```

**RP-4: Competing catalyst systems cited but not numerically benchmarked**

Each paper positions itself against prior or parallel catalyst systems without substrate-matched quantitative comparison.

- Kumada 1972: Tamura-Kochi Fe/Cu catalysts and Corriu/Masse Ni(acac)₂ cited without yield comparison (C-1, C-3).
- Kumada 1976b: Fe/Ag/Cu catalysts (C1) and Murahashi Pd-phosphine (C2) cited without matched-pair comparison.
- Mazet 2021: Saper/Hartwig NHC-Ni mechanistic study (C4) cited for Ni(0)/Ni(II) precedent without comparing mechanistic observables (resting state, RDS, catalyst order).

```
evidence_chain: Kumada_1972 : C-1, C-3 ; Kumada_1976b : C1, C2 ; Mazet_2021 : C4
```

**RP-5: Ligand effect attribution without multi-variable deconvolution**

All three papers attribute catalyst performance differences to specific ligand properties without experimentally separating confounded variables.

- Kumada 1972: Ligand activity order attributed to cis-geometry requirement from a single substrate pair (B-3, U-4).
- Kumada 1976b: dppp > dppe preference unexplained ("hard to find valid reasons," A4); dmpe anomaly uninterpreted (A5).
- Mazet 2021: dppe/dmpe reactivity difference attributed to steric environment from a two-point comparison confounding steric, electronic, and bite-angle effects (B10).

```
evidence_chain: Kumada_1972 : B-3, U-4 ; Kumada_1976b : A4, A5 ; Mazet_2021 : B10
```

---

## temperature_patterns

```
temperature_pattern: RP-1 (mechanism without validation) | papers: [Kumada_1972, Kumada_1976b, Mazet_2021] | profile_consistency: divergent | note: Severity escalates across time — Kumada_1972 V2=critical for B-2, Kumada_1976b V2=critical for A2, while Mazet_2021 deploys multiple experimental tools yet the core issue (complete catalytic cycle validation) persists at B1 V1=V2=V3=high (convergence 3/4). The gap transforms from "absent for a communication" to [REDACTED: substantial verbatim quotation; see Tier 9]
```

```
temperature_pattern: RP-2 (analytical undercharacterization) | papers: [Kumada_1972, Kumada_1976b, Mazet_2021] | profile_consistency: consistent | note: V3-severity remains medium-to-high across all three papers (Kumada_1972 B-4 V3=medium; Kumada_1976b B4/B5 V3=high; Mazet_2021 B17 V3=medium). The specific analytical method changes (glpc → GLPC → NMR/IR) but the pattern of reporting yields without uncertainty, replication, or complete method specification persists unchanged.
```

```
temperature_pattern: RP-3 (mass balance absence) | papers: [Kumada_1972, Kumada_1976b, Mazet_2021] | profile_consistency: consistent | note: All three papers receive V1=high for selectivity-related omissions (Kumada_1972 B-1: V1=V2=V3=high, convergence 3/3; Kumada_1976b B2: convergence 3/3; Mazet_2021 B14: V3=medium, single agent). The gap persists at similar severity across 50 years despite the shift from synthetic to mechanistic study design.
```

---

## recurring_roots

```
recurring_root: Catalytic mechanism assembled from external analogy rather than internal experimental validation | papers: [Kumada_1972, Kumada_1976b, Mazet_2021] | member_items: Kumada_1972: SRG-1 (B-2, B-14, U-1, U-2, U-4); Kumada_1976b: SRG-1 (A2, A6, A8, U1, U2, C3, C4); Mazet_2021: SRG-2 (B1, B8, U1, U3) | note: This is a structural gap that transforms across 54 years but never fully closes. In 1972 and 1976, the mechanism rests entirely on analogy to other Ni systems. By 2021, several intermediates are characterized, but the cycle as a whole — particularly the dmpe bimolecular transmetalation — retains structural dependence on indirect evidence. The root is structural (complete cycle validation requires a different scale of experimental investment) rather than individually chosen.
```

```
recurring_root: Yield/selectivity data without quantitative analytical foundation | papers: [Kumada_1972, Kumada_1976b, Mazet_2021] | member_items: Kumada_1972: SRG-3 (B-4, B-8, B-9, B-12, B-13); Kumada_1976b: SRG-3 (B4, B5, B9, U3, B7, B8); Mazet_2021: SRG-6 (B13, B14, B15, B17) | note: Genre convention — yield reporting norms in organometallic chemistry tolerate qualitative or semi-quantitative analytical statements across journals (JACS, BCSJ, ACS Catalysis) and decades (1972–2021). This is a field-wide convention, not a paper-specific choice.
```

```
recurring_root: Ligand-effect attribution from under-determined data | papers: [Kumada_1972, Kumada_1976b, Mazet_2021] | member_items: Kumada_1972: B-3, U-4; Kumada_1976b: A4, A5; Mazet_2021: SRG-4 (B10, C3) | note: Structural gap — deconvoluting steric, electronic, and geometric contributions of phosphine ligands requires systematic ligand libraries that exceed the scope of any single paper. Each paper attributes effects to a single variable (Kumada_1972: cis-geometry; Kumada_1976b: unstated; Mazet_2021: steric environment) without multi-variable control.
```

---

## suppression_diagnostic

| Pattern | Diagnostic | Reasoning |
|---------|-----------|-----------|
| RP-1 (mechanism without validation) | Structurally suppressed → individually chosen (evolving) | In 1972–1976, complete catalytic cycle validation required techniques (low-T NMR, radical clocks, VTNA) not yet standard — structurally suppressed. By 2021, these tools are available and deployed, but incompletely applied (dmpe resting state unidentified, VTNA lacking goodness-of-fit) — the residual gap is individually chosen. |
| RP-2 (analytical undercharacterization) | Genre convention | The level of analytical detail reported matches journal norms across all three eras. No paper deviates from the expected reporting standard of its venue, suggesting the gap is convention-driven rather than individually chosen. |
| RP-3 (mass balance absence) | Individually chosen | Mass balance measurement was technically feasible in all three eras (glpc/GLPC/NMR can detect byproducts). The consistent omission across 50 years suggests that the field treats selectivity as a qualitative descriptor rather than a quantitative metric — an active, recurring choice. |
| RP-4 (benchmark absence) | Individually chosen | Each paper had access to the prior/competing systems' published data and could have performed matched-pair comparisons. The omission is strategic positioning, not structural limitation. |
| RP-5 (ligand effect attribution) | Structurally suppressed | Multi-variable ligand deconvolution requires systematic ligand libraries that exceed the scope of any single paper and require collaborative or high-throughput approaches. |

---

## paradigm_competition

This group reveals **paradigm succession** rather than paradigm competition. The three papers represent three successive paradigms for understanding Ni-phosphine cross-coupling:

**Paradigm 1: Empirical method development (Kumada 1972)**
- Goal: Demonstrate that Ni-phosphine complexes catalyze selective cross-coupling.
- Systematically unanswered: What is the mechanism? (answered partially by Paradigm 2, substantially by Paradigm 3)
```
evidence_chain: Kumada_1972 : B-2 ("working hypothesis"); Kumada_1972 : A-2 ("further studies required")
```

**Paradigm 2: Scope mapping (Kumada 1976b)**
- Goal: Define the substrate scope and identify the best catalyst for each substrate class.
- Systematically unanswered: Why does each catalyst-substrate combination succeed or fail? Why the anomalous halide reactivity order? Why the dmpe/secondary alkyl isomerization?
```
evidence_chain: Kumada_1976b : A2 ("mechanism not yet fully clarified"); Kumada_1976b : A3 ("strange behavior"); Kumada_1976b : A5 ("hard to find valid reasons"); Kumada_1976b : U2 (β-elimination/isomerization self-contradiction)
```

**Paradigm 3: Mechanistic elucidation (Mazet 2021)**
- Goal: Characterize intermediates, determine rate laws, and propose complete catalytic cycles.
- Systematically unanswered: What are the quantitative kinetic parameters (activation energies, rate constants)? What controls E/Z selectivity? What is the dmpe resting state?
```
evidence_chain: Mazet_2021 : A2 (activation parameters forgotten); Mazet_2021 : A1, B12 (E/Z selectivity origin unaddressed); Mazet_2021 : B8 (dmpe resting state unidentified)
```

The relationship is sequential: Paradigm 1's blind spot (mechanism) becomes Paradigm 2's acknowledged deferral ("While much remains to be studied"), which becomes Paradigm 3's founding problem. Each paradigm's unanswered questions are precisely the next paradigm's entry point. This is paradigm succession, not competition — no two paradigms coexist in tension over the same question at the same time.

**Critical observation**: Paradigm 3 (Mazet 2021) does not close Paradigm 1's original gaps. The original Kumada 1972 question — [REDACTED: substantial verbatim quotation; see Tier 9] (D4-1, SRG-2 in Kumada 1972) — remains unanswered in 2021. The paradigm succession advances the depth of mechanistic understanding while leaving the foundational selectivity quantification untouched.

---

## divergences

**DV-1: Substrate class — sp² halides (1972/1976) vs. enol phosphates (2021)**

Kumada 1972 and 1976b use aryl/vinyl halides as electrophilic partners; Mazet 2021 uses enol phosphates. This substrate shift introduces the phosphate/bromide ion exchange step (Mazet 2021 B7, U2) that has no precedent in the halide-based systems.

```
evidence_chain: Kumada_1972 : B-5 ("Only Csp² halides"); Mazet_2021 : B7 ("rapid phosphate/bromide ion exchange")
```

Accounts for divergence: Subfield evolution — C(sp²)–O electrophile cross-coupling emerged as a distinct field post-2000, driven by cost and environmental advantages of enol phosphates over aryl halides. The divergence reflects journal and subfield norms (2021 ACS Catalysis vs. 1972 JACS/1976 BCSJ).

**DV-2: Experimental depth — qualitative assertions (1972) vs. tabular scope (1976) vs. stoichiometric/kinetic characterization (2021)**

The evidentiary standard escalates across the three papers: Kumada 1972 asserts mechanistic claims without data; Kumada 1976b maps scope without mechanism; Mazet 2021 deploys NMR/X-ray/VTNA/radical probes.

```
evidence_chain: Kumada_1972 : B-2 (mechanism from analogy); Kumada_1976b : A2 (mechanism deferred); Mazet_2021 : B1 (VTNA kinetic data, albeit with limitations)
```

Accounts for divergence: Year (1972 → 1976 → 2021), journal format (communication → full paper → full paper with SI), and the maturation of available experimental techniques (low-T NMR, VTNA, radical clocks became standard tools).

**DV-3: MgX₂ byproduct — invisible (1972) → predicted but uncharacterized (1976) → unaddressed (2021)**

Kumada 1972 does not discuss MgXX'. Kumada 1976b predicts MgXX' stoichiometrically but never characterizes it (U1). Mazet 2021 does not address MgBr₂ accumulation or its potential catalytic role, despite deploying kinetic methods where salt effects could confound rate measurements.

```
evidence_chain: Kumada_1972 : "no textual basis in Kumada_1972" (retrospective — the 1972 paper does not discuss MgXX'); Kumada_1976b : U1 (MgXX' predicted but uncharacterized); Mazet_2021 : "no textual basis in Mazet_2021" (retrospective — MgBr₂ accumulation not discussed despite VTNA analysis)
```

Accounts for divergence: The MgXX' gap is invisible in 1972 (communication format), acknowledged structurally in 1976 (stoichiometric equation implies it), and remains invisible in 2021 — the gap re-submerges when the paradigm shifts from scope mapping to mechanistic elucidation. This is an example of a gap that becomes visible in one paradigm and disappears in the next, not because it was resolved, but because it falls outside the new paradigm's scope.

---

## recurring_U

```
recurring_U: Self-contradictory absence between proposed mechanism and absent byproduct/observation data | papers: [Kumada_1972, Kumada_1976b, Mazet_2021] | item_ids: [Kumada_1972: U-1, U-2; Kumada_1976b: U1, U2; Mazet_2021: U1, U3] | note: All three papers contain observations or predictions within their own text that are inconsistent with their own conclusions but pass without acknowledgment. Kumada_1972: eq 3 predicts R–R but R–R is unreported (U-1); black mixture consistent with heterogeneous catalysis but homogeneous cycle proposed (U-2). Kumada_1976b: MgXX' predicted but uncharacterized (U1); isomerization contradicts β-suppression claim (U2). Mazet_2021: stoichiometric experiment yields consistent with statistical scrambling rather than selective interception (U1); VTNA reliability disclaimed yet used as primary mechanistic evidence (U3). This recurring pattern — where papers generate internal predictions that go untested — may indicate a systematic gap in the A/B/C framework: the framework captures "what is absent" (B) and "what is deferred" (A) but does not have a dedicated category for "what the paper's own logic predicts but the paper fails to test."
```

---

## group_unasked_question

[REDACTED: substantial verbatim quotation; see Tier 9]

```
evidence_chain: Kumada_1972 : B-1 (selectivity unquantified), U-1 (R–R predicted but unreported); Kumada_1976b : B2 (homo-coupling observed but uncharacterized), B7 (benzene not determined for key entries), U1 (MgXX' uncharacterized); Mazet_2021 : B14 (mass balance qualitative), U1 (stoichiometric experiment ambiguous), B1 (VTNA unreliable for catalyst order)
```

TEMPERATURE_SUMMARY correspondence: The group-level unasked question corresponds to Kumada_1972's high_convergence_low_gap item B-1 (convergence 3/3, V1=V2=V3=high) and Kumada_1976b's B2 (convergence 3/3). In Mazet_2021, the question transforms into the mass-balance and byproduct dimension (B14, single agent V3=medium) — the severity drops because the 2021 paper is a mechanistic study rather than a synthetic scope study, but the underlying gap persists.

recurring_root correspondence: This group-level question integrates the recurring root [REDACTED: substantial verbatim quotation; see Tier 9] with "Yield/selectivity data without quantitative analytical foundation." The selectivity question cannot be answered without both mechanistic understanding (which pathway produces homo-coupling) and analytical rigor (quantitative mass balance). The 54-year persistence of this gap reflects the structural interdependence of these two roots.

---

> **Tier 8 redaction notice**: This file is a redacted copy of the corresponding Tier 3 / Tier 9 output. Verbatim source-paper quotations have been replaced by `[REDACTED: see source paper §<loc>; full text retained in Tier 9 reviewer-only deposit]` markers, preserving location references and our own analytical content. Bibliographic fields (title, authors, journal, year, DOI), analytical labels (`evidence_chain:` with B-/U-/A-/C- internal IDs), short technical terms, and our own analytical text are not redacted. The redaction was applied by `scripts/redact_for_tier8.py` and, for this version, by `scripts/build_paperA_R1_public.py` with `scripts/redact_source_ngram_runs.py` (scripts of the project repository; they are not deposited).
