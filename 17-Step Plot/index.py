import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [10, 15, 12, 18, 20]

plt.step(x, y)
plt.title("Simple Step Plot")
plt.xlabel("Days")
plt.ylabel("Sales")
plt.show()