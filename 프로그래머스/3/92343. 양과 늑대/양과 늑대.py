# 전역 변수로 최대 양의 수를 저장
max_sheep = 0

def solution(info, edges):
    # 각 노드의 자식 노드를 저장할 리스트 초기화
    children = [[] for _ in range(len(info))]

    # edges에 따라 부모-자식 관계를 설정
    for parent, child in edges:
        children[parent].append(child)

    # 깊이 우선 탐색(DFS)을 수행하는 재귀 함수 정의
    def dfs(current_node, sheep_count, wolf_count, available_nodes):
        global max_sheep

        # 해당 경로에서 늑대가 양을 잡아먹기 때문에 더 이상 탐색할 필요가 없음
        # 늑대 수가 양 수보다 많아지면 탐색 중지
        if wolf_count >= sheep_count:
            return

        # 최대 양의 수를 갱신
        if sheep_count > max_sheep:
            max_sheep = sheep_count

        # 현재 노드의 자식 노드들을 탐색 가능 노드 리스트에 추가
        available_nodes.extend(children[current_node])

        # 다음으로 이동할 수 있는 노드들을 순회
        for next_node in available_nodes:
            # 다음 노드가 현재 위치가 아닌 경우에만 이동
            # available_nodes 리스트를 새로 생성하여 다른 경로를 시도할 수 있게 함
            new_available_nodes = [node for node in available_nodes if node != next_node]
            if info[next_node]:  # 다음 노드에 늑대가 있는 경우
                dfs(next_node, sheep_count, wolf_count + 1, new_available_nodes)
            else:  # 다음 노드에 양이 있는 경우
                dfs(next_node, sheep_count + 1, wolf_count, new_available_nodes)

    # 루트 노드(0번)에서 DFS 시작 (처음에 양 1마리가 있음)
    dfs(0, 1, 0, children[0])

    return max_sheep