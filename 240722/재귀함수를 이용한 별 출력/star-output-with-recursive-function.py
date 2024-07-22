n=int(input())
def f1(n):
    if n==0:
        return
    f1(n-1)
    print("*"*n)
f1(n)