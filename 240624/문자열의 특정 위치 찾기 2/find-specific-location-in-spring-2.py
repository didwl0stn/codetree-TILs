arr = ["apple","banana","grape","blueberry","orange"]
a=input()
cnt=0
for i in arr:
    if a in i[2:4]:
        cnt+=1
        print(i)
print(cnt)