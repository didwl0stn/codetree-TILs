n=int(input())
arr=[
    [0 for _ in range(n)]
    for _ in range(n)
]

for i in range(n):
    for j in range(n):
        arr[i][j] = (i+1)+n*j
for row in arr:
    for elem in row:
        print(elem,end=" ")
    print("")