prompt_version: stage1-v184-20260502
model_info: claude-sonnet-4-6

NOTE (Arm W — stub only): Body text is not available. The full document
information consists solely of the bibliographic stub (Title / Authors /
Journal / Year). Questions anchored to the title text are labeled T1 or T2.
All questions requiring knowledge beyond the stub are labeled T3 [external
inference]. Quotes are drawn from the title where possible; otherwise
"not recoverable from stub" is noted. Location references are "not
recoverable" throughout.

---

target_title:   Selective Carbon-Carbon Bond Formation by Cross-Coupling of Grignard Reagents with Organic Halides. Catalysis by Nickel-Phosphine Complexes
target_authors: Kohei Tamao, Koji Sumitani, Makoto Kumada
target_start:   not stated (stub only — page/line information not available)
target_end:     not stated (stub only — page/line information not available)

---

[Turn 1: Agent V1]
field: Synthetic organometallic chemistry / transition-metal-catalyzed C–C bond formation
field_rationale: BIB-3 (JACS) and BIB-1 (title references Grignard reagents, organic halides, and nickel-phosphine complexes) place this paper squarely in synthetic organometallic chemistry; S0-4 is not available from the stub but the title specifies catalytic cross-coupling as the primary method.

V1-Q1 | loc: not recoverable from stub | quote: [REDACTED: verbatim source quotation; see `loc:`] (title) | question: By what metric and numerical criterion is "selectivity" defined? Is the selectivity of cross-coupling over homo-coupling reported quantitatively, and if so, is it expressed as a cross/homo ratio, yield of each product, or GC ratio? | severity: high | inference_tier: T2 [paper-grounded inference: "selective" in title implies a selectivity measurement must exist]

V1-Q2 | loc: not recoverable from stub | quote: [REDACTED: verbatim source quotation; see `loc:`] (title) | question: What range of organic halides is demonstrated — aryl chlorides, bromides, iodides, vinyl halides, or alkyl halides? The title uses the broad term "organic halides" without specifying the halide or hybridization of the carbon center. | severity: high | inference_tier: T2 [paper-grounded inference: "organic halides" is a category broader than what any single paper can cover]

V1-Q3 | loc: not recoverable from stub | quote: [REDACTED: verbatim source quotation; see `loc:`] (title) | question: What range of Grignard reagents was tested — arylmagnesium, alkylmagnesium, or vinylmagnesium halides? The title does not specify the organometallic coupling partner beyond "Grignard Reagents." | severity: high | inference_tier: T2 [paper-grounded inference: Grignard reagents span multiple classes with different reactivity]

V1-Q4 | loc: not recoverable from stub | quote: [REDACTED: verbatim source quotation; see `loc:`] (title) | question: Which specific nickel-phosphine complexes were used? What is the rationale for the choice of phosphine ligand denticity and electronics? The title specifies the catalyst class but not the individual complex. | severity: medium | inference_tier: T2 [paper-grounded inference: "Nickel-Phosphine Complexes" is a class description requiring specification]

V1-Q5 | loc: not recoverable from stub | quote: not recoverable from stub | question: What catalyst loading (mol%) is employed, and is a turnover number (TON) or turnover frequency (TOF) reported to characterize catalytic efficiency? | severity: medium | inference_tier: T3 [external inference: standard expectation for a catalysis paper]

V1-Q6 | loc: not recoverable from stub | quote: not recoverable from stub | question: Are the reported yields GC yields, isolated yields, or both? What is the mass balance for reactions where significant homo-coupling or other side products might account for remaining substrate? | severity: high | inference_tier: T3 [external inference: yield basis is a standard reporting requirement in synthetic chemistry]

V1-Q7 | loc: not recoverable from stub | quote: not recoverable from stub | question: What reaction conditions (solvent, temperature, reaction time, base if any) were employed, and were these systematically optimized or reported as a single set of conditions? | severity: medium | inference_tier: T3 [external inference: condition reporting is standard in synthetic communication papers]

V1-Q8 | loc: not recoverable from stub | quote: not recoverable from stub | question: What is the functional group tolerance of the reaction? Are carbonyl groups, esters, nitriles, or other electrophilic functional groups compatible with Grignard-based cross-coupling? | severity: high | inference_tier: T3 [external inference: Grignard reagents are incompatible with many functional groups; functional group tolerance is a key limitation of Kumada coupling]

V1-Q9 | loc: not recoverable from stub | quote: not recoverable from stub | question: Are sp3-hybridized electrophiles (alkyl halides with sp3 carbon centers) included in the substrate scope, or is the reaction limited to sp2 electrophiles (aryl and vinyl halides)? | severity: medium | inference_tier: T3 [external inference: limitation to sp2 electrophiles is a well-known feature of early Kumada coupling but is not stated in title]

V1-Q10 | loc: not recoverable from stub | quote: not recoverable from stub | question: For Grignard reagents with beta-hydrogens (e.g., n-alkyl or sec-alkyl), is beta-hydride elimination a competing pathway, and if so, is its extent quantified? | severity: medium | inference_tier: T3 [external inference: beta-hydride elimination is a known concern in Ni-catalyzed coupling with alkyl Grignards]

V1-Q11 | loc: not recoverable from stub | quote: not recoverable from stub | question: What is the scope of the "selective" cross-coupling in terms of geometric (E/Z) selectivity for vinyl-containing substrates or coupling partners? Are vinyl products formed with retention or scrambling of geometry? | severity: medium | inference_tier: T3 [external inference: geometric selectivity is a key parameter in vinyl cross-coupling]

V1-Q12 | loc: not recoverable from stub | quote: not recoverable from stub | question: Is the catalyst formed in situ from NiX₂ and phosphine, or is a preformed complex used? What is the evidence that a single species is the active catalyst rather than a mixture of phosphine-nickel complexes? | severity: medium | inference_tier: T3 [external inference: catalyst speciation in Ni-phosphine systems is complex and rarely fully characterized in early communications]

V1-Q13 | loc: not recoverable from stub | quote: not recoverable from stub | question: What characterization of the homo-coupling byproduct(s) is provided — are they identified structurally, and is their formation quantified across all substrate combinations? | severity: medium | inference_tier: T3 [external inference: quantification of homo-coupling is needed to evaluate selectivity claims]
