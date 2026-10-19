[Turn 3: Agent V3]
field: Analytical chemistry / experimental design
field_rationale: S0-2 identifies GC yield tables as the primary evidence base; V1 raised yield calibration and V2 raised mechanistic gaps, but neither addressed systematic issues in experimental design — specifically replication, control experiments, compound identity verification methodology, and internal consistency of the quantitative claims across the table.

--- New questions ---

V3-Q1 | P529:Table1 footnote | [REDACTED: substantial verbatim quotation; see Tier 9] | No internal standard, GC calibration curve, or response factor correction is described for yield determination — what analytical method (internal vs. external standard, specific detector) was used to convert GC peak areas to molar yields? | high | T1

V3-Q2 | P529:Table1 | Runs 1–13 presented as single experiments with no error statistics | No replicate experiments are reported for any run — what is the run-to-run reproducibility of the GC yields, and would the characterization "almost quantitative" survive replicate measurement at ±5% standard deviation? | high | T2

V3-Q3 | P529:Table1 | Yields ranging from 4% to 100% across 13 runs | The Table spans an enormous yield range with no explanation of what determines high vs. low yield — is a systematic trend (steric, electronic, substrate concentration) discernible, and were conditions independently optimized per substrate or uniformly applied? | medium | T1

V3-Q4 | P530:Lcol:1-5* | [REDACTED: substantial verbatim quotation; see Tier 9] | Run 1 yields 75% 1:1 product + 8% 1:2 product = 83% GC yield total — the remaining ~17% is not accounted for; what are the other products and were they identified? | high | T1

V3-Q5 | P529:Table1 footnote | [REDACTED: substantial verbatim quotation; see Tier 9] | "Standard methods" for structure determination is unspecified — does this mean NMR only, or does it include mass spectrometry, X-ray crystallography for at least one representative product, or elemental analysis? | medium | T1

V3-Q6 | P529:Rcol:5-10* | [REDACTED: substantial verbatim quotation; see Tier 9] | Catalyst comparison data are described qualitatively without a common benchmark reaction — under identical conditions (same substrate, temperature, time), what yields do each alternative Ru complex produce relative to RuH₂(CO)(PPh₃)₃? | medium | T1

V3-Q7 | P530:Table1 | Run 4 uses an autoclave (6 kg/cm² ethylene pressure); all other runs open/reflux | Run 4 (ethylene, autoclave) cannot be directly compared with atmospheric-pressure runs — were any blank or control experiments conducted without catalyst to confirm the reaction is catalytic rather than thermally promoted under autoclave conditions? | medium | T2

V3-Q8 | P529:Lcol:1* | [REDACTED: substantial verbatim quotation; see Tier 9] | The substrate concentration (2 mmol in 3 mL ≈ 0.67 M) is not varied — was the effect of concentration on yield or selectivity tested, and could concentration-dependent side reactions (dimerization, olefin polymerization) explain the low yields in some runs? | low | T2

V3-Q9 | P530:Table1 | Run 6: yield 20% with 10 mmol olefin; Run 7: yield 4% with 10 mmol olefin | Runs 6 and 7 use the same excess olefin but give dramatically different yields (20% vs 4%) — what distinguishes these substrates electronically or sterically, and were reaction times or temperatures adjusted to probe the low-yield cases? | medium | T1

--- Overlaps with V1/V2 ---

V3-OV1 | overlaps_with: V1-Q3 | severity_V3: high | note: GC yield without calibration method is an analytical standards failure — reported yields cannot be independently verified or reproduced without knowing detector type, standard, and correction protocol.

V3-OV2 | overlaps_with: V1-Q5 | severity_V3: high | note: The missing ~17% mass balance in run 1 is a data integrity issue — unaccounted products could include Ru-containing organometallics, oligomers, or regioisomers that would change the yield accounting.

V3-OV3 | overlaps_with: V1-Q11 | severity_V3: high | note: "Almost quantitative yields based on both starting materials" with excess olefin is an internally inconsistent claim — 100% yield on both cannot hold simultaneously when olefin is present in 2–5-fold excess unless all olefin is recovered, which is not stated.

V3-OV4 | overlaps_with: V2-Q1 | severity_V3: medium | note: From an experimental design perspective, the absence of mechanistic controls (no blank without catalyst, no radical inhibitor test) means the paper cannot distinguish ruthenium catalysis from uncatalyzed thermal reaction under its own experimental conditions.

---

> **Tier 8 redaction notice**: This file is a redacted copy of the corresponding Tier 3 / Tier 9 output. Verbatim source-paper quotations have been replaced by `[REDACTED: see source paper §<loc>; full text retained in Tier 9 reviewer-only deposit]` markers, preserving location references and our own analytical content. Bibliographic fields (title, authors, journal, year, DOI), analytical labels (`evidence_chain:` with B-/U-/A-/C- internal IDs), short technical terms, and our own analytical text are not redacted. The redaction was applied by `scripts/redact_for_tier8.py` and, for this version, by `scripts/build_paperA_R1_public.py` with `scripts/redact_source_ngram_runs.py` (scripts of the project repository; they are not deposited).
