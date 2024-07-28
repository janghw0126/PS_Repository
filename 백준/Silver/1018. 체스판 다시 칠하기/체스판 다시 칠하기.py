import sys
input = sys.stdin.readline

M, N = map(int, input().split())
chess = [input().strip() for _ in range(M)]

def count_repaints(x, y, start_color):
    count = 0
    for i in range(8):
        for j in range(8):
            if (i + j) % 2 == 0:
                if chess[x + i][y + j] != start_color:
                    count += 1
            else:
                if chess[x + i][y + j] == start_color:
                    count += 1
    return count

min_repaints = float('inf')
for i in range(M - 7):
    for j in range(N - 7):
        repaints_w = count_repaints(i, j, 'W')
        repaints_b = count_repaints(i, j, 'B')
        min_repaints = min(min_repaints, repaints_w, repaints_b)

print(min_repaints)