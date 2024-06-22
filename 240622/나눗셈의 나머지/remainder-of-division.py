a,b= map(int,input().split())
ans=[0]*10
while(a>1):
    temp=a%b
    a=a//b
    ans[temp]+=1

res=[i**2 for i in ans]
print(sum(res))