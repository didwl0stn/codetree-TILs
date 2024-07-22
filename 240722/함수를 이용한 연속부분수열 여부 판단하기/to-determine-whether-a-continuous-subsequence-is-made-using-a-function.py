n1,n2 = map(int,input().split())
a = list(input().split())
b = list(input().split())

def func(a,b):
    for i in range(0, len(a)-len(b)):
        for j in range(len(b)):
            if int(a[i+j]) == int(b[j]):
                if (j == len(b)-1):
                    return True
                continue
            else:
                break

if (func(a,b)):
    print('Yes')
else:
    print('No')