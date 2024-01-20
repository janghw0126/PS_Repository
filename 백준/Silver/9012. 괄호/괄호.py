import sys
input=sys.stdin.readline

T=int(input())

for _ in range(T):
    stack=[]
    for char in input().rstrip():
        if char=="(":
            stack.append(char)
        else:
            try:
                stack.pop()
            except:
                print("NO")
                break
    else:
        print("YES" if not stack else "NO")
