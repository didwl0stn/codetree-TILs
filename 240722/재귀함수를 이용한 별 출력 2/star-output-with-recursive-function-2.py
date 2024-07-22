N = int(input())

def f1(N):
    if (N==0):
        return
    print("* "*N,sep=" ")
    f1(N-1)
    print("* "*N,sep=" ")
f1(N)