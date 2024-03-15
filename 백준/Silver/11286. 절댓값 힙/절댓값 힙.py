import sys
import heapq
input = sys.stdin.readline

n = int(input().rstrip())

q = []
for i in range(n):
    num = int(input().rstrip())
    
    if num == 0:
        if q: print(heapq.heappop(q)[1])
        else: print(0)
    else: # 절댓값과 실제값을 튜플로 추가
        heapq.heappush(q,(abs(num),num))