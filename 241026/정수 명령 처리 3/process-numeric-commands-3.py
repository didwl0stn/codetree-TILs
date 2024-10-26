from collections import deque
n = int(input())

dq = deque()
for _ in range(n):
    com = input()
    if " " in com:
        a,b = map(str,com.split())
        if a =="push_front":
            dq.appendleft(b)
        else:
            dq.append(b)
    else:
        if com == "pop_front":
            a = dq.popleft()
            print(a)
        elif com == "pop_back":
            a = dq.pop()
            print(a)
        elif com == "front":
            print(dq[0])
        elif com == "back":
            print(dq[-1])
        elif com == "size":
            print(len(dq))
        elif com == "empty":
            if len(dq) == 0:
                print(1)
            else:
                print(0)