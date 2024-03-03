import sys
from collections import deque

input = sys.stdin.readline

r, c, n= map(int,input().split())

dx = [0,0,1,-1]
dy = [1,-1,0,0]
q = deque()
graph = []

def bfs():
  while q:
    x , y = q.popleft()
    graph[x][y] = '.'
    
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]

      if nx < 0 or nx >= r or ny < 0 or ny >= c:
        continue

      if graph[nx][ny] == 'O':
        graph[nx][ny] = '.'
    
for _ in range(r):
  graph.append(list(input().rstrip()))

for i in range(1,n+1):
  if i == 1:
    for x in range(r):
      for y in range(c):
        if graph[x][y] == "O":
          q.append((x,y))

  elif i % 2 == 1:
    bfs()
    for x in range(r):
      for y in range(c):
        if graph[x][y] == "O":
          q.append((x,y))
  else:
    graph = [['O'] * c for _ in range(r)]

for i in graph:
  print(''.join(i))