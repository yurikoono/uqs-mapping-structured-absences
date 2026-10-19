"""
SI Fig. S1: Quantitative improvements across the v15 → v16.1 → v17 refinement cycle.

Data source: improvements/v17_formal_decision.md §2.3 "v17の定量的改善".
Because version-specific counts have heterogeneous units (U-item totals vs B / D-4
per-paper averages), each metric is rendered as its own subplot with raw value
labels. Cumulative percentage gains (v15 → v17) are annotated on each panel.
"""
from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
# Repository: data in ROOT/data, output to ROOT/output. Deposit copy (Tier 7): ROOT is the deposit root, the data are in
# tier_4_classification_tables/figures_data/ and the output goes to rerun_output/ at the deposit root.
DATA_DIR = next(d for d in (ROOT / "data", ROOT / "tier_4_classification_tables" / "figures_data") if d.is_dir())
OUT = ROOT / "output" if (ROOT / "data").is_dir() else ROOT / "rerun_output"
DATA = DATA_DIR / "figS1_refinement_improvements.csv"
OUT.mkdir(exist_ok=True)

df = pd.read_csv(DATA)

# --- Font-size scale, ordered by the figure's information hierarchy ---
# Message: every metric improves across v15 -> v16.1 -> v17, and the cumulative
# gains (top-right of each panel) are the headline result. Sizes by importance:
FS_SUPTITLE = 13     # overall title (top level)
FS_GAIN     = 13     # cumulative % gain — the headline number (emphasised)
FS_PANEL    = 10.5   # per-panel metric name
FS_VALUE    = 10     # raw bar value labels (the data)
FS_TICK     = 10     # version tick labels (v15 / v16.1 / v17)
FS_AXIS     = 8.5    # y-axis unit label (auxiliary)

VERSIONS = ["v15", "v16_1", "v17"]
VERSION_LABELS = {"v15": "v15", "v16_1": "v16.1", "v17": "v17"}
VERSION_COLORS = {"v15": "#999999", "v16_1": "#56B4E9", "v17": "#009E73"}

fig, axes = plt.subplots(1, len(df), figsize=(11.5, 3.9), sharey=False)

for ax, (_, row) in zip(axes, df.iterrows()):
    values = [row[v] for v in VERSIONS]
    colors = [VERSION_COLORS[v] for v in VERSIONS]
    labels = [VERSION_LABELS[v] for v in VERSIONS]
    bars = ax.bar(labels, values, color=colors, edgecolor="black", linewidth=0.8)
    # Value labels above bars
    for bar, val in zip(bars, values):
        ax.text(bar.get_x() + bar.get_width() / 2,
                bar.get_height() + max(values) * 0.03,
                f"{val:g}" if val != int(val) else f"{int(val)}",
                ha="center", va="bottom", fontsize=FS_VALUE, fontweight="bold")
    # Cumulative gain — the headline result: emphasised in a boxed callout,
    # placed top-left to avoid the tall v17 bar on the right.
    ax.text(0.04, 0.95, row["cumulative_gain"],
            transform=ax.transAxes, ha="left", va="top",
            fontsize=FS_GAIN, color="#D55E00", fontweight="bold",
            bbox=dict(boxstyle="round,pad=0.28", facecolor="#FFF1E8",
                      edgecolor="#D55E00", linewidth=1.0))
    # Panel title (metric name)
    ax.set_title(row["metric"], fontsize=FS_PANEL, pad=6)
    ax.set_ylabel(row["unit"], fontsize=FS_AXIS)
    ax.set_ylim(0, max(values) * 1.28)
    ax.grid(axis="y", alpha=0.3, linestyle="--")
    ax.set_axisbelow(True)
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    ax.tick_params(axis="y", labelsize=FS_AXIS)
    for tick in ax.get_xticklabels():
        tick.set_fontsize(FS_TICK)

fig.suptitle("Quantitative improvements across the UQS refinement cycle "
             "(v15 → v16.1 → v17, 10-paper test corpus)",
             fontsize=FS_SUPTITLE, y=1.03)

plt.tight_layout()
for ext in ("svg", "pdf", "png"):
    out_path = OUT / f"figS1_refinement_improvements.{ext}"
    kwargs = {"bbox_inches": "tight"}
    if ext == "png":
        kwargs["dpi"] = 600
    plt.savefig(out_path, **kwargs)
    print(f"wrote {out_path}")
plt.close(fig)
