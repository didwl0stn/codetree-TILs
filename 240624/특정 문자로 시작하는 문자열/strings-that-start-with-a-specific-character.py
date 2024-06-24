n=int(input())
arr=[
    input() for _ in range(n)
]
a=input()
cnt=0
len_sum=0
for i in arr:
    if i[0]==a:
        cnt+=1
        len_sum+=len(i)
print(f"{cnt} {len_sum/cnt:.2f}")