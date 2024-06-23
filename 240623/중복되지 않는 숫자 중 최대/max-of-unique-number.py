n=int(input())
arr=list(map(int,input().split()))
new=[]
for i in arr:
    if arr.count(i)>=2:
        pass
    else:
        new.append(i)
if (len(new)):
    print(max(new))
else:
    print(-1)