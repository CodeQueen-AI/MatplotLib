import numpy as np
import matplotlib.pyplot as plt

data = np.array([
    [5, 10, 15],
    [10, 20, 25],
    [20, 30, 35]
])

plt.imshow(data)
plt.colorbar()

plt.xticks([0, 1, 2], ["Col1", "Col2", "Col3"])
plt.yticks([0, 1, 2], ["Row1", "Row2", "Row3"])
plt.title("Heatmap using Matplotlib only")

plt.show()