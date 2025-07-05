from collections import deque

n = int(input())
commands = [tuple(input().split()) for _ in range(n)]
x = []
dir = []
for num, direction in commands:
    x.append(int(num))
    dir.append(direction)

# Please write your code here.

now=n*100
arr= [0 for _ in range(2*n * 100)]
arr.append(0)
left = now
right= now
for i in range(n):
    if dir[i] == 'R':
        for j in range(now, now+x[i]):
            arr[j] = 2
        now = now+x[i]-1

        if (now>right):
            right=now
        # if (pos[-1][0]==2):
        #     black += x[i]-1
        #     white = max(0,white-x[i]-1)
        # else:
        #     black += x[i]
        #     white = max(0,white-x[i])
        # now += x[i]-1
        # pos.append((2,now))
    if dir[i] == 'L':
        for j in range(now, now-x[i],-1):
            arr[j] = 1
        now = now-x[i]+1
        if (now<left):
            left=now
    
        # if (pos[-1][0]==1):
        #     white += x[i]-1
        #     black = max(0,black-x[i]-1)
        # else:
        #     white += x[i]
        #     black = max(0,black-x[i])
        # now += x[i]-1
        
        # pos.append((1,now))



white = arr.count(1)
black=arr.count(2)


print(white, black)



