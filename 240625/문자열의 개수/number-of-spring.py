ans=[]
cnt=0
while True:
    n=input()
    if (n=='0'):
        break
    cnt+=1
    if(cnt%2==1):
        ans.append(n)
print(cnt)
for i in ans:
    print(i)