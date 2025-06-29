y = int(input())

# Please write your code here.

def bitch(n):
    if (n%4!=0):
        return False
    if (n%100==0 and n%400!=0):
        return False
    return True

print("true" if bitch(y) else "false")