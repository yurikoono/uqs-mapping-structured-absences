"""
Fig. 3: VQ-Level Trajectory

Data source: derived from Fig. 2 EP filling matrix + Kumada S3 §5 VQ route assignments.

Level mapping per cell value:
  Unfilled -> 0
  Minimal  -> 1.0   (small contribution, target not approached)
  Partial (VQ-1/VQ-2 target) -> 2.0
  Substantial (VQ-1/VQ-2 target) -> 2.0
  Partial (VQ-3 target) -> 2.5 (half-step toward VQ-3)
  Partial (VQ-4 target) -> 2.0 (no step toward VQ-4 is drawn: the exploratory
    Partial labels on EP-09a fall below Partial under the locked audit, P* in Fig. 2)
  The Molander 2016 paradigm-shift annotation (PS, all EPs) is excluded from the
  max-VQ trace (different mechanism, separate axis); an EP-specific paradigm-shift
  filling (S in Fig. 2, EP-07a in Breitenfeld 2014, "Substantial") is plotted.

Each EP's trace is the cumulative maximum VQ level reached across the corpus.
"""
from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
# Repository: data in ROOT/data, output to ROOT/output. Deposit copy (Tier 7): ROOT is the deposit root, the data are in
# tier_4_classification_tables/figures_data/ and the output goes to rerun_output/ at the deposit root.
DATA_DIR = next(d for d in (ROOT / "data", ROOT / "tier_4_classification_tables" / "figures_data") if d.is_dir())
OUT = ROOT / "output" if (ROOT / "data").is_dir() else ROOT / "rerun_output"
DATA = DATA_DIR / "fig3_vq_trajectory.csv"
OUT.mkdir(exist_ok=True)

df = pd.read_csv(DATA).set_index("year")

# Colour-vision-safe scheme:
#   colour encodes ONLY the VQ group (3 maximally CVD-distinct colours);
#   individual EP identity is carried by UNIQUE marker + line style.
# Group colours (Okabe-Ito blue / Okabe-Ito orange / dark neutral grey) stay
# distinct under deuteranopia, protanopia and tritanopia (min ΔE ≈ 29).
VQ_COLOR = {
    "VQ-2": "#0072B2",   # blue   — filled-early group (3 EPs)
    "VQ-3": "#E69F00",   # orange — main filling group (5 EPs)
    "VQ-4": "#444444",   # dark grey — never-filled group (2 EPs)
}
EP_STYLE = {
    "EP-02a": dict(color=VQ_COLOR["VQ-2"], ls="--", marker="*", lw=1.6, label="EP-02a (target VQ-1 res., Identity)"),
    "EP-01a": dict(color=VQ_COLOR["VQ-2"], ls="-",  marker="o", lw=1.8, label="EP-01a (target VQ-2, Reporting)"),
    "EP-07a": dict(color=VQ_COLOR["VQ-2"], ls=":",  marker="s", lw=1.8, label="EP-07a (target VQ-2, Boundary)"),
    "EP-03a": dict(color=VQ_COLOR["VQ-3"], ls="-",  marker="^", lw=1.8, label="EP-03a (target VQ-3, Observation)"),
    "EP-04a": dict(color=VQ_COLOR["VQ-3"], ls="--", marker="v", lw=1.8, label="EP-04a (target VQ-3, Discrimination)"),
    "EP-05a": dict(color=VQ_COLOR["VQ-3"], ls=":",  marker="D", lw=1.8, label="EP-05a (target VQ-3, Qt. ranking)"),
    "EP-06a": dict(color=VQ_COLOR["VQ-3"], ls="-.", marker="P", lw=1.8, label="EP-06a (target VQ-3, Analogy)"),
    "EP-10a": dict(color=VQ_COLOR["VQ-3"], ls="-",  marker="H", lw=1.6, label="EP-10a (target VQ-3, Kinetic)"),
    "EP-08a": dict(color=VQ_COLOR["VQ-4"], ls=":",  marker="x", lw=1.8, label="EP-08a (target VQ-4, Replication)"),
    "EP-09a": dict(color=VQ_COLOR["VQ-4"], ls="--", marker="+", lw=1.8, label="EP-09a (target VQ-4, Benchmark)"),
}

# Small multiples (R1 revision, Referee 2 minor 2): one panel per EP so that no
# two traces share an axis and nothing overlaps. Panels follow the Fig. 2 column
# order (VQ target). Each trace is a cumulative maximum, so it is drawn as a step.
# figsize is the printed size (15 cm ~ 5.9 in), so the font sizes below are the
# sizes that appear on the page.
plt.rcParams.update({"font.size": 8})
ORDER = ["EP-02a", "EP-01a", "EP-07a", "EP-03a", "EP-04a",
         "EP-05a", "EP-06a", "EP-10a", "EP-08a", "EP-09a"]
TITLE = {ep: EP_STYLE[ep]["label"].split(" (")[0] for ep in ORDER}
# second title line = evidence aspect only (the VQ target is carried by colour)
ASPECT = {ep: EP_STYLE[ep]["label"].split(", ")[-1].rstrip(")") for ep in ORDER}
ASPECT["EP-02a"] = "Identity (VQ-1)"
BANDS = [(0, "#F5F5F5"), (1, "#F0F4F8"), (2, "#E6F0E9"), (3, "#FDF1E6"), (4, "#F7E6EE")]

fig, axes = plt.subplots(2, 5, figsize=(5.9, 3.5), sharex=True, sharey=True)
for ax, ep in zip(axes.flat, ORDER):
    for y, color in BANDS:
        ax.axhspan(y - 0.5, y + 0.5, facecolor=color, zorder=0)
    color = EP_STYLE[ep]["color"]
    ax.step(df.index, df[ep].values, where="post", color=color, lw=1.8, zorder=3)
    ax.plot(df.index, df[ep].values, ls="none", marker="o", ms=2.8,
            color=color, zorder=4)
    ax.set_title(f"{TITLE[ep]}\n{ASPECT[ep]}", fontsize=8, pad=3)
    ax.set_xlim(1968, 2028)
    ax.set_ylim(-0.5, 4.5)
    ax.set_xticks([1980, 2020])
    ax.set_xticklabels(["1980", "2020"], fontsize=7.5)
    ax.set_yticks([0, 1, 2, 3, 4])
    ax.set_yticklabels(["0", "min.", "VQ-2", "VQ-3", "VQ-4"], fontsize=7.5)
    ax.grid(True, axis="y", alpha=0.25, linestyle="--")
    ax.tick_params(length=2, pad=1.5)

# Editorial callouts, placed inside the panel they refer to
_box = dict(boxstyle="round,pad=0.2", facecolor="white", edgecolor="#BBBBBB", alpha=0.9)
axes.flat[ORDER.index("EP-03a")].annotate(
    "Mazet 2021", xy=(2021, 2.5), xytext=(1972, 3.7), fontsize=7, bbox=_box,
    arrowprops=dict(arrowstyle="->", color="#444444", lw=0.9))
for ep in ("EP-08a", "EP-09a"):
    axes.flat[ORDER.index(ep)].text(
        1971, 3.7, "below audit\nPartial", fontsize=7, va="center", bbox=_box)

fig.supxlabel("Year", fontsize=8.5)
fig.supylabel("Maximum filling status reached (ordinal)", fontsize=8.5)
# Group key: colour = VQ target group
from matplotlib.lines import Line2D
handles = [Line2D([], [], color=VQ_COLOR[g], lw=2, label=f"{g} target") for g in VQ_COLOR]
fig.legend(handles=handles, loc="upper center", ncol=3, fontsize=7.5,
           frameon=False, bbox_to_anchor=(0.5, 1.02))
fig.subplots_adjust(top=0.84, wspace=0.14, hspace=0.5)

for ext in ("svg", "pdf", "png"):
    out_path = OUT / f"fig3_vq_trajectory.{ext}"
    kwargs = {"bbox_inches": "tight"}
    if ext == "png":
        kwargs["dpi"] = 600
    plt.savefig(out_path, **kwargs)
    print(f"wrote {out_path}")
plt.close(fig)
