prompt_version: stage2f-v7-20260417

---

**[F. Within-Group Comparison]**

**Group composition:** G1 — Direct lineage (dpe/dppe-Ni system, 1972–2021), prompt v18.4 / Sonnet S0–S3v2 inputs
- Kumada 1972 (JACS Communication, 3 pp): method discovery via [NiCl₂(dpe)] catalysis
- Kumada 1976b (BCSJ Full Paper, 12 pp): general scope and limitations across ~60 entries with [Ni(dppp)Cl₂] benchmark
- Mazet 2021 (ACS Catal. Full Paper, 10 pp): comparative dppe/dmpe mechanistic study on enol phosphate vinylation

---

**Repeated patterns**

**RP-1: Catalytic cycle proposed without independent system-specific validation**

All three papers advance a Ni(0)/Ni(II) catalytic cycle for their respective systems and in each case the cycle is constructed by importing organonickel precedent rather than by closing the loop on every elementary step within the actual reaction system reported. Even in 2021, where modern in-situ tools were deployed, the cycle is supported by partial evidence (X-ray of one OA complex; one stoichiometric proof-of-concept) rather than by integrated kinetic and spectroscopic confirmation of every intermediate.

evidence_chain: [Kumada_1972 : A-2, B-12, U-1, U-2 | Kumada_1976b : A-1, A-1d, U-1, U-2, C-7, C-4 | Mazet_2021 : A-3, B-5, B-6, U-1, U-2]

- Kumada 1972: cycle in eqs 2–4 imported by analogy from stoichiometric (dipy)Ni reactions (refs 11–12); intermediates 1, 2, 3 unobserved under [NiCl₂(dpe)] conditions; black mixture in Example 1 unanalyzed (B-12, U-2); cycle predicts R–R unreported (U-1).
- Kumada 1976b: Scheme 1 acknowledged as "rationalization" of results, with the authors stating mechanism "has not yet been fully clarified"; premises of Scheme 1 imported from Jolly-Wilke organonickel chemistry (ref. 31, C-4); competing Felkin-Corriu Ni(0) oxidative-addition mechanism acknowledged but not experimentally excluded (C-7); yellow species from [Ni(dppp)Cl₂] + n-BuMgBr identified only by color despite being a likely resting-state intermediate of Scheme 1.
- Mazet 2021: dppe cycle anchored by X-ray of OA complex 9c; dmpe cycle relies on apparent second-order kinetics from a three-point VTNA dataset under acknowledged catalyst decomposition (B-5); proposed bimetallic Ni–Ni transmetalation step (I-a + III-b → IV) lacks DFT corroboration and is not numerically integrated into a rate law that reproduces the observed orders (U-1).

---

**RP-2: Quantitative analytical basis for primary measurements systematically underspecified**

All three papers ground their headline numbers (yields, conversions, kinetic orders, selectivity ratios) in instrumental measurements whose reliability cannot be evaluated independently from the published data. The specific deficit shifts across decades but the structural absence is conserved.

evidence_chain: [Kumada_1972 : B-2, B-7, B-9, B-11 | Kumada_1976b : B-1, B-2, B-10, B-5 | Mazet_2021 : B-5, B-7, B-6]

- Kumada 1972: glpc internal standard and response factors undisclosed (B-2); characterization via "and/or" formulation (B-7); all yields single determinations (B-9); cis:trans ratio analytical method unstated (B-11).
- Kumada 1976b: GLPC response factor data absent for all ~60 entries (B-10); internal standard identity inconsistent across tables (B-1); Table 2 entry sums to 104% (mass balance violation, B-2); Table 7 mixes yield bases and denominators without reconciling legend (B-5).
- Mazet 2021: three-point VTNA dataset for second-order assignment without goodness-of-fit statistics (B-5); Grignard reagent order undefined and Schlenk-equilibrium speciation uncharacterized (B-7); stoichiometric Figure 9 experiment with ~75–85% mass balance unaccounted (B-6).

---

**RP-3: Selectivity / scope claims without complete byproduct accounting**

Each paper makes selectivity central to its identity yet declines to fully account for byproducts that its own logic predicts.

evidence_chain: [Kumada_1972 : B-1, B-6, U-1 | Kumada_1976b : A-2, B-2, U-3, U-4 | Mazet_2021 : B-1, B-6, U-3]

- Kumada 1972: "selective" cross-coupling is the title and central claim; eq 3 explicitly predicts R–R homo-coupling product, which is never reported, quantified, or acknowledged as below detection limit (U-1, B-6).
- Kumada 1976b: "most serious limitation" — alkyl Grignard + dihaloethylene gives "complex mixture, usually homo coupling predominating" — never characterized for product identity or yield distribution (A-2, U-4); β-hydride suppression invoked as mechanistic feature, but olefin byproducts (1-butene, 2-butene) are not systematically searched for (U-3); >50 substrate entries from Fiorito 2018 referenced without failure analysis (B-1).
- Mazet 2021: scope failures (adamantyl 1d, electron-deficient aryl, cyclopropyl Grignard 2b, isomerization with 2c) flagged in Introduction but never mechanistically rationalized within the proposed dmpe cycle (A-7); Figure 9 stoichiometric experiment leaves ~75–85% of material unexplained (B-6); radical-clock and TEMPO non-detection used as positive mechanistic evidence without quantifying detection sensitivity (U-3).

---

**RP-4: Self-contradictory absence — paper's own model predicts observables that are not tested or whose results contradict the model**

In each paper a proposed model generates a specific, testable prediction that the paper either does not test, or tests with a result inconsistent with the model that is then explained away rather than acknowledged as tension.

evidence_chain: [Kumada_1972 : U-1, U-2 | Kumada_1976b : U-1, U-2, U-3, U-5 | Mazet_2021 : U-1, U-2, U-3, U-4]

- Kumada 1972: eq 3 predicts R–R formation per turnover, unreported (U-1); homogeneous Ni(II) cycle proposed, black mixture observed but unanalyzed (U-2).
- Kumada 1976b: Scheme 1 predicts normal C–X reactivity order, but [Ni(dppp)Cl₂] gives anomalous PhI>PhCl>PhBr labelled "difficult to explain" rather than a Scheme 1 challenge (U-2); β-hydride suppression claim invoked as mechanistic feature contradicted by extensive sec→prim isomerization with [Ni(dmpe)Cl₂] (U-3 in S2_en mapping; aligns with kumada1976b U-3); landmark C–F oxidative addition claim asserted with zero isolated yield and via an analytical method declared inapplicable in the adjacent table (U-5); crossover experiment that would distinguish Scheme 1 from Felkin-Corriu absent (U-1).
- Mazet 2021: dmpe mechanism predicts selective interception of I-a by III-b but stoichiometric experiment (Figure 9, 7–17% / 8% yields) is consistent with statistical scrambling and is presented as supporting selective interception (U-1); VTNA acknowledged as unreliable due to deactivation, yet mechanistic conclusions drawn unchanged (U-2); X-ray of 9c acquired but phosphate binding mode (κ¹ vs κ²) — load-bearing for the "rapid ion exchange" claim — unreported in main text; E/Z reversal (40:60 → 4:96) within paper's own dataset never returned to in mechanistic section (U-4).

---

**RP-5: Ligand-effect attribution from insufficient experimental basis**

Each paper offers structure–activity attribution for phosphine ligands from comparisons in which multiple variables (chelate size, bite angle, σ-donor strength, steric bulk) covary simultaneously.

evidence_chain: [Kumada_1972 : B-3, U-4 | Kumada_1976b : A-5, B-11 | Mazet_2021 : B-3, B-4]

- Kumada 1972: 6-catalyst activity order [NiCl₂(dpp)] > [NiCl₂(dpe)] > … inferred from one substrate (n-BuMgBr + PhCl); cis-geometry hypothesis ("first requisite") drawn without isolating geometric, electronic, and steric contributions.
- Kumada 1976b: dppp vs dppe preference acknowledged as not explainable "with the experimental results at hand" (A-5 in S2 mapping); dmpe anomaly (poor for primary alkyl, best for secondary alkyl) labelled "strange"; aryl-halide reactivity ranked qualitatively by "exothermicity of reactions" (B-11).
- Mazet 2021: dppe vs dmpe OA reactivity difference attributed to %V_Bur measured in non-catalytic cod complexes (7c/7d; 48.9 vs 43.1) rather than in OA complex 9c whose X-ray is in hand (B-3); steric vs electronic decomposition for adamantyl 1d failure asserted, not measured (B-4).

---

**RP-6: Genre-induced labeling mismatch — hypothesis vocabulary at one location, factual verbs elsewhere**

All three papers display the labeling-mismatch pattern: a hypothesis label is concentrated at one rhetorical location while declarative or near-factual verbs predominate around the same content elsewhere.

evidence_chain: [Kumada_1972 : B-2, A-1 final sentence | Kumada_1976b : A-1, A-1d | Mazet_2021 : A-3, Conclusions]

- Kumada 1972: "working hypothesis[REDACTED: substantial verbatim quotation; see Tier 9]reacts with," "is converted to," "is regenerated").
- Kumada 1976b: hedging "can be rationalized by Scheme 1" coexists with substantive narrative drawing mechanistic conclusions (β-hydride suppression as feature, "two or more rate-limiting steps" inference) presented without parallel hedging.
- Mazet 2021: Results section uses "we propose" and "must be analyzed cautiously" for the bimetallic TM step; Conclusions reverts to "transmetalation is likely to occur between vinyl nickel intermediates" and "we establish" for the dppe cycle whose ion-exchange element (D-4-2 of S3v2) contains its own undervalidated component.

---

**Cross-field temperature patterns**

temperature_pattern: RP-1 (mechanism validation) | papers: [Kumada_1972, Kumada_1976b, Mazet_2021] | profile_consistency: divergent | note: In Kumada 1972, mechanism validation receives V1=high, V2=high (A-2; convergence 2/3). In Kumada 1976b, V2 alone rates A-1 high; but downstream cluster (B-3, U-5, A-6 around C–F) reaches V1=high + V3=high (2/3). In Mazet 2021, the bimetallic TM cluster (A-3, B-5) achieves V1=V2=V3=high (3/3 convergence). The gap's multi-agent severity rises across the 49-year span: a single-viewpoint concern in 1972 becomes a field-wide cross-disciplinary concern in 2021, even as the absolute tools available have improved.

temperature_pattern: RP-2 (analytical underreporting) | papers: [Kumada_1972, Kumada_1976b, Mazet_2021] | profile_consistency: consistent | note: V3-equivalent agents flag analytical-quality items at medium-to-high severity in all three papers; the gap character shifts from "no method stated" (1972) → "method partially stated, mass balance violated" (1976) → "method stated but statistical rigor and speciation absent" (2021). Severity is comparably flagged across eras; only the gap's specific manifestation changes.

temperature_pattern: RP-3 (selectivity / mass balance) | papers: [Kumada_1972, Kumada_1976b, Mazet_2021] | profile_consistency: consistent | note: Kumada 1972 B-1 receives V1=V2=V3=medium (3/3). Kumada 1976b B-2 / B-5 receive 2/3 convergence at medium. Mazet 2021 B-6 receives V1=V2=high (2/3). The mass-balance / selectivity-without-byproduct-data gap is the most reliably co-flagged content type across the three papers.

temperature_pattern: RP-4 (self-contradictory absence) | papers: [Kumada_1972, Kumada_1976b, Mazet_2021] | profile_consistency: consistent | note: All three papers contain at least one U-item flagged at high severity by the mechanistic agent (V2). Mazet 2021 has the strongest convergence (U-1 critical) but the structural pattern — a model generates a prediction, the paper does not test it (or tests it with a result inconsistent with the model and explains it away) — is conserved across all three papers.

temperature_pattern: RP-5 (ligand attribution) | papers: [Kumada_1972, Kumada_1976b, Mazet_2021] | profile_consistency: consistent | note: V1 and V2 flag the multi-variable confound at medium-to-high severity in all three; the structural confound (covarying parameters) is era-invariant.

---

**Same-root group patterns**

recurring_root: Catalytic cycle assembled by analogy or imported model rather than validated by system-specific elementary-step characterization | papers: [Kumada_1972, Kumada_1976b, Mazet_2021] | member_items: [Kumada_1972 SRG-1: A-2, U-1, U-2, B-12 | Kumada_1976b SRG-1: A-1, A-1d, U-1, U-2, C-7 (with C-4 as authority anchor) | Mazet_2021 SRG-2: A-3, B-6, C-3 (bimetallic TM); SRG-1: kinetic foundation under deactivation] | note: This is a structural gap (RI-06 imported model + RI-03 unobserved explanatory in Stage 3 mapping), not a genre convention. In 1972/1976 in-situ characterization tools for catalytic intermediates were largely unavailable, making the gap structurally suppressed; by 2021 the tools exist (³¹P NMR, VTNA, X-ray, DFT), but their deployment in this specific system produced ambiguous or partial results, shifting the gap toward methodologically limited / individually chosen.

recurring_root: Quantitative measurement basis underreported | papers: [Kumada_1972, Kumada_1976b, Mazet_2021] | member_items: [Kumada_1972 SRG-5: B-2, B-7, B-9, B-11 | Kumada_1976b SRG-2: B-1, B-2, B-10, B-5 | Mazet_2021 SRG-1 + within-paper kinetic foundation: B-5, B-7] | note: This is field-wide genre convention. Chemistry journals have not enforced raw-data deposition, response-factor tables, replicate measurements, or speciation analysis as standard requirements. The convention spans 49 years across two journals (JACS, BCSJ, ACS Catal.), three countries, and a complete change of analytical infrastructure (glpc → in-situ IR + NMR + VTNA), confirming the field-wide rather than instrument-bound nature of the convention.

recurring_root: Selectivity claim without mass-balance closure | papers: [Kumada_1972, Kumada_1976b, Mazet_2021] | member_items: [Kumada_1972 SRG-2: B-1, B-6, U-1 | Kumada_1976b SRG-6: A-2, U-4 (dichloroethylene/alkyl failure) | Mazet_2021 B-6 + Figure 9 cluster] | note: Recurs in all three papers but with shifting prominence: dominant in the methodology papers (1972, 1976) where selectivity is the headline claim; less prominent but still present in the mechanistic paper (2021) where mass-balance closure becomes a discriminating test for the proposed bimetallic mechanism rather than a primary selectivity claim. Both genre convention and structural gap.

recurring_root: Self-contradictory absence around mechanism-derived predictions | papers: [Kumada_1972, Kumada_1976b, Mazet_2021] | member_items: [Kumada_1972: U-1, U-2 | Kumada_1976b: U-1, U-2, U-3, U-5 | Mazet_2021: U-1, U-2, U-3, U-4] | note: Recurs in all three papers as U-items not classifiable as A/B/C, suggesting that the A/B/C framework captures reporting omissions and methodological limitations but does not naturally accommodate the structure of [REDACTED: substantial verbatim quotation; see Tier 9] This is a gap in the classification framework itself: self-contradictory absence is a distinct epistemic category and a stable feature of cross-coupling mechanism narratives across 49 years.

recurring_root: Ligand structure–activity attribution from confounded comparisons | papers: [Kumada_1972, Kumada_1976b, Mazet_2021] | member_items: [Kumada_1972: B-3, U-4 | Kumada_1976b: A-5, B-11 | Mazet_2021: B-3, B-4 / CLA-2] | note: Structurally suppressed across all three papers: deconvoluting steric, electronic, and geometric ligand effects requires a multi-ligand systematic series, which is a different research program than any single paper undertakes.

---

**Temporal trajectory of recurring patterns**

temporal_trajectory: RP-1 (mechanism validation) | classification: shifting | transition_point: 2021 (Mazet) | note: 1972–1976: structurally suppressed (no in-situ NMR, no VTNA, no DFT routinely available for catalytic intermediates) → 2021: tools available but their deployment yielded ambiguous evidence (VTNA compromised by decomposition; resting state for dmpe unidentified; X-ray of one intermediate 9c established but not used for OA-geometry steric maps). Gap shifts from structurally suppressed to methodologically limited / individually chosen.

temporal_trajectory: RP-2 (analytical underreporting) | classification: narrowing | transition_point: none (continuous improvement) | note: 1972: no analytical method details. 1976: instrument and column specified but calibration absent and mass-balance violation present. 2021: methods named (VTNA, in-situ IR, NMR, X-ray, SambVca, DFT) but goodness-of-fit statistics, Schlenk speciation, and replication absent. Continuous improvement, never closed.

temporal_trajectory: RP-3 (mass balance) | classification: narrowing | transition_point: 1976 (Kumada 1976b benzene quantified for some entries) | note: 1972: no byproduct data. 1976: benzene monitored for some Table 1/2 entries but not all; one entry sums to 104%. 2021: scope failures tabulated and bimetallic Figure 9 yields reported but ~75–85% unaccounted. Progressive improvement, never complete.

temporal_trajectory: RP-4 (self-contradictory absence) | classification: time-invariant | transition_point: n/a | note: Each paper independently generates internal predictions that it does not test or whose tests yield results inconsistent with the model: R–R in 1972; β-elimination contradiction and anomalous reactivity order in 1976; statistical scrambling vs selective interception, VTNA-under-decomposition retention, and unanalyzed E/Z reversal in 2021. Specific predictions change but the structural pattern persists unchanged across 49 years.

temporal_trajectory: RP-5 (ligand attribution) | classification: time-invariant | transition_point: n/a | note: 1972: 6-catalyst activity order from one substrate → geometric hypothesis. 1976: dppp/dppe preference "difficult to explain"; dmpe anomaly "strange." 2021: dppe/dmpe two-point %V_Bur comparison from non-catalytic cod complexes with three covarying variables. Pattern structurally identical despite 49 years of intervening ligand-development infrastructure.

temporal_trajectory: RP-6 (labeling mismatch) | classification: time-invariant | transition_point: n/a | note: All three papers concentrate hypothesis vocabulary at one rhetorical location while letting declarative / near-factual verbs dominate the surrounding mechanistic narrative. Conserved across journal (JACS, BCSJ, ACS Catal.), language community, and decade.

---

**Structural suppression vs. individual choice**

RP-1 (mechanism validation): *Era-dependent.* Structurally suppressed 1972–1976 (no in-situ tools); shifts toward individually chosen / methodologically limited by 2021 (tools exist, deployed, gave incomplete answer). Mazet 2021 sits at the boundary: additional individually-chosen experiments (DFT for bimetallic TS; numerical kinetic integration; OA-geometry %V_Bur) could have been performed.

RP-2 (analytical underreporting): *Era-dependent.* Structurally suppressed 1972/1976 (journal conventions did not require raw data, calibration tables, replication) → incentive-suppressed 2021 (ACS Catal. Supporting Information allows full disclosure, but a study whose contribution is [REDACTED: substantial verbatim quotation; see Tier 9] would not constitute publishable contribution; the gap is preserved because no incentive exists to close it independently).

RP-3 (mass balance / selectivity): *Incentive-suppressed.* A comprehensive mass-balance audit of any specific Ni-Kumada coupling — measuring all byproducts, establishing detection limits, defining selectivity as a quantitative metric — has been technically feasible since at least 1976 and certainly since 2000, but no group has published such an audit as a standalone study. The gap is incentive-suppressed rather than individually chosen.

RP-4 (self-contradictory absence): *Individually chosen.* In every paper, the untested prediction or unaddressed contradiction is derivable using the paper's own infrastructure. Testing R–R formation (1972, 1976) required only the glpc already in use. Testing β-elimination/isomerization relationship (1976) required one additional control. Testing the statistical scrambling null hypothesis (2021) required one single-electrophile control. Computing %V_Bur for the OA complex 9c (2021) required one additional SambVca run on data already deposited.

RP-5 (ligand attribution): *Structurally suppressed.* Deconvoluting steric, electronic, and geometric effects requires a multi-ligand systematic series — a different research program than any single paper typically undertakes. Era-invariant.

RP-6 (labeling mismatch): *Genre convention / incentive-suppressed.* Hypothesis vocabulary at one location with declarative verbs elsewhere is reinforced by reviewer expectations: a fully hedged manuscript reads as undercommitted; a fully declarative manuscript reads as overclaimed. The labeling-mismatch convention is the equilibrium between these incentives.

---

**Paradigm competition**

This group reveals a paradigm succession rather than paradigm competition.

**Paradigm 1: Scope-first methodology (1972, 1976).**
Both Kumada papers prioritize demonstrating that Ni-phosphine catalysis enables selective cross-coupling across broad substrate classes. Mechanism is deferred as secondary ("working hypothesis" 1972; "Scheme 1 rationalizes" 1976). Success metric: yield coverage.

Systematically unanswered questions:
- What are the elementary steps of the catalytic cycle under actual catalytic conditions?
  evidence_chain: [Kumada_1972 : A-2 → [REDACTED: substantial verbatim quotation; see Tier 9] | Kumada_1976b : A-1 → [REDACTED: substantial verbatim quotation; see Tier 9]]
- What is the complete mass balance of the catalytic reaction?
  evidence_chain: [Kumada_1972 : B-1, U-1 → no homo-coupling product reported | Kumada_1976b : B-2 → Table 2 sums to 104%, "no textual basis in Kumada_1976b" for full mass-balance closure]
- Is the catalysis homogeneous or heterogeneous?
  evidence_chain: [Kumada_1972 : U-2 → "black mixture" | "no textual basis in Kumada_1976b" — black-mixture observation from 1972 not revisited; aging experiment Table 2 establishes activity persistence over 16 h but does not characterize the species]

**Paradigm 2: Mechanism-first investigation (2021).**
Mazet 2021 prioritizes mechanistic discrimination — intermediate characterization, kinetic analysis, radical probes — for a reaction already established synthetically (ref 6, Fiorito 2018). Success metric: mechanistic discrimination between competing manifolds (Ni(0)/Ni(II) vs Ni(I)/Ni(III); Scheme 1 vs Felkin-Corriu; classical TM vs bimetallic TM).

Systematically unanswered questions:
- What is the complete mass balance of the catalytic reaction?
  evidence_chain: ["no textual basis in Mazet_2021" — mass balance qualitative as "excellent" (Figure 4 dppe section) but never quantified; Figure 9 leaves ~75–85% unaccounted (B-6)]
- What is the origin of cross/homo selectivity as a quantitative metric?
  evidence_chain: ["no textual basis in Mazet_2021" — selectivity as a defined metric is absent from the mechanistic study]
- What is the basis for substrate failures (cyclopropyl Grignard 2b, isomerization with 2c, adamantyl 1d) within the proposed dmpe cycle?
  evidence_chain: [Mazet_2021 : A-7, B-4 → flagged in Introduction as motivating the study, never revisited in mechanistic Results]

**Succession relationship:** Paradigm 2's founding problem (mechanism) is precisely Paradigm 1's blind spot (deferred mechanism). Paradigm 1's founding contribution (scope) is taken as given by Paradigm 2 (scope reproduced from Fiorito 2018 in Figure 1B without independent verification). Each paradigm's systematic silence is the other paradigm's research program. This is paradigm succession, not competition — the gaps are temporally sequential rather than coexistent.

**Shared blind spot persisting across both paradigms:** Neither the scope-first nor the mechanism-first paradigm closes the quantitative analytical foundation of its primary data (RP-2, recurring_root #2). This is a field-wide structural convention that both paradigms accept without examination, surviving the change of journal, the change of analytical infrastructure (glpc → VTNA), and the change of decade.

---

**Divergences**

**DV-1: Genre-driven depth of reporting.**
The 1972 Communication (3 pp) compresses 14 evidentiary gaps into a dense reporting omission set; the 1976 Full Paper (12 pp) partially addresses some (experimental section, GLPC instrument model, catalyst aging data) but introduces new ones (Table 2 mass-balance violation; PhF analytical inconsistency) and creates a landmark claim (first C–F oxidative addition) that the paper itself analytically undermines; the 2021 Full Paper (10 pp + SI) deploys sophisticated tools but introduces a new class of gaps (VTNA validity under decomposition; bimetallic TM mass-balance gap; %V_Bur from non-catalytic intermediate).

evidence_chain: [Kumada_1972 : B-2 (no GLPC conditions) vs Kumada_1976b : B-1 (GLPC conditions partial) vs Mazet_2021 : B-5 (statistical adequacy of three-point dataset)]

**DV-2: Treatment of mechanistic uncertainty.**
Kumada 1972 labels its mechanism a "working hypothesis[REDACTED: substantial verbatim quotation; see Tier 9]can be rationalized by Scheme 1[REDACTED: substantial verbatim quotation; see Tier 9]two or more rate-limiting steps[REDACTED: substantial verbatim quotation; see Tier 9]we establish") and dmpe ("we propose," "must be analyzed cautiously") — the most epistemically differentiated language across the three papers — yet the "established" dppe cycle's ion-exchange element retains its own undervalidated component (κ¹ vs κ² phosphate binding mode unreported despite X-ray availability).

evidence_chain: [Kumada_1972 : "working hypothesis[REDACTED: substantial verbatim quotation; see Tier 9]can be rationalized by Scheme 1" | Mazet_2021 : A-3 → "we propose" (dmpe) vs Conclusions "transmetalation is likely to occur" / "we establish" (dppe)]

**DV-3: Self-contradictory absence type.**
The character of self-contradictory absence shifts across papers. 1972: model-predicts-byproduct, byproduct-not-reported (R–R via eq 3). 1976: empirical-observation-contradicts-stated-generalization (sec→prim isomerization with [Ni(dmpe)Cl₂] under a stated β-hydride-suppression generalization; anomalous PhI>PhCl>PhBr order under Scheme 1's expected normal order). 2021: data-acknowledged-unreliable, conclusions-drawn-unchanged (VTNA decomposition acknowledgment paired with mechanistic conclusions; Figure 9 yield distribution consistent with statistical scrambling presented as supporting selective interception; X-ray of 9c acquired but binding-mode characterization unreported).

evidence_chain: [Kumada_1972 : U-1 (model→prediction→untested) | Kumada_1976b : U-2 (Scheme 1 prediction contradicted) + U-3 (β-suppression contradicted) | Mazet_2021 : U-2 (data-unreliable, conclusions-unchanged) + U-4 (E/Z reversal unanalyzed)]

**DV-4: Layered claim architecture explicitness.**
Layer architecture is implicit in 1972 (synthetic utility vs working-hypothesis mechanism) and 1976 (scope vs Scheme 1 vs C–F landmark vs β-hydride suppression — four implicit layers). It becomes explicit in 2021 (Layer A Ni(0)/Ni(II) manifold + Layer B dppe ion-exchange + Layer C dmpe bimetallic TM, with Layer C structurally fragile by acknowledgment). Layered architecture has become more visible across the 49 years, but the structural pattern of placing the most novel claim on the most fragile layer is conserved.

evidence_chain: [Kumada_1972 : Stage 3 §1 layered structure (Layer 1 + Layer 2) | Kumada_1976b : Stage 3 §1 (4 layers) | Mazet_2021 : Stage 3 §1 (3 layers, Layer C explicitly fragile)]

---

**U-item patterns**

recurring_U: Self-contradictory absence involving mechanism-derived predictions | papers: [Kumada_1972, Kumada_1976b, Mazet_2021] | item_ids: [Kumada_1972: U-1, U-2 | Kumada_1976b: U-1, U-2, U-3, U-5 | Mazet_2021: U-1, U-2, U-3, U-4] | note: Recurs across all three papers as U-items (not classifiable as A/B/C). This recurring U pattern signals that the A/B/C framework captures reporting omissions, scope deferrals, and severed citations but does not naturally accommodate the specific structure of [REDACTED: substantial verbatim quotation; see Tier 9] Self-contradictory absence is a distinct epistemic category. The framework gap is conserved across journal, era, and analytical infrastructure.

recurring_U: Available-but-unutilized characterization | papers: [Kumada_1976b, Mazet_2021] | item_ids: [Kumada_1976b: U-8 (yellow species color-only despite NMR/UV-vis available) | Mazet_2021: U-5 (fluxional assignment for 6c at 298 K co-circular with NMR-only Ni(I) exclusion); CLA-2 (X-ray of 9c not used for OA-geometry %V_Bur)] | note: A subtype of self-contradictory absence in which the necessary characterization tool is available (and in some cases data have been acquired) but the analysis is not performed. Distinct from era-suppressed analytical limitation (RP-2 in 1972). Implication: the A/B/C framework should consider an "available-but-unutilized" subclass within U or B-items.

recurring_U: Mechanistic discrimination test absent for competing mechanisms | papers: [Kumada_1976b, Mazet_2021] | item_ids: [Kumada_1976b: U-1 (crossover experiment for Scheme 1 vs Felkin-Corriu absent) | Mazet_2021: U-1 (kinetic model integration absent for bimetallic TM); CLA-1 (radical-clock without rate constant)] | note: When two mechanisms are formally consistent with the same data, the discriminating experiment is structurally privileged information and its absence is more consequential than a generic missing experiment. This pattern is era-tolerated in 1976 but era-deficient in 2021.

---

**Self-contradictory absence patterns**

self_contradictory: [Kumada_1972] : Ni(0)/Ni(II) catalytic cycle (eqs 2–4) → predicts R–R homo-coupling product per turnover (eq 3) → R–R neither reported, quantified, nor acknowledged as undetectable | item_id: U-1

self_contradictory: [Kumada_1972] : Homogeneous Ni(0)/Ni(II) molecular cycle proposed → "black mixture" observation consistent with Ni(0) nanoparticle formation → observation recorded without analysis or acknowledgment of mechanistic implications | item_id: U-2

self_contradictory: [Kumada_1976b] : Scheme 1 cycle predicts oxidative-addition rate scaling with C–X bond strength (normal order PhBr>PhCl>PhF) → [Ni(dppp)Cl₂] gives anomalous PhI>PhCl>PhBr labelled "difficult to explain" → Scheme 1 retained without revision; instead "two or more rate-limiting steps" invoked from same qualitative dataset | item_id: U-2

self_contradictory: [Kumada_1976b] : β-hydride elimination claimed as generally suppressed in Ni-alkyl intermediates → extensive secondary-to-primary isomerization observed with [Ni(dmpe)Cl₂] (requires β-hydride elimination/reinsertion) → contradiction unacknowledged; treated as independent anomaly | item_id: U-3

self_contradictory: [Kumada_1976b] : Landmark "first C–F oxidative addition to a transition metal" claim → Table 3 footnote c declares GLPC inapplicable due to PhF/benzene co-elution; Table 4 reports 24–26% PhF conversion by the same method without documenting analytical resolution; no isolated yield reported | item_id: U-5

self_contradictory: [Mazet_2021] : dmpe mechanism proposes selective interception of I-a by III-b → stoichiometric Figure 9 experiment yields near-equal products from both electrophilic partners (1a: 7%/8%; 8a: 17%/8%) consistent with statistical scrambling → pattern presented as supporting selective interception | item_id: U-1

self_contradictory: [Mazet_2021] : VTNA catalyst-order assignment acknowledged as unreliable due to decomposition ("must be taken with care") → apparent first-order (dppe) and apparent second-order (dmpe) used as mechanistic basis for proposing two fundamentally different catalytic cycles → no alternative kinetic model tested against the same data | item_id: U-2

self_contradictory: [Mazet_2021] : "rapid phosphate/bromide ion exchange" proposed as key dppe cycle feature → X-ray structure of 9c deposited (CCDC 2116220) containing Ni–O bond geometry → phosphate binding mode (κ¹ vs κ²), which determines exchange lability, unreported in main text | item_id: U-2-supplement (within S2_en U-2 cluster)

self_contradictory: [Mazet_2021] : Temperature-dependent E/Z reversal (40:60 at 23°C → 4:96 at −40°C) documented in Figure 1B → reversal implies opposite-sign ΔΔH‡ and ΔΔS‡, an entropy-controlled selectivity reversal directly testable by Eyring analysis from existing data → mechanistic Results section never returns to this observation | item_id: U-4

**Recurring pattern assessment.** The self-contradictory absence pattern recurs in all three papers across 49 years. This reflects a **narrative function of mechanism diagrams in cross-coupling papers**: catalytic cycles serve to organize and contextualize scope/selectivity data rather than to generate testable predictions that the paper falsifies. When the cycle does generate a testable prediction (R–R formation; homogeneity; β-suppression universality; Scheme 1 normal-order C–X reactivity; selective interception; entropy-controlled E/Z selectivity), the prediction is treated as an implication to be noted and passed over. This is simultaneously a **genre convention** (mechanism sections in methodology and mechanistic papers alike are expected to propose cycles, not to falsify them) and a **genuine analytical gap** (each untested prediction could be tested with the paper's own infrastructure, especially in 2021 where DFT, Eyring analysis, and additional control experiments are within reach without new synthesis). The convention persists because testing one's own mechanistic proposal against its predictions either (a) confirms it (unpublishable as standalone) or (b) falsifies it (requiring a revised mechanism that would constitute a different paper). The publication incentive structure thus preserves self-contradictory absence as a stable feature of the literature across decades, journals, and tool generations.

---

**Group-level unasked question**

[REDACTED: substantial verbatim quotation; see Tier 9]

evidence_chain: [Kumada_1972 : B-1 (selectivity w/o byproduct data), U-1 (R–R predicted but unreported), B-2 (analytical conditions absent), U-2 (black mixture unanalyzed) | Kumada_1976b : A-1 (mechanism deferred), B-1 (response factors absent), B-2 (mass balance violation 104%), U-1 (crossover experiment absent), U-4 (failure mode uncharacterized) | Mazet_2021 : A-3 (bimetallic TM proposed without DFT or numerical kinetic integration), B-5 (statistical inadequacy), B-6 (~75–85% mass-balance gap), U-1 (predicted apparent order not derived from proposed cycle), U-2 (VTNA preconditions violated)]

**TEMPERATURE_SUMMARY correspondence.** In Kumada 1972, B-1 (selectivity w/o byproduct data) and B-4 (sp² boundary without negative-result evidence) are the strongest convergence items at 3/3 — both are instances of the group-level question. In Kumada 1976b, A-4 / B-8 (Z:E stereo without analytical method or mechanism) and B-7 (Grignard order undefined) reach 3/3 convergence — the absence of complete species-level analytical metadata is the highest-confidence shared concern. In Mazet 2021, A-3, B-5, B-7 reach 3/3 convergence — the absence of integrated kinetic, speciation, and statistical foundation is again the most multi-agent-flagged content. The group-level question subsumes recurring_root 1 (catalytic cycle validation) and recurring_root 2 (quantitative measurement basis) as facets of one underlying deficit: the field has never produced a complete, time-resolved, quantitatively validated account of all species during Ni-diphosphine Kumada coupling. The 1972/1976 papers lacked tools; the 2021 paper had tools and chose mechanistic discrimination over comprehensive speciation. The shared blind spot is era-invariant.

**recurring_root correspondence.** The group-level unasked question maps directly onto recurring_root 1 (catalytic cycle validation) + recurring_root 2 (quantitative measurement basis) + recurring_root 4 (self-contradictory absence): the absence of a closed, time-resolved, quantitatively validated species-level account of Ni-diphosphine Kumada coupling is simultaneously the unfulfilled mechanism-validation, the unfulfilled measurement-quality, and the unaddressed self-contradictory-absence concern. A single line of work — Eyring analysis on existing E/Z data, DFT for the bimetallic TS, OA-geometry %V_Bur from the 9c X-ray, complete mass balance for Figure 9, integrated kinetic model — would simultaneously close all three recurring roots for the 2021 case. None has been performed.

---

*End of G1 output.*

---

> **Tier 8 redaction notice**: This file is a redacted copy of the corresponding Tier 3 / Tier 9 output. Verbatim source-paper quotations have been replaced by `[REDACTED: see source paper §<loc>; full text retained in Tier 9 reviewer-only deposit]` markers, preserving location references and our own analytical content. Bibliographic fields (title, authors, journal, year, DOI), analytical labels (`evidence_chain:` with B-/U-/A-/C- internal IDs), short technical terms, and our own analytical text are not redacted. The redaction was applied by `scripts/redact_for_tier8.py` and, for this version, by `scripts/build_paperA_R1_public.py` with `scripts/redact_source_ngram_runs.py` (scripts of the project repository; they are not deposited).
