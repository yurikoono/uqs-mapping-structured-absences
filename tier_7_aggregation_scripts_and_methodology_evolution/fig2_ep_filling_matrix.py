"""
Fig. 2: EP-Filling Matrix (core figure of the paper)

Data source: papers/ep/kumada1972/kumada1972_all_v17_opus_s2fv71.md
  §"Cross-reference with Stage 3 EP filling landscape" (lines 105-114)
  Updated 2026-04-21: EP-02a and EP-10a added to match 10-EP dictionary
  (EP-10a added to SI-3.7 on 2026-04-19 after five runs assigned it from a label already in the Stage 3 prompt; not independent, SI-6.5).

VQ grouping from Kumada 1972 S3 §5:
  VQ-1 residual: EP-02a (identity — straddles VQ-1/VQ-2)
  VQ-2 route: EP-01a, EP-07a
  VQ-3 route: EP-03a, EP-04a, EP-05a, EP-06a, EP-10a
  VQ-4 route: EP-08a, EP-09a

R1 revision (2026-10-05, Referee 2 minor 1 "fonts too small"): redrawn at the
printed size. The canvas is exactly 15 cm wide (= \includegraphics width in the
RSC source; saved without bbox_inches="tight"), so every fontsize below is the
point size on the page (all >= 7.5 pt). Data, colours, labels and layout are
unchanged; the right-hand annotations and the legend are re-wrapped to fit.
"""
from pathlib import Path

import matplotlib.patches as mpatches
import matplotlib.pyplot as plt
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
# Repository: data in ROOT/data, output to ROOT/output. Deposit copy (Tier 7): ROOT is the deposit root, the data are in
# tier_4_classification_tables/figures_data/ and the output goes to rerun_output/ at the deposit root.
DATA_DIR = next(d for d in (ROOT / "data", ROOT / "tier_4_classification_tables" / "figures_data") if d.is_dir())
OUT = ROOT / "output" if (ROOT / "data").is_dir() else ROOT / "rerun_output"
DATA = DATA_DIR / "fig2_ep_filling_matrix.csv"
OUT.mkdir(exist_ok=True)

df = pd.read_csv(DATA)

# Column order: VQ-1 res. (EP-02a) -> VQ-2 -> VQ-3 -> VQ-4
EP_COLS = [
    ("EP-02a", "VQ-1 res."),
    ("EP-01a", "VQ-2"),
    ("EP-07a", "VQ-2"),
    ("EP-03a", "VQ-3"),
    ("EP-04a", "VQ-3"),
    ("EP-05a", "VQ-3"),
    ("EP-06a", "VQ-3"),
    ("EP-10a", "VQ-3"),
    ("EP-08a", "VQ-4"),
    ("EP-09a", "VQ-4"),
]
VQ_GROUP_BOUNDARIES = [1, 3, 8]  # column indices where VQ groups transition

# Short names for EPs (1-2 words) displayed under each column
EP_SHORT = {
    "EP-02a": "Identity",
    "EP-01a": "Reporting",
    "EP-07a": "Boundary",
    "EP-03a": "Observation",
    "EP-04a": "Discrimin.",
    "EP-05a": "Qt. ranking",
    "EP-06a": "Analogy",
    "EP-10a": "Kinetic",
    "EP-08a": "Replication",
    "EP-09a": "Benchmark",
}

# Colour / label map for cell values
CELL_COLOR = {
    "Origin":        "#2F2F2F",   # Kumada 1972 origin row (near-black)
    "Substantial":   "#009E73",   # dark green — boundary overcome (paradigm-driven)
    "Partial":       "#56B4E9",   # sky blue (Okabe-Ito) — distinct hue from Substantial green under CVD
    "Minimal":       "#E69F00",   # yellow/orange — small contribution
    "ParadigmShift": "#CC79A7",   # purple — Molander 2016
    "Review":        "#999999",   # gray — excluded (Cherney 2015)
    "-":             "#F5F5F5",   # near-white — unfilled
}
CELL_LABEL = {
    "Origin":        "·",
    "Substantial":   "S",
    "Partial":       "P",
    "Minimal":       "M",
    "ParadigmShift": "PS",
    "Review":        "R",
    "-":             "",
}

# Cells where the LLM-parametric Stage 4 pass recorded "Partial" but the stricter
# pre-locked WoS audit (run on EP-07a/08a/09a; SI-9.8) reclassifies the same
# candidates below Partial. These are flagged with hatching + a "P*" label so the
# figure does not visually assert a Partial filling that the headline
# bounded-non-detection warrant (locked-audit criteria) contradicts.
AUDIT_DOWNGRADE = {
    ("tamao1976", "EP-09a"),
    ("monnereau2009", "EP-09a"),
}

# Rows sorted ascending by year; Kumada 1972 at top
df = df.sort_values("year").reset_index(drop=True)
n_rows = len(df)
n_cols = len(EP_COLS)

# ---- Printed-size canvas: 15 cm wide; data unit = one matrix cell ----
CM = 1 / 2.54
W_CM = 15.0
CELL = 0.91                      # cell edge in cm
X_LO = -2.75                     # room for the paper labels (cell units)
X_HI = X_LO + W_CM / CELL
Y_LO, Y_HI = -3.35, n_rows + 0.12
H_CM = (Y_HI - Y_LO) * CELL
fig = plt.figure(figsize=(W_CM * CM, H_CM * CM))
ax = fig.add_axes([0, 0, 1, 1])
FS = 7.5                         # text floor (pt on the page)


# Draw cells
for i, row in df.iterrows():
    y = n_rows - i - 1  # top-to-bottom = ascending year
    for j, (ep, vq) in enumerate(EP_COLS):
        val = row[ep]
        color = CELL_COLOR.get(val, "#F5F5F5")
        downgraded = (row["paper_id"], ep) in AUDIT_DOWNGRADE
        if downgraded:
            rect = mpatches.Rectangle((j, y), 1, 1, facecolor=color,
                                      edgecolor="#D55E00", linewidth=1.1,
                                      hatch="xxxx", zorder=2)
        else:
            rect = mpatches.Rectangle((j, y), 1, 1, facecolor=color,
                                      edgecolor="black", linewidth=0.45)
        ax.add_patch(rect)
        text = CELL_LABEL.get(val, "")
        if downgraded and text:
            text = text + "*"
        if text:
            text_color = "white" if val in {"Origin", "ParadigmShift"} else "black"
            ax.text(j + 0.5, y + 0.5, text, ha="center", va="center",
                    fontsize=8.5, fontweight="bold", color=text_color, zorder=3)

# Paper labels on left (year in parentheses)
for i, row in df.iterrows():
    y = n_rows - i - 1
    label = f"{row['paper_label']}\n({row['year']})"
    ax.text(-0.15, y + 0.5, label, ha="right", va="center", fontsize=FS,
            linespacing=1.1)

# EP labels on bottom — two lines (prefix + code) so adjacent codes don't
# run together into one string (full names are in the caption).
for j, (ep, vq) in enumerate(EP_COLS):
    num = ep.split("-")[1]  # e.g. "02a"
    ax.text(j + 0.5, -0.12, f"EP-\n{num}", ha="center", va="top",
            fontsize=FS, fontweight="bold", linespacing=1.15)

# VQ group bars under the column labels — four bands matching caption
vq_ranges = [("VQ-1\nres.",  0,  1, "#E8D5E0"),   # EP-02a only
             ("VQ-2",        1,  3, "#BFDDF0"),    # EP-01a, EP-07a
             ("VQ-3",        3,  8, "#C8E6C9"),    # EP-03a–EP-06a, EP-10a
             ("VQ-4",        8, 10, "#FFD6CC")]    # EP-08a, EP-09a
for name, x0, x1, fill in vq_ranges:
    band_h = 0.62 if "\n" in name else 0.42
    band_y = -1.62 if "\n" in name else -1.42
    ax.add_patch(mpatches.Rectangle((x0, band_y), x1 - x0, band_h,
                                    facecolor=fill, edgecolor="black",
                                    linewidth=0.6, clip_on=False))
    ax.text((x0 + x1) / 2, band_y + band_h / 2, name,
            ha="center", va="center",
            fontsize=FS if "\n" in name else 8.5,
            fontweight="bold", linespacing=1.0)

# VQ group vertical separators
for b in VQ_GROUP_BOUNDARIES:
    ax.plot([b, b], [0, n_rows], color="black", linewidth=0.9, linestyle="--")

# Kumada 1972 (origin) — horizontal separator below
kumada_y = n_rows - int(df.index[df["paper_id"] == "kumada1972"][0]) - 1
ax.plot([0, n_cols], [kumada_y, kumada_y], color="black",
        linewidth=1.1, zorder=5)

# Layer 1 / Layer 2 visual divider — horizontal separator between Tamao 1976
# (Layer 1: 1973–1982 conventional self-filling) and Monnereau 2009 (Layer 2:
# 2009–2024 regime-shift). The ~33-year gap is indicated by a thick double line.
tamao_y = n_rows - int(df.index[df["paper_id"] == "tamao1976"][0]) - 1
ax.plot([0, n_cols], [tamao_y, tamao_y], color="#555555",
        linewidth=1.8, zorder=4)
ax.plot([0, n_cols], [tamao_y - 0.06, tamao_y - 0.06], color="#555555",
        linewidth=0.7, linestyle=":", zorder=4)
ax.text(n_cols + 0.12, tamao_y - 0.03,
        "≈33-year gap\n(1976 → 2009;\nPd-variant\ndiffusion)",
        fontsize=FS, color="#555555", linespacing=1.05, va="center", ha="left",
        style="italic")

# Red dashed highlights — position on EP-03a (Mazet 2021 is the sole partial filling)
mazet_y = n_rows - int(df.index[df["paper_id"] == "mazet2021"][0]) - 1
ep03_x = [i for i, (ep, _) in enumerate(EP_COLS) if ep == "EP-03a"][0]
# 49-year delay box (EP-03a column from just above Mazet 2021 row up to below Kumada)
ax.add_patch(mpatches.Rectangle((ep03_x, mazet_y + 1), 1, kumada_y - mazet_y - 1,
                                fill=False, edgecolor="#D55E00", linewidth=1.4,
                                linestyle="--"))
# 54-year unfilled (EP-08a column)
ep08_x = [i for i, (ep, _) in enumerate(EP_COLS) if ep == "EP-08a"][0]
ax.add_patch(mpatches.Rectangle((ep08_x, 0), 1, kumada_y,
                                fill=False, edgecolor="#D55E00", linewidth=1.4,
                                linestyle="--"))

# Annotation arrows for the two highlighted regions
ax.annotate("49-year interval\nto system-matched\nVQ-3 filling\n(EP-03a, Mazet 2021)",
            xy=(ep03_x + 1.0, (mazet_y + kumada_y) / 2),
            xytext=(n_cols + 0.25, (mazet_y + kumada_y) / 2 + 0.5),
            fontsize=FS, color="#D55E00", va="center", linespacing=1.05,
            arrowprops=dict(arrowstyle="->", color="#D55E00", linewidth=0.9))
ax.annotate("VQ-4 unfilled\nacross 1972–2026\nwindow (EP-08a:\nreplication)",
            xy=(ep08_x + 0.5, kumada_y / 2 - 0.5),
            xytext=(n_cols + 0.25, 1.5),
            fontsize=FS, color="#D55E00", va="center", linespacing=1.05,
            arrowprops=dict(arrowstyle="->", color="#D55E00", linewidth=0.9))

# Legend (below figure)
legend_patches = [
    mpatches.Patch(facecolor="#2F2F2F", edgecolor="black", label="Origin (Kumada 1972)"),
    mpatches.Patch(facecolor="#009E73", edgecolor="black", label="Substantial (paradigm-driven)"),
    mpatches.Patch(facecolor="#56B4E9", edgecolor="black", label="Partial"),
    mpatches.Patch(facecolor="#E69F00", edgecolor="black", label="Minimal"),
    mpatches.Patch(facecolor="#CC79A7", edgecolor="black", label="Paradigm-shift"),
    mpatches.Patch(facecolor="#999999", edgecolor="black", label="Review (excluded)"),
    mpatches.Patch(facecolor="#F5F5F5", edgecolor="black", label="Unfilled"),
    mpatches.Patch(facecolor="#56B4E9", edgecolor="#D55E00", hatch="xxxx",
                   label="P* = LLM-parametric Partial;\nbelow Partial under locked\nWoS audit (SI-9.8)"),
]
ax.legend(handles=legend_patches, loc="upper center",
          bbox_to_anchor=((X_LO + X_HI) / 2, -1.85),
          bbox_transform=ax.transData,
          ncol=3, fontsize=FS, frameon=False, handlelength=1.6,
          handleheight=0.9, columnspacing=1.2, labelspacing=0.35,
          borderaxespad=0, borderpad=0)

# Axes setup
ax.set_xlim(X_LO, X_HI)
ax.set_ylim(Y_LO, Y_HI)
ax.set_aspect("equal")
ax.axis("off")

for ext in ("svg", "pdf", "png"):
    out_path = OUT / f"fig2_ep_filling_matrix.{ext}"
    # no bbox_inches="tight": keep the exact 15 cm print width
    kwargs = {"dpi": 600} if ext == "png" else {}
    plt.savefig(out_path, **kwargs)
    print(f"wrote {out_path}")
plt.close(fig)
