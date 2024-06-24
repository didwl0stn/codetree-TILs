n=int(input())
arr=[
    input() for _ in range(n)
]
len_sum=0
a_cnt=0
for i in arr:
    len_sum+=len(i)
    if i[0]=='a':
        a_cnt+=1
print(len_sum,a_cnt)