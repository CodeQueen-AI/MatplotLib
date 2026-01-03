import pandas as pd
import matplotlib.pyplot as plt

data = {
    "Day": [1, 2, 3, 4, 5],
    "Sales": [10, 18, 14, 22, 30]
}

df = pd.DataFrame(data)

plt.plot(df["Day"], df["Sales"], marker="o")
plt.title("Sales from DataFrame")
plt.show()
