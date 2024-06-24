string=input()
ee_cnt=0
eb_cnt=0
for i in range(len(string)-1):
    if (string[i]=='ee'[0] and string[i+1]=='ee'[1]):
        ee_cnt+=1
    if (string[i]=='eb'[0] and string[i+1]=='eb'[1]):
        eb_cnt+=1
print(ee_cnt, eb_cnt)