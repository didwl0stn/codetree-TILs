a,b=map(int,input().split())
check=0
for i in range(a,b+1):
    if (1920 % i==0 and 2880 % i==0):
        check=1
        break

print(check)