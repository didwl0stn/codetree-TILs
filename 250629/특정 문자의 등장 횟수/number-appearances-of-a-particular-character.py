a=input()
cnt1=0
cnt2=0
for i in range(len(a)-1):
    if (a[i]=='e' and a[i+1]=='e'):
        cnt1+=1
    if (a[i]=='e' and a[i+1]=='b'):
        cnt2+=1

print(cnt1,cnt2,sep=" ")