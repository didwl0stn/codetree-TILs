a,o,c = input().split()
a = int(a); c=int(c)
def f1(a,o,c):
    if (o=='+'):
        return a+c
    if (o=='-'):
        return a-c
    if (o=='/'):
        return a/c
    if (o=='*'):
        return a*c
print(f"{a} {o} {c} = ",f1(a,o,c),sep="")