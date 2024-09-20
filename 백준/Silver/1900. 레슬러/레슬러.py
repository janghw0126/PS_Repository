import sys

# 선수 수 입력
N = int(sys.stdin.readline())
wrestlers = []  # 각 선수의 힘과 반지 크기 저장
wins = dict()  # 각 선수의 승리 횟수 저장

# 각 선수의 정보 입력
for i in range(N):
    strength, ring_size = map(int, sys.stdin.readline().split())
    wrestlers.append([strength, ring_size])
    wins[i] = 0  # 초기 승리 횟수는 0으로 설정

# 선수들끼리 대결
for i in range(N - 1):
    for j in range(i + 1, N):  # i번째와 j번째 선수가 대결
        score_i = wrestlers[i][0] + wrestlers[j][0] * wrestlers[i][1]  # i번째 선수 점수
        score_j = wrestlers[j][0] + wrestlers[i][0] * wrestlers[j][1]  # j번째 선수 점수

        if score_i > score_j:  # i가 승리할 경우
            wins[i] += 1
        elif score_i < score_j:  # j가 승리할 경우
            wins[j] += 1

# 승리 횟수에 따라 정렬
sorted_wins = sorted(wins.items(), key=lambda x: x[1], reverse=True)

# 결과 출력
for wrestler in sorted_wins:
    print(wrestler[0] + 1)  # 선수 번호는 1부터 시작하므로 +1