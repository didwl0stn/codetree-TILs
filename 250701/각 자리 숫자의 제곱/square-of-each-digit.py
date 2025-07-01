N = int(input())

# Please write your code here.

def temp(N):
    if N==0:
        return 0

 
    return temp(N//10) + (N%10)**2

print(temp(N))