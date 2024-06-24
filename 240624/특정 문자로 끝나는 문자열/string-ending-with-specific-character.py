arr=[
    input() for _ in range(10)
]
a=input()
cnt=0
for i in arr:
    if i[-1]==a:
        print(i)
        cnt+=1
if (cnt==0):
    print('None')