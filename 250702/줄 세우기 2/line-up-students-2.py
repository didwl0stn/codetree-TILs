n = int(input())
students = [
    (h, w, i + 1)
    for i, (h, w) in enumerate([tuple(map(int, input().split())) for _ in range(n)])
]

# Please write your code here.

class Student:
    def __init__(self,h,w,i):
        self.h=h
        self.w=w 
        self.i=i 
ans = []
for i in range(n):
    ans.append(Student(students[i][0],students[i][1],students[i][2]))

ans.sort(key = lambda x: (x.h, -x.w))

for elem in ans:
    print(elem.h, elem.w, elem.i)