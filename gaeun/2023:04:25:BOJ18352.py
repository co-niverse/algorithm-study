from collections import deque
import sys
N,M,K,X = map(int,sys.stdin.readline().split())
graph = [[] for i in range(0,N)]
visited = [False for i in range(0,N)]
distanceList = [0 for _ in range(0,N)]
queue = deque([])
for i in range(0,M) :
    start , dest = map(int,sys.stdin.readline().split())
    if start == X :
        # visited[dest-1] = True
        queue.append((dest,1))
    graph[start-1].append(dest)

while(queue):
    city = queue.popleft()
    cityNum = city[0]
    cityDist = city[1]
    if visited[cityNum-1] == False:
        distanceList[cityNum - 1] = cityDist
        visited[cityNum-1] = True
           
        for num in graph[cityNum - 1] :
            if visited[num - 1] == True :
                continue 
            else :
                queue.append((num,cityDist+1))

flag = False
for i in range(0,len(distanceList)) :
    if distanceList[i] == K and (i+1)!=X:
        print(i+1)
        flag = True
if flag == False :
    print(-1)




