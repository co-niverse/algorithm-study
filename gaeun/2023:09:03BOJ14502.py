import sys
from collections import deque
readline = sys.stdin.readline
N,M = map(int,readline().rstrip().split())
result = 0
lab = [[] for j in range(N) ]
viruses = []
# 위,오른쪽,아래,왼쪽
dn = [-1,0,+1,0]
dm = [0,+1,0,-1]



def spreadOut():
    safeArea = 0
    visited = [[False for i in range(M)] for j in range(N)]
    queue = deque(viruses)
    while queue :
        virus = queue.popleft()
        for next in range(4):
            nextN  = virus[0]+dn[next]
            nextM = virus[1]+dm[next]
            if 0<=nextN<N and 0<=nextM<M :
                if lab[nextN][nextM] == 0 and visited[nextN][nextM]==False:
                    visited[nextN][nextM] = True
                    queue.append((nextN,nextM))
    
    #영역확인
    for checkN in range(N):
        for checkM in range(M):
            if lab[checkN][checkM] == 0 and visited[checkN][checkM] == False :
                safeArea+=1
    
    return safeArea

                    
        
#백트래킹
def makeWall(start_n,count):
    global result
    if count == 3 :
        # 바이러스 전파 및 영영 구하기 함수 시작
        area = spreadOut()
        result = max(result,area)
        return
    else :
        for n in range(start_n,N):
            for m in range(M):
                if lab[n][m] == 0:
                    lab[n][m] = 1
                    if m + 1 < M:
                        makeWall( n, count + 1) 
                    else:
                        makeWall( n + 1, count + 1)
                    # makeWall(count+1)
                    lab[n][m] = 0

    
for n in range(N):
    line = list(map(int,readline().rstrip().split()))
    for ind in range(len(line)) :
        if line[ind] == 2 :
            viruses.append((n,ind))
    lab[n] = line
makeWall(0,0)
print(result)
