import sys, heapq

input = sys.stdin.readline
N = int(input())  # 행렬의 크기
min_heap = []

for _ in range(N):
    row = list(map(int, input().split()))
    
    if not min_heap:  # 첫 번째 입력 시 힙 초기화
        for num in row:
            heapq.heappush(min_heap, num)
    else:
        for num in row:
            if min_heap[0] < num:  # 힙의 최솟값보다 현재 숫자가 크다면
                heapq.heappush(min_heap, num)
                heapq.heappop(min_heap)  # 힙의 크기를 N으로 유지

# N번째 큰 수 출력
print(min_heap[0])