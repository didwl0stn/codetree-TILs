n, m = map(int, input().split())

# Please write your code here.

def gcd(n,m):
    maxs=-1
    for i in range(1,min(n,m)+1):
        if (n%i==0 and m%i==0 and i>maxs):
            maxs=i

    print(maxs)

gcd(n,m)