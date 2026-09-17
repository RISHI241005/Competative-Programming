# Binary Search

a = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
n = 10
key = int(input("Enter element to search: "))

low = 0
high = n - 1
found = False

while low <= high:
    mid = (low + high) // 2
    if a[mid] == key:
        print("Element found at position", mid + 1)
        found = True
        break
    elif a[mid] < key:
        low = mid + 1
    else:
        high = mid - 1

if not found:
    print("Element not found")