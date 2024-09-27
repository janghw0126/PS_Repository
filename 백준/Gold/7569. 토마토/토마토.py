import sys
from collections import deque
input = sys.stdin.readline

# 입력 처리 (가로 M, 세로 N, 높이 H)
M, N, H = map(int, input().split())
grid = [[list(map(int, input().split())) for _ in range(N)] for _ in range(H)]

# 방문 여부를 확인하는 3차원 리스트
visited = [[[False] * M for _ in range(N)] for _ in range(H)]

# 상, 하, 좌, 우, 앞, 뒤 방향 벡터
dz = [1, -1, 0, 0, 0, 0]
dy = [0, 0, 1, -1, 0, 0]
dx = [0, 0, 0, 0, 1, -1]

# 익은 토마토의 좌표를 큐에 추가
queue = deque([(z, y, x) for z in range(H) for y in range(N) for x in range(M) if grid[z][y][x] == 1])

# BFS 탐색
def bfs():
    while queue:
        z, y, x = queue.popleft()
        for i in range(6):
            nz, ny, nx = z + dz[i], y + dy[i], x + dx[i]
            # 유효 범위 내에서 아직 익지 않은 토마토를 찾음
            if 0 <= nx < M and 0 <= ny < N and 0 <= nz < H and grid[nz][ny][nx] == 0 and not visited[nz][ny][nx]:
                visited[nz][ny][nx] = True
                grid[nz][ny][nx] = grid[z][y][x] + 1  # 날짜를 +1 해서 익음
                queue.append((nz, ny, nx))

# BFS 실행
bfs()

# 결과 계산
days = 0
for floor in grid:
    for row in floor:
        if 0 in row:  # 익지 않은 토마토가 있으면
            print(-1)
            exit(0)
        days = max(days, max(row))  # 가장 늦게 익은 날짜

# 시작일이 1부터 시작하므로 -1을 해줌
print(days - 1)