a,b = map(int,input().split())

def f1(n):
    if (n%2==0):
        return False
    if (n%10==5):
        return False
    if(n%3==0 and n%9 !=0):
        return False
    
    return True
cnt = 0
for i in range(a,b+1):
    if (f1(i)==True):
        cnt+=1

print(cnt)