# import matplotlib.pyplot as plt

# x = [5, 7, 8, 7, 2, 17, 2, 9, 4, 11]
# y = [99, 86, 87, 88, 100, 86, 103, 87, 94, 78]

# plt.scatter(x, y)

# plt.title('Simple Scatter Plot')
# plt.xlabel('X Values')
# plt.ylabel('Y Values')
# plt.show()




import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 2*np.pi, 50)

y1 = np.sin(x)
y2 = np.cos(x)

plt.scatter(x, y1)
plt.scatter(x, y2)

plt.title("sin(x) and cos(x)")
plt.xlabel("x values")
plt.ylabel("y values")
plt.show()
