n = int(input())

# Please write your code here.

def temp(n):
    a = 0
    n=list(str(n))
    for i in n:
        a +=int(i)
    return a

if (n%2==0 and temp(n)%5==0):
    print("Yes")
else:
    print("No")