#!/usr/bin/env python3
"""D4 single-prompt baseline driver (Paper A R1 prereg, commit 88e7cc3). Run from repo root.
Prompts are extracted verbatim from the frozen prereg code blocks."""
import json, re, subprocess, sys, pathlib, datetime
PRE = pathlib.Path("manuscript_A/DigitalDiscovery_R1/01_response/preregistration_D3_D4_R1.md")
OUT = pathlib.Path("papers/dev/kumada/baseline_R1_2026-09")
MODEL = "claude-sonnet-4-6"
blocks = re.findall(r"```\n(.*?)```", PRE.read_text(), re.S)
pre, b0, b1x = blocks[0], blocks[1], blocks[2]
b2x = blocks[-1]
PROMPTS = {"bl0": pre + "\n" + b0, "bl1": pre + "\n" + b0 + "\n" + b1x, "bl2": pre + "\n" + b0 + "\n" + b1x + "\n" + b2x}
ARMS = sys.argv[2].split(",") if len(sys.argv) > 2 else list(PROMPTS)
N = int(sys.argv[1]) if len(sys.argv) > 1 else 5
log = open(OUT / "runs.log", "a")
for arm, prompt in [(a, PROMPTS[a]) for a in ARMS]:
    (OUT / f"prompt_{arm}.txt").write_text(prompt)
    for k in range(1, N + 1):
        out = OUT / f"kumada_{arm}_sonnet46_run{k}.md"
        if out.exists():
            print(f"[skip] {out.name}", file=log, flush=True); continue
        for attempt in range(1, 4):
            r = subprocess.run(["claude", "-p", "--model", MODEL, "--output-format", "json",
                                "--allowedTools", "Read"], input=prompt, capture_output=True, text=True)
            raw = OUT / "logs" / f"kumada_{arm}_run{k}_a{attempt}.json"
            raw.write_text(r.stdout + ("\n--stderr--\n" + r.stderr if r.stderr else ""))
            try:
                d = json.loads(r.stdout); models = sorted(d.get("modelUsage", {}))
            except Exception:
                d, models = {}, []
            ok = models and all(m.startswith("claude-sonnet-4-6") for m in models) and not d.get("is_error")
            ts = datetime.datetime.now().isoformat(timespec="seconds")
            print(f"[{'done' if ok else 'QUAR'}] {arm} run{k} a{attempt} {ts} models={models}", file=log, flush=True)
            if ok:
                out.write_text(f"<!-- model_info: {','.join(models)} | arm: {arm} | prereg: 88e7cc3 | {ts} -->\n\n" + d["result"])
                break
