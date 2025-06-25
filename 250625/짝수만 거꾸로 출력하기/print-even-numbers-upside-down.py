n = int(input())
arr = list(map(int,input().split()))

temp = []
for i in range(len(arr)-1,-1,-1):
    if (arr[i]%2==0):
        temp.append(arr[i])
for i in temp:
    print(i,end=" ")