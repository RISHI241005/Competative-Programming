
n = int(input("Enter number of elements: "))
arr = list(map(int, input("Enter numbers in descending order: ").split()))

target = int(input("Enter target number: "))

low = 0
high = n - 1
result = -1

while low <= high:
    mid = (low + high) // 2

    if arr[mid] == target:
        result = mid
        break

    elif arr[mid] < target:
        high = mid - 1

    else:
        low = mid + 1

print("Index:", result)

