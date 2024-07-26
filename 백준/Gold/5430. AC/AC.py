from collections import deque
import sys

input=sys.stdin.readline

T=int(input())

for _ in range(T):
    p=input()
    n=int(input())
    arr=input()

    if n>0:
        arr=deque(arr.strip()[1:-1].split(","))
    else:
        arr=deque()

    flag=True
    error=False

    for char in p:
        if char=="R":
            flag=not flag
        elif char=="D":
            if not arr:
                print("error")
                error=True
                break
            if flag==False:
                arr.pop()
            elif flag==True:
                arr.popleft()
    if not error:
        if flag==False:
            arr.reverse()
            print("["+",".join(arr)+"]")
        if flag==True:
            print("["+",".join(arr)+"]")