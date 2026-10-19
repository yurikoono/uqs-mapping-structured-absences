# Direct Existence-Verification Queries for 6 LLM Candidates

**Purpose.** Determine for each of the 6 LLM-identified EP-03a filling papers whether (i) the paper is indexed in WoS Core Collection at all, and (ii) its abstract field is populated. Results disambiguate the three failure modes diagnosed in `diagnostic_report.md`.

**How to use.** For each candidate, run the two-tier query pair below in WoS Core Collection:
- **Tier 1 (primary)**: exact DOI lookup. Reliable if DOI is indexed.
- **Tier 2 (fallback)**: author + year + journal triangulation. Use if Tier 1 returns 0.

Export each resulting record (if any) to the file name indicated. If both tiers return 0, save an empty file with just the WoS header line (so the automation recognizes "confirmed absent").

## Candidate 1: Parshall 1974 *J. Am. Chem. Soc.*

Full citation: Parshall, G. W. *J. Am. Chem. Soc.* **1974**, *96*, 2360. DOI: 10.1021/ja00815a017

```
# Tier 1 — DOI lookup
DO=(10.1021/ja00815a017)

# Tier 2 — author-year-journal fallback
AU=(Parshall G*) AND PY=1974 AND SO=("JOURNAL OF THE AMERICAN CHEMICAL SOCIETY")
```

**Save export as**: `candidate_check_1_parshall1974.txt`

---

## Candidate 2: Morrell & Kochi 1975 *J. Am. Chem. Soc.*

Full citation: Morrell, D. G.; Kochi, J. K. *J. Am. Chem. Soc.* **1975**, *97*, 7262. DOI: 10.1021/ja00858a011

```
# Tier 1
DO=(10.1021/ja00858a011)

# Tier 2
AU=(Kochi J*) AND PY=1975 AND SO=("JOURNAL OF THE AMERICAN CHEMICAL SOCIETY")
# — the Tier 2 query will return multiple Kochi 1975 JACS papers; the target is the one with "Alkylnickel" or "Grignard" in the title
```

**Save export as**: `candidate_check_2_morrell_kochi1975.txt`

---

## Candidate 3: Yamamoto 1978 *Bull. Chem. Soc. Jpn.*

Full citation: Yamamoto, T.; Kohara, T.; Yamamoto, A. *Bull. Chem. Soc. Jpn.* **1978**, *51*, 2091. DOI: 10.1246/bcsj.51.2091

```
# Tier 1
DO=(10.1246/bcsj.51.2091)

# Tier 2
AU=(Yamamoto A*) AND PY=1978 AND SO=("BULLETIN OF THE CHEMICAL SOCIETY OF JAPAN")
```

**Save export as**: `candidate_check_3_yamamoto1978.txt`

---

## Candidate 4: Anderson-Jones-Vicic 2004 *J. Am. Chem. Soc.*

Full citation: Anderson, T. J.; Jones, G. D.; Vicic, D. A. *J. Am. Chem. Soc.* **2004**, *126*, 8100. DOI: 10.1021/ja0488380

```
# Tier 1
DO=(10.1021/ja0488380)

# Tier 2
AU=(Vicic D*) AND PY=2004 AND SO=("JOURNAL OF THE AMERICAN CHEMICAL SOCIETY")
```

**Save export as**: `candidate_check_4_vicic2004.txt`

---

## Candidate 5: Jones-Martin-McMurdo-Vicic 2006 *J. Am. Chem. Soc.*

Full citation: Jones, G. D.; Martin, J. L.; McFarland, C.; Allen, O. R.; Hall, R. E.; Haley, A. D.; Brandon, R. J.; Konovalova, T.; Desrochers, P. J.; Pulay, P.; Vicic, D. A. *J. Am. Chem. Soc.* **2006**, *128*, 13175. DOI: 10.1021/ja063334i

(Note: the Opus 4.7 output abbreviates this as "Jones, Martin, McMurdo, Vicic" — McMurdo may be a mistaken abbreviation of "McFarland." The actual 2006 JACS paper is by the Vicic group on Ni(I)/Ni(III) in alkyl-alkyl Kumada.)

```
# Tier 1
DO=(10.1021/ja063334i)

# Tier 2
AU=(Vicic D*) AND PY=2006 AND SO=("JOURNAL OF THE AMERICAN CHEMICAL SOCIETY")
```

**Save export as**: `candidate_check_5_vicic2006.txt`

---

## Candidate 6: Dawson 2020 *Chem. Eur. J.*

Full citation: Dawson, G. A. *et al.* *Chem. Eur. J.* **2020**, *26*, 8002. DOI: 10.1002/chem.202000215

```
# Tier 1
DO=(10.1002/chem.202000215)

# Tier 2
AU=(Dawson G*) AND PY=2020 AND SO=("CHEMISTRY-A EUROPEAN JOURNAL")
```

**Save export as**: `candidate_check_6_dawson2020.txt`

---

## Diagnostic decision tree (applied to each candidate after running the queries)

```
If Tier 1 returns 1 record → candidate IS in WoS, DOI is indexed. Check AB field:
    If AB is non-empty  → Diagnosis: abstract IS indexed. Must be (ii) or (iii) failure (ligand/compound-name gap).
    If AB is empty/absent → Diagnosis: (i) abstract-coverage gap, confirmed.

If Tier 1 returns 0 and Tier 2 returns ≥1 record → DOI not indexed but paper is indexed by author/title metadata:
    Check whether the target paper is among the hits.
    If yes → same as above (candidate in WoS).
    If no  → candidate not in WoS Core Collection at all; report as coverage gap.

If Tier 1 returns 0 and Tier 2 returns 0 → candidate is NOT in WoS Core Collection at all.
    Diagnosis: deepest form of coverage gap (not just abstract-missing, but record-missing).
```

## Expected outcome (hypothesis)

Based on the diagnosis in `diagnostic_report.md`:

| Candidate | Predicted WoS coverage | Predicted abstract | Expected Tier 1 / Tier 2 |
|---|---|---|---|
| 1. Parshall 1974 | Record exists | **absent** (pre-1991 gap) | T1:1 / T2:≥1, AB empty |
| 2. Morrell-Kochi 1975 | Record exists | **absent** (pre-1991 gap) | T1:1 / T2:≥1, AB empty |
| 3. Yamamoto 1978 | Record exists | **absent** (pre-1991 BCSJ) | T1:1 / T2:≥1, AB empty |
| 4. Vicic 2004 | Record exists | present | T1:1, AB present (confirms failure mode (ii): ligand gap) |
| 5. Vicic 2006 | Record exists | present | T1:1, AB present (confirms (ii)) |
| 6. Dawson 2020 | Record exists | present | T1:1, AB present (confirms (iii): compound-name gap) |

If the actual results match this prediction, the three failure modes are all confirmed empirically.
