import math

import matplotlib

matplotlib.use("svg")
import matplotlib.pyplot as plt
from matplotlib.patches import Arc

GREEN, ORANGE, BLUE, PURPLE, GREY = "#2e7d32", "#ef6c00", "#1565c0", "#6a1b9a", "#9e9e9e"
LIGHT_BLUE, LIGHT_PURPLE, LIGHT_GREY = "#e3ecf8", "#e1d3ec", "#d6d6d6"
plt.rcParams.update({"font.size": 12, "svg.fonttype": "path"})


def plane(xlim, ylim, width=6.5):
    height = width * (ylim[1] - ylim[0]) / (xlim[1] - xlim[0])
    fig, ax = plt.subplots(figsize=(width, height))
    ax.set_xlim(*xlim)
    ax.set_ylim(*ylim)
    ax.set_aspect("equal")
    ax.spines[["top", "right"]].set_visible(False)
    ax.spines[["left", "bottom"]].set_position("zero")
    ax.grid(color="#eeeeee")
    ax.set_axisbelow(True)
    no_zero = plt.FuncFormatter(lambda v, _: "" if abs(v) < 1e-9 else f"{v:g}")
    ax.xaxis.set_major_formatter(no_zero)
    ax.yaxis.set_major_formatter(no_zero)
    return fig, ax


def save(fig, name):
    fig.savefig(name, format="svg", bbox_inches="tight")
    print("saved", name)


def angle(ax, deg, r=0.2, color=BLUE, start=0):
    ax.add_patch(Arc((0, 0), 2 * r, 2 * r, theta1=start, theta2=deg, color=color, lw=1.5))


def circle(ax, upto=360, color=GREY, lw=1.2):
    ts = [math.radians(d / 4) for d in range(0, 4 * upto + 1)]
    ax.plot([math.cos(t) for t in ts], [math.sin(t) for t in ts], color=color, lw=lw)


rad = math.radians
