n = int(input())
arr = list(map(int, input().split()))

# Please write your code here.

for i in range(1,len(arr)+1):
    if (i%2==1):
        temp = sorted(arr[:i])
        print(temp[(i-1)//2],end=" ")