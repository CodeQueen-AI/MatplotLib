import matplotlib.pyplot as plt
import numpy as np

x, y = np.meshgrid(np.arange(0, 5), np.arange(0, 5))
u = np.ones((5, 5))
v = np.ones((5, 5))

plt.quiver(x, y, u, v)
plt.title("Quiver Plot")
plt.show()
