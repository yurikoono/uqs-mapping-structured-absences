#!/usr/bin/env python3
"""D1 item draw + rewrite (prereg preregistration_D1_itemwise.md, commits c3673f8/499d91e). Run from repo root."""
import importlib.util, json, random, re, subprocess, sys
sys.argv = ["x"]
spec = importlib.util.spec_from_file_location("rx", "scripts/repro_extract.py"); rx = importlib.util.module_from_spec(spec); spec.loader.exec_module(rx)
D = "manuscript_A/DigitalDiscovery_R1/01_response/d1_expert"; R = "papers/dev/kumada/repro_2026-07"
s1 = open(f"{R}/kumada_v184_sonnet46_repro_run1_s1.md").read(); s2 = open(f"{R}/kumada_v184_sonnet46_repro_run1_s2.md").read()
_, _, s1_items = rx.count_items(s1)
d4 = rx.d4_section(s2)
hs = [m.start() for m in re.finditer(r"^\*\*候補 D-4-\d+", d4, re.M)]
d4_items = [d4[a:b].strip() for a, b in zip(hs, hs[1:] + [len(d4)])]
assert len(s1_items) == 13 and len(d4_items) == 8, (len(s1_items), len(d4_items))
rng = random.Random(20261001)
pick1 = rng.sample(range(13), 7); pick2 = rng.sample(range(8), 3)
drawn = [("S1", i, s1_items[i]) for i in pick1] + [("D4", i, d4_items[i]) for i in pick2]
PROMPT = open(f"{D}/preregistration_D1_itemwise.md").read().split("```\n")[1].split("```")[0].rstrip() + "\n"
out = []
for typ, i, txt in drawn:
    r = subprocess.run(["claude", "-p", "--model", "claude-sonnet-4-6", "--output-format", "json"], input=PROMPT + txt, capture_output=True, text=True)
    j = json.loads(r.stdout); models = sorted(j.get("modelUsage", {}))
    assert models and all(m.startswith("claude-sonnet-4-6") for m in models), models
    out.append({"type": typ, "pool_index": i, "source": txt, "rewrite": j["result"].strip(), "models": models})
    print(typ, i, "|", j["result"].strip()[:120], flush=True)
order = list(range(10)); rng.shuffle(order)
for n, k in enumerate(order, 1): out[k]["form_no"] = n
json.dump(out, open(f"{D}/items_drawn_rewritten.json", "w"), ensure_ascii=False, indent=1)
