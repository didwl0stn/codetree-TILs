a,b= map(int,input().split())
ans=[0]*10
while(a>1):
    temp=a%b
    a=a//b
    ans[temp]+=1
answer=0
for i in ans:
    answer+=i**2

print(answer)