A = input()

# Please write your code here.
ans=str(A[0])
now=A[0]
cnt=0
for i in A:
    temp=A.count(i)
    if (now==i):
        cnt+=1
        continue
    else:
        ans = ans + str(cnt)
        now=i
        ans+=i
        cnt=1
ans+=str(cnt)
print(len(ans))
print(ans)