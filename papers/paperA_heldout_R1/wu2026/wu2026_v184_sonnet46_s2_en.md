```
prompt_version: stage2-v184-en-20260502
model_info: claude-sonnet-4-6
```

[D-1] declared_motivation

novelty_claims:
- (T1) Rare intermolecular asymmetric Heck-type coupling of internal alkenes: [REDACTED: verbatim source quotation; see the source paper via its DOI] The paper explicitly positions the intermolecular variant of the asymmetric Heck reaction on internal cyclic alkenes as rare and underexplored.
- (T1) NHC ligand as enabling technology: [REDACTED: verbatim source quotation; see the source paper via its DOI] The development and application of the SIPE/ANIPE-type chiral NHC ligands (L1–L5) is presented as the key methodological advance.
- (T1) Quantitative performance: [REDACTED: verbatim source quotation; see the source paper via its DOI] — three independent performance axes each making an extreme-value claim.
- (T1) Mechanistic conclusion: [REDACTED: verbatim source quotation; see the source paper via its DOI] — a mechanistic novelty claim distinguishing this work from prior Ni-hydride-initiated hydroarylation reactions.
- (T1) Broad scope and practical utility: [REDACTED: verbatim source quotation; see the source paper via its DOI]
- (T2) Directing-group-free generality [paper-grounded inference: comparison asserted, not experimentally verified]: The paper implies that the absence of substrate directing groups makes this protocol more generally applicable than refs 26-34, but no side-by-side numerical comparison is provided.

success_criteria:
- (T1) High enantioselectivity (≥80% ee) across a broad range of aryl triflates and cyclic internal alkenes
- (T1) Good to excellent yields (the paper qualifies selected substrates as "good yields")
- (T1) Regioisomeric ratios >99:1 for most cyclic alkene substrates
- (T1) Gram-scale feasibility with comparable performance
- (T1) Functional group tolerance including heterocycles (morpholine, benzofuran, dibenzofuran)

layered_structure: yes — three partially independent claim layers exist:
  Layer 1 (Synthetic): the scope and efficiency of the Ni/NHC system for internal alkene Heck coupling. Refutability: requires showing prior art achieves comparable scope or finding a substrate class that fails.
  Layer 2 (Ligand design): the claim that bulky yet flexible NHC ligands are the key enabler. Refutability: requires showing that a different ligand class achieves the same result, or that NHC flexibility is not necessary.
  Layer 3 (Mechanistic): carbometallation vs. hydrometallation assignment. Refutability: requires showing that deuterium labeling and kinetics are consistent with hydrometallation. Layer 3 is the most fragile (U-1, U-2, U-3).
  Inter-layer dependency: Layer 3 (mechanistic) supports Layer 2 (ligand design rationale) — the NHC design reasoning rests on the carbometallation assignment. If Layer 3 falls, Layer 2's rationale weakens (though the ligand's empirical performance would persist). Layer 1 is the most independent.

---

[D-2] inferred_motivation

competitive_positioning: The paper positions against two groups of prior art: (i) directing-group strategies (refs 26-34), described as [REDACTED: verbatim source quotation; see the source paper via its DOI] — asserted advantage, not experimentally verified within this paper; (ii) Ni-phosphine methods for asymmetric Heck-type coupling (refs 35-42), described as not sufficiently general — similarly asserted. No head-to-head yield/ee comparison with any cited prior work appears in the results or conclusion sections. Both competitive advantages are stated claims (T2: comparison asserted, not experimentally verified).

concurrent_submissions: not applicable (no Note Added in Proof)

timing_pressure: The A items in Stage 1 are sparse (only A-1 through A-3), and most are about mechanistic understanding rather than synthetic completeness. This suggests the paper did not rush the scope development but did compress the mechanistic study. Specifically, A-2 (triflate mechanism labeled a "speculation") and U-1 (77% D incorporation without accounting) together suggest that mechanistic work was not fully completed before submission. Anchored to A-2 and U-1.

format_exploitation: The paper is an 11-page full article in CCS Chemistry, which accommodates extensive scope tables (four substrate scope/optimization tables, one mechanistic figure with five panels). The format does not appear to have been exploited to compress weaknesses. However, B-4 (no replicate data) and B-7 (no GC calibration details) represent standard methodological data that would be expected in full papers from leading synthetic journals and are absent here despite the full-paper format. Anchored to B-4, B-7.

audience_targeting: The paper's vocabulary ("C(sp³)-hybridized stereogenic carbon centers," "chiral dihydrofuran skeletons," "drug discovery," "medicinal chemistry") and example selection (aniline, carbobenzyloxy, morpholine, Boc substrates from pharmaceutical chemistry) indicate a synthetic chemistry audience with pharmaceutical synthesis interests, likely including industrial chemists evaluating method practicality.

institutional_visibility: [external inference — one sentence maximum] The paper's cross-institutional authorship (SIOC/CAS Shanghai, NUS Singapore, Ningbo) reflects a high-profile Chinese-Singapore synthetic chemistry collaboration that has recently produced multiple top-tier publications from these groups.

---

[D-3] institutional_motivation

journal_constraint: CCS Chemistry is the flagship journal of the Chinese Chemical Society, publishing full papers with high selectivity; the 11-page format allows comprehensive scope tables and SI but the limited mechanistic depth (Figure 2 with 5 panels for a full catalytic cycle) is consistent with what the journal accepts for a synthetic methodology paper prioritizing scope. Anchored to B-4 (no replicates — not required by journal norm for this format) and B-9 (Heck/reductive Heck ratio under standard conditions — a gap that may be acceptable in this journal's synthetic paper norms).

field_competition_state: [external inference] The asymmetric Ni-catalyzed alkene functionalization field has been growing rapidly since 2019, with at least 5–10 groups publishing related chemistry each year; the first demonstration of enantioselective intermolecular Heck coupling of internal cyclic alkenes without directing groups represents a priority-sensitive result in this highly competitive subfield. [external inference — one sentence maximum]

entry_criteria: The paper's framing implies that to be taken seriously in this area, a protocol must demonstrate: (i) ≥20 substrate examples with ≥85% ee for non-chelating internal alkenes in the intermolecular variant; (ii) at least one gram-scale example; (iii) some mechanistic evidence for carbometallation over hydrometallation (which distinguishes this from Ni-H initiated reactions in refs 64-69).

holy_grail_narrative: no — the paper uses "remains scarce," "challenging," and "fundamental and unresolved problem in synthetic chemistry" but does not employ "holy grail," "long-sought," "dream reaction," or similar quest-framing language.

commercialization_potential:
- (T1) "readily available aryl triflates" — positions the reaction as using accessible commercial starting materials
- (T1) "pharmaceutically relevant heterocycles, including morpholine" — explicitly flags pharmaceutical relevance
- (T1) gram-scale demonstration (1.36 g, 95% yield) — explicitly addresses synthetic scale
- (T1) "mild reaction conditions" — implies compatibility with sensitive functional groups relevant to medicinal chemistry

---

[D-4] Unquestioned motivations (English)

high_convergence_high_gap: none — fallback rule applied.
Fallback order: (a) no single-agent critical items; (b) high_convergence_low_gap items with convergence 2/3 prioritized; (c) SRG-1 (6 member items, largest group). Priority: U items (high severity, multi-critical protection), then SRG-rooted candidates, then B-1, then SRG-4/C items.

Extension ceiling applied: 8 candidates (default). U-1, U-2, U-3 are recorded independently (multi-critical U-item protection, v18.1).

---

**D-4 Candidate 1: Why is the proposed H-transfer from iPrOH incomplete (77% deuterium)?**

The paper proposes that the hydride originates from the methine C–H of isopropanol (iPrOH or iPrONa), distinguishing this from prior Ni-hydride-initiated hydroarylation. A carbometallation mechanism where the only H-source is the solvent iPrOH predicts that iPrOD-d8 (deuterated at the methine) would give ≈100% D incorporation. The paper reports 77% D incorporation.

The paper's mode of handling: the 77% value is reported without explanation and the conclusion ("the hydride likely originates from the methine") is drawn as if the 77% value is sufficient confirmation. The 23% unlabeled product is not discussed in the main text.

Consequence had it been answered: a mechanistic accounting of the 23% unlabeled product is necessary to distinguish between (a) partial H/D scrambling in the iPrOD-d8 solvent (would indicate a measurement artifact), (b) a parallel minor mechanism that uses a non-methine H-source (would indicate the mechanism is not as proposed), or (c) an analytical precision issue in D-incorporation quantification. If (b), the mechanistic interpretation of all the control experiments is compromised because the paper's distinguishing claim — "different from previous nickel hydride-initiated hydroarylation reactions" — depends on the H-source being exclusively the methine. If (a), the claim still holds but the evidence quality is lower than implied.

Relation to Stage 1 observations: directly grounded in U-1 (self-contradictory absence: model predicts ≈100% but 77% observed), A-2 (proposed mechanism labeled as "plausible"/speculative), and SRG-1 (mechanistic validation incompleteness).

grounded_in: U-1, A-2
key_quote: [REDACTED: see source paper; full text in Tier 9]
temperature_note: U-1 (V2=high, V3=high; convergence 2/3; gap=none) — drawn from high_convergence_low_gap
same_root_group: SRG-1 (Mechanistic validation incompleteness)

---

**D-4 Candidate 2: Does the BHT radical scavenger experiment genuinely rule out radical intermediates?**

The paper performs a radical scavenger experiment with 1.0 equiv butylated hydroxytoluene (BHT) and observes 85% product yield. From this, the conclusion is drawn that "radical intermediates are unlikely to be involved." This conclusion requires that the BHT concentration (1.0 equiv) be sufficient to intercept any radical intermediate within the productive catalytic timescale, and that a 15% yield reduction represents absence of radical involvement rather than a minor radical pathway operating in parallel.

The paper's mode of handling: the 85% yield is presented as a positive mechanistic conclusion without stating the detection limit of this experiment (i.e., the minimum radical flux that would reduce yield to ≤10% or ≤50%). The paper does not analyze whether 1.0 equiv BHT could intercept a transient radical intermediate with a half-life shorter than the BHT trapping timescale.

Consequence had it been answered: if the radical trapping window is properly characterized (by varying BHT equivalents from 0.1 to 10 equiv, or by using a faster radical clock), the conclusion about the ionic vs. radical character of the reaction becomes substantially more reliable. The mechanistic distinction between carbometallation (ionic) and radical carbometallation (radical) is the central claim of the mechanistic studies — a 15% yield reduction with 1.0 equiv BHT does not unambiguously support either assignment.

Relation to Stage 1 observations: grounded in U-2 (self-contradictory absence: 85% yield with radical scavenger is ambiguous), A-3 (unresolved isomerization control linked to reaction pathway), and SRG-1 (mechanistic validation incompleteness).

grounded_in: U-2, A-3
key_quote: [REDACTED: see source paper; full text in Tier 9]
temperature_note: U-2 (V2=high, flagged by V2 alone; convergence 1/3)
same_root_group: SRG-1 (Mechanistic validation incompleteness)

---

**D-4 Candidate 3: What is the actual precision of the kinetic rate-order assignments?**

The paper reports that the reaction is zero order in both internal alkene and aryl triflate, and first order in catalyst. These rate orders are the primary kinetic evidence for the mechanistic interpretation that the resting state is downstream of both substrate binding events. However, the paper provides no information about the number of data points per kinetic run, the concentration range over which zero-order behavior was verified, whether measurements were replicated, or the uncertainty (± value) of the derived rate orders.

The paper's mode of handling: the rate orders are presented as definitive conclusions ([REDACTED: verbatim source quotation; see the source paper via its DOI]) without statistical qualification. The kinetic plots in Figure 2e are referenced but the numerical quality metrics that would allow assessment of the rate-order precision are absent.

Consequence had it been answered: knowledge of the rate-order uncertainties would determine whether the kinetic data discriminate between zero-order and weak first-order behavior in each substrate. Zero-order kinetics in both substrates imply a resting state that is fully loaded with both substrates — but if the true order in triflate is 0.2 ± 0.3, the conclusion is not established. The rate-determining step identification (the mechanistic consequence of the zero-order kinetics) is the paper's explanation for why the NHC structure controls enantioselectivity.

Relation to Stage 1 observations: directly grounded in U-3 (prerequisite absence for mechanistic interpretation), B-4 (no replicate data across the study), and SRG-2 (quantitative measurement completeness).

grounded_in: U-3, B-4
key_quote: [REDACTED: see source paper; full text in Tier 9]
temperature_note: U-3 (V3=high; convergence 1/3)
same_root_group: SRG-2 (Quantitative measurement and reporting completeness)

---

**D-4 Candidate 4: Why do aryl halides completely inhibit the reaction, and what does this imply for the active catalytic species?**

The paper demonstrates that replacing aryl triflate with aryl chloride, bromide, or iodide completely inhibits the reaction (Figure 2d, N.R. for all three halides). This is presented as evidence for the "unique importance of aryl triflate for high efficiency," and the paper speculates that [REDACTED: verbatim source quotation; see the source paper via its DOI] However, the mechanistic reason for this complete inhibition — and the specific claim that a cationic Ni species is responsible — are not supported by any additional experiment.

The paper's mode of handling: the halide inhibition is treated as a positive feature (confirming the electrophile specificity), and the mechanistic speculation ("cationic aryl nickel species") is offered without testing. The speculation predicts that a cationic [Ar-Ni(NHC)]+ species (formed from ArOTf) should be more reactive toward carbometallation than a neutral [Ar-Ni(NHC)X] species (from ArX) — a prediction that could in principle be tested by stoichiometric reactions of isolated Ni complexes, or by using other cation-generating leaving groups (e.g., ArOMs, ArOTs, ArBF₄).

Consequence had it been answered: the cationic Ni hypothesis, if confirmed, would constitute a mechanistic design principle generalizable to other Ni-catalyzed reactions where triflates outperform halides. If refuted, the triflate requirement would need a different explanation (e.g., Ni(0)/Ni(II) vs. Ni(I)/Ni(III) manifold differences, leaving group coordination effects). The general applicability of the method — and the ligand design principle — depends on whether the triflate requirement is a fundamental feature or a contingent observation.

Relation to Stage 1 observations: grounded in B-1 (intentional narrowing to triflates with unexplained mechanistic basis), A-2 (speculation labeled as such), and SRG-1 (mechanistic validation incompleteness). Overlaps with C-3 (catalytic cycle imported from analogous systems).

grounded_in: B-1, A-2
key_quote: [REDACTED: see source paper; full text in Tier 9]
temperature_note: B-1 (V1=high, V2=high; convergence 2/3; gap=none) — drawn from high_convergence_low_gap
same_root_group: SRG-1 (Mechanistic validation incompleteness)

---

**D-4 Candidate 5: How is the absolute configuration assigned for the 58 products without X-ray crystallography?**

The paper reports 60 enantioselective transformations with ee values from chiral HPLC. Two products (3c and 4k) have X-ray crystallographic confirmation of absolute configuration. The remaining 58 products are characterized by ee values from chiral HPLC, but the method by which absolute configuration is assigned to each product is not stated in the main text or in the methods section. The paper defers HPLC parameters to SI but does not specify in SI (based on the SI reference in the main text) how the absolute configuration is determined for non-X-ray-confirmed products.

The paper's mode of handling: the X-ray structures of 3c and 4k are shown in Table 2, implying that these serve as configuration anchors. Whether HPLC elution order relative to the X-ray-confirmed standards is used to assign all other products — or whether optical rotation is used — is not stated.

Consequence had it been answered: the absolute configuration assignments are a core claim of an enantioselective synthesis paper. If HPLC elution order is used by analogy across structurally diverse substrates (Table 2 includes dihydrofurans, pyrrolines, chromanes, thiochromanes, acyclic alkenes, and styrene-type substrates), the validity of the analogy needs to be established. Misassignment of absolute configuration would not affect the paper's selectivity claims but would affect its usefulness for synthesis applications where the specific enantiomer matters.

Relation to Stage 1 observations: grounded in B-3 (reporting_omission: absolute configuration assignment method absent from main text), B-4 (no replicate data), and SRG-2 (quantitative measurement and reporting completeness).

grounded_in: B-3, B-4
key_quote: [REDACTED: see source paper; full text in Tier 9]
temperature_note: B-3 (V1=medium, V3=high; convergence 2/3; gap=low) — drawn from high_convergence_low_gap
same_root_group: SRG-2 (Quantitative measurement and reporting completeness)

---

**D-4 Candidate 6: Is the Ni/NHC system genuinely superior to prior Ni-phosphine and directing-group methods, or is this asserted?**

The paper's core novelty claim rests on being "more general and broadly applicable" than prior asymmetric Heck-type systems for internal alkenes. However, no direct numerical comparison of yield, ee, or substrate scope breadth with any specific cited prior work (refs 26-42) appears in the results or discussion. Ref 37 (Huang et al. 2021, Angew. Chem.) reports enantioselective reductive Heck of aryl triflates with Ni (the most directly comparable prior work) but its specific performance values are never placed alongside the current paper's results.

The paper's mode of handling: the superiority claim is framed by the introduction's citation of refs 35-42 as showing a persistent challenge, and the conclusion's statement that [REDACTED: verbatim source quotation; see the source paper via its DOI] The results section does not revisit this claim with data. The dropped quantitative benchmark pattern (C-1, C-2) means the paper can assert superiority without demonstrating it.

Consequence had it been answered: a table or figure directly comparing this work's performance (ee, yield, substrate scope diversity) against the closest prior Ni-based system (e.g., ref 37) would transform the "more general" claim from an assertion into a demonstration. Without this comparison, a reader cannot determine whether the improvement is incremental (e.g., 5 additional substrate examples at comparable ee) or transformative (e.g., an entirely new class of substrates now accessible with high ee).

Relation to Stage 1 observations: grounded in C-1 (Dropped Quantitative Benchmark — refs 35-42 cited but not compared), C-2 (refs 26-34 cited but not compared), and SRG-4 (Dropped prior-art numerical comparison).

grounded_in: C-1, C-2
key_quote: [REDACTED: see source paper; full text in Tier 9]
temperature_note: n/a (C items not in TEMPERATURE_SUMMARY)
same_root_group: SRG-4 (Dropped prior-art numerical comparison)

---

**D-4 Candidate 7: What is the Heck:reductive Heck product ratio under the standard conditions, and what controls this selectivity?**

The paper claims that in the presence of NaOiPr, "reductive Heck" product predominates, while in its absence, "Heck" product predominates. The evidence for this branching is that reducing NaOiPr gives "desired product 4f in 27%, alongside undesired Heck products" (B-9). Under standard conditions (3.05 equiv NaOiPr), the paper does not state whether the reductive Heck product is the exclusive product or merely the major product, and does not characterize the Heck:reductive Heck ratio.

The paper's mode of handling: the sentence about "undesired Heck products" under reduced NaOiPr conditions is used solely as mechanistic evidence for the carbometallation mechanism. The question of what controls the Heck/reductive Heck competition under standard conditions is not addressed.

Consequence had it been answered: quantifying the Heck:reductive Heck ratio as a function of base equivalents would establish whether the selectivity is sharp (e.g., >99:1 reductive Heck at 3 equiv base) or gradual (e.g., 90:10 at 3 equiv, 70:30 at 2 equiv). If the standard conditions give only 90% reductive Heck, the ee of the Heck by-product and its structure would be analytically significant. More importantly, the mechanistic competition between β-H elimination (Heck) and hydride transfer (reductive Heck) — and whether this is kinetic or thermodynamic control — remains entirely uncharacterized.

Relation to Stage 1 observations: grounded in B-9 (reporting_omission of Heck product quantity under standard conditions), A-2 (speculative mechanistic understanding), and SRG-1 (mechanistic validation incompleteness).

grounded_in: B-9, A-2
key_quote: [REDACTED: see source paper; full text in Tier 9]
temperature_note: B-9 (V2=high; convergence 1/3)
same_root_group: SRG-1 (Mechanistic validation incompleteness)

---

**D-4 Candidate 8: Is the claimed isomerization suppression of 2,5-dihydrofuran demonstrated or merely claimed?**

The paper's strongest novelty claim for the dihydrofuran substrates (Tables 2 and 4) is that it achieves selectivity that "has yet to be reported" for 2,5-dihydrofuran — which was previously impossible [REDACTED: verbatim source quotation; see the source paper via its DOI] However, the paper provides no direct evidence that 2,3-dihydrofuran (the isomerization product of 2,5-dihydrofuran) is absent or suppressed under the reaction conditions. If 2,3-dihydrofuran forms even in 5–10% yield, it would be a distinct substrate capable of undergoing Heck coupling to give a structurally different product, complicating the product ee and rr assignments.

The paper's mode of handling: the isomerization challenge is raised in the introduction as the reason previous work failed, and the paper implicitly claims to have overcome it by the fact that good yields and ee values are obtained. But no control experiment (e.g., reaction with pure 2,3-dihydrofuran, or GC analysis of the crude reaction for 2,3-dihydrofuran, or NMR monitoring during the reaction) is reported to confirm isomerization suppression.

Consequence had it been answered: if 2,3-dihydrofuran forms during the reaction and also undergoes Heck coupling (likely at a different rate and with different enantioselectivity), the ee values reported in Table 4 would represent a mixture of products from two distinct substrates. If 2,3-dihydrofuran is not present, this demonstration would be a genuinely important mechanistic observation: the Ni/NHC system kinetically competes with substrate isomerization under these conditions.

Relation to Stage 1 observations: grounded in A-3 (deferred/forgotten: isomerization suppression not evidentially closed), B-5 (modified conditions for certain substrates may reflect partial isomerization sensitivity), and SRG-3 (scope boundary and failure disclosure).

grounded_in: A-3, B-5
key_quote: [REDACTED: see source paper; full text in Tier 9]
temperature_note: A-3 (V1=medium, V2=high; convergence 2/3; gap=low) — drawn from high_convergence_low_gap
same_root_group: SRG-3 (Scope boundary and failure disclosure)

---

questions_that_cannot_be_asked:
- The authors' rationale for not conducting stoichiometric experiments with Ni(0) + ArOTf to characterize intermediate I is not accessible from the paper's text; the decision not to do this experiment reflects the authors' experimental priorities, which are not stated. [grounded_in: none (retrospective)]
- Whether the synthetic route was optimized for patent-oriented substrate coverage or for fundamental scope understanding is not determinable from the paper. [grounded_in: none (retrospective)]

priority_structure: 
The dominant structure visible across the 8 candidates is a two-tier pattern: the mechanistic evidence (Candidates 1, 2, 3, 4, 7) is systematically compressed by the paper's framing of each control experiment as conclusive, while the quantitative rigor supporting the mechanistic conclusions (Candidates 3, 5) is not established. This structure can be read as: the paper's mechanistic narrative (Figure 3, the proposed catalytic cycle) depends on three control experiments (D-labeling, BHT, kinetics) each of which has an internal ambiguity (77% D, 85% yield with BHT, undisclosed kinetic precision), and the analogy-based cycle import (C-3) fills the gap rather than independent evidence.

Pivot items:
A-2 ↔ B-1 (pivot): The paper's mechanistic speculation about "cationic aryl nickel species" (A-2) and the experimental observation that halides give no product (B-1) together form a pivot: the paper chooses to label the mechanistic hypothesis as speculation rather than testing it, while simultaneously relying on the mechanistic narrative to justify the ligand design rationale. If the cationic Ni hypothesis were tested and confirmed, it would strengthen both the mechanism claim and the ligand design principle simultaneously.

U-1 ↔ B-9 (pivot): The incomplete D incorporation (U-1, 77%) and the uncharacterized Heck by-product (B-9) together point to the same unresolved question: the H-transfer step (step 4 of the proposed cycle) that is responsible for the reductive Heck selectivity is the least experimentally grounded step in the cycle; if it were fully characterized, both the D-labeling ambiguity and the Heck:reductive Heck selectivity would be resolved.

---

[E] Questions of scope

The paper answered the question: "Can a Ni catalyst bearing a bulky chiral NHC ligand selectively promote enantioselective carbometallation of internal cyclic alkenes with aryl triflates under mild conditions, giving high regio- and enantioselectivity without requiring a substrate-directing group?"

derived_from: D-4-4 (triflate/Ni mechanistic rationale), B-1, A-1
anchoring_note: T1 for the scope and selectivity claims; T2 for the mechanistic rationale underlying the design principle.

Scope abstraction and transformations:

1. Narrow chemistry analogy (same structure, different metal): Can Pd or Fe NHC catalysts achieve enantioselective reductive Heck coupling of internal cyclic alkenes without directing groups? — same structure in a different guise (metal substitution).

2. Broader chemical design principle: Can bulky, flexible chiral ligands redirect reactive metal intermediates away from kinetically preferred but non-productive pathways (β-H elimination) toward enantioselective productive pathways, in any intermolecular transformation involving prochiral cyclic substrates? — a framework question about ligand steric control of competing reaction pathways.

3. Asymmetric catalysis design principle: Under what conditions can chiral ligand environment alone overcome the intrinsic kinetic preference for an unselective process in intermolecular reactions of hindered internal substrates? — a generalization to asymmetric catalysis design.

4. Beyond chemistry — philosophy of catalytic design: When does substrate structural bias cease to be necessary for asymmetric control, and can catalyst structural complexity substitute for substrate direction in the limit? — this moves beyond chemistry into general questions of "where must the selectivity come from?"

The broadest transformation with highest chemical reach: Transformation 2 (whether bulky chiral ligands can redirect reactive intermediates away from non-productive pathways toward enantioselective outcomes) is selected because: (a) it extends beyond Ni/NHC and internal cyclic alkenes to any metal/ligand/substrate combination where competing elementary steps (productive vs. unproductive) are controlled by ligand steric profile; (b) it is a framework question that encompasses asymmetric Heck, Reppe, Kumada coupling, and other reactions where β-H elimination vs. productive coupling is the selectivity-determining branch point; (c) it is answerable within chemistry (unlike transformation 4 which moves into philosophy).

confirmed_english
confirmed_english_propositional: "Nickel/NHC complexes catalyze enantioselective reductive Heck or Heck coupling of internal cyclic alkenes with aryl or alkenyl triflates."
confirmed_english_question: "Can bulky chiral NHC ligands enable Ni-catalyzed enantioselective carbometallation of internal cyclic alkenes without substrate directing groups, and does this represent a general principle for controlling β-H elimination selectivity in intermolecular Heck-type reactions?"
scope_type: "framework_question"

inference_time_sec: not available — inject externally

---

> **Public-cut redaction notice**: verbatim quotations from the analysed papers in this file have been replaced by `[REDACTED: …]` markers (rules in the repository README). The unredacted file is in the reviewer version of the deposit.
