import sys
from collections import deque

# 입력 받기
num_students, num_comparisons = map(int, sys.stdin.readline().split())

# 그래프와 진입 차수 리스트 초기화
adj_list = [[] for _ in range(num_students + 1)]
in_degree = [0 for _ in range(num_students + 1)]
queue = deque()
order = []

# 비교 관계 입력 및 그래프 구성
for _ in range(num_comparisons):
    first, second = map(int, sys.stdin.readline().rstrip().split())
    adj_list[first].append(second)  # 첫 번째 학생이 두 번째 학생 앞에 서야 함
    in_degree[second] += 1  # 두 번째 학생의 진입 차수를 증가

# 진입 차수가 0인 학생들 큐에 삽입
for student in range(1, num_students + 1):
    if in_degree[student] == 0:
        queue.append(student)

# 위상 정렬 시작
while queue:
    current_student = queue.popleft()  # 진입 차수가 0인 학생을 큐에서 꺼냄
    order.append(current_student)  # 해당 학생을 줄 세우기에 추가
    
    # 현재 학생 뒤에 서야 하는 학생들의 진입 차수를 감소
    for next_student in adj_list[current_student]:
        in_degree[next_student] -= 1
        if in_degree[next_student] == 0:  # 진입 차수가 0이 되면 큐에 추가
            queue.append(next_student)

# 줄 세우기 결과 출력
print(*order)