#!/usr/bin/env bash
# repro_driver.sh — UQS reproducibility experiment, Phase 1 (kumada, N=5, v18.4 + v19)
# RUN FROM REPO ROOT. Model is HARD-PINNED to claude-sonnet-4-6 (the frozen baseline).
# Each replicate = one fresh `claude -p` process = independent context (single-context
# S0->S1(4 turns)->S2 per pipeline spec). Resumable: cells with a valid _s2.md are skipped.
set -uo pipefail

MODEL="claude-sonnet-4-6"
N="${N:-5}"                       # replicates per version (override: N=3 bash repro_driver.sh)
VERSIONS=(v184 v19)
OUT="papers/dev/kumada/repro_2026-07"
PDF="papers/dev/kumada/Kumada_1972.pdf"
RUNLOG="$OUT/runs.log"
mkdir -p "$OUT/logs" "$OUT/quarantine"

# ---- preflight ----------------------------------------------------------------
fail() { echo "PREFLIGHT FAIL: $*" >&2; exit 1; }
command -v claude >/dev/null 2>&1 || fail "'claude' CLI not found on PATH."
[ -f "$PDF" ] || fail "PDF not found: $PDF (run from repo root)."
for v in "${VERSIONS[@]}"; do
  for p in prompt_stage0 prompt_stage1_turn1 prompt_stage1_turn2 \
           prompt_stage1_turn3 prompt_stage1_turn4 prompt_stage2; do
    ls "prompts/$v/${p}_${v}.md" >/dev/null 2>&1 || fail "missing prompt: prompts/$v/${p}_${v}.md"
  done
done
echo "[preflight] ok. model=$MODEL N=$N versions=${VERSIONS[*]}" | tee -a "$RUNLOG"
echo "[preflight] NOTE: confirm 'claude --model $MODEL' actually yields claude-sonnet-4-6." \
     "Any run whose S0 model_info != $MODEL is quarantined below." | tee -a "$RUNLOG"

# ---- run loop -----------------------------------------------------------------
for ver in "${VERSIONS[@]}"; do
  PDIR="prompts/$ver"
  for k in $(seq 1 "$N"); do
    tag="kumada_${ver}_sonnet46_repro_run${k}"
    s0="$OUT/${tag}_s0.md"; s1="$OUT/${tag}_s1.md"; s2="$OUT/${tag}_s2.md"

    # resume: skip if s2 exists and its paired s0 confirms 4.6
    if [ -f "$s2" ] && grep -q "claude-sonnet-4-6" "$s0" 2>/dev/null; then
      echo "[skip] $tag (already complete, model ok)" | tee -a "$RUNLOG"; continue
    fi

    echo "[run ] $tag $(date '+%F %T')" | tee -a "$RUNLOG"
    PROMPT=$(cat <<EOF
You are executing ONE independent UQS reproducibility replicate. Do NOT consult or write the
production registry (papers/_database/uqs_analysis_registry.csv). Do NOT run /record.

TARGET PAPER: $PDF is a JACS page carrying THREE communications. The target is the MIDDLE one:
Tamao, Sumitani & Kumada, "Selective Carbon-Carbon Bond Formation by Cross-Coupling of Grignard
Reagents with Organic Halides. Catalysis by Nickel-Phosphine Complexes." Use the Stage 0 boundary
procedure to isolate it (do not import the hydrosilylation paper before it or the chymotrypsin
paper after it).

PROMPTS: use ONLY the canonical prompt files in $PDIR:
  ${PDIR}/prompt_stage0_${ver}.md
  ${PDIR}/prompt_stage1_turn1_${ver}.md ... prompt_stage1_turn4_${ver}.md
  ${PDIR}/prompt_stage2_${ver}.md
(Do NOT use any *pilot* / *textbook* turn4 variants.)

RUN: in THIS single context (do not split), read the PDF and execute S0 -> S1 turn1 -> turn2 ->
turn3 -> turn4 -> S2, exactly per the prompts. Stage 2 must see the full PDF+S0+turn1-3 context.

MODEL GUARD: after S0, check its model_info. If it is not "claude-sonnet-4-6", STOP immediately,
write only the S0 file, and end your reply with the literal token MODEL_MISMATCH so the driver can
quarantine this run.

SAVE each stage verbatim (the exact prompt-defined output, no extra commentary) to:
  $s0
  $s1
  $s2
EOF
)
    claude -p --model "$MODEL" "$PROMPT" >"$OUT/logs/${tag}.log" 2>&1

    # ---- post-run verification ----
    status="ok"
    if grep -q "MODEL_MISMATCH" "$OUT/logs/${tag}.log" 2>/dev/null; then status="model_mismatch"; fi
    if [ ! -f "$s0" ]; then status="no_s0"; fi
    if [ -f "$s0" ] && ! grep -q "claude-sonnet-4-6" "$s0" 2>/dev/null; then status="model_mismatch"; fi
    if [ "$status" = "ok" ] && { [ ! -f "$s1" ] || [ ! -f "$s2" ]; }; then status="incomplete"; fi

    if [ "$status" = "model_mismatch" ]; then
      mv -f "$s0" "$s1" "$s2" "$OUT/quarantine/" 2>/dev/null
      echo "[QUAR] $tag -> quarantine ($status). Model pin not satisfied." | tee -a "$RUNLOG"
    elif [ "$status" != "ok" ]; then
      echo "[WARN] $tag status=$status (see $OUT/logs/${tag}.log)" | tee -a "$RUNLOG"
    else
      echo "[done] $tag ok" | tee -a "$RUNLOG"
    fi
  done
done

echo "[driver] finished $(date '+%F %T'). Next: python3 $OUT/repro_extract.py" | tee -a "$RUNLOG"
