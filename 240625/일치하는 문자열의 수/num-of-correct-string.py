n,A = input().split()
cnt=0
for _ in range(int(n)):
    temp = input()
    if temp==A:
        cnt+=1
print(cnt)