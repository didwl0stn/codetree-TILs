a,b = input().split()
for idx,value in enumerate(a):
    if not value.isdigit():
        a=a[:idx]
for idx,value in enumerate(b):
    if not value.isdigit():
        b=b[:idx]
print(int(a)+int(b))