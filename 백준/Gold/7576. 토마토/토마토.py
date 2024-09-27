from collections import deque
import sys
input = sys.stdin.readline

# 입력 처리 (세로 n, 가로 m)
m, n = map(int, input().split())
tomato_grid = [list(map(int, input().split())) for _ in range(n)]

# 익은 토마토 좌표를 큐에 추가
queue = deque([(i, j) for i in range(n) for j in range(m) if tomato_grid[i][j] == 1])

# 방향 벡터 (상, 하, 좌, 우)
directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

# BFS 탐색 함수
def bfs():
    while queue:
        x, y = queue.popleft()
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            # 범위 내에 있고, 익지 않은 토마토(0)일 경우 익히기
            if 0 <= nx < n and 0 <= ny < m and tomato_grid[nx][ny] == 0:
                tomato_grid[nx][ny] = tomato_grid[x][y] + 1
                queue.append((nx, ny))

# BFS 실행
bfs()

# 결과 계산
days = 0
for row in tomato_grid:
    if 0 in row:  # 익지 않은 토마토가 있으면 -1 출력
        print(-1)
        exit()
    days = max(days, max(row))  # 가장 큰 값이 걸린 날짜

# 시작을 1에서 했으므로 결과에서 1을 빼줌
print(days - 1)