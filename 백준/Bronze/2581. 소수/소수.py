#소수
#1. 첫째줄에 M, 둘째 줄에 N을 입력받는다.
#2. 소수인 수들을 정렬하는 배열을 선언한다.
#3. 반복문을 통해 소수인 경우 append해주고 아닌 경우 그냥 넘어간다.
#4. 소수인 수들만 모아놓은 배열의 요소들의 합을 구하고 min값을 구한다.
M=int(input())
N=int(input())

prime_number=[]
sum=0

for i in range(M,N+1):
    for j in range(2,i+1):
        if i==j:
            prime_number.append(i)
        elif i%j==0:
            break

for m in range(0,len(prime_number)):
    sum+=prime_number[m]

if not prime_number:
    print(-1)
else:
    print(sum)
    print(prime_number[0])