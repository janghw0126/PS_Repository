from itertools import permutations

def solution(k, dungeons):
    answer = 0
    
    # 모든 던전 방문 순서를 생성
    for order in permutations(range(len(dungeons))):
        remaining_energy = k
        visited_count = 0
        
        # 현재 순서에 따른 던전 방문 시도
        for dungeon_index in order:
            min_energy, cost = dungeons[dungeon_index]
            if remaining_energy >= min_energy:
                visited_count += 1
                remaining_energy -= cost
        
        # 방문한 던전의 수를 기록
        answer = max(answer, visited_count)
    
    return answer