import sys
import math

input = sys.stdin.read
data = input().split()

# 참가자의 수
n = int(data[0])

# 티셔츠 사이즈별 신청자의 수
tshirt = list(map(int, data[1:7]))

# 티셔츠와 팬의 묶음 수
tbunch = int(data[7])
pbunch = int(data[8])

# 주문할 티셔츠 묶음 수 계산
tsum = 0
for i in range(6):
    tsum += (tshirt[i] // tbunch) + (1 if tshirt[i] % tbunch != 0 else 0)

# 주문할 티셔츠 묶음 수와 펜의 묶음 수, 낱개 수 출력
print(tsum)
print(n // pbunch, n % pbunch)