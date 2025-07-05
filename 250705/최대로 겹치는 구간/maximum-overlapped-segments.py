n = int(input())
segments = [tuple(map(int, input().split())) for _ in range(n)]

# Please write your code here.
arr = [0 for _ in range(201)]
for seg in segments:
    start,end = seg
    for i in range(start,end):
        arr[i]+=1

print(max(arr))