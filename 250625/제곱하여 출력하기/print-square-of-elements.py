n=int(input())
arr =list(map(int,input().split()))
arr2 = [i*i for i in arr]
for i in arr2:
    print(i,end=" ")