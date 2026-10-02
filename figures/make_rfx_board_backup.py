#!/usr/bin/env python3
"""Backup-slide version of the RFX apex-vs-unexposed board (final pass, 2 Oct 2026).

Redraws TWO of the four panels of
  ../rfx/analysis/ebsd_orientations_all_2026-09-29/figures/board_apex_vs_unexposed.png
(the wide map class, historical partition A and matched-confidence partition B2)
at their on-slide size so that labels are ~7 pt instead of ~2 pt.
Data and plotting logic are those of that directory's make_figures.py
(draw_board, L118-275; map lists L24-50); the rfx directory is only read.
Rows: the intragranular, structure-function and pixel/pair groups; the
descriptive (grain-size / boundary) and indexing-quality rows are omitted on the
slide and remain in the full board. Colors follow the deck's tier key:
copper = field-exposed apex, purple = field-exposed side (low field),
teal band = unexposed apex range.

usage: make_rfx_board_backup.py <rfx analysis dir> <output png>
"""
import sys
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from matplotlib.lines import Line2D
from matplotlib.patches import Patch

SRC = Path(sys.argv[1])
OUT = Path(sys.argv[2])
pm = pd.read_csv(SRC / "per_map_table.csv", dtype={"map_id": str})

APEX_WIDE = ["20260726165136475", "20260802131227765", "20260802135843857"]
BASE_WIDE = ["20260803160203297", "20260803164200897", "20260818160723190", "20260818164736626"]
SIDE = ["20260727153135499", "20260727155854979", "20260810154627403",
        "20260810161620292", "20260810172408506", "20260810181431058"]

COPPER, PURPLE, TEAL, INK, MUTED = "#C7663A", "#4C2A85", "#007C83", "#17243A", "#5D6978"
XMIN, XMAX = -0.35, 1.35
BAND_LO, BAND_HI = 0.25, 0.75

ROWS = [
    ("group", None, "Intragranular (primary)"),
    ("metric", "grain_slope_median", r"per-grain $\theta(L)$ slope"),
    ("metric", "grain_intercept_median", r"per-grain $\theta(L)$ intercept"),
    ("metric", "gos_median_5", "GOS median"),
    ("metric", "grod_max_median_5", "GROD max median"),
    ("group", None, "Structure function (map)"),
    ("metric", "sf_slope", r"map $\theta(L)$ slope"),
    ("metric", "sf_intercept", r"map $\theta(L)$ intercept"),
    ("group", None, "Pixel / pair (cross-check)"),
    ("metric", "kam_dge3", r"interior KAM$_1$ ($\geq$3 px)"),
    ("metric", "kam1", r"KAM$_1$"),
    ("metric", "ma_010", r"MA 0–10$^\circ$"),
    ("metric", "ma_3um", r"pair MA $\leq$5$^\circ$ at 3 µm"),
    ("metric", "ma_3um_excl", "excluded pairs at 3 µm"),
]
YS = np.arange(len(ROWS) - 1, -1, -1, dtype=float)
FS = 7.0

plt.rcParams.update({"font.family": "DejaVu Sans", "font.size": FS,
                     "pdf.fonttype": 42, "axes.unicode_minus": True})


def vals(ids, col):
    return pd.to_numeric(pm.loc[pm.map_id.isin(ids), col], errors="coerce").to_numpy(float)


def norm_x(v, vmin, vmax):
    if not np.isfinite(v):
        return np.nan
    if vmax == vmin:
        return 0.5 if v == vmin else (XMAX + 1.0 if v > vmin else XMIN - 1.0)
    return BAND_LO + (BAND_HI - BAND_LO) * (v - vmin) / (vmax - vmin)


def marks(ax, y, xs, filled, color, z):
    for x in xs:
        if not np.isfinite(x):
            continue
        fc = color if filled else "none"
        kw = dict(linestyle="none", markerfacecolor=fc, markeredgecolor=color,
                  markeredgewidth=1.0, zorder=z, clip_on=False)
        if x < XMIN:
            ax.plot(XMIN, y, marker="<", markersize=5.5, **kw)
        elif x > XMAX:
            ax.plot(XMAX, y, marker=">", markersize=5.5, **kw)
        else:
            ax.plot(x, y, marker="o", markersize=5.0 if filled else 4.6, **kw)


def board(ax, part, title, report):
    ax.axvline(BAND_LO, color="#9A9A9A", lw=0.6, zorder=1)
    ax.axvline(BAND_HI, color="#9A9A9A", lw=0.6, zorder=1)
    for y, (kind, stem, lab) in zip(YS, ROWS):
        if kind == "group":
            if y < YS[0] - 0.1:
                ax.plot([XMIN, XMAX], [y + 0.5, y + 0.5], color="#D0D0D0", lw=0.6, zorder=0, clip_on=False)
            continue
        col = f"{stem}_{part}"
        base, apex, side = vals(BASE_WIDE, col), vals(APEX_WIDE, col), vals(SIDE, col)
        nb = int(np.isfinite(base).sum())
        report.append((part, stem, nb, int(np.isfinite(apex).sum())))
        if nb < 2:
            ax.text(0.5, y, "insufficient", va="center", ha="center", fontsize=FS - 0.5, color="#8A8A8A")
            continue
        fb = base[np.isfinite(base)]
        vmin, vmax = float(fb.min()), float(fb.max())
        ax.barh(y, BAND_HI - BAND_LO, left=BAND_LO, height=0.7, color=TEAL, alpha=0.22,
                edgecolor="none", zorder=0)
        marks(ax, y, [norm_x(v, vmin, vmax) for v in side], False, PURPLE, 3)
        marks(ax, y, [norm_x(v, vmin, vmax) for v in apex], True, COPPER, 4)
    ax.set_xlim(XMIN - 0.04, XMAX)
    ax.set_ylim(-0.6, len(ROWS) - 0.4)
    ax.set_yticks(YS)
    ax.set_yticklabels([r[2] for r in ROWS], fontsize=FS)
    for t, r in zip(ax.get_yticklabels(), ROWS):
        if r[0] == "group":
            t.set_style("italic"); t.set_color(MUTED)
    ax.set_xticks([BAND_LO, BAND_HI])
    ax.set_xticklabels(["min", "max"], fontsize=FS)
    ax.tick_params(axis="y", length=0, pad=2)
    ax.tick_params(axis="x", length=2.5, pad=1.5)
    for sp in ax.spines.values():
        sp.set_linewidth(0.7); sp.set_color("#333333")
    ax.set_title(title, fontsize=FS + 0.5, pad=3, color=INK)


fig, axes = plt.subplots(1, 2, figsize=(8.6 / 2.54, 5.7 / 2.54), dpi=300, sharey=True)
report = []
board(axes[0], "A", "historical", report)
board(axes[1], "B2", "matched CI ≥ 0.2", report)
axes[1].tick_params(axis="y", labelleft=False)
handles = [Line2D([], [], marker="o", ls="none", mfc=COPPER, mec=COPPER, ms=4.6, label="#3-25 apex"),
           Line2D([], [], marker="o", ls="none", mfc="none", mec=PURPLE, ms=4.4, label="#3-25 side"),
           Patch(facecolor=TEAL, alpha=0.22, label="unexposed range")]
fig.legend(handles=handles, loc="lower center", ncol=3, fontsize=FS - 0.5, frameon=False,
           handletextpad=0.3, columnspacing=0.7, bbox_to_anchor=(0.6, -0.02))
fig.text(0.685, 0.115, "unexposed apex maps #1-25, #2-25", ha="center", fontsize=FS - 0.5, color=MUTED)
fig.subplots_adjust(left=0.385, right=0.985, top=0.925, bottom=0.215, wspace=0.07)
fig.savefig(OUT, dpi=300)
for r in report:
    print(*r)
