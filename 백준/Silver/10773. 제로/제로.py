import sys
input=sys.stdin.readline

K=int(input())

list=[]

for _ in range(K):
    num=int(input())

    if num==0:
        list.pop()
    else:
        list.append(num)

sum=0

for li in list:
    sum+=li

print(sum)