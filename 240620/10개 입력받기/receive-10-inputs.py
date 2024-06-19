arr = list(map(int,input().split()))

for i in range(10):
    if arr[i]==0:
        arr=arr[:i]
        break
print(f"{sum(arr)} {sum(arr)/len(arr):.1f}")