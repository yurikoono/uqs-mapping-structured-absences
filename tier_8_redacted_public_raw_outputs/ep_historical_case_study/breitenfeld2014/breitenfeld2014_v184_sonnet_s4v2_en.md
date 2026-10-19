prompt_version: stage4-v2-en-20260419
model_info: claude-sonnet-4-6

# EP-Filling Selection Map

## Breitenfeld, Wodrich, and Hu 2014 (Organometallics, full_paper)

---

### §A Three-tier classification of EP filling difficulty

**Tier 1 (clearly trackable in the literature):** EP-04a, EP-03a
  — EP-04a: The demand for quasi-RRHO correction and DLPNO-CCSD(T) benchmarking of Ni(III) barrier heights is a concrete computational question; independent benchmarking papers exist from ca. 2012–2016.
  — EP-03a: Spectroscopic characterization of Ni(III) aryl alkyl intermediates and spin-state assignment for open-shell singlet TSs were independently pursued by the Mirica group (2014) for parallel research purposes.

**Tier 2 (indirectly trackable):** EP-06a, EP-07a, EP-05a, EP-08a, EP-01a
  — EP-06a: Comproportionation (Ni(I) + Ni(III) → 2 Ni(II)) thermodynamics appear in the Ni-photoredox dual-catalysis literature (2018–2023) but not as an independent paper on the Nickamine system.
  — EP-07a: Activation parameters for Nickamine's TDS at room temperature do not appear as the primary subject of any independent paper; the gap is addressed only incidentally within later Hu group papers, if at all.
  — EP-05a: The statistical methodology gap (confidence intervals on log-log kinetic orders) is addressed at the field level by the Burés 2016 VTNA paper, not by a Nickamine-specific reanalysis.
  — EP-08a: GC yield and conversion data for radical-clock experiments appear in the alkyl–alkyl predecessor (Breitenfeld 2013) by analogy; no alkyl–aryl-specific replication paper identified.
  — EP-01a: Propyl/hex-5-en-1-yl truncation validation for Nickamine is unlikely to appear as an independent paper; would be buried in SI of a subsequent Hu/Wodrich computational paper.

**Tier 3 (filling may not be found):** none
  — All EPs derive from RI-03, RI-04, RI-06, RI-07, RI-08, PRI-11 types rather than RI-01 reporting-format or RI-08 replication-convention types that most strongly predict Tier 3.

---

### §B Filling-paper candidates for each EP

**EP-04a [Discrimination / replication pack] (Tier 1)**

* **RI to be filled**: RI-04 [Unreplicated discriminator] (primary); RI-06 [Imported model] (secondary)
* **Filling Onset**: Grimme, S. *Chem. Eur. J.* 2012, 18, 9955–9964 — quasi-RRHO entropy correction for transition-metal complex free-energy calculations; directly addresses the RRHO overestimation for B1 + Pr• → B2 acknowledged in the paper. **[tentative_citation: Grimme 2012 Chem. Eur. J. — title "Supramolecular Binding Thermodynamics by Dispersion-Corrected DFT" needs exact verification; high confidence on existence and year]**
* **Filling Establishment**: Laplaza, R.; Wodrich, M. D.; Corminboeuf, C. *J. Chem. Theory Comput.* ca. 2021 — EPFL computational group (same as Breitenfeld 2014 co-author) benchmarked PBE0-dDsC variants for organometallic thermochemistry. **[tentative_citation: title and pages need verification]**; DLPNO-CCSD(T) accuracy for 3d-metal barriers addressed by Liakos and Neese (*JCTC* ca. 2015). **[tentative_citation: exact title/pages need verification]**
* **Nature of filling**: Partial — Grimme 2012 fills the RRHO entropy element; Wodrich/Corminboeuf series partially fills functional-adequacy; Ni(III) d7-specific DLPNO benchmarking is not a single definitive paper.
* **Confidence**: Medium

---

**EP-03a [Direct-observation / state-assignment pack] (Tier 1)**

* **RI to be filled**: RI-03 [Unobserved explanatory] (primary); RI-08 [Unquantified reliability] (secondary)
* **Filling Onset**: Zheng, B.; Tang, F. Z.; Luo, J.; Schultz, J. S.; Rath, N. P.; Mirica, L. M. *J. Am. Chem. Soc.* 2014, 136, 6499–6504 — isolated and characterized (X-ray, EPR, UV-Vis) a discrete Ni(III) aryl alkyl complex; direct evidence for B2-type intermediate and C–C reductive elimination from Ni(III). **[tentative_citation: cited as ref 22 in Breitenfeld 2014; high confidence on existence and content; ⟨S²⟩ data in SI need verification]**
* **Filling Establishment**: same as above.
* **Nature of filling**: Partial — fills Ni(III) characterization and reductive-elimination elements; does not fill ⟨S²⟩/Yamaguchi correction reporting for TSE1,E2 specifically, or spectroscopic evidence for Grignard adduct 12. **[tentative_citation: Hu group follow-up papers post-2014 on intermediate 12 — plausible but unconfirmed]**
* **Confidence**: Medium

---

**EP-06a [Analogy-validation pack] (Tier 2)**

* **RI to be filled**: RI-03 [Unobserved explanatory] (primary); RI-06 [Imported model] (secondary)
* **Filling Onset**: Lipschutz, M. I.; Tilley, T. D. *Angew. Chem. Int. Ed.* 2014, 53, 7290–7294 — evidence for Ni(I)/Ni(III) involvement in C–C coupling with N-donor ligands; contemporary support for comproportionation-type mechanistic picture. **[tentative_citation: cited as ref 23 in Breitenfeld 2014; comproportionation rates specifically need verification]**
* **Filling Establishment**: **unidentified** — no paper measuring or computing the Ni(I) 16 + Ni(III) 14 → Ni(II) 11 + Ni(II) 13 comproportionation for the Nickamine alkyl–aryl system has been identified. DFT thermodynamics in related Ni-photoredox systems (Diao, Stahl, Engle groups, 2018–2023) provide indirect context. **[tentative_citation: general field knowledge; specific papers not confirmed]**
* **Nature of filling**: Partial (onset only); Nickamine-specific comproportionation kinetics unfilled.
* **Confidence**: Low

---

**EP-07a [Boundary-test pack] (Tier 2)**

* **RI to be filled**: RI-07 [Unsupported boundary] (primary)
* **Filling Onset**: **unidentified** — No paper reports Eyring activation parameters for the transmetalation TDS of Nickamine-catalyzed alkyl–aryl Kumada coupling.
* **Filling Establishment**: **unidentified**
* **Nature of filling**: Attempted at best via Yamamoto redistributive transmetalation analogy (refs 47–48), but Yamamoto reports Ni(0)/biaryl kinetics, not Nickamine-specific activation parameters.
* **Confidence**: Low

---

**EP-05a [Quantitative-ranking substantiation pack] (Tier 2)**

* **RI to be filled**: RI-05 [Qualitative overread] (primary); RI-08 [Unquantified reliability] (secondary)
* **Filling Onset**: Burés, J. *Angew. Chem. Int. Ed.* 2016, 55, 2028–2031 — VTNA (Variable Time Normalization Analysis) defines the modern standard for kinetic order determination with statistical rigor, against which the two-trials-per-point log-log analysis of Breitenfeld 2014 is retrospectively deficient.
* **Filling Establishment**: same as above; no Nickamine-specific reanalysis using VTNA has been identified.
* **Nature of filling**: Indirect — methodological standard only; non-integer orders (1.7 catalyst, −0.3 alkyl iodide) remain unaddressed in any subsequent Nickamine paper.
* **Confidence**: High (Burés 2016); Low (Nickamine-specific).

---

**EP-08a [Replication / uncertainty pack] (Tier 2)**

* **RI to be filled**: RI-08 [Unquantified reliability] (primary); RI-01 [Reporting integrity] (secondary)
* **Filling Onset**: Breitenfeld, J.; Ruiz, J.; Wodrich, M. D.; Hu, X. L. *J. Am. Chem. Soc.* 2013, 135, 12004–12012 — alkyl–alkyl predecessor (ref 20) with same GC-MS internal-standard procedure; establishes analogy context for radical-clock replication standards.
* **Filling Establishment**: **unidentified** for alkyl–aryl-specific system — no independent paper provides GC yields and conversions at each catalyst loading for substrate 7 + PhMgCl.
* **Nature of filling**: Indirect (alkyl–alkyl analogy); alkyl–aryl-specific EP-08a unfilled.
* **Confidence**: High for Breitenfeld 2013; Low for alkyl–aryl-specific filling.

---

**EP-01a [Reporting-coherence pack] (Tier 2)**

* **RI to be filled**: RI-01 [Reporting integrity] (primary); RI-04 [Unreplicated discriminator] (secondary)
* **Filling Onset**: Wodrich/Corminboeuf group, post-2014 DFT truncation papers for organometallics. **[tentative_citation: plausible; specific papers not confirmed]**
* **Filling Establishment**: **unidentified** — no paper comparing propyl vs. hex-5-en-1-yl DFT barriers for TSB2,B3 / TSE1,E2 in the Nickamine system.
* **Nature of filling**: Indirect at best.
* **Confidence**: Low

---

### §C Recommended selection list

| Order | Paper | EPs filled | VQ level | Year | Confidence |
|-------|-------|------------|----------|------|------------|
| 1 | Breitenfeld, Ruiz, Wodrich, Hu. *J. Am. Chem. Soc.* 2013, 135, 12004 | EP-08a, EP-06a (analogy base) | VQ-2 | 2013 | High |
| 2 | Grimme, S. *Chem. Eur. J.* 2012, 18, 9955 | EP-04a (quasi-RRHO entropy correction) | VQ-3 | 2012 | High |
| 3 | Zheng, Tang, Luo, Schultz, Rath, Mirica. *J. Am. Chem. Soc.* 2014, 136, 6499 | EP-03a (Ni(III) aryl alkyl direct characterization) | VQ-3 | 2014 | Medium |
| 4 | Lipschutz, Tilley. *Angew. Chem. Int. Ed.* 2014, 53, 7290 | EP-06a (Ni(I)/Ni(III) C–C coupling context) | VQ-3 | 2014 | Medium |
| 5 | Burés, J. *Angew. Chem. Int. Ed.* 2016, 55, 2028 | EP-05a (kinetic order statistical standard) | VQ-4 | 2016 | High |
| 6 | Laplaza, Wodrich, Corminboeuf. *J. Chem. Theory Comput.* ca. 2021 | EP-04a (DFT benchmarking for PBE0-dDsC protocol) | VQ-3 | 2021 | Medium |

**Selection rationale:** The list covers VQ-2 through VQ-4 with temporal spread 2012–2021. Entry 1 (Breitenfeld 2013) provides the analogy foundation for EP-08a and EP-06a (self-filling by predecessor). Entries 2 and 6 together fill the two elements of EP-04a: the Grimme 2012 quasi-RRHO correction (pre-emptive, predating the paper) and the Wodrich/Corminboeuf DFT benchmarking series. Entry 3 (Zheng/Mirica 2014, cited as ref 22) fills EP-03a most directly. Entry 4 (Lipschutz/Tilley 2014, cited as ref 23) provides independent Ni(I)/Ni(III) context for EP-06a. Entry 5 (Burés 2016) fills EP-05a as the field's kinetic-order methodology standard. EP-07a has no High-confidence filler and is absent from the list.

---

### §D Correspondence between VQ hierarchy and filling time order

**Filling time axis:**
- VQ-2 requirement: EP-08a (replication/uncertainty for radical-clock) → 2013, Breitenfeld et al., self-filling by predecessor
- VQ-3 requirement: EP-04a (quasi-RRHO correction) → 2012, Grimme, technology-driven (pre-emptive)
- VQ-3 requirement: EP-03a (Ni(III) direct characterization) → 2014, Zheng/Mirica, cross-field filling
- VQ-3 requirement: EP-06a (Ni(I)/Ni(III) comproportionation context) → 2014, Lipschutz/Tilley, cross-field; Nickamine-specific comproportionation unfilled
- VQ-4 requirement: EP-05a (kinetic order statistical methodology) → 2016, Burés, technology-driven
- VQ-4 requirement: EP-07a (room-temperature activation parameters) → unfilled as of 2026

**Evaluation of hierarchy–time correspondence:** The hypothesis (higher VQ level = longer filling time) receives partial support. VQ-3 EPs (EP-03a, EP-04a onset) received literature responses in 2012–2014, while the VQ-4 EP-05a was addressed in 2016, supporting the hierarchy direction. However, EP-04a's quasi-RRHO filling (Grimme 2012) predates Breitenfeld 2014 by two years — a technology-available-but-unapplied pattern that breaks the hypothesis. The VQ-2 EP-08a is addressed only via the predecessor, not a subsequent paper, further inverting the expected low-VQ rapid-response pattern.

**Notable patterns:**
- **Technology-driven (pre-emptive):** EP-04a — Grimme 2012 quasi-RRHO predates submission; gap is technology-available-but-unapplied.
- **Cross-field filling (concurrent):** EP-03a, EP-06a onset — Mirica and Tilley groups independently addressed these EPs for their own objectives.
- **Self-filling by predecessor:** EP-08a, EP-06a analogy base — Breitenfeld 2013 pre-fills these EPs in reverse temporal direction.
- **Unfilled:** EP-07a (room-temperature TDS boundary test, 12+ years); comproportionation kinetics in EP-06a; EP-08a alkyl–aryl-specific; EP-01a.

---

### §E Heuristic significance of unfilled EPs

**List of unfilled EPs:**

EP-07a [Boundary-test pack — room-temperature activation parameters]:
* **Reason for non-filling**: Misaligned incentive structure. Eyring analysis at two temperatures (0 °C and −20 °C, same apparatus) is technically trivial, but reporting ΔH‡/ΔS‡ for an already-characterized catalyst does not meet novelty standards. The field convention accepts single-temperature kinetic characterization as sufficient TDS assignment.
* **Heuristic significance**: Yes. Breitenfeld 2014's mechanistic conclusions (second order in catalyst, bimetallic transmetalation as TDS) are cited as "the mechanism" of Nickamine without confirmation at room temperature — the condition of >120 synthetic examples (ref 24). This is 12+ years of unchallenged extrapolation across a 25 °C temperature gap.
* **Future filling feasibility**: High — technically trivial; incentive structure is the only obstacle.

EP-06a (comproportionation-specific kinetics) [partial unfilled element]:
* **Reason for non-filling**: Technical difficulty + Misaligned incentive structure. Ni(I) Nickamine species are not reported as isolable (Ni(I) d9 with N2N pincer tends to be thermally unstable); generating both Ni(I) 16 and Ni(III) 14 independently is a non-trivial synthesis challenge. Even if achieved, validating one mechanistic step in an already-published cycle is low-novelty.
* **Heuristic significance**: Yes. Comproportionation is mechanistically obligatory for catalytic turnover; without it, Ni(I) accumulates and the cycle breaks. The observed catalyst decomposition under fast Grignard addition at room temperature is exactly consistent with Ni(I) accumulation/comproportionation failure — a connection uninvestigated in print for 12+ years.
* **Future filling feasibility**: Medium — DFT profiling of the comproportionation free-energy profile is feasible immediately from existing Breitenfeld 2014 geometries; stoichiometric mixing experiment requires Ni(I)/Ni(III) Nickamine synthesis.

EP-08a (alkyl–aryl radical-clock replication) [unfilled]:
* **Reason for non-filling**: Misaligned incentive structure + Reporting-format issue. GC yields and conversions are generated by the described C₁₂H₂₆-standard procedure but suppressed; a dedicated paper for this one data quality element has no publication pathway.
* **Heuristic significance**: No. If conversions are uniform (plausible at ≤10% yield), the first-order conclusion holds. EP-08a is a methodological blind spot, not evidence of a false claim.
* **Future filling feasibility**: High — GC data likely exist in original laboratory files; re-running is one day's work.

**VQ-hierarchy inversion diagnosis:** EP-08a and EP-01a (VQ-2, low-VQ) are the least-filled EPs; EP-03a and EP-04a (VQ-3, higher-VQ) received direct independent literature responses. Two forces drive this inversion: (i) cross-field filling where Mirica 2014 and Grimme 2012 high-novelty work coincidentally addressed high-VQ EPs; (ii) misaligned incentive structure making low-VQ replication EPs economically unpublishable despite being technically trivial. The field's publication incentive structure maintains structural absences preferentially at the low-VQ observational level — the incentive-inversion signature UQS predicts.
