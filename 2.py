n = int(input("Enter number of students: "))

a = list(map(int, input("Enter attendance percentages: ").split()))

threshold = int(input("Enter attendance threshold: "))

count = 0

for i in range(n):
    if a[i] < threshold:
        count += 1

min_attendance = a[0]
pos = 0

for i in range(1, n):
    if a[i] < min_attendance:
        min_attendance = a[i]
        pos = i

avg = sum(a) / n

print("Students below threshold =", count)
print("Lowest attendance =", min_attendance, "%")
print("Position =", pos + 1)
print("Average attendance = {:.2f}%".format(avg))
