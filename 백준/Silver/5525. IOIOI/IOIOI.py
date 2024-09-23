import sys
input=sys.stdin.readline

# 각각의 입력값 받기
N=int(input())
M=int(input())
S=input().strip()

# S안에 Pn이 몇 군데 포함되어 있는지 구하는 변수 선언
count=0

# S의 길이만큼 반복하면서 몇 군데 포함되어 있는지 갯수 세기
for i in range(len(S)):
    P="IO"*N+"I"
    if S[i:i+len(P)]==P:
        count+=1

print(count)