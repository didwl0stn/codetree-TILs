arr = list(map(int,input().split()))
sum = cnt = 0
for val in arr:
    if val >= 250:
        break
    sum+=val
    cnt+=1

print(f"{sum} {sum/cnt:.1f}")