#!/usr/bin/env python3
"""Generate the compact appendix summary for Experiments IV and V."""

from pathlib import Path

import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np


ROOT = Path(__file__).resolve().parent

COLORS = {
    "VG": "#2B6CB0",
    "OI": "#C05621",
    "PSG": "#2F855A",
    "pass": "#2F855A",
    "fail": "#FFFFFF",
    "object": "#2B6CB0",
    "triplet": "#C05621",
}


def style() -> None:
    mpl.rcParams.update(
        {
            "font.family": "DejaVu Sans",
            "font.size": 7.2,
            "axes.titlesize": 8.2,
            "axes.labelsize": 7.2,
            "xtick.labelsize": 6.7,
            "ytick.labelsize": 6.7,
            "legend.fontsize": 6.4,
            "axes.linewidth": 0.7,
            "xtick.major.width": 0.6,
            "ytick.major.width": 0.6,
            "pdf.fonttype": 42,
            "ps.fonttype": 42,
        }
    )


def panel_grounding(ax: plt.Axes) -> None:
    rows = [
        ("VG / EGTR", 90.09, 67.85, 61.25),
        ("VG / RelTR", 78.71, 66.04, 52.19),
        ("VG / SGTR", 81.21, 64.74, 52.74),
        ("OI / EGTR", 98.02, 56.83, 55.40),
        ("OI / SGTR", 96.53, 58.50, 56.38),
        ("PSG / Motifs", 64.16, 84.93, 54.91),
        ("PSG / VCTree", 64.16, 84.80, 54.98),
        ("PSG / PSGF", 66.97, 85.96, 57.76),
        ("PSG / PSGTR", 77.71, 83.08, 65.00),
    ]

    y = np.arange(len(rows))[::-1]
    labels = [row[0] for row in rows]
    localization = np.asarray([row[1] for row in rows])
    recognition = np.asarray([row[2] for row in rows])
    grounded = np.asarray([row[3] for row in rows])

    for yi, values in zip(y, zip(localization, recognition, grounded)):
        ax.hlines(yi, min(values), max(values), color="#CBD5E0",
                  linewidth=1.0, zorder=0)
    ax.scatter(localization, y, marker="s", s=21, color="#2B6CB0",
               edgecolor="white", linewidth=0.5, label="Localized", zorder=3)
    ax.scatter(recognition, y, marker="o", s=21, color="#C05621",
               edgecolor="white", linewidth=0.5, label="Recognition | loc.",
               zorder=3)
    ax.scatter(grounded, y, marker="D", s=20, color="#2F855A",
               edgecolor="white", linewidth=0.5, label="Grounded", zorder=3)

    ax.legend(
        loc="lower center",
        bbox_to_anchor=(0.5, 1.0),
        frameon=False,
        ncol=3,
        handletextpad=0.3,
        columnspacing=0.7,
        borderaxespad=0.1,
    )
    ax.set_yticks(y)
    ax.set_yticklabels(labels)
    ax.set_xlim(48, 101)
    ax.set_ylim(-0.6, len(rows) - 0.4)
    ax.set_xlabel("Rate (%)")
    ax.set_title("(a) SGDet bottleneck decomposition", loc="left", pad=27)
    ax.grid(axis="x", color="#E2E8F0", linewidth=0.5, alpha=0.8)


def panel_validation(ax: plt.Axes) -> None:
    rows = [
        ("S17", 0.504, 3.210, True, (0.504, 3.38)),
        ("S23", 0.511, 3.235, True, (0.525, 3.48)),
        ("S31", 0.427, 1.589, False, (0.435, 1.69)),
        ("G17", 0.497, 3.216, False, (0.486, 2.96)),
        ("G23", 0.518, 3.231, True, (0.528, 2.96)),
        ("G31", 0.490, 3.210, False, (0.483, 3.48)),
    ]
    for label, gain, ece, passed, offset in rows:
        ax.scatter(
            gain,
            ece,
            s=25,
            facecolor=COLORS["pass"] if passed else COLORS["fail"],
            edgecolor=COLORS["pass"] if passed else "#4A5568",
            linewidth=0.9,
            zorder=3,
        )
        ax.annotate(
            label,
            (gain, ece),
            xytext=offset,
            textcoords="data",
            fontsize=5.7,
            color="#1A202C",
            ha="center",
            va="center",
            arrowprops={
                "arrowstyle": "-",
                "color": "#A0AEC0",
                "linewidth": 0.5,
                "shrinkA": 2,
                "shrinkB": 3,
            },
        )

    handles = [
        mpl.lines.Line2D(
            [0],
            [0],
            marker="o",
            linestyle="",
            markersize=4.5,
            markerfacecolor=COLORS["pass"],
            markeredgecolor=COLORS["pass"],
            label="Gate pass",
        ),
        mpl.lines.Line2D(
            [0],
            [0],
            marker="o",
            linestyle="",
            markersize=4.5,
            markerfacecolor="white",
            markeredgecolor="#4A5568",
            label="Gate fail",
        ),
    ]
    ax.legend(handles=handles, loc="upper left", frameon=False, ncol=1,
              handletextpad=0.4, borderaxespad=0.1)
    ax.set_xlim(0.415, 0.535)
    ax.set_ylim(1.35, 3.55)
    ax.set_xlabel("Object Top-1 gain (points)")
    ax.set_ylabel("ECE after tuning (%)")
    ax.set_title("(b) Validation gain and calibration", loc="left", pad=5)
    ax.grid(color="#E2E8F0", linewidth=0.5, alpha=0.8)


def panel_transfer(ax: plt.Axes) -> None:
    values = {
        ("GQA", "Object"): [8.57, 8.57, 10.92, 8.57, 8.57, 8.62],
        ("GQA", "Triplet"): [5.88, 5.88, 7.22, 5.88, 5.88, 5.94],
        ("VRD", "Object"): [6.13, 6.16, 6.71, 6.16, 6.16, 6.16],
        ("VRD", "Triplet"): [1.33, 1.37, 1.54, 1.37, 1.37, 1.37],
    }
    rows = [
        ("GQA", "Object"),
        ("GQA", "Triplet"),
        ("VRD", "Object"),
        ("VRD", "Triplet"),
    ]
    for y, (dataset, metric) in enumerate(rows[::-1]):
        vals = np.asarray(values[(dataset, metric)])
        color = COLORS[metric.lower()]
        ax.hlines(y, vals.min(), vals.max(), color=color, linewidth=3.1,
                  alpha=0.45)
        ax.scatter(vals, np.full_like(vals, y, dtype=float), s=10,
                   color=color, alpha=0.65, linewidth=0)
        median = float(np.median(vals))
        ax.scatter(median, y, s=27, color=color, edgecolor="white",
                   linewidth=0.6, zorder=3)
        label_y = y - 0.10 if y == 3 else y + 0.10
        label_va = "top" if y == 3 else "bottom"
        ax.text(median + 0.10, label_y, f"{median:.2f}", va=label_va,
                fontsize=6.2, color="#1A202C")

    ax.axvline(0, color="#4A5568", linewidth=0.7)
    ax.set_yticks(range(4))
    ax.set_yticklabels([f"{d} {m}" for d, m in rows[::-1]])
    ax.set_xlim(0, 11.8)
    ax.set_ylim(-0.15, 3.18)
    ax.set_xlabel("Accuracy gain (points)")
    ax.set_title("(c) Frozen-transfer gains", loc="left", pad=5)
    ax.grid(axis="x", color="#E2E8F0", linewidth=0.5, alpha=0.8)


def main() -> None:
    style()
    fig, axes = plt.subplots(
        1,
        3,
        figsize=(7.05, 2.60),
        gridspec_kw={"width_ratios": [1.18, 1.0, 1.0]},
    )
    panel_grounding(axes[0])
    panel_validation(axes[1])
    panel_transfer(axes[2])
    fig.subplots_adjust(left=0.12, right=0.99, bottom=0.20, top=0.78,
                        wspace=0.52)
    for suffix in ("pdf", "png"):
        fig.savefig(
            ROOT / f"appendix_result_summary.{suffix}",
            dpi=300,
            bbox_inches="tight",
            pad_inches=0.03,
        )
    plt.close(fig)


if __name__ == "__main__":
    main()
