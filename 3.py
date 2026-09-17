base = int(input("Enter base address: "))
i = int(input("Enter row index: "))
j = int(input("Enter column index: "))

columns = 4
size = 4

address = base + ((i * columns + j) * size)

print("Effective Address =", address)
