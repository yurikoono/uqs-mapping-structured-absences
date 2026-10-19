"""
Fig. 4: Temporal Distribution of Recurring Roots (CRRs / IPs)

Data source: papers/ep/kumada1972/kumada1972_all_v17_opus_s2fv71.md
  §"Patterns that emerged independently in multiple sub-groups" (IP-1 through IP-4)
  §"Cross-referencing recurring_roots across sub-groups"

R1 revision (2026-10-05, Referee 2 minor 1 "fonts too small"): redrawn at the
printed size. The canvas is exactly 15 cm wide (= \includegraphics width in the
RSC source; margins set in cm, saved without bbox_inches="tight"), so every
fontsize below is the point size on the page (all >= 7.5 pt). Data, colours
and layout are unchanged.
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
DATA = DATA_DIR / "fig4_recurring_roots.csv"
OUT.mkdir(exist_ok=True)

df = pd.read_csv(DATA)

CRR_INFO = {
    "CRR-1": dict(ip="IP-1", color="#0072B2",
                  desc="Catalytic cycle proposed without\nelementary-step validation"),
    "CRR-2": dict(ip="IP-2", color="#009E73",
                  desc="Quantitative analytical basis\nfor primary data underreported"),
    "CRR-3": dict(ip="IP-3", color="#E69F00",
                  desc="Self-contradictory absence\n(observable predicted but not tested)"),
    "CRR-4": dict(ip="IP-5",  # IP-4 in the v17 source output; IP-5 in the seven-IP numbering of Results Part 3
                  color="#D55E00",
                  desc="Benchmark superiority asserted\nwithout matched-pair comparison"),
}
# Order: top-to-bottom = most universal -> less universal
order = ["CRR-1", "CRR-2", "CRR-3", "CRR-4"]
n = len(order)

# ---- Printed-size canvas: 15 cm x 8.4 cm, axes margins in cm ----
CM = 1 / 2.54
W_CM, H_CM = 15.0, 8.4
L_CM, R_CM, B_CM, T_CM = 2.35, 1.95, 1.05, 0.75   # left/right/bottom/top margins
fig = plt.figure(figsize=(W_CM * CM, H_CM * CM))
ax = fig.add_axes([L_CM / W_CM, B_CM / H_CM,
                   1 - (L_CM + R_CM) / W_CM, 1 - (B_CM + T_CM) / H_CM])
FS = 7.5   # text floor (pt on the page)

year_min, year_max = 1970, 2026

for i, crr in enumerate(order):
    subset = df[df["crr_id"] == crr].sort_values("year")
    info = CRR_INFO[crr]
    y_pos = n - i - 1
    years = subset["year"].values
    # Horizontal range bar
    ax.barh(y_pos, years.max() - years.min(), left=years.min(), height=0.40,
            color=info["color"], alpha=0.25, edgecolor=info["color"], linewidth=0.9)
    # Jitter slightly when multiple papers share a year (e.g. 2016)
    years_jittered = []
    seen = {}
    for y in years:
        seen[y] = seen.get(y, 0)
        off = (seen[y] - 0.5) * 0.8 if list(years).count(y) > 1 else 0
        years_jittered.append(y + off)
        seen[y] += 1
    ax.scatter(years_jittered, [y_pos] * len(years),
               s=46, color=info["color"], edgecolor="black",
               linewidth=0.5, zorder=3)
    # Paper count label at right of bar
    ax.text(year_max + 1.6, y_pos, f"{len(years)}/9 papers",
            ha="left", va="center", fontsize=FS, clip_on=False)

# Y-axis labels: IP number in the seven-IP numbering of Results Part 3 (the v17 CRR numbering
# differs from the CRR numbering of SI-5, so CRR labels are not shown)
yticklabels = []
for crr in order:
    info = CRR_INFO[crr]
    yticklabels.append(info["ip"])
ax.set_yticks(range(n))
ax.set_yticklabels([yticklabels[n - i - 1] for i in range(n)], fontsize=8.5)
ax.tick_params(axis="x", labelsize=FS, width=0.6, length=3)
ax.tick_params(axis="y", width=0.6, length=3)
for sp in ("left", "bottom"):
    ax.spines[sp].set_linewidth(0.7)

# Annotate each bar's descriptor inline.
# Descriptor text uses a neutral dark grey (high contrast on white, ~12:1) rather
# than the row colour: the coloured italics failed WCAG contrast (orange 2.3:1,
# vermillion 3.9:1, green 3.4:1). Row identity is still carried by the band,
# the dots, and the y-axis label, so no information is lost.
DESC_TEXT_COLOR = "#333333"
for i, crr in enumerate(order):
    info = CRR_INFO[crr]
    y_pos = n - i - 1
    # Place descriptor under the bar
    ax.text(year_min + 0.5, y_pos - 0.25, info["desc"],
            ha="left", va="top", fontsize=FS, color=DESC_TEXT_COLOR,
            style="italic", linespacing=1.1)

# X-axis
ax.set_xlim(year_min, year_max + 1)
ax.set_ylim(-0.85, n - 0.45)
ax.set_xlabel("Year", fontsize=8.5, labelpad=2)
ax.xaxis.grid(True, alpha=0.25, linestyle="--")
ax.set_axisbelow(True)
ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)

# Title / subtitle
ax.set_title("Field-wide recurring roots (Stage 2F integrative output, 9-paper corpus)",
             fontsize=8.5, pad=6)

for ext in ("svg", "pdf", "png"):
    out_path = OUT / f"fig4_recurring_roots.{ext}"
    # no bbox_inches="tight": keep the exact 15 cm print width
    kwargs = {"dpi": 600} if ext == "png" else {}
    plt.savefig(out_path, **kwargs)
    print(f"wrote {out_path}")
plt.close(fig)
