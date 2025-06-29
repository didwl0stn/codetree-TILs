cnt = 0
a=input()
b=input()
while(True):
    cnt+=1
    a=a[-1] + a[:-1]
    if (a==b):
        break
    if cnt==len(a):
        cnt=-1
        break

print(cnt)