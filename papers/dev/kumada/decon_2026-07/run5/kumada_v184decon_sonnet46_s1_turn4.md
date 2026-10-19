```
prompt_version: stage1-v184-20260502
model_info: claude-sonnet-4-6

target_title:   Selective Carbon-Carbon Bond Formation by Cross-Coupling of Grignard Reagents with Organic Halides. Catalysis by Nickel-Phosphine Complexes
target_authors: Kohei Tamao, Koji Sumitani, Makoto Kumada
target_start:   page 1: [REDACTED: paper boundary quote; see Tier 9]
target_end:     page 3: [REDACTED: paper boundary quote; see Tier 9]

[Agent fields]
V1: Synthetic organometallic chemistry / homogeneous catalysis (cross-coupling) — identifies gaps in catalytic scope, yield quantification, mass balance, ligand selection rationale, and mechanistic evidence from a synthetic practitioner perspective.
V2: Mechanistic organometallic chemistry / physical organic chemistry — identifies gaps in rate-determining step, oxidation-state assignment, crossover experiments, kinetic vs. thermodynamic selectivity, and radical/ionic pathway discrimination.
V3: Analytical chemistry / chromatographic and spectroscopic characterization — identifies gaps in internal standard identification, characterization method specification, purity determination, replication data, and yield-basis consistency.

--- Step 0: Boundary recheck ---

All quotes in Turns 1–3 were reviewed against target_start and target_end. All passages are confirmed to originate from the Kumada 1972 communication (pages 4374–4376 of JACS 94:12) and fall between the target boundaries. No boundary violations detected.

--- Step 1: Cross-field temperature ---

V1-Q1 / V2-OV1: V1=high(3), V2=critical(4); convergence=2/3; distance=1 → temperature_gap=low
V1-Q9 / V2-OV2: V1=high(3), V2=critical(4); convergence=2/3; distance=1 → temperature_gap=low
V1-Q10 / V2-OV3: V1=high(3), V2=high(3); convergence=2/3; distance=0 → temperature_gap=none
V1-Q5 / V2-OV4: V1=high(3), V2=high(3); convergence=2/3; distance=0 → temperature_gap=none
V1-Q6 / V2-OV5: V1=medium(2), V2=high(3); convergence=2/3; distance=1 → temperature_gap=low
V1-Q8 / V3-OV1: V1=medium(2), V3=high(3); convergence=2/3; distance=1 → temperature_gap=low
V1-Q11 / V3-OV2: V1=medium(2), V3=medium(2); convergence=2/3; distance=0 → temperature_gap=none
V1-Q2 / V3-OV3: V1=medium(2), V3=medium(2); convergence=2/3; distance=0 → temperature_gap=none
V2-Q1 / V3-OV4: V2=high(3), V3=high(3); convergence=2/3; distance=0 → temperature_gap=none

--- Step 2: Same-root groups ---

SRG-1 (Mechanistic evidence for proposed catalytic cycle): V1-Q9, V2-Q2, V2-Q3, V2-Q4, V2-Q5, V2-Q8 — all derive from the same root: the catalytic cycle (eqs 1–4) is proposed without any direct experimental evidence (kinetic data, intermediate characterization, spectroscopic observation, radical probes) for any elementary step.

SRG-2 (Selectivity basis absent): V1-Q1, V2-Q1, V2-Q4 — all derive from the same root: the paper claims "selective cross-coupling" as its central result but neither quantifies the competing homo-coupling product nor establishes whether selectivity is kinetically or thermodynamically controlled.

SRG-3 (Ligand effect interpretation): V1-Q5, V1-Q15, V2-Q6, V2-Q11 — all derive from the same root: the ligand activity order and the cis-geometry interpretation rely on no structural or electronic data for any of the proposed diorganonickel intermediates.

SRG-4 (Stereochemical outcome): V1-Q6, V1-Q11, V2-Q7, V3-Q5 — all derive from the same root: the nonstereospecific stilbene product formation from cis- and trans-vinyl chlorides is acknowledged as anomalous but neither the analytical basis nor the mechanistic origin is addressed.

SRG-5 (Quantitative data quality): V1-Q2, V1-Q8, V3-Q1, V3-Q4, V3-Q7 — all derive from the same root: the paper provides no replication data, no mass balance, and the glpc-based yields lack calibration details, making the quantitative claims non-independently verifiable.

SRG-6 (β-hydride elimination contradiction): V1-Q10, V2-Q9 — both derive from the same root: the mechanism predicts a dialkyl-Ni(II) intermediate for β-H-bearing alkyl Grignard reagents, but footnote 17 in the paper itself cites evidence that such species are commonly unstable.

--- Step 3: Classification ---

[A] A-1 | P3:Lcol:L29-L34* | [REDACTED: verbatim source quotation; see the source paper via its DOI] | deferral_type: deferred | mixed_detail: n/a | reason_inferred: T1 | linked_to: B-1, B-4, U-1, U-3 | cross_field_temperature: V1-Q6 V2-OV5: V1=medium,V2=high; convergence=2/3; temperature_gap=low

[A] A-2 | P3:Lcol:L34-L36* | [REDACTED: verbatim source quotation; see the source paper via its DOI] | deferral_type: deferred | mixed_detail: scope and application explicitly deferred; "not necessarily optimum" conditions (Table I footnote a) indicate the reported substrate scope is not exhaustive | reason_inferred: T1 | linked_to: B-5, B-9 | cross_field_temperature: n/a

[B] B-1 | P2:Lcol:L20-L28*; P3:Lcol:L29-L32* | [REDACTED: verbatim source quotation; see the source paper via its DOI] / [REDACTED: verbatim source quotation; see the source paper via its DOI] | classification: methodological_limitation | rhetorical_function: Working hypothesis label qualifying the proposed catalytic cycle while acknowledging absence of experimental verification. | note: The paper explicitly acknowledges the cycle is a "working hypothesis"; no intermediate in the cycle (complexes 1, 2, or 3) has been isolated or spectroscopically observed under the reported conditions; precedents cited (eq 1, ref 11/12; halogen-Ni/Grignard, ref 13) are stoichiometric models under different conditions, not mechanistic probes under catalytic turnover. Prospective character: deferred to A-1. Related SRG-1. | cross_field_temperature: V1-Q9 V2-OV2: V1=high,V2=critical; convergence=2/3; temperature_gap=low

[B] B-2 | P1:Rcol:L5-L10*; P2:Lcol:L10-L13* (eqs 2–4) | [REDACTED: verbatim source quotation; see the source paper via its DOI] / [REDACTED: verbatim source quotation; see the source paper via its DOI] | classification: reporting_omission | rhetorical_function: Statement establishing the deficiency of prior methods (homo-coupling byproducts) that this work claims to overcome, paired with the proposed mechanistic step (eq 3) that inherently generates homo-coupling product R-R. | note: The paper's central claim is "selective cross-coupling" over homo-coupling, yet no quantitative data on homo-coupling byproduct (R–R) are reported for any entry in Table I. Critically, the proposed mechanism (eq 3) explicitly predicts formation of R–R in the catalyst activation step (L2NiR2 + R'X" → L2Ni(R')(X") + R-R); this prediction is not tested. → self-contradictory absence (see U-1). Flag: metric incompleteness. Related SRG-2. | cross_field_temperature: V1=high,V2-OV1=critical; convergence=2/3; temperature_gap=low

[B] B-3 | P2:Lcol:Table I footnote a* | [REDACTED: verbatim source quotation; see the source paper via its DOI] | classification: reporting_omission | rhetorical_function: Disclaimer qualifying the completeness of the optimization and the meaning of the reported yields. | note: No turnover number (TON) or turnover frequency (TOF) is reported; only a catalyst loading range is given without explicit mol% for individual entries. Isolated yield figures and glpc yields cannot be converted to TON without the exact catalyst moles used per reaction. | cross_field_temperature: V1-Q2 V3-OV3: V1=medium,V3=medium; convergence=2/3; temperature_gap=none

[B] B-4 | P3:Lcol:L9-L22*; footnote 21* | [REDACTED: verbatim source quotation; see the source paper via its DOI] / footnote 21: [REDACTED: verbatim source quotation; see the source paper via its DOI] | classification: reporting_omission | rhetorical_function: Summary of ligand screening results presented as support for the cis-geometry mechanistic interpretation. | note: (Consolidated from V1-Q5, V1-Q15, V2-Q6, V2-Q11, V2-OV4.) No yield, conversion rate, or reaction time data are reported for any individual ligand in the comparison; the ligand activity order is asserted without tabulated data. The interpretation (cis geometry = first requisite) is inferred from ligand structure without spectroscopic or crystallographic evidence for intermediate geometry under reaction conditions; electronic effects of the phosphine ligands (σ-donor/π-acceptor balance) are not distinguished from geometric effects. Related SRG-3. | cross_field_temperature: V1-Q5 V2-OV4: V1=high,V2=high; convergence=2/3; temperature_gap=none

[B] B-5 | P3:Lcol:L1-L5* | [REDACTED: verbatim source quotation; see the source paper via its DOI] | classification: mixed | rhetorical_function: Positive framing of a substrate limitation as a mechanistically significant and synthetically useful feature. | note: The sp2-halide restriction is stated as a fact without any supporting data from failed sp3-halide trials; no yield or qualitative result for any sp3-halide substrate is reported. The high chloride reactivity is asserted as "remarkable" compared to bromides/iodides (footnote 18) but no direct comparison data are given. Mixed: intentional_narrowing (sp2 scope is a deliberate choice) and reporting_omission (failed sp3 cases are not documented). | cross_field_temperature: V1-Q4,V1-Q12: both medium from V1; convergence from V1 only; temperature_gap: n/a

[B] B-6 | P3:Lcol:L24-L28* | [REDACTED: verbatim source quotation; see the source paper via its DOI] | classification: reporting_omission | rhetorical_function: Definitive comparative statement on solvent effects presented as a significant feature of the method. | note: No experimental data (yields, conversion rates, or reaction times for ether vs. THF) are presented for any substrate combination; the assertion is stated as a fact without supporting evidence. | cross_field_temperature: V1-Q7: high from V1 only; convergence=1/3

[B] B-7 | P2:Rcol:L14-L22* (Example 1) | [REDACTED: verbatim source quotation; see the source paper via its DOI] | classification: reporting_omission | rhetorical_function: Workup procedure supporting the reported isolated yield figure. | note: (Consolidated from V1-Q8, V3-OV1.) The fate of the remaining ~6% of material (and analogous fractions for all other entries) is not characterized; no statement on homo-coupling product, unreacted starting materials, or other identifiable byproducts. Mass balance closure is a standard requirement for yield data to be interpretable as selectivity evidence. Related SRG-5. | cross_field_temperature: V1-Q8 V3-OV1: V1=medium,V3=high; convergence=2/3; temperature_gap=low

[B] B-8 | P3:Lcol:L17-L22*; Table I (cis/trans-stilbene rows)* | [REDACTED: verbatim source quotation; see the source paper via its DOI] | classification: reporting_omission | rhetorical_function: Acknowledgment of an anomalous stereochemical outcome presented as a mechanistically interesting observation without further analysis. | note: (Consolidated from V1-Q11, V3-OV2, V3-Q5.) The analytical method for determining cis:trans ratios (glpc, NMR integration, or other) is not stated; no measurement uncertainty is given; the presence or absence of other byproducts (PhCH=CH2, PhPh, PhCH2CHPh) is not addressed. Related SRG-4. | cross_field_temperature: V1-Q11 V3-OV2: V1=medium,V3=medium; convergence=2/3; temperature_gap=none

[B] B-9 | P2:Rcol:L38-L42* (Example 2, yield basis) | [REDACTED: verbatim source quotation; see the source paper via its DOI] vs. Example 1: "9.63 g, 94%, based on m-dichlorobenzene" | classification: reporting_omission | rhetorical_function: not stated in paper | note: The paper uses different yield calculation bases for the two representative procedures (Example 1: yield based on organic halide; Example 2: yield based on Grignard reagent) without explanation. Per the B-item consolidation exception for yield basis mixing, this is retained as an independent item. This precludes direct efficiency comparison between the two procedures. Source: V1-Q14.

[B] B-10 | P2:Lcol:Table I, footnotes c, d, e* | [REDACTED: verbatim source quotation; see the source paper via its DOI] | classification: reporting_omission | rhetorical_function: Footnotes specifying characterization scope and yield determination method for Table I entries. | note: (Consolidated from V3-Q1, V3-Q2, V3-Q3.) (a) The internal standard used for glpc-based yield determination (footnote e) is not identified; its detector response factor relative to each analyte is not stated. (b) The "and/or" formulation in footnote c does not specify which characterization technique was applied to which product. (c) For entries reported as isolated yields, no purity percentage (glpc % or elemental analysis) is given; the descriptor "pure" (Example 1) is not quantified. These gaps collectively make the yield data non-independently verifiable. Related SRG-5. | cross_field_temperature: V3-Q1,V3-Q2,V3-Q3: high from V3; convergence=1/3 (V3 only)

[B] B-11 | P2:Lcol:Table I footnote a*; P3:Lcol:L1-L3* | "The experimental conditions are not necessarily optimum" / [REDACTED: verbatim source quotation; see the source paper via its DOI] | classification: reporting_omission | rhetorical_function: Disclaimer and scope statement presented as features 1 and 2 of the method. | note: No replication data are presented for any entry in Table I; all yields are single-run values. Given that the conditions are acknowledged as "not necessarily optimum," the reproducibility and representative nature of the reported yields are unestablished. Related SRG-5. Source: V3-Q4, V3-Q7. | cross_field_temperature: V3-Q4: medium from V3 only; convergence=1/3

[C] C-1 | P1:Rcol:L12-L18* | [REDACTED: verbatim source quotation; see the source paper via its DOI] | textual_function: Positioned as the immediately preceding best available method to contextualize the new Ni-phosphine approach. | reason_severed: Dropped Quantitative Benchmark — cited as "extremely effective" with qualitative scope limitations noted, but no yields, rates, or selectivity values from Tamura/Kochi for the same substrate combinations are presented; the results/discussion section does not make a direct numerical comparison on the same metric. | affects_claims: yes — the paper's claim of superiority in "selective cross-coupling" requires a comparative standard; the absence of a direct numerical comparison leaves the advantage over Tamura/Kochi's iron catalyst (for alkenyl halides) unquantified for any overlapping substrate. | symmetric_pattern: no

[C] C-2 | P1:Rcol:footnote 1* | [REDACTED: verbatim source quotation; see the source paper via its DOI] (refs 2, 3, 3a) | textual_function: Background citation acknowledging prior Ni-catalyzed coupling precedent as the inspiration for using nickel complexes. | reason_severed: Corriu and Masse (ref 3, 1970 and ref 3a, 1972) and Chuit et al. (ref 2) are acknowledged as precedents for Ni-catalyzed coupling but not compared on yield, selectivity, or substrate scope; the Note Added in Proof (ref 3a) acknowledges concurrent discovery of similar cross-coupling chemistry but contains no evaluation of differences or similarities. | affects_claims: medium — the concurrent Corriu/Masse work (ref 3a) directly overlaps the central claim; acknowledging it without evaluation leaves the novelty boundary of the present paper unspecified. | symmetric_pattern: partial — refs 2 and 3 are grouped under the same footnote but represent different chemistry (hydrosilylation vs. allylic alcohol coupling); ref 3a is the most relevant (direct overlap) but appears only as a Note Added in Proof.

[C] C-3 | P1:Rcol:footnote 7* | [REDACTED: verbatim source quotation; see the source paper via its DOI] (refs 8, 9, 10) | textual_function: Explicit exclusion of closely related stoichiometric selective C–C bond-forming reagents from the scope of comparison. | reason_severed: Corey/Posner cuprate chemistry and π-allylnickel chemistry are described as "excellent reagents" for selective cross-coupling but explicitly excluded from numerical comparison with the present method; no yield or selectivity data from refs 8–10 are cited for parallel substrates. | affects_claims: medium — the paper's claim of selective cross-coupling could in principle be benchmarked against these stoichiometric reagents for the same substrates in Table I; the exclusion is stated as deliberate (catalytic focus) but no evidence is presented that the Ni-phosphine catalyst is superior in selectivity or yield to these reagents for any shared substrate. | symmetric_pattern: partial — refs 8/9 (Corey/Posner copper) and ref 10 (Whitesides cuprate) are grouped but represent related chemistry at different metal centers.

[U] U-1 | P2:Lcol:eqs 2–4*; P1:Rcol:L5-L10* | [REDACTED: verbatim source quotation; see the source paper via its DOI] (eq 3: L2NiR2 + R'X" → L2Ni(R')(X") + R-R) / [REDACTED: verbatim source quotation; see the source paper via its DOI] | question: Why does homo-coupling of the Grignard-derived R group not occur to a significant extent under the reported catalytic conditions, given that the paper's own proposed mechanism (eq 3) explicitly predicts production of R-R homo-coupling product in the catalyst activation step? | originating_agent: V1 (V1-Q1), V2 (V2-Q4, V2-OV1) | severity: critical | note: self-contradictory absence — the paper's proposed catalytic cycle (eq 3) predicts that R-R homo-coupling is produced when intermediate 1 (L2NiR2) reacts with R'X" to form intermediate 2; yet the paper's central claim is "selective cross-coupling" with R-R suppressed. No data on R-R amounts, no mechanistic explanation for suppression, and no crossover experiment are provided. This is neither merely a reporting omission (B) nor a prospective deferral (A): it is a case where the paper's own mechanistic model makes a falsifiable prediction that is never tested. Multi-critical rule: recorded independently of U-2 and U-3.

[U] U-2 | P2:Lcol:L14-L28* (eqs 1–4) | [REDACTED: verbatim source quotation; see the source paper via its DOI] | question: What is the oxidation state of nickel at each stage of the proposed catalytic cycle, and specifically what experimental evidence establishes that the cycle operates exclusively through Ni(0)/Ni(II) rather than Ni(I)/Ni(III) radical pathways? | originating_agent: V2 (V2-Q2, V2-Q8) | severity: critical | note: self-contradictory absence — the paper proposes a concerted reductive elimination (2e) mechanism but never specifies the oxidation states of intermediates 1, 2, and 3 (all are written as Ni species but without oxidation-state labels); no spectroscopic evidence (EPR, UV-Vis, electrochemistry) is presented; the "black mixture" observed in Example 1 is consistent with Ni(0) or Ni(I) formation but is not characterized. The absence of oxidation-state specification makes the proposed cycle internally underdetermined. Multi-critical rule: recorded independently of U-1 and U-3.

[U] U-3 | P2:Lcol:footnote 17*; P1:Rcol:L22-L24* (feature 1) | [REDACTED: verbatim source quotation; see the source paper via its DOI] (footnote 17) / [REDACTED: verbatim source quotation; see the source paper via its DOI] | question: How does the proposed dialkylnickel intermediate 1 (L2NiR2, where R = n-butyl or n-hexyl bearing β-H atoms) avoid β-hydride elimination, given that the paper itself cites evidence in footnote 17 that such transition metal alkyls are commonly unstable? | originating_agent: V1 (V1-Q10), V2 (V2-Q9, V2-OV3) | severity: high | note: self-contradictory absence — the paper presents tolerance of β-H-bearing alkyl Grignard reagents as a key synthetic advantage, while simultaneously acknowledging in footnote 17 that β-H-bearing transition metal alkyls are "commonly unstable." The paper's mechanism requires complex 1 (L2NiR2 with R = n-alkyl) to be kinetically competent, but no data distinguish whether the mechanism avoids accumulation of complex 1 (e.g., fast transmetalation makes 1 a non-accumulating species) or whether the Ni-P ligand stabilizes the β-H-bearing alkyl intermediate. Multi-critical rule: recorded independently of U-1 and U-2. Related SRG-6.

[U] U-4 | P1:Rcol:L5-L10*; P2:Lcol:L20-L28* (eqs 2–4) | [REDACTED: verbatim source quotation; see the source paper via its DOI] / [proposed cycle as presented] | question: Is the observed cross-coupling selectivity under kinetic or thermodynamic control, and does the selectivity pattern change with reaction time, temperature, or reagent addition order? | originating_agent: V2 (V2-Q1), V3 (V3-OV4) | severity: high | note: prerequisite-absence for interpreting the "selective" claim — without time-course data or temperature-variation data, the observed product ratio cannot be attributed to either kinetic or thermodynamic selectivity; the paper presents only endpoint yields from a single set of conditions (not necessarily optimum), making mechanistic attribution of selectivity origin impossible from the reported data. This is distinct from U-1 (which concerns why homo-coupling is suppressed by the mechanism) and U-3 (which concerns β-H stability). Multi-critical rule (high severity): recorded independently.

[META]
  linked_items:
    A-1 ↔ B-1 (deferred mechanistic details correspond to the acknowledged working hypothesis)
    A-1 ↔ U-1 (the stereo/mechanistic deferral includes but does not address the self-contradictory selectivity absence)
    A-1 ↔ U-3 (β-H compatibility is part of the mechanistic details deferred)
    A-2 ↔ B-5 (scope extension explicitly deferred; sp2-only limitation is its current boundary)
    B-2 ↔ U-1 (homo-coupling reporting omission and self-contradictory absence are complementary)
    B-1 ↔ U-2 (working hypothesis limitation and Ni oxidation-state absence are complementary)
    B-1 ↔ B-4 (ligand effect and mechanistic cycle are linked: the cis-geometry interpretation is part of the working hypothesis)
    B-7 ↔ U-1 (mass balance absence and homo-coupling absence share the root: uncharacterized byproduct fractions)

  same_root_groups:
    SRG-1 (Mechanistic evidence for proposed catalytic cycle): B-1, U-2 — root: proposed eqs 1–4 cycle lacks experimental support for any elementary step
    SRG-2 (Selectivity basis absent): B-2, U-1, U-4 — root: "selective cross-coupling" claim lacks quantification of competing products and mechanistic selectivity origin
    SRG-3 (Ligand effect interpretation): B-4 — root: ligand activity order inferred without structural/electronic data for intermediates
    SRG-4 (Stereochemical outcome): B-8, A-1 — root: anomalous cis-stilbene enrichment is acknowledged but uncharacterized
    SRG-5 (Quantitative data quality): B-3, B-7, B-10, B-11 — root: yield figures lack calibration details, mass balance, and replication data
    SRG-6 (β-hydride elimination contradiction): U-3 — root: mechanism predicts stable dialkyl-Ni with β-H atoms, contradicted by footnote 17

  symmetric_citations: C-2 (Corriu/Masse 1970 and 1972, cited together in footnote 1 / Note Added in Proof)

  unreported_data:
    - Homo-coupling product (R–R) amounts for all entries in Table I (predicted by eq 3, never quantified)
    - Yield data for sp3 halide substrates (stated as failing, no data shown)
    - Yield/rate data for each individual ligand in the activity series (only ordinal ranking given)
    - cis:trans ratio determination method and uncertainty for stilbene entries
    - Comparison yield data for ether vs. THF as solvent

  series_signal: yes — T1 (paper-stated) — [REDACTED: verbatim source quotation; see the source paper via its DOI] Relates to A-2.

[TEMPERATURE_SUMMARY]
  high_convergence_high_gap: [] (empty — no item with convergence ≥ 2/3 and distance > 1)
  high_convergence_low_gap: [B-1(V1-Q9/V2-OV2), B-2(V1-Q1/V2-OV1), A-1(V1-Q6/V2-OV5), B-7(V1-Q8/V3-OV1)]
  low_convergence_high_gap: [U-1 (V2-Q4: critical, 1/3 as new question from V2), U-2 (V2-Q2: critical, 1/3), V2-Q3 (critical, 1/3)]

[GAP] GAP-1 | type: 1 | priority: high | description: Retrieve Tamura and Kochi (Synthesis, 303, 1971) to obtain specific yield and selectivity data for iron-catalyzed Grignard/alkenyl halide cross-coupling, enabling a quantitative comparison of the selective cross-coupling performance against the present Ni-phosphine system. | candidate_paper: M. Tamura and J. Kochi, Synthesis, 303 (1971) | inference_label: T1 | status: pending

[GAP] GAP-2 | type: 3 | priority: high | description: Papers reporting direct mechanistic evidence (kinetics, EPR, crossover experiments, intermediate isolation) for the Ni(0)/Ni(II) vs. Ni(I)/Ni(III) oxidation-state assignment in Ni-phosphine-catalyzed cross-coupling reactions would directly answer U-2 and partially U-1. | candidate_paper: Subsequent Kumada group papers on mechanistic studies of the Ni-catalyzed cross-coupling (e.g., Tamao, Yamamoto, Kumada, J. Organomet. Chem., 1977) | inference_label: T3 | status: pending

[GAP] GAP-3 | type: 2 | priority: medium | description: Corriu and Masse (Chem. Commun., 144, 1972 — Note Added in Proof, ref 3a) reported "similar cross-coupling reactions" using nickel catalysts; retrieval would enable comparison of substrate scope, selectivity, and proposed mechanism to establish the boundaries of independent discovery and novelty. | candidate_paper: R. J. P. Corriu and J. P. Masse, Chem. Commun., 144 (1972) | inference_label: T1 | status: pending

inference_time_sec: not available — inject externally
```

---

> **Public-cut redaction notice**: verbatim quotations from the analysed papers in this file have been replaced by `[REDACTED: …]` markers (rules in the repository README). The unredacted file is in the reviewer version of the deposit.
