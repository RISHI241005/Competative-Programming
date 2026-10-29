
n = int(input("Enter number of elements: "))
prices = list(map(int, input("Enter prices: ").split()))

target = int(input("Enter target amount: "))

seen = {}

for i in range(n):
    needed = target - prices[i]

    if needed in seen:
        print("Indices:", seen[needed], i)
        break

    seen[prices[i]] = i

