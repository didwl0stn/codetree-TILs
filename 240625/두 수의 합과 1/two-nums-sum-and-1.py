a,b = map(int,input().split())
c = a+b
cnt=0
for i in str(c):
    if i =='1':
        cnt+=1
print(cnt)