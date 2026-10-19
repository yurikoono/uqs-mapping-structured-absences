prompt_version: stage2f-v6-20260329

group: G1 — Direct Lineage
papers: Kumada 1972 (JACS Communication), Kumada 1976b (BCSJ Full Paper), Mazet 2021 (ACS Catalysis)
model_info: claude-opus-4-7

---

[F] Within-Group Comparison

---

## repeated_patterns

**RP-1: Catalytic cycle proposed without complete elementary-step validation in the actual catalytic system**

All three papers propose Ni-phosphine catalytic cycles for cross-coupling but never validate every elementary step under the exact catalytic conditions used to generate the scope/yield data. The depth of available technique grows across the series, yet the "complete cycle validation" gap persists.

- Kumada 1972: Proposed Ni(II) cycle (eqs 2–4) is constructed entirely by analogy with stoichiometric (dipy)Ni reactions; no intermediate observed under [NiCl₂(dpe)] catalytic conditions; black mixture observation (B-12) consistent with Ni⁰ left uncharacterized.
- Kumada 1976b: Scheme 1 explicitly labeled "rationalization, not elucidation" ("the mechanism has not yet been fully clarified"); aging-experiment yellow species (B-7) — the only direct in-paper evidence of a catalytically competent Ni-organic species — characterized only by color; competing Felkin-Corriu mechanism acknowledged (C-7) but not experimentally excluded.
- Mazet 2021: Multiple intermediates synthesized and X-ray characterized (7c/7d, 9c), but the bimetallic transmetalation intermediate IV is never observed (B11/SRG-2); dmpe Ni(0) species 6d not quantifiable (A-8/SRG-3); proposed bimetallic TM step rests on three-point VTNA under acknowledged deactivation (B5).

```
evidence_chain: Kumada_1972 : A-2, U-2, B-12 (SRG-1) ; Kumada_1976b : A-1, U-1, U-2, C-7 (SRG-1), B-7 ; Mazet_2021 : SRG-1 (A-3, B-5, U-1, U-2), SRG-2 (A-3, B-6, C-3)
```

---

**RP-2: Quantitative analytical foundation for yield/order claims undercharacterized or internally inconsistent**

All three papers' core quantitative claims rest on a single analytical pillar (glpc/GLPC/VTNA) whose calibration, replication, or method-precondition is incompletely specified.

- Kumada 1972: Dual yield-basis (isolated vs. glpc-only) within one Table column without systematic justification (B-2); internal standard, response factors, and calibration undisclosed (B-2, B-7); no replicate data (B-9).
- Kumada 1976b: GLPC response factors not documented across ~60 entries (B-10); internal standard inconsistently identified across tables (mesitylene / "normal alkane" / unspecified, B-1, B-10); Table 2 mass balance violation: butylbenzene 69% + benzene 35% = 104% (B-2/SRG-2) unacknowledged; single Silicone DC 550 column not validated for structural diversity (B-9).
- Mazet 2021: Three-point VTNA for second-order catalyst assignment (B-5); no goodness-of-fit statistics; method's precondition (constant catalyst concentration) violated by acknowledged deactivation (U-2/SRG-1); Grignard order undefined / contradictorily assigned across systems (B-7).

```
evidence_chain: Kumada_1972 : B-2, B-7, B-9, SRG-5 ; Kumada_1976b : B-1, B-2, B-10, SRG-2 ; Mazet_2021 : B-5, B-7, U-2, SRG-1
```

---

**RP-3: Selectivity / mass-balance against the principal competing pathway not quantitatively benchmarked**

The selectivity claim that anchors each paper is asserted by absence rather than measured.

- Kumada 1972: "Selective" is the title keyword; eq 3 explicitly predicts homo-coupling product R–R as a stoichiometric byproduct of intermediate formation; no R–R quantified or acknowledged below detection limit (B-6, U-1).
- Kumada 1976b: β-hydride suppression invoked as "the most remarkable feature" (CLA-2); olefin byproducts (1-butene, propylene) from β-hydrogen-bearing alkyl Grignard reagents not systematically searched for; single GLPC column not validated for volatile C₄–C₆ olefins (U-3, B-9). Benzene formation (homo-coupling index) reported for some Table 3 entries but "not determined" for others (B7).
- Mazet 2021: Mass balance for stoichiometric bimetallic experiment (Figure 9) accounts for only ~15–25% of theoretical (B-6/SRG-2); ~75–85% of material unaccounted; no replicate runs / uncertainty for any scope entry (B-17, RI-08); 16% NMR yield of OA complex 9d with no mass-balance discussion (B-8/SRG-3).

```
evidence_chain: Kumada_1972 : B-6, U-1 ; Kumada_1976b : U-3, B-9, B-7 ; Mazet_2021 : B-6 (SRG-2), B-8 (SRG-3)
```

---

**RP-4: Catalyst-system positioning asserted without numerical head-to-head benchmark on shared substrates**

Each paper claims advantage over a prior or competing system; none provides a matched-substrate quantitative comparison.

- Kumada 1972: Tamura-Kochi Fe/Cu catalysts (C-1) and Corey cuprates/π-allylnickel (C-2) cited and dismissed without yield comparison; concurrent Corriu-Masse Ni(acac)₂ acknowledged in proof but not compared (A-4/SRG-6).
- Kumada 1976b: Kharasch background (C-1), Murahashi Pd-phosphine (C-2), Posner/Normant/Collman cuprates (C-3) all cited as inferior baselines without side-by-side substrate matching.
- Mazet 2021: Martin, Tobisu/Chatani/Mori, Balcells/Hazari prior C(sp²)–O mechanistic studies (C-2, C-6) cited to establish "mechanism is ligand/substrate sensitive" without reproducing rate constants or barriers; ref 15 (Wendt; Qi/Diao) "low RE barrier" claim imported from a different Ni system without isomorphism check (C-3/SRG-2 secondary RI-06).

```
evidence_chain: Kumada_1972 : C-1, C-2, A-4 (SRG-6) ; Kumada_1976b : C-1, C-2, C-3 ; Mazet_2021 : C-2, C-3, C-6
```

---

**RP-5: Ligand-effect attribution without multi-variable deconvolution**

All three papers attribute differential catalyst performance to a single ligand property derived from a low-dimensional comparison.

- Kumada 1972: Activity order [NiCl₂(dpp)] > [NiCl₂(dpe)] > [NiCl₂(dmpe)] ≈ [NiCl₂(PPh₃)₂] ≫ [NiCl₂(PEt₃)₂] attributed to [REDACTED: substantial verbatim quotation; see Tier 9] as "the first requisite" — the cis-geometry hypothesis is not separated from bite angle, electronics, or cone angle effects (B-3, U-4 from D-4 Candidate 7).
- Kumada 1976b: dppp > dppe activity reversal explained via the "overly stable [Ni(dppe)(CH₂SiMe₃)₂]" hypothesis grounded in an inaccessible reference (C-8); dmpe-specific failure with cyclopropyl Grignard 2b and isomerization with 2c (Mazet's A-7 antecedent in Mazet's reading) not mechanistically rationalized (A-4 narrative around "hard to find valid reasons" — recalled by Mazet's framing).
- Mazet 2021: The dppe/dmpe OA reactivity difference toward adamantyl 1d (0% vs ~50% with vinyl bromide 8d) attributed to sterics from %VBur(7c)=48.9 vs %VBur(7d)=43.1 in cod complexes — a 5.8-percentage-point difference measured in non-catalytic intermediates without electronic deconvolution (B-3, B-4, CLA-2).

```
evidence_chain: Kumada_1972 : B-3, D-4 Candidate 7 ; Kumada_1976b : C-8 ; Mazet_2021 : B-3, B-4, CLA-2
```

---

## temperature_patterns

```
temperature_pattern: RP-1 (cycle proposed without elementary-step validation) | papers: [Kumada_1972, Kumada_1976b, Mazet_2021] | profile_consistency: divergent | note: Severity profile shifts across the series. Kumada_1972 A-2 reaches V1=high+V2=high (convergence 2/3) for the entire mechanistic gap; Kumada_1976b U-1/U-2 are V2-driven (low_convergence_high_gap) and the SRG-1 gap migrates from "no intermediate observed" to "intermediate observed by color only"; Mazet_2021 elevates this exact pattern to V1=V2=V3=high (convergence 3/3 on A-3 and B-5) — every adjacent-field agent flags the same gap, while individual severities for sub-items grow as the field's expected granularity tightens.
```

```
temperature_pattern: RP-2 (analytical foundation incomplete) | papers: [Kumada_1972, Kumada_1976b, Mazet_2021] | profile_consistency: consistent | note: V3 (analytical / chemical-kinetics agent) consistently flags this pattern at medium-to-high across all three (Kumada_1972 B-2 V3=medium; Kumada_1976b B-1 V3=high, B-10 V3=high; Mazet_2021 B-5 V3=high, B-7 V3=high). The instrument changes (glpc → GLPC → VTNA + in-situ IR) but the V3 severity stays in the same band — quantitative-method validation is the load-bearing axis whose under-reporting is genre-stable across journals and 50 years.
```

```
temperature_pattern: RP-3 (selectivity / mass-balance absence) | papers: [Kumada_1972, Kumada_1976b, Mazet_2021] | profile_consistency: consistent | note: Kumada_1972 B-6/U-1 V2=V3=high (3/3 effective); Kumada_1976b U-3 V2=high (1/3, but the issue is the pattern, not convergence); Mazet_2021 B-6 V1=high+V2=high (2/3). The [REDACTED: substantial verbatim quotation; see Tier 9] pattern persists at high severity even as the analytical infrastructure becomes more capable — i.e., the gap is increasingly indefensible by era norms (see §era-norm consistency below).
```

```
temperature_pattern: RP-5 (ligand-effect attribution under-determined) | papers: [Kumada_1972, Kumada_1976b, Mazet_2021] | profile_consistency: divergent | note: Kumada_1972 attributes activity order to a single hypothesis (cis-geometry, V1-Q6 medium); Kumada_1976b leaves the dppp/dppe/dmpe ordering essentially unrationalized within the paper; Mazet_2021 explicitly invokes %VBur as a quantitative-looking proxy (V1=high, V2=high, convergence 2/3 on B-4) — but the proxy is measured in the wrong geometry. Severity rises across the series; this is the one RP whose temperature_gap appears to widen — what was a soft hand-waving in 1972 has become a quantitative claim that demands quantitative defense by 2021.
```

---

## recurring_roots

```
recurring_root: Catalytic cycle assembled by analogy / proxy rather than internal step-by-step verification | papers: [Kumada_1972, Kumada_1976b, Mazet_2021] | member_items: Kumada_1972 SRG-1 (A-2, U-1, U-2, B-12) ; Kumada_1976b SRG-1 (A-1, A-1d, U-1, U-2, C-7) and SRG-4 (A-5, C-5) ; Mazet_2021 SRG-1 (A-3, A-4, A-5, B-5, B-7, U-1, U-2) and SRG-2 (A-3, B-6, C-3) | note: Structural gap. The "external proxy" identity changes — (dipy)Ni stoichiometric reactions in 1972, Jolly-Wilke / Morrell-Kochi reviews in 1976, Wendt 2007 + Qi/Diao 2020 + Balcells/Hazari DFT in 2021 — but the structural move is identical: an authority citation licenses an elementary-step claim that the paper itself does not verify under its own catalytic conditions. The 54-year persistence of this root, despite the maturation of NMR / X-ray / VTNA / DFT, is the central methodological observation of G1.
```

```
recurring_root: Quantitative claims without the analytical metadata required to evaluate them | papers: [Kumada_1972, Kumada_1976b, Mazet_2021] | member_items: Kumada_1972 SRG-5 (B-2, B-7, B-9, B-11) ; Kumada_1976b SRG-2 (B-1, B-2, B-10, B-5) and SRG-7 (B-5, B-14) ; Mazet_2021 SRG-1 (B-5, B-7, U-2) | note: Genre convention with rising gap. Yield/order/selectivity numbers are reported without the calibration, replication, or precondition documentation needed to evaluate them. Reporting standard within each era is met at the time of publication (era-norm tolerated for Kumada_1972/1976b), but Mazet 2021's three-point VTNA under acknowledged deactivation falls into the era-deficient bucket because the cited methodology paper (Burés 2016) explicitly defines preconditions that are simultaneously acknowledged as violated.
```

```
recurring_root: Selectivity / mass-balance claim supported by absence of byproduct rather than measured suppression | papers: [Kumada_1972, Kumada_1976b, Mazet_2021] | member_items: Kumada_1972 SRG-2 (B-6, U-1, C-1) ; Kumada_1976b CLA-2 (U-3, B-9) and B-7 ; Mazet_2021 SRG-2 (B-6) and SRG-3 (B-8) | note: Structural-and-individual hybrid. "Selective" or "mass-balanced" is treated as established when no byproduct is reported, in spite of mechanism-internal predictions (eq 3 in 1972; β-hydride elimination in 1976; bimetallic TM statistical distribution in 2021) that there should be a quantifiable byproduct. Each paper has the analytical capability to detect the predicted byproduct and does not deploy it.
```

```
recurring_root: Ligand-effect attribution from a low-dimensional or wrong-geometry comparison | papers: [Kumada_1972, Kumada_1976b, Mazet_2021] | member_items: Kumada_1972 B-3, D-4 Candidate 7 ; Kumada_1976b A-4 narrative (dppp/dppe ordering "hard to find valid reasons"), C-8 ; Mazet_2021 SRG-3 indirectly + CLA-2 (B-3, B-4) | note: Structural gap. Multi-variable phosphine-effect deconvolution (steric vs. electronic vs. bite-angle vs. chelate-ring-size) requires systematic ligand libraries that exceed any single paper's scope. Mazet's choice to use cod-complex %VBur — measurable from in-paper X-ray data of the actually catalytically relevant 9c — is the one case where the gap is individually chosen rather than structurally suppressed (see suppression_diagnostic below).
```

---

## suppression_diagnostic

| Pattern | Diagnostic | Reasoning |
|---|---|---|
| RP-1 (cycle proposed without elementary-step validation) | Structurally suppressed → individually chosen (evolving) | In 1972/1976, the mechanistic toolkit (in-situ NMR of catalysis intermediates, low-T NMR for transient species, VTNA, DFT) was either nascent or not standard for synthetic-organometallic publication. By 2021, every relevant tool is available and Mazet deploys most — yet the bimetallic TM intermediate IV is not observed and the kinetic model is not numerically integrated (Mazet U-1, critical severity). The residual gap in 2021 is individually chosen; in 1972/1976 it was structurally suppressed. |
| RP-2 (analytical foundation incomplete) | Genre convention | The level of analytical documentation in each paper matches the journal/era norm. Kumada_1972 (JACS Communication 1972) and Kumada_1976b (BCSJ full paper 1976) meet the 1970s reporting standard; Mazet_2021's three-point VTNA matches 2021 ACS Catalysis norms (era-norm tolerated per Mazet §4). The persistence at high temperature across three journals and three eras suggests the convention itself is the gap. |
| RP-3 (selectivity / mass-balance absence) | Individually chosen | Mass-balance and byproduct quantification were technically feasible in all three eras using the analytical infrastructure each paper already deployed (glpc / GLPC / NMR + GC-MS). The consistent omission across 50 years suggests an active field-wide choice to treat selectivity as a binary descriptor rather than a quantitative metric. |
| RP-4 (no head-to-head benchmark) | Individually chosen | Each paper had access to the prior/competing systems' published data (or, for 1972 vs Corriu-Masse, the concurrent communication) and could have run a single matched-substrate comparison. The omission is positioning by exclusion, not technical impossibility. |
| RP-5 (ligand-effect attribution under-determined) | Mixed (structurally suppressed for the systematic library; individually chosen for the wrong-geometry proxy) | Building a 12-ligand systematic library is a dedicated paper; that aspect is structurally suppressed. But Mazet's choice to measure %VBur on the cod complex 7c when the X-ray structure of the OA complex 9c was already in hand is individually chosen — the in-paper data make the catalytically relevant geometry available, the paper instead reports the non-catalytic geometry. |

---

## paradigm_competition

This group reveals **paradigm succession**, not paradigm competition. Three sequential paradigms occupy the same problem space:

**Paradigm 1 — Empirical method establishment (Kumada 1972, JACS communication)**
- Operating goal: demonstrate that Ni-phosphine complexes catalyze selective cross-coupling.
- Systematically unanswered: what is the actual catalytic mechanism? what is the quantitative selectivity? where is the sp²/sp³ boundary?
```
evidence_chain: Kumada_1972 : A-2 ([REDACTED: substantial verbatim quotation; see Tier 9]) ; Kumada_1972 : B-1 ("conditions are not necessarily optimum")
```

**Paradigm 2 — Scope cartography (Kumada 1976b, BCSJ full paper "I.")**
- Operating goal: define the substrate scope and identify the best catalyst per substrate class. Title series-marker "I." signals planned mechanistic / stereochemical follow-up papers.
- Systematically unanswered: which elementary step is rate-determining? what is the failure mode for alkyl Grignard + dihaloethylene? why does dppp beat dppe? — and in which step does Mg-vs-Li specificity operate?
```
evidence_chain: Kumada_1976b : A-1 ([REDACTED: substantial verbatim quotation; see Tier 9]) ; Kumada_1976b : A-2 ("one of the most serious limitations") ; Kumada_1976b : A-5 ([REDACTED: substantial verbatim quotation; see Tier 9]); Kumada_1976b : C-7 (Felkin-Corriu acknowledged but not excluded)
```

**Paradigm 3 — Mechanistic elucidation (Mazet 2021, ACS Catalysis)**
- Operating goal: characterize intermediates, assign rate-determining step, propose a complete catalytic cycle distinguishing two structurally similar precatalysts.
- Systematically unanswered: what is the activation barrier of the bimetallic TM step? what controls E/Z selectivity reversal? what is the mass balance of the stoichiometric bimetallic experiment? what is the dmpe-specific failure mechanism with Grignard reagent 2b that motivated the entire study?
```
evidence_chain: Mazet_2021 : A-3 ("we propose ... rate-determining transmetalation between (I-a) and (III-b)") ; Mazet_2021 : A-6 (E/Z reversal not analyzed) ; Mazet_2021 : A-7 (dmpe-specific anomalies with 2b/2c never revisited in Results) ; Mazet_2021 : U-1 (no kinetic model integration, critical severity)
```

The relationship is sequential: Paradigm 1's deferral ("Further studies are required") becomes Paradigm 2's task ([REDACTED: substantial verbatim quotation; see Tier 9]), whose deferral ("the mechanism has not yet been fully clarified") becomes Paradigm 3's founding problem ([REDACTED: substantial verbatim quotation; see Tier 9]). Each paradigm's blind spot is the next paradigm's entry point.

**Critical observation 1 — succession, not closure:** Paradigm 3 does not close Paradigm 1's foundational selectivity question. The cross:homo product ratio that Kumada 1972 implied but never quantified (SRG-2) is not quantified in Mazet 2021 either. Mazet's mass-balance gap (~75–85% unaccounted in Figure 9) is the 2021 echo of the same structural absence.

**Critical observation 2 — substrate-class transposition:** The three papers operate on different but lineage-connected substrate classes (sp² aryl/vinyl halides → broader aryl/alkenyl halides + first C–F OA → enol phosphates / C(sp²)–O electrophiles). Each substrate class transposition introduces new sub-paradigm-specific gaps (e.g., the phosphate→bromide ion exchange in Mazet has no analogue in the 1972/1976 halide systems). When Mazet inherits Paradigm 1's Ni(0)/Ni(II) framework, it inherits the gap structure too.

**Critical observation 3 — gap re-submergence:** Some 1972/1976 gaps disappear from the 2021 paradigm not because they are resolved but because they fall outside the new paradigm's scope (e.g., MgX₂ byproduct accumulation: invisible in Kumada 1972, predicted-but-uncharacterized in Kumada 1976b U-1, unaddressed in Mazet 2021 despite VTNA being sensitive to salt effects). This is the mechanism by which paradigm succession masquerades as paradigm progress.

---

## divergences

**DV-1: Substrate class — sp² halides (1972/1976) vs. C(sp²)–O electrophiles (2021)**

```
evidence_chain: Kumada_1972 : B-4 ([REDACTED: substantial verbatim quotation; see Tier 9]) ; Kumada_1976b : Tables 6–7 (aryl/alkenyl halides) ; Mazet_2021 : S0-3 (enol phosphates), B-7 from Mazet (phosphate-to-bromide ion exchange is the dppe-specific step with no analogue in halide systems)
```

Accounts for divergence: The C(sp²)–O electrophile field emerged in the 2000s driven by phenol-derived electrophile cost and waste advantages. The Mazet paper explicitly addresses a 40-year gap between Wenkert's introduction of enol phosphates (~1979) and any mechanistic study. Substrate class transposition introduces the phosphate-to-bromide ion exchange pathway that had no counterpart in Kumada 1972/1976b.

---

**DV-2: Experimental depth — Communication-format compression (1972) → tabular scope (1976) → multi-modal mechanistic study (2021)**

```
evidence_chain: Kumada_1972 : B-1 (Table I disclaimer "conditions are not necessarily optimum") ; Kumada_1976b : Table 7 (~60 entries with the same disclaimer carried forward) ; Mazet_2021 : Figures 2–9 (NMR / X-ray / VTNA / radical clock / TEMPO / SambVca steric maps)
```

Accounts for divergence: Year (1972 → 1976 → 2021), journal format (3-page communication → BCSJ full paper → ACS Catalysis 10-page research article), and the maturation of the experimental toolkit. Yet the depth of evidence required to certify the central mechanistic claim has scaled with the available techniques: VQ-3 fails for all three papers (Kumada_1972 fails for Layer 2 mechanism; Kumada_1976b fails for Layer 2 Scheme 1 + Layer 3 PhF landmark; Mazet_2021 fails for Layer C bimetallic TM). The depth of the failure converges even as the depth of the evidence diverges.

---

**DV-3: MgXX′ stoichiometric byproduct visibility — invisible (1972) → predicted-but-uncharacterized (1976) → re-submerged (2021)**

```
evidence_chain: Kumada_1972 : "no textual basis in Kumada_1972" (retrospective — the 1972 paper does not discuss MgXX′ formation); Kumada_1976b : U-1 antecedent (Stage 1 unreported_data: "MgXX' predicted by stoichiometry but uncharacterized"); Mazet_2021 : "no textual basis in Mazet_2021" (retrospective — MgBr₂ accumulation not discussed despite VTNA being sensitive to salt-induced rate effects)
```

Accounts for divergence: The MgXX′ gap becomes visible exactly when stoichiometric scope is being defined (1976) and re-submerges when the paradigm shifts to mechanistic kinetics (2021). VTNA's same-excess-experiment failure (Mazet's A-4 and U-2) is potentially attributable in part to MgBr₂ accumulation — a hypothesis that Mazet's data could test but the paper does not raise. This is a paradigm-succession-induced gap re-submergence: the question is not closed in 2021; it is moved out of frame.

---

**DV-4: Landmark "first" claim treatment — absent (1972) → present and undersupported (1976) → absent (2021)**

```
evidence_chain: Kumada_1972 : (no landmark [REDACTED: verbatim source quotation; see the source paper via its DOI] claim, but bimetallic TM is framed as [REDACTED: verbatim source quotation; see the source paper via its DOI] — supported by three-point VTNA + low-yield stoichiometric proof-of-concept)
```

Accounts for divergence: The 1976 PhF landmark claim is fatal at VQ-1 (no isolated yield, co-elution acknowledged then circumvented without explanation). Mazet 2021's "never observed[REDACTED: substantial verbatim quotation; see Tier 9]landmark claim under-supported by the paper's own data" pattern recurs across the lineage, suggesting a structural feature of mechanistic novelty publication rather than an isolated error.

---

## recurring_U

```
recurring_U: Self-contradictory absence — paper's own model predicts an observable that the paper's own data fail to test or report | papers: [Kumada_1972, Kumada_1976b, Mazet_2021] | item_ids: [Kumada_1972: U-1 (eq 3 predicts R–R; not reported), U-2 (Ni(II) cycle predicted; black mixture consistent with Ni⁰ uncharacterized) ; Kumada_1976b: U-1 (Scheme 1 vs Felkin-Corriu crossover not performed), U-3 (β-hydride suppression invoked; volatile olefins not searched), U-5 (PhF landmark claim under co-elution constraint), U-2 (anomalous reactivity order PhI>PhCl>PhBr that Scheme 1 cannot explain) ; Mazet_2021: U-1 (kinetic model not integrated to confirm bimetallic apparent second-order; critical severity), U-2 (VTNA preconditions cited then violated), U-3 (radical-clock without ring-opening rate constant), U-4 (E/Z reversal not analyzed despite being the only stereochemical probe of the dmpe cycle), U-5 (NMR-based fluxional assignment + NMR-based Ni(I) exclusion are mutually circular at 298 K)] | note: Recurring U pattern across all three papers shows an analytical category gap in the A/B/C framework: each paper's own model generates testable predictions that the paper does not test, in spite of having the analytical tools to do so. This is neither "deferred" (A) nor "reporting omission" (B) nor "severed citation[REDACTED: substantial verbatim quotation; see Tier 9]self-contradictory absence between a paper's model and its data". Three independent papers confirm this U-pattern across 54 years and across three different journal genres (communication, full-paper scope survey, mechanistic full paper); the pattern is robust enough to warrant a dedicated classification axis. The recurrence also confirms that PRI-11 (Mechanism–kinetics decoupling: rate law not algebraically derived from the proposed cycle) is a special case of this broader self-contradictory-absence category — Mazet's U-1 (critical severity) is an exact PRI-11 instance; Kumada_1972's U-1 and Kumada_1976b's U-1 are pre-formal antecedents.
```

---

## group_unasked_question

[REDACTED: substantial verbatim quotation; see Tier 9]

```
evidence_chain: Kumada_1972 : B-6 (cross:homo ratio absent for any Table I entry), U-1 (R–R predicted by eq 3 not reported), C-1 (Tamura-Kochi comparison asserted not measured), A-2 (entire mechanistic verification deferred) ; Kumada_1976b : SRG-2 (B-1, B-2, B-10, B-5: GLPC integrity undermined by mass-balance violation 104%), CLA-2/U-3 (β-hydride olefins not searched), C-1/C-2/C-3 (Kharasch / Pd / cuprate baselines asserted not compared), A-1/SRG-1 (Scheme 1 rationalized not elucidated) ; Mazet_2021 : SRG-2 (B-6: ~75–85% mass balance unaccounted in Figure 9 bimetallic experiment), SRG-1 (B-5/U-1/U-2: VTNA under deactivation, kinetic model not integrated), CLA-2 (steric attribution from non-catalytic geometry), C-3 (RE barrier imported from different Ni system without isomorphism check)
```

TEMPERATURE_SUMMARY correspondence: The group-unasked-question ties together three high_convergence_low_gap items at the lineage frontier — Kumada_1972's B-1 (V1=V2=V3=high, convergence 3/3), Kumada_1976b's B-5 (V1=medium+V3=medium, 2/3) — and Mazet_2021's A-3 (V1=high, V2=high, V3=high, convergence 3/3) and B-5 (V1=high, V2=high, V3=high, convergence 3/3). All three papers are converged-on-the-same-question by adjacent fields, and the severity is consistently medium-to-high across 54 years, despite the quantitative-method change (glpc → GLPC → VTNA + DFT-importing). The temperature profile is the audit signal that identifies the group-unasked-question as field-wide rather than paper-specific.

recurring_root correspondence: This group-unasked-question is the integrated sum of three of the four recurring_roots — "cycle assembled by analogy / proxy" + "quantitative claims without analytical metadata" + "selectivity / mass-balance supported by absence". The 54-year persistence reflects the structural interdependence of these three roots: selectivity cannot be quantified without mass-balanced byproduct measurement; byproduct measurement cannot be interpreted without an internally validated mechanism; the mechanism cannot be validated internally if the analytical foundation is incomplete. The G1 Direct Lineage shows that this triple-bind has propagated unbroken from Kumada 1972 through Kumada 1976b to Mazet 2021, and that each paradigm transition has displaced the bind into a new substrate class without resolving it.

---

> **Tier 8 redaction notice**: This file is a redacted copy of the corresponding Tier 3 / Tier 9 output. Verbatim source-paper quotations have been replaced by `[REDACTED: see source paper §<loc>; full text retained in Tier 9 reviewer-only deposit]` markers, preserving location references and our own analytical content. Bibliographic fields (title, authors, journal, year, DOI), analytical labels (`evidence_chain:` with B-/U-/A-/C- internal IDs), short technical terms, and our own analytical text are not redacted. The redaction was applied by `scripts/redact_for_tier8.py` and, for this version, by `scripts/build_paperA_R1_public.py` with `scripts/redact_source_ngram_runs.py` (scripts of the project repository; they are not deposited).
