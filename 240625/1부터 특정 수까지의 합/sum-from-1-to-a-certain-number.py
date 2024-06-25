n=int(input())
def temp(n):
    x=0
    for i in range(1,n+1):
        x+=i
    return x//10
print(temp(n))