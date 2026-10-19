#!/usr/bin/env python3
"""Re-derive per-paper EP / SRG counts for the ten-paper Heck refinement set
(papers/test/{hom1,hom2,het1,het2,comp1,comp2,app1,app2,scr1,scr2}), v17 S0-S2,
from the primary Stage 3 outputs. Both Stage 3 prompt versions present in the
folders are counted: s3 (Stage 3 v1, tag stage3-v1-20260402) and s3v2
(Stage 3 v2, tag stage3-v2-20260416). Read-only; writes recount.csv next to itself.

Counting rule
-------------
* Scope: only the Stage 3 section "### §2 SRG / CLA -> RI / ER / EP Crosswalk"
  (from that heading to the next "### §3" heading). EP identifiers that occur only
  in §3-§6 (VQ judgement, shortest-reinforcement route, dictionary-contribution
  notes) are mentions, not assignments, and are not counted (reported separately
  as n_EP_anywhere for sensitivity).
* SRG: a bold block heading line beginning "**SRG-<n>" inside §2. n_SRG = number of
  distinct <n>. CLA blocks (bold heading beginning "**CLA") are counted separately.
  A "SRG外：CLA" header with no CLA block (app1 s3v2: "CLA 登録しない") gives 0 CLA.
* EP assignment: the "* **EP**:" field of each SRG/CLA block, including indented
  continuation lines up to the next bullet / blank line. Every EP-<nn><letter>
  token in that field is assigned, whether listed first or as an auxiliary/secondary
  pack (e.g. "EP-05a ...（RI-05 補助）") and whether marked provisional
  ("EP-10a ...（暫定）").
* n_EP_SRG  = distinct EPs assigned to SRG blocks only.
  n_EP_all  = distinct EPs assigned to SRG + CLA blocks (headline count: the
  manuscript speaks of "EP types per paper", and CLA-linked EPs are EPs of the record).
"""
import csv, re, pathlib, collections

ROOT = pathlib.Path(__file__).resolve().parents[4]   # uqs-project
TEST = ROOT / "papers" / "test"
# Zenodo deposit of Paper A (2026-10-17): the ten papers are in Tier 3 (reviewer version only) and the CSV is written to
# rerun_output/ at the deposit root; the `file` column keeps the project path, as in the deposited recount.csv
DEPOSIT = not TEST.is_dir()
if DEPOSIT:
    ROOT = pathlib.Path(__file__).resolve().parents[2]
    TEST = ROOT / "tier_3_stage_outputs" / "test_set"
PAPERS = [("hom1","HOM"),("hom2","HOM"),("het1","HET"),("het2","HET"),
          ("comp1","COMP"),("comp2","COMP"),("app1","APP"),("app2","APP"),
          ("scr1","SCR"),("scr2","SCR")]
EP_RE = re.compile(r"EP-\d{2}[a-z]")
HEAD_RE = re.compile(r"^(?:#+\s*)?\*{0,2}\s*(SRG-(\d+)|CLA[-\w]*)")

def parse(path):
    txt = path.read_text(encoding="utf-8").splitlines()
    meta = {"prompt_version":"", "model_info":""}
    for l in txt[:6]:
        if l.startswith("prompt_version:"): meta["prompt_version"]=l.split(":",1)[1].strip()
        if l.startswith("model_info:"): meta["model_info"]=l.split(":",1)[1].strip()
    # section §2
    s = next(i for i,l in enumerate(txt) if l.startswith("###") and "§2" in l)
    e = next(i for i,l in enumerate(txt) if i>s and l.startswith("###") and "§3" in l)
    sec = txt[s+1:e]
    srgs, clas = [], []
    ep_srg, ep_cla = collections.OrderedDict(), collections.OrderedDict()
    cur = None; in_ep = False
    for l in sec:
        st = l.strip()
        if st.startswith("**SRG-") or st.startswith("**CLA"):
            m = re.match(r"\*\*(SRG-(\d+)|CLA[^*\s:：\[「]*)", st)
            if m and "外" not in st:
                if m.group(2):
                    cur = ("SRG", "SRG-"+m.group(2)); srgs.append(cur[1])
                else:
                    cur = ("CLA", f"CLA#{len(clas)+1}"); clas.append(cur[1])
            in_ep = False; continue
        if re.match(r"^[*-] \*\*EP\*\*", st):
            in_ep = True; chunk = st
        elif in_ep and l.startswith("  ") and st and not re.match(r"^[*-] ", st):
            chunk = st
        else:
            in_ep = False; continue
        if cur is None: continue
        tgt = ep_srg if cur[0]=="SRG" else ep_cla
        for ep in EP_RE.findall(chunk):
            tgt.setdefault(ep, []).append(cur[1])
    ep_all = list(dict.fromkeys(list(ep_srg)+list(ep_cla)))
    anywhere = sorted(set(EP_RE.findall("\n".join(txt))))
    return meta, sorted(set(srgs), key=lambda x:int(x[4:])), clas, sorted(ep_srg), sorted(ep_all), anywhere

rows = []
for pid, cat in PAPERS:
    for stage in ("s3","s3v2"):
        f = TEST/pid/f"{pid}_v17_sonnet_{stage}.md"
        meta, srgs, clas, eps, epall, anyw = parse(f)
        rows.append(dict(paper=pid, category=cat, stage3=stage,
            file=(str(pathlib.PurePosixPath("papers", "test", pid, f.name)) if DEPOSIT else str(f.relative_to(ROOT))), s0_s2_prompt="v17",
            stage3_prompt_tag=meta["prompt_version"], model_info=meta["model_info"],
            n_SRG=len(srgs), n_CLA=len(clas),
            n_EP_SRG=len(eps), n_EP_all=len(epall), EP_all=";".join(epall),
            EP_CLA_only=";".join(x for x in epall if x not in eps),
            n_EP_anywhere=len(anyw), EP_anywhere_extra=";".join(x for x in anyw if x not in epall)))

out = pathlib.Path(__file__).with_name("recount.csv")
if DEPOSIT:
    out = ROOT / "rerun_output" / "01_response" / "r34_recount" / "recount.csv"; out.parent.mkdir(parents=True, exist_ok=True)
with out.open("w", newline="", encoding="utf-8") as fh:
    w = csv.DictWriter(fh, fieldnames=list(rows[0])); w.writeheader(); w.writerows(rows)

for stage in ("s3","s3v2"):
    R = [r for r in rows if r["stage3"]==stage]
    print(f"\n== Stage 3 file {stage}")
    for r in R:
        print(f"{r['paper']:6}{r['category']:5} SRG={r['n_SRG']} CLA={r['n_CLA']} EP_SRG={r['n_EP_SRG']} EP_all={r['n_EP_all']} [{r['EP_all']}] anywhere_extra={r['EP_anywhere_extra']} model={r['model_info'][:30]}")
    rng = lambda k: (min(r[k] for r in R), max(r[k] for r in R))
    print("ranges: SRG", rng("n_SRG"), "EP_SRG", rng("n_EP_SRG"), "EP_all", rng("n_EP_all"))
    for key in ("EP_all",):
        percat = collections.defaultdict(set); perpaper = []
        for r in R:
            s=set(r[key].split(";")); percat[r["category"]] |= s; perpaper.append(s)
        allcat = set.intersection(*percat.values()); allpap = set.intersection(*perpaper)
        print("EP present in >=1 paper of every category:", sorted(allcat))
        print("EP present in every paper:", sorted(allpap))
        five = ["EP-01a","EP-03a","EP-06a","EP-07a","EP-08a"]
        for ep in five:
            miss = [r["paper"] for r,s in zip(R,perpaper) if ep not in s]
            print(f"  {ep}: in {10-len(miss)}/10 papers; missing in {miss}")
