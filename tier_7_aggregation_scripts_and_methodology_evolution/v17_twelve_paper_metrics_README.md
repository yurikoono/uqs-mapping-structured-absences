# v17 Twelve-Paper Test Set Metrics — README

**File**: `v17_twelve_paper_metrics.csv`
**Generated**: 2026-05-17
**Source**: `scripts/extract_v17_metrics.sh`

## Purpose

Per-paper count of UQS Stage 1 U-category items, Stage 1 B-category items, and Stage 2 D-4 candidates for the twelve-paper test set (Kumada + Murai dev set + 10 Heck test papers), under the v17 prompt configuration with Claude Sonnet 4.6.

Provides the audit trail for the aggregate metrics statement in Results Part 4:

> "Aggregated across the twelve, the v17 prompt produced approximately 38 U-category items (unclassified, self-contradictory absences), 240 B-category items (traces of rejected directions), and 78 D-4 candidates (unquestioned motivations); per-paper averages were ~3 U-items, ~20 B-items, and ~6.5 D-4 items."

## Extraction methodology

Counts extracted from `papers/{dev,test}/{paper}/{paper}_v17_sonnet_s1.md` and `..._s2.md` by `scripts/extract_v17_metrics.sh`.

Item definition patterns recognised (3 variants per category, due to format drift across the v17 cycle):

**B and U items (Stage 1)**:
- `[B] B-N |` / `[U] U-N |` (kumada-style, single-line pipe-separated)
- `B-N |` after standalone `[B]` header (murai-style)
- `[B-N] item_id: B-N` (hom2-style, multi-line block)

**D-4 candidates (Stage 2)**:
- `**D4-N: ...**` (kumada)
- `**D-4候補N: ...**` / `**D-4候補 N: ...**` (murai, app1)
- `**D-4-N: ...**` (app2, scr2)
- `【D-4候補N】` (hom1, full-width brackets)
- `**候補N: ...**` / `候補N: ...` (hom2, comp1, comp2, scr1 — drop "D-4" prefix)

IDs are deduplicated per paper before counting, so cross-references within rationale text do not inflate the count.

## Aggregate comparison: extracted vs Results Part 4 claim

| Metric | Manuscript current (post-2026-05-17 audit) | Extracted total | Extracted per-paper average | Match |
|---|---|---|---|---|
| U-category | 39 | 39 | 3.25 | ✅ exact |
| B-category | 232 | 232 | 19.33 | ✅ exact |
| D-4 candidates | 94 | 94 | 7.83 | ✅ exact |

The Results Part 4 main-text numbers now match the extracted counts exactly. The CSV serves as the auditable source for these numbers.

### Origin of the previous "approximately 78" value

The pre-2026-05-17 manuscript carried "approximately 38 U-category items, 240 B-category items, and 78 D-4 candidates" — a v17 cycle interim snapshot computed during the initial Phase Q manuscript drafting (~Apr 2026). The "78" value originated from a v15→v17 progression narrative in the earliest Paper A draft (`manuscript_A_v1/sections/results_en.md`, 2026-04-24):

> "U-category items increased from 4 in v15 to approximately 38 in v17; B-category items increased from approximately 100 to 240; and D-4 candidates increased from approximately 50 to 78."

This number was carried forward through subsequent manuscript revisions without re-counting, even after the v17 cycle was fully completed across all 12 papers. The post-cycle per-paper average (~7.8 D-4) was already recorded in `improvements/session_handover_v17.md` (Line 78: "D-4候補平均: v16.1 ~6.5 → v17 ~7.8 (+20%)"), but this update was not propagated into the manuscript text until the 2026-05-17 audit.

The 2026-05-17 audit (this CSV + `scripts/extract_v17_metrics.sh`) re-counted all D-4 candidates across the 12 papers using 5 format-variant patterns observed in the v17 outputs and confirmed the post-cycle total of **94 D-4 candidates** (per-paper average 7.83, consistent with the session_handover record).

The Results Part 4 main text was updated to **39 / 232 / 94** in the 2026-05-17 audit cycle. The change-log entry in `3_results_en.md` postamble (Phase Q section) records this provenance for reproducibility.

## Reproducibility

```bash
bash scripts/extract_v17_metrics.sh > manuscript_A/figures/data/v17_twelve_paper_metrics.csv
```

## Data Availability

This CSV and the extraction script are part of the Zenodo deposit under item (viii) "the source CSV files underlying Figs. 2–5 and SI Fig. S1" — but note that this CSV is **referenced by Results Part 4 text, not by a figure**. Consider extending item (viii) to "source CSV files for figures + the v17 twelve-paper aggregate metrics CSV that supports the Results Part 4 statement" for explicitness.
