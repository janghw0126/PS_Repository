import sys

count = int(sys.stdin.readline().strip())

for _ in range(count):
    sequence = sys.stdin.readline().strip()

    # 최대 깊이
    max_depth = 0  
    # 현재 괄호 스택
    stack = []  

    # 입력된 괄호 문자열 처리
    for bracket in sequence:
        # 닫는 괄호인 경우
        if bracket == ']':
            # 스택 길이를 기반으로 깊이 갱신
            max_depth = max(len(stack), max_depth) 
            # 스택에서 여는 괄호 제거
            stack.pop()
        else:
            # 여는 괄호를 스택에 추가
            stack.append('[')

    # 가장 깊은 곳에서의 2의 제곱 출력
    print(2 ** max_depth)