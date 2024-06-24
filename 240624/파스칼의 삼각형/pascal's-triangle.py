n=int(input())

arr = [
    [0 for _ in range(n)]
    for _ in range(n)
]

for i in range(0,n):
    for j in range(i+1):
        if(j==0 or j==i):
            arr[i][j]=1
        else:
            arr[i][j] = arr[i-1][j]+arr[i-1][j-1]

for row in arr:
    for elem in row:
        if (elem!=0):
            print(elem,end=" ")
    print("")