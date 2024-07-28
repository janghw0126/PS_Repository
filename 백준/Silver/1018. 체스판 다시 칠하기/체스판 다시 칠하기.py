import sys
input=sys.stdin.readline

M,N=map(int,input().split())
chess=[]

for _ in range(M):
    chess.append(input().strip())

def chess_paint(m,n,color):
    count=0
    for i in range(8):
        for j in range(8):
            if (i+j)%2==0:
                if chess[m+i][n+j]!=color:
                    count+=1
            else:
                if chess[m+i][n+j]==color:
                    count+=1
    return count

# 최솟값 초기화
min_paint=float('inf')

# B가 먼저 시작할 때 최솟값인지 W가 먼저 시작할 때 최솟값인지 알 수 없기 때문에 둘 다 구해서 최솟값 계산하기
for m in range(M-7):
    for n in range(N-7):
        B_paint=chess_paint(m,n,"B")
        W_paint=chess_paint(m,n,"W")
        min_paint=min(min_paint,B_paint,W_paint)

print(min_paint)
