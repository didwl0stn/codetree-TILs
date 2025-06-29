a = list(input())
for i in a:
    if i.isalpha()==False:
        continue
    else:
        print(i.upper(),end="")