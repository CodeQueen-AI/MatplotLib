import matplotlib.pyplot as plt

data = [7, 8, 5, 6, 9, 12, 10, 8, 6, 5, 14, 15, 8]

plt.boxplot(data)
plt.title("Simple Box Plot")
plt.ylabel("Values")

plt.show()

# Multiple Box Plots
data1 = [7, 8, 5, 6, 9, 12]
data2 = [10, 12, 15, 8, 9, 11]

plt.boxplot([data1, data2], labels=["Group 1", "Group 2"], patch_artist=True,
            boxprops=dict(facecolor="lightgreen"))

plt.title("Multiple Box Plots Comparison")
plt.ylabel("Values")

plt.show()
