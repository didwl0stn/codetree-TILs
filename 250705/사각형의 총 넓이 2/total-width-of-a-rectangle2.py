n = int(input())
x1, y1, x2, y2 = [], [], [], []
for _ in range(n):
    a, b, c, d = map(int, input().split())
    x1.append(a)
    y1.append(b)
    x2.append(c)
    y2.append(d)

# Please write your code here.
arr= [[0 for _ in range(201)]
        for _ in range(201)]

cnt = 0
for i in range(n):
    ax,ay,bx,by = x1[i],y1[i],x2[i],y2[i]
    for j in range(ay,by):
        for k in range(ax,bx):
            arr[j][k] = 1

for i in range(201):
    for j in range(201):
        if arr[i][j]:
            cnt+=1

print(cnt)