# 입력
n = int(input())

# 후보와 득표수 리스트
dasom = int(input())  # 다솜이 득표수
lst = []  # 나머지 득표수
for _ in range(n - 1):
    lst.append(int(input()))

# 다솜이 매수한 표 수
cnt = 0

# 만약 n= 1이면 바로 종료
if n == 1:
    print(0)
    exit()

# 나머지 사람들 중 최고에게서, 다솜이의 득표수 에 1더하면 될듯.
while dasom <= max(lst):
    lst[lst.index(max(lst))] -= 1
    dasom += 1
    cnt += 1

print(cnt)