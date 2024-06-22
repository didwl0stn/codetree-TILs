arr = list(map(int,input().split()))
arr2=[]
for i in arr:
    if (i==0):
        break
    else:
        arr2.append(i)

for i in arr2:
    if (i%2==0):
        print(i//2,end=" ")
    else:
        print(i+3,end=" ")