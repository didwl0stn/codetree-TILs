n = int(input())
def f1(n,sums):
    if (n==0):
        print(sums)
        return
    sums+=n
    
    f1(n-1,sums)

f1(n,0)