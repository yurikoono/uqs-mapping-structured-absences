prompt_version: stage1-v184-20260502
model_info: claude-sonnet-4-6

target_title:   Discovery of the cross-coupling reaction between Grignard reagents and C(sp2) halides catalyzed by nickel–phosphine complexes
target_authors: Kohei Tamao
target_start:   page 1: [REDACTED: paper boundary quote; see Tier 9]
target_end:     end of document

---

## Step 0: Boundary recheck

All quotes from Turns 1–3 were verified against the target paper boundary (4-page mini-review, J. Organometall. Chem. 653 (2002) 23–26). The paper is self-contained; all quoted passages appear within this single article. The reference list on page 4 includes companion articles in the same special volume with placeholder page numbers ([8b], [11b], [14d], [15], [16d]); these are cited materials, not a separate paper in the same PDF. No quotes originate from an adjacent paper. No boundary violations detected. No items appended [?boundary].

---

## Step 1: Cross-field temperature for overlapping questions

**V2-OV1 (overlaps V1-Q12):**
- V1 severity: low
- V2 severity: high
- Temperature gap: distance = 3 (low=1, high=3) → temperature_gap: **medium** (low↔high = 2 steps)
- Convergence: 2/3 (V1 + V2)
- V3-OV2 also overlaps V1-Q12 with V3 severity: medium
- Full cross-field: V1=low, V2=high, V3=medium → max=high(3), min=low(1), distance=2 → temperature_gap: **medium**
- Convergence: 3/3

**V2-OV2 (overlaps V1-Q7):**
- V1 severity: medium
- V2 severity: high
- Distance = 1 → temperature_gap: **low**
- Convergence: 2/3

**V2-OV3 (overlaps V1-Q3):**
- V1 severity: medium
- V2 severity: medium
- Distance = 0 → temperature_gap: **none**
- Convergence: 2/3

**V2-OV4 (overlaps V1-Q6):**
- V1 severity: medium
- V2 severity: medium
- Distance = 0 → temperature_gap: **none**
- Convergence: 2/3

**V3-OV1 (overlaps V1-Q11):**
- V1 severity: low
- V3 severity: high
- Distance = 2 → temperature_gap: **medium**
- Convergence: 2/3

**V3-OV2 (overlaps V1-Q12):** already folded into V2-OV1 above (3/3 convergence)

**V3-OV3 (overlaps V2-Q10):**
- V2 severity: medium
- V3 severity: medium
- Distance = 0 → temperature_gap: **none**
- Convergence: 2/3

---

## Step 2: Same-root question groups (pre-classification scan)

**SRG-1: Catalytic cycle elementary-step evidence absent**
Members (candidate): V2-Q1, V2-Q2, V2-Q4, V2-Q8, V2-Q10, V3-OV3/V2-Q10
Shared root: The paper proposes a three-step Ni(II)/Ni(0) catalytic cycle (Scheme 1) and claims it "has become the prototype" for subsequent Pd cross-coupling, but provides no experimental evidence from the 1972 work or its successors that the individual elementary steps (oxidative addition, transmetallation, reductive elimination) occur as proposed rather than via alternative manifolds.

**SRG-2: Mechanistic attribution of isomerization pathway**
Members (candidate): V2-Q3, V2-Q11, V1-Q3 (partial — yield side)
Shared root: The paper reports ligand- and halide-dependent sec-to-primary alkyl isomerization (eq. 3) but does not establish which mechanistic pathway (β-hydride elimination/re-insertion chain-walking, radical chain-transfer, Grignard pre-equilibration) is operative, and the apparent reversal of the ligand-dependence relative to chain-walking predictions is not addressed.

**SRG-3: Prototype/influence claim — priority, mechanism, and bibliometrics**
Members (candidate): V1-Q12, V2-OV1/V2-Q2, V3-Q4, V3-OV2
Shared root: The claim that Scheme 1 "has become the prototype" for palladium cross-coupling is simultaneously a priority claim (historiographic), a mechanistic lineage claim (which specific elementary steps were adopted), and an influence claim (demonstrated by citation analysis), all of which are asserted without systematic evidence.

**SRG-4: Citation-trend data reliability (Fig. 2)**
Members (candidate): V1-Q11, V3-Q3, V3-OV1
Shared root: The entire bibliometric argument in Section 3 rests on Fig. 2 (citation counts 1984–1999), whose database, search protocol, self-citation handling, and reproducibility are entirely unspecified.

**SRG-5: Ni > Pd reactivity comparison — quantitative basis absent**
Members (candidate): V1-Q7, V2-OV2/V2-Q9
Shared root: The claim that Ni is "generally more reactive" toward C(sp2)-halides than Pd is stated without rate constants, competition experiments, or identification of which elementary step(s) account for the difference; the comparison also inverts the typical oxidative addition reactivity expectation for ArCl substrates.

**SRG-6: Reporting completeness of scope equations (yields, conditions, measurement basis)**
Members (candidate): V1-Q1, V1-Q2, V1-Q3, V1-Q4, V1-Q6, V1-Q8
Shared root: Across features 3–8 in Section 2, quantitative claims (activity orders, yields, stereochemical ratios) are presented without specifying measurement basis (GC vs. isolated), experimental conditions, or referencing primary data for verification.

**SRG-7: Discovery narrative — retrospective reconstruction vs. contemporaneous documentation**
Members (candidate): V3-Q1, V3-Q2, V3-Q6, V3-OV3/V2-Q10
Shared root: The chronological narrative of ideas and experiments (1970–1971 background → October 1971 start → end of 1971 communication [1]) is presented from first-person retrospective recollection 30 years after the events, without archival corroboration, and at least one cited precedent paper (ref [9]) was published after the discovery communication.

---

## Step 3: Classification of all questions

---

### [A] Deferred Questions

No items from Turns 1–3 qualify as pure A-category (the paper does not send any issue to future work, and it does not raise a specific research question it then leaves open). The paper's Epilogue gestures toward future importance of cross-coupling but does not identify a specific deferred question. The paper does not acknowledge any methodological failure of its own primary method (it is a retrospective review, not a primary research report with computational or spectroscopic method). Therefore: **A count = 0**.

---

### [B] Traces of Rejection

**B-1** | loc: P2:Lcol:Feature 3 | quote: [REDACTED: substantial verbatim quotation; see Tier 9] | classification: reporting_omission | rhetorical_function: Summary statement of ligand activity ranking presented as a general empirical observation. | note: The order covers only 4 of the 6 Ni–phosphine complexes that the paper states were prepared (Section 1 names also Ni(dmpe)Cl₂ and Ni(dmpf)Cl₂); the omission of dmpe and dmpf from the activity ranking is not acknowledged. No substrate, temperature, solvent, or data source is cited; ref [10] is invoked en bloc. Measurement basis for "catalytic activity" (TON, isolated yield, rate?) is not defined. | cross_field_temperature: V1=medium (Q1); no V2 or V3 overlap on this specific item.

**B-2** | loc: P2:Rcol:Feature 4 / eq. 2 | quote: [REDACTED: substantial verbatim quotation; see Tier 9] | classification: reporting_omission | rhetorical_function: Highlighted claim of a unique selectivity feature, exemplified by a single representative reaction. | note: Yield of 80% is stated but basis (GC vs. isolated), reaction scale, optimized vs. representative status, and mass balance for β-hydride elimination or homocoupling byproducts are not reported. The "most significant feature" framing elevates this to the paper's central empirical claim, making the reporting omission more consequential. | cross_field_temperature: V1=medium (Q2); V2 raises the mechanistic dimension of β-hydride elimination suppression (V2-Q4, high) but addresses a different question from B-2 (why does the reaction outcompete β-hydride elimination? vs. what is the yield basis?); V2-OV3 does not overlap B-2 directly.

**B-3** | loc: P2:Rcol:Feature 5 / eq. 3 | quote: [REDACTED: substantial verbatim quotation; see Tier 9] | classification: reporting_omission | rhetorical_function: Statement of a selectivity phenomenon with ligand and electronic dependence, illustrated by two data points. | note: Eq. 3 shows isomer ratios (96:4 and 9:84 for dppp and dmpe) but no yield data accompany either entry; whether ratios are from GC of crude or isolated products is not specified. Only 2 of 6 available ligands are shown. | cross_field_temperature: V1=medium (Q3), V2=medium (OV3) — convergence 2/3, temperature_gap: none.

**B-4** | loc: P3:Lcol:Feature 7 | quote: [REDACTED: substantial verbatim quotation; see Tier 9] | classification: reporting_omission | rhetorical_function: Parenthetical note on substrate scope extension to an otherwise unreactive substrate class. | note: No Grignard reagent, catalyst loading, temperature, solvent, reaction time, yield, or citation to primary data is provided. The claim is noted without supporting evidence in this paper; "rather low" is not quantified. | cross_field_temperature: V1=medium (Q4); V2=medium (Q7, mechanistic angle on C–F oxidative addition barrier) — these are parallel but distinct questions; B-4 records the reporting omission, V2-Q7 is handled under U.

**B-5** | loc: P3:Lcol:Feature 7 | quote: [REDACTED: substantial verbatim quotation; see Tier 9] | classification: reporting_omission | rhetorical_function: Claim of high reactivity and industrial application, with forward citation to a companion article not yet published. | note: Ref [15] (Banno, J. Organomet. Chem. xxx (2002) yyy) has placeholder page numbers and is unpublished at submission date. No industrial scale, TON, TOF, or process conditions are provided in this paper. The industrial claim is unverifiable from the cited reference. | cross_field_temperature: V1=medium (Q5).

**B-6** | loc: P3:Lcol:Feature 8 | quote: [REDACTED: substantial verbatim quotation; see Tier 9] | classification: reporting_omission | rhetorical_function: Stereochemical scope statement presented as a general feature. | note: No substrates, E:Z ratios of products vs. starting materials, or conditions are cited for this general statement. No citation to primary data accompanies this specific claim. | cross_field_temperature: V1=medium (Q6), V2=medium (OV4, mechanistic angle on retention mechanism) — convergence 2/3, temperature_gap: none.

**B-7** | loc: P3:Rcol:Feature 10 / eq. 6 | quote: [REDACTED: substantial verbatim quotation; see Tier 9] | classification: reporting_omission | rhetorical_function: Priority claim for oligomer synthesis illustrated by a single representative equation. | note: Eq. 6 shows 64% yield for a quaterthiophene but does not specify yield basis (GC vs. isolated), selectivity for intended chain length vs. longer/shorter oligomers, or product purity. | cross_field_temperature: V1=low (Q8).

**B-8** | loc: P3:Rcol:Section 3 / Fig. 2 | quote: [REDACTED: substantial verbatim quotation; see Tier 9] | classification: reporting_omission | rhetorical_function: Bibliometric data presented as evidence for the growing importance of cross-coupling reactions. | note: No database, search date, self-citation exclusion rule, language coverage, or search protocol is specified. Fig. 2 y-axis bar heights appear readable from the figure (scale goes to ~140 citations), but without the named source database the data cannot be independently reproduced. Submitted August 2001, data extends only to 1999. | cross_field_temperature: V1=low (Q11), V3=high (OV1/Q3) — convergence 2/3, temperature_gap: medium (low=1, high=3, distance=2).

---

### [C] Uncontinued Citations

**C-1** | loc: P1:Rcol:Section 1 | citation: [4] J. Chatt, B.L. Shaw, J. Chem. Soc. (1960) 1718 | textual_function: Background citation for the NiX(Ar)(PR₃)₂ class of σ-organonickel complexes within the inventory of ~20 known complexes. | reason_severed: Cited as structural precedent only; no specific finding, property, or reactivity datum from [4] is discussed or compared in the paper. | affects_claims: medium — the classification of σ-organonickel complexes (three types) feeds into the historical narrative of how transmetallation was understood, which is the first mechanistic pillar of Scheme 1. | symmetric_pattern: yes — refs [4], [5], [6] are all cited in a parallel list-classification pattern for the three σ-organonickel complex types; all are cited-and-dropped at the same level.

**C-2** | loc: P1:Rcol:Section 1 | citation: [5] H. Yamazaki, N. Hagihara, Bull. Chem. Soc. Jpn. 37 (1964) 907 | textual_function: Background citation for CpNi(C₂H₅)(PPh₃) class within the same inventory. | reason_severed: Cited as structural precedent only; no specific finding compared or engaged. | affects_claims: medium — same as C-1 (mechanistic narrative pillar). | symmetric_pattern: yes — part of the [4]/[5]/[6] symmetric citation group.

**C-3** | loc: P1:Rcol:Section 1 | citation: [6] (a) Yamamoto et al. J. Am. Chem. Soc. 87 (1965) 4652; (b) Saito et al. J. Am. Chem. Soc. 88 (1966) 5198; (c) Wilke, Herrmann, Angew. Chem. 78 (1966) 591 | textual_function: Background citation for Ni(C₂H₅)₂(bpy) class, establishing that β-alkyl-nickel complexes can be stabilized by bidentate ligands. | reason_severed: The specific claim cited — β-stabilization by bidentate bpy — is the second of three mechanistic ideas Tamao identifies as underpinning the discovery, yet no kinetic or structural data from [6a–c] are quoted or compared with 1972 results. | affects_claims: medium — mechanistic narrative: the idea that β-alkyl-nickel species could survive long enough for reductive elimination is a prerequisite for the selectivity claim (feature 4). | symmetric_pattern: yes — parallel to [4] and [5] in the three-type inventory citation.

**C-4** | loc: P1:Rcol:Section 1 / P2:Lcol:Feature 2 | citation: [7] J.P. Collman, Acc. Chem. Res. 1 (1968) 136 | textual_function: Dual citation: (a) first use — attributed as source for the concept of β-hydrogen stabilization by bidentate ligand (second main idea); (b) second use — for the oxidative addition/reductive elimination terminology. | reason_severed: In both uses, Collman [7] is cited for vocabulary and conceptual framing only; no specific Collman result is compared with Kumada cross-coupling data. | affects_claims: medium — Collman's conceptual framework is the terminological basis for the catalytic cycle (Scheme 1), so the lack of substantive engagement means the intellectual debt is acknowledged but the mechanistic foundation is not empirically grounded from [7]. | symmetric_pattern: no — unique function as dual conceptual source.

**C-5** | loc: P1:Rcol:Section 1 | citation: [9] Y. Kiso, M. Kumada, K. Maeda, K. Sumitani, K. Tamao, J. Organomet. Chem. 50 (1973) 311 | textual_function: Citation for Sumitani's preparation of Ni(0)-ethylene complexes from NiCl₂(PR₃)₂ + ethyl Grignard, framed as pre-discovery foundational work (1970–1971). | reason_severed: Ref [9] is cited as supporting evidence for the pre-discovery experimental basis, but [9] was published in 1973 — one year after the discovery communication [1]. No data from [9] are reproduced or compared in this mini-review; the citation functions as a retrospective documentation rather than a directly engaged result. The chronological framing implies [9] records work predating [1], but this is not stated in [9]'s publication record. | affects_claims: yes — the precatalyst activation narrative (Ni(0) from NiCl₂ + RMgX) is presented as a mechanistic underpinning of the discovery; if [9] is retrospective, this specific mechanistic grounding may be post-hoc. | symmetric_pattern: no — unique chronological complexity.

**C-6** | loc: P2:Lcol:Feature 1 | citation: [11] (a) M. Yamamura, S.-I. Murahashi, I. Moritani, J. Organomet. Chem. 91 (1975) C39; (b) S.-I. Murahashi, J. Organomet. Chem. xxx (2002) 000 (This special volume) | textual_function: Citation for the claim that the Scheme 1 catalytic cycle [REDACTED: substantial verbatim quotation; see Tier 9] | reason_severed: [11a] is the first example cited of palladium cross-coupling adopting an analogous cycle, but the paper makes no specific comparison between Scheme 1 and the mechanistic proposal in [11a]; no data from [11a] are reproduced. [11b] has placeholder page numbers and is not yet published. The "prototype" claim requires citation to mechanistic papers that explicitly adopted Scheme 1, but [11] is cited without that demonstration. | affects_claims: yes — the prototype claim is the central historiographic assertion of the paper; severing of specific engagement with [11] means the claim rests on assertion rather than demonstrated intellectual lineage. | symmetric_pattern: no.

**C-7** | loc: P2:Lcol:Feature 2 | citation: [12] M.S. Kharasch, O. Reinmuth, Grignard Reactions of Nonmetallic Substances, Prentice-Hall, NJ, 1954 | textual_function: Background citation for the "traditional Kharasch-type Grignard reactions" that served as the conceptual contrast class for the "molecular catalysis[REDACTED: substantial verbatim quotation; see Tier 9]first case" priority claim (feature 2) depends implicitly on [12] delimiting what counts as Kharasch-type catalysis, but the boundary is not defined. | symmetric_pattern: no.

**C-8** | loc: P2:Rcol:Feature 5 | citation: [13] (a) K. Tamao, Y. Kiso, K. Sumitani, M. Kumada, J. Am. Chem. Soc. 94 (1972) 9268; (b) Y. Kiso, K. Tamao, M. Kumada, J. Organomet. Chem. 50 (1973) C12 | textual_function: Citations for the ligand-basicity and aromatic-halide-electronics dependence of sec-alkyl isomerization. | reason_severed: The isomerization phenomenon (eq. 3) is attributed to refs [13a,b], but no specific data table, rate constant, or selectivity comparison from those papers is reproduced or discussed. The mini-review presents only two data points (dppp and dmpe) without engaging the full scope reported in [13a,b]. | affects_claims: medium — the incomplete engagement means the mechanistic question about which pathway produces the ligand-dependence cannot be evaluated from this paper. | symmetric_pattern: partial — [13a] and [13b] are cited together for the same phenomenon but cover different experimental variables (ligand basicity vs. halide electronics), so they are not fully symmetric.

**C-9** | loc: P2:Rcol:Feature 6 | citation: [14] (a) Consiglio, Botteghi, Helv. Chim. Acta 56 (1973) 460; (b) Kiso, Tamao, Miyake, Yamamoto, Kumada, Tetrahedron Lett. (1974) 3; (c) Hayashi, Tajika, Tamao, Kumada, J. Am. Chem. Soc. 98 (1977) 3718; (d) T. Hayashi, J. Organomet. Chem. xxx (2002) xxx (This special volume) | textual_function: Citations for the claim that asymmetric cross-coupling is possible with chiral phosphine–Ni catalysts. | reason_severed: Feature 6 is stated in one sentence with no ee values, substrate scope, reaction conditions, or mechanistic information. All four references are cited-and-dropped. [14d] has placeholder page numbers. | affects_claims: medium — the ee data in [14] would be necessary to evaluate whether the enantioselectivity is synthetically useful or merely demonstrable, and the mechanistic origin (which step is stereodetermining) is unaddressed. | symmetric_pattern: yes — all four references serve the same rhetorical function (existence proof of asymmetric coupling).

**C-10** | loc: P3:Lcol:Feature 9 | citation: [16] (a) Negishi, Baba, J. Chem. Soc. Chem. Commun. (1976) 596; (b) Negishi, King, Okukado, J. Org. Chem. 42 (1977) 1821; (c) Negishi, van Horn, J. Am. Chem. Soc. 99 (1977) 3168; (d) Negishi, J. Organomet. Chem. xxx (2002) zzz (This special volume) | textual_function: Citations for palladium-catalyzed cross-coupling reactions, supporting the Ni > Pd reactivity comparison. | reason_severed: The comparative claim [REDACTED: substantial verbatim quotation; see Tier 9] cites [11] and [16] but makes no direct numerical comparison of any rate, yield, TON, or TOF from any of these Negishi papers with corresponding Kumada results. [16d] has placeholder page numbers. | affects_claims: yes — the Ni > Pd reactivity claim underpins feature 9 (stepwise halide selectivity), and without data engagement it cannot be evaluated or falsified. | symmetric_pattern: partial — [16a–c] all report Pd cross-coupling, but they vary in organometallic partner (Zn, Mg, Zr) and halide substrate, so they are not fully parallel.

**C-11** | loc: P3:Lcol:Feature 9 | citation: [17] A. Minato, K. Suzuki, K. Tamao, J. Am. Chem. Soc. 109 (1987) 1257 | textual_function: Citation for the stepwise cross-coupling of aromatic dihalides using Ni reactivity selectivity, illustrated in eq. 5. | reason_severed: Eq. 5 references the stepwise dihalide coupling but provides no comparison with the full scope or selectivity data from [17]; only one dihalide substrate pair is shown. | affects_claims: medium — the selectivity feature for stepwise coupling is the application of the Ni > Pd reactivity claim; without engagement of [17]'s full scope, the generality of eq. 5 is unestablished. | symmetric_pattern: partial — [17] and [18] are both cited for stepwise/oligomer coupling but represent different products (dihalide stepwise vs. oligomers).

**C-12** | loc: P3:Rcol:Feature 10 | citation: [18] A. Minato, K. Suzuki, K. Tamao, M. Kumada, J. Chem. Soc. Chem. Commun. (1984) 511 | textual_function: Citation for mixed-oligomer synthesis, alongside [10b] for homo-oligomers. | reason_severed: Cited alongside [10b] for the oligomer synthesis feature; eq. 6 (homo-oligomer) is the only example shown, and no mixed-oligomer example from [18] is presented or compared. | affects_claims: medium — the claim of "first practical method for tailor-made synthesis of … mixed-oligomers" is unsubstantiated from the mini-review text; engagement with [18] data would be needed to evaluate it. | symmetric_pattern: partial — [10b] (homo-oligomers) and [18] (mixed-oligomers) cited for related but distinct structural targets.

---

### [U] Unclassified

**U-1** | loc: P2:Lcol:Feature 1 / Scheme 1 | quote: [REDACTED: substantial verbatim quotation; see Tier 9] | question: Does the 1972 communication [1] itself contain experimental evidence (kinetic measurements, intermediate trapping, isotope effects, radical-clock or crossover experiments) that the catalytic reaction proceeds through the discrete Ni(II)/Ni(0) two-electron intermediates of Scheme 1 rather than through a Ni(I)/Ni(III) or radical-chain manifold? | originating_agent: V2 (Q1, primary); V1 approaches via the prototype claim (Q12, partial) | severity: high | note: Cannot be classified as B (reporting_omission) because the paper is a mini-review of established chemistry, not a primary experimental report; the proposed cycle is presented as historical fact, not as a new result. Cannot be classified as A because the paper does not defer this question to future work — it presents Scheme 1 as resolved. Cannot be classified as C because [1] is the paper's own prior work, not an uncontinued external citation. The question is analytically critical: the mechanistic validity of Scheme 1 as a "prototype" rests on whether the elementary steps were experimentally grounded in [1] or constructed by analogy from stoichiometric Yamamoto chemistry. Self-contradictory absence note: the paper proposes Scheme 1 as an established mechanistic framework while citing no experimental evidence within this paper or from [1] that distinguishes the proposed ionic two-electron pathway from competing mechanisms.

**U-2** | loc: P2:Lcol:Feature 1 / Scheme 1 | quote: [REDACTED: substantial verbatim quotation; see Tier 9] | question: What documented evidence establishes that Pd cross-coupling workers explicitly adopted Scheme 1 as their mechanistic model rather than developing mechanistic proposals independently from Wilkinson, Collman, or other organometallic precedents? | originating_agent: V2 (Q2, primary); V3 (Q4, historiographic dimension); V1 (Q12, priority dimension) — convergence 3/3 on this root | severity: high | note: Cannot be classified as B because it is not a reporting omission of a standard datum; the claim is a positive historiographic assertion. Cannot be classified as A (no deferral). Cannot be classified as C because ref [11] is cited as evidence for the claim, not as a severed citation — though [11] is in fact insufficiently engaged to support it (C-6 records this separately). The prototype claim requires two distinct types of evidence that are both absent: (i) mechanistic — that Scheme 1's elementary steps were validated before adoption; (ii) historiographic — that citation to [1] in mechanistic Pd papers is documented. Both are absent; the claim rests on assertion of analogy. Note: U-1 and U-2 are linked (same conceptual root) but are independent U items because U-1 concerns the internal validity of Scheme 1 and U-2 concerns the external influence claim. Both are D-4 candidates.

**U-3** | loc: P2:Rcol:Feature 5 / eq. 3 | quote: [REDACTED: substantial verbatim quotation; see Tier 9] | question: Is the ligand-dependent isomerization (dppp: 96:4 primary:secondary; dmpe: 9:84) mechanistically consistent with β-hydride elimination/re-insertion (chain-walking), with Grignard pre-equilibration, or with a radical mechanism — and does the stronger σ-donor dmpe disfavoring isomerization to primary contradict the chain-walking model (where stronger donation should accelerate β-hydride elimination)? | originating_agent: V2 (Q3, Q11, primary); V1 (Q3, partial — yield side) | severity: high | note: Cannot be classified as B because the isomerization phenomenon is reported (not omitted); the unasked question is about its mechanistic attribution, not a missing datum. Cannot be classified as A because the paper does not acknowledge or defer this mechanistic ambiguity. Cannot be classified as C because [13a,b] are cited (though not substantively engaged — recorded as C-8). The apparent reversal of the expected ligand-dependence (stronger σ-donor dmpe disfavors isomerization to primary, where chain-walking predicts the opposite) is a potential self-contradiction in the proposed mechanism that the paper does not acknowledge. Independent from U-1/U-2: concerns a different elementary step (the Ni–alkyl intermediate behavior) and a different substrate class (sec-alkyl Grignard reagents).

**U-4** | loc: P3:Lcol:Feature 9 | quote: [REDACTED: substantial verbatim quotation; see Tier 9] | question: The Ni > Pd reactivity order inverts the expected oxidative addition reactivity trend for ArCl substrates (Pd(0) is generally more electrophilic toward C–Cl than Ni(0) in isolation). What elementary step or combination of steps in the full catalytic cycle produces the overall higher turnover rate for Ni, and has this been measured kinetically? | originating_agent: V2 (Q9, primary; OV2 noting the inversion of expected trend); V1 (Q7, partial) | severity: high | note: Cannot be classified as B because it is not an omission of a reporting standard — it is a mechanistic question about a comparative claim. Cannot be classified as A (no deferral stated). Cannot be classified as C because [11] and [16] are cited but their specific kinetic data are not invoked and then dropped — rather, the paper makes a comparative claim that would require kinetic data to ground. The inversion of the typical ArCl oxidative addition trend is an analytically important tension: for Pd cross-coupling, ArI >> ArBr >> ArCl, which implies that the Ni > Pd preference for ArCl is not simply due to faster oxidative addition at Ni, and an alternative explanation (rate-limiting step difference, catalyst speciation, decomposition of Pd under ArCl conditions) is needed. | cross_field_temperature: V1=medium, V2=high — convergence 2/3, temperature_gap: low.

**U-5** | loc: P3:Lcol:Feature 7 | quote: [REDACTED: substantial verbatim quotation; see Tier 9] | question: Given that C(sp²)–F bonds (BDE ~125 kcal/mol) require exceptional activation, is oxidative addition of ArF to Ni(0) the rate-limiting step here, and what activation barrier or kinetic measurement, if any, has been reported? The paper provides no conditions, no yield, no rate data, and no citation for the ArF claim. | originating_agent: V2 (Q7, primary); V1 (Q4, reporting-omission dimension) | severity: medium | note: V1-Q4 records the reporting omission (B-4). U-5 is independent: the mechanistic question is why an ArF reaction occurs at all at Ni(0) — the self-contradictory absence is that the paper's own scope framework (feature 7: [REDACTED: substantial verbatim quotation; see Tier 9]) predicts ArF would be unreactive, yet the paper simultaneously states ArF reacts (with low reactivity). The paper does not explain the mechanistic basis for this scope exception. B-4 and U-5 are complementary (B-4 = reporting omission, U-5 = unexplained scope exception within the paper's own reactivity framework).

**U-6** | loc: P1:Lcol:Section 1, opening / P3:Rcol:Section 3 / Fig. 2 | quote: [REDACTED: substantial verbatim quotation; see Tier 9] | question: On what documented archival evidence — submission dates, correspondence records, notebook entries, or independent historiographic analysis — is the independence of the two 1972 discoveries established? The "generally recognized" framing is sociological assertion, not documented fact; no submission/acceptance dates for [1] or [2] are given. | originating_agent: V3 (Q1, primary) | severity: medium | note: Cannot be classified as B (no reporting omission of a standard methodological datum — this is a priority claim). Cannot be classified as A (no deferral). Cannot be classified as C ([2] is cited but with a fully stated function — announcing simultaneous discovery; the question is not about whether [2] was engaged but about the evidentiary basis for the independence claim). The question is analytically important because the independent co-discovery narrative is the paper's first substantive claim, and its foundation is archival, not experimental.

**U-7** | loc: P1:Rcol:Section 1 | quote: [REDACTED: substantial verbatim quotation; see Tier 9] | question: Ref [9] (Kiso, Kumada, Maeda, Sumitani, Tamao, J. Organomet. Chem. 50 (1973) 311) was published in 1973, one year after the discovery communication [1] (1972). The mini-review frames this Ni(0)-ethylene complex work as a causal precursor to the 1972 discovery, but if [9] documents work conducted in 1970–1971, its 1973 publication date means the narrative rests on the assumption that [9] is retrospective documentation of pre-1972 experiments. Is there archival evidence (laboratory notebooks, internal reports) confirming that the Ni(0)-ethylene complex preparation occurred before October 1971? | originating_agent: V3 (Q6, primary); V2 (Q10, mechanistic dimension); V3-OV3 (historiographic dimension) | severity: medium | note: Cannot be classified as B, A, or C for the same structural reasons as U-6 — this is a chronological evidence question about the discovery narrative. U-7 is independent from U-6 (U-6 concerns independent co-discovery; U-7 concerns the internal chronological sequencing of the Kumada group's own pre-discovery work). Self-contradictory absence note: the paper's causal narrative asserts that Sumitani's Ni(0) work (published 1973 as [9]) enabled the 1972 discovery, but [9]'s publication date makes this causal claim non-verifiable from published literature alone.

**U-8** | loc: P2:Rcol:Feature 4 / eq. 2 | quote: [REDACTED: substantial verbatim quotation; see Tier 9] | question: The suppression of β-hydride elimination in Ni(n-Bu)(Ar)(dppp) intermediates that underlies this selectivity claim requires that the rate of reductive elimination exceeds the rate of β-hydride elimination under reaction conditions. What is the kinetic basis for this rate ordering, and what activation parameters (ΔH‡, ΔS‡) or competition experiments establish it? | originating_agent: V2 (Q4, primary) | severity: high | note: B-2 records the reporting omission (yield basis missing). U-8 is independent and not absorbed by B-2: where B-2 concerns missing quantitative reporting, U-8 concerns the mechanistic prerequisite for the paper's "most significant feature" claim. Self-contradictory absence: the paper claims this selectivity is attained "by the nickel–phosphine molecular catalysis" — implying that the phosphine ligand is mechanistically responsible for suppressing β-hydride elimination — but no kinetic or mechanistic evidence is cited that attributes the selectivity to any specific feature of the Ni–phosphine system. This is a self-contradictory absence because the paper's own causal attribution (phosphine catalysis enables selective cross-coupling) predicts that a mechanistic explanation would be available, yet none is provided. | linked_to: B-2 (same passage, different analytical angle; B-2 and U-8 are complementary per the B/U dual-classification protocol).

---

## Step 4: META

```
[META]
  linked_items:
    - B-2 ↔ U-8: same passage (eq. 2 / feature 4); B-2 = reporting omission (yield basis); U-8 = mechanistic prerequisite (β-hydride suppression kinetics); complementary, not mutually exclusive
    - B-4 ↔ U-5: same passage (fluorobenzene / feature 7); B-4 = reporting omission (no conditions/yield cited); U-5 = self-contradictory scope exception (paper's reactivity framework predicts ArF unreactive, yet ArF reacts)
    - U-1 ↔ U-2: linked but independent; U-1 = internal validity of Scheme 1 elementary steps; U-2 = external prototype/influence claim; both D-4 candidates
    - U-1 ↔ C-6: C-6 records the severed engagement with [11] that would be needed to support U-2; U-1 addresses the prior mechanistic validation question
    - U-3 ↔ B-3: B-3 = yield omission in eq. 3; U-3 = mechanistic question about isomerization pathway and apparent ligand-dependence reversal; independent
    - U-4 ↔ B-5 (partial): both concern the Ni > Pd reactivity claim, but B-5 records the industrial claim's unverifiable citation, while U-4 is the mechanistic basis for the reactivity comparison
    - U-7 ↔ C-5: C-5 records the chronological complexity of [9]'s citation function; U-7 asks the archival question about whether [9] represents retrospective publication of pre-1972 work

  same_root_groups:
    - SRG-1 [Catalytic cycle elementary-step evidence absent]: U-1, U-2, U-8, V2-Q10 (absorbed into U-7 context). These items all derive from the same underlying data absence: no experimental evidence from [1] or any cited paper establishes that the Ni(II)/Ni(0) two-electron cycle operates under catalytic conditions rather than alternative manifolds.
    - SRG-2 [Mechanistic attribution of isomerization pathway]: U-3, B-3. These items derive from the same absent data: no mechanistic characterization of the sec-to-primary isomerization pathway is provided, and the reported ligand-dependence may contradict the chain-walking model.
    - SRG-3 [Prototype/influence claim — priority, mechanism, bibliometrics]: U-2, C-6, V3-Q4 (absorbed into U-2 note). These items derive from the same absent data: no systematic citation analysis or mechanistic lineage documentation supports the prototype claim.
    - SRG-4 [Citation-trend data reliability]: B-8, U-6 (partial). These items derive from the same absent data: Fig. 2 citation methodology is unspecified, and the independent co-discovery claim similarly lacks archival documentation. Note: B-8 concerns Fig. 2 bibliometrics; U-6 concerns the independence claim — they are in the same SRG because both are historiographic/bibliometric claims lacking methodological grounding.
    - SRG-5 [Ni > Pd reactivity comparison — quantitative basis absent]: U-4, C-10, B-5 (partial). These items derive from the same absent data: no kinetic measurement or competition experiment grounds the Ni > Pd reactivity comparison.
    - SRG-6 [Reporting completeness of scope equations]: B-1, B-2, B-3, B-4, B-6, B-7. These items derive from the same absent data class: across features 3–8 in Section 2, quantitative claims are presented without measurement basis, experimental conditions, or primary data citations.
    - SRG-7 [Discovery narrative — retrospective reconstruction vs. contemporaneous documentation]: U-6, U-7, C-5. These items derive from the same absent data: the chronological discovery narrative rests on retrospective recollection without archival corroboration, and at least one cited reference ([9]) was published after the discovery it is used to support.

  symmetric_citations:
    - C-1, C-2, C-3: symmetric group — refs [4], [5], [6] all cited in the parallel three-type σ-organonickel inventory list, cited-and-dropped at identical depth
    - C-9: internal symmetry — refs [14a–d] all cited-and-dropped for asymmetric coupling existence proof

  unreported_data:
    - Conditions and yield for fluorobenzene cross-coupling reaction (B-4/U-5)
    - E:Z ratios and substrate scope for stereoretentive alkenyl halide coupling (B-6)
    - Yield data for isomer-ratio entries in eq. 3 (B-3)
    - Activity order entries for Ni(dmpe)Cl₂ and Ni(dmpf)Cl₂ in catalytic cross-coupling (B-1)
    - Mass balance / byproduct profile for eq. 2 (80% yield; B-2)
    - Chain-length selectivity data for oligothiophene synthesis eq. 6 (B-7)
    - Database source, search date, and self-citation protocol for Fig. 2 (B-8)

  series_signal: yes — inference label: special-volume companion articles. The reference list contains multiple companion articles in the same J. Organomet. Chem. special volume with placeholder page numbers: [8b] Yamamoto companion, [11b] Murahashi companion, [14d] Hayashi companion, [15] Banno companion, [16d] Negishi companion. These are not published at the time of submission and represent a coordinated retrospective series on cross-coupling discovery, not a prospective research series. The pattern indicates that several unresolved citation-engagement issues (C-5/[9], C-6/[11b], C-9/[14d], C-10/[16d]) may be partially addressed in companion articles that are not available to the reader at submission date. Series signal affects: C-5 (Yamamoto/Ni(0) mechanism), C-6 (Murahashi/Pd prototype), C-9 (Hayashi/asymmetric), C-10 (Negishi/Pd).
```

---

## Step 5: GAP

```
[GAP]
GAP-1 | type: 1 | priority: high | description: The 1972 communication [1] (K. Tamao, K. Sumitani, M. Kumada, J. Am. Chem. Soc. 94 (1972) 4374) is cited throughout but never substantively engaged; it is the paper that would answer U-1 (whether the original communication contained mechanistic evidence for the Ni(II)/Ni(0) cycle) and also bears on U-2. | candidate_paper: Tamao, Sumitani, Kumada, J. Am. Chem. Soc. 94 (1972) 4374 | inference_label: T1 | status: pending

GAP-2 | type: 1 | priority: high | description: The 1976 full paper [10a] (K. Tamao et al., Bull. Chem. Soc. Jpn. 49 (1976) 1958) and 1972 sec-alkyl mechanistic paper [13a] (J. Am. Chem. Soc. 94 (1972) 9268) would answer U-3 (isomerization mechanism) and partially U-1. | candidate_paper: Tamao et al. BCSJ 49 (1976) 1958; Tamao, Kiso, Sumitani, Kumada, JACS 94 (1972) 9268 | inference_label: T1 | status: pending

GAP-3 | type: 1 | priority: high | description: Ref [9] (Kiso, Kumada, Maeda, Sumitani, Tamao, J. Organomet. Chem. 50 (1973) 311) is needed to resolve U-7 — whether the Ni(0)-ethylene complex preparation documented in [9] reflects pre-1972 work or post-discovery retrospective publication. | candidate_paper: Kiso, Kumada et al., J. Organomet. Chem. 50 (1973) 311 | inference_label: T1 | status: pending

GAP-4 | type: 1 | priority: medium | description: Ref [11a] (Yamamura, Murahashi, Moritani, J. Organomet. Chem. 91 (1975) C39) is needed to determine whether the first palladium cross-coupling paper explicitly cited [1] as its mechanistic model (U-2, C-6). | candidate_paper: Yamamura, Murahashi, Moritani, J. Organomet. Chem. 91 (1975) C39 | inference_label: T1 | status: pending

GAP-5 | type: 2 | priority: high | description: By 2001, substantial mechanistic work on Ni- and Pd-catalyzed cross-coupling had been published (e.g., Amatore and Jutand on Pd oxidative addition; Negishi on transmetallation; later Knochel and Fürstner on Ni mechanisms). These contemporaries would address U-1, U-4, and V2-Q3/V2-Q4 but are not cited in this 2001 mini-review. | candidate_paper: Amatore, Jutand (Pd OA/RE kinetics, 1991–2000); Negishi mechanistic reviews (1982–2001); Knochel Ni cross-coupling mechanism papers | inference_label: T2 | status: pending

GAP-6 | type: 2 | priority: medium | description: The Corriu–Masse 1972 paper [2] (Chem. Commun. (1972) 144) would allow independent verification of the simultaneous independent discovery claim (U-6) — specifically, whether [2]'s submission date and intellectual context corroborate independence. | candidate_paper: Corriu, Masse, Chem. Commun. (1972) 144 | inference_label: T1 | status: pending

GAP-7 | type: 3 | priority: high | description: A systematic citation analysis of mechanistic Pd cross-coupling papers (1975–2001) citing [1] would answer U-2 (whether Scheme 1 was adopted as a mechanistic prototype by Pd workers, or whether Pd mechanistic proposals were independently developed from Wilkinson/Collman precedents). No such analysis exists in this paper; a historiometric study would be required. | candidate_paper: Systematic review: cross-coupling mechanism papers 1975–2001 — mechanistic lineage from Ni [1] vs. independent Pd development | inference_label: T3 | status: pending
```

---

## Classification summary

**A items:** 0
**B items:** 8 (B-1 through B-8)
**C items:** 12 (C-1 through C-12)
**U items:** 8 (U-1 through U-8)
**SRG count:** 7 (SRG-1 through SRG-7)

---

## [TEMPERATURE_SUMMARY]

```
[TEMPERATURE_SUMMARY]

high_convergence_high_gap:
  - B-8 / V1-Q11 + V3-OV1: convergence 2/3, temperature_gap medium (V1=low, V3=high)
  - U-2 / V1-Q12 + V2-OV1 + V3-OV2: convergence 3/3, temperature_gap medium (V1=low, V2=high, V3=medium)

high_convergence_low_gap:
  - B-3 / V1-Q3 + V2-OV3: convergence 2/3, temperature_gap none (V1=medium, V2=medium)
  - B-6 / V1-Q6 + V2-OV4: convergence 2/3, temperature_gap none (V1=medium, V2=medium)
  - U-4 / V1-Q7 + V2-OV2: convergence 2/3, temperature_gap low (V1=medium, V2=high)
  - U-7 / V2-Q10 + V3-OV3: convergence 2/3, temperature_gap none (V2=medium, V3=medium)

low_convergence_high_gap:
  - U-1 / V2-Q1: convergence 1/3, severity=high from V2 (no V1 or V3 direct overlap at this specific formulation)
  - U-3 / V2-Q3+Q11: convergence 1/3 (V2 only on isomerization mechanism), severity=high from V2
  - U-8 / V2-Q4: convergence 1/3, severity=high from V2

Note: high_convergence_high_gap is non-empty for this paper; U-2 (3/3 convergence, medium gap) and B-8 (2/3, medium gap) are the primary high-convergence high-gap items. U-1, U-3, and U-8 are low-convergence high-gap and should be treated as D-4 candidates via the standard fallback path (single high-severity agent).
```

---

inference_time_sec: not available — inject externally

---

> **Tier 8 redaction notice**: This file is a redacted copy of the corresponding Tier 3 / Tier 9 output. Verbatim source-paper quotations have been replaced by `[REDACTED: see source paper §<loc>; full text retained in Tier 9 reviewer-only deposit]` markers, preserving location references and our own analytical content. Bibliographic fields (title, authors, journal, year, DOI), analytical labels (`evidence_chain:` with B-/U-/A-/C- internal IDs), short technical terms, and our own analytical text are not redacted. The redaction was applied by `scripts/redact_for_tier8.py` and, for this version, by `scripts/build_paperA_R1_public.py` with `scripts/redact_source_ngram_runs.py` (scripts of the project repository; they are not deposited).
