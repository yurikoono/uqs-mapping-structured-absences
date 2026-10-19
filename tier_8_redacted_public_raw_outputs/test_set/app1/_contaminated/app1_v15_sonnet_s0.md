```
prompt_version: stage0-v15-20260331
model_info: claude-sonnet-4-6

[BIB-1] title: Palladium-catalyzed enantioselective Heck alkenylation of trisubstituted allylic alkenols: a redox-relay strategy to construct vicinal stereocenters
[BIB-2] authors: Chun Zhang, Brandon Tutkowski, Ryan J. DeLuca, Leo A. Joyce, Olaf Wiest, Matthew S. Sigman
[BIB-3] journal: Chemical Science
[BIB-4] year: 2017
[BIB-5] volume_pages: 8, 2277–2282
[BIB-6] doi: 10.1039/c6sc04585e
[BIB-7] format: full_paper
[BIB-8a] target_paper_start: page 2277: "Palladium-catalyzed enantioselective Heck"
[BIB-8b] target_paper_end: end of document

[S0-1] core_claim: [REDACTED: verbatim source text; see the source paper via its DOI] that [REDACTED: substantial verbatim quotation; see Tier 9]

[S0-2] evidence_type: Reaction optimization table (Table 1, 10 entries varying solvent and base); substrate scope table for alkenol substrates (Table 2, 11 substrates 3a–3k); alkenyl triflate scope table (Table 3, 15 substrates 3m–3y); alkenol substitution pattern evaluation (Table 4, 5 entries including (E)/(Z) comparison and homo- vs. allylic alkenols); cyclopropyl ring-opening cascade (Scheme 2, one substrate); DFT transition-state calculations at M06/6-31+G*/LANL2DZ level (Gaussian 09) for (E)- and (Z)-alkenol substrates; electronic circular dichroism (ECD) for absolute configuration determination of product 3d; isolated yields (0.25 mmol scale); er by SFC or HPLC.

[S0-3] prior_work_position: The paper explicitly builds on prior enantioselective redox-relay Heck reactions from the same group (ref 2a–f, Sigman group) that formed only a single (tertiary or quaternary) stereocenter. The stated gap is that [REDACTED: substantial verbatim quotation; see Tier 9] The present work claims to extend the redox-relay strategy to construct vicinal (two adjacent) stereocenters using trisubstituted alkenols (type 2), which prior work with di- and trisubstituted alkenes had not achieved. Early intermolecular asymmetric Heck work with acyclic olefins (refs 3, 8) is acknowledged as precedent for the challenge of enantioface discrimination on sterically encumbered trisubstituted alkenes.

[S0-4] methodology: Pd₂(dba)₃ as Pd(0) source with a chiral pyridine-oxazoline (PyrOx) ligand; trisubstituted allylic alkenol (2) and alkenyl triflate (1) as coupling partners; ethyl pivalate as optimized solvent; Li₂CO₃ as base; reactions run at 0.25 mmol scale; products isolated by chromatography; er determined by SFC or HPLC analysis; absolute configuration of 3d established by ECD; DFT transition-state geometry optimizations at M06/6-31+G*/LANL2DZ in Gaussian 09 to rationalize enantioselectivity differences between (E)- and (Z)-alkenol substrates.

[S0-5] conclusion_reach: The reaction is claimed to be effective for a range of trisubstituted allylic alkenols and alkenyl triflates (including cyclopentenone, lactone, β-keto ester, TMS, phthalimide, and natural product-derived triflates), providing generally high er (90–98:2) and >20:1 dr for most substrates. Limitations acknowledged: homoallylic alkenol 2z gave only 31% yield and 89:11 er, with the paper noting "the current system is optimized for allylic substrates"; (Z)-alkenol 2aa gave significantly reduced enantioselectivity (57:43 er); 2-bromo-substituted triflate 3p gave only 22% yield; cholesterol-derived 3y gave 26% yield; cyclopropyl substrate 3k gave 19% yield. Absolute configuration was determined for 3d by ECD; "other products were assigned by analogy to product 3d."

[S0-6] next_question_stated: [REDACTED: substantial verbatim quotation; see Tier 9]

[S0-7] note_added_in_proof: none.

inference_time_sec: not available — inject externally
```

---

> **Tier 8 redaction notice**: This file is a redacted copy of the corresponding Tier 3 / Tier 9 output. Verbatim source-paper quotations have been replaced by `[REDACTED: see source paper §<loc>; full text retained in Tier 9 reviewer-only deposit]` markers, preserving location references and our own analytical content. Bibliographic fields (title, authors, journal, year, DOI), analytical labels (`evidence_chain:` with B-/U-/A-/C- internal IDs), short technical terms, and our own analytical text are not redacted. The redaction was applied by `scripts/redact_for_tier8.py` and, for this version, by `scripts/build_paperA_R1_public.py` with `scripts/redact_source_ngram_runs.py` (scripts of the project repository; they are not deposited).
