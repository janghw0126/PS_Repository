n = int(input())
nums = list(map(int, input().split()))

new = [0 for _ in range(n)]

for i in range(1, n + 1):
    num = nums[i - 1]
    cnt = 0
    for j in range(n):
        if cnt == num and new[j] == 0:
            new[j] = i
            break
        elif new[j] == 0:
            cnt += 1
            
print(*new)
