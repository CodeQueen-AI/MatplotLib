import matplotlib.pyplot as plt

x = [1,2,3,4,5]
y = [5, 15, 10, 20, 25]

plt.plot(x, y , marker='o' , label='Profit')

plt.title('Profit Growth')
plt.xlabel("Months")
plt.ylabel("Profit")

plt.legend()
plt.grid()
plt.show()