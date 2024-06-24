string,q = input().split()
for _ in range(int(q)):
    n=int(input())
    if n==1:
        string = string[1:] + string[0]
        print(string)
    if n==2:
        string = string[-1]+string[:-1]
        print(string)
    if n==3:
        string = string[::-1]
        print(string)