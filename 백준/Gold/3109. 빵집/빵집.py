r, c = map(int, input().split())
arr = [list(input()) for _ in range(r)]
directx = [-1, 0, 1]
directy = [1, 1, 1]

cnt = 0

def dfs(x, y):
    global cnt
    if y == c - 1:
        cnt += 1
        return True

    for k in range(3):
        dx, dy = x + directx[k], y + directy[k]
        if 0 <= dx < r and 0 <= dy < c and arr[dx][dy] == '.':
            arr[dx][dy] = 'x' 
            if dfs(dx, dy):
                return True
    return False

for i in range(r):
    dfs(i, 0)

print(cnt)