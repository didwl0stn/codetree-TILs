n = int(input())

# Please write your code here.

def temp(n):
    if (n==0):
        return

    print("* "*n)
    temp(n-1)
    print("* "*n)

temp(n)