import sys
input = sys.stdin.readline
from collections import Counter

n = int(input())
lst = [int(input()) for _ in range(n)]
lst.sort()

average = round(sum(lst)/n)
print(average)

mid = n//2
print(lst[mid])

mode = Counter(lst)
max_frequency = max(mode.values())
modes = []
for key, value in mode.items():
    if value == max_frequency:
        modes.append(key)
if len(modes) == 1:
    print(modes[0])
else:
    print(modes[1])

num_range=max(lst)-min(lst)
print(num_range)