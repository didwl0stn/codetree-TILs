a, b = map(int, input().split())
n = input()

# Please write your code here.

n=list(n)
ans = 0
for i in n:
    ans = ans*8 + int(i)
ans = int(ans)
ans2= ""
while(True):
    ans2 += str(ans%b)
    ans = ans//b
    if (ans==0):
        break
print(ans2[::-1])


