prompt_version: stage2f-v6-20260329

group: G2 — 境界突破 (Boundary Breakthrough)
papers: Kumada 1972 (JACS Communication), Breitenfeld 2014 (Organometallics), Cherney 2015 (Chemical Reviews), Pengfei 2024 (Nature Catalysis)
model_info: claude-opus-4-6

---

[F] Within-Group Comparison

---

## repeated_patterns

**RP-1: Mechanistic proposals exceeding their experimental basis**

All four papers propose catalytic cycle mechanisms whose completeness exceeds the direct experimental evidence provided.

- Kumada 1972: Ni(0)/Ni(II) cycle (eqs 2–4) from analogy to other Ni systems; no intermediate characterized in NiCl₂(dpe) system (B-2, B-14).
- Breitenfeld 2014: "Complete catalytic cycle" (Figure 8) with seven intermediates (10–16), none observed or characterized; bimetallic OA selected over escape-rebound solely by DFT (U-3); rate law derivation absent (U-2).
- Cherney 2015: DYKAT invoked as standard mechanism for enantioselective coupling throughout Sections 2.1–2.2 without krac/kproductive verification (B-1); DET proposed computationally without conversion-ee validation (U-1).
- Pengfei 2024: Ni(I/II/III) radical cycle proposed with Path I / Path II ambiguity unresolved (A-1, U-1); DFT potentials disagree with SWV by 360 mV (U-2, B-13).

```
evidence_chain: Kumada_1972 : B-2, B-14 ; Breitenfeld_2014 : U-1, U-2, U-3 ; Cherney_2015 : B-1, U-1 ; Pengfei_2024 : A-1, U-1, U-2
```

**RP-2: Mass balance / byproduct data systematically absent**

The selectivity claim central to each paper's contribution is never quantitatively benchmarked against competing pathways across the full substrate scope.

- Kumada 1972: No homo-coupling (R–R) product reported despite eq 3 predicting it (B-1, U-1).
- Breitenfeld 2014: Kinetic rates measured but absolute rate constant unreported (B-7); product ratios averaged without individual replicates (B-6).
- Cherney 2015: Mass balance for low-yield early DYKAT reactions unreported (B-8); ee reported without conversion data making DYKAT/KR indistinguishable.
- Pengfei 2024: >90 substrates with isolated yields only; homo-coupling quantified only for Table 1 model reaction; TEMPO experiment 59% unaccounted (B-1, B-11).

```
evidence_chain: Kumada_1972 : B-1, U-1 ; Breitenfeld_2014 : B-6, B-7 ; Cherney_2015 : B-8 ; Pengfei_2024 : B-1, B-11, B-12
```

**RP-3: Competing systems cited without quantitative benchmarking**

- Kumada 1972: Tamura-Kochi Fe/Cu and Corriu/Masse Ni(acac)₂ cited without yield comparison (C-1, C-3).
- Breitenfeld 2014: Yamamoto Ni(0) biaryl coupling cited as transmetalation analogy without rate constant comparison (C-1); Kochi cage-rebound cited but DFT rather than experiment distinguishes pathways.
- Cherney 2015: Multiple prior catalyst systems cited without head-to-head comparison; Alexakis reviews used to exclude pre-2008 Cu literature without coverage verification (C-1).
- Pengfei 2024: Lin eXEC, Gong thermal XEC, photochemical approaches all cited without substrate-matched yield comparison (C-1, C-2, C-3).

```
evidence_chain: Kumada_1972 : C-1, C-3 ; Breitenfeld_2014 : C-1 ; Cherney_2015 : C-1 ; Pengfei_2024 : C-1, C-2
```

**RP-4: DFT calculations used as primary mechanistic discriminant without experimental validation**

- Kumada 1972: not applicable (no DFT in 1972).
- Breitenfeld 2014: DFT is the sole discriminant between bimetallic OA and escape-rebound; B1→B2 energy difference acknowledged as imprecise, yet used to draw mechanistic conclusion (B-5, U-3).
- Cherney 2015: DET classification based on computational study without experimental validation (U-1).
- Pengfei 2024: DFT redox potentials (B-4) and RE barriers (B-5) presented as mechanistic support; 360 mV discrepancy with SWV undiscussed (U-2).

```
evidence_chain: Breitenfeld_2014 : B-5, U-3 ; Cherney_2015 : U-1 ; Pengfei_2024 : B-4, B-5, U-2
```

**RP-5: Radical mechanism evidence incomplete for all substrate classes claimed**

- Kumada 1972: No radical pathway considered; Ni(0)/Ni(II) two-electron cycle assumed.
- Breitenfeld 2014: Radical probe experiments conducted at 0°C but catalytic reactions at RT; temperature discrepancy unaddressed (B-1).
- Cherney 2015: Radical OA proposed for Ni-catalyzed sp³ couplings but spectroscopic evidence for Ni(III) intermediates absent for most systems; "proof of concept" photoredox at 50% ee (B-6).
- Pengfei 2024: Racemization and TEMPO trapping established for secondary halides only; primary halide radical mechanism generalized without direct evidence (B-10, SRG-5).

```
evidence_chain: Kumada_1972 : "no textual basis" (retrospective — radical pathway not considered) ; Breitenfeld_2014 : B-1 ; Cherney_2015 : B-6 ; Pengfei_2024 : B-10, B-11, B-12
```

---

## temperature_patterns

```
temperature_pattern: RP-1 (mechanism exceeding evidence) | papers: [Kumada_1972, Breitenfeld_2014, Cherney_2015, Pengfei_2024] | profile_consistency: consistent | note: All papers show V2 (mechanistic) severity at high-to-critical levels: Kumada_1972 B-2 V2=critical; Breitenfeld_2014 U-3 convergence=3/3 all high; Cherney_2015 B-1 convergence=3/3 all high; Pengfei_2024 U-1 V2=high. The gap's severity is stable across 52 years despite the shift from two-electron to radical mechanisms, from sp² to sp³ substrates, and from thermal to electrochemical activation.
```

```
temperature_pattern: RP-2 (mass balance absence) | papers: [Kumada_1972, Breitenfeld_2014, Cherney_2015, Pengfei_2024] | profile_consistency: consistent | note: Kumada_1972 B-1 (V1=V2=V3=high, 3/3 convergence); Pengfei_2024 B-1 (3/3 convergence, all high). Mass balance as a gap is rated at the highest severity by all agents in both the original and most recent paper. The 52-year persistence of this gap at the same severity level is notable.
```

```
temperature_pattern: RP-4 (DFT as discriminant) | papers: [Breitenfeld_2014, Cherney_2015, Pengfei_2024] | profile_consistency: divergent | note: Breitenfeld_2014 explicitly acknowledges DFT imprecision but uses it anyway (B-5: V1=V2=high); Pengfei_2024 does not acknowledge the 360 mV DFT-SWV discrepancy at all (U-2: V2=medium, single agent). The gap's severity decreases in Pengfei_2024 despite a larger quantitative discrepancy — suggesting that the temperature_gap may be increasing (growing acceptance of DFT without validation in the field).
```

---

## recurring_roots

```
recurring_root: Catalytic cycle proposed as "complete" or "established[REDACTED: substantial verbatim quotation; see Tier 9]established" in Breitenfeld, "complete cycle" implied) exceeds what the evidence supports, making the rhetorical framing an individually chosen gap superimposed on a structural limitation.
```

```
recurring_root: Selectivity (cross vs homo) claimed qualitatively without quantitative byproduct accounting | papers: [Kumada_1972, Breitenfeld_2014, Pengfei_2024] | member_items: Kumada_1972: SRG-2 (B-1, U-1, C-1); Breitenfeld_2014: B-7 (no absolute rate constant); Pengfei_2024: SRG-1 (B-1, B-11, B-12, B-14, B-15) | note: Individually chosen — mass balance measurement is technically feasible by GC/GC-MS in all three eras. The persistent omission across 52 years and different research groups suggests a field-level norm: [REDACTED: substantial verbatim quotation; see Tier 9]
```

```
recurring_root: Computational evidence presented without adequate experimental validation or acknowledged uncertainty | papers: [Breitenfeld_2014, Cherney_2015, Pengfei_2024] | member_items: Breitenfeld_2014: SRG-1 (U-3, B-5, B-3); Cherney_2015: SRG-2 (U-1, U-3); Pengfei_2024: SRG-4 (B-4, B-5, B-13, U-2) | note: This root emerges only in post-2010 papers — it is an era-specific structural gap reflecting the rapid adoption of DFT as a mechanistic tool without concurrent development of validation protocols. The gap is becoming more entrenched: Breitenfeld_2014 acknowledges DFT imprecision (B-5), while Pengfei_2024 does not acknowledge a 360 mV discrepancy (U-2).
```

---

## suppression_diagnostic

| Pattern | Diagnostic | Reasoning |
|---------|-----------|-----------|
| RP-1 (mechanism exceeding evidence) | Individually chosen → structurally suppressed (evolving) | In 1972, intermediate characterization tools were limited — structurally suppressed. By 2014–2024, NMR, EPR, and in situ spectroscopy are available but not applied to the actual catalytic system — individually chosen. The DFT component (2014/2024) is individually chosen: authors can benchmark DFT against known quantities but do not. |
| RP-2 (mass balance absence) | Individually chosen | GC/GC-MS can detect and quantify byproducts in all four papers' eras and contexts. The omission persists as a field convention: synthetically focused papers define success by product yield, not by mass balance. |
| RP-3 (benchmark absence) | Individually chosen | Each paper had access to prior systems' published data. The omission is strategic: qualitative superiority claims are easier to defend than quantitative comparisons that might reveal substrate-specific trade-offs. |
| RP-4 (DFT as discriminant) | Individually chosen | DFT validation against experimental barriers (Eyring analysis) is standard practice; its absence is a choice. The choice is reinforced by publication incentives: an unvalidated DFT cycle is publishable, whereas a validated one that disagrees with the proposed mechanism is problematic. |
| RP-5 (incomplete radical evidence) | Mixed | Structurally suppressed for primary alkyl radicals (short-lived, difficult to trap); individually chosen for the generalization from secondary to primary without caveat. |

---

## paradigm_competition

This group reveals a genuine **paradigm competition** between two-electron and radical mechanisms for Ni-catalyzed cross-coupling, overlaid on a **paradigm succession** from sp² to sp³ substrates.

**Paradigm A: Two-electron Ni(0)/Ni(II) cycle (Kumada 1972, partially Cherney 2015)**
- Foundational mechanism for sp² cross-coupling
- Systematically unanswered: "Can this mechanism operate for sp³ substrates?" The answer is retrospectively NO — sp³ halides are too slow for concerted oxidative addition to Ni(0) — but Kumada 1972 does not ask this question; it frames the sp² restriction as a positive feature.
```
evidence_chain: Kumada_1972 : B-5 ("Only Csp² halides can be used") → "no textual basis in Kumada_1972" for why sp³ fails (retrospective gap)
```

**Paradigm B: Radical Ni(I)/Ni(III) cycle (Breitenfeld 2014, Pengfei 2024)**
- Enables sp³ substrates via SET-generated carbon radicals
- Systematically unanswered: "What determines cross-selectivity between two radical species?" Breitenfeld 2014 proposes bimetallic transmetalation (eq 3) without algebraic derivation (U-2); Pengfei 2024 defers the selectivity model to SI (B-3) and does not resolve Path I/II (A-1, U-1).
```
evidence_chain: Breitenfeld_2014 : U-2 (rate law not derived), B-2 ("redistribution[REDACTED: substantial verbatim quotation; see Tier 9]cannot be ruled out"), U-1 (Path I/II unresolved)
```

**Paradigm overlap (Cherney 2015):**
The review documents the transition zone where both paradigms coexist: enantioselective sp³ coupling via DYKAT assumes configurationally labile organometallics (Paradigm A logic), while radical OA mechanisms (Paradigm B logic) appear in the same substrate class. The review does not explicitly articulate this as a paradigm competition; instead, it treats the two mechanisms as alternative explanations for different reaction types.
```
evidence_chain: Cherney_2015 : B-1 (DYKAT invoked without krac/kproductive), B-6 (radical Ni/Ir photoredox as "proof of concept")
```

**Critical observation — paradigm succession with retained blind spots:**
Paradigm B (radical mechanism) was developed precisely to answer Paradigm A's blind spot (sp³ substrate limitation). However, Paradigm B inherits Paradigm A's mass balance blind spot (RP-2) without modification. Both paradigms claim "selectivity" without quantifying homo-coupling, and both propose "complete" cycles without characterizing all intermediates. The paradigm shift changed the catalytic mechanism but not the evidentiary standard for claiming selectivity.

---

## divergences

**DV-1: Substrate class — sp² halides (1972) → sp³ halides (2014/2024) → comprehensive review (2015)**

The group spans the most significant substrate boundary in cross-coupling: sp² vs sp³ electrophiles. Kumada 1972 restricts to sp²; Breitenfeld 2014 and Pengfei 2024 specifically target sp³; Cherney 2015 reviews both.

```
evidence_chain: Kumada_1972 : B-5 ("Only Csp² halides"); Breitenfeld_2014 : S0-1 ("alkyl−aryl Kumada coupling"); Pengfei_2024 : S0-1 ("C(sp3)–C(sp3) cross-coupling")
```

Accounts for divergence: This is the defining divergence of the group — the progression from sp² restriction to sp³ enablement constitutes the "boundary breakthrough" that organizes G2.

**DV-2: Mechanistic paradigm — two-electron (1972) → radical (2014/2024)**

Kumada 1972 proposes Ni(0)/Ni(II) oxidative addition; Breitenfeld 2014 establishes radical SET/Ni(I)/Ni(III); Pengfei 2024 proposes electrochemical Ni(I/II/III) radical cycle. The mechanistic shift is driven by the substrate class change: sp³ halides undergo SET more readily than concerted OA.

```
evidence_chain: Kumada_1972 : B-2 (Ni(0)/Ni(II) cycle); Breitenfeld_2014 : S0-1 ("bimetallic oxidative addition" via radical); Pengfei_2024 : S0-1 ("Ni(I/II/III) radical cycle")
```

Accounts for divergence: Subfield mechanistic evolution; the radical mechanism is a necessary consequence of extending coupling to sp³ electrophiles whose C–X bonds do not undergo concerted OA to Ni(0).

**DV-3: Activation mode — thermal (1972/2014) → electrochemical (2024)**

Kumada 1972 and Breitenfeld 2014 use thermal activation (Grignard reagent + catalyst); Pengfei 2024 uses cathodic reduction to generate Ni(0) and carbon radicals electrochemically. The activation mode change eliminates the need for Grignard reagents entirely (cross-electrophile coupling).

```
evidence_chain: Kumada_1972 : S0-4 ("Grignard reagent with a vinyl or aryl halide"); Pengfei_2024 : S0-1 ("cross-electrophile coupling of unactivated alkyl halides")
```

Accounts for divergence: Electrochemical activation enables a fundamentally different coupling strategy (two electrophiles rather than nucleophile + electrophile), which in turn creates different selectivity challenges (B-3 in Pengfei 2024).

**DV-4: Evidentiary standard — assertion (1972) → DFT+kinetics (2014) → DFT+electroanalysis (2024)**

The mechanistic evidentiary standard escalates across the group but shifts to increasingly computational evidence. Kumada 1972 asserts mechanism from analogy; Breitenfeld 2014 uses radical clock + DFT + kinetics; Pengfei 2024 uses CV/SWV + DFT + radical trapping.

```
evidence_chain: Kumada_1972 : B-2 (analogy only); Breitenfeld_2014 : U-3 (DFT as sole discriminant); Pengfei_2024 : U-2 (DFT–SWV 360 mV discrepancy)
```

Accounts for divergence: Year and journal norms; also reflects the increasing role of DFT as a mechanistic tool that is adopted faster than its validation protocols.

---

## recurring_U

```
recurring_U: Self-contradictory absence between proposed mechanism and untested predictions | papers: [Kumada_1972, Breitenfeld_2014, Pengfei_2024] | item_ids: [Kumada_1972: U-1, U-2; Breitenfeld_2014: U-1, U-2; Pengfei_2024: U-1, U-2] | note: Each paper's proposed mechanism generates testable predictions that the paper itself does not test: Kumada_1972 predicts R–R from eq 3 but does not report it; Breitenfeld_2014 proposes eq 3 redistribution but does not derive the rate law algebraically; Pengfei_2024 proposes two alternative pathways but does not experimentally discriminate them and presents DFT potentials that disagree with SWV. The pattern — proposing a mechanism whose own predictions go untested — is the most persistent U-pattern in this group. Its recurrence across three independent research groups over 52 years suggests it may be a structural feature of mechanistic publication practice: the incentive to propose a complete cycle exceeds the incentive to test all its predictions.
```

---

## group_unasked_question

[REDACTED: substantial verbatim quotation; see Tier 9]

```
evidence_chain: Kumada_1972 : B-1 (selectivity unquantified), B-2 (two-electron cycle unvalidated); Breitenfeld_2014 : U-2 (rate law not derived for eq 3), B-2 (TDS assignment without algebraic proof); Cherney_2015 : B-1 (DYKAT krac/kproductive absent); Pengfei_2024 : B-3 (selectivity model in SI only), A-1 (Path I/II unresolved), U-1 (mechanism undiscriminated)
```

TEMPERATURE_SUMMARY correspondence: The group-level question corresponds to the highest-convergence items: Kumada_1972 B-1 (3/3 convergence, all high) and Pengfei_2024 B-1 (3/3 convergence, all high) — both concern the gap between claimed selectivity and absent quantitative accounting. The selectivity question is the through-line connecting sp² (Kumada 1972) to sp³ (Breitenfeld 2014, Pengfei 2024) to the review's classification framework (Cherney 2015).

recurring_root correspondence: This group-level question integrates all three recurring roots: (1) "catalytic cycle proposed as complete without intermediate observation" → the selectivity-determining step cannot be identified without knowing which cycle operates; (2) "selectivity claimed without byproduct accounting" → selectivity cannot be quantified without mass balance; (3) "DFT used without validation" → the computational barrier/rate comparisons used to explain selectivity are unanchored to experimental rates. The three roots converge on the same question: what is the quantitative, experimentally grounded basis for selectivity in Ni-catalyzed cross-coupling?

---

> **Tier 8 redaction notice**: This file is a redacted copy of the corresponding Tier 3 / Tier 9 output. Verbatim source-paper quotations have been replaced by `[REDACTED: see source paper §<loc>; full text retained in Tier 9 reviewer-only deposit]` markers, preserving location references and our own analytical content. Bibliographic fields (title, authors, journal, year, DOI), analytical labels (`evidence_chain:` with B-/U-/A-/C- internal IDs), short technical terms, and our own analytical text are not redacted. The redaction was applied by `scripts/redact_for_tier8.py` and, for this version, by `scripts/build_paperA_R1_public.py` with `scripts/redact_source_ngram_runs.py` (scripts of the project repository; they are not deposited).
