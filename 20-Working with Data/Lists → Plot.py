import matplotlib.pyplot as plt

days = [1, 2, 3, 4, 5]
sales = [10, 18, 14, 22, 30]

plt.plot(days, sales, marker="o")
plt.title("Sales Data")
plt.xlabel("Days")
plt.ylabel("Sales")
plt.show()
