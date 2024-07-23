import sys
from collections import deque

def count_windows(test_cases):
    results = []
    for case in test_cases:
        N, M, K, arr = case
        right = 0
        current_sum, count = 0, 0
        window = deque()
        
        # 슬라이딩 윈도우를 이용하여 부분 배열의 합 계산
        for left in range(N):
            while right < N + M - 1 and len(window) < M:
                window.append(arr[right % N])  # 원형 배열 처리
                current_sum += arr[right % N]
                right += 1
            
            # 현재 윈도우의 합이 K보다 작으면 count 증가
            if current_sum < K:
                count += 1
            
            # 윈도우의 왼쪽 끝 요소 제거 및 합 갱신
            current_sum -= window.popleft()
            left += 1
            
            # N과 M이 같은 경우 한 번만 계산 후 종료
            if N == M:
                break
        
        results.append(count)
    
    return results

if __name__ == '__main__':
    input = sys.stdin.read
    data = input().split()
    
    test_cases = []
    index = 0
    num_cases = int(data[index])
    index += 1
    
    # 각 테스트 케이스를 파싱하여 리스트에 추가
    for _ in range(num_cases):
        N = int(data[index])
        M = int(data[index + 1])
        K = int(data[index + 2])
        index += 3
        arr = list(map(int, data[index:index + N]))
        index += N
        test_cases.append((N, M, K, arr))
    
    # 슬라이딩 윈도우 계산 함수 호출
    results = count_windows(test_cases)
    
    # 각 테스트 케이스의 결과 출력
    for result in results:
        print(result)
