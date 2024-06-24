string = input()
ans=""
for idx,value in enumerate(string):
    if value.isalpha():
        ans+=value.upper()
print(ans)