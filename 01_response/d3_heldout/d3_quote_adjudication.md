# D3 held-out — S0–S2 quote adjudication (all FAILs + WARN < partial 85)

> **Note (2026-10-19).** This record gives the state of 2026-09-29. The author check of 2026-10-05 is in `01_response/verification/human_verification_D3D4_20260929.md` (the author's marks and notes) and is reported in SI-6.10 and SI-11.20; statements below that no human has verified the ratings or the adjudication describe the state before it.

Adjudicator: orchestrator (Claude), with the decisive cases checked on rendered page images. **Not yet verified by a human.**
Scope: 50 gate rows (48 unique strings). Earlier reports said 54; that number was wrong (Fable 5.1 review F2).

| class | meaning | rows |
|---|---|---|
| M | 原典を正確に伝えていない | 4 |
| B | 引用符内の語の追加（意味はほぼ同じ） | 1 |
| S | 原典に実在（表・図・text 層の崩れ・省略記号） | 16 |
| C | 意味を保った縮約・言い換え | 9 |
| A | model 自身の文、または gate の拾い誤り | 20 |

| paper | file | kind | gate | partial | class | string (≤110 chars) | basis |
|---|---|---|---|---|---|---|---|
| liu2026 | s2_en.md | quoted | WARN | 81.2 | M | concerted [4+2] electrocyclization | D-4: 'The paper assigns the ring-forming step as a "concerted [4+2] electrocyclization"'; source says '[4+2] electrocyclization' only (no 'concerted' in main or SI); the D-4 argument rests on the inserted qualifier |
| wang2026 | s2_en.md | quoted | WARN | 82.3 | M | anti-cancer agents, pesticide research, and functional materials | source: 'drugs, synthetic chemistry, pesticide research, and functional materials'; 'anti-cancer' only in ref. 1 title |
| wu2026 | s1.md | quoted | FAIL | 62.5 | M | recent advancements on asymmetric Ni-phosphine couplings | source p.2 (page image): 'asymmetric Heck-type couplings'; content word substituted |
| wu2026 | s2_en.md | key_quote | WARN | 78.4 | M | [REDACTED: verbatim source text; see the source paper via its DOI] | source p.2 (page image): 'asymmetric Heck-type couplings'; content word substituted |
| wang2026 | s1.md | quoted | WARN | 63.2 | B | merely four esterification derivatives | source: 'offering merely four derivatives'; word inserted inside quotation marks |
| liu2026 | s1.md | quoted | FAIL | 63.3 | S | representative recent advances | Scheme 1b label (page image) |
| liu2026 | s1.md | quoted | WARN | 65.2 | S | [REDACTED: verbatim source text; see the source paper via its DOI] | Table 1 entry 5 'nd (68% of 3a)' (page image) |
| liu2026 | s2_en.md | key_quote | WARN | 66.0 | S | [REDACTED: verbatim source text; see the source paper via its DOI] | Table 1 entry 7 (page image) |
| liu2026 | s1.md | quoted | WARN | 70.7 | S | [REDACTED: verbatim source text; see the source paper via its DOI] | present verbatim |
| liu2026 | s1.md | quoted | WARN | 75.0 | S | 20 mmol % DABCO 365 nd | Table 1 entry 7 (page image) |
| liu2026 | s2_en.md | quoted | WARN | 75.0 | S | 20 mmol % DABCO 365 nd | Table 1 entry 7 (page image) |
| liu2026 | s2_en.md | quoted | WARN | 78.2 | S | sustainable and efficient approaches... remain undeveloped | present, ellipsis |
| shekarizadeh2026 | s1.md | quoted | WARN | 70.0 | S | [REDACTED: verbatim source text; see the source paper via its DOI] cm³g⁻¹) co | present |
| shekarizadeh2026 | s1.md | quoted | WARN | 84.7 | S | [REDACTED: verbatim source text; see the source paper via its DOI] | Table 1; page image confirms column order C/O/N/Pd, so Pd = 41.72 is correct |
| wang2026 | s2_en.md | key_quote | FAIL | 57.9 | S | 5h, 66%, 1.3:1 dr; 5i, 65%, 1.2:1 dr" (Scheme 3) | values present in experimental section (1.3:1 dr, 1.2:1 dr); list spliced |
| wang2026 | s1.md | quoted | FAIL | 65.5 | S | 5h, 66%, 1.3:1 dr; 5i, 65%, 1.2:1 dr | values present in experimental section (1.3:1 dr, 1.2:1 dr); list spliced |
| wang2026 | s2_en.md | quoted | FAIL | 65.5 | S | 5h, 66%, 1.3:1 dr; 5i, 65%, 1.2:1 dr | values present in experimental section (1.3:1 dr, 1.2:1 dr); list spliced |
| wang2026 | s2_en.md | key_quote | WARN | 64.7 | S | bIsolated yield." (Table 1, footnote b) | Table 1 footnote b |
| wang2026 | s2_en.md | quoted | WARN | 78.3 | S | to overcome these limitations... we herein report | present, ellipsis |
| wu2026 | s2_en.md | quoted | WARN | 78.4 | S | [REDACTED: verbatim source text; see the source paper via its DOI] reactivit | present; ligature ﬂ breaks the text layer |
| wu2026 | s1.md | quoted | WARN | 83.6 | S | substrate-chelating protocol... [REDACTED: verbatim source text; see the source paper via its DOI] alk | present, ellipsis |
| liu2026 | s1.md | quoted | WARN | 83.3 | C | overcome the current obstacles | source: 'overcoming the current obstacles' |
| shekarizadeh2026 | s1.md | quoted | WARN | 61.3 | C | [REDACTED: verbatim source text; see the source paper via its DOI] | source: '[REDACTED: verbatim source text; see the source paper via its DOI]' |
| shekarizadeh2026 | s2_en.md | quoted | WARN | 69.6 | C | N-Pd electronic donation facilitating oxidative addition | source: '[REDACTED: verbatim source text; see the source paper via its DOI]' |
| shekarizadeh2026 | s2_en.md | quoted | WARN | 72.2 | C | completely overrides pore dimensions | source: 'completely overrides the minor reduction in pore dimensions' |
| shekarizadeh2026 | s2_en.md | quoted | WARN | 73.2 | C | [REDACTED: verbatim source text; see the source paper via its DOI] | source: '[REDACTED: verbatim source text; see the source paper via its DOI]'; reordered |
| wang2026 | s2_en.md | quoted | WARN | 76.9 | C | mechanistically distinct ionic manifold | source: 'mechanistically distinct' + 'ionic carbonylation manifold' |
| wang2026 | s2_en.md | quoted | WARN | 81.0 | C | overcomes limitations | source: 'overcomes the limitations of conventional radical pathways' |
| wu2026 | s2_en.md | quoted | WARN | 72.1 | C | C(sp³)-hybridized stereogenic carbon centers, | source: 'stereogenic sp3-hybridized carbon centers' |
| wu2026 | s1.md | quoted | WARN | 75.0 | C | ongoing research | source: 'Further research … is ongoing in our laboratories' |
| liu2026 | s1.md | quoted | FAIL | 47.8 | A | and the delegation to SI make the analytical basis for this claim unevaluable from the main text. The main tex | gate harvested text between two quoted terms |
| liu2026 | s2_en.md | quoted | FAIL | 49.8 | A | Can substrate-substrate EDA complex formation generate reactive radical intermediates that initiate a cascade  | E-section abstraction |
| liu2026 | s2_en.md | quoted | FAIL | 66.7 | A | (DABCO regenerated) and | gate harvested text between two quoted terms |
| liu2026 | s2_en.md | quoted | WARN | 59.1 | A | Can EDA complex photochemistry (DABCO/aryl iodide, 365 nm) drive a tandem Heck-type radical arylation and [4+2 | E-section: model's formulation of the question the paper answered |
| liu2026 | s2_en.md | quoted | WARN | 63.2 | A | system and DABCO as | gate harvested text between quoted 'photocatalytic' and 'the base' (both present in source) |
| shekarizadeh2026 | s2_en.md | quoted | FAIL | 50.3 | A | Does the coordination-site density of a molecular scaffold determine the loading density and per-site activity | E-section abstraction |
| shekarizadeh2026 | s2_en.md | quoted | FAIL | 58.3 | A | further work is underway | listed as language the paper does not use |
| shekarizadeh2026 | s2_en.md | quoted | WARN | 72.2 | A | framework_question | scope_type label |
| wang2026 | s2_en.md | quoted | FAIL | 49.5 | A | A gaseous hazardous reagent that defines a prior method's mechanism can be replaced by a solid stable surrogat | model's scope abstraction |
| wang2026 | s2_en.md | quoted | FAIL | 63.2 | A | Note Added in Proof | model states there is NO Note Added in Proof |
| wang2026 | s2_en.md | quoted | WARN | 78.6 | A | dream reaction. | listed as language the paper does not use |
| wang2026 | s2_en.md | quoted | WARN | 81.2 | A | ionic, no radical. | model's summary of the paper's logic |
| wu2026 | s2_en.md | quoted | FAIL | 51.7 | A | Can a Ni catalyst bearing a bulky chiral NHC ligand selectively promote enantioselective carbometallation of i | E-section formulation |
| wu2026 | s0.md | quoted | FAIL | 51.8 | A | compared to the well-developed intramolecular variants, and that substrate-chelating directing-group strategie | gate harvested text between two quoted source phrases |
| wu2026 | s0.md | quoted | FAIL | 55.3 | A | The paper positions its approach as providing a | gate harvested text between two quoted source phrases |
| wu2026 | s2_en.md | quoted | FAIL | 55.6 | A | framework_question | scope_type label |
| wu2026 | s2_en.md | quoted | FAIL | 57.3 | A | product predominates. The evidence for this branching is that reducing NaOiPr gives | gate harvested text between quoted 'reductive Heck' / 'Heck' |
| wu2026 | s2_en.md | quoted | FAIL | 58.5 | A | product predominates, while in its absence, | gate harvested text between quoted 'reductive Heck' / 'Heck' |
| wu2026 | s2_en.md | quoted | FAIL | 61.1 | A | where must the selectivity come from? | model's rhetorical question |
| wu2026 | s1.md | quoted | WARN | 47.4 | A | requires that the BHT concentration (1.0 equiv) be sufficient to intercept any radical intermediate on a times | gate harvested text between quoted 'unlikely' and next quote |
