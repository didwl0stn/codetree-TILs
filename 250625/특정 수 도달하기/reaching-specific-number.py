arr=[]
temp = list(map(int,input().split()))
for n in temp:
    if (n>=250):
        break
    arr.append(n)

print(f"{sum(arr)} {sum(arr)/len(arr):.1f}")