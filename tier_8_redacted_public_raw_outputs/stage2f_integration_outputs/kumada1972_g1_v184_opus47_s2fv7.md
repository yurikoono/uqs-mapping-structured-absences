prompt_version: stage2f-v7-20260417

---

**[F. Within-Group Comparison]**

**Group composition:** G1 — Direct lineage (dpe/dppe-Ni system, 1972–2021)
- Kumada_1972 (Tamao, Sumitani, Kumada; JACS Communication, 3 pp): method discovery — selective Ni-phosphine catalyzed Grignard cross-coupling.
- Kumada_1976b (Tamao, Sumitani, Kiso, Zembayashi, Fujioka, Kodama, Nakajima, Minato, Kumada; BCSJ Full Paper, 12 pp): general scope and limitations — first comprehensive scope survey.
- Mazet_2021 (Poisson, Tran, Besnard, Mazet; ACS Catalysis Full Paper, 10 pp): comparative mechanistic study of [(dppe)NiBr₂] vs. [(dmpe)NiBr₂] for vinylation of enol phosphates.

Spans 49 years across one direct experimental lineage (the dpe/dppe-Ni Grignard coupling system); the Stage 0–S3v2 outputs were generated under the v18.4 prompt cascade (Sonnet 4.6).

---

**Repeated patterns**

**RP-1: Catalytic cycle proposed without complete experimental validation in the operating system**

All three papers propose Ni(0)/Ni(II) catalytic cycles, yet in none is the full set of elementary steps directly observed under actual catalytic turnover in the system being claimed.

evidence_chain: [Kumada_1972 : A-2, B-12, U-2, U-1 | Kumada_1976b : A-1, A-1d, U-1, U-2, C-7 | Mazet_2021 : A-3, B-5, U-1, U-2]

- Kumada_1972: eqs 2–4 are constructed by analogy with stoichiometric (dipy)Ni reactions (RI-06 cycle-level import); intermediates 1, 2, 3 are not observed under [NiCl₂(dpe)] catalytic conditions; the homo-coupling byproduct R–R predicted by eq 3 is unreported (U-1); a black mixture consistent with Ni⁰ formation is recorded but uncharacterized (B-12, U-2).
- Kumada_1976b: Scheme 1 is acknowledged as "rationalization" rather than proven mechanism ([REDACTED: verbatim source quotation; see the source paper via its DOI] (U-2).
- Mazet_2021: the dppe ion-exchange mechanism is partially validated by X-ray of 9c, but the dmpe bimetallic transmetalation rate-determining step (the paper's most novel claim) rests on a three-point VTNA dataset under acknowledged catalyst deactivation (B-5) and a stoichiometric proof-of-concept with ~75–85% mass unaccounted (B-6); the proposed kinetic model is not numerically integrated (U-1).

---

**RP-2: Quantitative analytical basis for primary metrics is systematically underreported**

Each paper grounds its primary claims in instrumental data (GLPC for the 1972/1976 papers; in situ IR + NMR for 2021) whose reliability cannot be independently audited from what is published.

evidence_chain: [Kumada_1972 : B-2, B-7, B-9, B-11 | Kumada_1976b : B-1, B-2, B-9, B-10 | Mazet_2021 : B-5, B-7, B-10]

- Kumada_1972: the Table I column mixes glpc-only and isolated yields without systematic justification; internal standard identity and FID response factors are not stated (B-2); replicates are absent (B-9); cis:trans ratio analytical method (gpc vs ¹H NMR) is not stated (B-11); identity assignment is allowed by "and/or" formulation (B-7).
- Kumada_1976b: a single Silicone DC 550 column is used for all ~60 entries (B-9) without resolution data; FID response factors are undocumented (B-10); the internal standard differs across tables (mesitylene in Table 1, "normal alkane" in Procedure A, unspecified for Tables 6–7); Table 2 contains a mass-balance violation of 104% (B-2).
- Mazet_2021: the three-point VTNA dataset for the dmpe second-order assignment carries no goodness-of-fit statistics (B-5); the Grignard order is treated as "positive" for dppe and "zeroth" for dmpe without speciation analysis or a unified Schlenk-equilibrium account (B-7); the Ni(I) exclusion is NMR-only without quantified detection limit (B-10).

---

**RP-3: Selectivity / scope claim asserted without complete byproduct accounting**

In each paper, a selectivity or scope claim is central but lacks the byproduct quantification or mass-balance closure that would substantiate it.

evidence_chain: [Kumada_1972 : B-6, U-1, C-1 | Kumada_1976b : A-2, U-4, B-2 | Mazet_2021 : B-6, B-8]

- Kumada_1972: "selective" cross-coupling is the title and central claim, yet no cross:homo product ratio is reported for any Table I entry (B-6); the homo-coupling product predicted by the proposed cycle is neither detected nor acknowledged as below detection limit (U-1); prior-art comparison with Tamura-Kochi is asserted but not measured on a shared substrate (C-1).
- Kumada_1976b: the self-declared "most serious limitation" (alkyl Grignard + dichloroethylene → "mixture of products, usually homo coupling predominating") is named but neither component identity nor yield distribution is reported (A-2, U-4); the Table 2 mass-balance violation (104%) goes unacknowledged (B-2).
- Mazet_2021: the stoichiometric bimetallic proof-of-concept (Figure 9) reports 7–17% 3aa and 8% diene 14, leaving ~75–85% of material unaccounted (B-6); the OA complex 9d is obtained at 16% NMR yield with no mass-balance discussion of the remaining ~84% (B-8).

---

**RP-4: Self-contradictory absence — the paper's own model predicts an observable that the same paper does not test or acknowledge as untested**

evidence_chain: [Kumada_1972 : U-1, U-2 | Kumada_1976b : U-2, U-3, U-5 | Mazet_2021 : U-1, U-3, U-4]

- Kumada_1972: eq 3 predicts R–R as a stoichiometric byproduct of every initiation step, yet R–R is never reported (U-1); the black mixture is consistent with Ni⁰ formation that would invalidate the homogeneous Ni(II)/Ni(0)/Ni(II) cycle but is recorded without comment (U-2).
- Kumada_1976b: Scheme 1 predicts oxidative-addition rate scaling with C–X bond strength (giving normal PhBr > PhCl > PhF), but [(dppp)NiBr₂] gives PhI > PhCl > PhBr — the discrepancy is recorded as "difficult to explain" rather than as internal tension with Scheme 1 (U-2); β-hydride suppression is asserted but olefin byproducts are never specifically searched for (U-3); the C–F oxidative-addition landmark claim is made while Table 3 declares the GLPC method inapplicable to PhF/benzene quantification (U-5).
- Mazet_2021: the dmpe bimetallic mechanism predicts rate ∝ [I-a][III-b] but [I-a] and [III-b] as functions of total [Ni] are never derived, so the apparent second-order observation cannot be shown to be uniquely explained by the proposed mechanism (U-1); the radical-clock non-detection is treated as binary exclusion without the ring-opening rate constant of substrate 1g (U-3); the temperature-dependent E/Z reversal for 3ce (40:60 at 23°C → 04:96 at −40°C) is reported in the Introduction but never analyzed mechanistically (U-4).

---

**RP-5: Ligand-effect attribution from insufficient experimental basis (multiple covarying variables)**

evidence_chain: [Kumada_1972 : B-3, A-2 | Kumada_1976b : B-1, B-7 | Mazet_2021 : B-3, B-4]

- Kumada_1972: the activity order [NiCl₂(dpp)] > [NiCl₂(dpe)] > ... is presented without yield values for each catalyst on the test substrate (B-3); the explanation invokes cis-geometry as "first requisite" with chelate size, bite angle, and electronics simultaneously varying.
- Kumada_1976b: Table 1 catalytic activity ranking rests on GLPC-only yields with no replicate data and no FID response factor (B-1); the dppp vs. dppe preference is asserted across multiple substrate classes without a controlled stoichiometric reactivity probe (B-7).
- Mazet_2021: the dppe/dmpe reactivity difference is attributed to "markedly different steric environment" (%VBur 48.9 vs. 43.1) measured on cod complexes 7c/7d that are absent from the catalytic cycle (B-3); the steric vs. electronic decomposition for 1d (adamantyl enol phosphate) failure with [(dppe)Ni(0)] is not quantified by Hammett correlation, activation-energy measurement, or DFT on the relevant OA geometry (B-4).

---

**Cross-field temperature patterns**

temperature_pattern: RP-1 mechanism validation | papers: [Kumada_1972, Kumada_1976b, Mazet_2021] | profile_consistency: divergent | note: Severity of mechanism-validation gaps grows from V1+V2 high (Kumada_1972 A-2) to V2-only high (Kumada_1976b A-1) to V1+V2+V3 high (Mazet_2021 A-3, 3/3 convergence) — by 2021 a physical-organic chemistry agent (V3) joins organometallic and computational agents in flagging the kinetic-evidence gap as high severity, indicating that the field's evaluation lens has expanded.

temperature_pattern: RP-2 analytical underreporting | papers: [Kumada_1972, Kumada_1976b, Mazet_2021] | profile_consistency: consistent | note: Across all three papers the analytical-quality agent rates the absence of replication, calibration, and uncertainty quantification at medium-to-high severity. The character of the gap shifts (no method → method named without calibration → method named without statistical rigor) but severity remains comparably flagged.

temperature_pattern: RP-3 selectivity without byproduct data | papers: [Kumada_1972, Kumada_1976b, Mazet_2021] | profile_consistency: consistent | note: The selectivity-claim-without-mass-balance pattern receives high severity in every paper (Kumada_1972 B-6 V2=V3=high; Kumada_1976b U-4 V1=V2=high; Mazet_2021 B-6 V1=V2=high). The gap is genre-stable across method, scope, and mechanism papers in this lineage.

temperature_pattern: RP-4 self-contradictory absence | papers: [Kumada_1972, Kumada_1976b, Mazet_2021] | profile_consistency: divergent (intensifying) | note: U-item severity for self-contradictory absences increases over time — Kumada_1972 U-1 severity=high (V2 only); Kumada_1976b U-2/U-5 severity=high (V2 + V1/V3); Mazet_2021 U-1 severity=critical (V3) + U-4 severity=high (V2+V3). The model-prediction-vs-data tension becomes more visible to multiple agents as papers acquire more elaborate mechanistic models that generate more testable predictions.

---

**Same-root group patterns**

recurring_root: Catalytic cycle constructed by analogy and not validated by system-specific direct intermediate observation | papers: [Kumada_1972, Kumada_1976b, Mazet_2021] | member_items: [Kumada_1972: SRG-1 (A-2, U-2, B-12); Kumada_1976b: SRG-1 (A-1, A-1d, U-1, U-2, C-7); Mazet_2021: SRG-2 (A-3, B-6, C-3) and SRG-1 (A-3, A-4, A-5, B-5, B-7, U-1, U-2)] | note: Structural gap, not genre convention. In 1972/1976 the tools for in situ characterization of organonickel intermediates under catalytic conditions did not exist; by 2021 NMR, VTNA, X-ray, and DFT all exist but produce ambiguous results when combined with catalyst deactivation and unspecified Grignard speciation. The root persists as the field's most stable unanswered question.

recurring_root: Quantitative measurement basis underreported (response factors, mass balance, replicate data) | papers: [Kumada_1972, Kumada_1976b, Mazet_2021] | member_items: [Kumada_1972: SRG-5 (B-2, B-7, B-9, B-11); Kumada_1976b: SRG-2 (B-1, B-2, B-10, B-5) and SRG-7 (B-5, B-14); Mazet_2021: SRG-1 (B-5, B-7) and CLA-1 partial (B-9)] | note: Genre convention. Synthetic and organometallic chemistry journals across 1972–2021 have not standardized raw-data deposition, replicate reporting, or response-factor disclosure for chromatographic / VTNA quantification. Field-wide rather than paper-specific.

recurring_root: Selectivity / scope claim without complete byproduct mass balance | papers: [Kumada_1972, Kumada_1976b, Mazet_2021] | member_items: [Kumada_1972: SRG-2 (B-6, U-1, C-1); Kumada_1976b: SRG-6 (A-2, U-4); Mazet_2021: SRG-2 (A-3, B-6, C-3)] | note: Spans both methodology papers (1972, 1976) and the mechanistic study (2021), shifting from "selectivity claim without homo-coupling quantification" to "limitation claim without failure-mode characterization" to "bimetallic claim without expected-yield derivation." The structural form is constant: a positive or negative claim is asserted; the byproduct distribution that would test it is not reported.

recurring_root: Stereochemical / E:Z observation reported without analytical method or mechanistic attribution | papers: [Kumada_1972, Kumada_1976b, Mazet_2021] | member_items: [Kumada_1972: SRG-4 (A-1, B-11); Kumada_1976b: SRG-5 (A-4, B-8); Mazet_2021: SRG-4 (A-6, U-4)] | note: This root recurs verbatim across all three papers. In 1972 the cis:trans ratio (80:20 vs. 43:57) is reported without analytical method and the mechanistic origin is deferred. In 1976 the Z:E ratio (90:10 from (Z)-DCE, 80:20 from (E)-DCE) is reported and explicitly deferred to ref. 26 / future work. In 2021 the temperature-dependent E/Z reversal of 3ce in the dmpe system is reported in the Introduction and never returned to. The stereochemical observation–to–mechanistic attribution pipeline is structurally interrupted in every paper.

---

**Temporal trajectory of recurring patterns**

temporal_trajectory: RP-1 mechanism validation | classification: shifting | transition_point: 2021 (Mazet) | note: 1972/1976 mechanism-validation absences are *structurally suppressed* (in situ NMR of organonickel intermediates under catalytic conditions was not feasible; no VTNA or DFT framework existed); by 2021 the tools exist, but execution under catalyst-deactivation conditions still produces ambiguous results — the gap shifts from "structurally suppressed" to "individually chosen / methodologically chosen" because it would now be answerable with sufficient experimental investment.

temporal_trajectory: RP-2 analytical underreporting | classification: narrowing | transition_point: none (continuous improvement) | note: 1972 (no instrument or column stated) → 1976 (instrument and column stated, calibration absent) → 2021 (method named, replication and statistics absent). The gap closes monotonically but is not fully resolved in any paper.

temporal_trajectory: RP-3 selectivity without byproduct data | classification: time-invariant | transition_point: none | note: The pattern persists with the same character across method, scope, and mechanistic-study formats in this lineage. This is the strongest evidence in G1 for a field-wide structural convention (selective-claim rhetorical structure without mass-balance disclosure) rather than an era- or individual-specific choice.

temporal_trajectory: RP-4 self-contradictory absence | classification: shifting (intensifying) | transition_point: 2021 (Mazet) | note: As models become more articulated (eq 3 in 1972 → Scheme 1 in 1976 → Figure 8B bimetallic cycle in 2021) they generate more testable predictions per page; the gap between predictions made and predictions tested grows. The Mazet U-1 (critical severity) is the most acute instance.

temporal_trajectory: RP-5 ligand-effect attribution | classification: shifting | transition_point: 2021 (Mazet) | note: 1972/1976 ligand attributions cite chelate/bite-angle qualitatively without computation; 2021 cites %VBur computed on non-catalytic cod complex — the rhetorical form has migrated from "qualitative steric reasoning" to "numerical descriptor on wrong geometry," reflecting available-but-unutilized characterization rather than tool unavailability.

temporal_trajectory: stereochemical observation without attribution (recurring root above) | classification: time-invariant | transition_point: none | note: cis:trans (1972) → Z:E (1976) → E/Z temperature reversal (2021) — same structural gap across 49 years. This is the second strongest evidence in G1 for a field-wide structural convention.

---

**Structural suppression vs. individual choice (per repeated pattern)**

- RP-1: era-dependent. *Structurally suppressed (1972/1976: no in situ characterization tools)* → *individually chosen (2021: tools available, deactivation tolerated, kinetic model not integrated).*
- RP-2: incentive-suppressed across all three eras — replicate runs and complete response-factor calibration tables are not publishable contributions in synthetic / organometallic chemistry; no group in the field is incentivized to report them in primary papers.
- RP-3: era-dependent. *Era-tolerated (1972: communication-format) → era-tolerated (1976: full paper, mass-balance not required for scope tables) → individually chosen (2021: stoichiometric experiments could and should report mass balance to >90%; mass-balance closure for the bimetallic test would have been possible).*
- RP-4: individually chosen in 2021 (the predictions could be tested and the prediction-data tension acknowledged in the same paper); structurally suppressed in 1972/1976 only for the mechanistic predictions, not for the selectivity prediction (homo-coupling glpc detection was feasible in 1972).
- RP-5: era-dependent. *Structurally suppressed (1972/1976: no DFT or %VBur tools) → individually chosen (2021: DFT on OA-relevant geometry is feasible).*

---

**Paradigm competition**

The group exhibits **paradigm succession rather than paradigm competition** within the dpe/dppe-Ni lineage. Each paper inherits and extends the predecessor's mechanistic frame rather than competing against an alternative paradigm internal to the lineage.

The relevant paradigm tension is *external* to G1: Felkin-Corriu's Ni(0)-oxidative-addition cycle (1975) competes with the Kumada/Tamao Ni(II)/Ni(0)/Ni(II) frame that all three G1 papers adopt. Mazet_2021 explicitly cites Felkin-Corriu (C-7) as a competing mechanism but does not perform the crossover experiment that would distinguish them (CLA-1 / U-1).

evidence_chain: [Kumada_1972 : no textual basis in Kumada_1972 (Felkin-Corriu paper postdates 1972) | Kumada_1976b : C-7 → [REDACTED: substantial verbatim quotation; see Tier 9] | Mazet_2021 : C-7 / U-1 → competing mechanism acknowledged; crossover experiment not performed]

The systematically unanswered question across all three papers is therefore: *does the Ni(0)/Ni(II) Kumada-cycle frame, or the Felkin-Corriu Ni(0)-oxidative-addition frame, govern the actual catalytic event in this lineage?* The 1972 paper cannot ask this question (Felkin-Corriu had not yet been proposed). The 1976 paper acknowledges the alternative but does not resolve it. The 2021 paper acknowledges it again, builds an elaborated bimetallic variant on the Kumada side, and again does not resolve it. This is paradigm succession on the Kumada side combined with persistent unresolved paradigm competition with the Felkin-Corriu side.

---

**Divergences**

div-1: Mass-balance discipline — Kumada_1972 (no mass balance attempted) vs. Kumada_1976b (mass balance partially attempted but violated in Table 2 at 104%) vs. Mazet_2021 ("excellent mass balance" claimed for dppe but ~75–85% unaccounted in the bimetallic stoichiometric test).
evidence_chain: [Kumada_1972 : B-6, U-1 | Kumada_1976b : B-2 | Mazet_2021 : B-6]
Subfield-and-format-driven: communication papers (Kumada_1972) do not attempt mass-balance; full scope papers (Kumada_1976b) attempt it across tables; mechanistic studies (Mazet_2021) attempt it locally for stoichiometric experiments — yet none achieve closure.

div-2: Engagement with competing mechanism — Kumada_1972 (no competing mechanism cited; Felkin-Corriu had not yet been published) vs. Kumada_1976b (Felkin-Corriu cited as "essentially consistent" without distinguishing experiment, C-7) vs. Mazet_2021 (Felkin-Corriu re-cited but again not experimentally excluded; rather, the bimetallic variant adds further mechanistic structure that further entangles the two paradigms).
evidence_chain: [Kumada_1976b : C-7 | Mazet_2021 : U-1, A-3]
Era-driven: as the alternative paradigm became established post-1975, citation increases but experimental discrimination does not.

div-3: Scope vs. mechanism emphasis — Kumada_1972 and Kumada_1976b are scope-driven with mechanism as supporting commentary; Mazet_2021 is mechanism-driven with scope drawn from a separate prior paper (Fiorito 2018). The reporting omissions migrate accordingly: 1972/1976 papers compress mechanistic data; 2021 paper compresses scope-substrate failure analysis (B-1: >50 examples cited from Fiorito 2018 without failure analysis brought forward).
evidence_chain: [Kumada_1972 : A-1, A-2 | Kumada_1976b : A-1 | Mazet_2021 : B-1, A-7]

---

**U-item patterns**

recurring_U: Self-contradictory absence — paper's own model predicts an observable that the same paper does not test | papers: [Kumada_1972, Kumada_1976b, Mazet_2021] | item_ids: [Kumada_1972 U-1 (homo-coupling byproduct R–R predicted by eq 3, not detected), Kumada_1972 U-2 (Ni⁰ alternative consistent with B-12 black mixture), Kumada_1976b U-2 (anomalous PhI > PhCl > PhBr inconsistent with Scheme 1), Kumada_1976b U-3 (β-hydride suppression claim with no olefin byproduct search), Kumada_1976b U-5 (C–F landmark with PhF GLPC declared inapplicable in same paper), Mazet_2021 U-1 (apparent second-order kinetics not derived from proposed bimetallic rate law), Mazet_2021 U-2 (VTNA applied under acknowledged deactivation that violates VTNA preconditions)] | note: This recurring U is not a defect of the A/B/C framework but a stable analytical category — [REDACTED: substantial verbatim quotation; see Tier 9] It deserves first-class status in the classification framework. The Mazet_2021 instances reach severity=critical and high — the tension intensifies as models become more articulated.

recurring_U: Stereochemical observation reported without analytical method or mechanistic attribution | papers: [Kumada_1972, Kumada_1976b, Mazet_2021] | item_ids: [Kumada_1972 (A-1 + B-11), Kumada_1976b (A-4 + B-8), Mazet_2021 (A-6 + U-4)] | note: While each paper places this in A/B (deferral + reporting omission), the recurrence across three papers and 49 years suggests this is a structural genre pattern — stereochemical observations are framed as "interesting but for elsewhere" with high consistency.

---

**Self-contradictory absence patterns**

self_contradictory: Kumada_1972 : eq 3 catalytic cycle ("L₂NiR₂ + R'X" → L₂Ni(R')(X) + R–R") → predicts homo-coupling byproduct R–R as stoichiometric per turnover → R–R never detected, quantified, or acknowledged as below detection limit in any Table I entry | item_id: U-1

self_contradictory: Kumada_1972 : Homogeneous Ni(II)/Ni(0)/Ni(II) cycle (eqs 2–4) → predicts catalyst remains as intact phosphine-Ni complex → black mixture (B-12) observed, consistent with Ni⁰ nanoparticle formation, recorded but uncharacterized | item_id: U-2

self_contradictory: Kumada_1976b : Scheme 1 (Ni(II)/Ni(0)/Ni(II) cycle predicting OA-rate scaling with C–X bond strength) → predicts normal reactivity order PhBr > PhCl > PhF → [(dppp)NiBr₂] gives anomalous PhI > PhCl > PhBr; labeled "difficult to explain" rather than acknowledged as internal tension | item_id: U-2

self_contradictory: Kumada_1976b : β-hydride suppression mechanistic claim → predicts olefin byproducts (1-butene, propene) absent → no systematic search for these byproducts is documented; absence-of-detection treated as evidence-of-absence | item_id: U-3

self_contradictory: Kumada_1976b : Landmark C–F oxidative-addition claim → requires evidence ≥ scope-table standard → Table 3 declares PhF/benzene GLPC co-elution inapplicable; Table 4 reports PhF conversion 24–26% via undocumented analytical modification; isolated yield = 0 | item_id: U-5

self_contradictory: Mazet_2021 : Bimetallic rate-determining step (I-a + III-b → IV) → predicts rate ∝ [I-a][III-b] → [I-a] and [III-b] as functions of total [Ni] never derived; numerical kinetic-model integration absent | item_id: U-1

self_contradictory: Mazet_2021 : VTNA methodology (Burés 2016, ref 18) → requires constant catalyst concentration → catalyst deactivation and product inhibition acknowledged; same-excess overlay fails; VTNA orders nonetheless reported as mechanistic evidence | item_id: U-2

self_contradictory: Mazet_2021 : Radical-clock substrate 1g → non-detection of 12/13 used as binary radical exclusion → ring-opening rate constant of 1g not reported; upper bound on radical lifetime not derived | item_id: U-3

This pattern recurs in all three papers (n=8 instances). Assessment of its function across the lineage:

- **Genre convention** (partially): in 1972/1976, mechanism diagrams in synthetic/scope methodology papers are expected to *contextualize* the data rather than to generate testable predictions — the diagrams perform a *narrative function* of organizing scope claims. Both papers signal this with "working hypothesis" / "rationalization" language. Era-tolerated.
- **Genuine analytical gap** (predominantly, especially in 2021): Mazet_2021 is a mechanistic study whose central deliverable is the bimetallic mechanistic claim; the predictions could and should be tested within the same paper, and the tools (DFT, kinetic-model integration, EPR for Ni(I) exclusion, mass-balance accounting) were available. The pattern in Mazet_2021 cannot be defended as genre convention.
- **Narrative function** (residual, in all three): all three papers use mechanistic diagrams partly to organize scope/utility data into a cognitively coherent story; the predictions remain a byproduct of that organization rather than a primary deliverable.

The lineage shows that the same structural pattern *changes function over time*: from era-justified (genre convention + structural suppression in 1972/1976) to era-deficient (genuine analytical gap in 2021). The pattern's persistence across this functional shift is one of the most informative signals in G1.

---

**Group-level unasked question**

The question this group of three papers most systematically failed to ask is:

**[REDACTED: substantial verbatim quotation; see Tier 9]**

This question subsumes RP-1, RP-3, RP-4 and the cycle-validation recurring root. It is the question that the Kumada_1972 working hypothesis deferred ("Further studies are required..."); that Kumada_1976b advanced from working hypothesis to "rationalization" (Scheme 1) without resolving; and that Mazet_2021 elaborated into a comparative dppe-vs-dmpe bimetallic proposal while leaving the central Felkin-Corriu vs. Kumada-cycle paradigm question, the catalyst-identity question (Ni⁰ nanoparticle vs. intact phosphine-Ni complex), and the kinetic-model integration question all unresolved.

evidence_chain: [Kumada_1972 : A-2, U-1, U-2, B-12 → mechanistic working hypothesis with no intermediate observation and Ni⁰ ambiguity unresolved | Kumada_1976b : A-1, A-1d, U-1, U-2, C-7 → "rationalization" framing with Felkin-Corriu acknowledged but unexcluded | Mazet_2021 : A-3, B-5, B-6, U-1, U-2 → bimetallic claim with kinetic-model integration absent and VTNA preconditions violated]

The TEMPERATURE_SUMMARY data support this assignment: A-2 (Kumada_1972: V1+V2=high), A-1 (Kumada_1976b: V2=high), and A-3 (Mazet_2021: V1+V2+V3=high, 3/3 convergence) are the highest-severity items in each paper and all map to the same recurring root (catalytic-cycle validation). The convergence of the agent-frame severity assessments grows monotonically across the lineage (1/3 → 1/3 → 3/3), indicating that what was a single-discipline concern in 1972/1976 has become a multi-discipline concern by 2021. The same_root_groups for "catalytic cycle constructed by analogy without system-specific validation" recur as SRG-1 in each paper.

The group-level question is *not* a paradigm-competition question internal to G1; the Felkin-Corriu vs. Kumada-cycle external paradigm contest is part of the unresolved structure but is not the only component. The catalyst-identity question (Ni(II) vs. Ni⁰ vs. Ni(I)) and the kinetic-model integration question (apparent order vs. derived rate law) are independent components that recur across the lineage with the same character. The unified group-level unasked question encompasses all three threads.

---

**Anomalies / notes for downstream stages**

- The single most under-pursued empirical-prediction pack across the three papers is EP-04a (Discrimination / replication) applied to homo-coupling byproduct quantification (Kumada_1972) → byproduct mixture characterization in dichloroethylene + alkyl Grignard (Kumada_1976b) → bimetallic stoichiometric mass-balance closure (Mazet_2021). The same EP type recurs across the lineage for distinct chemical questions, suggesting EP-04a is a high-leverage filling target for the group.
- EP-03a (Direct observation / state assignment) is also under-pursued in all three papers (Ni⁰ vs. Ni(II) characterization in 1972, ³¹P NMR of yellow species in 1976, EPR of Ni(I) and DFT bimetallic TS in 2021). This is the second cross-paper EP recurrence.
- The stereochemical-observation-without-attribution pattern (RP-5 secondary recurring root) is a candidate for separate Stage 3 attention if a group-level VQ-3 advancement strategy is designed.

---

> **Tier 8 redaction notice**: This file is a redacted copy of the corresponding Tier 3 / Tier 9 output. Verbatim source-paper quotations have been replaced by `[REDACTED: see source paper §<loc>; full text retained in Tier 9 reviewer-only deposit]` markers, preserving location references and our own analytical content. Bibliographic fields (title, authors, journal, year, DOI), analytical labels (`evidence_chain:` with B-/U-/A-/C- internal IDs), short technical terms, and our own analytical text are not redacted. The redaction was applied by `scripts/redact_for_tier8.py` and, for this version, by `scripts/build_paperA_R1_public.py` with `scripts/redact_source_ngram_runs.py` (scripts of the project repository; they are not deposited).
