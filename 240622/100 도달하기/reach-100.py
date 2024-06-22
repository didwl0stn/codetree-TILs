arr=[1,0]
arr[1]=int(input())
i=2
while True:
    arr.append(arr[i-1]+arr[i-2])
    
    if (arr[i]>100):
        break
    i+=1
for i in arr:
    print(i,end=" ")