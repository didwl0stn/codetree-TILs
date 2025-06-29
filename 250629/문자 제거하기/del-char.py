s=input()
while(True):
    if (len(s)==1):
        break;
    n=int(input())
    s=list(s)
    if (n>=len(s)):
        s.pop(-1)
    else:
        s.pop(n)
    print("".join(s))