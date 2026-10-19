#!/usr/bin/env python3
"""v2 (re-adjudication with B2; prereg B2 section). Build adjudication packets (rubric adjudication_rubric_20260929.md, step 1). Run from repo root.
Each (run, axis, scope) cell gets every line matching a broad candidate pattern (+-1 line), under a random cell ID.
The key mapping cell ID -> (arm, run, scope) is written separately and not shown to Rater 2."""
import importlib.util, json, random, re, sys
# Paths (2026-10-17). In the project repository this script is run from the repository root, as before, and every path
# below is the repository path. Inside the Zenodo deposit of Paper A it can be run from any directory: an input that is not
# found relative to the working directory is read from the deposit (`_src`), the implementations come from
# tier_7_aggregation_scripts_and_methodology_evolution/lib/, and outputs go to rerun_output/ at the deposit root (`_out`),
# so the deposited results are not overwritten and can be compared with the re-run.
import os as _os
_DEP = _os.path.abspath(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), "..", ".."))
_LIB = "tier_7_aggregation_scripts_and_methodology_evolution/lib/"
def _src(repo, dep=None):
    return repo if _os.path.exists(repo) else _os.path.join(_DEP, repo if dep is None else dep)
def _out(repo, dep):
    if _os.path.isdir(repo):
        return repo
    d = _os.path.join(_DEP, "rerun_output", dep); _os.makedirs(d, exist_ok=True); return d
sys.argv = ["x"]
spec = importlib.util.spec_from_file_location("rx", _src("scripts/repro_extract.py", _LIB + "repro_extract.py")); rx = importlib.util.module_from_spec(spec); spec.loader.exec_module(rx)
D = _out("manuscript_A/DigitalDiscovery_R1/01_response/d4_baseline", "01_response/d4_baseline")
R = _src("papers/dev/kumada/repro_2026-07"); B = _src("papers/dev/kumada/baseline_R1_2026-09")
canon = json.load(open(f"{R}/canon.json"))
BROAD = {
 "homocoupling": r"homo|R–R|R-R|R′–R′|dispropor|by-?product|副生|ホモ",
 "black_precipitate": r"black|黒|Ni\s*\(0\)|Ni⁰|Ni0|nickel\s*\(0\)|zero-?valent|0価|particle|粒子|colloid|heterogen|不均一|decompos|分解|precipit|沈殿",
 "exotherm_radical": r"exotherm|発熱|radical|ラジカル|odd-?electron|single-?electron|Ni\s*\(I\)|Ni\(III\)|heat",
 "stereo_nonspec": r"stereo|立体|cis|trans|80\s*:\s*20|43\s*:\s*57|isomer|異性",
 "ligand_ranking": r"\bdpp\b|\bdpe\b|dmpe|activity.{0,20}order|序列|ligand|配位子|bidentate|二座",
 "glpc_standard": r"glpc|GLPC|GLC|\bGC\b|gas chromat|internal standard|内部標準|response factor|応答係数|calibrat|検量|isolated yield|単離収率|yield basis",
 "ether_thf": r"ether|エーテル|\bTHF\b|tetrahydrofuran|solvent|溶媒",
}
for k, v in canon.items():  # the broad pattern must be a superset of the canon regex
    BROAD[k] = BROAD[k] + "|" + v
def snippets(text, pat):
    L = text.split("\n"); out = []
    for i, l in enumerate(L):
        if re.search(pat, l, re.I):
            out.append("\n".join(x for x in L[max(0, i-1):i+2] if x.strip()))
    return out
cells = []
for k in range(1, 6):
    s1 = open(f"{R}/kumada_v184_sonnet46_repro_run{k}_s1.md").read(); s2 = open(f"{R}/kumada_v184_sonnet46_repro_run{k}_s2.md").read()
    _, _, lines = rx.count_items(s1)
    cells.append(("uqs_v184", k, "loose", s1 + "\n" + s2))
    cells.append(("uqs_v184", k, "strict", "\n".join(lines) + "\n" + rx.d4_section(s2)))
    for arm in ("bl0", "bl1", "bl2"):
        cells.append((arm, k, "loose", open(f"{B}/kumada_{arm}_sonnet46_run{k}.md").read()))
rng = random.Random(20260930); packets, key = [], {}
for arm, k, scope, text in cells:
    for ax, pat in BROAD.items():
        cid = f"C{rng.randrange(10**6):06d}"
        while cid in key: cid = f"C{rng.randrange(10**6):06d}"
        key[cid] = {"arm": arm, "run": k, "scope": scope, "axis": ax}
        sn = snippets(text, pat)
        packets.append({"cell": cid, "axis": ax, "n_snippets": len(sn), "snippets": sn})
rng.shuffle(packets)
json.dump(packets, open(f"{D}/adjudication_v2_packets.json", "w"), ensure_ascii=False, indent=1)
json.dump(key, open(f"{D}/adjudication_v2_key.json", "w"), indent=1)
print(len(packets), "cells;", sum(p["n_snippets"] == 0 for p in packets), "with no candidate line;",
      "total snippets", sum(p["n_snippets"] for p in packets))
