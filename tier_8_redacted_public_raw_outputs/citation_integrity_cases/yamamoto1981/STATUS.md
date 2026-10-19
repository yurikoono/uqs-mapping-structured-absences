# STATUS — `yamamoto1981/`

> **Note (2026-10-19).** SI section numbers in this card are those of April 2026: the citation-integrity material cited as SI-10 (e.g. SI-10.3 (iv)) is SI-9 of the present SI (SI-9.3 (iv)).

**Paper**: Takakazu Yamamoto, Teiji **Kohara**, Akio Yamamoto, *Bull. Chem. Soc. Jpn.* **1981**, *54*, 2010–2016. "Preparation and Properties of Monoalkylnickel(II) Complexes Having a Phenoxo, Benzenethiolato, Oximato, β-Diketonato, or Halo Ligand."

**Retrieval pathway**: SI-10 WoS × PDF cross-check (library hardcopy scanned 2026-04-21). This paper was **not** surfaced by any v17 Stage 4 run (Haiku 4.5 / Sonnet 4.6 / Opus 4.7 / GPT-5.4 Thinking). Its role as a candidate Partial EP-03a filler for Kumada 1972 was identified by the analyst after reading the PDF and is now substantiated by a full v17 UQS self-analysis (see §Files below).

**Analysis status**: ✅ **Complete** (2026-04-21). Full v17 + Stage 3 v2 + Stage 4 v2 pipeline executed in one Sonnet session.

## Files

| File | Content |
|---|---|
| `yamamoto1981.pdf` | Analysis source (copy of `validation/ep03a_wos_llm/pdfs/yamamoto1981_bcsj_54_2010.pdf`) |
| `yamamoto1981_v17_sonnet_s0.md` | Core claim, evidence types, prior-work position, methodology, reach |
| `yamamoto1981_v17_sonnet_s1_turn{1,2,3}.md` | Per-vantage Stage 1 extractions (V1 organometallic / V2 coordination chemistry / V3 methodology) |
| `yamamoto1981_v17_sonnet_s1.md` | Turn 4 integrated A/B/C/U classification + SRG + cross-field temperature |
| `yamamoto1981_v17_sonnet_s2.md` | D-1..D-4 motivational analysis, E-section scope propositions |
| `yamamoto1981_v17_sonnet_s3v2.md` | Assessment Sheet §1..§6 (Root-Issue Codebook, VQ judgment, Era-Norm, EP dictionary, shortest-reinforcement path) |
| `yamamoto1981_v17_sonnet_s4v2.md` | EP filling map for THIS paper (5 recommended candidates for Yamamoto 1981's own EPs) |

## Stage 3 headline (this paper's self-analysis)

- **SRGs**: 5 — SRG-1 structural characterization completeness; SRG-2 mechanism without direct evidence; SRG-3 mass balance / product accounting; SRG-4 quantitative spectroscopy; SRG-5 severed citations
- **CLAs**: 2 — CLA-1 acyl-alkyl coupling Ni product; CLA-2 catalytic-cycle connection
- **VQ judgment**: VQ-1 passes (first layer, non-fatal RI-02); VQ-2 passes for first layer, Qualified for coordination + reactivity layers; VQ-3 not reached (RI-03, RI-05, RI-06 all fatal for the mechanistic claims in Eq. 2, 4, 5); VQ-4 not reached
- **Era-Norm**: dual-layer present — 5 items tolerated by 1981 BCSJ full-paper norms, 5 items modern-era deficient, 2 items in both
- **EP dictionary for Yamamoto 1981**: 7 EPs across 6 codes (EP-02a, EP-03a ×2, EP-04a secondary, EP-05a, EP-06a, EP-08a, EP-09a)

## Stage 4 headline (filling papers for Yamamoto 1981's own EPs)

Five recommended candidates in the Stage 4 map (Henc et al. 1980 *J. Organomet. Chem.*; Yamamoto-Yamamoto-Ikeda 1971 *JACS* via its ref 18; Vrieze 1975 via ref 17; Stahl-Labinger-Bercaw-type Inorg. Chem. 1998 or analog; Jolly-Wilke 1975 "Organic Chemistry of Nickel"). EP-08a and EP-09a are classified as **Group 3 unfilled** on incentive-structure grounds (no publication motivation for replicating yield / mass balance, nor for catalytic performance tests of isolated model complexes).

## EP alignment with Kumada 1972 (the manuscript-relevant cross-link)

The primary reason this paper is in `papers/ep/kumada1972/` is its candidate role as a **Partial EP-03a filler for Kumada 1972**. Now that the full UQS pipeline is complete for both Kumada 1972 (`../kumada1972_v17_sonnet_s3.md`) and Yamamoto 1981 (this folder), the alignment can be stated with methodological traceability rather than analyst judgment alone.

### Kumada 1972's EP-03a (from `../kumada1972_v17_sonnet_s3.md` SRG-1)

Kumada's EP-03a requires: direct observation / state-assignment of intermediates **1** (Ph₂Ni(dpe)), **2** (PhNi(X)(dpe)), and **3** (transmetalation step) in the NiCl₂(dpe) + PhMgBr / PhCl system. Case-specific implementation calls for: (i) low-temperature NMR or ESI-MS of the stoichiometric PhMgBr + NiCl₂(dpe) reaction observing intermediate **1**; (ii) demonstrating that an isolated intermediate or analog (e.g., Me₂Ni(dpe)) reacts with PhCl to give the expected coupling product; (iii) EPR / radical-clock experiments to exclude Ni(I)/Ni(III) radical pathways.

### What Yamamoto 1981 does with respect to Kumada EP-03a

| Kumada EP-03a requirement | Yamamoto 1981 evidence | Filling depth |
|---|---|---|
| Isolation of a monoorgano-Ni(II) species analogous to intermediate **2** (R-Ni-X-L₂) | **Complex 14 = NiEt(Cl)(bpy)** isolated, fully characterized (elemental analysis, IR, ¹H-NMR, ³¹P-NMR, visible). **Complex 10 = *trans*-NiMe(OCOPh)(PEt₃)₂** isolated and characterized. | **Partial** — the NiR(X)Lₙ scaffold is empirically accessible, validated across bpy and PEt₃ ligand families, for R = Me, Et. |
| R = **aryl** (Kumada's system uses PhMgBr / PhCl) | R = **alkyl only** (Me, Et). The paper explicitly states: [REDACTED: verbatim source quotation; see the source paper via its DOI] (introduction, p. 2010), attributing monoaryl isolation to its refs 8–10 (Hidai 1971, Morrell-Kochi 1975, Uchino-Yamamoto-Ikeda 1975). | **Not filled** — the aryl case is demarcated by the paper itself as prior work of other groups. |
| L = **dpe** (Kumada's actual ligand) | L = **bpy** or **PEt₃**. dpe is absent from the Yamamoto 1981 ligand set. | **Not filled** — the specific chelate geometry that Kumada 1972 invokes as mechanistically important (see Kumada CLA-2 on bidentate diphosphine requirement) is outside the isolated scaffold. |
| Demonstration that the isolated intermediate undergoes the proposed coupling step (Kumada's eq 2 → 3) | Yamamoto 1981 does NOT connect its isolated complexes to catalytic cross-coupling. CLA-2 (catalytic-cycle connection) is flagged as unfilled in Yamamoto 1981's own Stage 3 (EP-09a, Group 3 unfilled). | **Not filled** — the paper explicitly declines to test catalytic relevance. |
| EPR / radical-clock exclusion of Ni(I)/Ni(III) pathway | Not performed. | **Not filled** |

### Verdict

**Partial filler** for Kumada 1972's EP-03a, with filling depth restricted to the *structural framework* layer. Specifically:

- ✅ **NiR(X)Lₙ scaffold** with a primary alkyl group and an X / heteroatom donor is experimentally accessible and stable enough for full characterization — this supports the *existence* of the compound class Kumada postulated.
- ❌ **R = aryl, L = dpe, catalytic connection, and Ni(I)/Ni(III) exclusion** remain unfilled. The aryl case is explicitly cited to refs 8–10 as separate prior work (Hidai 1971, Morrell-Kochi 1975, Uchino-Yamamoto-Ikeda 1975), which the analyst-driven SI-10 cross-check ultimately traces back into the already-identified Parshall 1974 / Morrell-Kochi 1975 arc from the LLM Stage 4 output.

### Parallel EP gaps between the two papers (not cross-fills)

Yamamoto 1981's own Stage 3 surfaces its EP-02a, EP-05a, EP-08a, EP-09a — the same EP codes that are open in Kumada 1972. This is a **parallel unfilled gap** structure, not a cross-filling relationship: both papers share reporting-integrity and benchmark-absence issues, but neither fills the other's version. In the manuscript narrative, this reinforces the SI-4.9 observation that early-1970s and early-1980s Ni organometallic papers inherited a genre-level set of absences that required decades to address systematically.

### EP-06a (analogy validation) — partial reinforcement

Kumada 1972's SRG-1 notes the paper's appeal to dipy-Ni analogs as a mechanistic model source (RI-06 imported model). Yamamoto 1981 actually isolates several bpy-coordinated NiR(Y)(bpy) complexes (complexes 2, 3, 4, 8, 9, 14), substantiating that bpy-Ni-alkyl species of the postulated kind are isolable. This is a **weak indirect reinforcement** of Kumada's analogy basis, not a direct filling (the analogy itself is about mechanistic equivalence, which Yamamoto 1981 does not test).

## Cross-references

- Triple-mismatch diagnosis (LLM hallucination that surfaced this paper): `manuscript/si/output/SI-10.md` §10.3 (iv)
- SI-6.7 revised row: `manuscript/si/output/SI-6.md` §6.7 (1981 row added as post-hoc retrieval-diagnostic filler)
- PDF-level verification log: `validation/ep03a_wos_llm/verification_log.md`
- Parent folder README: `papers/ep/kumada1972/README.md`
- Source-paper S3 for EP-alignment reference: `../kumada1972_v17_sonnet_s3.md`

---

> **Tier 8 redaction notice**: This file is a redacted copy of the corresponding Tier 3 / Tier 9 output. Verbatim source-paper quotations have been replaced by `[REDACTED: see source paper §<loc>; full text retained in Tier 9 reviewer-only deposit]` markers, preserving location references and our own analytical content. Bibliographic fields (title, authors, journal, year, DOI), analytical labels (`evidence_chain:` with B-/U-/A-/C- internal IDs), short technical terms, and our own analytical text are not redacted. The redaction was applied by `scripts/redact_for_tier8.py` and, for this version, by `scripts/build_paperA_R1_public.py` with `scripts/redact_source_ngram_runs.py` (scripts of the project repository; they are not deposited).
