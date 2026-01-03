import matplotlib.pyplot as plt

categories = ["A", "B", "C", "D"]
values = [20, 30, 25, 25]

plt.pie(values, labels=categories)

plt.title("Category Distribution")
plt.show()
