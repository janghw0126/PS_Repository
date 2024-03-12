#단어 공부
#1. 첫째 줄에 단어를 입력받고 대문자로 변경한다.
#2. 중복된 문자들을 제거한다.
#3. 반복문을 통해서 각각의 문자들이 몇번 나왔는지 센다
#4. max가 여러개 있을 경우 ? 출력
#5. 아닌 경우 답 출력

word=input().upper()

word_list=list(set(word))
word_count=[]


for char in word_list:
    count=word.count(char)
    word_count.append(count)

if word_count.count(max(word_count))>=2:
    print("?")
else:
    print(word_list[word_count.index(max(word_count))])
