n = int(input())
students = [tuple(map(int, input().split())) + (i + 1,) for i in range(n)]

# Please write your code here.
class Student:
    def __init__(self,height,weight,num):
        self.height=height
        self.weight=weight
        self.num=num

ans = []
for i in range(n):
    ans.append(Student(students[i][0],students[i][1],students[i][2]))

ans.sort(key=lambda x: (-x.height,-x.weight,x.num))
for elem in ans:
    print(elem.height,elem.weight,elem.num)