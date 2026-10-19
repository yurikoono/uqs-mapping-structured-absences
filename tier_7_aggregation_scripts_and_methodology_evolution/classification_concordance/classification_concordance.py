#!/usr/bin/env python3
"""classification_concordance.py — A/B/C/U 分類の model 間一致率（移行 trigger 軸 2）。

なぜ要るか（2026-07-30、`improvements/uqs_model_migration_trigger_20260730.md` 軸 2）
------------------------------------------------------------------------------------
Sonnet 4.6 → 5 の移行条件 3 つのうち **classification concordance が実質手つかず**だった
（逸話 n=2 = kumada の homo-coupling self-contradiction が 4.6=high-U → Sonnet 5=B/SRG、
murai では critical U 保持、で「系統的劣化ではない」と判断していた）。n=2 では判断が早すぎる。
本 script は paired run から一致率と**不一致の方向**を機械的に出す。

**item id では対応が取れない**（設計の中心）
--------------------------------------------
実出力を見ると 3 つの理由で item 単位の同定が不可能:
  1. `item_id` は run 間で不安定（U-1 が同じものを指す保証がない）。
  2. **`loc` の枠が model で違う** — 4.6 は `P3:col1:L27-30*`（刷り位置）、
     Sonnet 5 は `P4376:L18-27*`（印刷ページ番号）。loc は key にできない。
  3. **1 item が複数 quote を持ち**（`"…" / "…"`）、**1 quote が複数 item に付く**
     （4.6 の A-1 と A-2 が同一 quote を共有）。∴ quote↔item は 1:1 でない。

∴ 比較単位を **item ではなく datum（= 引用された原典の箇所）**に置く。
各 run を「datum → 付与された bin の集合」に還元し、datum 同士を quote の
fuzzy 一致で対応付けて bin 集合を比べる。これは移行 trigger 文書の
「同一 datum に対する分類 bin の一致率」の素直な実装であり、
**A/B/C/U は partition が価値であって label 名ではない**（memory
`project_uqs_abcu_partition_over_labels`）という前提と整合する。

**within-arm baseline が無い一致率は解釈できない**（最重要）
-----------------------------------------------------------
移行 trigger 文書は閾値を「一致率 ≥0.80」と書いたが、**これは単独では意味を持たない**。
同一 model の 2 run 間でも分類は揺れる（run-to-run lottery）。もし 4.6 同士の一致率も 0.80 なら、
cross-model の 0.80 は **model 差を何も示していない**。
∴ 本 script は必ず 3 つを同時に出す:

    within-A（4.6 同士） / within-B（Sonnet 5 同士） / cross（A×B）

読み方: **cross が within の下限を下回らなければ、model 差は run 揺れに埋もれている。**
（H27「清潔論文 held-out 対照 = 偽陽性率の唯一の外部計器」と同じ形の対照。）

**presence と classification を混ぜない**
-----------------------------------------
片方の arm にしか無い datum は「分類が違う」のではなく **recall が違う**。
別軸なので別分母で報告する（今日の分母規律、Entry 090/091）。

Usage:
    python3 scripts/classification_concordance.py \
        papers/dev/kumada/v20_tierE_2026-07 \
        papers/dev/kumada/v20_tierE_diag_sonnet5_2026-07 \
        --only-b _v20_sonnet5_ --label-a sonnet46 --label-b sonnet5
    python3 scripts/classification_concordance.py --selftest
"""
from __future__ import annotations

import argparse
import glob
import itertools
import json
import math
import os
import re
import sys

try:
    from rapidfuzz import fuzz
except ImportError:
    sys.exit("rapidfuzz required: pip install rapidfuzz")

# item 行。**2 つの書式を受ける**（bin 接頭は任意）:
#   inline   `[A] A-1 | loc | "quote" | …`            ← v19/v20/v24 系
#   section  `[A]` が独立行 → `A-1 | loc | "quote" | …` ← scr1 capbias 4.6 run3 系
# 後者を受けていなかったため run3 は **item 0 件**と読まれ、同一 model 同一条件の
# within pair が「対応 0 件 = Jaccard 0.000」になっていた（2026-07-30 に発見）。
# bin は id の文字（A-1 の A）から採る — 接頭の有無に依存しない。
# `|` を必須にして、散文中の "A-1 は…" 等を拾わない。
# 2026-07-31 修正（Fable 5 査読）: ハイフン無し形 `[A] A1 | …` を読めず、repo 内で唯一の
# **真の cross-vendor データ**（`papers/dev/kumada/gpt54thinking/`, GPT-5.4）を 0 件として
# 読み捨てていた。`turn4_schema_lint._BAD_ID` は同じ形を違反として検出しており、
# **自分の 2 計器が「item 行とは何か」で食い違っていた**。
# 誤検出を避けるため、ハイフン省略は **角括弧 prefix がある場合のみ**許す
# （散文の "C1"/"B1" は化学の炭素位置・化合物名にも当たるため）。
# v18.4 期の出力は `A1 |`（ハイフンなし・bracket なし）、v27.1 は `[A] A-1 |`。
# 第 2 分岐のハイフンを optional にしないと v18.4 の item 行を 1 つも拾えない
# （2026-10-01 発見: Haiku v184 を 5.3 項目/run と誤読していた。実際は約 30）
_ITEM = re.compile(r'^\s*(?:\[([ABCU])\]\s*([ABCU])-?(\d+)|([ABCU])-?(\d+))\s*\|')
_QUOTED = re.compile(r'["“]([^"”]{4,})["”]')
_MIN_SIG = 30          # これ未満の signature は fuzzy 対応付けに使わない（短文は誤マッチする）
_FUZZ = 88             # 対応付け閾値
_MIN_PARTIAL = 40      # partial_ratio（包含）を許す最小長。短い側が長い側に埋まる誤マッチを防ぐ


def normalize(s: str) -> str:
    s = re.sub(r'\s+', ' ', s).strip().lower()
    s = s.replace('’', "'").replace('“', '"').replace('”', '"')
    s = re.sub(r'[·•\*​]', '', s)
    return re.sub(r'[\s\.,;:]+$', '', s)


def _score(a: str, b: str) -> float:
    s = fuzz.ratio(a, b)
    if min(len(a), len(b)) >= _MIN_PARTIAL:
        s = max(s, fuzz.partial_ratio(a, b))
    return s


_LABELLED = re.compile(r'^\s*(?:anchor_quote|key_quote|quote)\s*:\s*(.*)$', re.I | re.S)
_CIT_LABEL = re.compile(r'^\s*citation\s*:\s*(.*)$', re.I | re.S)
_NOTE_CUT = re.compile(r'\|\s*note\s*:', re.I)


def _signatures(line: str, bin_: str) -> list[str]:
    """行から signature（引用 or citation）を取る。**欄の位置に依存しない**。

    実出力に少なくとも 3 つの schema がある（位置固定にすると静かに壊れる）:
      v19/v20 系   `[A] A-1 | P3:col1:L27* | "quote" | deferred | …`       → 3 番目が引用
      murai 4.6 系 `[A] A-1 | anchor_quote: "quote" (p. 531) | classification: … | …`
                                                                          → 2 番目・ラベル付き
      C 項目       `[C] C-1 | loc | Tamura and Kochi, JACS 93, 1483 … | …`  → 引用符なし citation

    位置固定（field[2]）にしていたため murai 4.6 では `classification:` 本文を
    signature として拾い、**cross 対応が 0 件**になった（2026-07-30 に発見・修正）。
    ラベルがあればそれを優先し、無ければ引用符つき span を探す、の順にする。
    """
    head = _NOTE_CUT.split(line)[0]          # note: 欄の引用を signature にしない
    fields = [f.strip() for f in head.split('|')]
    for f in fields[1:]:
        lm = _LABELLED.match(f)
        if lm:
            q = _QUOTED.findall(lm.group(1))
            if q:
                return q
        cm = _CIT_LABEL.match(f)
        if cm and cm.group(1).strip():
            return [cm.group(1).strip()]
    if len(fields) > 2:
        q = _QUOTED.findall(fields[2])
        if q:
            return q
    q = _QUOTED.findall(head)                # 位置不明でも引用符があれば拾う
    if q:
        return q
    if bin_ == 'C' and len(fields) > 2 and fields[2]:
        return [fields[2]]                   # 引用符なし citation
    return []


def parse_items(path: str) -> list[dict]:
    """s1 出力 → [{bin, id, sigs:[str]}]。signature は quote 欄のみから採る。"""
    out, seen = [], set()
    for line in open(path, encoding='utf-8', errors='ignore').read().splitlines():
        m = _ITEM.match(line)
        if not m:
            continue
        b2, n2 = (m.group(2), m.group(3)) if m.group(2) else (m.group(4), m.group(5))
        bin_, iid = b2, f'{b2}-{n2}'
        if iid in seen:      # 両書式が混在する file で二重計上しない
            continue
        seen.add(iid)
        sigs = [normalize(s) for s in _signatures(line, bin_)]
        out.append({'bin': bin_, 'id': iid, 'sigs': [s for s in sigs if s]})
    return out


def run_datums(items: list[dict]) -> tuple[list[dict], int]:
    """run 内で datum を作る。同一/近似 signature を 1 datum にまとめ bin 集合を持たせる。

    1 quote が複数 item に付く（4.6 の A-1/A-2 が同一 quote）ので、この畳み込みが要る。
    畳み込まないと同じ datum が 2 回数えられ、分母が run ごとに変わってしまう。
    """
    datums: list[dict] = []
    short = 0
    for it in items:
        usable = [s for s in it['sigs'] if len(s) >= _MIN_SIG]
        if not usable:
            short += 1
            continue
        for sig in usable:
            hit = next((d for d in datums if _score(d['sig'], sig) >= _FUZZ), None)
            if hit:
                hit['bins'].add(it['bin'])
                hit['ids'].append(it['id'])
            else:
                datums.append({'sig': sig, 'bins': {it['bin']}, 'ids': [it['id']]})
    return datums, short


def match(da: list[dict], db: list[dict]) -> tuple[list[tuple], list[dict], list[dict]]:
    """datum 同士を 1:1 で対応付ける（score 降順の貪欲法）。"""
    cand = []
    for i, x in enumerate(da):
        for j, y in enumerate(db):
            s = _score(x['sig'], y['sig'])
            if s >= _FUZZ:
                cand.append((s, i, j))
    cand.sort(reverse=True)
    ua, ub, pairs = set(range(len(da))), set(range(len(db))), []
    for s, i, j in cand:
        if i in ua and j in ub:
            ua.discard(i); ub.discard(j)
            pairs.append((da[i], db[j], s))
    return pairs, [da[i] for i in sorted(ua)], [db[j] for j in sorted(ub)]


def binom_two_sided(k: int, n: int) -> float:
    """p=0.5 の両側二項検定（記述用。scipy 非依存）。"""
    if n == 0:
        return 1.0
    k = max(k, n - k)
    tail = sum(math.comb(n, i) for i in range(k, n + 1)) / 2 ** n
    return min(1.0, 2 * tail)


def compare_pair(fa: str, fb: str) -> dict:
    da, sa = run_datums(parse_items(fa))
    db, sb = run_datums(parse_items(fb))
    pairs, ua, ub = match(da, db)
    exact = sum(1 for x, y, _ in pairs if x['bins'] == y['bins'])
    overlap = sum(1 for x, y, _ in pairs if x['bins'] & y['bins'])
    trans: dict[str, int] = {}
    single = 0
    for x, y, _ in pairs:
        if len(x['bins']) == 1 and len(y['bins']) == 1:
            single += 1
            a, b = next(iter(x['bins'])), next(iter(y['bins']))
            if a != b:
                trans[f'{a}->{b}'] = trans.get(f'{a}->{b}', 0) + 1
    return {'a': os.path.basename(fa), 'b': os.path.basename(fb),
            'n_datum_a': len(da), 'n_datum_b': len(db), 'matched': len(pairs),
            'exact': exact, 'overlap': overlap, 'single_bin_pairs': single,
            'only_a': len(ua), 'only_b': len(ub), 'short_skipped': sa + sb,
            'transitions': trans}


def _rate(rows, num, den='matched'):
    n = sum(r[den] for r in rows)
    return (sum(r[num] for r in rows) / n if n else float('nan')), n


def _fmt(rows, label):
    if not rows:
        return f'  {label:22} (pair なし)'
    ex, n = _rate(rows, 'exact')
    ov, _ = _rate(rows, 'overlap')
    return (f'  {label:22} pair={len(rows):>3} 対応 datum={n:>4}  '
            f'exact={ex:.3f}  overlap={ov:.3f}')


def _jaccard(rows):
    """datum 集合そのものの重なり（何を引用の対象に選んだか）。

    bin 一致率は **両 arm が同じ datum を選んだ場合にしか定義されない**。
    実測では対応が 4 割弱しかなく、model 差の主成分は「どう分類したか」ではなく
    **「何を anchor に選んだか」**だった。∴ こちらも within baseline つきで出す
    （一致率だけ出すと、選択の差が分母から消えたまま「概ね一致」と読めてしまう）。
    """
    if not rows:
        return float('nan'), float('nan'), 0
    m = sum(r['matched'] for r in rows)
    den = m + sum(r['only_a'] for r in rows) + sum(r['only_b'] for r in rows)
    cov = m / (m + sum(r['only_a'] for r in rows)) if m or sum(r['only_a'] for r in rows) else float('nan')
    return (m / den if den else float('nan')), cov, den


def _fmt_j(rows, label):
    j, cov, den = _jaccard(rows)
    if den == 0:
        return f'  {label:22} (pair なし)'
    return (f'  {label:22} Jaccard={j:.3f}  A 側被覆={cov:.3f}  '
            f'（和集合 datum={den}）')


def report(within_a, within_b, cross, la, lb, verbose=False) -> int:
    print('\n## 一致率（datum 単位、bin 集合の一致）\n')
    print(_fmt(within_a, f'within-{la}'))
    print(_fmt(within_b, f'within-{lb}'))
    print(_fmt(cross, f'cross {la}×{lb}'))
    print('\n  exact = bin 集合が完全一致 / overlap = 少なくとも 1 bin 共有')
    print('  ↑ **両 arm が同じ datum を選んだ場合にしか定義されない指標**')

    print('\n## datum 選択の重なり（何を anchor に選んだか。上の一致率の分母そのもの）\n')
    print(_fmt_j(within_a, f'within-{la}'))
    print(_fmt_j(within_b, f'within-{lb}'))
    print(_fmt_j(cross, f'cross {la}×{lb}'))
    jc, _, _ = _jaccard(cross)
    jfloor = [x for x in (_jaccard(within_a)[0], _jaccard(within_b)[0]) if x == x]
    if jc == jc and jfloor:
        lo = min(jfloor)
        print(f'\n  cross Jaccard={jc:.3f} vs within 下限={lo:.3f} → '
              + ('選択の差も run 揺れの範囲' if jc >= lo
                 else '**選択の差が run 揺れを超える = model 差の主成分はここ**'))

    ex_c, n_c = _rate(cross, 'exact')
    floors = [r for r in (_rate(within_a, 'exact')[0], _rate(within_b, 'exact')[0])
              if r == r]
    floor = min(floors) if floors else float('nan')
    print('\n## 判定の形\n')
    if n_c and floor == floor:
        verdict = ('model 差は run 揺れに埋もれている' if ex_c >= floor
                   else '**cross が within の下限を下回る = model 差が run 揺れを超える**')
        print(f'  cross exact={ex_c:.3f} vs within 下限={floor:.3f} → {verdict}')
    else:
        print('  判定不能（cross または within の pair が無い）')
    print('  **within baseline の無い一致率は解釈できない** — 同一 model でも分類は揺れる。'
          '\n  絶対閾値（0.80 等）ではなく within 下限との比較で読む。')

    pooled: dict[str, int] = {}
    for r in cross:
        for k, v in r['transitions'].items():
            pooled[k] = pooled.get(k, 0) + v
    print('\n## 不一致の方向（cross、単一 bin 同士の pair のみ）\n')
    if not pooled:
        print('  不一致なし')
    else:
        for k, v in sorted(pooled.items(), key=lambda x: -x[1]):
            print(f'    {k:12} {v}')
        best = max(pooled, key=lambda k: pooled[k])
        a, b = best.split('->')
        fwd, rev = pooled[best], pooled.get(f'{b}->{a}', 0)
        p = binom_two_sided(fwd, fwd + rev)
        print(f'\n  最大非対称: {best} {fwd} 件 vs 逆方向 {rev} 件 → '
              f'両側二項 p={p:.3f}（記述用。多重比較補正なし）')
        print('  **「U が B になった」を一律の劣化と数えない** — A/B/C/U は partition が価値で '
              'label 名ではない。\n  判定は方向の系統性で行う。')

    m, den = _rate(cross, 'only_a', 'matched')
    tot_a = sum(r['only_a'] for r in cross); tot_b = sum(r['only_b'] for r in cross)
    tot_s = sum(r['short_skipped'] for r in cross)
    print('\n## presence（分類ではなく recall の差 — 別軸・別分母）\n')
    print(f'  cross pair 合計: {la} のみ={tot_a} / {lb} のみ={tot_b} / '
          f'対応={den} / 短すぎて対応付け対象外={tot_s}')
    print(f'  （signature <{_MIN_SIG} 字は誤マッチを避けるため除外。分母に入れていない）')

    n_runs = len({r['a'] for r in cross} | {r['b'] for r in cross})
    print(f'\n  **非独立性**: cross の {len(cross)} pair は {n_runs} run から作られている。'
          f'\n  実効 N は run 数であって pair 数ではない — 対応 datum 数を「独立 n」として読まないこと。')
    if verbose:
        print('\n## pair 別\n')
        for r in cross:
            print(f'    {r["a"]} × {r["b"]}: matched={r["matched"]} exact={r["exact"]} '
                  f'only_a={r["only_a"]} only_b={r["only_b"]} {r["transitions"] or ""}')
    return 0


def collect(spec: str, only: str | None) -> list[str]:
    files = (sorted(glob.glob(f'{spec}/**/*_s1.md', recursive=True))
             if os.path.isdir(spec) else sorted(glob.glob(spec)))
    files = [f for f in files if '_s1_turn' not in os.path.basename(f)]
    if only:
        files = [f for f in files if only in os.path.basename(f)]
    return files


# ---------------------------------------------------------------- selftest
_FA = """[A] A-1 | P3:col1:L27* | "[REDACTED: verbatim source text; see the source paper via its DOI]." | deferred | n/a | T1
[A] A-2 | P3:col1:L27* | "[REDACTED: verbatim source text; see the source paper via its DOI]" | deferred | n/a | T1
[B] B-1 | P2:col1:Table I footnote e | "Yields based on glpc analysis using an internal standard." | reporting_omission | T2 | note: no calibration
[U] U-1 | P2:col2:L5* | "[REDACTED: verbatim source text; see the source paper via its DOI]" | critical | T1 | note: heterogeneity unexamined
[C] C-1 | P1:Rcol:L15* | Tamura and Kochi, J. Amer. Chem. Soc. 93, 1483 (1971) [ref 5] | prior_art | T1
"""
# 同じ 4 datum。U-1 の datum が B に落ち、C の citation は一致、短い quote は除外される。
# murai 4.6 系の schema（`anchor_quote:` ラベル + 位置ずれ）。位置固定パーサだと
# `classification:` 本文を signature にして cross 対応が 0 件になった実際の形。
_FC = """[A] A-1 | anchor_quote: "[REDACTED: verbatim source text; see the source paper via its DOI]." (p. 531 col. 1) | classification: A — explicit deferral of the mechanism | nested: V2-Q1
[B] B-1 | anchor_quote: "Yields based on glpc analysis using an internal standard." (Table I footnote) | era_status: structural | question: what internal standard
[U] U-1 | anchor_quote: "[REDACTED: verbatim source text; see the source paper via its DOI]" (p. 4375) | severity: critical | note: heterogeneity unexamined
"""

# section-header 書式（`[A]` が独立行 + bin 接頭なしの item 行）。scr1 capbias 4.6 run3 の実形。
_FD = """[A]
A-1 | P7:L42-50* | "[REDACTED: verbatim source text; see the source paper via its DOI]" | deferred | n/a | T1
[B]
B-1 | P5:L2* | "Yields based on glpc analysis using an internal standard." | reporting_omission | T2 | note: none
B-7 | P5:L9* | "[REDACTED: verbatim source text; see the source paper via its DOI]" | reporting_omission | T2 | note: physical state
"""

_FB = """[A] A-1 | P4376:L18-27* | "[REDACTED: verbatim source text; see the source paper via its DOI]." | deferred | n/a | T1
[B] B-1 | P4375:L20* | "Yields based on glpc analysis using an internal standard." | reporting_omission | T1 | note: four of ten entries
[B] B-7 | P4375:L5* | "[REDACTED: verbatim source text; see the source paper via its DOI]" | reporting_omission | T2 | note: physical state
[C] C-1 | P1:Rcol:L15* | Tamura and Kochi, J. Amer. Chem. Soc. 93, 1483 (1971) [ref 5] | prior_art | T1
[B] B-9 | P4376:L2* | "cis: trans = 80:20" | reporting_omission | T2 | note: too short to match
"""


def selftest() -> int:
    import tempfile
    fails = []
    with tempfile.TemporaryDirectory() as td:
        pa, pb = f'{td}/x_sonnet46_run1_s1.md', f'{td}/x_sonnet5_run1_s1.md'
        open(pa, 'w').write(_FA); open(pb, 'w').write(_FB)

        items = parse_items(pa)
        if len(items) != 5:
            fails.append(f'item 数が 5 でない: {len(items)}')
        if [i['bin'] for i in items] != ['A', 'A', 'B', 'U', 'C']:
            fails.append(f'bin 抽出が不正: {[i["bin"] for i in items]}')

        da, sa = run_datums(items)
        # A-1/A-2 が同一 quote を共有 → 1 datum に畳まれるべき（畳まないと分母が壊れる）
        if len(da) != 4:
            fails.append(f'run 内 datum 畳み込みが不正（期待 4）: {len(da)} / '
                         f'{[d["sig"][:30] for d in da]}')
        shared = [d for d in da if len(d['ids']) == 2]
        if not shared:
            fails.append('同一 quote を共有する 2 item が 1 datum に畳まれていない')

        r = compare_pair(pa, pb)
        if r['matched'] != 4:
            fails.append(f'対応 datum 数が 4 でない: {r["matched"]}')
        if r['transitions'].get('U->B') != 1:
            fails.append(f'U->B の遷移を検出できていない: {r["transitions"]}')
        if r['exact'] != 3:
            fails.append(f'exact 一致が 3 でない: {r["exact"]}')
        if r['short_skipped'] < 1:
            fails.append('短い signature（"cis: trans = 80:20"）を除外していない')
        # loc が全く違う（P3:col1 vs P4376）のに対応が取れることの確認 = 設計の核
        if r['matched'] < 4:
            fails.append('loc 枠が違う run 間で quote 対応が取れていない')

        # schema 変種（murai 4.6 形）でも同じ datum に対応が取れること = 位置固定回帰の防止
        pc = f'{td}/x_sonnet46_schemaB_run1_s1.md'
        open(pc, 'w').write(_FC)
        ic = parse_items(pc)
        if any(not i['sigs'] for i in ic):
            fails.append('anchor_quote: ラベル schema から signature を取れていない')
        rc = compare_pair(pc, pb)
        if rc['matched'] < 3:
            fails.append(f'schema 変種と v20 schema の間で datum 対応が取れない: {rc}')
        if rc['transitions'].get('U->B') != 1:
            fails.append(f'schema 変種でも U->B を検出できるべき: {rc["transitions"]}')

        # section-header 書式（bin 接頭なし）を読めること = scr1 capbias run3 回帰の防止
        pd_ = f'{td}/x_sonnet46_sectionhdr_run1_s1.md'
        open(pd_, 'w').write(_FD)
        idd = parse_items(pd_)
        if len(idd) != 3:
            fails.append(f'section-header 書式の item を読めていない（期待 3）: {len(idd)}')
        if [i['bin'] for i in idd] != ['A', 'B', 'B']:
            fails.append(f'id 文字からの bin 判定が不正: {[i["bin"] for i in idd]}')
        if any(not i['sigs'] for i in idd):
            fails.append('section-header 書式から signature を取れていない')

        p = binom_two_sided(4, 4)
        if not (0.1 < p < 0.15):
            fails.append(f'二項検定が想定外（4/4 は p=0.125）: {p}')

    if fails:
        print('  selftest FAIL')
        for f in fails:
            print(f'    - {f}')
        return 1
    print('  selftest PASS — loc 枠が違う run 間で datum 対応が取れ、同一 quote の 2 item が '
          '1 datum に畳まれ、\n  U->B の遷移が検出され、短すぎる signature が分母から除外される')
    return 0


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument('arm_a', nargs='?')
    ap.add_argument('arm_b', nargs='?')
    ap.add_argument('--only-a', default=None, help='arm A の filename 部分一致 filter')
    ap.add_argument('--only-b', default=None)
    ap.add_argument('--label-a', default='armA')
    ap.add_argument('--label-b', default='armB')
    ap.add_argument('--verbose', action='store_true')
    ap.add_argument('--json', default=None)
    ap.add_argument('--selftest', action='store_true')
    a = ap.parse_args()
    if a.selftest:
        return selftest()
    if not a.arm_a or not a.arm_b:
        ap.error('arm_a と arm_b、または --selftest が必要')

    fa, fb = collect(a.arm_a, a.only_a), collect(a.arm_b, a.only_b)
    # item 0 件の run を除外する。**残すと「対応 0 件」の pair を作って一致率と Jaccard を
    # 静かに 0 方向へ引っぱる**（今朝 repro_extract に入れた incomplete 門と同じ family。
    # 実例: scr1 capbias 4.6 run3 は書式違いで 0 件と読まれ within pair を 0.000 にした）。
    dropped = []
    for lst in (fa, fb):
        for f in list(lst):
            if not parse_items(f):
                lst.remove(f); dropped.append(f)
    if dropped:
        print('  ⚠️ item 0 件のため除外（未完走 or 未知書式 — 0 を測定値として扱わない）:')
        for f in dropped:
            print(f'    - {os.path.basename(f)}')
    if not fa or not fb:
        print(f'  s1 file が足りない: {a.label_a}={len(fa)} / {a.label_b}={len(fb)}')
        return 1
    print(f'  {a.label_a}: {len(fa)} run / {a.label_b}: {len(fb)} run')
    for f in fa + fb:
        print(f'    - {os.path.basename(f)}')

    within_a = [compare_pair(x, y) for x, y in itertools.combinations(fa, 2)]
    within_b = [compare_pair(x, y) for x, y in itertools.combinations(fb, 2)]
    cross = [compare_pair(x, y) for x in fa for y in fb]

    # 「datum は取れているのに、相手側と 1 件も対応しない」run は schema 変種の疑い。
    # murai 4.6 v20 が実際にこれで、位置固定パーサが `classification:` 本文を signature に
    # していたため cross 対応 0 件 = **model 差の極大**のように見えた（2026-07-30）。
    # 0 を結果として読ませないための門。
    for label, own, rows, side in ((a.label_a, fa, cross, 'a'), (a.label_b, fb, cross, 'b')):
        for f in own:
            key = os.path.basename(f)
            mine = [r for r in rows if r[side] == key]
            if mine and all(r['matched'] == 0 for r in mine) \
                    and any(r[f'n_datum_{side}'] > 0 for r in mine):
                print(f'\n  ⚠️ WARNING: {key} は datum を '
                      f'{max(r[f"n_datum_{side}"] for r in mine)} 件持つのに相手側と 1 件も対応しない。'
                      f'\n     schema 変種で signature を取り違えている可能性が高い — '
                      f'0 を「model 差」として読まないこと。')
    report(within_a, within_b, cross, a.label_a, a.label_b, a.verbose)
    if a.json:
        json.dump({'within_a': within_a, 'within_b': within_b, 'cross': cross},
                  open(a.json, 'w'), ensure_ascii=False, indent=1)
        print(f'\n  wrote {a.json}')
    return 0


if __name__ == '__main__':
    sys.exit(main())
