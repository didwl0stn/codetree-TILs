arr = list(map(int,input().split()))
arr1 = arr[1::2]

arr2 = arr[2::3]
print(f"{sum(arr1)} {sum(arr2)/len(arr2):.1f}")