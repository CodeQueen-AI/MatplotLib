import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [10, 15, 12, 18, 20]

plt.step(x, y)

# Annotation: max value highlight
max_index = y.index(max(y))
plt.annotate(
    "Peak Sales",
    xy=(x[max_index], y[max_index]),
    xytext=(x[max_index]-1, y[max_index]+2),
    arrowprops=dict(arrowstyle="->", color="red")
)

plt.title("Step Plot with Annotation")
plt.xlabel("Days")
plt.ylabel("Sales")
plt.show()
