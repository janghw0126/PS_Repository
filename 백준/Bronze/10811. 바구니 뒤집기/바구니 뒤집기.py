#1.N,M을 입력받는다.
import sys
input=sys.stdin.readline

N,M=map(int,input().split())

#2. 바구니 리스트를 만든다.
basket = list(range(1, N+1))

#3. 반복문을 통해 바구니의 순서를 역순으로 만든다.
for _ in range(M):
    #4. i,j를 입력받는다.
    i,j=map(int,input().split())

    for _ in range((j-i+1)//2):
        temp=basket[i-1]
        basket[i-1]=basket[j-1]
        basket[j-1]=temp
        i+=1
        j-=1


for result in range(0,N):
    print(basket[result],end=" ")
