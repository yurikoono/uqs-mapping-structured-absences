```
prompt_version: stage3-v2-en-20260419
model_info: claude-sonnet-4-6
```

# Re-certification Assessment Sheet for Scientific Knowledge

## Tellis, Kelly, Primer, Jouffroy, Patel, and Molander 2016 (Accounts of Chemical Research, full_paper)

---

### §1 Claim Architecture

**Core claim summary:**

The paper's core claim is that single-electron transmetalation via photoredox/nickel dual catalysis constitutes a mechanistically distinct paradigm for Csp³–Csp² cross-coupling that inverts the inherent reactivity hierarchy of conventional two-electron transmetalation, rendering Csp³ organometallics preferentially activated rather than reluctant partners. The **Novelty pillar** operates on two levels: (i) the mechanistic paradigm claim that SET-based oxidative fragmentation bypasses the high-activation-barrier two-electron transmetalation step, making Csp³ reagents more reactive than Csp² reagents within this manifold; and (ii) a suite of eight substrate-class demonstrations (benzylic, secondary alkyl, α-amino, α-alkoxy, α-CF₃ trifluoroborates; alkylsilicates; alkenyl coupling; azaborines; thioetherification) as realization of that paradigm. The **Utility pillar** rests on mild conditions (room temperature, visible light, bench-stable reagents), broad functional group tolerance, and the enabling of product classes (unnatural amino acids, benzylic ethers, 1,1-diaryltrifluoroethanes) inaccessible under conventional protocols.

**Layered structure judgment:**

The claim is explicitly layered across four independent tiers. (1) The **mechanistic paradigm tier** — the assertion that SET transmetalation is a "mechanistic sea-change" supported by DFT PES (Figure 9) — stands independently of the empirical scope. (2) The **eight substrate-class empirical tiers** are each independently grounded in scope tables; refutation of one substrate class does not collapse the others. (3) The **computational mechanistic tier** (B1 pathway preference, Curtin–Hammett DKR model) is sub-nested within tier 1 but constitutes the primary evidential basis for the mechanistic claim; its collapse would degrade tier 1 to an empirically supported hypothesis rather than a mechanistically validated paradigm. (4) The **selectivity tier** (eq 3 competition experiment, orthogonal reactivity) is independent of both the DFT tier and individual substrate-class scope. This is a "independent layers exist" architecture: a single refutation of the DFT mechanistic tier does not collapse the empirical scope claims, but the paper's rhetorical elevation — "paradigm" — depends specifically on the mechanistic tier holding. The most important inter-layer dependency is that the DKR stereochemical model (tier 3) is fully entangled with the DFT PES (tier 3 is tier 1's sole mechanistic support), so DFT tier collapse also collapses the DKR model and the enantioselectivity predictive claim, even while the empirical scope (tier 2) survives.

---

### §2 SRG / CLA → RI / ER / EP Crosswalk

**SRG-1 [DFT solvation model invalidity]**

* **Primary RI**: RI-06 [Imported model] — The PES reproduced from Gutierrez et al. (ref 24) was computed using SMD-water (ε ≈ 80) as the implicit solvation environment; the experimental reactions are conducted in acetone/MeOH 95:5 (ε ≈ 21–33), dioxane (ε ≈ 2.2), EtOAc (ε ≈ 6.0), or DMF (ε ≈ 38). The model is imported from a different solvent environment without demonstrating that the ~6 kcal/mol A1/B1 barrier difference is invariant across this dielectric range.
* **Secondary RI**: RI-04 [Unreplicated discriminator] — The ~6 kcal/mol preference is a single computed quantity (one PES, one solvent model, one substrate model) used to draw the mechanistic pathway conclusion without sensitivity analysis or alternative functional benchmark.
* **ER**: To sustain the claim that the B1 pathway (radical addition to Ni⁰) is kinetically preferred over A1 (oxidative addition), solvation sensitivity calculations across the actual dielectric range of the experimental solvents must demonstrate that the pathway preference is robust; alternatively, the barrier difference must be shown to exceed the expected solvation model error (estimated ≥3 kcal/mol for SMD across dielectric range).
* **EP**: EP-06a [Analogy-validation pack]; EP-03a [Direct-observation / state-assignment pack]
* **Case-specific implementation**: Recompute the Ni⁰/BnBF₃K/PhBr PES using the SMD dielectric of acetone (ε = 20.7) and dioxane (ε = 2.2) and compare the A1-TS / B1-TS ΔΔG‡ to the SMD-water result. If the preference reverses or narrows below ~3 kcal/mol under any experimental solvent condition, the pathway conclusion requires experimental corroboration (e.g., Stern–Volmer quenching to establish which species intercepts the excited Ir* first). As an alternative EP-03a implementation: measure the Stern–Volmer quenching rate constant k_q for BnBF₃K oxidation by excited [Ir(dF(CF₃)ppy)₂(dtbbpy)]⁺ in acetone/MeOH to directly establish whether SET to generate the benzyl radical occurs faster than reductive quenching of Ir* by Ni species.
* **Notes**: Members V1-Q4, V2-Q1, V2-OV1, V3-Q3, V3-OV1. Positioned in TEMPERATURE_SUMMARY as the highest-priority cluster (convergence 3/3, temperature_gap none). B-5 records the reporting omission of ⟨S²⟩ values, ZPE provenance, and solvation validation data in this Accounts article.

---

**SRG-2 [Pathway A vs. B discriminability — computational and experimental]**

* **Primary RI**: RI-03 [Unobserved explanatory] — The central mechanistic species (benzyl radical in proximity to Ni⁰ forming the B1 encounter complex) is neither directly observed (no EPR, no radical-clock product detected) nor kinetically constrained by Stern–Volmer data; the B1 pathway preference is inferred solely from the computed ΔG‡ difference.
* **Secondary RI**: RI-04 [Unreplicated discriminator] — The paper simultaneously concedes "it appears possible that both may operate simultaneously," meaning the single PES from which the preference is derived cannot in practice discriminate the two pathways under catalytic conditions at low radical and Ni⁰ concentration.
* **ER**: A mechanistic claim of pathway predominance requires at least one experimental discriminator: either (a) a Stern–Volmer experiment establishing the rate of SET from BnBF₃K to Ir* under catalytic concentrations, or (b) a radical-clock substrate (e.g., cyclopropylmethyl trifluoroborate) whose ring-opening product yield establishes the radical lifetime relative to Ni-trapping, or (c) kinetic isotope experiments at the Ni center that distinguish between concerted two-electron and stepwise radical processes.
* **EP**: EP-03a [Direct-observation / state-assignment pack]; EP-04a [Discrimination / replication pack]
* **Case-specific implementation**: For EP-03a: conduct a Stern–Volmer fluorescence quenching experiment in which [Ir(dF(CF₃)ppy)₂(dtbbpy)]⁺ excited state emission is titrated against (a) benzyltrifluoroborate and (b) NiCl₂·dme/dtbbpy separately, obtaining k_q for each; if k_q(BnBF₃K) >> k_q(Ni), pathway B1 (radical generation preceding Ni involvement) is confirmed. For EP-04a: use cyclopropylmethyl potassium trifluoroborate as a radical-clock probe with bromobenzene under standard conditions; the ratio of ring-opened (homoallylic) to ring-closed coupling product directly establishes whether the benzyl-type radical persists long enough for intermolecular radical capture by Ni⁰ (B1 manifold) or reacts at Ni while still bound in an oxidative-addition-like encounter (A1 manifold).
* **Notes**: Members V1-Q5, V2-Q2, V3-OV4. Convergence 3/3, temperature_gap none. The paper's own concession ("both may operate simultaneously") creates an internal indeterminacy that the B1 pathway narrative does not resolve.

---

**SRG-3 [Open-shell Ni DFT reliability — spin contamination and basis set]**

* **Primary RI**: RI-06 [Imported model] — The UB3LYP/LANL2DZ and UM06/6-311+G(d,p) calculations on NiI (d⁹), NiIII (d⁷), and alkyl radical intermediates are imported from Gutierrez et al. (ref 24) without validation of spin-state assignments (doublet vs. quartet for NiIII; singlet vs. triplet for Ni⁰) at each stationary point, ⟨S²⟩ values, or multireference correction assessment. For open-shell 3d transition metal systems, ⟨S²⟩ deviation from S(S+1) by >0.05 indicates significant spin contamination that can introduce errors of 3–10 kcal/mol in relative energies.
* **Secondary RI**: RI-01 [Reporting integrity] — The paper does not report the spin-state assignments for each PES stationary point, making cross-comparison between the A1 (closed-shell singlet Ni⁰ + ArBr TS) and B1 (open-shell doublet Ni⁰ + alkyl radical TS) pathways impossible without knowing whether the underlying calculations are on a consistent spin manifold.
* **ER**: For a PES involving transitions between closed-shell singlet (Ni⁰) and open-shell doublet (Ni–radical encounter) surfaces, spin-state assignments and ⟨S²⟩ values must be reported for each stationary point; any spin-state crossing must be located as a minimum energy crossing point (MECP) to establish whether the pathway comparison is energetically meaningful on a single surface.
* **EP**: EP-06a [Analogy-validation pack]; EP-01a [Reporting-coherence pack]
* **Case-specific implementation**: Re-report ⟨S²⟩ values for all stationary points in Figure 9 from ref 24's original calculation data. For the transition states A1-TS and B1-TS specifically, compute ⟨S²⟩ and compare to the expected value (0.0 for singlet; 0.75 for doublet; 3.75 for triplet; 8.75 for quartet); if |⟨S²⟩_computed − ⟨S²⟩_expected| > 0.1, apply spin-projection correction (e.g., AP-DFT or CASSCF single-point). Locate the singlet–doublet MECP using SEAM calculations (e.g., with DL-FIND or the Harvey MECP code) to determine whether spin-state crossing between the A1 and B1 pathways occurs at an accessible energy.
* **Notes**: Members V2-Q10, V3-Q1, V3-Q4, V3-OV2. Convergence 2/3, temperature_gap none. RI-06 scope note applies: this is a cycle-level model import (the entire Ni catalytic cycle PES is imported from ref 24 without re-validation for the conditions of this paper).

---

**SRG-4 [Curtin–Hammett dynamic kinetic resolution — computational and experimental support]**

* **Primary RI**: RI-03 [Unobserved explanatory] — The NiIII diastereomeric complexes I and epi-I, which are postulated to interconvert rapidly via Ni–C bond homolysis/recombination (k_interconvert >> k_RE), are neither observed nor kinetically constrained; the kinetic hierarchy required for the DKR model (fast equilibration, slow irreversible reductive elimination) is inferred entirely from the computed ~6 kcal/mol reductive elimination barrier without variable-temperature ee data, trapping experiments, or measured rate constants.
* **Secondary RI**: RI-04 [Unreplicated discriminator] — The correlation in Figure 10B (three data points: 57/54%, 62/74%, 65/84% exp/calc ee) is presented as experimental validation of the DKR model, but the three-point correlation with the same functional and solvation model does not constitute an independent test of the model since both the predicted and observed quantities are generated within the same computational framework.
* **ER**: The Curtin–Hammett DKR mechanism requires an independent experimental test of the kinetic hierarchy k_interconvert >> k_RE: variable-temperature ee measurements (ln(er) vs. 1/T) that directly return ΔΔG‡ for the diastereomeric reductive elimination, or a radical-clock experiment during the chiral coupling that establishes whether NiIII bond homolysis is faster than reductive elimination at the reaction temperature.
* **EP**: EP-03a [Direct-observation / state-assignment pack]; EP-04a [Discrimination / replication pack]
* **Case-specific implementation**: Measure ee for the stereoconvergent coupling of PhCH(Me)BF₃K with 4-cyanobromobenzene (ligand L2, the system of Figure 10B) at five temperatures from −20 °C to 40 °C; a linear ln(er) vs. 1/T plot with positive slope and the intercept consistent with a pre-exponential factor near 1 (Curtin–Hammett condition) would confirm the DKR mechanism. Alternatively, use a radical-clock alkyl trifluoroborate (primary cyclopropylmethyl group tethered to the chiral center) to detect NiIII homolysis by observation of ring-opened byproduct; if ring-opening is observed at a rate commensurate with the reported ee values, the radical lifetime at NiIII confirms k_interconvert is accessible.
* **Notes**: Members V2-Q3, V2-Q4, V3-Q8, V3-OV3. Convergence 2/3, temperature_gap none. Entangled with SRG-1 and SRG-3 at the PES level, but constitutes a distinct question: even on a perfectly reliable PES, the kinetic hierarchy k_interconvert >> k_RE requires experimental confirmation because a computed barrier is not a measured rate constant.

---

**SRG-5 [Amine additive — BF₃-scavenging hypothesis unverified]**

* **Primary RI**: RI-07 [Unsupported boundary] — The paper asserts that 2,6-lutidine [REDACTED: substantial verbatim quotation; see Tier 9] and generalizes this to all nine trifluoroborate substrate sections via "vide infra," but presents no experiment testing this hypothesis; no experiment adding BF₃·OEt₂, no pKa-matched non-amine base, and no quantum-yield measurement to test whether amine modulates SET efficiency are reported.
* **ER**: The boundary claim "2,6-lutidine acts as BF₃ scavenger" requires at minimum one positive experiment: demonstration that BF₃·OEt₂ addition to the reaction without 2,6-lutidine inhibits the reaction to the same extent as amine omission, and that a pKa-matched non-amine base (e.g., 2,6-di-tert-butylpyridine) replicates the effect, distinguishing Brønsted-base from Lewis-base function.
* **EP**: EP-07a [Boundary-test pack]
* **Case-specific implementation**: In the benzylic trifluoroborate/bromobenzene model system (eq 1 conditions), compare yield under four conditions: (a) standard (3.5 equiv 2,6-lutidine), (b) no additive, (c) 3.5 equiv 2,6-di-tert-butylpyridine (matched pKa, sterically blocked from Ni coordination), (d) 3.5 equiv 2,6-lutidine + 3.5 equiv BF₃·OEt₂. If (c) replicates (a) and (d) is inhibited relative to (a), the BF₃-scavenging hypothesis is confirmed; if (c) fails, an alternative function (Ni ligand, HAT mediator, radical quencher) must be considered.
* **Notes**: Members V1-Q6, V2-Q5, V2-OV5. Convergence 2/3, temperature_gap none. The unusually high loading (3.5 equiv) relative to expected BF₃ equivalence (1 equiv per oxidation event) is an unreported anomaly suggesting the BF₃-scavenging hypothesis may be incomplete.

---

**SRG-6 [Thioetherification HAT mechanism — BDE-only support]**

* **Primary RI**: RI-05 [Qualitative overread] — The HAT mechanism is assigned based solely on the BDE thermodynamic argument (ΔBDEᶜ⁻ᴴ − ᵀˢ⁻ᴴ = 101 − 88 = 13 kcal/mol "renders this process irreversible"), without kinetic data; BDE thermodynamics establishes reaction spontaneity but not the rate competition between HAT and Ni-radical capture, which is the operative selectivity determinant.
* **Secondary RI**: RI-04 [Unreplicated discriminator] — The 62–97% thioetherification yields across Figure 14 are presented without any control experiment excluding competitive cross-coupling under the reported conditions (alkylsilicate + aryl bromide + thiol + [Ru(bpy)₃]²⁺ + [NiCl₂(dme)]/dtbbpy), meaning the complete selectivity for thioetherification over cross-coupling under Ni-catalyzed conditions is presented as a single observation without kinetic rationalization.
* **ER**: A proposed HAT mechanism requires that the rate of intermolecular HAT from thiol to alkyl radical (k_HAT) exceeds the rate of radical addition to Ni⁰ or Ni¹ (k_add) under the reaction conditions; this rate competition must be supported by at minimum one kinetic experiment, such as a primary deuterium KIE (k_H/k_D) for the R-SH vs. R-SD thiol HAT step, or a Stern–Volmer-type experiment establishing the rate of radical quenching by thiol.
* **EP**: EP-05a [Quantitative-ranking substantiation pack]; EP-04a [Discrimination / replication pack]
* **Case-specific implementation**: Measure k_H/k_D for the thioetherification of a representative aryl bromide (e.g., 4-cyanobromobenzene) with propanethiol-SH vs. propanethiol-SD under identical conditions; a primary KIE (k_H/k_D ≥ 2.5) would confirm that S–H(D) bond breaking is involved in the rate-limiting step. Additionally, measure the thioetherification yield and competing cross-coupling yield as a function of thiol concentration (0.1, 0.5, 1.0, 2.0 equiv relative to silicate); if cross-coupling product appears at low thiol concentration, k_HAT/k_add can be estimated and the selectivity boundary mapped.
* **Notes**: Members V1-Q11, V2-Q7, V2-OV3. Convergence 2/3, temperature_gap none. RI-05 application: "irreversible" is a kinetic claim (rate competition) derived solely from a thermodynamic quantity (BDE), constituting qualitative overread.

---

**SRG-7 [Yield anomalies without attribution — compound-level outliers]**

* **Primary RI**: RI-08 [Unquantified reliability] — Compounds (±)-43 (59%, Figure 6), 64 (32%, Figure 7), 83 (50%), and 84 (53%, Figure 11) fall substantially below the modal yield range of their respective scope tables (69–95%, 56–93%, 64–95%) without electronic, steric, or mechanistic attribution; the absence of replicate measurements or uncertainty estimates prevents assessment of whether these are statistical outliers or systematic substrate-dependent limitations.
* **ER**: Yield outliers deviating >20% from the modal scope yield require attribution: electronic rationalization (substrate E_ox or radical stability relative to successful substrates), steric rationalization (torsional strain, buried Ni coordination site), or at minimum an explicit statement of failure mode (competing reaction identified by byproduct isolation or GC trace).
* **EP**: EP-08a [Replication / uncertainty pack]; EP-05a [Quantitative-ranking substantiation pack]
* **Case-specific implementation**: For compound 64 (α-CF₃ trifluoroborate, 32%): measure E_ox by CV in acetonitrile relative to SCE; if E_ox exceeds E*(Ir complex 6) (+1.32 V vs. SCE), SET is endergonic and the low yield is rationalized as endergonic SET-limited. For compounds 83/84 (amine-containing alkylsilicates, 50–53%): compare isolated yield with and without amine-protecting group (Boc vs. free amine) to determine whether Ni poisoning by free amine is responsible; provide GC yield to distinguish incomplete conversion from product decomposition.
* **Notes**: Members V1-Q2 (compound (±)-43), V1-Q8 (compound 64), V1-Q10 (compounds 83/84). Convergence 1/3 per individual member but collectively grounded in a shared root (yield basis unreported). Positioned in SRG-7 [yield anomalies without attribution].

---

**SRG-8 [Yield reporting basis — absence of yield type, uncertainty, and mass balance]**

* **Primary RI**: RI-08 [Unquantified reliability] — All scope tables (Figures 5–7, 11–15) report yields without specifying whether values are isolated or GC yields, single-run or averaged, or what experimental uncertainty applies; compound 11 (4-bromostyrene, 61%) is presented with the claim "no competitive side reactions or polymerization" without mass balance, GPC trace, or byproduct identification, making the 39% unaccounted fraction unaddressable.
* **ER**: A substrate scope table that claims general applicability requires, at minimum, specification of yield type (isolated vs. GC) and whether values are single-run or represent an average of replicate reactions; the "no polymerization" claim for a radical process applied to a vinyl-halide-bearing substrate requires GPC data or byproduct quantification to close the mass balance.
* **EP**: EP-01a [Reporting-coherence pack]; EP-08a [Replication / uncertainty pack]
* **Case-specific implementation**: For the Accounts format, the minimal acceptable addition is a footnote to each scope figure specifying "yields are isolated unless noted" or "GC yields corrected for internal standard"; for compound 11, report the GC yield alongside isolated yield and confirm by GPC that M_n of the crude product mixture does not exceed that of the monomer, or identify the byproduct accounting for the remaining 39%.
* **Notes**: Members V1-Q1, V1-Q12. Convergence 1/3. Era-norm consideration: see §4 — the Accounts format partially tolerates yield-type omission, but the mass balance claim for compound 11 is not tolerated because it is a positive mechanistic assertion ("no polymerization"), not a passive omission.

---

**SRG-9 [Competition experiment (eq 3) selectivity robustness]**

* **Primary RI**: RI-07 [Unsupported boundary] — The claim that single-electron transmetalation is [REDACTED: substantial verbatim quotation; see Tier 9] is made from a single competition experiment (eq 3, one substrate pair at one concentration ratio under one set of conditions, 91:0 product distribution) without confirmation that selectivity is robust across substrate ratios, substrate electronic variants, or different sp³/sp² trifluoroborate pairs.
* **ER**: A boundary claim of "broadly preferable" selectivity requires testing under conditions that could challenge the selectivity: (a) non-equimolar ratios of sp³:sp² trifluoroborate to determine the range over which 91:0 selectivity holds; (b) a second sp³/sp² substrate pair with different radical stabilities to determine whether the selectivity is general or benzylic-specific; (c) CV-measured E_ox values for both 33 and 34 to confirm the electrochemical basis for selective photooxidation.
* **EP**: EP-07a [Boundary-test pack]; EP-09a [Internal benchmark pack]
* **Case-specific implementation**: Run eq 3 with molar ratios of 33:34 at 1:1, 1:3, and 1:10 (sp³ deficient) and report the product distribution; run an analogous competition experiment with a secondary alkyltrifluoroborate (§2.2 substrate class) vs. aryl trifluoroborate to test generality beyond the benzylic case; measure E_ox of 33 and 34 by CV in acetonitrile and calculate the expected selectivity from the Rehm–Weller equation to compare with observed selectivity.
* **Notes**: Members V1-Q15, V2-Q11. Convergence 2/3, temperature_gap none. Linked to U-3 (absent E_ox data for trifluoroborate series): the mechanistic basis for the 91:0 selectivity (selective photooxidation vs. selective radical addition vs. thermodynamic sink) is entirely unaddressed.

---

**SRG-10 [PES substrate-scope generalization — single-system computation applied to nine substrate classes]**

* **Primary RI**: RI-06 [Imported model] — The PES from Gutierrez et al. (ref 24) is computed for a benzylic radical (PhCH₂•) + bromobenzene model system and is applied to mechanistically rationalize nine substrate sections including secondary unactivated alkyltrifluoroborates, α-amino, α-alkoxy, α-CF₃ trifluoroborates, alkylsilicates (different oxidation manifold), alkenyl halide partners, azaborines, and thioetherification; no additional PES computation for any non-benzylic substrate is presented.
* **ER**: Generalization of a single-substrate PES to nine mechanistically non-equivalent substrate classes requires at minimum one additional PES for a representative secondary alkyltrifluoroborate (the substrate class for which SET was identified as mildly endergonic, §2.2) to establish that the B1/A1 pathway preference is maintained when radical stability and E_ox are substantially different from the benzylic case.
* **EP**: EP-06a [Analogy-validation pack]
* **Case-specific implementation**: Compute the PES for a representative secondary alkyltrifluoroborate (e.g., cyclohexylmethyltrifluoroborate + bromobenzene) at the same level of theory as ref 24, reporting the A1-TS / B1-TS ΔΔG‡; if the barrier preference is maintained within 2 kcal/mol of the benzylic case despite higher E_ox, the mechanistic generalization is supported; if the preference narrows or reverses, individual substrate-class PES computations are required.
* **Notes**: Member V3-Q5. Convergence 1/3 (V3 only), but classified as high-severity U-7 prerequisite-absence because the generalization step is made explicitly in §§2.2–2.9 without any additional computation.

---

**Outside the SRGs: CLAs**

**CLA-1: DKR model not applied to founding stereoconvergent datum (eq 2)**

* **Primary RI**: RI-03 [Unobserved explanatory] — The paper's DKR model explicitly predicts that ee is a direct readout of ΔΔG‡ for diastereomeric NiIII reductive elimination; three substrates are modeled (Figure 10B) using chiral ligand L2, but the founding stereoconvergent experiment (eq 2, 75:25 er, chiral ligand L1) receives neither a ΔΔG‡ computation nor a mechanistic comment within the DKR framework. The DKR model predicts an observable (ΔΔG‡ for L1 system) that the paper does not report as its own data.
* **ER**: A mechanistic model that quantitatively predicts ee from ΔΔG‡ must be applied to every founding experimental datum it is invoked to explain; the 75:25 er of eq 2 must be compared to a computed ΔΔG‡ for the L1 diastereomeric transition states, or its deviation from the L2 correlation must be explicitly addressed.
* **EP**: EP-03a [Direct-observation / state-assignment pack]
* **Case-specific implementation**: Compute the diastereomeric NiIII reductive elimination TS energies using L1 (the imidazolidine bis-Bn ligand) and the substrate of eq 2 (PhCH(Me)BF₃K + methyl 4-bromobenzoate) at the same level of theory (UM06/6-311+G(d,p)//UB3LYP/6-31G(d), SMD-water), and compare the predicted ee to the observed 75:25 er; if the model predicts a value substantially different from 50% ee, investigate whether L1 operates through a different mechanism from L2 or whether the DFT functional shows ligand-dependent artifacts.
* **Notes**: Derived from U-5 (high severity, 2/3 agents). Self-contradictory absence: the paper's DKR model predicts the ee of all stereoconvergent couplings but omits the prediction for its own founding datum. Not captured in SRGs because U-5 is linked to SRG-4 but represents a distinct mechanistic gap (model non-application rather than kinetic hierarchy non-verification).

---

**CLA-2: Electrochemical basis for sp³/sp² selectivity — absent CV data for trifluoroborate series**

* **Primary RI**: RI-05 [Qualitative overread] — The paper invokes the radical stability ordering (Csp³ > Csp² > Csp) as the mechanistic basis for sp³/sp² selectivity (Figure 4A, eq 3), but reports CV-measured E_ox values only for alkylsilicates (§2.6, E⁰ ≈ +0.37 to +0.75 V vs. SCE). No E_ox values for any alkyltrifluoroborate class (benzylic, secondary alkyl, α-amino, α-alkoxy, α-CF₃) are reported, despite E_ox being the operationally relevant quantity governing SET rate from the substrate to Ir*.
* **ER**: A selectivity claim based on differential E_ox (Figure 4A, eq 3) requires reporting E_ox for at least one representative substrate from each class whose selectivity is claimed (benzylic vs. aryl trifluoroborate) to verify that the photoredox catalyst excited state can oxidize sp³ but not sp² trifluoroborate under the reported conditions.
* **EP**: EP-05a [Quantitative-ranking substantiation pack]
* **Case-specific implementation**: Measure E_ox by CV (glassy carbon electrode, acetonitrile, 0.1 M TBAPF₆, referenced to SCE via ferrocene) for benzylic trifluoroborate 33, aryl trifluoroborate 34, and representative secondary alkyl trifluoroborate (§2.2); compare to the excited-state reduction potential E*(Ir complex 6, estimated +1.32 V vs. SCE) to determine the thermodynamic driving force for each SET; a ΔG° gradient of ≥5 kcal/mol between 33 and 34 is required to sustain the selectivity claim as electrochemically controlled.
* **Notes**: Derived from U-3 (high severity, 2/3 agents: V2-Q6, V1-Q9). Linked to B-7 (competition experiment) and SRG-9. Self-contradictory absence: the paper proposes E_ox ordering as the mechanistic design principle but does not report E_ox for the primary substrate class (trifluoroborates) through which that principle is demonstrated.

---

### §3 Current VQ assessment

**Current judgment: VQ-2 (Method), with qualified passage at VQ-1**

**VQ-1 [Observation] — holds (with non-fatal caveat)**

RI-02 (Object identification): The products are characterized by standard NMR and the substrate scope tables provide molecular structures with yields; isolated products are structurally assigned. However, RI-02 carries a non-fatal caveat: compound 11 (61% yield, 4-bromostyrene substrate) and the "no polymerization" claim leave 39% of material unaccounted and structurally uncharacterized. This is non-fatal because the main coupling products are structurally established across 40+ examples, and the polymerization concern is specific to one compound. VQ-1 holds on the premise that the non-fatal RI-02 caveat (mass balance for compound 11) does not undermine the identity of the primary coupling products.

**VQ-2 [Method] — holds (with non-fatal qualification)**

Building on VQ-1 and with the premise that RI-02 is non-fatal: RI-01 (Reporting integrity): Non-fatal. The yield type (isolated vs. GC) is unreported across all scope tables, and the mass balance for compound 11 is open, but the scope claims are directionally supported by the density and structural diversity of the reported compounds. RI-07 (Unsupported boundary): Non-fatal at the method level. The competition experiment (eq 3) and the "broadly preferable" claim lack robustness tests, but the empirical demonstration of sp³ cross-coupling under mild conditions is supported by multiple independent substrate classes regardless of the exact scope of the competition selectivity. VQ-2 holds on the premise that RI-01 and RI-07 are non-fatal within the scope-demonstration context; the method for achieving Csp³–Csp² coupling under visible light is established even without resolution of yield-type reporting and competition scope.

**VQ-3 [Mechanism] — fails**

VQ-3 requires resolution of RI-03, RI-04, and RI-06 (inheriting VQ-2 requirements). All three are unresolved at fatal or near-fatal severity for the mechanistic claim:

- RI-06 (SRG-1, SRG-3, SRG-10): The PES is imported from a different solvation environment (SMD-water for reactions in dioxane/acetone/DMF), applied without solvation sensitivity tests, and the open-shell Ni intermediates are not validated with ⟨S²⟩ data. Fatal for the quantitative pathway preference (the ~6 kcal/mol A1/B1 ΔΔG‡ may not be reliable across the actual dielectric range and may be subject to spin contamination errors of comparable magnitude).
- RI-03 (SRG-2, SRG-4, CLA-1): The benzyl radical intermediate, the NiIII diastereomeric complexes I and epi-I, and the DKR kinetic hierarchy are all proposed but unobserved explanatory species with no kinetic constraints. Fatal for the mechanistic pathway claim and the DKR stereochemical model.
- RI-04 (SRG-2): The pathway preference rests on a single computed ΔΔG‡ without experimental discrimination; the paper simultaneously concedes that "both may operate simultaneously," rendering the pathway conclusion internally indeterminate. Fatal for the specific claim that B1 "predominates" under catalytic conditions.

VQ-3 fails because RI-03, RI-04, and RI-06 remain unresolved for the paper's central mechanistic claims. The empirical scope claims (VQ-2 layer) are insulated from this failure, but the paradigm-level mechanistic claim cannot be certified.

**VQ-4 [Benchmark] — fails (inherited from VQ-3 failure)**

RI-08 and RI-09 are also unresolved: RI-08 (SRG-7, SRG-8): Yield data lack replicate measurements, uncertainty, and yield-type specification. RI-09 (C-1, C-2): Superiority over conventional protocols is asserted from condition comparison (Figure 2) without substrate-matched head-to-head yield comparison. VQ-4 cannot be assessed independently because VQ-3 fails, but even conditional on a hypothetical VQ-3 certification, RI-08 and RI-09 remain unresolved.

**Layered VQ asymmetry:**

However, **the empirical Csp³–Csp² cross-coupling substrate scope tier on its own**: the eight substrate-class demonstrations (benzylic, secondary alkyl, α-amino, α-alkoxy, α-CF₃ trifluoroborates; silicates; azaborines; thioetherification) viewed as independent scope claims rather than mechanistic validations of the paradigm reach VQ-2 (Method) individually. Within this layer, the regioisomeric fidelity claim (secondary alkyltrifluoroborates coupled without β-hydride elimination/isomerization) is particularly well-documented: the structural assignments of scope compounds in Figure 6 directly demonstrate the absence of isomerization products, which provides a clean falsifiable observation not dependent on the DFT mechanistic framework.

---

### §4 Era-Norm Annotation

**communication-era tolerated:**

- **B-1 (yield type unreported in scope tables)**: Accounts of Chemical Research full papers are review-format articles (11 pages, no SI) reporting a group's own published work. By 2016 norms, scope table yields in an Accounts article were understood to reflect the same values as the original primary papers (refs 16, 18–24), where isolation procedures are detailed; yield-type omission in a review-format article was tolerated because the primary papers were assumed to contain the SI data. The format is complicit in this compression: Accounts explicitly does not require SI.
- **B-5 (PES reproduced from ref 24 without validation data)**: The Accounts format explicitly permits reproduction of figures from original papers; the mechanistic data (⟨S²⟩, ZPE, solvation sensitivity) would reside in the SI of ref 24 (Gutierrez et al., J. Am. Chem. Soc. 2015) rather than in the Accounts article itself. By 2016 norms, reproducing a PES from a primary paper in a review article without repeating the computational SI was standard practice; readers were expected to consult the original.
- **B-8 (amine silicate "performed poorly" without yield data)**: In 2016 Accounts articles, qualitative characterizations of failed substrate classes without quantitative negative data were tolerated; SI was not available and the review format created legitimate space for summarizing failure modes by description rather than quantification.
- **C-1 / C-2 (grouped citations without head-to-head comparison)**: Citing prior protocols to establish a motivating landscape without conducting matched-substrate comparisons was standard in Accounts methodology reviews; the format's purpose is to describe the group's own findings, not to conduct comparative benchmarking.

**modern-era deficient:**

- **B-5 (DFT methodology data absent) — dual classification**: By current 2026 standards, a mechanistic claim resting on DFT must report ⟨S²⟩ values, spin-state assignments, ZPE provenance, and at minimum one solvation sensitivity test even in a review article, because the mechanistic conclusion (B1 pathway predominance) is a load-bearing claim of the paper, not merely contextual background. The omission of these data from this Accounts paper — even by reference to ref 24 — is deficient by modern standards because the mechanistic claim is centrally advanced here, not only in ref 24.
- **B-9 (compound 11 mass balance, "no polymerization" claim without GPC)**: The claim "without competitive side reactions or polymerization" for a radical process applied to a vinyl-halide substrate at 61% yield is a positive mechanistic assertion (not merely a scope yield), and by modern radical methodology paper standards (post-2018) it requires GPC data or byproduct quantification regardless of format. This is deficient rather than merely compressed.
- **B-7 (competition experiment eq 3, "broadly preferable[REDACTED: substantial verbatim quotation; see Tier 9]broadly preferable" requires at minimum a concentration-ratio sensitivity test (is 91:0 selectivity maintained when sp² partner is in 5-fold excess?); the single-condition competition experiment is insufficient for the scope of the verbal claim.
- **U-3 (E_ox data absent for trifluoroborate series)**: By contemporary photoredox methodology standards (post-2018), CV data are expected for all substrate classes whose reactivity is mechanistically attributed to SET; the absence of E_ox for the benzylic and secondary alkyltrifluoroborate series, while alkylsilicate E_ox is reported, constitutes an asymmetric omission that is modern-era deficient.

---

### §5 Shortest-reinforcement route

**First objective function: VQ-3 (Mechanism)**

The VQ-3 failure is driven by three unresolved RIs: RI-06 (imported solvation model / spin-state inconsistency), RI-03 (unobserved key intermediates / DKR kinetic hierarchy), and RI-04 (unreplicated pathway discriminator). Resolution requires addressing SRG-1+3+10 (RI-06), SRG-2+4+CLA-1 (RI-03+04), and CLA-2 (RI-05).

**Shortest route to VQ-3:**

1. **EP-04a [Discrimination / replication pack]** — Perform Stern–Volmer fluorescence quenching to separately measure k_q for (a) benzyltrifluoroborate oxidation and (b) NiCl₂(dtbbpy) reduction by excited [Ir(dF(CF₃)ppy)₂(dtbbpy)]⁺ in acetone/MeOH; if k_q(BnBF₃K) >> k_q(Ni), the SET sequence (radical generation before Ni involvement) is confirmed, establishing pathway B1 as operative on kinetic grounds independent of the DFT PES. This single experiment advances RI-03 (establishes radical as a formed intermediate under catalytic conditions) and RI-04 (provides experimental discrimination between A1 and B1 pathways). Advances RI-03, RI-04.

2. **EP-06a [Analogy-validation pack]** — Recompute the Ni⁰/BnBF₃K/PhBr PES using SMD-acetone (ε = 20.7) and SMD-dioxane (ε = 2.2) in addition to SMD-water and report ⟨S²⟩ values for all stationary points; if the A1/B1 ΔΔG‡ is maintained within ±2 kcal/mol across all solvents and ⟨S²⟩ deviations are <0.05, the imported model is validated for the experimental solvents. Advances RI-06 (SRG-1 and SRG-3).

3. **EP-03a [Direct-observation / state-assignment pack]** — Conduct variable-temperature ee measurements (−20 to +40 °C) for the stereoconvergent coupling of PhCH(Me)BF₃K with 4-CN-C₆H₄Br using ligand L2; fit the ln(er) vs. 1/T data to extract ΔΔH‡ and ΔΔS‡; compare to the computed ΔΔG‡ values of Figure 10B; if ΔΔH‡ matches the computed ΔΔG‡ at 298 K, the DKR model (SRG-4) is independently validated and the Curtin–Hammett kinetic hierarchy is functionally confirmed by its consequence. Advances RI-03 (SRG-4), CLA-1 (provides the framework to include L1 system).

4. **EP-05a [Quantitative-ranking substantiation pack]** — Measure E_ox by CV for benzylic trifluoroborate 33 and aryl trifluoroborate 34 (the eq 3 competition substrate pair) to confirm the electrochemical basis for the 91:0 selectivity; extend to one secondary alkyltrifluoroborate and compare to Ir* excited-state oxidation potential. Advances RI-05 (CLA-2), RI-07 (SRG-9).

Certification-gate note: The experimental investment order above follows information gain (Stern–Volmer discriminates pathway first, solvation PES validates the quantitative gap, VT-ee validates DKR, CV closes E_ox gaps), but the final VQ-3 certification follows the inheritance gate order VQ-1 → VQ-2 → VQ-3 → VQ-4 and requires all of RI-03, RI-04, and RI-06 to be resolved.

**Second objective function: VQ-4 (Benchmark)**

VQ-4 additionally requires resolution of RI-08 and RI-09:

**Shortest route to VQ-4 (after VQ-3 is certified):**

5. **EP-08a [Replication / uncertainty pack]** — For the three most significant scope entries (one benzylic, one secondary alkyl, one silicate), report yield as mean ± standard deviation over three replicate reactions, and specify isolated vs. GC yield basis for all scope table entries. Advances RI-08 (SRG-7, SRG-8).

6. **EP-09a [Internal benchmark pack]** — Select five substrates that appear in both the new photoredox/Ni protocol and refs 7a–7f (prior secondary alkyl Suzuki–Miyaura protocols, e.g., from Figure 2) and conduct head-to-head yield comparisons under matched substrate conditions. Advances RI-09 (C-1).

---

### §6 Contribution to institutional design

**New representative cases for existing RI codes:**

**RI-06 (Imported model) — cycle-level import with cross-system solvation mismatch:** This paper provides a clear case of RI-06 scope note application: the entire Ni catalytic cycle PES is imported not only from another substrate system (benzylic/bromobenzene) but from a computational environment (SMD-water) that is dielectrically mismatched to the experimental solvents (dioxane, acetone/MeOH) by factors of 2–40. This case refines the RI-06 case-specific implementation to include "solvation-model mismatch" as a specific subtype: when an imported computational model is run under an implicit solvation condition that differs from the experimental dielectric by more than a factor of 5, the RI-06 characterization should always include solvation sensitivity as a mandatory EP-06a component. This is a new implementation note not previously documented in the v0.2a codebook.

**RI-05 (Qualitative overread) — BDE thermodynamics applied as kinetic argument:** SRG-6 (thioetherification HAT) provides a clear RI-05 case where a thermodynamic quantity (13 kcal/mol BDE difference) is used to draw a kinetic conclusion ("renders this process irreversible"). This is a recurring pattern in radical chemistry papers where BDE arguments are deployed without rate data. The case-specific implementation — compare the rate of HAT from thiol (k_HAT measured by laser flash photolysis against the target thiol at relevant concentration) to the rate of radical addition to Ni under catalytic conditions (k_add estimated from organometallic radical trapping rates) — should be added as a canonical implementation of RI-05 for HAT-mediated selectivity claims.

**PRI-11 (Mechanism–kinetics decoupling) — confirmation case:** The Curtin–Hammett DKR mechanism (SRG-4) exhibits a precise isomorphism with PRI-11: the proposed catalytic cycle (DKR mechanism via NiIII homolysis/recombination) is not used to derive a rate law algebraically; the mechanism is supported only by agreement of computed ΔΔG‡ values with observed ee values (Figure 10B), without an algebraic derivation of the ee equation from the mechanism or independent measurement of k_interconvert and k_RE. This case provides the second independent paper confirmation for PRI-11 (after Breitenfeld 2014 + Pengfei 2024 as the two-paper standard), but with a novel variant: PRI-11 here applies not to a rate law for conversion but to an enantioselectivity law. The PRI-11 definition should be extended: [REDACTED: substantial verbatim quotation; see Tier 9] This extension makes PRI-11 applicable to stereodetermination claims as well as rate claims.

**New pattern detected — Self-reinforcing computational loop:**

This paper exemplifies a pattern not previously codified: the computation and the mechanistic claim form a closed loop in which (a) the DFT PES (Figure 9) establishes the pathway preference (B1 > A1), (b) the DKR model is built on the same PES (NiIII equilibration from the C–B2 homolysis barrier), and (c) the ee prediction (Figure 10B) uses the same functional and solvation model as (a) and (b) to generate "experimental validation" data. The loop is self-consistent but not externally validated: each component (pathway preference, DKR kinetic hierarchy, enantioselectivity prediction) is supported by a different inference from the same PES, creating the appearance of multiple independent confirmations when they are actually three faces of the same single computation. This pattern co-occurs with RI-06 (imported model) and RI-03 (unobserved explanatory) and requires both to be resolved together. **Proposed as PRI-12 candidate: "Self-reinforcing computational loop"** — a pattern in which the proposed catalytic mechanism, the kinetic hierarchy, and the stereochemical prediction are all derived from a single computational framework whose reliability is not independently validated, creating an appearance of multi-layered support from a single unvalidated source. Promotion criterion: isomorphic pattern confirmed in one additional paper with explicit three-component loop structure (mechanism + kinetics + observable prediction from same PES).

**Labeling mismatch pattern:**

A labeling mismatch is present in §2.5: the paper uses factual language ([REDACTED: substantial verbatim quotation; see Tier 9] "the Ni¹ pathway predominates") throughout the mechanistic section, but the actual conclusion of the DFT analysis is a computed ΔΔG‡ that supports the preference only under the unvalidated solvation model. The hypothesis label ("we believe it is likely") appears once in the paper (in reference to the NiI pathway under catalytic conditions) but the mechanistic language in §2.5 uses factual verbs for the B1 pathway preference throughout. This labeling mismatch — hypothesis established as computational result but narrated as experimental finding — is concentrated in the mechanistic subsection and is invisible from the Accounts summary/outlook, where "pathway predominates" appears as an established fact. This co-occurs with RI-06 as expected from the codebook note.

**RI co-occurrence pattern:**

SRG-1+3 exhibits a new co-occurrence structure: RI-06 (solvation mismatch) and RI-01 (reporting integrity — ⟨S²⟩ absent) co-occur such that resolving only RI-06 (solvation sensitivity) is insufficient if RI-01 (spin-state assignment) remains unresolved. Specifically, even a correct solvation model would produce unreliable energies for open-shell Ni intermediates if spin contamination is present; the two RIs must be resolved jointly. This is a new co-occurrence case: RI-06 + RI-01 in the context of open-shell transition-metal DFT, requiring EP-06a (solvation validation) and EP-01a (spin-state reporting) to be implemented simultaneously rather than sequentially.

---

> **Tier 8 redaction notice**: This file is a redacted copy of the corresponding Tier 3 / Tier 9 output. Verbatim source-paper quotations have been replaced by `[REDACTED: see source paper §<loc>; full text retained in Tier 9 reviewer-only deposit]` markers, preserving location references and our own analytical content. Bibliographic fields (title, authors, journal, year, DOI), analytical labels (`evidence_chain:` with B-/U-/A-/C- internal IDs), short technical terms, and our own analytical text are not redacted. The redaction was applied by `scripts/redact_for_tier8.py` and, for this version, by `scripts/build_paperA_R1_public.py` with `scripts/redact_source_ngram_runs.py` (scripts of the project repository; they are not deposited).
