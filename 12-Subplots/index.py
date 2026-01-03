import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y1 = [10, 20, 15, 25, 30]
y2 = [5, 15, 10, 20, 25]
y3 = [7, 14, 9, 18, 12]
y4 = [12, 18, 15, 20, 25]

plt.subplot(2, 2, 1)
plt.plot(x, y1, color="blue")
plt.title("Sales")

plt.subplot(2, 2, 2)
plt.plot(x, y2, color="green")
plt.title("Profit")

plt.subplot(2, 2, 3)
plt.plot(x, y3, color="red")
plt.title("Expenses")

plt.subplot(2, 2, 4)
plt.plot(x, y4, color="orange")
plt.title("Revenue")

plt.tight_layout()
plt.show()
