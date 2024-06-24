a=input()
b=input()
ans=-1
for i in range(len(a)):
    a = a[-1] + a[:-1]
    if (a==b):
        ans = i+1
        break
print(ans)