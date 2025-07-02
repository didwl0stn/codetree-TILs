n = int(input())
date = []
day = []
weather = []

for _ in range(n):
    d, dy, w = input().split()
    date.append(d)
    day.append(dy)
    weather.append(w)

# Please write your code here.

class Temp:
    def __init__(self,date,day,weather):
        self.data = date
        self.day=day
        self.weather=weather

ans=[]
for i in range(n):
    ans.append(Temp(date[i],day[i],weather[i]))

ans.sort(key = lambda elem : elem.data)
for elem in ans:
    if (elem.weather=='Rain'):
        print(elem.data,elem.day,elem.weather)
        break