binary = input()

# Please write your code here.

binary = list(binary)

ans = 0
for i in binary:
    ans = ans*2 + int(i)

print(ans)