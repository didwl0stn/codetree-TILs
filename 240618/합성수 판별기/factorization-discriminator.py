n=int(input())
check='N'
for i in range(2,n):
    if n%i==0:
        check='C'
        break
print(check)