import sys
input=sys.stdin.readline

N=int(input())
list=[]

for _ in range(N):
    age,name=map(str,input().split())
    list.append([int(age),name])

list.sort(key=lambda x:x[0])

for li in list:
    print(li[0],li[1])