# 10개의 정수를 입력받아 리스트로 저장
arr = list(map(int, input().split()))

count = 0
total_sum = 0

# 0이 입력되기 전까지 2의 배수를 찾아 개수와 합계 계산
for i in range(10):
    if arr[i] == 0:
        break
    if arr[i] % 2 == 0:
        count += 1
        total_sum += arr[i]

# 2의 배수의 개수와 합계 출력
print(f"{count} {total_sum}")