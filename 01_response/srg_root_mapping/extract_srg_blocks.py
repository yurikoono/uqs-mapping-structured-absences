#!/usr/bin/env python3
"""Extract SRG/CLA blocks from the §2 section of Kumada 1972 Stage 3 outputs (7 outputs + the Sonnet reference). Run from repo root."""
import json, random, re
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
SRC = {
 "sonnet46_2026-04": "papers/dev/kumada/kumada_v17_sonnet_s3v2.md",
 "haiku45_2026-04": "papers/dev/kumada/kumada_v17_haiku_s3v2.md",
 "opus47_2026-04": "papers/dev/kumada/kumada_v17_opus47_s3v2.md",
 "gpt54thinking_2026-04": "papers/dev/kumada/gpt54thinking/kumada_v17_gpt54thinking_s3.md",
 "haiku45_2026-09_run1": "papers/dev/kumada/haiku45_repro_2026-09/kumada_v17_haiku45_repro_run1_s3v2.md",
 "haiku45_2026-09_run2": "papers/dev/kumada/haiku45_repro_2026-09/kumada_v17_haiku45_repro_run2_s3v2.md",
 "haiku45_2026-09_run3": "papers/dev/kumada/haiku45_repro_2026-09/kumada_v17_haiku45_repro_run3_s3v2.md",
}
HEAD = re.compile(r"^\s*(?:#{2,4}\s*)?\*\*\s*(SRG[-\s]?[0-9α-ωA-Za-z]+|CLA[-\s]?[0-9]*)\b[^\n]*", re.M)
def section2(t):
    a = re.search(r"^#{2,3}\s*§\s*2\b.*$", t, re.M)
    b = re.search(r"^#{2,3}\s*§\s*3\b.*$", t, re.M)
    return t[a.end(): b.start()] if a and b else t
out, key = [], {}
rng = random.Random(20260929)
for name, p in SRC.items():
    # deposit: the 2026-04 outputs of the project folder papers/dev/kumada/ are in Tier 3 (reviewer version only)
    s2 = section2(open(_src(p, p.replace("papers/dev/kumada/", "tier_3_stage_outputs/dev_set/kumada/", 1)
                            if "/haiku45_repro_2026-09/" not in p else p)).read())
    hs = [m for m in HEAD.finditer(s2) if not re.search(r"の RI-|co-?occur|共起", m.group(0))]
    for i, m in enumerate(hs):
        end = hs[i+1].start() if i + 1 < len(hs) else len(s2)
        blk = s2[m.start():end].strip()
        cid = f"S{rng.randrange(10**6):06d}"
        key[cid] = {"output": name, "heading": m.group(0).strip()[:120]}
        out.append({"block": cid, "text": blk})
    print(name, len(hs), [h.group(1) for h in hs])
rng.shuffle(out)
D = _out("manuscript_A/DigitalDiscovery_R1/01_response/srg_root_mapping", "01_response/srg_root_mapping")
json.dump(out, open(f"{D}/srg_blocks_packets.json", "w"), ensure_ascii=False, indent=1)
json.dump(key, open(f"{D}/srg_blocks_key.json", "w"), ensure_ascii=False, indent=1)
print(len(out), "blocks")
