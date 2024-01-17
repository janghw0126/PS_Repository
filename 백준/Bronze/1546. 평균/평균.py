import sys
input=sys.stdin.readline

#시험 본 과목의 개수 N을 입력받는다.
N=int(input())

#시험 친 과목의 점수들을 입력받는다.
score=list(map(int,input().split()))

#평균을 구하기 위한 합을 초기화한다.
sum=0
max_score = max(score)

#모든 점수를 점수/M*100으로 고치고 평균을 구하기 위한 합을 구한다.
for i in range(N):
    score[i]=score[i]/max_score*100
    sum+=score[i]

#평균을 구한다.
print(sum/N)