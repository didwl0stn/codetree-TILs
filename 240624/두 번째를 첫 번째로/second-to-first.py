string=list(input())
a=string[0]
b=string[1]
for i in range(len(string)):
    if (string[i]==b):
        string[i]=a
print("".join(string))