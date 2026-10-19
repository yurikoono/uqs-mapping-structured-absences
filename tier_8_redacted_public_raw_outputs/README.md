# Tier 8 — Redacted Stage Outputs (public version)

**Spec (SI-11.11)**: the Stage 0–Stage 4 and Stage 2F outputs of Tier 3 with verbatim source-paper quotations (`key_quote`, `quote`, `target_*` fields, and other quoted or verbatim passages of the analysed paper) replaced by `[REDACTED: …]` markers that point to the source paper (via its DOI, or the item's `loc:` field, which is kept) or to the unredacted copy in Tier 9 (in the reviewer version, the Tier 3 copies). Model-written paraphrases of a paper's title or claims (the quoted E-propositions, i.e. the `confirmed_english_propositional` statements of Stage 2 and tables that list them, with fewer than ten contiguous words of the paper's text) are not source quotations and are kept. UQS classifications, inference tiers and reasoning are unchanged. The full versions with the quotations are in `tier_3_stage_outputs/` *(reviewer version only; redacted Markdown copies under `tier_8_redacted_public_raw_outputs/`)* (reviewer access).

(Before the revision this README carried the Tier 3 heading by mistake; corrected 2026-09-28.)

The folder layout mirrors Tier 3:

## Structure

```
tier_8_redacted_public_raw_outputs/   (same layout as tier_3_stage_outputs/ *(reviewer version only; redacted Markdown copies under `tier_8_redacted_public_raw_outputs/`)*)
├── dev_set/                              (2 papers)
│   ├── kumada/                           — Kumada 1972 (primary case study)
│   └── murai/                            — Murai 1993 (secondary dev-set)
├── test_set/                             (10 Heck papers)
│   ├── hom1/, hom2/                      — homogeneous catalysis
│   ├── het1/, het2/                      — heterogeneous catalysis
│   ├── comp1/, comp2/                    — computational chemistry
│   ├── app1/, app2/                      — synthetic application
│   └── scr1/, scr2/                      — condition screening
├── ep_historical_case_study/             (8 historical + 1 mini-review = 9 papers)
│   ├── kumada1976b_tamao_bcsj_layer1_anchor/   — Tamao 1976 BCSJ Full Paper I
│   ├── monnereau2009/, breitenfeld2014/, cherney2015/  — Layer-2 paradigm-shift
│   ├── molander2016/, morken2016/, mazet2021/, li2024/ — Layer-2 paradigm-shift
│   └── tamao2002_minireview/             — Stage 2F integration anchor (Tamao 2002)
└── stage2f_integration_outputs/          (24 Stage 2F outputs + 1 Stage 3 anchor)
    ├── kumada1972_{g1,g2,g3,all}_v17_opus_s2f{,v7,v71}.md          (12 v17 outputs)
    ├── kumada1972_{g1,g2,g3,all}_v184_opus47_s2f{,v7,v71}.md       (12 v184 outputs)
    └── kumada1972_v17_sonnet_s3.md                                 (Stage 3 anchor)
```

**Total**: 21 source-paper folders + 25 Stage 2F-and-anchor files = **21-paper corpus per Tier 3 spec**.

## Outside the 21-paper corpus

Deposited in Tier 3 since the R1 version (2026-09-28), outside the 21-paper corpus (redacted copies at the same sub-paths of this tier; added by the public-cut build, see `REVISION_R1.md`):

- `tier_3_stage_outputs/context_analyses/` *(reviewer version only; redacted Markdown copies under `tier_8_redacted_public_raw_outputs/`)* — `jones2005/`, `martin2007/`, `terao2002/`, `uchino1970/` (project path `papers/dev/`): analyses of three cross-coupling references cited for context and of the Uchino 1970 dipy-Ni system; not primary evidence and not part of the per-reference verification catalogue.
- `tier_3_stage_outputs/citation_integrity_cases/` *(reviewer version only; redacted Markdown copies under `tier_8_redacted_public_raw_outputs/`)* — `yamamoto1978/`, `yamamoto1981/` (project path `papers/ep/kumada1972/`): the Yamamoto 1978 / 1981 citation-integrity audit cases (SI-9); audit material, not historical case-study fillers.

Not deposited: `papers/dev/uqs_self/` (a self-application of the method, not part of the corpus) and `papers/ep/etc/kumada1976/` (Hayashi–Tajika–Tamao–Kumada 1976 JACS, a different paper from Tamao 1976 BCSJ = `kumada1976b`; outside the 21-paper scope).

## Naming alignment

- Folder `papers/ep/kumada1972/molken2016/` is copied here as `morken2016/` (canonical surname; the source-folder typo `molken` is preserved at the link target).
- Folder `papers/ep/kumada1972/pengfei2024/` is copied here as `li2024/` (canonical surname; the source folder uses the author's given name).

---

> **Tier 8 redaction notice**: This file is a redacted copy of the corresponding Tier 3 / Tier 9 output. Verbatim source-paper quotations have been replaced by `[REDACTED: see source paper §<loc>; full text retained in Tier 9 reviewer-only deposit]` markers, preserving location references and our own analytical content. Bibliographic fields (title, authors, journal, year, DOI), analytical labels (`evidence_chain:` with B-/U-/A-/C- internal IDs), short technical terms, and our own analytical text are not redacted. The redaction was applied by `scripts/redact_for_tier8.py` and, for this version, by `scripts/build_paperA_R1_public.py` with `scripts/redact_source_ngram_runs.py` (scripts of the project repository; they are not deposited).
