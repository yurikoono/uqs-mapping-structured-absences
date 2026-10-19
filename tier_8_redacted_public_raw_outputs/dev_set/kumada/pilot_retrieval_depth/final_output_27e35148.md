Reading PDF, S0–S3v2 outputs, and the latest Stage 4 prompt (v6) in parallel.

All inputs read. Now I'll execute Stage 4 v6 with externalized retrieval reasoning. Given the high hallucination risk flagged for Kumada papers in memory (67% Sonnet rate, named-reaction trigger, dense author network), I'll be conservative with bibliographic claims and mark Verification recommendation [必須] for most entries.

Let me first externalize my early retrieval thinking, then write the full output.

**Retrieval externalization (recorded before formal output):**

When I read EP-01a (reporting coherence — Table I gaps), the *immediate* candidate was Tamao's full paper in BCSJ 1976 — this is a Tier I retrieval, surfacing before I had to "search." It's the textbook Letter→Full Paper auto-resolution pattern (C23 trigger).

EP-03a (direct intermediate observation) triggered Tier II reasoning: "diorganonickel observation" → Akio Yamamoto group at Tokyo Inst. Tech. → Komiya as the named author for [NiR₂(L₂)] decomposition kinetics. Confidence Medium because I'm uncertain about exact year/journal pairing.

EP-09a (Ni(acac)₂ vs NiCl₂(dpe) head-to-head) was the hardest — I considered Wenkert 1979 (rejected: aryl ether substrate, not aryl chloride; doesn't replicate the comparison), Negishi reviews (rejected: reviews don't fill), and ultimately landed on a "likely unfilled" judgment with C7 (success-driven erasure by Pd cross-coupling pivot).

Now writing the full output.

Stage 4 v6 with retrieval-depth annotation complete. Output written to [kumada_v17_sonnet_s4v6_retrieval_depth.md](papers/dev/kumada/kumada_v17_sonnet_s4v6_retrieval_depth.md).

**Summary of findings:**

- **9 EPs classified** into 三群: 第一群 (EP-01a, 03a, 06a, 07a), 第二群 (EP-02a, 04a, 05a, 09a), 第三群 (EP-08a)
- **Primary filling candidate**: Tamao 1976 BCSJ Full Paper (C23 Letter→Full Paper auto-resolution, バンドル充填 4-6 EPs)
- **2 unfilled EPs flagged**: EP-08a (C6 incentive-structural unfilling) and EP-09a (C7 success-driven question erasure by Pd-coupling pivot)

**Retrieval depth distribution (the experimental signal you asked for):**
- **Tier I (immediate)**: 3 entries — all anchored on Tamao 1976 BCSJ via the C23 trigger pattern
- **Tier II (associative)**: 1 entry (Komiya/Yamamoto, EP-03a/06a)
- **Tier II→III**: 2 entries (EP-04a Tamao続報, EP-05a Kochi 系列)
- **Tier III (deep)**: 2 entries (EP-07a Knochel, EP-09a Corriu/Masse)
- **N/A**: 1 unfilled (EP-08a)

**Honest hallucination flagging:** All 6 selected papers marked Verification recommendation [必須] (named reaction + 1980 年以前 + dense author network triggers all fired). Author lists, volumes, and pages for Komiya 1983, Tamao 1972 続報, and Smith-Kochi entries are explicitly recorded as推定 requiring Crossref verification — the memory record's 67% Sonnet hallucination rate for this paper is a binding warning.

**Externalized rejected candidates (4 flagged):** Wenkert 1979 (rejected on substrate-class mismatch), Negishi reviews (reviews don't fill), Vicic Ni(I)/Ni(III) (different context), Hayashi-Konishi-Kumada asymmetric (different focus from EP-04a).