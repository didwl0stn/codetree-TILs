a,b,c = map(int,input().split())
cnt="YES"
for i in range(a,b+1):
    if(i%c==0):
        cnt="NO"
        break

print(cnt)