from collections import Counter

a=input()
b=input()
cnt=0
for i in range(0,len(a)-len(b)+1):
    if (a[i:i+len(b)]==b):
        cnt+=1

print(cnt)