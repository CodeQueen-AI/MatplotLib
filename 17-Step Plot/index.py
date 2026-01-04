# import matplotlib.pyplot as plt
# x = [1, 2, 3, 4, 5]
# y = [10, 15, 12, 18, 20]

# plt.step(x, y)

# max_index = y.index(max(y))
# plt.annotate(
#     "Peak Sales",
#     xy=(x[max_index], y[max_index]),
#     xytext=(x[max_index]-1, y[max_index]+2),
#     arrowprops=dict(arrowstyle="->", color="red")
# )

# plt.title("Step Plot with Annotation")
# plt.xlabel("Days")
# plt.ylabel("Sales")
# plt.show()

import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [10, 18, 14, 22, 30]

# Create figure
fig = plt.figure(figsize=(8,5))

plt.stem(x, y)

# Simple annotation (highest point)
max_index = y.index(max(y))
plt.text(x[max_index], y[max_index]+1, "Peak Sales")

plt.title("Simple STEM Plot")
plt.xlabel("Days")
plt.ylabel("Sales")

# Save the figure
fig.savefig("stem_plot.png")

plt.show()
