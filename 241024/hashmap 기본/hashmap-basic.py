n = int(input())

dic ={}
for _ in range(n):
    command = input().split()
    if len(command) == 3:
        dic[command[1]] = command[2]
    else:
        a,b = command
        if a == 'remove':
            dic.pop(b)
        else:
            val = b in dic
            if (val):
                print(dic[b])
            else:
                print("None")