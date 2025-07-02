n = int(input())
name = []
height = []
weight = []

for _ in range(n):
    n_i, h_i, w_i = input().split()
    name.append(n_i)
    height.append(int(h_i))
    weight.append(int(w_i))

# Please write your code here.

ans = []
class Total:
    def __init__(self,name,height,weight):
        self.name=name
        self.height=height
        self.weight=weight

for i in range(n):
    ans.append(Total(name[i],height[i],weight[i]))

ans.sort(key = lambda x:x.height)

for elem in ans:
    print(f"{elem.name} {elem.height} {elem.weight}")