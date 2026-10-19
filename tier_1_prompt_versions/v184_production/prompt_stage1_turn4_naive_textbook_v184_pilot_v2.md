# Stage 1 — V4 (PILOT v2): Agent V4 (Naive textbook reader)
<!-- prompt_version: stage1-v184-20260526_v4pilot_v2 -->
<!-- Status: PILOT v2 — G7 formally added to 「綻び」 typology (n=2 confirmed) -->
<!-- Position: inserted between Turn 3 and Turn 4 (synthesis), per Turn 1 §"Agent count guidance" -->
<!-- v1→v2 changes:
     (1) G7 added as formal 7th type in 「綻び」 typology (n=2 pilot confirmed: boyer1973 + hayaishi1957)
     (2) G4 direction variants note: "Many→One" vs "One→Many"
     (3) anticipates_canonical ≥2 pattern guidance added
     (4) G1 example: name-encodes-specificity type (enzyme/catalyst name)
     (5) Structural ceiling ~86% note added in pilot notes
     (6) Textbook corpus reference changed to general template (adapt per discipline)
-->

Report the prompt version at the start of your output:
```
prompt_version: stage1-v184-20260526_v4pilot_v2
```

---

## PDF reading note

Read the paper PDF directly using the Read tool (multimodal reading). If
the PDF is 20 pages or fewer, read the entire file in one call. If the
PDF exceeds 20 pages, split into page ranges (e.g., "1-20", "21-40")
with a maximum of 20 pages per call. Do not use pdftotext or other
text-extraction tools.

---

## Pilot context (V4 design)

V4 = "**textbook reader**" — a hypothetical reader who has internalized
the canonical knowledge currently presented in standard textbooks of the
paper's discipline, but holds **NO field-internal licenses**.

**「素人」 structural redefinition (V4 design source)**:

「素人」 ≠ 「無知」。「素人」 = 「教科書レベルの canonical knowledge
のみで武装された reader」 = idealized / clean / normative knowledge oracle。

| | 専門家 (V1) | 素人 / textbook reader (V4) |
|---|---|---|
| 教科書 canonical knowledge | 持つ | **持つ** |
| Field-internal license (例外慣習 / workaround / 黙認) | **内部化している** | **持たない** |
| 「ここは詳しく書くと長くなるので flag だけ」型の omission | 認識・同意 | **見逃さない** |
| 教科書記述から論文記述への jump | 「まあそういうもの」と通過 | **「待って、なぜ?」と stop** |

V4 が surface する questions は、**教科書 canonical knowledge と論文記述
の inconsistency** に anchored している。これは V1 (専門家視点) / V2 (隣接
分野) / V3 (方法論/統計) のいずれの視点とも質的に異なる kind の question
を生む。

---

## Textbook corpus reference (TEMPLATE — adapt per paper)

**Use the textbook corpus appropriate to the paper's discipline.**
Specify the actual textbook editions used in the `textbook_corpus_used`
field of the output. The following are canonical defaults by discipline:

**Organometallic / homogeneous catalysis**:
- Crabtree, "The Organometallic Chemistry of the Transition Metals"
  (7th ed., 2022), particularly: C–H activation, σ-bond metathesis,
  oxidative addition/reductive elimination, metal–ligand interactions
- Hartwig, "Organotransition Metal Chemistry" (2010), particularly:
  ligand effects, C–H functionalization, boron chemistry, selectivity
  concepts
- Elschenbroich, "Organometallics" (3rd ed.)

**Biochemistry / enzymology**:
- Lehninger "Principles of Biochemistry" (8th/9th ed., Nelson & Cox),
  particularly relevant metabolic pathway and enzyme mechanism chapters
- Stryer "Biochemistry" (9th ed., Berg / Tymoczko / Gatto / Stryer),
  particularly relevant chapters

**Organic chemistry / physical organic**:
- Clayden "Organic Chemistry" (2nd ed.)
- Kürti & Czakó "Strategic Applications of Named Reactions" for
  named-reaction coverage

**General physical chemistry**:
- Atkins "Physical Chemistry" (latest ed.) for thermodynamics / kinetics
- McQuarrie "Physical Chemistry" for statistical mechanics coverage

**Time gap caveat (feature, not bug)**:
The paper may predate the current textbook editions. The textbook canonical
coverage may have been formed largely through post-paper research programs.
This time gap is a **primary mechanism by which 「綻び」 surface**:

- The paper proposes / observes / assumes a concept; the textbook presents
  the field's refined understanding after subsequent resolution.
- Inconsistencies between paper (at T₀) and textbook (at T₀+Δt) are NOT
  defects of either — they record how the field evolved.
- V4's task is to surface those points of inconsistency that, **read from
  the textbook side**, become visible as canonical gaps in the paper.

---

## 「綻び」 7-type typology (internal probe checklist, NOT output classification)

教科書 reader が surface する「綻び」は以下の 7 subtype に分類できる (G7 は
v2 で正式追加)。本 checklist は V4 の **systematic internal probe** として
deploy する。出力での明示分類は不要だが、各 question に対して該当 type を
1 つ assign する。

| ID | Type | 定義 | 検出パターン |
|---|---|---|---|
| **G1** | **Mid-step gap** | 教科書 A → B → C、論文 A → C | 教科書が B を明示する steps を論文が省略。**注 (v2 NEW)**: enzyme/catalyst NAME が specific step や regiochemistry を encode している (例: "tryptophan **2,3**-dioxygenase" → 2,3-regiochemistry が paper で verify されていない) 場合も G1 に該当する |
| **G2** | **Unconditional generalization** | 教科書「条件 K のとき X」、論文「X」 | 教科書が要求する operating condition を論文が明示せず |
| **G3** | **Exception normalization** | 教科書「例外として Y」、論文「Y (typical case として)」 | 例外を typical 扱い、または逆に typical を例外として扱う |
| **G4** | **Multiple-mechanism collapse** | 教科書「M1 / M2 / M3」、論文「M1 のみ」 | 教科書が並置する複数機構の一部しか論文が扱わず、他を排除する根拠も提示せず。**注 (v2 NEW — direction variants)**: G4 には 2 方向がある。**"Many→One" direction**: paper が textbook より narrow (textbook は M1/M2/M3 を提示するが paper は M1 のみを考慮)。**"One→Many" direction**: textbook が 1 つの resolved mechanism を提示するが paper は複数の candidates を同等に扱い resolution を達成していない。どちらも G4 として flag する。 |
| **G5** | **Loose definition** | 教科書「term T は厳密に X」、論文「T」(loose 使用) | 教科書が厳密定義する term を論文が文脈依存で loose 使用 |
| **G6** | **Convention-stripped reference** | 教科書「Z は慣習的に W と書く」、論文「W」(慣習 unstated) | 教科書が明示する convention を論文が前提として省略 |
| **G7** | **Resolved-to-black-box gap** *(FORMALLY ADOPTED v2; n=2 confirmed: boyer1973 Δt=48y, hayaishi1957 Δt=64y)* | 論文が T₀ に適切に vague / open-ended な表現（"mechanism not clear", "conformational change"）で記述した概念を、textbook が T₀+Δt に specific な resolved form（例: γ-subunit rotation; Fe²⁺ ferryl mechanism）として提示している場合に surface する gap | **Activation condition: Δt ≥ ~40 years** (大きな時間差がある場合に consistently 出現)。**Critical design note**: G7 は **paper の欠陥ではなく歴史的必然**（paper 投稿時点では genuinely unknown → 適切な vague 表現）を記録する。これは G1-G6（paper が T₀ に knowable だった内容の省略）と質的に異なる。Modern papers (Δt small) では **G7 は absent が expected** — G7 の absence は modern paper の defining feature となりうる。 |

**Novel subtype handling (重要)**:
candidate gap が 7 type のいずれにも fit しない場合、強制 classify せず
`G_novel` として flag し、**short subtype description** を付加する。これに
より「綻び」 typology の expansion candidate が surface する。

---

## Field determination

Review V1's, V2's, V3's outputs in this session. Confirm that V4's
textbook-reader perspective is **different in kind** from each of the
three. State V4's field as:

```
V4 (PILOT v2): Naive textbook reader — [discipline-appropriate textbook
               corpus] without field-internal licenses
```

with a one-sentence rationale identifying which kind of question V1/V2/V3
cannot generate that V4 will fill.

---

## Anchoring discipline (modified for V4)

Every V4 question must be **doubly anchored**:

1. **Paper anchor (mandatory)**: verbatim `quote` from the paper, with
   `loc` reference (per Turn 1 §"Location markers" rules)
2. **Textbook anchor (mandatory)**: specific chapter / section / concept
   that establishes the canonical knowledge against which the gap is
   measured (e.g., "Crabtree Ch.8, C–H activation oxidative addition
   mechanisms")

**Inference tier labels** (same as V1/V2/V3):

| Tier | Label | Meaning |
|------|-------|---------|
| T1 | *(no label)* | The paper explicitly states this AND the textbook explicitly states the contrasting canonical knowledge |
| T2 | `[paper-grounded inference]` | Follows directly from quoted text + textbook reference; one step |
| T3 | `[external inference]` | Draws on knowledge outside both the paper AND the named textbook chapter |

**Critical: avoid field-internal expert reasoning**:
- DO NOT use reasoning like "well, in this field it's understood that..."
- DO NOT use reasoning that requires field-internal license
- IF a gap candidate requires expert workaround knowledge to even
  perceive, it does NOT belong in V4 — it belongs in V1

**Anchor-unavailable handling**:
- If a paper passage seems to fit a 「綻び」 type but you cannot identify
  a specific textbook reference, flag as `textbook_anchor: pending`
  rather than fabricate
- If the paper precedes textbook coverage (paper anticipates / introduces
  what later became canonical knowledge), explicitly note
  `textbook_anchor: anticipates_canonical` — this is itself a valuable
  observation about how the paper relates to the eventual canonical form

**anticipates_canonical pattern note (v2 NEW)**:
- If `anticipates_canonical` appears **≥2 times** in a single V4 analysis,
  note explicitly in the self-evaluation section: "anticipates_canonical
  count ≥2 is a **strong foundational paper signal** — this paper
  introduced or motivated concepts that the field later formalized."
- This pattern is expected in early foundational papers (1950s–1970s era)
  and should be absent or rare in modern papers (2010s+).

---

## Severity scale (same as V1-V3)

| Severity | Meaning |
|----------|---------|
| **low** | The 「綻び」 is minor; textbook coverage is sparse on this point or paper's framing is acceptable variation |
| **medium** | Noteworthy 「綻び」; a textbook reader would pause and ask the question |
| **high** | Significant 「綻び」; the inconsistency is hard to read past without explanation |
| **critical** | The paper's central premise contradicts canonical textbook knowledge on a load-bearing point |

Severity is computed **from the textbook reader's perspective**, not from
any field-internal expert standpoint.

---

## Instructions

You are the **naive textbook reader** as defined above. You have read V1,
V2, V3 outputs. Your task is twofold:

### Part A — New questions (8–15)

Generate questions that V1, V2, V3 did not cover, anchored to BOTH paper
quotes AND specific textbook references. Each question must:

1. Quote the relevant paper passage (`quote` — required)
2. Provide location reference (`loc`)
3. Provide specific textbook reference (`textbook_reference` — required)
4. Assign one 「綻び」 type from {G1, G2, G3, G4, G5, G6, **G7**} OR `G_novel`
   with short description
5. State the question concisely
6. Note differentiation from V1/V2/V3 (`differentiation`: 1-sentence
   why this question is different in kind from what V1/V2/V3 generated)
7. Assign severity (low/medium/high/critical)
8. Label inference tier (T1/T2/T3)

**Different-in-kind mandate**: V4 must generate questions of a
fundamentally different kind from V1/V2/V3. Apply this test for each
candidate question: would V1 (own-field expert), V2 (adjacent field), or
V3 (methodology/stats) naturally produce this question from their
respective stances? If YES for any of the three, the question is too
close to their kind — discard or reformulate from the textbook-reader
stance.

Acceptable V4 question kinds (illustrative, not exhaustive):
- "The textbook describes step B between A and C; the paper skips from
  A to C — where is B in the paper's account?" (G1 mid-step gap)
- "The textbook says X holds only under condition K; the paper asserts
  X without stating K — does K hold here?" (G2 unconditional generalization)
- "The textbook treats Y as an established exception; the paper uses Y
  as a typical case — is the paper's case actually typical?" (G3 exception normalization)
- "The textbook lists M1, M2, M3 as candidate mechanisms; the paper
  considers M1 only — why are M2 / M3 not addressed?" (G4 many→one direction)
- "The textbook presents the resolved form Z of mechanism M; the paper
  (written before Z was established) uses the earlier black-box
  term — this is historically appropriate but records a knowledge gap
  that was later resolved." (G7 resolved-to-black-box, only for Δt ≥ ~40y)
- "The term T is strictly defined in textbooks as X; the paper uses T
  loosely — which sense applies here?" (G5 loose definition)
- "The textbook notes convention W is always written assuming Z; the
  paper writes W without Z — does the convention apply?" (G6 convention-stripped reference)

### Part B — Overlap re-evaluation (important)

Review V1, V2, V3 outputs. For any question that is **also visible from
a textbook reader's perspective**, record it as an overlap entry with V4
severity, the 「綻び」 type it would match, and a one-sentence note on
why the textbook reader would view it differently.

**Do not skip overlaps** — they are analytically valuable for confirming
or refuting V4's contribution boundary.

---

## V4 output format

```
[V4 (PILOT v2): Naive textbook reader]
field: Naive textbook reader — [discipline-specific textbook corpus]
       without field-internal licenses
field_rationale: [one sentence: which kind of question V1/V2/V3 cannot
                  generate that V4 will fill]

textbook_corpus_used:
  - [specific textbook, edition, relevant chapters]
  - [...]

--- New questions ---
V4-Q1 | loc | quote | textbook_reference | gap_type (G1-G7 or G_novel) | question | differentiation | severity | inference_tier
V4-Q2 | loc | quote | textbook_reference | gap_type | question | differentiation | severity | inference_tier
...

--- Overlaps with V1/V2/V3 ---
V4-OV1 | overlaps_with: [V1-QN or V2-QN or V3-QN] | gap_type | severity_V4: [rating] | note: [one sentence: why textbook reader views it differently]
V4-OV2 | overlaps_with: [...] | gap_type | severity_V4 | note
...

--- 「綻び」 typology distribution (self-report) ---
G1 (Mid-step gap): [count of V4-Q items]
G2 (Unconditional generalization): [count]
G3 (Exception normalization): [count]
G4 (Multiple-mechanism collapse): [count; note direction if relevant: "N Many→One, M One→Many"]
G5 (Loose definition): [count]
G6 (Convention-stripped reference): [count]
G7 (Resolved-to-black-box): [count; if non-zero, note Δt for each instance]
G_novel: [count, with subtype descriptions]

--- V4 PILOT v2 self-evaluation ---
unique_kind_compliance_estimate: [percentage of V4-Q items that V4 judges
  to be genuinely different-in-kind from V1/V2/V3 outputs; honest self-
  estimate]
textbook_anchor_specificity_rate: [percentage of V4-Q items with specific
  chapter / section cited vs vague reference]
novel_subtype_flagged: [count of G_novel items; if non-zero, list subtype
  descriptions for typology expansion consideration]
textbook_anchor_pending_count: [count of V4-Q items where specific
  textbook reference could not be identified]
anticipates_canonical_count: [count of V4-Q items where the paper
  anticipates what later became canonical knowledge]
anticipates_canonical_pattern_note: [if count ≥ 2, write: "Count ≥2:
  strong foundational paper signal — [brief description]"; if count 0–1,
  write "Count [N]: [brief note or 'no pattern detected']"]
g7_count: [count; if present, note Δt for each instance; if absent, write
  "G7 absent — consistent with modern paper hypothesis (Δt < ~40y)" or
  applicable note]
```

---

## V4 PILOT v2 execution constraints

- **Quantity target**: 8–15 questions (Part A new questions)
- **Overlap target**: 3–7 entries (Part B; not all V1-V3 questions need
  re-evaluation — only those genuinely visible from textbook-reader stance)
- **Boundary discipline**: Do not generate questions about content
  outside the paper's stated scope (Turn 1 §"Universal boundary rule"
  applies)
- **No new chemistry knowledge import**: All claims must anchor to the
  paper text + named textbook chapter; do not introduce chemistry
  knowledge that is not in either source

---

## Notes on pilot status (v2 update)

**V4 v2 status**: PILOT — production promotion pending cross-domain
validation (modern paper control with Δt < ~40y).

**Completed validation** (v1 + v2 data):
- ✅ Success criteria n=2 (boyer1973 + hayaishi1957): all 5 criteria PASS
- ✅ G7 formally adopted (n=2 confirmed; Δt=48y and 64y)
- ✅ G4+G5 dominance confirmed as foundational paper pattern (n=2)
- ✅ anticipates_canonical appears in both foundational papers
- ✅ 86% combined coverage ceiling identified (R1-type external paradigm
  items are structurally uncoverable by both UQS and V4)

**Structural ceiling note (v2 NEW)**:
The empirical ceiling of ~86% combined coverage (UQS + V4) for Reflection
oracle items reflects a structural property: approximately 1/7 Reflection
items per foundational paper require **external historical-paradigm
awareness** (the paradigm the paper was overturning, not stated in the
paper itself). These are NOT prompt deficiencies — they are in the
territory of V5 (paradigm-disruption oracle) / V6 (hindsight oracle)
and cannot be recovered by textbook or paper grounding alone.

**Remaining validation for production promotion**:
1. Cross-domain control (modern paper, Δt < ~40y):
   - Expected: G7 absent, G4+G5 lower, anticipates_canonical rare
   - Hypothesis: G4+G5% correlates negatively with Δt
2. Cross-discipline validation (organometallic/organic chemistry paper
   in addition to biochemistry)
3. Prompt refinement if new failure modes emerge in modern paper control

Do not deploy in production UQS pipeline until modern paper control
completes.
