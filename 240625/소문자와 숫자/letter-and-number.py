string = input()
for i in string:
    if i.isalpha():
        print(i.lower(),end="")
    if i.isdigit():
        print(i,end="")