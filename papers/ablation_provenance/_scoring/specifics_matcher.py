#!/usr/bin/env python3
"""E2 specifics matcher — 出力中の content-specifics (数値・化学 entity) の実論文一致率。

Provenance ablation の secondary endpoint E2 (内容層)。E1 (逐語層 = anchor_matcher.py) が
検出できない register 変換 retrieval を、specifics の一致で挟む:
Arm W で「本文なし」なのに数値・entity が実論文と一致する = 内容レベルの retrieval 証拠。

Usage:
  python3 scripts/specifics_matcher.py <pdf> [<si_pdf> ...] <output_md> [...] [--dump] [--tsv F]

抽出対象 (機械的、LLM 判定なし):
  numeric = 単位/percent/小数を伴う数値 (% °C K mol% equiv h Hz nm kcal kJ M mmol mol g mL)。
            年 (19xx/20xx 単独) と書誌 stub 内の数値は除外。
  entity  = 英字+数字の混在 token または括弧つき化学式様 token (B3LYP, 6-31G(d), Pd(OAc)2,
            RuH2(CO)(PPh3)3, dppe 等の 3-6 文字小文字略号)。stub token は除外。

特異度 5 層のうち本 script が機械化するのは entity (≈ system-specific 層) と
numeric (≈ 定量値層) のみ。document-specific relation / absence relation 層は
canonical record coding (事前登録 §3 / memo §9) の管轄で、本 script の scope 外。

一致判定 = anchor_matcher.normalize() 後の連続部分文字列 (reference = 本文+SI 連結)。
"""
import re, sys, unicodedata
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from anchor_matcher import normalize, build_source  # noqa: E402

UNIT = r"(?:%|°c|°C|K\b|mol%|equiv|equiv\.|h\b|Hz|MHz|nm|kcal|kJ|mmol|mol\b|mg\b|g\b|mL|M\b|atm|bar|ppm|ee\b)"
NUM_RE = re.compile(rf"\b\d+(?:\.\d+)?(?:\s*[-–—:]\s*\d+(?:\.\d+)?)?\s*{UNIT}", re.IGNORECASE)
DECIMAL_RE = re.compile(r"\b\d+\.\d+\b")
ENTITY_RE = re.compile(r"[A-Za-z][A-Za-z0-9]*\d[A-Za-z0-9()\[\]'′,\-]*|[A-Z][a-z]?\([A-Za-z0-9()]+\)[0-9₀-₉]*")
ABBREV_RE = re.compile(r"\b(?:dppe|dppp|dppf|dtbpy|cod|acac|dba|binap|phen|bpy|pyox|nbe|dmf|dmso|nmp|thf|gvl)\b", re.IGNORECASE)
YEAR_RE = re.compile(r"^(?:19|20)\d{2}$")
# UQS 内部 ID (出力スキーマの識別子であって化学 specifics でない) — 抽出前に text から除去
UQS_ID_RE = re.compile(
    r"\bV\d+[-–]Q\d+\S*|\b(?:EP|RI|SRG|PRI|IP|SSP|BIB|SAT|VQ)[-–]?\d+[a-z]?\b"
    r"|\b[ABCDU][-–]\d+[a-z]?\b|\bS[0-4](?:[-–]\d+)?\b|\bT[1-4]\b|\bV[1-4]\b"
    r"|\bTurn\s?\d\b|\bStage\s?\d[A-F]?\b|\bG[1-3]\b|\bD4\b")


def extract_specifics(text: str, stub_norm_tokens: set):
    text = UQS_ID_RE.sub(" ", text)
    nums, ents = set(), set()
    for m in NUM_RE.finditer(text):
        nums.add(m.group(0))
    for m in DECIMAL_RE.finditer(text):
        nums.add(m.group(0))
    for m in ENTITY_RE.finditer(text):
        tok = m.group(0).rstrip(".,;:)")
        if "(" in tok and tok.count("(") != tok.count(")"):
            tok = tok[:tok.index("(")]
        if YEAR_RE.match(tok) or len(tok) < 3:
            continue
        ents.add(tok)
    for m in ABBREV_RE.finditer(text):
        ents.add(m.group(0))
    nums = {n for n in nums if normalize(n) not in stub_norm_tokens}
    ents = {e for e in ents if normalize(e) and normalize(e) not in stub_norm_tokens}
    return nums, ents


def matches(spec: str, ref_norm: str, ref_tokens: set, kind: str) -> bool:
    qn = normalize(spec)
    if qn in ref_norm:
        return True
    if kind == "num":
        core = re.findall(r"\d+(?:\.\d+)?", spec)
        return bool(core) and all(c in ref_tokens for c in core)
    # entity fallback: 末尾の量論数字を落として再照合 (OCR で下付きが崩れる系)
    qn2 = re.sub(r"\s*\d+$", "", qn)
    return len(qn2) >= 4 and qn2 in ref_norm


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
    mds = [Path(a) for a in args if not a.endswith(".pdf")]
    stubs = [Path(a) for a in args if a.endswith(".txt")]
    mds = [m for m in mds if m.suffix == ".md"]
    if not pdfs or not mds:
        sys.exit("need >=1 reference .pdf and >=1 output .md (optional stub .txt)")

    ref_norm = " ".join(build_source(p)[1] for p in pdfs)
    ref_tokens = set(ref_norm.split())
    stub_tokens = set()
    for s in stubs:
        stub_tokens |= set(normalize(s.read_text()).split())

    rows = []
    for md in mds:
        text = md.read_text()
        nums, ents = extract_specifics(text, stub_tokens)
        nm = {n for n in nums if matches(n, ref_norm, ref_tokens, "num")}
        em = {e for e in ents if matches(e, ref_norm, ref_tokens, "ent")}
        rows.append((md.name, len(nm), len(nums), len(em), len(ents)))
        if dump:
            for label, miss in (("NUM", nums - nm), ("ENT", ents - em)):
                for x in sorted(miss):
                    print(f"  [UNMATCHED {label}] {md.name}: {x}")

    tn = sum(r[2] for r in rows); tnm = sum(r[1] for r in rows)
    te = sum(r[4] for r in rows); tem = sum(r[3] for r in rows)
    label = "+".join(p.name for p in pdfs)
    print(f"# E2 vs {label}")
    for name, a, b, c, d in rows:
        print(f"  {name}: numeric {a}/{b}  entity {c}/{d}")
    print(f"  TOTAL numeric = {tnm}/{tn}" + (f" = {tnm/tn:.3f}" if tn else " (none)"))
    print(f"  TOTAL entity  = {tem}/{te}" + (f" = {tem/te:.3f}" if te else " (none)"))
    if tsv:
        with open(tsv, "a") as f:
            for r in rows:
                f.write(f"{label}\t" + "\t".join(map(str, r)) + "\n")


if __name__ == "__main__":
    main()
