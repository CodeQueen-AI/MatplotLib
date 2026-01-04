import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [10, 0, 15, 25, 30]

plt.plot(x, y, label="Data Line")   

plt.title("Simple Line Plot")
plt.xlabel("X Axis")
plt.ylabel("Y Axis")

plt.legend()       
plt.grid(True)   

plt.show()
