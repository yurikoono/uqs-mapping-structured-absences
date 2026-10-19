# WoS Query Anomalies Log

Anomalies encountered during EP-03a structured-retrieval pilot (2026-04-20). Retained as methodological evidence for the manuscript defense.

## Anomaly #1: `alkylnickel` → `allylnickel` autocorrect

**Date**: 2026-04-20
**Context**: Re-running Variant C.
**Observation**: WoS displayed a "Did you mean?" suggestion replacing the term `"alkylnickel"` in the Variant C query with `"allylnickel"`, offering 75 results for the auto-corrected query. The original query (with `alkylnickel`) was effectively rejected or returned a smaller/empty set.

**Impact**: Allyl (η³-allyl, C–C=C coordinated) and alkyl (σ-bonded Ni–C single bond) nickel complexes are chemically distinct. Accepting the autocorrect would redirect retrieval to an unrelated ligand class, silently breaking the semantic intent of the query.

**Root cause (hypothesis)**: WoS's indexed term dictionary contains "allylnickel" as a common term (η³-allyl Ni complexes in polymerization and allylic substitution chemistry are extensively studied) but not "alkylnickel" as a single unhyphenated word. The autocorrect is literal — it swaps the term without respecting chemical meaning.

**Mitigation adopted**: Replaced `"alkylnickel"` with hyphenated/spaced variants `"alkyl nickel"` and `"alkyl-nickel"` in the revised Variant C query. These phrases bypass the autocorrect because they are multi-token and the dictionary cannot single-word-correct them.

**Methodological note**: This is a concrete example of a structural retrieval failure mode absent from LLM parametric retrieval. An LLM asked about "alkylnickel intermediate characterization" will correctly recall alkyl-Ni species without semantic substitution. A structured database query inherits the indexer's term normalization, which can silently distort chemical intent.

This anomaly is worth citing in the manuscript as a concrete, non-anecdotal illustration of the complementarity between LLM-parametric and keyword-structured retrieval modes (Methods 2 computational-nature paragraph).
