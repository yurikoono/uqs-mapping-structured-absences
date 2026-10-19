#!/usr/bin/env python3
"""R3-3 re-aggregation: Top-3 reinforcement EP SET from the 24 per-run Stage 3 records.

Source (frozen as submitted): submissions/paperA_2026-06-30_Digital_Discovery_v1/papers/dev/{kumada,murai}/
  {paper}_v184_sonnet_s3v2{,_runN}.md      (JA cell, run1 = no suffix)
  {paper}_v184_sonnet_s3v2_en{,_runN}.md   (EN cell)

The Stage 3 v2 prompt defines no "Top-3" field. §5 ("Shortest-reinforcement route")
lists, per objective function, an EP investment order. Two extraction rules:

  FIRSTOBJ  first three distinct EPs of the FIRST route block in §5
            (= the prompt's first objective function, one VQ level above the
            current one; Kumada is at VQ-2 -> VQ-3 route, Murai at VQ-1 -> VQ-2 route)
  VQ3       first three distinct EPs of the "route to VQ-3" block
            (fixed target, comparable across papers)
  FIRST3    first three distinct EPs mentioned anywhere in §5 (sensitivity check)

Outputs (next to this script):
  multirun_top3_per_run.csv       one row per run × rule
  inclusion_frequency_per_cell.csv one row per cell × rule × EP
  extraction_trace.md             §5 route header + EP order per run, for manual audit
"""
import csv, re
from collections import Counter
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[3]
SNAP = ROOT / "submissions/paperA_2026-06-30_Digital_Discovery_v1/papers/dev"
EP = re.compile(r"EP-(\d{2}[a-z])")
SEC5 = re.compile(r"^#{2,4}\s*(?:§\s*5|5[.．:]|Step 5)", re.M)
SEC6 = re.compile(r"^#{2,4}\s*(?:§\s*6|6[.．:]|Step 6)", re.M)
# route block headers, e.g. "**Shortest route to VQ-3:**" / "**VQ-3 への最短ルート（…）:**"
# (the §5 section heading "最短補強ルート" is deliberately NOT matched)
# Kumada JA run1 heads its blocks "第一目的関数: VQ-3 …" instead; blocks with no EPs are dropped
ROUTE = re.compile(r"Shortest route to VQ-(\d)|VQ-(\d)[^\n]{0,30}?への最短ルート|第[一二]目的関数[:：]\s*\**\s*VQ-(\d)", re.I)


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
                yield paper, lang, run, SNAP / paper / f"{paper}_v184_sonnet_s3v2{tag}{suf}.md"


def section5(text):
    m = SEC5.search(text)
    if not m:
        return None
    rest = text[m.end():]
    n = SEC6.search(rest)
    return rest[: n.start()] if n else rest


def distinct(seq):
    out = []
    for x in seq:
        if x not in out:
            out.append(x)
    return out


def routes(sec):
    """[(vq_level, header_line, [EPs in block order])] for each route block in §5."""
    hs = list(ROUTE.finditer(sec))
    out = []
    for i, h in enumerate(hs):
        end = hs[i + 1].start() if i + 1 < len(hs) else len(sec)
        le = sec.find("\n", h.start())
        header = sec[h.start(): le if le != -1 else h.end()].strip()
        eps = distinct(EP.findall(sec[h.end():end]))
        if eps:
            out.append((int(h.group(1) or h.group(2) or h.group(3)), header, eps))
    return out


RULES = ("FIRSTOBJ", "VQ3", "FIRST3")
rows, trace = [], ["# Extraction trace (R3-3 re-aggregation)\n"]
for paper, lang, run, f in files():
    sec = section5(_resolve(f).read_text())
    if sec is None:
        for rule in RULES:
            rows.append(dict(paper=paper, lang=lang, run=run, rule=rule, top3="", note="§5 not found", file=f.name))
        trace.append(f"## {f.name}\n\n§5 NOT FOUND\n")
        continue
    rs = routes(sec)
    vq3 = next((r for r in rs if r[0] == 3), None)
    picks = {
        "FIRSTOBJ": (rs[0][2][:3] if rs else [], f"first route = VQ-{rs[0][0]}" if rs else "no route block"),
        "VQ3": (vq3[2][:3] if vq3 else [], "" if vq3 else "no VQ-3 route block"),
        "FIRST3": (distinct(EP.findall(sec))[:3], ""),
    }
    for rule in RULES:
        eps, note = picks[rule]
        if eps and len(eps) < 3:
            note = (note + "; " if note else "") + f"only {len(eps)} EPs"
        rows.append(dict(paper=paper, lang=lang, run=run, rule=rule, top3=",".join(eps), note=note, file=f.name))
    trace.append(f"## {paper} {lang} run{run} — `{f.name}`\n")
    for lvl, header, eps in rs:
        trace.append(f"- route VQ-{lvl}: {', '.join(eps) or '—'}  ← `{header[:80]}`")
    trace.append(f"- all §5 EPs in order: {', '.join(distinct(EP.findall(sec)))}\n")

with open(HERE / "multirun_top3_per_run.csv", "w", newline="") as fh:
    w = csv.DictWriter(fh, fieldnames=["paper", "lang", "run", "rule", "top3", "note", "file"])
    w.writeheader(); w.writerows(rows)

freq = []
for paper in ("kumada", "murai"):
    for lang in ("JA", "EN"):
        for rule in RULES:
            sel = [r for r in rows if (r["paper"], r["lang"], r["rule"]) == (paper, lang, rule)]
            c = Counter(ep for r in sel for ep in r["top3"].split(",") if ep)
            for ep, k in sorted(c.items(), key=lambda x: (-x[1], x[0])):
                freq.append(dict(paper=paper, lang=lang, rule=rule, ep=f"EP-{ep}", runs_included=k,
                                 n_runs=len(sel), frequency=round(k / len(sel), 3)))
with open(HERE / "inclusion_frequency_per_cell.csv", "w", newline="") as fh:
    w = csv.DictWriter(fh, fieldnames=["paper", "lang", "rule", "ep", "runs_included", "n_runs", "frequency"])
    w.writeheader(); w.writerows(freq)
(HERE / "extraction_trace.md").write_text("\n".join(trace))
print(f"{len(rows)} rows; trace written")
