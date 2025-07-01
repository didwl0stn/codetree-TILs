n = int(input())

# Please write your code here.

def temp1(n):
    if (n==0):
        return
    temp1(n-1)
    print(n,end=" ")

def temp2(n):
    if (n==0):
        return
    print(n,end=" ")
    temp2(n-1)

temp1(n)
print()
temp2(n)