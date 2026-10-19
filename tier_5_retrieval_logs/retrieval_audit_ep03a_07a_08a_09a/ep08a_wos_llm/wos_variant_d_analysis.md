# EP-08a — WoS Variant D Analysis (2026-05-20)

## Query

```
TS=("Kumada-Tamao" OR "Kumada-Corriu") AND TS=("replicate" OR "n=3" OR "standard error" OR "variability") AND DT=(Article)
```

- Database: WoS Core Collection
- Filter: Document Type = Article
- Date executed: 2026-05-20
- Executor: User (Hokkaido U subscription)
- **Hit count: 0** ("Your search found no results")

## Interpretation

The strict named-reaction terminology (`Kumada-Tamao` or `Kumada-Corriu`, with hyphenated phrase matching) **combined with** replicate variability keywords (`replicate` / `n=3` / `standard error` / `variability`) returns **zero papers in WoS Core Collection**.

This 0-hit result is itself a **diagnostically informative** finding for the EP-08a negative claim:

1. **No paper in WoS Core Collection that uses the named-reaction terminology** (Kumada-Tamao or Kumada-Corriu, in hyphenated form) **also discusses replicate methodology** (replicate / n=3 / SD / variability) in its indexed topic field.
2. This is consistent with the Variants A, B, C findings — at every narrowing of the keyword combination toward the EP-08a target, the structured retrieval returns either zero or no applicable filler.
3. The result complements the cross-model LLM-parametric retrieval (Sonnet + GPT-5.4 cross-vendor convergence on unfilled status) at a **fourth independent retrieval dimension**.

## Diagnostic note — query design boundary

The 0-hit result also reflects a known property of WoS Topic search with hyphenated phrases:

- `"Kumada-Tamao"` (with hyphen, in quotes) matches only papers using the literal hyphenated form
- Papers using `"Kumada–Tamao"` (em-dash), `"Kumada Tamao"` (no hyphen, two words), or `"Kumada-Tamao-Corriu"` (longer compound) may not match
- The strict phrase form is the most conservative choice; broader alternatives are noted below

**Alternative Variant D′ (relaxed AND co-occurrence) executed 2026-05-20**:

```
TS=((Kumada AND Tamao) OR (Kumada AND Corriu)) AND TS=("replicate" OR "n=3" OR "standard error" OR "variability") AND DT=(Article)
```

**Hit count: 0** ("Your search found no results")

**Alternative Variant D″ (NEAR/3 proximity operator) executed 2026-05-20**:

```
TS=((Kumada NEAR/3 Tamao) OR (Kumada NEAR/3 Corriu)) AND TS=("replicate" OR "n=3" OR "standard error" OR "variability") AND DT=(Article)
```

**Hit count: 0** ("Your search found no results")

### Triangulation across three Variant D formulations

| Formulation | Syntax | Hit count |
|---|---|---|
| Variant D (strict phrase) | `"Kumada-Tamao" OR "Kumada-Corriu"` (hyphenated phrase, quoted) | 0 |
| Variant D′ (AND co-occurrence) | `Kumada AND Tamao` / `Kumada AND Corriu` (any topic-field co-occurrence) | 0 |
| Variant D″ (NEAR/3 proximity) | `Kumada NEAR/3 Tamao` / `Kumada NEAR/3 Corriu` (within 3 words) | 0 |

All three formulations — strict phrase matching, AND co-occurrence in topic field, and NEAR/3 proximity — return **zero papers in WoS Core Collection that combine "Kumada" + ("Tamao" OR "Corriu") with replicate methodology terms**.

This triangulation **rules out the hypothesis that the 0-hit result is a hyphen-syntax artifact**. The 0-hit finding is a **robust negative result** at the WoS-bibliographic-retrieval layer, independent of phrase-quoting / proximity / co-occurrence query design choice.

This is the strongest possible form of the Variant D diagnostic for the EP-08a negative claim: no paper in WoS Core Collection — under any of three orthogonal keyword-matching strategies — combines the named-reaction terminology with replicate variability keywords.

## Summary — Variant D

| Classification | Count |
|---|---|
| Complete filler | **0** |
| Partial filler | **0** |
| Minimal filler | **0** |
| Not applicable | **0** |
| **Total hits** | **0** |

## EP-08a WoS Module — final summary (4 variants complete)

| Variant | Query target | Hits | Complete | Partial | Minimal | Not applicable |
|---|---|---|---|---|---|---|
| A (strict) | Kumada/Ni-cat + cross-coupling + reproducibility | 3 | 0 | 0 | 0 | 3 |
| B (Ni-specific methodology) | Kumada-cpld/NiCl₂(dpe)/(dppe)/Ni-phosphine Grignard + triplicate/n=3/SD/CI | 1 | 0 | 0 | 0 | 1 |
| C (cis/trans + kinetic) | cis-/trans-stilbene/dichloroethylene + kinetic/thermodynamic/isomerisation + Ni/Grignard | 7 | 0 | 0 | 0 | 7 |
| D (named-reaction control) | Kumada-Tamao/Kumada-Corriu + replicate/n=3/SE/variability | 0 | — | — | — | — |
| **WoS Module Total** | — | **11** | **0** | **0** | **0** | **11** |

## EP-08a negative claim — final WoS Module diagnostic

Across four orthogonal WoS Variants (general Ni-Kumada-reproducibility / Ni-specific catalyst + replicate methodology / substrate-specific time-course / named-reaction control), **structured Web of Science Core Collection retrieval returned 11 candidate papers, none of which provide systematic replicate measurements (n ≥ 3 with reported SDs) for the dppe-Ni Kumada Table I substrate set per 0B §4 Complete / Partial / Minimal filler criteria**.

This independently triangulates the cross-model LLM-parametric retrieval finding (Sonnet + GPT-5.4 cross-vendor convergence on EP-08a unfilled status). The EP-08a negative claim is **strongly supported** at the WoS-bibliographic-retrieval dimension.

## Next steps

- ✅ EP-08a WoS Module complete (4 variants, 11 hits, 0 applicable)
- Optional: Scopus 4 variants for EP-08a (orthogonal database; nice-to-have for reviewer-defense thoroughness but not gating)
- **Recommended next**: EP-09a WoS Module (4 variants) — parallel HIGH-stakes negative claim
- Or EP-07a positive control if user prefers (2 variants, abbreviated)

## File locations

- Hit count summary: `validation/ep08a_wos_llm/hit_counts.md`
- All 4 variant raw exports: `validation/ep08a_wos_llm/wos_variant_{a,b,c}.txt` + Variant D = 0 hits (no export saved)
- Per-variant analyses: `validation/ep08a_wos_llm/wos_variant_{a,b,c,d}_analysis.md`
