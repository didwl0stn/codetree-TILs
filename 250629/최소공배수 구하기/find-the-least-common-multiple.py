n, m = map(int, input().split())

# Please write your code here.
def gg(n,m):
    cnt=1
    while(True):
        if  ((max(n,m)*cnt)%n==0 and (max(n,m)*cnt)%m==0):
            print(max(n,m)*cnt)
            break
        cnt+=1

gg(n,m)
        
    