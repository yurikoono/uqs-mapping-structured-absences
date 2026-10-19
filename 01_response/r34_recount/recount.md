# R3-4 / B6: recount of the Results Part 4 refinement-set sentence

Date: 2026-10-05. Script: `recount.py` (read-only; it writes `recount.csv`). Re-run from the repo root with
`python3 manuscript_A/DigitalDiscovery_R1/01_response/r34_recount/recount.py`.

## 1. The sentence and what it refers to

`manuscript_A/sections/9_manuscript_en.md:305` (Results Part 4, the internal-robustness paragraph):

> The ten-paper Heck-reaction refinement set (five evidence-architecture categories; v17; SI-11.17) produced
> structurally coherent outputs across all categories, yielding 7–8 EP types and 6–7 SRGs per paper (single-run
> counts); five EP types (EP-01a, EP-03a, EP-06a, EP-07a, EP-08a) recur across all sampled categories.

Referent: the ten papers of SI-11.17 (HOM-1/2, HET-1/2, COMP-1/2, APP-1/2, SCR-1/2 = `papers/test/{hom1,…,scr2}`).
The development set (Kumada, Murai) is not part of this sentence. "Sampled categories" = the five SI-11.17 categories,
two papers each.

Primary files: each folder has **two** Stage 3 records on the same v17 S0–S2 run, and both are in the R1 reviewer
deposit (`zenodo_deposit_paperA_reviewer_R1_20260928/tier_3_stage_outputs/test_set/`, byte-identical to `papers/test/`):

| file | Stage 3 prompt tag | model_info (verbatim, self-reported) |
|---|---|---|
| `{id}_v17_sonnet_s3.md` | `stage3-v1-20260402` | `claude-sonnet-4-6` for 9 papers; **APP-2: `claude-sonnet-4-5 (claude-sonnet-4-5-20251101)`** |
| `{id}_v17_sonnet_s3v2.md` | `stage3-v2-20260416` | `claude-sonnet-4-6` for all 10 |

The manuscript does not say which Stage 3 version the counts come from, so both are counted. The SRG ranges and EP
ranges come out the same for both versions (below). Side finding: the APP-2 Stage 3 v1 record names Sonnet 4.5 in its
`model_info`, but the filename carries the bare `_sonnet_` tag, which by convention means Sonnet 4.6. The date suffix
`20251101` does not look like a real model ID, so this may be a self-report error. Either way, the Stage 3 v2 set is the
clean one to cite.

## 2. Counting rule

* **Scope.** Only Stage 3 §2 ("SRG / CLA → RI / ER / EP Crosswalk"), from that heading to the `### §3` heading.
* **SRG.** A bold block heading starting `**SRG-<n>` inside §2. n_SRG = number of distinct `<n>`. CLA blocks
  (`**CLA…`) are counted separately. The "SRG外：CLA" header is not a block. APP-1 s3v2 has that header but registers no
  CLA ("CLA 登録しない"), so it has 0 CLAs.
* **EP assigned.** Every `EP-<nn><letter>` token in the `* **EP**:` field of an SRG or CLA block, including wrapped
  continuation lines. In APP-2 s3 and HOM-1 s3, the second EP sits on the continuation line. A second-listed, auxiliary
  ("RI-05 補助") or provisional ("EP-10a（暫定）") pack counts as assigned.
* **Headline n_EP = EPs assigned to SRG or CLA blocks** (`n_EP_all`). Two variants are reported for sensitivity:
  `n_EP_SRG` (SRG blocks only) and "anywhere" (any EP token in the file). "Anywhere" adds EPs that appear only in §5
  (shortest-reinforcement route) or §6 (dictionary notes). These are recommendations or mentions, not assignments: for
  example, COMP-1 s3 §5 item 6 "EP-08a", and HET-2 s3v2 §5 item 4 "EP-07a".
* **Hand check.** Done against the §2 text for COMP-1 s3 (6 EPs = {01,03,04,05,07,09}; 5 assigned to SRGs), APP-1 s3v2
  (6 EPs, 0 CLA), HOM-2 s3v2 (8 SRGs; 7 EPs, with EP-07a coming only from CLA-2), HET-2 (5 SRGs in both versions) and
  APP-2 s3 (EP-06a on a continuation line). Each matched the script.

## 3. Per-paper table (Stage 3 v2 = s3v2; Stage 3 v1 in brackets where it differs)

| paper | cat | n_SRG | n_CLA | n_EP (SRG+CLA) | EP assigned (s3v2) |
|---|---|---|---|---|---|
| hom1 | HOM | 7 | 1 | 8 [7] | 01a 03a 04a 05a 06a 07a 08a 10a |
| hom2 | HOM | 8 | 3 [2] | 7 [8] | 01a 03a 04a 05a 07a 08a 09a |
| het1 | HET | 6 | 3 [2] | 8 | 01a 03a 04a 05a 06a 07a 08a 09a |
| het2 | HET | 5 | 2 | 7 | 01a 03a 04a 05a 06a 08a 09a |
| comp1 | COMP | 6 | 2 | 7 [6] | 01a 03a 04a 05a 06a 07a 09a |
| comp2 | COMP | 5 | 3 | 7 | 01a 03a 04a 05a 07a 08a 09a |
| app1 | APP | 6 | 0 [1] | 6 [8] | 01a 03a 04a 05a 06a 08a |
| app2 | APP | 6 | 2 [1] | 8 [7] | 01a 03a 04a 05a 06a 07a 08a 09a |
| scr1 | SCR | 6 | 1 | 7 [8] | 01a 03a 04a 06a 07a 08a 09a |
| scr2 | SCR | 6 | 1 | 7 [8] | 01a 02a 03a 04a 06a 07a 08a |

The per-paper EP lists for v1 are in `recount.csv`.

Ranges (the same for both Stage 3 versions):

| quantity | Stage 3 v2 | Stage 3 v1 |
|---|---|---|
| n_SRG | **5–8** (5,5,6,6,6,6,6,6,7,8) | **5–8** (same SRGs) |
| n_EP, SRG+CLA (headline) | **6–8** (6,7,7,7,7,7,7,8,8,8) | **6–8** (6,7,7,7,7,8,8,8,8,8) |
| n_EP, SRG only | 5–8 | 5–8 |
| n_EP, anywhere in file | 7–8 | 7–9 |

Recurrence of EPs, using the headline rule (SRG+CLA):

| reading | Stage 3 v2 | Stage 3 v1 |
|---|---|---|
| EP in ≥1 paper of every category | 01a 03a 04a 06a 07a 08a 09a (7 EPs) | 01a 03a 04a 05a 06a 07a 08a 09a (8 EPs) |
| EP in every one of the 10 papers | 01a 03a 04a | 01a 03a 04a 07a |

How often each of the manuscript's five EPs occurs (s3v2 / s3 v1): EP-01a 10/10 / 10/10; EP-03a 10/10 / 10/10;
**EP-06a 8/10** (absent in HOM-2 and COMP-2) / 9/10 (absent in COMP-1); **EP-07a 8/10** (absent in HET-2 and APP-1) /
10/10; **EP-08a 9/10** (absent in COMP-1) / 9/10 (absent in COMP-1). Under the SRG-only rule in v1, EP-07a is absent
from both HET papers, so it does not recur in every category.

## 4. Verdict on each part of the sentence

| part | holds? | basis |
|---|---|---|
| "7–8 EP types per paper" | **No.** The assigned count is 6–8 under both Stage 3 versions: COMP-1 (v1) and APP-1 (v2) have 6. | 7–8 is obtained only by counting every EP token anywhere in the s3v2 file, including §5 recommendations, which is not an assignment |
| "6–7 SRGs per paper" | **No.** It is 5–8 under both versions: HET-2 and COMP-2 have 5, HOM-2 has 8. Only 6 of the 10 papers fall in 6–7. | §2 SRG headings |
| "five EP types … recur across all sampled categories" | **True only in a weak sense, and the list is misleading.** Under the weak reading (each EP occurs in at least one paper per category), all five do recur, but so do EP-04a and EP-09a (and EP-05a in v1). The set of five is therefore not the set of recurrent types. Under the strict reading (each EP in every paper), the claim fails: EP-06a, EP-07a and EP-08a are each missing from one or two papers. EP-04a is assigned in all ten papers in both versions but is left off the list. | §3 |

The source of the original numbers could not be found. The only earlier trace is
`improvements/paperA_absolute_count_sweep_20260721.md` #4, which added "(single-run counts)" to the existing figures
without recounting them. One observation, which may be coincidence: under the loose "anywhere in file" rule with Stage 3
v1, the EPs present in every paper are {01a, 03a, 04a, 07a, 08a}. That is five types, but with EP-04a in place of EP-06a.

## 5. Proposed corrected sentence (EN)

> The ten-paper Heck-reaction refinement set (five evidence-architecture categories; v17 Stages 0–2, Stage 3 v2;
> SI-11.17) produced structurally coherent outputs across all categories, yielding 5–8 SRGs and 6–8 assigned EP types
> per paper (single-run counts); EP-01a, EP-03a and EP-04a are assigned in all ten papers, and seven of the ten
> dictionary types recur in at least one paper of every category.

Notes: the ranges and the all-ten-papers set {01a, 03a, 04a} hold under Stage 3 v1 as well (v1 adds EP-07a to the
all-papers set and gives 8 category-recurrent types). The sentence therefore stays true whichever version a reader opens.
Naming "Stage 3 v2" pins the version. If the shorter form is preferred: "…yielding 5–8 SRGs and 6–8 EP types per paper
(single-run counts); EP-01a, EP-03a and EP-04a are assigned in every paper."

JA (for the 48-h sync; same content):

> 10 報の Heck 反応精緻化セット（5 つの証拠アーキテクチャ・カテゴリー；Stage 0–2 は v17、Stage 3 は v2；SI-11.17）は、
> 全カテゴリーにわたって構造的に整合した出力を生成し、論文あたり 5–8 の SRG と 6–8 種類の割り当て済み EP タイプを得た
> （いずれも single-run の計数である）。EP-01a、EP-03a、EP-04a は 10 報すべてで割り当てられ、辞書の 10 タイプのうち
> 7 つは全カテゴリーの少なくとも 1 報に現れる。

## 6. Every location of the claim

Live files (need the change):

1. `manuscript_A/sections/9_manuscript_en.md:305` (EN canonical, Results Part 4).
2. `manuscript_A/sections/9_manuscript_jp.md:310` (JA canonical: 「論文あたり 7–8 種類の EP タイプと 6–7 の SRG」「5 つの
   EP タイプ（EP-01a、EP-03a、EP-06a、EP-07a、EP-08a）は…再帰する」).
3. `manuscript_A/build/manuscript_en_main.tex:1443` (generated by build; fixed by rebuilding after item 1).
4. `manuscript_A/build/royal-society-of-chemistry-article-template/paperA.tex:505` (RSC/Overleaf version, older wording
   "Heck-reaction test set … 7--8 EP types and 6--7 SRGs per paper; five EP types …", without "(single-run counts)").
   This needs a targeted edit if this tex is used for resubmission.

Not present: the SI (`manuscript_A/SI/output/SI-*.md`, including SI-11.17, which gives no counts), the response letter
(`response_letter_R1_draft.md`), the abstract, Discussion and Conclusions, and the split section files
(`sections/3_results_en.md` and `3_results_ja.md` are stale as of 2026-09-09 and carry neither the sentence nor the
numbers).

R1 working notes that quote the claim (update their status when done; they are not submission text):
`DigitalDiscovery_R1/01_response/resubmission_tasklist_20261005.md:39` (B6), `revision_changelog_R1.md:79`,
`fable51_review_20260928.md:47`, and `ja_sync/en_20260826.md:285` and `ja_sync/diffs_for_translation.md:357` (frozen
sync snapshots).

Historical copies (frozen; no change): `manuscript_A/shared/9_manuscript_A_jp_2606*.md`, `manuscript_A/preprint/*`,
`manuscript_A/drafts/documentary_resolution_20260908/*`, `manuscript_A/build/_jp_sync/*`, and the submitted version
under `submissions/paperA_2026-06-30_*`.

Suggested response-letter point (R3-4): say that the counts were re-derived from the deposited Stage 3 records with the
script and rule above, that the SRG range was corrected from 6–7 to 5–8 and the EP range from 7–8 to 6–8, and that the
recurrence statement now names the types present in every paper.
