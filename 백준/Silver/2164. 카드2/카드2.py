import sys
from collections import deque
input=sys.stdin.readline


N=int(input())

arr=deque(i+1 for i in range(N))

while(len(arr)>1):
    arr.popleft()
    bottom=arr.popleft()
    arr.append(bottom)

print(arr[0])