#!/usr/bin/env python3
"""R3-3 (remainder 2): the "11-paper v18.4 EN corpus" claims.

Claims re-counted (as submitted, main text):
  Results Part 2  "The VQ-hierarchy inversion recurs across all 11 papers of the v18.4 EN corpus"
  Discussion 1    "mechanistic EPs (VQ-3) fill within 4–12 years while replication and benchmarking
                   EPs (VQ-4) remain weakly represented 30–54 years later"

Corpus = Phase 2 report (2026-05-10): 2 dev papers (Kumada, Murai; EN run 1 = the un-suffixed
`_s4v2_en.md`) + 9 EP-filling-context papers (single run each). Same definitions as
reaggregate_stage4.py (fixed before counting; §B labels only; model's own diagnosis not used).

Delay = (first four-digit year in the §B "Filling Onset" line) − (publication year of the analysed
paper, from its folder name). Onset citations are LLM-parametric recall and were NOT
bibliographically verified here, so delays describe what the Stage 4 runs assert, not the record.
"""
import csv, re
from pathlib import Path
from statistics import median

import reaggregate_stage4 as S4

HERE = Path(__file__).resolve().parent
SNAP = S4.ROOT / "submissions/paperA_2026-06-30_Digital_Discovery_v1/papers"
FILES = [
    ("kumada1972", 1972, "dev/kumada/kumada_v184_sonnet_s4v2_en.md"),
    ("murai1993", 1993, "dev/murai/murai_v184_sonnet_s4v2_en.md"),
    ("kumada1976b", 1976, "ep/kumada1972/kumada1976b/kumada1976b_v184_sonnet_s4v2_en.md"),
    ("monnereau2009", 2009, "ep/kumada1972/monnereau2009/monnereau2009_v184_sonnet_s4v2_en.md"),
    ("breitenfeld2014", 2014, "ep/kumada1972/breitenfeld2014/breitenfeld2014_v184_sonnet_s4v2_en.md"),
    ("cherney2015", 2015, "ep/kumada1972/cherney2015/cherney2015_v184_sonnet_s4v2_en.md"),
    ("molander2016", 2016, "ep/kumada1972/molander2016/molander2016_v184_sonnet_s4v2_en.md"),
    ("molken2016", 2016, "ep/kumada1972/molken2016/molken2016_v184_sonnet_s4v2_en.md"),
    ("mazet2021", 2021, "ep/kumada1972/mazet2021/mazet2021_v184_sonnet_s4v2_en.md"),
    ("pengfei2024", 2024, "ep/kumada1972/pengfei2024/pengfei2024_v184_sonnet_s4v2_en.md"),
    ("tamao2002", 2002, "ep/discussion/tamao2002/tamao2002_v184_sonnet_s4v2_en.md"),
]
ONSET = re.compile(r"\*\*(?:Filling Onset|充填開始点)\*\*\s*[:：]\s*([^\n]*)")
YEAR = re.compile(r"\b(19[4-9]\d|20[0-2]\d)\b")

ep_rows, paper_rows = [], []
for pid, pub, rel in FILES:
    t = S4._resolve(SNAP / rel).read_text()
    secB, secE = S4.section(t, "B", "C"), S4.section(t, "E", "F")
    heads = list(S4.EP_HEAD.finditer(secB))
    info = {}
    for i, h in enumerate(heads):
        blk = secB[h.end(): heads[i + 1].start() if i + 1 < len(heads) else len(secB)]
        lm, om = S4.LABEL.search(blk), ONSET.search(blk)
        if h.group(1) in info and info[h.group(1)][0]:
            continue
        yr = YEAR.search(om.group(1)) if om else None
        info[h.group(1)] = (lm.group(1).strip() if lm else "", int(yr.group(1)) if yr else None)
    in_E = set(S4.E_EP.findall(secE))
    present = set(info)
    for ep in S4.ALL_EP:
        raw, onset = info.get(ep, ("", None))
        cls = S4.classify(raw) if ep in info else "absent"
        grp = next(g for g in ("VQ12", "VQ3", "VQ4") if ep in S4.G[g])
        ep_rows.append(dict(paper=pid, pub_year=pub, ep=f"EP-{ep}a", group=grp, label_class=cls,
                            onset_year=onset or "", delay=(onset - pub) if onset else "",
                            in_E=int(ep in in_E), raw_label=raw[:160], file=rel.split("/")[-1]))
    for lv, ok in S4.LEVELS.items():
        fs = {r["ep"][3:5] for r in ep_rows if r["paper"] == pid and r["label_class"] in ok}
        v3p = [e for e in S4.G["VQ3"] if e in present]
        vq4_unf = all(e not in fs for e in S4.G["VQ4"])
        paper_rows.append(dict(paper=pid, level=lv, vq3_present=len(v3p),
                               vq3_filled=sum(e in fs for e in S4.G["VQ3"]),
                               vq4_present=sum(e in present for e in S4.G["VQ4"]),
                               vq4_filled=sum(e in fs for e in S4.G["VQ4"]),
                               inversion=int(vq4_unf and any(e in fs for e in S4.G["VQ3"])),
                               inversion_strong=int(vq4_unf and bool(v3p) and sum(e in fs for e in v3p) > len(v3p) / 2)))

for name, rows in (("corpus11_labels_per_ep.csv", ep_rows), ("corpus11_inversion_per_paper.csv", paper_rows)):
    with open(HERE / name, "w", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=list(rows[0])); w.writeheader(); w.writerows(rows)

# printed summary
for lv in S4.LEVELS:
    sel = [r for r in paper_rows if r["level"] == lv]
    print(f"{lv:10} inversion {sum(r['inversion'] for r in sel)}/11  strong {sum(r['inversion_strong'] for r in sel)}/11  "
          + " ".join(f"{r['paper']}:{r['inversion']}" for r in sel))
fill = [r for r in ep_rows if r["label_class"] in S4.LEVELS["L_std"] and r["delay"] != ""]
for g in ("VQ12", "VQ3", "VQ4"):
    d = sorted(r["delay"] for r in fill if r["group"] == g)
    print(g, "filled(L_std) with onset:", len(d), "delays:", d, "median:", median(d) if d else "-")
print("filled but no onset year:", sum(1 for r in ep_rows if r["label_class"] in S4.LEVELS["L_std"] and r["delay"] == ""))
