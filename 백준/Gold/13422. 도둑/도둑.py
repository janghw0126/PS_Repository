import sys
from collections import deque

def count_windows(test_cases):
    results = []
    for case in test_cases:
        N, M, K, arr = case
        right = 0
        current_sum, count = 0, 0
        window = deque()
        
        for left in range(N):
            while right < N + M - 1 and len(window) < M:
                window.append(arr[right % N])
                current_sum += arr[right % N]
                right += 1
            
            if current_sum < K:
                count += 1
            
            current_sum -= window.popleft()
            left += 1
            
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
    
    for _ in range(num_cases):
        N = int(data[index])
        M = int(data[index + 1])
        K = int(data[index + 2])
        index += 3
        arr = list(map(int, data[index:index + N]))
        index += N
        test_cases.append((N, M, K, arr))
    
    results = count_windows(test_cases)
    
    for result in results:
        print(result)