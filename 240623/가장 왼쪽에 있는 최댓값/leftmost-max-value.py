n=int(input())
arr=list(map(int,input().split()))
max_idx = -1
while(max_idx!=0):
    max_val=max(arr)
    max_idx=arr.index(max_val)
    print(max_idx+1,end=" ")
    arr=arr[:max_idx]