#!/usr/bin/env python3
"""B2 -> Stage 3 check (prereg d4_baseline/preregistration_B2_stage3.md, commit 052a74c). Run from repo root."""
import json, random, re, subprocess, pathlib, datetime, concurrent.futures as cf
O = pathlib.Path("papers/dev/kumada/b2_stage3_R1_2026-09"); MODEL = "claude-sonnet-4-6"
R = "papers/dev/kumada/repro_2026-07"; B = "papers/dev/kumada/baseline_R1_2026-09"
PDF = "papers/dev/kumada/Kumada_1972.pdf"; S3 = "prompts/stage2f3/prompt_stage3_v2_en.md"
ADAPTER = ("The file(s) below are the Stage 1/2 record of this paper. Apply the Stage 3 prompt to them and to the PDF. "
           "Where the prompt refers to a field the record does not contain, say so explicitly rather than supplying it.")
def stage():
    keyf = O / "_key.json"
    if keyf.exists(): return json.load(open(keyf))
    rng = random.Random(20260929); key = {}
    for arm in ("U", "B"):
        for k in range(1, 6):
            i = f"{rng.randrange(10**6):06d}"
            while i in key: i = f"{rng.randrange(10**6):06d}"
            key[i] = {"arm": arm, "run": k}
            d = O / f"in_{i}"; d.mkdir(exist_ok=True)
            if arm == "U":
                txt = "".join(f"--- file: {s} ---\n" + open(f"{R}/kumada_v184_sonnet46_repro_run{k}_{s}.md").read() + "\n" for s in ("s0", "s1", "s2"))
            else:
                txt = re.sub(r"^<!--.*?-->\n*", "", open(f"{B}/kumada_bl2_sonnet46_run{k}.md").read(), flags=re.S)
            (d / "record.md").write_text(txt)
    json.dump(key, open(keyf, "w"), indent=1); return key
def prompt(i):
    d = O / f"in_{i}"
    return f"""You are executing ONE Stage 3 analysis. Do NOT read any file other than the three named below. Do NOT consult the registry. Do NOT run /record.

TARGET PAPER: {PDF} is a JACS page carrying THREE communications. The target is the MIDDLE one:
Tamao, Sumitani & Kumada, "Selective Carbon-Carbon Bond Formation by Cross-Coupling of Grignard
Reagents with Organic Halides. Catalysis by Nickel-Phosphine Complexes." Analyse only that communication.

STAGE 3 PROMPT (apply exactly as written): {S3}
RECORD: {d}/record.md

{ADAPTER}

Write the Stage 3 output verbatim (the exact prompt-defined output, no extra commentary) with the Write tool to:
  {d}/s3.md
End your reply with the literal token RUN_COMPLETE."""
def run(i):
    d = O / f"in_{i}"
    if (d / "s3.md").exists(): return i, "skip"
    for att in (1, 2):
        r = subprocess.run(["claude", "-p", "--model", MODEL, "--output-format", "json", "--allowedTools", "Read", "Write"],
                           input=prompt(i), capture_output=True, text=True)
        (d / f"_cli_a{att}.json").write_text(r.stdout + ("\n--stderr--\n" + r.stderr if r.stderr else ""))
        try: j = json.loads(r.stdout); models = sorted(j.get("modelUsage", {}))
        except Exception: models = []
        ok = bool(models) and all(m.startswith("claude-sonnet-4-6") for m in models)
        st = "done" if ok and (d / "s3.md").exists() else ("MODEL" if not ok else "NO_OUTPUT")
        with open(O / "runs.log", "a") as f: print(f"[{st}] {i} a{att} {datetime.datetime.now().isoformat(timespec='seconds')} models={models}", file=f)
        if ok: return i, st
        if (d / "s3.md").exists(): (d / "s3.md").rename(d / f"s3_discarded_a{att}.md")
    return i, st
if __name__ == "__main__":
    key = stage()
    with cf.ThreadPoolExecutor(5) as ex:
        for i, st in ex.map(run, list(key)): print(i, st, flush=True)
