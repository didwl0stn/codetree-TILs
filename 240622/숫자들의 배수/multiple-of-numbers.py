n=int(input())
arr=[]
cnt=0
i=1
while (cnt!=2):
    if(n*i%5==0):
        cnt+=1
    arr.append(n*i)
    i+=1
for i in arr:
    print(i,end=" ")