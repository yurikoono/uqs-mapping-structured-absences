#!/usr/bin/env python3
"""Haiku 4.5 replication of the SI-6 arm (prereg haiku45_replication/preregistration_haiku45_R1.md, commit 0b14dde).
Run from repo root. N=3 fresh processes in parallel; single context S0 -> S1 turn1-4 -> S2 -> S3 v2 (JA)."""
import json, subprocess, sys, pathlib, datetime, concurrent.futures as cf
OUT = pathlib.Path("papers/dev/kumada/haiku45_repro_2026-09"); MODEL = "claude-haiku-4-5"
PDF = "papers/dev/kumada/Kumada_1972.pdf"; P = "prompts/v17"; S3 = "prompts/stage2f3/prompt_stage3_v2.md"
LOG = OUT / "runs.log"
FILES = ["s0", "s1_turn1", "s1_turn2", "s1_turn3", "s1", "s2", "s3v2"]
def prompt(k):
    t = f"{OUT}/kumada_v17_haiku45_repro_run{k}"
    return f"""You are executing ONE independent UQS replicate. Do NOT consult or write papers/_database/uqs_analysis_registry.csv.
Do NOT run /record. Do NOT read any other UQS output anywhere in the repository.

TARGET PAPER: {PDF} is a JACS page carrying THREE communications. The target is the MIDDLE one:
Tamao, Sumitani & Kumada, "Selective Carbon-Carbon Bond Formation by Cross-Coupling of Grignard
Reagents with Organic Halides. Catalysis by Nickel-Phosphine Complexes." Use the Stage 0 boundary
procedure to isolate it (do not import the hydrosilylation paper before it or the chymotrypsin
paper after it).

PROMPTS: use ONLY these canonical files, exactly as written:
  {P}/prompt_stage0_v17.md
  {P}/prompt_stage1_turn1_v17.md, {P}/prompt_stage1_turn2_v17.md, {P}/prompt_stage1_turn3_v17.md, {P}/prompt_stage1_turn4_v17.md
  {P}/prompt_stage2_v17.md
  {S3}
RUN: in THIS single context (do not split), read the PDF and execute S0 -> S1 turn1 -> turn2 -> turn3 -> turn4 -> S2 -> S3.

SAVE each stage verbatim (the exact prompt-defined output, no extra commentary) with the Write tool to:
""" + "\n".join(f"  {t}_{f}.md" for f in FILES) + "\nEnd your reply with the literal token RUN_COMPLETE after all seven files are written."
def run(k):
    t = OUT / f"kumada_v17_haiku45_repro_run{k}"
    if pathlib.Path(f"{t}_s3v2.md").exists(): return k, "skip"
    with open(LOG, "a") as f: print(f"[run ] run{k} {datetime.datetime.now().isoformat(timespec='seconds')}", file=f)
    r = subprocess.run(["claude", "-p", "--model", MODEL, "--output-format", "json", "--allowedTools", "Read", "Write"],
                       input=prompt(k), capture_output=True, text=True)
    pathlib.Path(f"{OUT}/_run{k}_cli.json").write_text(r.stdout + ("\n--stderr--\n" + r.stderr if r.stderr else ""))
    try: j = json.loads(r.stdout); models = sorted(j.get("modelUsage", {})); res = j.get("result", "")
    except Exception: models, res = [], ""
    missing = [f for f in FILES if not pathlib.Path(f"{t}_{f}.md").exists()]
    ok = bool(models) and all(m.startswith("claude-haiku-4-5") for m in models)
    st = "done" if ok and not missing else ("MODEL" if not ok else "INCOMPLETE")
    with open(LOG, "a") as f: print(f"[{st}] run{k} {datetime.datetime.now().isoformat(timespec='seconds')} models={models} missing={missing}", file=f)
    return k, st
if __name__ == "__main__":
    with cf.ThreadPoolExecutor(3) as ex:
        for k, st in ex.map(run, [1, 2, 3]): print(k, st, flush=True)
