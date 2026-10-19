#!/usr/bin/env python3
"""Parse WoS tagged-format export into a CSV-like table for triage."""
import re
import sys
from pathlib import Path


def parse_wos(path: Path) -> list[dict]:
    records = []
    current = {}
    current_tag = None
    for line in path.read_text(encoding="utf-8-sig").splitlines():
        if line == "ER":
            if current:
                records.append(current)
            current = {}
            current_tag = None
            continue
        if line.startswith("EF") or line.startswith("FN ") or line.startswith("VR "):
            continue
        m = re.match(r"^([A-Z0-9]{2})\s(.*)$", line)
        if m:
            current_tag = m.group(1)
            current[current_tag] = m.group(2)
        elif line.startswith("   ") and current_tag:
            current[current_tag] = current.get(current_tag, "") + " " + line.strip()
    return records


def main():
    src = Path(__file__).parent / "wos_raw_49hits.txt"
    recs = parse_wos(src)
    out = Path(__file__).parent / "wos_49hits_triage_table.md"
    lines = [
        "# WoS 49 Hits Triage Table",
        "",
        "Generated from wos_raw_49hits.txt. For each record, mark the relevance column manually:",
        "",
        "- **R** (Relevant): Directly reports spectroscopic observation/characterization of a Ni–diphosphine intermediate in a Kumada-type or closely related catalytic context.",
        "- **P** (Peripheral): Ni–diphosphine complex characterized, but not as a catalytic intermediate; or a different reaction system.",
        "- **N** (Not relevant): Off-target match (different metal focus, different chemistry, false keyword hit).",
        "",
        "| # | Year | Authors | Title | Journal | DOI | Relevance | Notes |",
        "|---|------|---------|-------|---------|-----|-----------|-------|",
    ]
    for i, r in enumerate(recs, 1):
        py = r.get("PY", "?")
        au = r.get("AU", "?").split(";")[0].strip() if r.get("AU") else "?"
        ti = r.get("TI", "?").strip()
        so = r.get("SO", "?").strip()
        di = r.get("DI", "")
        lines.append(f"| {i} | {py} | {au} | {ti} | {so} | {di} |  |  |")
    out.write_text("\n".join(lines), encoding="utf-8")
    print(f"Wrote {out} with {len(recs)} records")


if __name__ == "__main__":
    main()
