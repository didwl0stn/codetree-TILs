# 입력 받기
n, m = map(int, input().split())

# 2차원 배열 초기화
arr = [[0 for _ in range(m)] for _ in range(n)]

# 숫자 채우기
num = 1
for k in range(n + m - 1):
    for i in range(n):
        for j in range(m):
            if j + i == k:
                arr[i][j] = num
                num += 1

# 배열 출력
for row in arr:
    for elem in row:
        print(elem,end=" ")
    print("")