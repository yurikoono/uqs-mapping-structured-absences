# Content-Level Verification Log

**Date**: 2026-04-20 (initial); 2026-04-21 (Yamamoto BCSJ papers verified via library hardcopy)
**Purpose**: Direct PDF reading to verify LLM content claims for each EP-03a filling candidate.

## Verified candidates

### Parshall 1974 *JACS* 96, 2360 (verified via PDF)

- **LLM claim (Opus 4.7)**: "trans-NiAr(X)(PEt₃)₂ の単離を独立に報告"
- **Actual content (confirmed)**: Oxidative addition of fluorohalobenzenes to M(PEt₃)₄ (M = Ni, Pd, Pt) yielding trans-MX(C₆H₄F)(PEt₃)₂ complexes. Isolation, ¹H/¹⁹F NMR, elemental analysis. Decomposition via reductive elimination. Ref 17b cites Tamao-Zembayashi-Kiso-Kumada *J. Organomet. Chem.* **1973**, *55*, C91 — direct Kumada lineage reference.
- **LLM accuracy**: ✅ Fully accurate
- **Ligand**: **PEt₃** (monodentate triethylphosphine)
- **EP-03a filling verdict**: Partial (analogous Ni system with monodentate PEt₃, not the dpe system)
- **Failure mode explanation**:
  - (i) pre-1991 abstract gap (WoS record confirmed to have AB field empty)
  - Even if diphosphine restriction relaxed, title alone ("σ-Aryl Compounds of Nickel, Palladium, and Platinum. Synthesis and Bonding Studies") cannot satisfy 5 AND-connected topical clauses in variants A, B, C, D

### Anderson-Jones-Vicic 2004 *JACS* 126, 8100 (verified via PDF)

- **LLM claim (Opus 4.7)**: "Ni(I)/Ni(III) 中間体を単離・EPR 検出し、Tamao-Kumada の Ni(II)/Ni(IV) vs Ni(0)/Ni(II) の曖昧性を alkyl 系では Ni(I)/Ni(III) 経路に再定式化"
- **Actual content (confirmed)**: (tpy)Ni(CH₃) complex 3 is isolated, characterized by magnetic susceptibility (µeff = 1.64 µB, Evans NMR method = 1 unpaired d-electron), cyclic voltammetry (reversible oxidation wave at −1.316 V vs Ag/Ag⁺ after erratum correction), X-ray connectivity structure. Stoichiometric reaction with cyclohexyl iodide at 25 °C gives methylcyclohexane (79%) via Ni(I) alkyl complex. Proposed radical Ni(I)/Ni(III) mechanism (Scheme 1) for catalytic cross-coupling of alkyl electrophiles. Ref 21 cites Morrell-Kochi 1975 as seminal electron-transfer work.
- **LLM accuracy**: ✅ Fully accurate for the Ni(I)/Ni(III) mechanistic claim
- **Ligand**: **Terpyridine (tpy)** (tridentate, not phosphine)
- **EP-03a filling verdict**: Paradigm-shift (Ni(I)/Ni(III) cycle, not Ni(0)/Ni(II) as in Kumada 1972)
- **Failure mode explanation**:
  - (ii) ligand-class gap: paper uses tpy, not phosphine; all five WoS variants require phosphine-family keywords → systematic exclusion by query design
  - (i) also applies: 2004 *JACS* communication, AB field empty in WoS record

### Anderson-Jones-Vicic 2004 erratum *JACS* 126, 11113 (verified via PDF)

- **Content**: Single paragraph correction to oxidation potential of compound 3 (original value incorrect; corrected value −1.316 V vs Ag/Ag⁺ in THF). Authors explicitly state: "This correction has no effect on the conclusions of the paper since, as expected, compound 3 can easily reduce alkyl halides."
- **Impact on EP-03a filling verdict**: none. Compound 3 identification, mechanism proposal, and Ni(I) active species evidence all unchanged.
- **Handling decision**: Case (A) minor correction; original paper treated as canonical, erratum noted as metadata.

## Pending verification (lower priority)

- Morrell-Kochi 1975 *JACS* 97, 7262 — PDF available, not yet read. LLM claim verifiable from WoS title alone ("Mechanistic Studies of Nickel Catalysis in the Cross Coupling of Aryl Halides with Alkylmetals — Role of Arylalkylnickel(II) Species as Intermediates"), matches LLM description.
- Jones-Martin-McFarland-...-Vicic 2006 *JACS* 128, 13175 — PDF available. WoS title ("Ligand redox effects in the synthesis, electronic structure, and reactivity of an alkyl-alkyl cross-coupling catalyst") and Vicic 2004 context confirm TPY-based paradigm-shift filling.
- Dawson 2020 *Chem. Eur. J.* — not yet uploaded locally, but WoS AB field available and fully substantiates LLM claim.

### Yamamoto-Hayashi-Yamamoto 1978 *BCSJ* 51, 2091 (verified via PDF, retrieved 2026-04-21)

- **LLM claim (Opus 4.7)**: Citation given as "Yamamoto-Kohara-Yamamoto 1978 *BCSJ* 51, 2091" with content description "trans-NiAr(X)(PEt₃)₂ 系の単離・特性評価（Kumada 系譜）"
- **Actual 1978 paper** (Takakazu Yamamoto, Yasuhiro **Hayashi**, Akio Yamamoto):
  - Title: "A Novel Type of Polycondensation Utilizing Transition Metal-Catalyzed C–C Coupling. I. Preparation of Thermostable Polyphenylene Type Polymers"
  - Content: Ni/Pd/Fe/Cr/Co catalysts (NiCl₂(bpy), NiBr₂(PPh₃)₂, PdCl₂(bpy) etc.) + Mg dehalogenation polycondensation of p-dihalobenzenes to poly(p-phenylene). Scheme 1 proposes a NiX₂L₂ → NiR₂L₂ → NiR'(X)L₂ catalytic cycle (intermediates **1** and **2**) in the Kumada 1972 lineage, and cites Kumada 1972 as ref 6(a). Fig. 3 reports time-course kinetics at 3 ± 1 °C.
  - **NO trans-NiAr(X)(PEt₃)₂ isolation, no monoarylnickel characterization**, no PEt₃ experiments.
- **LLM accuracy**: ❌ **Triple mismatch** between citation and described content:
  - (α) Authorship: 1978 middle author is Hayashi, not Kohara (Kohara is the 1981 middle author)
  - (β) Journal/year/volume/page: "1978 BCSJ 51, 2091" is the Hayashi polycondensation paper, not any isolation paper
  - (γ) Content: the described "trans-NiAr(X)(PEt₃)₂ isolation" matches neither 1978 (polycondensation, no isolation) nor 1981 (monoALKYL, not monoaryl)
- **EP-03a filling verdict for 1978 paper itself**: Contextual Kumada-lineage support (proposes mechanism, cites Kumada 1972) but **not an EP-03a filler** (no intermediate isolation)
- **Failure mode explanation**: (iv) Citation–content separation. The LLM apparently fused the *existence* of a Yamamoto–Kohara–Yamamoto isolation paper (which is 1981, and even then is for monoalkyl-Ni) with a generic "trans-NiAr(X)(PR₃)₂" content stub, producing a conflated citation with three independent errors.

### Yamamoto-Kohara-Yamamoto 1981 *BCSJ* 54, 2010 (verified via PDF, retrieved 2026-04-21)

- **Actual content** (Takakazu Yamamoto, Teiji **Kohara**, Akio Yamamoto):
  - Title: "Preparation and Properties of Monoalkylnickel(II) Complexes Having a Phenoxo, Benzenethiolato, Oximato, β-Diketonato, or Halo Ligand"
  - Thirteen monoalkyl-Ni(II) complexes of type NiR(Y)Lₙ (R = CH₃ or C₂H₅) isolated and characterized (elemental analysis, IR, ¹H/³¹P NMR, visible). Key complexes include **Complex 14 = NiEt(Cl)(bpy)**, Complex 10 = *trans*-NiMe(OCOPh)(PEt₃)₂, Complex 5 = *trans*-NiMe(OC₆H₄-p-C₆H₅)(PEt₃)₂.
  - **The paper explicitly states** (introduction, p. 2010): [REDACTED: verbatim source quotation; see the source paper via its DOI] — i.e., the monoarylnickel isolation is attributed to refs 8–10 (Hidai, Morrell-Kochi, Parshall-class papers), *not* to this paper.
- **EP-03a filling verdict**: Partial filler — monoALKYL-Ni analog of Kumada's proposed monoARYL-Ni intermediate. Validates the general NiR(X)Lₙ scaffold with bpy and PEt₃ ligand families but does not directly isolate the Ph-Ni-Cl-(dpe) species Kumada proposed.
- **Failure mode explanation for why this paper does not appear in any WoS variant**:
  - (i) Pre-1991 AB field gap (confirmed empty in BCSJ records of this era)
  - (ii) Title keyword "Monoalkylnickel" would require alkyl-Ni semantics in the query; all five variants restrict to aryl-type linkage phrases (e.g., "aryl halide", "Kumada"), so this paper is outside the intended query scope by design
- **Relationship to the LLM's 1978 citation error**: This is the paper that, with its authorship (Kohara), journal family (BCSJ), and isolation-type content, most plausibly served as the conflation source for the LLM's mis-citation. But even this paper does *not* describe the content the LLM claimed (trans-NiAr(X)(PEt₃)₂ isolation): it describes monoalkyl-Ni, with explicit textual demarcation from monoaryl-Ni work.

## Implications confirmed empirically

| Failure mode | Candidate(s) demonstrating it | Status |
|---|---|---|
| (i) Pre-1991 / selective 2000s AB gap | Parshall 1974, Morrell-Kochi 1975, Vicic 2004, Vicic 2006 | ✅ PDF-confirmed |
| (ii) Ligand-class semantic gap | Vicic 2004 (tpy), Vicic 2006 (tpy) | ✅ PDF-confirmed |
| (iii) Compound-name enumeration gap | Dawson 2020 (Xantphos) | ✅ WoS AB-confirmed |
| (iv) Citation-content separation (triple mismatch) | Yamamoto 1978 citation: author (Hayashi≠Kohara) + journal/year/volume (1978,51,2091 ≠ 1981,54,2010) + content (polycondensation / monoalkyl ≠ monoaryl isolation) | ✅ PDF-confirmed (both 1978 Hayashi polycondensation paper and 1981 Kohara monoalkyl paper read) |

---

> **Public-cut redaction notice**: verbatim quotations from the analysed papers in this file have been replaced by `[REDACTED: …]` markers (rules in the repository README). The unredacted file is in the reviewer version of the deposit.
