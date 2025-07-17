from collections import deque
n, m = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.
visited = [
    [0 for _ in range(m)]
    for _ in range(n)
]

q = deque([(0,0)])
visited[0][0]=1
dx = [-1,0,1,0]
dy = [0,-1,0,1]
def bfs(x,y):
    while(q):
        x,y = q.popleft()
        for i in range(4):
            if (0<=(x+dx[i])<n) and (0<=(y+dy[i])<m) and (visited[x+dx[i]][y+dy[i]]==0) and (a[x+dx[i]][y+dy[i]]==1):
                q.append((x+dx[i],y+dy[i]))
                visited[x+dx[i]][y+dy[i]]=1
        
bfs(0,0)
print(visited[n-1][m-1])
