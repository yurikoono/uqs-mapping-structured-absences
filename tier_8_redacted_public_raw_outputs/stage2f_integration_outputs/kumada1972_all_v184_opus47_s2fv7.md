prompt_version: stage2f-v7-20260417

---

**[F. Within-Group Comparison — Integration Mode]**

**Input:** Stage 2F v7 outputs from three sub-groups, all generated under v18.4 prompt cascade (Sonnet 4.6 for S0–S3v2; Opus 4.7 for Stage 2F):
- G1: Direct lineage (kumada1972, kumada1976b, mazet2021) — 3 papers, 1972–2021, dpe/dppe-Ni Grignard system
- G2: Boundary breakthrough (kumada1972, breitenfeld2014, cherney2015, pengfei2024) — 4 papers, 1972–2024, sp²→sp³ frontier
- G3: Methodological expansion (kumada1972, monnereau2009, molander2016, morken2016) — 4 papers, 1972–2016, ligand / activation-mode / selectivity axes

**Reference paper:** Kumada 1972 (shared across all three sub-groups)
**Stage 3 output available:** kumada_v184_sonnet_s3v2_en.md (six SRGs + two CLAs; SRG→RI→ER→EP crosswalk; PRI-12 candidate flagged)
**Total unique papers across sub-groups:** 9 (kumada1972, kumada1976b, mazet2021, breitenfeld2014, cherney2015, pengfei2024, monnereau2009, molander2016, morken2016)

The integration assesses whether sub-group-level patterns emerged independently in multiple sub-groups without being seeded by the shared reference paper, cross-references recurring_roots across sub-groups for field-wide vs. paradigm-specific signatures, synthesizes the three sub-group group_unasked_questions as either independent or facets of a single problem, and cross-references the EP filling landscape from S3 against the observed 2F patterns.

---

**Patterns that emerged independently in multiple sub-groups**

The following integrated patterns (IPs) were each named in all three sub-groups under different sub-group-internal labels but with structurally identical substance, despite the sub-groups being constituted to probe different field axes (lineage / boundary / expansion). Independent emergence across all three sub-groups — combined with the diversity of papers in each sub-group beyond the shared Kumada 1972 anchor — is the strongest evidence that these are field-wide structural conventions rather than sub-group-specific or anchor-seeded artefacts.

**IP-1: Catalytic cycle proposed without elementary-step validation in the operating system**

- G1: RP-1 across Kumada_1972 + Kumada_1976b + Mazet_2021 (49-year direct lineage)
- G2: RP-1 across Kumada_1972 + Breitenfeld_2014 + Cherney_2015 + Pengfei_2024 (52-year paradigm shift from 2-electron through radical and review-organized to electrochemical Ni(I/II/III))
- G3: RP-1 across Kumada_1972 + Monnereau_2009 + Molander_2016 + Morken_2016 (44-year coexisting expansion across ligand architecture, photoredox/Ni dual catalysis, and asymmetric desymmetrization)

The pattern recurs in every one of the 9 papers across all paradigms (2-electron Ni(0)/Ni(II), Ni(I)/Ni(III) radical bimetallic, photoredox/Ni SET-transmetalation, electrochemical Ni(I/II/III), asymmetric Ni/PyBox), all formats (JACS Communication, BCSJ Full Paper, ACS Catalysis Full Paper, Organometallics Full Paper, Chemical Reviews Review, Nature Catalysis Full Paper, Adv. Synth. Catal. Full Paper, Acc. Chem. Res. Account, JACS Communication), and 8 distinct journals. Aggregating across G1/G2/G3, no paper in the corpus directly observes the full set of named cycle intermediates under operating turnover conditions in the system whose mechanism it claims; mechanism is constructed from analogy with stoichiometric precedents (Kumada 1972 from (dipy)Ni; Breitenfeld 2014 comproportionation from ref-20 alkyl–alkyl predecessor; Cherney 2015 Ni¹/Ni³ from Lin DFT; Pengfei 2024 halide OA from Anderson-Vicic Zn-mediated chemistry; Monnereau 2009 Pd-bite-angle dynamics imported as Ni precedent; Molander 2016 PES from ref-24 benzylic single-substrate; Morken 2016 SN2 attack-geometry imported from organic chemistry; Mazet 2021 dmpe bimetallic OA from prior dppe analogy).

**IP-2: Quantitative analytical basis for primary metrics is systematically underreported**

- G1: RP-2 (glpc-only without conditions → instrument named without calibration → VTNA without statistical rigor; nine pieces of evidence across three papers)
- G2: RP-2 (glpc → rate-orders without statistical tests → review-scale inheritance → isolated yields without conversion or unified reference electrode; sixteen evidence items across four papers)
- G3: RP-4 (glpc → GC without response factors → DFT validation tables absent → SFC column/conditions absent for 17 er entries; ten evidence items across four papers)

This pattern recurs in every one of the 9 papers. The specific instrument or computational framework changes across the corpus (glpc → GC → VTNA → SFC → CV → SWV → DFT) but the structural gap (measurement conditions or computational protocol insufficient for independent replication or audit) is invariant across 1972–2024. The load-bearing claim shifts as the corpus advances — yield (Kumada 1972), TOF (Monnereau 2009), rate orders (Breitenfeld 2014), comprehensive coverage (Cherney 2015), mechanistic conclusion + scope (Molander 2016), er (Morken 2016), bimetallic mechanism (Mazet 2021), comprehensive Csp³–Csp³ method (Pengfei 2024) — and in every case the metric directly underwriting the central novelty is the metric whose analytical foundation is least audit-ready.

**IP-3: Self-contradictory absence — the paper's own model predicts an observable that the same paper does not test**

- G1: RP-4 — 8 instances across 3 papers (R–R untested → β-elimination contradiction → VTNA preconditions violated; predicates intensify from "working hypothesis" to "rationalization" to elaborated bimetallic claim)
- G2: RP-4 — 15 instances across 4 papers (R–R prediction; intermediates 10–16 unobserved; Ni¹/Ni³ EPR/CV absent across 427 cited references; anodic half-reaction undescribed; DFT initiation barrier exceeds proposed RDS; CV vs. kinetic ordering unreconciled)
- G3: RP-3 — 15 instances across 4 papers (R–R; 41.8 ppm species oxidation state unassigned; rigid-analogue control deferred; SMD-water PES extrapolated to acetone/dioxane without solvation sensitivity; CV reported only for silicates while the claim concerns trifluoroborates; HAT vs. Ni-trapping competition unmeasured; axial-conformer hypothesis not differentiated from equatorial backside attack; ArMgBr cycle drawn while text identifies aging-induced Ar₂Mg active speciation)

Across all three sub-groups, this is the single densest recurring U-item category, with **38 explicitly recorded self-contradictory absence instances** in the 9-paper corpus (G1: 8; G2: 15; G3: 15). The U-density grows with paper complexity (~2 per paper in 1972/1976/Morken communications; ~5 per paper in 2014/2024 full papers; ~10 in the Cherney 2015 review; ~7 in the Molander 2016 Account). The independent emergence of this pattern in all three sub-groups, with each sub-group separately concluding that its character is partly genre-conventional and partly genuine analytical gap, confirms G1/G2/G3's individual assessments and elevates the conclusion from sub-group-level to corpus-level: the gap is field-structural, not authorial.

**IP-4: Selectivity / scope claim asserted without complete byproduct mass balance**

- G1: RP-3 across all 3 papers (selective coupling without homo-coupling quantification; Table 2 mass-balance violation 104%; bimetallic stoichiometric test ~75–85% material unaccounted)
- G2: RP-5 across Kumada_1972 + Breitenfeld_2014 + Pengfei_2024 (selectivity claim without homo-coupling data; uniform-conversion assumption required for radical-clock mechanistic interpretation; 17%+13% homocoupling reported but unreconciled with proposed selectivity model)
- G3: RP-6 across all 4 papers (sp³ exclusion asserted as feature with no failed-example data; bromomesitylene 780 h⁻¹ outlier in Monnereau Table 3 unattributed; compound 64 32% without electronic mechanistic attribution; quaternary-substrate failure listed in Scheme 2 inset without data)

Mass-balance closure is **paradigm-invariant absent** across the entire corpus. The failure mode shifts over time — from "byproducts unreported" (1972: zero homo-coupling data anywhere in Table I; 1976: 104% mass-balance violation unacknowledged) to "byproducts reported but model-inconsistent" (Pengfei 2024: 17%+13% homocoupling reported once at Entry 1 but not reconciled with the proposed selectivity model; Mazet 2021: ~75–85% unaccounted in the bimetallic stoichiometric proof-of-concept) — but no paper in the 9-paper corpus closes the mass balance for any catalytic experiment supporting its central novelty claim.

**IP-5: External benchmark superiority asserted without matched-pair shared-substrate comparison (RI-09)**

- G1: not prominently flagged at sub-group level (the lineage is intra-program rather than inter-program competitive)
- G2: RP-6 across all 4 papers (Tamura-Kochi qualitative; Yamamoto + Mirica without activation parameters; Nobel methods + Consiglio + Kumada-Consiglio dropped without ee comparison; Lin Nature 2022 + Gong refs 29–30 introduced as direct benchmarks for the "first general eXEC" claim with no shared-substrate comparison)
- G3: RP-5 across all 4 papers (Tamura-Kochi cited; Corriu-Masse forgotten deferral; refs 7a–7f Pd-Suzuki cited at qualitative dot-matrix level; Tamao 1976 / Stille 1983 rate trend invoked without numbers; Fu, Zhong-Bian, Nakamura, Breit, Carretero, Jarvo enantioselective and enantiospecific contrasted without er/yield numbers)

This pattern recurs in 7–8 of 9 papers (G1's mazet2021 partially exempt as a mechanism-driven study, though it still positions against Felkin-Corriu without a crossover experiment that would distinguish the two cycles). The persistence is strikingly time-invariant across 52 years and four formats — communication, full paper, review, and account formats all permit cited-without-compared positioning.

---

**Cross-referencing recurring_roots across sub-groups**

| Recurring root | G1 | G2 | G3 | Field-wide vs. paradigm-specific |
|---|---|---|---|---|
| Catalytic cycle from analogy without system-specific validation | All 3 papers | All 4 papers | All 4 papers | **Field-wide (9/9)** |
| Quantitative measurement basis underreported | All 3 papers | All 4 papers | All 4 papers | **Field-wide (9/9)** |
| Self-contradictory absence (model predicts → untested) | All 3 papers | All 4 papers | All 4 papers | **Field-wide (9/9)** |
| Selectivity claim without complete byproduct mass balance | Kumada_1972, Kumada_1976b, Mazet_2021 | Kumada_1972, Pengfei_2024 | Kumada_1972, Monnereau_2009, Molander_2016, Morken_2016 | **Field-wide (8–9/9), strongest in methodology papers** |
| Imported mechanistic model without isomorphism demonstration (RI-06 cycle-level) | All 3 papers | All 4 papers | 3 of 4 (not Kumada_1972) | **Field-wide (8–9/9)** |
| Asserted superiority over prior art without matched-pair comparison | Partial (lineage internal) | All 4 papers | All 4 papers | **Field-wide (7–8/9), partly format-driven** |
| Stereochemical observation without analytical method or mechanistic attribution | All 3 papers | (not foregrounded) | (not foregrounded) | **Lineage-specific** (G1 only) |
| DFT as sole mechanistic discriminant | (Mazet only, partial) | Breitenfeld, Cherney, Pengfei | Molander only | **Paradigm-specific** (post-2010 mechanistic and computational papers) |
| Ligand-effect attribution from insufficient experimental basis | Kumada_1972, Kumada_1976b, Mazet_2021 | (not foregrounded) | Kumada_1972, Monnereau_2009 | **Paradigm-specific** (diphosphine-ligand methodology papers) |
| Imported-model prerequisite-absence (DFT functional / reference electrode / spin state / anode characterization) | (Mazet partial) | Breitenfeld, Cherney, Pengfei | Molander, Morken | **Paradigm-conditional** (papers deploying computational or electrochemical infrastructure) |

**Field-wide patterns (paradigm-invariant, present in 8–9/9 papers):** IP-1 (cycle validation by analogy), IP-2 (analytical underreporting), IP-3 (self-contradictory absence), IP-4 (selectivity without mass balance), and IP-5 (external benchmarking absent). RI-06 cycle-level import is field-wide except for Kumada 1972 itself, where the import is qualitative working-hypothesis hedged.

**Paradigm-conditional patterns (present where the requisite tooling is deployed):** DFT-as-discriminant (post-DFT papers only); imported-model prerequisite-absence (papers deploying DFT or electrochemistry); ligand-effect attribution (diphosphine-architecture papers).

**Lineage-specific pattern:** stereochemical-observation-without-attribution recurs across all three G1 papers in identical structural form (cis:trans 1972 → Z:E 1976 → temperature-dependent E/Z reversal in Mazet 2021); G2/G3 do not foreground this root, so it is a feature of the dpe/dppe-Ni Grignard lineage rather than a corpus-wide convention.

---

**Cross-field temperature patterns (integrated)**

temperature_pattern: IP-1 mechanism validation | papers: [all 9] | profile_consistency: divergent (intensifying) | note: Severity of mechanism-validation gaps grows monotonically across the corpus. Kumada 1972 A-2 reaches 2/3 convergence (V1+V2 high). Kumada 1976b A-1 reaches V2-only high. Mazet 2021 A-3 reaches 3/3 convergence. Cherney 2015 U-1 reaches **3/3 convergence with all three agents at high severity (gap=none)** — the single highest-temperature item across the corpus, reflecting that even a review aggregating 427 references cannot mask the absence of EPR/CV evidence for the Ni¹/Ni³ unifying mechanism. Pengfei 2024 U-6 reaches 3/3 convergence with V2=V3=high on the DFT 2.8 kcal mol⁻¹ discriminator within method error. The agent-frame severity assessments grow from single-discipline (1972/1976: organometallic only) to multi-discipline (2014–2024: synthetic + mechanistic + analytical).

temperature_pattern: IP-2 analytical underreporting | papers: [all 9] | profile_consistency: consistent | note: Severity is medium-to-high from the analytical-quality agent (V3) across all 9 papers. The gap shifts character (no method named → method named without calibration → method named without statistical rigor → method named without uncertainty propagation), but the V3 severity profile remains consistently flagged. Pengfei 2024 B-1 acquires V1=V2=V3 medium-medium-high signature: scope-without-conversion is now flagged from the synthetic perspective as well, indicating era-shifting field expectations.

temperature_pattern: IP-3 self-contradictory absence | papers: [all 9] | profile_consistency: divergent (intensifying with model articulation) | note: U-density per paper grows with the elaboration of mechanistic narrative (Kumada 1972 has 3 U; Kumada 1976b has 5 U; Mazet 2021 has 4 U; Breitenfeld 2014 has 5 U; Cherney 2015 has 10 U; Pengfei 2024 has 7 U; Monnereau 2009 has 4 U; Molander 2016 has 8 U; Morken 2016 has 4 U). U-item severity remains predominantly high or critical even as count grows. Mazet 2021 U-1 reaches severity=critical (V3); Cherney 2015 U-1 reaches 3/3 convergence at high; Pengfei 2024 U-6 reaches 3/3 with V2=V3=high. The "model-prediction-vs-data tension" becomes more visible to multiple agents as papers acquire more elaborate mechanistic models that generate more testable predictions per page.

temperature_pattern: IP-4 selectivity without mass balance | papers: [all 9 except Mazet partial] | profile_consistency: consistent | note: The selectivity/scope-claim-without-mass-balance pattern receives high severity in every methodology paper. Kumada 1972 B-1/B-6 reaches 3/3 convergence; Kumada 1976b U-4 reaches V1+V2 high; Mazet 2021 B-6 reaches V1+V2 high; Pengfei 2024 B-1 reaches V1=medium for explicit mass balance (3/3); Morken 2016 B-1 reaches 3/3 convergence on radical-clock mass balance; Monnereau 2009 B-7/U-1 reaches 3/3 convergence on TOF denominator validity. The gap is genre-stable across method, scope, mechanism, and review formats.

temperature_pattern: IP-5 external benchmarking | papers: [7–8 of 9] | profile_consistency: consistent | note: V1 (synthetic-utility agent) raises severity wherever superiority claims rest on omitted comparisons (Monnereau B-3 V1=high; others V1=medium). The pattern is time-invariant across 52 years and four formats; no paper performs the matched-pair head-to-head comparison its own positioning requires.

temperature_gap (gap whose severity increases across later papers): The strongest temperature_gap signal is **IP-3 self-contradictory absence with respect to DFT-derived predictions**. Pre-DFT, the gap is V2-only (mechanistic agent flags untested predictions like R–R byproduct). Post-DFT, the gap acquires V3 (analytical agent flags computational protocol absence) in addition to V2 (mechanistic agent flags PES/intermediates unobserved). The temperature_gap **increases** because the analytical agent gains a domain to flag (computational protocol audit) that did not exist pre-2005. This indicates that the field's evaluation lens for "computational mechanism" is becoming more contested — V3 severity for DFT-derived predictions has migrated from "tools were unavailable" (era-justified absence) to "tools deployed but unbenchmarked" (era-deficient absence).

---

**Synthesis of sub-group group_unasked_questions**

**G1 group_unasked_question:** [REDACTED: substantial verbatim quotation; see Tier 9]

**G2 group_unasked_question:** [REDACTED: substantial verbatim quotation; see Tier 9]

**G3 group_unasked_question:** [REDACTED: substantial verbatim quotation; see Tier 9]

**Assessment: Facets of a single problem**

The three sub-group questions are **facets of a single underlying problem**, not independent questions. They can be unified as:

**Unified group_unasked_question:**

[REDACTED: substantial verbatim quotation; see Tier 9]

**Relationship of sub-group questions to the unified question:**
- G1 addresses facets (a) + (b): the complete speciation and time-resolved product-distribution question for the dpe/dppe-Ni system, with extension to homogeneous-vs-heterogeneous catalyst identity.
- G2 addresses facets (b) + (c): selectivity quantification across the sp²→sp³ paradigm shift, with explicit emphasis on cross- vs. homo-coupling under each activation mode and the evidentiary basis for paradigm-discriminating mechanism claims.
- G3 addresses facet (c): the evidentiary-standard question — what minimum set of mechanistic evidence validates a cycle, an imported analogy, or a stereochemical model — generalized across the three expansion axes. G3 also surfaces facet (d) implicitly through its shared blind spot of head-to-head benchmarking absent across all three paradigms (RP-5).

The unified question is more than the sum of its parts because it identifies a **methodological deficit at the field level**: no single paper in the 9-paper corpus has simultaneously achieved (a), (b), (c), and (d) for any Ni-catalyzed cross-coupling system. Mazet 2021 comes closest on (a) — characterizing intermediates 9c/III-b for the dppe system specifically — and on (c) — proposing distinct mechanisms for two catalysts — but does not achieve (b) (its bimetallic stoichiometric test leaves ~75–85% unaccounted) and does not achieve (d) (no Felkin-Corriu crossover experiment). Cherney 2015 attempts a corpus-scale view of (c) but reproduces rather than enforces the missing evidentiary standard. Pengfei 2024 deploys the most diverse mechanistic toolkit (CV, SWV, DFT, kinetics, radical clock, TEMPO, racemization) yet still relies on a 2.8 kcal mol⁻¹ DFT discriminator within method error and leaves the anodic half-reaction unspecified despite its decisive influence on yield (85% Fe vs. 30% Zn vs. 17% Mg).

evidence_chain: [Kumada_1972 : B-1 (selectivity w/o byproduct), B-6, U-1, A-2 (cycle from analogy), B-12/U-2 (heterogeneous candidate untested), C-1 (Tamura-Kochi cited not compared) | Kumada_1976b : A-1 (mechanism deferred), B-2 (104% mass balance), C-7 (Felkin-Corriu unexcluded), U-2 (PhI > PhCl > PhBr anomalous) | Mazet_2021 : B-5 (VTNA reliability), B-6 (~85% unaccounted), B-8 (dmpe resting state unidentified), U-1 (rate law not derived) | Breitenfeld_2014 : U-1 (intermediates 10–16 unobserved), U-3 (DFT sole discriminant + B2 imprecision), B-3 (TDS ambiguity), C-6/C-7/C-8 (Yamamoto/Mirica/ref-20 unbenchmarked) | Cherney_2015 : U-1 (Ni¹/Ni³ EPR/CV across 427 refs), U-3 (DKR rate constants absent), CLA-1 (DFT-without-experiment as review-scale norm; PRI-12 candidate), C-1–C-4 (Nobel methods + Consiglio + pre-2008 reviews dropped) | Pengfei_2024 : B-3 (selectivity model in SI), U-1 (homocoupling unreconciled), U-3 (anodic half-reaction absent), U-6 (DFT 2.8 kcal mol⁻¹ within method error), B-8/C-1/C-2 (Lin/Gong cited not compared) | Monnereau_2009 : U-1 (41.8 ppm species oxidation state), U-2 (RE/OA causal chain), B-7 (TOF denominator), C-10 (NiBr₂/propyl prior art not compared) | Molander_2016 : U-1 (NiI/NiIII undetected), U-7 (PES generalisation across 9 substrate classes), B-5 (DFT validation absent), C-1–C-3 (Pd-Suzuki refs cited at dot-matrix level) | Morken_2016 : U-1 (four-intermediate cycle unobserved), B-5/B-6 (RE-retention assumed), B-13 (transmetalation step kinetically untested), C-1–C-6 (Fu/Zhong-Bian/Nakamura/Breit/Carretero/Jarvo cited without numerical comparison)]

---

**Cross-reference with Stage 3 EP filling landscape**

The S3v2 output for Kumada 1972 (v18.4 cascade, English version) identifies six SRGs and two CLAs, with EP packs assigned to each. The 2F sub-group analyses allow assessment of whether the EP filling landscape corresponds to the observed filling order across the 8 EP papers.

| S3 EP pack | S3 target (SRG/CLA) | Papers that partially fill this EP | Filling degree | Notes |
|---|---|---|---|---|
| EP-06a (Analogy validation) | SRG-1 (mechanism cycle imported from (dipy)Ni) | Mazet 2021 (intermediate 9c characterized for dppe); Breitenfeld 2014 (radical bimetallic OA for Nickamine); Monnereau 2009 (calixarene-diphosphine retains analogy without isomorphism test); Molander 2016 (PES from ref-24 generalised); Morken 2016 (SN2 attack-geometry imported) | Partial | Mazet 2021 fills for the dppe system specifically; Breitenfeld 2014 fills for a different catalyst class. Neither validates the original dpe-Ni system's cycle. The remaining post-1972 papers extend rather than fill the analogy-validation gap. |
| EP-03a (Direct observation / state assignment) | SRG-1 (mechanism cycle) | Mazet 2021 (9c/III-b observed by NMR/X-ray); Monnereau 2009 (³¹P NMR 41.8 ppm species without oxidation-state assignment) | Partial | Only the dppe system OA complex characterized; the dmpe resting state remains unidentified (Mazet B8). The 41.8 ppm species in Monnereau is observed but its oxidation state is not assigned. Ni⁰ vs. Ni(II) homogeneous-vs-heterogeneous question for the original [NiCl₂(dpe)] system is unanswered in any post-1972 paper. |
| EP-04a (Discrimination / replication) | SRG-2 (selectivity claim; cross- vs. homo-coupling) | Kumada 1976b (benzene monitored for some Table 3 entries); Pengfei 2024 (homo-coupling 17%+13% reported once at Entry 1 of model reaction); Morken 2016 (n=2 averaging without SD) | Minimal | No paper provides complete mass balance across the scope. Pengfei 2024 reports byproducts but does not reconcile them with the proposed selectivity model. |
| EP-01a (Reporting coherence) | SRG-5 (Table I analytical quality) | Kumada 1976b (GLPC instrument and column stated; FID response factors absent; mass-balance violation in Table 2 unacknowledged); Mazet 2021 (VTNA method named without statistics); Pengfei 2024 (DFT methodology compressed into Supplementary) | Partial | Kumada 1976b improves over 1972 but still lacks calibration and has internal inconsistency. The 2009–2024 papers do not retroactively improve the 1972 analytical record. |
| EP-07a (Boundary test) | SRG-3 (sp³ exclusion without negative-result data) | Breitenfeld 2014, Pengfei 2024 (sp³ coupling achieved); Cherney 2015 review (documents sp³ frontier traversal across multiple groups); Morken 2016 (asymmetric sp³ via cyclic sulfate) | Substantial | The sp² boundary is **completely overcome** by radical / electrochemical / asymmetric methods. However, the boundary is *circumvented by paradigm shift* rather than tested within the original 2-electron paradigm. The S3 ER for SRG-3 (a single failed-example datum from n-BuMgBr + n-BuCl under [NiCl₂(dpe)]) is never reported in any paper. |
| EP-09a (Internal benchmark) | SRG-2 + CLA-1/CLA-2 (utility; Tamura-Kochi vs. Corriu-Masse) | Kumada 1976b (broader scope vs. 1972); Monnereau 2009 (dppp comparison at one substrate, one loading); Molander 2016 (Figure 1B qualitative dot-matrix); Morken 2016 (Fu/Zhong-Bian/Nakamura cited without er comparison) | Minimal | No paper performs the specific Tamura-Kochi (Ag/Cu/Fe) vs. Kumada [NiCl₂(dpe)] head-to-head comparison or the concurrent Corriu-Masse Ni(acac)₂ vs. Kumada NiCl₂(dpe) head-to-head comparison. |
| EP-04a' (Stereochemical replication) | SRG-4 (cis:trans 80:20 / 43:57 by undisclosed method) | None | Unfilled | Mazet 2021's temperature-dependent E/Z reversal of 3ce extends the lineage stereochemical-observation pattern but is not a discriminating measurement of the 1972 ratios. |

**VQ hierarchy correspondence to filling order:**

The S3v2 analysis places Kumada 1972 at VQ-1 (Observation) with VQ-2 advancement blocked primarily by RI-04 / RI-09 (selectivity-evidence integrity, SRG-2), RI-01 / RI-04 (analytical quality, SRG-5), and RI-07 (unsupported boundary, SRG-3). VQ-3 advancement requires SRG-1 mechanistic resolution.

- **SRG-3 / RI-07 (sp² boundary):** Substantially filled by paradigm shift (G2 papers). However, this filling does not test the boundary within the original 2-electron paradigm — it circumvents it. The S3 ER (a single sp³ failed-example datum under original conditions) remains uncollected.
- **SRG-5 / RI-01 (analytical quality):** Only partially filled. The 2009–2024 papers do not retroactively improve the 1972 data; each paper reproduces the convention of underdocumented primary measurement.
- **SRG-1 / RI-06 (mechanism by analogy):** Partially filled by Mazet 2021 for the dppe system specifically and by radical mechanism papers for different catalyst systems. The original dpe-Ni mechanism remains analogically derived 53 years later (1972–2025).
- **SRG-2 / RI-04 (cross- vs. homo-coupling selectivity):** Minimally filled. Mass balance closure is paradigm-invariant absent across the 9-paper corpus.
- **SRG-4 (stereochemical outcome):** Unfilled; the 1972 cis:trans ratios are never re-measured by a disclosed method.

**Key observation:** The EP filling order does NOT follow the VQ hierarchy. The VQ-2-blocking RI-07 (sp² boundary) was filled substantially by paradigm shift, while the equally VQ-2-blocking RI-01 (analytical quality) and RI-04 (selectivity) were filled only partially or minimally. The VQ-3-level RIs (RI-03, RI-06 — mechanism) were partially filled by Mazet 2021 (dppe) and Breitenfeld 2014 (Nickamine) before VQ-2 was fully resolved. This suggests that the field prioritizes **paradigm expansion** (RI-07 filling via new mechanisms / new substrate classes / new activation modes) over **analytical consolidation** (RI-01 / RI-04 filling via improved reporting and mass-balance closure). The incentive structure flagged in IP-2 — incentive-suppressed reporting of replication, calibration, and uncertainty — is consistent with this filling order: the corpus's filling pattern reflects what is publishable rather than what is logically prior.

A second-order observation: the PRI-12 candidate (DFT-without-experiment as review-scale norm) anchored single-paper in Cherney 2015 receives partial cross-paper support from the G2 paradigm-competition analysis. Across Breitenfeld 2014, Cherney 2015, Pengfei 2024, and Molander 2016, DFT serves as the sole or dominant pathway discriminator without consistent benchmarking, functional-and-basis disclosure, or uncertainty propagation. This is not yet sufficient for PRI-12 promotion (which requires another review or multi-system paper anchor), but the cross-paradigm consistency strengthens the case for PRI-12 as a candidate priority for v18.5/v19 development. The G2 sub-group explicitly flagged this as the dominant integrative observation for review-genre expansion.

---

**Integrated group_unasked_question**

[REDACTED: substantial verbatim quotation; see Tier 9]

This question integrates the three sub-group questions as follows:
- From G1: the demand for complete speciation and time-resolved product profiles (facets i + ii) within the original dpe/dppe-Ni Grignard lineage.
- From G2: the demand for a quantitative selectivity model spanning sp²→sp³ and chemical-reductant→electrochemical transitions (facets ii + iii), with evidence beyond DFT and analogy.
- From G3: the demand for an agreed evidentiary standard for mechanistic / imported-analogy / stereochemical claims across coexisting paradigms (facets iii + iv), with attention to the cross-paradigm shared blind spot of head-to-head benchmarking absent.

The question is not answered by any paper in the 9-paper corpus. Its persistence across 53 years (1972–2025), 9 papers, 5 paradigms (2-electron Ni(0)/Ni(II), Ni(I)/Ni(III) radical bimetallic, photoredox/Ni dual catalysis, electrochemical Ni(I/II/III), asymmetric Ni/PyBox), and 8 journals constitutes the strongest available evidence that it represents a field-wide structural convention — the convention that scope demonstration takes priority over mechanistic proof, that catalytic cycle proposals serve narrative contextualization rather than predictive falsification, that DFT energy differences are accepted as mechanistic discriminators in the absence of complete experimental discrimination, and that head-to-head comparison against prior art is consistently substituted by qualitative citation.

The convention persists despite radically expanded analytical and computational capability across the 53-year span. The 1972 communication compresses analysis under genuine tool unavailability (structurally suppressed). The 2024 Nature Catalysis full paper deploys CV, SWV, DFT, kinetics, radical clock, TEMPO, and racemization simultaneously yet still leaves the anodic half-reaction unspecified, the DFT discriminator within method error, and the homocoupling distribution unreconciled (individually chosen + incentive-suppressed). The era-dependent diagnosis applies to most recurring roots: structurally suppressed in 1972/1976 → individually chosen by 2014–2024 → incentive-suppressed at the field level (Cherney 2015's review function reproduces rather than enforces the standard).

evidence_chain: [All 9 papers contribute through their IP-1, IP-2, IP-3, IP-4, and IP-5 patterns as documented in G1/G2/G3 analyses; the strongest single-paper anchors at each level are Cherney_2015 U-1 (3/3 convergence on Ni¹/Ni³ EPR/CV absent) for facet (iii); Pengfei_2024 U-1 (homocoupling reported but unreconciled with selectivity model) for facet (ii); Mazet_2021 B-6 (~75–85% unaccounted in stoichiometric proof-of-concept) for facet (ii); Mazet_2021 A-3 (3/3 convergence on bimetallic mechanism evidence basis) for facet (i); and the universal absence of matched-pair shared-substrate comparison across all 9 papers for facet (iv)]

TEMPERATURE_SUMMARY cross-reference: The strongest convergence items across all sub-groups share a common structure — they are the items where all three viewpoints (synthetic V1, mechanistic V2, analytical V3) agree that a gap exists with high or critical severity. The 3/3 high-convergence items are:
- Kumada 1972 B-4 (3/3 medium-medium-medium = sp³ exclusion without negative-result evidence; SRG-3)
- Kumada 1976b B-2 (3/3 = 104% mass-balance violation unacknowledged)
- Mazet 2021 A-3 (3/3 high = bimetallic mechanism evidence basis)
- Breitenfeld 2014 B-1 (3/3 = kinetic measurement validity for radical-clock procedure)
- Cherney 2015 U-1 (3/3 high = Ni¹/Ni³ EPR/CV absent across 427 cited references; the **single highest-temperature item** in the corpus)
- Pengfei 2024 B-1 (3/3 medium = mass balance not closed; "synthetic potential" claim w/o byproduct accounting) and U-6 (3/3 with V2=V3 high = DFT 2.8 kcal mol⁻¹ within method error)
- Monnereau 2009 B-7 / U-1 (3/3 = TOF denominator validity)
- Morken 2016 B-1 (3/3 = radical-clock mass balance) and B-6 (3/3)
- Molander 2016 B-5 cluster / U-1 / U-2 (3/3 with V1=V2=V3 high = DFT validation absence + NiI/NiIII undetected + spin-manifold consistency unverified) — "DFT model extrapolation" reaching V1+V2+V3 high

The 3/3-convergence items across the corpus collectively point to the same unified question: the field has not produced the complete, quantitative, experimentally validated account that the unified question demands. The convergence of the agent-frame severity assessments grows monotonically across the corpus (1/3 → 2/3 → 3/3 from 1972 to 2024), indicating that what was a single-discipline concern in 1972/1976 has become a multi-discipline concern by 2014–2024. The S3 ER for SRG-1 (dpe-Ni elementary-step characterization under operating conditions) remains the highest-leverage unfilled EP across the 53-year span: no paper has independently synthesized [dpe-Ni(R)(Cl)] or [dpe-Ni(R)₂] and demonstrated that stoichiometric reactions reproduce catalytic selectivity, and no paper has performed a mercury-drop / hot-filtration test on the original [NiCl₂(dpe)] system to distinguish homogeneous Ni(II) from heterogeneous Ni⁰.

---

**Anomalies vs. sub-group level analyses**

- The integration corroborates the G1/G2/G3 individual assessments rather than introducing significant new patterns; all 5 IPs (IP-1 through IP-5) were independently flagged by at least two sub-groups, and 3 of 5 (IP-1, IP-2, IP-3) were flagged by all three sub-groups in structurally identical form. This is the strongest available within-corpus convergence signal in the analysis.
- One pattern is *promoted* in the integration relative to sub-group level: the **DFT-as-discriminant prerequisite-absence** pattern, flagged at sub-group level only in G2 (RP-3) and partially in G3 (Molander), recurs across 5 of the 9 papers (Breitenfeld, Cherney, Pengfei, Molander, and Mazet partially) and forms a cross-paradigm signature consistent with the PRI-12 candidate. This is more visible at integration scale than at sub-group scale.
- One pattern is *contained* in the integration: the **stereochemical-observation-without-attribution** root recurs across all three G1 papers in identical form but is absent from G2/G3, indicating that it is a lineage-specific rather than corpus-wide convention. The integration confirms its lineage-specificity by absence elsewhere.
- One pattern is *paradigm-conditional*: imported-model prerequisite-absence (DFT functional / reference electrode / spin state / anode characterization) is present in 5 of 9 papers and absent in the 4 pre-DFT or non-electrochemical papers (1972, 1976b, 2009, Morken 2016 partial). This conditional emergence is consistent with G2/G3's individual diagnoses and indicates that prerequisite-absence as a category emerges only when the requisite tooling is deployed; it is not a defect of the A/B/C framework but a paradigm-conditional U-item subtype.
- The G2 sub-group's PRI-12 candidate (Field-consensus overread, single-paper anchor in Cherney 2015) survives the integration: while no second review or multi-system paper is in the corpus to provide the second anchor, the cross-paradigm propagation of DFT-without-experiment across Breitenfeld / Cherney / Pengfei / Molander indicates that the candidate has empirical support beyond Cherney 2015 itself. This integration provides the cross-paper warrant that single-paper Stage 2 cannot, while still preserving the formal rule that PRI-12 promotion requires a second review-genre or multi-system paper anchor.

---

*End of integration output (v18.4 / Opus 4.7).*

---

> **Tier 8 redaction notice**: This file is a redacted copy of the corresponding Tier 3 / Tier 9 output. Verbatim source-paper quotations have been replaced by `[REDACTED: see source paper §<loc>; full text retained in Tier 9 reviewer-only deposit]` markers, preserving location references and our own analytical content. Bibliographic fields (title, authors, journal, year, DOI), analytical labels (`evidence_chain:` with B-/U-/A-/C- internal IDs), short technical terms, and our own analytical text are not redacted. The redaction was applied by `scripts/redact_for_tier8.py` and, for this version, by `scripts/build_paperA_R1_public.py` with `scripts/redact_source_ngram_runs.py` (scripts of the project repository; they are not deposited).
