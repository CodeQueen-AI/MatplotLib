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
