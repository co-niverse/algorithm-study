import sys
from collections import deque
sys.setrecursionlimit(10**7)
readline = sys.stdin.readline
N,M,K = map(int,readline().split())
Map = [[]for _ in range(N)]
for n in range(N) :
    Map[n] = list(map(int,readline().split()))

row = deque([4,1,3])
col = deque([2,1,5,6])

def getDice(direct):
    # 동쪽
    if direct == 1 :
        rowNode = row.pop()
        colNode = col.pop()
        col.append(rowNode)
        row.appendleft(colNode)
        col[1] = row[1]
    # 서쪽
    elif direct == 3 :
        rowNode = row.popleft()
        colNode = col.pop()
        row.append(colNode)
        col.append(rowNode)
        col[1] = row[1]
    # 남쪽
    elif direct == 2 :
        node = col.pop()
        col.appendleft(node)
        row[1] = col[1]
    # 북쪽
    else :
        node = col.popleft()
        col.append(node)
        row[1] = col[1]

def getScore(n, m,target) :
    count = 1
    queue = deque([[n,m]])
    while queue:
        info=queue.popleft()
        nextN = info[0]
        nextM = info[1]
        for i in range(4):
            if 0<= nextN+dn[i]<N and  0<= nextM+dm[i]<M :
                if visited[nextN+dn[i]][nextM+dm[i]] and Map[nextN+dn[i]][nextM+dm[i]] == target :
                    visited[nextN+dn[i]][nextM+dm[i]] = False
                    queue.append([nextN+dn[i],nextM+dm[i]])
                    count+=1
    return count


                




nextDirect = 1
sumScore = 0
# 북(0),동(1),남(2),서(3)
dn = [-1,0,+1,0]
dm = [0,+1,0,-1]
# 현재 위치 , N과 M
nn = 0
nm = 0
for k in range(K):
    maxScore = 0
    # 다음 방향으로 이동
    direct = nextDirect
    # 만약 이동하는 방향에 칸이 없으면 , 반대 방향
    if not (0<=nn+dn[direct]<N and 0<=nm +dm[direct]<M ):    
        if direct > 1 :
            direct -=2
            nextDirect =direct
        else :
            direct+=2
            nextDirect =direct
    #다음 위치
    nn = nn+dn[direct]
    nm = nm +dm[direct]

    # 방향으로 이동한 주사위
    getDice(direct)

    # 점수를 획득한다.
    visited = [[True for _ in range(M)] for _ in range(N)]
    visited[nn][nm] = False

    numCount= getScore(nn,nm,Map[nn][nm])
    score = numCount * Map[nn][nm]

    sumScore+=score

    #다음 방향 정하기
    #90도 시계 방향
    if col[3] > Map[nn][nm] :
        if direct != 3 :
            nextDirect +=1
        else :
            nextDirect = 0
    # 90도 반시계방향
    elif col[3] < Map[nn][nm] :
        if direct != 0 :
            nextDirect -=1
        else :
            nextDirect = 3
    #방향 변화없음
    else :
        nextDirect = direct
print(sumScore)