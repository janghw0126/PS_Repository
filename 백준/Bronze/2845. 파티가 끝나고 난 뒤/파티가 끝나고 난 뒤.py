import sys
input=sys.stdin.readline


L,area = map(int,input().split())
real_num=L*area

num=list(map(int,input().split()))

for i in range(len(num)):
    result=num[i]-real_num
    print(result,end=" ")