string=input()
target=input()

cnt=0

for i in range(len(string)-len(target)+1):
    temp = True
    for j in range(len(target)):
        if (string[i+j]!=target[j]):
            temp=False
            break
    if temp==True:
        cnt+=1
print(cnt)