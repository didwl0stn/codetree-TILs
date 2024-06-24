a = input()
command= input()
for i in range(len(command)):
    if (command[i]=='L'):
        a = a[1:]+a[0]
    elif (command[i]=='R'):
        a= a[-1] + a[:-1]
print(a)