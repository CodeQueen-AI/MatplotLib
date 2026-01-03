import matplotlib.pyplot as plt
import numpy as np

# Data using NumPy
x = np.array([1, 2, 3, 4, 5])
y = np.array([10, 20, 15, 25, 30])

plt.plot(x, y, marker="o", color="blue")
plt.title("NumPy Data Plot")
plt.xlabel("X Values")
plt.ylabel("Y Values")
plt.show()










import pandas as pd

# Pandas Series
sales = pd.Series([10, 20, 15, 25, 30], index=["Mon", "Tue", "Wed", "Thu", "Fri"])

sales.plot(marker="o", color="green", title="Weekly Sales")
plt.xlabel("Days")
plt.ylabel("Sales")
plt.show()





data = pd.DataFrame({
    "Days": ["Mon", "Tue", "Wed", "Thu", "Fri"],
    "Sales": [10, 20, 15, 25, 30],
    "Profit": [5, 10, 7, 12, 15]
})

plt.plot(data["Days"], data["Sales"], marker="o", label="Sales")
plt.plot(data["Days"], data["Profit"], marker="s", label="Profit")

plt.title("Sales vs Profit")
plt.xlabel("Days")
plt.ylabel("Values")
plt.legend()
plt.grid()
plt.show()

