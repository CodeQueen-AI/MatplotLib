import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]

product_A = [10, 20, 30, 40, 50]
product_B = [5, 10, 15, 20, 25]

# plt.stackplot(x, product_A, product_B)

# plt.title("Simple Stacked Area Plot")
# plt.xlabel("X Values")
# plt.ylabel("Values")

# plt.show()


# plt.stackplot(
#     x,
#     product_A,
#     product_B,
#     labels=["Product A", "Product B"],
#     alpha=0.7
# )

# plt.title("Stacked Area Plot with Legend")
# plt.xlabel("X Values")
# plt.ylabel("Values")
# plt.legend(loc="upper left")

# plt.show()


product_C = [2, 5, 10, 15, 20]

plt.stackplot(
    x,
    product_A,
    product_B,
    product_C,
    labels=["Product A", "Product B", "Product C"],
    alpha=0.8
)

plt.title("Stacked Plot with 3 Products")
plt.xlabel("X Values")
plt.ylabel("Total Value")
plt.legend()

plt.show()
