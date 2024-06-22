arr = list(map(int,input().split()))
ans=[0]*10
for i in arr:
    if i==0:
        break
    else:
        ans[i//10]+=1
for i in range(1,10):
    print(f"{i} - {ans[i]}")