num = 1
n,m = map(int,input().split())

arr=[]
for _ in range(n):
    temp=[]
    for _ in range(m):
        temp.append(num)
        num+=1
    arr.append(temp)

for i in range (n):
    for j in range(m):
        print(arr[i][j],end=" ")
    print("")