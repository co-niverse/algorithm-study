import sys
from collections import deque
readline = sys.stdin.readline
n,m = map(int,readline().split())
maze = [[] for _ in range(n)]
visited = [[False for _ in range(m)] for _ in range(n)]
for i in range(n):
    maze[i] = list(map(int,readline().strip()))

#위, 오른쪽 ,아래 , 왼쪽
dn = [-1,0,+1,0]
dm = [0,+1,0,-1]
minCount = 1e9
def bfs(nextN,nextM):
    global minCount
    queue = deque([[nextN,nextM,1]])

    while queue :
        node = queue.popleft()
        nextN = node[0]
        nextM = node[1]
        count = node[2]
        for i in range(4):
            if -1 < nextN+dn[i] < n and -1 < nextM+dm[i] < m :
                if nextN+dn[i] == n-1 and nextM+dm[i] == m-1 :
                    minCount = min(minCount,count+1)
                    continue
                if maze[nextN+dn[i]][nextM+dm[i]] == 1 :
                    queue.append([nextN+dn[i],nextM+dm[i],count+1])
                    maze[nextN+dn[i]][nextM+dm[i]] = 0
                




bfs(0,0)

print(minCount)





