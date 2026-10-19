---
title: Paper A R1 — D1 item-level blind advisor evaluation (pre-registration)
created: 2026-09-29
status: active
audience: paperA
open_questions: true
---

# Pre-registration: D1 item-level blind evaluation

**Status: frozen at this commit (2026-09-29), before any item was drawn.** The author decided: two raters who are
organic chemists; 10 items; paper forms.

## Purpose

Referee 2 point 1 asks for a blind evaluation by subject-matter experts, with inter-rater reliability. We apply the
**Tier 1 advisor protocol that was specified in the submitted paper** (SI-8.1–8.2, six response categories), so that the
evaluation design predates the review.

## Raters

Two organic chemists, neither of whom has seen any UQS output. They are *not* the expert who gave the unstructured SSP
feedback of 2026-06-01 ("Expert 1"), whose feedback is reported separately as a preliminary pilot, so the two sources of
expert evidence are independent. Neither rater sees any UQS output or this pre-registration beyond the items.

**Blinding, naming and relationship to the authors.**
- *Blinding.* Blinding here means three things: the raters do not know which items come from the pipeline and which from
  the single-prompt baseline; they are not told the hypotheses; and they rate independently, without seeing each other's
  ratings.
- *Naming.* The raters are named in the Acknowledgements after the evaluation, with their consent. The main text and the SI
  refer to them only as "Rater 1" and "Rater 2". No rating, comment or quotation is attributed to a named person, and the
  Acknowledgements do not say which name is which rater.
- *Relationship to the authors (disclosed in Methods 7).* The raters are not authors of this paper. Both collaborate with an author on a separate research project.
- *Prior exposure.* Neither rater has seen UQS output. Expert 1, who saw the SSP list in June 2026, is not a rater.
- *Names in the repository.* No rater's or expert's name is written in any repository file. Names appear only in the
  final Acknowledgements.

Draft wording:
- *Methods 7:* "Two experimental chemists who are not authors of this paper, and who collaborate with one of the
  authors on a separate research project, rated the items independently and without knowledge of which items came from
  the pipeline."
- *Acknowledgements:* "We thank [Name 1] ([affiliation]) and [Name 2] ([affiliation]) for evaluating the UQS outputs
  (Methods 7; SI-8)." 

## Items

10 items (decided by the author).
- **Pool.** Pipeline items only; the single-prompt comparison is dropped at 10 items. The items come from the Kumada
  1972 v18.4 reproducibility run 1: its 13 Stage 1 final-taxonomy items (A 2, B 6, C 4, U 1; the `[X] X-n` lines extracted
  by `repro_extract.count_items`) and its 8 Stage 2 D-4 candidates. Run 1 is used so that the selection is not tuned.
- **Draw.** `random.Random(20261001)`: 7 of the 13 Stage 1 items and 3 of the 8 D-4 candidates, drawn in that order. There is
  no replacement: every drawn item is used, even if it overlaps another.
- **Rewriting (SI-8.1 Steps 1–2).** One LLM pass per item (Sonnet 4.6, a fresh `claude -p` process, the item text
  appended to the prompt below, no PDF). It produces a two-sentence Japanese student form: *question*, then *what in the
  paper prompted it*. The prompt, verbatim:

```
あなたは、ある論文を読んだ大学院生が指導教員に持ってくる「質問・気づき」を書き起こす役です。
以下に、論文（Tamao, Sumitani & Kumada, J. Am. Chem. Soc. 1972 の中央の報、Ni–ホスフィン錯体触媒による Grignard 試薬と有機ハロゲン化物のクロスカップリング）についての分析項目を 1 つ示します。
この項目を、次の規則で書き直してください。

1. 2 文で書く。1 文目は学生の質問（「〜ではないでしょうか」「〜はなぜですか」などの問いの形）。2 文目は、論文中のどの記述・データからその質問が出てきたか（頁・表・式・例、または短い引用）。
2. 項目が指している具体的な対象（化合物、反応、表の項目、主張など）と、論文中の根拠の場所は必ず残す。
3. 項目の ID、分類記号（A/B/C/U、D-4 など）、分析用語（SRG、RI、EP、convergence、severity、tier など）、評価語（重要、致命的、価値がある、など）はすべて除く。
4. 項目にない内容を足さない。判断や提案を加えない。
5. 日本語で書く。化合物名・専門用語・引用は英語のままでよい。全体で 150 字程度まで。

出力は書き直した 2 文だけにしてください。

【項目】
```
  - An author checks every rewrite against its source item for preservation only, without judging quality.
- **Order.** Items are shuffled with the same seed, and both raters see the same order.

## Instrument

- **Prompt** (SI-8.1 Step 3, verbatim): "The following is a list of questions and observations that a student brought to you after reading a paper. As an advisor, how would you evaluate each?"
- **Materials (paper).** Each rater receives:
  - a printout of the paper (Kumada 1972, the full JACS page; the middle communication is marked);
  - a one-page instruction sheet in Japanese, with the six SI-8.2 category definitions and their examples;
  - the 10-item form.
- **Per item.**
  - one category, (i)–(vi); a blank is allowed when nothing fits;
  - confidence (high / medium / low);
  - an optional one-line comment.
- **Time.** About 3 minutes per item. Raters are told not to look anything up, as in Expert 1's own framing.

## Analysis (fixed now)

1. Category distribution per rater, and per item type (Stage 1 or D-4).
2. Inter-rater agreement: raw agreement and Cohen's κ on the six categories, and on a collapsed scheme:
   {(i), (ii), (iii)} = worth raising; {(iv), (v)} = not; (vi) = unable.
3. The proportion "worth raising" per rater, with a 95% CI. With 10 items, no significance claim is made.
4. Everything is reported as it comes out. No item is dropped after rating. Free-text comments are reported in summary.

## Interpretation limits (stated in advance)

- n = 2 raters and 10 items. There is no baseline comparison in this evaluation.
- Kumada 1972 only.
- The rewriting pass could improve or degrade an item. The author's preservation check guards against lost content, not
  against improved wording.

## Amendment 1 (2026-10-02) — a third rater and a rater-expertise question

**Made before any rating was seen.** At the time of this commit, three organic chemists have agreed to rate. Two have returned their forms, and the author has not opened them. The third form has not been returned.

**Why.** (a) A third chemist agreed. (b) In accepting, two raters pointed out that organic chemistry is highly subdivided, and they asked whether it mattered that the paper is outside their own speciality. How close a rater's speciality is to the paper may affect their ratings. The original design should have recorded this and did not. This amendment adds the record before the ratings are read.

**Changes.**
1. *Primary analysis unchanged.* Analysis items 1–4 apply to Rater 1 and Rater 2. They are the two raters whose forms had been returned when this amendment was committed. The rule depends only on the order of return, which is known before any rating is seen.
2. *Third rater (secondary).* Rater 3's ratings are reported in full, whatever they show. They enter two secondary analyses: the three pairwise Cohen's κ values and Fleiss' κ across the three raters, on the six categories and on the collapsed scheme. If Rater 3 does not return the form, this is reported, and the primary analysis stands.
3. *Rater expertise (post-rating, descriptive).* After returning their form, each rater answers three questions (`expertise_followup.md`): research field (free text, reported only in coarse form); whether transition-metal-catalysed cross-coupling is within their own research (yes / adjacent / no); and familiarity with Kumada 1972 before this evaluation (had not read / known by name / read or used). Answers are reported per rater, in a form that identifies no one. With three raters, no comparison between expertise groups is made; any pattern is described as such.
4. *No further raters.* Two raters offered to suggest more raters to widen the range of fields. We declined for this evaluation, because adding raters after the design is fixed would invite the reading that raters were added until a result appeared. A wider panel is registered as future work and would need its own pre-registration.

**Text affected.** Methods 7, the Acknowledgements and SI-8.7 say "three raters" (two primary, one secondary). The interpretation limit "n = 2 raters" becomes "n = 2 raters in the primary analysis, plus 1". Rater expertise is a new interpretation limit: the raters are organic chemists, not specialists in Ni-catalysed cross-coupling.

**Addition to Amendment 1 (2026-10-02, same day; still before any rating was seen).** The two raters' concerns pointed in opposite directions. One noted that organometallic chemistry is outside their speciality. The other noted that they are so close to the field that they know too much of its inside story. Being too close is not covered by questions 1–3, so a fourth post-rating question is added: knowledge of the background of this work beyond the published literature (none / some / substantial; for example, a personal connection to the research group, or first-hand accounts of how the work was done or what came after). It is reported coarsely, like the other three. A rater who knows later work or the inside story may judge an item as already answered. This is a direction of bias, not an error, and it is stated as an interpretation limit alongside the out-of-field one. The two concerns are reported as the raters' own pre-rating remarks, without attribution.

## Amendment 2 (2026-10-02) — a fourth rater, a cap, prior exposure and relationships

**Made before any rating was seen.** Two forms have been returned and remain unopened.

**Change of course, stated plainly.** Amendment 1, committed earlier the same day, said that no further raters would be added. A fourth organic chemist has since agreed to rate. We add this rater on the same terms as the third. Neither rater enters the primary analysis, and no rating has been read.

**Changes.**
1. *Labels by order of return.* Rater 1 and Rater 2 are the two raters whose forms had been returned when Amendment 1 was committed. They form the primary analysis, which is unchanged. Rater 3 and Rater 4 are the other two raters, numbered in the order in which their forms are returned. This rule does not depend on any rating.
2. *Secondary analyses.* All six pairwise Cohen's κ values are reported, and Fleiss' κ is computed over the raters who return forms, on the six categories and on the collapsed scheme. Every returned form is reported in full.
3. *Cap.* Four raters is the maximum. If anyone else offers to rate, their ratings are not used in this evaluation.
4. *Prior exposure (checked against the author's records).* In June 2026 the SSP list, which is UQS output, was sent to two chemists. One of them replied, and that reply is the Expert 1 pilot (SI-8.6). The other did not comment on the items. Neither of these two is a rater. The author confirms that none of the four raters received the SSP list or saw any other UQS output.
5. *Relationships (corrects the Raters section).* The Raters section said that both raters collaborate with an author on a separate research project. In fact, three of the four raters are former collaborators of an author on separate projects, including Raters 1 and 2. The fourth was formerly an office neighbour of an author and has not collaborated with them. Methods 7 states the relationship for each rater, without names.
6. *Expertise.* The post-rating questions of Amendment 1 (four questions) apply to all four raters. In accepting, one rater said organometallic chemistry is outside their speciality (they work in catalysis), and one said they know the field's inside story. Both remarks are reported without attribution.

## Amendment 3 (2026-10-05) — anonymity of the expertise answers and the comments

**Made before any post-rating questionnaire was handed out.** All four rating forms had been read and analysed (provisional, `d1_results_20261005.md`) when this amendment was made. It changes only how the expertise answers and the comments are reported, not any rating or analysis.

**Why.** Blinding and naming (Raters section) promise that no rating, comment or quotation is attributed to a named person. Amendment 1 said the expertise answers would be reported per rater. With four raters named in the Acknowledgements, per-rater answers combined with the raters' pre-rating remarks and with the content of the comments would let anyone who knows the four people match answers, comments and ratings to names.

**Changes.**
1. The post-rating answers are reported only as counts over the four raters, never per rater and never linked to R1–R4. The free-text research field is not reported. Amendment 1's "reported per rater" is withdrawn.
2. The questionnaire tells raters that answers are used only in aggregate.
3. Rater comments are reported only as an unattributed summary by theme (`ratings/comments_summary.md`). The verbatim comments are kept in `_private/`, which is neither committed nor deposited, and are removed from `ratings/ratings.csv`. An earlier local commit of `ratings.csv` contained them; no copy has left the project repository.
4. The pre-rating remarks ("outside my field", "knows the inside history") are still reported, unattributed, as Amendment 1 says. They are not linked to any R-number or comment.

**Cost.** Expertise can no longer be related to individual ratings. With four raters no such comparison was planned (Amendment 1), so nothing pre-registered is lost.

## Amendment 4 (2026-10-05) — the post-rating questionnaire is not administered

**Decision of the author, made before the questionnaire was handed to any rater.** The four post-rating questions of Amendment 1 (and their aggregate reporting under Amendment 3) are dropped. No rater received the questionnaire. The only information on the raters' expertise is their own remarks before rating, which are reported unattributed (Amendment 1). The interpretation limit on rater expertise stands: the raters are organic chemists, not specialists in Ni-catalysed cross-coupling, and their closeness to the field differs in both directions.

**Reason.** The questionnaire adds little with four raters, for whom no comparison between expertise groups was planned, and even aggregate answers add to what could be combined with the named Acknowledgements. Asking the raters for more effort was not justified by that gain.


## Record (2026-10-05): naming outcome

Three of the four raters consented to be named in the Acknowledgements; one declined. The Acknowledgements list the three names in alphabetical order, do not say which name is which rater, and mention one further rater without a name. This follows the Naming rule above; no amendment to the design.

**Update to the naming record (2026-10-05, author's decision).** The Acknowledgements do not single out the raters. The three raters who consented are thanked, in alphabetical order, together with the two chemists who commented on the SSP list in June 2026, all for "helpful discussions on the organometallic and synthetic-organic chemistry context". The rater who declined is not mentioned. Reason: a list that named the raters as raters, or the June commentators as commentators, would narrow down who gave which rating or comment. This departs from the draft Acknowledgements wording above ("for evaluating the UQS outputs") in order to keep the Naming rule's purpose.
