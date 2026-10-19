#!/usr/bin/env python3
"""E1 anchor matcher — key_quote の PDF 内実在を OCR-robust に機械判定する。

Paper A provenance ablation の primary endpoint (anchor 実在率) 用計器。LLM 判定は使わない。
設計背景 = improvements/_methodology/ablation_di_probe_results_20260808.md §6:
古スキャン (kumada 1972 / murai 1993) では真正な引用すら bad text layer と不一致になり
偽の「捏造」信号を出すため、① 正規化強化 ② 文字 8-gram containment による fuzzy 判定
③ 数式引用の分離 ④ 真正 run (Arm P) による床キャリブレーション、を備える。

Usage:
  python3 scripts/anchor_matcher.py <pdf> [<si_pdf> ...] <output_md> [...] [--dump] [--tsv FILE]

引数の .pdf はすべて参照 source (先頭 = MAIN、以降 = SI 等の追加 source として連結照合し、
どの source に一致したかを帰属報告)。⚠ `*_bundle.pdf` (bundle skill 成果物) は stage 出力を
含むため参照に渡さないこと (循環)。.md はすべて出力 file として quote 抽出対象。

判定カテゴリ (text quote):
  EXACT     正規化後に連続部分文字列として実在 (score=1.0)
  HIGH      8-gram containment >= 0.75  (OCR 劣化を許容した実在)
  PARTIAL   0.45 <= score < 0.75        (部分一致 — 要目視)
  NOT_FOUND score < 0.45
  FORMULA   数式/記号引用 (wordlike token 率 < 0.5) — 別枠報告、実在率の分母から除外
  CAPTION   Scheme/Figure/Table 等の caption 引用 — 別枠報告 (画像内容と text layer の
            境界に跨るため)、実在率の分母から除外
閾値は暫定 (2026-08-09 calibration: 真正 min 0.756 / 逸脱 max 0.562 で分離帯空)。
anchor 実在率 = (EXACT+HIGH) / text quotes。
"""
import re, subprocess, sys, unicodedata
from collections import defaultdict
from pathlib import Path

N = 8  # char n-gram size

DASHES = "‐‑‒–—―−"
QUOTES = "‘’“”´`"


def normalize(s: str) -> str:
    s = unicodedata.normalize("NFKC", s).lower()
    for d in DASHES:
        s = s.replace(d, "-")
    for q in QUOTES:
        s = s.replace(q, "'")
    s = s.replace("→", ">").replace("⇒", ">").replace("×", "x")
    s = re.sub(r"-\s*\n\s*", "", s)          # 行末ハイフネーション結合
    s = re.sub(r"[^a-z0-9>'\-\+=\(\)\[\]%]", " ", s)
    return re.sub(r"\s+", " ", s).strip()


def grams(s: str):
    return [s[i:i + N] for i in range(max(0, len(s) - N + 1))]


def is_formula(quote: str) -> bool:
    toks = quote.split()
    if not toks:
        return True
    wordlike = sum(1 for t in toks if len(re.sub(r"[^A-Za-z]", "", t)) >= 3)
    return wordlike / len(toks) < 0.5


CAPTION_RE = re.compile(
    r"^(scheme|figure|fig\.?|table|chart|equation|eq\.?)\s*(s?\d+|[ivx]+)?\s*[.:)]",
    re.IGNORECASE)


def is_caption(quote: str) -> bool:
    return bool(CAPTION_RE.match(quote.strip()))


def extract_quotes(md_path: Path):
    out = []
    for i, line in enumerate(md_path.read_text().splitlines(), 1):
        m = re.search(r"key_quote:\s*[\"「“]?(.*?)[\"」”]?\s*$", line)
        if m and m.group(1).strip():
            out.append((i, m.group(1).strip()))
    return out


def build_source(pdf: Path):
    if pdf.name.endswith("_bundle.pdf"):
        sys.exit(f"refusing to use {pdf.name} as reference: bundle は stage 出力を含む (循環)")
    raw = subprocess.run(["pdftotext", "-q", str(pdf), "-"],
                         capture_output=True, text=True).stdout
    norm = normalize(raw)
    gram_pos = defaultdict(list)
    for i, g in enumerate(grams(norm)):
        gram_pos[g].append(i)
    return pdf.name, norm, gram_pos


def match_one(qn: str, src_norm: str, gram_pos) -> tuple:
    """単一 source に対する (score, locus)。exact は score=1.0。"""
    if qn in src_norm:
        i = src_norm.index(qn)
        return (1.0, src_norm[max(0, i - 40):i + len(qn) + 40], True)
    qgrams = grams(qn)
    hits = [g for g in qgrams if g in gram_pos]
    score = len(hits) / len(qgrams) if qgrams else 0.0
    locus = ""
    if hits:
        centers = sorted(p for g in hits for p in gram_pos[g][:4])
        med = centers[len(centers) // 2]
        locus = src_norm[max(0, med - len(qn)):med + len(qn)]
    return (score, locus, False)


def match_quote(quote: str, sources) -> tuple:
    """全 source に照合し最良を採る。returns (verdict, score, locus, source_label)。"""
    qn = normalize(quote)
    if len(qn) < N:
        return ("TOO_SHORT", 0.0, "", "")
    best = (-1.0, "", False, "")
    for label, norm, gram_pos in sources:
        score, locus, exact = match_one(qn, norm, gram_pos)
        if exact:
            return ("EXACT", 1.0, locus, label)
        if score > best[0]:
            best = (score, locus, exact, label)
    score, locus, _, label = best
    verdict = "HIGH" if score >= 0.75 else ("PARTIAL" if score >= 0.45 else "NOT_FOUND")
    return (verdict, round(score, 3), locus, label)


def main():
    argv = sys.argv[1:]
    dump = "--dump" in argv
    tsv = None
    if "--tsv" in argv:
        i = argv.index("--tsv")
        tsv = Path(argv[i + 1])
        argv = argv[:i] + argv[i + 2:]
    args = [a for a in argv if not a.startswith("--")]
    pdfs = [Path(a) for a in args if a.endswith(".pdf")]
    stubs = [Path(a) for a in args if a.endswith(".txt")]
    outputs = [Path(a) for a in args if a.endswith(".md")]
    if not pdfs or not outputs:
        sys.exit("need >=1 reference .pdf and >=1 output .md (optional stub .txt)")
    sources = [build_source(p) for p in pdfs]
    # stub echo 検出 (Arm W 用): 書誌 stub に含まれる文言の引用は「文書からの抽出」でも
    # 「記憶からの retrieval」でもない (stub の反響)。gram 含有率 >= 0.6 で STUB_ECHO に分類。
    stub_grams = set(grams(normalize(" ".join(s.read_text() for s in stubs)))) if stubs else set()

    rows, agg = [], defaultdict(int)
    cat_found = defaultdict(lambda: [0, 0])   # category -> [found, n]
    src_attr = defaultdict(int)
    for md in outputs:
        for lineno, quote in extract_quotes(md):
            verdict, score, locus, src = match_quote(quote, sources)
            qn = normalize(quote)
            stub_echo = False
            if stub_grams and len(qn) >= N:
                qgrams = grams(qn)
                stub_echo = bool(qgrams) and sum(g in stub_grams for g in qgrams) / len(qgrams) >= 0.6
            category = ("STUB_ECHO" if stub_echo
                        else "FORMULA" if is_formula(quote)
                        else "CAPTION" if is_caption(quote) else "TEXT")
            if verdict != "TOO_SHORT" and category != "TEXT":
                cat_found[category][0] += verdict == "EXACT" or score >= 0.75
                cat_found[category][1] += 1
                verdict_out = f"{category}({verdict})"
            else:
                verdict_out = verdict
                agg[verdict] += 1
            if verdict in ("EXACT", "HIGH"):
                src_attr[src] += 1
            rows.append((md.name, lineno, verdict_out, score, quote, src, locus))
            if dump:
                print(f"[{verdict_out} {score} @{src}] {md.name}:{lineno}\n"
                      f"  Q: {quote}\n  S: {locus}\n")

    text_n = sum(agg[v] for v in ("EXACT", "HIGH", "PARTIAL", "NOT_FOUND"))
    found = agg["EXACT"] + agg["HIGH"]
    label = "+".join(p.name for p in pdfs)
    print(f"# {label}: quotes={len(rows)} (text={text_n}, "
          f"formula={cat_found['FORMULA'][1]}, caption={cat_found['CAPTION'][1]}, "
          f"stub_echo={cat_found['STUB_ECHO'][1]}, too_short={agg['TOO_SHORT']})")
    print(f"  EXACT={agg['EXACT']} HIGH={agg['HIGH']} PARTIAL={agg['PARTIAL']} "
          f"NOT_FOUND={agg['NOT_FOUND']}")
    print(f"  anchor実在率 (text) = {found}/{text_n}"
          f" = {found / text_n:.3f}" if text_n else "  (no text quotes)")
    for cat in ("FORMULA", "CAPTION", "STUB_ECHO"):
        f_, n_ = cat_found[cat]
        if n_:
            print(f"  {cat} found-rate (参考) = {f_}/{n_}")
    if len(sources) > 1 and src_attr:
        print("  source 帰属 (EXACT+HIGH): "
              + ", ".join(f"{k}={v}" for k, v in src_attr.items()))
    if tsv:
        with open(tsv, "a") as f:
            for r in rows:
                f.write("\t".join(map(str, r[:6])) + "\n")


if __name__ == "__main__":
    main()
