import sys
input=sys.stdin.readline

# 명령의 수 N을 선언한다.
N=int(input())

#요소들을 담을 큐 리스트를 선언한다.
command_queue=[]

# N번 반복하면서 각 명령들을 수행한다.
for _ in range(N):
    command=input().rstrip().split()
    if command[0]=="push":
        command_queue.append(command[1])
    elif command[0]=="pop":
        print(command_queue.pop(0) if command_queue else -1)
    elif command[0]=="size":
        print(len(command_queue))
    elif command[0]=="empty":
        print(0 if command_queue else 1)
    elif command[0]=="front":
        print(command_queue[0] if command_queue else -1)
    elif command[0]=="back":
        print(command_queue[-1] if command_queue else -1)


