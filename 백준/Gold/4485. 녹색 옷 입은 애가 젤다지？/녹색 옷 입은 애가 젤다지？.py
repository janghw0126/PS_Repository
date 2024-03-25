from collections import deque
count,dx,dy=0,[0,0,1,-1],[1,-1,0,0]

def bfs():
    queue=deque()
    queue.append([0,0])
    cost[0][0]=field[0][0]
    while queue:

        x,y=queue.popleft()

        for i in range(4):
            nx,ny=x+dx[i],y+dy[i]
            if -1<nx<n and -1<ny<n:
                if cost[y][x]+field[ny][nx]<cost[ny][nx]:
                    cost[ny][nx]=cost[y][x]+field[ny][nx]
                    queue.append([nx,ny])
    return cost[n-1][n-1]


while True:
    n=int(input())
    if n==0:break
    count+=1
    field=[]
    for i in range(n):field.append(list(map(int,input().split())))
    cost=[[1e9 for j in range(n)]for i in range(n)]
    print(f"Problem {count}: {bfs()}")