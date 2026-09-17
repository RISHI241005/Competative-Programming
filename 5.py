base = int(input("Enter base address: "))
row = int(input("Enter row index: "))
col = int(input("Enter column index: "))

columns = 4
size = 4

address = base + ((row * columns + col) * size)

print("Effective Address =", address)
print("Binary Address =", bin(address)[2:])
