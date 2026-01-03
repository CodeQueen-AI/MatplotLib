import matplotlib.pyplot as plt

x = [5, 7, 8, 7, 2, 17, 2, 9, 4, 11]
y = [99, 86, 87, 88, 100, 86, 103, 87, 94, 78]

plt.scatter(x, y)

plt.title('Simple Scatter Plot')
plt.xlabel('X Values')
plt.ylabel('Y Values')
plt.show()