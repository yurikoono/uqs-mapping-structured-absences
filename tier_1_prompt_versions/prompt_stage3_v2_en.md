# Stage 3: Re-certification Assessment Sheet for Scientific Knowledge — English-only track
<!-- prompt_version: stage3-v2-en-20260419 -->
**Language: English throughout (English-only evaluation variant of stage3-v2-20260416). RI/EP/VQ codes and technical terms remain in English as in the original.**

Report the prompt version at the start of your output:
```
prompt_version: stage3-v2-en-20260419
```

---

## Input

Paste the following before this prompt:
1. **Stage 0 output** (BIB-1 through BIB-8b, S0-1 through S0-7)
2. **Stage 1 Turn 4 output** (A, B, C, U, META, TEMPERATURE_SUMMARY, GAP)
3. **Stage 2 output** (D-1 through E, confirmed_english)
4. **Stage 2F output** (optional; used in group mode. When absent, run in
   single-paper mode.)

---

## Output discipline

Follow the §1 through §6 structure below and output only the structured
assessment sheet. Do not add explanatory prose, follow-up questions, next-
step suggestions, or text outside the specified fields.

**Basic stance:** write not as "criticism of past authors" but as an
"upgrade blueprint from the present." Use the form "investing X would
allow the paper to reach VQ-N," not "the paper should have done X."

---

## Reference system

### Root-Issue Codebook v0.2

| Code | Label | Definition |
|:-----|:------|:-----------|
| **RI-01** | Reporting integrity | Cross-comparison is impossible due to inconsistent measurement frames, condition reporting, or units. |
| **RI-02** | Object identification | Product or catalyst structure/purity is not established at a granularity that excludes alternative candidates. |
| **RI-03** | Unobserved explanatory | A species or state central to the explanation is neither directly observed nor kinetically constrained. |
| **RI-04** | Unreplicated discriminator | A single data point with strong discriminatory power is interpreted at a high level without analytical precision or exclusion of alternative pathways. |
| **RI-05** | Qualitative overread | Structural or causal implications are derived from qualitative rankings without numerical support. |
| **RI-06** | Imported model | A model from another system is imported without demonstrating isomorphism in the target system. |
| **RI-07** | Unsupported boundary | A limit of the form "only X is possible" is asserted without failure examples. |
| **RI-08** | Unquantified reliability | Comparative data lack replicate measurements or uncertainty descriptions. |
| **RI-09** | External superiority | Superiority is asserted on the basis of external literature values only, without a direct comparison. |
| **PRI-10** | Kinetic overclaim | An absolute rate enhancement is claimed without kinetic data (provisional code). |
| **PRI-11** | Mechanism–kinetics decoupling | The proposed catalytic cycle is not used to derive a rate law algebraically; mechanism is supported only by agreement with observed rate orders (provisional code). |

**Codebook application notes (v0.2a):**

The following are recurring patterns observed across 8+ papers of analysis.
Consult when applying each RI.

- **RI-03 subtype — Available-but-unutilized characterization:** cases in
  which acquired experimental data (X-ray structures, NMR spectra, etc.)
  could verify a mechanistic claim but the implications are not extracted
  in the main text. Not "unobserved" but "observed yet unutilized."
- **RI-06 scope note — cycle-level import:** RI-06 applies not only to
  analogies between individual elementary steps but also to large-scale
  model import in which an entire catalytic cycle is constructed from
  another system.
- **RI-07 extended use — negative boundary claims:** RI-07 applies also to
  negative boundary claims of the form "X is the most serious limitation"
  made without data, not only to positive boundaries of the form "only X
  is effective."
- **RI-08 subtype — internal inconsistency:** when two quantities
  calculable from the same sample (e.g., yield and conversion) show a
  mathematical inconsistency, apply RI-08 as absence of measurement
  consistency in addition to absence of replication.

**PRI promotion criterion:** isomorphism confirmed across two independent
papers, or cross-case recurrence confirmed by a Stage 2F recurring_pattern.
When a new pattern that does not fit existing RIs is detected, propose it
in §6 as a "PRI-NN candidate."

**PRI promotion status (as of v0.2a):**
- PRI-10 (Kinetic overclaim): provisional. Confirmed in Monnereau 2009.
  One additional paper required for promotion.
- PRI-11 (Mechanism–kinetics decoupling): provisional. Proposed in
  Breitenfeld 2014; isomorphic pattern confirmed in Pengfei 2024. Two-paper
  independent confirmation is satisfied; promotion candidate. Definition:
  "mechanism is supported only by agreement with observed rate orders,
  without an algebraic derivation of the rate law from the proposed
  catalytic cycle or reaction mechanism."

### VQ decision matrix

| Level | Label | Required resolutions |
|:------|:------|:---------------------|
| **VQ-1** | Observation | RI-02 |
| **VQ-2** | Method | RI-01, RI-07 (+ inherits VQ-1) |
| **VQ-3** | Mechanism | RI-03, RI-04, RI-06 (+ inherits VQ-2) *note 1 |
| **VQ-4** | Benchmark | RI-08, RI-09 (+ inherits VQ-3) |

**Inheritance principle:** higher VQ levels inherit all lower-level
requirements.
*Note 1: if RI-05 remains in a serious form, VQ-3 is "qualified."

**Lethality judgments:**
- Fatal: if unresolved, the claim at that VQ level cannot in principle
  hold.
- Non-fatal: remains unresolved but does not fundamentally overturn the
  claim.
- Era-norm dependent: non-fatal at the time, fatal by contemporary
  standards. → Record in §4.

### EP dictionary (common labels)

| EP Code | Common label |
|:--------|:-------------|
| **EP-01a** | Reporting-coherence pack |
| **EP-02a** | Identity / purity substantiation pack |
| **EP-03a** | Direct-observation / state-assignment pack |
| **EP-04a** | Discrimination / replication pack |
| **EP-05a** | Quantitative-ranking substantiation pack |
| **EP-06a** | Analogy-validation pack |
| **EP-07a** | Boundary-test pack |
| **EP-08a** | Replication / uncertainty pack |
| **EP-09a** | Internal benchmark pack |
| **EP-10a** | Kinetic verification pack (provisional) |

---

## Assessment-sheet generation procedure

### Step 1: §1 Claim Architecture

**Input:** Stage 2 D-1

Record the following:
- One-paragraph summary of the **core claim**, making the Novelty pillar
  and the Utility pillar explicit.
- Presence or absence and form of **layered structure**. Decide whether "a
  single refutation collapses all claims" or "independent layers exist,"
  and describe any inter-layer dependencies.

---

### Step 2: §2 SRG / CLA → RI / ER / EP Crosswalk

**Input:** Stage 1 Turn 4 META (same_root_groups) + Stage 2 D-4 candidates
+ TEMPERATURE_SUMMARY

**Procedure:**

**2a. SRG acquisition:**
Take the same_root_groups from Stage 1 Turn 4 as given.

**2b. CLA candidate identification:**
Extract from the Stage 2 D-4 candidates those that belong to no SRG.
Record as a CLA (Claim-level Adjunct) those that satisfy:
- Directly bear on whether the D-1 claim holds (tied to title or NC items)
- The B/A items listed in grounded_in are not included in any SRG's
  member_items

**Self-contradictory-absence CLA check:**
Among Stage 1 U items, specifically detect cases where "an observable
that the paper's proposed model (catalytic cycle, reaction mechanism,
etc.) predicts is not reported as the paper's own data." This pattern
appears as:
- The catalytic cycle predicts R–R (homocoupling) formation, but R–R
  yield is not reported
- A proposed intermediate should be spectroscopically observable, but the
  observation is not performed
- A rate law should be derivable, but has not been derived
- DFT calculations predict quantities comparable to experimental values,
  but the comparison is not made
Record these as CLAs if they are not captured in existing SRGs.

**2c. RI mapping:**
For each SRG/CLA, consult the Codebook (above) and record using the
following template:

```
**SRG-N [name]** (or CLA: [name])

* **Primary RI**: RI-XX [Label]
* **Secondary RI**: RI-YY [Label] (if applicable; otherwise omit)
* **ER**: [normative requirement for the claim to hold. 1–2 sentences]
* **EP**: EP-XXa [common label] (; EP-YYa [common label])
* **Case-specific implementation**: [describe experiments aligned with
  the paper's specific chemistry]
* **Notes**: [list of sub-B/A/U items. Position in TEMPERATURE_SUMMARY
  (high_convergence_low_gap, etc.). convergence and gap information]
```

**Mapping rules:**
- One Primary RI per SRG/CLA. Select the structurally heaviest RI.
- Secondary RIs may be listed as needed. EPs are attached per RI.
- If one SRG fits multiple RIs equally, choose as Primary the RI
  supported by the larger number of sub-B items.
- Case-specific implementation must be written in terms of the paper's
  own chemistry (metal, ligand, substrate, analytical method). EP-03a in
  a Ni system differs in implementation from EP-03a in a Pd system.

**Additional processing when Stage 2F is present (group mode):**
- Cross-reference Stage 2F's recurring_roots against the paper's SRGs.
  If an SRG corresponds to a recurring_root, append to the notes:
  "recurring_root: [description], cross-case confirmed."
- If any U items match Stage 2F's recurring_U, add them to the CLA
  candidates.

---

### Step 3: §3 Current VQ assessment

**Input:** §2 crosswalk result + VQ decision matrix

**Procedure:**
Judge pass/fail for each level in the order VQ-1 → VQ-2 → VQ-3 → VQ-4.

For each level record:
- **Pass:** "VQ-N [label] holds" + 1–2 sentences of grounds. If any item
  was judged Non-fatal, note it explicitly.
- **Fail:** "VQ-N [label] fails" + 1–2 sentences of grounds. List the
  unresolved RIs.
- **Qualified:** used when RI-05 etc. remain. Record as "VQ-N
  (qualified)" with one sentence on the reason for qualification.

**Explicit inheritance:** at VQ-2 and above, record that the lower-VQ
requirements are assumed to hold. Example: "VQ-2 holds on the premise
that RI-02 is non-fatal."

**Layered VQ asymmetry detection:** when §1's layered structure
identifies independent layers, in addition to the paper-wide VQ judgment
evaluate VQ per independent layer. If a layer has reached a higher VQ
level than the paper as a whole, record in the form:
"However, **[layer name]** on its own: [grounds for reaching VQ-N]."
This per-layer asymmetry carries analytical information about which parts
of the paper's claim are most robust and which are most fragile.

---

### Step 4: §4 Era-Norm Annotation

**Input:** Stage 2 D-2 (format_exploitation, timing_pressure) +
Stage 2 D-3 (journal_constraint, field_competition_state) +
Stage 0 (BIB-4 year, BIB-7 format)

**Procedure:**
Separately from VQ, classify into the following two tags:

- **communication-era tolerated**: omissions allowed within the genre
  convention of that era, journal, and format. List the corresponding
  B/A items and give one sentence each on why they were tolerated then.
- **modern-era deficient**: omissions not acceptable in present-day
  re-certification. List the corresponding B/A items and give one
  sentence each on why they are insufficient now.

**Criteria:**
- Items cited in Stage 2 D-3's journal_constraint → communication-era
  tolerated candidates.
- Items cited in Stage 2 D-2's format_exploitation that directly conflict
  with the requirements for a VQ upgrade → modern-era deficient.
- Items that belong to both (tolerated then but deficient now) → record
  in both tags, noting the dual classification.

---

### Step 5: §5 Shortest-reinforcement route

**Input:** §2 crosswalk result + §3 VQ assessment

**Procedure:**

**5a. Objective-function setting:**
Treat the VQ level above the current one as the first objective function.
Example: current VQ-2 → first objective function is VQ-3.
Record the reach to VQ-4 as a second objective function (with VQ-3 as a
prerequisite).

**5b. EP investment ordering:**
For each objective function, determine the EP investment order by:
- Information gain (EPs that advance the largest number of RIs
  simultaneously come first)
- Experimental feasibility (EPs executable with existing infrastructure
  come first)

**5c. Certification-gate order:**
Separately from the experimental investment order, make explicit that
final VQ certification follows the inheritance principle. Append the
note: "The experimental investment order follows information gain, but
the final certification is fixed by the gate order VQ-1 → VQ-2 → VQ-3 →
VQ-4."

**Output format:**
```
**Shortest route to VQ-N:**
1. EP-XXa [common label] — [one-sentence case-specific implementation].
   Advances RI-XX.
2. EP-YYa [common label] — [one-sentence case-specific implementation].
   Advances RI-YY.
...

Certification-gate note: [one sentence noting that the final
certification follows the inheritance principle]
```

---

### Step 6: §6 Contribution to institutional design

**Input:** the full results of §2 through §5

Describe what this paper's analysis contributed to the Codebook, the VQ
criteria, and the EP dictionary. Consider:

- Whether it provided a new representative case for an existing RI code
- Whether a pattern requiring a new PRI candidate was detected
- Whether new insights appeared about the boundary conditions (lethality,
  era-norm) of the VQ criteria
- Whether new case-specific implementations should be added to the EP
  dictionary
- In group mode, whether Stage 2F recurring_patterns provided evidence
  for RI promotion

**Record explicitly if any of the following patterns is detected:**

- **Labeling mismatch:** the authors explicitly label a hypothesis or
  limitation, yet the narrative uses factual verbs ("reacts with,"
  "forms," "is converted to"). Often co-occurs with RI-06. Record the
  position of the hypothesis label (e.g., concentrated in the final
  sentence).
- **Automatic-resolution pattern via communication→Full Paper
  transition:** patterns in which RI-07 or RI-01 arise from the page-
  limit constraints of the communication format and are automatically
  resolved in the Full Paper. Check the correspondence with A items in
  §4's Era-Norm Annotation.
- **RI co-occurrence pattern:** cases in which two or more RIs co-occur
  in the same SRG and resolving only one is insufficient (e.g.,
  co-occurrence of RI-04 and RI-06 requires resolving both). Describe
  the structure of the co-occurrence.
- **Incomplete negative evidence:** patterns in which negative
  experimental results (radical clocks, TEMPO trapping, etc.) are used
  as positive mechanistic evidence without mass-balance closure or
  kinetic-window evaluation. Record as a case-specific implementation of
  RI-04.

If no new insight emerged, state: "This case confirms existing
institutional design."

---

## Output format

```
prompt_version: stage3-v2-en-20260419
model_info: <model name and version>

# Re-certification Assessment Sheet for Scientific Knowledge

## [Paper authors] [year] ([BIB-3] [BIB-7])

### §1 Claim Architecture
[core-claim summary]
[layered-structure judgment]

### §2 SRG / CLA → RI / ER / EP Crosswalk

[template for each SRG]
...

Outside the SRGs: CLAs
[template for each CLA] (if applicable)
...

### §3 Current VQ assessment
Current judgment: VQ-N ([label])
[pass/fail grounds for VQ-1 through VQ-4 in order]

### §4 Era-Norm Annotation
communication-era tolerated:
[item list with one-sentence grounds each]

modern-era deficient:
[item list with one-sentence grounds each]

### §5 Shortest-reinforcement route
[EP investment order per objective function]
[certification-gate note]

### §6 Contribution to institutional design
[description of insights]
```
