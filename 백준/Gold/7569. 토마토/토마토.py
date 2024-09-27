import sys
from collections import deque
input = sys.stdin.readline

# 테스트케이스를 입력받음
M, N, H = map(int, input().split())
grid = [[list(map(int, input().split())) for _ in range(N)] for _ in range(H)]

# 방문 여부를 확인하는 3차원 리스트를 선언함
visited = [[[False] * M for _ in range(N)] for _ in range(H)]

# 상, 하, 좌, 우, 앞, 뒤 방향 벡터를 초기화함
dz = [1, -1, 0, 0, 0, 0]
dy = [0, 0, 1, -1, 0, 0]
dx = [0, 0, 0, 0, 1, -1]

# 익은 토마토의 좌표를 큐에 추가함
queue = deque([(z, y, x) for z in range(H) for y in range(N) for x in range(M) if grid[z][y][x] == 1])

# BFS를 탐색함
def bfs():
    while queue:
        z, y, x = queue.popleft()
        for i in range(6):
            nz, ny, nx = z + dz[i], y + dy[i], x + dx[i]
            # 유효 범위 내에서 아직 익지 않은 토마토를 찾음
            if 0 <= nx < M and 0 <= ny < N and 0 <= nz < H and grid[nz][ny][nx] == 0 and not visited[nz][ny][nx]:
                visited[nz][ny][nx] = True
                # 날짜를 +1 해서 익음
                grid[nz][ny][nx] = grid[z][y][x] + 1 
                queue.append((nz, ny, nx))

# BFS를 실행함
bfs()

# 결과를 계산함
days = 0
for floor in grid:
    for row in floor:
        # 익지 않은 토마토가 있으면
        if 0 in row:
            print(-1)
            exit(0)
        # 가장 늦게 익은 날짜를 갱신함
        days = max(days, max(row))

# 시작일이 1부터 시작하므로 -1을 해줌
print(days - 1)
