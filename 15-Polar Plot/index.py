import matplotlib.pyplot as plt
import numpy as np

theta = np.linspace(0, 2 * np.pi, 100)
r = 1 + np.sin(theta)

plt.polar(theta, r)
plt.title("Polar Plot")
plt.show()
