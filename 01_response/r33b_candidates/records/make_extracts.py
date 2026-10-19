#!/usr/bin/env python3
"""Deposit the two prose verification records that build_tally.py transcribes (record sets B4 and B5).

B4: improvements/stage4_literature_update_20260419.md -> copied unchanged.
B5: the project record pilot_retrieval_depth_20260508.md (an exploratory pilot of 2026-05-08; not deposited) -> line-preserving
    extract. The record holds the bibliographic verification of the Kumada 1972 retrieval-depth Stage 4 runs (§10, §11, §13, §15, §16)
    together with notes on other work. Only the verification sections are kept; every other line is left
    empty, so line N of the extract is line N of the record and the line numbers in candidates.csv and build_tally.py hold.
    Lines 1-9 (the record's front matter) carry this note instead.
Run from anywhere:  python3 make_extracts.py
"""
import shutil, subprocess
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[4]
shutil.copy2(ROOT / "improvements/stage4_literature_update_20260419.md", HERE / "stage4_literature_update_20260419.md")

# The version the tally was built against (2026-10-05 12:47): commit aabbef2. A note appended to the memo later that day
# shifted its line numbers; it concerns the Hayashi-Tajika entry, whose confirmation §13.2 already records.
# The B5 source is a project record of an exploratory pilot (2026-05-08), not deposited. It is found in the project repository
# by its file name at that commit (exactly one file there ends with this name).
MEMO_NAME = "pilot_retrieval_depth_20260508.md"
_tree = subprocess.run(["git", "-C", str(ROOT), "ls-tree", "-r", "--name-only", "aabbef2"], capture_output=True, text=True,
                       check=True).stdout.split("\n")
_hits = [p for p in _tree if p.startswith("improvements/") and p.endswith(MEMO_NAME)]
assert len(_hits) == 1, _hits
MEMO = _hits[0]
src = subprocess.run(["git", "-C", str(ROOT), "show", f"aabbef2:{MEMO}"], capture_output=True, text=True, check=True).stdout.split("\n")
KEEP = [(10, 12, "title and date"), (253, 313, "§10.1–10.4 bibliographic verification"),
        (376, 462, "§11.1–11.3 second pilot, candidate sets, verification"), (520, 523, "§11.6 Hayashi–Tajika 1976 check"),
        (595, 639, "§13.1–13.3 six-run candidate matrix"), (855, 935, "§15.1–15.4 GPT runs: matrix and verification"),
        (950, 976, "§15.6 cross-run agreement"), (1087, 1149, "§16.1–16.2 Opus / Haiku runs")]
keep = set()
for a, b, _ in KEEP:
    keep.update(range(a, b + 1))
out = ["" if (i + 1) not in keep else l for i, l in enumerate(src)]
note = ["# Verification record for the Kumada 1972 retrieval-depth Stage 4 runs (line-preserving extract)",
        "",
        "Extract of the project record `pilot_retrieval_depth_20260508.md` (an exploratory pilot of 2026-05-08, as of 2026-06-10;",
        "the record itself is not deposited), deposited as record set B5 of `../tally.md`.",
        "Kept verbatim: " + "; ".join(f"l.{a}–{b} {d}" for a, b, d in KEEP) + ".",
        "All other lines (method notes, interpretation and planning for other work) are left empty, so line numbers are the",
        "record's own and the `verification_record_line` values in `../candidates.csv` point here. The run files are under",
        "`tier_3_stage_outputs/dev_set/kumada/` (reviewer version). Built by `make_extracts.py`.",
        ""]
assert len(note) == 9
out[:9] = note
(HERE / "kumada_retrieval_depth_verification_extract.md").write_text("\n".join(out), encoding="utf-8")
print("lines", len(out), "kept", len(keep))
