import sys
input = sys.stdin.readline
###########################################
# 입력데이터 정보 받아오기
n, k, q, m = map(int, input().split())

# 자는 학생 저장하기
# n+2까지 숫자가 index로 들어가야 하므로 길이는 n+3
sleep = [False for _ in range(n+3)]
for i in map(int, input().split()):
    sleep[i] = True

check = [1 for _ in range(n+3)]

for i in map(int, input().split()):
    if sleep[i]:
        continue

    for j in range(i, n+3, i):
        if sleep[j]:
            continue

        check[j] = 0

sum_ = 0
check[2] = 0
for i in range(3, n+3):
    if check[i]:
        sum_ += 1

    check[i] = sum_

for _ in range(m):
    s, e = map(int, input().split())
    print(check[e] - check[s-1])