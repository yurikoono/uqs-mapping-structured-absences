#!/usr/bin/env python3
"""repro_aggregate.py — aggregate repro_metrics.csv into repro_summary.md.

Generalized from the kumada Phase 1 version on 2026-07-20 (Phase 2 / hom1-hom2 reuse):
directory is a CLI argument; the number of canonical axes is derived from the CSV columns;
canonical coverage is reported as TWO instruments (strict = final taxonomy + D-4,
loose = anywhere in the final artifacts) with a spot-check list for strict/loose gaps.

Per version: mean / SD / CV of each count; miss rates from both coverage instruments;
scope_type mode + flip count. Then a version comparison that flags a difference ONLY when
|mean gap| exceeds the pooled within-version SD. Runs with model_ok=0 are excluded.

Usage:
    python3 scripts/repro_aggregate.py papers/dev/kumada/repro_2026-07
"""
import argparse, csv, os, statistics as st

COUNTS = ['nA', 'nB', 'nC', 'nU', 'nUcrit', 'nUhigh', 'nD4']


def stats(xs):
    if not xs:
        return (float('nan'),) * 3
    m = st.mean(xs)
    sd = st.stdev(xs) if len(xs) > 1 else 0.0
    cv = (sd / m) if m else float('nan')
    return m, sd, cv


def fmt(m, sd, cv):
    return f'{m:.2f} ± {sd:.2f} (CV {cv:.2f})' if m == m else 'n/a'


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('dir', nargs='?', default='.',
                    help='directory containing repro_metrics.csv (default: cwd)')
    args = ap.parse_args()
    pdir = os.path.abspath(args.dir)
    src = os.path.join(pdir, 'repro_metrics.csv')
    if not os.path.exists(src):
        raise SystemExit(f'{src} not found — run scripts/repro_extract.py first.')

    with open(src, encoding='utf-8') as f:
        rdr = csv.DictReader(f)
        fields = rdr.fieldnames or []
        rows = [r for r in rdr if r.get('model_ok') == '1'
                and r.get('incomplete', '0') != '1']
    axes = [c[len('strict_'):] for c in fields if c.startswith('strict_')]
    ncanon = len(axes)
    # 空欄は 0 ではなく**欠測**（repro_extract が「数えられない」を空欄で出す: 中断 run /
    # 番号なし essay の nD4）。int('') で落とさず None にし、平均の分母から外す。
    # 0 として畳み込むと欠測が下向きのバイアスになる — これが Entry 091 の修正点。
    for r in rows:
        for k in COUNTS + ['canon_strict', 'canon_loose']:
            v = (r.get(k) or '').strip()
            r[k] = int(v) if v else None

    vers = sorted({r['ver'] for r in rows})
    out = ['# UQS reproducibility — summary (model-pinned)', '']

    per = {}
    for v in vers:
        rs = [r for r in rows if r['ver'] == v]
        out += [f'## {v}  (n={len(rs)} valid runs)', '']
        out += ['| metric | mean ± SD (CV) |', '|---|---|']
        agg = {}
        for k in COUNTS:
            m, sd, cv = stats([r[k] for r in rs if r[k] is not None])
            agg[k] = (m, sd, cv)
            out.append(f'| {k} | {fmt(m, sd, cv)} |')
        for label, col in (('strict (final taxonomy + D-4)', 'canon_strict'),
                           ('loose (anywhere in final artifacts)', 'canon_loose')):
            mcov, _, _ = stats([r[col] / ncanon for r in rs if r[col] is not None])
            miss = 1 - mcov if mcov == mcov else float('nan')
            out.append(f'| canonical {label} | {mcov*ncanon:.2f} / {ncanon} '
                       f'(miss {miss:.2%}) |')
        scopes = [r['scope_type'] for r in rs if r['scope_type']]
        mode = max(set(scopes), key=scopes.count) if scopes else 'n/a'
        out.append(f'| scope_type | mode={mode}, distinct={len(set(scopes))} '
                   f'(flips={max(len(set(scopes)) - 1, 0)}) |')
        out += ['', '_per-run canonical strict/loose:_ ' +
                ', '.join(f'{r["run"]}:{r["canon_strict"]}/{r["canon_loose"]} (of {ncanon})'
                          for r in sorted(rs, key=lambda x: x['run'])), '']
        per[v] = agg

    # spot-check list: surfaced in turns but absent from the final taxonomy
    gaps = [(r['ver'], r['run'], k) for r in rows for k in axes
            if r.get('loose_' + k) == '1' and r.get('strict_' + k) == '0']
    truly_absent = [(r['ver'], r['run'], k) for r in rows for k in axes
                    if r.get('loose_' + k) == '0']
    out += ['## Canonical instrument disagreement', '',
            '_strict=0/loose=1 = surfaced during turns, did not reach the final taxonomy '
            'under the axis vocabulary (spot-check whether the taxonomy covers it in other '
            'words). loose=0 = genuinely absent from the run\'s final artifacts._', '']
    out.append('- strict=0/loose=1 cells: ' +
               (', '.join(f'{v}/run{r}:{k}' for v, r, k in gaps) if gaps else 'none'))
    out.append('- loose=0 (true absence) cells: ' +
               (', '.join(f'{v}/run{r}:{k}' for v, r, k in truly_absent)
                if truly_absent else 'none'))
    out.append('')

    if len(vers) == 2:
        a, b = vers
        out += [f'## {a} vs {b} — is the difference real or lottery?', '',
                '_A gap is flagged **REAL** only if |mean gap| > pooled within-version SD '
                '(i.e. exceeds run-to-run noise). Otherwise it is within lottery range._', '',
                f'| metric | {a} | {b} | gap | pooled SD | verdict |', '|---|---|---|---|---|---|']
        for k in COUNTS:
            ma, sda, _ = per[a][k]
            mb, sdb, _ = per[b][k]
            gap = abs(ma - mb)
            pooled = ((sda**2 + sdb**2) / 2) ** 0.5
            verdict = 'REAL' if gap > pooled else 'within noise'
            if pooled == 0 and gap > 0:
                verdict = 'REAL (0 within-var)'
            out.append(f'| {k} | {ma:.2f} | {mb:.2f} | {gap:.2f} | {pooled:.2f} | {verdict} |')
        out += ['',
                '> Interpretation: **REAL** rows are prompt-attributable differences (model is '
                'fixed). **within noise** rows mean the apparent difference is a sampling '
                'artifact — do NOT register it as a regression.', '']

    out += ['---', '',
            '_Canonical coverage is a keyword proxy on two scopes; spot-check the disagreement '
            'list before citing any per-finding claim. Rigorous metrics: the count table and '
            'scope_type._', '',
            '**Paper A hook:** report absolute-count claims as `mean ± SD (CV=…)`; use the '
            'STRICT miss rate as "probability a single run\'s final taxonomy omits a canonical '
            'finding" and the LOOSE miss rate as "probability it is absent from the run '
            'entirely". Relative claims (X > Y) are unaffected; absolute claims carry this error.']

    dst = os.path.join(pdir, 'repro_summary.md')
    open(dst, 'w', encoding='utf-8').write('\n'.join(out) + '\n')
    print('wrote', dst)
    print('\n'.join(out))


if __name__ == '__main__':
    main()
