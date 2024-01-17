#1. 테스트 케이스의 개수를 입력받는다.
T=int(input())

#2. 테스트 케이스만큼 반복하면서 문자열의 첫 글자와 마지막 글자를 출력한다.

for i in range(T):
    string=str(input())
    print(string[0]+string[-1])