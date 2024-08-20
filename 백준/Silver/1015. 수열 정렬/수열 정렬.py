n = int(input())
numbers = list(map(int, input().split()))
sort_numbers = sorted(numbers)
result = []

for index in range(n):
  idx = sort_numbers.index(numbers[index])
  result.append(idx)
  sort_numbers[idx] = None

print(*result)