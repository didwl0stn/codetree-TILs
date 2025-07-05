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
arr=[]
for i in range(n):
    if dir[i] == 'R':
        black += x[i]
        white = max(0,white-x[i])

    if dir[i] == 'L':
        white += x[i]
        black = max(0,black-x[i])
print(white, black)



