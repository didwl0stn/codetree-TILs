n = int(input())
def square(n):
    temp = 1
    for i in range(1,n*n+1):
        print(temp,end=" ")
        temp += 1
        if temp==10:
            temp = 1
        if i%n == 0:
            print("")
square(n)