n = int(input())
arr = [int(input()) for _ in range(n)]

# Please write your code here.
now = arr[0]
cnt = 1
maxs=1
for i in range(1,len(arr)):
    
    if now==arr[i]:
        cnt +=1
        if i==len(arr)-1:
            maxs=max(cnt,maxs)
    else:
        maxs = max(cnt,maxs)
        now=arr[i]
        cnt=1

    
print(maxs)