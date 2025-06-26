n,m = map(int,input().split())

arr1 = [
    list(map(int,input().split()))
    for _ in range(n)
]

arr2 = [
    list(map(int,input().split()))
    for _ in range(n)
]

arr3 = []

for i in range(n):
    temp = []
    for j in range(m):
        a = 0 if (arr1[i][j] == arr2[i][j]) else 1
        temp.append(a)
    arr3.append(temp)

for i in range(n):
    for j in range(m):
        print(arr3[i][j],end=" ")
    print("")