import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [10, 15, 20, 18, 25]

# plt.figure(figsize=(8, 5))

plt.plot(x, y, marker = 'o' , label='Growth')

plt.title('Company Growth')
plt.xlabel('Years')
plt.ylabel("Value")