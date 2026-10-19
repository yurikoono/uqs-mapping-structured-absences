# Alternative WoS Queries for EP-03a (Sensitivity Analysis)

**Purpose.** Explore how query reformulation changes the retrieved set, to understand which choices in the original query (v1) drove the zero-overlap result against the LLM candidates.

**Original query (v1, 49 hits).** See `wos_query.txt`. Key constraints:
- Diphosphine-required (`diphosphine OR dppe OR dpe OR dppp OR dmpe`)
- No reaction-context constraint (Kumada / cross-coupling not required)
- Five AND-clauses (metal × ligand × species × operation × method)

---

## Variant A: Drop diphosphine restriction — test monodentate phosphine coverage

**Rationale.** Four of six LLM candidates (Parshall 1974, Yamamoto 1978, Vicic 2004/2006) use monodentate PEt₃ / PPh₃. Relaxing the ligand clause to any phosphine should recover these. Predicts substantially more hits.

```
TS=(
  (nickel OR Ni)
  AND (phosphine OR phosphan* OR "PEt3" OR "PPh3" OR diphosphine OR dppe OR dpe OR dppp OR dmpe)
  AND (intermediate* OR "organometallic species" OR nickelacycle* OR arylnickel* OR alkylnickel*)
  AND (characteriz* OR identif* OR observ* OR detect* OR isolat*)
  AND (spectroscop* OR NMR OR EPR OR "X-ray" OR IR OR "UV-vis" OR XRD OR crystallograph*)
)
AND PY=(1972-2026)
AND DT=("Article")
AND WC=("Chemistry, Inorganic & Nuclear" OR "Chemistry, Multidisciplinary" OR "Chemistry, Organic")
```

**Expected outcome.** 5–20× more hits than v1. Should include Parshall 1974, Yamamoto 1978. High noise from unrelated Ni–phosphine chemistry. Triage cost increases proportionally.

---

## Variant B: Kumada / cross-coupling context required — narrow by reaction system

**Rationale.** v1 retrieves many Ni–diphosphine complexes unrelated to cross-coupling (hydrogenase models, electrocatalysis). Adding a reaction-context clause should restrict to Kumada-relevant chemistry. Predicts fewer but more relevant hits.

```
TS=(
  (nickel OR Ni)
  AND (diphosphine OR "bis(phosphine)" OR dppe OR dpe OR dppp OR dmpe OR phosphine OR phosphan*)
  AND (intermediate* OR "organometallic species" OR arylnickel* OR alkylnickel* OR nickelacycle*)
  AND ("cross-coupling" OR "cross coupling" OR Kumada OR "Grignard" OR "C-C bond formation" OR "C-C coupling")
  AND (characteriz* OR identif* OR observ* OR detect* OR isolat*)
)
AND PY=(1972-2026)
AND DT=("Article")
AND WC=("Chemistry, Inorganic & Nuclear" OR "Chemistry, Multidisciplinary" OR "Chemistry, Organic")
```

**Expected outcome.** Smaller set than v1 (perhaps 20–80 hits). Should still miss Parshall/Yamamoto (they don't frame their work as "cross-coupling" in title/abstract — the coupling context was downstream). Likely captures Morrell-Kochi 1975, Vicic 2004/2006, Dawson 2020 — the papers explicitly framed as mechanistic studies of coupling.

---

## Variant C: Intermediate-isolation focused — different experimental operation

**Rationale.** v1 emphasizes "spectroscopic characterization." EP-03a filling is also satisfied by isolation of the active species (Parshall's isolation of trans-NiAr(X)(PEt₃)₂ is a filling event without spectroscopic emphasis). Tests whether shifting operational vocabulary changes the slice.

```
TS=(
  (nickel OR Ni)
  AND (phosphine OR phosphan* OR dppe OR dpe OR dppp OR dmpe)
  AND ("arylnickel" OR "alkylnickel" OR "organonickel" OR "Ni(Ar)" OR "Ni(aryl)" OR "NiR" OR "Ni-C" OR "nickelacycle")
  AND (isolat* OR synthes* OR preparat* OR "single crystal" OR "X-ray structure")
)
AND PY=(1972-2026)
AND DT=("Article")
AND WC=("Chemistry, Inorganic & Nuclear" OR "Chemistry, Multidisciplinary" OR "Chemistry, Organic")
```

**Expected outcome.** Different slice than v1. Higher chance of hitting Parshall 1974 / Yamamoto 1978 (both are isolation-and-characterization papers). Less overlap with 49 v1 hits. Possibly more pre-1985 records.

---

## Variant D: Ni(I)/Ni(III) paradigm-shift layer — target the 2004+ Vicic filling

**Rationale.** v1 cannot retrieve the alkyl-Kumada paradigm-shift filling (Vicic 2004/2006, Breitenfeld 2014) because its vocabulary is Ni(II)-centric. This variant targets the radical / Ni(I) / Ni(III) filling explicitly.

```
TS=(
  (nickel OR Ni)
  AND ("Ni(I)" OR "Ni(III)" OR "nickel(I)" OR "nickel(III)" OR "Ni-I" OR radical)
  AND (intermediate* OR "organometallic species")
  AND (isolat* OR characteriz* OR identif* OR observ* OR detect*)
  AND (EPR OR NMR OR "X-ray" OR spectroscop*)
  AND ("cross-coupling" OR "cross coupling" OR Kumada OR alkyl-alkyl OR alkyl-aryl)
)
AND PY=(2000-2026)
AND DT=("Article")
AND WC=("Chemistry, Inorganic & Nuclear" OR "Chemistry, Multidisciplinary" OR "Chemistry, Organic")
```

**Expected outcome.** Much smaller set (20–60 hits). Targets the post-2000 paradigm-shift layer specifically. Likely captures Vicic 2004/2006 and Nickamine-line work (Breitenfeld 2014).

---

## Design summary

| Variant | Ligand scope | Context clause | Operation emphasis | Expected size | Target LLM candidate recovery |
|---|---|---|---|---|---|
| v1 (baseline) | diphosphine only | none | spectroscopic | 49 | 0/6 |
| A | any phosphine | none | spectroscopic + isolation | ~300–1000 | Parshall, Yamamoto |
| B | any phosphine | cross-coupling required | characterization | ~30–80 | Morrell-Kochi, Vicic, Dawson |
| C | any phosphine | none | isolation + aryl/alkyl Ni | ~150–400 | Parshall, Yamamoto |
| D | any + Ni(I)/Ni(III) | cross-coupling required | EPR / radical emphasis | ~20–60 | Vicic 2004/2006, Breitenfeld |

## Recommended execution order

1. **Run Variant B first** (most focused; lowest triage cost; tests whether contextual narrowing yields the 2 cross-model-converged candidates: Morrell-Kochi and Dawson).
2. **Then Variant A** (broadest; tests whether Parshall/Yamamoto are recoverable at all via structured search).
3. **Skip C and D initially** unless A or B leave specific LLM candidates still unretrieved.

This two-query follow-up will let us report in the manuscript a defensible three-point picture: baseline precision, scope-expansion sensitivity, and reaction-context sensitivity — without running a full 4-cell matrix.
