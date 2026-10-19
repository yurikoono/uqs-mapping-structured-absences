prompt_version: stage2f-v7-20260417

---

**[F. Within-Group Comparison]**

**Group composition:** G1 — Direct lineage (dpe/dppe-Ni system, 1972–2021)
- Kumada 1972 (JACS Communication, 3 pp): method discovery
- Kumada 1976b (BCSJ Full Paper, 12 pp): scope and limitations
- Mazet 2021 (ACS Catal., 10 pp): comparative mechanistic study

---

**Repeated patterns**

**RP-1: Catalytic cycle proposed without experimental validation in the operating catalyst system**

All three papers propose Ni(0)/Ni(II) catalytic cycles as the operative mechanism for their respective systems, yet in none of the three is a complete set of elementary steps experimentally validated within the actual catalytic system under catalytic conditions.

evidence_chain: [Kumada_1972 : B-2, B-14, U-1, U-2, U-4 | Kumada_1976b : A2, C3, C4, U1, U2 | Mazet_2021 : B1, B3, B8, U1, U3]

- Kumada 1972: intermediates 1, 2, 3 in eqs 2–4 are not isolated or observed; mechanism assembled from dipy-Ni stoichiometric analogy (B-14); the cycle predicts R–R but this is never reported (U-1); a black mixture consistent with heterogeneous catalysis is unremarked (U-2).
- Kumada 1976b: Scheme 1 acknowledged as unverified ([REDACTED: substantial verbatim quotation; see Tier 9] — A2); the two mechanistic precedents (refs 30–32) are from different Ni systems (C3); sole external support (Morrell/Kochi, ref 46) cited without elaboration (C4); MgXX' stoichiometric byproduct never characterized (U1); β-elimination suppression claim contradicted by isomerization observation (U2).
- Mazet 2021: dppe cycle partially supported by intermediate characterization (9c/III-b), but dmpe cycle rests entirely on apparent second-order catalyst kinetics (B1) qualified by acknowledged decomposition artifacts (B3), an unidentified resting state (B8), and a stoichiometric experiment (U1) that does not distinguish selective interception from statistical scrambling (U3).

---

**RP-2: Quantitative analytical basis for yield/rate data systematically underreported**

All three papers ground their primary quantitative claims (yields, conversions, kinetic orders) in instrumental measurements whose reliability cannot be independently assessed from the published data.

evidence_chain: [Kumada_1972 : B-4, B-8, B-9, B-12, B-13 | Kumada_1976b : B4, B5, B7, B8, B9, U3 | Mazet_2021 : B4, B5, B13, B14, B17]

- Kumada 1972: glpc conditions (column, detector, standard) absent (B-4); reaction times for 9/11 entries missing (B-8); yield basis switching between halide and Grignard reagent undisclosed (B-12); characterization via "and/or" construction (B-13).
- Kumada 1976b: GLPC column temperature, carrier gas, detector type absent (B4); calibration curves and response factors absent (B5); internal standard changes between experiments without cross-validation (B9); yield exceeds conversion in one entry (U3: 81% yield vs 80% conversion, mathematical impossibility).
- Mazet 2021: IR band monitored in VTNA not specified (B5); no within-condition replicates for any kinetic run (B4); NMR yields without uncertainty estimates across the scope table (B17); "excellent mass balance" stated qualitatively without numerical value (B14).

---

**RP-3: Selectivity or scope claims without complete byproduct accounting**

Each paper asserts selectivity or scope as a defining feature of its method/system, but none provides full mass balance or complete byproduct characterization for the claimed selective process.

evidence_chain: [Kumada_1972 : B-1, U-1, C-1 | Kumada_1976b : B2, B7 | Mazet_2021 : B9, B17]

- Kumada 1972: "selective" cross-coupling is the title and central claim, yet homo-coupling product R–R (predicted by the paper's own mechanism, eq 3) is never reported, quantified, or even acknowledged as untested (B-1, U-1). Prior art comparison is qualitative (C-1).
- Kumada 1976b: the principal limitation (alkyl Grignard + dihaloethylene) is named but uncharacterized — "mixture of products, usually homo coupling predominating" with no product identities or yields (B2). Benzene formation (side-reaction index) is not determined for some Table 3 entries (B7).
- Mazet 2021: three substrate-specific scope failures (adamantyl, electron-deficient aryl, cyclopropyl Grignard) are tabulated without mechanistic attribution in a mechanistic study (B9). NMR yields are the primary metric; isolated yields given only for selected examples (B17).

---

**RP-4: Self-contradictory absence — paper's own model predicts observables that are not tested**

All three papers contain at least one instance where a proposed model generates a specific, testable prediction that the paper itself does not test or even acknowledge as untested.

evidence_chain: [Kumada_1972 : U-1, U-2 | Kumada_1976b : U2 | Mazet_2021 : U1, U2, U3]

- Kumada 1972: eq 3 predicts R–R formation in every catalytic turnover — unreported (U-1). Black mixture is consistent with Ni(0) particles undermining the proposed homogeneous cycle — unanalyzed (U-2).
- Kumada 1976b: general claim of β-hydride elimination suppression contradicted by extensive sec→prim isomerization with [Ni(dmpe)Cl₂] — contradiction unacknowledged (U2).
- Mazet 2021: dmpe mechanism predicts selective I-a/III-b cross-over, but stoichiometric experiment yields are consistent with statistical scrambling — discrepancy unacknowledged (U1). X-ray structure of 9c available but phosphate binding mode (κ¹ vs κ²) unreported despite being load-bearing for the "rapid ion exchange" claim (U2). VTNA acknowledged as unreliable due to decomposition, yet mechanistic conclusions are drawn unchanged (U3).

---

**RP-5: Ligand-effect attribution from insufficient experimental basis**

All three papers propose structure–activity relationships for phosphine ligands based on comparisons where multiple variables covary simultaneously.

evidence_chain: [Kumada_1972 : B-3, U-4 | Kumada_1976b : A4, A5 | Mazet_2021 : B10, C3]

- Kumada 1972: activity order [NiCl₂(dpp)] > [NiCl₂(dpe)] > ... → "cis configuration is the first requisite" — inferred from a single substrate (B-3), with chelate size, bite angle, and electronics covarying (U-4).
- Kumada 1976b: dppp vs dppe preference acknowledged as unexplained with "the experimental results at hand" (A4); dmpe anomaly (poor for primary alkyl, best for secondary alkyl) labeled "strange" and left unresolved (A5).
- Mazet 2021: dppe vs dmpe reactivity difference attributed to steric environment (%V_Bur) from a two-point comparison where %V_Bur, σ-donor strength, and bite angle all change simultaneously (B10). Computational barrier predictions invoked but not numerically compared with experimental data (C3).

---

**Cross-field temperature patterns**

temperature_pattern: RP-1 (mechanism validation) | papers: [Kumada_1972, Kumada_1976b, Mazet_2021] | profile_consistency: divergent | note: In Kumada 1972, mechanism validation receives V1=high, V2=critical (B-2); in Kumada 1976b, V2 alone rates A2 as critical (1/3 convergence); in Mazet 2021, the VTNA reliability cluster (B1) receives V1=V2=V3=high (3/4 convergence). The gap's severity INCREASES in terms of multi-agent convergence from 1972 to 2021: what was a single-viewpoint concern in the early papers becomes a field-wide concern in the modern paper.

temperature_pattern: RP-2 (analytical underreporting) | papers: [Kumada_1972, Kumada_1976b, Mazet_2021] | profile_consistency: consistent | note: V3-equivalent agents consistently rate analytical data quality at medium-to-high severity across all three papers; the gap character shifts from "no method stated" (1972) to "method partially stated" (1976) to "method stated but statistical rigor absent" (2021), but severity remains comparably flagged.

temperature_pattern: RP-3 (selectivity w/o byproduct data) | papers: [Kumada_1972, Kumada_1976b, Mazet_2021] | profile_consistency: consistent | note: Kumada 1972 B-1 receives V1=V2=V3=high (3/3 convergence, strongest item); Kumada 1976b B2 receives V1=high×2, V2=high, V3=medium (3/3 convergence). The same mass-balance absence is the most convergent item in both papers.

---

**Same-root group patterns**

recurring_root: Catalytic cycle assembled by analogy rather than validated by system-specific experiment | papers: [Kumada_1972, Kumada_1976b, Mazet_2021] | member_items: [Kumada_1972: SRG-1 (B-2, B-14, U-1, U-2, U-4), Kumada_1976b: SRG-1 (A2, A6, A8, U1, U2, C3, C4), Mazet_2021: SRG-2 (B1, B8, U1, U3)] | note: This is a structural gap rather than a genre convention; it persists because each paper relies on external analogies or partial evidence rather than demonstrating all elementary steps in situ. In 1972/1976, no tools existed for in situ intermediate characterization under catalytic conditions; by 2021, tools were available (NMR, VTNA) but produced ambiguous results.

recurring_root: Quantitative measurement basis underreported | papers: [Kumada_1972, Kumada_1976b, Mazet_2021] | member_items: [Kumada_1972: SRG-3 (B-4, B-8, B-9, B-12, B-13), Kumada_1976b: SRG-3 (B4, B5, B9, U3, B7, B8), Mazet_2021: SRG-1 (B1, B2, B3, B4, B5, B6) + SRG-6 (B13, B14, B15, B17)] | note: This is a genre convention — chemistry journals do not require raw data deposition, uncertainty quantification, or within-condition replication as standard practice. The convention is field-wide, not individually chosen.

recurring_root: Selectivity claim without mass balance | papers: [Kumada_1972, Kumada_1976b] | member_items: [Kumada_1972: SRG-2 (B-1, U-1, C-1), Kumada_1976b: SRG-2 (B2, A1)] | note: This root recurs strongly in the methodology papers (1972, 1976) but is less prominent in the mechanistic paper (2021), which focuses on mechanism rather than scope. Genre convention for methodology papers.

---

**Temporal trajectory of recurring patterns**

temporal_trajectory: RP-1 (mechanism validation) | classification: shifting | transition_point: 2021 (Mazet) | note: 1972–1976: structurally suppressed (no in situ NMR, no VTNA methodology available) → 2021: tools available but evidence remains ambiguous (VTNA compromised by decomposition, resting state unidentified for dmpe), shifting to individually/methodologically chosen gap.

temporal_trajectory: RP-2 (analytical underreporting) | classification: narrowing | transition_point: none (continuous improvement) | note: 1972: no analytical method details at all; 1976: instrument model and column specified but calibration absent; 2021: method (IR-VTNA, NMR) named but replication and statistical rigor absent. Gap progressively addressed but never fully closed.

temporal_trajectory: RP-3 (byproduct accounting) | classification: narrowing | transition_point: 1976 (Kumada 1976b) | note: 1972: no byproduct data at all; 1976: benzene monitored for some entries but not all; 2021: scope failures tabulated but uncharacterized mechanistically. Progressive improvement but complete mass balance never achieved.

temporal_trajectory: RP-4 (self-contradictory absence) | classification: time-invariant | transition_point: n/a | note: Each paper independently generates internal predictions that it does not test: R–R in 1972, β-elimination contradiction in 1976, statistical scrambling vs selective interception in 2021. The specific prediction changes but the structural pattern — proposing a model, deriving a consequence, and not testing it — persists unchanged across 49 years.

temporal_trajectory: RP-5 (ligand effect attribution) | classification: time-invariant | transition_point: n/a | note: 1972: 6-catalyst activity order from 1 substrate → geometric hypothesis. 1976: dppp/dppe preference "difficult to explain." 2021: dppe/dmpe 2-point comparison with 3-variable confound. The insufficient-data-for-multi-variable-attribution pattern is structurally identical across all three papers despite 49 years of intervening ligand development.

---

**Structural suppression vs. individual choice**

RP-1 (mechanism validation):
- *Era-dependent*: structurally suppressed (1972: no in situ NMR, no radical-clock methodology, no VTNA; 1976: same) → individually chosen / methodologically limited (2021: all tools available — in situ NMR, VTNA, radical-clock, X-ray — were deployed but produced incomplete/ambiguous results). The transition point is the emergence of modern in situ spectroscopic and kinetic methodology (post-2000). In the 2021 paper, the gap is no longer that tools are unavailable but that the tools deployed did not fully resolve the question; this places Mazet 2021 at the boundary between "methodologically limited" (tools exist but may be inherently insufficient for this system) and "individually chosen" (additional experiments such as Eyring analysis from available data, or testing the phosphate binding mode from the deposited X-ray structure, could have been performed).

RP-2 (analytical underreporting):
- *Era-dependent*: structurally suppressed (1972, 1976: JACS/BCSJ did not require raw data, calibration curves, or replicate data for publications) → incentive-suppressed (2021: ACS Catalysis allows Supporting Information for full analytical details, but depositing replicate kinetic data and uncertainty ranges would not constitute a publishable contribution in itself; the analytical rigor gap is maintained because no incentive exists to close it independently).

RP-3 (byproduct accounting):
- *Incentive-suppressed*: A comprehensive mass-balance audit of any specific cross-coupling reaction — measuring all byproducts, determining detection limits, and establishing selectivity as a defined metric — would be technically feasible (GCMS) but would not constitute a publishable study under current norms. This has been true since at least 1976 when GLPC was available. No group in the field has published such an audit for Kumada coupling as a standalone study, suggesting the gap is incentive-suppressed rather than individually chosen.

RP-4 (self-contradictory absence):
- *Individually chosen*: In each paper, the untested prediction is derivable from the paper's own model using the paper's own experimental infrastructure. Testing R–R formation (1972, 1976) required only GLPC analysis already being performed. Testing the β-elimination/isomerization relationship (1976) required only an additional control experiment. Testing the statistical scrambling null hypothesis (2021) required only a single-electrophile control. These are individually chosen omissions.

RP-5 (ligand effect attribution):
- *Structurally suppressed*: Deconvoluting steric, electronic, and geometric ligand effects requires a multi-ligand series with systematic variation — a different research program than any single paper typically undertakes. This remains structurally suppressed because the required systematic ligand variation would constitute a separate investigation.

---

**Paradigm competition**

This group reveals a paradigm succession rather than paradigm competition:

**Paradigm 1: Scope-first methodology (1972, 1976)**
The first two papers prioritize demonstrating that Ni-phosphine catalysis enables selective cross-coupling across broad substrate classes. Mechanism is deferred as secondary ("working hypothesis" in 1972; "While much remains to be studied" in 1976). Success is measured by yield coverage.

Systematically unanswered questions:
- What are the elementary steps of the catalytic cycle under actual catalytic conditions?
  evidence_chain: [Kumada_1972 : B-2, B-14 → "working hypothesis"; Kumada_1976b : A2 → "mechanism has not yet been fully clarified"]
- Is the catalysis homogeneous or heterogeneous?
  evidence_chain: [Kumada_1972 : U-2 → "black mixture"; "no textual basis in Kumada_1976b" — the black mixture observation from 1972 is not revisited]

**Paradigm 2: Mechanism-first investigation (2021)**
The 2021 paper prioritizes mechanistic elucidation — intermediate characterization, kinetic analysis, radical probes — for a reaction already established synthetically (ref 6, Fiorito 2018). Success is measured by mechanistic discrimination.

Systematically unanswered questions:
- What is the complete mass balance of the catalytic reaction?
  evidence_chain: ["no textual basis in Mazet_2021" — mass balance is stated qualitatively as "excellent" (B14) but never quantified]
- What is the origin of selectivity (cross-coupling vs homo-coupling)?
  evidence_chain: ["no textual basis in Mazet_2021" — selectivity as a defined metric is not discussed in the mechanistic study]

**Succession relationship:** Paradigm 2's founding problem (mechanism) is precisely Paradigm 1's blind spot (deferred mechanism). Conversely, Paradigm 1's founding contribution (scope) is taken as given by Paradigm 2 (scope data from ref 6 reproduced in Figure 1B without independent verification). Each paradigm's systematic silence is the other paradigm's research program. This is paradigm succession, not competition — the gaps are temporally sequential rather than coexistent.

However, a shared blind spot persists across both paradigms: neither the scope-first nor the mechanism-first paradigm addresses the quantitative analytical basis of its primary data (RP-2). This is a field-wide structural convention that both paradigms accept without examination.

---

**Divergences**

**DV-1: Genre-driven depth of reporting**
The 1972 communication (3 pp) compresses all evidentiary gaps into a dense set of reporting omissions (14 B-items); the 1976 full paper (12 pp) partially addresses some gaps (explicit experimental section, GLPC instrument model, catalyst aging data) but introduces new ones (U3: yield > conversion inconsistency); the 2021 full paper (10 pp + SI) deploys sophisticated tools but introduces a new class of gaps (VTNA statistical validity, SRG-1).

evidence_chain: [Kumada_1972 : B-4 (no GLPC conditions at all) vs Kumada_1976b : B4 (partial GLPC conditions) vs Mazet_2021 : B5 (no IR band specification despite VTNA centrality)]

**DV-2: Treatment of mechanistic uncertainty**
Kumada 1972 labels its mechanism a "working hypothesis[REDACTED: substantial verbatim quotation; see Tier 9]can be rationalized by Scheme 1[REDACTED: substantial verbatim quotation; see Tier 9]we establish") and dmpe ("hypothesis... corroborated") — the most epistemically differentiated language, yet the "established" dppe cycle contains its own undervalidated element (ion exchange, D-4-2 of S2).

evidence_chain: [Kumada_1972 : B-2 → "working hypothesis" in last sentence only | Kumada_1976b : A2 → "can be rationalized by" | Mazet_2021 : B1, B8 → "we establish" (dppe) vs "the order in catalyst must be taken with care" (dmpe)]

**DV-3: Self-contradictory absence type**
The character of self-contradictory absence shifts across papers. In 1972, it involves the paper's own mechanism predicting a byproduct (R–R) that is not reported. In 1976, it involves an empirical observation (isomerization) that contradicts a stated generalization (β-suppression). In 2021, it involves quantitative data (stoichiometric yields, VTNA decomposition) being used to support a hypothesis despite being acknowledged as unreliable for that purpose.

evidence_chain: [Kumada_1972 : U-1 (model → prediction → prediction untested) | Kumada_1976b : U2 (observation contradicts generalization) | Mazet_2021 : U3 (data acknowledged unreliable → conclusions drawn unchanged)]

---

**U-item patterns**

recurring_U: Self-contradictory absence involving mechanism-derived predictions | papers: [Kumada_1972, Kumada_1976b, Mazet_2021] | item_ids: [Kumada_1972: U-1, U-2; Kumada_1976b: U2; Mazet_2021: U1, U3] | note: Recurring across all three papers as U-items (not classifiable as A/B/C) suggests that the A/B/C framework captures reporting omissions and methodological limitations but does not naturally accommodate the specific structure of "model generates prediction → prediction untested → model retained." This is a gap in the classification framework itself: self-contradictory absence is a distinct epistemic category.

---

**Self-contradictory absence patterns**

self_contradictory: [Kumada_1972] : Ni(0)/Ni(II) catalytic cycle (eqs 2–4) → predicts R–R homo-coupling product in every turnover (eq 3) → R–R neither reported, quantified, nor acknowledged as untested | item_id: U-1

self_contradictory: [Kumada_1972] : Homogeneous Ni(0)/Ni(II) molecular cycle proposed → "black mixture" observation consistent with Ni(0) nanoparticle formation → observation recorded without analysis or acknowledgment of its mechanistic implications | item_id: U-2

self_contradictory: [Kumada_1976b] : β-hydride elimination claimed as generally suppressed in Ni-alkyl intermediates (A8) → extensive secondary-to-primary isomerization observed with [Ni(dmpe)Cl₂] (requires β-hydride elimination/reinsertion) → contradiction unacknowledged; treated as independent anomaly | item_id: U2

self_contradictory: [Mazet_2021] : dmpe mechanism predicts selective interception of I-a by III-b → stoichiometric experiment (Figure 9) yields near-equal products from both electrophilic partners (1a: 7%/8%; 8a: 17%/8%) → pattern consistent with statistical scrambling but presented as supporting selective interception | item_id: U1

self_contradictory: [Mazet_2021] : "rapid phosphate/bromide ion exchange" proposed as key dppe cycle feature → X-ray structure of 9c deposited (CCDC 2116220) containing Ni–O bond geometry → phosphate binding mode (κ¹ vs κ²) — which determines exchange lability — unreported in main text | item_id: U2

self_contradictory: [Mazet_2021] : VTNA catalyst-order determination acknowledged as unreliable due to decomposition ("must be taken with care") → apparent first-order (dppe) and apparent second-order (dmpe) used as the mechanistic basis for proposing two fundamentally different catalytic cycles → no alternative mechanism tested against the same kinetic data | item_id: U3

**Recurring pattern assessment:** The self-contradictory absence pattern recurs in all three papers across 49 years. This reflects a **narrative function of mechanism diagrams in cross-coupling papers**: catalytic cycles serve to organize and contextualize scope/selectivity data rather than to generate testable predictions. When the cycle does generate a testable prediction (R–R formation, homogeneity, β-suppression universality, selective interception), the prediction is not treated as a hypothesis to be tested but as an implication to be noted and passed over. This is simultaneously a **genre convention** (mechanism sections in methodology and mechanistic papers alike are expected to propose cycles, not to falsify them) and a **genuine analytical gap** (each untested prediction could be tested with the paper's own infrastructure). The convention persists because testing one's own mechanistic proposal against its predictions would either (a) confirm it (unpublishable) or (b) falsify it (requiring a revised mechanism that would constitute a different paper). The incentive structure of publication thus preserves self-contradictory absence as a stable feature of the literature.

---

**Group-level unasked question**

[REDACTED: substantial verbatim quotation; see Tier 9]

evidence_chain: [Kumada_1972 : B-1 (selectivity w/o byproduct data), U-1 (R–R predicted but unreported), B-4 (analytical conditions absent) | Kumada_1976b : B4 (GLPC conditions incomplete), B5 (calibration absent), U3 (yield > conversion), U1 (MgXX' fate unknown) | Mazet_2021 : B1 (VTNA order unreliable), B5 (IR band unspecified), B8 (dmpe resting state unidentified), B14 (mass balance qualitative)]

TEMPERATURE_SUMMARY correspondence: In Kumada 1972, B-1 (selectivity w/o byproduct data) is the sole high_convergence_low_gap item with 3/3 convergence. In Kumada 1976b, B2 (dihaloethylene limitation with no product data) is the strongest convergence item at 3/3. Both are instances of the group-level question — what is actually formed, in what amounts, under what conditions? The absence of a complete product/intermediate profile is the single gap that, if filled, would simultaneously resolve the selectivity question (1972), the scope limitation question (1976), and the kinetic order ambiguity (2021).

recurring_root correspondence: The group-level unasked question subsumes recurring_root 1 (catalytic cycle validation) and recurring_root 2 (quantitative measurement basis) as two facets of a single underlying deficit: the field has never produced a complete, time-resolved, quantitatively validated account of all species present during Ni-diphosphine Kumada coupling. The 1972 and 1976 papers lacked the tools; the 2021 paper possessed the tools but focused on mechanism discrimination rather than comprehensive speciation.

---

*End of G1 output.*

---

> **Tier 8 redaction notice**: This file is a redacted copy of the corresponding Tier 3 / Tier 9 output. Verbatim source-paper quotations have been replaced by `[REDACTED: see source paper §<loc>; full text retained in Tier 9 reviewer-only deposit]` markers, preserving location references and our own analytical content. Bibliographic fields (title, authors, journal, year, DOI), analytical labels (`evidence_chain:` with B-/U-/A-/C- internal IDs), short technical terms, and our own analytical text are not redacted. The redaction was applied by `scripts/redact_for_tier8.py` and, for this version, by `scripts/build_paperA_R1_public.py` with `scripts/redact_source_ngram_runs.py` (scripts of the project repository; they are not deposited).
