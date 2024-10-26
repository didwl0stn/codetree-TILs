n = int(input())
grid = [[0 for _ in range(n)] for _ in range(n)]

for i in range(n):
    inputs = list(map(int,input().split()))
    for j in range(n):
        grid[i][j] = inputs[j]

answer = 0
for i in range(n - 2):
    for j in range(n-2):
        temp = 0
        for k in range(3):
            for l in range(3):
                if grid[i+k][j+l] == 1:
                    temp += 1
        
        answer = max(answer,temp)

print(answer)