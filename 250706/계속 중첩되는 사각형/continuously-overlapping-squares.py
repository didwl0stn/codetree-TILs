n = int(input())
x1, y1, x2, y2 = [], [], [], []
for _ in range(n):
    a, b, c, d = map(int, input().split())
    x1.append(a)
    y1.append(b)
    x2.append(c)
    y2.append(d)

# Please write your code here.
arr = [
    [0 for _ in range(201)]
    for _ in range(201)
]

for i in range(n):
    if (i%2==0):
        for j in range(x1[i],x2[i]):
            for k in range(y1[i],y2[i]):
                arr[j][k] = 1
    else:
        for j in range(x1[i],x2[i]):
            for k in range(y1[i],y2[i]):
                arr[j][k] = 2
cnt=0
for j in range(201):
    for k in range(201):
        if arr[j][k]==2:
            cnt+=1

print(cnt)


