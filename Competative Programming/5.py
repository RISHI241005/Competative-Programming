
s = input("Enter brackets: ")

stack = []

for ch in s:
    if ch == '(' or ch == '[' or ch == '{':
        stack.append(ch)

    else:
        if len(stack) == 0:
            print(False)
            break

        top = stack.pop()

        if ch == ')' and top != '(':
            print(False)
            break

        elif ch == ']' and top != '[':
            print(False)
            break

        elif ch == '}' and top != '{':
            print(False)
            break

else:
    if len(stack) == 0:
        print(True)
    else:
        print(False)

