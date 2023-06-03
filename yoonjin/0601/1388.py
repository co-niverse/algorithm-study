def dfs(x,y):
  if graph[x][y] == '-':
    graph[x][y] = 1
    for i in [1,-1]:
        yi = y + i
        if (yi > 0 and yi < m) and graph[x][yi] == '-':
            dfs(x,yi)
  if graph[x][y] == '|':
    graph[x][y] = 1
    for i in [1,-1]:
        xi = x + i
        if (xi > 0 and xi < n) and graph[xi][y] == '|':
            dfs(xi,y)


n, m = map(int, input().split())
graph = []
for i in range(n):
    graph.append(list(input()))


count = 0
for i in range(n):
  for j in range(m):
    if graph[i][j] == '-' or graph[i][j] == '|':
        dfs(i,j)
        count += 1


print(count)
