```
prompt_version: stage1-v17-20260415
model_info: claude-sonnet-4-6

target_title:   Selective Carbon–Carbon Bond Formation by Cross-Coupling of Grignard Reagents with Organic Halides. Catalysis by Nickel–Phosphine Complexes
target_authors: Kohei Tamao, Koji Sumitani, Makoto Kumada
target_start:   page 1 (PDF): [REDACTED: paper boundary quote; see Tier 9]
target_end:     page 3 (PDF): [REDACTED: paper boundary quote; see Tier 9]

[Agent fields]
V1: Synthetic organometallic chemistry / transition metal-catalyzed cross-coupling — subfield matches JACS, Ni-phosphine catalysis, and substrate scope methodology (S0-3, S0-4).
V2: Mechanistic / physical organic chemistry — paper proposes a Ni(0)/Ni(II) catalytic cycle with no kinetic data, no intermediate characterization, and no mechanistic probes; V1 covered synthetic completeness gaps but not rate-determining step, radical vs. ionic pathway, or kinetic/thermodynamic selectivity control.
V3: Analytical chemistry / product characterization — primary evidence is yield table (glpc- and isolated-yield data) and "glpc, nmr, ir, and/or mass spectra" characterization; neither V1 nor V2 interrogated analytical validity of yield measurement, completeness of characterization, or statistical basis for comparisons.

---

Step 0: Boundary recheck — all quotes in Turns 1–3 verified as originating from between target_start and target_end. Footnote-referenced prior work (refs 11–13) cited within the target paper. No boundary violations detected.

---

[A] A-1 | P3:Lcol:L17* | [REDACTED: substantial verbatim quotation; see Tier 9] | deferral_type: deferred | mixed_detail: n/a | reason_inferred: T1 | linked_to: B-9, U-3 | cross_field_temperature: V1=medium, V2=high; convergence=2/3; temperature_gap=low
note: Paper raises the cis-enrichment observation, notes "some interesting mechanistic implications," and explicitly defers explanation to [REDACTED: substantial verbatim quotation; see Tier 9] This is a pure-A item — the paper makes no claim to explain the phenomenon; it documents and defers it. The A classification stands because the incompleteness is explicitly prospective, with no current-paper claim of explanation to falsify. Originating agents: V1-Q7, V2-Q4.

[A] A-2 | P3:Lcol:last sentence | [REDACTED: substantial verbatim quotation; see Tier 9] | deferral_type: deferred | mixed_detail: n/a | reason_inferred: T1 | linked_to: B-5, B-9 | cross_field_temperature: V1=medium (V1-Q1, V1-Q3); convergence=1/3; temperature_gap: n/a
note: The paper explicitly sends scope extension (additional substrate classes, condition refinement) to future work. Substrates not represented in Table I (e.g., secondary/tertiary alkyl Grignard reagents, heterocyclic halides) are genuinely prospective — no current-paper claim about them exists, so no B-component applies. Originating agents: V1-Q1 (refinement aspect), V1-Q3 (extension aspect).

---

[B] B-1 | P1:Rcol:L1* | [REDACTED: substantial verbatim quotation; see Tier 9] | classification: reporting_omission | rhetorical_function: Opening claim asserting selectivity as the defining feature of the method. | note: No quantitative data on homo-coupling (R–R), proto-demetalation, or β-hydride elimination byproducts are reported for any Table I entry. "Selective" is used as a descriptor in the title and opening sentence, yet selectivity is never measured or defined numerically. Metric incompleteness flag: isolated yield ≠ cross-coupling selectivity without byproduct data. Self-contradictory absence: equation 3 of the proposed mechanism explicitly generates R–R as the homo-coupling byproduct; this prediction of the paper's own proposed cycle is nowhere reported or tested. Triggers U-1 (see below). | cross_field_temperature: V1=high, V2=high, V3=high; convergence=3/3; temperature_gap=none

[B] B-2 | P2:Lcol:L1* | [REDACTED: substantial verbatim quotation; see Tier 9] | classification: methodological_limitation | rhetorical_function: Presentation of a proposed catalytic cycle as the operative mechanism, explicitly labeled [REDACTED: verbatim source quotation; see the source paper via its DOI] Classification is B (not A) because the paper actively presents the mechanism in declarative language throughout eqs 2–4, constituting a current-paper claim. | cross_field_temperature: V1=high, V2=critical (V2-OV1); convergence=2/3; temperature_gap=low

[B] B-3 | P3:Lcol:L5* | [REDACTED: substantial verbatim quotation; see Tier 9] + [REDACTED: substantial verbatim quotation; see Tier 9] | classification: mixed | rhetorical_function: Catalyst structure–activity ordering presented as evidence for a specific geometric mechanistic hypothesis. | note: (i) reporting_omission component — no yields or other quantitative data for catalysts other than [NiCl₂(dpe)] are provided; the ordering is stated without data (V1-Q5). (ii) methodological_limitation component — the mechanistic conclusion (cis geometry required for reductive elimination) is attributed to the activity order, but the order could equally reflect differences in Ni redox potential, transmetalation rate, or steric access; no independent evidence distinguishes the geometric hypothesis from alternatives. The order was established for only one substrate combination (n-BuMgBr + PhCl; footnote 21) and its generality is unstated (V1-Q4, V2-Q8). | cross_field_temperature: V1=medium (V1-Q5), V2=medium (V2-OV4)/high (V2-Q8); convergence=2/3; temperature_gap=low

[B] B-4 | P2:Rcol:L1* (Table I footnotes a and e) | "Yields based on glpc analysis using an internal standard." | classification: reporting_omission | rhetorical_function: Footnote distinguishing glpc-based from isolated yields. | note: No glpc conditions are stated (column type, stationary phase, detector, temperature program, internal standard identity/concentration). Four entries in Table I report glpc yields (98%, 95%, 89%, 80%) that cannot be verified or reproduced without this information. Mixed yield reporting within the same table — glpc-based yields (footnote e) and isolated yields coexist — without per-entry specification of which method was applied to which product; this makes cross-entry yield comparisons unreliable (V1-Q2, V3-Q1, V3-OV1). | cross_field_temperature: V1=medium (V1-Q2), V3=medium (V3-Q1, V3-OV1); convergence=2/3; temperature_gap=none

[B] B-5 | P3:Lcol:L3* | [REDACTED: substantial verbatim quotation; see Tier 9] | classification: mixed | rhetorical_function: Scope restriction of the method to sp² halides framed as a positive distinguishing feature. | note: (i) intentional_narrowing component — the sp² restriction is actively presented as a positive characteristic, not acknowledged as a limitation. (ii) methodological_limitation component — it is not stated whether sp³ halides were tested and found unreactive, or simply not investigated. No mechanistic attribution is given for the sp² requirement (whether oxidative addition, transmetalation, or reductive elimination is the discriminating step; V2-Q11). Substrate selection bias flag: all halide coupling partners in Table I are aryl or vinyl — no failed sp³ case is included, making the restriction's basis unavailable for evaluation. Note: scope extension beyond sp² halides is explicitly deferred (A-2). V1-Q3; V2-Q11.

[B] B-6 | P3:Lcol:L3* + footnote 18 | [REDACTED: substantial verbatim quotation; see Tier 9] | classification: reporting_omission | rhetorical_function: Claim that chloride reactivity is a distinctive advantage over prior work citing bromide/iodide predominance. | note: No entry in Table I compares chloride directly against bromide or iodide for the same substrate under identical conditions. The claim of "high reactivity" is comparative but unsupported by within-paper data; footnote 19 supports sp² C–Cl reactivity in principle (via oxidative addition precedent) but provides no quantitative rate or yield comparison. V1-Q14.

[B] B-7 | P3:Lcol:L22* | [REDACTED: substantial verbatim quotation; see Tier 9] | classification: reporting_omission | rhetorical_function: Comparative solvent claim stated with certainty ("definitely superior"). | note: No yields in THF are reported for any Table I entry. The mechanistic basis for the solvent effect is not stated; in a Ni(0)/Ni(II) cycle, coordinating THF could inhibit transmetalation or oxidative addition (V2-Q5), but this is not tested. The comparison is asserted without data. V1-Q8, V2-Q5.

[B] B-8 | P2:Rcol:L10* | [REDACTED: substantial verbatim quotation; see Tier 9] [Example 1 only] | classification: reporting_omission | rhetorical_function: Experimental procedure for Example 1, providing reaction time for that entry only. | note: Reaction time is given only for Examples 1 and 2 (20 hr each); no reaction times are reported for any of the 9 other Table I entries. Conversion completeness of the reported yields cannot be assessed. V1-Q10, V3-OV2. | cross_field_temperature: V1=medium, V3=medium; convergence=2/3; temperature_gap=none

[B] B-9 | P2:Rcol:L1* (Table I footnote a) | "The experimental conditions are not necessarily optimum." | classification: mixed | rhetorical_function: Disclaimer qualifying all yield data in Table I. | note: (i) reporting_omission component — the disclaimer covers all 11 entries without specifying which substrates are most sensitive to condition variation or which parameters were examined. (ii) prospective character (linked to A-2): "Investigations are continuing on the refinement." Cross-entry yield comparisons (e.g., 89% for ortho vs 95% for para di-n-butylbenzene) cannot be attributed to intrinsic reactivity differences vs. non-optimized conditions. V1-Q1.

[B] B-10 | P2:Rcol:L10* | [REDACTED: substantial verbatim quotation; see Tier 9] | classification: reporting_omission | rhetorical_function: Observation of reaction mixture color and salt formation during Example 1. | note: A black reaction mixture is consistent with Ni(0) particle formation (catalyst decomposition or colloidal Ni), yet this observation is not characterized or analyzed. No homogeneity test, filtration experiment, or catalyst poisoning study (e.g., Hg drop test) is reported to establish whether catalysis is homogeneous or heterogeneous. Self-contradictory absence: the paper proposes a homogeneous Ni(0)/Ni(II) molecular catalytic cycle; the black precipitate is consistent with heterogeneous catalysis or catalyst decomposition, either of which would undermine this mechanism — but neither is acknowledged. Triggers U-2. V2-Q6, V3-OV3. | cross_field_temperature: V2=medium, V3=medium; convergence=2/3; temperature_gap=none

[B] B-11 | P3:Lcol:L17* | "cis: trans = 80:20 ... cis: trans = 43:57" | classification: reporting_omission | rhetorical_function: Reporting of product isomer ratios from stilbene synthesis entries. | note: Analytical method for ratio determination (glpc area ratio, NMR integration, or separate isolation) is not stated. No uncertainty or replication data are given. The precision implied by "43:57" is unsubstantiated. V3-Q4.

[B] B-12 | P2:Rcol:L15* vs P2:Rcol:L28* | "9.63 g, 94%, based on m-dichlorobenzene" [Example 1] vs "6.8 g (80% based on the Grignard reagent)" [Example 2] | classification: reporting_omission | rhetorical_function: Yield report for the two detailed preparative examples. | note: B-item consolidation exception (yield basis mixing): Example 1 yield is based on the organic halide; Example 2 yield is based on the Grignard reagent. This inconsistency is not disclosed, and it is unclear which basis applies to Table I entries, making the three reporting contexts internally inconsistent. V3-Q8.

[B] B-13 | P2:Rcol:L1* (Table I footnote c) | "Characterized by glpc, nmr, ir, and/or mass spectra." | classification: reporting_omission | rhetorical_function: Generic characterization disclaimer covering all Table I products. | note: The "and/or" construction means product identity for some entries may rest on glpc retention time alone, with no spectroscopic verification. No spectroscopic data (NMR, IR, MS) are tabulated or listed by entry. For 1972 JACS, elemental analysis was standard for new compound characterization; none appears. V3-Q2, V3-Q3.

[B] B-14 | P2:Lcol:L20* | [REDACTED: substantial verbatim quotation; see Tier 9] | classification: methodological_limitation | rhetorical_function: Logical transition from two literature precedents to the proposed catalytic capability of NiCl₂(dpe). | note: The "two independent facts" (eq 1 from dipy-Ni, refs 11–12; transmetalation, ref 13) are drawn from complexes with fundamentally different ancillary ligands (dipy vs. dpe; monodentate vs. bidentate phosphine). No stoichiometric step in the proposed cycle (eqs 2–4) is demonstrated with the actual NiCl₂(dpe) catalyst used in Table I. The mechanistic analogy is by structural extrapolation without experimental validation on the target system. V1-Q15, V2-OV5. | cross_field_temperature: V1=medium, V2=high; convergence=2/3; temperature_gap=low

---

[C] C-1 | P1:Rcol:L8* | refs 5–6 (Tamura and Kochi, J. Amer. Chem. Soc. 1971; Synthesis 1971) | textual_function: Cited to establish that prior cross-coupling methods are "seldom employed in synthetic practice" due to homo-coupling and disproportionation; iron catalyst cited as the best prior system for alkenyl halide coupling. | reason_severed: Dropped Quantitative Benchmark — the iron catalyst (ref 6) is the closest prior precedent for the alkenyl–aryl coupling entries in Table I, but no direct yield or selectivity comparison is made using the same substrate pair. The improvement claimed is qualitative only. | affects_claims: yes — the central advantage of the new method cannot be evaluated quantitatively without this comparison. | symmetric_pattern: partial — ref 5 is dismissed as "homo coupling only," while ref 6 is dismissed as "only for alkenyl halides"; these represent qualitatively different limitations.

[C] C-2 | P1:Rcol:L20* (footnote 7) | refs 7–10 (Corey/Semmelhack allylnickel; Corey/Posner; Whitesides organocuprate) | textual_function: Cited as "excellent reagents" for selective cross-coupling but set aside: [REDACTED: verbatim source quotation; see the source paper via its DOI]

[C] C-3 | P1:Rcol:L1* (footnote 3a) | Corriu and Masse, Chem. Commun. 144 (1972) [Note Added in Proof] | textual_function: Acknowledged concurrent communication describing "similar cross-coupling reactions" with Ni(acac)₂ catalyst. | reason_severed: Acknowledged after submission; no comparison of scope, selectivity, or yield for any common substrate pair. | affects_claims: yes — if Ni(acac)₂ (without chelating diphosphine) achieves similar selectivity, the attributed role of the bidentate ligand and the cis-geometry mechanistic hypothesis (B-3) would require reassessment. | symmetric_pattern: no — single reference.

[C] C-4 | P1:Rcol:L1* (footnote 1) | refs 1–3 (prior NiCl₂(PPh₃)₂-catalyzed coupling with allylic alcohols and hydrosilanes; Corriu/Masse Chem. Commun. 213, 1970) | textual_function: Background footnote establishing NiCl₂(PPh₃)₂ prior art, used to justify novelty of bidentate ligand approach. | reason_severed: Cited as historical context only; no yield or selectivity comparison with current [NiCl₂(dpe)] system for any overlapping substrate. | affects_claims: medium — novelty of bidentate vs. monodentate phosphine ligand is part of finding 3 (ligand order, B-3), but no direct [NiCl₂(PPh₃)₂] vs. [NiCl₂(dpe)] comparison on a common substrate is made in the results. | symmetric_pattern: partial — refs 1–3 share the background function but represent different substrate classes.

---

[U] U-1 | P2:Lcol:L1* | "L₂NiR₂ + R'X'' → L₂Ni(R')(X'') + R–R (3)" | question: The proposed mechanism explicitly predicts formation of R–R (homo-coupling product) in eq 3, yet no homo-coupling product is reported, quantified, or discussed for any Table I entry. Is the claimed selectivity for cross-coupling over homo-coupling genuine, or are small amounts of R–R formed but below the glpc detection threshold? | originating_agent: V1 (V1-Q6), V2 (V2-OV3), V3 (V3-OV4) | severity: high | note: self-contradictory absence — the paper's proposed catalytic cycle (eq 3) predicts R–R formation as a byproduct of each catalytic turnover, but this predicted product is neither reported nor acknowledged as untested. B-1 captures the reporting omission; U-1 captures the self-contradictory absence between the proposed mechanism and the absent byproduct data.

[U] U-2 | P2:Rcol:L10* | [REDACTED: substantial verbatim quotation; see Tier 9] | question: The black color is consistent with Ni(0) nanoparticle formation or catalyst decomposition, yet the paper proposes a homogeneous Ni(0)/Ni(II) molecular cycle. Is the active catalyst species homogeneous or heterogeneous? | originating_agent: V2 (V2-Q6), V3 (V3-OV3) | severity: medium | note: self-contradictory absence — an observation noted in the paper (black mixture) is consistent with a scenario (heterogeneous catalysis or catalyst decomposition) that would undermine the paper's proposed homogeneous mechanism, but is recorded without characterization or analysis. B-10 captures the reporting omission; U-2 captures the self-contradictory absence.

[U] U-3 | P3:Lcol:L17* | [REDACTED: substantial verbatim quotation; see Tier 9] | question: Is the cis/trans product ratio a kinetically frozen outcome (which would change with extended reaction time or elevated temperature) or a thermodynamic equilibrium distribution? Without a time or temperature series, the nature of the selectivity cannot be determined. | originating_agent: V2 (V2-Q4) | severity: medium | note: Not A (paper raises no hypothetical mechanism for this observation), not B (no current-paper claim about kinetic vs. thermodynamic control), not C (no severed citation specific to this question). Arises at the intersection of A-1 (deferred mechanism) and B-11 (absent ratio measurement details) but is independent of both: the kinetic/thermodynamic ambiguity would persist even if the mechanism and analytical method were known.

[U] U-4 | P3:Lcol:L5*–L14* | [REDACTED: substantial verbatim quotation; see Tier 9] | question: The paper infers that cis geometry of the diorganonickel intermediate is the rate-controlling factor from a ligand activity order established in one reaction. Multiple structural parameters covary with activity (chelate ring size, bite angle, phosphine electronics, steric bulk). The attribution of the order to one specific geometric feature is not independently established by any experiment. What evidence distinguishes the geometric hypothesis from electronic or steric alternatives? | originating_agent: V1 (V1-Q4), V2 (V2-Q8) | severity: medium | note: B-3 records the absence of quantitative data for the ligand order. U-4 records the separate logical gap between the evidence (activity order) and the conclusion (cis geometry requirement): even with complete quantitative ligand data, the causal attribution would remain ambiguous without mechanistic probes (e.g., a known cis-diorganonickel complex tested independently).

---

[META]
  linked_items:
    - B-1 ↔ U-1 (self-contradictory absence from B-1's selectivity claim)
    - B-10 ↔ U-2 (self-contradictory absence from B-10's black mixture observation)
    - A-1 ↔ B-11 (both involve the cis/trans stilbene ratios; A-1 defers mechanism, B-11 records absent analytical detail)
    - A-1 ↔ U-3 (A-1 defers mechanism; U-3 identifies an additional kinetic/thermodynamic indeterminacy)
    - A-2 ↔ B-5 (A-2 defers scope extension; B-5 records current-paper intentional_narrowing)
    - B-2 ↔ B-14 (B-2 = catalytic cycle without evidence; B-14 = analogy basis)
    - B-2 ↔ U-1 (mechanism predicts R–R; U-1 notes it was not reported)
    - B-3 ↔ U-4 (B-3 = absent quantitative ligand data; U-4 = equivocal causal attribution)
    - C-1 ↔ B-1 (Dropped Quantitative Benchmark: selectivity advantage over Tamura-Kochi iron is unquantified)
    - C-3 ↔ B-3 (Ni(acac)₂ without chelating diphosphine: if similar selectivity achieved, B-3's cis-geometry hypothesis is challenged)

  same_root_groups:
    SRG-1: Mechanistic cycle without experimental evidence in the dpe-Ni system
      members: B-2, B-14, U-1, U-2, U-4
      shared root: No stoichiometric step validation, no intermediate detection, and no mechanistic probe experiments within the NiCl₂(dpe) system used in Table I.

    SRG-2: Selectivity claim without byproduct data
      members: B-1, U-1, C-1
      shared root: The paper's central claim of "selective" cross-coupling is never quantified against homo-coupling products; all three items derive from the same absent byproduct and mass balance data.

    SRG-3: Analytical quality of Table I yield data
      members: B-4, B-8, B-9, B-12, B-13
      shared root: All derive from incomplete analytical reporting for yield data in Table I — absent glpc conditions, absent reaction times, inconsistent yield basis, absent per-entry characterization, and unqualified condition disclaimer.

    SRG-4: Scope restriction basis
      members: B-5, B-6, A-2
      shared root: Claims about what the method does and does not accommodate (sp² only, chlorides reactive) without within-paper comparative evidence for the restrictions.

    SRG-5: Solvent and condition effects without quantitative or mechanistic basis
      members: B-7, B-9
      shared root: Both derive from qualitative claims about optimal conditions stated without quantitative data or mechanistic attribution.

    SRG-6: Cis/trans selectivity observation
      members: A-1, B-11, U-3
      shared root: All derive from the reported cis/trans stilbene ratios — A-1 for the deferred mechanistic explanation, B-11 for the absent analytical specification, U-3 for the kinetic/thermodynamic ambiguity.

  symmetric_citations:
    - C-1 and C-2 share a symmetric "cite-and-dismiss without yield comparison" function for prior cross-coupling methods (C-1 for catalytic Fe/Cu; C-2 for stoichiometric Ni/Cu reagents).

  unreported_data:
    - Homo-coupling (R–R) product yields and identities (B-1, U-1)
    - glpc calibration conditions and internal standard identity (B-4)
    - Reaction times for Table I entries other than the two detailed examples (B-8)
    - Catalyst activity data (yields per catalyst) for the five Ni complexes in the activity order (B-3)
    - THF-solvent yields for any Table I entry (B-7)
    - Analytical method and replication data for cis/trans stilbene ratios (B-11)

  series_signal: yes — T1 (explicitly stated: [REDACTED: substantial verbatim quotation; see Tier 9]) — linked_to: A-2.

---

[TEMPERATURE_SUMMARY]
  high_convergence_high_gap: none
  note: All inter-agent severity disagreements were ≤1 step (distance=1 = temperature_gap "low"). Normal outcome for adjacent-field agents in a 2–4 page communication.

  high_convergence_low_gap:
    B-1 (V1=high, V2=high, V3=high; convergence=3/3; gap=none)
    B-2 (V1=high, V2=critical; convergence=2/3; gap=low)
    B-4 (V1=medium, V3=medium; convergence=2/3; gap=none)
    B-8 (V1=medium, V3=medium; convergence=2/3; gap=none)
    B-10 (V2=medium, V3=medium; convergence=2/3; gap=none)
    B-3 (V1=medium, V2=high; convergence=2/3; gap=low)
    B-14 (V1=medium, V2=high; convergence=2/3; gap=low)
    A-1 (V1=medium, V2=high; convergence=2/3; gap=low)

  low_convergence_high_gap: none

  D-4 selection path: Apply standard path. Highest-priority candidates for D-4 are:
    (1) convergence=3/3: B-1 (selectivity claim without byproduct data)
    (2) convergence=2/3, temperature_gap=low, highest severity: B-2 (catalytic cycle without evidence), B-14 (mechanism by analogy), B-3 (ligand order + cis-geometry inference)
    (3) Self-contradictory absence U items: U-1 (R–R not reported), U-2 (black mixture)

---

[GAP] GAP-1 | type: 1 | priority: high | description: Retrieve Tamura and Kochi (1971) data on iron-catalyzed cross-coupling of Grignard reagents with alkenyl halides to perform the yield/selectivity comparison absent from this paper. | candidate_paper: M. Tamura and J. Kochi, Synthesis, 303 (1971) [ref 6] | inference_label: T1 | status: pending

[GAP] GAP-2 | type: 2 | priority: high | description: Retrieve Corriu and Masse (Chem. Commun. 144, 1972) concurrent communication on cross-coupling with Ni(acac)₂ to assess whether chelating phosphine provides unique selectivity advantages or whether the Ni center alone is sufficient. | candidate_paper: R. J. P. Corriu and J. P. Masse, Chem. Commun., 144 (1972) [ref 3a] | inference_label: T1 | status: pending

[GAP] GAP-3 | type: 3 | priority: medium | description: A mechanistic study of Ni-phosphine-catalyzed cross-coupling providing kinetic data, intermediate characterization, or radical clock experiments would answer the core questions in B-2, U-1, U-4. | candidate_paper: Anticipated Tamao/Kumada follow-up on mechanism (series_signal). | inference_label: T2 [paper-grounded inference] | status: pending

[GAP] GAP-4 | type: 3 | priority: medium | description: A stereochemical/mechanistic study of vinylhalide cross-coupling addressing cis/trans product ratio formation would answer A-1 and U-3. | candidate_paper: not specified | inference_label: T3 [external inference] | status: pending

inference_time_sec: not available — inject externally
```

---

> **Tier 8 redaction notice**: This file is a redacted copy of the corresponding Tier 3 / Tier 9 output. Verbatim source-paper quotations have been replaced by `[REDACTED: see source paper §<loc>; full text retained in Tier 9 reviewer-only deposit]` markers, preserving location references and our own analytical content. Bibliographic fields (title, authors, journal, year, DOI), analytical labels (`evidence_chain:` with B-/U-/A-/C- internal IDs), short technical terms, and our own analytical text are not redacted. The redaction was applied by `scripts/redact_for_tier8.py` and, for this version, by `scripts/build_paperA_R1_public.py` with `scripts/redact_source_ngram_runs.py` (scripts of the project repository; they are not deposited).
