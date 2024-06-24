a=input()
b=input()
while True:
    a=a.replace(b,"")
    if (b not in a):
        break
print(a)