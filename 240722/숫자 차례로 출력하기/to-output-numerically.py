n = int(input())

def pr(n):
    if n==0:
        return
    print(n,end=" ")
    pr(n-1)
def f1(n,temp = 1):
    if (temp == n+1):
        return
    print(temp,end=" ")
    f1(n,temp+1)
f1(n)
print("")
pr(n)