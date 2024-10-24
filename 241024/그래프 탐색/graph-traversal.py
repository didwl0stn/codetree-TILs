n,m = map(int,input().split())
vertex = [[0 for _ in range(n+1)] for _ in range(n+1)]
visited = [0 for _ in range(n+1)]
cnt = 0
for _ in range(m):
    x,y = map(int,input().split())
    vertex[x][y] = 1
    vertex[y][x] = 1

def dfs(start_v):
    global cnt
    visited[start_v] = 1
    for i in range(1, n+1):
        if vertex[start_v][i] == 1 and visited[i] == 0:
            cnt +=1  # 연결되어 있고, 아직 방문하지 않은 노드
            dfs(i)
dfs(1)
print(cnt)