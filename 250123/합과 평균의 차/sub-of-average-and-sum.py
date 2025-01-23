arr = list(map(int,input().split()))
print(f'{sum(arr)}\n{sum(arr)//len(arr)}\n{sum(arr) - (sum(arr)//len(arr))}')