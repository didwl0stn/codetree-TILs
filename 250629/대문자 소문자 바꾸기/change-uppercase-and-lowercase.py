a=input()
for i in a:
    if (i.islower()==True):
        print(i.upper(),end="")
    elif (i.isupper()==True):
        print(i.lower(),end="")