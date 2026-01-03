import matplotlib.pyplot as plt

# Vertical Bar
# categories = ['A' , 'B' , 'C' , 'D']
# values = [10, 15, 7, 12]

# plt.bar(categories, values)

# plt.title('Category values')
# plt.xlabel('Categories')
# plt.ylabel('Values')

# plt.show()

# # Horizontal Bar
# plt.bar(categories, values)

# Grouped Bar Chart
categories = ['A' , 'B' , 'C' , 'D']
values1 = [10, 15, 7, 12]
values2 = [8, 12, 5, 10]

plt.bar(categories, values1, width=0.4, label='2025' , align='edge', color='green')
plt.bar(categories, values1, width=0.4, label='2026' , align='center', color='orange')

plt.title('Category Comparison')
plt.xlabel('Categories')
plt.label('Values')
plt.legend()
plt.show()




