import sys
input=sys.stdin.readline

# 정점의 갯수, 간선의 갯수, 탐색을 시작할 정점의 번호
N,M,V=map(int,input().split())

# 미리 딕셔너리에 추가하기
graph={i:[] for i in range(1,N+1)}

for _ in range(M):
    a,b=map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)  # 양방향 간선 추가

# 각 노드에 연결된 노드들을 정렬 (작은 번호부터 방문하기 위해)
for key in graph:
    graph[key].sort()
    
# DFS를 수행한 결과
def dfs(graph,V):
    # 방문했던 배열
    visited=list()
    # 방문할 예정인 배열
    stack=list()

    # 시작 노드 stack에 넣기
    stack.append(V)

    while stack:
        # 스택에 있는 최상위 노드 꺼내기
        node = stack.pop()

        # 최상위 노드와 연결되어 있는 인접노드가 방문하지 않았던 노드라면
        # 스택에 다시 넣기
        if node not in visited:
            # visited 배열에 추가
            visited.append(node)
            # 해당 노드에 연결되어 있는 노드들 추가
            stack.extend(reversed(graph[node]))
    
    return visited
        
def bfs(graph,V):
    # 방문한 노드들 추가
    visited=list()
    # 방문할 노드들 추가
    queue=list()

    queue.append(V)

    while queue:
        node=queue.pop(0)

        if node not in visited:
            visited.append(node)
            queue.extend(graph[node])
    
    return visited

result_dfs = dfs(graph,V)
print(' '.join(map(str,result_dfs)))

result_bfs = bfs(graph,V)
print(' '.join(map(str,result_bfs)))