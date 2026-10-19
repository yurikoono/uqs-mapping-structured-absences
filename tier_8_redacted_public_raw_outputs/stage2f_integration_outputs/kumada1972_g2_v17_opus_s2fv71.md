prompt_version: stage2f-v7-20260417

---

**[F. Within-Group Comparison]**

**Group composition:** G2 — Boundary Breakthrough (Csp³ frontier, 1972–2024)
- Kumada 1972 (JACS Communication): Ni-catalyzed Csp²–Csp² and Csp²–Csp³ cross-coupling; Csp³ halides explicitly excluded
- Breitenfeld 2014 (Organometallics Full Paper): Ni-pincer-catalyzed alkyl(sp³)–aryl Kumada coupling via radical bimetallic OA
- Cherney 2015 (Chem. Rev. Review): enantioselective/enantiospecific cross-coupling survey documenting Csp³ as the frontier
- Pengfei 2024 (Nature Catalysis): Ni-electrocatalyzed Csp³–Csp³ cross-electrophile coupling of unactivated alkyl halides

---

**Repeated patterns**

**RP-1: Mechanistic proposals with incomplete intermediate characterization or pathway discrimination**

All four papers propose or discuss catalytic cycles whose elementary steps are not fully validated within the operating catalytic system.

evidence_chain: [Kumada_1972 : B-2, B-14, U-1, U-4 | Breitenfeld_2014 : U-1, U-2, U-3, B-2, B-5 | Cherney_2015 : B-1, B-6, B-7, U-1, U-3 | Pengfei_2024 : A-1, U-1, B-3, B-4, B-5]

- Kumada 1972: Ni(0)/Ni(II) catalytic cycle (eqs 2–4) assembled from stoichiometric analogies in different Ni systems; no intermediate observed in the NiCl₂(dpe) system (B-2, B-14). R–R predicted by eq 3 but unreported (U-1).
- Breitenfeld 2014: "Complete catalytic cycle" (Figure 8) proposed with intermediates 10–16, none observed under stoichiometric or catalytic conditions (U-1). Bimetallic OA vs escape-rebound discrimination rests entirely on unvalidated DFT (U-3). Rate law algebraic derivation from eq 3 not provided (U-2).
- Cherney 2015: DYKAT invoked as standard mechanism throughout Sections 2.1–2.2 without krac/kproductive measurement (B-1). SET mechanism for Ni/Ir photoredox proposed with NiIII and IrII intermediates never spectroscopically observed (U-3). DET hypothesis untested by conversion-ee profile (U-1).
- Pengfei 2024: Two mechanistic pathways (Path I: Ni(0)→radical; Path II: Ni(II)→Ni(I)→Ni(III)) acknowledged as undiscriminated (A-1, U-1). Selectivity model — the paper's central claim — deferred to SI (B-3). DFT methodology unreported in main text (B-4, B-5).

---

**RP-2: Quantitative analytical basis for primary data underreported**

Every paper in this group grounds its claims in quantitative measurements whose reliability cannot be independently assessed.

evidence_chain: [Kumada_1972 : B-4, B-8, B-9, B-12, B-13 | Breitenfeld_2014 : B-6, B-7, B-9 | Cherney_2015 : B-2, B-3 | Pengfei_2024 : B-1, B-14, B-15]

- Kumada 1972: glpc conditions absent, reaction times absent for 9/11 entries, yield basis mixing, characterization via "and/or" (SRG-3).
- Breitenfeld 2014: radical-clock fit with unexamined negative intercept (B-6); rate-order slopes (1.7 for "second order") accepted without statistical testing; consecutive kinetic runs without randomization (B-9).
- Cherney 2015: no PRISMA-style search methodology for the review (B-2); cross-study ee comparisons disclaimed in one figure but applied uncaveated elsewhere (B-3).
- Pengfei 2024: >90 substrate examples with isolated yields only, no GC/conversion data (B-1); no replicate measurements anywhere (B-14); yield basis mixing between limiting and excess reagent (B-15).

---

**RP-3: DFT computation used as mechanistic discriminant without experimental validation**

Two of the four papers deploy DFT as the primary or sole basis for distinguishing between competing mechanisms, without validating the computational protocol against experimental observables.

evidence_chain: [Breitenfeld_2014 : U-3, B-3, B-5 | Pengfei_2024 : U-2, B-4, B-5, B-13]

- Breitenfeld 2014: DFT is the sole discriminant between bimetallic OA and escape-rebound; the critical free energy difference (−0.4 vs 0.0 kcal/mol) is acknowledged as imprecise ("best accomplished through molecular dynamics simulations") yet used as the mechanistic conclusion (B-5, U-3). The PBE0-dDsC//M06 composite protocol is not benchmarked (B-3).
- Pengfei 2024: DFT-calculated Ni(I)/Ni(0) potential (−2.38 V) and SWV-measured value (−2.74 V) disagree by 360 mV without discussion (U-2, B-13). DFT methodology (functional, basis set, solvation model) absent from main text (B-4, B-5).

Note: Kumada 1972 predates DFT; Cherney 2015 cites DFT indirectly (DET computational study, U-1) but the issue is the DET experimental test rather than DFT quality per se.

---

**RP-4: Self-contradictory absence — models generating untested predictions**

All four papers contain instances where a proposed model predicts specific observables that the paper does not test.

evidence_chain: [Kumada_1972 : U-1, U-2 | Breitenfeld_2014 : U-1, U-2 | Cherney_2015 : U-1, U-2, U-3 | Pengfei_2024 : U-2]

- Kumada 1972: Catalytic cycle predicts R–R (untested, U-1); "black mixture" observation consistent with heterogeneous catalysis but homogeneous mechanism proposed (U-2).
- Breitenfeld 2014: "Complete catalytic cycle" predicts intermediates 10–16, none detected (U-1); eq 3 mechanism predicts a specific rate law never derived (U-2).
- Cherney 2015: DET mechanism predicts conversion-independent ee, untested (U-1); Kagan-Durst kinetic resolution model predicts specific conversion-ee relationship for s ≈ 5, not verified with conversion data (U-2); SET mechanism predicts IrII and NiIII intermediates, never spectroscopically observed (U-3).
- Pengfei 2024: DFT predicts Ni(I)/Ni(0) potential that disagrees with SWV by 360 mV, undiscussed (U-2).

---

**RP-5: Scope/selectivity claims without complete mass balance**

Papers making scope or selectivity claims report product yields without accounting for competing pathways.

evidence_chain: [Kumada_1972 : B-1, U-1, C-1 | Breitenfeld_2014 : B-7 (rate orders without absolute rate constant) | Pengfei_2024 : B-1, B-11, B-12]

- Kumada 1972: "Selective" cross-coupling with no homo-coupling data (B-1, U-1).
- Pengfei 2024: >90 substrates with no homocoupling byproduct data beyond model reaction; TEMPO experiment with 59% unaccounted mass (B-11); radical clock without non-ring-opened product yield (B-12).

---

**Cross-field temperature patterns**

temperature_pattern: RP-1 (mechanism validation) | papers: [Kumada_1972, Breitenfeld_2014, Pengfei_2024] | profile_consistency: consistent | note: Mechanism validation gaps receive high severity from V2 (mechanistic agent) across all experimental papers; Kumada 1972 B-2: V2=critical; Breitenfeld 2014 B-5: V1=V2=high (convergence=2/3); Pengfei 2024 A-1: V2=high. The consistent high severity from the mechanistic perspective, combined with lower attention from other viewpoints, indicates this is recognized as significant within the mechanistic community but not by synthetic chemists evaluating practical utility.

temperature_pattern: RP-2 (analytical underreporting) | papers: [Kumada_1972, Breitenfeld_2014, Pengfei_2024] | profile_consistency: consistent | note: Analytical reporting gaps receive consistent medium-to-high severity from V3 (analytical agent) across all three experimental papers: Kumada 1972 B-4 V3=medium; Breitenfeld 2014 B-7 V3=high; Pengfei 2024 B-1 V1=V2=V3=high (3/3 convergence). The 2024 paper's B-1 is the strongest convergence item in its TEMPERATURE_SUMMARY, suggesting that scope-without-conversion-data is increasingly recognized as a field-wide concern.

temperature_pattern: RP-5 (mass balance) | papers: [Kumada_1972, Pengfei_2024] | profile_consistency: consistent | note: Mass balance absence receives 3/3 convergence in both Kumada 1972 (B-1: V1=V2=V3=high) and Pengfei 2024 (B-1: V1=V2=V3=high). The gap's temperature_gap INCREASES in severity across the 52-year span as the reaction complexity grows: reporting selectivity among two Csp² coupling pathways (1972) is simpler than among four Csp³ radical pathways (2024), yet the reporting standard has not improved.

---

**Same-root group patterns**

recurring_root: Catalytic cycle proposed without experimental validation of elementary steps | papers: [Kumada_1972, Breitenfeld_2014, Pengfei_2024] | member_items: [Kumada_1972: SRG-1 (B-2, B-14, U-1, U-2, U-4), Breitenfeld_2014: SRG-4 (U-1, B-2), Pengfei_2024: SRG-3 (A-1, B-3, U-1)] | note: Structural gap across all three experimental papers — mechanism is assembled from kinetics, radical probes, and/or DFT analogy but no elementary step is directly demonstrated in the operating catalytic system. Genre convention that has persisted across 52 years and different reaction paradigms (2-electron vs 1-electron).

recurring_root: Quantitative measurement basis underreported | papers: [Kumada_1972, Breitenfeld_2014, Pengfei_2024] | member_items: [Kumada_1972: SRG-3, Breitenfeld_2014: SRG-3+SRG-6, Pengfei_2024: SRG-1] | note: Genre convention — chemistry journals across all three eras (1972 JACS, 2014 Organometallics, 2024 Nature Catalysis) do not enforce replicate-based uncertainty, raw data deposition, or full mass balance.

recurring_root: Selectivity claim without byproduct accounting | papers: [Kumada_1972, Pengfei_2024] | member_items: [Kumada_1972: SRG-2, Pengfei_2024: SRG-1 partial] | note: The same gap (selectivity asserted through product yield without byproduct quantification) appears in both the founding paper and the 2024 extension, despite 52 years of methodological development.

---

**Temporal trajectory of recurring patterns**

temporal_trajectory: RP-1 (mechanism validation) | classification: shifting | transition_point: ~2000 (emergence of radical Ni catalysis) | note: 1972: 2-electron Ni(0)/Ni(II) cycle proposed by analogy (structurally suppressed — no radical clock, no DFT available). 2014: radical mechanism investigated with radical-clock probes and DFT, but DFT becomes the sole pathway discriminant (shifting from suppressed to individually chosen). 2024: electrochemical mechanistic probes (CV, SWV) deployed but pathway I/II discrimination remains unresolved (shifting — tools available but insufficient for complete resolution). The gap shifts from "no tools" to "tools deployed but conclusions remain provisional."

temporal_trajectory: RP-2 (analytical underreporting) | classification: time-invariant | transition_point: n/a | note: The character of analytical underreporting is essentially unchanged: 1972 reports glpc yields without conditions; 2014 reports rate orders without statistical tests; 2024 reports isolated yields without conversion data. Reporting conventions have not improved despite increased analytical capability.

temporal_trajectory: RP-3 (DFT as discriminant) | classification: emergent | transition_point: ~2005 (DFT becomes routine in organometallics) | note: This pattern appears only in post-2005 papers. Kumada 1972 predates DFT. By 2014, DFT is the sole pathway discriminant; by 2024, DFT potentials disagree with experiment by 360 mV yet are used as mechanistic evidence. The pattern is emergent and intensifying.

temporal_trajectory: RP-4 (self-contradictory absence) | classification: time-invariant | transition_point: n/a | note: The specific untested predictions change (R–R in 1972; intermediates 10–16 in 2014; conversion-ee profiles in 2015; DFT-experiment discrepancy in 2024), but the structural pattern — model predicts observable, observable not tested — is invariant across 52 years.

temporal_trajectory: RP-5 (mass balance absence) | classification: time-invariant | transition_point: n/a | note: Mass balance is absent in both the first (1972) and most recent (2024) experimental papers. The gap persists despite dramatically different reaction complexity.

---

**Structural suppression vs. individual choice**

RP-1 (mechanism validation):
- *Era-dependent*: structurally suppressed (1972: no radical probes, no DFT, no in situ spectroscopy) → individually chosen / methodologically limited (2014: radical clock and DFT deployed but DFT precision acknowledged as insufficient; 2024: CV/SWV deployed but pathway discrimination acknowledged as incomplete). By 2014–2024, tools exist but do not fully resolve the question.

RP-2 (analytical underreporting):
- *Incentive-suppressed*: Publishing replicate kinetic data, GC conversion alongside isolated yields, or statistical uncertainty of rate orders would not constitute a publishable contribution in itself. The incentive structure of chemical journals (synthetic = scope breadth; mechanistic = cycle proposals) does not reward this work.

RP-3 (DFT as sole discriminant):
- *Individually chosen*: In both Breitenfeld 2014 and Pengfei 2024, additional experiments (stoichiometric intermediate trapping, Eyring analysis, matched-pair DFT benchmarking) could have been performed with the paper's own infrastructure but were not. The reliance on DFT as discriminant is individually chosen.

RP-4 (self-contradictory absence):
- *Individually chosen*: Each untested prediction is testable with the paper's own experimental setup. Testing R–R formation (1972) requires only glpc. Testing intermediates 10–16 (2014) requires stoichiometric NMR. Testing conversion-ee profiles (2015 primary papers) requires time-course sampling. Testing DFT prediction against SWV (2024) requires only a single paragraph of discussion.

RP-5 (mass balance):
- *Incentive-suppressed*: A comprehensive mass balance study of Ni-catalyzed cross-coupling — quantifying all byproducts, protodehalogenation, homocoupling, oligomerization — would constitute a standalone analytical paper that no high-impact journal would publish. No group in the field has published such a study.

---

**Paradigm competition**

This group reveals a clear paradigm succession:

**Paradigm A: Two-electron Ni(0)/Ni(II) mechanism (1972)**
Kumada 1972 proposes oxidative addition → transmetalation → reductive elimination as the catalytic cycle, with selectivity arising from the Ni–phosphine ligand environment. This paradigm is restricted to Csp² halides.

Systematically unanswered question by Paradigm A:
- Why are Csp³ halides excluded? What mechanistic feature prevents oxidative addition or subsequent steps with Csp³ electrophiles?
  evidence_chain: [Kumada_1972 : B-5 → "Only Csp² halides... can be used"; "no textual basis in Kumada_1972" for the mechanism of exclusion — the Csp³ boundary is noted but not explained]

**Paradigm B: One-electron radical Ni(I)/Ni(II)/Ni(III) mechanism (2014, 2024)**
Breitenfeld 2014 and Pengfei 2024 propose that Csp³ halides undergo radical activation (homolytic C–X cleavage via SET from Ni(I) or Ni(0)), generating carbon radicals that recombine with Ni(II) species. This paradigm was developed specifically because the two-electron pathway fails for Csp³ substrates.

Systematically unanswered questions by Paradigm B:
- What is the quantitative selectivity mechanism that prevents homo-coupling of two radicals generated from two different alkyl halides?
  evidence_chain: [Pengfei_2024 : B-3 → "see Supplementary Discussion on the Selectivity for details"; Breitenfeld_2014 : B-2 → rate law algebraic derivation absent]
- Are all proposed intermediates (10–16 in Breitenfeld; Ni species A–D in Pengfei) experimentally accessible?
  evidence_chain: [Breitenfeld_2014 : U-1 → none characterized; Pengfei_2024 : U-1 → Path I/II undiscriminated]

**Succession relationship:** Paradigm B's founding problem (Csp³ coupling) is precisely Paradigm A's acknowledged blind spot ("Only Csp² halides can be used"). Paradigm A's two-electron mechanism becomes the paradigmatic predecessor that Paradigm B explicitly supersedes for Csp³ substrates. This is paradigm succession, not competition — by 2014, no group proposes a two-electron mechanism for Csp³ alkyl halide coupling.

However, a shared blind spot persists across both paradigms: neither paradigm quantifies the selectivity of cross-coupling over homo-coupling through mass balance data. Kumada 1972 reports no R–R; Pengfei 2024 reports >90 isolated yields with no homocoupling data beyond the model reaction. The mass balance gap is paradigm-invariant.

**The review (Cherney 2015)** documents this succession by organizing the field into enantioselective (catalyst-controlled) and enantiospecific (substrate-controlled) categories. The review's SRG-2 (mechanistic proposals without direct verification: B-4, B-7, U-1, U-3) captures exactly the gap that persists across both paradigms — mechanism is proposed but not experimentally verified at the elementary-step level.

---

**Divergences**

**DV-1: Mechanism of selectivity — 2-electron geometric control vs 1-electron concentration/kinetic control**
Kumada 1972 attributes selectivity to ligand geometry (cis-configuration of diorganonickel intermediate) — a structural argument. Breitenfeld 2014 attributes selectivity to bimetallic transmetalation kinetics — a rate argument. Pengfei 2024 attributes selectivity to concentration differential and electrochemical characteristics of the two halides — a thermodynamic/kinetic argument. These are fundamentally different selectivity paradigms.

evidence_chain: [Kumada_1972 : B-3 → "cis configuration... is the first requisite" | Breitenfeld_2014 : B-2 → "second order in both catalyst and Grignard reagent" | Pengfei_2024 : B-3 → "difference in concentration and the electrochemical characteristics"]

**DV-2: Role of DFT — absent vs central**
Kumada 1972 has no computational component. Breitenfeld 2014 uses DFT as the sole pathway discriminant but acknowledges its limitations. Pengfei 2024 uses DFT to calculate redox potentials and reductive elimination barriers with a 360 mV experimental discrepancy. The increasing reliance on DFT inversely correlates with experimental mechanistic depth.

evidence_chain: [Kumada_1972 : none (pre-DFT) | Breitenfeld_2014 : U-3, B-5 | Pengfei_2024 : U-2, B-4, B-5, B-13]

**DV-3: Review vs primary papers — inherited mechanism vs tested mechanism**
Cherney 2015 inherits mechanistic proposals (DYKAT, DET, SET) from primary papers without independently testing them, creating a new class of gap: the mechanistic classification that becomes authoritative through review endorsement rather than experimental validation (B-1, SRG-2 in Cherney S1).

evidence_chain: [Cherney_2015 : B-1 → DYKAT without krac/kproductive, B-7 → π-allyl convergence as "sufficient" evidence | Kumada_1972 : B-2 → "working hypothesis" in primary paper → no equivalent caveat in Cherney_2015 when citing Kumada-type reactions]

---

**U-item patterns**

recurring_U: Self-contradictory absence involving models that generate testable predictions | papers: [Kumada_1972, Breitenfeld_2014, Cherney_2015, Pengfei_2024] | item_ids: [Kumada_1972: U-1, U-2; Breitenfeld_2014: U-1, U-2, U-3; Cherney_2015: U-1, U-2, U-3; Pengfei_2024: U-2] | note: The classification framework (A/B/C) does not naturally capture "model predicts → prediction untested → model retained." This pattern is the most densely recurring across all four papers, suggesting it is a field-wide structural convention rather than an individual authorial choice. The A/B/C framework is designed for gaps within a paper's stated claims; self-contradictory absence is a gap between the paper's model and its model's own implications.

---

**Self-contradictory absence patterns**

self_contradictory: [Kumada_1972] : catalytic cycle eq 3 → R–R predicted → R–R unreported | item_id: U-1
self_contradictory: [Kumada_1972] : homogeneous mechanism → "black mixture" → heterogeneous possibility unanalyzed | item_id: U-2
self_contradictory: [Breitenfeld_2014] : "complete catalytic cycle" Figure 8 → intermediates 10–16 predicted → none characterized | item_id: U-1
self_contradictory: [Breitenfeld_2014] : eq 3 redistributive TM → specific rate law predicted → derivation not provided | item_id: U-2
self_contradictory: [Breitenfeld_2014] : bimetallic OA vs escape-rebound → DFT discriminates with acknowledged imprecision → imprecision not quantified | item_id: U-3
self_contradictory: [Cherney_2015] : DET mechanism → conversion-independent ee predicted → conversion-ee profile untested | item_id: U-1
self_contradictory: [Cherney_2015] : KR with s ≈ 5 → specific conversion-ee relationship predicted → conversion not reported alongside 90% ee | item_id: U-2
self_contradictory: [Cherney_2015] : SET cycle → IrII and NiIII predicted → neither spectroscopically observed | item_id: U-3
self_contradictory: [Pengfei_2024] : DFT Ni(I)/Ni(0) = −2.38 V → SWV measures −2.74 V → 360 mV discrepancy undiscussed | item_id: U-2

**Recurring pattern assessment:** Self-contradictory absence recurs in all four papers across all paradigms (2-electron, radical, electrochemical) and all formats (communication, full paper, review). This pattern reflects a **genre convention**: mechanism sections in cross-coupling papers serve a narrative function (contextualizing the scope data within a plausible cycle) rather than a hypothesis-testing function (generating and testing falsifiable predictions from the cycle). The convention is maintained because testing one's own mechanistic predictions would either confirm them (unpublishable) or falsify them (requiring a different paper). It is simultaneously a **genuine analytical gap** because each untested prediction is testable.

---

**Group-level unasked question**

[REDACTED: substantial verbatim quotation; see Tier 9]

evidence_chain: [Kumada_1972 : B-1 (selectivity w/o byproduct data), B-5 (Csp³ exclusion unexplained) | Breitenfeld_2014 : B-2 (transmetalation rate law not derived), U-2 (rate orders ≠ rate law) | Cherney_2015 : B-1 (DYKAT w/o krac/kproductive), D-4-1 (DYKAT as unexamined premise) | Pengfei_2024 : B-3 (selectivity model in SI), B-1 (no homocoupling data)]

TEMPERATURE_SUMMARY correspondence: In Kumada 1972, B-1 (selectivity claim without byproduct data) is the strongest convergence item (3/3, all high). In Pengfei 2024, B-1 (isolated yields only, no mass balance) is the strongest convergence item (3/3, all high). Both are instances of the same underlying question: what determines cross vs homo selectivity? The 52-year persistence of this as the most convergent gap item — across paradigms, substrates, and journals — indicates it is a field-wide structural convention that each individual paper inherits rather than chooses.

recurring_root correspondence: The group-level unasked question subsumes recurring_root 1 (catalytic cycle validation) and recurring_root 3 (selectivity without mass balance) as two facets of a single deficit: the field has never produced a quantitative selectivity model validated by complete mass balance data for Ni-catalyzed cross-coupling. The 1972 paper lacked Csp³ substrates to make the question visible; the 2014 and 2024 papers have Csp³ substrates but still lack the quantitative selectivity data.

---

*End of G2 output.*

---

> **Tier 8 redaction notice**: This file is a redacted copy of the corresponding Tier 3 / Tier 9 output. Verbatim source-paper quotations have been replaced by `[REDACTED: see source paper §<loc>; full text retained in Tier 9 reviewer-only deposit]` markers, preserving location references and our own analytical content. Bibliographic fields (title, authors, journal, year, DOI), analytical labels (`evidence_chain:` with B-/U-/A-/C- internal IDs), short technical terms, and our own analytical text are not redacted. The redaction was applied by `scripts/redact_for_tier8.py` and, for this version, by `scripts/build_paperA_R1_public.py` with `scripts/redact_source_ngram_runs.py` (scripts of the project repository; they are not deposited).
