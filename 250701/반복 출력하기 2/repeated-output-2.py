n = int(input())

# Please write your code here.

def temp(n):
    if (n==0):
        return
    print("HelloWorld")
    temp(n-1)

temp(n)