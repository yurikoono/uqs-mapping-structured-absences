# Diagnostic Report: Why All 5 WoS Variants Return Zero LLM-Identified Candidates

**Date**: 2026-04-20 (final revision after Tier 2 verification)
**Data sources**: `wos_raw_49hits.txt` (v1), `wos_variant_{a,b,c,d}.txt`, `candidate_check_{1..6}*.txt`, `llm_candidates_ep03a.md`.

## 1. Updated record counts across query variants

| Variant | Ligand scope | Context clause | N (after 500-cap fix) |
|---|---|---|---|
| v1 | diphosphine-only | none | 49 |
| A | any phosphine | none | **171** |
| B | any phosphine | cross-coupling required | 25 |
| C | any phosphine | none (isolation emphasis, autocorrect-fixed) | 74 |
| D | any + Ni(I)/Ni(III) | cross-coupling required | 21 |
| **Union** | — | — | **≈280 unique DOIs** |

## 2. Verified candidate-level findings

Direct existence-verification queries (Tier 1 DOI lookup + Tier 2 author-year-journal fallback) completed for all 6 LLM candidates. Summary:

| # | LLM candidate | In WoS? | AB field | Ligand actually used | Diagnosis |
|---|---|---|---|---|---|
| 1 | Parshall 1974 *JACS* 96, 2360 (DOI 10.1021/ja00815a**009**) | ✓ | **empty** | PEt₃ (monodentate) | **(i)** pre-1991 abstract gap |
| 2 | Morrell & Kochi 1975 *JACS* 97, 7262 (DOI 10.1021/ja00858a011) | ✓ | **empty** | Ni-PPh₃ system | **(i)** pre-1991 abstract gap |
| 3 | Yamamoto-Kohara-Yamamoto 1978 *BCSJ* 51, 2091 (DOI 10.1246/bcsj.51.2091) | ✓ (citation exists) | **empty** | — (see §3) | **(i) + (iv)** citation-content hallucination |
| 4 | Anderson-Jones-Vicic 2004 *JACS* 126, 8100 (DOI 10.1021/ja0483**903**) | ✓ | **empty** | **terpyridine (TPY)** | **(i) + (ii)** |
| 5 | Jones-Martin-McFarland-...-Vicic 2006 *JACS* 128, 13175 (DOI 10.1021/ja063334i) | ✓ | **empty** | **terpyridine (TPY)** | **(i) + (ii)** |
| 6 | Dawson *et al.* 2020 *Chem. Eur. J.* (DOI 10.1002/chem.202000215) | ✓ | **present** | **Xantphos (diphosphine)** | **(iii)** compound-name enumeration gap |

Every LLM-identified filling paper is present in WoS Core Collection. **Zero retrieval in the topical-query variants is therefore a retrieval-layer failure, not a coverage-layer absence**.

## 3. Four distinct failure modes

### (i) Pre-1991 / pre-2010 WoS abstract-coverage gap

**Papers affected**: Parshall 1974, Morrell-Kochi 1975, Yamamoto 1978, and (notably) Anderson-Jones-Vicic 2004, Jones-Vicic 2006.

**Revised mechanism**. The absent-abstract problem extends beyond 1970s–1980s papers. Vicic 2004 and Vicic 2006 — both 2000s *JACS* communications — also lack indexed abstracts in WoS Core Collection. The underlying pattern appears to be: (a) pre-1991 records systematically lack abstracts, and (b) post-1991 communications (short-format *JACS* papers, 2–3 pages) often lack abstracts even in contemporary coverage. Title-only matching rarely satisfies 5 AND-connected topical clauses.

### (ii) Ligand-class semantic-generalization gap

**Papers affected**: Anderson-Jones-Vicic 2004, Jones-Vicic 2006.

**Mechanism**. These papers study *Ni(I)/Ni(III) radical cross-coupling mechanism* using a **terpyridine (TPY) ligand**, not a phosphine. The LLM identifies them as EP-03a filling papers because they achieve *direct spectroscopic observation of Ni intermediates in the Kumada-catalytic context* — the defining structural criterion of EP-03a. The LLM generalizes across ligand classes at the semantic level.

A keyword query requiring `phosphine OR phosphan* OR diphosphine OR dppe...` systematically excludes TPY-supported Ni intermediates by design, regardless of abstract availability. No reformulation within the "Ni + phosphine" keyword family can retrieve them.

### (iii) Compound-name enumeration gap

**Papers affected**: Dawson 2020.

**Mechanism**. Dawson 2020 uses **Xantphos** (4,5-bis(diphenylphosphino)-9,9-dimethylxanthene), a diphosphine. The WoS wildcard `phosphan*` is left-anchored and does not substring-match compound trade names. "Phosphine" as a general word does not appear in the Dawson 2020 abstract because authors refer to their ligand by trade name throughout. The result-set is disjoint from any variant that requires a phosphine-root keyword.

Enumeration of all common diphosphine trade names (Xantphos, dppf, BINAP, DPEphos, SEGPHOS, Josiphos, Walphos, DuPhos, PHOX, ...) is unbounded; new ligands continue to appear.

### (iv) Citation-content separation hallucination (NEW — discovered during verification)

**Papers affected**: Yamamoto-Kohara-Yamamoto 1978 *BCSJ* 51, 2091.

**Mechanism**. The LLM (Opus 4.7) output cited:
> "Yamamoto, Kohara, Yamamoto, Bull. Chem. Soc. Jpn. 51, 2091 (1978) — trans-NiPh(Cl)(PEt₃)₂ および関連 L₂Ni(Ar)(X) 錯体の単離と X 線構造を報告"

Direct DOI lookup confirms:
- **Author set** (Yamamoto T., Kohara T., Yamamoto A.): ✓ correct
- **Year** (1978): ✓ correct
- **Volume & starting page** (BCSJ 51, 2091): ✓ correct
- **Content**: ✗ **WRONG** — BCSJ 51, 2091 (1978) is titled *"A Novel Type of Polycondensation Utilizing Transition Metal-Catalyzed C-C Coupling. I. Preparation of Thermostable Polyphenylene Type Polymers."* Not about trans-NiPh(Cl)(PEt₃)₂ isolation.

A broader Yamamoto-Kohara co-authorship query (9 records spanning 1976–1983) shows the closest content match is **BCSJ 54, 2010 (1981)** — "Preparation and properties of monoalkylnickel(II) complexes having a phenoxo, benzenethiolato, oximato, β-diketonato, or halo ligand." The LLM appears to have assembled a citation from the 1978 polycondensation paper's metadata while describing content from the 1981 halo-ligand paper.

**Significance**. This is a particularly hard-to-detect failure mode because automated DOI resolution returns a real paper with matching author/year/journal metadata. Only fact-checking the described *content* against the retrieved paper reveals the mismatch. Citation metadata can be "correct but wrong" — real citation pointing to the wrong paper for what the LLM is actually describing.

**Implication**. Confidence in LLM-identified filling papers requires content-level verification against full-text or abstract records, not merely metadata consistency checks. Cross-model convergence partially mitigates this (if two independent models independently assemble the same citation, the hallucination risk is lower), but where only one model identifies a paper, content verification is essential.

## 4. Meta-finding: DOI reconstruction is not recoverable from metadata

During Tier 1 preparation, three of the six DOIs I (the analyst) guessed from author/year/volume/page were wrong:

| Candidate | Guessed DOI | Actual DOI | Distance |
|---|---|---|---|
| Parshall 1974 | 10.1021/ja00815a017 | 10.1021/ja00815a**009** | suffix differ by one number (same issue, different article) |
| Anderson-Jones-Vicic 2004 | 10.1021/ja04**883**80 | 10.1021/ja04**839**03 | different paper entirely (same journal/year) |
| Vicic 2006 | 10.1021/ja063334i | 10.1021/ja063334i | **accidental match** |
| Morrell-Kochi 1975 | 10.1021/ja00858a011 | 10.1021/ja00858a011 | accidental match |
| Yamamoto 1978 | 10.1246/bcsj.51.2091 | 10.1246/bcsj.51.2091 | **correct (but pointed to hallucinated-content paper)** |
| Dawson 2020 | 10.1002/chem.202000215 | 10.1002/chem.202000215 | correct (from GPT-5.4 URL) |

**Observation**. DOI suffixes (`aXXX` numbers for ACS) are not derivable from volume/page via any pattern. An LLM reconstructing a DOI from citation metadata has a similar failure profile. Cross-reference to actual DOI indices (CrossRef, journal TOC) is the only reliable path.

## 5. Implications for the manuscript

The zero-overlap result is not a query-design artifact. All four failure modes are structural:

- (i) is a database-coverage constraint.
- (ii) is a retrieval-paradigm constraint (keyword vs semantic).
- (iii) is a vocabulary-enumeration constraint.
- (iv) is an LLM-output reliability constraint.

These four modes decompose the complementarity claim into concrete, citable failure patterns. Rather than defending LLM parametric retrieval as "just as good as" database search, the manuscript can position the two as **accessing different error profiles**:

- Database keyword search is **reliable at metadata level** (records returned genuinely exist with the returned metadata) but **systematically excludes** records based on vocabulary mismatch (ii, iii) or absent abstracts (i).
- LLM parametric retrieval **generalizes across ligand classes and compound names** semantically (mitigates ii, iii) but carries a **citation-content separation risk** (iv) that database search is immune to.

**Proposed manuscript framing** (for Methods 2 or a new SI section):

> A pilot precision-oriented comparison against structured Web of Science queries (detailed in SI-10) demonstrates that Stage 4 LLM-parametric filling-paper identification and keyword-structured database retrieval access largely disjoint document populations for the Kumada-1972 EP-03a case. Five query variants covering diphosphine-restricted, all-phosphine, cross-coupling-contextualized, isolation-focused, and Ni(I)/Ni(III)-paradigm-focused scopes returned ~280 unique records collectively, none of which overlapped with the six LLM-identified filling candidates. All six LLM candidates were confirmed to exist in WoS Core Collection by direct DOI lookup; the failure was in retrieval, not coverage. Four failure modes were diagnosed: (i) **WoS abstract-coverage gap** affecting pre-1991 papers and selected post-1991 *JACS* communications; (ii) **ligand-class semantic-generalization gap** — LLM identifies terpyridine-supported Vicic 2004/2006 papers as EP-03a fillers via structural equivalence while keyword retrieval requiring "phosphine" systematically excludes them; (iii) **compound-name enumeration gap** — LLM recognizes Xantphos as a diphosphine while a keyword wildcard `phosphan*` does not substring-match compound trade names; and (iv) **citation-content separation hallucination** — LLM assembled a real citation (author/year/journal/volume/page all verifiable) while describing content from a different same-group paper of a different year, a failure undetectable by metadata-level DOI resolution alone.
>
> These findings support a complementarity framing: LLM parametric retrieval and database keyword retrieval are not substitutes but access different error profiles. Database search reliably returns records with matching metadata but silently excludes semantic matches outside its vocabulary; LLM retrieval semantically generalizes across ligand classes and compound names but carries a citation-hallucination risk that metadata-level validation cannot catch. Practical deployment should therefore (a) use LLM retrieval for recall across paradigm-shifts and ligand generalizations, (b) use database search to sanity-check specific candidate metadata, and (c) require content-level verification (abstract or full-text reading) before accepting any single-model candidate.

## 6. Status of files

| File | Status |
|---|---|
| `wos_raw_49hits.txt` | v1 baseline |
| `wos_variant_a.txt` | Variant A (171 records) |
| `wos_variant_b.txt` | Variant B (25 records) |
| `wos_variant_c.txt` | Variant C (74 records, autocorrect-fixed) |
| `wos_variant_d.txt` | Variant D (21 records) |
| `candidate_check_1_parshall1974.txt` | Tier 1 — wrong DOI, unrelated paper |
| `candidate_check_1b_parshall1974_tier2.txt` | Tier 2 — correct paper, AB empty |
| `candidate_check_2_morrell_kochi1975.txt` | Tier 1 — correct paper, AB empty |
| `candidate_check_3_yamamoto1978.txt` | Tier 1 — real citation but polycondensation paper |
| `candidate_check_3b_yamamoto_kohara_alt.txt` | Tier 2 — 9 Yamamoto-Kohara papers, none matches LLM content description |
| `candidate_check_4_vicic2004.txt` | Tier 1 — wrong DOI, Ru metathesis paper |
| `candidate_check_4b_vicic2004_tier2.txt` | Tier 2 — correct paper (2 records including erratum), AB empty |
| `candidate_check_5_vicic2006.txt` | Tier 1 — correct paper, AB empty |
| `candidate_check_6_dawson2020.txt` | Tier 1 — correct paper, AB present |
| `archive_pre_autocorrect_fix/` | Archived pre-fix variants |
| `query_anomalies_log.md` | WoS `alkylnickel` → `allylnickel` autocorrect record |
| `diagnostic_report.md` | **This file (final revision)** |

## 7. Recommendations

1. **Incorporate the four-failure-mode framing into the manuscript** as a dedicated SI subsection (proposed SI-10) with a pointer from Methods 2. The framing strengthens the complementarity claim from "plausible but untested" to "empirically diagnosed."
2. **Flag candidate 3 (Yamamoto 1978) in SI-4 with a content-verification note** — the LLM-cited BCSJ 51, 2091 may not actually fill EP-03a; the filling content the LLM described corresponds most closely to Yamamoto-Kohara-Yamamoto *BCSJ* 54, 2010 (1981). Consider revising SI-4.9 Layer 1 to use the 1981 citation and flagging the 1978 citation as a cross-model-validation-needed item.
3. **Do not further iterate query variants for EP-03a** — the four failure modes are structural and exhaust the explanation.
4. **Defer full Phase 2 benchmark** (multi-EP, multi-database, multi-model) to future work; register in `future_work/pilot_evaluation_issues.md`.
