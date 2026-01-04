# import matplotlib.pyplot as plt

# x = [1,2,3,4,5]
# y = [10,0,15,25,30]

# plt.plot(x , y)
# plt.title('Simple Line Plot')
# plt.xlabel('X Axis')
# plt.ylabel('Y Axis')

# plt.show()






import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [10, 0, 15, 25, 30]

plt.plot(x, y, label="Data Line")   # legend ke liye label

plt.title("Simple Line Plot")
plt.xlabel("X Axis")
plt.ylabel("Y Axis")

plt.legend()        # legend
plt.grid(True)     # grid

plt.show()
