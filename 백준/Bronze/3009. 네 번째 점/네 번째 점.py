import sys
input=sys.stdin.readline

rectangular=[]
x=[]
y=[]
result=[]

for _ in range(3):
    xy=list(map(int,input().split()))
    x.append(xy[0])
    y.append(xy[1])

for i in range(3):
    if x.count(x[i])%2!=0:
        result.append(x[i])

for i in range(3):
    if y.count(y[i])%2!=0:
        result.append(y[i])

print(result[0], result[1])