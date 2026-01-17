import matplotlib.pyplot as plt

categories = ['A' , 'B' , 'C' , 'D']
values = [10, 15, 7, 12]

# Vertical Bar
plt.bar(categories, values)

# Horizontal Bar
plt.barh(categories, values)

plt.title('Category values')
plt.xlabel('Categories')
plt.ylabel('Values')

plt.show()

# Grouped bar Chart
categories = ["A", "B", "C", "D"]
values1 = [10, 15, 7, 12]
values2 = [8, 12, 5, 10]

plt.bar(categories, values1, width=0.4, label="2025", align="edge", color="skyblue")
plt.bar(categories, values2, width=0.4, label="2026", align="center", color="orange")

plt.title("Category Comparison")
plt.xlabel("Categories")
plt.ylabel("Values")
plt.legend()
plt.show()