n = int(input())
cnt = [0 for _ in range(10)]
arr = list(map(int,input().split()))
for i in arr:
    cnt[i]+=1;
for i in cnt[1::]:
    print(i)