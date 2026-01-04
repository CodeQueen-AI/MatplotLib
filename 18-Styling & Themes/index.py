import matplotlib.pyplot as plt

plt.style.use("dark_background")

x = [1, 2, 3, 4, 5]
y = [10, 18, 14, 22, 30]

plt.figure(figsize=(9, 5))
plt.plot(x, y, color="#00E5FF", linewidth=3, linestyle="-", marker="o", markersize=9, markerfacecolor="white", markeredgewidth=2, label="Sales Trend")

plt.title("Sales Growth Analysis", fontsize=16, fontweight="bold", pad=15)
plt.xlabel("Days", fontsize=12)
plt.ylabel("Sales Units", fontsize=12)

plt.grid(True, linestyle="--", alpha=0.3)

plt.legend(loc="upper left", frameon=True, fancybox=True, shadow=True)

plt.annotate(
    "Peak Value",
    xy=(5, 30),
    xytext=(3.5, 26),
    fontsize=11,
    arrowprops=dict(
        arrowstyle="->",
        color="white",
        lw=1.5
    )
)

plt.show()