n=int(input())
arr=list(map(int,input().split()))

arr2=[i**2 for i in arr]
for i in arr2:
    print(i,end=" ")