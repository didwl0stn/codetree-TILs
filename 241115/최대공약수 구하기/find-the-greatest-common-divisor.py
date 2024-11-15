n,m = map(int,input().split())
def gcd(n,m):
    if n < m:
	    n, m = m, n
    if m==0:
	    print(n)
    if n % m == 0:
	    print(m)
    else:
	    return gcd(m, n%m)

gcd(n,m)