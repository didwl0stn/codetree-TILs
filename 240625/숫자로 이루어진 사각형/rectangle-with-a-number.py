n = int(input())

def num_rect(n):
    num=1
    for i in range(n):
        for j in range(n):
            print(num,end=" ")
            num+=1
            if (num>=10):
                num=1
        print()
num_rect(n)