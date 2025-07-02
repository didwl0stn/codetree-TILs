m1, d1, m2, d2 = map(int, input().split())

# Please write your code here.
days = [0,31,28,31,30,31,30,31,31,30,31,30,31]

ans1=0
ans2=0
for i in range(m1):
    ans1+= days[i]
ans1+=d1
for i in range(m2):
    ans2+= days[i]
ans2+=d2
print(ans2-ans1+1)