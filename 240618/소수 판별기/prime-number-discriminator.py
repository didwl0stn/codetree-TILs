n=int(input())
check="P"
for i in range(2,n):
    if (n%i==0):
        check="C"
        break

print(check)