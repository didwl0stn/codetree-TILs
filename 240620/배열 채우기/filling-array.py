arr = list(map(int,input().split()))
arr.pop()
arr = arr[::-1]
for i in arr:
    print(i,end=" ")