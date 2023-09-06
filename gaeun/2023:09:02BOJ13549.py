import sys
from collections import deque
readline = sys.stdin.readline
N,K = map(int,readline().rstrip().split())
visited = [ -1 for _ in range(200001)]

queue = deque()
queue.append(N)
visited[N] = 0
while queue:
    node = queue.popleft()
    # 순간이동
    if node*2 < len(visited) and visited[node*2] == -1 :
        visited[node*2] = visited[node]
        queue.append(node*2)
        if node*2 == K :
            break
    # 뒤로 걷기
    if node-1 >=0 and visited[node-1] == -1  :
        visited[node-1] = visited[node]+1
        queue.append(node-1)
        if node-1 == K :
            break
    # 앞으로 걷기
    if node+1 < len(visited) and visited[node+1] == -1  :
        visited[node+1] = visited[node]+1
        queue.append(node+1)
        if node+1 == K :
            break

print(visited[K])





# DP 풀이
import sys
readline = sys.stdin.readline
N,K = map(int,readline().rstrip().split())
start = min(N,K)
finish = max(N,K)
dp = [0 for _ in range(finish*2)]
for ind in range(start-1,-1,-1):
    if ind*2 <=start:
        dp[ind] = min(dp[ind+1]+1 , dp[ind*2])
    else : dp[ind] = dp[ind+1]+1

for ind in range(start+1,len(dp)) :
    if (ind % 2 == 0) and ((dp[ind-1]+1) >= dp[ind//2]) :
        dp[ind] = dp[ind//2]
        dp[ind-1] = min(dp[ind-1],dp[ind] + 1)
    else :
        dp[ind] = dp[ind-1]+1

print(dp[finish])
