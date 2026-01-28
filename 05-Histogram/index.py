import matplotlib.pyplot as plt

data = [22, 87, 5, 43, 56, 73, 55, 54, 11, 20, 51, 5, 79, 31, 27]

plt.hist(data, bins=5, color="skyblue", edgecolor="black")

plt.title("Histogram")
plt.xlabel("Value Range")
plt.ylabel("Frequency")

plt.show()
