#!/usr/bin/env python3
"""D3 screening (prereg §2.1 criteria 1-4, title/abstract only) and random draw (§2.2).
Every exclusion is listed with its reason; everything else dated >= 2026-02-01 is eligible."""
import csv, random, re
EXCL = {
 # criterion 1 (date unresolved)
 "": "c1: Crossref lookup failed (corpus row, Chem Sci 2021)",
 # criterion 3 (not a research article)
 "10.1007/s10563-026-09481-w": "c3: review ('Recent Coverage…', Catalysis Surveys)",
 "10.1002/ejoc.202501238": "c3: review (abstract surveys recent progress)",
 "10.1002/open.70244": "c3: review (abstract surveys recent attention)",
 "10.1055/a-2782-9258": "c3: Synfacts highlight", "10.1055/a-2806-6544": "c3: Synfacts highlight",
 "10.1055/a-2847-3903": "c3: Synfacts highlight", "10.1055/a-2915-0243": "c3: Synfacts highlight",
 "10.1055/a-2935-3388": "c3: Synfacts highlight",
 "10.1002/ange.9925574": "c3: German edition duplicate of 10.1002/anie.9925574",
 # criterion 4 (Heck-type coupling not the subject)
 "10.1002/adsc.70544": "c4: Heck is the side reaction being suppressed",
 "10.1002/cctc.71037": "c4: Heck is a competing pathway; subject is selective Ullmann coupling",
 "10.1002/cssc.70827": "c4: Heck–Cassar = copper-free Sonogashira, not Heck-type",
 "10.1021/acs.joc.6c00901": "c4: Heck–Cassar–Sonogashira",
 "10.1080/00958972.2026.2674204": "c4: Heck–Casser–Sonogashira",
 "10.1007/s00105-026-05779-y": "c4: non-chemistry (Heck's disease)",
 "10.47196/6k4v5m41": "c4: non-chemistry (Heck's disease)",
 "10.1093/jacamr/dlag072": "c4: non-chemistry (mnemonic)",
 "10.1515/zrgg-2026-0028": "c4: non-chemistry (author named Heck)",
 "10.1609/aaai.v40i43.40944": "c4: non-chemistry",
 "10.18296/set.1587": "c4: non-chemistry",
 "10.3224/ijar.v21i3.07": "c4: non-chemistry (person named Heck)",
 "10.3390/cancers18142322": "c4: non-chemistry",
}
rows = [x for x in csv.DictReader(open("candidate_pool.csv")) if (x["date"] or "") >= "2026-02-01"]
screen, elig = [], []
for x in sorted(rows, key=lambda x: x["doi"]):
    key = x["doi"] if x["date"][:1] == "2" else ""
    reason = EXCL.get(key)
    screen.append({**x, "title": re.sub(r"\s+", " ", re.sub("<[^>]+>", "", x["title"])), "decision": "exclude" if reason else "eligible", "reason": reason or ""})
    if not reason: elig.append(screen[-1])
for i, e in enumerate(elig, 1): e["n"] = i
pick = random.Random(20260929).sample(range(1, len(elig) + 1), len(elig))  # full order; first 4 = draw, rest = replacements
order = {n: r for r, n in enumerate(pick, 1)}
for e in elig: e["draw_rank"] = order[e["n"]]
with open("screening.csv", "w", newline="") as f:
    w = csv.DictWriter(f, fieldnames=["n", "draw_rank", "decision", "reason", "doi", "date", "journal", "title"], extrasaction="ignore")
    w.writeheader(); w.writerows(screen)
print(f"screened {len(screen)}; eligible {len(elig)}; excluded {len(screen)-len(elig)}")
for n in pick[:8]:
    e = elig[n - 1]; print(order[n], n, e["doi"], e["date"], "|", e["journal"][:25], "|", e["title"][:100])
