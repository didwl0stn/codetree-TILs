n = int(input())

name = []
score1 = []
score2 = []
score3 = []

for _ in range(n):
    student_input = input().split()
    name.append(student_input[0])
    score1.append(int(student_input[1]))
    score2.append(int(student_input[2]))
    score3.append(int(student_input[3]))

# Please write your code here.

class Student:
    def __init__(self,name,score1,score2,score3):
        self.name=name
        self.score1=score1
        self.score2=score2
        self.score3=score3

ans = []
for i in range(n):
    ans.append(Student(name[i],score1[i],score2[i],score3[i]))
ans.sort(key = lambda x:x.score1+x.score2+x.score3)
for elem in ans:
    print(elem.name, elem.score1, elem.score2, elem.score3)