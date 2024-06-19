arr = list(map(int,input().split()))
for i in range(0,len(arr)):
    if (arr[i]==0):
        arr=arr[i-1::-1]
        break

    elif(i==len(arr)-1):
        arr=arr[::-1]
for i in arr:
    print(i,end=" ")