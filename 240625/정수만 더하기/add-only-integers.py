sum=0
string=input()
for i in string:
    if i.isdigit():
        sum+=int(i)

print(sum)