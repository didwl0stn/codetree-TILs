from collections import deque

n = int(input())
commands = [tuple(input().split()) for _ in range(n)]
x = []
dir = []
for num, direction in commands:
    x.append(int(num))
    dir.append(direction)

# Please write your code here.
white=0
black=0
now=0
pos=[(-1,0)] #흰색 1 검은색 2
for i in range(n):
    if dir[i] == 'R':
        if (pos[-1][0]==2):
            black += x[i]-1
            white = max(0,white-x[i]-1)
        else:
            black += x[i]
            white = max(0,white-x[i])
        now += x[i]-1
        pos.append((2,now))
    if dir[i] == 'L':
        if (pos[-1][0]==1):
            white += x[i]-1
            black = max(0,black-x[i]-1)
        else:
            white += x[i]
            black = max(0,black-x[i])
        now += x[i]-1
        
        pos.append((1,now))


        
print(white, black)



