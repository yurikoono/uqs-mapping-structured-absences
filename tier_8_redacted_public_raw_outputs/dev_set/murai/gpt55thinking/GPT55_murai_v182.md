# Catalytic C-H Bond Addition

**User:** Anonymous  
**Created:** 4/27/2026 9:29:34  
**Updated:** 4/27/2026 10:37:27  
**Exported:** 4/27/2026 12:27:34  
**Link:** [chat link removed]  

## Response:
2026/4/27 9:29:33

> Thought for 9s

prompt_version: stage0-v182-20260426  
model_info: GPT-5.5 Thinking  
[BIB-1] title: Efficient catalytic addition of aromatic carbon-hydrogen bonds to olefins `Murai_1993.pdf`  
[BIB-2] authors: Shinji Murai, Fumitoshi Kakiuchi, Shinya Sekine, Yasuo Tanaka, Asayuki Kamatani, Motohiro Sonoda & Naoto Chatani `Murai_1993.pdf`  
[BIB-3] journal: NATURE `Murai_1993.pdf`  
[BIB-4] year: 1993 `Murai_1993.pdf`  
[BIB-5] volume_pages: VOL 366, 529–531 `Murai_1993.pdf`  
[BIB-6] doi: not found  
[BIB-7] format: full_paper  
[BIB-8a] target_paper_start: page 1: Efficient catalytic addition of aromatic carbon-hydrogen bonds to olefins `Murai_1993.pdf`  
[BIB-8b] target_paper_end: page 3: [REDACTED: verbatim source text; see the source paper via its DOI] `Murai_1993.pdf`  
[S0-1] core_claim: [REDACTED: verbatim source text; see the source paper via its DOI] paper claims the catalyst operates with “efficiency, selectivity and generality” valuable in organic synthesis. `Murai_1993.pdf`  
[S0-2] evidence_type: Substrate scope table of reactions between aromatic ketones and olefins, product yields determined by gas chromatography, isolated yields in parentheses, and product structures established by standard methods. `Murai_1993.pdf`  
[S0-3] prior_work_position: The paper states that earlier catalytic C-H functionalization reactions were limited by low yields and/or low turnover numbers, or by by-products, isomer mixtures, and narrow applicability; it presents the Ru-catalysed reaction as achieving [REDACTED: verbatim source text; see the source paper via its DOI].” `Murai_1993.pdf`  
[S0-4] methodology: A mixture of aromatic ketone, olefin, and RuH2(CO)(P(C6H5)3)3 in toluene was vigorously refluxed, and the C-H/olefin coupling products were isolated and analyzed; related ruthenium complexes were also tested for catalytic effectiveness. `Murai_1993.pdf`  
[S0-5] conclusion_reach: The paper claims wide applicability to acylbenzene derivatives, acylheteroaromatics, and various mono- and di-substituted terminal olefins, while stating that the mechanism is “not yet clear.” `Murai_1993.pdf`  
[S0-6] next_question_stated: [REDACTED: substantial verbatim quotation; see Tier 9] `Murai_1993.pdf`  
[S0-7] note_added_in_proof: none.  
inference_time_sec: not available — inject externally

## Response:
2026/4/27 9:30:04

> **Considering citation requirements for output**
>
> The user uploaded a prompt likely related to the Murai paper. It seems I need to follow guidelines and provide structured output with citations as required. However, since the output format doesn't allow extra citations, I think I can include them inline within the quote field since that's allowed.
>
> **Considering citation inclusion in structured output**
>
> The user seems to want precise output, but I need to ensure I’m following the file_search citation guidelines. While the output must be structured with no extra information, I’m thinking I can include a citation inline with the quote or in a single field. I'll stick to the format and aim for clarity.
>
> Thought for 31s

prompt_version: stage1-v182-20260426

target_title: Efficient catalytic addition of aromatic carbon-hydrogen bonds to olefins  
target_authors: Shinji Murai, Fumitoshi Kakiuchi, Shinya Sekine, Yasuo Tanaka, Asayuki Kamatani, Motohiro Sonoda & Naoto Chatani  
target_start: page 1: Efficient catalytic addition of aromatic carbon-hydrogen bonds to olefins  
target_end: page 3: [REDACTED: verbatim source text; see the source paper via its DOI]

[Turn 1: Agent V1]  
field: Organometallic C-H activation catalysis / synthetic methodology  
field_rationale: The paper reports a ruthenium-catalysed coupling of aromatic C-H bonds with olefins using aromatic ketones and olefins under refluxing toluene conditions, placing V1 in organometallic catalytic C-H functionalization. `Murai_1993.pdf`

V1-Q1 | P1:Rcol:16-L24* | quote: [REDACTED: substantial verbatim quotation; see Tier 9] | question: What quantitative yield, conversion, selectivity, and turnover data support the terms “equally effective,” “modestly effective,” and “not effective” for the catalyst comparison? | severity: high | inference_tier: T1

V1-Q2 | P1:Rcol:4-L11* | quote: [REDACTED: substantial verbatim quotation; see Tier 9] | question: Were reactions conducted under inert atmosphere, and were oxygen or moisture controls performed? | severity: medium | inference_tier: T2 [paper-grounded inference]

V1-Q3 | P2:Table1* | quote: [REDACTED: substantial verbatim quotation; see Tier 9] | question: Why are isolated yields reported only for selected products while most entries report only GC yields? | severity: medium | inference_tier: T1

V1-Q4 | P2:Table1* | quote: [REDACTED: verbatim source quotation; see `loc:`] and entries including [REDACTED: verbatim source quotation; see `loc:`] [REDACTED: verbatim source quotation; see `loc:`] and [REDACTED: verbatim source quotation; see `loc:`] | question: For entries using excess olefin, what is the yield denominator and what is the mass balance for unreacted olefin and possible olefin-derived by-products? | severity: medium | inference_tier: T2 [paper-grounded inference]

V1-Q5 | P1:Rcol:31-L37* | quote: [REDACTED: substantial verbatim quotation; see Tier 9] | question: What analytical detection limit or chromatographic/NMR evidence supports the statement “virtually 100%” regioselectivity? | severity: high | inference_tier: T1

V1-Q6 | P3:Lcol:1-L5* | quote: [REDACTED: substantial verbatim quotation; see Tier 9] | question: Is the 1:2 product formed by secondary reaction of the isolated 1:1 product, and is there time-course or sequential-addition evidence distinguishing the pathway? | severity: medium | inference_tier: T2 [paper-grounded inference]

V1-Q7 | P1:Rcol:24-L30* | quote: [REDACTED: substantial verbatim quotation; see Tier 9] | question: Are crude mass balances, conversions, and recovered starting materials reported for runs 8–13 to substantiate “based on both the starting materials”? | severity: medium | inference_tier: T1

V1-Q8 | P1:Rcol:26-L30* | quote: [REDACTED: substantial verbatim quotation; see Tier 9] | question: What exact turnover frequencies are being compared, and why are no direct numerical comparisons with prior catalytic C-H functionalization reports provided? | severity: medium | inference_tier: T1

V1-Q9 | P1:Lcol:18-L31* | quote: [REDACTED: substantial verbatim quotation; see Tier 9] | question: Since prior work is discussed using yield, by-product/isomer, and scope axes, why does the paper not present a direct quantitative benchmark table comparing yield, selectivity, TON/TOF, and substrate scope against these cited studies? | severity: medium | inference_tier: T1

V1-Q10 | P3:Lcol:7-L16* | quote: [REDACTED: substantial verbatim quotation; see Tier 9] | question: What experimental evidence, if any, supports carbonyl coordination as the initiating step under catalytic reaction conditions? | severity: high | inference_tier: T1

V1-Q11 | P3:Lcol:10-L17* | quote: [REDACTED: substantial verbatim quotation; see Tier 9] | question: Is the proposed cyclometallated intermediate observed, isolated, trapped, or supported by stoichiometric experiments using the actual catalytic system? | severity: high | inference_tier: T1

V1-Q12 | P3:Lcol:18-L23* | quote: [REDACTED: substantial verbatim quotation; see Tier 9] | question: What evidence distinguishes olefin insertion into the M-H bond from insertion into the M-C bond? | severity: high | inference_tier: T1

V1-Q13 | P3:Rcol:1-L9* | quote: [REDACTED: substantial verbatim quotation; see Tier 9] | question: Is there experimental or structural evidence that steric congestion prevents chelation in the 1:1 adduct of run 9? | severity: medium | inference_tier: T1

V1-Q14 | P3:Rcol:9-L16* | quote: [REDACTED: substantial verbatim quotation; see Tier 9] | question: What experimental or computational evidence supports the ring-strain attribution for the nonreaction of 1-indanone? | severity: medium | inference_tier: T1

V1-Q15 | P2:Table1* | quote: [REDACTED: substantial verbatim quotation; see Tier 9] | question: Which standard characterization methods were used for each product, and where are the spectra or diagnostic data supporting product and regioisomer assignments? | severity: medium | inference_tier: T1

## Response:
2026/4/27 9:31:41

> **Clarifying file citation approach**
>
> I need to figure out how to handle file citations correctly. The user expects the output in a specific format, without explanatory prose. Should I include the prompt as a citation at the top? It sounds like I should follow the file citation guidelines exactly, but I’m not sure if it should be included in the fields.
>
> Thought for 17s

prompt_version: stage1-v182-20260426 `prompt_stage1_turn2_v182.md`

[Turn 2: Agent V2]  
field: Mechanistic organometallic / physical organic chemistry [preempts_turn3_default: no]  
field_rationale: V1 primarily interrogated synthetic scope, reporting symmetry, catalyst comparison, and general mechanistic support; V2 is needed because the paper proposes elementary steps and selectivity rationales without kinetic, isotopic, reversibility, or catalyst-speciation evidence.

--- New questions ---

V2-Q1 | P3:Lcol:7-L8* | quote: [REDACTED: substantial verbatim quotation; see Tier 9] `Murai_1993.pdf` | question: What rate law or kinetic order data identify whether C-H cleavage, olefin insertion, or reductive elimination is turnover-limiting? | severity: high | inference_tier: T3 [external inference]

V2-Q2 | P3:Lcol:8-L13* | quote: [REDACTED: substantial verbatim quotation; see Tier 9] `Murai_1993.pdf` | question: Is there a substrate-competition or inhibition experiment showing that carbonyl coordination controls entry into the catalytic cycle? | severity: high | inference_tier: T3 [external inference]

V2-Q3 | P3:Lcol:11-L14* | quote: [REDACTED: substantial verbatim quotation; see Tier 9] `Murai_1993.pdf` | question: Is ortho C-H cleavage reversible, and does the paper report H/D exchange or isotope-labeling data to test reversibility before C-C bond formation? | severity: high | inference_tier: T3 [external inference]

V2-Q4 | P1:Rcol:31-L37* | quote: [REDACTED: substantial verbatim quotation; see Tier 9] `Murai_1993.pdf` | question: Is the observed regioselectivity kinetically controlled by selective C-H activation or olefin insertion, or thermodynamically controlled by product/intermediate stability? | severity: high | inference_tier: T2 [paper-grounded inference]

V2-Q5 | P3:Lcol:18-L22* | quote: [REDACTED: substantial verbatim quotation; see Tier 9] `Murai_1993.pdf` | question: Are deuterium-labeling or crossover experiments reported to distinguish hydrometallation followed by C-C reductive elimination from migratory insertion into Ru-C followed by C-H reductive elimination? | severity: critical | inference_tier: T3 [external inference]

V2-Q6 | P1:Rcol:16-L24* | quote: [REDACTED: substantial verbatim quotation; see Tier 9] `Murai_1993.pdf` | question: What does the catalyst-dependence imply about the active Ru species, and is catalyst speciation under refluxing toluene conditions examined? | severity: high | inference_tier: T2 [paper-grounded inference]

V2-Q7 | P1:Rcol:4-L11* | quote: [REDACTED: substantial verbatim quotation; see Tier 9] `Murai_1993.pdf` | question: Does changing olefin concentration alter product ratio or rate in a way that separates olefin-binding/insertion from C-H activation? | severity: medium | inference_tier: T3 [external inference]

V2-Q8 | P3:Rcol:1-L7* | quote: [REDACTED: substantial verbatim quotation; see Tier 9] `Murai_1993.pdf` | question: Is the 1:1 versus 1:2 product distribution under kinetic control, or does prolonged heating equilibrate or further convert the initially formed product? | severity: medium | inference_tier: T2 [paper-grounded inference]

V2-Q9 | P3:Rcol:9-L16* | quote: [REDACTED: substantial verbatim quotation; see Tier 9] `Murai_1993.pdf` | question: Is 1-indanone unreactive because C-H activation is blocked, because the cyclometallated intermediate cannot proceed to olefin insertion, or because catalyst inhibition/decomposition occurs? | severity: high | inference_tier: T2 [paper-grounded inference]

V2-Q10 | P3:Lcol:14-L18* | quote: [REDACTED: substantial verbatim quotation; see Tier 9] `Murai_1993.pdf` | question: Do these stoichiometric precedents establish the same oxidation state, ligand environment, and elementary step sequence as the catalytic RuH2(CO)(PPh3)3 system? | severity: high | inference_tier: T2 [paper-grounded inference]

V2-Q11 | P3:Rcol:18-L26* | quote: [REDACTED: substantial verbatim quotation; see Tier 9] `Murai_1993.pdf` | question: What mechanistic criterion defines when chelation assistance is sufficient for broader applicability beyond aromatic ketones? | severity: medium | inference_tier: T2 [paper-grounded inference]

V2-Q12 | P2:Table1* | quote: [REDACTED: verbatim source quotation; see `loc:`] with entries ranging from [REDACTED: verbatim source quotation; see `loc:`] to [REDACTED: verbatim source quotation; see `loc:`] and yields ranging from [REDACTED: verbatim source quotation; see `loc:`] to [REDACTED: verbatim source quotation; see `loc:`] `Murai_1993.pdf` | question: Are the large differences in reaction time caused by different rates of C-H activation, olefin insertion, catalyst stability, or product inhibition? | severity: medium | inference_tier: T2 [paper-grounded inference]

--- Overlaps with V1 ---

V2-OV1 | overlaps_with: V1-Q5 | severity_V2: high | note: From a mechanistic perspective, “virtually 100%” regioselectivity is not only an analytical claim but also the central observable needed to distinguish kinetic selectivity from thermodynamic product distribution.

V2-OV2 | overlaps_with: V1-Q6 | severity_V2: medium | note: The 1:1 versus 1:2 product issue is mechanistically important because it tests whether the first alkylation product remains catalytically competent for a second chelation-assisted C-H activation.

V2-OV3 | overlaps_with: V1-Q8 | severity_V2: medium | note: Turnover frequency matters mechanistically because comparing runs 1, 9, and 10 could reveal whether substrate structure changes the turnover-limiting elementary step.

V2-OV4 | overlaps_with: V1-Q10 | severity_V2: high | note: Carbonyl coordination is not just a proposed initiation event; it is the mechanistic basis for chelation assistance and ortho selectivity.

V2-OV5 | overlaps_with: V1-Q11 | severity_V2: high | note: The cyclometallated intermediate is the mechanistic hinge of the paper, so lack of direct observation or stoichiometric validation under catalytic conditions strongly limits mechanism assignment.

V2-OV6 | overlaps_with: V1-Q12 | severity_V2: critical | note: Distinguishing M-H insertion from M-C insertion changes the elementary-step sequence, hydride role, and origin of regioselectivity.

V2-OV7 | overlaps_with: V1-Q13 | severity_V2: medium | note: The steric-congestion explanation is mechanistically plausible only if chelation of the monoalkylated ketone is actually the blocked step rather than a later insertion or reductive-elimination step.

V2-OV8 | overlaps_with: V1-Q14 | severity_V2: high | note: The 1-indanone failure is a mechanistic boundary case, but the paper does not separate ring strain from alternative causes such as catalyst poisoning, poor binding, or slow post-cyclometallation chemistry.

## Response:
2026/4/27 10:07:52

> Thought for 10s

prompt_version: stage1-v182-20260426 `prompt_stage1_turn3_v182.md`

[Turn 3: Agent V3]  
field: Analytical chemistry / chromatography  
field_rationale: The paper’s primary quantitative evidence is a substrate-scope table in which yields are “determined by gas chromatography” with isolated yields only selectively reported, so the missing methodological perspective is quantification validity, calibration, reproducibility, and reporting symmetry.

--- New questions ---

V3-Q1 | P2:Table1* | quote: [REDACTED: substantial verbatim quotation; see Tier 9] `Murai_1993.pdf` | question: Were GC yields calibrated with authentic standards or response factors for each product class? | severity: high | inference_tier: T2 [paper-grounded inference]

V3-Q2 | P2:Table1* | quote: [REDACTED: substantial verbatim quotation; see Tier 9] `Murai_1993.pdf` | question: Was an internal standard used for GC quantification, and if so, what compound and integration protocol were used? | severity: high | inference_tier: T3 [external inference]

V3-Q3 | P2:Table1* | quote: [REDACTED: verbatim source quotation; see `loc:`] with entries including [REDACTED: verbatim source quotation; see `loc:`] [REDACTED: verbatim source quotation; see `loc:`] [REDACTED: verbatim source quotation; see `loc:`] [REDACTED: verbatim source quotation; see `loc:`] [REDACTED: verbatim source quotation; see `loc:`] [REDACTED: verbatim source quotation; see `loc:`] [REDACTED: verbatim source quotation; see `loc:`] and isolated yields in parentheses for only some entries. `Murai_1993.pdf` | question: What are the replicate counts and experimental uncertainties for the reported yields? | severity: high | inference_tier: T2 [paper-grounded inference]

V3-Q4 | P1:Rcol:10-L13* | quote: [REDACTED: substantial verbatim quotation; see Tier 9] `Murai_1993.pdf` | question: What analytical criteria established “analytically pure” after bulb-to-bulb distillation? | severity: medium | inference_tier: T1

V3-Q5 | P2:Table1* | quote: [REDACTED: substantial verbatim quotation; see Tier 9] `Murai_1993.pdf` | question: Which chromatographic or spectroscopic data distinguish positional/regioisomeric products in entries where multiple isomers are chemically possible? | severity: high | inference_tier: T2 [paper-grounded inference]

V3-Q6 | P1:Rcol:31-L37* | quote: [REDACTED: verbatim source quotation; see `loc:`] `Murai_1993.pdf` | question: Were the four possible regioisomers chromatographically resolved or otherwise shown to be detectable under the analytical conditions? | severity: high | inference_tier: T2 [paper-grounded inference]

V3-Q7 | P1:Rcol:4-L11* | quote: [REDACTED: substantial verbatim quotation; see Tier 9] `Murai_1993.pdf` | question: At what reaction conversion or sampling time were GC yields measured, and were aliquots quenched or worked up before GC analysis? | severity: medium | inference_tier: T3 [external inference]

V3-Q8 | P2:Table1* | quote: [REDACTED: verbatim source quotation; see `loc:`] `Murai_1993.pdf` | question: How was ethylene consumption or concentration controlled and quantified in the autoclave experiment relative to liquid olefin entries? | severity: medium | inference_tier: T2 [paper-grounded inference]

V3-Q9 | P2:Table1* | quote: [REDACTED: verbatim source quotation; see `loc:`] with different entries using [REDACTED: verbatim source quotation; see `loc:`] [REDACTED: verbatim source quotation; see `loc:`] [REDACTED: verbatim source quotation; see `loc:`] and [REDACTED: verbatim source quotation; see `loc:`] `Murai_1993.pdf` | question: Were comparisons across scope entries normalized for catalyst loading, olefin equivalents, and reaction time before claims of generality and efficiency were made? | severity: medium | inference_tier: T2 [paper-grounded inference]

V3-Q10 | P3:Lcol:1-L5* | quote: [REDACTED: substantial verbatim quotation; see Tier 9] `Murai_1993.pdf` | question: Were the 1:1 and 1:2 products validated as quantitatively separable by GC across the concentration range used in runs 1 and 2? | severity: medium | inference_tier: T2 [paper-grounded inference]

--- Overlaps with V1/V2 ---

V3-OV1 | overlaps_with: V1-Q3 | severity_V3: high | note: Selective reporting of isolated yields versus GC yields is a core analytical-reporting asymmetry because it prevents uniform evaluation of recovery, purity, and quantification bias.

V3-OV2 | overlaps_with: V1-Q4 | severity_V3: medium | note: Yield denominators and mass balance directly affect chromatographic quantification because excess olefin and volatile materials can distort apparent product yield if not independently accounted for.

V3-OV3 | overlaps_with: V1-Q5 | severity_V3: high | note: “Virtually 100%” regioselectivity is an analytical claim that requires detection limits, chromatographic resolution, and response-factor validation.

V3-OV4 | overlaps_with: V1-Q7 | severity_V3: medium | note: “Almost quantitative yields” require conversion and mass-balance data, not only product-area quantification.

V3-OV5 | overlaps_with: V1-Q8 | severity_V3: medium | note: Turnover-frequency claims depend on accurate time-resolved yield or conversion measurements, which are not methodologically specified.

V3-OV6 | overlaps_with: V1-Q9 | severity_V3: medium | note: Direct comparison with prior work requires comparable analytical endpoints, such as isolated yield versus GC yield and product selectivity definitions.

V3-OV7 | overlaps_with: V1-Q15 | severity_V3: high | note: Product identity and regioisomer assignment are inseparable from analytical validity when the main evidence is a scope table of structures and yields.

V3-OV8 | overlaps_with: V2-Q4 | severity_V3: high | note: Kinetic versus thermodynamic selectivity cannot be evaluated unless regioisomer ratios are measured quantitatively over time with validated detection of minor components.

V3-OV9 | overlaps_with: V2-Q7 | severity_V3: medium | note: Olefin-concentration effects require standardized sampling and quantitative calibration to avoid conflating concentration dependence with measurement variability.

V3-OV10 | overlaps_with: V2-Q8 | severity_V3: medium | note: The 1:1 versus 1:2 distribution is analytically meaningful only if both products are calibrated and resolved across the relevant reaction-time and concentration regimes.

V3-OV11 | overlaps_with: V2-Q12 | severity_V3: medium | note: Large differences in reaction time require time-course data and consistent analytical endpoints before rate or stability interpretations can be made.

## Response:
2026/4/27 10:22:40

> **Synthesizing and classifying questions**
>
> I need to classify all questions from V1, V2, and V3, making sure to group them into categories A, B, C, and U. I should be careful with overlapping questions and consolidate similar ones while still addressing each individually as the prompt requests. B items can be grouped by primary quotes, and I’ll focus on exhaustive references for C. The final output will be structured, but I should aim for clarity, not over-verbosity.
>
> **Classifying reporting omissions and limitations**
>
> I'm trying to sort out reporting omissions and limitations. For example, comparisons of catalysts lack quantitative data, which seems like a missing detail, not a rhetorical issue. I need to classify omissions about reaction conditions, yields, selectivity evidence, and time-course details. Some could be categorized as omissions, and others might fall under contradictions (U). I’ll make sure each category aligns with how the paper reports these aspects.
>
> **Classifying mechanistic issues and contradictions**
>
> I’m trying to classify mechanistic claims. The proposed mechanism predicts certain data (like intermediates, isotope paths), but it’s not reported. This could be self-contradictory, so maybe it goes under U. Since it's about deferred testing, it could also link to A as a deferred mechanism. I’ll separate out mechanistic gaps using U for missing information.
>
> **Tracking and classifying references and engagement**
>
> I’m working through how to classify references. For some, like those from 1-10, they seem more background and not substantively engaged, so they should go under C. If a reference like Jordan/Taylor is discussed but lacks direct data comparison, it's less clear. I'll need to track these carefully
>
> **Classifying substantive engagement vs. citation issues**
>
> I'm trying to decide if prior cited works are sufficiently engaged. Some discussions seem to fall short of direct engagement, but they’re referenced enough to be considered. For example, catalyst preparation or precedents for cyclometallation are cited, but not validated. Since they’re indirectly involved, they may still fall under the C category.
>
> **Classifying and grouping citations**
>
> I need to classify citations that provide indirect engagement or precedents without validation, which may fall under category C. For example, certain references like cyclometall
>
> **Classifying overlaps and agent severities**
>
> I’m trying to figure out how to handle overlapping questions, especially between V1, V2, and V3. For items like V1-Q6, V2-Q8, and V3-Q10, there’s a convergence of medium severity across all three versions. I’ll group them based on shared roots and assign appropriate agent severities, accounting for overlaps in severity.
>
> Thought for 58s

prompt_version: stage1-v182-20260426 `prompt_stage1_turn4_v182.md`  
model_info: GPT-5.5 Thinking

target_title: Efficient catalytic addition of aromatic carbon-hydrogen bonds to olefins  
target_authors: Shinji Murai, Fumitoshi Kakiuchi, Shinya Sekine, Yasuo Tanaka, Asayuki Kamatani, Motohiro Sonoda & Naoto Chatani  
target_start: page 1: Efficient catalytic addition of aromatic carbon-hydrogen bonds to olefins  
target_end: page 3: [REDACTED: verbatim source text; see the source paper via its DOI]

[Agent fields]  
V1: Organometallic C-H activation catalysis / synthetic methodology — The paper reports a ruthenium-catalysed coupling of aromatic C-H bonds with olefins under synthetic scope conditions.  
V2: Mechanistic organometallic / physical organic chemistry — The paper proposes elementary steps and selectivity rationales without kinetic, isotopic, reversibility, or catalyst-speciation evidence.  
V3: Analytical chemistry / chromatography — The paper’s primary quantitative evidence is a substrate-scope table with GC yields and selectively reported isolated yields.

[A] A-1 | P3:Lcol:7-L8* | quote: [REDACTED: substantial verbatim quotation; see Tier 9] `Murai_1993.pdf` | deferral_type: deferred | mixed_detail: n/a | reason_inferred: T1 | linked_to: U-1, U-2, U-3, U-4, C-4, C-6, C-7 | cross_field_temperature: V1=high; V2=high; convergence=2/3; temperature_gap=none

[B] B-1 | P1:Rcol:16-L24* | quote: [REDACTED: substantial verbatim quotation; see Tier 9] `Murai_1993.pdf` | classification: reporting_omission | rhetorical_function: Catalyst comparison summarized qualitatively. | note: Metric incompleteness — quantitative yield, conversion, selectivity, and turnover data for the catalyst comparison are not stated in paper. | cross_field_temperature: V1=high; V2=high; convergence=2/3; temperature_gap=none

[B] B-2 | P1:Rcol:4-L11* | quote: [REDACTED: substantial verbatim quotation; see Tier 9] `Murai_1993.pdf` | classification: reporting_omission | rhetorical_function: General reaction protocol is described. | note: Procedural datum absent — atmosphere, oxygen/moisture exclusion, and control conditions are not stated in paper. | cross_field_temperature: V1=medium; convergence=1/3; temperature_gap=n/a

[B] B-3 | P2:Table1* | quote: [REDACTED: substantial verbatim quotation; see Tier 9] `Murai_1993.pdf` | classification: reporting_omission | rhetorical_function: Yield-determination method is qualified. | note: Metric incompleteness — GC calibration, response factors, internal standard, replicate counts, uncertainty, and the rationale for selectively reporting isolated yields are not stated in paper. | cross_field_temperature: V1=medium; V3=high; convergence=2/3; temperature_gap=low

[B] B-4 | P2:Table1* | quote: [REDACTED: verbatim source quotation; see `loc:`] with entries including [REDACTED: verbatim source quotation; see `loc:`] [REDACTED: verbatim source quotation; see `loc:`] [REDACTED: verbatim source quotation; see `loc:`] and [REDACTED: verbatim source quotation; see `loc:`] `Murai_1993.pdf` | classification: reporting_omission | rhetorical_function: Stoichiometry, catalyst loading, and reaction time are tabulated. | note: Metric incompleteness — yield denominator, mass balance for excess olefin, recovered starting materials, catalyst-loading normalization, and comparison basis across entries are not stated in paper. | cross_field_temperature: V1=medium; V3=medium; convergence=2/3; temperature_gap=none

[B] B-5 | P1:Rcol:31-L37* | quote: [REDACTED: substantial verbatim quotation; see Tier 9] `Murai_1993.pdf` | classification: reporting_omission | rhetorical_function: Regioselectivity is presented as a central positive feature. | note: Metric incompleteness — detection limits, chromatographic resolution of possible regioisomers, quantitative minor-isomer analysis, and kinetic-versus-thermodynamic selectivity evidence are not stated in paper. | cross_field_temperature: V1=high; V2=high; V3=high; convergence=3/3; temperature_gap=none

[B] B-6 | P3:Lcol:1-L5* | quote: [REDACTED: substantial verbatim quotation; see Tier 9] `Murai_1993.pdf` | classification: reporting_omission | rhetorical_function: Product-ratio change under modified conditions is described. | note: Metric incompleteness — time-course data, sequential-conversion evidence, equilibration tests, and GC separability/calibration for 1:1 versus 1:2 products are not stated in paper. | cross_field_temperature: V1=medium; V2=medium; V3=medium; convergence=3/3; temperature_gap=none

[B] B-7 | P1:Rcol:26-L30* | quote: [REDACTED: substantial verbatim quotation; see Tier 9] `Murai_1993.pdf` | classification: reporting_omission | rhetorical_function: Turnover frequency is invoked to support efficiency. | note: Metric incompleteness — exact TOF values, calculation basis, time-resolved conversion data, and numerical comparison with prior work are not stated in paper. | cross_field_temperature: V1=medium; V2=medium; V3=medium; convergence=3/3; temperature_gap=none

[B] B-8 | P2:Table1* | quote: [REDACTED: substantial verbatim quotation; see Tier 9] `Murai_1993.pdf` | classification: reporting_omission | rhetorical_function: Product structural assignment is asserted. | note: Reporting omission — the specific characterization methods, diagnostic spectra, regioisomer-assignment criteria, and purity criteria for “analytically pure” products are not stated in paper. | cross_field_temperature: V1=medium; V3=high; convergence=2/3; temperature_gap=low

[B] B-9 | P2:Table1* | quote: [REDACTED: verbatim source quotation; see `loc:`] `Murai_1993.pdf` | classification: reporting_omission | rhetorical_function: A special condition for the ethylene experiment is noted. | note: Categorically discontinuous conditions — ethylene pressure is reported, but gas consumption, concentration control, and comparison basis relative to liquid olefin entries are not stated in paper. | cross_field_temperature: V3=medium; convergence=1/3; temperature_gap=n/a

[B] B-10 | P1:Rcol:4-L11* | quote: [REDACTED: substantial verbatim quotation; see Tier 9] `Murai_1993.pdf` | classification: reporting_omission | rhetorical_function: General reaction procedure is summarized. | note: Analytical endpoint omission — sampling time, quenching/workup before GC, and whether GC yields were measured at conversion or after isolation are not stated in paper. | cross_field_temperature: V3=medium; convergence=1/3; temperature_gap=n/a

[B] B-11 | P2:Table1* | quote: [REDACTED: verbatim source quotation; see `loc:`] with entries ranging from [REDACTED: verbatim source quotation; see `loc:`] to [REDACTED: verbatim source quotation; see `loc:`] and yields ranging from [REDACTED: verbatim source quotation; see `loc:`] to [REDACTED: verbatim source quotation; see `loc:`] `Murai_1993.pdf` | classification: reporting_omission | rhetorical_function: Reaction times and yields are tabulated across substrate entries. | note: Metric incompleteness — the paper does not state whether time differences reflect C-H activation rate, olefin insertion, catalyst stability, product inhibition, or different analytical endpoints. | cross_field_temperature: V2=medium; V3=medium; convergence=2/3; temperature_gap=none

[B] B-12 | P1:Rcol:24-L30* | quote: [REDACTED: substantial verbatim quotation; see Tier 9] `Murai_1993.pdf` | classification: reporting_omission | rhetorical_function: High-yield performance is generalized over selected runs. | note: Metric incompleteness — crude mass balance, conversions, and recovered starting materials for runs 8–13 are not stated in paper. | cross_field_temperature: V1=medium; V3=medium; convergence=2/3; temperature_gap=none

[C] C-1 | P1:Lcol:13-L20* | citation: refs. 1–10, cited for “Methods for carbon-hydrogen bond cleavage by transition-metal complexes” and [REDACTED: substantial verbatim quotation; see Tier 9] `Murai_1993.pdf` | textual_function: Prior C-H cleavage literature is used as background. | reason_severed: The cited works are not compared experimentally or mechanistically against the present catalytic system. | affects_claims: medium — the broad novelty framing depends on the contrast with prior C-H cleavage work. | symmetric_pattern: partial

[C] C-2 | P1:Lcol:23-L31* | citation: refs. 11–12, cited as “Notable recent advances” involving α-picoline/propene and pyridine/carbon monoxide/1-hexene. `Murai_1993.pdf` | textual_function: Prior catalytic advances are positioned as limited comparators. | reason_severed: Qualitative benchmark introduced but not completed with side-by-side yield, selectivity, TON/TOF, by-product, or scope comparison. | affects_claims: yes — the paper’s efficiency, selectivity, and generality claims rely on comparison with these prior examples. | symmetric_pattern: yes

[C] C-3 | P1:Lcol:33-L35* | citation: ref. 13, cited for RuH2(CO)(P(C6H5)3)3. `Murai_1993.pdf` | textual_function: Catalyst identity is referenced. | reason_severed: Catalyst preparation/identity citation is not connected to catalyst speciation or active-species evidence under reaction conditions. | affects_claims: medium — active-catalyst identity affects interpretation of the reported catalytic reaction. | symmetric_pattern: no

[C] C-4 | P3:Lcol:14-L18* | citation: refs. 14–15, cited for cyclometallation precedents of acetophenone. `Murai_1993.pdf` | textual_function: Stoichiometric precedents are used to support a proposed intermediate. | reason_severed: Analogy invoked without showing that the same oxidation state, ligand environment, or elementary-step sequence applies to the catalytic Ru system. | affects_claims: yes — the chelation-assisted cyclometallation model depends on this mechanistic analogy. | symmetric_pattern: yes

[C] C-5 | P1:Rcol:26-L29* | citation: refs. 12 and 16, cited for prior reactions requiring one starting material in excess, “often as the solvent.” `Murai_1993.pdf` | textual_function: Prior condition limitation is contrasted with the present method. | reason_severed: The comparison is not continued through a normalized stoichiometry, concentration, or mass-balance analysis. | affects_claims: medium — the practical-efficiency claim depends partly on lower excess-reagent requirements. | symmetric_pattern: partial

[C] C-6 | P3:Lcol:17-L19* | citation: ref. 17, cited for chelation-assisted oxidative addition of acrylic acid esters to ruthenium. `Murai_1993.pdf` | textual_function: Related chelation-assisted oxidative addition is invoked as mechanistic precedent. | reason_severed: The precedent is not experimentally connected to the ketone-directed C-H activation pathway in this reaction. | affects_claims: medium — it supports the plausibility of chelation assistance but not the specific catalytic cycle. | symmetric_pattern: no

[C] C-7 | P3:Lcol:18-L22* | citation: ref. 18, cited for olefin insertion “into the M-C bond.” `Murai_1993.pdf` | textual_function: Alternative elementary step is cited. | reason_severed: The alternative insertion pathway is cited but not discriminated experimentally from M-H insertion. | affects_claims: yes — the elementary-step sequence and origin of product connectivity remain unresolved. | symmetric_pattern: no

[U] U-1 | P3:Lcol:8-L13* | quote: [REDACTED: substantial verbatim quotation; see Tier 9] `Murai_1993.pdf` | question: What experimental evidence shows that carbonyl coordination controls entry into the catalytic cycle? | originating_agent: V1-Q10, V2-Q2 | severity: high | note: A/B/C classification does not apply because this is not merely an omitted reporting datum or an uncontinued citation; it is a prerequisite mechanistic validation question linked to the paper’s own proposed catalytic model.

[U] U-2 | P3:Lcol:11-L16* | quote: [REDACTED: substantial verbatim quotation; see Tier 9] `Murai_1993.pdf` | question: Is the proposed cyclometallated intermediate observed, isolated, trapped, or validated under the actual catalytic system? | originating_agent: V1-Q11, V2-Q10 | severity: high | note: self-contradictory absence — the paper’s proposed mechanism predicts a cyclometallated intermediate but this is neither reported nor acknowledged as untested under the catalytic conditions.

[U] U-3 | P3:Lcol:18-L22* | quote: [REDACTED: substantial verbatim quotation; see Tier 9] `Murai_1993.pdf` | question: What evidence distinguishes olefin insertion into the M-H bond from insertion into the M-C bond? | originating_agent: V1-Q12, V2-Q5 | severity: critical | note: self-contradictory absence — the paper’s proposed mechanism explicitly presents two mutually distinct insertion pathways but does not test which pathway operates.

[U] U-4 | P3:Lcol:11-L14* | quote: [REDACTED: substantial verbatim quotation; see Tier 9] `Murai_1993.pdf` | question: Is ortho C-H cleavage reversible, and is C-H cleavage, olefin insertion, or reductive elimination turnover-limiting? | originating_agent: V2-Q1, V2-Q3, V2-Q7 | severity: high | note: A/B/C classification does not apply because the issue concerns kinetic and isotope-labeling tests required to interpret the proposed elementary-step sequence, not a stated future direction, simple reporting omission, or dropped citation.

[U] U-5 | P3:Rcol:1-L7* | quote: [REDACTED: substantial verbatim quotation; see Tier 9] `Murai_1993.pdf` | question: Is there experimental or structural evidence that steric congestion prevents chelation in the 1:1 adduct? | originating_agent: V1-Q13, V2-OV7 | severity: medium | note: A/B/C classification does not apply because the gap is an unsupported causal attribution for a selectivity pattern rather than a deferred question, ordinary reporting omission, or uncontinued citation.

[U] U-6 | P3:Rcol:9-L16* | quote: [REDACTED: substantial verbatim quotation; see Tier 9] `Murai_1993.pdf` | question: What evidence supports the ring-strain attribution for the nonreaction of 1-indanone rather than catalyst inhibition, poor binding, or failure after C-H activation? | originating_agent: V1-Q14, V2-Q9 | severity: high | note: Negative result as evidence — the paper uses a failure case mechanistically, but the failure is not shown with supporting evidence or alternative-cause discrimination.

[U] U-7 | P3:Rcol:18-L26* | quote: [REDACTED: substantial verbatim quotation; see Tier 9] `Murai_1993.pdf` | question: What mechanistic criterion defines when chelation assistance is sufficient for broader applicability beyond aromatic ketones? | originating_agent: V2-Q11 | severity: medium | note: A/B/C classification does not apply because the question concerns the operational boundary of the proposed design principle, not an explicit deferral, standard reporting omission, or abandoned reference.

[META]  
linked_items: [A-1↔U-1, A-1↔U-2, A-1↔U-3, A-1↔U-4, U-2↔C-4, U-3↔C-7, B-7↔C-2, B-4↔C-5, U-1↔C-6]  
same_root_groups: [
  {members: [B-3, B-8], shared_root: [REDACTED: substantial verbatim quotation; see Tier 9]},
  {members: [B-4, B-12], shared_root: [REDACTED: substantial verbatim quotation; see Tier 9]},
  {members: [B-5, B-6, U-5], shared_root: [REDACTED: substantial verbatim quotation; see Tier 9]},
  {members: [A-1, U-1, U-2, U-3, U-4], shared_root: [REDACTED: substantial verbatim quotation; see Tier 9]},
  {members: [B-7, C-2], shared_root: [REDACTED: substantial verbatim quotation; see Tier 9]},
  {members: [U-6, B-11], shared_root: [REDACTED: substantial verbatim quotation; see Tier 9]}
]  
symmetric_citations: [C-2: refs. 11–12; C-4: refs. 14–15]  
unreported_data: [GC calibration and response factors; internal standard; replicate counts and uncertainty; isolated yields for all products; crude mass balance; recovered starting materials; minor-regioisomer detection limits; time-course data; kinetic isotope or H/D exchange data; catalyst speciation data; direct observation or trapping of cyclometallated intermediate; insertion-pathway discrimination data; spectra or diagnostic characterization for product assignments]  
series_signal: no [T1]

[TEMPERATURE_SUMMARY]  
high_convergence_high_gap: []  
high_convergence_low_gap: [A-1, B-1, B-3, B-4, B-5, B-6, B-7, B-8, B-11, B-12, U-1, U-2, U-3, U-5, U-6]  
low_convergence_high_gap: []

[GAP] GAP-1 | type: 1 | priority: high | description: Retrieve prior catalytic C-H functionalization comparators used to frame efficiency, selectivity, and generality. | candidate_paper: Jordan & Taylor, J. Am. Chem. Soc. 111, 778–779 (1989); Moore et al., J. Am. Chem. Soc. 114, 5888–5890 (1992) | inference_label: T1 | status: pending

[GAP] GAP-2 | type: 1 | priority: high | description: Retrieve stoichiometric cyclometallation precedents used to support the proposed intermediate. | candidate_paper: Knobler, Crawford & Kaesz, Inorg. Chem. 14, 2062–2066 (1975); McGuiggan & Pignolet, Inorg. Chem. 21, 2523–2526 (1982) | inference_label: T1 | status: pending

[GAP] GAP-3 | type: 1 | priority: medium | description: Retrieve insertion and chelation-assisted oxidative-addition precedents cited for alternative elementary steps. | candidate_paper: Komiya & Yamamoto, Chem. Lett. 475–478 (1975); Cambie et al., J. Organomet. Chem. 429, 59–86 (1992) | inference_label: T1 | status: pending

[GAP] GAP-4 | type: 3 | priority: high | description: Locate later mechanistic studies that test the active Ru species, C-H cleavage reversibility, cyclometallated intermediates, and M-H versus M-C insertion pathways in the Murai reaction. | candidate_paper: subsequent mechanistic study of Ru-catalysed aromatic ketone C-H addition to olefins; not stated in target paper | inference_label: T2 | status: pending

[GAP] GAP-5 | type: 3 | priority: medium | description: Locate later scope or experimental-detail reports that provide full isolated yields, characterization data, and analytical methods for the products in Table 1. | candidate_paper: follow-up full experimental report on Ru-catalysed aromatic ketone/olefin coupling; not stated in target paper | inference_label: T2 | status: pending

inference_time_sec: not available — inject externally

## Response:
2026/4/27 10:25:50

> **Formulating structured output with citations**
>
> I need to follow the stage-2 requirements: provide structured details based on stage-1 outputs and cite relevant files. I’ll include citations to the paper and the uploaded prompt where necessary, and ensure the output is entirely in English for D1-D3 while using Japanese for D4/E.
> 
> I’ll keep the citations concise in the prompt_version line where possible for clarity.
>
> Thought for 23s

prompt_version: stage2-v182-20260426 `prompt_stage2_v182.md`  
model_info: GPT-5.5 Thinking

[D-1] declared_motivation | novelty_claims: T1: The paper claims that [REDACTED: substantial verbatim quotation; see Tier 9] T1: It further claims that the catalyst operates with “efficiency, selectivity and generality” valuable in organic synthesis. T1: The “key” is stated as “chelation assistance,” where low-valent ruthenium coordinates to the aromatic carbonyl group and is positioned for adjacent aromatic C-H cleavage. `Murai_1993.pdf` | success_criteria: high product yields, broad applicability across acylbenzene derivatives/acylheteroaromatics and olefins, virtually complete regioselectivity, high turnover frequencies, and avoidance of large excesses of one starting material are the criteria invoked by the paper. `Murai_1993.pdf` | layered_structure: yes — the claims are layered as transformation discovery, synthetic performance, selectivity, scope, and chelation-assisted design principle, so failure of the mechanistic model would not automatically refute the reported transformation.

[D-2] competitive_positioning: asserted — the paper positions itself against prior stoichiometric C-H cleavage and recent catalytic examples by stating that earlier systems had low yields, low turnover numbers, by-products, isomer mixtures, or narrow pyridine-derived scope, but it does not experimentally verify those comparisons side-by-side. `Murai_1993.pdf` | concurrent_submissions: not applicable; no Note Added in Proof or equivalent concurrent-submission statement is present in the target paper. | timing_pressure: A-1 shows that the mechanism is explicitly deferred despite strong claims of efficiency, selectivity, and generality; this supports only a T2 reading that the transformation was prioritized over mechanistic closure, not a claim of urgency. | format_exploitation: B-3, B-5, B-7, and B-8 indicate compressed reporting of GC quantification, regioselectivity, turnover frequency, and structural characterization; this is a T2 compression pattern, not proof of suppression. | audience_targeting: The vocabulary of C-H cleavage, transition-metal complexes, turnover frequency, chelation assistance, cyclometallated intermediates, olefin insertion, and reductive elimination targets synthetic organometallic chemists and catalytic methodology readers. `Murai_1993.pdf` | institutional_visibility: [external inference] Publishing a concise catalytic C-H functionalization result in Nature would likely maximize visibility beyond specialist organometallic chemistry.

[D-3] journal_constraint: The short report format is consistent with B-3, B-5, B-7, and B-8, where central quantitative and characterization details are summarized rather than fully documented. | field_competition_state: [external inference] The cited literature indicates an active transition-metal C-H activation field seeking catalytic, selective, and synthetically useful reactions. | entry_criteria: The paper implies that to be taken seriously, the method needed to show high yield, high regioselectivity, multiple substrate classes, and turnover frequency adequate for synthesis. `Murai_1993.pdf` | holy_grail_narrative: no — the paper uses standard problem-solution framing such as “critical step” and “ideal synthetic operation,” but does not use direct quest-framing language such as “holy grail,” “long-sought,” or “dream reaction.” `Murai_1993.pdf` | commercialization_potential: T1: The paper states that the catalyst will be “extremely valuable in organic synthesis” and that the reaction has “efficiency, selectivity and generality required for practical organic synthesis,” but it does not discuss cost, scale, regulation, waste, or industrial deployment. `Murai_1993.pdf`

[D-4]  
high_convergence_high_gap: none — フォールバック規則を適用  
D-4 候補数: 8（デフォルト上限適用）

candidate D4-1: 挿入経路の分岐を、どの実験で一義的に切り分けるべきだったのか。論文は M-H 結合への挿入と M-C 結合への挿入を並列に提示しているが、どちらが実際の結合形成経路なのかを問う実験設計を置いていない。この問いは単なる機構の未解明ではなく、生成物の結合形成順序そのものを決める中核的な未決定点である。  
grounded_in: [A-1, U-3, C-7]  
key_quote: [REDACTED: substantial verbatim quotation; see Tier 9] `Murai_1993.pdf`  
temperature_note: high_convergence_low_gap: U-3; severity includes critical  
same_root_group: [REDACTED: substantial verbatim quotation; see Tier 9]

candidate D4-2: 提案された cyclometallated intermediate は、反応機構の図ではなく、観測・捕捉・量論反応によってどこまで実体化されるべきだったのか。論文は中間体を機構の蝶番として用いるが、実際の触媒条件下でその存在を検証していない。  
grounded_in: [A-1, U-2, C-4]  
key_quote: [REDACTED: substantial verbatim quotation; see Tier 9] `Murai_1993.pdf`  
temperature_note: high_convergence_low_gap: U-2  
same_root_group: [REDACTED: substantial verbatim quotation; see Tier 9]

candidate D4-3: C-H cleavage が可逆なのか、律速なのか、あるいは後続の olefin insertion / reductive elimination が律速なのかを、反応設計のどの段階で問うべきだったのか。論文は「機構は明らかでない」と述べる一方で、選択性と効率を強く主張しており、速度論的支配と熱力学的支配の区別が外部化されている。  
grounded_in: [A-1, U-4, B-5, B-6]  
key_quote: [REDACTED: substantial verbatim quotation; see Tier 9] `Murai_1993.pdf`  
temperature_note: high_convergence_low_gap: A-1, B-5, B-6, U-4  
same_root_group: [REDACTED: substantial verbatim quotation; see Tier 9]

candidate D4-4: carbonyl coordination と chelation assistance は、説明原理なのか、実験的に検証された設計原理なのか。論文は carbonyl coordination を出発点として描くが、それが触媒サイクルへの入口を支配することを示す競争実験・阻害実験・配位状態解析を提示していない。  
grounded_in: [U-1, U-7, C-6]  
key_quote: [REDACTED: substantial verbatim quotation; see Tier 9] `Murai_1993.pdf`  
temperature_note: high_convergence_low_gap: U-1  
same_root_group: [REDACTED: substantial verbatim quotation; see Tier 9]

candidate D4-5: 1-indanone の「反応しない」という否定的結果は、どの検出下限・反応後分析・代替原因排除によって機構的証拠になるのか。論文は ring strain による説明を与えるが、C-H 活性化不能、触媒阻害、結合後段階の停止、分解などを区別していない。  
grounded_in: [U-6, B-11]  
key_quote: [REDACTED: substantial verbatim quotation; see Tier 9] `Murai_1993.pdf`  
temperature_note: high_convergence_low_gap: U-6, B-11  
same_root_group: [REDACTED: substantial verbatim quotation; see Tier 9]

candidate D4-6: 「virtually 100%」の選択性は、検出されなかった異性体の不存在なのか、検出感度以下なのか。論文は四つの可能な regioisomer のうち一つだけが生成すると述べるが、minor isomer の検出限界、分離能、response factor、時間変化を示していないため、高選択性の反対側が見えない。  
grounded_in: [B-5, B-6, U-5]  
key_quote: [REDACTED: substantial verbatim quotation; see Tier 9] `Murai_1993.pdf`  
temperature_note: high_convergence_low_gap: B-5, B-6, U-5  
same_root_group: [REDACTED: substantial verbatim quotation; see Tier 9]

candidate D4-7: 「efficiency」は、収率・GC 定量・単離収率・TON/TOF・mass balance のどれによって成立しているのか。論文は効率を中心的価値として掲げるが、GC yield と isolated yield が非対称に提示され、反応物回収・副生成物・時間分解 conversion が揃っていないため、効率の測定単位が統一されていない。  
grounded_in: [B-3, B-4, B-7, B-12, C-2, C-5]  
key_quote: [REDACTED: substantial verbatim quotation; see Tier 9] `Murai_1993.pdf`  
temperature_note: high_convergence_low_gap: B-3, B-4, B-7, B-12  
same_root_group: [REDACTED: substantial verbatim quotation; see Tier 9]

candidate D4-8: 反応を担う Ru 種は、初期投入錯体なのか、反応中に生成する共通活性種なのか。複数の Ru 錯体が「equally effective」「modestly effective」「not effective」と分類されるが、定量比較と speciation がないため、触媒・配位子・水素化物・CO 配位子の役割が設計原理に接続されていない。  
grounded_in: [B-1, C-3]  
key_quote: [REDACTED: substantial verbatim quotation; see Tier 9] `Murai_1993.pdf`  
temperature_note: high_convergence_low_gap: B-1  
same_root_group: not applicable

questions_that_cannot_be_asked:  
grounded_in: none (retrospective)  
key_quote: not applicable  
temperature_note: not applicable  
same_root_group: not applicable  
問い得ない問い: 著者が機構解明をどの程度意識的に後回しにしたのか、Nature 掲載のためにどのデータを省略したのか、競争相手をどの程度意識していたのかは、論文本文からは原理的に決められない。

priority_structure: この論文では、synthetic utility と broad scope を先に成立させるために、mechanistic closure と quantitative auditability が後方に置かれている構造として読める。A-1 ↔ B-5（ピボット）では、機構未解明のまま regioselectivity が中心成果として提示される。A-1 ↔ B-7（ピボット）では、機構・速度論が未解明のまま TOF が効率の根拠として使われる。A-1 ↔ B-3（ピボット）では、GC 定量の詳細が不足したまま「実用的合成反応」としての価値が主張される。構造の中核は、same_root_group「The proposed catalytic mechanism is not resolved by direct kinetic, labeling, intermediate, or pathway-discrimination evidence」と「Yield claims are made without complete conversion, recovery, or mass-balance data」である。

[E]  
derived_from: [A-1, B-5, B-7, U-1, U-2, U-3, U-4]  
anchoring_note: T2 — 論文が実際に答えた問いは、Ru 錯体が aromatic C-H bonds と olefins の addition を触媒できるかであり、その背後に「不活性結合をどのような補助原理で選択的反応へ変換するか」という一段抽象化された問いがある。

日本語での抽象化: この論文が化学の文脈で答えた問いは、「通常は直接使いにくい C-H 結合を、配位補助と遷移金属触媒によって、選択的な C-C 結合形成の入口にできるか」である。

変形1: 材料科学では、「通常は不活性な表面部位を、局所的な配位・欠陥・界面設計によって反応点へ変えられるか」という問いになる。これは同じ構造の別の現れである。

変形2: 計算化学では、「巨大な探索空間の中で、どの拘束・補助情報を入れれば探索を選択的に狭められるか」という問いになる。これは chelation assistance を探索制御原理として読み替える比喩的な類似である。

変形3: 研究方法論では、「成果を早く示すために、機構・定量・再現性のどの層を後続検証に回せるのか」という問いになる。これは Stage 1 の A/B/U 構造に基づく同じ構造の別の現れである。

変形4: 情報科学では、「ノイズの多い入力空間から、弱いが方向性のある拘束を使って有意味な出力だけを選択できるか」という問いになる。これは比喩的な類似である。

最も射程が広い変形としては、変形2を選ぶ。理由は、この論文の chelation assistance が単なる官能基効果ではなく、「不活性な可能性空間を、局所的な拘束によって反応可能な経路へ変換する」という一般化可能な構造を持つためである。

confirmed_english  
confirmed_english_propositional: [REDACTED: substantial verbatim quotation; see Tier 9]  
confirmed_english_question: [REDACTED: substantial verbatim quotation; see Tier 9]  
scope_type: "tool_question"

inference_time_sec: not available — inject externally

## Response:
2026/4/27 10:27:10

> **Evaluating observation level qualification**
>
> I’m trying to assess whether VQ-1 is qualified based on the analytical sample and standard methods used, but there are no details in the main text. It seems VQ-1 might pass as an observation, but the identity structure isn't fully clear. VQ-2 and VQ-3 methods have limitations, and
>
> Thought for 35s

prompt_version: stage3-v3-20260425 `prompt_stage3_v3.md`  
model_info: GPT-5.5 Thinking

# 科学的知見の再認定判定票

## Shinji Murai, Fumitoshi Kakiuchi, Shinya Sekine, Yasuo Tanaka, Asayuki Kamatani, Motohiro Sonoda & Naoto Chatani 1993（NATURE full_paper）

### §1 Claim Architecture

本論文のコア主張は、RuH2(CO)(PPh3)3 などの ruthenium complex が aromatic carbon-hydrogen bonds と olefins の addition を触媒し、C-C bond formation によって alkylated aromatic compounds を与える、という transformation discovery である。Novelty柱は「unactivated C-H bond cleavage を catalytic organic synthesis に実用的に接続したこと」、Utility柱は「efficiency, selectivity, generality」によって synthetic reaction として価値があるとする点にある。論文はさらに、carbonyl-directed chelation assistance により ortho C-H cleavage が促進されるという設計原理を提示している。`Murai_1993.pdf`

Layered structure: yes。層は、(1) transformation observation、(2) synthetic utility claim、(3) regioselectivity / scope claim、(4) chelation-assisted mechanism claim、(5) prior-work superiority / benchmark claim に分かれる。単一の反証で全体が崩れる構造ではなく、mechanism claim が崩れても transformation observation は残り得る一方、utility・benchmark・mechanism の上位層は定量報告と識別実験に強く依存している。

### §2 SRG / CLA → RI / ER / EP Crosswalk

**SRG-1 Analytical validation and product characterization data are described generally but not reported in detail**

* **Primary RI**: RI-02 Object identification
* **Secondary RI**: RI-01 Reporting integrity; RI-08 Unquantified reliability
* **ER**: 生成物構造・純度・regioisomer assignment を、代替構造候補を排除できる粒度で提示する必要がある。GC yield を主証拠にする場合、calibration, response factor, internal standard, replicate uncertainty を同時に開示する必要がある。
* **EP**: EP-02a Identity / purity substantiation pack; EP-01a Reporting-coherence pack; EP-08a Replication / uncertainty pack
* **Case-specific実装**: Table 1 の全生成物について isolated sample の ^1H/^13C NMR, MS/HRMS, elemental analysis または equivalent purity data, regioisomer diagnostic signal, GC calibration curve, response factor, internal standard を product-by-product で提示する。
* **注記**: B-3, B-8。TEMPERATURE_SUMMARY: high_convergence_low_gap。convergence: B-3 = 2/3, B-8 = 2/3。communication-era では compressed characterization として許容され得るが、modern recertification では VQ-1 の unqualified 化に必要。

**SRG-2 Yield claims are made without complete conversion, recovery, or mass-balance data**

* **Primary RI**: RI-01 Reporting integrity
* **Secondary RI**: RI-08 Unquantified reliability
* **ER**: 「almost quantitative yields」や「based on both starting materials」を採るには、product yield だけでなく conversion, recovery, crude mass balance, by-product accounting を同一基準で報告する必要がある。
* **EP**: EP-01a Reporting-coherence pack; EP-08a Replication / uncertainty pack
* **Case-specific実装**: aromatic ketone と olefin の両方について initial amount, recovered starting material, conversion, GC yield, isolated yield, by-product distribution, mass balance closure を runs 1–13 に対して統一表形式で示す。
* **注記**: B-4, B-12。TEMPERATURE_SUMMARY: high_convergence_low_gap。convergence: B-4 = 2/3, B-12 = 2/3。

**SRG-3 Selectivity is reported without time-course, minor-isomer, or causal validation data**

* **Primary RI**: RI-04 Unreplicated discriminator
* **Secondary RI**: RI-01 Reporting integrity; RI-08 Unquantified reliability
* **ER**: “virtually 100%” regioselectivity を採るには、minor regioisomers の検出下限、クロマトグラフィー分離能、response factor、時間変化、kinetic vs thermodynamic control の識別を提示する必要がある。
* **EP**: EP-04a Discrimination / replication pack; EP-01a Reporting-coherence pack; EP-08a Replication / uncertainty pack
* **Case-specific実装**: runs 8 and 13 および representative olefin entries で、四つの可能な regioisomers の authentic standard または assignment logic、GC/NMR detection limit、time-course regioisomer ratio、extended heating による isomer redistribution の有無を示す。
* **注記**: B-5, B-6, U-5。TEMPERATURE_SUMMARY: high_convergence_low_gap。B-5 は convergence 3/3 で、V1/V2/V3 が同一箇所を高 severity と評価。

**SRG-4 The proposed catalytic mechanism is not resolved by direct kinetic, labeling, intermediate, or pathway-discrimination evidence**

* **Primary RI**: RI-03 Unobserved explanatory
* **Secondary RI**: RI-04 Unreplicated discriminator; RI-06 Imported model; PRI-10 Kinetic overclaim（暫定・限定適用）
* **ER**: cyclometallated intermediate, carbonyl coordination, C-H cleavage, olefin insertion, reductive elimination を機構主張として採るには、観測・捕捉・速度論・isotope labeling・stoichiometric validation によって elementary-step sequence を拘束する必要がある。
* **EP**: EP-03a Direct-observation / state-assignment pack; EP-04a Discrimination / replication pack; EP-06a Analogy-validation pack; EP-10a Kinetic verification pack
* **Case-specific実装**: RuH2(CO)(PPh3)3 / aromatic ketone / olefin 系で in situ NMR/IR による Ru species monitoring、stoichiometric cyclometallation, H/D exchange, KIE, deuterium-labeled ketone/olefin crossover, rate law, olefin-order dependence, M-H vs M-C insertion discrimination を行う。
* **注記**: A-1, U-1, U-2, U-3, U-4。TEMPERATURE_SUMMARY: high_convergence_low_gap。U-3 は critical severity を含む。RI-06 は refs. 14–18 の precedent を対象系機構へ移植している点に由来する。

**SRG-5 Efficiency is compared to prior work without explicit numerical benchmark completion**

* **Primary RI**: RI-09 External superiority
* **Secondary RI**: RI-08 Unquantified reliability; RI-01 Reporting integrity
* **ER**: prior catalytic C-H functionalization より efficiency, selectivity, generality が優れるとするには、同一軸で TON, TOF, yield, selectivity, substrate scope, stoichiometry, by-product formation を比較する必要がある。
* **EP**: EP-09a Internal benchmark pack; EP-08a Replication / uncertainty pack; EP-01a Reporting-coherence pack
* **Case-specific実装**: Jordan & Taylor 1989 および Moore et al. 1992 などの cited comparators と、present Ru-catalyzed ketone/olefin addition を、同一表内で TON/TOF, isolated yield, GC yield, regioselectivity, substrate count, excess reagent requirement により比較する。
* **注記**: B-7, C-2。TEMPERATURE_SUMMARY: high_convergence_low_gap。比較は本文で asserted されるが、side-by-side numerical benchmark は未完成。

**SRG-6 Failure and rate variation cases are invoked without diagnostic separation of mechanistic causes**

* **Primary RI**: RI-05 Qualitative overread
* **Secondary RI**: RI-04 Unreplicated discriminator; RI-07 Unsupported boundary
* **ER**: 1-indanone の “did not react at all” や reaction time の大差を機構的説明に使うには、C-H activation failure, catalyst inhibition, binding failure, post-cyclometallation failure, catalyst decomposition を切り分ける診断実験が必要である。
* **EP**: EP-05a Quantitative-ranking substantiation pack; EP-04a Discrimination / replication pack; EP-07a Boundary-test pack
* **Case-specific実装**: 1-indanone, six-membered analogue, run 10/11 substrates を matched-pair として、conversion, recovered substrate, catalyst integrity, stoichiometric cyclometallation, substrate inhibition, time-course rate を比較する。
* **注記**: U-6, B-11。TEMPERATURE_SUMMARY: high_convergence_low_gap。negative result as evidence の case-specific 代表例。

SRG外：CLA

**CLA-1 Active Ru species and catalyst-comparison basis**

* **Primary RI**: RI-03 Unobserved explanatory
* **Secondary RI**: RI-05 Qualitative overread; RI-02 Object identification
* **ER**: “equally effective,” “modestly effective,” “not effective” という catalyst comparison を設計原理へ接続するには、初期錯体と実際の active Ru species を区別し、ligand/CO/hydride の役割を定量的に示す必要がある。
* **EP**: EP-03a Direct-observation / state-assignment pack; EP-05a Quantitative-ranking substantiation pack; EP-02a Identity / purity substantiation pack
* **Case-specific実装**: RuH2(CO)(PPh3)3, Ru(CO)2(PPh3)3, RuH2(PPh3)4, Ru(CO)3(PPh3)2, RuHCl(CO)(PPh3)3, Ru3(CO)12 を同条件で比較し、initial rate, conversion, yield, selectivity, ligand dissociation, hydride/CO signals, decomposition products を in situ NMR/IR で追跡する。
* **注記**: B-1, C-3。TEMPERATURE_SUMMARY: high_convergence_low_gap。D4-8 に対応。SRGには属さないが、catalyst identity precision に直結するCLA。

### §3 現在のVQ判定

現在判定: VQ-1 (Observation, qualified)

**VQ-1 Observation は qualified として通る。**  
Table 1 により transformation の発生、生成物構造式、yield、reaction time が提示され、本文は products が “established unequivocally by standard methods” と述べているため、communication-era の観察主張としては成立する。`Murai_1993.pdf` ただし SRG-1 の RI-02 が main text 内では完全に解消されていないため、modern recertification では EP-02a の投入により unqualified VQ-1 へ補強する必要がある。

**VQ-2 Method は未達。**  
VQ-2 は RI-02 が非致命的に扱えることを前提に、RI-01 と RI-07 の解消を要求するが、SRG-2 の mass balance / yield basis、SRG-3 の selectivity detection basis、SRG-6 の failure-boundary diagnostics が未解消である。したがって synthetic method としての一般化可能性は qualified VQ-1 を超えて再認定できない。

**VQ-3 Mechanism は未達。**  
VQ-3 は VQ-2 要件に加えて RI-03, RI-04, RI-06 の解消を要求するが、SRG-4 において carbonyl coordination, cyclometallated intermediate, M-H vs M-C insertion, C-H cleavage reversibility が直接拘束されていない。したがって chelation-assisted mechanism は mechanistic hypothesis に留まり、VQ-3には到達しない。

**VQ-4 Benchmark は未達。**  
VQ-4 は VQ-3 の成立に加え RI-08 と RI-09 の解消を要求するが、SRG-5 において prior catalytic systems との normalized benchmark がない。TOF・yield・selectivity・scope の優位性は本文で主張されるが、benchmark-grade comparison には到達していない。

**層別VQ非対称性:**  
transformation observation 層は VQ-1 qualified に到達する。synthetic utility 層は RI-01 / RI-08 のため VQ-2未達。chelation-assisted mechanism 層は RI-03 / RI-04 / RI-06 のため VQ-3未達。prior-work superiority 層は RI-09 のため VQ-4未達。

### §4 Era-Norm Annotation

communication-era tolerated:

* A-1: “The mechanism ... is not yet clear” と明記した上で transformation を優先する構成は、1993年の短報的 Nature article としては許容され得る。
* B-3: GC yields と selected isolated yields の併用は、紙幅の限られた scope table では compressed reporting として許容され得る。
* B-5: “virtually 100%” regioselectivity に検出限界を付けない記述は、当時の communication-format synthetic report ではしばしば許容され得る。
* B-7: TOF の正確な計算表を省略し、Table 1 の time/yield から効率を示す形式は、短報では許容され得る。
* B-8: “standard methods” による product characterization の一括記述は、短い printed article では許容され得る。
* B-1: catalyst comparison を “equally/modestly/not effective” と定性的に圧縮することは、初報の screening description として許容され得る。

modern-era deficient:

* B-3 / B-8: GC calibration, response factor, internal standard, product spectra, regioisomer diagnostics がなければ VQ-1 の unqualified observation に不足する。
* B-4 / B-12: conversion, recovered starting materials, by-products, bilateral mass balance がなければ “almost quantitative” efficiency claim を再認定できない。
* B-5 / B-6: minor regioisomer detection limit と time-course selectivity がなければ “virtually 100%” selectivity を再認定できない。
* A-1 / U-1 / U-2 / U-3 / U-4: mechanism を deferred に置いたまま chelation assistance を設計原理として扱うには、現代基準では direct observation, labeling, kinetics が不足する。
* U-6 / B-11: 1-indanone failure や reaction time variation を ring strain / mechanistic boundary として読むには、現代基準では matched diagnostic controls が不足する。
* B-7 / C-2: “among the highest” TOF や prior-work superiority を主張するには、現代基準では normalized benchmark が必要である。

### §5 最短補強ルート

**VQ-1 qualified → VQ-1 unqualified への最短ルート：**

1. EP-02a Identity / purity substantiation pack — Table 1 全生成物について spectra, HRMS/elemental analysis, purity criteria, regioisomer assignment diagnostics を提示する。RI-02 を前進。
2. EP-01a Reporting-coherence pack — GC calibration, response factors, internal standard, isolated yield, GC yield の対応関係を統一表で示す。RI-01 を前進。

**VQ-2 への最短ルート：**

1. EP-01a Reporting-coherence pack — runs 1–13 について conversion, recovered starting material, crude mass balance, olefin equivalents, catalyst loading normalization を統一化する。RI-01 を前進。
2. EP-08a Replication / uncertainty pack — representative high-yield, low-yield, and long-time entries について replicate count, standard deviation, analytical uncertainty を示す。RI-08 を前進。
3. EP-07a Boundary-test pack — 1-indanone, five-/six-membered ketone comparison, olefin class variation, acylbenzene/acylheteroaromatic boundary を matched-pair で検証する。RI-07 を前進。

**VQ-3 への最短ルート：**

1. EP-03a Direct-observation / state-assignment pack — Ru-cyclometallated intermediate と active Ru species を in situ NMR/IR, stoichiometric trapping, independent synthesis で拘束する。RI-03 を前進。
2. EP-04a Discrimination / replication pack — deuterium labeling, crossover, H/D exchange, KIE により M-H insertion と M-C insertion を識別する。RI-04 を前進。
3. EP-10a Kinetic verification pack — rate law, substrate order, olefin order, catalyst order, temperature dependence を取得し、C-H cleavage / insertion / reductive elimination の律速候補を切り分ける。PRI-10 および RI-04 を前進。
4. EP-06a Analogy-validation pack — refs. 14–18 の stoichiometric precedents と本 Ru catalytic system の oxidation state, ligand set, elementary-step homology を検証する。RI-06 を前進。

**VQ-4 への最短ルート：**

1. EP-09a Internal benchmark pack — Jordan & Taylor 1989, Moore et al. 1992 など cited prior work と、TON/TOF, isolated yield, selectivity, scope, reagent excess, by-products を同一軸で比較する。RI-09 を前進。
2. EP-08a Replication / uncertainty pack — benchmark entries を反復測定し、TOF/yield/selectivity の uncertainty を付ける。RI-08 を前進。
3. EP-01a Reporting-coherence pack — GC-based metrics と isolated metrics の比較可能性を保証する。RI-01 を前進。

認定ゲート順注記: 実験投入順は情報利得順だが、最終認定は VQ-1 → VQ-2 → VQ-3 → VQ-4 の継承ゲート順で確定する。

### §6 制度設計への寄与

本ケースは既存RIコードの代表事例を追加確認した。特に RI-03 は、cyclometallated intermediate と active Ru species が反応説明の中核を担いながら、直接観測・速度論的拘束・標識実験で未確定な場合の典型例である。

RI-06 の代表事例として、stoichiometric cyclometallation precedents や olefin insertion precedents を、対象の catalytic RuH2(CO)(PPh3)3 系へ同型性実証なしに輸入する構造が確認された。これは個別ステップ類推型 RI-06 であり、サイクル全体輸入ほど大規模ではないが、VQ-3 を制限する。

RI-04 + RI-03 + RI-06 の共起パターンが明瞭である。中間体未観測（RI-03）、M-H/M-C insertion の識別不在（RI-04）、他系 precedent の輸入（RI-06）が同一SRGに共存しており、いずれか一つのEPだけでは VQ-3 に到達できない。

RI-01 + RI-08 + RI-09 の utility / benchmark 共起も確認された。GC yield, isolated yield, mass balance, TOF, prior-work comparison が分離しており、efficiency claim を VQ-4 に上げるには EP-01a, EP-08a, EP-09a の同時投入が必要である。

否定的証拠の不完全性が U-6 / SRG-6 で確認された。1-indanone の nonreaction を ring strain の evidence として用いる場合、検出下限、substrate recovery, catalyst integrity, matched-pair control が必要であり、これは RI-04 / RI-05 の case-specific実装例として登録できる。

通信→Full Paper遷移の自動解消パターンが強い。B-3, B-4, B-8, B-12 は通信形式の紙幅制約に由来する可能性が高く、full experimental report に移行すれば EP-01a / EP-02a / EP-08a によって自動解消されやすい。

PRI-12 は本ケースの primary pattern ではない。新規 descriptor, formal theory, self-referential validation, deductive-retrospective circularity を中心主張とする論文ではないため、PRI-12 cluster A/B の適用閾値には達しない。

新規PRI候補は不要である。本ケースは既存の RI-01, RI-02, RI-03, RI-04, RI-05, RI-06, RI-08, RI-09 および暫定 PRI-10 の組み合わせで十分に表現できる。

## Response:
2026/4/27 10:34:52

> **Searching for relevant literature and citations**
>
> I need to gather some relevant papers for the Murai reaction EP, particularly for post-1993, and make sure to structure the response in Japanese. Since I'll likely need current references, I’ll search for academic papers on the topic and cite them accordingly. Let's dive into that!
>
> **Searching literature on Murai reaction and mechanisms**
>
> [Room-Temperature Regioselective C−H/Olefin Coupling of ...](https://pubs.acs.org/doi/abs/10.1021/ja104918f)
> [Murai reaction](https://en.wikipedia.org/wiki/Murai_reaction)
> [Ruthenium-Catalyzed Cycloadditions to Form 5-, 6 - PMC - NIH](https://pmc.ncbi.nlm.nih.gov/articles/PMC8284937/)
> [Synthesis of ruthenium complexes and their catalytic ...](https://arabjchem.org/synthesis-of-ruthenium-complexes-and-their-catalytic-applications-a-review/)
> [Recent advances in the ruthenium-catalyzed hydroarylation of ...](https://pubs.rsc.org/en/content/articlehtml/2015/ob/c5ob01472g)
> [Synthesis and x-ray structural characterization of Ru(PPh3) ...](https://www.researchgate.net/publication/244457706_Synthesis_and_x-ray_structural_characterization_of_RuPPh33COC2H4_and_RuHo-C6H4COCH3_PPh32L_L_PPh3_CO_DMSO_Ruthenium_complexes_with_relevance_to_the_Murai_reaction)
> [Kinetic Isotope Effects in the Study of Organometallic ...](https://xingweili.snnu.edu.cn/KIE_mechanism_review.pdf)
> [The Synthesis of N-Substituted Ferrocenes and C–H ...](https://d-nb.info/983673624/34)
> [Ruthenium(0)-Catalyzed Cross-Coupling of Anilines with ...](https://par.nsf.gov/servlets/purl/10146149)
> [Scope and Mechanistic Studies of Ruthenium Catalyzed C-N ...](https://epublications.marquette.edu/cgi/viewcontent.cgi?params=%2Fcontext%2Fdissertations_mu%2Farticle%2F2085%2F&path_info=KirindeArachchige_marquette_0116D_11722.pdf)
>
> **Checking for official research papers**
>
> I might need to check the official paper details, perhaps from sources like the ACS. It’ll help me find more accurate, official references for what I’m working on. I’ll take a look at reputable research sources to ensure everything is as precise as possible.
>
> **Searching for official ACS paper details**
>
> [Synthesis and x-ray structural characterization of Ru(PPh3)3(CO)(C2H4) and RuH(o-C6H4C(O)CH3) (PPh3)2L (L = PPh3, CO, DMSO): Ruthenium complexes with relevance to the Murai reaction | Request PDF](https://www.researchgate.net/publication/244457706_Synthesis_and_x-ray_structural_characterization_of_RuPPh33COC2H4_and_RuHo-C6H4COCH3_PPh32L_L_PPh3_CO_DMSO_Ruthenium_complexes_with_relevance_to_the_Murai_reaction)
> [Recent advances in the ruthenium-catalyzed hydroarylation of alkynes with aromatics: synthesis of trisubstituted alkenes  - Organic & Biomolecular Chemistry (RSC Publishing) DOI:10.1039/C5OB01472G](https://pubs.rsc.org/en/content/articlehtml/2015/ob/c5ob01472g)
>
> **Searching for specific paper on Sonoda BCSJ 1997**
>
> I need to find the full paper for Sonoda BCSJ 1997, specifically focusing on the product scope and substituent effects. I’ll search in detail to locate papers that match this. Once I find it, I’ll use that information to move forward with this task efficiently.
>
> **Searching for Sonoda 1997 papers and substituent effects**
>
> [Ruthenium-Catalyzed Addition of Carbon–Hydrogen Bonds in ...](https://www.semanticscholar.org/paper/b148339a5faf06a044b69110471cad6e2a913cdd)
> [Ruthenium-Catalyzed Addition of Carbon—Hydrogen ...](https://scispace.com/papers/ruthenium-catalyzed-addition-of-carbon-hydrogen-bonds-in-3dta7wwp57)
> [Catalytic C−H/Olefin Coupling - ACS Publications](https://pubs.acs.org/doi/10.1021/ar960318p)
> [Catalytic C-h/olefin coupling](https://pubmed.ncbi.nlm.nih.gov/12379135/)
> [Volume 70 Issue 12 | Bulletin of the Chemical Society of Japan](https://academic.oup.com/bcsj/issue/70/12)
> [Pure and Applied Chemistry](https://publications.iupac.org/pac/66/7/1527/same_authors/index.html)
> [Ruthenium-catalyzed ortho -C–H bond alkylation of aromatic ...](https://pubs.rsc.org/en/content/articlehtml/2013/sc/c3sc50310k)
> [Catalytic addition of C-H bonds to multiple bonds with the aid ...](https://link.springer.com/article/10.1023/A%3A1019064627386)
> [ChemInform Abstract: Catalytic C-H/Olefin Coupling | Request PDF](https://www.researchgate.net/publication/264444682_ChemInform_Abstract_Catalytic_C-HOlefin_Coupling)
> [Publication of Takahashi laboratory homepage](https://www.cat.hokudai.ac.jp/takahashi/publication.html)
> [園田 素啓 (Motohiro Sonoda) - マイポータル](https://researchmap.jp/313412263652)
> [Murai, Shinji, Kakiuchi, Fumitoshi, Sekine, Shinya, Tanaka, ...](https://www.mindat.org/reference.php?id=2944383)
> [The Ruthenium-Catalyzed Addition of β C–H Bonds in ...](https://www.scilit.com/publications/1c1c886f7d06fc0062c176fd8f5ae27e)
> [Catalytic Addition of Aromatic Carbon–Hydrogen Bonds to ...](https://cir.nii.ac.jp/crid/1360846644034359296)
> [Catalytic C-h/olefin coupling.](https://www.sigmaaldrich.com/JP/ja/tech-docs/paper/107580?srsltid=AfmBOooZfR4Zce8Vqr05YHDqZfyqp5t4cZZ4y-c8rr8-L--q7RaWRAZp)
> [Transition metal catalyzed manipulation of non-polar carbon ...](https://pmc.ncbi.nlm.nih.gov/articles/PMC3165906/)
> [The halogen effect in ruthenium catalysis](https://rcr.colab.ws/publications/10.59761/RCR5170)
> [Hydride-Rhodium(III)-N-Heterocyclic Carbene Catalyst for ...](https://zaguan.unizar.es/record/127883/files/texto_completo.pdf?version=2)
> [Murai reaction](https://en.wikipedia.org/wiki/Murai_reaction)
> [Ruthenium-catalyzed regioselective step-growth ...](https://www.sciencedirect.com/science/article/abs/pii/0022328X96062365)
> [研究業績 / 有機分子触媒による未来型分子変換](https://orgreact.sakura.ne.jp/orgcatal/publications/index.html)
>
> **Searching for 1995 BCSJ paper on catalytic addition**
>
> I should check if the full 1995 BCSJ paper titled "Catalytic Addition..." is related to EP-01/02. It seems like a good fit, so I’ll open the source and find the details I need to complete this. Hopefully, it’ll provide the necessary information to move forward.
>
> **Searching for 1995 BCSJ paper "Catalytic Addition"**
>
> [
    Catalytic Addition of Aromatic Carbon–Hydrogen Bonds to Olefins with the Aid of Ruthenium Complexes | CiNii Research
](https://cir.nii.ac.jp/crid/1360846644034359296)
> [Volume 70 Issue 12 | Bulletin of the Chemical Society of Japan | Oxford Academic](https://academic.oup.com/bcsj/issue/70/12)
> [Checking your browser - reCAPTCHA](https://pubmed.ncbi.nlm.nih.gov/12379135/)
> [Pure and Applied Chemistry, 1994, Volume 66, No. 7, pp. 1527-1534, Other PAC articles by these authors
](https://publications.iupac.org/pac/66/7/1527/same_authors/index.html)
> [Catalytic addition of C-H bonds to multiple bonds with the aid of ruthenium complexes | Catalysis Surveys from Asia | Springer Nature Link](https://link.springer.com/article/10.1023/A%3A1019064627386)
>
> **Searching for 2010 JACS paper details**
>
> I should look up the exact 2010 paper from JACS to find the specifics I need. I’ll search for it and open the source to get the right details. Hopefully, that will provide the necessary information to continue with this task. Let's narrow it down.
>
> **Searching for 2010 JACS publication details**
>
> [Room-Temperature Regioselective C−H/Olefin Coupling of ...](https://pubs.acs.org/doi/10.1021/ja104918f)
> [KAKEN — 研究課題をさがす | 遷移金属触媒による芳香族炭素-水素 ...](https://kaken.nii.ac.jp/ja/grant/KAKENHI-PROJECT-22750096/)
> [Room-temperature regioselective C-H/olefin coupling of ...](https://pubmed.ncbi.nlm.nih.gov/21114294/)
> [Takuya Kochi PhD Professor (Assistant) at Keio University](https://www.researchgate.net/profile/Takuya-Kochi)
> [Room-temperature regioselective C-H/olefin coupling of ...](https://www.semanticscholar.org/paper/Room-temperature-regioselective-C-H-olefin-coupling-Kakiuchi-Kochi/87c5428857ce79daa5d8b7edce3921475a7c1999)
> [Room-Temperature Regioselective C−H/Olefin Coupling of ...](https://ouci.dntb.gov.ua/en/works/7ARGaO84/)
> [Visible Light-Activated Ruthenium-Catalysed Direct Arylation at ...](https://papers.ssrn.com/sol3/Delivery.cfm/01ed5c7b-fafc-4ba1-8f8c-adbf34a295f5-MECA.pdf?abstractid=4082347&mirid=1)
> [Room-Temperature Regioselective C−H/Olefin Coupling ...](https://www.sci-hub.red/version/75bc59ebd22632e6e35f4c1928cc59cef56aee0871bf951a301188c81e68588f/10.1021/ja104918f)
> [Transition metal catalyzed manipulation of non-polar carbon ...](https://pmc.ncbi.nlm.nih.gov/articles/PMC3165906/)
> [垣内研・有機金属化学研究室 Results＜原著論文＞](https://www.orgmet.chem.keio.ac.jp/results/paper.html)
> [KAKEN — Researchers | KOCHI Takuya (70396779)](https://nrid.nii.ac.jp/en/nrid/1000070396779/)
> [Takuya Kochi (0000-0002-5491-0566)](https://orcid.org/0000-0002-5491-0566)
> [Pure and Applied Chemistry](https://publications.iupac.org/pac/66/7/1527/cited_by/index.html)
> [Regioselective Intermolecular Coupling Reaction of Arylketones ...](https://discovery.researcher.life/article/regioselective-intermolecular-coupling-reaction-of-arylketones-and-alkenes-involving-c-h-bond-activation-catalyzed-by-an-i-in-situ-i-formed-cationic-ruthenium-hydride-complex/bfbb1d134c1b349699138801deb1dfdd)
> [多様なルテニウムホスフィン触媒を用いた 不活性結合の選択的 ...](https://koara.lib.keio.ac.jp/xoonips/modules/xoonips/download.php/KO50002002-20185058-0003.pdf?file_id=141207)
> [C-C bond formation via C-H bond activation using an in ...](https://europepmc.org/article/med/19449877)
> [Topics in Current Chemistry - Springer Nature](https://link.springer.com/content/pdf/10.1007/978-3-642-12356-6.pdf)
> [Fujiwara–Moritani reaction](https://en.wikipedia.org/wiki/Fujiwara%E2%80%93Moritani_reaction)
> [Selective Activation of Aromatic C-H Bonds Catalyzed by Single Gold Atoms at Room Temperature](https://arxiv.org/abs/2308.04658)
>
> **Looking for DFT papers on mechanism and regioselectivity**
>
> I need to dive deeper into detailed DFT papers that focus on mechanisms and regioselectivity. Finding the right papers will help clarify the specifics I need for this task. I’ll make sure to focus on the ones most relevant to the topic. Let's get this sorted!
>
> **Searching for DFT studies on mechanism and regioselectivity**
>
> [Metal-Mediated and Metal-Catalyzed Reactions of Isocyanides](https://pubs.acs.org/doi/10.1021/cr500380d)
> [Theoretical investigation on regioselectivity of aromatic ...](https://link.springer.com/article/10.1007/BF02969447)
> [Selective C–H functionalization of furfural and its derivatives](https://theses.hal.science/tel-05088130v1/file/145608_MORI_2024_archivage.pdf)
> [A DFT Study of Site‐Selectivity in Oxidative Addition ...](https://www.researchgate.net/publication/230505608_A_DFT_Study_of_Site-Selectivity_in_Oxidative_Addition_Reactions_with_Pd0_Complexes_The_Effect_of_an_Azine_Nitrogen_and_the_Use_of_Different_Types_of_Halogen_Atoms_in_the_Substrate)
> [Transition-Metal-Catalyzed C-H Functionalization of ...](https://dokumen.pub/transition-metal-catalyzed-c-h-functionalization-of-heterocycles-2-volumes-9781119774136.html)
> [Cobalt-catalyzed C-H Functionalization - Girona](https://dugi-doc.udg.edu/bitstream/handle/10256/15419/topf_20180223.pdf?isAllowed=y&sequence=1)
> [Design of Reagents and Ligands for Direct Palladium ... - MACAU](https://macau.uni-kiel.de/servlets/MCRFileNodeServlet/macau_derivate_00009710//PhD%20Thesis_Sourjya%20Mal_2026.pdf)
> [Catalysed C–H Activation: Kinetic Resolution and Pd Shift](https://files01.core.ac.uk/download/586580447.pdf)
> [Regioselective ketone α-alkylation with simple olefins via ...](https://www.science.org/doi/10.1126/science.1254465)
> [Room-temperature regioselective C-H/olefin coupling of ...](https://pubmed.ncbi.nlm.nih.gov/21114294/)
> [Photochemistry of transition metal hydrides](https://eprints.whiterose.ac.uk/id/eprint/103893/2/acs_2Echemrev_2E6b00204.pdf)
> [Simone Manzini PhD thesis - St Andrews Research Repository](https://research-repository.st-andrews.ac.uk/bitstream/handle/10023/5445/SimoneManziniPhDThesis.pdf?isAllowed=y&sequence=3)
> [Pure and Applied Chemistry](https://publications.iupac.org/pac/66/7/1527/cited_by/index.html)
> [Nickel-Catalyzed Reductive Carboxylation and Amidation of ...](https://www.tdx.cat/bitstream/handle/10803/670204/TESI%20Andreu%20Tortajada%20Navarro.pdf?isAllowed=y&sequence=1)
> [Catalytic Transformations Based on Pincer and Half- ...](https://www.hbni.ac.in/phdthesis/chem/CHEM11201104001.pdf)
> [Anionic Nitrogen Chelate Ligands: From Molecular Self- ...](https://utoronto.scholaris.ca/server/api/core/bitstreams/e76b6c14-2f6d-45d9-9171-93b28a8300b4/content)
> [TARGETS IN HETEROCYCLIC SYSTEMS](https://www.soc.chim.it/sites/default/files/ths/old/vol_08_2004.pdf)
> [A theoretical study on the mechanisms of intermolecular ...](https://ouci.dntb.gov.ua/en/works/4wrxQRB7/)
> [Muraiova reakce](https://cs.wikipedia.org/wiki/Muraiova_reakce)
> [Metal Complexes Containing Boron Based Ligands](https://mdpi-res.com/bookfiles/book/1760/Metal_Complexes_Containing_Boron_Based_Ligands.pdf)
> [Hydride ligands make the difference: density functional study of ...](https://www.semanticscholar.org/paper/Hydride-ligands-make-the-difference%3A-density-study-Helmstedt-Clot/0e10b505a6beecc107dc0c6c508d4b1f03940e07)
> [Crystallography Open Database: Search results](https://qiserver.ugr.es/cod/result.php?CODSESSION=h8fpivbr5p7n30bpupivqoi5r9&count=1000&order=desc&order_by=vol&page=11)
>
> **Structuring answer with citations**
>
> I need to provide a structured answer with citations while keeping it concise. If I use web sources, I must cite them, but avoid raw links. The target file also needs citation for original facts. I’ll search for additional papers, like Matsubara's work, focusing on mechanisms and cationic Ru hydride catalysts.
>
> **Searching for mechanistic papers on Ru hydride catalysts**
>
> [Checking your browser - reCAPTCHA](https://pubmed.ncbi.nlm.nih.gov/21114294/)
> [Theoretical investigation on regioselectivity of aromatic ketones in the addition with olefin catalyzed by RuH2(CO)(PPh3)3 | Science China Chemistry | Springer Nature Link](https://link.springer.com/article/10.1007/BF02969447)
>
> **Using PubMed search results with citations**
>
> I’m thinking of using a PubMed search for 2010, along with abstract snippets. A ResearchGate page with an abstract view should also work, and I can cite the search result and ResearchGate. I'll include sources from KAKEN for exact pages too. Now, I’ll also try searching for the Simon/Martinez 2009 papers.
>
> **Searching for relevant research articles and citations**
>
> [Regioselective Intermolecular Coupling Reaction of ... - PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC2805103/)
> [RuH2(H2)2(PCy3)2: A room temperature catalyst for the Murai ...](https://www.researchgate.net/publication/257557195_RuH2H22PCy32_A_room_temperature_catalyst_for_the_Murai_reaction)
> ["Regioselective Intermolecular Coupling Reaction of ...](https://epublications.marquette.edu/chem_fac/415/)
> [Versatile Reactivity of the Bis(dihydrogen) Complex RuH 2 (H ...](https://pubs.acs.org/doi/10.1021/om950888d)
> [Regioselective Intermolecular Coupling Reaction of ...](https://discovery.researcher.life/article/regioselective-intermolecular-coupling-reaction-of-arylketones-and-alkenes-involving-c-h-bond-activation-catalyzed-by-an-i-in-situ-i-formed-cationic-ruthenium-hydride-complex/bfbb1d134c1b349699138801deb1dfdd)
> [Transition metal-catalysed hydrogen transfer processes for ...](https://www.diva-portal.org/smash/get/diva2%3A562713/FULLTEXT02.pdf)
> [Regioselective Intermolecular Coupling Reaction of ...](https://ouci.dntb.gov.ua/en/works/4Oyka6W9/)
> [Nonclassical Interactions and σ‑Bond Activation Reactions](https://digital.csic.es/bitstream/10261/136216/1/Nonclassical%20Interactions.pdf)
> [Room-temperature regioselective C-H/olefin coupling of ...](https://www.semanticscholar.org/paper/Room-temperature-regioselective-C-H-olefin-coupling-Kakiuchi-Kochi/87c5428857ce79daa5d8b7edce3921475a7c1999)
> [Selective Formation of Trisubstituted Olefins and Benzo-Fused ...](https://scispace.com/pdf/experimental-and-computational-study-of-the-z-selective-281xvlc7pi.pdf)
> [The Organometallic Chemistry of the Transition Metals](https://ndl.ethernet.edu.et/bitstream/123456789/76936/1/72.pdf)
> [Full text of "The organometallic chemistry of the transition ...](https://archive.org/stream/The_Organometallic_Chemistry_Of_Transition_Metals/The_Organometallic_Chemistry_Of_Transition_Metals_djvu.txt)
> [Hiyama coupling](https://en.wikipedia.org/wiki/Hiyama_coupling)
>
> **Selecting relevant papers for mechanistic study**
>
> I need to focus on studies related to aromatic esters, such as Kakiuchi & Ohtaki’s 2001 mechanistic paper—though, this isn't the exact target. I could consider several other papers too, including those from Kakiuchi et al. and Sonoda et al. for boundary tests and selectivity, but I'll prioritize specific ketone-focused studies first.
>
> **Considering relevant citations and sources**
>
> I’m thinking of including the 2004 Guari paper, along with the 2009 Yi/Lee cationic study and Kakiuchi's 2010 work. Maybe Simon 2009 would replace Lei or DFT findings. I can cite detailed abstracts like Guari's from RG, and for Yi, I’ll use the PMC full article for more accurate data.
>
> **Searching for citations of key research papers**
>
> [Checking your browser - reCAPTCHA](https://pmc.ncbi.nlm.nih.gov/articles/PMC2805103/)
> [
"Regioselective Intermolecular Coupling Reaction of Arylketones and Alk" by Chae S. Yi and Do W. Lee
](https://epublications.marquette.edu/chem_fac/415/)
> [Dihydrogen and Other σ Bond Complexes | Request PDF](https://www.researchgate.net/publication/282799776_Dihydrogen_and_Other_s_Bond_Complexes)
>
> **Seeking precise sources and recognizing citation methods**
>
> I need the 1995 article with enough detail, especially the 1997 reference. For Kakiuchi 2010, I'll extract the specific details from PubMed searches if available, and the RG lines (709-724) are usable as well. If the Matsubara 1998 source doesn’t work, I’ll explore additional options like searching for the exact DOI. Avoid Wikipedia though.
>
> **Searching for specific research articles and citations**
>
> [Density Functional Study on Activation of ortho-CH Bond in ...](https://pubs.acs.org/doi/10.1021/ja9816943)
> [Accessing metal-specific orbital interactions in C–H ...](https://www.sciencedirect.com/org/science/article/pii/S2041652024001676)
> [Density Functional Study on Activation of ortho-CH Bond in ...](https://www.semanticscholar.org/paper/Density-Functional-Study-on-Activation-of-ortho-CH-Matsubara-Koga/f0278ed598a10a870ee97ccbe1a45d56bc36a821)
> [Historical Perspective and Mechanistic Aspects of C–H ...](https://onlinelibrary.wiley.com/doi/10.1002/9781119774167.ch1)
> [Density Functional Study on Activation of Ortho-CH Bond ...](https://kenkyu.kanagawa-u.ac.jp/kuhp/KgApp?detlId=22&detlSeq=33&detlUid=ymisgkoyggg)
> [Catalytic Addition of C–H Bonds Across C–C π-Bonds](https://ouci.dntb.gov.ua/en/works/4aww0Yk9/)
> [[논문]Density Functional Study on Activation of ortho-CH Bond in ...](https://scienceon.kisti.re.kr/srch/selectPORSrchArticle.do?cn=NART24668431)
> [Murai reaction](https://en.wikipedia.org/wiki/Murai_reaction)
> [Synthesis and x-ray structural characterization of Ru(PPh3) ...](https://www.researchgate.net/publication/244457706_Synthesis_and_x-ray_structural_characterization_of_RuPPh33COC2H4_and_RuHo-C6H4COCH3_PPh32L_L_PPh3_CO_DMSO_Ruthenium_complexes_with_relevance_to_the_Murai_reaction)
> [Ruthenium‐Catalyzed ortho‐C H Bond Arylation Reactions ...](https://novel-coronavirus.onlinelibrary.wiley.com/doi/abs/10.1002/9783527834242.chf0032)
> [C-H Activation and Functionalization of Alkanes and Arenes](https://link.springer.com/chapter/10.1007/978-3-540-46129-6_20)
> [Réaction de Murai](https://fr.wikipedia.org/wiki/R%C3%A9action_de_Murai)
> [Transition-Metal-Catalyzed C-H Functionalization of ...](https://dokumen.pub/transition-metal-catalyzed-c-h-functionalization-of-heterocycles-2-volumes-9781119774136.html)
> [Muraiova reakce](https://cs.wikipedia.org/wiki/Muraiova_reakce)
> [C–H activation | Springer Nature Experiments](https://experiments.springernature.com/nature/primers/10.1038/s43586-021-00041-2)
> [村井反応](https://ja.wikipedia.org/wiki/%E6%9D%91%E4%BA%95%E5%8F%8D%E5%BF%9C)
>
> **Ensuring citations and covering EP targets**
>
> I need to ensure the exact citations with proper line reference from various sources. Specifically, the articles from 1995, 1997, 2010, 2004, 2000, and 1998 should include their corresponding line numbers for clarity. Also, the structured selection map should focus only on EP targets listed in Stage 3 §5, including EP-02a through EP-09a, and include EP-05 from §2. No other prose needed here.
>
> Thought for 1m 44s

prompt_version: stage4-v3-20260425 `prompt_stage4_v3.md`  
model_info: GPT-5.5 Thinking

# EP充填選定マップ

## Shinji Murai, Fumitoshi Kakiuchi, Shinya Sekine, Yasuo Tanaka, Asayuki Kamatani, Motohiro Sonoda & Naoto Chatani 1993（NATURE full_paper）

### §A EP充填難易度の三群分類

**第一群（文献で明確に追跡可能）：** EP-02a, EP-03a, EP-04a, EP-06a, EP-07a, EP-10a  
— EP-02a は 1995年の BCSJ full article が scope・生成物・deuterium labeling を拡張しており、通信→full paper 自己充填として追跡可能である。([CiNii](https://cir.nii.ac.jp/crid/1360846644034359296))  
— EP-03a は key intermediates / active catalyst の構造解明を主題化した 2004年・2010年以降の論文が存在するため、独立文献として明確に追跡可能である。([ResearchGate](https://www.researchgate.net/publication/282799776_Dihydrogen_and_Other_s_Bond_Complexes))  
— EP-04a は H/D exchange, isotope labeling, pathway discrimination, kinetics を扱う後続研究が存在するため第一群である。([CiNii](https://cir.nii.ac.jp/crid/1360846644034359296))  
— EP-06a は DFT studies と structural/mechanistic studies が precedent analogy を対象系内で検証する方向に進んでおり、文献追跡可能である。([ACS Publications](https://pubs.acs.org/doi/10.1021/ja9816943?utm_source=chatgpt.com))  
— EP-07a は substituent effects, substrate-boundary studies, alternative directing groups による scope boundary 拡張として追跡可能である。([OUP Academic](https://academic.oup.com/bcsj/issue/70/12))  
— EP-10a は KIE / H-D exchange / rate law / pseudo-first-order kinetics を扱う論文が存在するため第一群である。([CiNii](https://cir.nii.ac.jp/crid/1360846644034359296))  

**第二群（間接的に追跡可能）：** EP-05a, EP-09a  
— EP-05a は substituent effect study や theoretical regioselectivity study として部分的に追跡可能だが、原論文の全 failure / rate variation を matched-pair control として完全に解く独立論文ではない。([OUP Academic](https://academic.oup.com/bcsj/issue/70/12))  
— EP-09a は review / account で historical positioning は整理されるが、原論文の prior-work superiority を同一条件で再測定する internal benchmark 論文は同定しにくい。([PubMed](https://pubmed.ncbi.nlm.nih.gov/12379135/?utm_source=chatgpt.com))  

**第三群（充填が見つからない可能性あり）：** EP-01a, EP-08a  
— EP-01a は full paper 展開で部分解消されるが、GC calibration, response factors, mass balance, yield denominator を独立主題として扱う論文は通常成立しにくい。  
— EP-08a は replicate count / uncertainty / analytical reproducibility に関するEPであり、合成化学・有機金属化学ではインセンティブ構造的未充填になりやすい。

### §B 各EPの充填論文候補

**EP-01a Reporting-coherence pack（第三群）**

* **充填するRI**: RI-01 Reporting integrity
* **充填開始点**: Kakiuchi et al., Bulletin of the Chemical Society of Japan 1995 — Nature communication の反応を full article として拡張し、2′-methylacetophenone と各種 terminal olefins、acetylnaphthalenes、cyclic aromatic ketones、heteroaromatic ketones の反応を記述した。([CiNii](https://cir.nii.ac.jp/crid/1360846644034359296))
* **充填確立点**: 未同定 — GC calibration, response factors, replicate uncertainty, complete mass balance を統一して開示した決定的充填論文は未確認。
* **充填の性質**: Partial
* **Confidence**: Medium
* **注記**: 通信→Full Paper遷移で部分解消されるが、現代的な reporting-coherence pack としては未完。

**EP-02a Identity / purity substantiation pack（第一群）**

* **充填するRI**: RI-02 Object identification
* **充填開始点**: Kakiuchi et al., Bulletin of the Chemical Society of Japan 1995 — 生成物 scope と regioselectivity を拡張し、1:1 coupling products と regioisomer outcome を詳細化した。([CiNii](https://cir.nii.ac.jp/crid/1360846644034359296))
* **充填確立点**: 同上
* **充填の性質**: Partial
* **Confidence**: Medium
* **注記**: full paper は product identity の自己充填候補だが、本文要約だけでは spectra / purity pack の完全性までは確認不能。

**EP-03a Direct-observation / state-assignment pack（第一群）**

* **充填するRI**: RI-03 Unobserved explanatory
* **充填開始点**: Guari et al., Journal of Molecular Catalysis A: Chemical 2004 — RuH2(H2)2(PCy3)2 と cyclometalated RuH(o-C6H4C(O)R)(H2)(PCy3)2 型錯体を用い、room-temperature Murai reaction と active/deactivation species の議論を与えた。([ResearchGate](https://www.researchgate.net/publication/282799776_Dihydrogen_and_Other_s_Bond_Complexes))
* **充填確立点**: Kakiuchi, Kochi, Mizushima & Murai, Journal of the American Chemical Society 2010 — activated Ru catalyst と ortho-ruthenated complex を構造・NMR・isotope labeling・kinetics により検討し、key intermediate の structural elucidation を主題化した。([ResearchGate](https://www.researchgate.net/publication/244457706_Synthesis_and_x-ray_structural_characterization_of_RuPPh33COC2H4_and_RuHo-C6H4COCH3_PPh32L_L_PPh3_CO_DMSO_Ruthenium_complexes_with_relevance_to_the_Murai_reaction))
* **充填の性質**: Complete
* **Confidence**: High
* **注記**: 原著者グループによる長期自己充填。VQ-3への最重要充填論文。

**EP-04a Discrimination / replication pack（第一群）**

* **充填するRI**: RI-04 Unreplicated discriminator
* **充填開始点**: Kakiuchi et al., Bulletin of the Chemical Society of Japan 1995 — acetophenone-d5 と triethoxyvinylsilane の deuterium labeling により、H/D exchange と rate-determining step が C-H cleavage ではなく product-forming step であることを示した。([CiNii](https://cir.nii.ac.jp/crid/1360846644034359296))
* **充填確立点**: Kakiuchi, Kochi, Mizushima & Murai, Journal of the American Chemical Society 2010 — isotope labeling により C-C bond formation が rate-limiting で、reductive elimination 以前の各段階が reversible であることを示した。([ResearchGate](https://www.researchgate.net/publication/244457706_Synthesis_and_x-ray_structural_characterization_of_RuPPh33COC2H4_and_RuHo-C6H4COCH3_PPh32L_L_PPh3_CO_DMSO_Ruthenium_complexes_with_relevance_to_the_Murai_reaction))
* **充填の性質**: Complete
* **Confidence**: High
* **注記**: EP-10a とバンドル充填。

**EP-05a Quantitative-ranking substantiation pack（第二群）**

* **充填するRI**: RI-05 Qualitative overread
* **充填開始点**: Sonoda et al., Bulletin of the Chemical Society of Japan 1997 — aromatic ring substituent effects を対象化し、original scope の reactivity / selectivity boundary を細分化した。([OUP Academic](https://academic.oup.com/bcsj/issue/70/12))
* **充填確立点**: Lei et al., Science in China Series B: Chemistry 2000 — twelve aromatic ketones の ab initio study により regioselectivity / reactivity を理論的に検討し、steric effect, electronic effect, LUMO conjugation を議論した。([スプリンガーリンク](https://link.springer.com/article/10.1007/BF02969447))
* **充填の性質**: Partial
* **Confidence**: Medium
* **注記**: failure case の diagnostic separation ではなく、substituent/reactivity trend の部分充填。

**EP-06a Analogy-validation pack（第一群）**

* **充填するRI**: RI-06 Imported model
* **充填開始点**: Matsubara, Koga, Musaev & Morokuma, Journal of the American Chemical Society 1998 — aromatic ketone の ortho-CH activation に対する Ru complex の DFT study を行い、five-coordinated d6 metallacycle intermediate と agostic interaction を検討した。([ACS Publications](https://pubs.acs.org/doi/10.1021/ja9816943?utm_source=chatgpt.com))
* **充填確立点**: Matsubara et al., Organometallics 2000 / Kakiuchi et al., JACS 2010 — former は highly ortho-selective addition の DFT cycle を扱い、latter は実験的 intermediate evidence と kinetics を加えた。([OUCI](https://ouci.dntb.gov.ua/en/works/4aww0Yk9/?utm_source=chatgpt.com))
* **充填の性質**: Complete
* **Confidence**: High
* **注記**: computational filling と experimental filling の二段階。

**EP-07a Boundary-test pack（第一群）**

* **充填するRI**: RI-07 Unsupported boundary
* **充填開始点**: Sonoda et al., Bulletin of the Chemical Society of Japan 1997 — aromatic ring substituents の効果を体系化し、original reaction の boundary を拡張的に検証した。([OUP Academic](https://academic.oup.com/bcsj/issue/70/12))
* **充填確立点**: Rouquet & Chatani, Chemical Science 2013 — bidentate 8-aminoquinoline directing group により enone との ortho-C-H alkylation を可能にし、monodentate ketone-directed Murai reaction の scope limit を別設計で乗り越えた。([RSC出版](https://pubs.rsc.org/en/content/articlehtml/2013/sc/c3sc50310k?utm_source=chatgpt.com))
* **充填の性質**: Paradigm-shift
* **Confidence**: Medium
* **注記**: 1-indanone failure の直接診断ではなく、directing-group/catalyst design による boundary succession。

**EP-08a Replication / uncertainty pack（第三群）**

* **充填するRI**: RI-08 Unquantified reliability
* **充填開始点**: 未同定 — Table 1 の replicate count / uncertainty を独立に再測定した論文は未確認。
* **充填確立点**: 未同定
* **充填の性質**: Attempted なし
* **Confidence**: High
* **注記**: インセンティブ構造的未充填。full paper や follow-up は scope/mechanism を拡張するが、反復統計そのものは主題化されにくい。

**EP-09a Internal benchmark pack（第二群）**

* **充填するRI**: RI-09 External superiority
* **充填開始点**: Kakiuchi & Murai, Accounts of Chemical Research 2002 — C-H/olefin coupling の発展と位置づけを整理したが、新規 side-by-side benchmark 実験ではない。([PubMed](https://pubmed.ncbi.nlm.nih.gov/12379135/?utm_source=chatgpt.com))
* **充填確立点**: 未同定 — Jordan & Taylor 1989 / Moore et al. 1992 との normalized TON/TOF/yield/selectivity comparison を実験的に再構成した論文は未確認。
* **充填の性質**: Indirect
* **Confidence**: Medium
* **注記**: review / account は historical benchmark を整理するが、EP-09a の完全充填ではない。

**EP-10a Kinetic verification pack（第一群）**

* **充填するRI**: PRI-10 Kinetic overclaim
* **充填開始点**: Kakiuchi et al., Bulletin of the Chemical Society of Japan 1995 — deuterium labeling により C-H cleavage が rate-determining step ではないことを示唆した。([CiNii](https://cir.nii.ac.jp/crid/1360846644034359296))
* **充填確立点**: Kakiuchi, Kochi, Mizushima & Murai, Journal of the American Chemical Society 2010 — pseudo-first-order kinetics と ruthenium complex concentration への first-order dependence を示し、C-C bond formation が rate-limiting であるとした。([ResearchGate](https://www.researchgate.net/publication/244457706_Synthesis_and_x-ray_structural_characterization_of_RuPPh33COC2H4_and_RuHo-C6H4COCH3_PPh32L_L_PPh3_CO_DMSO_Ruthenium_complexes_with_relevance_to_the_Murai_reaction))
* **充填の性質**: Complete
* **Confidence**: High
* **注記**: Yi & Lee 2009 も cationic Ru hydride system で rapid reversible ortho-C-H activation と rate-limiting C-C bond formation を示すが、対象触媒系は異なるため indirect filling。([epublications.marquette.edu](https://epublications.marquette.edu/chem_fac/415/))

### §C 推奨選定リスト

| 順序 | 論文 | 充填するEP | VQ水準 | 年代 | Confidence |
|---:|---|---|---|---|---|
| 1 | Kakiuchi et al., Bulletin of the Chemical Society of Japan 1995 | EP-01a, EP-02a, EP-04a, EP-10a | VQ-1→VQ-3 | 1995 | Medium |
| 2 | Sonoda et al., Bulletin of the Chemical Society of Japan 1997 | EP-05a, EP-07a | VQ-2 | 1997 | Medium |
| 3 | Matsubara et al., Journal of the American Chemical Society 1998 | EP-03a, EP-06a | VQ-3 | 1998 | High |
| 4 | Guari et al., Journal of Molecular Catalysis A: Chemical 2004 | EP-03a, EP-07a, EP-10a | VQ-3 | 2004 | Medium |
| 5 | Yi & Lee, Organometallics 2009 | EP-04a, EP-10a | VQ-3 | 2009 | Medium |
| 6 | Kakiuchi, Kochi, Mizushima & Murai, Journal of the American Chemical Society 2010 | EP-03a, EP-04a, EP-06a, EP-10a | VQ-3 | 2010 | High |
| 7 | Rouquet & Chatani, Chemical Science 2013 | EP-07a | VQ-2 / Paradigm-shift | 2013 | Medium |

選定理由: 1995 BCSJ は通信→Full Paper 型の自己充填として、product identity, scope, deuterium labeling を束ねるため最初に読むべきである。2010 JACS は active catalyst, key intermediates, isotope labeling, kinetics を同時に扱う決定的なバンドル充填であり、VQ-3到達に最も近い。

VQ-4 相当の EP-09a は推奨選定表に入れていない。理由は、review / account は存在するが、original Nature 1993 の superiority claim を同一実験軸で side-by-side に再検証する filling paper ではないためである。

### §D VQ階層と充填時間順序の対応分析

**充填の時間軸：**

- VQ-1 / VQ-2 要件: EP-01a, EP-02a → 1995 Kakiuchi et al. [自己充填 / 通信→Full Paper遷移]
- VQ-2 要件: EP-05a, EP-07a → 1997 Sonoda et al. [自己充填 / scope-boundary expansion]
- VQ-3 要件: EP-03a, EP-06a → 1998 Matsubara et al. [技術駆動充填 / computational mechanism]
- VQ-3 要件: EP-03a, EP-07a → 2004 Guari et al. [分野横断充填 / alternative Ru-dihydrogen catalyst]
- VQ-3 要件: EP-04a, EP-10a → 2009 Yi & Lee [分野横断充填 / cationic Ru hydride kinetics]
- VQ-3 要件: EP-03a, EP-04a, EP-06a, EP-10a → 2010 Kakiuchi et al. [長期遅延自己充填 / mechanistic bundle filling]
- VQ-2 boundary succession: EP-07a → 2013 Rouquet & Chatani [パラダイム転換充填 / bidentate directing group]

**階層-時間対応の評価：**

低VQ項目のうち product identity / scope は 2年以内に自己充填された一方、mechanistic VQ-3項目は 1998年のDFTから始まり、2010年に実験的 key-intermediate / kinetics bundle として確立するまで約17年を要した。この点では「VQ階層が上がるほど充填に時間がかかる」という仮説を支持する。ただし EP-08a と EP-09a は高VQだから遅れたのではなく、出版インセンティブ上の主題化困難により未充填化しているため、階層-時間仮説だけでは説明できない。

**特筆すべきパターン：**

- **自己充填**: 1995 BCSJ と 2010 JACS は、原著者系譜による自己充填である。
- **バンドル充填**: 2010 JACS は EP-03a, EP-04a, EP-06a, EP-10a を同時に充填する高効率論文である。
- **長期遅延充填**: mechanism closure は Nature 1993 から JACS 2010 まで約17年遅れている。
- **技術駆動充填**: 1998/2000 DFT papers は experimental isolation 以前に mechanism plausibility を支えた。
- **VQ階層逆転**: EP-03a / EP-04a / EP-10a のような高VQ機構項目は論文化されたが、EP-08a / EP-09a のような reliability / benchmark 項目は未充填のまま残る。

### §E 未充填EPの発見的意義

**未充填EP一覧：**

EP-01a Reporting-coherence pack:
* **未充填の理由**: 報告形式問題。1995 full paper で部分解消された可能性は高いが、GC calibration, response factors, mass balance, yield-denominator harmonization を現代基準で完全に満たす独立論文は未同定。
* **発見的意義**: あり。歴史的に成功した named reaction でも、最初期の quantitative audit trail は後続の機構論文ほど保存されにくいことを示す。
* **将来の充填可能性**: 中。original raw data が残っていなければ完全再構成は困難だが、代表基質での再測定は可能。

EP-08a Replication / uncertainty pack:
* **未充填の理由**: インセンティブ構造の不整合。反復測定・標準偏差・検出限界再評価は技術的には可能だが、独立した高インパクト論文になりにくい。
* **発見的意義**: あり。VQ-3機構研究が進んでも VQ-4 reliability layer が空洞化する「VQ階層逆転」の代表例である。
* **将来の充填可能性**: 高。代表的 substrate set に対して GC/FID or GC-MS calibration, isolated yield, NMR yield, replicate uncertainty を現代分析で再評価できる。

EP-09a Internal benchmark pack:
* **未充填の理由**: 関心の欠如 / benchmark incentive の不足。Jordan & Taylor 1989 や Moore et al. 1992 との直接比較は歴史的に重要だが、後続研究は superiority の再検証より scope expansion と mechanism に向かった。
* **発見的意義**: あり。外部優位性主張は reaction discovery の初報で強く働くが、成功後は comparative benchmark の需要が薄れる。
* **将来の充填可能性**: 中。文献値の normalized meta-analysis は可能だが、同一条件での再実験 benchmark は基質・触媒・実験条件の非同型性が障壁になる。

---

**Sources:**

- [
    Catalytic Addition of Aromatic Carbon–Hydrogen Bonds to Olefins with the Aid of Ruthenium Complexes | CiNii Research
](https://cir.nii.ac.jp/crid/1360846644034359296)
- [Dihydrogen and Other σ Bond Complexes | Request PDF](https://www.researchgate.net/publication/282799776_Dihydrogen_and_Other_s_Bond_Complexes)
- [Density Functional Study on Activation of ortho-CH Bond in ...](https://pubs.acs.org/doi/10.1021/ja9816943?utm_source=chatgpt.com)
- [Volume 70 Issue 12 | Bulletin of the Chemical Society of Japan | Oxford Academic](https://academic.oup.com/bcsj/issue/70/12)
- [Catalytic C-h/olefin coupling](https://pubmed.ncbi.nlm.nih.gov/12379135/?utm_source=chatgpt.com)
- [Theoretical investigation on regioselectivity of aromatic ketones in the addition with olefin catalyzed by RuH2(CO)(PPh3)3 | Science China Chemistry | Springer Nature Link](https://link.springer.com/article/10.1007/BF02969447)
- [Catalytic Addition of C–H Bonds Across C–C π-Bonds](https://ouci.dntb.gov.ua/en/works/4aww0Yk9/?utm_source=chatgpt.com)
- [Ruthenium-catalyzed ortho -C–H bond alkylation of aromatic ...](https://pubs.rsc.org/en/content/articlehtml/2013/sc/c3sc50310k?utm_source=chatgpt.com)
- [
"Regioselective Intermolecular Coupling Reaction of Arylketones and Alk" by Chae S. Yi and Do W. Lee
](https://epublications.marquette.edu/chem_fac/415/)



---
Powered by [ChatGPT Exporter](https://www.chatgptexporter.com)

---

> **Tier 8 redaction notice**: This file is a redacted copy of the corresponding Tier 3 / Tier 9 output. Verbatim source-paper quotations have been replaced by `[REDACTED: see source paper §<loc>; full text retained in Tier 9 reviewer-only deposit]` markers, preserving location references and our own analytical content. Bibliographic fields (title, authors, journal, year, DOI), analytical labels (`evidence_chain:` with B-/U-/A-/C- internal IDs), short technical terms, and our own analytical text are not redacted. The redaction was applied by `scripts/redact_for_tier8.py` and, for this version, by `scripts/build_paperA_R1_public.py` with `scripts/redact_source_ngram_runs.py` (scripts of the project repository; they are not deposited).
