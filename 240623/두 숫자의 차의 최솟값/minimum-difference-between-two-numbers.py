import sys
n=int(input())
arr=list(map(int,input().split()))
ans=sys.maxsize
min_val=arr[0]
max_val=arr[0]
for i in arr:
    if i>max_val:
        ans=min(ans,i-max_val)
        max_val=i
    if i<min_val:
        ans=min(ans,min_val-i)
        min_val=i 

print(ans)