n=int(input())
arr=list(map(int,input().split()))
temp_max=0
for i in range(1,n):
    a=min(arr[:i])
    b=max(arr[i:])
    if (b-a)>temp_max:
        temp_max=b-a 

print(temp_max)