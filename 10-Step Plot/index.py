import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [10, 18, 14, 22, 30]

fig = plt.figure(figsize=(8,5))

plt.stem(x, y)

plt.title("Simple STEM Plot")
plt.xlabel("Days")
plt.ylabel("Sales")

fig.savefig("stem_plot.png")

plt.show()
