ans=""
a=input()
former=a[0]
cnt=1
for i in range(1,len(a)):
    if a[i]==former:
        cnt+=1
    else:
        ans+=former
        ans+=str(cnt)
        former=a[i]
        cnt=1
    
    if (i==len(a)-1):
        ans+=former
        ans+=str(cnt)
print(len(ans))
print(ans)