n=int(input())
arr=list(map(int,input().split()))
first_max=max(arr)
idx=arr.index(first_max)
arr=arr[:idx]+arr[idx+1:]
print(first_max,max(arr))