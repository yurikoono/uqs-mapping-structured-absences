prompt_version: stage3-v2-en-20260419
model_info: claude-sonnet-4-6

# Re-certification Assessment Sheet for Scientific Knowledge

## Tamao 2002 (Journal of Organometallic Chemistry, historical mini-review)

---

### §1 Claim Architecture

**Core claim summary:**

The paper's Novelty pillar is threefold and layered. First, it asserts independent co-discovery: Tamao, Sumitani, and Kumada reported in 1972 the cross-coupling reaction of Grignard reagents with C(sp²) halides catalyzed by a nickel–phosphine complex, simultaneously and independently of Corriu and Masse in France. Second, it asserts mechanistic prototype status: the Ni(II)/Ni(0) oxidative addition–transmetallation–reductive elimination cycle of Scheme 1, "proposed in the first communication [1]," [REDACTED: substantial verbatim quotation; see Tier 9] Third, it asserts a conceptual priority claim: the use of well-defined transition metal–phosphine complexes for traditional Kharasch-type Grignard reactions constituted "the first case" of "molecular catalysis," enabling selectivity impossible with simple salt catalysts.

The Utility pillar is the enumeration of ten characteristic features (Section 2, features 1–10): the proposed catalytic cycle and its generalization (feature 1), the molecular catalysis concept (feature 2), ligand-activity order for catalytic performance (feature 3), selective coupling of β-hydrogen-bearing alkyl Grignard reagents (feature 4 — elevated to "the most significant feature"), ligand- and halide-dependent sec-alkyl isomerization (feature 5), asymmetric coupling with chiral phosphine catalysts (feature 6), halide-dependent reactivity order with ArF as boundary (feature 7), stereoretentive coupling of alkenyl halides (feature 8), Ni > Pd reactivity comparison enabling stepwise dihalide coupling (feature 9), and oligothiophene synthesis as the first practical tailor-made heteroaryl oligomer method (feature 10). The Epilogue adds a bibliometric utility claim: citation-trend data (Fig. 2, 1984–1999) demonstrate that the discovery's importance has been "steadily increasing" and "will be increasing."

**Layered structure judgment:**

Three logically independent layers exist.

Layer A (historical priority): independent co-discovery of Ni–phosphine Grignard cross-coupling in 1972, co-determined with Corriu–Masse. This is a historiographic claim whose evidentiary base is the author's first-person retrospective recollection of submission sequence, stated without archival documentation. Refuting Layer A would not collapse Layers B or C.

Layer B (mechanistic/conceptual prototype): Scheme 1 as the mechanistic template for all subsequent Pd cross-coupling, and the molecular catalysis concept as the enabling conceptual innovation. This is simultaneously a mechanistic claim (the Ni(II)/Ni(0) elementary-step sequence is operative under catalytic conditions) and a historiographic claim (Pd workers adopted Scheme 1 rather than developing mechanistic proposals independently). Refuting Layer B would not collapse Layers A or C.

Layer C (characteristic-features scope): the ten enumerated features of Section 2 and their supporting representative equations (eqs. 2–6). This layer is the most directly chemistry-evidenced and is the closest to independent empirical grounding, because the primary papers [10a–c] and [13a,b] contain the underlying experimental data tables. However, those primary papers are cited-and-not-engaged in this mini-review, so within this document Layer C is only as strong as the completeness of the representative equations.

Inter-layer dependencies: The Epilogue's bibliometric argument (Fig. 2) simultaneously supports all three layers — citation growth implies that both the priority claim (Layer A), the prototype claim (Layer B), and the practical utility (Layer C) are recognized by the community. This mutual-reinforcement structure means that if the bibliometric methodology (B-8) is flawed, it cannot serve as independent evidence for any layer. Furthermore, the prototype claim (Layer B) logically depends on the mechanistic grounding of Scheme 1 (SRG-1): if the elementary steps of Scheme 1 were not experimentally validated under catalytic conditions, the claim that Pd workers adopted a validated prototype is weakened because they would have adopted an analogy-based proposal rather than an experimentally confirmed cycle.

"A single refutation collapses all claims" — does not apply: independent layers exist. The paper is resilient at the layer level. However, within each layer the central claim is structurally fragile: Layer A is unverifiable from published sources alone (requires archival documentation), Layer B rests on a single asserted data point (ref [11a]) plus an analogy-based mechanistic cycle, and Layer C depends on primary papers not reproduced in this document.

---

### §2 SRG / CLA → RI / ER / EP Crosswalk

---

**SRG-1 [Catalytic cycle elementary-step evidence absent]**

Members: U-1 (Ni(II)/Ni(0) cycle validity under catalytic conditions), U-8 (β-hydride suppression kinetics for feature 4 / eq. 2), and the stoichiometric-to-catalytic extrapolation in Scheme 1.

* **Primary RI**: RI-03 [Unobserved explanatory]
* **Secondary RI**: RI-06 [Imported model]
* **ER**: For the Scheme 1 catalytic cycle to be certified as operative under turnover conditions — and for its [REDACTED: verbatim source quotation; see the source paper via its DOI] the rate ordering k(reductive elimination) > k(β-hydride elimination) in the L₂Ni(Ar)(n-Bu) intermediate must be grounded in measured activation parameters (ΔH‡, ΔS‡) or in a competition experiment where the two pathways are quantitatively distinguished.
* **EP**: EP-03a [Direct-observation / state-assignment pack]; EP-04a [Discrimination / replication pack]
* **Case-specific implementation**: EP-03a — synthesize L₂Ni(Ph)(n-C₄H₉)(dppp) independently by stoichiometric transmetallation from NiCl₂(dppp) with PhMgBr (first) and n-BuMgBr (second), or by oxidative addition of PhCl to Ni(0)(dppp)(cod) followed by transmetallation with n-BuMgBr in Et₂O at −78 °C, and characterize the intermediate by ³¹P NMR and ¹H NMR at −40 °C; then measure its thermal decay rate (reductive elimination to o-dibutylbenzene plus homocoupling) by monitoring product formation by GC as a function of temperature between −20 °C and +30 °C. The rate ratio k(RE)/k(β-HE) at the standard reaction temperature provides the first direct measurement of the kinetic basis for the selectivity claimed in eq. 2. EP-04a — use a radical-clock substrate: (cyclopropylcarbinyl)magnesium chloride under standard Ni(dppp)Cl₂/PhCl catalytic conditions (2 mol% Ni, Et₂O, 25 °C); measure the ring-opened homoallyl product vs. ring-intact cross-coupling product by GC-MS. If ring-opening yield is <2%, the radical-chain (Ni(I)/Ni(III)) manifold is excluded at the rate-constant resolution of the cyclopropylcarbinyl clock (~10⁸ s⁻¹). This is a standard experiment in the field by 2001 and therefore a feasibility-first EP investment.
* **Notes**: U-1 (low-convergence high-gap: V2 only, severity high; V1 and V3 address the prototype/influence dimension rather than the internal cycle validity). U-8 (low-convergence high-gap: V2 only, severity high). RI-06 applies at the cycle level (scope note — cycle-level import): Scheme 1 was constructed by combining (a) Yamamoto's stoichiometric reductive elimination of L₂Ni(Ar)₂ (eq. 1) and (b) literature knowledge that NiCl₂ + RMgX → L₂NiR₂ (transmetallation); the combination produces a catalytic cycle that was "proposed[REDACTED: substantial verbatim quotation; see Tier 9]neither directly observed nor kinetically constrained[REDACTED: substantial verbatim quotation; see Tier 9]we proposed" rather than "we demonstrated" for Scheme 1. RI-06 is Secondary because the source of the RI-03 gap is the analogy-based cycle import. No Stage 2F input present (single-paper mode).

---

**SRG-2 [Mechanistic attribution of isomerization pathway]**

Members: U-3 (ligand-dependence reversal of sec-alkyl isomerization vs. chain-walking model), B-3 (yield omission in eq. 3).

* **Primary RI**: RI-05 [Qualitative overread]
* **Secondary RI**: RI-03 [Unobserved explanatory]
* **ER**: For the ligand-dependent isomerization (feature 5 / eq. 3) to be interpreted as a "characteristic feature" of the nickel–phosphine molecular catalysis, the mechanistic pathway must be identified at a level that explains the observed selectivity reversal: why does Ni(dmpe)Cl₂ (stronger σ-donor, Me₂P–(CH₂)₂–PMe₂) give 9:84 primary:secondary (disfavoring migration to primary) while Ni(dppp)Cl₂ gives 96:4 (strongly favoring primary)? Under a β-hydride elimination/reinsertion (chain-walking) mechanism, the stronger trans-influence and electron-donating character of dmpe should accelerate β-hydride elimination from the Ni(sec-alkyl) intermediate and thus favor migration to the primary terminus, which is the opposite of what is observed. At minimum, the paper must either acknowledge this potential contradiction of the chain-walking model, propose an alternative mechanism (Grignard pre-equilibration at Mg, radical-chain isomerization, or direct β-carbon elimination), or cite kinetic evidence from [13a,b] that resolves the ambiguity.
* **EP**: EP-05a [Quantitative-ranking substantiation pack]; EP-03a [Direct-observation / state-assignment pack]
* **Case-specific implementation**: EP-05a — compile a complete cross-tabulation of isomer ratios vs. Tolman cone angles and Hammett σ-para values for all six Ni–phosphine complexes and at least three sec-alkyl Grignard substrates (e.g., sec-BuMgCl, isobutylMgCl, cyclohexylmethylMgBr) and for three aromatic halide electronics (electron-rich, neutral, electron-poor ArCl), using matched GC conditions to report both yield and selectivity simultaneously; this would allow a Hammett/Taft analysis to discriminate Ni-mediated chain-walking (correlated with metal-based parameters) from Grignard pre-equilibration (correlated with Mg-coordination parameters). EP-03a — perform an isotope-labeling crossover experiment: synthesize α-¹³C-sec-butylmagnesium chloride (¹³C at C-2 of the sec-butyl group) and run the cross-coupling under Ni(dppp)Cl₂ and Ni(dmpe)Cl₂ conditions; determine by ¹³C NMR of isolated product whether the label appears at C-1 (consistent with Grignard pre-equilibration prior to transmetallation) or at C-2 (consistent with chain-walking on Ni after transmetallation). The two mechanisms give distinguishable isotope distributions and this experiment is executable with commercially available isotope sources.
* **Notes**: U-3 (convergence 1/3, V2 only, severity high; the isomerization mechanistic attribution was detected as high-severity only by V2, which focused on mechanistic questions; V1 and V3 addressed the yield omission and the chronological dimensions). B-3 (convergence 2/3; V1-Q3 + V2-OV3, temperature_gap none — same temperature, same root). RI-05 is Primary because the selectivity ranking (dppp > dmpe for primary product formation) is presented as a characteristic feature, which is a causal structural implication derived from a qualitative ranking (two data points from eq. 3) without a numerical model that would predict the ordering. The apparent reversal of the chain-walking expectation is a specific qualitative overread: the paper presents the ligand-dependence as consistent with a mechanistic picture (implied: ligand basicity modulates the Ni–alkyl intermediate behavior) without addressing whether the observed direction is consistent or inconsistent with the leading mechanistic candidate. RI-03 is Secondary because the isomerizing Ni(sec-alkyl)(Ar) intermediate is neither isolated nor kinetically characterized — the branch point between chain-walking and alternative pathways is an unobserved explanatory species.

---

**SRG-3 [Prototype/influence claim — priority, mechanism, bibliometrics]**

Members: U-2 (prototype claim, mechanistic lineage), C-6 (severed engagement with ref [11a], the primary citation for the prototype claim).

* **Primary RI**: RI-04 [Unreplicated discriminator]
* **Secondary RI**: RI-09 [External superiority]
* **ER**: For the claim that Scheme 1 [REDACTED: substantial verbatim quotation; see Tier 9] to constitute a demonstrated historiographic fact rather than an asserted analogy, at minimum one of the following must be shown: (a) that the 1975 Yamamura–Murahashi paper [11a] (J. Organomet. Chem. 91, C39) explicitly cited [1] as the mechanistic source for its proposed Pd oxidative addition–transmetallation–reductive elimination cycle and quoted or reproduced Scheme 1 as the template; or (b) that a systematic survey of the first-generation Pd cross-coupling mechanistic papers (1975–1985) shows that a statistically significant fraction cite [1] for the mechanism rather than citing Wilkinson (Acc. Chem. Res. 4 (1971) 17), Collman (Acc. Chem. Res. 1 (1968) 136), or Heck (JACS 1968) as mechanistic sources.
* **EP**: EP-04a [Discrimination / replication pack]; EP-09a [Internal benchmark pack]
* **Case-specific implementation**: EP-04a — retrieve [11a] (Yamamura, Murahashi, Moritani, J. Organomet. Chem. 91 (1975) C39) and read its mechanistic discussion section; if [11a] cites [1] for the mechanistic scheme, record this as a positive evidence datum; if [11a] cites Wilkinson/Collman/Heck without citing [1], this is negative evidence for the prototype claim. Extend this analysis to the next five Pd cross-coupling mechanistic proposals in the same period (1975–1980) and report the fraction citing [1] in a mechanistic context. The result is a discrimination between the "prototype adopted" and "independently developed" hypotheses at a level appropriate for a historiographic claim. EP-09a — provide an internal benchmark comparison of Scheme 1 (Section 1 of this mini-review) and the generalized Fig. 1 (the "M" cycle) with the specific mechanistic cycle proposed in [11a]; if the elementary-step language, the metal oxidation states, and the organometallic partner types in [11a] closely parallel Scheme 1 in ways that are unlikely to be independently derived, this constitutes positive mechanistic-lineage evidence.
* **Notes**: U-2 (high-convergence high-gap: V1-Q12 + V2-OV1 + V3-OV2; convergence 3/3, temperature_gap medium — V1=low, V2=high, V3=medium). C-6 (severed engagement: [11a] is cited but not engaged; no specific data from [11a] are reproduced or quoted). This is the paper's highest-convergence item and the primary D-4 candidate. RI-04 is Primary because the prototype claim rests on a single asserted discriminatory data point (the bare citation to [11] as "proof" of adoption) without any analytical precision or exclusion of the null hypothesis (independent development from Wilkinson/Collman precedents). RI-09 is Secondary because the paper implicitly asserts that Scheme 1's influence is superior to alternative organometallic precedents (Wilkinson, Collman, Heck) without a direct comparison of which of those predecessors the first Pd workers actually cited.

---

**SRG-4 [Citation-trend data reliability]**

Members: B-8 (Fig. 2 bibliometrics, database and protocol unspecified), U-6 (independent co-discovery claim, archival basis undocumented).

* **Primary RI**: RI-01 [Reporting integrity]
* **Secondary RI**: RI-07 [Unsupported boundary]
* **ER**: For Fig. 2 to support the claim that the discovery's importance is "still steadily increasing," the citation data must be independently reproducible: the database name, the search string for each of the three papers ([1], [10a], [10b]), the self-citation exclusion rule (if any), the language coverage (English-only or all languages), the search date, and the year-by-year counts as raw numbers (rather than bar heights in a graph) must all be specified. For the independent co-discovery claim, at minimum the journal submission dates of [1] and [2] must be cited from the published papers' received/accepted headers, or the limitation to first-person recollection must be explicitly acknowledged.
* **EP**: EP-01a [Reporting-coherence pack]; EP-07a [Boundary-test pack]
* **Case-specific implementation**: EP-01a — provide Fig. 2 as a supplementary data table: for each year 1984–1999 and each of the three papers, give the raw citation count from a named database (Web of Science Core Collection is the appropriate retrospective database for organic-chemistry citation analysis) and specify whether self-citations are included or excluded; append the search query strings. This single table would transform a visually presented trend into a verifiable and reproducible dataset. EP-07a — cite the received/accepted dates from the masthead of [1] (JACS 94, 4374, 1972: submitted ~August 1971, received ~October 1971, from the paper header) and from [2] (Chem. Commun. 1972, 144: received date from the journal header); if these dates establish that [1] was received before [2] or vice versa, the "shortly after we had submitted" chronology can be partially corroborated from the published record without requiring archival access. If journal records are not available (the mini-review does not cite these dates), state explicitly that the independence claim rests on first-person recollection with an acknowledged evidentiary limit.
* **Notes**: B-8 (high-convergence high-gap: V1=low, V3=high; convergence 2/3, temperature_gap medium — the historical-documentation perspective assigns high severity because bibliometric methodology is the primary tool of that analytical mode; the chemistry perspective assigns low severity because the citation trend is a supporting rather than primary argument). U-6 (medium severity, V3 primary; convergence 1/3). RI-01 is Primary because the measurement frame for the citation-trend comparison is entirely absent (no database, no protocol), making independent replication of the Fig. 2 bars impossible. RI-07 is Secondary because the forward projection ("will be increasing") asserts a positive boundary claim for future importance without a failure condition (i.e., no condition is identified under which the trend would reverse or flatten).

---

**SRG-5 [Ni > Pd reactivity comparison — quantitative basis absent]**

Members: U-4 (Ni > Pd reactivity for C(sp²)–halides, kinetic basis absent), C-10 (severed engagement with Negishi papers [16a–c] that report Pd cross-coupling data), B-5 (industrial application claim citing unpublished companion [15]).

* **Primary RI**: RI-08 [Unquantified reliability]
* **Secondary RI**: RI-09 [External superiority]
* **ER**: For the claim that [REDACTED: substantial verbatim quotation; see Tier 9] to function as a design principle for the stepwise dihalide coupling strategy (feature 9 / eq. 5), at minimum one direct rate or yield comparison between a Ni–phosphine catalyst and a Pd–phosphine catalyst using the same ArCl substrate, same Grignard reagent, same solvent, and same temperature must be provided, along with identification (even qualitative) of which elementary step (oxidative addition, transmetallation, or reductive elimination) is rate-determining and responsible for the observed overall reactivity difference. Additionally, the apparent inversion of the standard ArCl oxidative addition trend (Pd(0) is typically more electrophilic than Ni(0) toward unactivated ArCl in model stoichiometric reactions) must be addressed by specifying whether the "more reactive" comparison refers to overall TOF, TON, or initial rate under catalytic rather than stoichiometric conditions.
* **EP**: EP-08a [Replication / uncertainty pack]; EP-09a [Internal benchmark pack]
* **Case-specific implementation**: EP-08a — measure initial TOF (first 30 min, ≥3 replicate runs) for Ni(dppp)Cl₂ and Pd(dppb)Cl₂ in identical parallel setups: 1 mol% catalyst, 4-chlorotoluene (1.0 equiv), PhMgBr (1.2 equiv), Et₂O, 25 °C; report mean ± SD and calculate the TOF ratio (Ni/Pd); repeat at −20 °C to assess whether the reactivity ratio changes with temperature, which would provide a preliminary indication of whether it is kinetic or thermodynamic. Report separately whether the reaction goes to completion for both catalysts and, if not, the conversion-time profiles. EP-09a — run a competition experiment: add 0.5 mol% Ni(dppp)Cl₂ and 0.5 mol% Pd(dppb)Cl₂ simultaneously to a solution of the ortho-dihalide used in eq. 5 and the appropriate Grignard reagent; measure product distribution by GC-MS to directly observe selective consumption by Ni vs. Pd under competitive conditions, which is the most direct internal benchmark for the Ni > Pd reactivity claim as used in the stepwise dihalide coupling strategy.
* **Notes**: U-4 (high-convergence low-gap: V1-Q7 + V2-OV2; convergence 2/3, temperature_gap low — V1=medium, V2=high). C-10 (severed: [16a–c] Negishi papers report Pd cross-coupling yields but no kinetic data are engaged). B-5 (unpublished companion [15] means the industrial-application claim cannot be independently verified from this paper or from any published source at the time of submission). RI-08 is Primary because the Ni > Pd comparative claim lacks any replicate measurements or uncertainty quantification: no rate constants, TON, TOF, or yield comparison from matched conditions is presented for any pair of Ni and Pd reactions, making the reliability of the comparison unquantifiable. RI-09 is Secondary because the superiority of Ni is asserted on the basis of external literature values for Pd cross-coupling (refs [11] and [16]) without a direct parallel comparison in the Kumada group's own system.

---

**SRG-6 [Reporting completeness of scope equations]**

Members: B-1 (ligand activity order, features 3), B-2 (β-hydrogen selectivity yield basis, feature 4 / eq. 2), B-3 (isomer ratios without yield, feature 5 / eq. 3), B-4 (fluorobenzene, no conditions or yield, feature 7), B-6 (stereoretentive alkenyl coupling, no substrates or E:Z ratios, feature 8), B-7 (oligothiophene synthesis, no chain-length selectivity, feature 10 / eq. 6).

* **Primary RI**: RI-01 [Reporting integrity]
* **Secondary RI**: RI-08 [Unquantified reliability]
* **ER**: For the ten characteristic features of Section 2 to be evaluable as synthetic protocols rather than cited existence proofs, each feature must be accompanied within this document by: (i) an unambiguous measurement basis for any reported yield (GC with internal standard vs. isolated yield); (ii) the key experimental variables (catalyst identity, catalyst loading, temperature, solvent, reaction time) sufficient to verify reproducibility at the reported level; (iii) for reactions where two or more pathways compete (β-hydride elimination in feature 4, chain-walking in feature 5, E-to-Z isomerization in feature 8), a mass balance entry reporting major byproduct yields; and (iv) for summary rankings (feature 3 ligand order), coverage of all catalysts mentioned in the paper (including Ni(dmpe)Cl₂ and Ni(dmpf)Cl₂, which are named in Section 1 but absent from the ranking in feature 3).
* **EP**: EP-01a [Reporting-coherence pack]; EP-08a [Replication / uncertainty pack]
* **Case-specific implementation**: EP-01a — for eq. 2 (feature 4, 80% yield claimed for synthesis of o-dibutylbenzene): specify whether the 80% figure is GC yield with internal standard or isolated yield after column chromatography; report the mass balance for the β-hydride elimination product (1-butylene or n-butane), the homocoupling product (4,4'-dibutylbiphenyl), and unreacted starting material at the end of the reaction. For eq. 3 (feature 5): add isolated yield for both the dppp and dmpe runs (not just the isomer ratio), and add the two missing ligands (dmpe and dmpf) to the ranking in feature 3 so that the complete six-ligand scope is covered. For eq. 6 (feature 10, 64% yield for 5,5',5'',5'''-tetrabromo-[2,2':5',2'':5'',2'''-quaterthiophene] synthesis): report the chain-length distribution (dimer, trimer, oligomer fraction >4 units) by GC or GPC to demonstrate that the 64% yield corresponds specifically to the quaterthiophene and not to a mixture. EP-08a — for features 3 and 9 (the two comparison-based claims), provide ≥3 replicate yield measurements for the representative reactions so that statistical uncertainty can be assessed; the current single data points for the Ni > Pd comparison (features 9) and the ligand ranking (feature 3) cannot be used to assign uncertainty limits.
* **Notes**: B-1 through B-7 (B-5 partially absorbed into SRG-5). High-convergence low-gap for B-3 (V1-Q3 + V2-OV3, temperature_gap none) and B-6 (V1-Q6 + V2-OV4, temperature_gap none). Low-convergence items: B-1, B-2, B-4, B-7 (V1 primary for each). RI-01 is Primary because the cross-comparison between features and between different Ni catalyst variants is impossible without knowing the measurement frame for each reported number. RI-08 is Secondary because no replicate measurements or uncertainty descriptions accompany any of the scope equation yields — all quantitative claims rest on single representative data points.

---

**SRG-7 [Discovery narrative — retrospective reconstruction vs. contemporaneous documentation]**

Members: U-6 (independent co-discovery claim, no archival documentation), U-7 (Ni(0)-ethylene complex chronology: ref [9] published 1973, cited as pre-1972 work), C-5 (chronological complexity of [9]).

* **Primary RI**: RI-04 [Unreplicated discriminator]
* **Secondary RI**: RI-05 [Qualitative overread]
* **ER**: For the causal chronological discovery narrative to function as a valid evidentiary basis for the paper's priority claim, the sequence (Sumitani's 1970–1971 Ni(0)-ethylene complex work → October 1971 project start → end-of-1971 results for [1]) must be corroborated by at least one independently verifiable piece of contemporaneous documentation: a journal submission date (from the JACS masthead of [1]), a dated internal report, or a laboratory notebook entry. Where only first-person recollection is available, the narrative must explicitly acknowledge this limitation. The specific anomaly is that ref [9] — cited as documenting Sumitani's pre-1972 Ni(0)-ethylene complex preparation — was published in 1973, one year after [1]. The citation functions in the narrative as if [9] represents contemporaneous work, but the 1973 publication date makes this chronologically non-verifiable from the published record alone.
* **EP**: EP-04a [Discrimination / replication pack]; EP-07a [Boundary-test pack]
* **Case-specific implementation**: EP-04a — retrieve the received and accepted dates from the masthead of [1] (Tamao, Sumitani, Kumada, JACS 94 (1972) 4374) and [2] (Corriu, Masse, Chem. Commun. (1972) 144); the received dates serve as the primary contemporaneous documentation of the chronological sequence and partially corroborate (or falsify) the "shortly after we had submitted" narrative without requiring access to private correspondence. If [1] was received before [2], the priority claim is supported; if they were received within days of each other, independence is plausible but not provable from publication records alone. EP-07a — state explicitly whether ref [9]'s Ni(0)-ethylene complex preparation (Kiso, Kumada, Maeda, Sumitani, Tamao, J. Organomet. Chem. 50 (1973) 311) reports experiments performed before or after the submission of [1] in 1971, and whether contemporaneous documentation (laboratory notebooks) exists for this claim; if laboratory notebooks are not available, acknowledge this as a documented evidentiary limit of the causal narrative. These two steps together would transform the discovery narrative from a retrospective first-person assertion to a partially archivally grounded account.
* **Notes**: U-6 (medium severity, V3 primary; convergence 1/3). U-7 (convergence 2/3; V2-Q10 + V3-OV3, temperature_gap none — same temperature, V2=medium, V3=medium). C-5 (chronological complexity: [9] is cited as pre-discovery foundational work but is a post-discovery publication). RI-04 is Primary because the entire discovery chronology and the independent co-discovery determination rest on a single asserted discriminatory data point (the author's first-person recollection of manuscript submission sequence), which has strong narrative discriminatory power but no independent corroboration or archival precision. RI-05 is Secondary because causal structural implications (Sumitani's Ni(0) work mechanistically enabled the 1972 discovery) are derived from a qualitative chronological narrative — specifically from the order in which events are presented — without numerical or archival support.

---

**Outside the SRGs: CLAs**

**CLA-1: Self-contradictory scope exception — ArF reactivity**

* Grounded in: U-5, B-4 (META-linked pair; B and U items not included in any SRG's member_items)
* Description: Feature 7 states that [REDACTED: substantial verbatim quotation; see Tier 9] thereby framing Ni's reactivity as broadly correlated with C(sp²)–halide bond strength in the order C–Cl preferred over C–Br and C–I (inverted relative to simple BDE considerations, suggesting a substrate-matched rate-determining step). The paper then immediately adds: [REDACTED: substantial verbatim quotation; see Tier 9] The juxtaposition is self-contradictory within the paper's own scope framework: if the preferred halide is ArCl (C–Cl BDE ~95 kcal/mol) and ArBr and ArI are less preferred (higher BDE = lower reactivity? — the ordering is already non-standard), then ArF (C–F BDE ~125 kcal/mol, the strongest C–halide bond) should be the most unreactive substrate, consistent with "rather low reactivity." However, the paper provides no conditions, no yield, no citation, and no mechanistic rationale for why ArF reacts at all under Ni(0) catalysis, which is not trivially expected given the high barrier to ArF oxidative addition. The paper's own Ni > Pd reactivity framework does not explain why an ArF substrate would react — if Ni is "generally more reactive toward C(sp²)-halides than Pd," and Pd ArF cross-coupling was not practical in 2001, what elementary step difference makes Ni capable of activating ArF? This is a self-contradictory absence: the paper's own proposed mechanism predicts that the strongest C–X bond would be least reactive, yet the ArF case is presented as an observable feature without mechanistic reconciliation.
* **Primary RI**: RI-07 [Unsupported boundary]
* **Secondary RI**: RI-03 [Unobserved explanatory]
* **ER**: For the ArF scope claim to be internally consistent with the paper's own Ni-reactivity framework, either (a) the yield and conditions for the fluorobenzene reaction must be reported (at minimum: catalyst identity, temperature, solvent, time, and isolated or GC yield) so that "rather low" is quantifiable, together with a mechanistic rationale for why ArF oxidative addition to Ni(0) is feasible, or (b) the ArF observation must be explicitly framed as an anomalous boundary case that represents a mechanistic regime distinct from the standard ArCl reactivity and is not explained by the paper's own rate-ordering model.
* **EP**: EP-07a [Boundary-test pack]; EP-03a [Direct-observation / state-assignment pack]
* **Case-specific implementation**: EP-07a — report the experimental conditions (catalyst identity, mol%, temperature, solvent, time) and quantitative yield for the fluorobenzene cross-coupling; specify the Grignard reagent used, and report the conversion of PhF relative to a standard PhCl run under identical conditions to provide a relative rate factor. EP-03a — measure the rate of oxidative addition of PhF to Ni(0)(dppp)(η²-PhF) or Ni(0)(dppe)(cod) in Et₂O at 25 °C by ³¹P NMR monitoring and compare with PhCl oxidative addition under matched conditions; the resulting rate ratio (k(OA, PhF)/k(OA, PhCl)) would determine whether the ArF activation by Ni occurs at the oxidative addition step or elsewhere in the cycle, and would resolve the self-contradiction within the paper's own rate-ordering framework.
* **Notes**: Self-contradictory-absence CLA check: the paper's own catalytic model predicts that the rate of C–X oxidative addition to Ni(0) should correlate with C–X bond electrofugality in the order C–I > C–Br > C–Cl >> C–F. The "ArCl preferred" statement in feature 7 implicitly inverts this (choosing C–Cl over C–Br and C–I, suggesting the rate-determining step is not oxidative addition for these substrates), which makes the ArF observation doubly anomalous. The paper does not acknowledge this dual anomaly. Directly bears on D-1 claim (feature 7 as part of the scope characterization that constitutes the paper's Utility pillar). The B and U items grounded_in (B-4 and U-5) are not included in any SRG's member_items.

---

### §3 Current VQ assessment

**Current judgment: VQ-1 (Observation) — qualified pass**

---

**VQ-1 [Observation] — non-fatal pass (qualified)**

RI-02 (Object identification): All nickel–phosphine catalysts are identified by molecular formula and the common phosphine abbreviations that were standard nomenclature by 2001 (dppp, dppe, dppb, dmpe, dmpf, PR₃). All cross-coupling products are identified by structural formula in equations 2–6 or by compound name (o-dibutylbenzene, quaterthiophene). Purity is not established within this document, but the paper is a retrospective mini-review of established chemistry, and the primary papers [10a–c] and [13a,b] contain the original product characterizations that serve as the purity basis. RI-02 is non-fatal for this genre: the mini-review format legitimately references rather than reproduces product characterization data. VQ-1 passes with the qualification that product identity depends entirely on the primary papers cited, and any error in those primary papers would propagate uncorrected into this document.

No item in §2 rises to the level of a fatal RI-02 issue: no product structure is claimed without an underlying primary reference, and no catalyst identity is ambiguous.

---

**VQ-2 [Method] — fails**

On the premise that RI-02 is non-fatal (as established above), VQ-2 requires resolution of RI-01 (Reporting integrity) and RI-07 (Unsupported boundary). Neither is resolved:

- RI-01 (SRG-6): The measurement basis for all yields in eqs. 2, 4, 5, 6 is unspecified (GC vs. isolated yield); the experimental conditions (temperature, catalyst loading, solvent, time) are absent from each scope equation within this document. The ligand activity ranking (feature 3) omits two of the six named catalysts (Ni(dmpe)Cl₂ and Ni(dmpf)Cl₂). Cross-comparison between the ten characteristic features and across different catalyst variants is impossible from the information given in this paper.
- RI-01 (SRG-4): Fig. 2 citation-trend data lack database identity, search protocol, self-citation handling, and raw year-by-year numbers. The comparison between the three papers' citation trends cannot be reproduced.
- RI-07 (CLA-1): The "ArF reacts at low reactivity" observation is asserted without conditions or yield, and the mechanistic basis for ArF oxidative addition to Ni(0) under catalytic conditions is not provided. This is an unsupported positive boundary claim within the paper's own scope framework: a substrate at the extreme end of the C–X BDE scale is claimed to react without any kinetic or yield quantification.
- RI-07 (SRG-4, secondary): The forward-projecting claim "will be increasing" asserts a positive boundary for future importance without a specified failure condition.

**VQ-2 fails** on RI-01 (SRG-4, SRG-6) and RI-07 (CLA-1, SRG-4). The RI-01 failure in SRG-6 is non-fatal for the chemistry claims (the primary papers supply the missing condition and yield data), but the bibliometric argument (RI-01 in SRG-4) and the ArF boundary claim (RI-07 in CLA-1) are not recoverable from the cited primary papers within this document's framework.

**Layered VQ asymmetry:** Layer C (characteristic-features scope) on its own is structurally closer to VQ-2 than Layers A and B. Were the measurement conditions extracted from primary papers [10a–c] and [13a,b] and presented as a supplementary table, RI-01 in SRG-6 would be substantially resolved for Layer C. The ArF boundary issue (CLA-1) and the bibliometric methodology issue (SRG-4) would remain as Layer B and Layer A/Epilogue failures respectively, but Layer C itself could reach VQ-2 with a primary-paper supplement engagement.

---

**VQ-3 [Mechanism] — fails**

On the premise that VQ-2 holds (for analytical continuation purposes only), VQ-3 requires resolution of RI-03, RI-04, and RI-06, and the RI-05 item in SRG-2 remains as a qualifying condition that would make VQ-3 "qualified" even if other RIs were resolved. None of these is resolved:

- RI-03 (SRG-1, Primary): The Ni(Ar)(R)(L₂) intermediate at the reductive elimination / β-hydride elimination branch point is neither directly observed (not characterized) nor kinetically constrained (no rate measurements) under catalytic conditions. The elementary step identity under turnover is inferred entirely by analogy from Yamamoto's stoichiometric chemistry.
- RI-06 (SRG-1, Secondary): Scheme 1 was imported by cycle-level analogy from stoichiometric diorganonickel chemistry. No isomorphism demonstration in the catalytic manifold is provided: neither by rate comparison of stoichiometric vs. catalytic elementary steps, nor by independent generation of proposed intermediates under catalytic conditions.
- RI-04 (SRG-3, Primary): The prototype claim rests on a single asserted data point — the bare citation to [11] — without independent verification of whether [11a] explicitly adopted Scheme 1 as its mechanistic model.
- RI-04 (SRG-7, Primary): The discovery chronology rests on a single first-person recollection data point, and the citation of [9] as pre-discovery work is unverifiable from the published dates of [9] alone.
- RI-05 (SRG-2, Primary, qualifying): The ligand-dependent isomerization selectivity (dppp 96:4 vs. dmpe 9:84) is presented without mechanistic attribution, and the apparent contradiction of the chain-walking model is not acknowledged. This makes VQ-3 "qualified" even in the best case.

**VQ-3 fails** on RI-03, RI-04, RI-06. Would reach VQ-3 (qualified) only after RI-03 and RI-06 are resolved and RI-04 is resolved for at least one SRG (either SRG-3 or SRG-7); RI-05 (SRG-2) would remain as a qualification.

**Layered VQ asymmetry:** Layer C (characteristic-features scope) on its own does not face RI-04 (prototype historiography) or RI-06 (cycle-level import) as fatal obstacles. The SRG-2 issue (RI-05 on isomerization) and SRG-1 issue (RI-03 on β-hydride suppression / eq. 2) are the mechanistic barriers for Layer C. If EP-03a for SRG-1 and EP-03a for SRG-2 were executed, Layer C could reach VQ-3 (qualified). **Layer B (prototype claim)** would require additionally resolving RI-04 in SRG-3 (citation-graph analysis), which is a historiometric rather than chemical experiment. **Layer A (priority claim)** would require resolving RI-04 in SRG-7 (archival documentation), which is an archival rather than chemical investigation.

---

**VQ-4 [Benchmark] — fails**

On the premise that VQ-3 holds (for analytical continuation), VQ-4 requires resolution of RI-08 (Unquantified reliability) and RI-09 (External superiority). Neither is resolved:

- RI-08 (SRG-5, Primary): The Ni > Pd reactivity comparison (feature 9) is presented without replicate measurements or uncertainty quantification for any Ni/Pd parallel run. No TON, TOF, or rate constant pair is provided; the comparison is entirely qualitative ("generally more reactive").
- RI-08 (SRG-6, Secondary): No replicate measurements or uncertainty descriptions accompany any of the scope equation yields (eqs. 2, 4, 5, 6 all report single yield values without error bars or replicate information).
- RI-09 (SRG-5, Secondary): The superiority of Ni over Pd for C(sp²)–halide reactivity is asserted on the basis of external Negishi Pd papers ([11], [16a–c]) without any direct comparison experiment run in the Kumada system.

**VQ-4 fails** on RI-08 (SRG-5, SRG-6) and RI-09 (SRG-5). These failures are structurally subordinate to the VQ-2 and VQ-3 failures (primary papers supply some of the replicate data for Layer C scope), but the Ni > Pd comparison (SRG-5) requires new experimental work — not simply retrieval of existing primary data — because no direct Ni/Pd head-to-head replicate experiment was performed in any of the cited papers.

---

### §4 Era-Norm Annotation

**Communication-era tolerated:**

- **B-1 (ligand activity order, no measurement basis; feature 3)**: In 2001, retrospective mini-reviews in special commemorative volumes routinely enumerated qualitative activity rankings without specifying the measurement basis (yield, TON, or rate), because readers were expected to consult the referenced primary papers for quantitative detail. The abbreviated ranking for features in a 4-page historical summary was the genre standard.

- **B-2 (eq. 2, 80% yield without mass balance; feature 4)**: In 2001, illustrative yields in mini-reviews served as existence proofs of feasibility rather than as reproducible protocols. The full experimental data reside in [10c] (Org. Synth. 58 (1978) 127), which was an Organic Syntheses procedure — a widely recognized validation format — making mass balance reporting in the mini-review redundant by era convention.

- **B-3 (eq. 3, isomer ratios without yield; feature 5)**: Era-tolerated for the same genre convention: selectivity ratios were the focal datum for isomerization studies, and yield completeness was assumed from refs [13a,b].

- **B-4 (fluorobenzene, no conditions or yield; feature 7)**: The parenthetical mention of ArF reactivity as a scope footnote was era-tolerated for a 4-page mini-review; journal expectations for this format in 2001 did not mandate quantitative support for parenthetical scope notes.

- **B-6 (stereoretentive alkenyl coupling, no substrate or E:Z ratio; feature 8)**: Era-tolerated as a general-scope statement; full E:Z data were available from the original primary literature and were not required in a 4-page historical summary.

- **B-7 (eq. 6, oligomer synthesis, no chain-length selectivity; feature 10)**: Era-tolerated; chain-length selectivity data from [10b] and [18] were the community's baseline knowledge, and a single illustrative yield for the quaterthiophene was the appropriate mini-review entry.

- **B-8 (Fig. 2, no database or search protocol)**: In 2001, citation-trend figures in chemical mini-reviews were routinely presented as visual illustrations of impact without PRISMA-level bibliometric documentation. The ISI Science Citation Index (predecessor to Web of Science) was the de facto tool, and citation-count figures without explicit protocol specification were standard for this genre.

- **U-6 (independent co-discovery, "generally recognized" framing)**: In 2001, the "generally recognized" formulation for simultaneous independent discovery was an accepted shorthand in chemical history literature, particularly for events that occurred 30 years earlier when archival standards were not yet a community expectation for mini-reviews.

**Modern-era deficient:**

- **B-8 (Fig. 2, no database or search protocol)** [dual classification]: By contemporary bibliometric standards (post-2010: PRISMA-adjacent expectations for systematic citation analyses; post-2015: explicit calls for reproducible bibliometrics in chemistry reviews), any citation-trend figure presented as primary evidence for growing importance must specify the database, search string, self-citation handling, and language filter. The current Fig. 2 is not reproducible by an independent analyst. This is a modern-era deficiency for any re-publication or republication of this claim.

- **B-2 (eq. 2, no mass balance for β-hydride byproducts)**: By contemporary standards, a claim elevated to "the most significant feature attained for the first time" requires mass balance closure for the competing pathway (β-hydride elimination to 1-butylene). Modern reviewers would require this for any claim about selective pathway suppression, regardless of format.

- **B-1 (ligand activity order, no measurement basis)**: Contemporary review standards, including for short perspective articles, require that any activity ranking specify the measurement basis (yield, TON, TOF, or rate) and cite the specific data table in the primary paper. The omission of measurement basis for the ligand ranking is now a standard reviewer concern.

- **CLA-1 (ArF scope exception, no conditions or mechanistic rationale)**: Modern scope-reporting standards require that a boundary case contradicting the paper's own reactivity framework be either quantitatively characterized or explicitly flagged as mechanistically unexplained. The "it is noted that even fluorobenzene…" formulation does not meet current review standards for anomalous scope exceptions.

- **U-6 (independent co-discovery claim, undocumented)** [dual classification]: In a modern resubmission context, a priority claim framed as "generally recognized" would be required to cite the submission or receipt dates from the original journal mastheads (which are publicly verifiable) rather than relying on first-person recollection.

- **U-7 (Ni(0)-ethylene complex chronology, ref [9] published after [1])**: Contemporary historiographic standards for science-history articles require explicit acknowledgment when a cited reference was published after the events it is used to document. The current paper presents [9] (J. Organomet. Chem. 50 (1973) 311) as contemporaneous foundational work for the 1972 discovery without flagging the 1973 publication date as a chronological anomaly.

Items classified in both (tolerated then, deficient now): B-8, U-6. These represent a discipline-level era-norm shift specifically in bibliometric and archival evidentiary standards, distinct from the measurement-precision shifts (qualitative to quantitative) that dominate era-norm transitions in primary research papers.

---

### §5 Shortest-reinforcement route

**Objective function 1: VQ-2 (Method)**

Current level: VQ-1 (qualified pass). VQ-2 requires RI-01 (SRG-4, SRG-6) and RI-07 (CLA-1) to be resolved.

**Shortest route to VQ-2:**

1. **EP-01a [Reporting-coherence pack] targeting SRG-6 (B-1 through B-7)** — create a supplementary Table S1 that cross-references each of the ten characteristic features with the corresponding primary-paper table: for features 3–10, extract from [10a–c] and [13a,b] the measurement basis (GC yield with internal standard vs. isolated yield), the catalyst loading, temperature, solvent, and reaction time, and the key byproduct entries where applicable (β-hydride elimination product for eq. 2, chain-length distribution for eq. 6, full six-ligand ranking for feature 3). This single investment advances RI-01 across all six B-item components of SRG-6 simultaneously, at low experimental cost (it requires literature retrieval rather than new experiments).

2. **EP-01a [Reporting-coherence pack] targeting SRG-4 (B-8)** — recompute Fig. 2 citation counts from a named database (Web of Science Core Collection) using reproducible search strings for each of the three papers ([1]: "4374 AND 1972 AND Tamao AND JACS"; [10a]: "1958 AND 1976 AND Tamao AND BCSJ"; [10b]: "3347 AND 1982 AND Kumada") with self-citation exclusion specified; present raw year-by-year counts as a supplementary table. This advances RI-01 for SRG-4 at negligible experimental cost.

3. **EP-07a [Boundary-test pack] targeting CLA-1 (U-5, B-4)** — report yield and conditions for the fluorobenzene cross-coupling from the primary experimental literature (if the data exist in one of the [10] or [13] papers, cite and reproduce the relevant entry; if not, add an explicit acknowledgment that "rather low reactivity" is a qualitative observation without quantitative characterization, framing it as an anomalous boundary case that falls outside the ArCl-optimized scope). This advances RI-07 in CLA-1 without requiring new experiments — it requires either data retrieval from existing papers or explicit scope-limitation acknowledgment.

Certification-gate note: The experimental investment order follows information gain (step 1 advances the most RI-01 components simultaneously, step 2 advances the bibliometric dimension, step 3 closes the RI-07 gap), but the final VQ-2 certification requires that both RI-01 (SRG-4 and SRG-6) and RI-07 (CLA-1) are resolved; VQ-2 inherits the VQ-1 non-fatal RI-02 qualification.

---

**Objective function 2: VQ-3 (Mechanism)**

Prerequisite: VQ-2 achieved. Additional RIs to resolve: RI-03 (SRG-1, Primary), RI-06 (SRG-1, Secondary), RI-04 (SRG-3 and SRG-7). RI-05 (SRG-2) remains as qualifying condition; VQ-3 would be reached as "qualified" even if fully resolved.

**Shortest route to VQ-3 (from VQ-2):**

1. **EP-03a [Direct-observation / state-assignment pack] targeting SRG-1 (U-1, U-8)** — independently synthesize L₂Ni(Ph)(n-Bu)(dppp) by controlled transmetallation at low temperature (−78 °C, Et₂O) and characterize by ³¹P and ¹H NMR; then measure its thermal decay rate (product distribution between o-dibutylbenzene via reductive elimination and n-butylene via β-hydride elimination) at temperatures between −20 °C and +25 °C to extract ΔΔG‡ between the two competing pathways. This single experiment advances both RI-03 (directly observes and characterizes the key branch-point intermediate) and RI-06 (confirms that the stoichiometrically characterized Yamamoto-type intermediate is kinetically accessible under conditions consistent with the catalytic rate). Information gain: highest — simultaneously advances both Primary and Secondary RI of SRG-1.

2. **EP-04a [Discrimination / replication pack] targeting SRG-1 (U-1, radical mechanism discrimination)** — use (cyclopropylcarbinyl)magnesium chloride as a radical-clock Grignard under standard Ni(dppp)Cl₂/PhCl catalytic conditions (2 mol% Ni, Et₂O, 25 °C); quantify the ring-opened product (homoallyl group in the cross-coupling product) and ring-intact product by GC-MS. If ring-opening yield is <2% of the cross-coupling products, the Ni(I)/Ni(III) or radical-chain manifold is excluded at the kinetic resolution of the cyclopropylcarbinyl clock (~10⁸ s⁻¹ ring-opening rate). Information gain: high — directly resolves the mechanistic discrimination question for SRG-1. Feasibility: high — radical-clock experiments with Grignard reagents were established by 2001; the required magnesium reagent is commercially available or readily prepared from cyclopropylcarbinyl chloride.

3. **EP-04a [Discrimination / replication pack] targeting SRG-3 (U-2, prototype claim historiometry)** — retrieve [11a] (Yamamura, Murahashi, Moritani, J. Organomet. Chem. 91 (1975) C39) and identify in its text whether Scheme 1 or [1] is explicitly cited as the mechanistic source for the proposed Pd cycle; extend this targeted retrieval to the next five mechanistic Pd cross-coupling papers (1975–1980) and report the citation-context for each. If ≥3 of these 6 papers cite [1] in a mechanistic context (not only as a substrate-scope precedent), the prototype claim is supported at a 3/6 rate. This is a literature-retrieval exercise rather than an experiment, and it can be completed rapidly. Information gain: high for the prototype claim (SRG-3); does not advance SRG-1.

4. **EP-03a [Direct-observation / state-assignment pack] targeting SRG-2 (U-3, isomerization mechanism)** — perform a ¹³C isotope-labeling crossover experiment (α-¹³C-sec-butylmagnesium chloride) under Ni(dppp)Cl₂ and Ni(dmpe)Cl₂ conditions and analyze the ¹³C distribution in the isolated cross-coupling product by ¹H-decoupled ¹³C NMR. Label at C-2 (starting position) appearing predominantly at C-1 of the product indicates chain-walking on Ni; label retention at C-2 indicates Grignard pre-equilibration prior to transmetallation. This resolves U-3 (the mechanistic attribution question) and would reduce RI-05 (SRG-2) from "potentially qualifies VQ-3" to either "resolved[REDACTED: substantial verbatim quotation; see Tier 9]identified anomaly requiring further kinetic study" (if chain-walking on Ni is confirmed despite the expected directional reversal). Information gain: medium — advances SRG-2 only.

5. **EP-07a [Boundary-test pack] targeting SRG-7 (U-6, U-7, archival documentation)** — cite the received and accepted dates from the mastheads of [1] and [2] to partially corroborate the chronological independence claim; state explicitly whether ref [9]'s Ni(0)-ethylene work is documented in laboratory notebooks predating [1]'s submission, and flag this as an archival boundary if notebooks are unavailable. Information gain: lower for VQ-3 chemistry certification (SRG-7 is a historiographic SRG, not a mechanistic one), but required for Layer A and Layer B historiographic sub-certification.

Certification-gate note: The experimental investment order follows information gain (step 1 > step 2 > step 3 > step 4 > step 5), but the final VQ-3 certification is fixed by the gate order VQ-1 → VQ-2 → VQ-3 → VQ-4.

---

**Objective function 3: VQ-4 (Benchmark) — from VQ-3**

Prerequisite: VQ-3 achieved (including qualified). Additional RIs to resolve: RI-08 (SRG-5, SRG-6) and RI-09 (SRG-5).

**Shortest route to VQ-4 (from VQ-3):**

1. **EP-08a [Replication / uncertainty pack] targeting SRG-5 (U-4, Ni > Pd comparison)** — measure initial TOF (first 30 min) for Ni(dppp)Cl₂ and Pd(dppb)Cl₂ in ≥3 replicate parallel runs: 1 mol% catalyst, 4-chlorotoluene (1.0 equiv), PhMgBr (1.2 equiv), Et₂O, 25 °C; report mean ± SD for each catalyst and the TOF ratio Ni/Pd with propagated uncertainty; determine the rate-determining step by Hammett analysis across five para-substituted ArCl substrates. This advances RI-08 (SRG-5, lack of replicate measurements) and partially RI-09 (SRG-5, now a direct parallel comparison rather than external literature inference). Information gain: highest for VQ-4.

2. **EP-09a [Internal benchmark pack] targeting SRG-5 (C-10, RI-09)** — run a one-pot competition experiment with 0.5 mol% Ni(dppp)Cl₂ + 0.5 mol% Pd(dppb)Cl₂ and the ortho-dihalide substrate from eq. 5 (1,2-dichlorobenzene) with n-C₄H₉MgBr; determine by GC-MS the product distribution between Ni-selective monohalide coupling and Pd-based coupling. This provides the direct internal benchmark for the stepwise selectivity claim (feature 9) that currently rests only on external Pd literature. Advances RI-09 (SRG-5).

3. **EP-08a [Replication / uncertainty pack] targeting SRG-6 (B-1 through B-7, replication)** — run ≥3 replicate yield measurements for the standard representative reaction in each of features 3–10 (the six scope equations) and report mean ± SD for each; for eq. 2 (feature 4), run ≥3 replicates with GC internal standard and report yield and byproduct fractions (1-butylene, homocoupling) with SDs. This advances RI-08 across SRG-6. Information gain: medium — requires new experimental runs for six reactions.

Certification-gate note: The experimental investment order follows information gain, but the final VQ-4 certification is fixed by the gate order VQ-1 → VQ-2 → VQ-3 → VQ-4.

---

### §6 Contribution to institutional design

**New representative case for RI-06 (Imported model) — cycle-level import from stoichiometric to catalytic manifold:**

Tamao 2002 provides the first clean representative case in the corpus for the RI-06 "cycle-level import[REDACTED: substantial verbatim quotation; see Tier 9]combining[REDACTED: substantial verbatim quotation; see Tier 9]stoichiometric-to-catalytic import": cases in which a cycle constructed from stoichiometric elementary steps is asserted as operative under catalytic (sub-stoichiometric) conditions without kinetic evidence that the same intermediates are accessible in the turnover regime.

**New domain of application for RI-04 (Unreplicated discriminator) — historiometric claims in retrospective accounts:**

SRG-3 and SRG-7 reveal that RI-04 applies beyond the usual domain of experimental-data single data points to historiometric claims in retrospective scientific accounts. In SRG-3, the prototype claim rests on a single asserted discriminatory data point (the bare citation to [11a] as proof that Pd workers adopted Scheme 1). In SRG-7, the independent co-discovery claim rests on a single first-person recollection (submission-sequence memory from 30 years prior). Both satisfy the RI-04 definition: [REDACTED: substantial verbatim quotation; see Tier 9] The alternative pathways in the historiometric case are: (a) independent development from Wilkinson/Collman precedents (alternative to prototype adoption) and (b) parallel-awareness scenarios (alternative to independent co-discovery). This is a new category of RI-04 application that should be recorded in the Codebook application notes: [REDACTED: substantial verbatim quotation; see Tier 9]

**New representative case for RI-01 (Reporting integrity) — applied to bibliometric methodology:**

SRG-4 extends RI-01 from its standard domain of reaction-condition reporting (where the measurement frame is temperature, solvent, catalyst loading) to bibliometric methodology (where the measurement frame is database, search string, self-citation handling, year range). The Fig. 2 citation-trend argument fails RI-01 because cross-comparison between the three papers' citation trends is impossible without knowing whether they were searched in the same database with the same protocol. This is a new representative case: RI-01 applied to science-historical arguments in chemistry mini-reviews. It should be recorded as a domain-extension case in the Codebook application notes for RI-01.

**Era-norm dual classification — bibliometric and archival evidentiary standards:**

Two items (B-8 and U-6) receive dual classification (communication-era tolerated and modern-era deficient). This dual classification reveals an era-norm shift in a standard-type that is distinct from the measurement-precision shifts (qualitative to quantitative) previously documented in primary research papers. The bibliometric and archival evidentiary standard shift is a discipline-level methodological shift: what was acceptable as "generally recognized" or "as shown in Fig. 2[REDACTED: substantial verbatim quotation; see Tier 9]documentation-standard shift" vs. the previously documented "precision-standard shift."

**Labeling mismatch pattern detected:**

The paper presents Scheme 1 as a "proposed" catalytic cycle in the sentence [REDACTED: verbatim source quotation; see the source paper via its DOI] The hypothesis label ([REDACTED: verbatim source quotation; see the source paper via its DOI] [REDACTED: substantial verbatim quotation; see Tier 9] The transition from "proposed" to "has become" / "involves" is a labeling mismatch that co-occurs with RI-06 (cycle-level import), as predicted by the institutional-design pattern for this pattern. The mismatch is located at the section boundary between the discovery narrative (Section 1) and the characteristic features enumeration (Section 2): once the paper enters Section 2, the proposed cycle is treated as an established mechanistic framework rather than an analogy-based proposal. This is the canonical labeling-mismatch presentation: hypothesis label confined to the original-attribution sentence, factual verbs used throughout the scope and impact discussion.

**Self-contradictory-absence CLA confirmed (CLA-1) — new implementation type:**

CLA-1 (ArF scope exception) provides a new case-specific implementation of the self-contradictory-absence CLA check in a genre where it was not previously documented: a retrospective mini-review. In primary research papers, self-contradictory absences typically take the form [REDACTED: substantial verbatim quotation; see Tier 9] In a mini-review, the pattern takes the form [REDACTED: substantial verbatim quotation; see Tier 9] This is a genre-transposable implementation of the self-contradictory-absence check that extends the CLA detection criterion beyond primary experimental papers to review-format documents.

**Retrospective mini-review format as structural analogue of A-item collective deferral:**

Tamao 2002 contains zero A-items (no explicit deferrals to future work stated within the paper). Yet all ten characteristic features in Section 2 implicitly defer quantitative verification to the primary papers [10]–[18], none of which are reproduced within this document beyond the representative equations. The mini-review format functions as a structural collective-A-item: by genre convention, the format permits broad scope assertion while deferring the full evidentiary weight to cited primary papers. This creates an A-item analogue that is implicit and format-legitimated rather than explicit and author-stated. The Codebook application notes should record this as a genre-dependent variant: [REDACTED: substantial verbatim quotation; see Tier 9]

**No new PRI candidate detected:**

The patterns identified above (RI-06 stoichiometric-to-catalytic import, RI-04 historiometric application, RI-01 bibliometric application) all fit within existing codebook entries as domain extensions or scope-note additions. No new recurrence pattern was identified that would require a PRI-NN candidate code. This case confirms and expands the institutional design of the existing codebook without requiring new provisional codes.

---

> **Tier 8 redaction notice**: This file is a redacted copy of the corresponding Tier 3 / Tier 9 output. Verbatim source-paper quotations have been replaced by `[REDACTED: see source paper §<loc>; full text retained in Tier 9 reviewer-only deposit]` markers, preserving location references and our own analytical content. Bibliographic fields (title, authors, journal, year, DOI), analytical labels (`evidence_chain:` with B-/U-/A-/C- internal IDs), short technical terms, and our own analytical text are not redacted. The redaction was applied by `scripts/redact_for_tier8.py` and, for this version, by `scripts/build_paperA_R1_public.py` with `scripts/redact_source_ngram_runs.py` (scripts of the project repository; they are not deposited).
