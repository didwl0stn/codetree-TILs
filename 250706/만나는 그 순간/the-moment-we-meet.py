n, m = map(int, input().split())

d = []
t = []
for _ in range(n):
    direction, time = input().split()
    d.append(direction)
    t.append(int(time))

d2 = []
t2 = []
for _ in range(m):
    direction, time = input().split()
    d2.append(direction)
    t2.append(int(time))

# Please write your code here.
arr = [0] * 2000001
start = 1000000

time_sum = sum(t)



a_nows=[]
b_nows=[]
a_now=0
b_now=0
for i in range(n):
    for j in range(t[i]):
        if (d[i]=='L'):
            a_now-=1
        else:
            a_now+=1
        a_nows.append(a_now)

for i in range(m):
    for j in range(t2[i]):
        if (d2[i]=='L'):
            b_now-=1
        else:
            b_now+=1
        b_nows.append(b_now)

        
    
for i in range(time_sum):
    if (a_nows[i]==b_nows[i]):
        print(i+1)
        break