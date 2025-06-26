n = int(input())
cnt = 1

arr = [[0 for _ in range(n)] for _ in range(n)]
for i in range(n):
    for j in range(n):
        arr[j][i] = cnt
        cnt +=1

for i in arr:
    for j in i:
        print(j,end=" ")
    print("")