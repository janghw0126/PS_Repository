import sys
input = sys.stdin.readline

def custom_round(value):
    if value - int(value) >= 0.5:
        return int(value) + 1
    return int(value)

num_scores = int(input())
if num_scores == 0:
    print(0)
else:
    scores = sorted([int(input()) for _ in range(num_scores)])
    
    trim_count = custom_round(num_scores * 0.15)
    trimmed_scores = scores[trim_count:num_scores - trim_count]
    average_score = custom_round(sum(trimmed_scores) / len(trimmed_scores))
    
    print(average_score)
