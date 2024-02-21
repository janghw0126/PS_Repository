N=int(input())

for i in range(N):
    sum=0
    for j in str(i):
        sum+=int(j)
    sum+=i
    if sum==N:
        print(i)
        break
else:
    print(0)