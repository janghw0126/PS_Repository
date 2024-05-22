import sys

input=sys.stdin.readline

N,M=map(int,input().split())

A=list(map(int,input().split()))
B=list(map(int,input().split()))

AB_list=A+B


AB_list=sorted(AB_list)

for char in AB_list:
    print(char,end=" ")