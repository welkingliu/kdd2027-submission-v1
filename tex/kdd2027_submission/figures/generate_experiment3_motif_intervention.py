#!/usr/bin/env python3
"""Render the formal Experiment III motif-intervention summary."""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


OUT_DIR = Path(__file__).resolve().parent

MODELS = ("Neural Motifs", "SGG Transformer")
COLORS = ("#147D73", "#D27624")
MARKERS = ("o", "s")

METRICS = ("PIR (all)", "MAR (correct)", "WSR (wrong)")
ESTIMATES = {
    "Neural Motifs": (88.87, 1.74, 96.60),
    "SGG Transformer": (86.18, 1.05, 99.51),
}
INTERVALS = {
    "Neural Motifs": ((85.66, 91.82), (0.00, 4.85), (95.32, 97.77)),
    "SGG Transformer": ((82.17, 89.79), (0.00, 2.89), (99.08, 99.84)),
}

CONTROL_DELTAS = {
    "Neural Motifs": (-4.26, -51.30, -0.08),
    "SGG Transformer": (-5.96, -57.89, 2.13),
}
CONTROL_INTERVALS = {
    "Neural Motifs": ((-6.85, -1.78), (-72.42, -31.24), (-1.65, 1.46)),
    "SGG Transformer": ((-10.11, -2.57), (-70.57, -43.60), (1.00, 3.46)),
}


def asymmetric_error(value, interval):
    return np.array([[value - interval[0]], [interval[1] - value]])


def main():
    plt.rcParams.update(
        {
            "font.family": "DejaVu Sans",
            "font.size": 6.5,
            "axes.titlesize": 7.5,
            "axes.labelsize": 6.5,
            "legend.fontsize": 5.8,
            "xtick.labelsize": 6,
            "ytick.labelsize": 6.5,
            "pdf.fonttype": 42,
            "ps.fonttype": 42,
        }
    )

    fig, axes = plt.subplots(
        2,
        1,
        figsize=(3.35, 3.35),
        gridspec_kw={"height_ratios": (1.0, 1.06), "hspace": 0.68},
    )
    y = np.arange(len(METRICS))[::-1]
    offsets = (0.13, -0.13)

    ax = axes[0]
    for model_idx, (model, color, marker, offset) in enumerate(
        zip(MODELS, COLORS, MARKERS, offsets)
    ):
        for idx, (metric, value, interval) in enumerate(
            zip(METRICS, ESTIMATES[model], INTERVALS[model])
        ):
            ypos = y[idx] + offset
            ax.errorbar(
                value,
                ypos,
                xerr=asymmetric_error(value, interval),
                fmt=marker,
                color=color,
                ecolor=color,
                markersize=4.2,
                capsize=2.0,
                elinewidth=1.1,
                markeredgewidth=0,
                label=model if idx == 0 else None,
                zorder=3,
            )
            label_right = value < 98.0
            lift_bottom_right = idx == 2 and model_idx == 1
            y_text_offset = 5 if model_idx == 0 or lift_bottom_right else -7
            ax.annotate(
                f"{value:.2f}",
                xy=(value, ypos),
                xytext=((4 if label_right else -4), y_text_offset),
                textcoords="offset points",
                va="bottom" if y_text_offset > 0 else "top",
                ha="left" if label_right else "right",
                fontsize=5.7,
                bbox={"facecolor": "white", "edgecolor": "none", "pad": 0.2},
                zorder=4,
            )

    ax.set_yticks(y, METRICS)
    ax.set_xlim(-2, 104)
    ax.set_ylim(-0.45, 2.55)
    ax.set_xlabel("Persistence after terminal removal (%)")
    ax.set_title(
        "a  Persistence by clean-prediction stratum",
        loc="left",
        fontweight="bold",
    )
    ax.grid(axis="x", color="#D9DEE2", linewidth=0.8)
    ax.spines[["top", "right", "left"]].set_visible(False)
    ax.tick_params(axis="y", length=0)
    ax.legend(
        loc="upper left",
        bbox_to_anchor=(0.01, 0.98),
        ncol=1,
        frameon=False,
        borderaxespad=0,
    )

    ax = axes[1]
    for model_idx, (model, color, marker, offset) in enumerate(
        zip(MODELS, COLORS, MARKERS, offsets)
    ):
        for idx, (metric, value, interval) in enumerate(
            zip(METRICS, CONTROL_DELTAS[model], CONTROL_INTERVALS[model])
        ):
            ypos = y[idx] + offset
            ax.errorbar(
                value,
                ypos,
                xerr=asymmetric_error(value, interval),
                fmt=marker,
                color=color,
                ecolor=color,
                markersize=4.2,
                capsize=2.0,
                elinewidth=1.1,
                markeredgewidth=0,
                zorder=3,
            )
            lift_bottom_right = idx == 2 and model_idx == 1
            x_text_offset = 5 if lift_bottom_right else 0
            y_text_offset = 5 if model_idx == 0 or lift_bottom_right else -7
            ax.annotate(
                f"{value:+.2f}",
                xy=(value, ypos),
                xytext=(x_text_offset, y_text_offset),
                textcoords="offset points",
                va="bottom" if y_text_offset > 0 else "top",
                ha="left" if lift_bottom_right else "center",
                fontsize=5.7,
                bbox={"facecolor": "white", "edgecolor": "none", "pad": 0.2},
                zorder=4,
            )

    ax.axvline(0, color="#30363B", linewidth=0.9, zorder=1)
    ax.set_yticks(y, METRICS)
    ax.set_xlim(-78, 10)
    ax.set_ylim(-0.45, 2.55)
    ax.set_xlabel("Terminal minus matched control (points)")
    ax.set_title(
        "b  Terminal effect relative to matched control",
        loc="left",
        fontweight="bold",
    )
    ax.grid(axis="x", color="#D9DEE2", linewidth=0.8)
    ax.spines[["top", "right", "left"]].set_visible(False)
    ax.tick_params(axis="y", length=0)

    fig.subplots_adjust(left=0.22, right=0.985, top=0.96, bottom=0.115)

    for suffix in ("pdf", "png"):
        path = OUT_DIR / f"experiment3_motif_intervention.{suffix}"
        fig.savefig(path, dpi=300, bbox_inches="tight")
    plt.close(fig)


if __name__ == "__main__":
    main()
