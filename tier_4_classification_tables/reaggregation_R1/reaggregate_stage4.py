#!/usr/bin/env python3
"""R3-3 (remainder): Stage 4 re-aggregation — VQ-hierarchy inversion and EP-08a/09a non-filling.

Definitions fixed BEFORE counting (filling_level_definition_proposal.md, user-approved 2026-09-28):
  D1  label source = §B "Nature of filling" / 「充填の性質」 of each EP only. EP absent from §B -> unfilled.
      Mixed labels -> the WEAKEST component. §B-filled but listed in §E -> conflict flag.
  D2  levels:  L_std (primary) = Complete, Partial | L_strict = Complete | L_lenient = + Indirect.
      Attempted and Paradigm-shift are never filled. Confidence is not used (L_std without Low is reported).
  D3  groups (Methods 1.2 / Fig. 3): VQ12 = 01,02,07 | VQ3 = 03,04,05,06,10 | VQ4 = 08,09.
      Sensitivity: VQ3core = 03,04,06 (the Stage 3 prompt's VQ matrix: VQ-3 = RI-03, RI-04, RI-06).
  D4  inversion(run) = both VQ4 EPs unfilled AND >=1 VQ3 EP filled; strong = >half of present VQ3 EPs filled.
  D5  EP-08a / EP-09a unfilled run counts per paper x language.
The model's own inversion diagnosis (§D/§E wording) is recorded in a separate column and NOT used.
"""
import csv, re
from collections import defaultdict
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[3]
SNAP = ROOT / "submissions/paperA_2026-06-30_Digital_Discovery_v1/papers/dev"

# strength order, weakest first; a label's value is the weakest token found in its head
ORDER = ["none", "not_filled", "Indirect", "Partial", "Complete"]
TOKENS = [  # (regex, class)
    (r"unidentified|not identified|no filling|none identified|\bn/?a\b|未同定|未充填|存在しない|見当たらない|特定できない", "none"),
    (r"attempted|試行", "not_filled"),
    (r"paradigm[- ]shift|パラダイム", "not_filled"),
    (r"indirect|間接", "Indirect"),
    (r"partial|部分", "Partial"),
    (r"complete|完全", "Complete"),
]
LEVELS = {"L_std": {"Complete", "Partial"}, "L_strict": {"Complete"}, "L_lenient": {"Complete", "Partial", "Indirect"}}
G = {"VQ12": ["01", "02", "07"], "VQ3": ["03", "04", "05", "06", "10"], "VQ3core": ["03", "04", "06"], "VQ4": ["08", "09"]}
ALL_EP = sorted({e for v in G.values() for e in v})

SEC = lambda letter: re.compile(rf"^###\s*§\s*{letter}\b", re.M)
EP_HEAD = re.compile(r"^\*\*EP-(\d\d)a\b[^\n]*\*\*\s*$", re.M)
LABEL = re.compile(r"\*\*(?:Nature of filling|充填の性質)\*\*\s*[:：]\s*([^\n]*)")
CONF = re.compile(r"\*\*(?:Confidence|確信度|信頼度)\*\*\s*[:：]\s*([^\n]*)")
E_EP = re.compile(r"^\*\*EP-(\d\d)a", re.M)


def section(text, letter, nxt):
    m = SEC(letter).search(text)
    if not m:
        return ""
    n = SEC(nxt).search(text, m.end())
    return text[m.end(): n.start() if n else len(text)]


def classify(raw):
    head = re.split(r"\s+[—–]\s+|\s+-\s+", raw, maxsplit=1)[0].lower()
    found = [cls for rx, cls in TOKENS if re.search(rx, head, re.I)]
    if not found:
        return "unparsed"
    return min(found, key=ORDER.index)


def _resolve(p):
    """Repository path if it exists; inside the Zenodo deposit, the file of the same name under
    tier_3_stage_outputs/ (this script then sits in tier_4_classification_tables/reaggregation_R1/)."""
    p = Path(p)
    if p.exists():
        return p
    dep = Path(__file__).resolve().parents[2] / "tier_3_stage_outputs"
    hits = list(dep.rglob(p.name)) if dep.exists() else []
    if len(hits) == 1:
        return hits[0]
    raise FileNotFoundError(f"{p} (deposit matches: {len(hits)})")


def files():
    for paper in ("kumada", "murai"):
        for lang, tag in (("JA", ""), ("EN", "_en")):
            for run in range(1, 7):
                suf = "" if run == 1 else f"_run{run}"
                yield paper, lang, run, SNAP / paper / f"{paper}_v184_sonnet_s4v2{tag}{suf}.md"


def main():
    ep_rows, run_rows = [], []
    for paper, lang, run, f in files():
        t = _resolve(f).read_text()
        secB, secD, secE = section(t, "B", "C"), section(t, "D", "E"), section(t, "E", "F")
        heads = list(EP_HEAD.finditer(secB))
        labels = {}
        for i, h in enumerate(heads):
            blk = secB[h.end(): heads[i + 1].start() if i + 1 < len(heads) else len(secB)]
            lm, cm = LABEL.search(blk), CONF.search(blk)
            # supplementary blocks ("**EP-03a 補充（…）：**") must not overwrite the EP's labelled entry
            if h.group(1) in labels and labels[h.group(1)][0]:
                continue
            labels[h.group(1)] = (lm.group(1).strip() if lm else "", cm.group(1).strip() if cm else "")
        in_E = set(E_EP.findall(secE))
        model_inv = bool(re.search(r"inversion|逆転", secD + secE, re.I))
        filled = {lv: set() for lv in LEVELS}
        filled["L_std_noLow"] = set()
        for ep in ALL_EP:
            raw, conf = labels.get(ep, ("", ""))
            cls = classify(raw) if ep in labels else "absent"
            low = bool(re.match(r"\s*(low|低)", conf, re.I))
            for lv, ok in LEVELS.items():
                if cls in ok:
                    filled[lv].add(ep)
            if cls in LEVELS["L_std"] and not low:
                filled["L_std_noLow"].add(ep)
            ep_rows.append(dict(paper=paper, lang=lang, run=run, ep=f"EP-{ep}a", in_B=int(ep in labels),
                                label_class=cls, confidence=conf[:40], in_E=int(ep in in_E),
                                conflict=int(cls in LEVELS["L_std"] and ep in in_E),
                                raw_label=raw[:160], file=f.name))
        present = set(labels)
        for lv, fs in filled.items():
            v3p = [e for e in G["VQ3"] if e in present]
            v3c = [e for e in G["VQ3core"] if e in present]
            vq4_unfilled = all(e not in fs for e in G["VQ4"])
            run_rows.append(dict(
                paper=paper, lang=lang, run=run, level=lv,
                vq12_filled=sum(e in fs for e in G["VQ12"]), vq3_filled=sum(e in fs for e in G["VQ3"]),
                vq3_present=len(v3p), vq3core_filled=sum(e in fs for e in G["VQ3core"]),
                vq4_filled=sum(e in fs for e in G["VQ4"]),
                ep08_unfilled=int("08" not in fs), ep09_unfilled=int("09" not in fs),
                inversion=int(vq4_unfilled and any(e in fs for e in G["VQ3"])),
                inversion_strong=int(vq4_unfilled and v3p and sum(e in fs for e in v3p) > len(v3p) / 2),
                inversion_core=int(vq4_unfilled and any(e in fs for e in G["VQ3core"])),
                inversion_core_strong=int(vq4_unfilled and v3c and sum(e in fs for e in v3c) > len(v3c) / 2),
                model_mentions_inversion=int(model_inv), file=f.name))

    for name, rows in (("stage4_labels_per_ep.csv", ep_rows), ("stage4_inversion_per_run.csv", run_rows)):
        with open(HERE / name, "w", newline="") as fh:
            w = csv.DictWriter(fh, fieldnames=list(rows[0]))
            w.writeheader(); w.writerows(rows)
    print(len(ep_rows), "EP rows;", len(run_rows), "run rows")


if __name__ == "__main__":
    main()
