import sys
input = sys.stdin.readline
T=int(input())
for i in range(T):
    stack = []
		#sys 모듈을 쓸 경우 개행문자도 문자열에 포함되기 때문에 rstrip()을 통해 제거해줌.
    for i in input().rstrip():
        if i == "(":
            stack.append(i)
        else:
						#오류가 발생할 가능성이 있는 코드
            try:
                stack.pop()
						#에러가 발생했을 경우 시행할 코드
            except:
                print("NO")
                break
                # 괄호를 열기도 전에 닫음
    else:
				# 스택이 안 비어있는 경우 NO 출력
        print("NO" if stack else "YES")