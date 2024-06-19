n=int(input())

arr=list(map(float,input().split()))

avg = sum(arr)/n
grade=0
if (avg>=4.0):
    grade="Perfect"
elif (avg>=3.0):
    grade="Good"
else:
    grade="Poor"

print(f"{avg:.1f}\n{grade}")