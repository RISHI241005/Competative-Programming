# wap in python to insertion and deletion of an element

a = [10, 20, 30, 40, 50]
n = 5

print("Enter position for insertion: ")
pos = int(input())
print("Enter value: ")
value = int(input())

# insertion
i = n
while i >= pos:
    a[i] = a[i - 1]
    i -= 1
a[pos - 1] = value
n += 1

print("After insertion: ", end="")
for i in range(n):
    print(a[i], end=" ")
print()

print("Enter position for deletion: ")
pos = int(input())

# deletion
for i in range(pos - 1, n - 1):
    a[i] = a[i + 1]
n -= 1

print("After deletion: ", end="")
for i in range(n):
    print(a[i], end=" ")
print()