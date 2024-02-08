import sys
input = sys.stdin.readline
stack = []

for i in range(int(input())):
    a = input().rstrip()
    if "push" in a:
        stack.append(a[5:])
    elif a == "pop":
        print(stack.pop() if stack else -1)
    elif a == "size":
        print(len(stack))
    elif a == "empty":
        print(0 if stack else 1)
    elif a == "top":
        print(stack[-1] if stack else -1)