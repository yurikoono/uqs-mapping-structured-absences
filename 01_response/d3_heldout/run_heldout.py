#!/usr/bin/env python3
"""D3 held-out driver (prereg preregistration_D3_D4_R1.md §2.3, commit 88e7cc3). Run from repo root.
One fresh `claude -p` process per paper, single context: S0 -> S1 turn1-4 -> S2 EN -> Stage 3 v2 EN.
Model pinned to claude-sonnet-4-6 and verified from the CLI modelUsage field. Papers run in parallel."""
import json, subprocess, sys, pathlib, datetime, concurrent.futures as cf
ROOT = pathlib.Path("papers/paperA_heldout_R1"); MODEL = "claude-sonnet-4-6"
PAPERS = {"wang2026": "10.1021/acs.joc.6c01425", "liu2026": "10.1021/acs.orglett.6c03536",
          "wu2026": "10.31635/ccschem.026.202607864", "shekarizadeh2026": "10.1007/s44442-026-00106-5"}
P = "prompts/v184"; S3 = "prompts/stage2f3/prompt_stage3_v2_en.md"
LOG = ROOT / "runs.log"

def prompt(pid, doi):
    d = ROOT / pid; t = f"{pid}_v184_sonnet46"
    return f"""You are executing ONE UQS analysis for a pre-registered held-out evaluation (Paper A revision).
Do NOT consult or write papers/_database/uqs_analysis_registry.csv. Do NOT run /record. Do NOT read any other
UQS output anywhere in the repository; this paper must be analysed without reference to prior analyses.

PAPER: {d}/{pid}.pdf (DOI {doi}). Supporting Information: {d}/{pid}_si.pdf (you may consult it as the paper's SI).
Read the main PDF with the Read tool directly (multimodal; use the pages parameter for >20 pages).

PROMPTS: use ONLY these canonical prompt files, exactly as written:
  {P}/prompt_stage0_v184.md
  {P}/prompt_stage1_turn1_v184.md, {P}/prompt_stage1_turn2_v184.md, {P}/prompt_stage1_turn3_v184.md,
  {P}/prompt_stage1_turn4_v184.md   (do NOT use any *pilot* / *textbook* variants)
  {P}/prompt_stage2_v184_en.md      (English Stage 2)
  {S3}                              (Stage 3 v2, English)

RUN: in THIS single context (do not split), execute S0 -> S1 turn1 -> turn2 -> turn3 -> turn4 -> S2 -> S3, exactly per
the prompts. Stage 2 and Stage 3 must see the full PDF + all earlier outputs in context.

MODEL GUARD: after S0, check its model_info. If it is not "claude-sonnet-4-6", STOP, write only the S0 file, and end
your reply with the literal token MODEL_MISMATCH.

SAVE each stage verbatim (the exact prompt-defined output, no extra commentary) with the Write tool to:
  {d}/{t}_s0.md
  {d}/{t}_s1_turn1.md
  {d}/{t}_s1_turn2.md
  {d}/{t}_s1_turn3.md
  {d}/{t}_s1.md          (turn 4 = final S1)
  {d}/{t}_s2_en.md
  {d}/{t}_s3v2_en.md
End your reply with the literal token RUN_COMPLETE after all seven files are written."""

def run(pid):
    doi = PAPERS[pid]; d = ROOT / pid; t = f"{pid}_v184_sonnet46"
    if (d / f"{t}_s3v2_en.md").exists():
        return pid, "skip"
    ts = datetime.datetime.now().isoformat(timespec="seconds")
    with open(LOG, "a") as f: print(f"[run ] {pid} {ts}", file=f)
    r = subprocess.run(["claude", "-p", "--model", MODEL, "--output-format", "json",
                        "--allowedTools", "Read", "Write"], input=prompt(pid, doi), capture_output=True, text=True)
    (d / f"_{t}_cli.json").write_text(r.stdout + ("\n--stderr--\n" + r.stderr if r.stderr else ""))
    try:
        j = json.loads(r.stdout); models = sorted(j.get("modelUsage", {})); res = j.get("result", "")
    except Exception:
        models, res = [], ""
    files = ["s0", "s1_turn1", "s1_turn2", "s1_turn3", "s1", "s2_en", "s3v2_en"]
    missing = [s for s in files if not (d / f"{t}_{s}.md").exists()]
    ok_model = bool(models) and all(m.startswith("claude-sonnet-4-6") for m in models)
    status = "done" if ok_model and not missing and "RUN_COMPLETE" in res else \
             ("MODEL" if not ok_model or "MODEL_MISMATCH" in res else "INCOMPLETE")
    with open(LOG, "a") as f:
        print(f"[{status}] {pid} {datetime.datetime.now().isoformat(timespec='seconds')} models={models} missing={missing}", file=f)
    return pid, status

if __name__ == "__main__":
    ids = sys.argv[1:] or list(PAPERS)
    with cf.ThreadPoolExecutor(len(ids)) as ex:
        for pid, st in ex.map(run, ids):
            print(pid, st, flush=True)
