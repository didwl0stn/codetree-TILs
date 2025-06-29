n=int(input())
arr = [
    int(input())
    for _ in range(n)
]

sums=str(sum(arr))
print(sums[1:]+sums[0])