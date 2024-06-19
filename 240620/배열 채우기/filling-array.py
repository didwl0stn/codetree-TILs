arr = list(map(int,input().split()))
if (arr[-1]==0):
    arr.pop()
arr = arr[::-1]
for i in arr:
    print(i,end=" ")