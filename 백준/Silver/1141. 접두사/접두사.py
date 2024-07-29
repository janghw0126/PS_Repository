n = int(input())
arr = sorted([input() for _ in range(n)], key=len)
ans = n

for i in range(n):
    for j in range(i+1, n):
        if arr[i] == arr[j][:len(arr[i])]:
            ans -= 1
            break
print(ans)