a,b = map(int,input().split())
def func(n):
    for i in range(2,n):
        if (n%i==0):
            return False
    sum = 0
    while (n != 0):
        sum += n%10
        n //= 10
    if (sum%2==0):
        return True
cnt = 0
for i in range(a,b+1):
    if(func(i)==True):
        cnt+=1
print(cnt)