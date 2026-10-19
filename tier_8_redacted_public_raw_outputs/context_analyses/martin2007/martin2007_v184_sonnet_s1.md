```
prompt_version: stage1-v184-20260502
model_info: claude-sonnet-4-6

target_title:   Pd-Catalyzed Kumada-Corriu Cross-Coupling Reactions at Low Temperatures Allow the Use of Knochel-type Grignard Reagents
target_authors: Ruben Martin, Stephen L. Buchwald
target_start:   page 1: [REDACTED: paper boundary quote; see Tier 9]
target_end:     end of document (single paper, 2 pages)

[Agent fields]
V1: Synthetic organometallic / transition-metal catalysis — Direct disciplinary home for substrate scope, ligand screening, and catalyst evaluation as primary evidence types.
V2: Mechanistic / physical organic chemistry — Interrogates elementary steps, kinetic basis for rate-limiting step assignment, and distinction between ionic and radical pathways; generates questions of a fundamentally different type than V1's synthetic perspective.
V3: Analytical chemistry / chromatographic and spectroscopic characterization — Addresses yield quantification methodology, mass balance closure, purity assessment, and statistical validity of reported data.

---

### Step 0: Boundary recheck

All quotes from Turns 1–3 are drawn from the two-page main paper or its Supporting Information. The paper is a single JACS Communication (pages 3844–3845) with no adjacent paper boundary issue. No boundary violations detected. V1-Q9 mentions Ni catalysis as an external inference (T3) — this is appropriately labeled; the quote itself comes from the main paper. No items require [?boundary] flagging.

---

### Step 1: Cross-field temperature

Items flagged by multiple agents:

| Original item | Agents flagging | V1 severity | V2 severity | V3 severity | convergence | temperature_gap |
|---|---|---|---|---|---|---|
| Rate-limiting step assignment (V1-Q3 / V2-Q1 / V2-OV1 / V3-OV5) | V1, V2, V3 | high | high | medium | 3/3 | low |
| Chemoselectivity / halide tolerance (V1-Q6 / V2-Q10 / V2-OV3 / V3-Q5 / V3-OV2) | V1, V2, V3 | high | high | high | 3/3 | none |
| LiCl role dismissal (V1-Q13 / V2-Q4 / V2-OV2) | V1, V2 | medium | high | — | 2/3 | low |
| Benzyne decomposition evidence (V1-Q8 / V2-Q7 / V2-OV4 / V3-OV4) | V1, V2, V3 | medium | high | high | 3/3 | low |
| Reproducibility / run-to-run variability (V1-Q4 / V3-Q1 / V3-OV1) | V1, V3 | medium | — | medium | 2/3 | none |
| Conditions variation unexplained (V1-Q5 / V3-OV3) | V1, V3 | medium | — | medium | 2/3 | none |

---

### Step 2: Same-root groups

SRG-1 (Kinetic / mechanistic evidence cluster): V1-Q3, V2-Q1, V2-Q2, V2-Q9, V3-OV5
— Shared root: "No kinetic or mechanistic probe data are reported; all mechanistic assignments (rate-limiting step, transmetalation vs. OA) rest on qualitative reactivity comparison alone."

SRG-2 (Chemoselectivity and mass balance cluster): V1-Q6, V2-Q10, V3-Q5
— Shared root: "The chemoselectivity claim (halide tolerance) lacks byproduct identification and mass balance data; competitive coupling experiments were not performed."

SRG-3 (Benzyne / decomposition pathway cluster): V1-Q8, V2-Q7, V3-OV4
— Shared root: "The assertion that benzyne decomposition 'did not occur' at low temperature is not supported by analytical identification of byproducts or trapping experiments."

SRG-4 (Yield data quality cluster): V1-Q4, V3-Q1, V3-Q2, V3-OV1
— Shared root: "Primary yield data (GC and isolated) lack run-to-run spread, response factors, and individual trial values; n=2 average without uncertainty is insufficient for analytical validation."

SRG-5 (LiCl / Grignard aggregation cluster): V1-Q13, V2-Q4
— Shared root: "The dismissal of LiCl's role is based on yield similarity without characterization of Grignard speciation or aggregation state."

SRG-6 (Ligand switch L2/L3 unexplained cluster): V1-Q7, V2-Q5
— Shared root: "The switch from L3 (Tables 2, 4) to L2 (Table 3) is acknowledged as unexplained and no mechanistic or electronic rationale is provided."

---

### Step 3: Classification

---

[A] A-1
loc: P2:Rcol:L18-22*
quote: [REDACTED: see `loc:` above; full text in Tier 9]
deferral_type: deferred
mixed_detail: n/a
reason_inferred: T1 (paper explicitly states)
linked_to: A-2, B-3
cross_field_temperature: V1=medium, V3=medium; convergence=2/3; temperature_gap=none

[A] A-2
loc: P1:Rcol:L20-22* (footnote 10b)
quote: [REDACTED: see `loc:` above; full text in Tier 9]
deferral_type: deferred
mixed_detail: n/a
reason_inferred: T1 (paper explicitly states ongoing work)
linked_to: A-1, B-3, U-1
cross_field_temperature: V1=medium; convergence=1/3; temperature_gap=n/a

[A] A-3
loc: P2:Rcol:L3-5* (Table 3 discussion)
quote: [REDACTED: see `loc:` above; full text in Tier 9]
deferral_type: deferred (authors explicitly state no current explanation)
mixed_detail: n/a
reason_inferred: T1
linked_to: B-4
cross_field_temperature: V1=medium, V2=medium; convergence=2/3; temperature_gap=none

---

[B] B-1
loc: P1:Rcol:L11-14*
quote: [REDACTED: see `loc:` above; full text in Tier 9]
classification: reporting_omission
rhetorical_function: Mechanistic interpretation offered as a likely inference from differential substrate reactivity.
note: The rate-limiting step assignment is presented as a "likely" inference based on ArI > ArOTf reactivity, but no kinetic data (rate constants, activation parameters, competition experiments, KIE) are reported. Standard practice in physical organic chemistry requires at least one experimental kinetic probe for a rate-determining step claim. This is absent from both the main paper and SI. SRG-1. Cross-agent flag: V1-Q3 (high), V2-Q1 (high), V3-OV5 (medium).
cross_field_temperature: V1=high, V2=high, V3=medium; convergence=3/3; temperature_gap=low

[B] B-2
loc: P2:Lcol:L7-10*
quote: [REDACTED: see `loc:` above; full text in Tier 9]
classification: reporting_omission
rhetorical_function: Chemoselectivity claim presented as a positive feature of the method based on survival of halide substituents in isolated products.
note: The chemoselectivity claim rests on isolation of halide-intact products, but no byproduct characterization or mass balance data are reported. Competition experiments between ArI and ArBr/ArCl electrophiles were not performed. Yield of homocoupling or dehalogenation products is not reported. Without these data, chemoselectivity is asserted by default (product isolated), not demonstrated analytically. SRG-2. Cross-agent flag: V1-Q6 (high), V2-Q10 (high), V3-Q5 (high).
cross_field_temperature: V1=high, V2=high, V3=high; convergence=3/3; temperature_gap=none

[B] B-3
loc: P1:Rcol:L1-3* (Table 1) and P2:Lcol:L4-6* (Table 2 footnotes)
quote: [REDACTED: see `loc:` above; full text in Tier 9]
classification: mixed (intentional_narrowing + reporting_omission)
rhetorical_function: General conditions claimed as standard but with silent per-entry deviations in ligand and catalyst loading.
note: Conditions vary across entries without explanation (L2 vs. L3, 2 mol% vs. 3 mol% Pd, 3 mol% vs. 4 mol% L3). The deviation is acknowledged only in table footnotes, not in the main text. This makes the "general conditions" framing partially misleading, as at least three entries require different conditions. The paper does not explain why standard conditions fail for specific substrates or what threshold of steric/electronic challenge triggers a conditions change. Cross-agent flag: V1-Q5 (medium), V3-OV3 (medium).
cross_field_temperature: V1=medium, V3=medium; convergence=2/3; temperature_gap=none

[B] B-4
loc: P2:Rcol:L7-12*
quote: [REDACTED: see `loc:` above; full text in Tier 9]
classification: reporting_omission
rhetorical_function: Assertion that benzyne decomposition was absent, presented as a positive outcome without analytical evidence.
note: The paper asserts benzyne decomposition "did not occur" but provides no GC-MS or trapping-experiment data in either the main paper or SI to substantiate this. For a claim about a specific decomposition pathway not occurring, analytical identification (or deliberate search for) benzyne-derived products is expected. SRG-3. Cross-agent flag: V1-Q8 (medium), V2-Q7 (high), V3-OV4 (high).
cross_field_temperature: V1=medium, V2=high, V3=high; convergence=3/3; temperature_gap=low

[B] B-5
loc: P1:Rcol:L1-5* (footnote 11)
quote: [REDACTED: see `loc:` above; full text in Tier 9]
classification: reporting_omission
rhetorical_function: Dismissal of a reviewer's concern about LiCl based on yield similarity between two Grignard preparation methods.
note: The dismissal of LiCl's role is based on "similar yields" but no tabulated comparison data are provided (which entries were tested? what were the two yields?). Grignard reagent aggregation state and halide identity are not characterized. LiCl could affect transmetalation kinetics without visible yield difference in endpoint measurements. SRG-5. Cross-agent flag: V1-Q13 (medium), V2-Q4 (high).
cross_field_temperature: V1=medium, V2=high; convergence=2/3; temperature_gap=low

[B] B-6
loc: P2:Lcol:L4* (Table 2 footnote b) and SI:P2
quote: [REDACTED: see `loc:` above; full text in Tier 9]
classification: reporting_omission
rhetorical_function: Disclosure that reported yields are averages of duplicate runs, with a caveat that SI procedures may give slightly different results.
note: Yields are reported as averages of only two runs with no standard deviations or individual values. The SI qualifier ("yields may differ slightly") acknowledges discrepancy between reported and reproducible yields without quantifying the range. For entries at −50 to −65 °C, low-temperature reproducibility is particularly critical. SRG-4. Cross-agent flag: V1-Q4 (medium), V3-Q2 (medium), V3-OV1 (medium).
cross_field_temperature: V1=medium, V3=medium; convergence=2/3; temperature_gap=none

[B] B-7
loc: P1:Rcol:L2-7* (Table 1 discussion)
quote: [REDACTED: see `loc:` above; full text in Tier 9]
classification: reporting_omission
rhetorical_function: Initial hypothesis statement that is revised when aryl iodides prove superior.
note: The switch from aryl triflates to aryl iodides is presented as an empirical finding, but no direct mechanistic test of whether transmetalation or OA is rate-limiting was performed. Solvent and precatalyst screening are mentioned as "systematically examined" but no data are presented for these screens. V1-Q1 and V2-Q9 both identify this data absence. Cross-agent flag: V1-Q1 (medium), V2-Q9 (medium).
cross_field_temperature: V1=medium, V2=medium; convergence=2/3; temperature_gap=none

---

[C] C-1
loc: P1:Lcol:L3-4* (footnotes 3, 4)
citation: refs 3 (Diederich/Stang textbook) and refs 4a–4d (Negishi, Suzuki-Miyaura, Stille, Hiyama)
textual_function: Background citations establishing the landscape of alternative cross-coupling protocols that use less nucleophilic coupling reagents; cited to contextualize why Grignard reagents are "less direct."
reason_severed: These are cited-and-dropped; no yield, rate, or selectivity data from any of these protocols are compared against the current method's data.
affects_claims: yes — the paper's central claim ("more direct and experimentally straightforward") is a comparative claim against these alternatives, but no quantitative comparison is provided.
symmetric_pattern: yes — all four refs (4a–4d) are cited in a single sentence as a grouped list with no differentiation

[C] C-2
loc: P1:Lcol:L5-7* (footnote 5)
citation: refs 5a (Hiriyakkanavar et al. Chem. Commun. 2006) and 5b (Knochel et al. ACIEE 2003)
textual_function: Reviews cited to establish the scope of Knochel's functionalized Grignard reagent methodology as the starting point for this work.
reason_severed: The specific Grignard reagents prepared in the present work (Tables 2, 3) use the methods of refs 5a/5b, but the performance/yields of those Grignard reagents in those previous cross-coupling contexts is not compared against the current low-temperature Pd protocol.
affects_claims: medium — these references partially define what "Knochel-type" means, but their cross-coupling scope claims (if any) are not engaged.
symmetric_pattern: yes — both cited together as a unit for the same function

[C] C-3
loc: P1:Rcol:L13-14* (footnote 10a)
citation: Alcazar-Roman, L. M.; Hartwig, J. F. Organometallics 2002, 21, 491
textual_function: Cited as mechanistic authority for the OA of aryl iodides vs. aryl triflates to Pd; used to support the rate-limiting OA assignment.
reason_severed: The paper invokes this mechanistic study but provides none of the study's numerical kinetic data (rate constants, activation parameters) for comparison with the current conditions. It is cited as a post-hoc authority without numerical engagement.
affects_claims: yes — the central mechanistic claim (rate-limiting OA) is supported by this citation alone, without reproducing the referenced kinetic analysis.
symmetric_pattern: no (single citation)

[C] C-4
loc: P1:Rcol:L15-18* (footnote 12)
citation: Organ et al. Chem. Eur. J. 2007, 13, 150 (ref 7a)
textual_function: Noted as a concurrent paper reporting a single example of Pd-catalyzed Kumada-Corriu at −20 °C with an unactivated aryl halide, cited to contextualize priority.
reason_severed: The overlap in scope is acknowledged but the paper does not compare yields, conditions, or substrate scope between the two methods; priority context only.
affects_claims: medium — the concurrent paper's existence potentially reduces novelty of −20 °C examples in Table 2, but no direct comparison is made.
symmetric_pattern: no (single citation)

[C] C-5
loc: P2:Rcol:L13-15* (footnote 16)
citation: Molander, G. A.; Biolatto, B. J. Org. Chem. 2003, 68, 4302
textual_function: Cited as the only prior example of cross-coupling of 2,6-difluoro aryl derivatives (as potassium trifluoroborate), to support the novelty of the present 2,6-difluorobiaryls.
reason_severed: The paper does not compare its isolated yields (Table 4: 81–97%) against Molander's yields; the prior method's numerical performance is not engaged.
affects_claims: yes — the novelty of the 2,6-difluorobiaryl synthesis claim depends on demonstrating superiority, but no direct yield/scope comparison is offered.
symmetric_pattern: no (single citation)

[C] C-6
loc: P1:Lcol:L6-7* (footnote 6a–6c)
citation: Bonnet/Mongin/Knochel et al. Tetrahedron 2002; Synlett 2002; Tet. Lett. 2001
textual_function: Cited as exceptions to the rule that Knochel-type Grignard reagents cannot be used directly in cross-coupling; cited to acknowledge prior art but immediately bounded by "some exceptions."
reason_severed: The paper does not explain how the present method's scope exceeds these exceptions (e.g., what functional groups, temperatures, or electrophile classes are newly accessible vs. refs 6a–6c).
affects_claims: yes — the novelty claim over refs 6a–6c is implicit but not supported by direct scope comparison; the differentiation is limited to a parenthetical "see refs 6a and 6c" for heteroaryl halides at −40 °C.
symmetric_pattern: yes — all three refs cited in a single parenthetical with no differentiation

---

[U] U-1
loc: P1:Rcol:L13-14* and footnote 10b
quote: [REDACTED: see `loc:` above; full text in Tier 9]
question: The paper's mechanistic model (rate-limiting OA) predicts specific, testable ordering of electrophile reactivity: ArI > ArBr > ArCl > ArF. This ordering implies that mixing ArI and ArBr/ArCl substrates in a single flask should result in preferential consumption of ArI. However, no competition experiments between electrophiles are reported, and no intermediate Pd(II) oxidative addition complexes are characterized. The paper's own mechanistic proposal predicts observable intermediates and competition ratios that are entirely absent from the paper.
originating_agent: V2 (V2-Q10, V2-Q1, V2-Q9) + V1 (V1-Q3)
severity: high
note: self-contradictory absence — the paper's proposed rate-limiting OA mechanism predicts specific electrophile competition ratios (ArI >> ArBr > ArCl) that are not reported, despite the paper using substrates bearing Cl and Br substituents in entries 2, 3, 8 (Table 2) where selective coupling at I is claimed.

[U] U-2
loc: P1:Rcol:L1-5* (footnote 11)
quote: [REDACTED: see `loc:` above; full text in Tier 9]
question: The paper dismisses the LiCl activation hypothesis with yield similarity data not shown in the paper. The Knochel "Turbo Grignard" mechanism (iPrMgCl·LiCl as an aggregate-disrupting reagent) is a known phenomenon invoked extensively in refs 5a/5b; dismissing it requires either demonstrating that the Grignard aggregation state is unchanged (NMR characterization) or that an equivalent Grignard without LiCl gives identical cross-coupling performance. Neither experiment is presented in paper or SI, and the SI notes only that "the use of iPrMgBr resulted in similar yields" — but iPrMgBr introduces a different halide (Br vs. Cl), not LiCl removal.
originating_agent: V1 (V1-Q13), V2 (V2-Q4)
severity: high
note: self-contradictory absence — the paper itself cites refs 5a/5b (Knochel's work on Turbo Grignard) as the source of the I/Mg-exchange method, yet dismisses LiCl's potential role in the Pd-catalysis without controlling for halide identity. The control experiment required to rule out LiCl effects is not performed.

[U] U-3
loc: P2:Rcol:L7-12*
quote: [REDACTED: see `loc:` above; full text in Tier 9]
question: The paper's central rationale for low-temperature operation is prevention of Grignard decomposition via benzyne and other pathways. The conclusion that "this did not occur" is asserted but not analytically verified. If benzyne or other decomposition products were present in even small amounts, they could (a) account for yields below 100%, (b) react with the catalyst or substrate, and (c) provide mechanistic insight. The paper's own decomposition hypothesis predicts identifiable byproducts that were never searched for.
originating_agent: V1 (V1-Q8), V2 (V2-Q7), V3 (V3-OV4)
severity: high
note: self-contradictory absence — the paper invokes benzyne decomposition as the reason low temperature is necessary (motivating the whole paper), yet provides no evidence that this decomposition is actually suppressed (e.g., trapped benzyne adducts absent, stoichiometric mass balance closes without byproducts). The absence of byproduct reporting makes the central rationale unverifiable.

---

[META]
  linked_items:
    - A-1 ↔ A-2 (both prospective deferral of aryl bromide/chloride extension)
    - A-2 ↔ U-1 (rate-limiting OA claim underpins both A-2 and U-1)
    - B-1 ↔ U-1 (same mechanistic deficit — B-1 is the reporting omission; U-1 is the self-contradictory absence)
    - B-4 ↔ U-3 (same benzyne deficit — B-4 is the reporting omission; U-3 is the self-contradictory absence)
    - B-5 ↔ U-2 (same LiCl deficit — B-5 is the reporting omission; U-2 is the self-contradictory absence)
    - B-3 ↔ A-3 (conditions variation in Tables 2–4 links to the unexplained L2/L3 switch in Table 3)
    - C-3 ↔ B-1 (Alcazar-Roman/Hartwig OA study cited to support rate-limiting step but not numerically engaged)
    - C-6 ↔ B-3 (refs 6a–6c describe prior exceptions; their scope vs. present method is not compared, making scope novelty claim incompletely differentiated)

  same_root_groups:
    - SRG-1 (Kinetic/mechanistic evidence absent): B-1, U-1, C-3, items V1-Q3, V2-Q1, V2-Q2, V2-Q9, V3-OV5 — shared root: "No kinetic data or mechanistic probe experiments are reported; all mechanistic assignments rest on qualitative reactivity comparison."
    - SRG-2 (Chemoselectivity/mass balance absent): B-2, U-1 (partial), items V1-Q6, V2-Q10, V3-Q5 — shared root: "Halide tolerance and chemoselectivity claims are asserted from product isolation without byproduct identification, mass balance, or competition experiments."
    - SRG-3 (Benzyne decomposition evidence absent): B-4, U-3, items V1-Q8, V2-Q7, V3-OV4 — shared root: "The benzyne-suppression rationale for low temperature is asserted without analytical verification."
    - SRG-4 (Yield data quality inadequate): B-6, items V1-Q4, V3-Q1, V3-Q2 — shared root: "Primary yield quantification (GC and isolated) lacks run-to-run spread, response factor corrections, and individual run data."
    - SRG-5 (LiCl dismissal uncontrolled): B-5, U-2, items V1-Q13, V2-Q4 — shared root: "The dismissal of LiCl activation is based on an inadequately controlled comparison; Grignard speciation is uncharacterized."
    - SRG-6 (Ligand switch L2/L3 unexplained): A-3, B-3, items V1-Q7, V2-Q5 — shared root: "The switch between L2 and L3 across Tables 2–4 is acknowledged but unexplained; no mechanistic or electronic rationale is offered."

  symmetric_citations:
    - C-1 (refs 3, 4a–4d): grouped background citations for alternative cross-coupling protocols, cited uniformly without differentiation
    - C-6 (refs 6a–6c): grouped exceptions cited symmetrically as "some exceptions" with no per-entry analysis

  unreported_data:
    - Individual run yields for Tables 2–4 (only averages stated; individual values exist but are not disclosed)
    - Solvent and precatalyst screening data (stated as "systematically examined" in main text; SI does not appear to contain a full screen — only procedure for L screening in Table 1')
    - GC-MS or trapping data for byproduct analysis (particularly benzyne byproducts and homocoupling products)
    - Grignard reagent characterization (aggregation state, halide identity in LiCl comparison experiment)

  series_signal: no

---

[TEMPERATURE_SUMMARY]
  high_convergence_high_gap: [] (empty — as expected; adjacent field agents agree within one severity step)
  high_convergence_low_gap:
    - B-1 (SRG-1: rate-limiting step; V1=high, V2=high, V3=medium; convergence=3/3; temperature_gap=low)
    - B-2 (SRG-2: chemoselectivity; V1=high, V2=high, V3=high; convergence=3/3; temperature_gap=none)
    - B-4 (SRG-3: benzyne; V1=medium, V2=high, V3=high; convergence=3/3; temperature_gap=low)
    - B-5 (SRG-5: LiCl; V1=medium, V2=high; convergence=2/3; temperature_gap=low)
    - B-6 (SRG-4: yield quality; V1=medium, V3=medium; convergence=2/3; temperature_gap=none)
  low_convergence_high_gap:
    - U-2 (LiCl self-contradictory absence; V1-Q13=medium, V2-Q4=high; divergence by 1 step; not full high_convergence but high severity from V2)

---

[GAP]
GAP-1 | type: 1 | priority: high | description: Alcazar-Roman/Hartwig Organometallics 2002 — cited for OA kinetics of ArI vs. ArOTf to Pd; need to assess whether rate constants and conditions are comparable to present low-temperature Pd/L3 system | candidate_paper: Alcazar-Roman, L. M.; Hartwig, J. F. Organometallics 2002, 21, 491 | inference_label: T1 | status: pending

GAP-2 | type: 1 | priority: medium | description: Knochel Turbo Grignard reviews (refs 5a, 5b) — need to assess what LiCl activation data exist for the specific Grignard reagents used in this paper to evaluate the dismissed LiCl effect | candidate_paper: Knochel et al. ACIEE 2003, 42, 4302; Hiriyakkanavar et al. Chem. Commun. 2006, 583 | inference_label: T1 | status: pending

GAP-3 | type: 1 | priority: medium | description: Refs 6a–6c (Bonnet/Mongin/Knochel) — exceptions to Knochel Grignard instability in coupling; need full scope/temperature/substrate comparison vs. present method to assess differentiation | candidate_paper: Bonnet/Mongin et al. Tetrahedron 2002, 58, 4429; Synlett 2002, 1008; Tet. Lett. 2001, 42, 5717 | inference_label: T1 | status: pending

GAP-4 | type: 2 | priority: medium | description: Concurrent Organ et al. 2007 (ref 7a) — published simultaneously reporting Pd-Kumada at −20 °C; direct scope/yield/condition comparison needed to establish differentiation between the two methods | candidate_paper: Organ et al. Chem. Eur. J. 2007, 13, 150 | inference_label: T1 | status: pending

GAP-5 | type: 3 | priority: low | description: Papers on Grignard reagent aggregation and LiCl "Turbo" activation — to contextualize whether LiCl could play a role in transmetalation at low temperature independently of Grignard formation | candidate_paper: Not stated in paper; general Knochel aggregation literature | inference_label: T3 | status: pending

inference_time_sec: not available — inject externally
```

---

> **Tier 8 redaction notice**: This file is a redacted copy of the corresponding Tier 3 / Tier 9 output. Verbatim source-paper quotations have been replaced by `[REDACTED: see source paper §<loc>; full text retained in Tier 9 reviewer-only deposit]` markers, preserving location references and our own analytical content. Bibliographic fields (title, authors, journal, year, DOI), analytical labels (`evidence_chain:` with B-/U-/A-/C- internal IDs), short technical terms, and our own analytical text are not redacted. The redaction was applied by `scripts/redact_for_tier8.py` and, for this version, by `scripts/build_paperA_R1_public.py` with `scripts/redact_source_ngram_runs.py` (scripts of the project repository; they are not deposited).
