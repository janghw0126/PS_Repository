import sys
input=sys.stdin.readline

N=int(input())

number=input()

sum=0

for i in range(N):
    sum+=int(number[i])

print(sum)