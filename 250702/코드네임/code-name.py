MAX_N = 5

codenames = []
scores = []
for _ in range(MAX_N):
    codename, score = input().split()
    codenames.append(codename)
    scores.append(int(score))

# Please write your code here.

ans=[]

class agent:
    def __init__(self,codename,score):
        self.codename=codename
        self.score=score

for i in range(5):
    ans.append(agent(codenames[i],scores[i]))

ans.sort(key=lambda agent : agent.score)
print(ans[0].codename,ans[0].score)