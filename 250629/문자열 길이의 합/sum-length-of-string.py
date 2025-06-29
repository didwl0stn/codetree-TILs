n=int(input())
cnt = 0
sums = 0
arr = [
    input()
    for _ in range(n)
]

for item in arr:
    if (item[0]=='a'):
        cnt+=1
    sums+=len(item)
print(sums,cnt)