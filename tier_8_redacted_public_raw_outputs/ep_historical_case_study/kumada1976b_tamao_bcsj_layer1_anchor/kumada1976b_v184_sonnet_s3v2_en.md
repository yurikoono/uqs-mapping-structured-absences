prompt_version: stage3-v2-en-20260419
model_info: claude-sonnet-4-6

# Re-certification Assessment Sheet for Scientific Knowledge

## Tamao, Sumitani, Kiso, Zembayashi, Fujioka, Kodama, Nakajima, Minato, and Kumada 1976 (Bulletin of the Chemical Society of Japan, full_paper)

---

### §1 Claim Architecture

**Core claim summary:**

The paper's central claim is that dihalodiphosphinenickel(II) complexes — optimally [Ni(dppp)Cl₂] — constitute a broadly applicable, catalytically practical C–C cross-coupling platform for Grignard reagents (alkyl, aryl, alkenyl, including β-hydrogen-bearing alkyl) with C(sp²)-halides (aryl and alkenyl) under mild conditions, with high yields and high isomeric purity across approximately sixty substrate combinations. The **Novelty pillar** rests on two components: (a) the first comprehensive scope-and-limitations survey of a Ni-phosphine catalyzed Grignard cross-coupling, expanding the 1972 communications into a systematic characterization of substrate breadth and failure modes; and (b) a priority claim for the first C–F oxidative addition to a transition metal complex. The **Utility pillar** rests on the demonstration that the system operates with catalytic metal loading under mild ether reflux, giving products of high isomeric purity without the stoichiometric metal requirements of organocuprates or the selectivity failures of unmodified Kharasch systems.

**Layered structure:**

The paper's claims form an independent-layer architecture rather than a single fragile tower. As established in D-1:

- **Layer 1 (Scope claim):** Broad applicability to ~60 Grignard/halide combinations (Tables 6–7). This layer stands on its own quantitative GLPC database. Its primary vulnerability is the evidentiary reliability of the GLPC yield basis (SRG-2).
- **Layer 2 (Mechanistic rationalization / Scheme 1):** The Ni(II)/Ni(0)/Ni(II) catalytic cycle is offered as a post-hoc rationalization. This layer is explicitly labeled "A Brief Comment on the Mechanism" and does not claim proof. Single refutation of the crossover-experiment gap (SRG-1/CLA-1) does not collapse Layer 1.
- **Layer 3 (Priority claim / C–F oxidative addition):** The fluorobenzene coupling claim (SRG-3) is structurally isolated from both Layer 1 and Layer 2 — its evidentiary failure does not collapse the general scope claim.
- **Layer 4 (β-hydride suppression):** The claim that β-hydrogen-bearing alkyl Grignard reagents give selective cross-coupling without β-hydride elimination (CLA-2) is presented as a remarkable mechanistic feature of the scope claim. Its refutation would not remove the observed yields from Tables 6–7 but would revise the mechanistic interpretation.

Inter-layer dependencies: Layer 2 depends on Layer 1 for its data input (product distributions rationalized by Scheme 1). Layer 3 depends on the analytical methods of Layer 1 (GLPC), but its co-elution problem (B-3/SRG-3) makes it analytically independent in a negative sense — the PhF result is the weakest-supported entry in the Layer 1 database. Layers 1 and 3 share an evidentiary vulnerability in SRG-2 (GLPC yield-basis integrity). A single refutation at Layer 3 (PhF claim) does not collapse Layers 1, 2, or 4.

---

### §2 SRG / CLA → RI / ER / EP Crosswalk

#### SRGs from Stage 1

---

**SRG-1 [Catalytic cycle elementary steps — kinetic and spectroscopic evidence absent]**

Members: A-1, A-1d, U-1, U-2, C-7

* **Primary RI:** RI-03 [Unobserved explanatory]
* **Secondary RI:** RI-06 [Imported model] (the Ni(II)/Ni(0)/Ni(II) cycle is constructed from stoichiometric organonickel precedent in Jolly-Wilke, ref. 31, and from Tamura-Kochi iron/copper chemistry, imported without isomorphism demonstration for the Ni-phosphine catalytic system); RI-04 [Unreplicated discriminator] (the anomalous reactivity order PhI>PhCl>PhBr with [Ni(dppp)Cl₂] versus normal order with [Ni(dppe)Cl₂] is interpreted as evidence for "two or more rate-limiting steps" from a single qualitative dataset, without replicate rate measurements)
* **ER:** For the mechanistic narrative of Scheme 1 to constitute an evidentially grounded claim rather than a rationalization, at least one elementary step of the Ni(II)/Ni(0)/Ni(II) cycle must be independently verified through direct observation of an intermediate (e.g., ³¹P NMR of the diorganonickel complex 2 or the haloorganonickel complex 3 under catalytic conditions) or through a mechanistic probe experiment (crossover experiment with two Grignard reagents and two halides) that distinguishes the Scheme 1 product distribution prediction from that of the competing Felkin-Corriu Ni(0) oxidative-addition mechanism.
* **EP:** EP-03a [Direct-observation / state-assignment pack]; EP-04a [Discrimination / replication pack]
* **Case-specific implementation:** (EP-03a) In situ ³¹P{¹H} NMR monitoring of [Ni(dppp)Cl₂] + n-BuMgBr in Et₂O at room temperature to identify and characterize the yellow species that the aging experiment (Table 2) demonstrates is catalytically competent over 16 h — if this species is [Ni(dppp)(n-Bu)₂], its identification as the resting state would directly support Scheme 1 step 1→2; UV-vis or EPR would supplement to exclude Ni(I) radical species. (EP-04a) Crossover experiment: combine PhMgBr + n-BuMgBr + PhCl + vinyl chloride with [Ni(dppp)Cl₂]; if Scheme 1 operates, the cross-products (Ph-Ph, Bu-vinyl, Ph-vinyl, Bu-Ph) should appear in a non-statistical distribution reflecting sequential diorganonickel formation; the Felkin-Corriu Ni(0) pathway predicts a different statistical pattern.
* **Notes:** SRG-1 is the largest member group and corresponds to the mechanistic core of the paper. U-2 (anomalous reactivity order) is a self-contradictory absence: Scheme 1 predicts oxidative addition rate scales with C–X bond strength (normal order PhBr>PhCl>PhF), but [Ni(dppp)Cl₂] gives PhI>PhCl>PhBr. The paper labels this "difficult to explain" rather than acknowledging it as internal tension with Scheme 1. C-7 (Felkin-Corriu acknowledgment) documents the competing mechanism without experimental exclusion. Position in TEMPERATURE_SUMMARY: U-1 (low_convergence_high_gap, V2=high); U-2 (low_convergence_high_gap, V2=high, V1=medium; temperature_gap=low); A-1 (single-agent V2=high deferred mechanistic question). RI-03 primary because the diorganonickel intermediates central to the explanation are neither directly observed nor kinetically constrained — the yellow species of Table 2 is the closest in-paper evidence but is characterized only by color. RI-06 secondary because Scheme 1 is explicitly assembled from Jolly-Wilke authority citation (ref. 31) for its two premises, without stoichiometric control experiments in the present system.

---

**SRG-2 [Quantitative GLPC yield-basis integrity across the substrate scope]**

Members: B-1, B-2, B-10, B-5

* **Primary RI:** RI-01 [Reporting integrity]
* **Secondary RI:** RI-08 [Unquantified reliability] (no replicate yield measurements are provided for any scope entry; Table 2 contains a mass balance violation of 104% that is unacknowledged)
* **ER:** For the catalytic activity rankings (Table 1), aging stability conclusions (Table 2), and scope yield claims (Tables 6–7) to be reproducible and comparable across the ~60-entry dataset, FID response factors must be documented for each structurally distinct product class vs. the internal standard (mesitylene or normal alkane), and mass balance must be verified and closed for at least the key comparison entries; yield denominators (halide-based vs. Grignard-based) and yield bases (isolated vs. GLPC) must be consistently reported or reconciled.
* **EP:** EP-01a [Reporting-coherence pack]; EP-08a [Replication / uncertainty pack]
* **Case-specific implementation:** (EP-01a) Report FID response factors for representative products in each structural class: alkylbenzene (n-butylbenzene vs. mesitylene), silylmethyl arene (benzyltrimethylsilane vs. mesitylene), cyclopropyl product (cyclopropylbenzene vs. mesitylene), and internal olefin ((E)-stilbene vs. mesitylene) — these four classes span the structural diversity of the ~60-entry scope; demonstrate that the single Silicone DC 550 column resolves each product from its nearest structural isomers (e.g., sec-butylbenzene from n-butylbenzene, (E)- from (Z)-stilbene) by reporting peak-to-valley ratios or resolution factors; reconcile the Table 2 entry that sums to 104% (69% butylbenzene + 35% benzene). (EP-08a) Report replicate GLPC measurements (n ≥ 3) for the Table 1 reference reaction ([Ni(dppp)Cl₂], n-BuMgBr, PhCl) and at least one Table 7 entry per catalyst type, with standard deviations; close mass balance for these representative entries by accounting for all GLPC-detectable components.
* **Notes:** SRG-2 is the shared evidentiary foundation beneath all the paper's quantitative claims. Its deficiencies do not individually collapse any single scope entry but collectively reduce the Layer 1 scope database to order-of-magnitude reliability. The internal standard identity discrepancy (mesitylene documented for Table 1 footnote b; "normal alkane" for Procedure A; unspecified for Tables 6–7) is a reporting-coherence violation (RI-01) independent from the response factor question. Position in TEMPERATURE_SUMMARY: B-1 (high_convergence_low_gap, V1=medium, V3=high; convergence=2/3; temperature_gap=low); B-2 and B-5 (high_convergence_low_gap, V1=medium, V3=medium; convergence=2/3; temperature_gap=none).

---

**SRG-3 [Analytical inconsistency in halobenzene reactivity — PhF co-elution]**

Members: B-3, U-5, A-6

* **Primary RI:** RI-02 [Object identification]
* **Secondary RI:** RI-04 [Unreplicated discriminator] (the competitive experiment conversion values of 24–26% for PhF in Table 4, obtained by an undocumented analytical modification, are the sole quantitative support for a landmark "first C–F oxidative addition" claim)
* **ER:** For the fluorobenzene coupling claim to constitute an established result — let alone a "first reported" C–F oxidative addition to a transition metal — the product (butylbenzene from PhF + n-BuMgBr) must be isolated, weighed, and characterized by NMR and mass spectrum; the co-elution of C₆H₅F and benzene on Silicone DC 550 must be resolved by documenting a different column, temperature program, or calculation approach that permits independent determination of PhF conversion and butylbenzene yield; alternatively, preparative scale isolation on the 5 mmol scale would bypass the GLPC resolution problem entirely.
* **EP:** EP-02a [Identity / purity substantiation pack]; EP-04a [Discrimination / replication pack]
* **Case-specific implementation:** (EP-02a) Isolate butylbenzene from PhF + n-BuMgBr + [Ni(dppp)Cl₂] on a preparative scale (≥5 mmol PhF); report isolated yield based on PhF charged; confirm identity by ¹H NMR comparison with authentic sample and mass spectrum (parent m/e 134, base peak m/e 91, absence of m/e 105 for sec-butylbenzene — the same protocol applied to butylbenzene in Procedure C(a)); this single isolation experiment would simultaneously resolve the co-elution problem (no GLPC needed if isolated yield is reported) and establish the landmark claim on the same evidentiary level as the strongest entries in Table 7. (EP-04a) Run three replicate competitive experiments (PhF vs. PhCl vs. n-BuMgBr, [Ni(dppp)Cl₂]) under identical conditions with independent GLPC analysis for each replicate, documenting column, temperature, and calculation method that resolves the co-elution; the three-run replication already present in Table 4 (runs 1/2/3: 24/26/— for PhF) demonstrates the right structure but lacks the analytical documentation.
* **Notes:** SRG-3 is a self-contradictory absence cluster: the landmark claim (C–F oxidative addition "not yet reported") is asserted in the same paper that explicitly acknowledges the analytical inaccessibility of the PhF result by single-substrate GLPC. The paper uses competitive-experiment conversions as a proxy without explaining how the co-elution problem is resolved in the competitive setup. This is Fatal to the landmark claim at VQ-1 (product identity not established for PhF coupling product; isolated yield is zero). Position in TEMPERATURE_SUMMARY: U-5 (low_convergence_high_gap, V1=high + V3=high, convergence=2/3, temperature_gap=none); B-3 (high_convergence_low_gap, V1=high, V3=high, convergence=2/3, temperature_gap=none). RI-02 primary because the coupling product's identity and yield for the PhF reaction are not established at a granularity that excludes the possibility that the competitive-experiment conversions reflect preferential PhCl consumption with PhF co-detection via the unresolved GLPC peak.

---

**SRG-4 [Mg-specific mechanistic localization — unpublished organolithium failure as sole evidence]**

Members: A-5, C-5

* **Primary RI:** RI-03 [Unobserved explanatory]
* **Secondary RI:** RI-07 [Unsupported boundary] (the assertion [REDACTED: substantial verbatim quotation; see Tier 9] implies a specific mechanistic boundary — Mg is necessary, Li is insufficient — without a positive test or failure-mode characterization)
* **ER:** For the inference that magnesium moieties specifically enable the selective cross-coupling to be mechanistically grounded, the organolithium failure experiments must be conducted within an accessible publication (or within this paper) with full experimental details (which RLi reagents were tested, with which Ni-phosphine catalysts, under what conditions, and what products formed), and the specific elementary step of Scheme 1 that requires Mg (most plausibly the transmetalation step) must be localized through at least one stoichiometric model reaction comparing MgX vs. Li in that step.
* **EP:** EP-03a [Direct-observation / state-assignment pack]; EP-06a [Analogy-validation pack]
* **Case-specific implementation:** (EP-03a) Perform stoichiometric transmetalation experiments: react [Ni(dppp)(Ph)(Cl)] (complex 3 of Scheme 1) separately with n-BuMgBr and n-BuLi under identical conditions and quantify product formation by ¹H NMR; if only the Grignard version gives [Ni(dppp)(Ph)(n-Bu)] (complex 4), this localizes the Mg requirement to the transmetalation step and distinguishes Scheme 1 from the Felkin-Corriu Ni(0) oxidative-addition mechanism (where Li vs. Mg substitution would affect the oxidative-addition step rather than transmetalation). (EP-06a) Compare the organolithium failure with the published organocopper analogy: stoichiometric cuprate transmetalation is also sensitive to metal identity; document whether the Mg-specific effect in the Ni system is mechanistically analogous to or distinct from the Mg-specific transmetalation efficiency documented in the Tamura-Kochi Fe/Cu Grignard coupling studies (refs. 15–17).
* **Notes:** Ref. 48 is explicitly "unpublished observations," making the sole mechanistic localization evidence inaccessible. U-1 overlaps with SRG-4 because the Mg-role inference is also relevant to the Scheme 1 vs. Felkin-Corriu distinction. Position in TEMPERATURE_SUMMARY: A-5 (low_convergence_high_gap, V2=high, V1=medium; temperature_gap=low). Non-fatal to the overall scope claim (Layer 1) but fatal to the Mg-mechanistic inference as currently stated.

---

**SRG-5 [Stereospecificity of vinylic coupling — Z:E assignment basis and mechanistic interpretation absent]**

Members: A-4, B-8

* **Primary RI:** RI-05 [Qualitative overread]
* **Secondary RI:** RI-01 [Reporting integrity] (the Z:E ratios are stated without specifying the assignment method — GLPC resolution or ¹H NMR J coupling — which prevents independent verification)
* **ER:** For the Z:E ratios (90:10 from (Z)-ClCH=CHCl; 80:20 from (E)-ClCH=CHCl; reported in Table 7 for stilbene products) to constitute a valid stereospecificity claim, the assignment method must be documented (¹H NMR coupling constants: J ~ 16 Hz for (E)-stilbene, J ~ 12 Hz for (Z)-stilbene would be unambiguous; or GC resolution data demonstrating baseline separation of (E)- and (Z)-stilbene on Silicone DC 550); and the mechanistic step controlling stereospecificity (retention at oxidative addition, vinyl-Ni isomerization, or thermodynamic equilibration of the vinylic Ni intermediate) must be attributed.
* **EP:** EP-05a [Quantitative-ranking substantiation pack]; EP-01a [Reporting-coherence pack]
* **Case-specific implementation:** (EP-05a) Report ¹H NMR coupling constants (J values) for the vinyl H in each stilbene product isolated from (Z)- and (E)-ClCH=CHCl + PhMgBr + [Ni(dppp)Cl₂]; (E)-stilbene: J ~ 16 Hz (trans); (Z)-stilbene: J ~ 12 Hz (cis) — these values are diagnostic and available from the HA-100 spectrometer listed in the Experimental; this single measurement converts the unverifiable "Z:E=90:10" entry to a documentable assignment with no additional synthesis required. (EP-01a) Add a footnote to Table 7 specifying the assignment method for each Z:E entry (by NMR J coupling or by GLPC comparison with authentic stilbene samples); document which internal standard and column temperature program was used for geometric isomer separation if GC-based assignment is claimed.
* **Notes:** Three-agent convergence (V1=medium, V2=medium, V3=medium; convergence=3/3; temperature_gap=none) — this is the highest-confidence item in the dataset by convergence metric, though moderate in individual severity. The deferral to ref. 26 (Tamao et al., Chem. Lett., 1974, 1363) and to "more detail elsewhere" is an explicit A-item (A-4); the reporting omission in Table 7 (B-8) is an independent co-problem. RI-05 primary because the Z:E ratio values themselves are derived from a qualitative GLPC peak assignment (if GC-based) without documented resolution, and the mechanistic implication — [REDACTED: substantial verbatim quotation; see Tier 9] — is derived from the ratio numbers without the mechanistic attribution required to support it.

---

**SRG-6 [Dichloroethylene + alkyl Grignard — characterization of the major failure mode]**

Members: A-2, U-4

* **Primary RI:** RI-03 [Unobserved explanatory]
* **Secondary RI:** RI-07 [Unsupported boundary] (the characterization of this as "one of the most serious limitations" implies a negative boundary claim — alkyl Grignard reagents cannot give acceptable yields with dihaloethylenes — but no failure mechanism is proposed, and no alternative conditions are tested to probe the boundary)
* **ER:** For the "most serious limitation" identification to be mechanistically actionable, the by-product mixture from alkyl Grignard + 1,1- or 1,2-dichloroethylene must be characterized (product identity and yield distribution for all components: expected homo-coupling product R–R, possible β-hydride elimination product, possible mono-insertion product, and unreacted halide); and at least one mechanistic probe must be performed (e.g., using neopentylmagnesium chloride, a β-hydride-free alkyl Grignard, to test whether homo-coupling persists in the absence of the β-hydride pathway, thereby distinguishing double-transmetalation from β-elimination as the source).
* **EP:** EP-03a [Direct-observation / state-assignment pack]; EP-07a [Boundary-test pack]
* **Case-specific implementation:** (EP-03a) Fully characterize the "mixture of products[REDACTED: substantial verbatim quotation; see Tier 9]a complex mixture of products" but assigns no identity or yield to any component. (EP-07a) Test neopentylmagnesium chloride (NpMgCl, β-hydride-free primary alkyl) with (E)-ClCH=CHCl + [Ni(dppp)Cl₂]: if homo-coupling still predominates in the absence of β-hydride, the double-transmetalation pathway (fast second transmetalation relative to reductive elimination from the monovinyl-nickel intermediate) is implicated rather than β-elimination; this experiment would directly test whether β-hydride is the mechanistic root cause of the limitation.
* **Notes:** Both A-2 and U-4 carry high convergence (V1=high, V2=high; convergence=2/3; temperature_gap=none), making this the highest-severity confirmed item outside SRG-3. The identified failure is the paper's self-declared "most serious limitation," yet no structural characterization of the failure is provided. RI-03 primary because the mechanistic species responsible for the failure (whether it is the β-hydrogen-bearing nickel alkyl undergoing elimination, or the dialkylnickel intermediate undergoing reductive elimination preferentially) is not observed or kinetically constrained.

---

**SRG-7 [Non-optimized conditions — scope vs. conditions conflation]**

Members: B-5, B-14

* **Primary RI:** RI-01 [Reporting integrity]
* **ER:** For the ~60-entry substrate scope in Table 7 to constitute a valid scope survey (the paper's central deliverable), entries with notably low yields must be annotated to indicate whether conditions were optimized or defaulted to the standard protocol; yield denominators (halide-based vs. Grignard-based) and yield bases (isolated vs. GLPC-parenthetical) must be reconciled in a single legend; and the initial charge of gaseous reagents (vinyl chloride) must be documented for the small-scale entries (2.4–10 mmol) with the same rigor applied to the large-scale Procedure D.
* **EP:** EP-01a [Reporting-coherence pack]
* **Case-specific implementation:** Add a reconciliation table to Table 7 footnotes specifying for each entry: (a) yield base (isolated or GLPC), (b) yield denominator (halide or Grignard), (c) optimization status (standard conditions or best achieved); for entries with yields <30%, note whether a brief optimization scan was attempted (e.g., catalyst loading, solvent, temperature); for vinyl chloride entries at small scale, document the handling procedure (condensation volume, pressure monitoring) used to establish the initial charge.
* **Notes:** SRG-7 is non-fatal to the paper's scope claim if the reader understands the non-optimized disclaimer; however, it prevents use of Table 7 for structure-reactivity analysis because inherent substrate limitations cannot be distinguished from condition artifacts. B-14 (vinyl chloride gaseous reagent yield denominator) adds a specific methodological dimension to B-5's general disclaimer problem. Position in TEMPERATURE_SUMMARY: B-5 (high_convergence_low_gap, V1=medium, V3=medium; convergence=2/3; temperature_gap=none).

---

#### Outside the SRGs: CLAs

**CLA-1: Crossover experiment absent — Scheme 1 vs. Felkin-Corriu mechanically unresolvable**

* Grounded in: U-1 (Stage 1); not captured in SRG-1 member items because U-1 is a self-contradictory absence (Scheme 1 makes testable crossover predictions that are not tested), not a B or A item

* **Primary RI:** RI-04 [Unreplicated discriminator]
* **Secondary RI:** RI-03 [Unobserved explanatory]
* **ER:** For the claim that "diorganonickel intermediates are involved in this reaction" (Section V closing sentence) to be treated as an evidentially supported conclusion rather than an inference, a crossover experiment must be performed and reported.
* **EP:** EP-04a [Discrimination / replication pack]
* **Case-specific implementation:** Mix PhMgBr (1 equiv) + n-BuMgBr (1 equiv) + PhCl (1 equiv) + vinyl chloride (1 equiv) with [Ni(dppp)Cl₂] (0.01 equiv) in Et₂O; analyze product distribution after complete halide consumption by GC-MS: Scheme 1 (sequential transmetalation → diorganonickel → reductive elimination) predicts selective coupling of the two organics loaded onto Ni at a single turnover, yielding a specific cross-product distribution; Felkin-Corriu (oxidative addition of Grignard to Ni(0)) predicts a different product distribution if the oxidative addition order controls selectivity.
* **Notes:** U-1 is flagged as low_convergence_high_gap (V2=high, single agent). The self-contradictory absence structure: Scheme 1 explicitly predicts the existence of the diorganonickel intermediate (complex 4 in the scheme), and that intermediate's structure determines the cross-coupling selectivity — yet the one experiment that tests this prediction (crossover) is not performed. Directly tied to BI-level concern: without this experiment, the distinction between Scheme 1 and Felkin-Corriu is formally unresolvable from the paper's data.

---

**CLA-2: β-Hydride elimination suppression — olefin by-products not systematically detected**

* Grounded in: U-3 (Stage 1); B-9 (single-column GLPC not validated for volatile olefins)

* **Primary RI:** RI-05 [Qualitative overread]
* **Secondary RI:** RI-02 [Object identification] (absence of C4–C6 terminal olefin detection is not the same as absence of formation; the single Silicone DC 550 column at the stated conditions may not retain C4 olefins sufficiently for reliable quantification)
* **ER:** For the claim that alkyl Grignard reagents give selective cross-coupling because β-hydride elimination is suppressed (Section V "the most remarkable feature") to be evidentially supported, the GLPC analysis must demonstrate that 1-butene, 2-butenes, and propylene (from n-BuMgBr, n-PrMgBr) are absent at or below a stated detection limit; alternatively, the mechanistic argument must be reformulated to acknowledge that the observed high yield is consistent with rapid β-hydride elimination followed by equally rapid reinsertion ("chain-walking") without implying that elimination is absolutely suppressed.
* **EP:** EP-05a [Quantitative-ranking substantiation pack]; EP-02a [Identity / purity substantiation pack]
* **Case-specific implementation:** (EP-05a) Validate the Silicone DC 550 column for retention and quantification of 1-butene (bp −6 °C) and 2-butene (bp ~1–4 °C) by injection of authentic samples; if these olefins elute before the solvent peak or overlap with ether, switch to a more retentive column (e.g., squalane or Apiezon L) for the volatile olefin analysis; report the detection limit for butenes as a percentage of charged n-BuMgBr; if butenes are absent at ≤2% of charged Grignard, the "not detected" statement becomes quantitatively meaningful. (EP-02a) For the Table 7 entries using n-C₃H₇MgBr (propylene expected from β-hydride elimination) and c-C₆H₁₁MgBr (cyclohexene expected), search specifically for propylene and cyclohexene in the post-hydrolysis organic layer by GC headspace analysis.
* **Notes:** U-3 medium severity (V2 only). The paper's mechanistic narrative in Section V invokes β-hydride suppression as the mechanistic explanation for the utility of alkyl Grignard reagents — making this CLA relevant to the Utility pillar of the core claim. Non-fatal to Layer 1 (the scope yields stand regardless of the mechanistic interpretation), but this absence qualifies the mechanistic conclusion at VQ-3 (see §3).

---

### §3 Current VQ assessment

**Current judgment: VQ-2 (Method) — qualified**

---

**VQ-1 [Observation] — Fails for SRG-3; Passes for all other SRGs**

- **SRG-3 (PhF coupling):** VQ-1 **fails**. RI-02 is **Fatal** for the landmark claim. The coupling product (butylbenzene from PhF + n-BuMgBr) is not established at VQ-1: no isolated yield, no product identification, and no verified analytical method for conversion determination is provided for single-substrate PhF experiments. The competitive-experiment conversions (24–26% in Table 4) are obtained by an undocumented analytical modification of the very GLPC method declared inapplicable in Table 3. The landmark C–F oxidative addition claim cannot survive VQ-1 certification.

- **All other SRGs (SRG-1, SRG-2, SRG-4, SRG-5, SRG-6, SRG-7; CLA-1, CLA-2):** VQ-1 **passes** conditionally. For the general scope claim (Layer 1), product identity is established by NMR and/or IR comparison with authentic samples or literature data for the majority of entries; the key benchmark product (butylbenzene) is confirmed by mass spectrum (m/e 134, base peak m/e 91, no m/e 105). RI-02 is **Non-fatal** for the general scope claim — the GLPC response factor concerns (SRG-2) reduce quantitative precision but do not eliminate product identity for entries with isolated yields. The Table 2 mass balance violation (B-2, 104%) is **Non-fatal** because it affects one aging entry rather than the central scope claim entries of Tables 6–7.

---

**VQ-2 [Method] — Qualified, on the premise that RI-02 is Non-fatal for the general scope claim**

VQ-2 requires resolution of RI-01 and RI-07.

- **RI-01 (Reporting integrity):** **Non-fatal, but unresolved at modern-era standards.** SRG-2 (B-1, B-2, B-10, B-5) and SRG-7 (B-5, B-14) collectively document reporting-coherence failures: undocumented FID response factors, inconsistent internal standard identification, mixed yield denominators in Table 7, Table 2 mass balance violation. These are **Era-norm dependent** (see §4): within 1976 BCSJ convention these omissions were acceptable; by contemporary standards they would prevent acceptance of a 60-entry scope paper. RI-01 is therefore **Non-fatal at 1976 standards but Era-norm deficient by current standards.**

- **RI-07 (Unsupported boundary):** **Non-fatal.** Two boundary claims are made: (a) "one of the most serious limitations" (SRG-6: alkyl Grignard + dihaloethylene). The boundary itself is established by the observation that these reactions give "sluggish[REDACTED: substantial verbatim quotation; see Tier 9]β-hydrogen-bearing alkyl Grignard reagents give selective cross-coupling" (CLA-2). This is a positive boundary claim supported by numerous high-yield entries in Tables 6–7, where by-products are not detected; the absence of systematic by-product search (CLA-2) qualifies but does not collapse this claim.

**Assessment:** VQ-2 **passes (qualified)** for the general scope claim at 1976 era norms; **fails** for the PhF landmark claim (RI-02 fatal at VQ-1). The qualification derives from RI-01 remaining unresolved at modern-era standards, and from the boundary-claim qualification of CLA-2. However, the phosphine ligand ranking (Table 1: dppp > dmpf > dppe > dmpe > dppb) and the solvent effect (Table 5: ether > THF) are established by internally consistent GLPC comparisons within the same analytical framework, making them method-level reproducible despite the response-factor gap.

**However, Layer 3 (C–F oxidative addition) on its own: VQ-1 fails — Fatal.** The PhF landmark claim cannot advance beyond a failed VQ-1.

---

**VQ-3 [Mechanism] — Fails**

VQ-3 requires resolution of RI-03, RI-04, RI-06, inheriting VQ-2.

- **RI-03 (Unobserved explanatory):** **Fatal for any mechanistic claim.** The diorganonickel intermediates central to Scheme 1 are not directly observed under catalytic conditions (SRG-1). The yellow species from [Ni(dppp)Cl₂] + n-BuMgBr (Table 2) is the only in-paper evidence for a catalytically relevant Ni-organic species, but it is characterized only by color. No ³¹P NMR, UV-vis, or any other analytical characterization is provided.

- **RI-04 (Unreplicated discriminator):** **Non-fatal but qualifying.** The anomalous reactivity order (U-2, SRG-1) interpreted as evidence for "two or more rate-limiting steps" is a single qualitative dataset without rate constants. The crossover experiment absence (CLA-1) prevents the discriminating experiment from being counted.

- **RI-06 (Imported model):** **Non-fatal.** Scheme 1 is assembled from Jolly-Wilke organonickel precedent and Tamura-Kochi mechanistic studies (ref. 46 cited as "essentially consistent"). The isomorphism is not demonstrated but is plausible given the shared organonickel framework.

- **RI-05 (Qualitative overread):** RI-05 is present in SRG-5 (Z:E ratios) and CLA-2 (β-hydride suppression). VQ-3 is therefore **"qualified"** even if RI-03 were resolved.

**VQ-3 fails** because RI-03 is Fatal: the mechanism cannot be certified as established when no intermediate is characterized and no mechanistic probe experiment distinguishes Scheme 1 from the Felkin-Corriu alternative.

---

**VQ-4 [Benchmark] — Fails (inherits VQ-3 failure)**

VQ-4 requires resolution of RI-08 and RI-09 in addition to inheriting VQ-3.

- **RI-08 (Unquantified reliability):** **Non-fatal at 1976 standards; Era-norm deficient now.** No replicate yield measurements with uncertainty are provided for any scope entry. The Table 2 mass balance violation (104%) is the most concrete evidence of measurement inconsistency.

- **RI-09 (External superiority):** **Non-fatal.** The superiority over organocuprates (stoichiometric requirement) and Kharasch systems (selectivity) is asserted without direct comparison; this is a structural claim (catalytic vs. stoichiometric metal) supported by the paper's own scope data, even without a matched-substrate head-to-head comparison.

VQ-4 fails on inheritance from VQ-3.

---

**Summary per independent layer:**

| Layer | VQ status | Bottleneck RI |
|---|---|---|
| Layer 1 (Scope claim) | VQ-2 (qualified, 1976 era norms) | RI-01 (era-norm dependent); RI-05 (CLA-2 qualifying) |
| Layer 2 (Scheme 1 mechanism) | VQ-2 (fails at VQ-3) | RI-03 (Fatal: no intermediates observed) |
| Layer 3 (C–F oxidative addition) | VQ-1 fails | RI-02 (Fatal: no isolated yield, no verified analytical method) |
| Layer 4 (β-hydride suppression) | VQ-2 (qualified) | RI-05 (CLA-2: olefin by-products not searched) |

---

### §4 Era-Norm Annotation

**communication-era tolerated:**

1. **GLPC-only yields without FID response factor documentation (B-1, B-10):** In 1976 BCSJ full-paper convention, quantitative GLPC with an internal standard was accepted as the primary analytical method for coupling yields without requiring published response factor tables; the implicit assumption of similar FID response for structurally related hydrocarbons was standard practice and not specifically required to be stated.

2. **Absence of replicate measurements and uncertainty reporting (B-2 partial, RI-08):** Single-run GLPC yield determinations were the norm for scope surveys in 1976; replicate analytical measurements with standard deviations were not routinely expected in full papers of this period for screening-type tables.

3. **Qualitative reactivity ranking by "exothermicity of reactions" (B-11):** Semi-quantitative ranking of substrate reactivity by operator-observed thermal response was an accepted observational practice in synthetic papers of this era, where Arrhenius-referenced rate measurements were not considered obligatory for scope papers.

4. **Mechanistic proposal without intermediate characterization (SRG-1, A-1):** In 1976 organometallic chemistry, the presentation of a catalytic cycle as a "rationalization[REDACTED: substantial verbatim quotation; see Tier 9]can be rationalized by Scheme 1," "A Brief Comment on the Mechanism") signals this status correctly within the conventions of the period.

5. **Citation of unpublished observations as mechanistic evidence (C-5, A-5):** Reference to group-internal unpublished data as mechanistic support was tolerated in 1976 BCSJ, particularly for preliminary mechanistic inferences labeled with hedging language ("it seems likely").

6. **Non-quantitative reactivity order discussion (B-11):** Qualitative ordering of substrate reactivity without competition kinetics was standard for scope papers; competition kinetics studies were published as separate mechanistic papers, not embedded in scope surveys.

---

**modern-era deficient:**

1. **Mass balance violation in Table 2 (B-2, 104% for [Ni(PPh₃)₂Cl₂], 16 h aging, 20 h reaction):** A sum of analytically determined product yields exceeding 100% of the limiting reagent is a calculation error or calibration artifact that must be investigated and corrected; modern reviewers would require re-measurement or explicit explanation. This is an internal inconsistency that is disqualifying by current standards regardless of era norm.

2. **Zero isolated product yield for a "first reported[REDACTED: substantial verbatim quotation; see Tier 9]first reported" C–F oxidative addition to a transition metal complex would require, by current standards, at minimum an isolated yield, a fully characterized product, and a verified analytical method; the co-elution problem documented in Table 3 footnote c makes the competitive-experiment values in Table 4 insufficient support for this landmark claim under any current journal's standards.

3. **Unspecified internal standard for Tables 6–7 (B-10):** By current standards for scope papers, the identity of the GLPC internal standard must be specified for every table, and representative response factor verifications reported; the discrepancy between "mesitylene" (Table 1) and "normal alkane" (Procedure A) and unspecified (Tables 6–7) is a reporting failure that would prevent reproducibility assessment.

4. **Z:E assignment method absent for stereochemical data (B-8, SRG-5):** Current standards require explicit documentation of the method used to assign geometric isomer ratios (NMR coupling constants or GC comparison with authentic samples), particularly for vinylic compounds where co-elution is possible on medium-polarity stationary phases.

5. **Vinyl chloride initial charge not documented for small-scale entries (B-14):** Current standards for gaseous reagents require explicit documentation of the charge method and quantity verification (weighing by condensation, pressure measurement, or titration) for all entries, not only the large-scale preparative procedure.

6. **Non-optimized conditions disclaimer without per-entry annotation (B-5):** A blanket disclaimer ("The reaction conditions are not necessarily optimum") applied to ~60 entries without per-entry optimization notes is considered insufficient in current-era scope papers; entries with yields below a threshold (typically <40%) are expected to carry a note indicating whether optimization was attempted or known yield-limiting factors exist.

---

### §5 Shortest-reinforcement route

#### Objective function 1: Advance Layer 1 (Scope claim) from VQ-2 (qualified) to VQ-3

The blocking RI for VQ-3 in Layer 1 is RI-03 (intermediates unobserved). However, resolving RI-03 fully (isolating and characterizing diorganonickel intermediates under catalytic conditions) is a multi-month program. The more tractable VQ-3 pathway for the scope claim is to address RI-05 (CLA-2: olefin by-product search) and RI-01 (SRG-2: GLPC basis) simultaneously, then tackle RI-03. Independently, Layer 3 (C–F oxidative addition) needs a separate investment pathway starting at VQ-1.

**Shortest route to VQ-3 (Layer 1 — Scope claim):**

1. **EP-01a [Reporting-coherence pack] — SRG-2 (B-1, B-2, B-10, B-5).** Document FID response factors for four representative product classes (alkylbenzene, silylmethyl arene, cyclopropyl, internal olefin) vs. internal standard; identify and resolve the Table 2 mass balance violation (104%) by GLPC re-measurement; add a reconciliation column to Table 7 specifying yield base and denominator per entry. Advances RI-01. This is the highest-information-gain EP investment because it simultaneously addresses SRG-2 (which underlies all quantitative claims) and SRG-7 (condition/scope conflation), requires no new chemistry (only recalibration and re-measurement), and uses the existing Hitachi GC 4B infrastructure.

2. **EP-02a [Identity / purity substantiation pack] — SRG-3 (U-5, A-6, B-3).** Prepare butylbenzene from PhF + n-BuMgBr + [Ni(dppp)Cl₂] at preparative scale (≥5 mmol PhF) and report isolated yield with full characterization (¹H NMR, mass spectrum parent ion m/e 134). Advances RI-02 for Layer 3 (enabling VQ-1 for C–F claim). This is the second-priority EP because it resolves the analytically fatal co-elution problem by bypassing GLPC entirely (isolation removes the need for analytical resolution) and establishes the landmark claim on the same evidentiary footing as Table 7 entries. Experimentally straightforward with existing infrastructure.

3. **EP-05a [Quantitative-ranking substantiation pack] — SRG-5 (B-8, A-4) + CLA-2 (U-3).** Report ¹H NMR J coupling constants for (E)- and (Z)-stilbene from dihaloethylene coupling (documents assignment method, advances RI-05 for SRG-5); simultaneously validate Silicone DC 550 column for C4 olefin detection and report GC headspace analysis for butene/propylene from representative β-hydrogen-bearing alkyl entries (resolves CLA-2 mechanistic claim qualification, advances RI-05 and RI-02 for CLA-2). Advances RI-05.

4. **EP-07a [Boundary-test pack] — SRG-6 (A-2, U-4).** Test neopentylmagnesium chloride (β-hydride-free alkyl) with (E)-ClCH=CHCl + [Ni(dppp)Cl₂]; characterize the product distribution by GC-MS. Advances RI-03 and RI-07 for the failure mode. This positions the paper to claim a mechanistic understanding of its "most serious limitation" and to propose a rational strategy for overcoming it.

5. **EP-03a [Direct-observation / state-assignment pack] — SRG-1 (A-1, U-1, U-8) + SRG-4 (A-5).** Characterize the yellow species from [Ni(dppp)Cl₂] + n-BuMgBr by ³¹P{¹H} NMR and UV-vis in situ; compare with [Ni(dppe)(CH₂SiMe₃)₂] (ref. 39) as an authentic diorganonickel standard; conduct the stoichiometric transmetalation comparison (n-BuMgBr vs. n-BuLi with [Ni(dppp)(Ph)(Cl)]). Advances RI-03 (primary for VQ-3 in Layer 2), RI-06, and the Mg-mechanistic localization (SRG-4). This is the most experimentally demanding investment and is placed last in information-gain order because EP-01a through EP-07a can be completed with existing infrastructure and significantly advance the VQ profile.

Certification-gate note: The experimental investment order follows information gain and experimental feasibility, but the final certification follows the inheritance gate order VQ-1 → VQ-2 → VQ-3 → VQ-4; Layer 3 (C–F claim) must pass VQ-1 (EP-02a) before its VQ-2/3 status is meaningful, and VQ-3 for Layer 1/2 requires RI-03 resolution (EP-03a, step 5) regardless of the order of steps 1–4.

---

#### Objective function 2: Advance Layer 2 (Scheme 1 mechanism) toward VQ-3, and Layer 1 toward VQ-4

**Shortest route to VQ-3 (Layer 2) and VQ-4 (Layer 1):**

1. **EP-04a [Discrimination / replication pack] — CLA-1 (U-1).** Crossover experiment with PhMgBr + n-BuMgBr + PhCl + vinyl chloride + [Ni(dppp)Cl₂]; GC-MS product distribution analysis. Advances RI-04 and RI-03 for the mechanistic layer. This is the single highest-information-gain experiment for Layer 2: a non-statistical crossover product distribution would confirm diorganonickel intermediates are involved (resolving U-1) and would begin to distinguish Scheme 1 from the Felkin-Corriu mechanism.

2. **EP-08a [Replication / uncertainty pack] — SRG-2 (B-2, RI-08).** Report triplicate GLPC determinations with standard deviations for the Table 1 reference reaction and at least one entry per catalyst in Tables 6–7; close mass balance for these representative entries. Advances RI-08 for VQ-4.

3. **EP-09a [Internal benchmark pack] — C-1, C-3 (D-2 competitive positioning).** Direct substrate comparison of the Ni-phosphine system against an organocuprate protocol on at least two overlapping substrates (e.g., PhCl + n-BuMgBr vs. Ph₂CuLi + n-BuX); this addresses RI-09 (external superiority asserted without direct comparison). Advances RI-09 for VQ-4.

Certification-gate note: The experimental investment order follows information gain, but the final certification is fixed by the gate order VQ-1 → VQ-2 → VQ-3 → VQ-4.

---

### §6 Contribution to institutional design

**1. Representative case for RI-03 — "Available-but-unutilized characterization" subtype:**

The yellow species from [Ni(dppp)Cl₂] + n-BuMgBr (Table 2, aging experiment) is the clearest example in the dataset of the RI-03 subtype "Available-but-unutilized characterization." The paper reports that this species is catalytically competent over 16 h at room temperature — a stability that is mechanistically informative (it is likely the resting state diorganonickel intermediate of Scheme 1) — yet no spectroscopic characterization is attempted despite the ³¹P NMR, UV-vis, and elemental analysis capabilities listed in the Experimental section. This case confirms and extends the RI-03 subtype annotation from Codebook v0.2a: the available characterization data (³¹P NMR would unambiguously identify a diorganonickel complex or a Ni(0) species) would verify the central mechanistic claim but the implications are not extracted in the main text. The color observation ("yellowish clear" vs. "dark brown") is presented as a mechanistic proxy, but this is qualitative overread (RI-05 co-occurrence with RI-03).

**2. New representative case for RI-02 — "Landmark-claim-without-product-isolation" pattern:**

The PhF coupling result (SRG-3) provides a new case-specific pattern for RI-02 that extends beyond the typical identity/purity substantiation context: a paper can explicitly acknowledge an analytical limitation (co-elution of PhF and benzene, Table 3 footnote c), then report competitive-experiment conversions by the same method in the adjacent table (Table 4) as if the limitation were resolved, without documenting the resolution. This "acknowledged-then-circumvented" analytical inconsistency is a distinct failure mode from simple omission of characterization data. The EP-02a implementation for this case (preparative scale isolation bypassing GLPC) is instructive for the EP dictionary: when the analytical method is compromised for a specific substrate, preparative isolation of the product at scale is the most direct resolution and simultaneously provides isolated yield, the strongest form of evidence for scope claim entries.

**3. RI co-occurrence pattern — RI-03 + RI-06 in SRG-1:**

SRG-1 exhibits a structurally important RI co-occurrence: RI-03 (unobserved intermediates) and RI-06 (imported model) co-occur in the same SRG, and resolving only one is insufficient. Even if the Jolly-Wilke premises of Scheme 1 are validated by isomorphism demonstration (resolving RI-06), the mechanism would remain at the rationalization level without direct intermediate observation or kinetic probe (resolving RI-03). Conversely, even if the yellow species is characterized as a diorganonickel complex (resolving RI-03 for step 1→2), the overall cycle would remain unvalidated without the crossover experiment (CLA-1, RI-04). This three-RI co-occurrence structure (RI-03 + RI-06 + RI-04) means that VQ-3 certification for Layer 2 requires resolving all three concurrently, not sequentially — each resolution is necessary but not sufficient.

**4. "Automatic resolution" pattern via communication→full paper transition — partial confirmation:**

The 1972 JACS communication (ref. 21: Tamao, Sumitani, Kumada) established the existence of the Ni-phosphine Grignard coupling; the present 1976 BCSJ full paper is the expected expansion. For RI-01 (reporting integrity) and RI-07 (boundary claims), the transition from communication to full paper did partially resolve limitations: the present paper provides ~60 substrate entries (vs. 6 in the 1972 communication), an explicit scope boundary statement (functional group incompatibility, dihaloethylene/alkyl Grignard limitation), and a catalyst screening table absent from the communication. However, RI-03 (unobserved intermediates) and RI-02 (PhF claim unsupported) are not resolved by the communication→full-paper transition — they are new deficiencies introduced in the full paper, not inherited from the communication. This case illustrates that the automatic-resolution pattern applies to some RI types (RI-01, RI-07 boundary claims) but not to self-contradictory absences (RI-03, RI-02 of SRG-3) that the full paper creates rather than inherits.

**5. PRI promotion evidence — PRI-10 (Kinetic overclaim):**

The paper contains a pattern relevant to PRI-10 (Kinetic overclaim): the statement "diethyl ether is better than THF as a solvent" and [REDACTED: substantial verbatim quotation; see Tier 9] (Table 5) are rate claims that rest on conversion data at fixed time points (16 h, 22 h) rather than on measured rate constants or initial rate comparisons. This is a kinetic overclaim from conversion data — the same pattern confirmed in Monnereau 2009. This paper provides a second independent instance, supporting PRI-10 promotion from provisional status. The implementation is more implicit (conversion-as-rate-proxy) than explicit (rate enhancement factor stated), but the structural pattern is isomorphic.

**6. No new PRI candidate required.**

All detected patterns are covered by existing RI codes (RI-01 through RI-06) or the PRI-10 provisional code. No pattern requiring a new PRI-NN candidate was detected in this single-paper analysis.

---

> **Tier 8 redaction notice**: This file is a redacted copy of the corresponding Tier 3 / Tier 9 output. Verbatim source-paper quotations have been replaced by `[REDACTED: see source paper §<loc>; full text retained in Tier 9 reviewer-only deposit]` markers, preserving location references and our own analytical content. Bibliographic fields (title, authors, journal, year, DOI), analytical labels (`evidence_chain:` with B-/U-/A-/C- internal IDs), short technical terms, and our own analytical text are not redacted. The redaction was applied by `scripts/redact_for_tier8.py` and, for this version, by `scripts/build_paperA_R1_public.py` with `scripts/redact_source_ngram_runs.py` (scripts of the project repository; they are not deposited).
