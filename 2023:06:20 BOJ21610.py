


from collections import deque
import sys

n,m = map(int,sys.stdin.readline().split())
#
baskets = []
#이동 정보 [방향, 이동거리]
move = []
# 구름 위치 
newCloud = [[n-2,0],[n-2,1],[n-1,0],[n-1,1]]


# cloud = deque(cloudInfo)
dx = [0,-1,-1,0,1,1,1,0,-1]
dy = [0,0,-1,-1,-1,0,+1,1,1]

ax = [-1,-1,1,1]
ay = [-1,+1,-1,1]

def moveCloud(d,s,flag):
    global visited
    global newCloud
    cloud = newCloud
    
    #구름 이동
    for c in range(len(cloud)) :
        cloud[c][0] = (cloud[c][0] + (dy[d]*s)) % n
        cloud[c][1] = (cloud[c][1] + (dx[d]*s)) % n
        cx = cloud[c][0]
        cy = cloud[c][1]
        visited[cx][cy] = True
        #비를 뿌려준다.
        baskets[cx][cy] +=1
    
    #대각선 구름 찾기
    for c in cloud :
        x = c[0]
        y = c[1]
        count = 0
        for i in range(4):
            if -1 < x+ax[i] < n and -1 < y+ay[i] < n :
                if baskets[x+ax[i]][y+ay[i]] > 0 :
                    count+=1
        baskets[x][y] += count
    sumWater = 0
    newCloud=[]
    #다른 구름들을 찾는다
    for ix in range(n) :
        for iy in range(n) :
            if not visited[ix][iy]:
                if baskets[ix][iy] >= 2 :
                    newCloud.append([ix,iy])
                    baskets[ix][iy] -=2
            # else :
            #     cloud.remove([ix,iy])
            if flag :
                sumWater += baskets[ix][iy]
    if flag:
        print(sumWater)


for _ in range(n):
    line = list(map(int,sys.stdin.readline().split()))
    baskets.append(line)

flag = False
for i in range(m):
    visited = [[False for i in range(n) ] for i in range(n)]
    line = list(map(int,sys.stdin.readline().split()))
    if i == (m-1) :
        flag = True
    moveCloud(line[0],line[1],flag)
