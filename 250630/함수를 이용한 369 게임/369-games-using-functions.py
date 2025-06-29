a, b = map(int, input().split())

# Please write your code here.

def number(n):
    n=list(str(n))
    if ('3' in n or '6' in n or '9' in n):
        return True
    else:
        return False

def sam(n):
    if(n%3==0 or number(n)):
        return True
    else:
        return False
cnt=0
for i in range(a,b+1):
    if sam(i):
        cnt+=1
print(cnt)