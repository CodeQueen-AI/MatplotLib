import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [10, 20, 15, 25, 30]

plt.fill_between(x, y)

plt.title("Simple Area Plot")
plt.xlabel("X Values")
plt.ylabel("Y Values")

plt.show()
