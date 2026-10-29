
n = int(input("Enter number of elements: "))
arr = list(map(int, input("Enter numbers: ").split()))

result = []
seen = set()

for num in arr:
    if num not in seen:
        result.append(num)
        seen.add(num)

print("List without duplicates:", result)
