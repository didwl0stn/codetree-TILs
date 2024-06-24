import sys
string = input()
target=input()
answer=-1
for i in range(len(string)-len(target)+1):
    for j in range(len(target)):
        if (string[i+j]==target[j]):
            pass
        else:
            break
        if (j==len(target)-1):
            print(i)
            sys.exit()
print(answer)