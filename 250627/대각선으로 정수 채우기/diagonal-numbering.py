n, m = map(int, input().split())

# Please write your code here.
start = []
for i in range(m):
    start.append([0,i])
for i in range(1,n):
    start.append([i,m-1])
num = 1

arr = [
    [0 for _ in range(m)]
    for _ in range(n)
]

for i in start:
    arr[i[0]][i[1]] = num
    num+=1
    while(i[0]+1 <n and i[1]-1 >=0):
        arr[i[0]+1][i[1]-1]=num
        i[0] +=1
        i[1] -=1
        num+=1
    
for i in arr:
    for j in i:
        print(j,end=" ")
    print()
