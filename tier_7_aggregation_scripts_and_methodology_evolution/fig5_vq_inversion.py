"""
Fig. 5: VQ hierarchy vs. actual filling order — core claim visualisation.

Two panels (drawn in a single shared axis so the A/B gap can be controlled directly):
  A. Scientific-logical priority order from Stage 3 (VQ-1 foundation -> VQ-4 top).
  B. Empirical filling order across 54 years of Kumada chemistry, with year-range
     annotations derived from Fig. 2 / Fig. 3 data.
Straight connecting arrows between the panels highlight the structural inversion.

R1 revision (2026-10-05, Referee 2 minor 1 "fonts too small"): redrawn at the
printed size. The canvas is exactly 15 cm wide (= \includegraphics width in the
RSC source; axes fill the figure, saved without bbox_inches="tight"), so every
fontsize below is the point size on the page (all >= 7.5 pt). Text, colours and
the two-panel layout are unchanged. Two overlaps in the previous version are
removed: the VQ code no longer collides with the note in the panel-B boxes, and
the upper connector label now sits under its arrow (it touched the panel-A title).
"""
from pathlib import Path

import matplotlib.patches as mpatches
import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch

ROOT = Path(__file__).resolve().parents[1]
# Repository: output to ROOT/output. Deposit copy (Tier 7): ROOT is the deposit root and the
# output goes to rerun_output/ there (this figure reads no data file).
OUT = ROOT / "output" if (ROOT / "data").is_dir() else ROOT / "rerun_output"
OUT.mkdir(exist_ok=True)


# --- Font-size scale, ordered by the figure's information hierarchy ---
# The figure's message is the CONTRAST between panel A (normative order) and
# panel B (empirical order). Sizes are assigned by semantic importance:
# (sizes are print sizes in pt; floor 7.5 pt)
FS_PANEL_TITLE = 9.5    # A. / B. — the two worlds being contrasted (top level)
FS_VQ_CODE     = 9      # VQ-1..VQ-4 — the row identifiers (primary)
FS_CONNECT     = 8.5    # inversion labels — the claim itself (primary, emphasised)
FS_NOTE        = 7.5    # in-box descriptors — supporting evidence/detail
FS_AXIS        = 7.5    # vertical direction labels — auxiliary orientation
FS_SUBORD      = 7.5    # "built upon VQ-n" — most subordinate note
FS_CAPTION     = 7.5    # footnote caption

# --- Horizontal layout (single coordinate system) ---
# columns, left to right:
#   [A priority arrow+label] [A boxes] [gap for connectors] [B boxes] [B arrow+label]
A_BOX_W = 3.0                      # panel A boxes (fits "Quantitative reliability")
B_BOX_W = 4.15                     # panel B boxes (unchanged)
GAP = 2.1                          # connector gap

A_BOX_X = 1.3                      # left edge of A boxes (room for priority arrow)
A_BOX_R = A_BOX_X + A_BOX_W        # right edge of A boxes
B_BOX_X = A_BOX_R + GAP            # left edge of B boxes
B_BOX_R = B_BOX_X + B_BOX_W        # right edge of B boxes
A_BOX_CX = A_BOX_X + A_BOX_W / 2
B_BOX_CX = B_BOX_X + B_BOX_W / 2
GAP_CX = (A_BOX_R + B_BOX_X) / 2   # centre of the connector gap

XLIM = (0, B_BOX_R + 1.4)          # room for B's right-side arrow/label

# --- Vertical layout ---
BOX_H = 2.3
PITCH = 2.55
Y0 = 0.3
CM = 1 / 2.54
W_CM = 15.0                        # printed width
UY = 0.70                          # cm per y unit


def box_bottom(lvl):
    return Y0 + (lvl - 1) * PITCH


def box_center(lvl):
    return box_bottom(lvl) + BOX_H / 2


TOP = box_bottom(4) + BOX_H
YLIM = (-1.35, TOP + 1.45)
MIDY = (Y0 + TOP) / 2

fig = plt.figure(figsize=(W_CM * CM, (YLIM[1] - YLIM[0]) * UY * CM))
ax = fig.add_axes([0, 0, 1, 1])

ax.set_xlim(*XLIM)
ax.set_ylim(*YLIM)
ax.axis("off")

VQ_LABELS = {
    1: ("VQ-1", "Identity / purity"),
    2: ("VQ-2", "Methodology"),
    3: ("VQ-3", "Mechanism"),
    4: ("VQ-4", "Quantitative reliability"),
}

# ---------------- Panel A: epistemic priority order ----------------
ax.text(A_BOX_CX, TOP + 0.30, "A. Epistemic priority order\n(Stage 3 design)",
        ha="center", va="bottom", fontsize=FS_PANEL_TITLE, fontweight="bold")

for lvl, (code, name) in VQ_LABELS.items():
    y = box_bottom(lvl)
    ax.add_patch(mpatches.FancyBboxPatch(
        (A_BOX_X, y), A_BOX_W, BOX_H,
        boxstyle="round,pad=0.05,rounding_size=0.1",
        facecolor="#F0F0F0", edgecolor="black", linewidth=0.8,
    ))
    if lvl > 1:
        ax.text(A_BOX_CX, y + 1.70, code, ha="center", va="center",
                fontsize=FS_VQ_CODE, fontweight="bold")
        ax.text(A_BOX_CX, y + 1.08, name, ha="center", va="center",
                fontsize=FS_NOTE, fontstyle="italic")
        ax.text(A_BOX_CX, y + 0.50, f"built upon VQ-{lvl - 1}",
                ha="center", va="center", fontsize=FS_SUBORD, color="#666666")
    else:
        # VQ-1 has no foundation note: centre the two lines in the box
        ax.text(A_BOX_CX, y + 1.45, code, ha="center", va="center",
                fontsize=FS_VQ_CODE, fontweight="bold")
        ax.text(A_BOX_CX, y + 0.85, name, ha="center", va="center",
                fontsize=FS_NOTE, fontstyle="italic")

# Priority arrow + label on the left of panel A
ax.add_patch(FancyArrowPatch(
    (A_BOX_X - 0.40, Y0 + 0.15), (A_BOX_X - 0.40, TOP - 0.05), arrowstyle="->",
    mutation_scale=12, color="black", linewidth=1.1,
))
ax.text(A_BOX_X - 0.85, MIDY, "Priority\n(foundation → advanced)",
        rotation=90, ha="center", va="center",
        fontsize=FS_AXIS, fontweight="bold", linespacing=1.1)

# ---------------- Panel B: actual filling order ----------------
ax.text(B_BOX_CX, TOP + 0.30, "B. Actual filling order\n(empirical, 1972–2026)",
        ha="center", va="bottom", fontsize=FS_PANEL_TITLE, fontweight="bold")

# note text uses up to 3 lines where it helps keep boxes compact
FILL_STATE = {
    1: dict(color="#009E73", alpha=0.85,
            note="identity and purity reported\n(Kumada 1972 baseline)"),
    2: dict(color="#009E73", alpha=0.75,
            note="1976–2024: broadly filled\nacross two layers (Tamao 1976;\nBreitenfeld 2014, Li 2024)"),
    3: dict(color="#66C2A5", alpha=0.55,
            note="1975–2021: Morrell-Kochi 1975\nstarting point; Mazet 2021\ndecisive dppe-specific (49-y delay)"),
    4: dict(color="#E69F00", alpha=0.22,
            note="1972–2026: no filling paper\nfound in the locked audit\n(EP-08a, EP-09a)"),
}
for lvl, (code, name) in VQ_LABELS.items():
    y = box_bottom(lvl)
    state = FILL_STATE[lvl]
    ax.add_patch(mpatches.FancyBboxPatch(
        (B_BOX_X, y), B_BOX_W, BOX_H,
        boxstyle="round,pad=0.05,rounding_size=0.1",
        facecolor=state["color"], edgecolor="black", linewidth=0.8,
        alpha=state["alpha"],
    ))
    if lvl == 1:
        ax.text(B_BOX_CX, y + 1.55, code, ha="center", va="center",
                fontsize=FS_VQ_CODE, fontweight="bold")
        ax.text(B_BOX_CX, y + 0.72, state["note"], ha="center", va="center",
                fontsize=FS_NOTE, linespacing=1.1)
    else:
        ax.text(B_BOX_CX, y + 1.93, code, ha="center", va="center",
                fontsize=FS_VQ_CODE, fontweight="bold")
        ax.text(B_BOX_CX, y + 0.86, state["note"], ha="center", va="center",
                fontsize=FS_NOTE, linespacing=1.1)

# Empirical-filling arrow + label on the right of panel B
ax.add_patch(FancyArrowPatch(
    (B_BOX_R + 0.40, Y0 + 0.15), (B_BOX_R + 0.40, TOP - 0.05), arrowstyle="->",
    mutation_scale=12, color="#D55E00", linewidth=1.1,
))
ax.text(B_BOX_R + 0.85, MIDY, "Empirical\nfilling state",
        rotation=90, ha="center", va="center",
        fontsize=FS_AXIS, fontweight="bold", color="#D55E00", linespacing=1.1)

# ---------------- Straight connecting arrows ----------------
# Top: A VQ-4 (epistemic top) -> B VQ-4 (filled late or not found)
ax.add_patch(FancyArrowPatch(
    (A_BOX_R, box_center(4)), (B_BOX_X, box_center(4)),
    arrowstyle="->", mutation_scale=12, color="#D55E00", linewidth=1.3,
))
# Bottom: A VQ-2 (accessible) -> B VQ-2 (filled early)
ax.add_patch(FancyArrowPatch(
    (A_BOX_R, box_center(2)), (B_BOX_X, box_center(2)),
    arrowstyle="->", mutation_scale=12, color="#0072B2", linewidth=1.1,
))

# Connector labels (3 lines), centred in the gap: the upper label sits just
# below its arrow (clear of the panel titles), the lower label just above.
_lab_bbox = dict(boxstyle="round,pad=0.18", facecolor="white",
                 edgecolor="none", alpha=0.92)
ax.text(GAP_CX, box_center(4) - 0.25, "epistemically\ntop → late\nor not found",
        ha="center", va="top", fontsize=FS_CONNECT, fontweight="bold",
        color="#D55E00", fontstyle="italic", linespacing=1.15, bbox=_lab_bbox)
ax.text(GAP_CX, box_center(2) + 0.25, "practically\naccessible →\nfilled first",
        ha="center", va="bottom", fontsize=FS_CONNECT, fontweight="bold",
        color="#0072B2", fontstyle="italic", linespacing=1.15, bbox=_lab_bbox)

# --- Caption ---
ax.text(XLIM[1] / 2, Y0 - 0.35,
        "VQ-hierarchy filling-order inversion (Stage 3 convention): highest-documentary-resolution "
        "levels are\nfilled late or not found (one reaction system, n = 1; see caption).",
        ha="center", va="top", fontsize=FS_CAPTION, fontstyle="italic",
        linespacing=1.15)

for ext in ("svg", "pdf", "png"):
    out_path = OUT / f"fig5_vq_inversion.{ext}"
    # no bbox_inches="tight": keep the exact 15 cm print width
    kwargs = {"dpi": 600} if ext == "png" else {}
    plt.savefig(out_path, **kwargs)
    print(f"wrote {out_path}")
plt.close(fig)
