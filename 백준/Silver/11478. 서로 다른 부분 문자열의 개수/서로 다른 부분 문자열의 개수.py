s = input().rstrip()
arr = set()
for i in range(len(s)+1):
    for j in range(i,len(s)+1):
        arr.add(s[i:j])
print(len(arr)-1) # 빈 문자열이 포함되어 -1을 해주었다.