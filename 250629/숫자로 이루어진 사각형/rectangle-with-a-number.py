n = int(input())

# Please write your code here.

def pri(n):
    num=[1,2,3,4,5,6,7,8,9]
    idx=0
    for i in range(n):
        for j in range(n):
            print(num[idx],end=" ")
            idx = (idx+1)%9
        print()

pri(n)