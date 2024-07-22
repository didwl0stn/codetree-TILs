n=int(input())
def f1(n,temp):
    if n ==0:
        print(temp)
        return
    else:
        temp += (n%10)**2
        n=n//10
        
        
        f1(n,temp)

f1(n,0)