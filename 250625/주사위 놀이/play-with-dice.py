arr = list(map(int,input().split()))
ans = [ 0 for _ in range(7)]
for i in arr:
    ans[i]+=1

for i in range(1,7):
    print(f"{i} - {ans[i]}")