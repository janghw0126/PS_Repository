import sys

input=sys.stdin.readline

arr=list(map(int,input().split()))
temp=0

for i in range(len(arr)):
    for j in range(i):
        if arr[i]<arr[j]:
            temp=arr[i]
            arr[i]=arr[j]
            arr[j]=temp

for i in arr:
    print(i,end=" ")   