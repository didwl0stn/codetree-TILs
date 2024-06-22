n=int(input())
arr=list(map(int,input().split()))
arr2=[i for i in arr if i%2==0]
for i in arr2:
    print(i,end=" ")