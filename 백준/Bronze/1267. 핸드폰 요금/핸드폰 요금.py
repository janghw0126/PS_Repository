import sys
input=sys.stdin.readline

N=int(input())
call_time=list(map(int,input().split()))

youngsik_money=0
minsik_money=0

for i in range(N):
    youngsik_money+=(call_time[i]//30+1)*10
    minsik_money+=(call_time[i]//60+1)*15

if youngsik_money>minsik_money:
    print("M",minsik_money)
elif youngsik_money<minsik_money:
    print("Y",youngsik_money)
else:
    print("Y","M",youngsik_money)