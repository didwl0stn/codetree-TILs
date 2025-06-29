a=input()
b=input()
a1=b1=""
for i in a:
    if i.isdigit()==True:
        a1+=i

for i in b:
    if i.isdigit()==True:
        b1+=i

print(int(a1)+int(b1))