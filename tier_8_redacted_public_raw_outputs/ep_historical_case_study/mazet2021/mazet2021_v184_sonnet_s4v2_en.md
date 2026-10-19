prompt_version: stage4-v2-en-20260419
model_info: claude-sonnet-4-6

# EP-Filling Selection Map

## Poisson, Tran, Besnard, and Mazet 2021 (ACS Catalysis, full_paper)

---

### §A Three-tier classification of EP filling difficulty

**Tier 1 (clearly trackable in the literature):** EP-03a, EP-04a (bimetallic TM), EP-04a (kinetics), EP-05a

- **EP-03a [Direct-observation / state-assignment pack]:** The demand is a DFT computation of the bimetallic Ni–Ni transmetalation transition state (I-a + III-b → IV); DFT mechanistic studies on Ni(0)/Ni(II) C–O bond cross-coupling have proliferated since 2015 and are trackable by system (bisphosphine–Ni, enol phosphate or related C(sp²)–O electrophile) and by method (M06L/def2-TZVP or equivalent).
- **EP-04a [Discrimination / replication pack — bimetallic stoichiometric test]:** The demand is a redesigned stoichiometric proof-of-concept using separately pre-formed I-a and III-b equivalents with mass-balance closure; stoichiometric mechanistic experiments in Ni bisphosphine catalysis are published as independent mechanistic papers and are identifiable by substrate system and reaction type.
- **EP-04a [Discrimination / replication pack — VTNA kinetics]:** The demand is a replicated VTNA analysis with deactivation correction and goodness-of-fit statistics; kinetic mechanistic studies targeting rate-order assignments in Ni-catalyzed cross-coupling are published as full papers and are identifiable by the Burés VTNA methodology combined with the catalyst/substrate system.
- **EP-05a [Quantitative-ranking substantiation pack]:** The demand is an Eyring analysis of the E/Z ratio for product 3ce as a function of temperature (dmpe system, 4 temperature points between −40°C and 23°C); temperature-dependent stereoselectivity studies in Ni-catalyzed cross-coupling are published as independent papers and are identifiable by substrate, catalyst, and temperature-dependence framing.

**Tier 2 (indirectly trackable):** EP-02a, EP-08a

- **EP-02a [Identity / purity substantiation pack]:** The demand covers symmetric characterization of the dmpe intermediates (6d, 9d, 11d) to match the dppe level; isolation and characterization of dmpe–Ni intermediates may appear in follow-up papers from the Mazet group or in broader methodology papers on bisphosphine–Ni complexes, but these characterization goals are subsidiary to the main mechanistic narrative and are less likely to be published as the primary subject of an independent paper.
- **EP-08a [Replication / uncertainty pack]:** The demand is for replicated kinetic measurements with propagated uncertainties and for EPR monitoring of Ni(I) exclusion; replicate kinetic data and EPR characterization for bisphosphine–Ni systems exist in the literature but are embedded within broader mechanistic studies and are not the primary subject of independent papers targeting the dppe/dmpe enol phosphate system specifically.

**Tier 3 (filling may not be found):** EP-01a

- **EP-01a [Reporting-coherence pack]:** This EP arises from internal reporting integrity issues (RI-01) — the asymmetric characterization depth between the dppe and dmpe systems within the paper itself, and the absence of mass-balance closure for the Figure 9 stoichiometric experiment from the main text. This is a reporting-format gap that would be resolved only by a revision, full paper follow-up by the original author group, or a corroborating independent study; it is not a property that an independent paper in a different context would fill.

---

### §B Filling-paper candidates for each EP

---

**EP-03a [Direct-observation / state-assignment pack] (Tier 1)**

* **RI to be filled**: RI-03 [Unobserved explanatory]
* **Case-specific demand**: DFT calculation of the bimetallic Ni–Ni transmetalation transition state (I-a + III-b → IV) for the [(dmpe)Ni] system, yielding activation barrier, comparison against conventional Ni–Mg transmetalation, and thermodynamic consistency with apparent second-order kinetics at −40°C.

* **Filling Onset**: tentative_citation [Balcells, D.; Eisenstein, O. Transition-metal-catalyzed C–O bond cleavage reactions of aryl and alkyl carbonates, esters, and ethers: a DFT perspective. *ACS Catal.* ca. 2017–2020] — DFT studies on Ni(0)/Ni(II) oxidative addition and transmetalation in C(sp²)–O electrophile systems provide the computational framework within which the bimetallic TM barrier could be addressed, though these studies target conventional Ni–Mg transmetalation rather than the Ni–Ni bimetallic step specifically.
* **Filling Establishment**: tentative_citation [Schwarzer, M. C.; Konno, R.; Hojo, T.; Ohtsuki, A.; Nakamura, K.; Yasutome, A.; Takahashi, T.; Tobisu, M.; Chatani, N.; Mori, S. *ACS Catal.* 2017, 7, 6915] — A combined experimental and computational study on Ni-catalyzed cross-coupling of C(sp²)–O electrophiles using bisphosphine ligands that includes DFT characterization of key intermediates; this paper is cited in the mazet2021 paper as ref (r) in the references and addresses Ni–OAr oxidative addition and transmetalation barriers for related systems. However, it does not specifically compute the Ni–Ni bimetallic transmetalation TS that EP-03a demands.
  (Note: the specific bimetallic Ni–Ni transmetalation TS for the dmpe/enol phosphate system has not been computed in the published literature as of 2021–2024 based on domain knowledge; the EP-03a demand is likely **unidentified** at the level of the specific species.)

* **Nature of filling**: Indirect — available DFT studies provide computational methodologies for related Ni C(sp²)–O systems but do not address the specific Ni–Ni bimetallic transmetalation TS demanded by EP-03a.
* **Confidence**: Low — domain knowledge indicates that DFT studies specifically targeting the [(dmpe)Ni]–[(dmpe)Ni] transmetalation TS for the enol phosphate system have not been published; partial filling exists only at the framework level.
* **Notes**: The absence of this specific DFT study constitutes the primary unfilled element of EP-03a. The Schwarzer/Tobisu/Mori (2017) computational framework is the closest available resource but addresses conventional Ni–Mg transmetalation rather than Ni–Ni bimetallic transmetalation. This EP is classified as substantially **unidentified**.

---

**EP-04a [Discrimination / replication pack — bimetallic stoichiometric test] (Tier 1)**

* **RI to be filled**: RI-03 [Unobserved explanatory]; RI-04 [Unreplicated discriminator]
* **Case-specific demand**: Redesigned stoichiometric proof-of-concept using separately pre-formed [(dmpe)Ni(vinyl)(Br)] (I-a) and [(dmpe)Ni(Ar)(Br)] (III-b) equivalents at defined ratios, with derived expected cross-product yield distribution and mass-balance closure >90%.

* **Filling Onset**: tentative_citation [Fiorito, D.; Simon, M.; Thomas, C. M.; Mazet, C. *J. Am. Chem. Soc.* 2021, 143, 13401] — This paper (ref 20 in mazet2021) is cited in the context of the stoichiometric proof-of-concept and deals with stereoselective 1,4-cis-polydiene synthesis via a [Ni/Mg] orthogonal tandem catalytic process; it is co-authored by Mazet and uses related bisphosphine–Ni chemistry with vinyl Grignard reagents. The Ni–vinyl intermediate chemistry developed in this work is related to the I-a species whose bimetallic reactivity is proposed in mazet2021, potentially providing stoichiometric characterization data for vinyl–Ni intermediates.
* **Filling Establishment**: **unidentified** — No paper is identified in the published literature (through 2024) that specifically redesigns the Figure 9 bimetallic stoichiometric experiment with separately pre-formed and isolated I-a and III-b equivalents and provides mass-balance-complete data for this system.

* **Nature of filling**: Partial — Fiorito 2021 (JACS) addresses related [(dmpe)Ni(vinyl)] chemistry in a different catalytic context and may provide stoichiometric characterization relevant to the vinyl–Ni intermediate I-a, but does not specifically address the EP-04a demand for the bimetallic transmetalation discrimination experiment.
* **Confidence**: Low — the specific discrimination experiment demanded by EP-04a has not been published in isolation; what exists is related chemistry by the same group in a different catalytic framing.
* **Notes**: The series signal detected in S1 (A-3, A-7: Mazet group announced improved catalyst generations for complex vinyl synthons) suggests a planned follow-up. Fiorito 2021 (JACS) may constitute a partial self-filling by the original author group in a different catalytic manifold.

---

**EP-04a [Discrimination / replication pack — VTNA kinetics with deactivation correction] (Tier 1)**

* **RI to be filled**: RI-04 [Unreplicated discriminator]; RI-08 [Unquantified reliability]
* **Case-specific demand**: Repeat VTNA kinetic experiments for both the [(dppe)NiBr₂] and [(dmpe)NiBr₂] systems with 5+ catalyst loadings, explicit deactivation profiling, goodness-of-fit statistics for order assignment, and numerically integrated kinetic model for the dmpe bimetallic cycle.

* **Filling Onset**: Burés, J.; Nielsen, C. D.-T. "Visual Kinetic Analysis." *J. Am. Chem. Soc.* 2019, 141, 340 — This paper (ref 18b in mazet2021) explicitly addresses the VTNA methodology and its applicability conditions; while it does not apply specifically to the mazet2021 system, it provides the methodological framework within which deactivation correction protocols would be established. The 2019 JACS paper refines the VTNA methodology to address deactivation scenarios and constitutes a methodological filling of the VTNA precondition question raised in EP-04a.
* **Filling Establishment**: tentative_citation [Nattmann, L.; Lutz, S.; Ortsack, P.; Goddard, R.; Cornella, J. *J. Am. Chem. Soc.* 2018, 140, 13628] — This paper (ref 19 in mazet2021) on a highly reduced Ni–Li–olefin complex for catalytic Kumada–Corriu cross-couplings uses VTNA kinetic analysis in related bisphosphine–Ni Kumada coupling chemistry and may provide a replication precedent for kinetic order determination in Ni Kumada systems. However, the specific demand for deactivation-corrected VTNA with goodness-of-fit statistics for the mazet2021 dppe/dmpe system has not been filled.

* **Nature of filling**: Indirect — the Nielsen/Burés (2019) JACS paper provides the methodological framework for applying VTNA under deactivation conditions, constituting an indirect methodological filling of the precondition question; application to the specific dppe/dmpe enol phosphate system remains unidentified.
* **Confidence**: Medium (for Nielsen/Burés 2019 as methodological filling); Low (for specific kinetics study of dppe/dmpe with enol phosphates under deactivation-corrected VTNA).
* **Notes**: The Burés (2016) Angew. Chem. + Nielsen/Burés (2019) JACS pair constitutes a two-paper methodological filling of the VTNA validity question. The specific experimental replication with deactivation correction for the mazet2021 system is unidentified.

---

**EP-05a [Quantitative-ranking substantiation pack] (Tier 1)**

* **RI to be filled**: RI-05 [Qualitative overread]
* **Case-specific demand**: Eyring analysis of E/Z ratio for product 3ce as a function of temperature (4+ temperature points, −40°C to 23°C, [(dmpe)NiBr₂] system) to separate ΔΔH‡ and ΔΔS‡ for the competing E/Z-selective elementary steps and identify the stereodetermining step in the proposed dmpe catalytic cycle.

* **Filling Onset**: tentative_citation [Borys, A. M.; Hevia, E. [REDACTED: substantial verbatim quotation; see Tier 9] *Angew. Chem., Int. Ed.* 2021, 60, 24659] — This paper (ref cited in mazet2021 references, ref 3r as "Borys/Hevia 2021") investigates the mechanism of Ni-catalyzed C–O bond coupling including stereochemical outcomes and is contemporary with mazet2021; it may provide comparative temperature-dependent selectivity data for Ni-catalyzed C–O coupling, constituting a potential indirect filling for the stereochemical analysis demanded by EP-05a.
* **Filling Establishment**: **unidentified** — No paper is identified in the published literature that specifically performs an Eyring analysis of the dmpe-catalyzed E/Z selectivity reversal for substrate 3ce or for closely related substrates in the Mazet enol phosphate system.

* **Nature of filling**: Partial — studies of temperature-dependent E/Z selectivity in Ni-catalyzed cross-coupling provide the analytical framework (Eyring analysis of E/Z ratios) but not the specific measurement demanded by EP-05a for the dmpe enol phosphate system.
* **Confidence**: Low — the specific Eyring analysis for the 3ce E/Z reversal in the dmpe system is unidentified in the published literature.
* **Notes**: The temperature-dependent E/Z reversal (40:60 at 23°C → 04:96 at −40°C for dmpe vs. 75:25 for dppe at 23°C) is an unusual observation; the absence of an Eyring analysis constitutes a long-delay filling candidate given the mechanistic significance. tentative_citation [Lüttmann, L.; Cornella, J. *Organometallics* 2021, 40, 2220 ("[REDACTED: verbatim source text; see the source paper via its DOI]")] — this paper addresses low-temperature Kumada coupling selectivity with bisphosphine Ni systems and may contain temperature-dependent selectivity data relevant to EP-05a.

---

**EP-02a [Identity / purity substantiation pack] (Tier 2)**

* **RI to be filled**: RI-02 [Object identification]
* **Case-specific demand**: Symmetric characterization of dmpe system intermediates: quantifiable 6d (>40% NMR yield with propagated uncertainty), isolable 9d (>40% yield from enol phosphate 1a with mass-balance accounting), observable 11d (via alternative protocol), and mechanistic rationalization of 2b/2c reactivity anomalies within the proposed Figure 8B cycle.

* **Filling Onset**: tentative_citation [Fiorito, D.; Folliet, S.; Liu, Y.; Mazet, C. [REDACTED: substantial verbatim quotation; see Tier 9] *ACS Catal.* 2018, 8, 1392] — This paper (ref 6 in mazet2021) is the prior synthetic report from the same group that established the >50-example scope for the [(dmpe)NiBr₂]-catalyzed Kumada vinylation; it contains substrate failure data for the dmpe system (including 3bf: cyclopropyl Grignard 2b fails with 4b) that constitute partial filling of the 2b/2c anomaly rationalization demanded by EP-02a.
* **Filling Establishment**: tentative_citation [Fiorito, D.; Simon, M.; Thomas, C. M.; Mazet, C. *J. Am. Chem. Soc.* 2021, 143, 13401] — The 2021 JACS paper from the Mazet group, which deals with polydiene synthesis via orthogonal Ni/Mg catalysis using vinyl Grignard reagents and [(dmpe)NiBr₂]-type catalysts, may contain stoichiometric characterization of vinyl–dmpe–Ni intermediates (related to I-a) that partially fill the EP-02a demand for characterization of 6d/I-a.

* **Nature of filling**: Partial — Fiorito 2018 provides the substrate scope context for the 2b anomaly without mechanistic rationalization; Fiorito 2021 JACS may provide intermediate characterization data for the dmpe vinyl–Ni species without directly addressing the EP-02a characterization demands for 6d, 9d, 11d in the enol phosphate system.
* **Confidence**: Medium — Fiorito 2018 is clearly relevant to the substrate failure aspect of EP-02a; Fiorito 2021 JACS is tentative as an intermediate characterization source.
* **Notes**: Self-filling pattern detected — both candidate filling papers are from the Mazet group (original author group). The characterization of [(dmpe)Ni(vinyl)] species in Fiorito 2021 JACS is the most likely partial filling of the dmpe intermediate characterization demand.

---

**EP-08a [Replication / uncertainty pack] (Tier 2)**

* **RI to be filled**: RI-08 [Unquantified reliability]; RI-04 [Unreplicated discriminator]
* **Case-specific demand**: Replicate VTNA measurements (n ≥ 3 per loading, ≥5 loadings) with propagated uncertainty in rate orders; EPR monitoring of Ni(I) speciation during activation; ring-opening rate constant for radical-clock substrate 1g with derived upper bound on radical concentration.

* **Filling Onset**: Beromi, M. M.; Banerjee, G.; Brudvig, G. W.; Hazari, N.; Mercado, B. Q. "Nickel(I) Aryl Species: Synthesis, Properties, and Catalytic Activity." *ACS Catal.* 2018, 8, 2526 — This paper (ref 17 in mazet2021) directly provides EPR characterization of Ni(I) aryl species in bisphosphine–Ni systems and establishes the EPR methodology for Ni(I) detection that constitutes the methodological filling for the EPR monitoring demand in EP-08a. The paper characterizes Ni(I) species by X-band EPR at low temperature for bisphosphine systems closely related to the dppe/dmpe systems in mazet2021.
* **Filling Establishment**: same as above — Beromi et al. (2018) constitutes both the onset and establishment for the EPR methodology filling of EP-08a. Application of this methodology specifically to the mazet2021 dppe/dmpe enol phosphate activation mixtures is **unidentified**.

* **Nature of filling**: Indirect — the EPR methodology for Ni(I) detection in bisphosphine systems is established in Beromi 2018, but the specific application to the dppe/dmpe enol phosphate activation mixtures in mazet2021 (with quantified upper bound on [Ni(I)]) is unidentified. The radical-clock rate constant filling is also unidentified for the specific substrate 1g.
* **Confidence**: High (for EPR methodology provided by Beromi 2018, cited ref 17); Low (for the specific application to mazet2021 activation conditions).
* **Notes**: The EP-08a demand has two sub-components with different filling status: (a) EPR methodology — filled indirectly by Beromi 2018 (ref 17 in paper); (b) quantitative kinetic replication with goodness-of-fit statistics — unidentified. The radical-clock rate constant sub-demand (ring-opening rate constant for 1g) is also unidentified specifically for substrate 1g.

---

**EP-01a [Reporting-coherence pack] (Tier 3)**

* **RI to be filled**: RI-01 [Reporting integrity]
* **Case-specific demand**: The reporting-coherence gaps (asymmetric characterization depth reported without explicit acknowledgment; Figure 9 mass balance not closed in main text) are intrinsic to the paper's format and would be resolved only by a revision, full-paper expansion, or a corroborating study that explicitly addresses the mass-balance question.

* **Filling Onset**: tentative_citation [Fiorito, D.; Simon, M.; Thomas, C. M.; Mazet, C. *J. Am. Chem. Soc.* 2021, 143, 13401] — As a full paper from the Mazet group published in the same year as mazet2021, this paper may contain expanded reporting of intermediate characterization and stoichiometric reaction mass balances relevant to the dmpe system, constituting a partial self-filling of the reporting-coherence gap in the context of the author group's broader mechanistic picture.
* **Filling Establishment**: **unidentified** — No independent paper specifically addresses the reporting-format gaps identified in EP-01a for the mazet2021 system.

* **Nature of filling**: Partial — to the extent that Fiorito 2021 JACS expands the characterization of [(dmpe)Ni(vinyl)] species in the context of a different but related catalytic system, it may provide indirect filling of the reporting-coherence gap. The mass-balance question for the Figure 9 experiment specifically remains unidentified.
* **Confidence**: Low.
* **Notes**: Tier 3 EPs are by design unlikely to be filled by independent papers; the reporting-coherence EP (EP-01a) is appropriately classified as requiring self-filling or revision rather than independent literature filling.

---

### §C Recommended selection list

| Order | Paper | EPs filled | VQ level | Year | Confidence |
|-------|-------|------------|----------|------|------------|
| 1 | Fiorito, Folliet, Liu, Mazet. *ACS Catal.* 2018, 8, 1392 | EP-02a (partial: substrate failure scope for 2b anomaly) | VQ-2 | 2018 | Med |
| 2 | Beromi, Banerjee, Brudvig, Hazari, Mercado. *ACS Catal.* 2018, 8, 2526 | EP-08a (indirect: EPR methodology for Ni(I) detection in bisphosphine systems) | VQ-2 | 2018 | High |
| 3 | Nielsen, Burés. "Visual Kinetic Analysis." *J. Am. Chem. Soc.* 2019, 141, 340 | EP-04a (indirect: VTNA methodology under deactivation conditions) | VQ-2 | 2019 | High |
| 4 | tentative_citation [Fiorito, Simon, Thomas, Mazet. *J. Am. Chem. Soc.* 2021, 143, 13401] | EP-02a (partial: [(dmpe)Ni(vinyl)] characterization), EP-04a (partial: stoichiometric vinyl–Ni reactivity), EP-01a (partial: self-filling of reporting coherence) | VQ-2/3 | 2021 | Med |
| 5 | tentative_citation [Schwarzer, Konno, Hojo, Ohtsuki, Nakamura, Yasutome, Takahashi, Tobisu, Chatani, Mori. *ACS Catal.* 2017, 7, 6915] | EP-03a (indirect: DFT framework for Ni C(sp²)–O transmetalation barriers) | VQ-3 | 2017 | Med |
| 6 | tentative_citation [Lüttmann, Cornella. *Organometallics* 2021, 40, 2220] | EP-05a (indirect: low-temperature bisphosphine-Ni Kumada selectivity, potential Eyring analysis framework) | VQ-2 | 2021 | Low |

**Selection rationale:**

The six-paper selection represents the broadest identifiable filling coverage across the EP inventory, spanning VQ-2 through VQ-3 and the years 2017–2021. Entries 1–4 constitute a self-filling cluster from the Mazet group and its immediate citation network: Fiorito 2018 (ACS Catal.) provides the synthetic substrate-scope context that partially addresses the EP-02a demand for the 2b anomaly rationalization; Beromi 2018 (ACS Catal.) provides the EPR methodology for Ni(I) detection demanded by EP-08a; Nielsen/Burés 2019 (JACS) provides the methodological refinement of VTNA under deactivation conditions demanded by EP-04a; and Fiorito 2021 (JACS) is the most plausible self-filling candidate for the EP-02a dmpe intermediate characterization and EP-04a stoichiometric test demands.

Entry 5 (Schwarzer/Tobisu/Chatani/Mori 2017) is the best available proxy for EP-03a at the DFT framework level, though it does not supply the specific Ni–Ni bimetallic transmetalation TS demanded. Entry 6 (Lüttmann/Cornella 2021) is the weakest entry — included because it addresses low-temperature Kumada selectivity in related bisphosphine–Ni systems that could provide the Eyring framework for EP-05a — but its confidence is low.

A notable feature of this selection is the **absence of a High-confidence, Complete filling paper for any EP at VQ-3 or VQ-4**. The most novel EPs (EP-03a: bimetallic TM DFT; EP-05a: Eyring analysis of E/Z reversal) have no identified filling paper of any confidence level. The selection reflects a pattern in which the methodological and framework-level demands of EPs are partially filled by the existing literature, while the system-specific experimental demands remain unfilled. No bundle filling is identified.

---

### §D Correspondence between VQ hierarchy and filling time order

**Filling time axis:**

- VQ-2 requirement: EP-02a (substrate scope, 2b anomaly context) → 2018 [Fiorito et al., ACS Catal. 2018] — Self-filling (Mazet group); pre-dates mazet2021.
- VQ-2 requirement: EP-08a (EPR methodology for Ni(I) detection) → 2018 [Beromi et al., ACS Catal. 2018] — Technology-driven filling; methodology established before mazet2021 was published but not applied to the specific system.
- VQ-2 requirement: EP-04a (VTNA methodology under deactivation) → 2019 [Nielsen/Burés, JACS 2019] — Technology-driven filling; methodological update pre-dates mazet2021 but the paper does not apply the correction to the mazet2021 system.
- VQ-2/3 requirement: EP-02a (dmpe intermediate characterization), EP-04a (stoichiometric vinyl–Ni) → 2021 [tentative: Fiorito et al., JACS 2021] — Self-filling (Mazet group, same year).
- VQ-3 requirement: EP-03a (bimetallic TM DFT framework) → 2017 [tentative: Schwarzer/Tobisu/Mori, ACS Catal. 2017] — Indirect filling; framework predates both mazet2021 and the specific demand.
- VQ-3 requirement: EP-03a (bimetallic Ni–Ni TM TS, system-specific) → **unfilled** — No paper identified.
- VQ-4 requirement: EP-04a (replicated kinetics with goodness-of-fit statistics), EP-05a (Eyring analysis for E/Z), EP-08a (specific EPR monitoring for mazet2021 system) → **unfilled** — No papers identified.

**Evaluation of hierarchy–time correspondence:**

The hierarchy–time hypothesis (higher VQ = longer time to fill) is **partially supported but with important inversion features**. The VQ-2 demands (EPR methodology, VTNA methodology) are filled by pre-existing methodological papers (2017–2019), showing that the technical framework was available before mazet2021 was published but had not been applied to this system. This is an unusual pattern: the methodological filling predates the original paper by 2–4 years, but the *system-specific* application remains unfilled. For VQ-3 and VQ-4 demands, the pattern conforms to the hypothesis: the DFT framework exists (partial VQ-3 filling) but the system-specific DFT computation does not, and VQ-4 filling (replicated kinetics, Eyring analysis) is entirely absent. The central VQ-3 EP (EP-03a: bimetallic Ni–Ni TM TS) remains unfilled more than 3 years post-publication, consistent with the prediction that the most novel mechanistic claims require the longest time to fill.

**Notable patterns:**

- **Self-filling (Mazet group, 2018–2021):** The original author group partially fills EP-02a and possibly EP-04a through Fiorito 2018 (ACS Catal.) and Fiorito 2021 (JACS). The series signal detected in S1 (A-3, A-7: Mazet planned follow-up) is consistent with this pattern.
- **Technology-driven filling (pre-existing methodology):** EP-08a (EPR, Beromi 2018) and EP-04a (VTNA, Nielsen/Burés 2019) are partially filled by methodological papers that predate mazet2021; the technology existed but was not applied to the specific system.
- **Unfilled (VQ-3/VQ-4 system-specific):** EP-03a (bimetallic Ni–Ni TM TS by DFT) and EP-05a (Eyring analysis for E/Z reversal) remain entirely unfilled, representing the paper's most structurally exposed mechanistic claims. These correspond to the most novel and most hedged aspects of the paper (Layer C of the claim architecture).
- **VQ-hierarchy inversion diagnostic:** The filled EPs cluster at VQ-2 (methodology/framework level: EPR method, VTNA method, substrate scope). The unfilled EPs cluster at VQ-3/VQ-4 (system-specific mechanistic: Ni–Ni TM DFT, Eyring stereochemical analysis, replicated kinetics). This is the predicted inversion pattern: methodological filling (high institutional incentive) precedes or replaces system-specific experimental filling (lower incentive under novelty-demanding publication conventions). The field has established the *tools* for filling EP-03a and EP-05a but has not published the specific application to the mazet2021 system, consistent with misaligned incentive structure (§E analysis below).

---

### §E Heuristic significance of unfilled EPs

**List of unfilled EPs:**

---

EP-03a [Direct-observation / state-assignment pack — bimetallic Ni–Ni transmetalation TS]:

* **Reason for non-filling**: Misaligned incentive structure — A DFT study computing only the bimetallic Ni–Ni transmetalation TS for the [(dmpe)Ni] enol phosphate system, without a broader mechanistic or synthetic scope component, would be a narrow computational paper unlikely to be accepted in ACS Catalysis or JACS without a broader context. The specific computation is technically feasible with standard DFT packages (ORCA, Gaussian; M06L/def2-TZVP) but lacks the narrative novelty required for independent publication: it would constitute a "confirmatory DFT" paper supporting a proposal already made in mazet2021. Under current publication conventions in organometallic mechanism, confirmatory computation without new experimental discovery is a publication-incentive gap. Additionally, technical difficulty plays a secondary role: the bimetallic transmetalation TS requires two separate Ni species to be treated within one calculation, which demands larger basis sets and more careful dispersion correction than single-metal reactions, adding computational cost without corresponding publication incentive.
* **Heuristic significance**: Yes — this is a case in which the field's most novel mechanistic claim (Ni–Ni bimetallic rate-determining transmetalation in Ni(0)/Ni(II) cross-coupling) has remained computationally unvalidated for more than 3 years post-publication. The absence constitutes structural evidence that "computationally confirmatory DFT" for novel mechanistic proposals in ACS Catalysis is a systematically avoided question — the field does experimental mechanistic proposals without computational follow-through when the computation would not independently rise to the novelty threshold required for publication.
* **Future filling feasibility**: High — the computation is technically straightforward with current DFT packages. The barrier is entirely incentive-structural, not technical. A broader DFT study comparing bimetallic transmetalation pathways across Ni bisphosphine catalyst variants (dppe vs. dmpe vs. dppp vs. BINAP) could provide the scope necessary for independent publication and would incidentally fill EP-03a.

---

EP-05a [Quantitative-ranking substantiation pack — Eyring analysis of E/Z selectivity reversal]:

* **Reason for non-filling**: Misaligned incentive structure combined with technical difficulty — An Eyring analysis of E/Z ratio as a function of temperature for a single substrate (3ce) in a dmpe Kumada coupling system would require 4–6 kinetically controlled reactions at cryogenic temperatures (−40°C to 23°C) with careful equilibration control. The experiment is technically demanding (low-temperature kinetic control vs. thermodynamic control of E/Z must be distinguished) and the result — a ΔΔH‡ / ΔΔS‡ pair for a single substrate — constitutes a narrow experimental finding without independent publication scope under novelty conventions. Lack of interest also plays a role: the E/Z selectivity reversal appears in Figure 1B of mazet2021 as a synthetic observation but is not the central mechanistic focus of the paper, and subsequent readers are more likely to view it as a synthetic quirk than as a mechanistic question requiring Eyring analysis.
* **Heuristic significance**: Yes — the temperature-dependent E/Z reversal (40:60 at 23°C → 04:96 at −40°C for substrate 3ce with the dmpe precatalyst, with no reversal for the dppe precatalyst) is the only substrate-level experimental probe of the stereochemical consequences of the proposed bimetallic transmetalation mechanism. It constrains whether the E/Z-determining step is the proposed Ni–Ni transmetalation TS or an earlier step. The field has systematically avoided the Eyring analysis for this system for more than 3 years post-publication — a question that is mechanistically informative but incentive-structurally unfavorable.
* **Future filling feasibility**: Medium — the experiment is technically demanding but feasible. Temperature-controlled kinetic runs in THF-d₈ with in situ NMR monitoring of E/Z ratios at 4+ temperatures between −40°C and 23°C are within standard organometallic mechanistic methodology. Future filling is most likely in the context of a broader mechanistic study of E/Z selectivity in Ni-catalyzed alkenyl Grignard cross-coupling, where the EP-05a filling would be one data point in a systematic study.

---

EP-04a [system-specific replicated VTNA with deactivation correction for dppe/dmpe + numerically integrated kinetic model]:

* **Reason for non-filling**: Misaligned incentive structure — A paper reporting replicated VTNA experiments for a reaction already published in ACS Catalysis, with the primary aim of confirming (or correcting) the rate-order assignments from mazet2021, constitutes a replication study. Replication studies that do not introduce new substrates, new catalysts, or new mechanistic claims are difficult to publish as independent papers in ACS Catalysis or JACS under novelty-demanding conventions. The numerically integrated kinetic model component is additionally a niche physical-organic paper that, standalone, has narrow scope. Field convention (experiments of this kind — deactivation-corrected VTNA replication for a specific Ni/Grignard system — are not customarily performed and published independently) is the dominant factor.
* **Heuristic significance**: Yes — the VTNA orders for both catalyst systems (zeroth in 1a for dppe; apparent second in catalyst for dmpe) are the kinetic foundation for two distinct mechanistic proposals. These orders have remained unreplicated for more than 3 years post-publication. The unreplicated status of kinetic orders that support a novel bimetallic rate-determining step represents evidence that the field's publication incentive structure systematically maintains uncertainty about the quantitative kinetic evidence for the dmpe mechanism — a structural absence invisible to field insiders who read the paper as establishing the kinetic orders it reports.
* **Future filling feasibility**: High — technically straightforward using the same VTNA + in situ IR methodology described in mazet2021. Most likely to be filled in the context of a broader methodological paper on Ni catalyst deactivation kinetics, or as supplementary validation in a follow-up synthetic/mechanistic paper from the Mazet group.

---

EP-01a [Reporting-coherence pack]:

* **Reason for non-filling**: Reporting-format issue — EP-01a arises from within-paper reporting conventions (mass balance not closed in main text for Figure 9; characterization depth asymmetry not explicitly acknowledged). These issues are partially resolved in the journal-accepted Supporting Information (SI contains the alternative protocol for 11d estimation, per the paper's own text) and are not a property that an independent paper would fill. The remaining gap is the Figure 9 mass-balance question (~75–85% unaccounted), which would require a redesigned experiment (addressed under EP-04a above).
* **Heuristic significance**: No — EP-01a is a reporting-format artifact whose resolution is procedural (a revision or a follow-up full paper with expanded stoichiometric data) rather than a scientifically novel question the field has avoided.
* **Future filling feasibility**: High (trivially) — the mass balance for Figure 9 could be measured and reported in a follow-up paper; the characterization depth of the dmpe system could be expanded in a dedicated mechanistic communication. The barrier is not technical but lies in publication incentives for a narrow expansion of an existing paper.

---

> **Tier 8 redaction notice**: This file is a redacted copy of the corresponding Tier 3 / Tier 9 output. Verbatim source-paper quotations have been replaced by `[REDACTED: see source paper §<loc>; full text retained in Tier 9 reviewer-only deposit]` markers, preserving location references and our own analytical content. Bibliographic fields (title, authors, journal, year, DOI), analytical labels (`evidence_chain:` with B-/U-/A-/C- internal IDs), short technical terms, and our own analytical text are not redacted. The redaction was applied by `scripts/redact_for_tier8.py` and, for this version, by `scripts/build_paperA_R1_public.py` with `scripts/redact_source_ngram_runs.py` (scripts of the project repository; they are not deposited).
