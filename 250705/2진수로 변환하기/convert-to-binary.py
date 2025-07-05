n = int(input())

# Please write your code here.
ans=""
while(True):
    ans+= str(int(n)%2)
    n=n//2
    if (n==0):
        break

print(ans[::-1])