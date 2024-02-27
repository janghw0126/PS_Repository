import sys
from collections import deque

def initialize_res():
    return deque()

def process_queries(n, list_a, list_b, m, list_c):
    res = initialize_res()

    for i in range(n):
        if list_a[i] == 0:
            res.appendleft(list_b[i])

    for i in range(m):
        res.append(list_c[i])
        print(res.popleft(), end=' ')

def main():
    n = int(sys.stdin.readline())
    list_a = list(map(int, sys.stdin.readline().split()))  # 0 1 1 0 (0 = queue, 1 = stack)
    list_b = list(map(int, sys.stdin.readline().split()))

    m = int(sys.stdin.readline())
    list_c = list(map(int, sys.stdin.readline().split()))

    process_queries(n, list_a, list_b, m, list_c)

if __name__ == '__main__':
    main()