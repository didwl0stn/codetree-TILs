
n = int(input())

def res(n):
    if (n % 2 == 0 and sum(map(int,str(n))) %5 == 0):
        return "Yes"
    else:
        return "No"
print(res(n))

