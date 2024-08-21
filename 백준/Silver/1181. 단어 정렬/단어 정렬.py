import sys
input=sys.stdin.readline

# 2차원 배열([단어, 단어길이]로 만들어서 길이가 작은 순부터 정렬
# 길이가 같은 경우에 단어 비교해서 출력하기
N=int(input())

words=[]

for _ in range(N):
    word=input().strip()
    words.append(word)

# 단어 정렬
words=list(set(words))
words.sort()
words.sort(key=len)
           
for word in words:
    print(word)