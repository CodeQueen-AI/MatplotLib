import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [10, 15, 13, 18, 20]
sizes = [100, 300, 200, 500, 400]

plt.scatter(x, y, s=sizes, alpha=0.6)
plt.title("Bubble Chart")
plt.xlabel("X values")
plt.ylabel("Y values")
plt.show()
