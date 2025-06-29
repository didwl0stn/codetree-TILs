arr = ["apple","banana","grape","blueberry","orange"]

c = input()
cnt =0
for item in arr:
    if (item[3]== c or item[2]==c):
        print(item)
        cnt+=1
print(cnt)