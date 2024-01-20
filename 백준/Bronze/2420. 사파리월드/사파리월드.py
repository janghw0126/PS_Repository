import sys
input=sys.stdin.readline

N,M=map(int,input().split())

difference=N-M

if N-M>0:
    print(N-M)
else:
    print(abs(N-M))
