y = int(input())

def f1(y):
    if y%100 ==0 and y%400 != 0:
        return False
    else:
        if (y%4==0):
            return True
        else:
            return False

if (f1(y) == True):
    print("true")
else:
    print("false")