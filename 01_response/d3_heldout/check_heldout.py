#!/usr/bin/env python3
"""D3 endpoints 1, 3, 4 (prereg §2.4). Criteria are taken from the prompt-defined output formats,
not from the outputs: S1 turn4 format (prompt_stage1_turn4_v184.md), S2 EN headers (prompt_stage2_v184_en.md),
S3 v2 EN output format + SRG/CLA template (prompt_stage3_v2_en.md §Output format, Step 2c).
Endpoint 2 (quote gate) is run separately with scripts/verbatim_quote_gate.py. Run from repo root."""
import importlib.util, json, re, sys
# Paths (2026-10-17). In the project repository this script is run from the repository root, as before, and every path
# below is the repository path. Inside the Zenodo deposit of Paper A it can be run from any directory: an input that is not
# found relative to the working directory is read from the deposit (`_src`), the implementations come from
# tier_7_aggregation_scripts_and_methodology_evolution/lib/, and outputs go to rerun_output/ at the deposit root (`_out`),
# so the deposited results are not overwritten and can be compared with the re-run.
import os as _os
_DEP = _os.path.abspath(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), "..", ".."))
_LIB = "tier_7_aggregation_scripts_and_methodology_evolution/lib/"
def _src(repo, dep=None):
    return repo if _os.path.exists(repo) else _os.path.join(_DEP, repo if dep is None else dep)
def _out(repo, dep):
    if _os.path.isdir(repo):
        return repo
    d = _os.path.join(_DEP, "rerun_output", dep); _os.makedirs(d, exist_ok=True); return d
sys.argv = ["x"]
spec = importlib.util.spec_from_file_location("rx", _src("scripts/repro_extract.py", _LIB + "repro_extract.py")); rx = importlib.util.module_from_spec(spec); spec.loader.exec_module(rx)
ROOT = _src("papers/paperA_heldout_R1"); IDS = ["wang2026", "liu2026", "wu2026", "shekarizadeh2026"]
S2_HEADERS = ["[D-1", "[D-2", "[D-3", "[D-4", "[E"]
S3_HEADERS = ["§1", "§2", "§3", "§4", "§5", "§6"]
ITEM = re.compile(r"\b(?:[ABCU]-\d+|V\d-(?:Q|OV)\d+)\b")
# E4 anchor as pre-registered: "key_quote か節の参照" = a quotation from the paper, or a reference to a location in the paper.
# Item IDs (A-/B-/U-n) are NOT counted: they point to UQS output, not to the paper (Fable 5.1 review F1).
QUOTE = re.compile(r"[\"“][^\"“”\n]{15,}[\"”]")
LOCREF = re.compile(r"\b(?:p\.\s?\d+|pp?\.\s?\d+|page \d+|Tables? \w+|Schemes? \d+|Figures? \d+|Figs?\.\s?\d+|entr(?:y|ies) \d+|Example \d+|Supporting Information|\bSI\b|ref(?:s)?\.? \d+|Section \d+|Introduction|Experimental|Conclusion)", re.I)
def srg_blocks(s3):
    # blocks start at a bold SRG-N / CLA heading (Step 2c template) and end at the next block or section heading
    starts = [m.start() for m in re.finditer(r"\*\*(?:SRG-\d+|CLA-?\d+)[^*]*\*\*", s3)]
    ends = starts[1:] + [len(s3)]
    out = []
    for a, b in zip(starts, ends):
        blk = s3[a:b]; cut = re.search(r"\n#{2,3} ", blk)
        out.append(blk[:cut.start()] if cut else blk)
    return out
res = {}
for pid in IDS:
    t = f"{ROOT}/{pid}/{pid}_v184_sonnet46"
    try:
        s1, s2, s3 = (open(f"{t}_{s}.md").read() for s in ("s1", "s2_en", "s3v2_en"))
    except FileNotFoundError as e:
        res[pid] = {"error": str(e)}; continue
    counts, sev, lines = rx.count_items(s1)
    blocks = srg_blocks(s3)
    ep_ok, tmpl = [], []
    for b in blocks:
        # E4 as pre-registered (§2.4): the block names an evidence class (EP-NNx) and anchors to the text
        ep_ok.append({"ep_class": bool(re.search(r"EP-\d+[a-z]", b)), "anchor_quote_or_location": bool(QUOTE.search(b) or LOCREF.search(b))})
        # template adherence (Step 2c field labels) — reported separately, not part of E4
        tmpl.append({k: bool(re.search(p, b)) for k, p in {"primary_ri": r"Primary RI[^\n]{0,15}RI-\d", "er": r"\bER\b[^\n]{0,5}:", "ep_field": r"\*\*EP\*\*:",
                                                           "implementation": r"[Cc]ase-specific implementation"}.items()})
    d4 = rx.d4_section(s2)
    ep_labels = sorted(set(re.findall(r"EP-\d+[a-z]", s3)))
    r = {
        "E1_s1_taxonomy": sum(counts.values()) > 0, "E1_s1_same_root_groups": "same_root_groups" in s1,
        "E1_s2_headers": {h: h in s2 for h in S2_HEADERS}, "E1_s3_headers": {h: h in s3 for h in S3_HEADERS},
        "E1_s3_srg_blocks": len(blocks),
        "E3_counts": {**counts, "U_critical": sev.get("critical", 0) if isinstance(sev, dict) else sev, "SRG_CLA_blocks": len(blocks),
                      "EP_labels": len(ep_labels), "D4_section_chars": len(d4)},
        "E4_blocks_all_fields": sum(all(f.values()) for f in ep_ok), "E4_blocks": len(ep_ok),
        "E4_missing": [ {k: v for k, v in f.items() if not v} for f in ep_ok if not all(f.values())],
        "EP_labels": ep_labels,
        "template_adherence": {k: sum(t[k] for t in tmpl) for k in (tmpl[0] if tmpl else {})},
    }
    r["E1_pass"] = r["E1_s1_taxonomy"] and r["E1_s1_same_root_groups"] and all(r["E1_s2_headers"].values()) and all(r["E1_s3_headers"].values()) and len(blocks) > 0
    r["E4_pass"] = len(ep_ok) > 0 and r["E4_blocks_all_fields"] == len(ep_ok)
    res[pid] = r
json.dump(res, open(_out("manuscript_A/DigitalDiscovery_R1/01_response/d3_heldout", "01_response/d3_heldout") + "/check_results.json", "w"), indent=1, ensure_ascii=False)
for pid, r in res.items():
    print(pid, {k: r[k] for k in ("E1_pass", "E4_pass", "E4_blocks", "E3_counts", "E4_missing", "template_adherence")} if "error" not in r else r)
