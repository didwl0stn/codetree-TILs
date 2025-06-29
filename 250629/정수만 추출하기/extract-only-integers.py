a,b = input().split()
a1=""
b1=""
for i in a:
    if i.isdigit()==True:
        a1+=i
    else:
        break
for i in b:
    if i.isdigit()==True:
        b1+=i
    else:
        break

print(f"{int(a1) + int(b1)}")