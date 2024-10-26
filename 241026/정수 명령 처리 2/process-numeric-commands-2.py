from collections import deque
que = deque()
n = int(input())
while(n):
    command = input()
    if " " in command:
        a,b = map(str, command.split())
        que.append(b)
    else:
        if command == "pop":
            a = que.popleft()
            print(a)
        if command == "size":
            print(len(que))
        if command == "empty":
            temp = 1 if len(que) == 0 else 0
            print(temp)
        if command == "front":
            print(que[0])
    
    n -=1