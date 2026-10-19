#!/usr/bin/env python3
"""repro_extract.py — deterministic metric extraction for UQS reproducibility experiments.

Generalized from the kumada Phase 1 version (papers/dev/kumada/repro_2026-07/) on 2026-07-20
for Phase 2 (hom1/hom2 measurement platform, see
improvements/_prompts/repro_phase2_platform_audit_hom_20260720.md):

  * per-paper canonical-finding axes come from a JSON config (<dir>/canon.json by default)
    instead of a hard-coded kumada dictionary;
  * canonical coverage is now TWO instruments (two-instrument disagreement discipline):
      - canon_strict : axis regex hits within the FINAL taxonomy — the single-line
        "[X] X-n | ..." items (which carry all fields incl. note bodies) plus the S2 D-4
        section. Reading: "a reader of the final taxonomy learns this finding."
      - canon_loose  : axis regex hits anywhere in the final artifacts — full *_s1.md +
        *_s2.md text, incl. the question-disposition ledger, META, TEMPERATURE_SUMMARY,
        and all S2 sections. Reading: "the finding surfaced somewhere in the run."
    strict <= loose by construction. A strict=0/loose=1 cell means the finding surfaced
    during the turns but did not reach the final taxonomy under the axis vocabulary ->
    spot-check target. loose=0 means the finding is genuinely absent from the run's final
    artifacts. (Phase 1 history: the single-instrument proxy scored v19 exotherm-radical
    as "missed" in runs whose disposition ledger discussed the radical pathway — an
    artifact this split makes visible instead of hiding.)
  * scan directory, model pin, and output path are CLI arguments.

Count metrics (nA..nD4, severity, scope_type) are unchanged from Phase 1. Item ids
(U-1, U-2, ...) are NOT stable across runs; cross-run identity is by content signature.

Usage:
    python3 scripts/repro_extract.py papers/dev/kumada/repro_2026-07
    python3 scripts/repro_extract.py papers/test/hom1/repro_2026-XX --canon canon_hom1.json

canon.json format (flat): {"axis_name": "python regex, searched case-insensitively", ...}
Do NOT author a new paper's canon single-model/ad hoc — define it by multi-arm consensus
BEFORE the repro runs (see the platform-audit memo, next-action 1).
"""
import argparse, csv, glob, json, os, re, sys

# item-definition line patterns (both v18.4 and v19 use "[X] X-n | ...";
# in the final turn-4 artifact each item is ONE physical line carrying all fields)
DEF = {c: re.compile(r'^\s*\[' + c + r'\]\s*' + c + r'-(\d+)\b') for c in 'ABCU'}
SEV = re.compile(r'severity:\s*(critical|high|medium|low)', re.I)
# Six D-4 output formats observed across runs:
#   A: "**候補 D-4-1: …"               → D4_LABEL  counts unique N in "D-4-N"
#   B: "D-4 候補数: 9" + prose          → D4_SUMMARY extracts the declared count
#   C: "**D-4 候補 1（…）: …"          → D4_LABEL_C counts "D-4 候補 N"
#   D: "[D-4] 候補N: title" per cand.  → D4_LABEL_D counts "[D-4] 候補N" lines
#   E: "候補1（grounded_in: …"          → D4_LABEL_E counts line-initial "候補 N"
#   F: 無ラベルの field block の連続      → ラベルが無いので grounded_in 行数で数える
#   G: [D-4] + 逐語 essay（番号なし）    → 数えられない = **空欄**（0 ではない）
#
# 2026-07-30 修正（Entry 091）。`nD4=0` が 3 つの別物を同じ 0 で表していた:
#   ① 見出し変種で section 検出が落ちた（`## D-4: Candidate research questions` は
#      旧 D4_START のどの形にも当たらず start=None → section 空 → 0）
#   ② ラベルの無い候補 block（F）→ ラベル 0 件 → 0
#   ③ 番号なし essay（G）→ 「数えられない」を 0 と書いていた
# ①②は取りこぼし、③は欠測。**いずれも「候補が 0 件だった」という測定ではない**のに
# repro_aggregate が平均に入れていた。→ 検出を広げ、数え方を `nD4_method` 列で開示し、
# 数えられない場合は空欄にして集計から外す。
D4_LABEL   = re.compile(r'\bD-4-(\d+)\b')
D4_SUMMARY = re.compile(r'D-4\s*候補数[:：]\s*(\d+)')
D4_LABEL_C = re.compile(r'\bD-4\s*候補\s+(\d+)\b')
D4_LABEL_D = re.compile(r'^\[D-4\]\s*候補(\d+)\b', re.M)
# E: line-initial "候補 N" in any dress — bare ("候補 1"), bold-titled
# ("**候補 1: …**"), or paren ("候補1（…"). The `^\**候補\s*(\d+)` anchor excludes
# "候補数:" (数 is not a digit), mid-line mentions ("…SRG-3（候補 1）…"), and
# anchoring_note lines ("anchoring_note: … D-4 候補 1 …") — all non-line-initial.
D4_LABEL_E = re.compile(r'^\**候補\s*(\d+)', re.M)
D4_START   = re.compile(r'\[D-4\]|\bD-4-\d+\b|\bD-4\s*候補|^#{1,4}[ \t]*\**\s*D-4')
# 見出し形を許すと、候補本体より前に出る**準備/自己チェック見出し**（実出力に
# `### D-4 生成前準備` / `### D-4 前出力自己チェック` / `### D-4 優先順位構造` がある）で
# section が始まってしまい、checklist 中の行頭「候補 N」を数えて逆に過大になりうる。
# ∴ 見出し由来の start はこれらの語を含む行を飛ばす。
D4_HEAD_SKIP = re.compile(r'生成前準備|自己チェック|優先順位|self-?check|preparation', re.I)
GROUNDED_IN = re.compile(r'^\s*grounded_in\s*:', re.M)
SCOPE = re.compile(r'scope_type:\s*"?([a-z_]+)"?', re.I)


def load_canon(path):
    try:
        with open(path, encoding='utf-8') as f:
            raw = json.load(f)
    except FileNotFoundError:
        sys.exit(f'canon config not found: {path}\n'
                 'Create it as {"axis_name": "regex", ...} — for a NEW paper, define the axes '
                 'by multi-arm consensus first (platform-audit memo, next-action 1).')
    if not raw or not isinstance(raw, dict):
        sys.exit(f'canon config {path} must be a non-empty flat JSON object.')
    return {k: re.compile(v, re.I) for k, v in raw.items()}


def count_items(s1_text):
    counts, sev = {}, {'critical': 0, 'high': 0, 'medium': 0, 'low': 0}
    item_lines = []
    for cat, pat in DEF.items():
        ids = set()
        for line in s1_text.splitlines():
            m = pat.match(line)
            if m:
                ids.add(int(m.group(1)))
                item_lines.append(line)
                if cat == 'U':
                    sm = SEV.search(line)
                    if sm:
                        sev[sm.group(1).lower()] += 1
        counts[cat] = len(ids)
    return counts, sev, item_lines


def d4_section(s2_text):
    # from [D-4] header (or first D-4-N label) to the E section
    lines = s2_text.splitlines()
    start = next((i for i, l in enumerate(lines)
                  if D4_START.search(l) and not D4_HEAD_SKIP.search(l)), None)
    if start is None:
        return ''
    end = next((i for i, l in enumerate(lines[start:], start)
                if re.search(r'questions_that_cannot_be_asked|^\[E\]|射程の問', l)), len(lines))
    return '\n'.join(lines[start:end])


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('dir', nargs='?', default='.',
                    help='directory containing *_repro_run*_s{0,1,2}.md (default: cwd)')
    ap.add_argument('--canon', default=None,
                    help='canonical-axes JSON (default: <dir>/canon.json)')
    ap.add_argument('--model-pin', default='claude-sonnet-4-6',
                    help='model_info string the S0 header must contain (default: claude-sonnet-4-6)')
    ap.add_argument('--out', default=None,
                    help='output CSV path (default: <dir>/repro_metrics.csv)')
    args = ap.parse_args()

    pdir = os.path.abspath(args.dir)
    canon = load_canon(args.canon or os.path.join(pdir, 'canon.json'))

    rows = []
    for s1 in sorted(glob.glob(os.path.join(pdir, '*_repro_run*_s1.md'))):
        base = os.path.basename(s1)[:-len('_s1.md')]
        s0 = os.path.join(pdir, base + '_s0.md')
        s2 = os.path.join(pdir, base + '_s2.md')
        s1_text = open(s1, encoding='utf-8', errors='replace').read()
        s2_text = open(s2, encoding='utf-8', errors='replace').read() if os.path.exists(s2) else ''
        s0_text = open(s0, encoding='utf-8', errors='replace').read() if os.path.exists(s0) else ''

        model_ok = args.model_pin in s0_text
        # 中断 run の検出（2026-07-30、Entry 091）。murai_v21 run4 は s1/s1_turn2/s1_turn3/s2 が
        # **すべて 0 byte** なのに model_ok=1 の行として CSV に載り、nA..nU/canon すべて 0 で
        # v21 の平均に入っていた。0 byte 出力は「所見ゼロの run」ではなく **run が完走していない**。
        # nD4 だけの話ではないので、行は残しつつ全 count を空欄にして集計から外す。
        incomplete = not s1_text.strip() or not s2_text.strip()
        counts, sev, item_lines = count_items(s1_text)
        # D-4 count: B (summary line) > A ("D-4-N") or C ("D-4 候補 N") > D/E (labels).
        # Label counts are scoped to the D-4 section so mid-body mentions and the
        # anchoring_note's "D-4 候補 1" (an E-section back-reference) do not inflate
        # the count — run10 previously read nD4=1 from exactly such a stray C match.
        d4sec = d4_section(s2_text)
        sm_d4 = D4_SUMMARY.search(s2_text)
        if sm_d4:
            n_d4, d4_method = int(sm_d4.group(1)), 'summary'
        else:
            n_label = max(len(set(D4_LABEL.findall(d4sec))),
                          len(set(D4_LABEL_C.findall(d4sec))),
                          len(set(D4_LABEL_D.findall(d4sec))),
                          len(set(D4_LABEL_E.findall(d4sec))))
            n_gi = len(GROUNDED_IN.findall(d4sec))
            if n_label:
                n_d4, d4_method = n_label, 'label'
            elif n_gi:
                # ラベルの無い候補 block（形式 F）。候補 1 件 = grounded_in 1 行なので代替指標になる。
                n_d4, d4_method = n_gi, 'grounded_in'
            elif d4sec.strip():
                # 番号なし essay（形式 G）。**0 ではなく欠測**として出す（平均に入れない）。
                n_d4, d4_method = '', 'unnumbered_prose'
            else:
                n_d4, d4_method = '', 'no_d4_section'
        sm = SCOPE.search(s2_text)
        scope = sm.group(1).lower() if sm else ''
        mver = re.search(r'_(v\d+)_', base)
        mrun = re.search(r'_run(\d+)', base)

        # two-instrument canonical presence
        strict_scope = '\n'.join(item_lines) + '\n' + d4_section(s2_text)
        loose_scope = s1_text + '\n' + s2_text
        strict = {k: int(bool(p.search(strict_scope))) for k, p in canon.items()}
        loose = {k: int(bool(p.search(loose_scope))) for k, p in canon.items()}

        blank = '' if incomplete else None

        def cell(v):
            return blank if incomplete else v

        rows.append({
            'file': base, 'model_ok': int(model_ok), 'incomplete': int(incomplete),
            'ver': mver.group(1) if mver else '', 'run': mrun.group(1) if mrun else '',
            'nA': cell(counts['A']), 'nB': cell(counts['B']), 'nC': cell(counts['C']),
            'nU': cell(counts['U']),
            'nUcrit': cell(sev['critical']), 'nUhigh': cell(sev['high']),
            'nD4': cell(n_d4), 'nD4_method': 'incomplete_run' if incomplete else d4_method,
            'scope_type': scope,
            'canon_strict': cell(sum(strict.values())),
            'canon_loose': cell(sum(loose.values())),
            **{'strict_' + k: cell(v) for k, v in strict.items()},
            **{'loose_' + k: cell(v) for k, v in loose.items()},
        })

    if not rows:
        print('No *_repro_run*_s1.md found in', pdir, '(run the driver first).', file=sys.stderr)
        sys.exit(1)

    out = args.out or os.path.join(pdir, 'repro_metrics.csv')
    with open(out, 'w', newline='', encoding='utf-8') as f:
        w = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
        w.writeheader()
        w.writerows(rows)
    print(f'wrote {out}  ({len(rows)} runs, {len(canon)} canon axes)')

    bad = [r['file'] for r in rows if not r['model_ok']]
    if bad:
        print(f'WARNING: {len(bad)} run(s) with model_info != {args.model_pin} -> EXCLUDE:',
              *bad, sep='\n  ')
    inc = [r['file'] for r in rows if r['incomplete']]
    if inc:
        print(f'WARNING: {len(inc)} run(s) with an EMPTY s1 or s2 (aborted run — counts left '
              'blank, NOT 0) -> EXCLUDE:', *inc, sep='\n  ')
    nonum = [(r['file'], r['nD4_method']) for r in rows
             if r['nD4_method'] in ('unnumbered_prose', 'no_d4_section')]
    if nonum:
        print(f'NOTE: {len(nonum)} run(s) where nD4 is not countable (blank, not 0):')
        for f_, why in nonum:
            print(f'  {f_} : {why}')
    byalt = [r['file'] for r in rows if r['nD4_method'] == 'grounded_in']
    if byalt:
        print(f'NOTE: {len(byalt)} run(s) counted nD4 from grounded_in lines '
              '(candidate blocks carried no labels):', *byalt, sep='\n  ')
    gaps = [(r['file'], k) for r in rows for k in canon
            if r['loose_' + k] and not r['strict_' + k]]
    if gaps:
        print(f'SPOT-CHECK ({len(gaps)} strict=0/loose=1 cells — surfaced in turns, '
              'absent from final taxonomy):')
        for f_, k in gaps:
            print(f'  {f_} : {k}')


if __name__ == '__main__':
    main()
