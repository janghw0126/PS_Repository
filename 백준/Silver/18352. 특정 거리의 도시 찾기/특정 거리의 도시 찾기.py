from collections import deque
import sys

# 입력
# n, m, k, s = map(int, input().split())
n, m, k, s = list(map(int, sys.stdin.readline().split()))

graph = {}
for i in range(n+1):
    graph[i] = []
for i in range(m):
    a, b = list(map(int, sys.stdin.readline().split()))
    graph[a].append(b)

# bfs
dist_list = [0 for _ in range(n + 1)]
visited = [0 for _ in range(n+1)]
queue = deque([s])
# queue.append(s)
visited[s] = 1
while (queue):
    now = queue.popleft()
    for j in graph[now]:
        if visited[j] == 0:
            queue.append(j)
            visited[j] = 1
            dist_list[j] = dist_list[now] + 1
check = 0
for i in range(1, n+1):
    if dist_list[i] == k:
        print(i)
        check += 1
if check == 0:
    print(-1)