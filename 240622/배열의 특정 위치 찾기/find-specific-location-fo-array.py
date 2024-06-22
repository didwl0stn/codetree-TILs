arr = list(map(int,input().split()))
sum_even=0
for i in range(1,len(arr),2):
    sum_even+=arr[i]

sum=0
for i in range(2,len(arr),3):
    sum+=arr[i]
print(f"{sum_even} {sum/3:.1f}")