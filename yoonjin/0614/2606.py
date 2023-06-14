computer = int(input())
num = int(input())
graph = [[] for _ in range(computer + 1)]
visit = [0] * (computer + 1)
            
for i in range(num):
    a,b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
    
def dfs(graph, v, visited):
    visit[v] = 1
    for i in graph[v]:
        if visit[i] == 0:
            dfs(graph, i, visited)

dfs(graph, 1, visit)
print(visit.count(1) - 1)
