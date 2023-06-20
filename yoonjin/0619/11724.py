import sys
sys.setrecursionlimit(5000)
input = sys.stdin.readline

def dfs(v):
    visited[v] = True
    for e in graph[v]:
        if not visited[e]:
            dfs(e)
    
n,m = map(int, input().split())
graph = [[] for _ in range(n+1)]
visited = [False] * (n+1)
count = 0

for i in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

for j in range(1, n+1):
    if not visited[j]:
        dfs(j)
        count += 1

print(count)
