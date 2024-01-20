import sys
input=sys.stdin.readline

n,m = map(int, input().split())

a = []
b = []

#반복문을 통해서 입력받음.
for i in range(n):
  a.append(list(map(int, input().split())))

for i in range(n):
  b.append(list(map(int,input().split())))

for i in range(n):
  for j in range(m):
    a[i][j] += b[i][j]

#언팩: 각 행의 원소들을 풀어서 나열하고 출력해줌
for i in range(n):
  print(*a[i])