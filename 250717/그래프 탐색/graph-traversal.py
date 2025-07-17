n, m = map(int, input().split())
edges = [tuple(map(int, input().split())) for _ in range(m)]

# Please write your code here.
graph ={}
vert = [ i for i in range(1,n+1)]
visited = [0] * (n+1)
for edge in edges:
    if edge[0] not in graph:
        graph[edge[0]] = []
    graph[edge[0]].append(edge[1])
    if edge[1] not in graph:
        graph[edge[1]] = []
    graph[edge[1]].append(edge[0])


def dfs(n):
    visited[n] = 1
    if n in graph:
        for item in graph[n]:
            if visited[item]==0:
                
                dfs(item)
cnt = 0
dfs(1)
for i in visited:
    if i==1:
        cnt+=1
print(cnt -1)

