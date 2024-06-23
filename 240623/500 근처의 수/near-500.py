arr=list(map(int,input().split()))
less_arr=[i for i in arr if i<500]
more_arr=[i for i in arr if i>500]

print(max(less_arr), min(more_arr))