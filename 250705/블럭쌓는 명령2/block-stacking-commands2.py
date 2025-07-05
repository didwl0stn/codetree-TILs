n, k = map(int, input().split())
commands = [tuple(map(int, input().split())) for _ in range(k)]

# Please write your code here.

arr = [0 for _ in range(n)]

for com in commands:
    start,end = com
    
    for i in range(start-1,end):
        arr[i]+=1

print(max(arr))