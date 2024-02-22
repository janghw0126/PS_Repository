import sys
input=sys.stdin.readline
N=int(input())

# 2차원 배열 입력
array=[]

for _ in range(N):
    xy=list(map(int,input().split()))
    array.append([xy[1],xy[0]])

array.sort()

for i in array:
    print(i[1],i[0])
