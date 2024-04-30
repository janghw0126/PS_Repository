while True:
    # 블록 수의 합을 초기화
    sum = 0
    
    # 기초 층의 크기를 입력
    n = int(input())
    
    # 입력값이 0이면 반복을 종료
    if not n:
        break
    
    # 1부터 n까지 반복하며 블록 수를 합산
    for i in range(1, n+1):
        sum += i
    
    # 피라미드를 구성하는 데 필요한 총 블록 수를 출력
    print(sum)