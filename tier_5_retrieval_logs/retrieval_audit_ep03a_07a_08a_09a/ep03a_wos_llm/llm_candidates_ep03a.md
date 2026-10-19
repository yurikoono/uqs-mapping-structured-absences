# LLM-Identified EP-03a Filling Papers

**Source runs:** Kumada 1972 Stage 4 v2 (prompt v17), 2026-04-19.

- Opus 4.7: `papers/dev/kumada/kumada_v17_opus47_s4v2.md`
- GPT-5.4 Thinking: `papers/dev/kumada/gpt54thinking/kumada_v17_gpt54thinking_s4.md`

EP-03a is classified as Tier 1 (clearly trackable) by both models. The candidates listed below are the union of specific papers each model named as filling-onset or filling-establishment points for EP-03a.

## Consolidated candidate list

| # | Citation | DOI | Role (Opus 4.7) | Role (GPT-5.4) | Cross-model convergence |
|---|---|---|---|---|---|
| 1 | Parshall, *J. Am. Chem. Soc.* **1974**, *96*, 2360 | 10.1021/ja00815a017 | Filling-onset (independent trans-NiAr(X)(PEt₃)₂ isolation) | — | Opus-only |
| 2 | Morrell & Kochi, *J. Am. Chem. Soc.* **1975**, *97*, 7262 | 10.1021/ja00858a011 | Partial (EP-03a alongside EP-04a, EP-10a) | Filling-onset | **both models** |
| 3 | Yamamoto, Kohara, Yamamoto, *Bull. Chem. Soc. Jpn.* **1978**, *51*, 2091 | 10.1246/bcsj.51.2091 | Filling-onset (trans-NiPh(Cl)(PEt₃)₂, X-ray) | — | Opus-only |
| 4 | Anderson, Jones, Vicic, *J. Am. Chem. Soc.* **2004**, *126*, 8100 | 10.1021/ja0488380 | Filling-establishment (Ni(I)/Ni(III), EPR) | — | Opus-only |
| 5 | Jones, Martin, McMurdo, Vicic, *J. Am. Chem. Soc.* **2006**, *128*, 13175 | 10.1021/ja063334i | Filling-establishment (paired with 2004 paper) | — | Opus-only |
| 6 | Dawson et al., *Chem. Eur. J.* **2020**, *26*, 8002 | 10.1002/chem.202000215 | — | Filling-establishment (catalyst resting state) | GPT-only |

## Notes on filling characterization

- **Opus 4.7** reads EP-03a as spp²-channel (L₂Ni(Ar)(X)) plus paradigm-shift Ni(I)/Ni(III) alkyl channel; it cites two filling-onset points (Parshall 1974 / Yamamoto 1978) and two filling-establishment points (Vicic 2004 / 2006), rated High confidence.
- **GPT-5.4 Thinking** reads EP-03a as aryl-alkyl intermediate role + Kumada-system catalyst resting state; cites Morrell-Kochi 1975 (onset) and Dawson 2020 (establishment), rated High confidence with a caveat that 1975 is "related system" (Kochi-line, not dppe-specific) and 2020 is "Kumada but benzylic ether substrate."
- **Convergence at one paper**: Morrell & Kochi 1975 is identified by both models. This is the only cross-model-converged EP-03a filling candidate.

## Characteristics relevant to WoS comparison

- Four of the six papers (Parshall 1974, Yamamoto 1978, Anderson 2004, Jones 2006) use *monodentate* PEt₃ or closely analogous monophosphine — the reverse-engineered WoS query required "diphosphine/dppe/dpe/dppp/dmpe" and will therefore systematically miss them.
- Dawson 2020 uses a Ni/Xantphos-adjacent system in a Kumada benzylic-ether variant; the "Xantphos" and "ether" terminology may not match the specific keyword set used.
- Morrell & Kochi 1975 is pre-indexed era for some databases; abstract-level keyword capture depends on WoS legacy record completeness.

## Filling-type classification (for downstream comparison)

| Paper | Filling type | VQ level satisfied |
|---|---|---|
| Parshall 1974 | Partial (independent isolation, analogous Ni system) | VQ-3 |
| Morrell-Kochi 1975 | Partial (Kochi-line, not dppe-exact) | VQ-3 |
| Yamamoto 1978 | Partial (trans-NiPh(Cl)(PEt₃)₂ X-ray) | VQ-3 |
| Anderson-Jones-Vicic 2004 | Paradigm-shift (Ni(I)/Ni(III) alkyl channel) | VQ-3 (re-framed) |
| Jones-Martin-McMurdo-Vicic 2006 | Paradigm-shift (paired with 2004) | VQ-3 (re-framed) |
| Dawson 2020 | Indirect (state assignment in Kumada-type variant) | VQ-3 |
