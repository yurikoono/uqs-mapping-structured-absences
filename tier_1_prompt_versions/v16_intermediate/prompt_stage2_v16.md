# Stage 2: Interpretation (D-1 through E)
<!-- prompt_version: stage2-v16-20260414 -->
**Language: English for D-1, D-2, D-3; Japanese for D-4 and E**

Report the prompt version at the start of your output:
```
prompt_version: stage2-v16-20260414
```

*Paste the full Stage 1 output (A, B, C, U, META, GAP, TEMPERATURE_SUMMARY)
before running this prompt.*

*If prior papers' Stage 2 analyses are available, paste them after the Stage
1 output. D-4 may reference patterns observed in prior papers. If no prior
analyses are available, proceed with this paper's Stage 1 output alone.*

---

## Output discipline

Produce only the structured fields listed in the Output format section below.
Do not add explanatory prose, offer follow-up questions, suggest next steps,
or append any text outside the specified fields. The output ends with the
`inference_time_sec` field.

---

## Anchoring discipline (carried forward from Stage 1)

The same three-tier distinction applies here:

| Tier | Label | Meaning |
|------|-------|---------|
| **T1** | *(no label)* | Directly stated in the paper text |
| **T2** | `[paper-grounded inference]` | Follows directly from the text; one step only |
| **T3** | `[external inference]` | Draws on knowledge outside the paper |

**Additional rules for Stage 2:**

- **Novelty claims (D-1):** Report what the paper claims as novel. Do not
  independently assess whether the claim is accurate against the literature
  — that requires external verification. If the paper's novelty claim
  depends on a literature comparison not supported by the paper's own cited
  evidence, flag it with
  `[paper-grounded inference: comparison asserted, not experimentally verified]`.

- **Catalyst identity precision:** When the paper names a specific complex
  as a representative catalyst within a class (e.g., one bidentate
  diphosphine complex among several tested), describe it as representative
  of the class, not as uniquely enabling. Privileging one complex above its
  reported class requires explicit textual support.

- **Scope of the propositional form (E):** The `confirmed_english_propositional`
  must encode the paper's stated substrate scope and nothing else. Apply
  these rules in order before writing the proposition:
  1. Use the paper's exact conjunction (or / and) as printed.
  2. Do not add any modifiers, result clauses, or feature phrases. The
     proposition ends after naming the substrate scope — no "to yield X",
     no "suppressing Y", no "with high Z".
  3. Check: could the proposition be falsified by a substrate-scope
     counterexample alone (not by a yield or selectivity measurement)?
     If no, remove the offending phrase and recheck.
  - **Bad examples** — do not produce any of these:
    - "…high-yield cross-coupling…" → "high-yield" is a feature, not scope
    - "…aryl and vinyl halides" → use "or" if the paper prints "or"
    - "…suppressing homocoupling products" → result phrase, not scope
    - "…to yield coupled products" → result clause, not scope
  - **Good example:** "Nickel-phosphine complexes catalyze selective
    cross-coupling of Grignard reagents with vinyl or aryl halides."

  **Mechanism papers:** For papers whose S0-1 core_claim describes a
  mechanistic finding (a pathway re-assignment, rate-determining step
  identification, or mechanistic distinction) rather than a new synthetic
  transformation, the confirmed_english_propositional describes the
  transformation studied — not the mechanistic finding itself. The
  proposition must still end after naming the substrate scope (no mechanism
  clause). Example:
    Correct:   "Palladium complexes catalyze copper-free Heck–Cassar–
                Sonogashira cross-coupling of terminal alkynes with aryl
                halides or triflates."
    Incorrect: "...via direct alkyne coordination rather than Pd(II)–Pd(II)
                transmetalation." [mechanism clause — prohibited]
  The mechanistic finding belongs in confirmed_english_question only.

- **Scope anchor rule:** The substrate scope terms in
  `confirmed_english_propositional` must be anchored to the **paper's own
  stated scope** (BIB-1 title and S0-1 core_claim), NOT to the actual
  coverage detected by Stage 1 agents. Stage 1 agents may correctly observe
  that the paper's data covers only chlorides, but if the paper's title says
  "organic halides" and S0-1 says "vinyl or aryl halides," the propositional
  must use "halides" (or "vinyl or aryl halides"), not "chlorides."
  The narrower actual scope is properly recorded as a D-4 candidate
  (the gap between stated and demonstrated scope), not in the propositional.
  - **Example of the error this rule prevents:**
    Title says "organic halides" → V3 notes "only chlorides tested" →
    propositional incorrectly narrows to "chlorides" → WRONG.
    Correct: propositional uses "halides" per title; D-4 records the
    gap between stated and demonstrated scope.

- **scope_type determination (E):** Assign scope_type based on the
  `confirmed_english_question` alone — independently of the broad
  transformations explored in the Japanese section of E. Ask: does this
  specific question, as written, require stepping outside chemistry to
  answer? If yes → beyond_chemistry. Does it ask for a general principle
  or framework within chemistry? If yes → framework_question. Does it ask
  for a specific tool, reagent, or condition? If yes → tool_question.
  Do not let the choice of "broadest transformation" in the Japanese
  section inflate the scope_type of the English question.

  **Disambiguation criteria for tool_question vs. framework_question:**
  Before assigning `tool_question`, check: does the
  `confirmed_english_question` ask *whether a specific tool, catalyst,
  or reagent enables a particular reaction* (→ tool_question), or does it
  ask *what boundary conditions, design principles, or governing factors
  determine reactivity or selectivity* (→ framework_question)? A question
  about catalyst design is `tool_question` only if the answer would be a
  specific reagent, condition, or protocol — not a general design
  principle or structure-activity relationship.

- **holy_grail_narrative (D-3):** Classify as "yes" only if the paper itself
  uses mythologising or quest-framing language (e.g., "long-sought",
  "elusive goal", "dream reaction", "holy grail"). Framing a known
  problem as unsolved and then presenting a solution is **not** sufficient
  for a "yes" classification — that is normal scientific rhetoric. Require
  direct textual evidence of aspirational/quest language.

- **Suppressed-reading guard (D-2, D-3, D-4):** Identifying a footnote or
  syntactic move as evidence of *suppression* requires that the paper shows
  (a) awareness of the tension and (b) a textual move away from it. The
  co-occurrence of an anomalous result and a utility reframe is suggestive
  but not conclusive. When the paper also acknowledges the anomaly directly
  elsewhere (e.g., in a "further studies are required" sentence), classify
  as T2 reframing rather than suppression.

- **Competitive and institutional narratives (D-2, D-3):** Statements about
  field dynamics, institutional motives, or publication culture that go
  beyond the paper's own text must be labeled `[external inference]` and
  kept to one sentence maximum. Do not construct narratives about group
  prestige, national standing, or competitive urgency that are not supported
  by the paper itself. The existence of a concurrent submission (Note Added
  in Proof) establishes priority-sensitive context; the strength or urgency
  of competition cannot be further characterized from the paper alone.

- **T3 elaboration limit:** A T3 claim must be stated in one sentence and
  must not be elaborated into a narrative, even if labeled. If more than one
  sentence is needed to make a T3 point, that is a signal the claim exceeds
  what the paper supports.

- **D-4 grounded_in — item_id rule:** Each candidate must carry a
  `grounded_in` field listing specific Stage 1 item_ids that actually
  appear in the Stage 1 output. **Use only the final A/B/C/U item_ids
  assigned in Turn 4** (e.g., A-1, B-3, C-2, U-1). **Do not reference
  turn-level question IDs** (V1-Qx, V2-Qx, V3-Qx) — these are
  intermediate labels that are superseded by Turn 4's classification.
  If a D-4 candidate draws on a question that was not classified into
  A/B/C/U (e.g., it was subsumed into another item's note), reference
  the A/B/C/U item that absorbed it.
  Candidates with no textual anchor
  (`grounded_in: none (retrospective)`) should be rare and clearly separated
  under the heading "questions_that_cannot_be_asked."

---

**[D-1. Declared motivation]** *(English)*

What does the paper explicitly state as its purpose and contribution?
Identify:
- The specific claims of novelty, using the paper's own language
- The performance criteria by which the authors measure success — report
  only criteria the paper itself invokes
- Whether the novelty claims are structured in layers such that no single
  refutation can collapse all claims simultaneously

For each claim, note whether it is **directly stated (T1)** or requires one
reasoning step from the text **(T2)**. Do not import external chemical
knowledge to strengthen or qualify claims.

---

**[D-2. Inferred motivation]** *(English)*

What motivations can be read from the paper's tone, emphasis, and citation
patterns — beyond what is explicitly stated? Address each of the following.
**Label each claim T2 or T3 as appropriate. T3 claims must be one sentence
maximum and must not be elaborated.**

- *Competitive positioning*: How does the paper position itself against named
  prior work? State whether the comparison is experimentally verified within
  the paper or asserted.
- *Concurrent submissions*: If the paper contains a "Note Added in Proof"
  or equivalent acknowledgment of a concurrent or competing submission,
  address the following as a mandatory sub-item: (a) does the paper
  establish any experimental or conceptual distinction between its system
  and the concurrent work? (b) If no distinction is drawn, note this as a
  gap in competitive positioning and assess whether it affects the paper's
  novelty claims (`affects_novelty_claims: yes/no/indeterminate + one
  sentence`). If no Note Added in Proof exists, write "not applicable."
- *Timing pressure*: Does the pattern of deferrals in A suggest urgency?
  Anchor to specific A-items; do not assert the degree of urgency beyond
  what the text supports.
- *Format exploitation*: Does the paper appear to use its publication format
  to compress weaknesses out of view? Anchor to specific B-items.
- *Audience targeting*: What does the paper's vocabulary and example
  selection suggest about its intended audience? Anchor to the text.
- *Institutional visibility*: `[external inference — one sentence maximum]`

---

**[D-3. Institutional motivation]** *(English)*

What competitive pressures, field trends, or publication conventions appear
to have shaped the paper's design and framing? Consider:
- Journal format and its constraints on reporting completeness — anchor to
  specific B-items
- State of the subfield at the time of publication — `[external inference]`
  if not derivable from the paper's own citations
- What the paper's own framing implies about what needed to be demonstrated
  to be taken seriously
- Whether the paper's framing invokes a "holy grail" narrative — requires
  direct textual evidence of aspirational or quest language in the paper
  itself (see anchoring rule above); classify as "no" if the paper uses
  only standard problem-solution framing

**Do not describe the paper as "entering a race" or characterize competitive
urgency with intensity modifiers (e.g., "intense," "high") unless the paper
itself uses such language.** Describe only what the paper's citation pattern
and framing imply.

**Commercialization potential:**
If the paper explicitly mentions commercial, practical, or industrial
context (cost, scale, availability, waste, regulatory), record these as
T1 or T2 entries under `commercialization_potential`. If the paper does not
mention any commercial context, write "not stated in paper." Do not import
external market, patent, or regulatory analysis — such information belongs
outside the paper-anchored analysis.

---

**[D-4. 問われていない動機]** *(日本語)*

Stage 1のA・B・C・U・METAで記録された観察を素材として、この論文が答えようとしていないにもかかわらず本来問われるべきだった動機・問いを記述してください。

**cross_field_temperatureの活用：**
Stage 1のTEMPERATURE_SUMMARYを参照し、以下の優先順位で候補を探索してください。
1. **high_convergence_high_gap項目**を最優先で検討する。これらは「全エージェントが指摘したが深刻度評価が分裂した」項目であり、分野の暗黙の合意が構造的に隠しているものを示す最も強い信号である。
2. **low_convergence_high_gap項目**も検討する。特定分野の基本前提に抵触するcritical評価を受けた項目は、その分野の視点からのみ見える構造的盲点を示す。
3. **U項目**（A/B/Cに分類不能だが重要と判断された質問）をD-4の探索空間に含める。

**フォールバック規則：** high_convergence_high_gap が空の場合（全ての高収束
項目がgap=none/lowの場合）、以下の順序で優先候補を選定すること：
(a) low_convergence_high_gap のcritical評価項目を最優先とする
(b) high_convergence_low_gap のうちconvergence=3/3の項目を次に検討する
(c) same_root_groupsに属し、グループ全体として最多のA/B項目を含むものを検討する
この場合、D-4出力の冒頭に「high_convergence_high_gap: none — フォールバック
規則を適用」と記載すること。

**same_root_groupsの活用：**
Stage 1 METAのsame_root_groupsを参照し、同一の根を持つ質問群が存在する場合、
その群を**一つのD-4候補として統合**して記述してください。個別の質問をバラバラに
候補化するのではなく、共通する根（例：「定量的実験検証の体系的不在」）を
候補の核として記述し、個別の質問（例：TON不在、マスバランス不在、再現性不在）
を下位要素として列挙する形式にしてください。

**テキスト根拠の要件：**
各候補には必ず以下を付記してください。各フィールドは**独立した行**に
記載すること（1行に連結しない）。
```
grounded_in: [Turn 4で付与されたA/B/C/U item_idのリスト。
              V1-Qx, V2-Qx等のターンレベルIDは使用禁止。
              Stage 1出力に実際に存在するA/B/C/U idのみ使用。U項目のidも使用可]
key_quote: [根拠となる論文メインテキストの一文。Supporting Information
            (ESI/SI) の記述は使用不可。メインテキストに直接の根拠が存在
            しない場合は、最も近い文脈を提供するメインテキストの一文を
            使用し、T2またはT3とラベルを付ける]
temperature_note: [該当する場合：この候補がTEMPERATURE_SUMMARYのどの項目に由来するか]
same_root_group: [該当する場合：METAのどのsame_root_groupに属するか]
```
**出力形式の厳守：** 上記4フィールドは必ず改行で区切ること。
`grounded_in: B-1, B-2 key_quote: "..."` のように1行に連結する形式は
downstreamパースで失敗するため禁止。
論文テキストに直接の根拠がない場合は、以下のように区別して記載してください：
- `grounded_in: [T2: item_id]` — Stage 1項目から一歩の推論で到達できる
- `grounded_in: none (retrospective)` — 論文テキストからは原理的に導けない遡及的観察

`grounded_in: none (retrospective)` の候補は最小限にとどめ、
「問い得ない問い」として独立項目に集約すること。

**重複排除（必須）：**
各候補を確定する前に、以下の重複チェックを行うこと。
- 同じkey_quoteを参照している候補は統合して1つにまとめる。
- 実質的に同一の問いは、最もkey_quoteが明確な候補1つに収束させ、
  他の側面はそのnote欄に1文で追記する。
- 収束後に8候補を超える場合は、key_quoteとgrounded_inが最も明確な
  上位8候補に絞り込むこと。

**出発点となる視点（これ以外の観察も歓迎）：**
- 触媒・試薬が反応の中で何を「消費」しているのか（失活・回収・再利用の問題）
- 「高選択性」の反対側——検出されなかったものの存在可能性
- 反応しない基質・条件の体系的な不在
- 具体的な合成標的との接続の不在
- 金属・配位子・溶媒選択の背後にある原理的根拠
- この反応が何のための手段であるかという目的論的問い
- 熱力学的フレームの不在：選択性・収率・条件が「速度論的制御か熱力学的駆動か」という問いと独立に提示されていないか。これはメカニズム考察（A類項目）とは独立した問いとして記録すること。
- 否定的証拠の分析的根拠：論文が「検出されず」「観測されず」という
  結果を肯定的な機構的証拠として用いている場合、その検出下限・検出
  条件が主テキストに記載されているかを必ず確認すること。
  「検出されない = 存在しない」と「検出されない = 検出感度以下」を
  区別するために必要な実験的根拠が欠けている場合は、D-4候補として
  記録すること。（B-itemフラグ "negative result as evidence" が付いた
  B項目は特に注意して確認すること。）

**必ず独立した項目として記載すること：**
- **問い得ない問い**：論文テキストから原理的に答えられない問い（制度的条件、資金源、著者の内心、偶発的な知識背景など）。`grounded_in: none (retrospective)` として明示し、「問われるべき」ではなく「問い得ない」種類の問いとして区別すること。

確定させる必要はありません。「〜かもしれない」「〜とも読める」のまま記述してください。ただし論文テキストから離れた推測が広がるときは、その都度 `[T3]` と記し、簡潔に止めてください（一文以内）。

**最後に記載すること（優先順位の構造）：**
これらの候補を横断して、「何かを達成するために別の何かが意図的に後回しにされた」という優先順位の構造が見えるなら、その構造を記述してください。ただし「意図的」という断定は避け、「〜という構造として読める」という形式を維持してください。どのA・B項目がその構造の根拠になるかを明示してください。
特に以下の「ピボット構造」を探索すること：
- 論文の中心的主張を成立させるために、ある実験的説明が「今後の課題」
  として外に置かれている場合（A項目がB項目の説明を引き受けることを
  回避している場合）、そのAとBのペアをピボット項目として明示する。
- 複数のB項目の定量的根拠が共通して省略されており（same_root_group）、
  その省略なしには主張の定量的信頼性が成立しない場合、そのSRGを
  構造の中核として明示する。
ピボット項目のitem_idを「A-n ↔ B-m（ピボット）」の形式で明示すること。

---

**[E. 射程の問い]** *(日本語で候補を出し、英語で二形式に確定する)*

この論文が化学の文脈で答えた問いの形式を、まず抽象化してください。

**付記すること：**
```
derived_from: [根拠となるD-4候補番号またはA/B/C/U item_id]
anchoring_note: [この抽象化がT1/T2/T3のどの層に属するかを一文で示す]
```

次に、その形式が別の文脈でどのような問いに変形されるかを複数挙げてください。変形先の文脈は自由です。各変形について：
- どのような問いに変形されるかを日本語で記述する
- 「同じ構造の別の現れ」なのか「比喩的な類似」なのかを自然に示す

最も射程が広いと感じる変形を選んだ理由を日本語で記述した上で、以下の二形式を英語で生成してください。

**confirmed_english_propositional の制約（再掲 + scope anchor rule）：**
- 単文、最大20語、従属節なし
- 化学的文脈で有意味な語を含む（embedding比較に使用）
- 論文が実際に示したことのみ（遡及的歴史化を含めない）
- **stated substrate scopeを反映し、featureを追加しない。
  scope語はBIB-1（タイトル）とS0-1（core claim）に準拠すること。
  Stage 1エージェントが検出した実際のカバレッジの狭さ（例：「実際には
  chlorideのみ」）はD-4候補として記録するのが適切な場所であり、
  E節のpropositionalに反映させてはならない。**
- 論文テキストの接続詞（or / and）をそのまま使う
- 結果節（"to yield X"）を付加しない
- **悪い例（生成禁止）：**
  - "…high-yield cross-coupling…" — featureの混入
  - "…aryl and vinyl halides" — 論文が"or"なら"and"は不可
  - "…to yield coupled products" — 結果節の付加
  - "…suppressing homocoupling…" — featureの付加
  - "…vinyl or aryl chlorides" — エージェントが検出した実質scopeへの縮小

**confirmed_english_question の制約：**
- 論文が実際に取り組んだ問いを英語で問い形式にしたもの
- E節の日本語で選んだ「最も射程が広い変形」ではなく、
  論文の実際の研究問題に忠実な問いを書く
- scope_typeはこのquestionに基づいて独立に判定する
  （日本語の変形候補の広さに引きずられないこと）

```
confirmed_english_propositional: "..."
confirmed_english_question: "..."
scope_type: "beyond_chemistry / tool_question / framework_question"
```

**REQUIRED OUTPUT — do not omit:**

```confirmed_english
confirmed_english_propositional: "..."
confirmed_english_question: "..."
scope_type: "..."
```

---

**Output format**

```
prompt_version: stage2-v16-20260414
model_info: <model name and version as reported by the system, or "not available">

[D-1] declared_motivation | novelty_claims (T1/T2 labeled) | success_criteria | layered_structure (yes/no + brief explanation)

[D-2] competitive_positioning (verified/asserted) | concurrent_submissions (distinction drawn? affects_novelty_claims?) | timing_pressure (anchored to A-items) | format_exploitation (anchored to B-items) | audience_targeting | institutional_visibility ([external inference], one sentence max)

[D-3] journal_constraint (anchored to B-items) | field_competition_state ([external inference] if not from paper's citations) | entry_criteria (paper-implied only) | holy_grail_narrative (yes/no + direct textual evidence required for "yes") | commercialization_potential (T1/T2 from paper text only, or "not stated in paper")

[D-4] （日本語テキスト）
      candidates: [各候補、grounded_in（A/B/C/U item_idのみ、V-Q番号禁止）
                   + key_quote + temperature_note + same_root_group付き、
                   重複排除済み、上限8]
      questions_that_cannot_be_asked: [grounded_in: none (retrospective)の項目を集約]
      priority_structure: [構造記述、「意図的」断定を避ける、根拠A/B項目を明示、
                           ピボット項目を「A-n ↔ B-m（ピボット）」形式で明示]

[E]   derived_from: [item_ids]
      anchoring_note: [T1/T2/T3の所属]
      （日本語：変形の記述 + 選択理由）

confirmed_english
confirmed_english_propositional: "..."
confirmed_english_question: "..."
scope_type: "..."

inference_time_sec: <wall-clock seconds if injected by the calling environment;
                     otherwise "not available — inject externally">
```
