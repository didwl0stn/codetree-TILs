n = int(input())

# Please write your code here.

def temp(n):
    sums=0
    for i in range(1,n+1):
        sums+=i
    return sums//10

print(temp(n))