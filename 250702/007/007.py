secret_code, meeting_point, time = input().split()
time = int(time)

# Please write your code here.

class Temp:
    def __init__(self,s,m,t):
        self.secret=s
        self.meeting=m
        self.time=t

temp = Temp(secret_code,meeting_point,time)
print(f"secret code : {temp.secret}\nmeeting point : {temp.meeting}\ntime : {temp.time}")