import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

n = int(input())
tree = [[] for _ in range(n+1)]

for _ in range(n-1):
  parent, child, weight = map(int, input().split())
  tree[parent].append((child, weight))
  tree[child].append((parent, weight))

def dfs(x, weight):
  for node, w in tree[x]:
    cal_w = weight + w
    if visited[node] == -1:
      visited[node] = cal_w
      dfs(node, cal_w)
  return

visited = [-1]*(n+1)
visited[1] = 0

dfs(1,0)
idx, tmp = 0, 0
for i in range(1, len(visited)):
  if visited[i] > tmp:
    tmp = visited[i]
    idx = i

visited = [-1]*(n+1)
visited[idx] = 0
dfs(idx, 0)

print(max(visited))
