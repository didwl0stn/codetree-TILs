N = int(input())

# Please write your code here.

def temp(N):
    if (N==1):
        return 1
    if (N==2):
        return 1
    return (temp(N-1)+temp(N-2))

print(temp(N))