m1, d1, m2, d2 = map(int, input().split())
A = input()

# Please write your code here.
days = [0,31,29,31,30,31,30,31,31,30,31,30,31]
mod = 0
ans1=0
ans2=0

for i in range(m1):
    ans1+=days[i]
ans1+=d1
for i in range(m2):
    ans2+=days[i]
ans2+=d2

if A=="Mon":
    mod=0
if A=="Tue":
    mod=1
if A=="Wed":
    mod=2
if A=="Thu":
    mod=3
if A=="Fri":
    mod=4
if A=="Sat":
    mod=5
if A=="Sun":
    mod=6
print((ans2-(ans1+mod))//7 + 1)