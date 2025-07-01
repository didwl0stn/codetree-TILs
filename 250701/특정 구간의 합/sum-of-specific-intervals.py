n, m = map(int, input().split())
arr = list(map(int, input().split()))
queries = [tuple(map(int, input().split())) for _ in range(m)]

# Please write your code here.

def temp(a,b):
    global arr
    
    return(sum(arr[a-1:b]))

for i in range(m):
    a,b = queries[i]
    print(temp(a,b))



