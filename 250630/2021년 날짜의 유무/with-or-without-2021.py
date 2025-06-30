M, D = map(int, input().split())

# Please write your code here.

def temp(M,D):
    arr=[1,3,5,7,8,10,12]
    if (M>12):
        return False
    if (M==2):
        if D>28:
            return False
    if (M not in arr):
        if (D>30):
            return False
    if (M in arr):
        if (D>31):
            return False

    return True
    

print("Yes" if temp(M,D) else "No")