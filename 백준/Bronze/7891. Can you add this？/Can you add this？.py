N=int(input())
sum=0

for _ in range(N):
    M,N=map(int,input().split())
    sum=N+M
    print(sum)