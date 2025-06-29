cnt = 0
temp=[]
while(True):
    a = input()
    if a=='0':
        break
    else:
        cnt+=1
        if(cnt%2==1):
            temp.append(a)

print(cnt)
for item in temp:
    print(item)