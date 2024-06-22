res=[0]*4
for _ in range(3):
    c,i = input().split()
    if (c=='Y' and int(i)>=37):
        res[0]+=1
    elif (c=='N' and int(i)>=37):
        res[1]+=1
    elif (c=='Y' and int(i)<37):
        res[2]+=1
    else:
        res[3]+=1

for i in range(len(res)):
    print(res[i],end=' ')
if (res[0]>=2):
    print('E')