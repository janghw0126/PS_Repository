from collections import deque

# 입력 받기
m, n = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]

# 방문 여부를 기록하는 배열 초기화
visited = [[False] * m for _ in range(n)]

# 이동할 수 있는 방향 정의 (오른쪽, 아래)
directions = [(0, 1), (1, 0)]
# (x, y) 위치가 유효한 범위 내에 있는지 확인하는 함수
def is_valid(x, y):
    return 0 <= x < n and 0 <= y < m

# BFS를 이용하여 (start_x, start_y)에서 목적지까지 이동할 수 있는지 확인하는 함수
def bfs(start_x, start_y):
    queue = deque([(start_x, start_y)])
    visited[start_x][start_y] = True

    while queue:
        x, y = queue.popleft()

        # 목적지에 도달한 경우
        if x == n - 1 and y == m - 1:
            return True

        for dx, dy in directions:
            nx, ny = x + dx, y + dy

            if not is_valid(nx, ny) or visited[nx][ny] or board[nx][ny] == 0:
                continue

            visited[nx][ny] = True
            queue.append((nx, ny))

    return False

# BFS 실행 및 결과 출력
if bfs(0, 0):
    print("Yes")
else:
    print("No")