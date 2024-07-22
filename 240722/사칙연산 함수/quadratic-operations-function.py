a,o,c = input().split()
a = int(a); c=int(c)
def f1(a,o,c):
    if (o=='+'):
        print(f"{a} {o} {c} = {a+c}")
    elif (o=='-'):
        print(f"{a} {o} {c} = {a-c}")
    elif (o=='/'):
        print(f"{a} {o} {c} = {a//c}")
    elif (o=='*'):
        print(f"{a} {o} {c} = {a*c}")
    else:
        print(False)

f1(a,o,c)