a=list(input())
a1=a[0]
a2=a[1]
for i in range(len(a)):
    if a[i]==a1:
        a[i]=a2
    elif a[i]==a2:
        a[i]=a1

print("".join(a))