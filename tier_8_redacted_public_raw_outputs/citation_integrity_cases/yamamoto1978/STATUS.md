# STATUS — `yamamoto1978/`

> **Note (2026-10-19).** SI section numbers in this card are those of April 2026: the citation-integrity material cited as SI-10 (e.g. SI-10.3 (iv)) is SI-9 of the present SI (SI-9.3 (iv)).

**Paper**: Takakazu Yamamoto, Yasuhiro **Hayashi**, Akio Yamamoto, *Bull. Chem. Soc. Jpn.* **1978**, *51*, 2091–2097. "A Novel Type of Polycondensation Utilizing Transition Metal-Catalyzed C–C Coupling. I. Preparation of Thermostable Polyphenylene Type Polymers."

**Retrieval pathway**: SI-10 WoS × PDF cross-check (library hardcopy scanned 2026-04-21). This paper was cited by Opus 4.7 as an EP-03a filler for Kumada 1972, but PDF verification established it is a polycondensation paper with no trans-NiAr(X)(PEt₃)₂ isolation — see SI-10.3 (iv) for the triple-mismatch citation-content hallucination diagnosis.

**Analysis status**: ✅ **Complete** (2026-04-21). Initial plan was to defer to Phase 2 (§1.14 of `future_work/deferred_items_registry.md`); the analysis was subsequently executed the same day via Sonnet agent in one coherent session.

## Files

| File | Content |
|---|---|
| `yamamoto1978.pdf` | Analysis source (copy of `validation/ep03a_wos_llm/pdfs/yamamoto1978_bcsj_51_2091.pdf`) |
| `yamamoto1978_v17_sonnet_s0.md` | Core claim, evidence types, prior-work position, methodology, reach |
| `yamamoto1978_v17_sonnet_s1_turn{1,2,3}.md` | Per-vantage Stage 1 extractions (V1 polymer chemistry / V2 organometallic / V3 methodology) |
| `yamamoto1978_v17_sonnet_s1.md` | Turn 4 integrated A/B/C/U classification + SRG + cross-field temperature |
| `yamamoto1978_v17_sonnet_s2.md` | D-1..D-4 motivational analysis, E-section scope propositions |
| `yamamoto1978_v17_sonnet_s3v2.md` | Assessment Sheet §1..§6 (Root-Issue Codebook, VQ judgment, Era-Norm, EP dictionary, shortest-reinforcement path) |
| `yamamoto1978_v17_sonnet_s4v2.md` | EP filling map for THIS paper (5 recommended candidates for Yamamoto 1978's own EPs) |

## Stage 3 headline (this paper's self-analysis)

- **SRGs**: 6 — SRG-1 absolute molecular weight absence; SRG-2 **catalytic cycle without experimental grounding**; SRG-3 kinetic data without rate-law analysis; SRG-4 no direct numerical comparison with conventional methods; SRG-5 homo-coupling byproduct + mass balance; SRG-6 stereo/regio chemistry assignment
- **CLAs**: 2 — CLA-1 Pd inactivity vs. Scheme 1 logical consistency (selective-Pd-inactivity not explained by the imported NiX₂L₂/NiR₂L₂ model); CLA-2 strong inference from negative evidence on end-group identification (D₂O/CO₂ probe without detection-limit disclosure)
- **VQ judgment**: VQ-1 passes (RI-02 non-fatal); VQ-2 passes qualified (RI-01, RI-07 non-fatal residuals; RI-05 minor residual); VQ-3 not reached (RI-06, RI-03, RI-04 all fatal for Scheme 1 mechanism; **PRI-11 non-fatal but mechanism-constraining**); VQ-4 not reached
- **Era-Norm**: dual-layer present — B-3 (Scheme 1 analogy import) is both communication-era tolerated AND modern-era deficient; 1978-era BCSJ full-paper norms tolerate qualitative kinetic-profile matches as mechanism support, but modern norms require algebraic rate-law derivation
- **EP dictionary for Yamamoto 1978**: **8 EPs** — EP-01a, EP-03a, EP-04a, EP-05a, EP-06a, EP-08a, EP-09a, **EP-10a** (the Kinetic verification pack, applied to Fig. 3 time-course data)

## Stage 4 headline (filling papers for Yamamoto 1978's own EPs)

Five primary filling candidates identified (Yamamoto-Kohara-Yamamoto 1981 *BCSJ*; Parshall 1974 *JACS*; Tamao-Sumitani-Kumada 1972 *JACS*; Tamao et al. 1976 *BCSJ*; Morrell-Kochi 1975 *JACS*). **Yamamoto 1981** (same group, subsequent paper) appears with **high confidence** as partial filler for EP-06a and EP-03a via monoalkyl-Ni(II) analog isolation. **Parshall 1974** appears with medium confidence as a direct trans-NiAr(X)(PEt₃)₂ filler that Yamamoto 1978 did not cite (pre-existing prior art not utilized — a C-item pattern).

## Cross-reference with Kumada 1972 (the manuscript-relevant observation)

The original deferral rationale registered in §1.14 of `deferred_items_registry.md` anticipated that Yamamoto 1978 would be a "mechanism-proposer without isolation" paper that inherits Kumada 1972's EP-03a gap rather than filling it. The UQS analysis **confirms this hypothesis with methodology-derived evidence**:

### Yamamoto 1978's relationship to Kumada 1972

| Dimension | Yamamoto 1978's behavior |
|---|---|
| Cites Kumada 1972 | ✓ (ref 6(a)) — explicitly in the Kumada lineage |
| Proposes a catalytic cycle in the Kumada mold | ✓ Scheme 1 (4 steps: NiX₂L₂ → NiR₂L₂ → NiR'(X)L₂ → coupling), intermediates **1** and **2** explicitly named |
| Isolates any Scheme 1 intermediate | ✗ — neither **1** nor **2** is observed, isolated, or spectroscopically characterized |
| Provides independent kinetic constraint | ✗ — Fig. 3 time-course profile given but no rate-law algebraic derivation from Scheme 1; PRI-11 applies |
| Rules out radical / alternative mechanism | ✗ — no TEMPO inhibition, no radical-clock, no crossover experiment |
| **Net role for Kumada 1972 EP-03a** | ✗ **Not a filler.** Yamamoto 1978 **inherits** Kumada's EP-03a gap (propose-without-isolation) and **extends it to the polymer-scale system**. |

This establishes the **"second-generation non-filler" chain**:

1. **Kumada 1972** proposes intermediates **1**, **2**, **3** for small-molecule cross-coupling without isolating any → EP-03a generated
2. **Yamamoto 1978** inherits that cycle, extends it to polycondensation (intermediates now polymer-bound), again without isolating any → EP-03a gap inherited and extended rather than closed
3. **Yamamoto 1981** (the sister paper with Kohara) provides the first **partial self-filling** at the alkyl-analog level — closing a structurally cognate but not identical form of the gap

### Parallel EP gaps (not cross-fills)

Yamamoto 1978's own EP dictionary includes EP-01a, EP-08a, EP-09a — the same codes open in Kumada 1972. Neither paper fills the other's version; the papers **share a genre-level absence profile** consistent with the SI-4.9 observation about early Ni organometallic literature conventions.

## Methodologically notable findings for the UQS project itself

### 1. PRI-11 (Mechanism-kinetics decoupling) — third independent confirmation

Yamamoto 1978's SRG-3 (Fig. 3 kinetic data without rate-law analysis) is a textbook instance of PRI-11 as defined in Codebook v0.2a:

> "提案触媒サイクルから速度式を代数的に導出せずに、観測速度次数との一致のみで機構を支持"

Breitenfeld 2014 (proposal) and Pengfei 2024 (second confirmation) brought PRI-11 to the "2-paper independent confirmation" threshold. **Yamamoto 1978 is now the third independent case**, strengthening the argument for elevating PRI-11 to a regular Root-Issue code (RI-11) in Codebook v0.3. This is relevant to `future_work/deferred_items_registry.md` §1.7 (Codebook v0.3 revision).

### 2. EP-10a (Kinetic verification pack) — first application outside Kumada 1972

EP-10a was added to the Kumada 1972 EP dictionary on 2026-04-19 via five-source cross-model derivation (see SI-3.7). Yamamoto 1978's analysis represents the **first independent application** of EP-10a to a different paper's own EP dictionary; the match is structurally close (both papers propose mechanism, produce Fig. 3-style time-course data, and do not derive rate law algebraically). This cross-paper applicability supports EP-10a's generality beyond its single-case origin.

### 3. Scheme-labeling mismatch pattern (detected in SRG-2 notes)

The S3 analysis surfaces a labeling pattern worth recording as a UQS observation candidate: Yamamoto 1978 introduces Scheme 1 with the hedge phrase "seems to proceed" but describes the individual steps using factual verbs ("formation of NiR₂L₂", "reaction of NiR₂L₂ with R'X to yield R-R"). The hedge label attaches to the overall cycle, while the step descriptions read as declarative facts. This creates a **visual separation between mechanistic hypothesis and mechanistic depiction** — a pattern that future UQS work may catalog as a recurring rhetorical mode in mechanism-proposer-without-evidence papers. Recommended for inclusion in Phase 2 Codebook revision notes.

## Cross-references

- Hallucination-victim diagnosis (the reason this paper is in `papers/ep/`): `manuscript/si/output/SI-10.md` §10.3 (iv)
- PDF-level verification log: `validation/ep03a_wos_llm/verification_log.md`
- Parent folder README: `papers/ep/kumada1972/README.md`
- Source-paper S3 for Kumada cross-reference: `../kumada1972_v17_sonnet_s3.md`
- Sister-paper S3 (Yamamoto 1981): `../yamamoto1981/yamamoto1981_v17_sonnet_s3v2.md`
- Phase 2 registry entry (now closed by this completion): `future_work/deferred_items_registry.md` §1.14
