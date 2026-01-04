
import matplotlib.pyplot as plt
import numpy as np

x = np.random.randn(1000)
y = np.random.randn(1000)

plt.hexbin(x, y, gridsize=30)
plt.colorbar(label="Count")
plt.title("Hexbin Plot")
plt.show()
