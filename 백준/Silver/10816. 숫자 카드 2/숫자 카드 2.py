import sys
input = sys.stdin.readline

# 입력
int(input())
nlist = list(map(int, input().split()))
int(input())
mlist = list(map(int, input().split()))

dic = dict()

for n in nlist:
    if n in dic:
        dic[n] += 1
    else:
        dic[n] = 1

print(' '.join(str(dic[m]) if m in dic else '0' for m in mlist))