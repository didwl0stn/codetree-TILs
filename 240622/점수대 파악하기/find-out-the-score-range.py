arr = list(map(int,input().split()))
cnt =[0]*11

for i in arr:
    if i==0:
        break
    cnt[i//10]+=1

for i in range(10,0,-1):
    print(f"{i*10} - {cnt[i]}")