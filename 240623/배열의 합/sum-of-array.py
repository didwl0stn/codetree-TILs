arr = [list(map(int, input().split())) for _ in range(4)]

# 각 줄의 합을 계산하여 출력
for line in arr:
    print(sum(line))