import sys
input=sys.stdin.readline

#N과 M을 입력한다.
N,M=map(int,input().split())

#점의 좌표를 입력한다.
spot_list=list(map(int,input().split()))
spot_list.sort()

# 주어진 점들 중에서 start 이상인 첫 번째 점의 위치를 반환하는 함수
def lower_bound(start):
    left, right = 0, N
    while left < right:
        mid = (left + right) // 2
        if spot_list[mid] >= start:
            right = mid
        else:
            left = mid + 1
    return right

# 주어진 점들 중에서 end를 초과하는 첫 번째 점의 위치를 반환하는 함수
def upper_bound(end):
    left, right = 0, N
    while left < right:
        mid = (left + right) // 2
        if spot_list[mid] <= end:
            left = mid + 1
        else:
            right = mid
    return right

#선분의 시작점과 끝점을 입력받으면서 입력으로 주어진 점이 몇 개 있는지 출력한다.
for _ in range(M):
    #선분의 시작점과 끝점을 입력받는다.
    a,b=map(int,input().split())
    # 주어진 점들 중에서 선분에 포함되는 점들의 개수를 계산한다.
    count = upper_bound(b) - lower_bound(a)
    print(count)
