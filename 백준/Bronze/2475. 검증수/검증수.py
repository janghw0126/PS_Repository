import sys
input=sys.stdin.readline

number=list(map(int,input().split()))
sum=0

for i in range(len(number)):
    sum+=number[i]*number[i]

test_number=sum%10

print(test_number)