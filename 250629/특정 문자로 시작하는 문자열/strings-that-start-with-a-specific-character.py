n=int(input())
arr = [
    input()
    for _ in range(n)
]

sums=0
cnt=0
c=input()
for item in arr:
    if(item[0]==c):
        sums+=len(item)
        cnt+=1
print(f"{cnt} {sums/cnt:.2f}")