n=int(input())
arr=list(map(int,input().split()))
new=[]
for i in arr:
    if arr.count(i)>=2:
        pass
    else:
        new.append(i)

print(max(new))