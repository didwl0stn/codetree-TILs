a, b = map(int, input().split())

# Please write your code here.

def isPrime(n):
    for i in range(2,n):
        if (n%i==0):
            return False
    return True

sums=0

for i in range(a,b+1):
    if isPrime(i):
        sums+=i

print(sums)