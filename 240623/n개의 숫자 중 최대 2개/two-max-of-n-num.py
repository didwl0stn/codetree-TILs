n=int(input())
arr=list(map(int,input().split()))
sorted_arr=sorted(arr,reverse=True)
print(sorted_arr[0], sorted_arr[1])