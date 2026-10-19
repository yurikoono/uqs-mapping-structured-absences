<!-- model_info: claude-sonnet-4-6 -->

prompt_version: stage0-v19-20260504
model_info: claude-sonnet-4-6

---
<!-- boundary identification — mandatory before S0 fields -->

Step 1. Boundaries found in document:
  (i)  PDF p.1 left column, bottom: author/affiliation/date block "Yoshihisa Kiso, Keiji
       Yamamoto, Kohei Tamao, Makoto Kumada* / Kyoto University / Received February 12, 1972"
       — closes the hydrosilylation paper.
  (ii) PDF p.1 right column, mid-page: bold title "Selective Carbon–Carbon Bond Formation by
       Cross-Coupling of Grignard Reagents with Organic Halides. Catalysis by Nickel–Phosphine
       Complexes" followed by "Sir:" — START of target paper.
 (iii) PDF p.3 right column: bold title "Evidence for the Participation of Aspartic Acid-194
       in a New Acylation–Deacylation Reaction of α-Chymotrypsin" followed by "Sir:" — END
       of target paper / start of chymotrypsin communication.

Step 2. BIB-8a = boundary (ii).
Step 3. BIB-8b = boundary (iii).
Step 4. All fields below draw only from text between (ii) and (iii).

---

[BIB-1] title: Selective Carbon-Carbon Bond Formation by Cross-Coupling of Grignard Reagents with Organic Halides. Catalysis by Nickel-Phosphine Complexes
[BIB-2] authors: Kohei Tamao, Koji Sumitani, Makoto Kumada
[BIB-3] journal: Journal of the American Chemical Society
[BIB-4] year: 1972
[BIB-5] volume_pages: 94 (12), 4374–4376 [three-communication block; target communication occupies right column of p.4374 through left column of p.4376]
[BIB-6] doi: not found
[BIB-7] format: communication
[BIB-8a] target_paper_start: page 4374 (PDF p.1), right column: "Selective Carbon-Carbon Bond Formation by Cross-Coupling of Grignard Reagents with Organic Halides. Catalysis by Nickel-Phosphine Complexes"
[BIB-8b] target_paper_end: page 4376 (PDF p.3), right column: "Evidence for the Participation of Aspartic Acid-194 in a New Acylation-Deacylation Reaction of α-Chymotrypsin"
[S0-1] core_claim: The paper reports [REDACTED: verbatim source quotation; see the source paper via its DOI] with "generally very high" yields demonstrated across eleven substrate combinations in Table I.
[S0-2] evidence_type: Substrate scope table (Table I) reporting isolated or glpc yields for eleven Grignard reagent / organic halide combinations catalyzed by [NiCl₂(dpe)]; two detailed preparative procedures with characterization data (bp, refractive index, glpc, nmr, ir, and/or mass spectra); qualitative activity ranking of six Ni-phosphine complexes by observed yield (footnote 21, single substrate pair); proposed three-step catalytic cycle (eqs 2–4) based on literature precedent.
[S0-3] prior_work_position: Prior transition-metal-halide-induced coupling reactions [REDACTED: verbatim source quotation; see the source paper via its DOI] (refs 4–5); Tamura and Kochi's iron "soluble catalyst" (ref 6) is described as effective but "only for alkenyl halides"; π-allylnickel and lithium diorganocuprate reagents (refs 8–10) are acknowledged as "excellent reagents" but distinguished from catalytic use ("our interest centers on a transition metal catalyst").
[S0-4] methodology: Addition of a Grignard reagent to a vinyl or aryl organic halide in diethyl ether with catalytic [NiCl₂(dpe)] (1–0.1 mol%); reactions run at 0 °C to room temperature or reflux depending on substrate; products isolated by hydrolysis, extraction, and reduced-pressure distillation; yields determined by glpc with internal standard (selected entries) or by isolation (remaining entries).
[S0-5] conclusion_reach: Scope is limited to "only Csp2 halides, such as vinylic and aromatic"; "The experimental conditions are not necessarily optimum"; the stereochemical outcome of stilbene formation is described as "rather nonstereospecific"; mechanistic and stereochemical understanding is deferred as "further studies are required"; the reaction is called "promising."
[S0-6] next_question_stated: [REDACTED: verbatim source quotation; see the source paper via its DOI]
[S0-7] note_added_in_proof: Yes. Footnote 3a: [REDACTED: verbatim source quotation; see the source paper via its DOI] — acknowledges a concurrent independent discovery of Ni-catalyzed Grignard cross-coupling.
inference_time_sec: not available — inject externally

---

> **Public-cut redaction notice**: verbatim quotations from the analysed papers in this file have been replaced by `[REDACTED: …]` markers (rules in the repository README). The unredacted file is in the reviewer version of the deposit.
