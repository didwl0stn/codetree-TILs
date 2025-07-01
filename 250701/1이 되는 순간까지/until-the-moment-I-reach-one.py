N = int(input())

# Please write your code here.
cnt = 0;
def temp(N):
    global cnt
    if (N==1):
        return cnt
    if (N%2==0):
        cnt+=1
        temp(N//2)
    else:
        cnt+=1
        temp(N//3)
temp(N)
print(cnt)