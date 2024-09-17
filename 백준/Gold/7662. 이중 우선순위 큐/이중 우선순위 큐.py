import heapq, sys

input = sys.stdin.readline

T = int(input())  # 테스트 케이스 수

for _ in range(T):
    k = int(input())  # 명령어 개수
    max_Q = []
    min_Q = []
    sync = {}  # 동기화 딕셔너리 (삽입된 값과 삭제된 값을 기록)

    for _ in range(k):
        char, n = input().split()
        n = int(n)
        if char == "I":  # 삽입 연산
            heapq.heappush(min_Q, n)  # 최소힙에 값 삽입
            heapq.heappush(max_Q, -n)  # 최대힙에 -값 삽입
            if n in sync:
                sync[n] += 1
            else:
                sync[n] = 1
        elif char == "D":  # 삭제 연산
            if n == 1:  # 최대값 삭제
                while max_Q and sync.get(-max_Q[0], 0) == 0:  # 동기화된 값만 남을 때까지 제거
                    heapq.heappop(max_Q)
                if max_Q:
                    max_val = -heapq.heappop(max_Q)
                    sync[max_val] -= 1
                    if sync[max_val] == 0:
                        del sync[max_val]
            else:  # 최소값 삭제
                while min_Q and sync.get(min_Q[0], 0) == 0:  # 동기화된 값만 남을 때까지 제거
                    heapq.heappop(min_Q)
                if min_Q:
                    min_val = heapq.heappop(min_Q)
                    sync[min_val] -= 1
                    if sync[min_val] == 0:
                        del sync[min_val]

    # 마지막으로 유효하지 않은 값 제거
    while max_Q and sync.get(-max_Q[0], 0) == 0:
        heapq.heappop(max_Q)
    while min_Q and sync.get(min_Q[0], 0) == 0:
        heapq.heappop(min_Q)

    if not max_Q or not min_Q:  # 큐가 비어 있는 경우
        print("EMPTY")
    else:  # 최댓값과 최솟값 출력
        print(-max_Q[0], min_Q[0])