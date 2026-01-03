import matplotlib.pyplot as plt

categories = ["A", "B", "C", "D"]
values = [20, 30, 25, 25]

plt.pie(values, labels=categories)

plt.title("Category Distribution")
plt.show()

# Percentage
colors = ["skyblue", "orange", "green", "pink"]
plt.pie(values, labels=categories, colors=colors, autopct="%1.1f%%", startangle=90)

plt.title("Category Distribution with Percentage")
plt.show()
