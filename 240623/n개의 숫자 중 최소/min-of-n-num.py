n=int(input())
arr = list(map(int,input().split()))

min_val=min(arr)
print(min_val,arr.count(min_val))