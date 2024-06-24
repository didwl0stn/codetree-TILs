ans=""
a=input()
former=a[0]
cnt=1
for i in range(len(a)):
    if i==0:
        pass
    else:
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