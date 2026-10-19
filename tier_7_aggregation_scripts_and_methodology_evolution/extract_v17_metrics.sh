#!/usr/bin/env bash
# Extract U / B / D-4 counts per paper from v17 Sonnet Stage 1 / Stage 2 outputs.
# Handles multiple format variants observed across the 12-paper test set:
#   B/U items:
#     - kumada-style: [B] B-1 | ...
#     - murai-style: [B] header then B-1 | ...
#     - hom2-style: [B-1] item_id: B-1
#   D-4 candidates:
#     - kumada-style: **D4-1: ...**
#     - murai/app1-style: **D-4候補1：...** or **D-4候補 1：...**
#     - app2/scr2-style: **D-4-1: ...**
#     - hom1-style: 【D-4候補1】 (full-width brackets)
#     - hom2/comp1/comp2/scr1-style: **候補1: ...** or 候補1: ... (no D-4 prefix)
#
# Output: CSV to stdout
set -e

count_items() {
  local file="$1"
  local letter="$2"  # B or U
  # Three definition patterns:
  #   1. [B] B-N at line start (kumada)
  #   2. B-N | at line start (murai, after [B] header)
  #   3. [B-N] at line start (hom2)
  grep -oE "(^\[$letter\] $letter-[0-9]+|^$letter-[0-9]+ \||^\[$letter-[0-9]+\])" "$file" 2>/dev/null \
    | sed -E "s/^\[$letter\] ($letter-[0-9]+).*/\1/" \
    | sed -E "s/^($letter-[0-9]+) \|.*/\1/" \
    | sed -E "s/^\[($letter-[0-9]+)\].*/\1/" \
    | sort -u | wc -l | tr -d ' '
}

count_d4() {
  local file="$1"
  # Multiple D-4 candidate definition patterns:
  #   - **D4-N: (kumada)
  #   - **D-4候補N: or **D-4候補 N: (murai, app1)
  #   - **D-4-N: (app2, scr2)
  #   - 【D-4候補N】 (hom1)
  #   - **候補N: or ^候補N: (hom2, comp1, comp2, scr1 — no D-4 prefix)
  # Normalise all to a single canonical "DN-N" ID, then dedupe by number.
  {
    grep -oE "(\*\*)?D4-[0-9]+" "$file" 2>/dev/null | sed -E "s/(\*\*)?D4-([0-9]+)/CAND-\2/"
    grep -oE "^(\*\*)?D-4候補 ?[0-9]+" "$file" 2>/dev/null | sed -E "s/^(\*\*)?D-4候補 ?([0-9]+).*/CAND-\2/"
    grep -oE "(\*\*)?D-4-[0-9]+" "$file" 2>/dev/null | sed -E "s/(\*\*)?D-4-([0-9]+)/CAND-\2/"
    grep -oE "【D-4候補[0-9]+】" "$file" 2>/dev/null | sed -E "s/【D-4候補([0-9]+)】/CAND-\1/"
    grep -oE "^(\*\*)?候補 ?[0-9]+" "$file" 2>/dev/null | sed -E "s/^(\*\*)?候補 ?([0-9]+).*/CAND-\2/"
  } | sort -u | wc -l | tr -d ' '
}

echo "paper,corpus,U_count,B_count,D4_count"

for pair in "kumada:dev" "murai:dev" "hom1:test" "hom2:test" "het1:test" "het2:test" "comp1:test" "comp2:test" "app1:test" "app2:test" "scr1:test" "scr2:test"; do
  paper="${pair%%:*}"
  set="${pair##*:}"
  base="<project-root>/papers/$set/$paper"
  s1="$base/${paper}_v17_sonnet_s1.md"
  s2="$base/${paper}_v17_sonnet_s2.md"

  u_count=$(count_items "$s1" "U")
  b_count=$(count_items "$s1" "B")
  d4_count=$(count_d4 "$s2")

  echo "$paper,$set,$u_count,$b_count,$d4_count"
done
