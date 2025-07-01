N = int(input())

# Please write your code here.

def temp(N):
    if (N==1):
        return 1
    return temp(N-1)+N

print(temp(N))