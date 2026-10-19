```
prompt_version: stage1-v184-20260502
```

---

target_title:   Enantioselective and Enantiospecific Transition-Metal-Catalyzed Cross-Coupling Reactions of Organometallic Reagents To Construct C−C Bonds
target_authors: Alan H. Cherney, Nathaniel T. Kadunce, and Sarah E. Reisman
target_start:   page 1 (9587): [REDACTED: paper boundary quote; see Tier 9]
target_end:     end of document

---

## [Turn 1: Agent V1]

field: Enantioselective and enantiospecific transition-metal catalysis (asymmetric cross-coupling chemistry)

field_rationale: The review is published in Chemical Reviews and covers transition-metal-catalyzed stereocontrolled C−C bond formation via asymmetric cross-coupling; the relevant expert is a specialist in asymmetric catalysis with experience in Ni/Pd/Cu-catalyzed reactions of organometallic reagents and chiral ligand design.

---

**V1-Q1**

loc: P2:Lcol:28-35* (p. 9588, left column, discussion of DYKAT and substrate scope under enantioselective Ni catalysis)

quote: [REDACTED: see `loc:` above; full text in Tier 9]
question: The review introduces four mechanistic categories of enantioselective cross-coupling (Figure 1: racemic nucleophile, racemic electrophile, achiral + achiral → chiral, desymmetrization) but never reports a systematic quantitative breakdown of how many of the ~427 cited references fall into each category, nor the distribution of ee values across categories. What fraction of the literature covers each mechanistic pathway, and how does the average attained ee compare across the four types?

severity: medium

inference_tier: T2 [paper-grounded inference]

---

**V1-Q2**

loc: P3:Lcol:1-10* (p. 9589, section 2.1.1 Organomagnesium Reagents, early enantioselective coupling with DIOP/Prophos)

quote: [REDACTED: see `loc:` above; full text in Tier 9]
question: The review notes ambiguity between kinetic resolution and DYKAT for the original Consiglio-Kumada 1973–1974 results but does not report whether subsequent mechanistic studies (e.g., varying the ratio of enantiomers in a partially resolved Grignard, measuring rate ratios k_fast/k_slow) have resolved this ambiguity. Has the KR vs. DYKAT question for the prototypical Ni/DIOP system ever been definitively settled, and if so, with what evidence?

severity: medium

inference_tier: T2 [paper-grounded inference]

---

**V1-Q3**

loc: P3:Rcol:20-40* (p. 9589–9590, Figure 5 caption and surrounding text on α-methylbenzyl Grignard coupling)

quote: [REDACTED: see `loc:` above; full text in Tier 9]
question: Figure 5 presents ee values for >20 ligands (L7–L25) in the coupling of α-methylbenzyl Grignard reagent 5 with vinyl bromide. The caption explicitly warns that conditions differ across studies, but the review makes no attempt to identify which variables (solvent, temperature, Grignard:halide ratio, Ni precursor, loading) are responsible for the variation. Without a controlled head-to-head comparison, are the observed differences in ee among ligands interpretable as reflecting ligand electronics/sterics, or are they confounded by experimental differences?

severity: medium

inference_tier: T2 [paper-grounded inference]

---

**V1-Q4**

loc: P4:Lcol:1-20* (p. 9590, discussion of amine directing group in PPFA-type ligands, Figure 6 catalytic cycle)

quote: [REDACTED: see `loc:` above; full text in Tier 9]
question: The catalytic cycle in Figure 6 invokes precoordination of the Grignard reagent's amino terminus to Ni during transmetalation to direct enantioselective delivery of one enantiomer of 5, but no kinetic, NMR spectroscopic, or computational data supporting the existence of this precoordination complex are cited. Is there direct evidence (e.g., isolation or spectroscopic detection of a Ni–amine precoordination intermediate, or kinetic isotope studies) for this mechanistic proposal beyond the indirect ligand SAR argument?

severity: high

inference_tier: T2 [paper-grounded inference]

---

**V1-Q5**

loc: P5:Lcol:18-30* (p. 9591, discussion of (E)-bromostyrene as electrophile with PPFA L13 delivering 10 in 52% ee)

quote: [REDACTED: see `loc:` above; full text in Tier 9]
question: For coupling of α-methylbenzyl Grignard 5 with (E)-bromostyrene, the review reports only 52% ee with the best Ni catalyst (PPFA, L13) and does not report ee values for more challenging disubstituted alkene electrophiles or alkyl halide electrophiles. What is the substrate scope limitation for the enantioselective Ni-catalyzed coupling of secondary Grignard reagents with respect to the electrophile (e.g., alkyl, aryl, heteroaryl, internal alkenyl halides), and why has this not been systematically explored? Are there failure cases for electrophiles beyond (E)-bromostyrene?

severity: medium

inference_tier: T2 [paper-grounded inference]

---

**V1-Q6**

loc: P5:Rcol:25-45* (p. 9591–9592, Scheme 2, coupling of α-silyl Grignard reagents 11/13 with vinyl bromide using PdCl₂[(R)-(S)-PPFA])

quote: [REDACTED: see `loc:` above; full text in Tier 9]
question: The kinetic resolution vs. DKR assignment for α-alkyl-substituted Grignard 13 is based on the ratio-dependence of ee, but the paper does not report the measured half-life of racemization for 13 under the reaction conditions, nor a direct comparison of the racemization rate constant with the cross-coupling rate constant. Without these rate constants, the KR/DKR assignment remains inferential. What are the actual racemization and coupling rates for 13 under these conditions?

severity: high

inference_tier: T2 [paper-grounded inference]

---

**V1-Q7**

loc: P7:Rcol:1-25* (p. 9593, section 2.2 on secondary alkyl electrophiles, and discussion of radical clock experiments throughout sections 2.2.1–2.2.6)

quote: [REDACTED: see `loc:` above; full text in Tier 9]
question: For enantioselective coupling of secondary alkyl *electrophiles* (sections 2.2.1–2.2.6), the review invokes radical clock experiments and SET mechanisms, but the turnover-limiting step (oxidative addition vs. transmetalation vs. reductive elimination) is rarely reported for each system. Does the rate-determining step vary across the Ni/Pd/Cu catalyst systems described in sections 2.2.1–2.2.6, and is there consistent kinetic characterization (e.g., rate orders, Hammett studies, KIEs) that would unify the mechanistic picture?

severity: medium

inference_tier: T2 [paper-grounded inference]

---

**V1-Q8**

loc: P8:Rcol:30-50* (p. 9594, section 2.2.2 Organozinc, Fu group coupling of α-bromo amides 30 with alkylzinc and Ni/L38)

quote: [REDACTED: see `loc:` above; full text in Tier 9]
question: The computational study (Lin et al.) is cited to support a Ni¹/Ni³ mechanism for the Fu group's α-bromo amide Negishi coupling, but the review does not state whether experimental validation of the Ni¹/Ni³ proposal has been reported (e.g., isolation of Ni¹ or Ni³ intermediates, EPR spectroscopic evidence, stoichiometric reactions). Is the Ni¹/Ni³ assignment exclusively computational, and do any experimental observations confirm or contradict it?

severity: high

inference_tier: T2 [paper-grounded inference]

---

**V1-Q9**

loc: P9:Lcol:15-30* (p. 9595, Ni/L39-catalyzed Negishi coupling of propargyl halides 34 with Ph₂Zn and Ph₂ZnEt; Figure 15)

quote: [REDACTED: see `loc:` above; full text in Tier 9]
question: The review states that a radical chain mechanism is supported for the propargyl halide Negishi coupling but provides no details on how the radical chain proposal was validated (e.g., TEMPO inhibition, radical clock ring-opening, quantum yield measurement). What specific experimental evidence distinguishes the radical chain pathway from a direct S_N2-type oxidative addition for the propargyl halide system?

severity: medium

inference_tier: T2 [paper-grounded inference]

---

**V1-Q10**

loc: P10:Rcol:18-35* (p. 9596, section 2.2.3 Organoboron Reagents, Molander dual catalysis with Ni/Ir, Figure 11)

quote: [REDACTED: see `loc:` above; full text in Tier 9]
question: The Ni/Ir dual catalysis system for cross-coupling of organoboron reagents (section 2.2.3, Figure 11, compound 23, 52% yield, 50% ee) represents a proof-of-concept with low ee. The review acknowledges that "additional investigations toward asymmetric catalysis would be valuable" but does not report whether the low ee arises from non-selective radical recombination with the Ni^II catalyst, background Suzuki-Miyaura coupling, or incomplete photocatalytic turnover. What controls (e.g., dark reaction control, TEMPO trapping of the alkyl radical, enantioselectivity as a function of light intensity) were performed to validate the mechanistic proposal and diagnose the origin of the poor ee?

severity: medium

inference_tier: T2 [paper-grounded inference]

---

**V1-Q11**

loc: P14:Rcol:20-40* (p. 9600, section 2.3.2 Organoboron Reagents, desymmetrization of meso-anhydrides with Pd/Josiphos L53, Figure 30b)

quote: [REDACTED: see `loc:` above; full text in Tier 9]
question: The halide-salt sensitivity of the Pd-catalyzed desymmetrization is noted (LiX addition drops ee sharply), and the authors propose that halides interfere with the chiral phosphoramide ligand coordination. However, no systematic variation of halide identity (Cl⁻, Br⁻, I⁻, OTf⁻) or halide concentration is reported, nor is the identity of the active Pd catalyst in the presence of halide characterized. Is the halide effect operative at the oxidative addition step (Pd affinity for halide) or at the transmetalation step (halide exchange on Zn), and what evidence addresses this?

severity: medium

inference_tier: T2 [paper-grounded inference]

---

**V1-Q12**

loc: P17:Lcol:5-25* (p. 9603, section 3.1.2 Organotin Reagents, Hiyama coupling of secondary silanes 113 and 114 with aryl triflates, Figure 34)

quote: [REDACTED: see `loc:` above; full text in Tier 9]
question: The stereochemical outcome of the Hiyama cross-coupling of sec-alkyltrifluorosilane 113 is highly sensitive to solvent polarity (retention at 50°C in THF; inversion at 90°C; HMPA → inversion with lower es). The review attributes these outcomes to competing S_E2(cyclic) and S_E2(open) transmetalation transition states, but does not report whether the enantiospecificity (es) at the same ee of starting material was tested at intermediate temperatures or in mixed solvent systems to map the transition state energy landscape. What is the full temperature/solvent profile of the retention-vs-inversion crossover, and has a linear free energy relationship been established?

severity: medium

inference_tier: T2 [paper-grounded inference]

---

**V1-Q13**

loc: P29:Rcol:15-30* (p. 9615, section 4.1.1 Organomagnesium Reagents in allylic substitution, early Ni-catalyzed results)

quote: [REDACTED: see `loc:` above; full text in Tier 9]
question: Throughout section 4.1.1, the review describes Ni-catalyzed asymmetric allylic substitution with organomagnesium reagents delivering only modest ee values for acyclic electrophiles (e.g., 47% ee, Scheme 26b; 47% ee with Consiglio conditions). The failure of acyclic substrates to give high ee is noted repeatedly but no mechanistic analysis of why acyclic electrophiles underperform cyclic ones is given (e.g., slower σ→π allyl isomerization vs. competing direct S_N2, lack of conformational lock). What structural and mechanistic factors account for the consistent inferiority of acyclic allylic electrophiles in Ni-catalyzed asymmetric allylic substitution with Grignard reagents?

severity: medium

inference_tier: T2 [paper-grounded inference]

---

**V1-Q14**

loc: P44:Lcol:8-25* (p. 9630, section 4.1.4 Organoboron Reagents, Cu/L101-catalyzed coupling of simple alkylboranes with allylic chlorides, Scheme 40)

quote: [REDACTED: see `loc:` above; full text in Tier 9]
question: Scheme 40 demonstrates the Cu/L101-catalyzed enantioselective allylic alkylation using simple, unactivated 9-BBN reagents (93% yield, 88% ee for tertiary center, 79% yield, 90% ee for quaternary center), but no functional group tolerance data are reported beyond the competition experiment with aryl bromide. What is the breadth of functional group compatibility for the nucleophile (e.g., ester, halide, free alcohol, amine) and for the allylic chloride electrophile (e.g., α-branching, heteroatom substituents), and what functional groups cause failure?

severity: medium

inference_tier: T2 [paper-grounded inference]

---

**V1-Q15**

loc: P53:Lcol:1-20* (p. 9639, section 5.3 Enantioselective Preparation of Planar Chiral Compounds, Scheme 59)

quote: [REDACTED: see `loc:` above; full text in Tier 9]
question: The Pd/Boc-L-Val-OH-catalyzed asymmetric C−H activation/arylation of N,N-dimethylaminomethylferrocene 542 gives 543 in 73% yield and 98% ee (Scheme 59), and a directing group role for the dimethylamino group is proposed. However, the review cites no experiment in which the directing group is systematically varied (e.g., N-methyl, N-phenyl, sulfonamide, ester) to probe the sensitivity of ee and yield to the directing group identity, nor is a stoichiometric palladacycle intermediate characterized. Has the palladacycle intermediate been isolated or characterized spectroscopically, and what variation in the directing group has been reported?

severity: medium

inference_tier: T2 [paper-grounded inference]

---

**[Scope failure verification — mandatory check]**

The review covers 66 pages; formal substrate scope tables with explicit 0% yield or trace entries are uncommon in a survey review (scope tables belong to the primary papers). The review does explicitly mention the following failure or limitation cases:

- Grignard reagent **13** (limiting reagent conditions) → ee falls precipitously (Scheme 2b): attributed to slow racemization relative to coupling (KR regime), but mechanistic evidence for this attribution is the subject of V1-Q6 above.
- Coupling of α-bromo amide **63** with Ph(9-BBN): "diphenyl amides and Weinreb amides delivered nearly racemic products" — no supporting evidence cited for why these amide substituents abolish selectivity (section 2.2.3, Figure 22). Attribution: identity of amide substituents matters, not stated why.
- Allylic substrates in Ni catalysis (acyclic vs. cyclic) — covered in V1-Q13.
- Propargyl carbonate substrates **36a/36b** give low yields and ee under Negishi conditions (Figure 15a, 8% and 60% ee respectively): attributed to competing background reactions; no mechanistic data.
- Cu-catalyzed coupling of primary RMgBr with acyclic linear allylic electrophiles often gives regioselectivity problems (mixture of α- and γ-products): noted throughout section 4.1.1 but mechanisms of regioselectivity control are not analyzed.

Failure case for **diphenyl and Weinreb amides** in α-chloroamide Suzuki-Miyaura (Figure 22):

loc: P11:Rcol:5-18* (p. 9597, Figure 22 discussion)

quote: [REDACTED: see `loc:` above; full text in Tier 9]
No mechanistic evidence is presented for why Weinreb amides fail enantioselectively while other amide substitutions succeed. This is a gap worth flagging as implicit in V1-Q4 (directing group) but is a separate scope failure.

---

**[Dropped Quantitative Benchmark check — mandatory]**

Several prior studies cited with numerical values in the introduction are never compared on the same metric in the Results/Discussion:

1. The introduction references the 2010 Nobel Prize and frames the field as having undergone a "paradigm shift," citing Heck, Negishi, and Suzuki reactions, but does not establish baseline ee/yield benchmarks from those achiral reactions against which the stereocontrolled variants are compared.

2. The review cites early Kumada-Corriu results (1973/1974) as giving "20% yield, 15% ee" and "80% yield, 38% ee" (Figure 3, L1 and L2), but never benchmarks subsequent Ni-catalyzed enantioselective Kumada coupling of secondary Grignard reagents against the original 1973/1974 numbers on the *same substrate pair* (sec-BuMgX + PhBr). The closest modern result cited is Scheme 1 (40% yield, 20% ee with CoCl₂/L5), which underperforms the 1974 values.

3. The review does not provide a table of the "current best" ee/yield/catalyst loading values for each reaction class at the review's time of writing (2014 cutoff), making it impossible to identify which areas represent the state-of-the-art and which remain underperforming relative to benchmarks cited in the introduction.

These patterns collectively constitute a C-item candidate (Dropped Quantitative Benchmark) — the introduction establishes numerical values (15–99% ee across ligands in Figure 5) but the discussion section does not perform a cross-paper quantitative comparison on a standardized substrate to identify the true performance frontier.

---

> **Tier 8 redaction notice**: This file is a redacted copy of the corresponding Tier 3 / Tier 9 output. Verbatim source-paper quotations have been replaced by `[REDACTED: see source paper §<loc>; full text retained in Tier 9 reviewer-only deposit]` markers, preserving location references and our own analytical content. Bibliographic fields (title, authors, journal, year, DOI), analytical labels (`evidence_chain:` with B-/U-/A-/C- internal IDs), short technical terms, and our own analytical text are not redacted. The redaction was applied by `scripts/redact_for_tier8.py` and, for this version, by `scripts/build_paperA_R1_public.py` with `scripts/redact_source_ngram_runs.py` (scripts of the project repository; they are not deposited).
