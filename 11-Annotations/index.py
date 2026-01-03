import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [10, 20, 15, 25, 30]

plt.plot(x, y, marker="o")

plt.title("Sales Trend")
plt.xlabel("Days")
plt.ylabel("Sales")

plt.text(3, 15, "Midpoint", fontsize=10, color="red")

plt.show()