import sys
from collections import deque
readline = sys.stdin.readline
R, C = map(int, readline().split())
graph = [[] for _ in range(R)]
result = 1e9
jx = -1
jy = -1
fx = []
fy = []
#위,오른쪽,아래,왼쪽
dx = [0,+1,0,-1]
dy = [-1,0,+1,0]
for r in range(R):
    graph[r]=list(readline().rstrip())
    for ind in range(C) :
        if  graph[r][ind] == "F" :
            fx.append(ind)
            fy.append(r)
        elif  graph[r][ind] == "J" :
            jx = ind
            jy = r

# 큐 J,F위치 입력
queue = deque()
queue.append((jx,jy,0))
for fire in range(len(fx)) :
    queue.append((fx[fire],fy[fire]))

while(queue) :
    node = queue.popleft()
    # J 위치이동
    if graph[node[1]][node[0]] == "J" :
        for arrow in range(4) :
            nextX = node[0]+dx[arrow]
            nextY = node[1]+dy[arrow]
            if -1<nextX<C and -1<nextY<R :
                if graph[nextY][nextX] == "." :
                    graph[nextY][nextX] = "J"
                    queue.append((nextX,nextY,node[2]+1))
            else :
                result = min(result,node[2]+1)
    elif graph[node[1]][node[0]] == "F" :
        for arrow in range(4) :
            nextX = node[0]+dx[arrow]
            nextY = node[1]+dy[arrow]
            if -1<nextX<C and -1<nextY<R :
                if graph[nextY][nextX] != "#" and graph[nextY][nextX] != "F" :
                    graph[nextY][nextX] = "F"
                    queue.append((nextX,nextY))

if result== 1e9 :
    print("IMPOSSIBLE")
else : print(result)

            







