arr = list(map(int,input().split()))
sums =0
avg = 0
cnt = 0
for i in range(len(arr)):
    if (arr[i] >=250):
        break
    else:
        sums += arr[i]
        cnt += 1


print(f'{sums} {sums/cnt}')