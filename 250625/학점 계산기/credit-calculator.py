n = int(input())
list = list(map(float,input().split()))
temp = sum(list)/n
if (temp >=4.0):
    grade = "Perfect"
elif (temp>=3.0):
    grade = "Good"
else:
    grade = "Poor"
print(f"{temp:.1f}\n{grade}")