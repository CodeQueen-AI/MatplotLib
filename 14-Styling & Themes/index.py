import matplotlib.pyplot as plt

# ---------------- STYLE / THEME ----------------
plt.style.use("ggplot")   # try: dark_background, bmh, classic

# ---------------- DATA ----------------
x = [1, 2, 3, 4, 5]
y = [10, 18, 14, 22, 30]

# ---------------- FIGURE ----------------
plt.figure(figsize=(8, 5))   # size control

# ---------------- PLOT ----------------
plt.plot(
    x, y,
    color="purple",
    linewidth=3,
    linestyle="--",
    marker="o",
    markersize=8,
    label="Sales Growth"
)

# ---------------- LABELS & TITLE ----------------
plt.title("Complete Styled Line Plot", fontsize=14)
plt.xlabel("Days", fontsize=11)
plt.ylabel("Sales", fontsize=11)

# ---------------- GRID ----------------
plt.grid(True, linestyle=":", alpha=0.7)

# ---------------- LEGEND ----------------
plt.legend(loc="upper left")

# ---------------- ANNOTATION ----------------
plt.annotate(
    "Highest Point",
    xy=(5, 30),
    xytext=(3.5, 26),
    arrowprops=dict(arrowstyle="->", color="black")
)

# ---------------- SAVE FIGURE ----------------
plt.savefig("styled_plot.png", dpi=300, bbox_inches="tight")

# ---------------- SHOW ----------------
plt.show()
